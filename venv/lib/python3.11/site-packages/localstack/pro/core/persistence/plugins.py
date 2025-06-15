import logging,os
from localstack import config
from localstack.pro.core import config as config_ext
from localstack.runtime import hooks
from localstack.services.internal import get_internal_apis
LOG=logging.getLogger(__name__)
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO)
def register_restricted_pods_api():from localstack.pro.core.persistence.pods.api.pods_api import CloudPodsRestrictedApi as A;get_internal_apis().add(A())
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO)
def register_remotes_pods_api():from localstack.pro.core.persistence.remotes.api import CloudPodsRemotesApi as A;get_internal_apis().add(A())
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO)
def register_ci_run_manager():from localstack.pro.core.utils.cloud_pods.ci_run_manager import get_ci_run_manager as A;A().startup()
@hooks.on_infra_shutdown(should_load=config_ext.ACTIVATE_PRO)
def shutdown_ci_run_manager():from localstack.pro.core.utils.cloud_pods.ci_run_manager import get_ci_run_manager as A;A().shutdown()
@hooks.on_infra_ready(should_load=config_ext.ACTIVATE_PRO)
def register_auto_load_pod():
	from localstack.pro.core.config import AUTO_LOAD_POD as A;from localstack.pro.core.persistence.pods.auto_load import PodLoaderFromEnv as D,PodLoaderFromInitDir as E;B=os.path.normpath(os.path.join(config.dirs.config,'..','init-pods.d'))
	if(A or os.path.exists(B))and config.PERSISTENCE:LOG.debug('AUTO_LOAD_POD has not effect if PERSISTENCE is enabled.');return
	if os.path.exists(B):C=E(init_dir=B);C.load()
	if A:C=D(A);C.load()