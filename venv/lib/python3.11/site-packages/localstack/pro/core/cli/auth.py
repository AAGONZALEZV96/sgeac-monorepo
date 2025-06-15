_B=False
_A=True
import os,click
from click import ClickException
from localstack.cli.localstack import LocalStackCliGroup
from localstack.utils.analytics.cli import publish_invocation
@click.group(name='auth',cls=LocalStackCliGroup,short_help='Authenticate with your LocalStack account',help='\n    Authenticate with your LocalStack account.\n\n    Manage your credentials and authenticate with your LocalStack account.\n    ')
def auth():0
@auth.command(name='set-token',short_help='Set your Localstack auth token to allow you to start LocalStack Pro',help='\n    Configure your auth token. Your auth token is used the license activation to activate LocalStack Pro.\n    This is different from `localstack auth login` which enables platform features such as pushing cloud pods to your\n    webapp account.\n\n    The auth token you configure here will be passed to the `LOCALSTACK_AUTH_TOKEN` environment variable of the\n    LocalStack container when you run `localstack start`.\n\n    AUTH_TOKEN: Your Localstack auth token that you can find in https://app.localstack.cloud.\n    ')
@click.argument('auth-token',type=str,required=_A)
@publish_invocation
def set_token(auth_token):
	from localstack.pro.core.bootstrap.licensingv2 import AuthToken as D;A=D(auth_token)
	if not A.is_syntax_valid():raise ClickException('The format of the token you provided is invalid, please make sure to set a valid token. Auth tokens start with `ls-` and are followed by a 36-character string. You can find your auth token in the LocalStack web app https://app.localstack.cloud.')
	if not A.is_checksum_valid():raise ClickException('The token you provided appears to be invalid, please make sure to set a valid token. You can find your auth token in the LocalStack web app https://app.localstack.cloud.')
	from localstack.pro.core import config as E;from localstack.pro.core.bootstrap.auth import get_auth_cache as F
	try:B=F();B['LOCALSTACK_AUTH_TOKEN']=A.encoded();B.save()
	except Exception as C:raise ClickException(f"Could not save auth configuration into {E.AUTH_CACHE_PATH}: {C}")from C
	click.echo('Token configured successfully')
@auth.command(name='clear-token',short_help='Clear any existing LocalStack auth token from your environment')
@publish_invocation
def clear_token():
	from localstack.pro.core import config as D;from localstack.pro.core.bootstrap.auth import get_auth_cache as E;from localstack.pro.core.bootstrap.licensingv2 import ENV_LOCALSTACK_AUTH_TOKEN as B,AuthToken as F
	try:
		A=E()
		if B not in A:click.echo('No token in environment, no change necessary');return
		G=F(A.pop(B));A.save();click.echo(f"Token {G} cleared successfully")
	except Exception as C:raise ClickException(f"Could not save auth configuration into {D.AUTH_CACHE_PATH}: {C}")from C
@auth.command(name='show-token',short_help='Show the auth token in your configuration',help='\n    Show the token that LocalStack picks up from your environment. This can either be the auth token set via\n    `localstack auth set-token`, or the value of `LOCALSTACK_AUTH_TOKEN`.\n    ')
@click.option('--plain',is_flag=_A,required=_B,default=_B,help='\n    Setting this flag will output only the value of the token in plain text, so it can be used as input\n    to other programs, like `LOCALSTACK_AUTH_TOKEN=$(localstack auth show-token --plain)`.\n    ')
@publish_invocation
def show_token(plain):
	H='Token not configured in environment yet, please run localstack auth set-token <AUTH_TOKEN>, or set the environment variable LOCALSTACK_AUTH_TOKEN to a valid auth token. You can find your auth token in the LocalStack web app https://app.localstack.cloud.';from localstack.pro.core import config as B;from localstack.pro.core.bootstrap.auth import get_auth_cache as I;from localstack.pro.core.bootstrap.licensingv2 import ENV_LOCALSTACK_AUTH_TOKEN as A,AuthToken as C
	def D(_token):
		A=_token;B=A.is_valid();click.echo(f"Valid: {B}",err=_A)
		if plain:click.echo(A.token)
		else:click.echo(f"Token: {A}")
	E=os.getenv(A,'').strip()
	if E:click.echo(f"Prioritizing auth token set in environment variable {A}",err=_A);D(C(E));return
	if not os.path.isfile(B.AUTH_CACHE_PATH):click.echo(H,err=_A);return
	try:J=I()
	except Exception as F:raise ClickException(f"Could not load auth configuration from {B.AUTH_CACHE_PATH}: {F}")from F
	G=J.get(A,'')
	if not G:click.echo(H,err=_A)
	D(C(G))
@auth.command(name='login',short_help='Login to the your LocalStack account',help='\n    Login to the LocalStack Platform.\n\n    This command performs a login to your LocalStack account, giving you access to features that require\n    platform permissions, such as uploading cloud pods to your account.\n\n    This command is deprecated and it will be removed soon.\n    To use LocalStack features that requires authentication to the LocalStack platform\n    (e.g., Cloud Pods), please run `localstack auth set-token <AUTH_TOKEN>`, or set the\n    environment variable `LOCALSTACK_AUTH_TOKEN` to a valid auth token.\n    ',deprecated=_A)
@click.option('-u','--username',help='Username (email address) for login',metavar='USER',required=_A)
@click.option('-p','--password',help='Password for login',metavar='PWD',prompt=_A,hide_input=_A,confirmation_prompt=_B,required=_A)
@publish_invocation
def login(username,password):
	from localstack.pro.core.bootstrap import auth
	try:auth.login(username,password);click.echo('successfully logged in')
	except Exception as A:raise click.ClickException(f"Authentication Error: {A}")
@auth.command(name='logout',short_help='Log out from your LocalStack account',help='\n    Log out from the LocalStack Platform.\n\n    This command performs a logout from the LocalStack platform and deletes all session information on your\n    machine.\n    ',deprecated=_A)
@publish_invocation
def logout():from localstack.pro.core.bootstrap import auth;auth.logout();click.echo('successfully logged out')