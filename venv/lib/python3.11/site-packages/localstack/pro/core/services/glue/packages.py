_G='jarsv1'
_F='3.0'
_E='1.0'
_D='4.0'
_C='0.9'
_B='2.0'
_A='5.0'
import glob,logging,os,re,shutil,textwrap
from typing import List
from localstack import config
from localstack.constants import MAVEN_REPO_URL
from localstack.packages import InstallTarget
from localstack.packages.api import Package
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.pro.core.constants import S3_ASSETS_BUCKET_URL
from localstack.pro.core.packages.bigdata_common import bigdata_jar_cache_dir,download_and_cache_jar_file
from localstack.pro.core.packages.cve_fixes import CVEFix,FixStrategyDelete,fix_cves_in_jar_files
from localstack.pro.core.packages.spark import DEFAULT_SPARK_VERSION,SparkInstaller,spark_package
from localstack.utils.archives import download_and_extract_with_retry
from localstack.utils.files import load_file,mkdir,save_file
LOG=logging.getLogger(__name__)
DEFAULT_GLUE_VERSION=os.getenv('GLUE_DEFAULT_VERSION','').strip()or _B
GLUE_VERSIONS=[_C,_E,_B,_F,_D,_A]
GLUE_SPARK_MAPPING={_C:'2.2.1',_E:'2.4.3',_B:'2.4.3',_F:'3.1.1',_D:'3.3.0',_A:'3.5.2'}
AWS_GLUE_LIBS_URL_0_9='https://github.com/localstack/aws-glue-libs/archive/refs/heads/glue-0.9.zip'
AWS_GLUE_LIBS_URL='https://github.com/awslabs/aws-glue-libs/archive/refs/heads/<glue_version>.zip'
AWS_GLUE_JAVA_LIBS_URL=f"{S3_ASSETS_BUCKET_URL}/aws-glue-libs.zip"
POSTGRESQL_JARS_BASE_URL='https://jdbc.postgresql.org/download'
REDSHIFT_MAVEN_BASE_URL='https://redshift-maven-repository.s3.amazonaws.com/release/com/amazon'
GLUE_JARS_BASE_URL='https://aws-glue-etl-artifacts.s3.amazonaws.com/release/com/amazonaws'
GLUE_JARS={'all':[f"{GLUE_JARS_BASE_URL}/AWSGlueETL/<version>/AWSGlueETL-<version>.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueDynamicSchemaHiveFormat/1.0.0/AWSGlueDynamicSchemaHiveFormat-1.0.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueSimd4j/1.0.0/AWSGlueSimd4j-1.0.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueDynamicSchema/0.9.0/AWSGlueDynamicSchema-0.9.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueGrokFork/0.9.0/AWSGlueGrokFork-0.9.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueJdbcCommons/0.9.0/AWSGlueJdbcCommons-0.9.0.jar",f"{S3_ASSETS_BUCKET_URL}/NimbleParquet-1.0.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueLineageCommons-1.0.jar",f"{MAVEN_REPO_URL}/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.jar",f"{MAVEN_REPO_URL}/it/unimi/dsi/fastutil/8.4.4/fastutil-8.4.4.jar",f"{MAVEN_REPO_URL}/com/fasterxml/jackson/dataformat/jackson-dataformat-xml/2.12.6/jackson-dataformat-xml-2.12.6.jar",f"{MAVEN_REPO_URL}/net/sourceforge/argparse4j/argparse4j/0.7.0/argparse4j-0.7.0.jar"],_C:[f"{GLUE_JARS_BASE_URL}/AWSGlueReaders/<version>/AWSGlueReaders-<version>.jar",f"{MAVEN_REPO_URL}/joda-time/joda-time/2.9.3/joda-time-2.9.3.jar",f"{MAVEN_REPO_URL}/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar",f"{POSTGRESQL_JARS_BASE_URL}/postgresql-42.1.4.jar",f"{REDSHIFT_MAVEN_BASE_URL}/redshift/redshift-jdbc41/1.2.12.1017/redshift-jdbc41-1.2.12.1017.jar"],_E:[f"{GLUE_JARS_BASE_URL}/AWSGlueReaders/<version>/AWSGlueReaders-<version>.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueDataplane-1.0-Scala2.11.jar",f"{MAVEN_REPO_URL}/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar",f"{POSTGRESQL_JARS_BASE_URL}/postgresql-42.1.4.jar",f"{REDSHIFT_MAVEN_BASE_URL}/redshift/redshift-jdbc41/1.2.12.1017/redshift-jdbc41-1.2.12.1017.jar"],_B:[f"{GLUE_JARS_BASE_URL}/AWSGlueReaders/<version>/AWSGlueReaders-<version>.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueDataplane-1.0-Scala2.11.jar",f"{MAVEN_REPO_URL}/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar",f"{POSTGRESQL_JARS_BASE_URL}/postgresql-42.1.4.jar",f"{REDSHIFT_MAVEN_BASE_URL}/redshift/redshift-jdbc41/1.2.12.1017/redshift-jdbc41-1.2.12.1017.jar"],_F:[f"{GLUE_JARS_BASE_URL}/AWSGlueReaders/<version>/AWSGlueReaders-<version>.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueArrowVectorShader/1.0/AWSGlueArrowVectorShader-1.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueLineageCommons/1.0/AWSGlueLineageCommons-1.0.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueDataplane-1.0-Scala2.12.jar",f"{MAVEN_REPO_URL}/joda-time/joda-time/2.9.3/joda-time-2.9.3.jar",f"{MAVEN_REPO_URL}/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar",f"{MAVEN_REPO_URL}/org/apache/spark/spark-hive_2.12/3.1.1/spark-hive_2.12-3.1.1.jar",f"{MAVEN_REPO_URL}/io/delta/delta-core_2.12/1.0.1/delta-core_2.12-1.0.1.jar",f"{POSTGRESQL_JARS_BASE_URL}/postgresql-42.2.18.jar",f"{REDSHIFT_MAVEN_BASE_URL}/redshift/redshift-jdbc41/1.2.12.1017/redshift-jdbc41-1.2.12.1017.jar"],_D:[f"{GLUE_JARS_BASE_URL}/AWSGlueArrowVectorShader/1.0/AWSGlueArrowVectorShader-1.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueLineageCommons/1.0/AWSGlueLineageCommons-1.0.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueDataplane-1.0-Scala2.12.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueReaders-4.0.0.jar",f"{MAVEN_REPO_URL}/joda-time/joda-time/2.10.13/joda-time-2.10.13.jar",f"{MAVEN_REPO_URL}/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar",f"{MAVEN_REPO_URL}/org/json4s/json4s-core_2.12/3.7.0-M11/json4s-core_2.12-3.7.0-M11.jar",f"{MAVEN_REPO_URL}/org/json4s/json4s-ast_2.12/3.7.0-M11/json4s-ast_2.12-3.7.0-M11.jar",f"{MAVEN_REPO_URL}/org/json4s/json4s-scalap_2.12/3.7.0-M11/json4s-scalap_2.12-3.7.0-M11.jar",f"{MAVEN_REPO_URL}/org/json4s/json4s-jackson_2.12/3.7.0-M11/json4s-jackson_2.12-3.7.0-M11.jar",f"{MAVEN_REPO_URL}/org/apache/spark/spark-hive_2.12/3.3.0/spark-hive_2.12-3.3.0.jar",f"{MAVEN_REPO_URL}/io/delta/delta-core_2.12/2.3.0/delta-core_2.12-2.3.0.jar",f"{MAVEN_REPO_URL}/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar",f"{POSTGRESQL_JARS_BASE_URL}/postgresql-42.3.6.jar",f"{REDSHIFT_MAVEN_BASE_URL}/redshift/redshift-jdbc42/2.1.0.16/redshift-jdbc42-2.1.0.16.jar"],_A:[f"{MAVEN_REPO_URL}/com/esotericsoftware/kryo/5.6.2/kryo-5.6.2.jar",f"{MAVEN_REPO_URL}/com/google/collections/google-collections/1.0/google-collections-1.0.jar{MAVEN_REPO_URL}/io/dropwizard/metrics/metrics-core/4.2.19/metrics-core-4.2.19.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueETL/4.0.0/AWSGlueETL-4.0.0.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueReaders-4.0.0.jar",f"{S3_ASSETS_BUCKET_URL}/AWSGlueDataplane-1.0-Scala2.12.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueArrowVectorShader/1.0/AWSGlueArrowVectorShader-1.0.jar",f"{GLUE_JARS_BASE_URL}/AWSGlueLineageCommons/1.0/AWSGlueLineageCommons-1.0.jar",f"{MAVEN_REPO_URL}/aopalliance/aopalliance/1.0/aopalliance-1.0.jar"]}
AWS_JAVA_SDK_JAR='aws-java-sdk-1.11.774.jar'
class GlueInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name='aws-glue-libs',version=version,extract_single_directory=True)
	def _get_download_url(A):
		if A.version==_C:return AWS_GLUE_LIBS_URL_0_9
		B='master'if A.version in{_D,_A}else f"glue-{A.version}";return AWS_GLUE_LIBS_URL.replace('<glue_version>',B)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin','gluepyspark')
	def _prepare_installation(A,target):B=A.get_spark_version();spark_package.install(version=B,target=target)
	def _post_process(A,target):B=target;A._apply_cve_fixes(B);A._download_glue_libs_into_spark(B);A._download_aws_glue_libs_jar(B);A._patch_aws_glue_libs_config(B)
	def _download_aws_glue_libs_jar(C,target):
		D=C._get_install_dir(target);A=os.path.join(D,_G)
		if not os.path.exists(os.path.join(A,AWS_JAVA_SDK_JAR)):
			LOG.debug('Fetching additional JARs for Glue job execution (this may take some time)');mkdir(A);E=os.path.join(config.dirs.tmp,'aws-glue-libs-java.zip');B=os.path.join(config.dirs.tmp,'aws-glue-libs-java');download_and_extract_with_retry(AWS_GLUE_JAVA_LIBS_URL,E,B)
			for F in glob.glob(os.path.join(B,'*.jar')):shutil.move(F,A)
	def _patch_aws_glue_libs_config(E,target):
		A=E._get_install_dir(target);C=os.path.join(A,_G);B=os.path.join(A,'conf','spark-defaults.conf')
		if not os.path.exists(B):D=os.path.join(A,'bin','glue-setup.sh');F=re.sub('^mvn','# mvn',load_file(D),flags=re.M);save_file(D,F);G=textwrap.dedent(f"\n                spark.driver.extraClassPath {C}/*\n                spark.executor.extraClassPath {C}/*\n                spark.driver.allowMultipleContexts = true\n            ");mkdir(os.path.dirname(B));save_file(B,G)
	def _apply_cve_fixes(B,target):A=CVEFix(paths=['aws-glue-libs/jarsv1/log4j-1.2.17.jar'],strategy=FixStrategyDelete());fix_cves_in_jar_files(target,fixes=[A])
	def _download_glue_libs_into_spark(B,target):
		D=target;E=B.get_spark_version();spark_package.install(version=E,target=D);F=spark_package.get_installed_dir(version=E);G=GLUE_JARS.get('all')+GLUE_JARS.get(B.version,[]);H=os.path.join(F,'jars');A=f"{B.version}.0";A='1.0.0'if A=='2.0.0'else A
		if B.version==_A:A='4.0.0'
		for C in G:C=C.replace('<version>',A);I=bigdata_jar_cache_dir(target=D);download_and_cache_jar_file(C,I,H)
	def get_spark_version(A):return GLUE_SPARK_MAPPING.get(A.version,DEFAULT_SPARK_VERSION)
	def get_spark_home(A):B=A.get_spark_version();return spark_package.get_installed_dir(version=B)
	def get_hadoop_home(A):from localstack.pro.core.packages.hadoop import HadoopInstaller,hadoop_package as B;C=A.get_spark_version();D=SparkInstaller.get_hadoop_version_for_spark(spark_version=C);E=B.get_installer(version=D);return E.get_hadoop_home()
	def get_java_home(B):A=B.get_spark_version();return spark_package.get_installer(version=A).add_java_home_for_spark_version(spark_version=A).get('JAVA_HOME')
class GluePackage(Package):
	def __init__(A):super().__init__('Glue',default_version=DEFAULT_GLUE_VERSION)
	def get_versions(A):return GLUE_VERSIONS
	def _get_installer(A,version):return GlueInstaller(version)
glue_package=GluePackage()