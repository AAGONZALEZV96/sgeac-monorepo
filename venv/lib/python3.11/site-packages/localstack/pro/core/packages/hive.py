_A='2.3.9'
import glob,logging,os,shutil
from html import escape
from typing import List
from xml.etree.ElementTree import Element,SubElement,tostring
from localstack import config
from localstack.constants import DEFAULT_AWS_ACCOUNT_ID,MAVEN_REPO_URL
from localstack.packages import InstallTarget,Package
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.pro.core import config as ext_config
from localstack.pro.core.packages.cve_fixes import HTRACE_NOOP_JAR_URL,CVEFix,FixStrategyDelete,FixStrategyDownloadFile,fix_cves_in_jar_files
from localstack.utils.files import file_exists_not_empty,mkdir,save_file
from localstack.utils.http import download
from localstack.utils.strings import short_uid
LOG=logging.getLogger(__name__)
HIVE_REMOVE_JAR_FILES=['hive-jdbc-handler-*.jar']
ICEBERG_JAR_URL=f"{MAVEN_REPO_URL}/org/apache/iceberg/iceberg-hive-runtime/1.6.0/iceberg-hive-runtime-1.6.0.jar"
delta_core_version='0.6.0'
delta_core_scala_version='2.11'
HIVE_JAR_FILES=[f"{MAVEN_REPO_URL}/org/postgresql/postgresql/42.5.0/postgresql-42.5.0.jar",f"{MAVEN_REPO_URL}/org/apache/hive/hive-jdbc-handler/3.1.3/hive-jdbc-handler-3.1.3.jar",f"{MAVEN_REPO_URL}/com/amazon/redshift/redshift-jdbc42/2.1.0.23/redshift-jdbc42-2.1.0.23.jar",f"{MAVEN_REPO_URL}/io/delta/delta-core_{delta_core_scala_version}/{delta_core_version}/delta-core_{delta_core_scala_version}-{delta_core_version}.jar",f"{MAVEN_REPO_URL}/io/delta/delta-hive_{delta_core_scala_version}/{delta_core_version}/delta-hive_{delta_core_scala_version}-{delta_core_version}.jar",f"{MAVEN_REPO_URL}/io/delta/delta-standalone_{delta_core_scala_version}/{delta_core_version}/delta-standalone_{delta_core_scala_version}-{delta_core_version}.jar",f"{MAVEN_REPO_URL}/io/delta/delta-storage/2.2.0/delta-storage-2.2.0.jar",f"{MAVEN_REPO_URL}/com/chuusai/shapeless_2.11/2.3.10/shapeless_2.11-2.3.10.jar",f"{MAVEN_REPO_URL}/org/apache/tez/tez-api/0.10.2/tez-api-0.10.2.jar",f"{MAVEN_REPO_URL}/org/apache/tez/tez-dag/0.10.2/tez-dag-0.10.2.jar",ICEBERG_JAR_URL]
HIVE_DL_URLS={_A:'https://archive.apache.org/dist/hive/hive-2.3.9/apache-hive-2.3.9-bin.tar.gz','3.1.3':'https://archive.apache.org/dist/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz'}
HIVE_DEFAULT_VERSION=os.getenv('HIVE_DEFAULT_VERSION','').strip()or _A
HIVE_VERSIONS=[_A,'3.1.3']
SERDES_USING_METASTORE=['org.apache.hadoop.hive.ql.io.orc.OrcSerde','org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe','org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe','org.apache.hadoop.hive.serde2.dynamic_type.DynamicSerDe','org.apache.hadoop.hive.serde2.MetadataTypedColumnsetSerDe','org.apache.hadoop.hive.serde2.columnar.LazyBinaryColumnarSerDe','org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe','org.apache.hadoop.hive.serde2.lazybinary.LazyBinarySerDe','org.apache.hadoop.hive.serde2.OpenCSVSerde']
class HiveInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name='hive',version=version,extract_single_directory=True)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin','hiveserver2')
	def _get_download_url(A):return HIVE_DL_URLS.get(A.version)
	def _prepare_installation(E,target):A=target;from localstack.packages.java import java_package as B;from localstack.pro.core.packages.hadoop import hadoop_package as C;from localstack.pro.core.packages.spark import spark_package as D;B.install(version='8',target=A);D.install(target=A);C.install(target=A)
	def _post_process(A,target):A._download_additional_hive_libs();A._fix_guava_incompatibility();A._remove_debug_script();A._apply_cve_fixes(target)
	def _download_additional_hive_libs(G):
		from localstack.pro.core.packages.hadoop import hadoop_package as H;A=G.get_hive_lib_dir();I=H.get_installer().get_hadoop_tool_lib_dir();J=['hadoop-aws-*.jar','aws-java-sdk-bundle-*.jar']
		for B in J:
			for C in glob.glob(f"{I}/{B}"):
				D=os.path.join(A,os.path.basename(C))
				if not os.path.exists(D):shutil.copy(C,D)
		for K in HIVE_REMOVE_JAR_FILES:
			B=f"{A}/{K}"
			for L in glob.glob(B):os.remove(L)
		for E in HIVE_JAR_FILES:
			F=os.path.join(A,E.rpartition('/')[2])
			if not file_exists_not_empty(F):download(E,F)
	def _fix_guava_incompatibility(B):
		from localstack.pro.core.packages.hadoop import hadoop_package as C;D=B.get_hive_lib_dir();E=C.get_installer().get_hadoop_home();A=glob.glob(os.path.join(E,'share/hadoop/hdfs/lib/guava-*-jre.jar'))
		if B.version.startswith('3.')and A:F=os.path.join(D,f"_{os.path.basename(A[0])}");os.symlink(A[0],F)
	def _remove_debug_script(B):
		C=B.get_hive_home();A=os.path.join(C,'bin/ext/debug.sh')
		if os.path.exists(A):os.remove(A)
	def write_hive_config(C,additional_configs):
		G='false';A='true';B=config.external_service_url();H=','.join(SERDES_USING_METASTORE);I=C.get_hive_warehouse_dir();D={'hive.server2.thrift.bind.host':'0.0.0.0','hive.server2.transport.mode':'binary','hive.server2.thrift.port':str(ext_config.PORT_HIVE_SERVER),'hive.metastore.uris':f"thrift://localhost:{str(ext_config.PORT_HIVE_METASTORE)}",'hive.metastore.warehouse.dir':I,'hive.server2.enable.doAs':G,'hive.server2.authentication':'NOSASL','mapred.input.dir.recursive':A,'hive.mapred.supports.subdirectories':A,'hive.supports.subdirectories':A,'hive.input.dir.recursive':A,'hive.serdes.using.metastore.for.schema':H,'hive.metastore.event.db.notification.api.auth':G,'fs.s3.awsAccessKeyId':DEFAULT_AWS_ACCOUNT_ID,'fs.s3.awsSecretAccessKey':DEFAULT_AWS_ACCOUNT_ID,'fs.s3.endpoint':B,'fs.s3.path.style.access':A,'fs.s3a.awsAccessKeyId':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.awsSecretAccessKey':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.access.key':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.secret.key':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.endpoint':B,'fs.s3a.path.style.access':A,'fs.s3n.awsAccessKeyId':DEFAULT_AWS_ACCOUNT_ID,'fs.s3n.awsSecretAccessKey':DEFAULT_AWS_ACCOUNT_ID,'fs.s3n.endpoint':B,'fs.s3n.path.style.access':A};D.update(additional_configs);E=Element('configuration')
		for(J,K)in D.items():F=SubElement(E,'property');SubElement(F,'name').text=escape(J);SubElement(F,'value').text=escape(K)
		L=C.get_hive_site_xml_path();save_file(L,tostring(E))
	def _apply_cve_fixes(D,target):A=target;B=CVEFix(paths=['hive/2.3.9/lib/avatica-1.8.0.jar'],strategy=FixStrategyDelete());C=CVEFix(paths=['hive/2.3.9/lib/htrace-core-3.1.0-incubating.jar','hive/3.1.3/lib/avatica-1.11.0.jar','hive/3.1.3/lib/htrace-core-3.2.0-incubating.jar'],strategy=[FixStrategyDownloadFile(file_url=f"{MAVEN_REPO_URL}/org/apache/calcite/avatica/avatica-core/1.23.0/avatica-core-1.23.0.jar",target_path=os.path.join(A.value,'hive/3.1.3/lib')),FixStrategyDelete(),FixStrategyDownloadFile(file_url=HTRACE_NOOP_JAR_URL,target_path=os.path.join(A.value,'hadoop/3.3.1/share/hadoop/common'))]);fix_cves_in_jar_files(A,fixes=[B,C])
	def get_hive_home(A):return A.get_installed_dir()
	def get_hive_lib_dir(B):
		A=B.get_hive_home()
		if A:return os.path.join(A,'lib')
	def get_hive_bin_dir(B):
		A=B.get_hive_home()
		if A:return os.path.join(A,'bin')
	def get_hive_conf_dir(B):
		A=B.get_hive_home()
		if A:return os.path.join(A,'conf')
	def get_hive_site_xml_path(B):
		A=B.get_hive_conf_dir()
		if A:return os.path.join(A,'hive-site.xml')
	def get_hive_warehouse_dir(C):
		if config.PERSISTENCE:A=config.dirs.data
		else:A=os.path.join(config.TMP_FOLDER,f"hive-{short_uid()}")
		B=os.path.join(A,f"hive-{C.version}",'hive-warehouse');mkdir(B);return B
	def get_hadoop_home(B):from localstack.pro.core.packages.hadoop import hadoop_package as A;return A.get_installer().get_hadoop_home()
	def get_java_home(C):from localstack.packages.java import java_package as B;A=B.get_installer('8');A.install();return A.get_java_home()
class HivePackage(Package):
	def __init__(A,default_version=HIVE_DEFAULT_VERSION):super().__init__(name='Hive',default_version=default_version)
	def get_versions(A):return HIVE_VERSIONS
	def _get_installer(A,version):return HiveInstaller(version)
hive_package=HivePackage()