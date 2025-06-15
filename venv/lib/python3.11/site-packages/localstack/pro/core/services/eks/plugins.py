from localstack.packages import Package
from localstack.pro.core.packages.core import pro_package
@pro_package(name='k3d')
def k3d_package():from localstack.pro.core.services.eks.packages import k3d_package as A;return A