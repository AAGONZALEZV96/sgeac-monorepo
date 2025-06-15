from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AWSRegionName = str
AccessKeyId = str
AccountId = str
ActionConfigurationKey = str
ActionConfigurationQueryableValue = str
ActionConfigurationValue = str
ActionExecutionId = str
ActionExecutionToken = str
ActionName = str
ActionNamespace = str
ActionProvider = str
ActionRunOrder = int
ActionTimeout = int
ActionTypeDescription = str
ActionTypeOwner = str
AllowedAccount = str
ApprovalSummary = str
ApprovalToken = str
ArtifactName = str
ArtifactStoreLocation = str
BlockerName = str
Boolean = bool
ClientId = str
ClientRequestToken = str
ClientToken = str
Code = str
Command = str
ContinuationToken = str
Description = str
DisabledReason = str
Enabled = bool
EncryptionKeyId = str
EnvironmentVariableName = str
EnvironmentVariableValue = str
ExecutionId = str
ExecutionSummary = str
ExternalExecutionId = str
ExternalExecutionSummary = str
FilePath = str
GitBranchNamePattern = str
GitFilePathPattern = str
GitTagNamePattern = str
JobId = str
JobTimeout = int
JsonPath = str
LambdaFunctionArn = str
LastChangedBy = str
LastUpdatedBy = str
LogStreamARN = str
MatchEquals = str
MaxBatchSize = int
MaxPipelines = int
MaxResults = int
MaximumActionTypeArtifactCount = int
MaximumArtifactCount = int
Message = str
MinimumActionTypeArtifactCount = int
MinimumArtifactCount = int
NextToken = str
Nonce = str
OutputVariable = str
OutputVariablesKey = str
OutputVariablesValue = str
Percentage = int
PipelineArn = str
PipelineExecutionId = str
PipelineExecutionStatusSummary = str
PipelineName = str
PipelineVariableDescription = str
PipelineVariableName = str
PipelineVariableValue = str
PipelineVersion = int
PolicyStatementsTemplate = str
PropertyDescription = str
ResourceArn = str
RetryAttempt = int
Revision = str
RevisionChangeIdentifier = str
RevisionSummary = str
RoleArn = str
RuleConfigurationKey = str
RuleConfigurationValue = str
RuleExecutionId = str
RuleExecutionToken = str
RuleName = str
RuleProvider = str
RuleTimeout = int
S3Bucket = str
S3BucketName = str
S3Key = str
S3ObjectKey = str
SecretAccessKey = str
ServicePrincipal = str
SessionToken = str
StageName = str
StopPipelineExecutionReason = str
String = str
TagKey = str
TagValue = str
TargetFilterValue = str
ThirdPartyJobId = str
TriggerDetail = str
Url = str
UrlTemplate = str
Version = str
WebhookArn = str
WebhookAuthConfigurationAllowedIPRange = str
WebhookAuthConfigurationSecretToken = str
WebhookErrorCode = str
WebhookErrorMessage = str
WebhookName = str
WebhookUrl = str


class ActionCategory(StrEnum):
    Source = "Source"
    Build = "Build"
    Deploy = "Deploy"
    Test = "Test"
    Invoke = "Invoke"
    Approval = "Approval"
    Compute = "Compute"


class ActionConfigurationPropertyType(StrEnum):
    String = "String"
    Number = "Number"
    Boolean = "Boolean"


class ActionExecutionStatus(StrEnum):
    InProgress = "InProgress"
    Abandoned = "Abandoned"
    Succeeded = "Succeeded"
    Failed = "Failed"


class ActionOwner(StrEnum):
    AWS = "AWS"
    ThirdParty = "ThirdParty"
    Custom = "Custom"


class ApprovalStatus(StrEnum):
    Approved = "Approved"
    Rejected = "Rejected"


class ArtifactLocationType(StrEnum):
    S3 = "S3"


class ArtifactStoreType(StrEnum):
    S3 = "S3"


class BlockerType(StrEnum):
    Schedule = "Schedule"


class ConditionExecutionStatus(StrEnum):
    InProgress = "InProgress"
    Failed = "Failed"
    Errored = "Errored"
    Succeeded = "Succeeded"
    Cancelled = "Cancelled"
    Abandoned = "Abandoned"
    Overridden = "Overridden"


class ConditionType(StrEnum):
    BEFORE_ENTRY = "BEFORE_ENTRY"
    ON_SUCCESS = "ON_SUCCESS"


class EncryptionKeyType(StrEnum):
    KMS = "KMS"


class EnvironmentVariableType(StrEnum):
    PLAINTEXT = "PLAINTEXT"
    SECRETS_MANAGER = "SECRETS_MANAGER"


class ExecutionMode(StrEnum):
    QUEUED = "QUEUED"
    SUPERSEDED = "SUPERSEDED"
    PARALLEL = "PARALLEL"


class ExecutionType(StrEnum):
    STANDARD = "STANDARD"
    ROLLBACK = "ROLLBACK"


class ExecutorType(StrEnum):
    JobWorker = "JobWorker"
    Lambda = "Lambda"


class FailureType(StrEnum):
    JobFailed = "JobFailed"
    ConfigurationError = "ConfigurationError"
    PermissionError = "PermissionError"
    RevisionOutOfSync = "RevisionOutOfSync"
    RevisionUnavailable = "RevisionUnavailable"
    SystemUnavailable = "SystemUnavailable"


class GitPullRequestEventType(StrEnum):
    OPEN = "OPEN"
    UPDATED = "UPDATED"
    CLOSED = "CLOSED"


class JobStatus(StrEnum):
    Created = "Created"
    Queued = "Queued"
    Dispatched = "Dispatched"
    InProgress = "InProgress"
    TimedOut = "TimedOut"
    Succeeded = "Succeeded"
    Failed = "Failed"


class PipelineExecutionStatus(StrEnum):
    Cancelled = "Cancelled"
    InProgress = "InProgress"
    Stopped = "Stopped"
    Stopping = "Stopping"
    Succeeded = "Succeeded"
    Superseded = "Superseded"
    Failed = "Failed"


class PipelineTriggerProviderType(StrEnum):
    CodeStarSourceConnection = "CodeStarSourceConnection"


class PipelineType(StrEnum):
    V1 = "V1"
    V2 = "V2"


class Result(StrEnum):
    ROLLBACK = "ROLLBACK"
    FAIL = "FAIL"
    RETRY = "RETRY"
    SKIP = "SKIP"


class RetryTrigger(StrEnum):
    AutomatedStageRetry = "AutomatedStageRetry"
    ManualStageRetry = "ManualStageRetry"


class RuleCategory(StrEnum):
    Rule = "Rule"


class RuleConfigurationPropertyType(StrEnum):
    String = "String"
    Number = "Number"
    Boolean = "Boolean"


class RuleExecutionStatus(StrEnum):
    InProgress = "InProgress"
    Abandoned = "Abandoned"
    Succeeded = "Succeeded"
    Failed = "Failed"


class RuleOwner(StrEnum):
    AWS = "AWS"


class SourceRevisionType(StrEnum):
    COMMIT_ID = "COMMIT_ID"
    IMAGE_DIGEST = "IMAGE_DIGEST"
    S3_OBJECT_VERSION_ID = "S3_OBJECT_VERSION_ID"
    S3_OBJECT_KEY = "S3_OBJECT_KEY"


class StageExecutionStatus(StrEnum):
    Cancelled = "Cancelled"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"
    Succeeded = "Succeeded"
    Skipped = "Skipped"


class StageRetryMode(StrEnum):
    FAILED_ACTIONS = "FAILED_ACTIONS"
    ALL_ACTIONS = "ALL_ACTIONS"


class StageTransitionType(StrEnum):
    Inbound = "Inbound"
    Outbound = "Outbound"


class StartTimeRange(StrEnum):
    Latest = "Latest"
    All = "All"


class TargetFilterName(StrEnum):
    TARGET_STATUS = "TARGET_STATUS"


class TriggerType(StrEnum):
    CreatePipeline = "CreatePipeline"
    StartPipelineExecution = "StartPipelineExecution"
    PollForSourceChanges = "PollForSourceChanges"
    Webhook = "Webhook"
    CloudWatchEvent = "CloudWatchEvent"
    PutActionRevision = "PutActionRevision"
    WebhookV2 = "WebhookV2"
    ManualRollback = "ManualRollback"
    AutomatedRollback = "AutomatedRollback"


class WebhookAuthenticationType(StrEnum):
    GITHUB_HMAC = "GITHUB_HMAC"
    IP = "IP"
    UNAUTHENTICATED = "UNAUTHENTICATED"


class ActionExecutionNotFoundException(ServiceException):
    """The action execution was not found."""

    code: str = "ActionExecutionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ActionNotFoundException(ServiceException):
    """The specified action cannot be found."""

    code: str = "ActionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ActionTypeAlreadyExistsException(ServiceException):
    """The specified action type already exists with a different definition."""

    code: str = "ActionTypeAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ActionTypeNotFoundException(ServiceException):
    """The specified action type cannot be found."""

    code: str = "ActionTypeNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ApprovalAlreadyCompletedException(ServiceException):
    """The approval action has already been approved or rejected."""

    code: str = "ApprovalAlreadyCompletedException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentModificationException(ServiceException):
    """Unable to modify the tag due to a simultaneous update request."""

    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentPipelineExecutionsLimitExceededException(ServiceException):
    """The pipeline has reached the limit for concurrent pipeline executions."""

    code: str = "ConcurrentPipelineExecutionsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ConditionNotOverridableException(ServiceException):
    """Unable to override because the condition does not allow overrides."""

    code: str = "ConditionNotOverridableException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """Your request cannot be handled because the pipeline is busy handling
    ongoing activities. Try again later.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class DuplicatedStopRequestException(ServiceException):
    """The pipeline execution is already in a ``Stopping`` state. If you
    already chose to stop and wait, you cannot make that request again. You
    can choose to stop and abandon now, but be aware that this option can
    lead to failed tasks or out of sequence tasks. If you already chose to
    stop and abandon, you cannot make that request again.
    """

    code: str = "DuplicatedStopRequestException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidActionDeclarationException(ServiceException):
    """The action declaration was specified in an invalid format."""

    code: str = "InvalidActionDeclarationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidApprovalTokenException(ServiceException):
    """The approval request already received a response or has expired."""

    code: str = "InvalidApprovalTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidArnException(ServiceException):
    """The specified resource ARN is invalid."""

    code: str = "InvalidArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidBlockerDeclarationException(ServiceException):
    """Reserved for future use."""

    code: str = "InvalidBlockerDeclarationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidClientTokenException(ServiceException):
    """The client token was specified in an invalid format"""

    code: str = "InvalidClientTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidJobException(ServiceException):
    """The job was specified in an invalid format or cannot be found."""

    code: str = "InvalidJobException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidJobStateException(ServiceException):
    """The job state was specified in an invalid format."""

    code: str = "InvalidJobStateException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNextTokenException(ServiceException):
    """The next token was specified in an invalid format. Make sure that the
    next token you provide is the token returned by a previous call.
    """

    code: str = "InvalidNextTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNonceException(ServiceException):
    """The nonce was specified in an invalid format."""

    code: str = "InvalidNonceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidStageDeclarationException(ServiceException):
    """The stage declaration was specified in an invalid format."""

    code: str = "InvalidStageDeclarationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidStructureException(ServiceException):
    """The structure was specified in an invalid format."""

    code: str = "InvalidStructureException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagsException(ServiceException):
    """The specified resource tags are invalid."""

    code: str = "InvalidTagsException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidWebhookAuthenticationParametersException(ServiceException):
    """The specified authentication type is in an invalid format."""

    code: str = "InvalidWebhookAuthenticationParametersException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidWebhookFilterPatternException(ServiceException):
    """The specified event filter rule is in an invalid format."""

    code: str = "InvalidWebhookFilterPatternException"
    sender_fault: bool = False
    status_code: int = 400


class JobNotFoundException(ServiceException):
    """The job was specified in an invalid format or cannot be found."""

    code: str = "JobNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class LimitExceededException(ServiceException):
    """The number of pipelines associated with the Amazon Web Services account
    has exceeded the limit allowed for the account.
    """

    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class NotLatestPipelineExecutionException(ServiceException):
    """The stage has failed in a later run of the pipeline and the
    ``pipelineExecutionId`` associated with the request is out of date.
    """

    code: str = "NotLatestPipelineExecutionException"
    sender_fault: bool = False
    status_code: int = 400


class OutputVariablesSizeExceededException(ServiceException):
    """Exceeded the total size limit for all variables in the pipeline."""

    code: str = "OutputVariablesSizeExceededException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineExecutionNotFoundException(ServiceException):
    """The pipeline execution was specified in an invalid format or cannot be
    found, or an execution ID does not belong to the specified pipeline.
    """

    code: str = "PipelineExecutionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineExecutionNotStoppableException(ServiceException):
    """Unable to stop the pipeline execution. The execution might already be in
    a ``Stopped`` state, or it might no longer be in progress.
    """

    code: str = "PipelineExecutionNotStoppableException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineExecutionOutdatedException(ServiceException):
    """The specified pipeline execution is outdated and cannot be used as a
    target pipeline execution for rollback.
    """

    code: str = "PipelineExecutionOutdatedException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineNameInUseException(ServiceException):
    """The specified pipeline name is already in use."""

    code: str = "PipelineNameInUseException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineNotFoundException(ServiceException):
    """The pipeline was specified in an invalid format or cannot be found."""

    code: str = "PipelineNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class PipelineVersionNotFoundException(ServiceException):
    """The pipeline version was specified in an invalid format or cannot be
    found.
    """

    code: str = "PipelineVersionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class RequestFailedException(ServiceException):
    """The request failed because of an unknown error, exception, or failure."""

    code: str = "RequestFailedException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """The resource was specified in an invalid format."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class StageNotFoundException(ServiceException):
    """The stage was specified in an invalid format or cannot be found."""

    code: str = "StageNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class StageNotRetryableException(ServiceException):
    """Unable to retry. The pipeline structure or stage state might have
    changed while actions awaited retry, or the stage contains no failed
    actions.
    """

    code: str = "StageNotRetryableException"
    sender_fault: bool = False
    status_code: int = 400


class TooManyTagsException(ServiceException):
    """The tags limit for a resource has been exceeded."""

    code: str = "TooManyTagsException"
    sender_fault: bool = False
    status_code: int = 400


class UnableToRollbackStageException(ServiceException):
    """Unable to roll back the stage. The cause might be if the pipeline
    version has changed since the target pipeline execution was deployed,
    the stage is currently running, or an incorrect target pipeline
    execution ID was provided.
    """

    code: str = "UnableToRollbackStageException"
    sender_fault: bool = False
    status_code: int = 400


class ValidationException(ServiceException):
    """The validation was specified in an invalid format."""

    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400


class WebhookNotFoundException(ServiceException):
    """The specified webhook was entered in an invalid format or cannot be
    found.
    """

    code: str = "WebhookNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class AWSSessionCredentials(TypedDict, total=False):
    """Represents an Amazon Web Services session credentials object. These
    credentials are temporary credentials that are issued by Amazon Web
    Services Secure Token Service (STS). They can be used to access input
    and output artifacts in the S3 bucket used to store artifact for the
    pipeline in CodePipeline.
    """

    accessKeyId: AccessKeyId
    secretAccessKey: SecretAccessKey
    sessionToken: SessionToken


class AcknowledgeJobInput(ServiceRequest):
    """Represents the input of an AcknowledgeJob action."""

    jobId: JobId
    nonce: Nonce


class AcknowledgeJobOutput(TypedDict, total=False):
    """Represents the output of an AcknowledgeJob action."""

    status: Optional[JobStatus]


class AcknowledgeThirdPartyJobInput(ServiceRequest):
    """Represents the input of an AcknowledgeThirdPartyJob action."""

    jobId: ThirdPartyJobId
    nonce: Nonce
    clientToken: ClientToken


class AcknowledgeThirdPartyJobOutput(TypedDict, total=False):
    """Represents the output of an AcknowledgeThirdPartyJob action."""

    status: Optional[JobStatus]


ActionConfigurationMap = Dict[ActionConfigurationKey, ActionConfigurationValue]


class ActionConfiguration(TypedDict, total=False):
    """Represents information about an action configuration."""

    configuration: Optional[ActionConfigurationMap]


ActionConfigurationProperty = TypedDict(
    "ActionConfigurationProperty",
    {
        "name": ActionConfigurationKey,
        "required": Boolean,
        "key": Boolean,
        "secret": Boolean,
        "queryable": Optional[Boolean],
        "description": Optional[Description],
        "type": Optional[ActionConfigurationPropertyType],
    },
    total=False,
)
ActionConfigurationPropertyList = List[ActionConfigurationProperty]


class ActionContext(TypedDict, total=False):
    """Represents the context of an action in the stage of a pipeline to a job
    worker.
    """

    name: Optional[ActionName]
    actionExecutionId: Optional[ActionExecutionId]


EnvironmentVariable = TypedDict(
    "EnvironmentVariable",
    {
        "name": EnvironmentVariableName,
        "value": EnvironmentVariableValue,
        "type": Optional[EnvironmentVariableType],
    },
    total=False,
)
EnvironmentVariableList = List[EnvironmentVariable]
OutputVariableList = List[OutputVariable]


class InputArtifact(TypedDict, total=False):
    """Represents information about an artifact to be worked on, such as a test
    or build artifact.
    """

    name: ArtifactName


InputArtifactList = List[InputArtifact]
FilePathList = List[FilePath]


class OutputArtifact(TypedDict, total=False):
    """Represents information about the output of an action."""

    name: ArtifactName
    files: Optional[FilePathList]


OutputArtifactList = List[OutputArtifact]
CommandList = List[Command]


class ActionTypeId(TypedDict, total=False):
    """Represents information about an action type."""

    category: ActionCategory
    owner: ActionOwner
    provider: ActionProvider
    version: Version


class ActionDeclaration(TypedDict, total=False):
    """Represents information about an action declaration."""

    name: ActionName
    actionTypeId: ActionTypeId
    runOrder: Optional[ActionRunOrder]
    configuration: Optional[ActionConfigurationMap]
    commands: Optional[CommandList]
    outputArtifacts: Optional[OutputArtifactList]
    inputArtifacts: Optional[InputArtifactList]
    outputVariables: Optional[OutputVariableList]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    namespace: Optional[ActionNamespace]
    timeoutInMinutes: Optional[ActionTimeout]
    environmentVariables: Optional[EnvironmentVariableList]


class ErrorDetails(TypedDict, total=False):
    """Represents information about an error in CodePipeline."""

    code: Optional[Code]
    message: Optional[Message]


Timestamp = datetime


class ActionExecution(TypedDict, total=False):
    """Represents information about the run of an action."""

    actionExecutionId: Optional[ActionExecutionId]
    status: Optional[ActionExecutionStatus]
    summary: Optional[ExecutionSummary]
    lastStatusChange: Optional[Timestamp]
    token: Optional[ActionExecutionToken]
    lastUpdatedBy: Optional[LastUpdatedBy]
    externalExecutionId: Optional[ExecutionId]
    externalExecutionUrl: Optional[Url]
    percentComplete: Optional[Percentage]
    errorDetails: Optional[ErrorDetails]
    logStreamARN: Optional[LogStreamARN]


OutputVariablesMap = Dict[OutputVariablesKey, OutputVariablesValue]


class ActionExecutionResult(TypedDict, total=False):
    """Execution result information, such as the external execution ID."""

    externalExecutionId: Optional[ExternalExecutionId]
    externalExecutionSummary: Optional[ExternalExecutionSummary]
    externalExecutionUrl: Optional[Url]
    errorDetails: Optional[ErrorDetails]
    logStreamARN: Optional[LogStreamARN]


class S3Location(TypedDict, total=False):
    """The Amazon S3 artifact location for an action's artifacts."""

    bucket: Optional[S3Bucket]
    key: Optional[S3Key]


class ArtifactDetail(TypedDict, total=False):
    """Artifact details for the action execution, such as the artifact
    location.
    """

    name: Optional[ArtifactName]
    s3location: Optional[S3Location]


ArtifactDetailList = List[ArtifactDetail]


class ActionExecutionOutput(TypedDict, total=False):
    """Output details listed for an action execution, such as the action
    execution result.
    """

    outputArtifacts: Optional[ArtifactDetailList]
    executionResult: Optional[ActionExecutionResult]
    outputVariables: Optional[OutputVariablesMap]


ResolvedActionConfigurationMap = Dict[String, String]


class ActionExecutionInput(TypedDict, total=False):
    """Input information used for an action execution."""

    actionTypeId: Optional[ActionTypeId]
    configuration: Optional[ActionConfigurationMap]
    resolvedConfiguration: Optional[ResolvedActionConfigurationMap]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    inputArtifacts: Optional[ArtifactDetailList]
    namespace: Optional[ActionNamespace]


class ActionExecutionDetail(TypedDict, total=False):
    """Returns information about an execution of an action, including the
    action execution ID, and the name, version, and timing of the action.
    """

    pipelineExecutionId: Optional[PipelineExecutionId]
    actionExecutionId: Optional[ActionExecutionId]
    pipelineVersion: Optional[PipelineVersion]
    stageName: Optional[StageName]
    actionName: Optional[ActionName]
    startTime: Optional[Timestamp]
    lastUpdateTime: Optional[Timestamp]
    updatedBy: Optional[LastUpdatedBy]
    status: Optional[ActionExecutionStatus]
    input: Optional[ActionExecutionInput]
    output: Optional[ActionExecutionOutput]


ActionExecutionDetailList = List[ActionExecutionDetail]


class LatestInPipelineExecutionFilter(TypedDict, total=False):
    """The field that specifies to filter on the latest execution in the
    pipeline.

    Filtering on the latest execution is available for executions run on or
    after February 08, 2024.
    """

    pipelineExecutionId: PipelineExecutionId
    startTimeRange: StartTimeRange


class ActionExecutionFilter(TypedDict, total=False):
    """Filter values for the action execution."""

    pipelineExecutionId: Optional[PipelineExecutionId]
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilter]


class ActionRevision(TypedDict, total=False):
    """Represents information about the version (or revision) of an action."""

    revisionId: Revision
    revisionChangeId: RevisionChangeIdentifier
    created: Timestamp


class ActionState(TypedDict, total=False):
    """Represents information about the state of an action."""

    actionName: Optional[ActionName]
    currentRevision: Optional[ActionRevision]
    latestExecution: Optional[ActionExecution]
    entityUrl: Optional[Url]
    revisionUrl: Optional[Url]


ActionStateList = List[ActionState]


class ArtifactDetails(TypedDict, total=False):
    """Returns information about the details of an artifact."""

    minimumCount: MinimumArtifactCount
    maximumCount: MaximumArtifactCount


class ActionTypeSettings(TypedDict, total=False):
    """Returns information about the settings for an action type."""

    thirdPartyConfigurationUrl: Optional[Url]
    entityUrlTemplate: Optional[UrlTemplate]
    executionUrlTemplate: Optional[UrlTemplate]
    revisionUrlTemplate: Optional[UrlTemplate]


class ActionType(TypedDict, total=False):
    """Returns information about the details of an action type."""

    id: ActionTypeId
    settings: Optional[ActionTypeSettings]
    actionConfigurationProperties: Optional[ActionConfigurationPropertyList]
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails


class ActionTypeArtifactDetails(TypedDict, total=False):
    """Information about parameters for artifacts associated with the action
    type, such as the minimum and maximum artifacts allowed.
    """

    minimumCount: MinimumActionTypeArtifactCount
    maximumCount: MaximumActionTypeArtifactCount


class ActionTypeUrls(TypedDict, total=False):
    """Returns information about URLs for web pages that display to customers
    as links on the pipeline view, such as an external configuration page
    for the action type.
    """

    configurationUrl: Optional[Url]
    entityUrlTemplate: Optional[UrlTemplate]
    executionUrlTemplate: Optional[UrlTemplate]
    revisionUrlTemplate: Optional[UrlTemplate]


class ActionTypeProperty(TypedDict, total=False):
    """Represents information about each property specified in the action
    configuration, such as the description and key name that display for the
    customer using the action type.
    """

    name: ActionConfigurationKey
    optional: Boolean
    key: Boolean
    noEcho: Boolean
    queryable: Optional[Boolean]
    description: Optional[PropertyDescription]


ActionTypeProperties = List[ActionTypeProperty]
AllowedAccounts = List[AllowedAccount]


class ActionTypePermissions(TypedDict, total=False):
    """Details identifying the users with permissions to use the action type."""

    allowedAccounts: AllowedAccounts


class ActionTypeIdentifier(TypedDict, total=False):
    """Specifies the category, owner, provider, and version of the action type."""

    category: ActionCategory
    owner: ActionTypeOwner
    provider: ActionProvider
    version: Version


PollingServicePrincipalList = List[ServicePrincipal]
PollingAccountList = List[AccountId]


class JobWorkerExecutorConfiguration(TypedDict, total=False):
    """Details about the polling configuration for the ``JobWorker`` action
    engine, or executor.
    """

    pollingAccounts: Optional[PollingAccountList]
    pollingServicePrincipals: Optional[PollingServicePrincipalList]


class LambdaExecutorConfiguration(TypedDict, total=False):
    """Details about the configuration for the ``Lambda`` action engine, or
    executor.
    """

    lambdaFunctionArn: LambdaFunctionArn


class ExecutorConfiguration(TypedDict, total=False):
    """The action engine, or executor, related to the supported integration
    model used to create and update the action type. The available executor
    types are ``Lambda`` and ``JobWorker``.
    """

    lambdaExecutorConfiguration: Optional[LambdaExecutorConfiguration]
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfiguration]


ActionTypeExecutor = TypedDict(
    "ActionTypeExecutor",
    {
        "configuration": ExecutorConfiguration,
        "type": ExecutorType,
        "policyStatementsTemplate": Optional[PolicyStatementsTemplate],
        "jobTimeout": Optional[JobTimeout],
    },
    total=False,
)


class ActionTypeDeclaration(TypedDict, total=False):
    """The parameters for the action type definition that are provided when the
    action type is created or updated.
    """

    description: Optional[ActionTypeDescription]
    executor: ActionTypeExecutor
    id: ActionTypeIdentifier
    inputArtifactDetails: ActionTypeArtifactDetails
    outputArtifactDetails: ActionTypeArtifactDetails
    permissions: Optional[ActionTypePermissions]
    properties: Optional[ActionTypeProperties]
    urls: Optional[ActionTypeUrls]


ActionTypeList = List[ActionType]


class ApprovalResult(TypedDict, total=False):
    """Represents information about the result of an approval request."""

    summary: ApprovalSummary
    status: ApprovalStatus


class S3ArtifactLocation(TypedDict, total=False):
    """The location of the S3 bucket that contains a revision."""

    bucketName: S3BucketName
    objectKey: S3ObjectKey


ArtifactLocation = TypedDict(
    "ArtifactLocation",
    {
        "type": Optional[ArtifactLocationType],
        "s3Location": Optional[S3ArtifactLocation],
    },
    total=False,
)


class Artifact(TypedDict, total=False):
    """Artifacts are the files that are worked on by actions in the pipeline.
    See the action configuration for each action for details about artifact
    parameters. For example, the S3 source action artifact is a file name
    (or file path), and the files are generally provided as a ZIP file.
    Example artifact name: SampleApp_Windows.zip
    """

    name: Optional[ArtifactName]
    revision: Optional[Revision]
    location: Optional[ArtifactLocation]


ArtifactList = List[Artifact]


class ArtifactRevision(TypedDict, total=False):
    """Represents revision details of an artifact."""

    name: Optional[ArtifactName]
    revisionId: Optional[Revision]
    revisionChangeIdentifier: Optional[RevisionChangeIdentifier]
    revisionSummary: Optional[RevisionSummary]
    created: Optional[Timestamp]
    revisionUrl: Optional[Url]


ArtifactRevisionList = List[ArtifactRevision]
EncryptionKey = TypedDict(
    "EncryptionKey",
    {
        "id": EncryptionKeyId,
        "type": EncryptionKeyType,
    },
    total=False,
)
ArtifactStore = TypedDict(
    "ArtifactStore",
    {
        "type": ArtifactStoreType,
        "location": ArtifactStoreLocation,
        "encryptionKey": Optional[EncryptionKey],
    },
    total=False,
)
ArtifactStoreMap = Dict[AWSRegionName, ArtifactStore]
RuleConfigurationMap = Dict[RuleConfigurationKey, RuleConfigurationValue]


class RuleTypeId(TypedDict, total=False):
    """The ID for the rule type, which is made up of the combined values for
    category, owner, provider, and version. For more information about
    conditions, see `Stage
    conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__.
    For more information about rules, see the `CodePipeline rule
    reference <https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html>`__.
    """

    category: RuleCategory
    owner: Optional[RuleOwner]
    provider: RuleProvider
    version: Optional[Version]


class RuleDeclaration(TypedDict, total=False):
    """Represents information about the rule to be created for an associated
    condition. An example would be creating a new rule for an entry
    condition, such as a rule that checks for a test result before allowing
    the run to enter the deployment stage. For more information about
    conditions, see `Stage
    conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
    and `How do stage conditions
    work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__.
    For more information about rules, see the `CodePipeline rule
    reference <https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html>`__.
    """

    name: RuleName
    ruleTypeId: RuleTypeId
    configuration: Optional[RuleConfigurationMap]
    commands: Optional[CommandList]
    inputArtifacts: Optional[InputArtifactList]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    timeoutInMinutes: Optional[RuleTimeout]


RuleDeclarationList = List[RuleDeclaration]


class Condition(TypedDict, total=False):
    """The condition for the stage. A condition is made up of the rules and the
    result for the condition. For more information about conditions, see
    `Stage
    conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
    and `How do stage conditions
    work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__..
    For more information about rules, see the `CodePipeline rule
    reference <https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html>`__.
    """

    result: Optional[Result]
    rules: Optional[RuleDeclarationList]


ConditionList = List[Condition]


class BeforeEntryConditions(TypedDict, total=False):
    """The conditions for making checks for entry to a stage. For more
    information about conditions, see `Stage
    conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
    and `How do stage conditions
    work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__.
    """

    conditions: ConditionList


BlockerDeclaration = TypedDict(
    "BlockerDeclaration",
    {
        "name": BlockerName,
        "type": BlockerType,
    },
    total=False,
)


class ConditionExecution(TypedDict, total=False):
    """The run of a condition."""

    status: Optional[ConditionExecutionStatus]
    summary: Optional[ExecutionSummary]
    lastStatusChange: Optional[Timestamp]


class RuleExecution(TypedDict, total=False):
    """Represents information about each time a rule is run as part of the
    pipeline execution for a pipeline configured with conditions.
    """

    ruleExecutionId: Optional[RuleExecutionId]
    status: Optional[RuleExecutionStatus]
    summary: Optional[ExecutionSummary]
    lastStatusChange: Optional[Timestamp]
    token: Optional[RuleExecutionToken]
    lastUpdatedBy: Optional[LastUpdatedBy]
    externalExecutionId: Optional[ExecutionId]
    externalExecutionUrl: Optional[Url]
    errorDetails: Optional[ErrorDetails]


class RuleRevision(TypedDict, total=False):
    """The change to a rule that creates a revision of the rule."""

    revisionId: Revision
    revisionChangeId: RevisionChangeIdentifier
    created: Timestamp


class RuleState(TypedDict, total=False):
    """Returns information about the state of a rule.

    Values returned in the ``revisionId`` field indicate the rule revision
    information, such as the commit ID, for the current state.
    """

    ruleName: Optional[RuleName]
    currentRevision: Optional[RuleRevision]
    latestExecution: Optional[RuleExecution]
    entityUrl: Optional[Url]
    revisionUrl: Optional[Url]


RuleStateList = List[RuleState]


class ConditionState(TypedDict, total=False):
    """Information about the state of the condition."""

    latestExecution: Optional[ConditionExecution]
    ruleStates: Optional[RuleStateList]


ConditionStateList = List[ConditionState]


class Tag(TypedDict, total=False):
    """A tag is a key-value pair that is used to manage the resource."""

    key: TagKey
    value: TagValue


TagList = List[Tag]


class CreateCustomActionTypeInput(ServiceRequest):
    """Represents the input of a CreateCustomActionType operation."""

    category: ActionCategory
    provider: ActionProvider
    version: Version
    settings: Optional[ActionTypeSettings]
    configurationProperties: Optional[ActionConfigurationPropertyList]
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails
    tags: Optional[TagList]


class CreateCustomActionTypeOutput(TypedDict, total=False):
    """Represents the output of a ``CreateCustomActionType`` operation."""

    actionType: ActionType
    tags: Optional[TagList]


GitFilePathPatternList = List[GitFilePathPattern]


class GitFilePathFilterCriteria(TypedDict, total=False):
    """The Git repository file paths specified as filter criteria to start the
    pipeline.
    """

    includes: Optional[GitFilePathPatternList]
    excludes: Optional[GitFilePathPatternList]


GitBranchPatternList = List[GitBranchNamePattern]


class GitBranchFilterCriteria(TypedDict, total=False):
    """The Git repository branches specified as filter criteria to start the
    pipeline.
    """

    includes: Optional[GitBranchPatternList]
    excludes: Optional[GitBranchPatternList]


GitPullRequestEventTypeList = List[GitPullRequestEventType]


class GitPullRequestFilter(TypedDict, total=False):
    """The event criteria for the pull request trigger configuration, such as
    the lists of branches or file paths to include and exclude.

    The following are valid values for the events for this filter:

    -  CLOSED

    -  OPEN

    -  UPDATED
    """

    events: Optional[GitPullRequestEventTypeList]
    branches: Optional[GitBranchFilterCriteria]
    filePaths: Optional[GitFilePathFilterCriteria]


GitPullRequestFilterList = List[GitPullRequestFilter]
GitTagPatternList = List[GitTagNamePattern]


class GitTagFilterCriteria(TypedDict, total=False):
    """The Git tags specified as filter criteria for whether a Git tag
    repository event will start the pipeline.
    """

    includes: Optional[GitTagPatternList]
    excludes: Optional[GitTagPatternList]


class GitPushFilter(TypedDict, total=False):
    """The event criteria that specify when a specified repository event will
    start the pipeline for the specified trigger configuration, such as the
    lists of Git tags to include and exclude.
    """

    tags: Optional[GitTagFilterCriteria]
    branches: Optional[GitBranchFilterCriteria]
    filePaths: Optional[GitFilePathFilterCriteria]


GitPushFilterList = List[GitPushFilter]


class GitConfiguration(TypedDict, total=False):
    """A type of trigger configuration for Git-based source actions.

    You can specify the Git configuration trigger type for all third-party
    Git-based source actions that are supported by the
    ``CodeStarSourceConnection`` action type.
    """

    sourceActionName: ActionName
    push: Optional[GitPushFilterList]
    pullRequest: Optional[GitPullRequestFilterList]


class PipelineTriggerDeclaration(TypedDict, total=False):
    """Represents information about the specified trigger configuration, such
    as the filter criteria and the source stage for the action that contains
    the trigger.

    This is only supported for the ``CodeStarSourceConnection`` action type.

    When a trigger configuration is specified, default change detection for
    repository and branch commits is disabled.
    """

    providerType: PipelineTriggerProviderType
    gitConfiguration: GitConfiguration


PipelineTriggerDeclarationList = List[PipelineTriggerDeclaration]


class PipelineVariableDeclaration(TypedDict, total=False):
    """A variable declared at the pipeline level."""

    name: PipelineVariableName
    defaultValue: Optional[PipelineVariableValue]
    description: Optional[PipelineVariableDescription]


PipelineVariableDeclarationList = List[PipelineVariableDeclaration]


class SuccessConditions(TypedDict, total=False):
    """The conditions for making checks that, if met, succeed a stage. For more
    information about conditions, see `Stage
    conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
    and `How do stage conditions
    work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__.
    """

    conditions: ConditionList


class RetryConfiguration(TypedDict, total=False):
    """The retry configuration specifies automatic retry for a failed stage,
    along with the configured retry mode.
    """

    retryMode: Optional[StageRetryMode]


class FailureConditions(TypedDict, total=False):
    """The configuration that specifies the result, such as rollback, to occur
    upon stage failure. For more information about conditions, see `Stage
    conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
    and `How do stage conditions
    work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__.
    """

    result: Optional[Result]
    retryConfiguration: Optional[RetryConfiguration]
    conditions: Optional[ConditionList]


StageActionDeclarationList = List[ActionDeclaration]
StageBlockerDeclarationList = List[BlockerDeclaration]


class StageDeclaration(TypedDict, total=False):
    """Represents information about a stage and its definition."""

    name: StageName
    blockers: Optional[StageBlockerDeclarationList]
    actions: StageActionDeclarationList
    onFailure: Optional[FailureConditions]
    onSuccess: Optional[SuccessConditions]
    beforeEntry: Optional[BeforeEntryConditions]


PipelineStageDeclarationList = List[StageDeclaration]


class PipelineDeclaration(TypedDict, total=False):
    """Represents the structure of actions and stages to be performed in the
    pipeline.
    """

    name: PipelineName
    roleArn: RoleArn
    artifactStore: Optional[ArtifactStore]
    artifactStores: Optional[ArtifactStoreMap]
    stages: PipelineStageDeclarationList
    version: Optional[PipelineVersion]
    executionMode: Optional[ExecutionMode]
    pipelineType: Optional[PipelineType]
    variables: Optional[PipelineVariableDeclarationList]
    triggers: Optional[PipelineTriggerDeclarationList]


class CreatePipelineInput(ServiceRequest):
    """Represents the input of a ``CreatePipeline`` action."""

    pipeline: PipelineDeclaration
    tags: Optional[TagList]


class CreatePipelineOutput(TypedDict, total=False):
    """Represents the output of a ``CreatePipeline`` action."""

    pipeline: Optional[PipelineDeclaration]
    tags: Optional[TagList]


Time = datetime


class CurrentRevision(TypedDict, total=False):
    """Represents information about a current revision."""

    revision: Revision
    changeIdentifier: RevisionChangeIdentifier
    created: Optional[Time]
    revisionSummary: Optional[RevisionSummary]


class DeleteCustomActionTypeInput(ServiceRequest):
    """Represents the input of a ``DeleteCustomActionType`` operation. The
    custom action will be marked as deleted.
    """

    category: ActionCategory
    provider: ActionProvider
    version: Version


class DeletePipelineInput(ServiceRequest):
    """Represents the input of a ``DeletePipeline`` action."""

    name: PipelineName


class DeleteWebhookInput(ServiceRequest):
    name: WebhookName


class DeleteWebhookOutput(TypedDict, total=False):
    pass


class DeployTargetEventContext(TypedDict, total=False):
    """The context for the event for the deploy action."""

    ssmCommandId: Optional[String]
    message: Optional[String]


class DeployTargetEvent(TypedDict, total=False):
    """A lifecycle event for the deploy action."""

    name: Optional[String]
    status: Optional[String]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    context: Optional[DeployTargetEventContext]


DeployTargetEventList = List[DeployTargetEvent]


class DeployActionExecutionTarget(TypedDict, total=False):
    """The target for the deploy action."""

    targetId: Optional[String]
    targetType: Optional[String]
    status: Optional[String]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    events: Optional[DeployTargetEventList]


DeployActionExecutionTargetList = List[DeployActionExecutionTarget]


class DeregisterWebhookWithThirdPartyInput(ServiceRequest):
    webhookName: Optional[WebhookName]


class DeregisterWebhookWithThirdPartyOutput(TypedDict, total=False):
    pass


class DisableStageTransitionInput(ServiceRequest):
    """Represents the input of a ``DisableStageTransition`` action."""

    pipelineName: PipelineName
    stageName: StageName
    transitionType: StageTransitionType
    reason: DisabledReason


class EnableStageTransitionInput(ServiceRequest):
    """Represents the input of an ``EnableStageTransition`` action."""

    pipelineName: PipelineName
    stageName: StageName
    transitionType: StageTransitionType


class ExecutionDetails(TypedDict, total=False):
    """The details of the actions taken and results produced on an artifact as
    it passes through stages in the pipeline.
    """

    summary: Optional[ExecutionSummary]
    externalExecutionId: Optional[ExecutionId]
    percentComplete: Optional[Percentage]


class ExecutionTrigger(TypedDict, total=False):
    """The interaction or event that started a pipeline execution."""

    triggerType: Optional[TriggerType]
    triggerDetail: Optional[TriggerDetail]


FailureDetails = TypedDict(
    "FailureDetails",
    {
        "type": FailureType,
        "message": Message,
        "externalExecutionId": Optional[ExecutionId],
    },
    total=False,
)


class GetActionTypeInput(ServiceRequest):
    category: ActionCategory
    owner: ActionTypeOwner
    provider: ActionProvider
    version: Version


class GetActionTypeOutput(TypedDict, total=False):
    actionType: Optional[ActionTypeDeclaration]


class GetJobDetailsInput(ServiceRequest):
    """Represents the input of a ``GetJobDetails`` action."""

    jobId: JobId


class StageContext(TypedDict, total=False):
    """Represents information about a stage to a job worker."""

    name: Optional[StageName]


class PipelineContext(TypedDict, total=False):
    """Represents information about a pipeline to a job worker.

    PipelineContext contains ``pipelineArn`` and ``pipelineExecutionId`` for
    custom action jobs. The ``pipelineArn`` and ``pipelineExecutionId``
    fields are not populated for ThirdParty action jobs.
    """

    pipelineName: Optional[PipelineName]
    stage: Optional[StageContext]
    action: Optional[ActionContext]
    pipelineArn: Optional[PipelineArn]
    pipelineExecutionId: Optional[PipelineExecutionId]


class JobData(TypedDict, total=False):
    """Represents other information about a job required for a job worker to
    complete the job.
    """

    actionTypeId: Optional[ActionTypeId]
    actionConfiguration: Optional[ActionConfiguration]
    pipelineContext: Optional[PipelineContext]
    inputArtifacts: Optional[ArtifactList]
    outputArtifacts: Optional[ArtifactList]
    artifactCredentials: Optional[AWSSessionCredentials]
    continuationToken: Optional[ContinuationToken]
    encryptionKey: Optional[EncryptionKey]


class JobDetails(TypedDict, total=False):
    """Represents information about the details of a job."""

    id: Optional[JobId]
    data: Optional[JobData]
    accountId: Optional[AccountId]


class GetJobDetailsOutput(TypedDict, total=False):
    """Represents the output of a ``GetJobDetails`` action."""

    jobDetails: Optional[JobDetails]


class GetPipelineExecutionInput(ServiceRequest):
    """Represents the input of a ``GetPipelineExecution`` action."""

    pipelineName: PipelineName
    pipelineExecutionId: PipelineExecutionId


class PipelineRollbackMetadata(TypedDict, total=False):
    """The metadata for the stage execution to be rolled back."""

    rollbackTargetPipelineExecutionId: Optional[PipelineExecutionId]


class ResolvedPipelineVariable(TypedDict, total=False):
    """A pipeline-level variable used for a pipeline execution."""

    name: Optional[String]
    resolvedValue: Optional[String]


ResolvedPipelineVariableList = List[ResolvedPipelineVariable]


class PipelineExecution(TypedDict, total=False):
    """Represents information about an execution of a pipeline."""

    pipelineName: Optional[PipelineName]
    pipelineVersion: Optional[PipelineVersion]
    pipelineExecutionId: Optional[PipelineExecutionId]
    status: Optional[PipelineExecutionStatus]
    statusSummary: Optional[PipelineExecutionStatusSummary]
    artifactRevisions: Optional[ArtifactRevisionList]
    variables: Optional[ResolvedPipelineVariableList]
    trigger: Optional[ExecutionTrigger]
    executionMode: Optional[ExecutionMode]
    executionType: Optional[ExecutionType]
    rollbackMetadata: Optional[PipelineRollbackMetadata]


class GetPipelineExecutionOutput(TypedDict, total=False):
    """Represents the output of a ``GetPipelineExecution`` action."""

    pipelineExecution: Optional[PipelineExecution]


class GetPipelineInput(ServiceRequest):
    """Represents the input of a ``GetPipeline`` action."""

    name: PipelineName
    version: Optional[PipelineVersion]


class PipelineMetadata(TypedDict, total=False):
    """Information about a pipeline."""

    pipelineArn: Optional[PipelineArn]
    created: Optional[Timestamp]
    updated: Optional[Timestamp]
    pollingDisabledAt: Optional[Timestamp]


class GetPipelineOutput(TypedDict, total=False):
    """Represents the output of a ``GetPipeline`` action."""

    pipeline: Optional[PipelineDeclaration]
    metadata: Optional[PipelineMetadata]


class GetPipelineStateInput(ServiceRequest):
    """Represents the input of a ``GetPipelineState`` action."""

    name: PipelineName


class RetryStageMetadata(TypedDict, total=False):
    """The details of a specific automatic retry on stage failure, including
    the attempt number and trigger.
    """

    autoStageRetryAttempt: Optional[RetryAttempt]
    manualStageRetryAttempt: Optional[RetryAttempt]
    latestRetryTrigger: Optional[RetryTrigger]


class StageConditionsExecution(TypedDict, total=False):
    """Represents information about the run of a condition for a stage."""

    status: Optional[ConditionExecutionStatus]
    summary: Optional[ExecutionSummary]


class StageConditionState(TypedDict, total=False):
    """The state of a run of a condition for a stage."""

    latestExecution: Optional[StageConditionsExecution]
    conditionStates: Optional[ConditionStateList]


StageExecution = TypedDict(
    "StageExecution",
    {
        "pipelineExecutionId": PipelineExecutionId,
        "status": StageExecutionStatus,
        "type": Optional[ExecutionType],
    },
    total=False,
)
LastChangedAt = datetime


class TransitionState(TypedDict, total=False):
    """Represents information about the state of transitions between one stage
    and another stage.
    """

    enabled: Optional[Enabled]
    lastChangedBy: Optional[LastChangedBy]
    lastChangedAt: Optional[LastChangedAt]
    disabledReason: Optional[DisabledReason]


StageExecutionList = List[StageExecution]


class StageState(TypedDict, total=False):
    """Represents information about the state of the stage."""

    stageName: Optional[StageName]
    inboundExecution: Optional[StageExecution]
    inboundExecutions: Optional[StageExecutionList]
    inboundTransitionState: Optional[TransitionState]
    actionStates: Optional[ActionStateList]
    latestExecution: Optional[StageExecution]
    beforeEntryConditionState: Optional[StageConditionState]
    onSuccessConditionState: Optional[StageConditionState]
    onFailureConditionState: Optional[StageConditionState]
    retryStageMetadata: Optional[RetryStageMetadata]


StageStateList = List[StageState]


class GetPipelineStateOutput(TypedDict, total=False):
    """Represents the output of a ``GetPipelineState`` action."""

    pipelineName: Optional[PipelineName]
    pipelineVersion: Optional[PipelineVersion]
    stageStates: Optional[StageStateList]
    created: Optional[Timestamp]
    updated: Optional[Timestamp]


class GetThirdPartyJobDetailsInput(ServiceRequest):
    """Represents the input of a ``GetThirdPartyJobDetails`` action."""

    jobId: ThirdPartyJobId
    clientToken: ClientToken


class ThirdPartyJobData(TypedDict, total=False):
    """Represents information about the job data for a partner action."""

    actionTypeId: Optional[ActionTypeId]
    actionConfiguration: Optional[ActionConfiguration]
    pipelineContext: Optional[PipelineContext]
    inputArtifacts: Optional[ArtifactList]
    outputArtifacts: Optional[ArtifactList]
    artifactCredentials: Optional[AWSSessionCredentials]
    continuationToken: Optional[ContinuationToken]
    encryptionKey: Optional[EncryptionKey]


class ThirdPartyJobDetails(TypedDict, total=False):
    """The details of a job sent in response to a ``GetThirdPartyJobDetails``
    request.
    """

    id: Optional[ThirdPartyJobId]
    data: Optional[ThirdPartyJobData]
    nonce: Optional[Nonce]


class GetThirdPartyJobDetailsOutput(TypedDict, total=False):
    """Represents the output of a ``GetThirdPartyJobDetails`` action."""

    jobDetails: Optional[ThirdPartyJobDetails]


class Job(TypedDict, total=False):
    """Represents information about a job."""

    id: Optional[JobId]
    data: Optional[JobData]
    nonce: Optional[Nonce]
    accountId: Optional[AccountId]


JobList = List[Job]


class ListActionExecutionsInput(ServiceRequest):
    pipelineName: PipelineName
    filter: Optional[ActionExecutionFilter]
    maxResults: Optional[MaxResults]
    nextToken: Optional[NextToken]


class ListActionExecutionsOutput(TypedDict, total=False):
    actionExecutionDetails: Optional[ActionExecutionDetailList]
    nextToken: Optional[NextToken]


class ListActionTypesInput(ServiceRequest):
    """Represents the input of a ``ListActionTypes`` action."""

    actionOwnerFilter: Optional[ActionOwner]
    nextToken: Optional[NextToken]
    regionFilter: Optional[AWSRegionName]


class ListActionTypesOutput(TypedDict, total=False):
    """Represents the output of a ``ListActionTypes`` action."""

    actionTypes: ActionTypeList
    nextToken: Optional[NextToken]


TargetFilterValueList = List[TargetFilterValue]


class TargetFilter(TypedDict, total=False):
    """Filters the list of targets."""

    name: Optional[TargetFilterName]
    values: Optional[TargetFilterValueList]


TargetFilterList = List[TargetFilter]


class ListDeployActionExecutionTargetsInput(ServiceRequest):
    pipelineName: Optional[PipelineName]
    actionExecutionId: ActionExecutionId
    filters: Optional[TargetFilterList]
    maxResults: Optional[MaxResults]
    nextToken: Optional[NextToken]


class ListDeployActionExecutionTargetsOutput(TypedDict, total=False):
    targets: Optional[DeployActionExecutionTargetList]
    nextToken: Optional[NextToken]


class SucceededInStageFilter(TypedDict, total=False):
    """Filter for pipeline executions that have successfully completed the
    stage in the current pipeline version.
    """

    stageName: Optional[StageName]


class PipelineExecutionFilter(TypedDict, total=False):
    """The pipeline execution to filter on."""

    succeededInStage: Optional[SucceededInStageFilter]


class ListPipelineExecutionsInput(ServiceRequest):
    """Represents the input of a ``ListPipelineExecutions`` action."""

    pipelineName: PipelineName
    maxResults: Optional[MaxResults]
    filter: Optional[PipelineExecutionFilter]
    nextToken: Optional[NextToken]


class StopExecutionTrigger(TypedDict, total=False):
    """The interaction that stopped a pipeline execution."""

    reason: Optional[StopPipelineExecutionReason]


class SourceRevision(TypedDict, total=False):
    """Information about the version (or revision) of a source artifact that
    initiated a pipeline execution.
    """

    actionName: ActionName
    revisionId: Optional[Revision]
    revisionSummary: Optional[RevisionSummary]
    revisionUrl: Optional[Url]


SourceRevisionList = List[SourceRevision]


class PipelineExecutionSummary(TypedDict, total=False):
    """Summary information about a pipeline execution."""

    pipelineExecutionId: Optional[PipelineExecutionId]
    status: Optional[PipelineExecutionStatus]
    statusSummary: Optional[PipelineExecutionStatusSummary]
    startTime: Optional[Timestamp]
    lastUpdateTime: Optional[Timestamp]
    sourceRevisions: Optional[SourceRevisionList]
    trigger: Optional[ExecutionTrigger]
    stopTrigger: Optional[StopExecutionTrigger]
    executionMode: Optional[ExecutionMode]
    executionType: Optional[ExecutionType]
    rollbackMetadata: Optional[PipelineRollbackMetadata]


PipelineExecutionSummaryList = List[PipelineExecutionSummary]


class ListPipelineExecutionsOutput(TypedDict, total=False):
    """Represents the output of a ``ListPipelineExecutions`` action."""

    pipelineExecutionSummaries: Optional[PipelineExecutionSummaryList]
    nextToken: Optional[NextToken]


class ListPipelinesInput(ServiceRequest):
    """Represents the input of a ``ListPipelines`` action."""

    nextToken: Optional[NextToken]
    maxResults: Optional[MaxPipelines]


class PipelineSummary(TypedDict, total=False):
    """Returns a summary of a pipeline."""

    name: Optional[PipelineName]
    version: Optional[PipelineVersion]
    pipelineType: Optional[PipelineType]
    executionMode: Optional[ExecutionMode]
    created: Optional[Timestamp]
    updated: Optional[Timestamp]


PipelineList = List[PipelineSummary]


class ListPipelinesOutput(TypedDict, total=False):
    """Represents the output of a ``ListPipelines`` action."""

    pipelines: Optional[PipelineList]
    nextToken: Optional[NextToken]


class RuleExecutionFilter(TypedDict, total=False):
    """Filter values for the rule execution."""

    pipelineExecutionId: Optional[PipelineExecutionId]
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilter]


class ListRuleExecutionsInput(ServiceRequest):
    pipelineName: PipelineName
    filter: Optional[RuleExecutionFilter]
    maxResults: Optional[MaxResults]
    nextToken: Optional[NextToken]


class RuleExecutionResult(TypedDict, total=False):
    """Execution result information, such as the external execution ID."""

    externalExecutionId: Optional[ExternalExecutionId]
    externalExecutionSummary: Optional[ExternalExecutionSummary]
    externalExecutionUrl: Optional[Url]
    errorDetails: Optional[ErrorDetails]


class RuleExecutionOutput(TypedDict, total=False):
    """Output details listed for a rule execution, such as the rule execution
    result.
    """

    executionResult: Optional[RuleExecutionResult]


ResolvedRuleConfigurationMap = Dict[String, String]


class RuleExecutionInput(TypedDict, total=False):
    """Input information used for a rule execution."""

    ruleTypeId: Optional[RuleTypeId]
    configuration: Optional[RuleConfigurationMap]
    resolvedConfiguration: Optional[ResolvedRuleConfigurationMap]
    roleArn: Optional[RoleArn]
    region: Optional[AWSRegionName]
    inputArtifacts: Optional[ArtifactDetailList]


class RuleExecutionDetail(TypedDict, total=False):
    """The details of the runs for a rule and the results produced on an
    artifact as it passes through stages in the pipeline.
    """

    pipelineExecutionId: Optional[PipelineExecutionId]
    ruleExecutionId: Optional[RuleExecutionId]
    pipelineVersion: Optional[PipelineVersion]
    stageName: Optional[StageName]
    ruleName: Optional[RuleName]
    startTime: Optional[Timestamp]
    lastUpdateTime: Optional[Timestamp]
    updatedBy: Optional[LastUpdatedBy]
    status: Optional[RuleExecutionStatus]
    input: Optional[RuleExecutionInput]
    output: Optional[RuleExecutionOutput]


RuleExecutionDetailList = List[RuleExecutionDetail]


class ListRuleExecutionsOutput(TypedDict, total=False):
    ruleExecutionDetails: Optional[RuleExecutionDetailList]
    nextToken: Optional[NextToken]


class ListRuleTypesInput(ServiceRequest):
    ruleOwnerFilter: Optional[RuleOwner]
    regionFilter: Optional[AWSRegionName]


RuleConfigurationProperty = TypedDict(
    "RuleConfigurationProperty",
    {
        "name": RuleConfigurationKey,
        "required": Boolean,
        "key": Boolean,
        "secret": Boolean,
        "queryable": Optional[Boolean],
        "description": Optional[Description],
        "type": Optional[RuleConfigurationPropertyType],
    },
    total=False,
)
RuleConfigurationPropertyList = List[RuleConfigurationProperty]


class RuleTypeSettings(TypedDict, total=False):
    """Returns information about the settings for a rule type."""

    thirdPartyConfigurationUrl: Optional[Url]
    entityUrlTemplate: Optional[UrlTemplate]
    executionUrlTemplate: Optional[UrlTemplate]
    revisionUrlTemplate: Optional[UrlTemplate]


class RuleType(TypedDict, total=False):
    """The rule type, which is made up of the combined values for category,
    owner, provider, and version.
    """

    id: RuleTypeId
    settings: Optional[RuleTypeSettings]
    ruleConfigurationProperties: Optional[RuleConfigurationPropertyList]
    inputArtifactDetails: ArtifactDetails


RuleTypeList = List[RuleType]


class ListRuleTypesOutput(TypedDict, total=False):
    ruleTypes: RuleTypeList


class ListTagsForResourceInput(ServiceRequest):
    resourceArn: ResourceArn
    nextToken: Optional[NextToken]
    maxResults: Optional[MaxResults]


class ListTagsForResourceOutput(TypedDict, total=False):
    tags: Optional[TagList]
    nextToken: Optional[NextToken]


WebhookLastTriggered = datetime


class WebhookAuthConfiguration(TypedDict, total=False):
    """The authentication applied to incoming webhook trigger requests."""

    AllowedIPRange: Optional[WebhookAuthConfigurationAllowedIPRange]
    SecretToken: Optional[WebhookAuthConfigurationSecretToken]


class WebhookFilterRule(TypedDict, total=False):
    """The event criteria that specify when a webhook notification is sent to
    your URL.
    """

    jsonPath: JsonPath
    matchEquals: Optional[MatchEquals]


WebhookFilters = List[WebhookFilterRule]


class WebhookDefinition(TypedDict, total=False):
    """Represents information about a webhook and its definition."""

    name: WebhookName
    targetPipeline: PipelineName
    targetAction: ActionName
    filters: WebhookFilters
    authentication: WebhookAuthenticationType
    authenticationConfiguration: WebhookAuthConfiguration


class ListWebhookItem(TypedDict, total=False):
    """The detail returned for each webhook after listing webhooks, such as the
    webhook URL, the webhook name, and the webhook ARN.
    """

    definition: WebhookDefinition
    url: WebhookUrl
    errorMessage: Optional[WebhookErrorMessage]
    errorCode: Optional[WebhookErrorCode]
    lastTriggered: Optional[WebhookLastTriggered]
    arn: Optional[WebhookArn]
    tags: Optional[TagList]


class ListWebhooksInput(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


WebhookList = List[ListWebhookItem]


class ListWebhooksOutput(TypedDict, total=False):
    webhooks: Optional[WebhookList]
    NextToken: Optional[NextToken]


class OverrideStageConditionInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    pipelineExecutionId: PipelineExecutionId
    conditionType: ConditionType


class PipelineVariable(TypedDict, total=False):
    """A pipeline-level variable used for a pipeline execution."""

    name: PipelineVariableName
    value: PipelineVariableValue


PipelineVariableList = List[PipelineVariable]
QueryParamMap = Dict[ActionConfigurationKey, ActionConfigurationQueryableValue]


class PollForJobsInput(ServiceRequest):
    """Represents the input of a ``PollForJobs`` action."""

    actionTypeId: ActionTypeId
    maxBatchSize: Optional[MaxBatchSize]
    queryParam: Optional[QueryParamMap]


class PollForJobsOutput(TypedDict, total=False):
    """Represents the output of a ``PollForJobs`` action."""

    jobs: Optional[JobList]


class PollForThirdPartyJobsInput(ServiceRequest):
    """Represents the input of a ``PollForThirdPartyJobs`` action."""

    actionTypeId: ActionTypeId
    maxBatchSize: Optional[MaxBatchSize]


class ThirdPartyJob(TypedDict, total=False):
    """A response to a ``PollForThirdPartyJobs`` request returned by
    CodePipeline when there is a job to be worked on by a partner action.
    """

    clientId: Optional[ClientId]
    jobId: Optional[JobId]


ThirdPartyJobList = List[ThirdPartyJob]


class PollForThirdPartyJobsOutput(TypedDict, total=False):
    """Represents the output of a ``PollForThirdPartyJobs`` action."""

    jobs: Optional[ThirdPartyJobList]


class PutActionRevisionInput(ServiceRequest):
    """Represents the input of a ``PutActionRevision`` action."""

    pipelineName: PipelineName
    stageName: StageName
    actionName: ActionName
    actionRevision: ActionRevision


class PutActionRevisionOutput(TypedDict, total=False):
    """Represents the output of a ``PutActionRevision`` action."""

    newRevision: Optional[Boolean]
    pipelineExecutionId: Optional[PipelineExecutionId]


class PutApprovalResultInput(ServiceRequest):
    """Represents the input of a ``PutApprovalResult`` action."""

    pipelineName: PipelineName
    stageName: StageName
    actionName: ActionName
    result: ApprovalResult
    token: ApprovalToken


class PutApprovalResultOutput(TypedDict, total=False):
    """Represents the output of a ``PutApprovalResult`` action."""

    approvedAt: Optional[Timestamp]


class PutJobFailureResultInput(ServiceRequest):
    """Represents the input of a ``PutJobFailureResult`` action."""

    jobId: JobId
    failureDetails: FailureDetails


class PutJobSuccessResultInput(ServiceRequest):
    """Represents the input of a ``PutJobSuccessResult`` action."""

    jobId: JobId
    currentRevision: Optional[CurrentRevision]
    continuationToken: Optional[ContinuationToken]
    executionDetails: Optional[ExecutionDetails]
    outputVariables: Optional[OutputVariablesMap]


class PutThirdPartyJobFailureResultInput(ServiceRequest):
    """Represents the input of a ``PutThirdPartyJobFailureResult`` action."""

    jobId: ThirdPartyJobId
    clientToken: ClientToken
    failureDetails: FailureDetails


class PutThirdPartyJobSuccessResultInput(ServiceRequest):
    """Represents the input of a ``PutThirdPartyJobSuccessResult`` action."""

    jobId: ThirdPartyJobId
    clientToken: ClientToken
    currentRevision: Optional[CurrentRevision]
    continuationToken: Optional[ContinuationToken]
    executionDetails: Optional[ExecutionDetails]


class PutWebhookInput(ServiceRequest):
    webhook: WebhookDefinition
    tags: Optional[TagList]


class PutWebhookOutput(TypedDict, total=False):
    webhook: Optional[ListWebhookItem]


class RegisterWebhookWithThirdPartyInput(ServiceRequest):
    webhookName: Optional[WebhookName]


class RegisterWebhookWithThirdPartyOutput(TypedDict, total=False):
    pass


class RetryStageExecutionInput(ServiceRequest):
    """Represents the input of a ``RetryStageExecution`` action."""

    pipelineName: PipelineName
    stageName: StageName
    pipelineExecutionId: PipelineExecutionId
    retryMode: StageRetryMode


class RetryStageExecutionOutput(TypedDict, total=False):
    """Represents the output of a ``RetryStageExecution`` action."""

    pipelineExecutionId: Optional[PipelineExecutionId]


class RollbackStageInput(ServiceRequest):
    pipelineName: PipelineName
    stageName: StageName
    targetPipelineExecutionId: PipelineExecutionId


class RollbackStageOutput(TypedDict, total=False):
    pipelineExecutionId: PipelineExecutionId


class SourceRevisionOverride(TypedDict, total=False):
    """A list that allows you to specify, or override, the source revision for
    a pipeline execution that's being started. A source revision is the
    version with all the changes to your application code, or source
    artifact, for the pipeline execution.

    For the ``S3_OBJECT_VERSION_ID`` and ``S3_OBJECT_KEY`` types of source
    revisions, either of the types can be used independently, or they can be
    used together to override the source with a specific ObjectKey and
    VersionID.
    """

    actionName: ActionName
    revisionType: SourceRevisionType
    revisionValue: Revision


SourceRevisionOverrideList = List[SourceRevisionOverride]


class StartPipelineExecutionInput(ServiceRequest):
    """Represents the input of a ``StartPipelineExecution`` action."""

    name: PipelineName
    variables: Optional[PipelineVariableList]
    clientRequestToken: Optional[ClientRequestToken]
    sourceRevisions: Optional[SourceRevisionOverrideList]


class StartPipelineExecutionOutput(TypedDict, total=False):
    """Represents the output of a ``StartPipelineExecution`` action."""

    pipelineExecutionId: Optional[PipelineExecutionId]


class StopPipelineExecutionInput(ServiceRequest):
    pipelineName: PipelineName
    pipelineExecutionId: PipelineExecutionId
    abandon: Optional[Boolean]
    reason: Optional[StopPipelineExecutionReason]


class StopPipelineExecutionOutput(TypedDict, total=False):
    pipelineExecutionId: Optional[PipelineExecutionId]


TagKeyList = List[TagKey]


class TagResourceInput(ServiceRequest):
    resourceArn: ResourceArn
    tags: TagList


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    resourceArn: ResourceArn
    tagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateActionTypeInput(ServiceRequest):
    actionType: ActionTypeDeclaration


class UpdatePipelineInput(ServiceRequest):
    """Represents the input of an ``UpdatePipeline`` action."""

    pipeline: PipelineDeclaration


class UpdatePipelineOutput(TypedDict, total=False):
    """Represents the output of an ``UpdatePipeline`` action."""

    pipeline: Optional[PipelineDeclaration]


class CodepipelineApi:
    service = "codepipeline"
    version = "2015-07-09"

    @handler("AcknowledgeJob")
    def acknowledge_job(
        self, context: RequestContext, job_id: JobId, nonce: Nonce, **kwargs
    ) -> AcknowledgeJobOutput:
        """Returns information about a specified job and whether that job has been
        received by the job worker. Used for custom actions only.

        :param job_id: The unique system-generated ID of the job for which you want to confirm
        receipt.
        :param nonce: A system-generated random number that CodePipeline uses to ensure that
        the job is being worked on by only one job worker.
        :returns: AcknowledgeJobOutput
        :raises ValidationException:
        :raises InvalidNonceException:
        :raises JobNotFoundException:
        """
        raise NotImplementedError

    @handler("AcknowledgeThirdPartyJob")
    def acknowledge_third_party_job(
        self,
        context: RequestContext,
        job_id: ThirdPartyJobId,
        nonce: Nonce,
        client_token: ClientToken,
        **kwargs,
    ) -> AcknowledgeThirdPartyJobOutput:
        """Confirms a job worker has received the specified job. Used for partner
        actions only.

        :param job_id: The unique system-generated ID of the job.
        :param nonce: A system-generated random number that CodePipeline uses to ensure that
        the job is being worked on by only one job worker.
        :param client_token: The clientToken portion of the clientId and clientToken pair used to
        verify that the calling entity is allowed access to the job and its
        details.
        :returns: AcknowledgeThirdPartyJobOutput
        :raises ValidationException:
        :raises InvalidNonceException:
        :raises JobNotFoundException:
        :raises InvalidClientTokenException:
        """
        raise NotImplementedError

    @handler("CreateCustomActionType")
    def create_custom_action_type(
        self,
        context: RequestContext,
        category: ActionCategory,
        provider: ActionProvider,
        version: Version,
        input_artifact_details: ArtifactDetails,
        output_artifact_details: ArtifactDetails,
        settings: ActionTypeSettings | None = None,
        configuration_properties: ActionConfigurationPropertyList | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateCustomActionTypeOutput:
        """Creates a new custom action that can be used in all pipelines associated
        with the Amazon Web Services account. Only used for custom actions.

        :param category: The category of the custom action, such as a build action or a test
        action.
        :param provider: The provider of the service used in the custom action, such as
        CodeDeploy.
        :param version: The version identifier of the custom action.
        :param input_artifact_details: The details of the input artifact for the action, such as its commit ID.
        :param output_artifact_details: The details of the output artifact of the action, such as its commit ID.
        :param settings: URLs that provide users information about this custom action.
        :param configuration_properties: The configuration properties for the custom action.
        :param tags: The tags for the custom action.
        :returns: CreateCustomActionTypeOutput
        :raises ValidationException:
        :raises LimitExceededException:
        :raises TooManyTagsException:
        :raises InvalidTagsException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("CreatePipeline")
    def create_pipeline(
        self,
        context: RequestContext,
        pipeline: PipelineDeclaration,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreatePipelineOutput:
        """Creates a pipeline.

        In the pipeline structure, you must include either ``artifactStore`` or
        ``artifactStores`` in your pipeline, but you cannot use both. If you
        create a cross-region action in your pipeline, you must use
        ``artifactStores``.

        :param pipeline: Represents the structure of actions and stages to be performed in the
        pipeline.
        :param tags: The tags for the pipeline.
        :returns: CreatePipelineOutput
        :raises ValidationException:
        :raises PipelineNameInUseException:
        :raises InvalidStageDeclarationException:
        :raises InvalidActionDeclarationException:
        :raises InvalidBlockerDeclarationException:
        :raises InvalidStructureException:
        :raises LimitExceededException:
        :raises TooManyTagsException:
        :raises InvalidTagsException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteCustomActionType")
    def delete_custom_action_type(
        self,
        context: RequestContext,
        category: ActionCategory,
        provider: ActionProvider,
        version: Version,
        **kwargs,
    ) -> None:
        """Marks a custom action as deleted. ``PollForJobs`` for the custom action
        fails after the action is marked for deletion. Used for custom actions
        only.

        To re-create a custom action after it has been deleted you must use a
        string in the version field that has never been used before. This string
        can be an incremented version number, for example. To restore a deleted
        custom action, use a JSON file that is identical to the deleted action,
        including the original string in the version field.

        :param category: The category of the custom action that you want to delete, such as
        source or deploy.
        :param provider: The provider of the service used in the custom action, such as
        CodeDeploy.
        :param version: The version of the custom action to delete.
        :raises ValidationException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeletePipeline")
    def delete_pipeline(self, context: RequestContext, name: PipelineName, **kwargs) -> None:
        """Deletes the specified pipeline.

        :param name: The name of the pipeline to be deleted.
        :raises ValidationException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteWebhook")
    def delete_webhook(
        self, context: RequestContext, name: WebhookName, **kwargs
    ) -> DeleteWebhookOutput:
        """Deletes a previously created webhook by name. Deleting the webhook stops
        CodePipeline from starting a pipeline every time an external event
        occurs. The API returns successfully when trying to delete a webhook
        that is already deleted. If a deleted webhook is re-created by calling
        PutWebhook with the same name, it will have a different URL.

        :param name: The name of the webhook you want to delete.
        :returns: DeleteWebhookOutput
        :raises ValidationException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeregisterWebhookWithThirdParty")
    def deregister_webhook_with_third_party(
        self, context: RequestContext, webhook_name: WebhookName | None = None, **kwargs
    ) -> DeregisterWebhookWithThirdPartyOutput:
        """Removes the connection between the webhook that was created by
        CodePipeline and the external tool with events to be detected. Currently
        supported only for webhooks that target an action type of GitHub.

        :param webhook_name: The name of the webhook you want to deregister.
        :returns: DeregisterWebhookWithThirdPartyOutput
        :raises ValidationException:
        :raises WebhookNotFoundException:
        """
        raise NotImplementedError

    @handler("DisableStageTransition")
    def disable_stage_transition(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        transition_type: StageTransitionType,
        reason: DisabledReason,
        **kwargs,
    ) -> None:
        """Prevents artifacts in a pipeline from transitioning to the next stage in
        the pipeline.

        :param pipeline_name: The name of the pipeline in which you want to disable the flow of
        artifacts from one stage to another.
        :param stage_name: The name of the stage where you want to disable the inbound or outbound
        transition of artifacts.
        :param transition_type: Specifies whether artifacts are prevented from transitioning into the
        stage and being processed by the actions in that stage (inbound), or
        prevented from transitioning from the stage after they have been
        processed by the actions in that stage (outbound).
        :param reason: The reason given to the user that a stage is disabled, such as waiting
        for manual approval or manual tests.
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises StageNotFoundException:
        """
        raise NotImplementedError

    @handler("EnableStageTransition")
    def enable_stage_transition(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        transition_type: StageTransitionType,
        **kwargs,
    ) -> None:
        """Enables artifacts in a pipeline to transition to a stage in a pipeline.

        :param pipeline_name: The name of the pipeline in which you want to enable the flow of
        artifacts from one stage to another.
        :param stage_name: The name of the stage where you want to enable the transition of
        artifacts, either into the stage (inbound) or from that stage to the
        next stage (outbound).
        :param transition_type: Specifies whether artifacts are allowed to enter the stage and be
        processed by the actions in that stage (inbound) or whether already
        processed artifacts are allowed to transition to the next stage
        (outbound).
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises StageNotFoundException:
        """
        raise NotImplementedError

    @handler("GetActionType")
    def get_action_type(
        self,
        context: RequestContext,
        category: ActionCategory,
        owner: ActionTypeOwner,
        provider: ActionProvider,
        version: Version,
        **kwargs,
    ) -> GetActionTypeOutput:
        """Returns information about an action type created for an external
        provider, where the action is to be used by customers of the external
        provider. The action can be created with any supported integration
        model.

        :param category: Defines what kind of action can be taken in the stage.
        :param owner: The creator of an action type that was created with any supported
        integration model.
        :param provider: The provider of the action type being called.
        :param version: A string that describes the action type version.
        :returns: GetActionTypeOutput
        :raises ActionTypeNotFoundException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetJobDetails")
    def get_job_details(
        self, context: RequestContext, job_id: JobId, **kwargs
    ) -> GetJobDetailsOutput:
        """Returns information about a job. Used for custom actions only.

        When this API is called, CodePipeline returns temporary credentials for
        the S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that S3 bucket for input or output artifacts. This
        API also returns any secret values defined for the action.

        :param job_id: The unique system-generated ID for the job.
        :returns: GetJobDetailsOutput
        :raises ValidationException:
        :raises JobNotFoundException:
        """
        raise NotImplementedError

    @handler("GetPipeline")
    def get_pipeline(
        self,
        context: RequestContext,
        name: PipelineName,
        version: PipelineVersion | None = None,
        **kwargs,
    ) -> GetPipelineOutput:
        """Returns the metadata, structure, stages, and actions of a pipeline. Can
        be used to return the entire structure of a pipeline in JSON format,
        which can then be modified and used to update the pipeline structure
        with UpdatePipeline.

        :param name: The name of the pipeline for which you want to get information.
        :param version: The version number of the pipeline.
        :returns: GetPipelineOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises PipelineVersionNotFoundException:
        """
        raise NotImplementedError

    @handler("GetPipelineExecution")
    def get_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        pipeline_execution_id: PipelineExecutionId,
        **kwargs,
    ) -> GetPipelineExecutionOutput:
        """Returns information about an execution of a pipeline, including details
        about artifacts, the pipeline execution ID, and the name, version, and
        status of the pipeline.

        :param pipeline_name: The name of the pipeline about which you want to get execution details.
        :param pipeline_execution_id: The ID of the pipeline execution about which you want to get execution
        details.
        :returns: GetPipelineExecutionOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises PipelineExecutionNotFoundException:
        """
        raise NotImplementedError

    @handler("GetPipelineState")
    def get_pipeline_state(
        self, context: RequestContext, name: PipelineName, **kwargs
    ) -> GetPipelineStateOutput:
        """Returns information about the state of a pipeline, including the stages
        and actions.

        Values returned in the ``revisionId`` and ``revisionUrl`` fields
        indicate the source revision information, such as the commit ID, for the
        current state.

        :param name: The name of the pipeline about which you want to get information.
        :returns: GetPipelineStateOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        """
        raise NotImplementedError

    @handler("GetThirdPartyJobDetails")
    def get_third_party_job_details(
        self, context: RequestContext, job_id: ThirdPartyJobId, client_token: ClientToken, **kwargs
    ) -> GetThirdPartyJobDetailsOutput:
        """Requests the details of a job for a third party action. Used for partner
        actions only.

        When this API is called, CodePipeline returns temporary credentials for
        the S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that S3 bucket for input or output artifacts. This
        API also returns any secret values defined for the action.

        :param job_id: The unique system-generated ID used for identifying the job.
        :param client_token: The clientToken portion of the clientId and clientToken pair used to
        verify that the calling entity is allowed access to the job and its
        details.
        :returns: GetThirdPartyJobDetailsOutput
        :raises JobNotFoundException:
        :raises ValidationException:
        :raises InvalidClientTokenException:
        :raises InvalidJobException:
        """
        raise NotImplementedError

    @handler("ListActionExecutions")
    def list_action_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        filter: ActionExecutionFilter | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListActionExecutionsOutput:
        """Lists the action executions that have occurred in a pipeline.

        :param pipeline_name: The name of the pipeline for which you want to list action execution
        history.
        :param filter: Input information used to filter action execution history.
        :param max_results: The maximum number of results to return in a single call.
        :param next_token: The token that was returned from the previous ``ListActionExecutions``
        call, which can be used to return the next set of action executions in
        the list.
        :returns: ListActionExecutionsOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises InvalidNextTokenException:
        :raises PipelineExecutionNotFoundException:
        """
        raise NotImplementedError

    @handler("ListActionTypes")
    def list_action_types(
        self,
        context: RequestContext,
        action_owner_filter: ActionOwner | None = None,
        next_token: NextToken | None = None,
        region_filter: AWSRegionName | None = None,
        **kwargs,
    ) -> ListActionTypesOutput:
        """Gets a summary of all CodePipeline action types associated with your
        account.

        :param action_owner_filter: Filters the list of action types to those created by a specified entity.
        :param next_token: An identifier that was returned from the previous list action types
        call, which can be used to return the next set of action types in the
        list.
        :param region_filter: The Region to filter on for the list of action types.
        :returns: ListActionTypesOutput
        :raises ValidationException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListDeployActionExecutionTargets")
    def list_deploy_action_execution_targets(
        self,
        context: RequestContext,
        action_execution_id: ActionExecutionId,
        pipeline_name: PipelineName | None = None,
        filters: TargetFilterList | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListDeployActionExecutionTargetsOutput:
        """Lists the targets for the deploy action.

        :param action_execution_id: The execution ID for the deploy action.
        :param pipeline_name: The name of the pipeline with the deploy action.
        :param filters: Filters the targets for a specified deploy action.
        :param max_results: The maximum number of results to return in a single call.
        :param next_token: An identifier that was returned from the previous list action types
        call, which can be used to return the next set of action types in the
        list.
        :returns: ListDeployActionExecutionTargetsOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises InvalidNextTokenException:
        :raises ActionExecutionNotFoundException:
        """
        raise NotImplementedError

    @handler("ListPipelineExecutions")
    def list_pipeline_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        max_results: MaxResults | None = None,
        filter: PipelineExecutionFilter | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListPipelineExecutionsOutput:
        """Gets a summary of the most recent executions for a pipeline.

        When applying the filter for pipeline executions that have succeeded in
        the stage, the operation returns all executions in the current pipeline
        version beginning on February 1, 2024.

        :param pipeline_name: The name of the pipeline for which you want to get execution summary
        information.
        :param max_results: The maximum number of results to return in a single call.
        :param filter: The pipeline execution to filter on.
        :param next_token: The token that was returned from the previous ``ListPipelineExecutions``
        call, which can be used to return the next set of pipeline executions in
        the list.
        :returns: ListPipelineExecutionsOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListPipelines")
    def list_pipelines(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxPipelines | None = None,
        **kwargs,
    ) -> ListPipelinesOutput:
        """Gets a summary of all of the pipelines associated with your account.

        :param next_token: An identifier that was returned from the previous list pipelines call.
        :param max_results: The maximum number of pipelines to return in a single call.
        :returns: ListPipelinesOutput
        :raises ValidationException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListRuleExecutions")
    def list_rule_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        filter: RuleExecutionFilter | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListRuleExecutionsOutput:
        """Lists the rule executions that have occurred in a pipeline configured
        for conditions with rules.

        :param pipeline_name: The name of the pipeline for which you want to get execution summary
        information.
        :param filter: Input information used to filter rule execution history.
        :param max_results: The maximum number of results to return in a single call.
        :param next_token: The token that was returned from the previous ``ListRuleExecutions``
        call, which can be used to return the next set of rule executions in the
        list.
        :returns: ListRuleExecutionsOutput
        :raises ValidationException:
        :raises PipelineNotFoundException:
        :raises InvalidNextTokenException:
        :raises PipelineExecutionNotFoundException:
        """
        raise NotImplementedError

    @handler("ListRuleTypes")
    def list_rule_types(
        self,
        context: RequestContext,
        rule_owner_filter: RuleOwner | None = None,
        region_filter: AWSRegionName | None = None,
        **kwargs,
    ) -> ListRuleTypesOutput:
        """Lists the rules for the condition. For more information about
        conditions, see `Stage
        conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
        and `How do stage conditions
        work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__.For
        more information about rules, see the `CodePipeline rule
        reference <https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html>`__.

        :param rule_owner_filter: The rule owner to filter on.
        :param region_filter: The rule Region to filter on.
        :returns: ListRuleTypesOutput
        :raises ValidationException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListTagsForResourceOutput:
        """Gets the set of key-value pairs (metadata) that are used to manage the
        resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to get tags for.
        :param next_token: The token that was returned from the previous API call, which would be
        used to return the next page of the list.
        :param max_results: The maximum number of results to return in a single call.
        :returns: ListTagsForResourceOutput
        :raises ValidationException:
        :raises ResourceNotFoundException:
        :raises InvalidNextTokenException:
        :raises InvalidArnException:
        """
        raise NotImplementedError

    @handler("ListWebhooks")
    def list_webhooks(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListWebhooksOutput:
        """Gets a listing of all the webhooks in this Amazon Web Services Region
        for this account. The output lists all webhooks and includes the webhook
        URL and ARN and the configuration for each webhook.

        If a secret token was provided, it will be redacted in the response.

        :param next_token: The token that was returned from the previous ListWebhooks call, which
        can be used to return the next set of webhooks in the list.
        :param max_results: The maximum number of results to return in a single call.
        :returns: ListWebhooksOutput
        :raises ValidationException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("OverrideStageCondition")
    def override_stage_condition(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        pipeline_execution_id: PipelineExecutionId,
        condition_type: ConditionType,
        **kwargs,
    ) -> None:
        """Used to override a stage condition. For more information about
        conditions, see `Stage
        conditions <https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html>`__
        and `How do stage conditions
        work? <https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html>`__.

        :param pipeline_name: The name of the pipeline with the stage that will override the
        condition.
        :param stage_name: The name of the stage for the override.
        :param pipeline_execution_id: The ID of the pipeline execution for the override.
        :param condition_type: The type of condition to override for the stage, such as entry
        conditions, failure conditions, or success conditions.
        :raises ValidationException:
        :raises ConflictException:
        :raises PipelineNotFoundException:
        :raises StageNotFoundException:
        :raises ConditionNotOverridableException:
        :raises NotLatestPipelineExecutionException:
        :raises ConcurrentPipelineExecutionsLimitExceededException:
        """
        raise NotImplementedError

    @handler("PollForJobs")
    def poll_for_jobs(
        self,
        context: RequestContext,
        action_type_id: ActionTypeId,
        max_batch_size: MaxBatchSize | None = None,
        query_param: QueryParamMap | None = None,
        **kwargs,
    ) -> PollForJobsOutput:
        """Returns information about any jobs for CodePipeline to act on.
        ``PollForJobs`` is valid only for action types with "Custom" in the
        owner field. If the action type contains ``AWS`` or ``ThirdParty`` in
        the owner field, the ``PollForJobs`` action returns an error.

        When this API is called, CodePipeline returns temporary credentials for
        the S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that S3 bucket for input or output artifacts. This
        API also returns any secret values defined for the action.

        :param action_type_id: Represents information about an action type.
        :param max_batch_size: The maximum number of jobs to return in a poll for jobs call.
        :param query_param: A map of property names and values.
        :returns: PollForJobsOutput
        :raises ValidationException:
        :raises ActionTypeNotFoundException:
        """
        raise NotImplementedError

    @handler("PollForThirdPartyJobs")
    def poll_for_third_party_jobs(
        self,
        context: RequestContext,
        action_type_id: ActionTypeId,
        max_batch_size: MaxBatchSize | None = None,
        **kwargs,
    ) -> PollForThirdPartyJobsOutput:
        """Determines whether there are any third party jobs for a job worker to
        act on. Used for partner actions only.

        When this API is called, CodePipeline returns temporary credentials for
        the S3 bucket used to store artifacts for the pipeline, if the action
        requires access to that S3 bucket for input or output artifacts.

        :param action_type_id: Represents information about an action type.
        :param max_batch_size: The maximum number of jobs to return in a poll for jobs call.
        :returns: PollForThirdPartyJobsOutput
        :raises ActionTypeNotFoundException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("PutActionRevision")
    def put_action_revision(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        action_name: ActionName,
        action_revision: ActionRevision,
        **kwargs,
    ) -> PutActionRevisionOutput:
        """Provides information to CodePipeline about new revisions to a source.

        :param pipeline_name: The name of the pipeline that starts processing the revision to the
        source.
        :param stage_name: The name of the stage that contains the action that acts on the
        revision.
        :param action_name: The name of the action that processes the revision.
        :param action_revision: Represents information about the version (or revision) of an action.
        :returns: PutActionRevisionOutput
        :raises PipelineNotFoundException:
        :raises StageNotFoundException:
        :raises ActionNotFoundException:
        :raises ValidationException:
        :raises ConcurrentPipelineExecutionsLimitExceededException:
        """
        raise NotImplementedError

    @handler("PutApprovalResult")
    def put_approval_result(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        action_name: ActionName,
        result: ApprovalResult,
        token: ApprovalToken,
        **kwargs,
    ) -> PutApprovalResultOutput:
        """Provides the response to a manual approval request to CodePipeline.
        Valid responses include Approved and Rejected.

        :param pipeline_name: The name of the pipeline that contains the action.
        :param stage_name: The name of the stage that contains the action.
        :param action_name: The name of the action for which approval is requested.
        :param result: Represents information about the result of the approval request.
        :param token: The system-generated token used to identify a unique approval request.
        :returns: PutApprovalResultOutput
        :raises InvalidApprovalTokenException:
        :raises ApprovalAlreadyCompletedException:
        :raises PipelineNotFoundException:
        :raises StageNotFoundException:
        :raises ActionNotFoundException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("PutJobFailureResult")
    def put_job_failure_result(
        self, context: RequestContext, job_id: JobId, failure_details: FailureDetails, **kwargs
    ) -> None:
        """Represents the failure of a job as returned to the pipeline by a job
        worker. Used for custom actions only.

        :param job_id: The unique system-generated ID of the job that failed.
        :param failure_details: The details about the failure of a job.
        :raises ValidationException:
        :raises JobNotFoundException:
        :raises InvalidJobStateException:
        """
        raise NotImplementedError

    @handler("PutJobSuccessResult")
    def put_job_success_result(
        self,
        context: RequestContext,
        job_id: JobId,
        current_revision: CurrentRevision | None = None,
        continuation_token: ContinuationToken | None = None,
        execution_details: ExecutionDetails | None = None,
        output_variables: OutputVariablesMap | None = None,
        **kwargs,
    ) -> None:
        """Represents the success of a job as returned to the pipeline by a job
        worker. Used for custom actions only.

        :param job_id: The unique system-generated ID of the job that succeeded.
        :param current_revision: The ID of the current revision of the artifact successfully worked on by
        the job.
        :param continuation_token: A token generated by a job worker, such as a CodeDeploy deployment ID,
        that a successful job provides to identify a custom action in progress.
        :param execution_details: The execution details of the successful job, such as the actions taken
        by the job worker.
        :param output_variables: Key-value pairs produced as output by a job worker that can be made
        available to a downstream action configuration.
        :raises ValidationException:
        :raises JobNotFoundException:
        :raises InvalidJobStateException:
        :raises OutputVariablesSizeExceededException:
        """
        raise NotImplementedError

    @handler("PutThirdPartyJobFailureResult")
    def put_third_party_job_failure_result(
        self,
        context: RequestContext,
        job_id: ThirdPartyJobId,
        client_token: ClientToken,
        failure_details: FailureDetails,
        **kwargs,
    ) -> None:
        """Represents the failure of a third party job as returned to the pipeline
        by a job worker. Used for partner actions only.

        :param job_id: The ID of the job that failed.
        :param client_token: The clientToken portion of the clientId and clientToken pair used to
        verify that the calling entity is allowed access to the job and its
        details.
        :param failure_details: Represents information about failure details.
        :raises ValidationException:
        :raises JobNotFoundException:
        :raises InvalidJobStateException:
        :raises InvalidClientTokenException:
        """
        raise NotImplementedError

    @handler("PutThirdPartyJobSuccessResult")
    def put_third_party_job_success_result(
        self,
        context: RequestContext,
        job_id: ThirdPartyJobId,
        client_token: ClientToken,
        current_revision: CurrentRevision | None = None,
        continuation_token: ContinuationToken | None = None,
        execution_details: ExecutionDetails | None = None,
        **kwargs,
    ) -> None:
        """Represents the success of a third party job as returned to the pipeline
        by a job worker. Used for partner actions only.

        :param job_id: The ID of the job that successfully completed.
        :param client_token: The clientToken portion of the clientId and clientToken pair used to
        verify that the calling entity is allowed access to the job and its
        details.
        :param current_revision: Represents information about a current revision.
        :param continuation_token: A token generated by a job worker, such as a CodeDeploy deployment ID,
        that a successful job provides to identify a partner action in progress.
        :param execution_details: The details of the actions taken and results produced on an artifact as
        it passes through stages in the pipeline.
        :raises ValidationException:
        :raises JobNotFoundException:
        :raises InvalidJobStateException:
        :raises InvalidClientTokenException:
        """
        raise NotImplementedError

    @handler("PutWebhook")
    def put_webhook(
        self,
        context: RequestContext,
        webhook: WebhookDefinition,
        tags: TagList | None = None,
        **kwargs,
    ) -> PutWebhookOutput:
        """Defines a webhook and returns a unique webhook URL generated by
        CodePipeline. This URL can be supplied to third party source hosting
        providers to call every time there's a code change. When CodePipeline
        receives a POST request on this URL, the pipeline defined in the webhook
        is started as long as the POST request satisfied the authentication and
        filtering requirements supplied when defining the webhook.
        RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs
        can be used to automatically configure supported third parties to call
        the generated webhook URL.

        When creating CodePipeline webhooks, do not use your own credentials or
        reuse the same secret token across multiple webhooks. For optimal
        security, generate a unique secret token for each webhook you create.
        The secret token is an arbitrary string that you provide, which GitHub
        uses to compute and sign the webhook payloads sent to CodePipeline, for
        protecting the integrity and authenticity of the webhook payloads. Using
        your own credentials or reusing the same token across multiple webhooks
        can lead to security vulnerabilities.

        If a secret token was provided, it will be redacted in the response.

        :param webhook: The detail provided in an input file to create the webhook, such as the
        webhook name, the pipeline name, and the action name.
        :param tags: The tags for the webhook.
        :returns: PutWebhookOutput
        :raises ValidationException:
        :raises LimitExceededException:
        :raises InvalidWebhookFilterPatternException:
        :raises InvalidWebhookAuthenticationParametersException:
        :raises PipelineNotFoundException:
        :raises TooManyTagsException:
        :raises InvalidTagsException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("RegisterWebhookWithThirdParty")
    def register_webhook_with_third_party(
        self, context: RequestContext, webhook_name: WebhookName | None = None, **kwargs
    ) -> RegisterWebhookWithThirdPartyOutput:
        """Configures a connection between the webhook that was created and the
        external tool with events to be detected.

        :param webhook_name: The name of an existing webhook created with PutWebhook to register with
        a supported third party.
        :returns: RegisterWebhookWithThirdPartyOutput
        :raises ValidationException:
        :raises WebhookNotFoundException:
        """
        raise NotImplementedError

    @handler("RetryStageExecution")
    def retry_stage_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        pipeline_execution_id: PipelineExecutionId,
        retry_mode: StageRetryMode,
        **kwargs,
    ) -> RetryStageExecutionOutput:
        """You can retry a stage that has failed without having to run a pipeline
        again from the beginning. You do this by either retrying the failed
        actions in a stage or by retrying all actions in the stage starting from
        the first action in the stage. When you retry the failed actions in a
        stage, all actions that are still in progress continue working, and
        failed actions are triggered again. When you retry a failed stage from
        the first action in the stage, the stage cannot have any actions in
        progress. Before a stage can be retried, it must either have all actions
        failed or some actions failed and some succeeded.

        :param pipeline_name: The name of the pipeline that contains the failed stage.
        :param stage_name: The name of the failed stage to be retried.
        :param pipeline_execution_id: The ID of the pipeline execution in the failed stage to be retried.
        :param retry_mode: The scope of the retry attempt.
        :returns: RetryStageExecutionOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises PipelineNotFoundException:
        :raises StageNotFoundException:
        :raises StageNotRetryableException:
        :raises NotLatestPipelineExecutionException:
        :raises ConcurrentPipelineExecutionsLimitExceededException:
        """
        raise NotImplementedError

    @handler("RollbackStage")
    def rollback_stage(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        stage_name: StageName,
        target_pipeline_execution_id: PipelineExecutionId,
        **kwargs,
    ) -> RollbackStageOutput:
        """Rolls back a stage execution.

        :param pipeline_name: The name of the pipeline for which the stage will be rolled back.
        :param stage_name: The name of the stage in the pipeline to be rolled back.
        :param target_pipeline_execution_id: The pipeline execution ID for the stage to be rolled back to.
        :returns: RollbackStageOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises PipelineNotFoundException:
        :raises PipelineExecutionNotFoundException:
        :raises PipelineExecutionOutdatedException:
        :raises StageNotFoundException:
        :raises UnableToRollbackStageException:
        """
        raise NotImplementedError

    @handler("StartPipelineExecution")
    def start_pipeline_execution(
        self,
        context: RequestContext,
        name: PipelineName,
        variables: PipelineVariableList | None = None,
        client_request_token: ClientRequestToken | None = None,
        source_revisions: SourceRevisionOverrideList | None = None,
        **kwargs,
    ) -> StartPipelineExecutionOutput:
        """Starts the specified pipeline. Specifically, it begins processing the
        latest commit to the source location specified as part of the pipeline.

        :param name: The name of the pipeline to start.
        :param variables: A list that overrides pipeline variables for a pipeline execution that's
        being started.
        :param client_request_token: The system-generated unique ID used to identify a unique execution
        request.
        :param source_revisions: A list that allows you to specify, or override, the source revision for
        a pipeline execution that's being started.
        :returns: StartPipelineExecutionOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises PipelineNotFoundException:
        :raises ConcurrentPipelineExecutionsLimitExceededException:
        """
        raise NotImplementedError

    @handler("StopPipelineExecution")
    def stop_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        pipeline_execution_id: PipelineExecutionId,
        abandon: Boolean | None = None,
        reason: StopPipelineExecutionReason | None = None,
        **kwargs,
    ) -> StopPipelineExecutionOutput:
        """Stops the specified pipeline execution. You choose to either stop the
        pipeline execution by completing in-progress actions without starting
        subsequent actions, or by abandoning in-progress actions. While
        completing or abandoning in-progress actions, the pipeline execution is
        in a ``Stopping`` state. After all in-progress actions are completed or
        abandoned, the pipeline execution is in a ``Stopped`` state.

        :param pipeline_name: The name of the pipeline to stop.
        :param pipeline_execution_id: The ID of the pipeline execution to be stopped in the current stage.
        :param abandon: Use this option to stop the pipeline execution by abandoning, rather
        than finishing, in-progress actions.
        :param reason: Use this option to enter comments, such as the reason the pipeline was
        stopped.
        :returns: StopPipelineExecutionOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises PipelineNotFoundException:
        :raises PipelineExecutionNotStoppableException:
        :raises DuplicatedStopRequestException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagList, **kwargs
    ) -> TagResourceOutput:
        """Adds to or modifies the tags of the given resource. Tags are metadata
        that can be used to manage a resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource you want to add tags to.
        :param tags: The tags you want to modify or add to the resource.
        :returns: TagResourceOutput
        :raises ValidationException:
        :raises ResourceNotFoundException:
        :raises InvalidArnException:
        :raises TooManyTagsException:
        :raises InvalidTagsException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceOutput:
        """Removes tags from an Amazon Web Services resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to remove tags from.
        :param tag_keys: The list of keys for the tags to be removed from the resource.
        :returns: UntagResourceOutput
        :raises ValidationException:
        :raises ResourceNotFoundException:
        :raises InvalidArnException:
        :raises InvalidTagsException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UpdateActionType")
    def update_action_type(
        self, context: RequestContext, action_type: ActionTypeDeclaration, **kwargs
    ) -> None:
        """Updates an action type that was created with any supported integration
        model, where the action type is to be used by customers of the action
        type provider. Use a JSON file with the action definition and
        ``UpdateActionType`` to provide the full structure.

        :param action_type: The action type definition for the action type to be updated.
        :raises RequestFailedException:
        :raises ValidationException:
        :raises ActionTypeNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdatePipeline")
    def update_pipeline(
        self, context: RequestContext, pipeline: PipelineDeclaration, **kwargs
    ) -> UpdatePipelineOutput:
        """Updates a specified pipeline with edits or changes to its structure. Use
        a JSON file with the pipeline structure and ``UpdatePipeline`` to
        provide the full structure of the pipeline. Updating the pipeline
        increases the version number of the pipeline by 1.

        :param pipeline: The name of the pipeline to be updated.
        :returns: UpdatePipelineOutput
        :raises ValidationException:
        :raises InvalidStageDeclarationException:
        :raises InvalidActionDeclarationException:
        :raises InvalidBlockerDeclarationException:
        :raises InvalidStructureException:
        :raises LimitExceededException:
        """
        raise NotImplementedError
