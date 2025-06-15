from typing import Any
from localstack.pro.core.runtime.plugin import ProPlatformPlugin
class KafkaEsmPollerPlugin(ProPlatformPlugin):
	name='lambda-esm-kafka'
	def on_service_load(A,service,provider):
		if service!='lambda':return
		from localstack.pro.core.services.lambda_.event_source_mapping import hooks;hooks.LOAD_KAFKA_ESM_HOOKS=True