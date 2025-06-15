from localstack.packages import Package
from localstack.pro.core.packages.core import pro_package
@pro_package(name='mysql')
def mariadb_package():from.mariadb import mariadb_package as A;return A
@pro_package(name='postgres')
def postgres_package():from.postgres import postgresql_package as A;return A
@pro_package(name='trino')
def trino_package():from.trino import trino_package as A;return A
@pro_package(name='hadoop')
def hadoop_package():from.hadoop import hadoop_package as A;return A
@pro_package(name='hive')
def hive_package():from.hive import hive_package as A;return A
@pro_package(name='spark')
def spark_package():from.spark import spark_package as A;return A