_A=None
import functools,json,logging,os
from abc import ABC
from typing import Any,Dict
from localstack.utils.objects import SubtypesInstanceManager
ESC=27
INDENTATION=2
class TreeRenderer(SubtypesInstanceManager,ABC):
	def render_tree(A,tree,tree_name):raise NotImplementedError
class TreeRendererRich(TreeRenderer):
	@staticmethod
	def impl_name():return'rich'
	def render_tree(C,tree,tree_name):
		from rich import print;from rich.tree import Tree as A
		def F(obj,parent):
			C=parent;B=obj
			if isinstance(B,list):
				for(H,I)in enumerate(B):E=A(str(H));C.add(F(I,E))
				return C
			elif isinstance(B,dict):
				for(G,D)in B.items():
					if isinstance(D,(dict,list)):
						if not D:return A(f"{G} = {D}")
						E=A(str(G));F(D,E);C.add(E)
					else:C.add(A(f"{G} = {D}"))
				return C
			return A(str(B))
		B=A(tree_name);F(tree,B);print(B)
class Tree:
	def __init__(A,name,obj):A.name=name;A.object=obj;A.expanded=True
	def render(A,depth,width):return A.pad(f"{' '*INDENTATION*depth}{A.icon()} {A.name}",width)
	@functools.lru_cache(maxsize=_A)
	def children(self):
		A=self
		def B(key,value):
			B=value;A=key
			if isinstance(B,(list,dict)):return A
			return f"{B}"if isinstance(A,int)else f"{A} = {B}"
		if isinstance(A.object,dict):return[Tree(B(C,A),A)for(C,A)in A.object.items()]
		if isinstance(A.object,list):return[Tree(B(C,A),A)for(C,A)in enumerate(A.object)]
		return[]
	def icon(A):
		if A.children()and not A.expanded:return'+'
		return'-'
	def expand(A):A.expanded=True
	def collapse(A):A.expanded=False
	def toggle(A):A.expanded=not A.expanded
	def traverse(A):
		yield(A,0)
		if not A.expanded:return
		for B in A.children():
			for(C,D)in B.traverse():yield(C,D+1)
	def pad(A,data,width):return data+' '*(width-len(data))
class TreeRendererCurses(TreeRenderer):
	LOG=_A
	@staticmethod
	def impl_name():return'curses'
	def render_tree(B,dict_obj,tree_name):
		from curses import wrapper as C;A=os.dup(0),os.dup(1)
		def D(_tree):
			def A(win):return B.curses_main(win,_tree)
			return A
		try:A=B.open_tty();E=Tree(tree_name,dict_obj);C(D(E))
		finally:os.close(0);os.close(1);os.dup(A[0]);os.dup(A[1])
	@staticmethod
	def curses_main(win,tree):
		C=win;import curses as A;C.clear();C.refresh();A.nl();A.noecho();C.timeout(0);C.nodelay(False);tree.expand();B=3;F=_A;A.use_default_colors()
		while True:
			C.clear();A.init_pair(1,A.COLOR_WHITE,A.COLOR_BLUE);E=0;G=max(0,B-A.LINES+3)
			for(H,I)in tree.traverse():
				if E==B:
					C.attrset(A.color_pair(1)|A.A_BOLD)
					if F:getattr(H,F)();F=_A
				else:C.attrset(A.color_pair(0))
				if 0<=E-G<A.LINES-1:C.addstr(E-G,0,H.render(I,A.COLS))
				E+=1
			C.refresh();D=C.getch()
			if D==A.KEY_UP:B-=1
			elif D==A.KEY_DOWN:B+=1
			elif D==A.KEY_PPAGE:
				B-=A.LINES
				if B<0:B=0
			elif D==A.KEY_NPAGE:
				B+=A.LINES
				if B>=E:B=E-1
			elif D==A.KEY_RIGHT:F='expand'
			elif D==A.KEY_LEFT:F='collapse'
			elif D==ord(' '):F='toggle'
			elif D==ESC:return
			B%=E
	@staticmethod
	def open_tty():A='/dev/tty';B=os.dup(0);C=os.dup(1);os.close(0);os.close(1);os.open(A,os.O_RDONLY);os.open(A,os.O_RDWR);return B,C
	@classmethod
	def log(A,*D,**E):
		if A.LOG:B=logging.getLogger(__file__);C=logging.FileHandler('cloud_pods_viewer.log');F=logging.Formatter('%(asctime)s %(levelname)s %(message)s');C.setFormatter(F);B.addHandler(C);B.setLevel(logging.INFO)
		A.LOG.info(*D,**E)
class TreeRendererJSON(TreeRenderer):
	@staticmethod
	def impl_name():return'json'
	def render_tree(A,dict_obj,tree_name):print(json.dumps(dict_obj,indent=4))