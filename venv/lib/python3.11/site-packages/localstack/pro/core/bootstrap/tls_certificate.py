_A='retries'
import logging,os
from collections.abc import Callable
import requests
from localstack import config
from localstack.constants import API_ENDPOINT
from localstack.pro.core.bootstrap.auth import get_platform_auth_headers
from localstack.pro.core.bootstrap.licensingv2 import DevLocalstackEnvironment,get_licensed_environment
from localstack.utils.http import download,get_proxies
from localstack.utils.patch import patch
from localstack.utils.ssl import get_cert_pem_file_path,setup_ssl_cert
from localstack.utils.sync import retry
from localstack.utils.time import now
PLATFORM_CERTIFICATE_ENDPOINT_URL=f"{API_ENDPOINT}/certs"
PLATFORM_CERTIFICATE_ENDPOINT_TIMEOUT=5
PLATFORM_RETRY_CONFIG={_A:3,'sleep':1.}
CERTIFICATE_DOWNLOAD_TIMEOUT=5
CERTIFICATE_DOWNLOAD_RETRY_CONFIG={_A:3,'sleep':1.}
LOG=logging.getLogger(__name__)
def patch_setup_ssl_cert():
	@patch(target=setup_ssl_cert)
	def A(setup_community_ssl_cert):
		B=setup_community_ssl_cert;A=get_cert_pem_file_path()
		if os.path.exists(A):
			E=86400;F=os.path.getmtime(A)
			if F>now()-E:LOG.debug('Using cached TLS certificate (less than 24 hrs since last update).');return
		G=get_licensed_environment()
		if isinstance(G,DevLocalstackEnvironment):LOG.debug('Developer credentials detected, falling back to fetching the community certificate');B();return
		LOG.debug('Attempting to download pro TLS certificate file');H=get_platform_auth_headers();C=requests.Session();D=get_proxies()
		if D:C.proxies.update(D)
		def I():
			A=C.get(PLATFORM_CERTIFICATE_ENDPOINT_URL,timeout=PLATFORM_CERTIFICATE_ENDPOINT_TIMEOUT,headers=H)
			if not A.ok:raise Exception(f"Failed to download certificate, response code: {A.status_code}")
			return A.json()['url']
		try:J=retry(I,**PLATFORM_RETRY_CONFIG);retry(download,url=J,path=A,timeout=CERTIFICATE_DOWNLOAD_TIMEOUT,quiet=True,**CERTIFICATE_DOWNLOAD_RETRY_CONFIG);LOG.debug('TLS certificate downloaded successfully to %s',A)
		except Exception:LOG.warning('Could not download custom per-organisation certificate, falling back to public certificate',exc_info=config.is_trace_logging_enabled());B()