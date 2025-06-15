from localstack.pro.core.bootstrap.licensingv2 import LicensedPluginLoaderGuard
from localstack.runtime import hooks
@hooks.on_infra_start()
def enable_lambda_executor_licensing():from localstack.services.lambda_.invocation.runtime_executor import EXECUTOR_PLUGIN_MANAGER as A;A.add_listener(LicensedPluginLoaderGuard())