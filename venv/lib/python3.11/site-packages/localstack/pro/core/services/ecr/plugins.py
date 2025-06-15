from localstack.packages import Package
from localstack.pro.core.packages.core import pro_package
@pro_package(name='ecr')
def registry_package():from localstack.pro.core.services.ecr.packages import registry_package as A;return A