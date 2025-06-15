_A='hadoop'
import glob,os
from typing import List
from xml.etree.ElementTree import Element,SubElement,tostring
from localstack import config
from localstack.constants import DEFAULT_AWS_ACCOUNT_ID,MAVEN_REPO_URL
from localstack.packages import InstallTarget,Package
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.pro.core.packages.bigdata_common import bigdata_jar_cache_dir,download_and_cache_jar_file
from localstack.pro.core.packages.cve_fixes import HTRACE_NOOP_JAR_URL,CVEFix,FixStrategyDelete,FixStrategyDownloadFile,fix_cves_in_jar_files
from localstack.pro.core.packages.spark import AWS_SDK_VER
from localstack.utils.files import rm_rf,save_file
URL_PATTERN_HADOOP='https://archive.apache.org/dist/hadoop/common/hadoop-{version}/hadoop-{version}.tar.gz'
AWS_SDK_BUNDLE_JAR=f"aws-java-sdk-bundle-{AWS_SDK_VER}.jar"
AWS_SDK_BUNDLE_JAR_URL=f"{MAVEN_REPO_URL}/com/amazonaws/aws-java-sdk-bundle/{AWS_SDK_VER}/{AWS_SDK_BUNDLE_JAR}"
HADOOP_DEFAULT_VERSION='3.3.1'
HADOOP_VERSIONS=['2.10.2','3.3.1','3.4.0']
class HadoopInstaller(ArchiveDownloadAndExtractInstaller):
	def __init__(A,version):super().__init__(name=_A,version=version,extract_single_directory=True)
	def _post_process(A,target):B=target;A._write_hadoop_config(B);A._replace_aws_sdk(B);A._apply_cve_fixes(B)
	def _get_download_url(A):return URL_PATTERN_HADOOP.format(version=A.version)
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,'bin',_A)
	def get_hadoop_home(A):return A.get_installed_dir()
	def get_hadoop_bin(A):B=A.get_hadoop_home();return A._get_install_marker_path(B)if B else None
	def get_hadoop_bin_dir(B):A=B.get_hadoop_home();return os.path.join(A,'bin')if A else None
	def get_hadoop_tool_lib_dir(B):A=B.get_hadoop_home();return os.path.join(A,'share',_A,'tools','lib')if A else None
	def _write_hadoop_config(E,target):
		B='true';A=config.external_service_url();F={'fs.s3.awsAccessKeyId':DEFAULT_AWS_ACCOUNT_ID,'fs.s3.awsSecretAccessKey':DEFAULT_AWS_ACCOUNT_ID,'fs.s3.endpoint':A,'fs.s3.path.style.access':B,'fs.s3a.awsAccessKeyId':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.awsSecretAccessKey':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.access.key':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.secret.key':DEFAULT_AWS_ACCOUNT_ID,'fs.s3a.endpoint':A,'fs.s3a.path.style.access':B,'fs.s3n.awsAccessKeyId':DEFAULT_AWS_ACCOUNT_ID,'fs.s3n.awsSecretAccessKey':DEFAULT_AWS_ACCOUNT_ID,'fs.s3n.endpoint':A,'fs.s3n.path.style.access':B,'fs.defaultFS':f"file://{config.TMP_FOLDER}/hadoop-fs",'fs.default.name':f"file://{config.TMP_FOLDER}/hadoop-fs"};C=Element('configuration')
		for(G,H)in F.items():D=SubElement(C,'property');SubElement(D,'name').text=G;SubElement(D,'value').text=H
		I=os.path.join(E._get_install_dir(target),'etc/hadoop/core-site.xml');save_file(I,tostring(C))
	def _replace_aws_sdk(C,target):
		A=C.get_hadoop_tool_lib_dir();B=glob.glob(os.path.join(A,'aws-java-sdk-*.jar'))
		for D in B:rm_rf(D)
		if B:E=bigdata_jar_cache_dir(target);download_and_cache_jar_file(AWS_SDK_BUNDLE_JAR_URL,E,A)
	def _apply_cve_fixes(E,target):A=target;B=CVEFix(paths=['hadoop/3.3.1/share/hadoop/common/lib/htrace-core4-4.1.0-incubating.jar','hadoop/3.3.1/share/hadoop/hdfs/lib/htrace-core4-4.1.0-incubating.jar','hadoop/3.3.1/share/hadoop/yarn/hadoop-yarn-applications-catalog-webapp-3.3.1.war:WEB-INF/lib/htrace-core4-4.1.0-incubating.jar','hadoop/3.3.1/share/hadoop/yarn/timelineservice/lib/htrace-core-3.1.0-incubating.jar'],strategy=FixStrategyDelete());C=CVEFix(paths=['hadoop/3.3.1/share/hadoop/client/hadoop-client-api-3.3.1.jar'],strategy=FixStrategyDownloadFile(file_url=HTRACE_NOOP_JAR_URL,target_path=os.path.join(A.value,'hadoop/3.3.1/share/hadoop/common')));D=CVEFix(paths=['hadoop/3.3.1/share/hadoop/hdfs/lib/log4j-1.2.17.jar','hadoop/3.3.1/share/hadoop/common/lib/log4j-1.2.17.jar','hadoop/3.3.1/share/hadoop/common/lib/slf4j-log4j12-1.7.30.jar'],strategy=FixStrategyDelete());fix_cves_in_jar_files(A,fixes=[B,C,D])
class HadoopPackage(Package):
	def __init__(A,default_version=HADOOP_DEFAULT_VERSION):super().__init__(name='Hadoop',default_version=default_version)
	def get_versions(A):return HADOOP_VERSIONS
	def _get_installer(A,version):return HadoopInstaller(version)
hadoop_package=HadoopPackage()