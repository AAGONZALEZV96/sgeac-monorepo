_A='config.properties'
import os
from typing import List
from localstack import config
from localstack.constants import LOCALHOST,MAVEN_REPO_URL
from localstack.packages import InstallTarget,Package
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.pro.core import config as ext_config
from localstack.pro.core.packages.bigdata_common import bigdata_jar_cache_dir,download_and_cache_jar_file
from localstack.pro.core.packages.cve_fixes import CVEFix,FixStrategyDelete,fix_cves_in_jar_files
from localstack.utils.files import cp_r,load_file,save_file
URL_PATTERN_TRINO=f"{MAVEN_REPO_URL}/io/trino/trino-server/<version>/trino-server-<version>.tar.gz"
TRINO_DEFAULT_VERSION='389'
TRINO_VERSIONS=[TRINO_DEFAULT_VERSION]
TRINO_JVM_CONFIG='\n-server\n-Xmx1G\n-XX:-UseBiasedLocking\n-XX:+UseG1GC\n-XX:+UseGCOverheadLimit\n-XX:+ExplicitGCInvokesConcurrent\n-XX:+HeapDumpOnOutOfMemoryError\n-XX:+ExitOnOutOfMemoryError\n-XX:ReservedCodeCacheSize=150M\n-Duser.timezone=UTC\n-Djdk.attach.allowAttachSelf=true\n-Djdk.nio.maxCachedBufferSize=2000000\n-Dpresto-temporarily-allow-java8=true\n'
TRINO_CONFIG_PROPS='\nnode.id=trino-master\nnode.environment=test\ncoordinator=true\nnode-scheduler.include-coordinator=true\nhttp-server.http.port=8080\nquery.max-memory=512MB\nquery.max-memory-per-node=512MB\n# query.max-total-memory-per-node=512MB\ndiscovery-server.enabled=true\ndiscovery.uri=http://localhost:8080\nprotocol.v1.alternate-header-name=Trino\n'
TRINO_HIVE_CONFIG='\nconnector.name=hive-hadoop2\n# hive.metastore=file\n# hive.metastore.catalog.dir=file:///tmp/hive_catalog\n# hive.metastore.user=test\nhive.metastore.uri=thrift://{hive_host}\nhive.s3.path-style-access=true\nhive.s3.endpoint={s3_endpoint}\nhive.s3.aws-access-key=test\nhive.s3.aws-secret-key=test\nhive.force-local-scheduling=true\nhive.non-managed-table-creates-enabled=true\nhive.non-managed-table-writes-enabled=true\nhive.allow-drop-table=true\nhive.recursive-directories=true\nhive.iceberg-catalog-name=iceberg\n'
TRINO_ICEBERG_CONFIG='\nconnector.name=iceberg\niceberg.catalog.type=HIVE_METASTORE\niceberg.hive-catalog-name=hive\nhive.metastore.uri=thrift://{hive_host}\nhive.s3.path-style-access=true\nhive.s3.endpoint={s3_endpoint}\nhive.s3.aws-access-key=test\nhive.s3.aws-secret-key=test\n'
TRINO_DELTALAKE_CONFIG='\nconnector.name=delta-lake\ndelta.hive-catalog-name=hive\nhive.metastore.uri=thrift://{hive_host}\nhive.s3.path-style-access=true\nhive.s3.endpoint={s3_endpoint}\nhive.s3.aws-access-key=test\nhive.s3.aws-secret-key=test\n'
TRINO_HIVE_CONFIGS=['hive.metastore.uri','hive.config.resources','hive.metastore-timeout','hive.metastore-cache-ttl','hive.metastore-cache-maximum-size','hive.metastore-refresh-interval','hive.metastore-refresh-max-threads','hive.metastore.glue.region','hive.metastore.glue.pin-client-to-current-region','hive.metastore.glue.max-connections','hive.metastore.glue.max-error-retries','hive.metastore.glue.default-warehouse-dir','hive.metastore.glue.aws-access-key','hive.metastore.glue.aws-secret-key','hive.metastore.glue.catalogid','hive.metastore.glue.endpoint-url','hive.metastore.glue.partitions-segments','hive.metastore.glue.get-partition-threads','hive.metastore.glue.iam-role','hive.s3.use-instance-credentials','hive.s3.aws-access-key','hive.s3.aws-secret-key','hive.s3.iam-role','hive.s3.endpoint','hive.s3.storage-class','hive.s3.signer-type','hive.s3.path-style-access','hive.s3.staging-directory','hive.s3.pin-client-to-current-region','hive.s3.ssl.enabled','hive.s3.sse.enabled','hive.s3.sse.type','hive.s3.sse.kms-key-id','hive.s3.kms-key-id','hive.s3.encryption-materials-provider','hive.s3.upload-acl-type','hive.s3.skip-glacier-objects','hive.s3.max-error-retries','hive.s3.max-client-retries','hive.s3.max-backoff-time','hive.s3.max-retry-time','hive.s3.connect-timeout','hive.s3.socket-timeout','hive.s3.max-connections','hive.s3.multipart.min-file-size','hive.s3.multipart.min-part-size','hive.recursive-directories']
class TrinoInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name='trino',version=version,extract_single_directory=True)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin','launcher')
	def _get_download_url(A):return URL_PATTERN_TRINO.replace('<version>',A.version)
	def _prepare_installation(D,target):A=target;from localstack.packages.java import java_package as B;from localstack.pro.core.packages.spark import spark_common_driver_package as C;C.install(target=A);B.install(version='11',target=A)
	def _post_process(A,target):B=target;A._write_trino_jvm_config();A._write_trino_config_properties();A._download_iceberg_jar(target=B);A._apply_cve_fixes(target=B)
	def _write_trino_jvm_config(C):
		B='jvm.config';A=C.get_trino_etc_dir()
		if not os.path.exists(os.path.join(A,B)):save_file(os.path.join(A,B),TRINO_JVM_CONFIG)
	def _write_trino_config_properties(B):
		A=B.get_trino_etc_dir()
		if not os.path.exists(os.path.join(A,_A)):save_file(os.path.join(A,_A),TRINO_CONFIG_PROPS)
	def _download_iceberg_jar(B,target):
		from localstack.pro.core.packages.hive import ICEBERG_JAR_URL as C;from localstack.pro.core.packages.spark import spark_common_driver_package as D;E=B.get_trino_lib_dir();F=D.get_installed_dir();G=bigdata_jar_cache_dir(target=target);H=download_and_cache_jar_file(jar_url=C,cache_dir=G,target_dir=F);A=os.path.join(E,'iceberg.jar')
		if not os.path.exists(A):cp_r(H,A)
	def get_trino_lib_dir(B):
		A=B.get_installed_dir()
		if not A:return
		return os.path.join(A,'lib')
	def get_trino_etc_dir(B):
		A=B.get_installed_dir()
		if not A:return
		return os.path.join(A,'etc')
	def write_trino_config(G,additional_configs):
		B=config.external_service_url();C=f"{LOCALHOST}:{ext_config.PORT_HIVE_METASTORE}";D=TRINO_HIVE_CONFIG.format(s3_endpoint=B,hive_host=C)
		for(E,H)in additional_configs.items():
			if E in TRINO_HIVE_CONFIGS:D+=f"\n{E}={H}"
		D+='\n';A=G.get_trino_etc_dir();I=os.path.join(A,'catalog/hive.properties');save_file(I,D);J=os.path.join(A,'catalog/iceberg.properties');K=TRINO_ICEBERG_CONFIG.format(hive_host=C,s3_endpoint=B);save_file(J,K);L=os.path.join(A,'catalog/deltalake.properties');M=TRINO_DELTALAKE_CONFIG.format(hive_host=C,s3_endpoint=B);save_file(L,M);F=os.path.join(A,_A);N=load_file(F).replace('8080',str(ext_config.PORT_TRINO_SERVER));save_file(F,N)
	def _apply_cve_fixes(B,target):A=CVEFix(paths=['trino/389/plugin/phoenix5/trino-phoenix5-patched-389.jar','trino/389/plugin/pinot/helix-core-0.9.8.jar','trino/389/plugin/accumulo/log4j-1.2.17.jar'],strategy=FixStrategyDelete());fix_cves_in_jar_files(target,fixes=[A])
	def get_java_home(B):from localstack.packages.java import java_package as A;return A.get_installer('11').get_java_home()
class TrinoPackage(Package):
	def __init__(A,default_version=TRINO_DEFAULT_VERSION):super().__init__(name='Trino',default_version=default_version)
	def get_versions(A):return TRINO_VERSIONS
	def _get_installer(A,version):return TrinoInstaller(version)
trino_package=TrinoPackage()