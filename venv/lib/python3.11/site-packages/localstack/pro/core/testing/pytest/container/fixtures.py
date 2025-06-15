_A=True
import os
from pathlib import Path
import pytest
from localstack import config,constants
from localstack.dev.run.configurators import EntryPointMountConfigurator,SourceVolumeMountConfigurator
from localstack.dev.run.paths import HostPaths
from localstack.testing.pytest.container import ENV_TEST_CONTAINER_MOUNT_SOURCES,ContainerFactory
from localstack.utils.bootstrap import Container,ContainerConfigurators
from localstack.utils.container_utils.container_client import ContainerConfigurator
@pytest.fixture
def pro_container_configurators(tmp_path,docker_network):
	F='test';C='LOCALSTACK_API_KEY';B='LOCALSTACK_AUTH_TOKEN';D=tmp_path/'localstack-volume';D.mkdir(parents=_A,exist_ok=_A);A=[ContainerConfigurators.random_gateway_port,ContainerConfigurators.random_container_name,ContainerConfigurators.mount_docker_socket,ContainerConfigurators.mount_localstack_volume(D),ContainerConfigurators.debug,ContainerConfigurators.network(docker_network),ContainerConfigurators.env_vars({'ACTIVATE_PRO':'1'})]
	if config.is_env_true(ENV_TEST_CONTAINER_MOUNT_SOURCES):G=os.path.join(constants.LOCALSTACK_VENV_FOLDER,'..','..');E=HostPaths(workspace_dir=Path(G).absolute(),volume_dir=D);A.append(SourceVolumeMountConfigurator(host_paths=E,pro=_A));A.append(EntryPointMountConfigurator(host_paths=E,pro=_A))
	elif os.getenv(B)and os.getenv(B)!=F:A.append(ContainerConfigurators.env_vars({B:os.getenv(B)}));A.append(ContainerConfigurators.env_vars({C:''}))
	elif os.getenv(C)and os.getenv(C)!=F:A.append(ContainerConfigurators.env_vars({C:os.getenv(C)}));A.append(ContainerConfigurators.env_vars({B:''}))
	else:raise ValueError('Cannot start LocalStack Pro without a valid LOCALSTACK_AUTH_TOKEN')
	return A
@pytest.fixture
def pro_container(container_factory,pro_container_configurators):return container_factory(pro=_A,configurators=pro_container_configurators)