from typing import List
from localstack.packages import Package,PackageInstaller
from localstack.packages.core import PythonPackageInstaller
_PYARROW_DEFAULT_VERSION='14.0.2'
class PyArrowPackage(Package):
	def __init__(A,default_version=_PYARROW_DEFAULT_VERSION):super().__init__(name='PyArrow',default_version=default_version)
	def _get_installer(A,version):return PyArrowPackageInstaller(version)
	def get_versions(A):return[_PYARROW_DEFAULT_VERSION]
class PyArrowPackageInstaller(PythonPackageInstaller):
	def __init__(A,version):super().__init__('pyarrow',version)
pyarrow_package=PyArrowPackage()