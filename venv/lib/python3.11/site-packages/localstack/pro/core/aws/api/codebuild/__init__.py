from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Boolean = bool
BuildTimeOut = int
FleetCapacity = int
FleetName = str
GitCloneDepth = int
KeyInput = str
NonEmptyString = str
NonNegativeInt = int
PageSize = int
Percentage = float
ProjectDescription = str
ProjectName = str
ReportGroupName = str
SensitiveNonEmptyString = str
SensitiveString = str
String = str
TimeOut = int
ValueInput = str
WrapperBoolean = bool
WrapperDouble = float
WrapperInt = int


class ArtifactNamespace(StrEnum):
    NONE = "NONE"
    BUILD_ID = "BUILD_ID"


class ArtifactPackaging(StrEnum):
    NONE = "NONE"
    ZIP = "ZIP"


class ArtifactsType(StrEnum):
    CODEPIPELINE = "CODEPIPELINE"
    S3 = "S3"
    NO_ARTIFACTS = "NO_ARTIFACTS"


class AuthType(StrEnum):
    OAUTH = "OAUTH"
    BASIC_AUTH = "BASIC_AUTH"
    PERSONAL_ACCESS_TOKEN = "PERSONAL_ACCESS_TOKEN"
    CODECONNECTIONS = "CODECONNECTIONS"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class BatchReportModeType(StrEnum):
    REPORT_INDIVIDUAL_BUILDS = "REPORT_INDIVIDUAL_BUILDS"
    REPORT_AGGREGATED_BATCH = "REPORT_AGGREGATED_BATCH"


class BucketOwnerAccess(StrEnum):
    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    FULL = "FULL"


class BuildBatchPhaseType(StrEnum):
    SUBMITTED = "SUBMITTED"
    DOWNLOAD_BATCHSPEC = "DOWNLOAD_BATCHSPEC"
    IN_PROGRESS = "IN_PROGRESS"
    COMBINE_ARTIFACTS = "COMBINE_ARTIFACTS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class BuildPhaseType(StrEnum):
    SUBMITTED = "SUBMITTED"
    QUEUED = "QUEUED"
    PROVISIONING = "PROVISIONING"
    DOWNLOAD_SOURCE = "DOWNLOAD_SOURCE"
    INSTALL = "INSTALL"
    PRE_BUILD = "PRE_BUILD"
    BUILD = "BUILD"
    POST_BUILD = "POST_BUILD"
    UPLOAD_ARTIFACTS = "UPLOAD_ARTIFACTS"
    FINALIZING = "FINALIZING"
    COMPLETED = "COMPLETED"


class CacheMode(StrEnum):
    LOCAL_DOCKER_LAYER_CACHE = "LOCAL_DOCKER_LAYER_CACHE"
    LOCAL_SOURCE_CACHE = "LOCAL_SOURCE_CACHE"
    LOCAL_CUSTOM_CACHE = "LOCAL_CUSTOM_CACHE"


class CacheType(StrEnum):
    NO_CACHE = "NO_CACHE"
    S3 = "S3"
    LOCAL = "LOCAL"


class CommandType(StrEnum):
    SHELL = "SHELL"


class ComputeType(StrEnum):
    BUILD_GENERAL1_SMALL = "BUILD_GENERAL1_SMALL"
    BUILD_GENERAL1_MEDIUM = "BUILD_GENERAL1_MEDIUM"
    BUILD_GENERAL1_LARGE = "BUILD_GENERAL1_LARGE"
    BUILD_GENERAL1_XLARGE = "BUILD_GENERAL1_XLARGE"
    BUILD_GENERAL1_2XLARGE = "BUILD_GENERAL1_2XLARGE"
    BUILD_LAMBDA_1GB = "BUILD_LAMBDA_1GB"
    BUILD_LAMBDA_2GB = "BUILD_LAMBDA_2GB"
    BUILD_LAMBDA_4GB = "BUILD_LAMBDA_4GB"
    BUILD_LAMBDA_8GB = "BUILD_LAMBDA_8GB"
    BUILD_LAMBDA_10GB = "BUILD_LAMBDA_10GB"
    ATTRIBUTE_BASED_COMPUTE = "ATTRIBUTE_BASED_COMPUTE"
    CUSTOM_INSTANCE_TYPE = "CUSTOM_INSTANCE_TYPE"


class CredentialProviderType(StrEnum):
    SECRETS_MANAGER = "SECRETS_MANAGER"


class EnvironmentType(StrEnum):
    WINDOWS_CONTAINER = "WINDOWS_CONTAINER"
    LINUX_CONTAINER = "LINUX_CONTAINER"
    LINUX_GPU_CONTAINER = "LINUX_GPU_CONTAINER"
    ARM_CONTAINER = "ARM_CONTAINER"
    WINDOWS_SERVER_2019_CONTAINER = "WINDOWS_SERVER_2019_CONTAINER"
    WINDOWS_SERVER_2022_CONTAINER = "WINDOWS_SERVER_2022_CONTAINER"
    LINUX_LAMBDA_CONTAINER = "LINUX_LAMBDA_CONTAINER"
    ARM_LAMBDA_CONTAINER = "ARM_LAMBDA_CONTAINER"
    LINUX_EC2 = "LINUX_EC2"
    ARM_EC2 = "ARM_EC2"
    WINDOWS_EC2 = "WINDOWS_EC2"
    MAC_ARM = "MAC_ARM"


class EnvironmentVariableType(StrEnum):
    PLAINTEXT = "PLAINTEXT"
    PARAMETER_STORE = "PARAMETER_STORE"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class FileSystemType(StrEnum):
    EFS = "EFS"


class FleetContextCode(StrEnum):
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    ACTION_REQUIRED = "ACTION_REQUIRED"
    PENDING_DELETION = "PENDING_DELETION"
    INSUFFICIENT_CAPACITY = "INSUFFICIENT_CAPACITY"


class FleetOverflowBehavior(StrEnum):
    QUEUE = "QUEUE"
    ON_DEMAND = "ON_DEMAND"


class FleetProxyRuleBehavior(StrEnum):
    ALLOW_ALL = "ALLOW_ALL"
    DENY_ALL = "DENY_ALL"


class FleetProxyRuleEffectType(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"


class FleetProxyRuleType(StrEnum):
    DOMAIN = "DOMAIN"
    IP = "IP"


class FleetScalingMetricType(StrEnum):
    FLEET_UTILIZATION_RATE = "FLEET_UTILIZATION_RATE"


class FleetScalingType(StrEnum):
    TARGET_TRACKING_SCALING = "TARGET_TRACKING_SCALING"


class FleetSortByType(StrEnum):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class FleetStatusCode(StrEnum):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    ROTATING = "ROTATING"
    PENDING_DELETION = "PENDING_DELETION"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    ACTIVE = "ACTIVE"


class ImagePullCredentialsType(StrEnum):
    CODEBUILD = "CODEBUILD"
    SERVICE_ROLE = "SERVICE_ROLE"


class LanguageType(StrEnum):
    JAVA = "JAVA"
    PYTHON = "PYTHON"
    NODE_JS = "NODE_JS"
    RUBY = "RUBY"
    GOLANG = "GOLANG"
    DOCKER = "DOCKER"
    ANDROID = "ANDROID"
    DOTNET = "DOTNET"
    BASE = "BASE"
    PHP = "PHP"


class LogsConfigStatusType(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MachineType(StrEnum):
    GENERAL = "GENERAL"
    NVME = "NVME"


class PlatformType(StrEnum):
    DEBIAN = "DEBIAN"
    AMAZON_LINUX = "AMAZON_LINUX"
    UBUNTU = "UBUNTU"
    WINDOWS_SERVER = "WINDOWS_SERVER"


class ProjectSortByType(StrEnum):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ProjectVisibilityType(StrEnum):
    PUBLIC_READ = "PUBLIC_READ"
    PRIVATE = "PRIVATE"


class ReportCodeCoverageSortByType(StrEnum):
    LINE_COVERAGE_PERCENTAGE = "LINE_COVERAGE_PERCENTAGE"
    FILE_PATH = "FILE_PATH"


class ReportExportConfigType(StrEnum):
    S3 = "S3"
    NO_EXPORT = "NO_EXPORT"


class ReportGroupSortByType(StrEnum):
    NAME = "NAME"
    CREATED_TIME = "CREATED_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ReportGroupStatusType(StrEnum):
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class ReportGroupTrendFieldType(StrEnum):
    PASS_RATE = "PASS_RATE"
    DURATION = "DURATION"
    TOTAL = "TOTAL"
    LINE_COVERAGE = "LINE_COVERAGE"
    LINES_COVERED = "LINES_COVERED"
    LINES_MISSED = "LINES_MISSED"
    BRANCH_COVERAGE = "BRANCH_COVERAGE"
    BRANCHES_COVERED = "BRANCHES_COVERED"
    BRANCHES_MISSED = "BRANCHES_MISSED"


class ReportPackagingType(StrEnum):
    ZIP = "ZIP"
    NONE = "NONE"


class ReportStatusType(StrEnum):
    GENERATING = "GENERATING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    INCOMPLETE = "INCOMPLETE"
    DELETING = "DELETING"


class ReportType(StrEnum):
    TEST = "TEST"
    CODE_COVERAGE = "CODE_COVERAGE"


class RetryBuildBatchType(StrEnum):
    RETRY_ALL_BUILDS = "RETRY_ALL_BUILDS"
    RETRY_FAILED_BUILDS = "RETRY_FAILED_BUILDS"


class ServerType(StrEnum):
    GITHUB = "GITHUB"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    GITLAB = "GITLAB"
    GITLAB_SELF_MANAGED = "GITLAB_SELF_MANAGED"


class SharedResourceSortByType(StrEnum):
    ARN = "ARN"
    MODIFIED_TIME = "MODIFIED_TIME"


class SortOrderType(StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class SourceAuthType(StrEnum):
    OAUTH = "OAUTH"
    CODECONNECTIONS = "CODECONNECTIONS"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class SourceType(StrEnum):
    CODECOMMIT = "CODECOMMIT"
    CODEPIPELINE = "CODEPIPELINE"
    GITHUB = "GITHUB"
    GITLAB = "GITLAB"
    GITLAB_SELF_MANAGED = "GITLAB_SELF_MANAGED"
    S3 = "S3"
    BITBUCKET = "BITBUCKET"
    GITHUB_ENTERPRISE = "GITHUB_ENTERPRISE"
    NO_SOURCE = "NO_SOURCE"


class StatusType(StrEnum):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    FAULT = "FAULT"
    TIMED_OUT = "TIMED_OUT"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"


class WebhookBuildType(StrEnum):
    BUILD = "BUILD"
    BUILD_BATCH = "BUILD_BATCH"
    RUNNER_BUILDKITE_BUILD = "RUNNER_BUILDKITE_BUILD"


class WebhookFilterType(StrEnum):
    EVENT = "EVENT"
    BASE_REF = "BASE_REF"
    HEAD_REF = "HEAD_REF"
    ACTOR_ACCOUNT_ID = "ACTOR_ACCOUNT_ID"
    FILE_PATH = "FILE_PATH"
    COMMIT_MESSAGE = "COMMIT_MESSAGE"
    WORKFLOW_NAME = "WORKFLOW_NAME"
    TAG_NAME = "TAG_NAME"
    RELEASE_NAME = "RELEASE_NAME"
    REPOSITORY_NAME = "REPOSITORY_NAME"
    ORGANIZATION_NAME = "ORGANIZATION_NAME"


class WebhookScopeType(StrEnum):
    GITHUB_ORGANIZATION = "GITHUB_ORGANIZATION"
    GITHUB_GLOBAL = "GITHUB_GLOBAL"
    GITLAB_GROUP = "GITLAB_GROUP"


class WebhookStatus(StrEnum):
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"


class AccountLimitExceededException(ServiceException):
    """An Amazon Web Services service limit was exceeded for the calling Amazon
    Web Services account.
    """

    code: str = "AccountLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class AccountSuspendedException(ServiceException):
    """The CodeBuild access has been suspended for the calling Amazon Web
    Services account.
    """

    code: str = "AccountSuspendedException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInputException(ServiceException):
    """The input value that was provided is not valid."""

    code: str = "InvalidInputException"
    sender_fault: bool = False
    status_code: int = 400


class OAuthProviderException(ServiceException):
    """There was a problem with the underlying OAuth provider."""

    code: str = "OAuthProviderException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceAlreadyExistsException(ServiceException):
    """The specified Amazon Web Services resource cannot be created, because an
    Amazon Web Services resource with the same settings already exists.
    """

    code: str = "ResourceAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """The specified Amazon Web Services resource cannot be found."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class AutoRetryConfig(TypedDict, total=False):
    """Information about the auto-retry configuration for the build."""

    autoRetryLimit: Optional[WrapperInt]
    autoRetryNumber: Optional[WrapperInt]
    nextAutoRetry: Optional[String]
    previousAutoRetry: Optional[String]


BuildIds = List[NonEmptyString]


class BatchDeleteBuildsInput(ServiceRequest):
    ids: BuildIds


class BuildNotDeleted(TypedDict, total=False):
    """Information about a build that could not be successfully deleted."""

    id: Optional[NonEmptyString]
    statusCode: Optional[String]


BuildsNotDeleted = List[BuildNotDeleted]


class BatchDeleteBuildsOutput(TypedDict, total=False):
    buildsDeleted: Optional[BuildIds]
    buildsNotDeleted: Optional[BuildsNotDeleted]


BuildBatchIds = List[NonEmptyString]


class BatchGetBuildBatchesInput(ServiceRequest):
    ids: BuildBatchIds


BuildReportArns = List[String]
ResolvedArtifact = TypedDict(
    "ResolvedArtifact",
    {
        "type": Optional[ArtifactsType],
        "location": Optional[String],
        "identifier": Optional[String],
    },
    total=False,
)
ResolvedSecondaryArtifacts = List[ResolvedArtifact]
Timestamp = datetime


class BuildSummary(TypedDict, total=False):
    """Contains summary information about a batch build group."""

    arn: Optional[String]
    requestedOn: Optional[Timestamp]
    buildStatus: Optional[StatusType]
    primaryArtifact: Optional[ResolvedArtifact]
    secondaryArtifacts: Optional[ResolvedSecondaryArtifacts]


BuildSummaries = List[BuildSummary]
Identifiers = List[NonEmptyString]


class BuildGroup(TypedDict, total=False):
    """Contains information about a batch build build group. Build groups are
    used to combine builds that can run in parallel, while still being able
    to set dependencies on other build groups.
    """

    identifier: Optional[String]
    dependsOn: Optional[Identifiers]
    ignoreFailure: Optional[Boolean]
    currentBuildSummary: Optional[BuildSummary]
    priorBuildSummaryList: Optional[BuildSummaries]


BuildGroups = List[BuildGroup]
FleetsAllowed = List[NonEmptyString]
ComputeTypesAllowed = List[NonEmptyString]


class BatchRestrictions(TypedDict, total=False):
    """Specifies restrictions for the batch build."""

    maximumBuildsAllowed: Optional[WrapperInt]
    computeTypesAllowed: Optional[ComputeTypesAllowed]
    fleetsAllowed: Optional[FleetsAllowed]


class ProjectBuildBatchConfig(TypedDict, total=False):
    """Contains configuration information about a batch build project."""

    serviceRole: Optional[NonEmptyString]
    combineArtifacts: Optional[WrapperBoolean]
    restrictions: Optional[BatchRestrictions]
    timeoutInMins: Optional[WrapperInt]
    batchReportMode: Optional[BatchReportModeType]


ProjectFileSystemLocation = TypedDict(
    "ProjectFileSystemLocation",
    {
        "type": Optional[FileSystemType],
        "location": Optional[String],
        "mountPoint": Optional[String],
        "identifier": Optional[String],
        "mountOptions": Optional[String],
    },
    total=False,
)
ProjectFileSystemLocations = List[ProjectFileSystemLocation]
WrapperLong = int
SecurityGroupIds = List[NonEmptyString]
Subnets = List[NonEmptyString]


class VpcConfig(TypedDict, total=False):
    """Information about the VPC configuration that CodeBuild accesses."""

    vpcId: Optional[NonEmptyString]
    subnets: Optional[Subnets]
    securityGroupIds: Optional[SecurityGroupIds]


class S3LogsConfig(TypedDict, total=False):
    """Information about S3 logs for a build project."""

    status: LogsConfigStatusType
    location: Optional[String]
    encryptionDisabled: Optional[WrapperBoolean]
    bucketOwnerAccess: Optional[BucketOwnerAccess]


class CloudWatchLogsConfig(TypedDict, total=False):
    """Information about CloudWatch Logs for a build project."""

    status: LogsConfigStatusType
    groupName: Optional[String]
    streamName: Optional[String]


class LogsConfig(TypedDict, total=False):
    """Information about logs for a build project. These can be logs in
    CloudWatch Logs, built in a specified S3 bucket, or both.
    """

    cloudWatchLogs: Optional[CloudWatchLogsConfig]
    s3Logs: Optional[S3LogsConfig]


class DockerServerStatus(TypedDict, total=False):
    """Contains information about the status of the docker server."""

    status: Optional[String]
    message: Optional[String]


class DockerServer(TypedDict, total=False):
    """Contains docker server information."""

    computeType: ComputeType
    securityGroupIds: Optional[SecurityGroupIds]
    status: Optional[DockerServerStatus]


class RegistryCredential(TypedDict, total=False):
    """Information about credentials that provide access to a private Docker
    registry. When this is set:

    -  ``imagePullCredentialsType`` must be set to ``SERVICE_ROLE``.

    -  images cannot be curated or an Amazon ECR image.

    For more information, see `Private Registry with Secrets Manager Sample
    for
    CodeBuild <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-private-registry.html>`__.
    """

    credential: NonEmptyString
    credentialProvider: CredentialProviderType


EnvironmentVariable = TypedDict(
    "EnvironmentVariable",
    {
        "name": NonEmptyString,
        "value": String,
        "type": Optional[EnvironmentVariableType],
    },
    total=False,
)
EnvironmentVariables = List[EnvironmentVariable]


class ProjectFleet(TypedDict, total=False):
    """Information about the compute fleet of the build project. For more
    information, see `Working with reserved capacity in
    CodeBuild <https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html>`__.
    """

    fleetArn: Optional[String]


class ComputeConfiguration(TypedDict, total=False):
    """Contains compute attributes. These attributes only need be specified
    when your project's or fleet's ``computeType`` is set to
    ``ATTRIBUTE_BASED_COMPUTE`` or ``CUSTOM_INSTANCE_TYPE``.
    """

    vCpu: Optional[WrapperLong]
    memory: Optional[WrapperLong]
    disk: Optional[WrapperLong]
    machineType: Optional[MachineType]
    instanceType: Optional[NonEmptyString]


ProjectEnvironment = TypedDict(
    "ProjectEnvironment",
    {
        "type": EnvironmentType,
        "image": NonEmptyString,
        "computeType": ComputeType,
        "computeConfiguration": Optional[ComputeConfiguration],
        "fleet": Optional[ProjectFleet],
        "environmentVariables": Optional[EnvironmentVariables],
        "privilegedMode": Optional[WrapperBoolean],
        "certificate": Optional[String],
        "registryCredential": Optional[RegistryCredential],
        "imagePullCredentialsType": Optional[ImagePullCredentialsType],
        "dockerServer": Optional[DockerServer],
    },
    total=False,
)
ProjectCacheModes = List[CacheMode]
ProjectCache = TypedDict(
    "ProjectCache",
    {
        "type": CacheType,
        "location": Optional[String],
        "modes": Optional[ProjectCacheModes],
        "cacheNamespace": Optional[String],
    },
    total=False,
)


class BuildArtifacts(TypedDict, total=False):
    """Information about build output artifacts."""

    location: Optional[String]
    sha256sum: Optional[String]
    md5sum: Optional[String]
    overrideArtifactName: Optional[WrapperBoolean]
    encryptionDisabled: Optional[WrapperBoolean]
    artifactIdentifier: Optional[String]
    bucketOwnerAccess: Optional[BucketOwnerAccess]


BuildArtifactsList = List[BuildArtifacts]


class ProjectSourceVersion(TypedDict, total=False):
    """A source identifier and its corresponding version."""

    sourceIdentifier: String
    sourceVersion: String


ProjectSecondarySourceVersions = List[ProjectSourceVersion]


class BuildStatusConfig(TypedDict, total=False):
    """Contains information that defines how the CodeBuild build project
    reports the build status to the source provider.
    """

    context: Optional[String]
    targetUrl: Optional[String]


SourceAuth = TypedDict(
    "SourceAuth",
    {
        "type": SourceAuthType,
        "resource": Optional[String],
    },
    total=False,
)


class GitSubmodulesConfig(TypedDict, total=False):
    """Information about the Git submodules configuration for an CodeBuild
    build project.
    """

    fetchSubmodules: WrapperBoolean


ProjectSource = TypedDict(
    "ProjectSource",
    {
        "type": SourceType,
        "location": Optional[String],
        "gitCloneDepth": Optional[GitCloneDepth],
        "gitSubmodulesConfig": Optional[GitSubmodulesConfig],
        "buildspec": Optional[String],
        "auth": Optional[SourceAuth],
        "reportBuildStatus": Optional[WrapperBoolean],
        "buildStatusConfig": Optional[BuildStatusConfig],
        "insecureSsl": Optional[WrapperBoolean],
        "sourceIdentifier": Optional[String],
    },
    total=False,
)
ProjectSources = List[ProjectSource]


class PhaseContext(TypedDict, total=False):
    """Additional information about a build phase that has an error. You can
    use this information for troubleshooting.
    """

    statusCode: Optional[String]
    message: Optional[String]


PhaseContexts = List[PhaseContext]


class BuildBatchPhase(TypedDict, total=False):
    """Contains information about a stage for a batch build."""

    phaseType: Optional[BuildBatchPhaseType]
    phaseStatus: Optional[StatusType]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    durationInSeconds: Optional[WrapperLong]
    contexts: Optional[PhaseContexts]


BuildBatchPhases = List[BuildBatchPhase]


class BuildBatch(TypedDict, total=False):
    """Contains information about a batch build."""

    id: Optional[NonEmptyString]
    arn: Optional[NonEmptyString]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    currentPhase: Optional[String]
    buildBatchStatus: Optional[StatusType]
    sourceVersion: Optional[NonEmptyString]
    resolvedSourceVersion: Optional[NonEmptyString]
    projectName: Optional[NonEmptyString]
    phases: Optional[BuildBatchPhases]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[BuildArtifacts]
    secondaryArtifacts: Optional[BuildArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    logConfig: Optional[LogsConfig]
    buildTimeoutInMinutes: Optional[WrapperInt]
    queuedTimeoutInMinutes: Optional[WrapperInt]
    complete: Optional[Boolean]
    initiator: Optional[String]
    vpcConfig: Optional[VpcConfig]
    encryptionKey: Optional[NonEmptyString]
    buildBatchNumber: Optional[WrapperLong]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    buildGroups: Optional[BuildGroups]
    debugSessionEnabled: Optional[WrapperBoolean]
    reportArns: Optional[BuildReportArns]


BuildBatches = List[BuildBatch]


class BatchGetBuildBatchesOutput(TypedDict, total=False):
    buildBatches: Optional[BuildBatches]
    buildBatchesNotFound: Optional[BuildBatchIds]


class BatchGetBuildsInput(ServiceRequest):
    ids: BuildIds


class DebugSession(TypedDict, total=False):
    """Contains information about the debug session for a build. For more
    information, see `Viewing a running build in Session
    Manager <https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html>`__.
    """

    sessionEnabled: Optional[WrapperBoolean]
    sessionTarget: Optional[NonEmptyString]


class ExportedEnvironmentVariable(TypedDict, total=False):
    """Contains information about an exported environment variable.

    Exported environment variables are used in conjunction with CodePipeline
    to export environment variables from the current build stage to
    subsequent stages in the pipeline. For more information, see `Working
    with
    variables <https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html>`__
    in the *CodePipeline User Guide*.

    During a build, the value of a variable is available starting with the
    ``install`` phase. It can be updated between the start of the
    ``install`` phase and the end of the ``post_build`` phase. After the
    ``post_build`` phase ends, the value of exported variables cannot
    change.
    """

    name: Optional[NonEmptyString]
    value: Optional[String]


ExportedEnvironmentVariables = List[ExportedEnvironmentVariable]


class NetworkInterface(TypedDict, total=False):
    """Describes a network interface."""

    subnetId: Optional[NonEmptyString]
    networkInterfaceId: Optional[NonEmptyString]


class LogsLocation(TypedDict, total=False):
    """Information about build logs in CloudWatch Logs."""

    groupName: Optional[String]
    streamName: Optional[String]
    deepLink: Optional[String]
    s3DeepLink: Optional[String]
    cloudWatchLogsArn: Optional[String]
    s3LogsArn: Optional[String]
    cloudWatchLogs: Optional[CloudWatchLogsConfig]
    s3Logs: Optional[S3LogsConfig]


class BuildPhase(TypedDict, total=False):
    """Information about a stage for a build."""

    phaseType: Optional[BuildPhaseType]
    phaseStatus: Optional[StatusType]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    durationInSeconds: Optional[WrapperLong]
    contexts: Optional[PhaseContexts]


BuildPhases = List[BuildPhase]


class Build(TypedDict, total=False):
    """Information about a build."""

    id: Optional[NonEmptyString]
    arn: Optional[NonEmptyString]
    buildNumber: Optional[WrapperLong]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    currentPhase: Optional[String]
    buildStatus: Optional[StatusType]
    sourceVersion: Optional[NonEmptyString]
    resolvedSourceVersion: Optional[NonEmptyString]
    projectName: Optional[NonEmptyString]
    phases: Optional[BuildPhases]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[BuildArtifacts]
    secondaryArtifacts: Optional[BuildArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    logs: Optional[LogsLocation]
    timeoutInMinutes: Optional[WrapperInt]
    queuedTimeoutInMinutes: Optional[WrapperInt]
    buildComplete: Optional[Boolean]
    initiator: Optional[String]
    vpcConfig: Optional[VpcConfig]
    networkInterface: Optional[NetworkInterface]
    encryptionKey: Optional[NonEmptyString]
    exportedEnvironmentVariables: Optional[ExportedEnvironmentVariables]
    reportArns: Optional[BuildReportArns]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    debugSession: Optional[DebugSession]
    buildBatchArn: Optional[String]
    autoRetryConfig: Optional[AutoRetryConfig]


Builds = List[Build]


class BatchGetBuildsOutput(TypedDict, total=False):
    builds: Optional[Builds]
    buildsNotFound: Optional[BuildIds]


CommandExecutionIds = List[NonEmptyString]


class BatchGetCommandExecutionsInput(ServiceRequest):
    sandboxId: NonEmptyString
    commandExecutionIds: CommandExecutionIds


CommandExecution = TypedDict(
    "CommandExecution",
    {
        "id": Optional[NonEmptyString],
        "sandboxId": Optional[NonEmptyString],
        "submitTime": Optional[Timestamp],
        "startTime": Optional[Timestamp],
        "endTime": Optional[Timestamp],
        "status": Optional[NonEmptyString],
        "command": Optional[SensitiveNonEmptyString],
        "type": Optional[CommandType],
        "exitCode": Optional[NonEmptyString],
        "standardOutputContent": Optional[SensitiveNonEmptyString],
        "standardErrContent": Optional[SensitiveNonEmptyString],
        "logs": Optional[LogsLocation],
        "sandboxArn": Optional[NonEmptyString],
    },
    total=False,
)
CommandExecutions = List[CommandExecution]


class BatchGetCommandExecutionsOutput(TypedDict, total=False):
    commandExecutions: Optional[CommandExecutions]
    commandExecutionsNotFound: Optional[CommandExecutionIds]


FleetNames = List[NonEmptyString]


class BatchGetFleetsInput(ServiceRequest):
    names: FleetNames


class Tag(TypedDict, total=False):
    """A tag, consisting of a key and a value.

    This tag is available for use by Amazon Web Services services that
    support tags in CodeBuild.
    """

    key: Optional[KeyInput]
    value: Optional[ValueInput]


TagList = List[Tag]
FleetProxyRuleEntities = List[String]
FleetProxyRule = TypedDict(
    "FleetProxyRule",
    {
        "type": FleetProxyRuleType,
        "effect": FleetProxyRuleEffectType,
        "entities": FleetProxyRuleEntities,
    },
    total=False,
)
FleetProxyRules = List[FleetProxyRule]


class ProxyConfiguration(TypedDict, total=False):
    """Information about the proxy configurations that apply network access
    control to your reserved capacity instances.
    """

    defaultBehavior: Optional[FleetProxyRuleBehavior]
    orderedProxyRules: Optional[FleetProxyRules]


class TargetTrackingScalingConfiguration(TypedDict, total=False):
    """Defines when a new instance is auto-scaled into the compute fleet."""

    metricType: Optional[FleetScalingMetricType]
    targetValue: Optional[WrapperDouble]


TargetTrackingScalingConfigurations = List[TargetTrackingScalingConfiguration]


class ScalingConfigurationOutput(TypedDict, total=False):
    """The scaling configuration output of a compute fleet."""

    scalingType: Optional[FleetScalingType]
    targetTrackingScalingConfigs: Optional[TargetTrackingScalingConfigurations]
    maxCapacity: Optional[FleetCapacity]
    desiredCapacity: Optional[FleetCapacity]


class FleetStatus(TypedDict, total=False):
    """The status of the compute fleet."""

    statusCode: Optional[FleetStatusCode]
    context: Optional[FleetContextCode]
    message: Optional[String]


class Fleet(TypedDict, total=False):
    """A set of dedicated instances for your build environment."""

    arn: Optional[NonEmptyString]
    name: Optional[FleetName]
    id: Optional[NonEmptyString]
    created: Optional[Timestamp]
    lastModified: Optional[Timestamp]
    status: Optional[FleetStatus]
    baseCapacity: Optional[FleetCapacity]
    environmentType: Optional[EnvironmentType]
    computeType: Optional[ComputeType]
    computeConfiguration: Optional[ComputeConfiguration]
    scalingConfiguration: Optional[ScalingConfigurationOutput]
    overflowBehavior: Optional[FleetOverflowBehavior]
    vpcConfig: Optional[VpcConfig]
    proxyConfiguration: Optional[ProxyConfiguration]
    imageId: Optional[NonEmptyString]
    fleetServiceRole: Optional[NonEmptyString]
    tags: Optional[TagList]


Fleets = List[Fleet]


class BatchGetFleetsOutput(TypedDict, total=False):
    fleets: Optional[Fleets]
    fleetsNotFound: Optional[FleetNames]


ProjectNames = List[NonEmptyString]


class BatchGetProjectsInput(ServiceRequest):
    names: ProjectNames


class ProjectBadge(TypedDict, total=False):
    """Information about the build badge for the build project."""

    badgeEnabled: Optional[Boolean]
    badgeRequestUrl: Optional[String]


class ScopeConfiguration(TypedDict, total=False):
    """Contains configuration information about the scope for a webhook."""

    name: String
    domain: Optional[String]
    scope: WebhookScopeType


WebhookFilter = TypedDict(
    "WebhookFilter",
    {
        "type": WebhookFilterType,
        "pattern": String,
        "excludeMatchedPattern": Optional[WrapperBoolean],
    },
    total=False,
)
FilterGroup = List[WebhookFilter]
FilterGroups = List[FilterGroup]


class Webhook(TypedDict, total=False):
    """Information about a webhook that connects repository events to a build
    project in CodeBuild.
    """

    url: Optional[NonEmptyString]
    payloadUrl: Optional[NonEmptyString]
    secret: Optional[NonEmptyString]
    branchFilter: Optional[String]
    filterGroups: Optional[FilterGroups]
    buildType: Optional[WebhookBuildType]
    manualCreation: Optional[WrapperBoolean]
    lastModifiedSecret: Optional[Timestamp]
    scopeConfiguration: Optional[ScopeConfiguration]
    status: Optional[WebhookStatus]
    statusMessage: Optional[String]


ProjectArtifacts = TypedDict(
    "ProjectArtifacts",
    {
        "type": ArtifactsType,
        "location": Optional[String],
        "path": Optional[String],
        "namespaceType": Optional[ArtifactNamespace],
        "name": Optional[String],
        "packaging": Optional[ArtifactPackaging],
        "overrideArtifactName": Optional[WrapperBoolean],
        "encryptionDisabled": Optional[WrapperBoolean],
        "artifactIdentifier": Optional[String],
        "bucketOwnerAccess": Optional[BucketOwnerAccess],
    },
    total=False,
)
ProjectArtifactsList = List[ProjectArtifacts]


class Project(TypedDict, total=False):
    """Information about a build project."""

    name: Optional[ProjectName]
    arn: Optional[String]
    description: Optional[ProjectDescription]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    sourceVersion: Optional[String]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[ProjectArtifacts]
    secondaryArtifacts: Optional[ProjectArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    timeoutInMinutes: Optional[BuildTimeOut]
    queuedTimeoutInMinutes: Optional[TimeOut]
    encryptionKey: Optional[NonEmptyString]
    tags: Optional[TagList]
    created: Optional[Timestamp]
    lastModified: Optional[Timestamp]
    webhook: Optional[Webhook]
    vpcConfig: Optional[VpcConfig]
    badge: Optional[ProjectBadge]
    logsConfig: Optional[LogsConfig]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    concurrentBuildLimit: Optional[WrapperInt]
    projectVisibility: Optional[ProjectVisibilityType]
    publicProjectAlias: Optional[NonEmptyString]
    resourceAccessRole: Optional[NonEmptyString]
    autoRetryLimit: Optional[WrapperInt]


Projects = List[Project]


class BatchGetProjectsOutput(TypedDict, total=False):
    projects: Optional[Projects]
    projectsNotFound: Optional[ProjectNames]


ReportGroupArns = List[NonEmptyString]


class BatchGetReportGroupsInput(ServiceRequest):
    reportGroupArns: ReportGroupArns


class S3ReportExportConfig(TypedDict, total=False):
    """Information about the S3 bucket where the raw data of a report are
    exported.
    """

    bucket: Optional[NonEmptyString]
    bucketOwner: Optional[String]
    path: Optional[String]
    packaging: Optional[ReportPackagingType]
    encryptionKey: Optional[NonEmptyString]
    encryptionDisabled: Optional[WrapperBoolean]


class ReportExportConfig(TypedDict, total=False):
    """Information about the location where the run of a report is exported."""

    exportConfigType: Optional[ReportExportConfigType]
    s3Destination: Optional[S3ReportExportConfig]


ReportGroup = TypedDict(
    "ReportGroup",
    {
        "arn": Optional[NonEmptyString],
        "name": Optional[ReportGroupName],
        "type": Optional[ReportType],
        "exportConfig": Optional[ReportExportConfig],
        "created": Optional[Timestamp],
        "lastModified": Optional[Timestamp],
        "tags": Optional[TagList],
        "status": Optional[ReportGroupStatusType],
    },
    total=False,
)
ReportGroups = List[ReportGroup]


class BatchGetReportGroupsOutput(TypedDict, total=False):
    reportGroups: Optional[ReportGroups]
    reportGroupsNotFound: Optional[ReportGroupArns]


ReportArns = List[NonEmptyString]


class BatchGetReportsInput(ServiceRequest):
    reportArns: ReportArns


class CodeCoverageReportSummary(TypedDict, total=False):
    """Contains a summary of a code coverage report.

    Line coverage measures how many statements your tests cover. A statement
    is a single instruction, not including comments, conditionals, etc.

    Branch coverage determines if your tests cover every possible branch of
    a control structure, such as an ``if`` or ``case`` statement.
    """

    lineCoveragePercentage: Optional[Percentage]
    linesCovered: Optional[NonNegativeInt]
    linesMissed: Optional[NonNegativeInt]
    branchCoveragePercentage: Optional[Percentage]
    branchesCovered: Optional[NonNegativeInt]
    branchesMissed: Optional[NonNegativeInt]


ReportStatusCounts = Dict[String, WrapperInt]


class TestReportSummary(TypedDict, total=False):
    """Information about a test report."""

    total: WrapperInt
    statusCounts: ReportStatusCounts
    durationInNanoSeconds: WrapperLong


Report = TypedDict(
    "Report",
    {
        "arn": Optional[NonEmptyString],
        "type": Optional[ReportType],
        "name": Optional[String],
        "reportGroupArn": Optional[NonEmptyString],
        "executionId": Optional[String],
        "status": Optional[ReportStatusType],
        "created": Optional[Timestamp],
        "expired": Optional[Timestamp],
        "exportConfig": Optional[ReportExportConfig],
        "truncated": Optional[WrapperBoolean],
        "testSummary": Optional[TestReportSummary],
        "codeCoverageSummary": Optional[CodeCoverageReportSummary],
    },
    total=False,
)
Reports = List[Report]


class BatchGetReportsOutput(TypedDict, total=False):
    reports: Optional[Reports]
    reportsNotFound: Optional[ReportArns]


SandboxIds = List[NonEmptyString]


class BatchGetSandboxesInput(ServiceRequest):
    ids: SandboxIds


class SandboxSessionPhase(TypedDict, total=False):
    """Contains information about the sandbox phase."""

    phaseType: Optional[String]
    phaseStatus: Optional[StatusType]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    durationInSeconds: Optional[WrapperLong]
    contexts: Optional[PhaseContexts]


SandboxSessionPhases = List[SandboxSessionPhase]


class SandboxSession(TypedDict, total=False):
    """Contains information about the sandbox session."""

    id: Optional[NonEmptyString]
    status: Optional[String]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    currentPhase: Optional[String]
    phases: Optional[SandboxSessionPhases]
    resolvedSourceVersion: Optional[NonEmptyString]
    logs: Optional[LogsLocation]
    networkInterface: Optional[NetworkInterface]


class Sandbox(TypedDict, total=False):
    """Contains sandbox information."""

    id: Optional[NonEmptyString]
    arn: Optional[NonEmptyString]
    projectName: Optional[NonEmptyString]
    requestTime: Optional[Timestamp]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    status: Optional[String]
    source: Optional[ProjectSource]
    sourceVersion: Optional[NonEmptyString]
    secondarySources: Optional[ProjectSources]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    environment: Optional[ProjectEnvironment]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    timeoutInMinutes: Optional[WrapperInt]
    queuedTimeoutInMinutes: Optional[WrapperInt]
    vpcConfig: Optional[VpcConfig]
    logConfig: Optional[LogsConfig]
    encryptionKey: Optional[NonEmptyString]
    serviceRole: Optional[NonEmptyString]
    currentSession: Optional[SandboxSession]


Sandboxes = List[Sandbox]


class BatchGetSandboxesOutput(TypedDict, total=False):
    sandboxes: Optional[Sandboxes]
    sandboxesNotFound: Optional[SandboxIds]


class BuildBatchFilter(TypedDict, total=False):
    """Specifies filters when retrieving batch builds."""

    status: Optional[StatusType]


class CodeCoverage(TypedDict, total=False):
    """Contains code coverage report information.

    Line coverage measures how many statements your tests cover. A statement
    is a single instruction, not including comments, conditionals, etc.

    Branch coverage determines if your tests cover every possible branch of
    a control structure, such as an ``if`` or ``case`` statement.
    """

    id: Optional[NonEmptyString]
    reportARN: Optional[NonEmptyString]
    filePath: Optional[NonEmptyString]
    lineCoveragePercentage: Optional[Percentage]
    linesCovered: Optional[NonNegativeInt]
    linesMissed: Optional[NonNegativeInt]
    branchCoveragePercentage: Optional[Percentage]
    branchesCovered: Optional[NonNegativeInt]
    branchesMissed: Optional[NonNegativeInt]
    expired: Optional[Timestamp]


CodeCoverages = List[CodeCoverage]


class ScalingConfigurationInput(TypedDict, total=False):
    """The scaling configuration input of a compute fleet."""

    scalingType: Optional[FleetScalingType]
    targetTrackingScalingConfigs: Optional[TargetTrackingScalingConfigurations]
    maxCapacity: Optional[FleetCapacity]


class CreateFleetInput(ServiceRequest):
    name: FleetName
    baseCapacity: FleetCapacity
    environmentType: EnvironmentType
    computeType: ComputeType
    computeConfiguration: Optional[ComputeConfiguration]
    scalingConfiguration: Optional[ScalingConfigurationInput]
    overflowBehavior: Optional[FleetOverflowBehavior]
    vpcConfig: Optional[VpcConfig]
    proxyConfiguration: Optional[ProxyConfiguration]
    imageId: Optional[NonEmptyString]
    fleetServiceRole: Optional[NonEmptyString]
    tags: Optional[TagList]


class CreateFleetOutput(TypedDict, total=False):
    fleet: Optional[Fleet]


class CreateProjectInput(ServiceRequest):
    name: ProjectName
    description: Optional[ProjectDescription]
    source: ProjectSource
    secondarySources: Optional[ProjectSources]
    sourceVersion: Optional[String]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: ProjectArtifacts
    secondaryArtifacts: Optional[ProjectArtifactsList]
    cache: Optional[ProjectCache]
    environment: ProjectEnvironment
    serviceRole: NonEmptyString
    timeoutInMinutes: Optional[BuildTimeOut]
    queuedTimeoutInMinutes: Optional[TimeOut]
    encryptionKey: Optional[NonEmptyString]
    tags: Optional[TagList]
    vpcConfig: Optional[VpcConfig]
    badgeEnabled: Optional[WrapperBoolean]
    logsConfig: Optional[LogsConfig]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    concurrentBuildLimit: Optional[WrapperInt]
    autoRetryLimit: Optional[WrapperInt]


class CreateProjectOutput(TypedDict, total=False):
    project: Optional[Project]


CreateReportGroupInput = TypedDict(
    "CreateReportGroupInput",
    {
        "name": ReportGroupName,
        "type": ReportType,
        "exportConfig": ReportExportConfig,
        "tags": Optional[TagList],
    },
    total=False,
)


class CreateReportGroupOutput(TypedDict, total=False):
    reportGroup: Optional[ReportGroup]


class CreateWebhookInput(ServiceRequest):
    projectName: ProjectName
    branchFilter: Optional[String]
    filterGroups: Optional[FilterGroups]
    buildType: Optional[WebhookBuildType]
    manualCreation: Optional[WrapperBoolean]
    scopeConfiguration: Optional[ScopeConfiguration]


class CreateWebhookOutput(TypedDict, total=False):
    webhook: Optional[Webhook]


class DeleteBuildBatchInput(ServiceRequest):
    id: NonEmptyString


class DeleteBuildBatchOutput(TypedDict, total=False):
    statusCode: Optional[String]
    buildsDeleted: Optional[BuildIds]
    buildsNotDeleted: Optional[BuildsNotDeleted]


class DeleteFleetInput(ServiceRequest):
    arn: NonEmptyString


class DeleteFleetOutput(TypedDict, total=False):
    pass


class DeleteProjectInput(ServiceRequest):
    name: NonEmptyString


class DeleteProjectOutput(TypedDict, total=False):
    pass


class DeleteReportGroupInput(ServiceRequest):
    arn: NonEmptyString
    deleteReports: Optional[Boolean]


class DeleteReportGroupOutput(TypedDict, total=False):
    pass


class DeleteReportInput(ServiceRequest):
    arn: NonEmptyString


class DeleteReportOutput(TypedDict, total=False):
    pass


class DeleteResourcePolicyInput(ServiceRequest):
    resourceArn: NonEmptyString


class DeleteResourcePolicyOutput(TypedDict, total=False):
    pass


class DeleteSourceCredentialsInput(ServiceRequest):
    arn: NonEmptyString


class DeleteSourceCredentialsOutput(TypedDict, total=False):
    arn: Optional[NonEmptyString]


class DeleteWebhookInput(ServiceRequest):
    projectName: ProjectName


class DeleteWebhookOutput(TypedDict, total=False):
    pass


class DescribeCodeCoveragesInput(ServiceRequest):
    reportArn: NonEmptyString
    nextToken: Optional[String]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[ReportCodeCoverageSortByType]
    minLineCoveragePercentage: Optional[Percentage]
    maxLineCoveragePercentage: Optional[Percentage]


class DescribeCodeCoveragesOutput(TypedDict, total=False):
    nextToken: Optional[String]
    codeCoverages: Optional[CodeCoverages]


class TestCaseFilter(TypedDict, total=False):
    """A filter used to return specific types of test cases. In order to pass
    the filter, the report must meet all of the filter properties.
    """

    status: Optional[String]
    keyword: Optional[String]


class DescribeTestCasesInput(ServiceRequest):
    reportArn: String
    nextToken: Optional[String]
    maxResults: Optional[PageSize]
    filter: Optional[TestCaseFilter]


class TestCase(TypedDict, total=False):
    """Information about a test case created using a framework such as NUnit or
    Cucumber. A test case might be a unit test or a configuration test.
    """

    reportArn: Optional[NonEmptyString]
    testRawDataPath: Optional[String]
    prefix: Optional[String]
    name: Optional[String]
    status: Optional[String]
    durationInNanoSeconds: Optional[WrapperLong]
    message: Optional[String]
    expired: Optional[Timestamp]
    testSuiteName: Optional[String]


TestCases = List[TestCase]


class DescribeTestCasesOutput(TypedDict, total=False):
    nextToken: Optional[String]
    testCases: Optional[TestCases]


ImageVersions = List[String]


class EnvironmentImage(TypedDict, total=False):
    """Information about a Docker image that is managed by CodeBuild."""

    name: Optional[String]
    description: Optional[String]
    versions: Optional[ImageVersions]


EnvironmentImages = List[EnvironmentImage]


class EnvironmentLanguage(TypedDict, total=False):
    """A set of Docker images that are related by programming language and are
    managed by CodeBuild.
    """

    language: Optional[LanguageType]
    images: Optional[EnvironmentImages]


EnvironmentLanguages = List[EnvironmentLanguage]


class EnvironmentPlatform(TypedDict, total=False):
    """A set of Docker images that are related by platform and are managed by
    CodeBuild.
    """

    platform: Optional[PlatformType]
    languages: Optional[EnvironmentLanguages]


EnvironmentPlatforms = List[EnvironmentPlatform]
FleetArns = List[NonEmptyString]


class GetReportGroupTrendInput(ServiceRequest):
    reportGroupArn: NonEmptyString
    numOfReports: Optional[PageSize]
    trendField: ReportGroupTrendFieldType


class ReportWithRawData(TypedDict, total=False):
    """Contains the unmodified data for the report. For more information, see ."""

    reportArn: Optional[NonEmptyString]
    data: Optional[String]


ReportGroupTrendRawDataList = List[ReportWithRawData]


class ReportGroupTrendStats(TypedDict, total=False):
    """Contains trend statistics for a set of reports. The actual values depend
    on the type of trend being collected. For more information, see .
    """

    average: Optional[String]
    max: Optional[String]
    min: Optional[String]


class GetReportGroupTrendOutput(TypedDict, total=False):
    stats: Optional[ReportGroupTrendStats]
    rawData: Optional[ReportGroupTrendRawDataList]


class GetResourcePolicyInput(ServiceRequest):
    resourceArn: NonEmptyString


class GetResourcePolicyOutput(TypedDict, total=False):
    policy: Optional[NonEmptyString]


class ImportSourceCredentialsInput(ServiceRequest):
    username: Optional[NonEmptyString]
    token: SensitiveNonEmptyString
    serverType: ServerType
    authType: AuthType
    shouldOverwrite: Optional[WrapperBoolean]


class ImportSourceCredentialsOutput(TypedDict, total=False):
    arn: Optional[NonEmptyString]


class InvalidateProjectCacheInput(ServiceRequest):
    projectName: NonEmptyString


class InvalidateProjectCacheOutput(TypedDict, total=False):
    pass


class ListBuildBatchesForProjectInput(ServiceRequest):
    projectName: Optional[NonEmptyString]
    filter: Optional[BuildBatchFilter]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildBatchesForProjectOutput(TypedDict, total=False):
    ids: Optional[BuildBatchIds]
    nextToken: Optional[String]


class ListBuildBatchesInput(ServiceRequest):
    filter: Optional[BuildBatchFilter]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildBatchesOutput(TypedDict, total=False):
    ids: Optional[BuildBatchIds]
    nextToken: Optional[String]


class ListBuildsForProjectInput(ServiceRequest):
    projectName: NonEmptyString
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildsForProjectOutput(TypedDict, total=False):
    ids: Optional[BuildIds]
    nextToken: Optional[String]


class ListBuildsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListBuildsOutput(TypedDict, total=False):
    ids: Optional[BuildIds]
    nextToken: Optional[String]


class ListCommandExecutionsForSandboxInput(ServiceRequest):
    sandboxId: NonEmptyString
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[SensitiveString]


class ListCommandExecutionsForSandboxOutput(TypedDict, total=False):
    commandExecutions: Optional[CommandExecutions]
    nextToken: Optional[String]


class ListCuratedEnvironmentImagesInput(ServiceRequest):
    pass


class ListCuratedEnvironmentImagesOutput(TypedDict, total=False):
    platforms: Optional[EnvironmentPlatforms]


class ListFleetsInput(ServiceRequest):
    nextToken: Optional[SensitiveString]
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[FleetSortByType]


class ListFleetsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    fleets: Optional[FleetArns]


class ListProjectsInput(ServiceRequest):
    sortBy: Optional[ProjectSortByType]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[NonEmptyString]


class ListProjectsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    projects: Optional[ProjectNames]


class ListReportGroupsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[ReportGroupSortByType]
    nextToken: Optional[String]
    maxResults: Optional[PageSize]


class ListReportGroupsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reportGroups: Optional[ReportGroupArns]


class ReportFilter(TypedDict, total=False):
    """A filter used to return reports with the status specified by the input
    ``status`` parameter.
    """

    status: Optional[ReportStatusType]


class ListReportsForReportGroupInput(ServiceRequest):
    reportGroupArn: String
    nextToken: Optional[String]
    sortOrder: Optional[SortOrderType]
    maxResults: Optional[PageSize]
    filter: Optional[ReportFilter]


class ListReportsForReportGroupOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reports: Optional[ReportArns]


class ListReportsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]
    maxResults: Optional[PageSize]
    filter: Optional[ReportFilter]


class ListReportsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reports: Optional[ReportArns]


class ListSandboxesForProjectInput(ServiceRequest):
    projectName: NonEmptyString
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[SensitiveString]


class ListSandboxesForProjectOutput(TypedDict, total=False):
    ids: Optional[SandboxIds]
    nextToken: Optional[String]


class ListSandboxesInput(ServiceRequest):
    maxResults: Optional[PageSize]
    sortOrder: Optional[SortOrderType]
    nextToken: Optional[String]


class ListSandboxesOutput(TypedDict, total=False):
    ids: Optional[SandboxIds]
    nextToken: Optional[String]


class ListSharedProjectsInput(ServiceRequest):
    sortBy: Optional[SharedResourceSortByType]
    sortOrder: Optional[SortOrderType]
    maxResults: Optional[PageSize]
    nextToken: Optional[NonEmptyString]


ProjectArns = List[NonEmptyString]


class ListSharedProjectsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    projects: Optional[ProjectArns]


class ListSharedReportGroupsInput(ServiceRequest):
    sortOrder: Optional[SortOrderType]
    sortBy: Optional[SharedResourceSortByType]
    nextToken: Optional[String]
    maxResults: Optional[PageSize]


class ListSharedReportGroupsOutput(TypedDict, total=False):
    nextToken: Optional[String]
    reportGroups: Optional[ReportGroupArns]


class ListSourceCredentialsInput(ServiceRequest):
    pass


class SourceCredentialsInfo(TypedDict, total=False):
    """Information about the credentials for a GitHub, GitHub Enterprise,
    GitLab, GitLab Self Managed, or Bitbucket repository.
    """

    arn: Optional[NonEmptyString]
    serverType: Optional[ServerType]
    authType: Optional[AuthType]
    resource: Optional[String]


SourceCredentialsInfos = List[SourceCredentialsInfo]


class ListSourceCredentialsOutput(TypedDict, total=False):
    sourceCredentialsInfos: Optional[SourceCredentialsInfos]


class PutResourcePolicyInput(ServiceRequest):
    policy: NonEmptyString
    resourceArn: NonEmptyString


class PutResourcePolicyOutput(TypedDict, total=False):
    resourceArn: Optional[NonEmptyString]


class RetryBuildBatchInput(ServiceRequest):
    id: Optional[NonEmptyString]
    idempotencyToken: Optional[String]
    retryType: Optional[RetryBuildBatchType]


class RetryBuildBatchOutput(TypedDict, total=False):
    buildBatch: Optional[BuildBatch]


class RetryBuildInput(ServiceRequest):
    id: Optional[NonEmptyString]
    idempotencyToken: Optional[String]


class RetryBuildOutput(TypedDict, total=False):
    build: Optional[Build]


class SSMSession(TypedDict, total=False):
    """Contains information about the Session Manager session."""

    sessionId: Optional[String]
    tokenValue: Optional[String]
    streamUrl: Optional[String]


class StartBuildBatchInput(ServiceRequest):
    projectName: NonEmptyString
    secondarySourcesOverride: Optional[ProjectSources]
    secondarySourcesVersionOverride: Optional[ProjectSecondarySourceVersions]
    sourceVersion: Optional[String]
    artifactsOverride: Optional[ProjectArtifacts]
    secondaryArtifactsOverride: Optional[ProjectArtifactsList]
    environmentVariablesOverride: Optional[EnvironmentVariables]
    sourceTypeOverride: Optional[SourceType]
    sourceLocationOverride: Optional[String]
    sourceAuthOverride: Optional[SourceAuth]
    gitCloneDepthOverride: Optional[GitCloneDepth]
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfig]
    buildspecOverride: Optional[String]
    insecureSslOverride: Optional[WrapperBoolean]
    reportBuildBatchStatusOverride: Optional[WrapperBoolean]
    environmentTypeOverride: Optional[EnvironmentType]
    imageOverride: Optional[NonEmptyString]
    computeTypeOverride: Optional[ComputeType]
    certificateOverride: Optional[String]
    cacheOverride: Optional[ProjectCache]
    serviceRoleOverride: Optional[NonEmptyString]
    privilegedModeOverride: Optional[WrapperBoolean]
    buildTimeoutInMinutesOverride: Optional[BuildTimeOut]
    queuedTimeoutInMinutesOverride: Optional[TimeOut]
    encryptionKeyOverride: Optional[NonEmptyString]
    idempotencyToken: Optional[String]
    logsConfigOverride: Optional[LogsConfig]
    registryCredentialOverride: Optional[RegistryCredential]
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsType]
    buildBatchConfigOverride: Optional[ProjectBuildBatchConfig]
    debugSessionEnabled: Optional[WrapperBoolean]


class StartBuildBatchOutput(TypedDict, total=False):
    buildBatch: Optional[BuildBatch]


class StartBuildInput(ServiceRequest):
    projectName: NonEmptyString
    secondarySourcesOverride: Optional[ProjectSources]
    secondarySourcesVersionOverride: Optional[ProjectSecondarySourceVersions]
    sourceVersion: Optional[String]
    artifactsOverride: Optional[ProjectArtifacts]
    secondaryArtifactsOverride: Optional[ProjectArtifactsList]
    environmentVariablesOverride: Optional[EnvironmentVariables]
    sourceTypeOverride: Optional[SourceType]
    sourceLocationOverride: Optional[String]
    sourceAuthOverride: Optional[SourceAuth]
    gitCloneDepthOverride: Optional[GitCloneDepth]
    gitSubmodulesConfigOverride: Optional[GitSubmodulesConfig]
    buildspecOverride: Optional[String]
    insecureSslOverride: Optional[WrapperBoolean]
    reportBuildStatusOverride: Optional[WrapperBoolean]
    buildStatusConfigOverride: Optional[BuildStatusConfig]
    environmentTypeOverride: Optional[EnvironmentType]
    imageOverride: Optional[NonEmptyString]
    computeTypeOverride: Optional[ComputeType]
    certificateOverride: Optional[String]
    cacheOverride: Optional[ProjectCache]
    serviceRoleOverride: Optional[NonEmptyString]
    privilegedModeOverride: Optional[WrapperBoolean]
    timeoutInMinutesOverride: Optional[BuildTimeOut]
    queuedTimeoutInMinutesOverride: Optional[TimeOut]
    encryptionKeyOverride: Optional[NonEmptyString]
    idempotencyToken: Optional[String]
    logsConfigOverride: Optional[LogsConfig]
    registryCredentialOverride: Optional[RegistryCredential]
    imagePullCredentialsTypeOverride: Optional[ImagePullCredentialsType]
    debugSessionEnabled: Optional[WrapperBoolean]
    fleetOverride: Optional[ProjectFleet]
    autoRetryLimitOverride: Optional[WrapperInt]


class StartBuildOutput(TypedDict, total=False):
    build: Optional[Build]


StartCommandExecutionInput = TypedDict(
    "StartCommandExecutionInput",
    {
        "sandboxId": NonEmptyString,
        "command": SensitiveNonEmptyString,
        "type": Optional[CommandType],
    },
    total=False,
)


class StartCommandExecutionOutput(TypedDict, total=False):
    commandExecution: Optional[CommandExecution]


class StartSandboxConnectionInput(ServiceRequest):
    sandboxId: NonEmptyString


class StartSandboxConnectionOutput(TypedDict, total=False):
    ssmSession: Optional[SSMSession]


class StartSandboxInput(ServiceRequest):
    projectName: Optional[NonEmptyString]
    idempotencyToken: Optional[SensitiveString]


class StartSandboxOutput(TypedDict, total=False):
    sandbox: Optional[Sandbox]


class StopBuildBatchInput(ServiceRequest):
    id: NonEmptyString


class StopBuildBatchOutput(TypedDict, total=False):
    buildBatch: Optional[BuildBatch]


class StopBuildInput(ServiceRequest):
    id: NonEmptyString


class StopBuildOutput(TypedDict, total=False):
    build: Optional[Build]


class StopSandboxInput(ServiceRequest):
    id: NonEmptyString


class StopSandboxOutput(TypedDict, total=False):
    sandbox: Optional[Sandbox]


class UpdateFleetInput(ServiceRequest):
    arn: NonEmptyString
    baseCapacity: Optional[FleetCapacity]
    environmentType: Optional[EnvironmentType]
    computeType: Optional[ComputeType]
    computeConfiguration: Optional[ComputeConfiguration]
    scalingConfiguration: Optional[ScalingConfigurationInput]
    overflowBehavior: Optional[FleetOverflowBehavior]
    vpcConfig: Optional[VpcConfig]
    proxyConfiguration: Optional[ProxyConfiguration]
    imageId: Optional[NonEmptyString]
    fleetServiceRole: Optional[NonEmptyString]
    tags: Optional[TagList]


class UpdateFleetOutput(TypedDict, total=False):
    fleet: Optional[Fleet]


class UpdateProjectInput(ServiceRequest):
    name: NonEmptyString
    description: Optional[ProjectDescription]
    source: Optional[ProjectSource]
    secondarySources: Optional[ProjectSources]
    sourceVersion: Optional[String]
    secondarySourceVersions: Optional[ProjectSecondarySourceVersions]
    artifacts: Optional[ProjectArtifacts]
    secondaryArtifacts: Optional[ProjectArtifactsList]
    cache: Optional[ProjectCache]
    environment: Optional[ProjectEnvironment]
    serviceRole: Optional[NonEmptyString]
    timeoutInMinutes: Optional[BuildTimeOut]
    queuedTimeoutInMinutes: Optional[TimeOut]
    encryptionKey: Optional[NonEmptyString]
    tags: Optional[TagList]
    vpcConfig: Optional[VpcConfig]
    badgeEnabled: Optional[WrapperBoolean]
    logsConfig: Optional[LogsConfig]
    fileSystemLocations: Optional[ProjectFileSystemLocations]
    buildBatchConfig: Optional[ProjectBuildBatchConfig]
    concurrentBuildLimit: Optional[WrapperInt]
    autoRetryLimit: Optional[WrapperInt]


class UpdateProjectOutput(TypedDict, total=False):
    project: Optional[Project]


class UpdateProjectVisibilityInput(ServiceRequest):
    projectArn: NonEmptyString
    projectVisibility: ProjectVisibilityType
    resourceAccessRole: Optional[NonEmptyString]


class UpdateProjectVisibilityOutput(TypedDict, total=False):
    projectArn: Optional[NonEmptyString]
    publicProjectAlias: Optional[NonEmptyString]
    projectVisibility: Optional[ProjectVisibilityType]


class UpdateReportGroupInput(ServiceRequest):
    arn: NonEmptyString
    exportConfig: Optional[ReportExportConfig]
    tags: Optional[TagList]


class UpdateReportGroupOutput(TypedDict, total=False):
    reportGroup: Optional[ReportGroup]


class UpdateWebhookInput(ServiceRequest):
    projectName: ProjectName
    branchFilter: Optional[String]
    rotateSecret: Optional[Boolean]
    filterGroups: Optional[FilterGroups]
    buildType: Optional[WebhookBuildType]


class UpdateWebhookOutput(TypedDict, total=False):
    webhook: Optional[Webhook]


class CodebuildApi:
    service = "codebuild"
    version = "2016-10-06"

    @handler("BatchDeleteBuilds")
    def batch_delete_builds(
        self, context: RequestContext, ids: BuildIds, **kwargs
    ) -> BatchDeleteBuildsOutput:
        """Deletes one or more builds.

        :param ids: The IDs of the builds to delete.
        :returns: BatchDeleteBuildsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetBuildBatches")
    def batch_get_build_batches(
        self, context: RequestContext, ids: BuildBatchIds, **kwargs
    ) -> BatchGetBuildBatchesOutput:
        """Retrieves information about one or more batch builds.

        :param ids: An array that contains the batch build identifiers to retrieve.
        :returns: BatchGetBuildBatchesOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetBuilds")
    def batch_get_builds(
        self, context: RequestContext, ids: BuildIds, **kwargs
    ) -> BatchGetBuildsOutput:
        """Gets information about one or more builds.

        :param ids: The IDs of the builds.
        :returns: BatchGetBuildsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetCommandExecutions")
    def batch_get_command_executions(
        self,
        context: RequestContext,
        sandbox_id: NonEmptyString,
        command_execution_ids: CommandExecutionIds,
        **kwargs,
    ) -> BatchGetCommandExecutionsOutput:
        """Gets information about the command executions.

        :param sandbox_id: A ``sandboxId`` or ``sandboxArn``.
        :param command_execution_ids: A comma separated list of ``commandExecutionIds``.
        :returns: BatchGetCommandExecutionsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetFleets")
    def batch_get_fleets(
        self, context: RequestContext, names: FleetNames, **kwargs
    ) -> BatchGetFleetsOutput:
        """Gets information about one or more compute fleets.

        :param names: The names or ARNs of the compute fleets.
        :returns: BatchGetFleetsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetProjects")
    def batch_get_projects(
        self, context: RequestContext, names: ProjectNames, **kwargs
    ) -> BatchGetProjectsOutput:
        """Gets information about one or more build projects.

        :param names: The names or ARNs of the build projects.
        :returns: BatchGetProjectsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetReportGroups")
    def batch_get_report_groups(
        self, context: RequestContext, report_group_arns: ReportGroupArns, **kwargs
    ) -> BatchGetReportGroupsOutput:
        """Returns an array of report groups.

        :param report_group_arns: An array of report group ARNs that identify the report groups to return.
        :returns: BatchGetReportGroupsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetReports")
    def batch_get_reports(
        self, context: RequestContext, report_arns: ReportArns, **kwargs
    ) -> BatchGetReportsOutput:
        """Returns an array of reports.

        :param report_arns: An array of ARNs that identify the ``Report`` objects to return.
        :returns: BatchGetReportsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetSandboxes")
    def batch_get_sandboxes(
        self, context: RequestContext, ids: SandboxIds, **kwargs
    ) -> BatchGetSandboxesOutput:
        """Gets information about the sandbox status.

        :param ids: A comma separated list of ``sandboxIds`` or ``sandboxArns``.
        :returns: BatchGetSandboxesOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("CreateFleet")
    def create_fleet(
        self,
        context: RequestContext,
        name: FleetName,
        base_capacity: FleetCapacity,
        environment_type: EnvironmentType,
        compute_type: ComputeType,
        compute_configuration: ComputeConfiguration | None = None,
        scaling_configuration: ScalingConfigurationInput | None = None,
        overflow_behavior: FleetOverflowBehavior | None = None,
        vpc_config: VpcConfig | None = None,
        proxy_configuration: ProxyConfiguration | None = None,
        image_id: NonEmptyString | None = None,
        fleet_service_role: NonEmptyString | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateFleetOutput:
        """Creates a compute fleet.

        :param name: The name of the compute fleet.
        :param base_capacity: The initial number of machines allocated to the ﬂeet, which deﬁnes the
        number of builds that can run in parallel.
        :param environment_type: The environment type of the compute fleet.
        :param compute_type: Information about the compute resources the compute fleet uses.
        :param compute_configuration: The compute configuration of the compute fleet.
        :param scaling_configuration: The scaling configuration of the compute fleet.
        :param overflow_behavior: The compute fleet overflow behavior.
        :param vpc_config: Information about the VPC configuration that CodeBuild accesses.
        :param proxy_configuration: The proxy configuration of the compute fleet.
        :param image_id: The Amazon Machine Image (AMI) of the compute fleet.
        :param fleet_service_role: The service role associated with the compute fleet.
        :param tags: A list of tag key and value pairs associated with this compute fleet.
        :returns: CreateFleetOutput
        :raises InvalidInputException:
        :raises ResourceAlreadyExistsException:
        :raises AccountLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateProject")
    def create_project(
        self,
        context: RequestContext,
        name: ProjectName,
        source: ProjectSource,
        artifacts: ProjectArtifacts,
        environment: ProjectEnvironment,
        service_role: NonEmptyString,
        description: ProjectDescription | None = None,
        secondary_sources: ProjectSources | None = None,
        source_version: String | None = None,
        secondary_source_versions: ProjectSecondarySourceVersions | None = None,
        secondary_artifacts: ProjectArtifactsList | None = None,
        cache: ProjectCache | None = None,
        timeout_in_minutes: BuildTimeOut | None = None,
        queued_timeout_in_minutes: TimeOut | None = None,
        encryption_key: NonEmptyString | None = None,
        tags: TagList | None = None,
        vpc_config: VpcConfig | None = None,
        badge_enabled: WrapperBoolean | None = None,
        logs_config: LogsConfig | None = None,
        file_system_locations: ProjectFileSystemLocations | None = None,
        build_batch_config: ProjectBuildBatchConfig | None = None,
        concurrent_build_limit: WrapperInt | None = None,
        auto_retry_limit: WrapperInt | None = None,
        **kwargs,
    ) -> CreateProjectOutput:
        """Creates a build project.

        :param name: The name of the build project.
        :param source: Information about the build input source code for the build project.
        :param artifacts: Information about the build output artifacts for the build project.
        :param environment: Information about the build environment for the build project.
        :param service_role: The ARN of the IAM role that enables CodeBuild to interact with
        dependent Amazon Web Services services on behalf of the Amazon Web
        Services account.
        :param description: A description that makes the build project easy to identify.
        :param secondary_sources: An array of ``ProjectSource`` objects.
        :param source_version: A version of the build input to be built for this project.
        :param secondary_source_versions: An array of ``ProjectSourceVersion`` objects.
        :param secondary_artifacts: An array of ``ProjectArtifacts`` objects.
        :param cache: Stores recently used information so that it can be quickly accessed at a
        later time.
        :param timeout_in_minutes: How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait
        before it times out any build that has not been marked as completed.
        :param queued_timeout_in_minutes: The number of minutes a build is allowed to be queued before it times
        out.
        :param encryption_key: The Key Management Service customer master key (CMK) to be used for
        encrypting the build output artifacts.
        :param tags: A list of tag key and value pairs associated with this build project.
        :param vpc_config: VpcConfig enables CodeBuild to access resources in an Amazon VPC.
        :param badge_enabled: Set this to true to generate a publicly accessible URL for your
        project's build badge.
        :param logs_config: Information about logs for the build project.
        :param file_system_locations: An array of ``ProjectFileSystemLocation`` objects for a CodeBuild build
        project.
        :param build_batch_config: A ProjectBuildBatchConfig object that defines the batch build options
        for the project.
        :param concurrent_build_limit: The maximum number of concurrent builds that are allowed for this
        project.
        :param auto_retry_limit: The maximum number of additional automatic retries after a failed build.
        :returns: CreateProjectOutput
        :raises InvalidInputException:
        :raises ResourceAlreadyExistsException:
        :raises AccountLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateReportGroup", expand=False)
    def create_report_group(
        self, context: RequestContext, request: CreateReportGroupInput, **kwargs
    ) -> CreateReportGroupOutput:
        """Creates a report group. A report group contains a collection of reports.

        :param name: The name of the report group.
        :param type: The type of report group.
        :param export_config: A ``ReportExportConfig`` object that contains information about where
        the report group test results are exported.
        :param tags: A list of tag key and value pairs associated with this report group.
        :returns: CreateReportGroupOutput
        :raises InvalidInputException:
        :raises ResourceAlreadyExistsException:
        :raises AccountLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateWebhook")
    def create_webhook(
        self,
        context: RequestContext,
        project_name: ProjectName,
        branch_filter: String | None = None,
        filter_groups: FilterGroups | None = None,
        build_type: WebhookBuildType | None = None,
        manual_creation: WrapperBoolean | None = None,
        scope_configuration: ScopeConfiguration | None = None,
        **kwargs,
    ) -> CreateWebhookOutput:
        """For an existing CodeBuild build project that has its source code stored
        in a GitHub or Bitbucket repository, enables CodeBuild to start
        rebuilding the source code every time a code change is pushed to the
        repository.

        If you enable webhooks for an CodeBuild project, and the project is used
        as a build step in CodePipeline, then two identical builds are created
        for each commit. One build is triggered through webhooks, and one
        through CodePipeline. Because billing is on a per-build basis, you are
        billed for both builds. Therefore, if you are using CodePipeline, we
        recommend that you disable webhooks in CodeBuild. In the CodeBuild
        console, clear the Webhook box. For more information, see step 5 in
        `Change a Build Project's
        Settings <https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console>`__.

        :param project_name: The name of the CodeBuild project.
        :param branch_filter: A regular expression used to determine which repository branches are
        built when a webhook is triggered.
        :param filter_groups: An array of arrays of ``WebhookFilter`` objects used to determine which
        webhooks are triggered.
        :param build_type: Specifies the type of build this webhook will trigger.
        :param manual_creation: If manualCreation is true, CodeBuild doesn't create a webhook in GitHub
        and instead returns ``payloadUrl`` and ``secret`` values for the
        webhook.
        :param scope_configuration: The scope configuration for global or organization webhooks.
        :returns: CreateWebhookOutput
        :raises InvalidInputException:
        :raises OAuthProviderException:
        :raises ResourceAlreadyExistsException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteBuildBatch")
    def delete_build_batch(
        self, context: RequestContext, id: NonEmptyString, **kwargs
    ) -> DeleteBuildBatchOutput:
        """Deletes a batch build.

        :param id: The identifier of the batch build to delete.
        :returns: DeleteBuildBatchOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteFleet")
    def delete_fleet(
        self, context: RequestContext, arn: NonEmptyString, **kwargs
    ) -> DeleteFleetOutput:
        """Deletes a compute fleet. When you delete a compute fleet, its builds are
        not deleted.

        :param arn: The ARN of the compute fleet.
        :returns: DeleteFleetOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteProject")
    def delete_project(
        self, context: RequestContext, name: NonEmptyString, **kwargs
    ) -> DeleteProjectOutput:
        """Deletes a build project. When you delete a project, its builds are not
        deleted.

        :param name: The name of the build project.
        :returns: DeleteProjectOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteReport")
    def delete_report(
        self, context: RequestContext, arn: NonEmptyString, **kwargs
    ) -> DeleteReportOutput:
        """Deletes a report.

        :param arn: The ARN of the report to delete.
        :returns: DeleteReportOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteReportGroup")
    def delete_report_group(
        self,
        context: RequestContext,
        arn: NonEmptyString,
        delete_reports: Boolean | None = None,
        **kwargs,
    ) -> DeleteReportGroupOutput:
        """Deletes a report group. Before you delete a report group, you must
        delete its reports.

        :param arn: The ARN of the report group to delete.
        :param delete_reports: If ``true``, deletes any reports that belong to a report group before
        deleting the report group.
        :returns: DeleteReportGroupOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteResourcePolicy")
    def delete_resource_policy(
        self, context: RequestContext, resource_arn: NonEmptyString, **kwargs
    ) -> DeleteResourcePolicyOutput:
        """Deletes a resource policy that is identified by its resource ARN.

        :param resource_arn: The ARN of the resource that is associated with the resource policy.
        :returns: DeleteResourcePolicyOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteSourceCredentials")
    def delete_source_credentials(
        self, context: RequestContext, arn: NonEmptyString, **kwargs
    ) -> DeleteSourceCredentialsOutput:
        """Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source
        credentials.

        :param arn: The Amazon Resource Name (ARN) of the token.
        :returns: DeleteSourceCredentialsOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteWebhook")
    def delete_webhook(
        self, context: RequestContext, project_name: ProjectName, **kwargs
    ) -> DeleteWebhookOutput:
        """For an existing CodeBuild build project that has its source code stored
        in a GitHub or Bitbucket repository, stops CodeBuild from rebuilding the
        source code every time a code change is pushed to the repository.

        :param project_name: The name of the CodeBuild project.
        :returns: DeleteWebhookOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises OAuthProviderException:
        """
        raise NotImplementedError

    @handler("DescribeCodeCoverages")
    def describe_code_coverages(
        self,
        context: RequestContext,
        report_arn: NonEmptyString,
        next_token: String | None = None,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        sort_by: ReportCodeCoverageSortByType | None = None,
        min_line_coverage_percentage: Percentage | None = None,
        max_line_coverage_percentage: Percentage | None = None,
        **kwargs,
    ) -> DescribeCodeCoveragesOutput:
        """Retrieves one or more code coverage reports.

        :param report_arn: The ARN of the report for which test cases are returned.
        :param next_token: The ``nextToken`` value returned from a previous call to
        ``DescribeCodeCoverages``.
        :param max_results: The maximum number of results to return.
        :param sort_order: Specifies if the results are sorted in ascending or descending order.
        :param sort_by: Specifies how the results are sorted.
        :param min_line_coverage_percentage: The minimum line coverage percentage to report.
        :param max_line_coverage_percentage: The maximum line coverage percentage to report.
        :returns: DescribeCodeCoveragesOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DescribeTestCases")
    def describe_test_cases(
        self,
        context: RequestContext,
        report_arn: String,
        next_token: String | None = None,
        max_results: PageSize | None = None,
        filter: TestCaseFilter | None = None,
        **kwargs,
    ) -> DescribeTestCasesOutput:
        """Returns a list of details about test cases for a report.

        :param report_arn: The ARN of the report for which test cases are returned.
        :param next_token: During a previous call, the maximum number of items that can be returned
        is the value specified in ``maxResults``.
        :param max_results: The maximum number of paginated test cases returned per response.
        :param filter: A ``TestCaseFilter`` object used to filter the returned reports.
        :returns: DescribeTestCasesOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetReportGroupTrend")
    def get_report_group_trend(
        self,
        context: RequestContext,
        report_group_arn: NonEmptyString,
        trend_field: ReportGroupTrendFieldType,
        num_of_reports: PageSize | None = None,
        **kwargs,
    ) -> GetReportGroupTrendOutput:
        """Analyzes and accumulates test report values for the specified test
        reports.

        :param report_group_arn: The ARN of the report group that contains the reports to analyze.
        :param trend_field: The test report value to accumulate.
        :param num_of_reports: The number of reports to analyze.
        :returns: GetReportGroupTrendOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetResourcePolicy")
    def get_resource_policy(
        self, context: RequestContext, resource_arn: NonEmptyString, **kwargs
    ) -> GetResourcePolicyOutput:
        """Gets a resource policy that is identified by its resource ARN.

        :param resource_arn: The ARN of the resource that is associated with the resource policy.
        :returns: GetResourcePolicyOutput
        :raises ResourceNotFoundException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ImportSourceCredentials")
    def import_source_credentials(
        self,
        context: RequestContext,
        token: SensitiveNonEmptyString,
        server_type: ServerType,
        auth_type: AuthType,
        username: NonEmptyString | None = None,
        should_overwrite: WrapperBoolean | None = None,
        **kwargs,
    ) -> ImportSourceCredentialsOutput:
        """Imports the source repository credentials for an CodeBuild project that
        has its source code stored in a GitHub, GitHub Enterprise, GitLab,
        GitLab Self Managed, or Bitbucket repository.

        :param token: For GitHub or GitHub Enterprise, this is the personal access token.
        :param server_type: The source provider used for this project.
        :param auth_type: The type of authentication used to connect to a GitHub, GitHub
        Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository.
        :param username: The Bitbucket username when the ``authType`` is BASIC_AUTH.
        :param should_overwrite: Set to ``false`` to prevent overwriting the repository source
        credentials.
        :returns: ImportSourceCredentialsOutput
        :raises InvalidInputException:
        :raises AccountLimitExceededException:
        :raises ResourceAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("InvalidateProjectCache")
    def invalidate_project_cache(
        self, context: RequestContext, project_name: NonEmptyString, **kwargs
    ) -> InvalidateProjectCacheOutput:
        """Resets the cache for a project.

        :param project_name: The name of the CodeBuild build project that the cache is reset for.
        :returns: InvalidateProjectCacheOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListBuildBatches")
    def list_build_batches(
        self,
        context: RequestContext,
        filter: BuildBatchFilter | None = None,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListBuildBatchesOutput:
        """Retrieves the identifiers of your build batches in the current region.

        :param filter: A ``BuildBatchFilter`` object that specifies the filters for the search.
        :param max_results: The maximum number of results to return.
        :param sort_order: Specifies the sort order of the returned items.
        :param next_token: The ``nextToken`` value returned from a previous call to
        ``ListBuildBatches``.
        :returns: ListBuildBatchesOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListBuildBatchesForProject")
    def list_build_batches_for_project(
        self,
        context: RequestContext,
        project_name: NonEmptyString | None = None,
        filter: BuildBatchFilter | None = None,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListBuildBatchesForProjectOutput:
        """Retrieves the identifiers of the build batches for a specific project.

        :param project_name: The name of the project.
        :param filter: A ``BuildBatchFilter`` object that specifies the filters for the search.
        :param max_results: The maximum number of results to return.
        :param sort_order: Specifies the sort order of the returned items.
        :param next_token: The ``nextToken`` value returned from a previous call to
        ``ListBuildBatchesForProject``.
        :returns: ListBuildBatchesForProjectOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListBuilds")
    def list_builds(
        self,
        context: RequestContext,
        sort_order: SortOrderType | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListBuildsOutput:
        """Gets a list of build IDs, with each build ID representing a single
        build.

        :param sort_order: The order to list build IDs.
        :param next_token: During a previous call, if there are more than 100 items in the list,
        only the first 100 items are returned, along with a unique string called
        a *nextToken*.
        :returns: ListBuildsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListBuildsForProject")
    def list_builds_for_project(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        sort_order: SortOrderType | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListBuildsForProjectOutput:
        """Gets a list of build identifiers for the specified build project, with
        each build identifier representing a single build.

        :param project_name: The name of the CodeBuild project.
        :param sort_order: The order to sort the results in.
        :param next_token: During a previous call, if there are more than 100 items in the list,
        only the first 100 items are returned, along with a unique string called
        a *nextToken*.
        :returns: ListBuildsForProjectOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListCommandExecutionsForSandbox")
    def list_command_executions_for_sandbox(
        self,
        context: RequestContext,
        sandbox_id: NonEmptyString,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        next_token: SensitiveString | None = None,
        **kwargs,
    ) -> ListCommandExecutionsForSandboxOutput:
        """Gets a list of command executions for a sandbox.

        :param sandbox_id: A ``sandboxId`` or ``sandboxArn``.
        :param max_results: The maximum number of sandbox records to be retrieved.
        :param sort_order: The order in which sandbox records should be retrieved.
        :param next_token: The next token, if any, to get paginated results.
        :returns: ListCommandExecutionsForSandboxOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListCuratedEnvironmentImages")
    def list_curated_environment_images(
        self, context: RequestContext, **kwargs
    ) -> ListCuratedEnvironmentImagesOutput:
        """Gets information about Docker images that are managed by CodeBuild.

        :returns: ListCuratedEnvironmentImagesOutput
        """
        raise NotImplementedError

    @handler("ListFleets")
    def list_fleets(
        self,
        context: RequestContext,
        next_token: SensitiveString | None = None,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        sort_by: FleetSortByType | None = None,
        **kwargs,
    ) -> ListFleetsOutput:
        """Gets a list of compute fleet names with each compute fleet name
        representing a single compute fleet.

        :param next_token: During a previous call, if there are more than 100 items in the list,
        only the first 100 items are returned, along with a unique string called
        a *nextToken*.
        :param max_results: The maximum number of paginated compute fleets returned per response.
        :param sort_order: The order in which to list compute fleets.
        :param sort_by: The criterion to be used to list compute fleet names.
        :returns: ListFleetsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListProjects")
    def list_projects(
        self,
        context: RequestContext,
        sort_by: ProjectSortByType | None = None,
        sort_order: SortOrderType | None = None,
        next_token: NonEmptyString | None = None,
        **kwargs,
    ) -> ListProjectsOutput:
        """Gets a list of build project names, with each build project name
        representing a single build project.

        :param sort_by: The criterion to be used to list build project names.
        :param sort_order: The order in which to list build projects.
        :param next_token: During a previous call, if there are more than 100 items in the list,
        only the first 100 items are returned, along with a unique string called
        a *nextToken*.
        :returns: ListProjectsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListReportGroups")
    def list_report_groups(
        self,
        context: RequestContext,
        sort_order: SortOrderType | None = None,
        sort_by: ReportGroupSortByType | None = None,
        next_token: String | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> ListReportGroupsOutput:
        """Gets a list ARNs for the report groups in the current Amazon Web
        Services account.

        :param sort_order: Used to specify the order to sort the list of returned report groups.
        :param sort_by: The criterion to be used to list build report groups.
        :param next_token: During a previous call, the maximum number of items that can be returned
        is the value specified in ``maxResults``.
        :param max_results: The maximum number of paginated report groups returned per response.
        :returns: ListReportGroupsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListReports")
    def list_reports(
        self,
        context: RequestContext,
        sort_order: SortOrderType | None = None,
        next_token: String | None = None,
        max_results: PageSize | None = None,
        filter: ReportFilter | None = None,
        **kwargs,
    ) -> ListReportsOutput:
        """Returns a list of ARNs for the reports in the current Amazon Web
        Services account.

        :param sort_order: Specifies the sort order for the list of returned reports.
        :param next_token: During a previous call, the maximum number of items that can be returned
        is the value specified in ``maxResults``.
        :param max_results: The maximum number of paginated reports returned per response.
        :param filter: A ``ReportFilter`` object used to filter the returned reports.
        :returns: ListReportsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListReportsForReportGroup")
    def list_reports_for_report_group(
        self,
        context: RequestContext,
        report_group_arn: String,
        next_token: String | None = None,
        sort_order: SortOrderType | None = None,
        max_results: PageSize | None = None,
        filter: ReportFilter | None = None,
        **kwargs,
    ) -> ListReportsForReportGroupOutput:
        """Returns a list of ARNs for the reports that belong to a ``ReportGroup``.

        :param report_group_arn: The ARN of the report group for which you want to return report ARNs.
        :param next_token: During a previous call, the maximum number of items that can be returned
        is the value specified in ``maxResults``.
        :param sort_order: Use to specify whether the results are returned in ascending or
        descending order.
        :param max_results: The maximum number of paginated reports in this report group returned
        per response.
        :param filter: A ``ReportFilter`` object used to filter the returned reports.
        :returns: ListReportsForReportGroupOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListSandboxes")
    def list_sandboxes(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListSandboxesOutput:
        """Gets a list of sandboxes.

        :param max_results: The maximum number of sandbox records to be retrieved.
        :param sort_order: The order in which sandbox records should be retrieved.
        :param next_token: The next token, if any, to get paginated results.
        :returns: ListSandboxesOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListSandboxesForProject")
    def list_sandboxes_for_project(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        max_results: PageSize | None = None,
        sort_order: SortOrderType | None = None,
        next_token: SensitiveString | None = None,
        **kwargs,
    ) -> ListSandboxesForProjectOutput:
        """Gets a list of sandboxes for a given project.

        :param project_name: The CodeBuild project name.
        :param max_results: The maximum number of sandbox records to be retrieved.
        :param sort_order: The order in which sandbox records should be retrieved.
        :param next_token: The next token, if any, to get paginated results.
        :returns: ListSandboxesForProjectOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListSharedProjects")
    def list_shared_projects(
        self,
        context: RequestContext,
        sort_by: SharedResourceSortByType | None = None,
        sort_order: SortOrderType | None = None,
        max_results: PageSize | None = None,
        next_token: NonEmptyString | None = None,
        **kwargs,
    ) -> ListSharedProjectsOutput:
        """Gets a list of projects that are shared with other Amazon Web Services
        accounts or users.

        :param sort_by: The criterion to be used to list build projects shared with the current
        Amazon Web Services account or user.
        :param sort_order: The order in which to list shared build projects.
        :param max_results: The maximum number of paginated shared build projects returned per
        response.
        :param next_token: During a previous call, the maximum number of items that can be returned
        is the value specified in ``maxResults``.
        :returns: ListSharedProjectsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListSharedReportGroups")
    def list_shared_report_groups(
        self,
        context: RequestContext,
        sort_order: SortOrderType | None = None,
        sort_by: SharedResourceSortByType | None = None,
        next_token: String | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> ListSharedReportGroupsOutput:
        """Gets a list of report groups that are shared with other Amazon Web
        Services accounts or users.

        :param sort_order: The order in which to list shared report groups.
        :param sort_by: The criterion to be used to list report groups shared with the current
        Amazon Web Services account or user.
        :param next_token: During a previous call, the maximum number of items that can be returned
        is the value specified in ``maxResults``.
        :param max_results: The maximum number of paginated shared report groups per response.
        :returns: ListSharedReportGroupsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListSourceCredentials")
    def list_source_credentials(
        self, context: RequestContext, **kwargs
    ) -> ListSourceCredentialsOutput:
        """Returns a list of ``SourceCredentialsInfo`` objects.

        :returns: ListSourceCredentialsOutput
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("PutResourcePolicy")
    def put_resource_policy(
        self,
        context: RequestContext,
        policy: NonEmptyString,
        resource_arn: NonEmptyString,
        **kwargs,
    ) -> PutResourcePolicyOutput:
        """Stores a resource policy for the ARN of a ``Project`` or ``ReportGroup``
        object.

        :param policy: A JSON-formatted resource policy.
        :param resource_arn: The ARN of the ``Project`` or ``ReportGroup`` resource you want to
        associate with a resource policy.
        :returns: PutResourcePolicyOutput
        :raises ResourceNotFoundException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("RetryBuild")
    def retry_build(
        self,
        context: RequestContext,
        id: NonEmptyString | None = None,
        idempotency_token: String | None = None,
        **kwargs,
    ) -> RetryBuildOutput:
        """Restarts a build.

        :param id: Specifies the identifier of the build to restart.
        :param idempotency_token: A unique, case sensitive identifier you provide to ensure the
        idempotency of the ``RetryBuild`` request.
        :returns: RetryBuildOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises AccountLimitExceededException:
        """
        raise NotImplementedError

    @handler("RetryBuildBatch")
    def retry_build_batch(
        self,
        context: RequestContext,
        id: NonEmptyString | None = None,
        idempotency_token: String | None = None,
        retry_type: RetryBuildBatchType | None = None,
        **kwargs,
    ) -> RetryBuildBatchOutput:
        """Restarts a failed batch build. Only batch builds that have failed can be
        retried.

        :param id: Specifies the identifier of the batch build to restart.
        :param idempotency_token: A unique, case sensitive identifier you provide to ensure the
        idempotency of the ``RetryBuildBatch`` request.
        :param retry_type: Specifies the type of retry to perform.
        :returns: RetryBuildBatchOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StartBuild")
    def start_build(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        secondary_sources_override: ProjectSources | None = None,
        secondary_sources_version_override: ProjectSecondarySourceVersions | None = None,
        source_version: String | None = None,
        artifacts_override: ProjectArtifacts | None = None,
        secondary_artifacts_override: ProjectArtifactsList | None = None,
        environment_variables_override: EnvironmentVariables | None = None,
        source_type_override: SourceType | None = None,
        source_location_override: String | None = None,
        source_auth_override: SourceAuth | None = None,
        git_clone_depth_override: GitCloneDepth | None = None,
        git_submodules_config_override: GitSubmodulesConfig | None = None,
        buildspec_override: String | None = None,
        insecure_ssl_override: WrapperBoolean | None = None,
        report_build_status_override: WrapperBoolean | None = None,
        build_status_config_override: BuildStatusConfig | None = None,
        environment_type_override: EnvironmentType | None = None,
        image_override: NonEmptyString | None = None,
        compute_type_override: ComputeType | None = None,
        certificate_override: String | None = None,
        cache_override: ProjectCache | None = None,
        service_role_override: NonEmptyString | None = None,
        privileged_mode_override: WrapperBoolean | None = None,
        timeout_in_minutes_override: BuildTimeOut | None = None,
        queued_timeout_in_minutes_override: TimeOut | None = None,
        encryption_key_override: NonEmptyString | None = None,
        idempotency_token: String | None = None,
        logs_config_override: LogsConfig | None = None,
        registry_credential_override: RegistryCredential | None = None,
        image_pull_credentials_type_override: ImagePullCredentialsType | None = None,
        debug_session_enabled: WrapperBoolean | None = None,
        fleet_override: ProjectFleet | None = None,
        auto_retry_limit_override: WrapperInt | None = None,
        **kwargs,
    ) -> StartBuildOutput:
        """Starts running a build with the settings defined in the project. These
        setting include: how to run a build, where to get the source code, which
        build environment to use, which build commands to run, and where to
        store the build output.

        You can also start a build run by overriding some of the build settings
        in the project. The overrides only apply for that specific start build
        request. The settings in the project are unaltered.

        :param project_name: The name of the CodeBuild build project to start running a build.
        :param secondary_sources_override: An array of ``ProjectSource`` objects.
        :param secondary_sources_version_override: An array of ``ProjectSourceVersion`` objects that specify one or more
        versions of the project's secondary sources to be used for this build
        only.
        :param source_version: The version of the build input to be built, for this build only.
        :param artifacts_override: Build output artifact settings that override, for this build only, the
        latest ones already defined in the build project.
        :param secondary_artifacts_override: An array of ``ProjectArtifacts`` objects.
        :param environment_variables_override: A set of environment variables that overrides, for this build only, the
        latest ones already defined in the build project.
        :param source_type_override: A source input type, for this build, that overrides the source input
        defined in the build project.
        :param source_location_override: A location that overrides, for this build, the source location for the
        one defined in the build project.
        :param source_auth_override: An authorization type for this build that overrides the one defined in
        the build project.
        :param git_clone_depth_override: The user-defined depth of history, with a minimum value of 0, that
        overrides, for this build only, any previous depth of history defined in
        the build project.
        :param git_submodules_config_override: Information about the Git submodules configuration for this build of an
        CodeBuild build project.
        :param buildspec_override: A buildspec file declaration that overrides the latest one defined in
        the build project, for this build only.
        :param insecure_ssl_override: Enable this flag to override the insecure SSL setting that is specified
        in the build project.
        :param report_build_status_override: Set to true to report to your source provider the status of a build's
        start and completion.
        :param build_status_config_override: Contains information that defines how the build project reports the
        build status to the source provider.
        :param environment_type_override: A container type for this build that overrides the one specified in the
        build project.
        :param image_override: The name of an image for this build that overrides the one specified in
        the build project.
        :param compute_type_override: The name of a compute type for this build that overrides the one
        specified in the build project.
        :param certificate_override: The name of a certificate for this build that overrides the one
        specified in the build project.
        :param cache_override: A ProjectCache object specified for this build that overrides the one
        defined in the build project.
        :param service_role_override: The name of a service role for this build that overrides the one
        specified in the build project.
        :param privileged_mode_override: Enable this flag to override privileged mode in the build project.
        :param timeout_in_minutes_override: The number of build timeout minutes, from 5 to 2160 (36 hours), that
        overrides, for this build only, the latest setting already defined in
        the build project.
        :param queued_timeout_in_minutes_override: The number of minutes a build is allowed to be queued before it times
        out.
        :param encryption_key_override: The Key Management Service customer master key (CMK) that overrides the
        one specified in the build project.
        :param idempotency_token: A unique, case sensitive identifier you provide to ensure the
        idempotency of the StartBuild request.
        :param logs_config_override: Log settings for this build that override the log settings defined in
        the build project.
        :param registry_credential_override: The credentials for access to a private registry.
        :param image_pull_credentials_type_override: The type of credentials CodeBuild uses to pull images in your build.
        :param debug_session_enabled: Specifies if session debugging is enabled for this build.
        :param fleet_override: A ProjectFleet object specified for this build that overrides the one
        defined in the build project.
        :param auto_retry_limit_override: The maximum number of additional automatic retries after a failed build.
        :returns: StartBuildOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises AccountLimitExceededException:
        """
        raise NotImplementedError

    @handler("StartBuildBatch")
    def start_build_batch(
        self,
        context: RequestContext,
        project_name: NonEmptyString,
        secondary_sources_override: ProjectSources | None = None,
        secondary_sources_version_override: ProjectSecondarySourceVersions | None = None,
        source_version: String | None = None,
        artifacts_override: ProjectArtifacts | None = None,
        secondary_artifacts_override: ProjectArtifactsList | None = None,
        environment_variables_override: EnvironmentVariables | None = None,
        source_type_override: SourceType | None = None,
        source_location_override: String | None = None,
        source_auth_override: SourceAuth | None = None,
        git_clone_depth_override: GitCloneDepth | None = None,
        git_submodules_config_override: GitSubmodulesConfig | None = None,
        buildspec_override: String | None = None,
        insecure_ssl_override: WrapperBoolean | None = None,
        report_build_batch_status_override: WrapperBoolean | None = None,
        environment_type_override: EnvironmentType | None = None,
        image_override: NonEmptyString | None = None,
        compute_type_override: ComputeType | None = None,
        certificate_override: String | None = None,
        cache_override: ProjectCache | None = None,
        service_role_override: NonEmptyString | None = None,
        privileged_mode_override: WrapperBoolean | None = None,
        build_timeout_in_minutes_override: BuildTimeOut | None = None,
        queued_timeout_in_minutes_override: TimeOut | None = None,
        encryption_key_override: NonEmptyString | None = None,
        idempotency_token: String | None = None,
        logs_config_override: LogsConfig | None = None,
        registry_credential_override: RegistryCredential | None = None,
        image_pull_credentials_type_override: ImagePullCredentialsType | None = None,
        build_batch_config_override: ProjectBuildBatchConfig | None = None,
        debug_session_enabled: WrapperBoolean | None = None,
        **kwargs,
    ) -> StartBuildBatchOutput:
        """Starts a batch build for a project.

        :param project_name: The name of the project.
        :param secondary_sources_override: An array of ``ProjectSource`` objects that override the secondary
        sources defined in the batch build project.
        :param secondary_sources_version_override: An array of ``ProjectSourceVersion`` objects that override the secondary
        source versions in the batch build project.
        :param source_version: The version of the batch build input to be built, for this build only.
        :param artifacts_override: An array of ``ProjectArtifacts`` objects that contains information about
        the build output artifact overrides for the build project.
        :param secondary_artifacts_override: An array of ``ProjectArtifacts`` objects that override the secondary
        artifacts defined in the batch build project.
        :param environment_variables_override: An array of ``EnvironmentVariable`` objects that override, or add to,
        the environment variables defined in the batch build project.
        :param source_type_override: The source input type that overrides the source input defined in the
        batch build project.
        :param source_location_override: A location that overrides, for this batch build, the source location
        defined in the batch build project.
        :param source_auth_override: A ``SourceAuth`` object that overrides the one defined in the batch
        build project.
        :param git_clone_depth_override: The user-defined depth of history, with a minimum value of 0, that
        overrides, for this batch build only, any previous depth of history
        defined in the batch build project.
        :param git_submodules_config_override: A ``GitSubmodulesConfig`` object that overrides the Git submodules
        configuration for this batch build.
        :param buildspec_override: A buildspec file declaration that overrides, for this build only, the
        latest one already defined in the build project.
        :param insecure_ssl_override: Enable this flag to override the insecure SSL setting that is specified
        in the batch build project.
        :param report_build_batch_status_override: Set to ``true`` to report to your source provider the status of a batch
        build's start and completion.
        :param environment_type_override: A container type for this batch build that overrides the one specified
        in the batch build project.
        :param image_override: The name of an image for this batch build that overrides the one
        specified in the batch build project.
        :param compute_type_override: The name of a compute type for this batch build that overrides the one
        specified in the batch build project.
        :param certificate_override: The name of a certificate for this batch build that overrides the one
        specified in the batch build project.
        :param cache_override: A ``ProjectCache`` object that specifies cache overrides.
        :param service_role_override: The name of a service role for this batch build that overrides the one
        specified in the batch build project.
        :param privileged_mode_override: Enable this flag to override privileged mode in the batch build project.
        :param build_timeout_in_minutes_override: Overrides the build timeout specified in the batch build project.
        :param queued_timeout_in_minutes_override: The number of minutes a batch build is allowed to be queued before it
        times out.
        :param encryption_key_override: The Key Management Service customer master key (CMK) that overrides the
        one specified in the batch build project.
        :param idempotency_token: A unique, case sensitive identifier you provide to ensure the
        idempotency of the ``StartBuildBatch`` request.
        :param logs_config_override: A ``LogsConfig`` object that override the log settings defined in the
        batch build project.
        :param registry_credential_override: A ``RegistryCredential`` object that overrides credentials for access to
        a private registry.
        :param image_pull_credentials_type_override: The type of credentials CodeBuild uses to pull images in your batch
        build.
        :param build_batch_config_override: A ``BuildBatchConfigOverride`` object that contains batch build
        configuration overrides.
        :param debug_session_enabled: Specifies if session debugging is enabled for this batch build.
        :returns: StartBuildBatchOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StartCommandExecution", expand=False)
    def start_command_execution(
        self, context: RequestContext, request: StartCommandExecutionInput, **kwargs
    ) -> StartCommandExecutionOutput:
        """Starts a command execution.

        :param sandbox_id: A ``sandboxId`` or ``sandboxArn``.
        :param command: The command that needs to be executed.
        :param type: The command type.
        :returns: StartCommandExecutionOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StartSandbox")
    def start_sandbox(
        self,
        context: RequestContext,
        project_name: NonEmptyString | None = None,
        idempotency_token: SensitiveString | None = None,
        **kwargs,
    ) -> StartSandboxOutput:
        """Starts a sandbox.

        :param project_name: The CodeBuild project name.
        :param idempotency_token: A unique client token.
        :returns: StartSandboxOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises AccountSuspendedException:
        """
        raise NotImplementedError

    @handler("StartSandboxConnection")
    def start_sandbox_connection(
        self, context: RequestContext, sandbox_id: NonEmptyString, **kwargs
    ) -> StartSandboxConnectionOutput:
        """Starts a sandbox connection.

        :param sandbox_id: A ``sandboxId`` or ``sandboxArn``.
        :returns: StartSandboxConnectionOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StopBuild")
    def stop_build(self, context: RequestContext, id: NonEmptyString, **kwargs) -> StopBuildOutput:
        """Attempts to stop running a build.

        :param id: The ID of the build.
        :returns: StopBuildOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StopBuildBatch")
    def stop_build_batch(
        self, context: RequestContext, id: NonEmptyString, **kwargs
    ) -> StopBuildBatchOutput:
        """Stops a running batch build.

        :param id: The identifier of the batch build to stop.
        :returns: StopBuildBatchOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StopSandbox")
    def stop_sandbox(
        self, context: RequestContext, id: NonEmptyString, **kwargs
    ) -> StopSandboxOutput:
        """Stops a sandbox.

        :param id: Information about the requested sandbox ID.
        :returns: StopSandboxOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateFleet")
    def update_fleet(
        self,
        context: RequestContext,
        arn: NonEmptyString,
        base_capacity: FleetCapacity | None = None,
        environment_type: EnvironmentType | None = None,
        compute_type: ComputeType | None = None,
        compute_configuration: ComputeConfiguration | None = None,
        scaling_configuration: ScalingConfigurationInput | None = None,
        overflow_behavior: FleetOverflowBehavior | None = None,
        vpc_config: VpcConfig | None = None,
        proxy_configuration: ProxyConfiguration | None = None,
        image_id: NonEmptyString | None = None,
        fleet_service_role: NonEmptyString | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> UpdateFleetOutput:
        """Updates a compute fleet.

        :param arn: The ARN of the compute fleet.
        :param base_capacity: The initial number of machines allocated to the compute ﬂeet, which
        deﬁnes the number of builds that can run in parallel.
        :param environment_type: The environment type of the compute fleet.
        :param compute_type: Information about the compute resources the compute fleet uses.
        :param compute_configuration: The compute configuration of the compute fleet.
        :param scaling_configuration: The scaling configuration of the compute fleet.
        :param overflow_behavior: The compute fleet overflow behavior.
        :param vpc_config: Information about the VPC configuration that CodeBuild accesses.
        :param proxy_configuration: The proxy configuration of the compute fleet.
        :param image_id: The Amazon Machine Image (AMI) of the compute fleet.
        :param fleet_service_role: The service role associated with the compute fleet.
        :param tags: A list of tag key and value pairs associated with this compute fleet.
        :returns: UpdateFleetOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises AccountLimitExceededException:
        """
        raise NotImplementedError

    @handler("UpdateProject")
    def update_project(
        self,
        context: RequestContext,
        name: NonEmptyString,
        description: ProjectDescription | None = None,
        source: ProjectSource | None = None,
        secondary_sources: ProjectSources | None = None,
        source_version: String | None = None,
        secondary_source_versions: ProjectSecondarySourceVersions | None = None,
        artifacts: ProjectArtifacts | None = None,
        secondary_artifacts: ProjectArtifactsList | None = None,
        cache: ProjectCache | None = None,
        environment: ProjectEnvironment | None = None,
        service_role: NonEmptyString | None = None,
        timeout_in_minutes: BuildTimeOut | None = None,
        queued_timeout_in_minutes: TimeOut | None = None,
        encryption_key: NonEmptyString | None = None,
        tags: TagList | None = None,
        vpc_config: VpcConfig | None = None,
        badge_enabled: WrapperBoolean | None = None,
        logs_config: LogsConfig | None = None,
        file_system_locations: ProjectFileSystemLocations | None = None,
        build_batch_config: ProjectBuildBatchConfig | None = None,
        concurrent_build_limit: WrapperInt | None = None,
        auto_retry_limit: WrapperInt | None = None,
        **kwargs,
    ) -> UpdateProjectOutput:
        """Changes the settings of a build project.

        :param name: The name of the build project.
        :param description: A new or replacement description of the build project.
        :param source: Information to be changed about the build input source code for the
        build project.
        :param secondary_sources: An array of ``ProjectSource`` objects.
        :param source_version: A version of the build input to be built for this project.
        :param secondary_source_versions: An array of ``ProjectSourceVersion`` objects.
        :param artifacts: Information to be changed about the build output artifacts for the build
        project.
        :param secondary_artifacts: An array of ``ProjectArtifact`` objects.
        :param cache: Stores recently used information so that it can be quickly accessed at a
        later time.
        :param environment: Information to be changed about the build environment for the build
        project.
        :param service_role: The replacement ARN of the IAM role that enables CodeBuild to interact
        with dependent Amazon Web Services services on behalf of the Amazon Web
        Services account.
        :param timeout_in_minutes: The replacement value in minutes, from 5 to 2160 (36 hours), for
        CodeBuild to wait before timing out any related build that did not get
        marked as completed.
        :param queued_timeout_in_minutes: The number of minutes a build is allowed to be queued before it times
        out.
        :param encryption_key: The Key Management Service customer master key (CMK) to be used for
        encrypting the build output artifacts.
        :param tags: An updated list of tag key and value pairs associated with this build
        project.
        :param vpc_config: VpcConfig enables CodeBuild to access resources in an Amazon VPC.
        :param badge_enabled: Set this to true to generate a publicly accessible URL for your
        project's build badge.
        :param logs_config: Information about logs for the build project.
        :param file_system_locations: An array of ``ProjectFileSystemLocation`` objects for a CodeBuild build
        project.
        :param build_batch_config: Contains configuration information about a batch build project.
        :param concurrent_build_limit: The maximum number of concurrent builds that are allowed for this
        project.
        :param auto_retry_limit: The maximum number of additional automatic retries after a failed build.
        :returns: UpdateProjectOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateProjectVisibility")
    def update_project_visibility(
        self,
        context: RequestContext,
        project_arn: NonEmptyString,
        project_visibility: ProjectVisibilityType,
        resource_access_role: NonEmptyString | None = None,
        **kwargs,
    ) -> UpdateProjectVisibilityOutput:
        """Changes the public visibility for a project. The project's build
        results, logs, and artifacts are available to the general public. For
        more information, see `Public build
        projects <https://docs.aws.amazon.com/codebuild/latest/userguide/public-builds.html>`__
        in the *CodeBuild User Guide*.

        The following should be kept in mind when making your projects public:

        -  All of a project's build results, logs, and artifacts, including
           builds that were run when the project was private, are available to
           the general public.

        -  All build logs and artifacts are available to the public. Environment
           variables, source code, and other sensitive information may have been
           output to the build logs and artifacts. You must be careful about
           what information is output to the build logs. Some best practice are:

           -  Do not store sensitive values in environment variables. We
              recommend that you use an Amazon EC2 Systems Manager Parameter
              Store or Secrets Manager to store sensitive values.

           -  Follow `Best practices for using
              webhooks <https://docs.aws.amazon.com/codebuild/latest/userguide/webhooks.html#webhook-best-practices>`__
              in the *CodeBuild User Guide* to limit which entities can trigger
              a build, and do not store the buildspec in the project itself, to
              ensure that your webhooks are as secure as possible.

        -  A malicious user can use public builds to distribute malicious
           artifacts. We recommend that you review all pull requests to verify
           that the pull request is a legitimate change. We also recommend that
           you validate any artifacts with their checksums to make sure that the
           correct artifacts are being downloaded.

        :param project_arn: The Amazon Resource Name (ARN) of the build project.
        :param project_visibility: Specifies the visibility of the project's builds.
        :param resource_access_role: The ARN of the IAM role that enables CodeBuild to access the CloudWatch
        Logs and Amazon S3 artifacts for the project's builds.
        :returns: UpdateProjectVisibilityOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateReportGroup")
    def update_report_group(
        self,
        context: RequestContext,
        arn: NonEmptyString,
        export_config: ReportExportConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> UpdateReportGroupOutput:
        """Updates a report group.

        :param arn: The ARN of the report group to update.
        :param export_config: Used to specify an updated export type.
        :param tags: An updated list of tag key and value pairs associated with this report
        group.
        :returns: UpdateReportGroupOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateWebhook")
    def update_webhook(
        self,
        context: RequestContext,
        project_name: ProjectName,
        branch_filter: String | None = None,
        rotate_secret: Boolean | None = None,
        filter_groups: FilterGroups | None = None,
        build_type: WebhookBuildType | None = None,
        **kwargs,
    ) -> UpdateWebhookOutput:
        """Updates the webhook associated with an CodeBuild build project.

        If you use Bitbucket for your repository, ``rotateSecret`` is ignored.

        :param project_name: The name of the CodeBuild project.
        :param branch_filter: A regular expression used to determine which repository branches are
        built when a webhook is triggered.
        :param rotate_secret: A boolean value that specifies whether the associated GitHub
        repository's secret token should be updated.
        :param filter_groups: An array of arrays of ``WebhookFilter`` objects used to determine if a
        webhook event can trigger a build.
        :param build_type: Specifies the type of build this webhook will trigger.
        :returns: UpdateWebhookOutput
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises OAuthProviderException:
        """
        raise NotImplementedError
