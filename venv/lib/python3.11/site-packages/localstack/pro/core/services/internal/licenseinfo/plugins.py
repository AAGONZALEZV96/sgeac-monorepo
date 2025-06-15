from localstack.pro.core import config as config_ext
from localstack.runtime import hooks
from rolo import Resource
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO)
def init_licenseinfo_handler():from localstack.pro.core.bootstrap.licensingv2 import get_licensed_environment as A;from localstack.pro.core.services.internal.licenseinfo.resource import LicenseInfoResource as B;from localstack.services.internal import get_internal_apis as C;D=A();C().add(Resource('/_localstack/licenseinfo',B(licensed_environment=D)))