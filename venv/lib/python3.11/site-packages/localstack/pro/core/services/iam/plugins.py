from localstack.aws.chain import CompositeHandler
from localstack.http import Router
from localstack.http.dispatcher import Handler as RouteHandler
from localstack.pro.core import config as config_ext
from localstack.pro.core.runtime.plugin import ProPlatformPlugin
from localstack.runtime import hooks
class IamEnforcementPlugin(ProPlatformPlugin):
	name='iam-enforcement'
	def update_request_handlers(B,handlers):from localstack.pro.core.services.iam.policy_engine.handler import IamEnforcementHandler as A;handlers.append(A.get())
	def update_gateway_routes(B,router):from localstack.pro.core.services.iam.router import IAMEnforcementRouter as A;A(router).register_routes()
class IamStreamPlugin(ProPlatformPlugin):
	name='iam-stream'
	def update_gateway_routes(B,router):from localstack.pro.core.services.iam.router import IAMStreamRouter as A;A(router).register_routes()
	def on_platform_shutdown(B):from localstack.pro.core.services.iam.policy_generation.policy_generator import PolicyGenerator as A;A.get().shutdown()
WANTED_ENFORCE_IAM=config_ext.ENFORCE_IAM
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO and WANTED_ENFORCE_IAM,priority=20)
def _disable_iam_during_startup():config_ext.ENFORCE_IAM=False
@hooks.on_infra_ready(should_load=config_ext.ACTIVATE_PRO and WANTED_ENFORCE_IAM,priority=-20)
def _enable_iam_after_ready():config_ext.ENFORCE_IAM=True