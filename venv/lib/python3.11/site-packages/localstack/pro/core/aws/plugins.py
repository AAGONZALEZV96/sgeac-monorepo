from localstack.aws.api import RequestContext
from localstack.aws.handlers.region import RegionRewriterStrategy
from localstack.pro.core.runtime.plugin import ProPlatformPlugin
class AllPartitionRegionRewriterStrategy(RegionRewriterStrategy):
	def apply(A,context):0
class NonDefaultPartitionPlugin(ProPlatformPlugin):
	name='non-default-partitions'
	def on_platform_start(B):from localstack.aws.handlers import rewrite_region as A;A.region_rewriter_strategy=AllPartitionRegionRewriterStrategy()