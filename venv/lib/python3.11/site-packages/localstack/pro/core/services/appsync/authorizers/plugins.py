_B='AppSyncAuthorizer'
_A=None
from typing import TYPE_CHECKING,Optional,cast
from plux import Plugin,PluginManager
if TYPE_CHECKING:from localstack.pro.core.services.appsync.authorizers.base import AppSyncAuthorizer
class AppSyncAuthorizerPlugin(Plugin):namespace:str='localstack.pro.core.services.appsync.authorizers'
class AppSyncApiKeyAuthorizerPlugin(AppSyncAuthorizerPlugin):
	name:str='api_key'
	def load(B,*C,**D):from localstack.pro.core.services.appsync.authorizers.api_key_authorizer import AppSyncAuthorizerApiKey as A;return A
class AppSyncCognitoAuthorizerPlugin(AppSyncAuthorizerPlugin):
	name:str='cognito'
	def load(B,*C,**D):from localstack.pro.core.services.appsync.authorizers.cognito_authorizer import AppSyncAuthorizerCognito as A;return A
class AppSyncIAMAuthorizerPlugin(AppSyncAuthorizerPlugin):
	name:str='iam'
	def load(B,*C,**D):from localstack.pro.core.services.appsync.authorizers.iam_authorizer import AppSyncAuthorizerIAM as A;return A
class AppSyncLambdaAuthorizerPlugin(AppSyncAuthorizerPlugin):
	name:str='lambda'
	def load(B,*C,**D):from localstack.pro.core.services.appsync.authorizers.lambda_authorizer import AppSyncAuthorizerLambda as A;return A
class AppSyncOIDCAuthorizerPlugin(AppSyncAuthorizerPlugin):
	name:str='oidc'
	def load(B,*C,**D):from localstack.pro.core.services.appsync.authorizers.oidc_authorizer import AppSyncAuthorizerOIDC as A;return A
class AuthorizerPluginManager(PluginManager[AppSyncAuthorizerPlugin]):
	instance:Optional['AuthorizerPluginManager']=_A
	def __init__(A):super().__init__(AppSyncAuthorizerPlugin.namespace)
	@classmethod
	def load_authorizer(A,name):
		if A.instance is _A:A.instance=A()
		B=A.instance.load(name)
		if B is _A:return
		C=cast(type[_B],B.load());return C()
	@classmethod
	def all_authorizers(A):
		if A.instance is _A:A.instance=A()
		B=A.instance.load_all();C=[cast(type[_B],A.load())for A in B];return[A()for A in C]