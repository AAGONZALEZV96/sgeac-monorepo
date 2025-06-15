from localstack.pro.core import config
from localstack.runtime import hooks
@hooks.on_infra_start(should_load=config.ACTIVATE_PRO)
def init_resources_handler():from localstack.aws.handlers import run_custom_response_handlers as A;from localstack.pro.core.services.internal.resources.handler import ServiceAccountRegionCollector as B;from localstack.pro.core.services.internal.resources.resource import ResourcesResource as C;from localstack.services.internal import get_internal_apis as D;E=B();A.append(E);D().add(C())