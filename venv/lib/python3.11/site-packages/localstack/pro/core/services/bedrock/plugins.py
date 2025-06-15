import logging
from localstack.pro.core import config as config_ext
from localstack.runtime import hooks
LOG=logging.getLogger(__name__)
@hooks.on_runtime_ready(should_load=config_ext.ACTIVATE_PRO and config_ext.BEDROCK_PREWARM,priority=20)
def start_foundation_model_manager():from localstack.pro.core.services.bedrock.backends import get_foundation_model_manager as A;LOG.debug('Pre-warming Bedrock engine because BEDROCK_PREWARM is set');A();LOG.debug('Bedrock engine successfully pre-warmed')