import logging
from typing import Any
from localstack.pro.core.runtime.plugin import ProPlatformPlugin
from rolo.gateway import CompositeHandler
LOG=logging.getLogger(__name__)
class FisEmulationPlatformPlugin(ProPlatformPlugin):
	name='fis-emulation'
	def on_service_load(A,service,provider):
		if service=='fis':from localstack.pro.core.services.fis.scheduler import EmulatedExperimentScheduler as B;provider.experiment_scheduler=B();LOG.debug('Loaded %s: Experiments will be fully emulated',A.name)
	def update_request_handlers(B,handlers):from localstack.pro.core.services.fis.handler import FisEmulationHandler as A;handlers.append(A())