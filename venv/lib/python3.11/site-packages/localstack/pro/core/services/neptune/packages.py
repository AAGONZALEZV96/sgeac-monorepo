_D='3.4.11'
_C='3.6.2'
_B='3.5.2'
_A='3.7.2'
import logging,os
from typing import List
import localstack.pro.core.config as config_ext
from localstack import config
from localstack.packages import DownloadInstaller,InstallTarget,Package,PackageInstaller
from localstack.packages.core import ArchiveDownloadAndExtractInstaller
from localstack.packages.java import JavaInstallerMixin
from localstack.pro.core.packages.cve_fixes import copy_entries_into_zip_file
from localstack.utils.archives import download_and_extract_with_retry
from localstack.utils.http import download
LOG=logging.getLogger(__name__)
NEO4J_JAR_URL='https://dist.neo4j.org/neo4j-community-<ver>-unix.tar.gz'
NEO4J_DEFAULT_VERSION='4.4.18'
ARTIFACTS_REPO_URL='https://github.com/localstack/localstack-artifacts/raw'
TINKERPOP_ID_MANAGER_COMMIT='d4531b134ba86f2a5603442e7e6de17d2296be32'
TINKERPOP_AUTHENTICATOR_COMMIT='7a345626381ef0bebb613de1110734bfd1574625'
TINKERPOP_PATCH_COMMIT='5ecd123bfde635c7cf40a9ea39bff1d53b0ce3ca'
TINKERPOP_ID_MANAGER_URL=f"{ARTIFACTS_REPO_URL}/{TINKERPOP_ID_MANAGER_COMMIT}/tinkerpop-id-manager/tinkerpop-id-manager{{suffix}}.jar"
TINKERPOP_ID_MANAGER_FILE_NAME='tinkerpop-id-manager.jar'
TINKERPOP_AUTHENTICATOR_URL=f"{ARTIFACTS_REPO_URL}/{TINKERPOP_AUTHENTICATOR_COMMIT}/tinkerpop-iam-authenticator/tinkerpop-iam-authenticator-37.jar"
TINKERPOP_AUTHENTICATOR_FILE_NAME='tinkerpop-iam-authenticator.jar'
TINKERPOP_PATCH_URL=f"{ARTIFACTS_REPO_URL}/{TINKERPOP_PATCH_COMMIT}/neptune-tinkerpop/gremlin-core-{{version}}-patches.zip"
TINKERPOP_PATCHED_VERSIONS=[_D,_B,_C,'3.6.5','3.7.1',_A]
GREMLIN_SERVER_URL_TEMPLATE='https://archive.apache.org/dist/tinkerpop/{version}/apache-tinkerpop-gremlin-server-{version}-bin.zip'
TINKERPOP_DEFAULT_VERSION=_A
NEPTUNE_TRANSACTION_VERSION=_A
TINKERPOP_VERSION_SUPPORT_NEPTUNE={'1.1.0.0':_D,'1.1.1.0':_B,'1.2.0.0':_B,'1.2.0.1':_B,'1.2.0.2':_B,'1.2.1.0':_C,'1.2.1.1':_C,'1.3.0.0':_C,'1.3.1.0':'3.6.5','1.3.2.0':_A,'1.3.2.1':_A,'1.3.4.0':_A,'1.4.0.0':_A,'1.4.1.0':_A,'1.4.2.0':_A,'1.4.3.0':_A}
def get_gremlin_version_for_neptune_db_version(neptune_version):
	A=TINKERPOP_VERSION_SUPPORT_NEPTUNE.get(neptune_version,TINKERPOP_DEFAULT_VERSION)
	if config_ext.NEPTUNE_ENABLE_TRANSACTION and A<NEPTUNE_TRANSACTION_VERSION:LOG.warning("NEPTUNE_ENABLE_TRANSACTION flag is set. Ignoring 'engine-version' for version '%s' and installing: '%s'",A,NEPTUNE_TRANSACTION_VERSION);return NEPTUNE_TRANSACTION_VERSION
	return A
class Neo4JPackage(Package):
	def __init__(A):super().__init__('Neo4J',NEO4J_DEFAULT_VERSION)
	def get_versions(A):return[NEO4J_DEFAULT_VERSION]
	def _get_installer(A,version):return Neo4JPackageInstaller('neo4j',version)
class Neo4JPackageInstaller(JavaInstallerMixin,ArchiveDownloadAndExtractInstaller):
	def _get_download_url(A):return NEO4J_JAR_URL.replace('<ver>',A.version)
	def _get_archive_subdir(A):return f"neo4j-community-{A.version}"
	def _get_install_marker_path(A,install_dir):return os.path.join(install_dir,f"neo4j-community-{A.version}",'bin','neo4j')
class TinkerpopPackage(Package):
	def __init__(A):super().__init__('Tinkerpop',TINKERPOP_DEFAULT_VERSION)
	def get_versions(A):
		if config_ext.NEPTUNE_ENABLE_TRANSACTION:return list(set(list(TINKERPOP_VERSION_SUPPORT_NEPTUNE.values())+[NEPTUNE_TRANSACTION_VERSION]))
		return list(TINKERPOP_VERSION_SUPPORT_NEPTUNE.values())
	def _get_installer(A,version):return TinkerpopPackageInstaller('tinkerpop',version)
class TinkerpopPackageInstaller(JavaInstallerMixin,DownloadInstaller):
	def _get_download_url(A):return GREMLIN_SERVER_URL_TEMPLATE.format(version=A.version)
	def _get_id_manager_url(A):
		if A.version.startswith('3.7'):return TINKERPOP_ID_MANAGER_URL.format(suffix='-37')
		return TINKERPOP_ID_MANAGER_URL.format(suffix='')
	def _get_patch_url(A):
		if A.version not in TINKERPOP_PATCHED_VERSIONS:return
		return TINKERPOP_PATCH_URL.format(version=A.version)
	def _install(A,target):
		B=target;C=A._get_install_dir(B);F=A._get_install_marker_path(C);D=os.path.join(A._get_install_dir(B),TINKERPOP_ID_MANAGER_FILE_NAME)
		if not os.path.exists(D):download(A._get_id_manager_url(),D)
		E=os.path.join(A._get_install_dir(B),TINKERPOP_AUTHENTICATOR_FILE_NAME)
		if not os.path.exists(E):download(TINKERPOP_AUTHENTICATOR_URL,E)
		if not os.path.exists(F):LOG.debug('Downloading dependencies for Neptune Graph DB API (this may take some time) ...');G=os.path.join(C,'neptunedb.zip');download_and_extract_with_retry(A._get_download_url(),G,C)
	def _get_install_marker_path(A,install_dir):return os.path.join(A._get_install_path(install_dir),'bin','gremlin-server.sh')
	def _get_install_path(A,install_dir):return os.path.join(install_dir,f"apache-tinkerpop-gremlin-server-{A.version}")
	def _post_process(A,target):
		if not(C:=A._get_patch_url()):LOG.info('Note: patch for multi-label vertices not yet available for Tinkerpop version %s',A.version);return
		B=os.path.join(config.dirs.tmp,f"neptune-tinkerpop-{A.version}-patches.jar");download(C,B);D=A._get_install_dir(target);E=A._get_install_path(D);F=os.path.join(E,'lib',f"gremlin-core-{A.version}.jar");copy_entries_into_zip_file(source_zip_file=B,target_zip_file=F)
neo4j_package=Neo4JPackage()
tinkerpop_package=TinkerpopPackage()