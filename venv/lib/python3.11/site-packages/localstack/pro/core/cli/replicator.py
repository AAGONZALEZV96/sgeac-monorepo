_I='--delay'
_H='region'
_G='replicator'
_F='endpoint_url'
_E='SINGLE_RESOURCE'
_D='region_name'
_C='aws_secret_access_key'
_B='aws_access_key_id'
_A=None
import json,os,subprocess as sp,sys,time
from configparser import ConfigParser
from pathlib import Path
from typing import Mapping,Optional,TypedDict
import click,requests
from localstack import config
from localstack.cli import console
from localstack.cli.exceptions import CLIError
from.cli import RequiresPlatformLicenseGroup,_assert_host_reachable
AWS_CONFIG_ENV_VARS={_B:'{}_ACCESS_KEY_ID',_C:'{}_SECRET_ACCESS_KEY','aws_session_token':'{}_SESSION_TOKEN',_D:'{}_DEFAULT_REGION',_F:'{}_ENDPOINT_URL','profile_name':'{}_PROFILE'}
PREVIEW_BANNER="\n*** Preview Feature ***\n\nThis feature is currently in preview mode in our Teams offering and it's availability may change in future releases.\n"
REPLICATOR_HELP=PREVIEW_BANNER+'\n\nThe replicator command group allows you to replicate AWS resources into LocalStack.\n'
class ProfileLoadError(RuntimeError):
	def __init__(A,profile_name):super().__init__(f"Could not find profile '{profile_name}'")
class ReplicatorCliGroup(RequiresPlatformLicenseGroup):
	name=_G;tier='Ultimate'
	def invoke(A,ctx):print(PREVIEW_BANNER,file=sys.stderr);super().invoke(ctx)
class AWSConfig(TypedDict,total=False):aws_access_key_id:str;aws_secret_access_key:str;aws_session_token:Optional[str];region_name:str;endpoint_url:Optional[str];profile_name:str
def get_aws_env_config(prefix):A={A:os.getenv(B.format(prefix))for(A,B)in AWS_CONFIG_ENV_VARS.items()};return AWSConfig(**{B:A for(B,A)in A.items()if A})
def get_config_from_profile(profile_name,profile_dir=_A):
	B=profile_name;A=profile_dir;A=A or Path.home()/'.aws'
	def C(path,profile_prefix=''):
		A=ConfigParser();A.read(path)
		try:return A[f"{profile_prefix}{B}"]
		except KeyError:raise ProfileLoadError(B)
	E=C(A/'config',profile_prefix='profile ');D=C(A/'credentials');return AWSConfig(aws_access_key_id=D[_B],aws_secret_access_key=D[_C],region_name=E[_H],profile_name=B)
def get_awscli_config():
	I='utf8';E='configure';D='aws'
	try:A=[D,E,'export-credentials'];B=sp.check_output(A,stderr=sp.PIPE);C=json.loads(B.decode(I))
	except sp.CalledProcessError as F:
		if b'AWS CLI version 2'in F.stderr:print('Warning: awscli v1 installed. Please use v2 for auto detection of credentials',file=sys.stderr);return
	try:A=[D,E,'get',_F];G=sp.check_output(A,stderr=sp.PIPE).decode(I)
	except sp.CalledProcessError:G=os.getenv('AWS_ENDPOINT_URL')
	try:
		A=[D,E,'list'];B=sp.check_output(A,stderr=sp.PIPE)
		for H in B.decode().splitlines():
			if _H not in H:continue
			J=H.split()
			try:K=J[1];return AWSConfig(aws_access_key_id=C['AccessKeyId'],aws_secret_access_key=C['SecretAccessKey'],aws_session_token=C.get('SessionToken'),region_name=K,endpoint_url=G)
			except IndexError:return
	except(sp.CalledProcessError,FileNotFoundError)as F:return
def get_source_config(profile_dir=_A):
	B=get_awscli_config()
	if B:print('Configured credentials from the AWS CLI',file=sys.stderr);return B
	A=get_aws_env_config('AWS')
	if not A.get(_D):raise CLIError("'AWS_DEFAULT_REGION' must bet set in environment.")
	if not A.get(_B):raise CLIError("'AWS_ACCESS_KEY_ID' must bet set in environment.")
	if not A.get(_C):raise CLIError("'AWS_SECRET_ACCESS_KEY' must bet set in environment.")
	return A
def get_target_config(access_key='',region_name=''):
	C=region_name;B=access_key;A=get_aws_env_config('TARGET')
	if B:A[_B]=B
	if C:A[_D]=C
	return A
def get_replicator_url():_assert_host_reachable();return f"{config.external_service_url()}/_localstack/replicator"
@click.group(name=_G,short_help='(Preview) Start a replication job or check its status',help=REPLICATOR_HELP,cls=ReplicatorCliGroup)
def replicator():0
def validate_start_command(replication_type,resource_arn=_A,resource_type=_A,resource_identifier=_A):
	C='You must specify either --resource-arn or --resource_type';B=resource_type;A=resource_arn
	if replication_type==_E:
		if not(A or B):raise CLIError(C)
		if A and B:raise CLIError(C)
		if B and not resource_identifier:raise CLIError('You must specify --resource-id when using --resource-type')
		if A and not A.startswith('arn:aws:'):raise CLIError('--resource-arn must start with arn:aws:')
@replicator.command(name='start',short_help='Replicate an AWS resource',help='\nStarts a job to replicate an AWS resource into localstack.\nYou must have credentials with sufficient read access to the resource trying to replicate.\nAt the moment only environment variables are recognized.\n`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_DEFAULT_REGION` must be set. `AWS_ENDPOINT_URL` and `AWS_SESSION_TOKEN` are optional.\n')
@click.option('--replication-type',type=click.Choice(['MOCK',_E]),default=_E,show_default=True,help='Type of replication job: MOCK, SINGLE_RESOURCE')
@click.option('--resource-arn',help='ARN of the resource to recreate. Optional for SINGLE_RESOURCE replication')
@click.option('--resource-type',help='CloudControl type of the resource to recreate. Optional for SINGLE_RESOURCE replication')
@click.option('--resource-identifier',help='CloudControl identifier of the resource to recreate. Mandatory if --resource-type is used')
@click.option('--target-account-id',help='Localstack account ID where the resources will be replicated. Defaults to 000000000000. See <docs> to enable same account replication')
@click.option('--target-region-name',help='Localstack region where the resources will be replicated. Only provide if different than source AWS account.')
@click.option(_I,help='Delay for the MOCK replication work')
def start(replication_type,resource_arn=_A,resource_type=_A,resource_identifier=_A,delay=_A,target_account_id=_A,target_region_name=_A):
	G=delay;F=resource_identifier;E=resource_type;D=resource_arn;C=replication_type;validate_start_command(C,D,E,F);H=get_source_config();I=get_target_config(access_key=target_account_id,region_name=target_region_name);A={}
	if D:A['resource_arn']=D
	if E:A['resource_type']=E
	if F:A['resource_identifier']=F
	if C=='MOCK':A['delay']=float(G)if G else 1
	J=f"{get_replicator_url()}/jobs";K={'replication_type':C,'replication_job_config':A,'source_aws_config':H,'target_aws_config':I};B=requests.post(J,json=K)
	if B.status_code==200:console.print_json(json=B.text)
	else:raise CLIError(f"Failed to create replication job: {B.status_code}, {B.text}")
@replicator.command(name='status',short_help='Check replication status',help='\nCheck the status of a replication job using its Job ID.\nUse the --follow flag to continuously check the status until the job is completed.\n')
@click.argument('job_id')
@click.option('--follow',is_flag=True,help='Follow the status until completed')
@click.option(_I,help='Delay between calls',default=5,type=int)
def status(job_id,follow,delay):
	D=f"{get_replicator_url()}/jobs/{job_id}"
	while True:
		A=requests.get(D)
		if A.status_code==200:
			B=A.json();console.print_json(data=B);C=B.get('state')
			if C=='ERROR':raise CLIError(B.get('error_message'))
			elif C=='SUCCEEDED':return
		else:raise CLIError(f"Failed to replicate resource: {A.status_code}, {A.text}")
		if not follow:return
		time.sleep(float(delay))
@replicator.command(name='resources',short_help='List supported resources')
def resources():
	B=f"{get_replicator_url()}/resources";A=requests.get(B)
	if A.status_code!=200:raise CLIError(f"Failed to get list of resources: {A.status_code}, {A.text}")
	console.print_json(json=A.text)