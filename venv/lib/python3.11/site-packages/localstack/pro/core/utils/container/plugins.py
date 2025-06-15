from localstack.pro.core.bootstrap.licensingv2 import LicensedPluginLoaderGuard
from localstack.utils.objects import singleton_factory
from plux import Plugin,PluginLifecycleListener,PluginManager
class ContainerRuntimePlugin(Plugin):namespace='localstack.container.runtime'
class DockerContainerRuntimePlugin(ContainerRuntimePlugin):
	name='docker'
	def load(B,*C,**D):from localstack.pro.core.utils.container.docker_container import DockerContainer as A;return A
class KubernetesContainerRuntimePlugin(ContainerRuntimePlugin):
	name='kubernetes';requires_license=True
	def load(B,*C,**D):from localstack.pro.core.utils.container.kubernetes_container import KubernetesContainer as A;return A
class ContainerRuntimePluginManager(PluginManager):
	def __init__(A,listener=None):super().__init__(ContainerRuntimePlugin.namespace,listener=listener)
	@staticmethod
	@singleton_factory
	def get():return ContainerRuntimePluginManager(LicensedPluginLoaderGuard())