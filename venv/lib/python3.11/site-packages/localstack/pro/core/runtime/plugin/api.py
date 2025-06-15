from typing import Any
from localstack.aws.chain import CompositeHandler,CompositeResponseHandler
from localstack.http import Router
from localstack.http.dispatcher import Handler as RouteHandler
from localstack.pro.core.constants import PLATFORM_PLUGIN_NAMESPACE
from plux import Plugin
class BasePlatformPlugin(Plugin):
	def load(A,*B,**C):return A
	def on_plugin_load(A,*B,**C):raise NotImplementedError
class PlatformPlugin(BasePlatformPlugin):
	namespace=PLATFORM_PLUGIN_NAMESPACE;requires_license:bool=False;priority:int=0
	def on_plugin_load(A):0
	def on_platform_start(A):0
	def update_gateway_routes(A,router):0
	def update_localstack_routes(A,router):0
	def update_request_handlers(A,handlers):0
	def update_response_handlers(A,handlers):0
	def on_service_load(A,service,provider):0
	def on_platform_ready(A):0
	def on_platform_shutdown(A):0
class ProPlatformPlugin(PlatformPlugin):
	requires_license:bool=True
	def should_load(B):from localstack.pro.core import config as A;return A.ACTIVATE_PRO