_A='[red]Error:[/red] '
import logging
from typing import Any
import click
from localstack.cli import LocalstackCli,LocalstackCliPlugin,console
from localstack.utils.analytics.cli import publish_invocation
from.auth import auth
from.aws import aws
from.cli import RequiresLicenseGroup
from.cloud_pods import pod
from.ephemeral import ephemeral
from.extensions import extensions
from.iam import iam
from.license import license
from.replicator import replicator
from.state import state
class ProCliPlugins(LocalstackCliPlugin):
	name='pro'
	def attach(B,cli):A=cli.group;A.add_command(dns);A.add_command(aws);A.add_command(extensions);A.add_command(license);A.add_command(state);A.add_command(auth);A.add_command(pod);A.add_command(ephemeral);A.add_command(replicator)
@click.group(name='dns',short_help='Manage LocalStack DNS host config',help='\n    Manage the usage of the LocalStack DNS on your host.\n\n    This command provides tools to configure your the DNS on your host machine to use the LocalStack DNS\n    on your host machine.\n    The LocalStack DNS is used for certain Pro features (like the transparent endpoint injection).\n\n    \x08\n    Visit https://docs.localstack.cloud/user-guide/tools/transparent-endpoint-injection/dns-server/\n    for more information on the LocalStack DNS and how it is used.\n    ',cls=RequiresLicenseGroup)
def dns():0
@dns.command(name='systemd-resolved',short_help='Manage LocalStack DNS in systemd-resolved',help='\n        Manage the LocalStack DNS configuration using systemd-resolved (Ubuntu, Debian, etc.).\n\n        This command sets (or reverts) the LocalStack DNS, running in the current LocalStack runtime, in\n        systemd-resolved for the docker network interface.\n        Most current Linux systems - like Ubuntu, Debian, or Fedora - use systemd-resolved for the network name\n        resolution.\n    ')
@click.option('--set/--revert','-s/-r','set_',default=True,help='Set or revert DNS settings')
@publish_invocation
def cmd_dns_systemd(set_):import localstack.pro.core.bootstrap.dns_utils;from localstack.pro.core.bootstrap.dns_utils import configure_systemd as A;console.print('Configuring systemd-resolved...');B=localstack.pro.core.bootstrap.dns_utils.LOG.name;localstack.pro.core.bootstrap.dns_utils.LOG=ConsoleLogger(B);A(not set_)
class ConsoleLogger(logging.Logger):
	def __init__(A,name):super(ConsoleLogger,A).__init__(name)
	def info(B,msg,*A,**C):console.print(msg%A)
	def warning(B,msg,*A,**C):console.print('[red]Warning:[/red] ',msg%A)
	def error(B,msg,*A,**C):console.print(_A,msg%A)
	def exception(B,msg,*A,**C):console.print(_A,msg%A);console.print_exception()