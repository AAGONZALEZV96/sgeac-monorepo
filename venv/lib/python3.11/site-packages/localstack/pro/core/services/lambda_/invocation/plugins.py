from localstack.services.lambda_.invocation.plugins import RuntimeExecutorPlugin
class KubernetesRuntimeExecutorPlugin(RuntimeExecutorPlugin):
	name='kubernetes';requires_license=True
	def load(B,*C,**D):from localstack.pro.core.services.lambda_.invocation.kubernetes_runtime_executor import KubernetesRuntimeExecutor as A;return A