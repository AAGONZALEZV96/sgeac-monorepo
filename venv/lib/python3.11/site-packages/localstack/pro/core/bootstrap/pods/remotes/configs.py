from dataclasses import asdict,dataclass,field
from typing import Dict
from urllib.parse import quote,urlparse
DEFAULT_REMOTE_SCHEME='platform'
@dataclass
class RemoteConfig:
	remote_url:str
	@property
	def scheme(self):
		A=DEFAULT_REMOTE_SCHEME
		if self.remote_url:A=urlparse(self.remote_url).scheme
		return A
@dataclass
class RemoteConfigParams:
	remote_name:str;remote_params:Dict[str,str]=field(default_factory=dict)
	def render_url(B,remote_url):
		A=remote_url
		if B.remote_params:C={A:quote(B or'')for(A,B)in B.remote_params.items()};A=A.format(**C)
		try:A.format()
		except Exception as D:raise Exception(f"Missing parameters for cloud pod remote URL template: {A}")from D
		return A
	def to_dict(A):return asdict(A)
	@classmethod
	def from_dict(A,params):return A(**params)