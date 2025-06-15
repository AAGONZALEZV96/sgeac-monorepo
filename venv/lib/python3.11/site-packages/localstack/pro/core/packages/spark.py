_E='spark-drivers'
_D='pkg:maven/org.apache.logging.log4j/log4j-api@2.17.2'
_C='pkg:maven/de.undercouch/bson4jackson@2.13.1'
_B='common'
_A='3.5.2'
import glob,logging,os,re,textwrap
from typing import List
from localstack.packages import InstallTarget,Package,PackageInstaller
from localstack.packages.core import ArchiveDownloadAndExtractInstaller,MavenDownloadInstaller
from localstack.packages.java import java_package
from localstack.pro.core.packages.bigdata_common import replace_in_file,replace_in_zip_file
from localstack.utils.files import chmod_r,save_file
LOG=logging.getLogger(__name__)
SPARK_URL='https://archive.apache.org/dist/spark/spark-{version}/spark-{version}-bin-without-hadoop.tgz'
DEFAULT_SPARK_VERSION=os.getenv('SPARK_DEFAULT_VERSION','').strip()or'2.4.3'
SPARK_VERSIONS=['2.2.1','2.4.3','2.4.8','3.1.1','3.1.2','3.3.0',_A]
AWS_SDK_VER='1.12.339'
SPARK_JAR_URLS={_B:['pkg:maven/com.typesafe/config@1.3.3','pkg:maven/com.github.tony19/named-regexp@0.2.6','pkg:maven/com.amazon.emr/emr-dynamodb-hadoop@4.12.0','pkg:maven/com.google.guava/guava@30.0-jre','pkg.maven/commons-configuration/commons-configuration@1.10','pkg.maven/org.apache.commons/commons-text@1.9','pkg:maven/commons-lang/commons-lang@2.6','pkg:maven/org.postgresql/postgresql@42.3.1','pkg:maven/com.google.guava/failureaccess@1.0.1','pkg:maven/org.apache.hadoop.thirdparty/hadoop-shaded-protobuf_3_7@1.0.0','pkg:maven/com.google.re2j/re2j@1.5','pkg:maven/org.apache.logging.log4j/log4j-api@2.22.1','pkg:maven/org.apache.logging.log4j/log4j-core@2.22.1','pkg:maven/org.apache.logging.log4j/log4j-1.2-api@2.22.1','pkg:maven/org.apache.logging.log4j/log4j-slf4j-impl@2.22.1',f"pkg:maven/com.amazonaws/aws-java-sdk-bundle@{AWS_SDK_VER}",'pkg:maven/net.snowflake/snowflake-jdbc@3.20.0','pkg:maven/net.snowflake/spark-snowflake_2.12@2.12.0-spark_3.3'],'all':['pkg:maven/org.apache.hadoop/hadoop-hdfs@<hadoop_version>','pkg:maven/org.apache.hadoop/hadoop-common@<hadoop_version>','pkg:maven/org.apache.hadoop/hadoop-auth@<hadoop_version>','pkg:maven/org.apache.hadoop/hadoop-aws@<hadoop_version>'],'(2\\..+)|(3\\.1\\.\\d)':['pkg:maven/com.fasterxml.jackson.dataformat/jackson-dataformat-csv@2.11.4','pkg:maven/com.fasterxml.jackson.core/jackson-core@2.11.4','pkg:maven/de.undercouch/bson4jackson@2.11.0','pkg:maven/org.apache.logging.log4j/log4j-api@2.14.0'],'3\\.3\\.0':['pkg:maven/com.fasterxml.jackson.dataformat/jackson-dataformat-csv@2.13.3','pkg:maven/com.fasterxml.jackson.core/jackson-core@2.13.3',_C,_D],'3\\.5\\.2':['pkg:maven/com.fasterxml.jackson.dataformat/jackson-dataformat-csv@2.12.6','pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.15.2','pkg:maven/com.fasterxml.jackson.core/jackson-core@2.15.2','pkg:maven/com.fasterxml.jackson.module/jackson-module-scala_3@2.15.2',_C,_D]}
class SparkDriverInstallerBase(PackageInstaller):
	def __init__(B,name,version,jars):A=version;super().__init__(name,A);B.dependencies=[MavenDownloadInstaller(B,os.path.join(name,f"spark-{A}"))for B in jars]
	def _get_install_dir(A,target):return os.path.join(target.value,A.name,f"spark-{A.version}")
	def _get_install_marker_path(A,install_dir):return A.dependencies[-1]._get_install_marker_path(install_dir)
	def _install(A,target):
		for B in A.dependencies:B.install(target=target)
class SparkCommonDriverInstaller(SparkDriverInstallerBase):
	def __init__(B,version):A=SPARK_JAR_URLS.get(_B,[]).copy();super().__init__(_E,version,A)
class SparkVersionSpecificDriverInstaller(SparkDriverInstallerBase):
	def __init__(D,version):B=version;A=SPARK_JAR_URLS.get('all',[]).copy();A.extend(D for(A,C)in SPARK_JAR_URLS.items()if re.match(A,B)for D in C);C=SparkInstaller.get_hadoop_version_for_spark(B);A=[A.replace('<hadoop_version>',C)for A in A];super().__init__(_E,B,A)
class SparkCommonDriverPackage(Package):
	def __init__(A):super().__init__('SparkCommonDriver',default_version=_B)
	def get_versions(A):return[_B]
	def _get_installer(A,version):return SparkCommonDriverInstaller(version)
class SparkVersionSpecificDriverPackage(Package):
	def __init__(A):super().__init__('SparkVersionSpecificDriver',default_version=DEFAULT_SPARK_VERSION)
	def get_versions(A):return SPARK_VERSIONS
	def _get_installer(A,version):return SparkVersionSpecificDriverInstaller(version)
class SparkPackage(Package):
	def __init__(A):super().__init__('Spark',default_version=DEFAULT_SPARK_VERSION)
	def get_versions(A):return SPARK_VERSIONS
	def _get_installer(A,version):return SparkInstaller(version)
class SparkInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name='spark',version=version,extract_single_directory=True)
	def _get_download_url(A):return SPARK_URL.format(version=A.version)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin','spark-submit')
	def _prepare_installation(A,target):B=target;A._install_java(B);A._install_hadoop(B);A._install_spark_drivers(B)
	def _post_process(A,target):B=target;A._patch_spark_hadoop_env_config(B);A._patch_spark_class(B);A._patch_spark_defaults_config_file(B);A._patch_spark_python_dependencies(B)
	@staticmethod
	def get_hadoop_version_for_spark(spark_version):from localstack.pro.core.packages.hadoop import HADOOP_DEFAULT_VERSION as A;B={'2.2.1':'2.10.2',_A:'3.4.0'};return B.get(spark_version,A)
	def _install_spark_drivers(B,target):A=target;spark_common_driver_package.install(target=A);spark_version_specific_driver_package.install(version=B.version,target=A)
	def _patch_spark_class(B,target):C=B._get_install_dir(target);A=os.path.join(C,'bin','spark-class');D=textwrap.dedent('\n        if [ -n "$SPARK_OVERWRITE_CP" ]; then CMD[2]="$SPARK_OVERWRITE_CP:${CMD[2]}"; fi\n        CMD=("${CMD[0]}" "-Dcom.amazonaws.sdk.disableCertChecking=true" "${CMD[@]:1}"); exec "${CMD[@]}"\n        ');E={'exec "${CMD[@]}"':D};replace_in_file(A,E);chmod_r(A,511)
	def _patch_spark_defaults_config_file(B,target):D=B._get_install_dir(target);A=spark_common_driver_package.get_installed_dir();C=spark_version_specific_driver_package.get_installed_dir(B.version);E=os.path.join(D,'conf','spark-defaults.conf');F=textwrap.dedent(f"\n            spark.driver.extraClassPath {A}:{A}/*:{C}/*\n            spark.executor.extraClassPath {A}:{A}/*:{C}/*\n            spark.driver.allowMultipleContexts = true\n        ");save_file(E,F)
	def _patch_spark_hadoop_env_config(A,target):from localstack.pro.core.packages.hadoop import hadoop_package as C;D=A.get_hadoop_version_for_spark(A.version);B=C.get_installer(D);E=B.get_hadoop_home();F=B.get_hadoop_bin();G=A._get_install_dir(target);H=textwrap.dedent(f'\n                    export SPARK_DIST_CLASSPATH="$({F} classpath)"\n                    export HADOOP_CONF_DIR="{E}/etc/hadoop"\n                ');save_file(f"{G}/conf/spark-env.sh",H)
	def _patch_spark_python_dependencies(F,target):E='co.co_freevars, co.co_cellvars, ';C=F._get_install_dir(target);A=os.path.join(C,'python/lib/py4j-*-src.zip');A=glob.glob(A)[0];B={'from collections import':'from collections.abc import'};replace_in_zip_file(A,'py4j/java_collections.py',B);A=os.path.join(C,'python/lib/pyspark.zip');B={'import collections\n':'import collections.abc\n','collections.Iterable':'collections.abc.Iterable'};replace_in_zip_file(A,'pyspark/resultiterable.py',B);D=textwrap.dedent('\n        def _walk_global_ops_patched(code):\n            for instr in dis.get_instructions(code):\n                op = instr.opcode\n                if op in GLOBAL_OPS:\n                    yield instr.argval\n        out_names = {name for name in _walk_global_ops_patched(co)}\n        ');B={'obj.co_argcount, obj.co_kwonlyargcount':'obj.co_argcount, obj.co_posonlyargcount, obj.co_kwonlyargcount','co.co_argcount,\n        ':'co.co_argcount, co.co_posonlyargcount, ','obj.co_name, obj.co_firstlineno, ':'obj.co_name, obj.co_qualname, obj.co_firstlineno, ','co.co_name,\n        ':'co.co_name, co.co_qualname, ','obj.co_name,\n        ':'obj.co_name, obj.co_qualname, ',', obj.co_lnotab, obj.co_freevars,':', obj.co_lnotab, obj.co_exceptiontable, obj.co_freevars,','co.co_lnotab,\n        ':'co.co_lnotab, co.co_exceptiontable, ','obj.co_linetable, obj.co_freevars':'obj.co_linetable, obj.co_exceptiontable, obj.co_freevars','co.co_cellvars,  # this is the trickery\n            (),':E,'co.co_cellvars,  # co_freevars is initialized with co_cellvars\n        (),':E,'oparg in _walk_global_ops(co))':'oparg in _walk_global_ops(co) if len(names) > oparg)\n'+textwrap.indent(D,' '*16),'oparg in _walk_global_ops(co)}':'oparg in _walk_global_ops(co) if len(names) > oparg}\n'+textwrap.indent(D,' '*8),'def cell_set(cell, value):\n    """':'def cell_set(cell, value):\n    cell.cell_contents = value; return\n    """'};replace_in_zip_file(A,'pyspark/cloudpickle.py',B);replace_in_zip_file(A,'pyspark/cloudpickle/cloudpickle.py',B);replace_in_zip_file(A,'pyspark/cloudpickle/cloudpickle_fast.py',B)
	def _install_hadoop(A,target):from localstack.pro.core.packages.hadoop import hadoop_package as B;C=A.get_hadoop_version_for_spark(A.version);B.install(version=C,target=target)
	def _install_java(A,target):from localstack.packages.java import java_package as B;C='17'if A.version==_A else'8';B.install(version=C,target=target)
	def add_java_home_for_spark_version(B,spark_version=None,env_vars={}):A=env_vars;C=spark_version or B.version;D='17'if C==_A else'8';E=java_package.get_installer(D);A['JAVA_HOME']=E.get_java_home();return A
	def get_spark_home(A):return A.get_installed_dir()
spark_package=SparkPackage()
spark_common_driver_package=SparkCommonDriverPackage()
spark_version_specific_driver_package=SparkVersionSpecificDriverPackage()