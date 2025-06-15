from localstack.pro.core import config as ext_config
from localstack.runtime import hooks
@hooks.on_infra_start(should_load=ext_config.ACTIVATE_PRO)
def register_pickle_patches_runtime():from.reducers import register as A;A()