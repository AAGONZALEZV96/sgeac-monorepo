from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

ApplicationArn = str
ApplicationId = str
ApplicationName = str
Arn = str
AttemptNumber = int
AutoStopConfigIdleTimeoutMinutesInteger = int
Boolean = bool
ClientToken = str
ConfigurationPropertyKey = str
ConfigurationPropertyValue = str
CpuSize = str
DiskSize = str
DiskType = str
Double = float
EncryptionKeyArn = str
EngineType = str
EntryPointArgument = str
EntryPointPath = str
HiveCliParameters = str
IAMRoleArn = str
ImageDigest = str
ImageUri = str
InitScriptPath = str
Integer = int
JobArn = str
JobRunId = str
JobRunType = str
ListApplicationsRequestMaxResultsInteger = int
ListJobRunAttemptsRequestMaxResultsInteger = int
ListJobRunsRequestMaxResultsInteger = int
LogGroupName = str
LogStreamNamePrefix = str
LogTypeString = str
MemorySize = str
NextToken = str
PolicyDocument = str
PrometheusUrlString = str
Query = str
ReleaseLabel = str
RequestIdentityUserArn = str
ResourceArn = str
RetryPolicyMaxFailedAttemptsPerHourInteger = int
SecurityGroupString = str
SparkSubmitParameters = str
String1024 = str
String256 = str
SubnetString = str
TagKey = str
TagValue = str
UriString = str
Url = str
WorkerTypeString = str


class ApplicationState(StrEnum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    STARTING = "STARTING"
    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    TERMINATED = "TERMINATED"


class Architecture(StrEnum):
    ARM64 = "ARM64"
    X86_64 = "X86_64"


class JobRunMode(StrEnum):
    BATCH = "BATCH"
    STREAMING = "STREAMING"


class JobRunState(StrEnum):
    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    QUEUED = "QUEUED"


class ConflictException(ServiceException):
    """The request could not be processed because of conflict in the current
    state of the resource.
    """

    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 409


class InternalServerException(ServiceException):
    """Request processing failed because of an error or failure with the
    service.
    """

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500


class ResourceNotFoundException(ServiceException):
    """The specified resource was not found."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class ServiceQuotaExceededException(ServiceException):
    """The maximum number of resources per account has been reached."""

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = True
    status_code: int = 402


class ValidationException(ServiceException):
    """The input fails to satisfy the constraints specified by an Amazon Web
    Services service.
    """

    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400


class SchedulerConfiguration(TypedDict, total=False):
    """The scheduler configuration for batch and streaming jobs running on this
    application. Supported with release labels emr-7.0.0 and above.
    """

    queueTimeoutMinutes: Optional[Integer]
    maxConcurrentRuns: Optional[Integer]


class InteractiveConfiguration(TypedDict, total=False):
    """The configuration to use to enable the different types of interactive
    use cases in an application.
    """

    studioEnabled: Optional[Boolean]
    livyEndpointEnabled: Optional[Boolean]


class PrometheusMonitoringConfiguration(TypedDict, total=False):
    """The monitoring configuration object you can configure to send metrics to
    Amazon Managed Service for Prometheus for a job run.
    """

    remoteWriteUrl: Optional[PrometheusUrlString]


LogTypeList = List[LogTypeString]
LogTypeMap = Dict[WorkerTypeString, LogTypeList]


class CloudWatchLoggingConfiguration(TypedDict, total=False):
    """The Amazon CloudWatch configuration for monitoring logs. You can
    configure your jobs to send log information to CloudWatch.
    """

    enabled: Boolean
    logGroupName: Optional[LogGroupName]
    logStreamNamePrefix: Optional[LogStreamNamePrefix]
    encryptionKeyArn: Optional[EncryptionKeyArn]
    logTypes: Optional[LogTypeMap]


class ManagedPersistenceMonitoringConfiguration(TypedDict, total=False):
    """The managed log persistence configuration for a job run."""

    enabled: Optional[Boolean]
    encryptionKeyArn: Optional[EncryptionKeyArn]


class S3MonitoringConfiguration(TypedDict, total=False):
    """The Amazon S3 configuration for monitoring log publishing. You can
    configure your jobs to send log information to Amazon S3.
    """

    logUri: Optional[UriString]
    encryptionKeyArn: Optional[EncryptionKeyArn]


class MonitoringConfiguration(TypedDict, total=False):
    """The configuration setting for monitoring."""

    s3MonitoringConfiguration: Optional[S3MonitoringConfiguration]
    managedPersistenceMonitoringConfiguration: Optional[ManagedPersistenceMonitoringConfiguration]
    cloudWatchLoggingConfiguration: Optional[CloudWatchLoggingConfiguration]
    prometheusMonitoringConfiguration: Optional[PrometheusMonitoringConfiguration]


ConfigurationList = List["Configuration"]
SensitivePropertiesMap = Dict[ConfigurationPropertyKey, ConfigurationPropertyValue]


class Configuration(TypedDict, total=False):
    """A configuration specification to be used when provisioning an
    application. A configuration consists of a classification, properties,
    and optional nested configurations. A classification refers to an
    application-specific configuration file. Properties are the settings you
    want to change in that file.
    """

    classification: String1024
    properties: Optional[SensitivePropertiesMap]
    configurations: Optional[ConfigurationList]


class ImageConfiguration(TypedDict, total=False):
    """The applied image configuration."""

    imageUri: ImageUri
    resolvedImageDigest: Optional[ImageDigest]


class WorkerTypeSpecification(TypedDict, total=False):
    """The specifications for a worker type."""

    imageConfiguration: Optional[ImageConfiguration]


WorkerTypeSpecificationMap = Dict[WorkerTypeString, WorkerTypeSpecification]
SecurityGroupIds = List[SecurityGroupString]
SubnetIds = List[SubnetString]


class NetworkConfiguration(TypedDict, total=False):
    """The network configuration for customer VPC connectivity."""

    subnetIds: Optional[SubnetIds]
    securityGroupIds: Optional[SecurityGroupIds]


class AutoStopConfig(TypedDict, total=False):
    """The configuration for an application to automatically stop after a
    certain amount of time being idle.
    """

    enabled: Optional[Boolean]
    idleTimeoutMinutes: Optional[AutoStopConfigIdleTimeoutMinutesInteger]


class AutoStartConfig(TypedDict, total=False):
    """The configuration for an application to automatically start on job
    submission.
    """

    enabled: Optional[Boolean]


TagMap = Dict[TagKey, TagValue]
Date = datetime


class MaximumAllowedResources(TypedDict, total=False):
    """The maximum allowed cumulative resources for an application. No new
    resources will be created once the limit is hit.
    """

    cpu: CpuSize
    memory: MemorySize
    disk: Optional[DiskSize]


class WorkerResourceConfig(TypedDict, total=False):
    """The cumulative configuration requirements for every worker instance of
    the worker type.
    """

    cpu: CpuSize
    memory: MemorySize
    disk: Optional[DiskSize]
    diskType: Optional[DiskType]


WorkerCounts = int


class InitialCapacityConfig(TypedDict, total=False):
    """The initial capacity configuration per worker."""

    workerCount: WorkerCounts
    workerConfiguration: Optional[WorkerResourceConfig]


InitialCapacityConfigMap = Dict[WorkerTypeString, InitialCapacityConfig]
Application = TypedDict(
    "Application",
    {
        "applicationId": ApplicationId,
        "name": Optional[ApplicationName],
        "arn": ApplicationArn,
        "releaseLabel": ReleaseLabel,
        "type": EngineType,
        "state": ApplicationState,
        "stateDetails": Optional[String256],
        "initialCapacity": Optional[InitialCapacityConfigMap],
        "maximumCapacity": Optional[MaximumAllowedResources],
        "createdAt": Date,
        "updatedAt": Date,
        "tags": Optional[TagMap],
        "autoStartConfiguration": Optional[AutoStartConfig],
        "autoStopConfiguration": Optional[AutoStopConfig],
        "networkConfiguration": Optional[NetworkConfiguration],
        "architecture": Optional[Architecture],
        "imageConfiguration": Optional[ImageConfiguration],
        "workerTypeSpecifications": Optional[WorkerTypeSpecificationMap],
        "runtimeConfiguration": Optional[ConfigurationList],
        "monitoringConfiguration": Optional[MonitoringConfiguration],
        "interactiveConfiguration": Optional[InteractiveConfiguration],
        "schedulerConfiguration": Optional[SchedulerConfiguration],
    },
    total=False,
)
ApplicationSummary = TypedDict(
    "ApplicationSummary",
    {
        "id": ApplicationId,
        "name": Optional[ApplicationName],
        "arn": ApplicationArn,
        "releaseLabel": ReleaseLabel,
        "type": EngineType,
        "state": ApplicationState,
        "stateDetails": Optional[String256],
        "createdAt": Date,
        "updatedAt": Date,
        "architecture": Optional[Architecture],
    },
    total=False,
)
ApplicationList = List[ApplicationSummary]
ApplicationStateSet = List[ApplicationState]


class CancelJobRunRequest(ServiceRequest):
    applicationId: ApplicationId
    jobRunId: JobRunId


class CancelJobRunResponse(TypedDict, total=False):
    applicationId: ApplicationId
    jobRunId: JobRunId


class ConfigurationOverrides(TypedDict, total=False):
    """A configuration specification to be used to override existing
    configurations.
    """

    applicationConfiguration: Optional[ConfigurationList]
    monitoringConfiguration: Optional[MonitoringConfiguration]


class ImageConfigurationInput(TypedDict, total=False):
    """The image configuration."""

    imageUri: Optional[ImageUri]


class WorkerTypeSpecificationInput(TypedDict, total=False):
    """The specifications for a worker type."""

    imageConfiguration: Optional[ImageConfigurationInput]


WorkerTypeSpecificationInputMap = Dict[WorkerTypeString, WorkerTypeSpecificationInput]
CreateApplicationRequest = TypedDict(
    "CreateApplicationRequest",
    {
        "name": Optional[ApplicationName],
        "releaseLabel": ReleaseLabel,
        "type": EngineType,
        "clientToken": ClientToken,
        "initialCapacity": Optional[InitialCapacityConfigMap],
        "maximumCapacity": Optional[MaximumAllowedResources],
        "tags": Optional[TagMap],
        "autoStartConfiguration": Optional[AutoStartConfig],
        "autoStopConfiguration": Optional[AutoStopConfig],
        "networkConfiguration": Optional[NetworkConfiguration],
        "architecture": Optional[Architecture],
        "imageConfiguration": Optional[ImageConfigurationInput],
        "workerTypeSpecifications": Optional[WorkerTypeSpecificationInputMap],
        "runtimeConfiguration": Optional[ConfigurationList],
        "monitoringConfiguration": Optional[MonitoringConfiguration],
        "interactiveConfiguration": Optional[InteractiveConfiguration],
        "schedulerConfiguration": Optional[SchedulerConfiguration],
    },
    total=False,
)


class CreateApplicationResponse(TypedDict, total=False):
    applicationId: ApplicationId
    name: Optional[ApplicationName]
    arn: ApplicationArn


class DeleteApplicationRequest(ServiceRequest):
    applicationId: ApplicationId


class DeleteApplicationResponse(TypedDict, total=False):
    pass


Duration = int
EntryPointArguments = List[EntryPointArgument]


class GetApplicationRequest(ServiceRequest):
    applicationId: ApplicationId


class GetApplicationResponse(TypedDict, total=False):
    application: Application


class GetDashboardForJobRunRequest(ServiceRequest):
    applicationId: ApplicationId
    jobRunId: JobRunId
    attempt: Optional[AttemptNumber]
    accessSystemProfileLogs: Optional[Boolean]


class GetDashboardForJobRunResponse(TypedDict, total=False):
    url: Optional[Url]


class GetJobRunRequest(ServiceRequest):
    applicationId: ApplicationId
    jobRunId: JobRunId
    attempt: Optional[AttemptNumber]


Long = int


class RetryPolicy(TypedDict, total=False):
    """The retry policy to use for a job run."""

    maxAttempts: Optional[AttemptNumber]
    maxFailedAttemptsPerHour: Optional[RetryPolicyMaxFailedAttemptsPerHourInteger]


class ResourceUtilization(TypedDict, total=False):
    """The resource utilization for memory, storage, and vCPU for jobs."""

    vCPUHour: Optional[Double]
    memoryGBHour: Optional[Double]
    storageGBHour: Optional[Double]


class TotalResourceUtilization(TypedDict, total=False):
    """The aggregate vCPU, memory, and storage resources used from the time job
    start executing till the time job is terminated, rounded up to the
    nearest second.
    """

    vCPUHour: Optional[Double]
    memoryGBHour: Optional[Double]
    storageGBHour: Optional[Double]


class Hive(TypedDict, total=False):
    """The configurations for the Hive job driver."""

    query: Query
    initQueryFile: Optional[InitScriptPath]
    parameters: Optional[HiveCliParameters]


class SparkSubmit(TypedDict, total=False):
    """The configurations for the Spark submit job driver."""

    entryPoint: EntryPointPath
    entryPointArguments: Optional[EntryPointArguments]
    sparkSubmitParameters: Optional[SparkSubmitParameters]


class JobDriver(TypedDict, total=False):
    """The driver that the job runs on."""

    sparkSubmit: Optional[SparkSubmit]
    hive: Optional[Hive]


class JobRun(TypedDict, total=False):
    """Information about a job run. A job run is a unit of work, such as a
    Spark JAR, Hive query, or SparkSQL query, that you submit to an Amazon
    EMR Serverless application.
    """

    applicationId: ApplicationId
    jobRunId: JobRunId
    name: Optional[String256]
    arn: JobArn
    createdBy: RequestIdentityUserArn
    createdAt: Date
    updatedAt: Date
    executionRole: IAMRoleArn
    state: JobRunState
    stateDetails: String256
    releaseLabel: ReleaseLabel
    configurationOverrides: Optional[ConfigurationOverrides]
    jobDriver: JobDriver
    tags: Optional[TagMap]
    totalResourceUtilization: Optional[TotalResourceUtilization]
    networkConfiguration: Optional[NetworkConfiguration]
    totalExecutionDurationSeconds: Optional[Integer]
    executionTimeoutMinutes: Optional[Duration]
    billedResourceUtilization: Optional[ResourceUtilization]
    mode: Optional[JobRunMode]
    retryPolicy: Optional[RetryPolicy]
    attempt: Optional[AttemptNumber]
    attemptCreatedAt: Optional[Date]
    attemptUpdatedAt: Optional[Date]
    startedAt: Optional[Date]
    endedAt: Optional[Date]
    queuedDurationMilliseconds: Optional[Long]


class GetJobRunResponse(TypedDict, total=False):
    jobRun: JobRun


JobRunAttemptSummary = TypedDict(
    "JobRunAttemptSummary",
    {
        "applicationId": ApplicationId,
        "id": JobRunId,
        "name": Optional[String256],
        "mode": Optional[JobRunMode],
        "arn": JobArn,
        "createdBy": RequestIdentityUserArn,
        "jobCreatedAt": Date,
        "createdAt": Date,
        "updatedAt": Date,
        "executionRole": IAMRoleArn,
        "state": JobRunState,
        "stateDetails": String256,
        "releaseLabel": ReleaseLabel,
        "type": Optional[JobRunType],
        "attempt": Optional[AttemptNumber],
    },
    total=False,
)
JobRunAttempts = List[JobRunAttemptSummary]
PolicyArnList = List[Arn]


class JobRunExecutionIamPolicy(TypedDict, total=False):
    """Optional IAM policy. The resulting job IAM role permissions will be an
    intersection of the policies passed and the policy associated with your
    job execution role.
    """

    policy: Optional[PolicyDocument]
    policyArns: Optional[PolicyArnList]


JobRunStateSet = List[JobRunState]
JobRunSummary = TypedDict(
    "JobRunSummary",
    {
        "applicationId": ApplicationId,
        "id": JobRunId,
        "name": Optional[String256],
        "mode": Optional[JobRunMode],
        "arn": JobArn,
        "createdBy": RequestIdentityUserArn,
        "createdAt": Date,
        "updatedAt": Date,
        "executionRole": IAMRoleArn,
        "state": JobRunState,
        "stateDetails": String256,
        "releaseLabel": ReleaseLabel,
        "type": Optional[JobRunType],
        "attempt": Optional[AttemptNumber],
        "attemptCreatedAt": Optional[Date],
        "attemptUpdatedAt": Optional[Date],
    },
    total=False,
)
JobRuns = List[JobRunSummary]


class ListApplicationsRequest(ServiceRequest):
    nextToken: Optional[NextToken]
    maxResults: Optional[ListApplicationsRequestMaxResultsInteger]
    states: Optional[ApplicationStateSet]


class ListApplicationsResponse(TypedDict, total=False):
    applications: ApplicationList
    nextToken: Optional[NextToken]


class ListJobRunAttemptsRequest(ServiceRequest):
    applicationId: ApplicationId
    jobRunId: JobRunId
    nextToken: Optional[NextToken]
    maxResults: Optional[ListJobRunAttemptsRequestMaxResultsInteger]


class ListJobRunAttemptsResponse(TypedDict, total=False):
    jobRunAttempts: JobRunAttempts
    nextToken: Optional[NextToken]


class ListJobRunsRequest(ServiceRequest):
    applicationId: ApplicationId
    nextToken: Optional[NextToken]
    maxResults: Optional[ListJobRunsRequestMaxResultsInteger]
    createdAtAfter: Optional[Date]
    createdAtBefore: Optional[Date]
    states: Optional[JobRunStateSet]
    mode: Optional[JobRunMode]


class ListJobRunsResponse(TypedDict, total=False):
    jobRuns: JobRuns
    nextToken: Optional[NextToken]


class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: ResourceArn


class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Optional[TagMap]


class StartApplicationRequest(ServiceRequest):
    applicationId: ApplicationId


class StartApplicationResponse(TypedDict, total=False):
    pass


class StartJobRunRequest(ServiceRequest):
    applicationId: ApplicationId
    clientToken: ClientToken
    executionRoleArn: IAMRoleArn
    executionIamPolicy: Optional[JobRunExecutionIamPolicy]
    jobDriver: Optional[JobDriver]
    configurationOverrides: Optional[ConfigurationOverrides]
    tags: Optional[TagMap]
    executionTimeoutMinutes: Optional[Duration]
    name: Optional[String256]
    mode: Optional[JobRunMode]
    retryPolicy: Optional[RetryPolicy]


class StartJobRunResponse(TypedDict, total=False):
    applicationId: ApplicationId
    jobRunId: JobRunId
    arn: JobArn


class StopApplicationRequest(ServiceRequest):
    applicationId: ApplicationId


class StopApplicationResponse(TypedDict, total=False):
    pass


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    resourceArn: ResourceArn
    tags: TagMap


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    resourceArn: ResourceArn
    tagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateApplicationRequest(ServiceRequest):
    applicationId: ApplicationId
    clientToken: ClientToken
    initialCapacity: Optional[InitialCapacityConfigMap]
    maximumCapacity: Optional[MaximumAllowedResources]
    autoStartConfiguration: Optional[AutoStartConfig]
    autoStopConfiguration: Optional[AutoStopConfig]
    networkConfiguration: Optional[NetworkConfiguration]
    architecture: Optional[Architecture]
    imageConfiguration: Optional[ImageConfigurationInput]
    workerTypeSpecifications: Optional[WorkerTypeSpecificationInputMap]
    interactiveConfiguration: Optional[InteractiveConfiguration]
    releaseLabel: Optional[ReleaseLabel]
    runtimeConfiguration: Optional[ConfigurationList]
    monitoringConfiguration: Optional[MonitoringConfiguration]
    schedulerConfiguration: Optional[SchedulerConfiguration]


class UpdateApplicationResponse(TypedDict, total=False):
    application: Application


class EmrServerlessApi:
    service = "emr-serverless"
    version = "2021-07-13"

    @handler("CancelJobRun")
    def cancel_job_run(
        self, context: RequestContext, application_id: ApplicationId, job_run_id: JobRunId, **kwargs
    ) -> CancelJobRunResponse:
        """Cancels a job run.

        :param application_id: The ID of the application on which the job run will be canceled.
        :param job_run_id: The ID of the job run to cancel.
        :returns: CancelJobRunResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("CreateApplication", expand=False)
    def create_application(
        self, context: RequestContext, request: CreateApplicationRequest, **kwargs
    ) -> CreateApplicationResponse:
        """Creates an application.

        :param release_label: The Amazon EMR release associated with the application.
        :param type: The type of application you want to start, such as Spark or Hive.
        :param client_token: The client idempotency token of the application to create.
        :param name: The name of the application.
        :param initial_capacity: The capacity to initialize when the application is created.
        :param maximum_capacity: The maximum capacity to allocate when the application is created.
        :param tags: The tags assigned to the application.
        :param auto_start_configuration: The configuration for an application to automatically start on job
        submission.
        :param auto_stop_configuration: The configuration for an application to automatically stop after a
        certain amount of time being idle.
        :param network_configuration: The network configuration for customer VPC connectivity.
        :param architecture: The CPU architecture of an application.
        :param image_configuration: The image configuration for all worker types.
        :param worker_type_specifications: The key-value pairs that specify worker type to
        ``WorkerTypeSpecificationInput``.
        :param runtime_configuration: The
        `Configuration <https://docs.
        :param monitoring_configuration: The configuration setting for monitoring.
        :param interactive_configuration: The interactive configuration object that enables the interactive use
        cases to use when running an application.
        :param scheduler_configuration: The scheduler configuration for batch and streaming jobs running on this
        application.
        :returns: CreateApplicationResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApplication")
    def delete_application(
        self, context: RequestContext, application_id: ApplicationId, **kwargs
    ) -> DeleteApplicationResponse:
        """Deletes an application. An application has to be in a stopped or created
        state in order to be deleted.

        :param application_id: The ID of the application that will be deleted.
        :returns: DeleteApplicationResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetApplication")
    def get_application(
        self, context: RequestContext, application_id: ApplicationId, **kwargs
    ) -> GetApplicationResponse:
        """Displays detailed information about a specified application.

        :param application_id: The ID of the application that will be described.
        :returns: GetApplicationResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetDashboardForJobRun")
    def get_dashboard_for_job_run(
        self,
        context: RequestContext,
        application_id: ApplicationId,
        job_run_id: JobRunId,
        attempt: AttemptNumber | None = None,
        access_system_profile_logs: Boolean | None = None,
        **kwargs,
    ) -> GetDashboardForJobRunResponse:
        """Creates and returns a URL that you can use to access the application UIs
        for a job run.

        For jobs in a running state, the application UI is a live user interface
        such as the Spark or Tez web UI. For completed jobs, the application UI
        is a persistent application user interface such as the Spark History
        Server or persistent Tez UI.

        The URL is valid for one hour after you generate it. To access the
        application UI after that hour elapses, you must invoke the API again to
        generate a new URL.

        :param application_id: The ID of the application.
        :param job_run_id: The ID of the job run.
        :param attempt: An optimal parameter that indicates the amount of attempts for the job.
        :param access_system_profile_logs: Allows access to system profile logs for Lake Formation-enabled jobs.
        :returns: GetDashboardForJobRunResponse
        :raises ValidationException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetJobRun")
    def get_job_run(
        self,
        context: RequestContext,
        application_id: ApplicationId,
        job_run_id: JobRunId,
        attempt: AttemptNumber | None = None,
        **kwargs,
    ) -> GetJobRunResponse:
        """Displays detailed information about a job run.

        :param application_id: The ID of the application on which the job run is submitted.
        :param job_run_id: The ID of the job run.
        :param attempt: An optimal parameter that indicates the amount of attempts for the job.
        :returns: GetJobRunResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListApplications")
    def list_applications(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: ListApplicationsRequestMaxResultsInteger | None = None,
        states: ApplicationStateSet | None = None,
        **kwargs,
    ) -> ListApplicationsResponse:
        """Lists applications based on a set of parameters.

        :param next_token: The token for the next set of application results.
        :param max_results: The maximum number of applications that can be listed.
        :param states: An optional filter for application states.
        :returns: ListApplicationsResponse
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListJobRunAttempts")
    def list_job_run_attempts(
        self,
        context: RequestContext,
        application_id: ApplicationId,
        job_run_id: JobRunId,
        next_token: NextToken | None = None,
        max_results: ListJobRunAttemptsRequestMaxResultsInteger | None = None,
        **kwargs,
    ) -> ListJobRunAttemptsResponse:
        """Lists all attempt of a job run.

        :param application_id: The ID of the application for which to list job runs.
        :param job_run_id: The ID of the job run to list.
        :param next_token: The token for the next set of job run attempt results.
        :param max_results: The maximum number of job run attempts to list.
        :returns: ListJobRunAttemptsResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListJobRuns")
    def list_job_runs(
        self,
        context: RequestContext,
        application_id: ApplicationId,
        next_token: NextToken | None = None,
        max_results: ListJobRunsRequestMaxResultsInteger | None = None,
        created_at_after: Date | None = None,
        created_at_before: Date | None = None,
        states: JobRunStateSet | None = None,
        mode: JobRunMode | None = None,
        **kwargs,
    ) -> ListJobRunsResponse:
        """Lists job runs based on a set of parameters.

        :param application_id: The ID of the application for which to list the job run.
        :param next_token: The token for the next set of job run results.
        :param max_results: The maximum number of job runs that can be listed.
        :param created_at_after: The lower bound of the option to filter by creation date and time.
        :param created_at_before: The upper bound of the option to filter by creation date and time.
        :param states: An optional filter for job run states.
        :param mode: The mode of the job runs to list.
        :returns: ListJobRunsResponse
        :raises ValidationException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> ListTagsForResourceResponse:
        """Lists the tags assigned to the resources.

        :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource to list the
        tags for.
        :returns: ListTagsForResourceResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StartApplication")
    def start_application(
        self, context: RequestContext, application_id: ApplicationId, **kwargs
    ) -> StartApplicationResponse:
        """Starts a specified application and initializes initial capacity if
        configured.

        :param application_id: The ID of the application to start.
        :returns: StartApplicationResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        """
        raise NotImplementedError

    @handler("StartJobRun")
    def start_job_run(
        self,
        context: RequestContext,
        application_id: ApplicationId,
        client_token: ClientToken,
        execution_role_arn: IAMRoleArn,
        execution_iam_policy: JobRunExecutionIamPolicy | None = None,
        job_driver: JobDriver | None = None,
        configuration_overrides: ConfigurationOverrides | None = None,
        tags: TagMap | None = None,
        execution_timeout_minutes: Duration | None = None,
        name: String256 | None = None,
        mode: JobRunMode | None = None,
        retry_policy: RetryPolicy | None = None,
        **kwargs,
    ) -> StartJobRunResponse:
        """Starts a job run.

        :param application_id: The ID of the application on which to run the job.
        :param client_token: The client idempotency token of the job run to start.
        :param execution_role_arn: The execution role ARN for the job run.
        :param execution_iam_policy: You can pass an optional IAM policy.
        :param job_driver: The job driver for the job run.
        :param configuration_overrides: The configuration overrides for the job run.
        :param tags: The tags assigned to the job run.
        :param execution_timeout_minutes: The maximum duration for the job run to run.
        :param name: The optional job run name.
        :param mode: The mode of the job run when it starts.
        :param retry_policy: The retry policy when job run starts.
        :returns: StartJobRunResponse
        :raises ValidationException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("StopApplication")
    def stop_application(
        self, context: RequestContext, application_id: ApplicationId, **kwargs
    ) -> StopApplicationResponse:
        """Stops a specified application and releases initial capacity if
        configured. All scheduled and running jobs must be completed or
        cancelled before stopping an application.

        :param application_id: The ID of the application to stop.
        :returns: StopApplicationResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagMap, **kwargs
    ) -> TagResourceResponse:
        """Assigns tags to resources. A tag is a label that you assign to an Amazon
        Web Services resource. Each tag consists of a key and an optional value,
        both of which you define. Tags enable you to categorize your Amazon Web
        Services resources by attributes such as purpose, owner, or environment.
        When you have many resources of the same type, you can quickly identify
        a specific resource based on the tags you've assigned to it.

        :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource to list the
        tags for.
        :param tags: The tags to add to the resource.
        :returns: TagResourceResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResponse:
        """Removes tags from resources.

        :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource to list the
        tags for.
        :param tag_keys: The keys of the tags to be removed.
        :returns: UntagResourceResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateApplication")
    def update_application(
        self,
        context: RequestContext,
        application_id: ApplicationId,
        client_token: ClientToken,
        initial_capacity: InitialCapacityConfigMap | None = None,
        maximum_capacity: MaximumAllowedResources | None = None,
        auto_start_configuration: AutoStartConfig | None = None,
        auto_stop_configuration: AutoStopConfig | None = None,
        network_configuration: NetworkConfiguration | None = None,
        architecture: Architecture | None = None,
        image_configuration: ImageConfigurationInput | None = None,
        worker_type_specifications: WorkerTypeSpecificationInputMap | None = None,
        interactive_configuration: InteractiveConfiguration | None = None,
        release_label: ReleaseLabel | None = None,
        runtime_configuration: ConfigurationList | None = None,
        monitoring_configuration: MonitoringConfiguration | None = None,
        scheduler_configuration: SchedulerConfiguration | None = None,
        **kwargs,
    ) -> UpdateApplicationResponse:
        """Updates a specified application. An application has to be in a stopped
        or created state in order to be updated.

        :param application_id: The ID of the application to update.
        :param client_token: The client idempotency token of the application to update.
        :param initial_capacity: The capacity to initialize when the application is updated.
        :param maximum_capacity: The maximum capacity to allocate when the application is updated.
        :param auto_start_configuration: The configuration for an application to automatically start on job
        submission.
        :param auto_stop_configuration: The configuration for an application to automatically stop after a
        certain amount of time being idle.
        :param network_configuration: The network configuration for customer VPC connectivity.
        :param architecture: The CPU architecture of an application.
        :param image_configuration: The image configuration to be used for all worker types.
        :param worker_type_specifications: The key-value pairs that specify worker type to
        ``WorkerTypeSpecificationInput``.
        :param interactive_configuration: The interactive configuration object that contains new interactive use
        cases when the application is updated.
        :param release_label: The Amazon EMR release label for the application.
        :param runtime_configuration: The
        `Configuration <https://docs.
        :param monitoring_configuration: The configuration setting for monitoring.
        :param scheduler_configuration: The scheduler configuration for batch and streaming jobs running on this
        application.
        :returns: UpdateApplicationResponse
        :raises ValidationException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError
