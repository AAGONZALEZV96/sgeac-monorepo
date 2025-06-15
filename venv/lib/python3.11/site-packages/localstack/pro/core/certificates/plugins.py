import logging,os
from localstack import config
from localstack.pro.core import config as config_ext
from localstack.pro.core.runtime.plugin import PlatformPlugin
from localstack.utils.objects import singleton_factory
from rolo import Router
LOG=logging.getLogger(__name__)
DEFAULT_ROOT_CA_NAME='LocalStack_LOCAL_Root_CA'
class CertificatesPlugin(PlatformPlugin):
	name='certificates'
	def on_platform_start(A):
		from localstack.pro.core.certificates.sni import patch_hypercorn_ssl_creation as B
		if config_ext.AUTO_SSL_CERTS:B(A.get_cert_store())
	def update_localstack_routes(A,router):from.resource import CertificateResource as B;router.add(B(A.get_cert_store()))
	def get_cert_store(A):return default_cert_store()
@singleton_factory
def default_cert_store():from.store import CertStore as A;return A(os.path.join(config.dirs.cache,'certs'),DEFAULT_ROOT_CA_NAME)