from localstack.packages import Package
from localstack.pro.core.packages.core import pro_package
@pro_package(name='pysiddhi')
def pysiddhi_package():from localstack.pro.core.services.kinesisanalytics.packages import siddhi_package as A;return A