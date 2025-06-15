_B='latest'
_A='2.0.20'
import logging
from typing import List
import distro
from localstack.constants import ARTIFACTS_REPO
from localstack.packages import Package,PackageInstaller
from localstack.packages.core import NodePackageInstaller,PermissionDownloadInstaller
from localstack.utils.platform import get_arch
LOG=logging.getLogger(__name__)
RULE_ENGINE_INSTALL_URL='https://github.com/whummer/serverless-iot-offline'
MOSQUITTO_DIST_URL=ARTIFACTS_REPO+'/raw/067e95fed974ea07860b198b4938c593358b4def/mosquitto/{os_codename}/v{version}/{platform}/mosquitto'
MOSQUITTO_VERSIONS=['2.0.12',_A]
DEFAULT_MOSQUITTO_VERSION=_A
class MosquittoPackage(Package):
	def __init__(A):super().__init__('Mosquitto',DEFAULT_MOSQUITTO_VERSION)
	def get_versions(A):return MOSQUITTO_VERSIONS
	def _get_installer(A,version):return MosquittoPackageInstaller(version)
class MosquittoPackageInstaller(PermissionDownloadInstaller):
	def __init__(A,version):super().__init__('mosquitto',version)
	def _get_download_url(A):B=distro.codename()or'bookworm';return MOSQUITTO_DIST_URL.format(version=A.version,platform=get_arch(),os_codename=B)
class IoTRuleEnginePackage(Package):
	def __init__(A):super().__init__('IoTRuleEngine',_B)
	def get_versions(A):return[_B]
	def _get_installer(A,version):return IoTRuleEnginePackageInstaller(version=version)
class IoTRuleEnginePackageInstaller(NodePackageInstaller):
	def __init__(A,version):super().__init__(package_name='serverless-iot-offline',package_spec=RULE_ENGINE_INSTALL_URL,version=version,main_module='query.js')
iot_rule_engine_package=IoTRuleEnginePackage()
mosquitto_package=MosquittoPackage()