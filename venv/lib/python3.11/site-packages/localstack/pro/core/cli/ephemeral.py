_C='response'
_B='--name'
_A=True
import json
from typing import Optional,Tuple
import click,requests
from localstack import constants as localstack_constants
from localstack.cli import console
from localstack.cli.exceptions import CLIError
from localstack.pro.core.bootstrap import auth
from localstack.pro.core.cli.cli import RequiresLicenseGroup
from localstack.utils.analytics.cli import publish_invocation
API_ENDPOINT=localstack_constants.API_ENDPOINT
API_CREATION_ENDPOINT=f"{API_ENDPOINT}/compute/instances"
API_DELETION_ENDPOINT=f"{API_ENDPOINT}/compute/instances/{{name}}"
API_LIST_ENDPOINT=f"{API_ENDPOINT}/compute/instances"
API_LOGS_ENDPOINT=f"{API_ENDPOINT}/compute/instances/{{name}}/logs"
@click.group(name='ephemeral',short_help='(Preview) Manage ephemeral LocalStack instances',help='\n    (Preview) Manage ephemeral LocalStack instances in the cloud.\n\n    This command group allows you to create, list, and delete ephemeral LocalStack instances.\n    Ephemeral instances are temporary cloud instances that can be used for testing and development.\n    ',cls=RequiresLicenseGroup)
def ephemeral():0
@ephemeral.command(name='create',short_help='Create a new ephemeral instance',help='\n    Create a new ephemeral LocalStack instance in the cloud.\n\n    Specify an instance name and optional parameters like lifetime and environment variables.\n    The instance will be created with the specified configuration and its connection details will be returned.\n\n    \x08\n    Examples:\n        localstack ephemeral create --name my-test-instance\n        localstack ephemeral create --name my-instance --lifetime 60\n        localstack ephemeral create --name my-instance --env DEBUG=1\n    ')
@click.option(_B,required=_A,help='Name of the ephemeral instance')
@click.option('--lifetime',required=False,type=int,help='Lifetime of the instance in minutes')
@click.option('--env','-e',help='Additional environment variables that are passed to the LocalStack instance',multiple=_A,required=False)
@publish_invocation
def create(name,lifetime,env):
	try:
		C={}
		if env:
			for B in env:
				if'='not in B:raise CLIError(f"Invalid environment variable format: {B}")
				E,F=B.split('=',1);C[E.strip()]=F.strip()
		G=auth.get_platform_auth_headers();H={'instance_name':name,'lifetime':lifetime or 60,'env_vars':C};D=requests.post(API_CREATION_ENDPOINT,headers=G,json=H);D.raise_for_status();console.print_json(json.dumps(D.json()))
	except requests.exceptions.RequestException as A:
		if hasattr(A,_C)and A.response is not None:
			try:I=A.response.json();raise CLIError(f"Failed to create ephemeral instance: {I}")
			except json.JSONDecodeError:raise CLIError(f"Failed to create ephemeral instance: {str(A)}")
		raise CLIError(f"Failed to create ephemeral instance: {str(A)}")
@ephemeral.command(name='list',short_help='List all ephemeral instances',help='\n    List all available ephemeral LocalStack instances.\n\n    This command shows all ephemeral instances associated with your account,\n    including their names, status, and other relevant details.\n\n    \x08\n    Examples:\n        localstack ephemeral list\n    ')
@publish_invocation
def list_instances():
	try:B=auth.get_platform_auth_headers();A=requests.get(API_LIST_ENDPOINT,headers=B);A.raise_for_status();C=A.json();console.print_json(json.dumps(C,indent=2))
	except requests.exceptions.RequestException as D:raise CLIError(f"Failed to list ephemeral instances: {str(D)}")
@ephemeral.command(name='delete',short_help='Delete an ephemeral instance',help='\n    Delete a specific ephemeral LocalStack instance.\n\n    Specify the name of the instance you want to delete.\n    Once deleted, the instance cannot be recovered.\n\n    \x08\n    Example:\n        localstack ephemeral delete --name my-test-instance\n    ')
@click.option(_B,required=_A,help='Name of the ephemeral instance to delete')
@publish_invocation
def delete(name):
	try:A=API_DELETION_ENDPOINT.format(name=name);B=auth.get_platform_auth_headers();C=requests.delete(A,headers=B);C.raise_for_status();console.print(f"Successfully deleted instance: {name} ✅")
	except requests.exceptions.RequestException as D:raise CLIError(f"Failed to delete ephemeral instance: {str(D)}")
@ephemeral.command(name='logs',short_help='Fetch logs from an ephemeral instance',help='\n    Fetch logs from a specific ephemeral LocalStack instance.\n\n    Retrieve the logs of a running ephemeral instance by specifying its name.\n    The logs are returned in chronological order.\n\n    \x08\n    Example:\n        localstack ephemeral logs --name my-test-instance\n    ')
@click.option(_B,required=_A,help='Name of the ephemeral instance to fetch logs from')
@publish_invocation
def logs(name):
	try:
		D=API_LOGS_ENDPOINT.format(name=name);E=auth.get_platform_auth_headers();B=requests.get(D,headers=E);B.raise_for_status();C=B.json()
		if not C:console.print('No logs available for this instance.');return
		for F in C:console.print(f"{F.get('content','')}")
	except requests.exceptions.RequestException as A:
		if hasattr(A,_C)and A.response is not None:
			try:G=A.response.json();raise CLIError(f"Failed to fetch logs: {G}")
			except json.JSONDecodeError:raise CLIError(f"Failed to fetch logs: {str(A)}")
		raise CLIError(f"Failed to fetch logs: {str(A)}")