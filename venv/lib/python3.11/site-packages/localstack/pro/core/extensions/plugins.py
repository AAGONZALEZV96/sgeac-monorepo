from __future__ import annotations
from localstack.pro.core import config
from localstack.runtime import hooks
EXTENSION_HOOK_PRIORITY=-1
@hooks.on_infra_start(priority=EXTENSION_HOOK_PRIORITY,should_load=config.ACTIVATE_PRO)
def extensions_on_infra_start():from localstack.pro.core.extensions.platform import run_on_infra_start_hook as A;from localstack.pro.core.extensions.resource import ExtensionsApi as B;from localstack.services.internal import get_internal_apis as C;C().add(B());A()
@hooks.on_infra_ready(priority=EXTENSION_HOOK_PRIORITY,should_load=config.ACTIVATE_PRO)
def extensions_on_infra_ready():from localstack.pro.core.extensions.platform import run_on_infra_ready_hook as A;A()
@hooks.on_infra_shutdown(priority=EXTENSION_HOOK_PRIORITY,should_load=lambda:config.ACTIVATE_PRO)
def extensions_on_infra_shutdown():from localstack.pro.core.extensions.platform import run_on_infra_shutdown_hook as A;A()
@hooks.configure_localstack_container(should_load=config.ACTIVATE_PRO and config.EXTENSION_DEV_MODE)
def configure_extensions_dev_container(container):from localstack.pro.core.extensions.bootstrap import run_on_configure_localstack_container_hook as A;A(container)
@hooks.prepare_host(should_load=config.ACTIVATE_PRO and config.EXTENSION_DEV_MODE)
def configure_extensions_dev_host():from localstack.pro.core.extensions.bootstrap import run_on_configure_host_hook as A;A()