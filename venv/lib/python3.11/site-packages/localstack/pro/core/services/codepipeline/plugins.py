import logging
from typing import Callable
from localstack.pro.core.aws.api.codepipeline import ActionTypeId
from localstack.pro.core.services.codepipeline.actions.approval import ManualApprovalAction
from localstack.pro.core.services.codepipeline.actions.base import ActionCallable
from localstack.pro.core.services.codepipeline.actions.cloudformation import CloudformationAction
from localstack.pro.core.services.codepipeline.actions.code_deploy import CodeDeployBlueGreenAction
from localstack.pro.core.services.codepipeline.actions.codebuild import CodeBuildAction
from localstack.pro.core.services.codepipeline.actions.codestar import CodeStarSourceConnectionAction
from localstack.pro.core.services.codepipeline.actions.ecr import ECRSourceAction
from localstack.pro.core.services.codepipeline.actions.ecs import ECSDeployAction
from localstack.pro.core.services.codepipeline.actions.lambda_ import LambdaInvokeAction
from localstack.pro.core.services.codepipeline.actions.s3 import S3DeployAction,S3SourceAction
from localstack.utils.objects import singleton_factory
from plugin import Plugin,PluginManager
LOG=logging.getLogger(__name__)
CODEPIPELINE_PLUGIN_NAMESPACE='localstack.services.codepipeline.plugins'
class CodePipelineActionPlugin(Plugin):namespace=CODEPIPELINE_PLUGIN_NAMESPACE
class Name(CodePipelineActionPlugin):
	name:str='approval.aws.manual.1'
	def load(A,*B,**C):return ManualApprovalAction
class CodePipelineECRSourceActionPlugin(CodePipelineActionPlugin):
	name:str='source.aws.ecr.1'
	def load(A,*B,**C):return ECRSourceAction
class CodePipelineS3SourceActionPlugin(CodePipelineActionPlugin):
	name:str='source.aws.s3.1'
	def load(A,*B,**C):return S3SourceAction
class CodePipelineS3DeployActionPlugin(CodePipelineActionPlugin):
	name:str='deploy.aws.s3.1'
	def load(A,*B,**C):return S3DeployAction
class CodePipelineCodeStarSourceConnectionActionPlugin(CodePipelineActionPlugin):
	name:str='source.aws.codestarsourceconnection.1'
	def load(A,*B,**C):return CodeStarSourceConnectionAction
class CodePipelineCodeBuildActionPlugin(CodePipelineActionPlugin):
	name:str='build.aws.codebuild.1'
	def load(A,*B,**C):return CodeBuildAction
class CodePipelineCodeBuildTestActionPlugin(CodePipelineActionPlugin):
	name:str='test.aws.codebuild.1'
	def load(A,*B,**C):return CodeBuildAction
class CodePipelineEcsDeployActionPlugin(CodePipelineActionPlugin):
	name:str='deploy.aws.ecs.1'
	def load(A,*B,**C):return ECSDeployAction
class CodePipelineCodeDeployBlueGreenPlugin(CodePipelineActionPlugin):
	name:str='deploy.aws.codedeploytoecs.1'
	def load(A,*B,**C):return CodeDeployBlueGreenAction
class CodePipelineLambdaInvokeActionPlugin(CodePipelineActionPlugin):
	name:str='invoke.aws.lambda.1'
	def load(A,*B,**C):return LambdaInvokeAction
class CodePipelineCFNDeployPlugin(CodePipelineActionPlugin):
	name:str='deploy.aws.cloudformation.1'
	def load(A,*B,**C):return CloudformationAction
class CodePipelineActionsPluginManager(PluginManager[CodePipelineActionPlugin]):
	def __init__(A):super().__init__(CODEPIPELINE_PLUGIN_NAMESPACE)
	def _get_plugin_name_from_action(F,action_type_id):A=action_type_id;B,C,D,E=A['category'],A['owner'],A['provider'],A['version'];return f"{B}.{C}.{D}.{E}".lower()
	def get_action(A,action_type_id):
		try:B=A._get_plugin_name_from_action(action_type_id);C=A.load(B);return C.load()()
		except ValueError:return
@singleton_factory
def get_actions_plugin_manager():return CodePipelineActionsPluginManager()