import logging
from localstack.pro.core import config as ext_config
from localstack.pro.core.runtime.plugin.api import ProPlatformPlugin
from localstack.runtime import hooks
LOG=logging.getLogger(__name__)
class EncryptionPlugin(ProPlatformPlugin):
	name='pod-encryption'
	def on_platform_ready(B):from localstack.pro.core.persistence.utils.encryption import patch_create_and_pull_content as A;A()
	def should_load(A):
		if not super().should_load():return False
		return ext_config.POD_ENCRYPTION
@hooks.on_infra_start(should_load=ext_config.ACTIVATE_PRO)
def register_public_cloudpods_endpoints():from localstack.services.internal import get_internal_apis as A;from localstack.services.plugins import SERVICE_PLUGINS as B;from.endpoints import PublicPodsResource as C;from.manager import PodStateManager as D;A().add(C(D(B)))