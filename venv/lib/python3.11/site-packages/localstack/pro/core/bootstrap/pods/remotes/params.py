import logging,os
from typing import Callable,Dict,Optional
from urllib.parse import urlparse
from localstack.pro.core.bootstrap.pods.remotes.configs import DEFAULT_REMOTE_SCHEME
LOG=logging.getLogger(__name__)
PARAM_ACCESS_KEY_ID='access_key_id'
PARAM_SECRET_ACCESS_KEY='secret_access_key'
PARAM_SESSION_TOKEN='session_token'
def _get_aws_credentials_from_boto_session():
	try:import boto3;B=boto3.session.Session();A=B.get_credentials();return{PARAM_ACCESS_KEY_ID:A.access_key,PARAM_SECRET_ACCESS_KEY:A.secret_key,PARAM_SESSION_TOKEN:A.token}
	except Exception as C:LOG.debug('Unable to extract remote parameters: %s',C)
def get_s3_remote_params():
	if(A:=_get_aws_credentials_from_boto_session()):return A
	B=os.getenv('AWS_ACCESS_KEY_ID');C=os.getenv('AWS_SECRET_ACCESS_KEY');D=os.getenv('AWS_SESSION_TOKEN')
	if not B or not C:raise Exception('Please export AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in the environment')
	A={PARAM_ACCESS_KEY_ID:B,PARAM_SECRET_ACCESS_KEY:C}
	if D:A[PARAM_SESSION_TOKEN]=D
	return A
def get_oras_remote_params():
	D='oras_password';C='oras_username';A=os.getenv('ORAS_USERNAME')or os.getenv(C);B=os.getenv('ORAS_PASSWORD')or os.getenv(D)
	if not A or not B:raise Exception('Please specify ORAS_USERNAME and ORAS_PASSWORD in the environment')
	return{C:A,D:B}
def get_platform_remote_params():
	A=os.getenv('LOCALSTACK_AUTH_TOKEN');B=os.getenv('LOCALSTACK_BEARER_TOKEN');C=os.getenv('LOCALSTACK_API_KEY')
	if not A and not C and not B:raise Exception('Please specify LOCALSTACK_AUTH_TOKEN in the environment')
	return{'api_key':C,'auth_token':A,'bearer_token':B}
remotes_protocols={'s3':get_s3_remote_params,'oras':get_oras_remote_params,'platform':get_platform_remote_params}
def get_remote_params_callable(url):A=urlparse(url).scheme or DEFAULT_REMOTE_SCHEME;return remotes_protocols.get(A,None)