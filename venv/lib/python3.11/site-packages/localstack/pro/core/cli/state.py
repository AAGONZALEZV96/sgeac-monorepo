_G='curses'
_F='format_'
_E='--format'
_D='--services'
_C='json'
_B=True
_A=None
import json
from typing import Optional
import click
from localstack.cli import console
from localstack.cli.exceptions import CLIError
from localstack.pro.core.bootstrap.pods_client import CloudPodsClient,StateService
from localstack.pro.core.cli.cli import RequiresLicenseGroup,_assert_host_reachable
from localstack.pro.core.cli.tree_view import TreeRenderer
from localstack.utils.analytics.cli import publish_invocation
from localstack.utils.collections import is_comma_delimited_list
@click.group(name='state',short_help='(Preview) Export, restore, and reset LocalStack state.',help="\n    (Preview) Manage and manipulate the localstack state.\n\n    The state command group allows you to interact with LocalStack's state backend.\n\n    Read more: https://docs.localstack.cloud/references/persistence-mechanism/#snapshot-based-persistence\n    ",cls=RequiresLicenseGroup)
def state():0
@state.command(name='reset',short_help='Reset the state of LocalStack services',help='\n    Reset the service states of the current LocalStack runtime.\n\n    This command invokes a reset of services in the currently running LocalStack container.\n    By default, all services are rest. The `services` options allows to select a subset of services\n    which should be reset.\n\n    This command tries to automatically discover the running LocalStack instance.\n    If LocalStack has not been started with `localstack start` (and is not automatically discoverable),\n    please set `LOCALSTACK_HOST`.\n    ')
@click.option('-s',_D,help='Comma-delimited list of services to reset. By default, the state of all running services is reset.')
@publish_invocation
def reset(services):
	A=services;from localstack.pro.core.bootstrap import pods_client as B
	if A and not is_comma_delimited_list(A):raise click.ClickException('Input the services as a comma-delimited list')
	C=[A.strip()for A in A.split(',')]if A else _A;B.reset_state(services=C);console.print('LocalStack state successfully reset')
@state.command(name='export',short_help='Export the state of LocalStack services',help='\n    Save the current state of the LocalStack container to a file on the local disk. This file can be restored at any\n    point in time using the `localstack state import` command. Please be aware that this might not be possible when\n    importing the state with a different version of LocalStack.\n\n    If you are looking for a managed solution to handle the state of your LocalStack container, please check out\n    the Cloud Pods feature: https://docs.localstack.cloud/user-guide/tools/cloud-pods/.\n\n    Use the DESTINATION argument to specify an absolute or relative path for the exported file.\n    If no destination is specified, a file named `ls-state-export` will be saved in the current working directory.\n\n    \x08\n    Examples:\n        localstack state export my-state\n        localstack state export ../parent-dir/my-state\n        localstack state export /home/johndoe/my-state\n\n    You can also specify a subset of services to export with the `--services` option.\n\n    \x08\n    For example:\n        localstack state export my-state --services s3,lambda\n\n    By default, the state of all running services is exported.\n    ')
@click.argument('destination',type=click.Path(resolve_path=_B),default='ls-state-export')
@click.option('-s',_D,help='Comma-delimited list of services to reset. By default, the state of all running services is exported.')
@click.option('-f',_E,_F,type=click.Choice([_C]),help='The formatting style for the save command output.')
@publish_invocation
def export(destination,services=_A,format_=_A):
	B=destination;A=services;_assert_host_reachable();D=StateService()
	try:
		A=[A.strip()for A in A.split(',')if A]if A else _A;E=D.export_pod(target=B,services=A)
		if format_==_C:console.print_json(json.dumps(E))
		else:console.print(f"LocalStack state successfully exported to: {B} ✅")
		return
	except Exception as C:raise CLIError(f"Failed to export LocalStack state - {C}")from C
@state.command(name='import',short_help='Import the state of LocalStack services',help='\n    Load the state of LocalStack from a file into the running container.\n    The SOURCE argument is the absolute or relative path to the file containing the state to import.\n    This file must have been generated from a previous `localstack state export` command.\n    Please be aware that it might not be possible to import a state generated from a different version of LocalStack.\n\n    \x08\n    Examples:\n        localstack state import my-state\n        localstack state import ../parent-dir/my-state\n        localstack state import /home/johndoe/my-state\n    ')
@click.argument('source',type=click.Path(exists=_B,resolve_path=_B))
@publish_invocation
def import_state(source):
	A=source;_assert_host_reachable();C=StateService()
	try:C.import_pod(source=A,show_progress=_B);console.print(f"LocalStack state successfully imported from {A} ✅")
	except Exception as B:raise CLIError(f"Failed to import LocalStack state - {B}")from B
@state.command(name='inspect',short_help='Inspect the state of LocalStack services',help='\n    Inspect the state of the Localstack Container.\n\n    By default, it starts a curses interface which allows an interactive inspection of the contents of the LocalStack\n    running instance.\n    ')
@click.option('-f',_E,_F,type=click.Choice([_G,'rich',_C]),default=_G,help='The formatting style for the inspect command output.')
@publish_invocation
def inspect_state(format_):
	_assert_host_reachable();B=CloudPodsClient()
	try:A=B.get_state_data()
	except Exception:raise CLIError('Error occurred while fetching the metamodel')
	C=['cloudwatch']
	for(D,E)in A.items():A[D]={A:B for(A,B)in E.items()if A not in C}
	TreeRenderer.get(format_).render_tree(A,'LocalStack State')