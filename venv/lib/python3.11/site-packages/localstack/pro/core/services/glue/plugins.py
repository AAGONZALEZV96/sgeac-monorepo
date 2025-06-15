from localstack.packages import Package
from localstack.pro.core.packages.core import pro_package
@pro_package(name='glue')
def glue_package():from.packages import glue_package as A;return A