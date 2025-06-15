from __future__ import annotations
from localstack.pro.core import config
from localstack.runtime import hooks
PLATFORM_PLUGIN_HOOK_PRIORITY=0
@hooks.on_infra_start(priority=8,should_load=config.ACTIVATE_PRO)
def platform_plugins_add_service_plugin_listener():from localstack.services.internal import PluginsResource as B;from localstack.services.plugins import SERVICE_PLUGINS as C;from.manager import PlatformPluginManager as D;A=D.get();A.add_service_plugin_listener(C.plugin_manager);B.plugin_managers.append(A)
@hooks.on_infra_start(priority=PLATFORM_PLUGIN_HOOK_PRIORITY,should_load=config.ACTIVATE_PRO)
def platform_plugins_on_infra_start():from localstack.aws.handlers import run_custom_response_handlers as B,serve_custom_service_request_handlers as C;from localstack.services import edge;from localstack.services.internal import get_internal_apis as D;from.manager import PlatformPluginManager as E;A=E.get();A.call_on_platform_start();A.call_update_gateway_routes(edge.ROUTER);A.call_update_localstack_routes(D());A.call_update_request_handlers(C);A.call_update_response_handlers(B)
@hooks.on_infra_ready(priority=PLATFORM_PLUGIN_HOOK_PRIORITY,should_load=config.ACTIVATE_PRO)
def platform_plugins_on_infra_ready():from.manager import PlatformPluginManager as A;A.get().call_on_platform_ready()
@hooks.on_infra_shutdown(priority=PLATFORM_PLUGIN_HOOK_PRIORITY,should_load=lambda:config.ACTIVATE_PRO)
def platform_plugins_on_infra_shutdown():from.manager import PlatformPluginManager as A;A.get().call_on_platform_shutdown()