from __future__ import annotations
_J='localstack.pro.core'
_I='neptune'
_H='transfer'
_G='mediastore'
_F='elasticache'
_E='apigatewayv2'
_D='apigateway'
_C='athena'
_B='rds'
_A='s3'
import logging,os
from localstack import config as localstack_config
from localstack.config import HostAndPort
from localstack.plugins import OASPlugin
from localstack.pro.core import config as config_ext
from localstack.pro.core.bootstrap import licensingv2
from localstack.pro.core.constants import S3_ASSETS_BUCKET
from localstack.runtime import hooks
from localstack.runtime.exceptions import LocalstackExit
from localstack.utils.bootstrap import API_DEPENDENCIES,Container,get_enabled_apis,get_preloaded_services
LOG=logging.getLogger(__name__)
EXTERNAL_PORT_APIS=_D,_E,_C,'cloudfront','codecommit','ecs','ecr',_F,_G,_B,_H,'kafka',_I
API_DEPENDENCIES.update({'amplify':[_A,'appsync','cognito'],_D:[_E],_C:[_A],'backup':[_A],'docdb':[_B],'ecs':['ecr'],_F:['ec2'],'elb':['elbv2'],'emr':[_C,_A],'glacier':[_A],'glue':[_A,'iam'],'iot':['iotanalytics','iot-data','iotwireless'],'kinesisanalytics':['kinesis','dynamodb'],_I:[_B],_B:['rds-data'],_G:['mediastore-data'],'redshift':['redshift-data'],'timestream':['timestream-write','timestream-query'],_H:[_A]})
get_enabled_apis.cache_clear()
get_preloaded_services.cache_clear()
def modify_gateway_listen_config(cfg):
	if os.getenv('GATEWAY_LISTEN')is None:A='0.0.0.0'if localstack_config.in_docker()else'127.0.0.1';cfg.GATEWAY_LISTEN.append(HostAndPort(host=A,port=443))
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO)
def add_custom_edge_routes():from localstack.pro.core.services.xray.routes import store_xray_records as A;from localstack.services.edge import ROUTER as B;B.add('/xray_records',A,methods=['POST'])
@hooks.prepare_host(priority=200)
def patch_community_pro_detection():from localstack.utils import bootstrap as A;A.is_auth_token_configured=config_ext.is_auth_token_configured
@hooks.prepare_host(priority=100,should_load=config_ext.ACTIVATE_PRO)
def activate_pro_key_on_host():
	try:licensingv2.get_licensed_environment().activate()
	except licensingv2.LicensingError as A:raise LocalstackExit(reason=A.get_user_friendly(),code=55)
@hooks.configure_localstack_container(priority=10,should_load=config_ext.ACTIVATE_PRO)
def configure_pro_container(container):modify_gateway_listen_config(localstack_config);container.configure(licensingv2.configure_container_licensing)
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO,priority=10)
def setup_pro_infra():
	from localstack.pro.core.bootstrap import tls_certificate as A;_setup_logging()
	try:licensingv2.get_licensed_environment().activate()
	except licensingv2.LicensingError as B:config_ext.ACTIVATE_PRO=False;raise LocalstackExit(reason=B.get_user_friendly(),code=55)
	modify_gateway_listen_config(localstack_config);from localstack.pro.core.aws.protocol import service_router as C;from localstack.pro.core.utils.aws import aws_utils as D;C.patch_service_router();D.patch_aws_utils();configure_licensing_for_service_plugins();set_default_providers_to_pro();A.patch_setup_ssl_cert()
def configure_licensing_for_service_plugins():from localstack.services.plugins import SERVICE_PLUGINS as A;A.plugin_manager.add_listener(licensingv2.LicensedPluginLoaderGuard())
def set_default_providers_to_pro():
	F='pro';from localstack.services.plugins import PLUGIN_NAMESPACE as D,SERVICE_PLUGINS as A;E=licensingv2.get_licensed_environment()
	if not config_ext.PROVIDER_FORCE_EXPLICIT_LOADING:
		for(B,G)in localstack_config.SERVICE_PROVIDER_CONFIG._provider_config.items():
			H=A.api_provider_specs[B];C=next((A for A in H if A==f"{G}_pro"),None)
			if C and E.has_product_license(f"{D}/{B}:{C}"):localstack_config.SERVICE_PROVIDER_CONFIG.set_provider(B,C)
	I=[B for B in A.apis_with_provider(F)if localstack_config.SERVICE_PROVIDER_CONFIG.default_value not in A.api_provider_specs[B]or E.has_product_license(f"{D}/{B}:pro")];localstack_config.SERVICE_PROVIDER_CONFIG.bulk_set_provider_if_not_exists(I,F)
@hooks.on_infra_ready(should_load=config_ext.ACTIVATE_PRO)
def initialize_health_info():from localstack.pro.core.utils.persistence import update_persistence_health_info as A;A()
@hooks.on_infra_start(priority=100)
def deprecation_warnings_pro():D='4.0.0';C='2.2.0';from localstack.deprecations import DEPRECATIONS as A,EnvVarDeprecation as B;A.append(B('EC2_AUTOSTART_DAEMON',C,'The localstack local daemons have been removed, please let us know if you were actively using them.'));A.append(B('AUTOSTART_UTIL_CONTAINERS',C,'The external bigdata image support has been removed. This option has no effect. Please remove it from your configuration.'));A.append(B('ACTIVATE_NEW_POD_CLIENT','2.3.0','This configuration does not have any effect anymore. Please remove this environment variable.'));A.append(B('S3_DIR',D,'The Legacy S3 implementation has been removed. This option has no effect. Please remove this environment variable.'));A.append(B('LOCALSTACK_API_KEY',D,'Please use your personal developer auth token or CI auth token with LOCALSTACK_AUTH_TOKEN.'))
DEFAULT_SKIP_PATTERNS={'.*(forums|console|docs|clientvpn|sso|boto3|(signin(\\-reg)?))\\.([^\\.]+\\.)?(aws\\.amazon|amazonaws)\\.com','.*captcha-prod\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com','^aws\\.amazon\\.com','^github-production-release-.*\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com','^aws-glue-etl-artifacts\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com','^redshift-maven-repository\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com',f"^{S3_ASSETS_BUCKET}\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com",'^localstack-pods-.*\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com','^prod-registry-k8s-io-.*\\.s3\\.(dualstack\\.)?.*\\.amazonaws\\.com','^(?:prod|staging)sharedcertsstack-.*\\.s3(\\.[^\\.]+)?\\.amazonaws\\.com'}
TRANSPARENT_ENDPOINT_INJECTION_NAMES=['.*.amazonaws.com','.*aws.amazon.com','.*cloudfront.net']
@hooks.on_infra_start(should_load=config_ext.ACTIVATE_PRO)
def configure_transparent_endpoint_injection():
	from localstack.dns.server import get_dns_server as B,is_server_running as C
	if not config_ext.DISABLE_TRANSPARENT_ENDPOINT_INJECTION and C():
		try:
			LOG.debug('setting up transparent endpoint injection');A=B()
			for D in TRANSPARENT_ENDPOINT_INJECTION_NAMES:A.add_host_pointing_to_localstack(D)
			for E in DEFAULT_SKIP_PATTERNS:A.add_skip(E)
		except Exception as F:LOG.warning('Unable to configure transparent endpoint injection: %s',F)
def _setup_logging():A=logging.DEBUG if localstack_config.DEBUG else logging.INFO;logging.getLogger(_J).setLevel(A);logging.getLogger('asyncio').setLevel(logging.INFO);logging.getLogger('botocore').setLevel(logging.INFO);logging.getLogger('dulwich').setLevel(logging.ERROR);logging.getLogger('hpack').setLevel(logging.INFO);logging.getLogger('jnius.reflect').setLevel(logging.INFO);logging.getLogger('kazoo').setLevel(logging.ERROR);logging.getLogger('kubernetes').setLevel(logging.INFO);logging.getLogger('parquet').setLevel(logging.INFO);logging.getLogger('pyftpdlib').setLevel(logging.INFO);logging.getLogger('pyhive').setLevel(logging.INFO);logging.getLogger('pyqldb').setLevel(logging.INFO);logging.getLogger('redshift_connector').setLevel(logging.INFO);logging.getLogger('websockets').setLevel(logging.INFO);logging.getLogger('Parser').setLevel(logging.CRITICAL);logging.getLogger('postgresql_proxy').setLevel(logging.WARNING);logging.getLogger('intercept').setLevel(logging.WARNING);logging.getLogger('root').setLevel(logging.ERROR);logging.getLogger('').setLevel(logging.ERROR)
class OASProCore(OASPlugin):name=_J