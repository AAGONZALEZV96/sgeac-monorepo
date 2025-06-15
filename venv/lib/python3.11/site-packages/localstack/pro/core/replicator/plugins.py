from localstack.http import Router
from localstack.http.dispatcher import Handler as RouteHandler
from localstack.pro.core.runtime.plugin import ProPlatformPlugin
class ReplicatorPlugin(ProPlatformPlugin):
	name='replicator'
	def update_localstack_routes(B,router):from localstack.pro.core.replicator.router import ReplicatorRouter as A;A(router).register_routes()
	def on_platform_ready(C):from localstack.aws import handlers as A;from localstack.pro.core.logging.format import MaskAwsCredentialsFilter as B;filter=B();A.log_response.http_logger.addFilter(filter);A.log_response.internal_http_logger.addFilter(filter)