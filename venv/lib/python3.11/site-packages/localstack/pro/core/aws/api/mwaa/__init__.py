from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AirflowIdentity = str
AirflowVersion = str
CeleryExecutorQueue = str
CloudWatchLogGroupArn = str
ConfigKey = str
ConfigValue = str
Double = float
EnvironmentArn = str
EnvironmentClass = str
EnvironmentName = str
ErrorCode = str
ErrorMessage = str
Hostname = str
IamIdentity = str
IamRoleArn = str
Integer = int
KmsKey = str
ListEnvironmentsInputMaxResultsInteger = int
LoggingEnabled = bool
MaxWebservers = int
MaxWorkers = int
MinWebservers = int
MinWorkers = int
NextToken = str
RelativePath = str
RestApiPath = str
S3BucketArn = str
S3ObjectVersion = str
Schedulers = int
SecurityGroupId = str
String = str
SubnetId = str
TagKey = str
TagValue = str
Token = str
UpdateSource = str
VpcEndpointServiceName = str
WebserverUrl = str
WeeklyMaintenanceWindowStart = str


class EndpointManagement(StrEnum):
    CUSTOMER = "CUSTOMER"
    SERVICE = "SERVICE"


class EnvironmentStatus(StrEnum):
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    UNAVAILABLE = "UNAVAILABLE"
    UPDATE_FAILED = "UPDATE_FAILED"
    ROLLING_BACK = "ROLLING_BACK"
    CREATING_SNAPSHOT = "CREATING_SNAPSHOT"
    PENDING = "PENDING"
    MAINTENANCE = "MAINTENANCE"


class LoggingLevel(StrEnum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"


class RestApiMethod(StrEnum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class Unit(StrEnum):
    Seconds = "Seconds"
    Microseconds = "Microseconds"
    Milliseconds = "Milliseconds"
    Bytes = "Bytes"
    Kilobytes = "Kilobytes"
    Megabytes = "Megabytes"
    Gigabytes = "Gigabytes"
    Terabytes = "Terabytes"
    Bits = "Bits"
    Kilobits = "Kilobits"
    Megabits = "Megabits"
    Gigabits = "Gigabits"
    Terabits = "Terabits"
    Percent = "Percent"
    Count = "Count"
    Bytes_Second = "Bytes/Second"
    Kilobytes_Second = "Kilobytes/Second"
    Megabytes_Second = "Megabytes/Second"
    Gigabytes_Second = "Gigabytes/Second"
    Terabytes_Second = "Terabytes/Second"
    Bits_Second = "Bits/Second"
    Kilobits_Second = "Kilobits/Second"
    Megabits_Second = "Megabits/Second"
    Gigabits_Second = "Gigabits/Second"
    Terabits_Second = "Terabits/Second"
    Count_Second = "Count/Second"
    None_ = "None"


class UpdateStatus(StrEnum):
    SUCCESS = "SUCCESS"
    PENDING = "PENDING"
    FAILED = "FAILED"


class WebserverAccessMode(StrEnum):
    PRIVATE_ONLY = "PRIVATE_ONLY"
    PUBLIC_ONLY = "PUBLIC_ONLY"


class WorkerReplacementStrategy(StrEnum):
    FORCED = "FORCED"
    GRACEFUL = "GRACEFUL"


class AccessDeniedException(ServiceException):
    """Access to the Apache Airflow Web UI or CLI has been denied due to
    insufficient permissions. To learn more, see `Accessing an Amazon MWAA
    environment <https://docs.aws.amazon.com/mwaa/latest/userguide/access-policies.html>`__.
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = True
    status_code: int = 403


class InternalServerException(ServiceException):
    """InternalServerException: An internal error has occurred."""

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500


class ResourceNotFoundException(ServiceException):
    """ResourceNotFoundException: The resource is not available."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class RestApiResponse(TypedDict, total=False):
    pass


class RestApiClientException(ServiceException):
    """An exception indicating that a client-side error occurred during the
    Apache Airflow REST API call.
    """

    code: str = "RestApiClientException"
    sender_fault: bool = True
    status_code: int = 400
    RestApiStatusCode: Optional[Integer]
    RestApiResponse: Optional[RestApiResponse]


class RestApiServerException(ServiceException):
    """An exception indicating that a server-side error occurred during the
    Apache Airflow REST API call.
    """

    code: str = "RestApiServerException"
    sender_fault: bool = True
    status_code: int = 400
    RestApiStatusCode: Optional[Integer]
    RestApiResponse: Optional[RestApiResponse]


class ValidationException(ServiceException):
    """ValidationException: The provided input is not valid."""

    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400


AirflowConfigurationOptions = Dict[ConfigKey, ConfigValue]


class CreateCliTokenRequest(ServiceRequest):
    Name: EnvironmentName


class CreateCliTokenResponse(TypedDict, total=False):
    CliToken: Optional[Token]
    WebServerHostname: Optional[Hostname]


TagMap = Dict[TagKey, TagValue]


class ModuleLoggingConfigurationInput(TypedDict, total=False):
    """Enables the Apache Airflow log type (e.g. ``DagProcessingLogs``) and
    defines the log level to send to CloudWatch Logs (e.g. ``INFO``).
    """

    Enabled: LoggingEnabled
    LogLevel: LoggingLevel


class LoggingConfigurationInput(TypedDict, total=False):
    """Defines the Apache Airflow log types to send to CloudWatch Logs."""

    DagProcessingLogs: Optional[ModuleLoggingConfigurationInput]
    SchedulerLogs: Optional[ModuleLoggingConfigurationInput]
    WebserverLogs: Optional[ModuleLoggingConfigurationInput]
    WorkerLogs: Optional[ModuleLoggingConfigurationInput]
    TaskLogs: Optional[ModuleLoggingConfigurationInput]


SecurityGroupList = List[SecurityGroupId]
SubnetList = List[SubnetId]


class NetworkConfiguration(TypedDict, total=False):
    """Describes the VPC networking components used to secure and enable
    network traffic between the Amazon Web Services resources for your
    environment. For more information, see `About networking on Amazon
    MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`__.
    """

    SubnetIds: Optional[SubnetList]
    SecurityGroupIds: Optional[SecurityGroupList]


class CreateEnvironmentInput(ServiceRequest):
    """This section contains the Amazon Managed Workflows for Apache Airflow
    (Amazon MWAA) API reference documentation to create an environment. For
    more information, see `Get started with Amazon Managed Workflows for
    Apache
    Airflow <https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html>`__.
    """

    Name: EnvironmentName
    ExecutionRoleArn: IamRoleArn
    SourceBucketArn: S3BucketArn
    DagS3Path: RelativePath
    NetworkConfiguration: NetworkConfiguration
    PluginsS3Path: Optional[RelativePath]
    PluginsS3ObjectVersion: Optional[S3ObjectVersion]
    RequirementsS3Path: Optional[RelativePath]
    RequirementsS3ObjectVersion: Optional[S3ObjectVersion]
    StartupScriptS3Path: Optional[RelativePath]
    StartupScriptS3ObjectVersion: Optional[S3ObjectVersion]
    AirflowConfigurationOptions: Optional[AirflowConfigurationOptions]
    EnvironmentClass: Optional[EnvironmentClass]
    MaxWorkers: Optional[MaxWorkers]
    KmsKey: Optional[KmsKey]
    AirflowVersion: Optional[AirflowVersion]
    LoggingConfiguration: Optional[LoggingConfigurationInput]
    WeeklyMaintenanceWindowStart: Optional[WeeklyMaintenanceWindowStart]
    Tags: Optional[TagMap]
    WebserverAccessMode: Optional[WebserverAccessMode]
    MinWorkers: Optional[MinWorkers]
    Schedulers: Optional[Schedulers]
    EndpointManagement: Optional[EndpointManagement]
    MinWebservers: Optional[MinWebservers]
    MaxWebservers: Optional[MaxWebservers]


class CreateEnvironmentOutput(TypedDict, total=False):
    Arn: Optional[EnvironmentArn]


class CreateWebLoginTokenRequest(ServiceRequest):
    Name: EnvironmentName


class CreateWebLoginTokenResponse(TypedDict, total=False):
    WebToken: Optional[Token]
    WebServerHostname: Optional[Hostname]
    IamIdentity: Optional[IamIdentity]
    AirflowIdentity: Optional[AirflowIdentity]


CreatedAt = datetime


class DeleteEnvironmentInput(ServiceRequest):
    Name: EnvironmentName


class DeleteEnvironmentOutput(TypedDict, total=False):
    pass


class Dimension(TypedDict, total=False):
    """**Internal only**. Represents the dimensions of a metric. To learn more
    about the metrics published to Amazon CloudWatch, see `Amazon MWAA
    performance metrics in Amazon
    CloudWatch <https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html>`__.
    """

    Name: String
    Value: String


Dimensions = List[Dimension]


class Document(TypedDict, total=False):
    pass


class UpdateError(TypedDict, total=False):
    """Describes the error(s) encountered with the last update of the
    environment.
    """

    ErrorCode: Optional[ErrorCode]
    ErrorMessage: Optional[ErrorMessage]


UpdateCreatedAt = datetime


class LastUpdate(TypedDict, total=False):
    """Describes the status of the last update on the environment, and any
    errors that were encountered.
    """

    Status: Optional[UpdateStatus]
    CreatedAt: Optional[UpdateCreatedAt]
    Error: Optional[UpdateError]
    Source: Optional[UpdateSource]
    WorkerReplacementStrategy: Optional[WorkerReplacementStrategy]


class ModuleLoggingConfiguration(TypedDict, total=False):
    """Describes the Apache Airflow log details for the log type (e.g.
    ``DagProcessingLogs``).
    """

    Enabled: Optional[LoggingEnabled]
    LogLevel: Optional[LoggingLevel]
    CloudWatchLogGroupArn: Optional[CloudWatchLogGroupArn]


class LoggingConfiguration(TypedDict, total=False):
    """Describes the Apache Airflow log types that are published to CloudWatch
    Logs.
    """

    DagProcessingLogs: Optional[ModuleLoggingConfiguration]
    SchedulerLogs: Optional[ModuleLoggingConfiguration]
    WebserverLogs: Optional[ModuleLoggingConfiguration]
    WorkerLogs: Optional[ModuleLoggingConfiguration]
    TaskLogs: Optional[ModuleLoggingConfiguration]


class Environment(TypedDict, total=False):
    """Describes an Amazon Managed Workflows for Apache Airflow (MWAA)
    environment.
    """

    Name: Optional[EnvironmentName]
    Status: Optional[EnvironmentStatus]
    Arn: Optional[EnvironmentArn]
    CreatedAt: Optional[CreatedAt]
    WebserverUrl: Optional[WebserverUrl]
    ExecutionRoleArn: Optional[IamRoleArn]
    ServiceRoleArn: Optional[IamRoleArn]
    KmsKey: Optional[KmsKey]
    AirflowVersion: Optional[AirflowVersion]
    SourceBucketArn: Optional[S3BucketArn]
    DagS3Path: Optional[RelativePath]
    PluginsS3Path: Optional[RelativePath]
    PluginsS3ObjectVersion: Optional[S3ObjectVersion]
    RequirementsS3Path: Optional[RelativePath]
    RequirementsS3ObjectVersion: Optional[S3ObjectVersion]
    StartupScriptS3Path: Optional[String]
    StartupScriptS3ObjectVersion: Optional[String]
    AirflowConfigurationOptions: Optional[AirflowConfigurationOptions]
    EnvironmentClass: Optional[EnvironmentClass]
    MaxWorkers: Optional[MaxWorkers]
    NetworkConfiguration: Optional[NetworkConfiguration]
    LoggingConfiguration: Optional[LoggingConfiguration]
    LastUpdate: Optional[LastUpdate]
    WeeklyMaintenanceWindowStart: Optional[WeeklyMaintenanceWindowStart]
    Tags: Optional[TagMap]
    WebserverAccessMode: Optional[WebserverAccessMode]
    MinWorkers: Optional[MinWorkers]
    Schedulers: Optional[Schedulers]
    WebserverVpcEndpointService: Optional[VpcEndpointServiceName]
    DatabaseVpcEndpointService: Optional[VpcEndpointServiceName]
    CeleryExecutorQueue: Optional[CeleryExecutorQueue]
    EndpointManagement: Optional[EndpointManagement]
    MinWebservers: Optional[MinWebservers]
    MaxWebservers: Optional[MaxWebservers]


EnvironmentList = List[EnvironmentName]


class GetEnvironmentInput(ServiceRequest):
    Name: EnvironmentName


class GetEnvironmentOutput(TypedDict, total=False):
    Environment: Optional[Environment]


class RestApiRequestBody(TypedDict, total=False):
    pass


class InvokeRestApiRequest(ServiceRequest):
    Name: EnvironmentName
    Path: RestApiPath
    Method: RestApiMethod
    QueryParameters: Optional[Document]
    Body: Optional[RestApiRequestBody]


class InvokeRestApiResponse(TypedDict, total=False):
    RestApiStatusCode: Optional[Integer]
    RestApiResponse: Optional[RestApiResponse]


class ListEnvironmentsInput(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListEnvironmentsInputMaxResultsInteger]


class ListEnvironmentsOutput(TypedDict, total=False):
    Environments: EnvironmentList
    NextToken: Optional[NextToken]


class ListTagsForResourceInput(ServiceRequest):
    ResourceArn: EnvironmentArn


class ListTagsForResourceOutput(TypedDict, total=False):
    Tags: Optional[TagMap]


class StatisticSet(TypedDict, total=False):
    """**Internal only**. Represents a set of statistics that describe a
    specific metric. To learn more about the metrics published to Amazon
    CloudWatch, see `Amazon MWAA performance metrics in Amazon
    CloudWatch <https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html>`__.
    """

    SampleCount: Optional[Integer]
    Sum: Optional[Double]
    Minimum: Optional[Double]
    Maximum: Optional[Double]


Timestamp = datetime


class MetricDatum(TypedDict, total=False):
    """**Internal only**. Collects Apache Airflow metrics. To learn more about
    the metrics published to Amazon CloudWatch, see `Amazon MWAA performance
    metrics in Amazon
    CloudWatch <https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html>`__.
    """

    MetricName: String
    Timestamp: Timestamp
    Dimensions: Optional[Dimensions]
    Value: Optional[Double]
    Unit: Optional[Unit]
    StatisticValues: Optional[StatisticSet]


MetricData = List[MetricDatum]


class PublishMetricsInput(ServiceRequest):
    EnvironmentName: EnvironmentName
    MetricData: MetricData


class PublishMetricsOutput(TypedDict, total=False):
    pass


TagKeyList = List[TagKey]


class TagResourceInput(ServiceRequest):
    ResourceArn: EnvironmentArn
    Tags: TagMap


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    ResourceArn: EnvironmentArn
    tagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateNetworkConfigurationInput(TypedDict, total=False):
    """Defines the VPC networking components used to secure and enable network
    traffic between the Amazon Web Services resources for your environment.
    For more information, see `About networking on Amazon
    MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`__.
    """

    SecurityGroupIds: SecurityGroupList


class UpdateEnvironmentInput(ServiceRequest):
    Name: EnvironmentName
    ExecutionRoleArn: Optional[IamRoleArn]
    AirflowConfigurationOptions: Optional[AirflowConfigurationOptions]
    AirflowVersion: Optional[AirflowVersion]
    DagS3Path: Optional[RelativePath]
    EnvironmentClass: Optional[EnvironmentClass]
    LoggingConfiguration: Optional[LoggingConfigurationInput]
    MaxWorkers: Optional[MaxWorkers]
    MinWorkers: Optional[MinWorkers]
    MaxWebservers: Optional[MaxWebservers]
    MinWebservers: Optional[MinWebservers]
    WorkerReplacementStrategy: Optional[WorkerReplacementStrategy]
    NetworkConfiguration: Optional[UpdateNetworkConfigurationInput]
    PluginsS3Path: Optional[RelativePath]
    PluginsS3ObjectVersion: Optional[S3ObjectVersion]
    RequirementsS3Path: Optional[RelativePath]
    RequirementsS3ObjectVersion: Optional[S3ObjectVersion]
    Schedulers: Optional[Schedulers]
    SourceBucketArn: Optional[S3BucketArn]
    StartupScriptS3Path: Optional[RelativePath]
    StartupScriptS3ObjectVersion: Optional[S3ObjectVersion]
    WebserverAccessMode: Optional[WebserverAccessMode]
    WeeklyMaintenanceWindowStart: Optional[WeeklyMaintenanceWindowStart]


class UpdateEnvironmentOutput(TypedDict, total=False):
    Arn: Optional[EnvironmentArn]


class MwaaApi:
    service = "mwaa"
    version = "2020-07-01"

    @handler("CreateCliToken")
    def create_cli_token(
        self, context: RequestContext, name: EnvironmentName, **kwargs
    ) -> CreateCliTokenResponse:
        """Creates a CLI token for the Airflow CLI. To learn more, see `Creating an
        Apache Airflow CLI
        token <https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-cli.html>`__.

        :param name: The name of the Amazon MWAA environment.
        :returns: CreateCliTokenResponse
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("CreateEnvironment")
    def create_environment(
        self,
        context: RequestContext,
        name: EnvironmentName,
        execution_role_arn: IamRoleArn,
        source_bucket_arn: S3BucketArn,
        dag_s3_path: RelativePath,
        network_configuration: NetworkConfiguration,
        plugins_s3_path: RelativePath | None = None,
        plugins_s3_object_version: S3ObjectVersion | None = None,
        requirements_s3_path: RelativePath | None = None,
        requirements_s3_object_version: S3ObjectVersion | None = None,
        startup_script_s3_path: RelativePath | None = None,
        startup_script_s3_object_version: S3ObjectVersion | None = None,
        airflow_configuration_options: AirflowConfigurationOptions | None = None,
        environment_class: EnvironmentClass | None = None,
        max_workers: MaxWorkers | None = None,
        kms_key: KmsKey | None = None,
        airflow_version: AirflowVersion | None = None,
        logging_configuration: LoggingConfigurationInput | None = None,
        weekly_maintenance_window_start: WeeklyMaintenanceWindowStart | None = None,
        tags: TagMap | None = None,
        webserver_access_mode: WebserverAccessMode | None = None,
        min_workers: MinWorkers | None = None,
        schedulers: Schedulers | None = None,
        endpoint_management: EndpointManagement | None = None,
        min_webservers: MinWebservers | None = None,
        max_webservers: MaxWebservers | None = None,
        **kwargs,
    ) -> CreateEnvironmentOutput:
        """Creates an Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
        environment.

        :param name: The name of the Amazon MWAA environment.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role for your
        environment.
        :param source_bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG
        code and supporting files are stored.
        :param dag_s3_path: The relative path to the DAGs folder on your Amazon S3 bucket.
        :param network_configuration: The VPC networking components used to secure and enable network traffic
        between the Amazon Web Services resources for your environment.
        :param plugins_s3_path: The relative path to the ``plugins.
        :param plugins_s3_object_version: The version of the plugins.
        :param requirements_s3_path: The relative path to the ``requirements.
        :param requirements_s3_object_version: The version of the ``requirements.
        :param startup_script_s3_path: The relative path to the startup shell script in your Amazon S3 bucket.
        :param startup_script_s3_object_version: The version of the startup shell script in your Amazon S3 bucket.
        :param airflow_configuration_options: A list of key-value pairs containing the Apache Airflow configuration
        options you want to attach to your environment.
        :param environment_class: The environment class type.
        :param max_workers: The maximum number of workers that you want to run in your environment.
        :param kms_key: The Amazon Web Services Key Management Service (KMS) key to encrypt the
        data in your environment.
        :param airflow_version: The Apache Airflow version for your environment.
        :param logging_configuration: Defines the Apache Airflow logs to send to CloudWatch Logs.
        :param weekly_maintenance_window_start: The day and time of the week in Coordinated Universal Time (UTC) 24-hour
        standard time to start weekly maintenance updates of your environment in
        the following format: ``DAY:HH:MM``.
        :param tags: The key-value tag pairs you want to associate to your environment.
        :param webserver_access_mode: Defines the access mode for the Apache Airflow *web server*.
        :param min_workers: The minimum number of workers that you want to run in your environment.
        :param schedulers: The number of Apache Airflow schedulers to run in your environment.
        :param endpoint_management: Defines whether the VPC endpoints configured for the environment are
        created, and managed, by the customer or by Amazon MWAA.
        :param min_webservers: The minimum number of web servers that you want to run in your
        environment.
        :param max_webservers: The maximum number of web servers that you want to run in your
        environment.
        :returns: CreateEnvironmentOutput
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("CreateWebLoginToken")
    def create_web_login_token(
        self, context: RequestContext, name: EnvironmentName, **kwargs
    ) -> CreateWebLoginTokenResponse:
        """Creates a web login token for the Airflow Web UI. To learn more, see
        `Creating an Apache Airflow web login
        token <https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-web.html>`__.

        :param name: The name of the Amazon MWAA environment.
        :returns: CreateWebLoginTokenResponse
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DeleteEnvironment")
    def delete_environment(
        self, context: RequestContext, name: EnvironmentName, **kwargs
    ) -> DeleteEnvironmentOutput:
        """Deletes an Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
        environment.

        :param name: The name of the Amazon MWAA environment.
        :returns: DeleteEnvironmentOutput
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetEnvironment")
    def get_environment(
        self, context: RequestContext, name: EnvironmentName, **kwargs
    ) -> GetEnvironmentOutput:
        """Describes an Amazon Managed Workflows for Apache Airflow (MWAA)
        environment.

        :param name: The name of the Amazon MWAA environment.
        :returns: GetEnvironmentOutput
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("InvokeRestApi")
    def invoke_rest_api(
        self,
        context: RequestContext,
        name: EnvironmentName,
        path: RestApiPath,
        method: RestApiMethod,
        query_parameters: Document | None = None,
        body: RestApiRequestBody | None = None,
        **kwargs,
    ) -> InvokeRestApiResponse:
        """Invokes the Apache Airflow REST API on the webserver with the specified
        inputs. To learn more, see `Using the Apache Airflow REST
        API <https://docs.aws.amazon.com/mwaa/latest/userguide/access-mwaa-apache-airflow-rest-api.html>`__

        :param name: The name of the Amazon MWAA environment.
        :param path: The Apache Airflow REST API endpoint path to be called.
        :param method: The HTTP method used for making Airflow REST API calls.
        :param query_parameters: Query parameters to be included in the Apache Airflow REST API call,
        provided as a JSON object.
        :param body: The request body for the Apache Airflow REST API call, provided as a
        JSON object.
        :returns: InvokeRestApiResponse
        :raises RestApiClientException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        :raises RestApiServerException:
        """
        raise NotImplementedError

    @handler("ListEnvironments")
    def list_environments(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: ListEnvironmentsInputMaxResultsInteger | None = None,
        **kwargs,
    ) -> ListEnvironmentsOutput:
        """Lists the Amazon Managed Workflows for Apache Airflow (MWAA)
        environments.

        :param next_token: Retrieves the next page of the results.
        :param max_results: The maximum number of results to retrieve per page.
        :returns: ListEnvironmentsOutput
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: EnvironmentArn, **kwargs
    ) -> ListTagsForResourceOutput:
        """Lists the key-value tag pairs associated to the Amazon Managed Workflows
        for Apache Airflow (MWAA) environment. For example,
        ``"Environment": "Staging"``.

        :param resource_arn: The Amazon Resource Name (ARN) of the Amazon MWAA environment.
        :returns: ListTagsForResourceOutput
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("PublishMetrics")
    def publish_metrics(
        self,
        context: RequestContext,
        environment_name: EnvironmentName,
        metric_data: MetricData,
        **kwargs,
    ) -> PublishMetricsOutput:
        """**Internal only**. Publishes environment health metrics to Amazon
        CloudWatch.

        :param environment_name: **Internal only**.
        :param metric_data: **Internal only**.
        :returns: PublishMetricsOutput
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: EnvironmentArn, tags: TagMap, **kwargs
    ) -> TagResourceOutput:
        """Associates key-value tag pairs to your Amazon Managed Workflows for
        Apache Airflow (MWAA) environment.

        :param resource_arn: The Amazon Resource Name (ARN) of the Amazon MWAA environment.
        :param tags: The key-value tag pairs you want to associate to your environment.
        :returns: TagResourceOutput
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: EnvironmentArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceOutput:
        """Removes key-value tag pairs associated to your Amazon Managed Workflows
        for Apache Airflow (MWAA) environment. For example,
        ``"Environment": "Staging"``.

        :param resource_arn: The Amazon Resource Name (ARN) of the Amazon MWAA environment.
        :param tag_keys: The key-value tag pair you want to remove.
        :returns: UntagResourceOutput
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("UpdateEnvironment")
    def update_environment(
        self,
        context: RequestContext,
        name: EnvironmentName,
        execution_role_arn: IamRoleArn | None = None,
        airflow_configuration_options: AirflowConfigurationOptions | None = None,
        airflow_version: AirflowVersion | None = None,
        dag_s3_path: RelativePath | None = None,
        environment_class: EnvironmentClass | None = None,
        logging_configuration: LoggingConfigurationInput | None = None,
        max_workers: MaxWorkers | None = None,
        min_workers: MinWorkers | None = None,
        max_webservers: MaxWebservers | None = None,
        min_webservers: MinWebservers | None = None,
        worker_replacement_strategy: WorkerReplacementStrategy | None = None,
        network_configuration: UpdateNetworkConfigurationInput | None = None,
        plugins_s3_path: RelativePath | None = None,
        plugins_s3_object_version: S3ObjectVersion | None = None,
        requirements_s3_path: RelativePath | None = None,
        requirements_s3_object_version: S3ObjectVersion | None = None,
        schedulers: Schedulers | None = None,
        source_bucket_arn: S3BucketArn | None = None,
        startup_script_s3_path: RelativePath | None = None,
        startup_script_s3_object_version: S3ObjectVersion | None = None,
        webserver_access_mode: WebserverAccessMode | None = None,
        weekly_maintenance_window_start: WeeklyMaintenanceWindowStart | None = None,
        **kwargs,
    ) -> UpdateEnvironmentOutput:
        """Updates an Amazon Managed Workflows for Apache Airflow (MWAA)
        environment.

        :param name: The name of your Amazon MWAA environment.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role in IAM that allows
        MWAA to access Amazon Web Services resources in your environment.
        :param airflow_configuration_options: A list of key-value pairs containing the Apache Airflow configuration
        options you want to attach to your environment.
        :param airflow_version: The Apache Airflow version for your environment.
        :param dag_s3_path: The relative path to the DAGs folder on your Amazon S3 bucket.
        :param environment_class: The environment class type.
        :param logging_configuration: The Apache Airflow log types to send to CloudWatch Logs.
        :param max_workers: The maximum number of workers that you want to run in your environment.
        :param min_workers: The minimum number of workers that you want to run in your environment.
        :param max_webservers: The maximum number of web servers that you want to run in your
        environment.
        :param min_webservers: The minimum number of web servers that you want to run in your
        environment.
        :param worker_replacement_strategy: The worker replacement strategy to use when updating the environment.
        :param network_configuration: The VPC networking components used to secure and enable network traffic
        between the Amazon Web Services resources for your environment.
        :param plugins_s3_path: The relative path to the ``plugins.
        :param plugins_s3_object_version: The version of the plugins.
        :param requirements_s3_path: The relative path to the ``requirements.
        :param requirements_s3_object_version: The version of the requirements.
        :param schedulers: The number of Apache Airflow schedulers to run in your Amazon MWAA
        environment.
        :param source_bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG
        code and supporting files are stored.
        :param startup_script_s3_path: The relative path to the startup shell script in your Amazon S3 bucket.
        :param startup_script_s3_object_version: The version of the startup shell script in your Amazon S3 bucket.
        :param webserver_access_mode: The Apache Airflow *Web server* access mode.
        :param weekly_maintenance_window_start: The day and time of the week in Coordinated Universal Time (UTC) 24-hour
        standard time to start weekly maintenance updates of your environment in
        the following format: ``DAY:HH:MM``.
        :returns: UpdateEnvironmentOutput
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError
