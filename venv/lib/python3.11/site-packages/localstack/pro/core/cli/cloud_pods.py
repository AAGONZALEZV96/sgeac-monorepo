_P='Secret for the Cloud Pod encryption. Encryption is an Enterprise only feature.'
_O='secret'
_N='--secret'
_M='services'
_L='version'
_K='delete'
_J='format_'
_I='--format'
_H='-f'
_G='table'
_F='remote'
_E='name'
_D='json'
_C=True
_B=False
_A=None
import json,logging
from typing import Dict,List,Optional,Tuple
from urllib.parse import urlparse
import click
from localstack.cli import console
from localstack.cli.exceptions import CLIError
from localstack.pro.core.bootstrap.auth import get_auth_cache
from localstack.pro.core.bootstrap.pods.api_types import DEFAULT_STRATEGY,MergeStrategy
from localstack.pro.core.bootstrap.pods.remotes.api import CloudPodsRemotesClient
from localstack.pro.core.bootstrap.pods.remotes.configs import RemoteConfigParams
from localstack.pro.core.bootstrap.pods_client import CloudPodRemoteAttributes,CloudPodsClient,list_public_pods
from localstack.pro.core.cli.cli import RequiresLicenseGroup,_assert_host_reachable
from localstack.pro.core.cli.click_utils import print_table
from localstack.pro.core.cli.diff_view import print_diff
from localstack.utils.analytics.cli import publish_invocation
from localstack.utils.collections import is_comma_delimited_list
from localstack.utils.time import timestamp
LOG=logging.getLogger(__name__)
DATE_FORMAT='%Y-%m-%d %H:%M:%S'
@click.group(name='pod',help='Manage the state of your instance via Cloud Pods.',context_settings=dict(max_content_width=120),cls=RequiresLicenseGroup if not get_auth_cache().get('token')else _A)
def pod():0
@pod.group(name=_F,help='Manage cloud pod remotes')
def remote():0
@remote.command(name='add',short_help='Add a remote',help='\n    Add a new remote for Cloud Pods.\n\n    A remote is the place where your Cloud Pods are stored. By default, Cloud Pods are store in the LocalStack platform.\n    ')
@click.argument(_E,required=_C)
@click.argument('url',required=_C)
def cmd_add_remote(name,url):
	A=name;_assert_host_reachable();C=CloudPodsRemotesClient();D=urlparse(url).scheme
	try:C.create_remote(name=A,protocols=[D],remote_url=url)
	except Exception as B:raise CLIError(f"Unable to determine URL for remote '{A}': {B}")from B
	console.print(f"Successfully added remote '{A}'")
@remote.command(name=_K,short_help='Delete a remote',help='Remove a remote for Cloud Pods.')
@click.argument(_E,required=_C)
def cmd_delete_remote(name):
	A=name;_assert_host_reachable();C=CloudPodsRemotesClient()
	try:C.delete_remote(name=A)
	except Exception as B:raise CLIError(f"Unable to delete remote '{A}': {B}")from B
	console.print(f"Successfully deleted remote '{A}'")
@remote.command(name='list',short_help='Lists the available remotes')
@click.option(_H,_I,_J,type=click.Choice([_G,_D]),default=_G,help='The formatting style for the remotes command output.')
def cmd_remotes(format_):
	_assert_host_reachable();B=CloudPodsRemotesClient();A=B.get_remotes()
	if not A:console.print('[yellow]No remotes[/yellow]');return
	if format_==_D:console.print_json(json.dumps(A));return
	print_table(column_headers=['Remote Name','URL'],columns=[[A[_E]for A in A],[A['url']for A in A]])
@pod.command(name=_K,short_help='Delete a Cloud Pod',help='\n    Delete a Cloud Pod registered on a remote (by default, the LocalStack platform).\n\n    This command will remove all the versions of a Cloud Pod, and the operation is not reversible.\n    ')
@click.argument(_E)
@click.argument(_F,required=_B)
@publish_invocation
def cmd_pod_delete(name,remote=_A):
	B=remote;A=name;D=CloudPodsClient()
	try:E=RemoteConfigParams(remote_name=B)if B else _A;D.delete(pod_name=A,remote=E);console.print(f"Successfully deleted Cloud Pod '{A}'")
	except Exception as C:raise CLIError(f"Unable to delete Cloud Pod '{A}': {C}")from C
@pod.command(name='save',short_help='Create a new Cloud Pod',help="\n    Save the current state of the LocalStack container in a Cloud Pod.\n\n    A Cloud Pod can be registered and saved with different storage options, called remotes. By default, Cloud Pods\n    are hosted in the LocalStack platform. However, users can decide to store their Cloud Pods in other remotes, such as\n    AWS S3 buckets or ORAS registries.\n\n    An optional message can be attached to any Cloud Pod.\n    Furthermore, one could decide to export only a subset of services with the optional --services option.\n\n    \x08\n    To use the LocalStack platform for storage, the desired Cloud Pod's name will suffice, e.g.:\n\n    \x08\n    localstack pod save <pod_name>\n\n    Please be aware that each following save invocation with the same name will result in a new version being created.\n\n    \x08\n    To save a local copy of your state, you can use the 'localstack state export' command.\n    ")
@click.argument(_E)
@click.argument(_F,required=_B)
@click.option('-m','--message',help="Add a comment describing this Cloud Pod's version")
@click.option('-s','--services',help='Comma-delimited list of services to push in the Cloud Pod (all by default)')
@click.option('--visibility',type=click.Choice(['public','private']),help='Set the visibility of the Cloud Pod [`public` or `private`]. Does not create a new version')
@click.option('-s',_N,_O,help=_P)
@click.option(_H,_I,_J,type=click.Choice([_D]),help='The formatting style for the save command output.')
@publish_invocation
def cmd_pod_save(name=_A,remote=_A,services=_A,message=_A,visibility=_A,secret=_A,format_=_A):
	F=visibility;E=remote;B=services;A=name;G=CloudPodsClient(_C);_assert_host_reachable()
	if B and not is_comma_delimited_list(B):raise CLIError('Input the services as a comma-delimited list')
	H=RemoteConfigParams(remote_name=E)if E else _A
	if F:
		try:G.set_remote_attributes(pod_name=A,attributes=CloudPodRemoteAttributes(is_public=_C),remote=H)
		except Exception as C:raise CLIError(str(C))
		console.print(f"Cloud Pod {A} made {F}")
	I=[A.strip()for A in B.split(',')]if B else _A
	try:D=G.save(pod_name=A,attributes=CloudPodRemoteAttributes(is_public=_B,description=message,services=I),remote=H,secret=secret)
	except Exception as C:raise CLIError(f"Failed to create Cloud Pod {A} ❌ - {C}")from C
	if format_==_D:console.print_json(json.dumps(D))
	else:console.print(f"Cloud Pod `{A}` successfully created ✅\nVersion: {D[_L]}\nRemote: {D[_F]}\nServices: {','.join(D[_M])or'none'}")
@pod.command(name='load',help="\n    Load the state of a Cloud Pod into the application runtime.\n    Users can import Cloud Pods from different remotes, with the LocalStack platform being the default one.\n    Users can also load a specific version by appending a version number to the pod name after a colon\n    (e.g., `localstack pod load my-pod:3`).\n    If not specified, the latest version will be loaded. Use the `localstack pod versions` to list all the available\n    versions.\n\n    Loading the state of a Cloud Pod into LocalStack might cause some conflicts with the current state of the container.\n    LocalStack will attempt a best-effort merging strategy between the current state and the one from the\n    Cloud Pod.\n    For a service X present in both the current state and the Cloud Pod, we will attempt to merge states\n    across different accounts and regions. If the service X has a state for the same account and region both in the\n    running container and the Cloud Pod, the latter will be used. If a service Y is present in the running container\n    but not in the Cloud Pod, it will be left untouched.\n    This is the default merge strategy which is activated by either the `--strategy account-region-merge` option or\n    by omitting the `--strategy` option at all.\n\n    In addition to the default one, LocalStack provides two more strategies:\n\n    \x08\n    - overwrite, in which the state of LocalStack is completely reset before loading the state from the Cloud Pod.\n    This strategy is activated with the `--strategy overwrite` option .\n    - service-merge: in which LocalStack merges the state of a service under the same account and region when\n    there is no resource overlap. In such a case, the loaded resources are preferred.\n    This option is activated with the `--strategy service-merge` option.\n\n    To load a local copy of a LocalStack state, you can use the 'localstack state import' command.\n    ")
@click.argument(_E)
@click.argument(_F,required=_B)
@click.option('-s',_N,_O,help=_P)
@click.option('--strategy',type=click.Choice([A.value for A in MergeStrategy]),default=DEFAULT_STRATEGY,help='The merge strategy to adopt when loading the Cloud Pod.')
@click.option('--yes','-y',help='Automatic yes to prompts. Assume a positive answer to all prompts and run non-interactively.',is_flag=_C,default=_B)
@click.option('--dry-run',help='Checks the resources added or modified in the application runtime by loading a Cloud Pod.',is_flag=_C,default=_B)
@publish_invocation
def cmd_pod_load(name=_A,remote=_A,strategy=_A,yes=_B,secret=_A,dry_run=_B):
	C=remote;B=name;D=CloudPodsClient(_C);_assert_host_reachable();E,F=get_pod_name_and_version(B)
	if dry_run:
		try:G=D.diff(pod_name=E,remote=C,version=F);print_diff(G);return
		except Exception as A:raise CLIError(f"Failed to dry-run the load operation: {A}")from A
	try:H=RemoteConfigParams(remote_name=C)if C else _A;D.load(pod_name=E,remote=H,version=F,merge_strategy=strategy,ignore_version_mismatches=yes,secret=secret)
	except Exception as A:raise CLIError(f"Failed to load Cloud Pod {B}: {A}")from A
	print(f"Cloud Pod {B} successfully loaded")
def get_pod_name_and_version(pod_name):
	A=pod_name
	if':'not in A:return A,_A
	C,D,B=A.rpartition(':')
	if B.isdigit():return C,int(B)
	return A,_A
@pod.command(name='list',short_help='List all available Cloud Pods',help='\n    List all the Cloud Pods available for a single user, or for an entire organization, if the user is part of one.\n\n    With the --public flag, it lists the all the available public Cloud Pods. A public Cloud Pod is available across\n    the boundary of a user and/or organization. In other words, any public Cloud Pod can be injected by any other\n    user holding a LocalStack Pro (or above) license.\n    ')
@click.argument(_F,required=_B)
@click.option('--public','-p',help='List all the available public Cloud Pods',is_flag=_C,default=_B)
@click.option('--mine','-m',help='List only the Cloud Pods created by the current user',is_flag=_C,default=_B)
@click.option(_H,_I,_J,type=click.Choice([_G,_D]),default=_G,help='The formatting style for the list pods command output.')
@publish_invocation
def cmd_pod_list_pods(remote=_A,public=_B,mine=_B,format_=_A):
	C='last_change';B=remote;D=CloudPodsClient();_assert_host_reachable()
	if public:E=list_public_pods();print_table(column_headers=['Cloud Pod'],columns=[E]);return
	F=RemoteConfigParams(remote_name=B)if B else _A;A=D.list(remote=F,creator='me'if mine else _A)
	if not A:console.print('[yellow]No pods available[/yellow]')
	if format_==_D:console.print_json(json.dumps(A));return
	print_table(column_headers=['Name','Max Version','Last Change'],columns=[[A['pod_name']for A in A],[str(A['max_version'])for A in A],[timestamp(A[C],format=DATE_FORMAT)if A.get(C)else'n/a'for A in A]])
@pod.command(name='versions',help='\n    List all available versions for a Cloud Pod\n\n    This command lists the versions available for a Cloud Pod.\n    Each invocation of the save command is going to create a new version for a named Cloud Pod, if a Pod with\n    such name already does exist in the LocalStack platform.\n    ')
@click.argument(_E)
@click.option(_H,_I,_J,type=click.Choice([_G,_D]),default=_G,help='The formatting style for the version command output.')
@publish_invocation
def cmd_pod_versions(name,format_):
	C=CloudPodsClient();_assert_host_reachable()
	try:A=C.get_versions(pod_name=name);A=[A for A in A if not A.get('deleted')]
	except Exception as B:raise CLIError(str(B))from B
	if not A:console.print('[yellow]No versions available[/yellow]')
	if format_==_D:console.print_json(json.dumps(A));return
	print_table(column_headers=['Version','Creation Date','LocalStack Version','Services','Description'],columns=[[str(A[_L])for A in A],[timestamp(A['created_at'],format=DATE_FORMAT)for A in A],[A['localstack_version']for A in A],[','.join(A[_M]or[])for A in A],[A['description']for A in A]])