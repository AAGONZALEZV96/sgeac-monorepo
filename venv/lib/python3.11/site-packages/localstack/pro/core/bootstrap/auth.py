_E='/user/signin'
_D='verify_signature'
_C='username'
_B='token'
_A=None
import base64,getpass,json,logging,sys,time
from typing import Any,Dict,Optional,Tuple,Union
import jwt
from localstack.constants import API_ENDPOINT
from localstack.pro.core import config as config_ext
from localstack.pro.core.bootstrap.licensingv2 import ApiKeyCredentials,get_credentials_from_environment
from localstack.pro.core.bootstrap.licensingv2 import AuthToken as LSAuthToken
from localstack.pro.core.constants import VERSION
from localstack.utils.functions import call_safe
from localstack.utils.http import safe_requests
from localstack.utils.json import FileMappedDocument
from localstack.utils.strings import to_bytes,to_str
LOG=logging.getLogger(__name__)
AuthCache=Union[FileMappedDocument,Dict]
class AuthToken:
	def __init__(A,token,metadata=_A):A.token=token;A.metadata=metadata
	def extract_jwt(B):A=B.token.strip().split(' ')[-1];jwt.decode(A,options={_D:False});return A
	def to_dict(A):return{**(A.metadata or{}),_B:A.token}
class AuthClient:
	TOKEN_REFRESH_LEAD_TIME=30
	def get_auth_token(C,username,password,headers=_A):
		D={_C:username,'password':password};A=safe_requests.post(C._api_url(_E),json.dumps(D),headers=headers)
		if not A.ok:return
		try:B=json.loads(to_str(A.content or'{}'));return AuthToken(token=B[_B],metadata=B)
		except Exception:pass
	def get_token_expiry(B,token):
		try:A=jwt.decode(token.extract_jwt(),options={_D:False});return A.get('exp')
		except jwt.PyJWTError:return
	def refresh_token(A,token):
		B=token;D=A.get_token_expiry(B)
		if not D or time.time()<D-A.TOKEN_REFRESH_LEAD_TIME:return B
		F=B.to_dict();C=safe_requests.put(A._api_url(_E),json.dumps(F))
		if not C.ok:raise Exception(f"Unable to obtain auth token (code {C.status_code}) - please log in again.")
		try:G=json.loads(to_str(C.content or'{}'));E=G[_B];return AuthToken(token=E[_B],metadata=E)
		except Exception as H:raise Exception(f"Unable to obtain token ({H}) - please log in again.")
	def read_credentials(C,username=_A,password=_A):
		B=password;A=username
		if not A or not B:sys.stdout.write('Please provide your login credentials below\n');sys.stdout.flush()
		if not A:sys.stdout.write('Username: ');sys.stdout.flush();A=input()
		if not B:B=getpass.getpass()
		return A,B,{}
	def _api_url(A,path):return f"{API_ENDPOINT}{path}"
def get_auth_cache():return FileMappedDocument(config_ext.AUTH_CACHE_PATH,mode=384)
def login(username=_A,password=_A):
	B=password;A=username;C=AuthClient();A,B,F=C.read_credentials(A,B);print('Verifying credentials ... (this may take a few moments)');D=C.get_auth_token(A,B,F)
	if not D:raise Exception('Unable to verify login credentials - please try again')
	E=get_auth_cache();E.update({_C:A,_B:D.token});call_safe(E.save,exception_message='error saving authentication information')
def logout():A=get_auth_cache();A.pop(_C,_A);A.pop(_B,_A);A.save()
def get_bearer_token_from_cache(auth_cache=_A):
	B=auth_cache;B=B or get_auth_cache();C=B.get(_B);A=C
	if isinstance(A,dict):
		G=AuthClient();D=AuthToken(C.get(_B),metadata=C);D=G.refresh_token(D);E=D.to_dict()
		if C!=E:C.update(E);B[_B]=C;B.save()
		A=D.token
	if A:
		H=B.get('provider')or'internal';F=f"{H} "
		if not A.startswith(F)and' 'not in A:A=f"{F}{A}"
		return{'authorization':A}
def get_platform_auth_headers(auth_cache=_A):
	A=get_credentials_from_environment()
	if isinstance(A,LSAuthToken):B=to_str(base64.b64encode(to_bytes(f":{A.encoded()}")));return{'Authorization':f"Basic {B}"}
	if isinstance(A,ApiKeyCredentials):return{'ls-api-key':A.encoded(),'ls-version':VERSION}
	if not(C:=get_bearer_token_from_cache(auth_cache or get_auth_cache())):raise Exception("Auth token not configured! Please run 'localstack auth set-token <AUTH_TOKEN>', or set the environment variable LOCALSTACK_AUTH_TOKEN to a valid auth token.")
	return C