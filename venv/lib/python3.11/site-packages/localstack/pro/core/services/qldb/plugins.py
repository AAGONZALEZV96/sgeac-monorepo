from localstack.packages import Package
from localstack.pro.core.packages.core import pro_package
@pro_package(name='qldb')
def partiql_package():from localstack.pro.core.services.qldb.packages import partiql_package as A;return A