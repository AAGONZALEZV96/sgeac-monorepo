from localstack.aws.protocol import service_router as localstack_service_router
from localstack.aws.spec import ServiceModelIdentifier
from localstack.utils.patch import patch
def patch_service_router():
	from typing import Callable,Optional
	@patch(localstack_service_router.custom_signing_name_rules)
	def A(fn,signing_name,path,**C):
		B='rds';A=signing_name
		if A in[B,'docdb','neptune']:return ServiceModelIdentifier(B)
		return fn(A,path,**C)
	@patch(localstack_service_router.custom_host_addressing_rules)
	def B(fn,host,**A):
		if'mediastore-'in host:return ServiceModelIdentifier('mediastore-data')
		return fn(host,**A)