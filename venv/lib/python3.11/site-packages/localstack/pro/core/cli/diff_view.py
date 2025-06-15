from typing import Dict,List
from localstack.cli import console
def print_diff(operations):
	F='MODIFICATION';B='operation_type';A=operations
	if not A:console.print('This load operation does not affect the runtime state.');return
	G=any(C.get(B)==F for A in A.values()for C in A)
	if G:console.print('[yellow]This load operation modifies one or more resources in the application runtime. The result will depend on the selected merge strategy. Use the --help option to read more about it.[/]\n')
	console.print('This load operation will modify the runtime state as follows:')
	for(H,C)in A.items():
		D=[A for A in C if A[B]=='ADDITION'];E=[A for A in C if A[B]==F]
		if not D and not E:return
		console.rule(H);console.print(f"[green]+[/] {len(D)} resources added.");console.print(f"[yellow]~[/] {len(E)} resources modified.")