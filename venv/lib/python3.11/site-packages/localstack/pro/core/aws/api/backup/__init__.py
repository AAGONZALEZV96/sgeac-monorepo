from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

ARN = str
AccountId = str
BackupOptionKey = str
BackupOptionValue = str
BackupPlanName = str
BackupRuleName = str
BackupSelectionName = str
BackupVaultName = str
Boolean = bool
ConditionKey = str
ConditionValue = str
ControlName = str
CronExpression = str
FrameworkDescription = str
FrameworkName = str
GlobalSettingsName = str
GlobalSettingsValue = str
IAMPolicy = str
IAMRoleArn = str
IsEnabled = bool
ListRestoreTestingPlansInputMaxResultsInteger = int
ListRestoreTestingSelectionsInputMaxResultsInteger = int
MaxFrameworkInputs = int
MaxResults = int
MessageCategory = str
MetadataKey = str
MetadataValue = str
ParameterName = str
ParameterValue = str
Region = str
ReportJobId = str
ReportPlanDescription = str
ReportPlanName = str
ResourceType = str
RestoreJobId = str
String = str
TagKey = str
TagValue = str
Timezone = str
boolean = bool
integer = int
string = str


class AggregationPeriod(StrEnum):
    ONE_DAY = "ONE_DAY"
    SEVEN_DAYS = "SEVEN_DAYS"
    FOURTEEN_DAYS = "FOURTEEN_DAYS"


class BackupJobState(StrEnum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ABORTING = "ABORTING"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    PARTIAL = "PARTIAL"


class BackupJobStatus(StrEnum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ABORTING = "ABORTING"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    PARTIAL = "PARTIAL"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class BackupVaultEvent(StrEnum):
    BACKUP_JOB_STARTED = "BACKUP_JOB_STARTED"
    BACKUP_JOB_COMPLETED = "BACKUP_JOB_COMPLETED"
    BACKUP_JOB_SUCCESSFUL = "BACKUP_JOB_SUCCESSFUL"
    BACKUP_JOB_FAILED = "BACKUP_JOB_FAILED"
    BACKUP_JOB_EXPIRED = "BACKUP_JOB_EXPIRED"
    RESTORE_JOB_STARTED = "RESTORE_JOB_STARTED"
    RESTORE_JOB_COMPLETED = "RESTORE_JOB_COMPLETED"
    RESTORE_JOB_SUCCESSFUL = "RESTORE_JOB_SUCCESSFUL"
    RESTORE_JOB_FAILED = "RESTORE_JOB_FAILED"
    COPY_JOB_STARTED = "COPY_JOB_STARTED"
    COPY_JOB_SUCCESSFUL = "COPY_JOB_SUCCESSFUL"
    COPY_JOB_FAILED = "COPY_JOB_FAILED"
    RECOVERY_POINT_MODIFIED = "RECOVERY_POINT_MODIFIED"
    BACKUP_PLAN_CREATED = "BACKUP_PLAN_CREATED"
    BACKUP_PLAN_MODIFIED = "BACKUP_PLAN_MODIFIED"
    S3_BACKUP_OBJECT_FAILED = "S3_BACKUP_OBJECT_FAILED"
    S3_RESTORE_OBJECT_FAILED = "S3_RESTORE_OBJECT_FAILED"


class ConditionType(StrEnum):
    STRINGEQUALS = "STRINGEQUALS"


class CopyJobState(StrEnum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIAL = "PARTIAL"


class CopyJobStatus(StrEnum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    ABORTING = "ABORTING"
    ABORTED = "ABORTED"
    COMPLETING = "COMPLETING"
    COMPLETED = "COMPLETED"
    FAILING = "FAILING"
    FAILED = "FAILED"
    PARTIAL = "PARTIAL"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class Index(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class IndexStatus(StrEnum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    DELETING = "DELETING"


class LegalHoldStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    CANCELING = "CANCELING"
    CANCELED = "CANCELED"


class RecoveryPointStatus(StrEnum):
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    DELETING = "DELETING"
    EXPIRED = "EXPIRED"


class RestoreDeletionStatus(StrEnum):
    DELETING = "DELETING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"


class RestoreJobState(StrEnum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    AGGREGATE_ALL = "AGGREGATE_ALL"
    ANY = "ANY"


class RestoreJobStatus(StrEnum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ABORTED = "ABORTED"
    FAILED = "FAILED"


class RestoreTestingRecoveryPointSelectionAlgorithm(StrEnum):
    LATEST_WITHIN_WINDOW = "LATEST_WITHIN_WINDOW"
    RANDOM_WITHIN_WINDOW = "RANDOM_WITHIN_WINDOW"


class RestoreTestingRecoveryPointType(StrEnum):
    CONTINUOUS = "CONTINUOUS"
    SNAPSHOT = "SNAPSHOT"


class RestoreValidationStatus(StrEnum):
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"
    TIMED_OUT = "TIMED_OUT"
    VALIDATING = "VALIDATING"


class StorageClass(StrEnum):
    WARM = "WARM"
    COLD = "COLD"
    DELETED = "DELETED"


class VaultState(StrEnum):
    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    FAILED = "FAILED"


class VaultType(StrEnum):
    BACKUP_VAULT = "BACKUP_VAULT"
    LOGICALLY_AIR_GAPPED_BACKUP_VAULT = "LOGICALLY_AIR_GAPPED_BACKUP_VAULT"


class AlreadyExistsException(ServiceException):
    """The required resource already exists."""

    code: str = "AlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400
    CreatorRequestId: Optional[string]
    Arn: Optional[string]
    Type: Optional[string]
    Context: Optional[string]


class ConflictException(ServiceException):
    """Backup can't perform the action that you requested until it finishes
    performing a previous action. Try again later.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class DependencyFailureException(ServiceException):
    """A dependent Amazon Web Services service or resource returned an error to
    the Backup service, and the action cannot be completed.
    """

    code: str = "DependencyFailureException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class InvalidParameterValueException(ServiceException):
    """Indicates that something is wrong with a parameter's value. For example,
    the value is out of range.
    """

    code: str = "InvalidParameterValueException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class InvalidRequestException(ServiceException):
    """Indicates that something is wrong with the input to the request. For
    example, a parameter is of the wrong type.
    """

    code: str = "InvalidRequestException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class InvalidResourceStateException(ServiceException):
    """Backup is already performing an action on this recovery point. It can't
    perform the action you requested until the first action finishes. Try
    again later.
    """

    code: str = "InvalidResourceStateException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class LimitExceededException(ServiceException):
    """A limit in the request has been exceeded; for example, a maximum number
    of items allowed in a request.
    """

    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class MissingParameterValueException(ServiceException):
    """Indicates that a required parameter is missing."""

    code: str = "MissingParameterValueException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class ResourceNotFoundException(ServiceException):
    """A resource that is required for the action doesn't exist."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


class ServiceUnavailableException(ServiceException):
    """The request failed due to a temporary failure of the server."""

    code: str = "ServiceUnavailableException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[string]
    Context: Optional[string]


BackupOptions = Dict[BackupOptionKey, BackupOptionValue]


class AdvancedBackupSetting(TypedDict, total=False):
    """The backup options for each resource type."""

    ResourceType: Optional[ResourceType]
    BackupOptions: Optional[BackupOptions]


AdvancedBackupSettings = List[AdvancedBackupSetting]
timestamp = datetime
Long = int


class RecoveryPointCreator(TypedDict, total=False):
    """Contains information about the backup plan and rule that Backup used to
    initiate the recovery point backup.
    """

    BackupPlanId: Optional[string]
    BackupPlanArn: Optional[ARN]
    BackupPlanVersion: Optional[string]
    BackupRuleId: Optional[string]


class BackupJob(TypedDict, total=False):
    """Contains detailed information about a backup job."""

    AccountId: Optional[AccountId]
    BackupJobId: Optional[string]
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    RecoveryPointArn: Optional[ARN]
    ResourceArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    State: Optional[BackupJobState]
    StatusMessage: Optional[string]
    PercentDone: Optional[string]
    BackupSizeInBytes: Optional[Long]
    IamRoleArn: Optional[IAMRoleArn]
    CreatedBy: Optional[RecoveryPointCreator]
    ExpectedCompletionDate: Optional[timestamp]
    StartBy: Optional[timestamp]
    ResourceType: Optional[ResourceType]
    BytesTransferred: Optional[Long]
    BackupOptions: Optional[BackupOptions]
    BackupType: Optional[string]
    ParentJobId: Optional[string]
    IsParent: Optional[boolean]
    ResourceName: Optional[string]
    InitiationDate: Optional[timestamp]
    MessageCategory: Optional[string]


BackupJobChildJobsInState = Dict[BackupJobState, Long]


class BackupJobSummary(TypedDict, total=False):
    """This is a summary of jobs created or running within the most recent 30
    days.

    The returned summary may contain the following: Region, Account, State,
    RestourceType, MessageCategory, StartTime, EndTime, and Count of
    included jobs.
    """

    Region: Optional[Region]
    AccountId: Optional[AccountId]
    State: Optional[BackupJobStatus]
    ResourceType: Optional[ResourceType]
    MessageCategory: Optional[MessageCategory]
    Count: Optional[integer]
    StartTime: Optional[timestamp]
    EndTime: Optional[timestamp]


BackupJobSummaryList = List[BackupJobSummary]
BackupJobsList = List[BackupJob]
ResourceTypes = List[ResourceType]


class IndexAction(TypedDict, total=False):
    """This is an optional array within a BackupRule.

    IndexAction consists of one ResourceTypes.
    """

    ResourceTypes: Optional[ResourceTypes]


IndexActions = List[IndexAction]


class Lifecycle(TypedDict, total=False):
    """Specifies the time period, in days, before a recovery point transitions
    to cold storage or is deleted.

    Backups transitioned to cold storage must be stored in cold storage for
    a minimum of 90 days. Therefore, on the console, the retention setting
    must be 90 days greater than the transition to cold after days setting.
    The transition to cold after days setting can't be changed after a
    backup has been transitioned to cold.

    Resource types that can transition to cold storage are listed in the
    `Feature availability by
    resource <https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource>`__
    table. Backup ignores this expression for other resource types.

    To remove the existing lifecycle and retention periods and keep your
    recovery points indefinitely, specify -1 for
    ``MoveToColdStorageAfterDays`` and ``DeleteAfterDays``.
    """

    MoveToColdStorageAfterDays: Optional[Long]
    DeleteAfterDays: Optional[Long]
    OptInToArchiveForSupportedResources: Optional[Boolean]


class CopyAction(TypedDict, total=False):
    """The details of the copy operation."""

    Lifecycle: Optional[Lifecycle]
    DestinationBackupVaultArn: ARN


CopyActions = List[CopyAction]
Tags = Dict[TagKey, TagValue]
WindowMinutes = int


class BackupRule(TypedDict, total=False):
    """Specifies a scheduled task used to back up a selection of resources."""

    RuleName: BackupRuleName
    TargetBackupVaultName: BackupVaultName
    ScheduleExpression: Optional[CronExpression]
    StartWindowMinutes: Optional[WindowMinutes]
    CompletionWindowMinutes: Optional[WindowMinutes]
    Lifecycle: Optional[Lifecycle]
    RecoveryPointTags: Optional[Tags]
    RuleId: Optional[string]
    CopyActions: Optional[CopyActions]
    EnableContinuousBackup: Optional[Boolean]
    ScheduleExpressionTimezone: Optional[Timezone]
    IndexActions: Optional[IndexActions]


BackupRules = List[BackupRule]


class BackupPlan(TypedDict, total=False):
    """Contains an optional backup plan display name and an array of
    ``BackupRule`` objects, each of which specifies a backup rule. Each rule
    in a backup plan is a separate scheduled task and can back up a
    different selection of Amazon Web Services resources.
    """

    BackupPlanName: BackupPlanName
    Rules: BackupRules
    AdvancedBackupSettings: Optional[AdvancedBackupSettings]


class BackupRuleInput(TypedDict, total=False):
    """Specifies a scheduled task used to back up a selection of resources."""

    RuleName: BackupRuleName
    TargetBackupVaultName: BackupVaultName
    ScheduleExpression: Optional[CronExpression]
    StartWindowMinutes: Optional[WindowMinutes]
    CompletionWindowMinutes: Optional[WindowMinutes]
    Lifecycle: Optional[Lifecycle]
    RecoveryPointTags: Optional[Tags]
    CopyActions: Optional[CopyActions]
    EnableContinuousBackup: Optional[Boolean]
    ScheduleExpressionTimezone: Optional[Timezone]
    IndexActions: Optional[IndexActions]


BackupRulesInput = List[BackupRuleInput]


class BackupPlanInput(TypedDict, total=False):
    """Contains an optional backup plan display name and an array of
    ``BackupRule`` objects, each of which specifies a backup rule. Each rule
    in a backup plan is a separate scheduled task.
    """

    BackupPlanName: BackupPlanName
    Rules: BackupRulesInput
    AdvancedBackupSettings: Optional[AdvancedBackupSettings]


class BackupPlanTemplatesListMember(TypedDict, total=False):
    """An object specifying metadata associated with a backup plan template."""

    BackupPlanTemplateId: Optional[string]
    BackupPlanTemplateName: Optional[string]


BackupPlanTemplatesList = List[BackupPlanTemplatesListMember]


class BackupPlansListMember(TypedDict, total=False):
    """Contains metadata about a backup plan."""

    BackupPlanArn: Optional[ARN]
    BackupPlanId: Optional[string]
    CreationDate: Optional[timestamp]
    DeletionDate: Optional[timestamp]
    VersionId: Optional[string]
    BackupPlanName: Optional[BackupPlanName]
    CreatorRequestId: Optional[string]
    LastExecutionDate: Optional[timestamp]
    AdvancedBackupSettings: Optional[AdvancedBackupSettings]


BackupPlanVersionsList = List[BackupPlansListMember]
BackupPlansList = List[BackupPlansListMember]


class ConditionParameter(TypedDict, total=False):
    """Includes information about tags you define to assign tagged resources to
    a backup plan.

    Include the prefix ``aws:ResourceTag`` in your tags. For example,
    ``"aws:ResourceTag/TagKey1": "Value1"``.
    """

    ConditionKey: Optional[ConditionKey]
    ConditionValue: Optional[ConditionValue]


ConditionParameters = List[ConditionParameter]


class Conditions(TypedDict, total=False):
    """Contains information about which resources to include or exclude from a
    backup plan using their tags. Conditions are case sensitive.
    """

    StringEquals: Optional[ConditionParameters]
    StringNotEquals: Optional[ConditionParameters]
    StringLike: Optional[ConditionParameters]
    StringNotLike: Optional[ConditionParameters]


ResourceArns = List[ARN]


class Condition(TypedDict, total=False):
    """Contains an array of triplets made up of a condition type (such as
    ``StringEquals``), a key, and a value. Used to filter resources using
    their tags and assign them to a backup plan. Case sensitive.
    """

    ConditionType: ConditionType
    ConditionKey: ConditionKey
    ConditionValue: ConditionValue


ListOfTags = List[Condition]


class BackupSelection(TypedDict, total=False):
    """Used to specify a set of resources to a backup plan.

    We recommend that you specify conditions, tags, or resources to include
    or exclude. Otherwise, Backup attempts to select all supported and
    opted-in storage resources, which could have unintended cost
    implications.

    For more information, see `Assigning resources
    programmatically <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-json>`__.
    """

    SelectionName: BackupSelectionName
    IamRoleArn: IAMRoleArn
    Resources: Optional[ResourceArns]
    ListOfTags: Optional[ListOfTags]
    NotResources: Optional[ResourceArns]
    Conditions: Optional[Conditions]


class BackupSelectionsListMember(TypedDict, total=False):
    """Contains metadata about a ``BackupSelection`` object."""

    SelectionId: Optional[string]
    SelectionName: Optional[BackupSelectionName]
    BackupPlanId: Optional[string]
    CreationDate: Optional[timestamp]
    CreatorRequestId: Optional[string]
    IamRoleArn: Optional[IAMRoleArn]


BackupSelectionsList = List[BackupSelectionsListMember]
BackupVaultEvents = List[BackupVaultEvent]
long = int


class BackupVaultListMember(TypedDict, total=False):
    """Contains metadata about a backup vault."""

    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    VaultType: Optional[VaultType]
    VaultState: Optional[VaultState]
    CreationDate: Optional[timestamp]
    EncryptionKeyArn: Optional[ARN]
    CreatorRequestId: Optional[string]
    NumberOfRecoveryPoints: Optional[long]
    Locked: Optional[Boolean]
    MinRetentionDays: Optional[Long]
    MaxRetentionDays: Optional[Long]
    LockDate: Optional[timestamp]


BackupVaultList = List[BackupVaultListMember]


class CalculatedLifecycle(TypedDict, total=False):
    """Contains ``DeleteAt`` and ``MoveToColdStorageAt`` timestamps, which are
    used to specify a lifecycle for a recovery point.

    The lifecycle defines when a protected resource is transitioned to cold
    storage and when it expires. Backup transitions and expires backups
    automatically according to the lifecycle that you define.

    Backups transitioned to cold storage must be stored in cold storage for
    a minimum of 90 days. Therefore, the “retention” setting must be 90 days
    greater than the “transition to cold after days” setting. The
    “transition to cold after days” setting cannot be changed after a backup
    has been transitioned to cold.

    Resource types that can transition to cold storage are listed in the
    `Feature availability by
    resource <https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource>`__
    table. Backup ignores this expression for other resource types.
    """

    MoveToColdStorageAt: Optional[timestamp]
    DeleteAt: Optional[timestamp]


class CancelLegalHoldInput(ServiceRequest):
    LegalHoldId: string
    CancelDescription: string
    RetainRecordInDays: Optional[Long]


class CancelLegalHoldOutput(TypedDict, total=False):
    pass


ComplianceResourceIdList = List[string]


class ControlInputParameter(TypedDict, total=False):
    """The parameters for a control. A control can have zero, one, or more than
    one parameter. An example of a control with two parameters is: "backup
    plan frequency is at least ``daily`` and the retention period is at
    least ``1 year``". The first parameter is ``daily``. The second
    parameter is ``1 year``.
    """

    ParameterName: Optional[ParameterName]
    ParameterValue: Optional[ParameterValue]


ControlInputParameters = List[ControlInputParameter]
stringMap = Dict[string, string]
ResourceTypeList = List[ARN]


class ControlScope(TypedDict, total=False):
    """A framework consists of one or more controls. Each control has its own
    control scope. The control scope can include one or more resource types,
    a combination of a tag key and value, or a combination of one resource
    type and one resource ID. If no scope is specified, evaluations for the
    rule are triggered when any resource in your recording group changes in
    configuration.

    To set a control scope that includes all of a particular resource, leave
    the ``ControlScope`` empty or do not pass it when calling
    ``CreateFramework``.
    """

    ComplianceResourceIds: Optional[ComplianceResourceIdList]
    ComplianceResourceTypes: Optional[ResourceTypeList]
    Tags: Optional[stringMap]


CopyJobChildJobsInState = Dict[CopyJobState, Long]


class CopyJob(TypedDict, total=False):
    """Contains detailed information about a copy job."""

    AccountId: Optional[AccountId]
    CopyJobId: Optional[string]
    SourceBackupVaultArn: Optional[ARN]
    SourceRecoveryPointArn: Optional[ARN]
    DestinationBackupVaultArn: Optional[ARN]
    DestinationRecoveryPointArn: Optional[ARN]
    ResourceArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    State: Optional[CopyJobState]
    StatusMessage: Optional[string]
    BackupSizeInBytes: Optional[Long]
    IamRoleArn: Optional[IAMRoleArn]
    CreatedBy: Optional[RecoveryPointCreator]
    ResourceType: Optional[ResourceType]
    ParentJobId: Optional[string]
    IsParent: Optional[boolean]
    CompositeMemberIdentifier: Optional[string]
    NumberOfChildJobs: Optional[Long]
    ChildJobsInState: Optional[CopyJobChildJobsInState]
    ResourceName: Optional[string]
    MessageCategory: Optional[string]


class CopyJobSummary(TypedDict, total=False):
    """This is a summary of copy jobs created or running within the most recent
    30 days.

    The returned summary may contain the following: Region, Account, State,
    RestourceType, MessageCategory, StartTime, EndTime, and Count of
    included jobs.
    """

    Region: Optional[Region]
    AccountId: Optional[AccountId]
    State: Optional[CopyJobStatus]
    ResourceType: Optional[ResourceType]
    MessageCategory: Optional[MessageCategory]
    Count: Optional[integer]
    StartTime: Optional[timestamp]
    EndTime: Optional[timestamp]


CopyJobSummaryList = List[CopyJobSummary]
CopyJobsList = List[CopyJob]


class CreateBackupPlanInput(ServiceRequest):
    BackupPlan: BackupPlanInput
    BackupPlanTags: Optional[Tags]
    CreatorRequestId: Optional[string]


class CreateBackupPlanOutput(TypedDict, total=False):
    BackupPlanId: Optional[string]
    BackupPlanArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    VersionId: Optional[string]
    AdvancedBackupSettings: Optional[AdvancedBackupSettings]


class CreateBackupSelectionInput(ServiceRequest):
    BackupPlanId: string
    BackupSelection: BackupSelection
    CreatorRequestId: Optional[string]


class CreateBackupSelectionOutput(TypedDict, total=False):
    SelectionId: Optional[string]
    BackupPlanId: Optional[string]
    CreationDate: Optional[timestamp]


class CreateBackupVaultInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    BackupVaultTags: Optional[Tags]
    EncryptionKeyArn: Optional[ARN]
    CreatorRequestId: Optional[string]


class CreateBackupVaultOutput(TypedDict, total=False):
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    CreationDate: Optional[timestamp]


class FrameworkControl(TypedDict, total=False):
    """Contains detailed information about all of the controls of a framework.
    Each framework must contain at least one control.
    """

    ControlName: ControlName
    ControlInputParameters: Optional[ControlInputParameters]
    ControlScope: Optional[ControlScope]


FrameworkControls = List[FrameworkControl]


class CreateFrameworkInput(ServiceRequest):
    FrameworkName: FrameworkName
    FrameworkDescription: Optional[FrameworkDescription]
    FrameworkControls: FrameworkControls
    IdempotencyToken: Optional[string]
    FrameworkTags: Optional[stringMap]


class CreateFrameworkOutput(TypedDict, total=False):
    FrameworkName: Optional[FrameworkName]
    FrameworkArn: Optional[ARN]


class DateRange(TypedDict, total=False):
    """This is a resource filter containing FromDate: DateTime and ToDate:
    DateTime. Both values are required. Future DateTime values are not
    permitted.

    The date and time are in Unix format and Coordinated Universal Time
    (UTC), and it is accurate to milliseconds ((milliseconds are optional).
    For example, the value 1516925490.087 represents Friday, January 26,
    2018 12:11:30.087 AM.
    """

    FromDate: timestamp
    ToDate: timestamp


ResourceIdentifiers = List[string]
VaultNames = List[string]


class RecoveryPointSelection(TypedDict, total=False):
    """This specifies criteria to assign a set of resources, such as resource
    types or backup vaults.
    """

    VaultNames: Optional[VaultNames]
    ResourceIdentifiers: Optional[ResourceIdentifiers]
    DateRange: Optional[DateRange]


class CreateLegalHoldInput(ServiceRequest):
    Title: string
    Description: string
    IdempotencyToken: Optional[string]
    RecoveryPointSelection: Optional[RecoveryPointSelection]
    Tags: Optional[Tags]


class CreateLegalHoldOutput(TypedDict, total=False):
    Title: Optional[string]
    Status: Optional[LegalHoldStatus]
    Description: Optional[string]
    LegalHoldId: Optional[string]
    LegalHoldArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    RecoveryPointSelection: Optional[RecoveryPointSelection]


class CreateLogicallyAirGappedBackupVaultInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    BackupVaultTags: Optional[Tags]
    CreatorRequestId: Optional[string]
    MinRetentionDays: Long
    MaxRetentionDays: Long


class CreateLogicallyAirGappedBackupVaultOutput(TypedDict, total=False):
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    VaultState: Optional[VaultState]


stringList = List[string]


class ReportSetting(TypedDict, total=False):
    """Contains detailed information about a report setting."""

    ReportTemplate: string
    FrameworkArns: Optional[stringList]
    NumberOfFrameworks: Optional[integer]
    Accounts: Optional[stringList]
    OrganizationUnits: Optional[stringList]
    Regions: Optional[stringList]


FormatList = List[string]


class ReportDeliveryChannel(TypedDict, total=False):
    """Contains information from your report plan about where to deliver your
    reports, specifically your Amazon S3 bucket name, S3 key prefix, and the
    formats of your reports.
    """

    S3BucketName: string
    S3KeyPrefix: Optional[string]
    Formats: Optional[FormatList]


class CreateReportPlanInput(ServiceRequest):
    ReportPlanName: ReportPlanName
    ReportPlanDescription: Optional[ReportPlanDescription]
    ReportDeliveryChannel: ReportDeliveryChannel
    ReportSetting: ReportSetting
    ReportPlanTags: Optional[stringMap]
    IdempotencyToken: Optional[string]


class CreateReportPlanOutput(TypedDict, total=False):
    ReportPlanName: Optional[ReportPlanName]
    ReportPlanArn: Optional[ARN]
    CreationTime: Optional[timestamp]


SensitiveStringMap = Dict[String, String]
RestoreTestingRecoveryPointTypeList = List[RestoreTestingRecoveryPointType]


class RestoreTestingRecoveryPointSelection(TypedDict, total=False):
    """``RecoveryPointSelection`` has five parameters (three required and two
    optional). The values you specify determine which recovery point is
    included in the restore test. You must indicate with ``Algorithm`` if
    you want the latest recovery point within your ``SelectionWindowDays``
    or if you want a random recovery point, and you must indicate through
    ``IncludeVaults`` from which vaults the recovery points can be chosen.

    ``Algorithm`` (*required*) Valid values: "``LATEST_WITHIN_WINDOW``" or
    "``RANDOM_WITHIN_WINDOW``".

    ``Recovery point types`` (*required*) Valid values: "``SNAPSHOT``"
    and/or "``CONTINUOUS``". Include ``SNAPSHOT`` to restore only snapshot
    recovery points; include ``CONTINUOUS`` to restore continuous recovery
    points (point in time restore / PITR); use both to restore either a
    snapshot or a continuous recovery point. The recovery point will be
    determined by the value for ``Algorithm``.

    ``IncludeVaults`` (*required*). You must include one or more backup
    vaults. Use the wildcard ["*"] or specific ARNs.

    ``SelectionWindowDays`` (*optional*) Value must be an integer (in days)
    from 1 to 365. If not included, the value defaults to ``30``.

    ``ExcludeVaults`` (*optional*). You can choose to input one or more
    specific backup vault ARNs to exclude those vaults' contents from
    restore eligibility. Or, you can include a list of selectors. If this
    parameter and its value are not included, it defaults to empty list.
    """

    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithm]
    ExcludeVaults: Optional[stringList]
    IncludeVaults: Optional[stringList]
    RecoveryPointTypes: Optional[RestoreTestingRecoveryPointTypeList]
    SelectionWindowDays: Optional[integer]


class RestoreTestingPlanForCreate(TypedDict, total=False):
    """This contains metadata about a restore testing plan."""

    RecoveryPointSelection: RestoreTestingRecoveryPointSelection
    RestoreTestingPlanName: String
    ScheduleExpression: String
    ScheduleExpressionTimezone: Optional[String]
    StartWindowHours: Optional[integer]


class CreateRestoreTestingPlanInput(ServiceRequest):
    CreatorRequestId: Optional[String]
    RestoreTestingPlan: RestoreTestingPlanForCreate
    Tags: Optional[SensitiveStringMap]


Timestamp = datetime


class CreateRestoreTestingPlanOutput(TypedDict, total=False):
    CreationTime: Timestamp
    RestoreTestingPlanArn: String
    RestoreTestingPlanName: String


class KeyValue(TypedDict, total=False):
    """Pair of two related strings. Allowed characters are letters, white
    space, and numbers that can be represented in UTF-8 and the following
    characters: ``+ - = . _ : /``
    """

    Key: String
    Value: String


KeyValueList = List[KeyValue]


class ProtectedResourceConditions(TypedDict, total=False):
    """The conditions that you define for resources in your restore testing
    plan using tags.
    """

    StringEquals: Optional[KeyValueList]
    StringNotEquals: Optional[KeyValueList]


class RestoreTestingSelectionForCreate(TypedDict, total=False):
    """This contains metadata about a specific restore testing selection.

    ProtectedResourceType is required, such as Amazon EBS or Amazon EC2.

    This consists of ``RestoreTestingSelectionName``,
    ``ProtectedResourceType``, and one of the following:

    -  ``ProtectedResourceArns``

    -  ``ProtectedResourceConditions``

    Each protected resource type can have one single value.

    A restore testing selection can include a wildcard value ("*") for
    ``ProtectedResourceArns`` along with ``ProtectedResourceConditions``.
    Alternatively, you can include up to 30 specific protected resource ARNs
    in ``ProtectedResourceArns``.

    ``ProtectedResourceConditions`` examples include as ``StringEquals`` and
    ``StringNotEquals``.
    """

    IamRoleArn: String
    ProtectedResourceArns: Optional[stringList]
    ProtectedResourceConditions: Optional[ProtectedResourceConditions]
    ProtectedResourceType: String
    RestoreMetadataOverrides: Optional[SensitiveStringMap]
    RestoreTestingSelectionName: String
    ValidationWindowHours: Optional[integer]


class CreateRestoreTestingSelectionInput(ServiceRequest):
    CreatorRequestId: Optional[String]
    RestoreTestingPlanName: String
    RestoreTestingSelection: RestoreTestingSelectionForCreate


class CreateRestoreTestingSelectionOutput(TypedDict, total=False):
    CreationTime: Timestamp
    RestoreTestingPlanArn: String
    RestoreTestingPlanName: String
    RestoreTestingSelectionName: String


class DeleteBackupPlanInput(ServiceRequest):
    BackupPlanId: string


class DeleteBackupPlanOutput(TypedDict, total=False):
    BackupPlanId: Optional[string]
    BackupPlanArn: Optional[ARN]
    DeletionDate: Optional[timestamp]
    VersionId: Optional[string]


class DeleteBackupSelectionInput(ServiceRequest):
    BackupPlanId: string
    SelectionId: string


class DeleteBackupVaultAccessPolicyInput(ServiceRequest):
    BackupVaultName: BackupVaultName


class DeleteBackupVaultInput(ServiceRequest):
    BackupVaultName: string


class DeleteBackupVaultLockConfigurationInput(ServiceRequest):
    BackupVaultName: BackupVaultName


class DeleteBackupVaultNotificationsInput(ServiceRequest):
    BackupVaultName: BackupVaultName


class DeleteFrameworkInput(ServiceRequest):
    FrameworkName: FrameworkName


class DeleteRecoveryPointInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN


class DeleteReportPlanInput(ServiceRequest):
    ReportPlanName: ReportPlanName


class DeleteRestoreTestingPlanInput(ServiceRequest):
    RestoreTestingPlanName: String


class DeleteRestoreTestingSelectionInput(ServiceRequest):
    RestoreTestingPlanName: String
    RestoreTestingSelectionName: String


class DescribeBackupJobInput(ServiceRequest):
    BackupJobId: string


class DescribeBackupJobOutput(TypedDict, total=False):
    AccountId: Optional[AccountId]
    BackupJobId: Optional[string]
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    RecoveryPointArn: Optional[ARN]
    ResourceArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    State: Optional[BackupJobState]
    StatusMessage: Optional[string]
    PercentDone: Optional[string]
    BackupSizeInBytes: Optional[Long]
    IamRoleArn: Optional[IAMRoleArn]
    CreatedBy: Optional[RecoveryPointCreator]
    ResourceType: Optional[ResourceType]
    BytesTransferred: Optional[Long]
    ExpectedCompletionDate: Optional[timestamp]
    StartBy: Optional[timestamp]
    BackupOptions: Optional[BackupOptions]
    BackupType: Optional[string]
    ParentJobId: Optional[string]
    IsParent: Optional[boolean]
    NumberOfChildJobs: Optional[Long]
    ChildJobsInState: Optional[BackupJobChildJobsInState]
    ResourceName: Optional[string]
    InitiationDate: Optional[timestamp]
    MessageCategory: Optional[string]


class DescribeBackupVaultInput(ServiceRequest):
    BackupVaultName: string
    BackupVaultAccountId: Optional[string]


class DescribeBackupVaultOutput(TypedDict, total=False):
    BackupVaultName: Optional[string]
    BackupVaultArn: Optional[ARN]
    VaultType: Optional[VaultType]
    VaultState: Optional[VaultState]
    EncryptionKeyArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CreatorRequestId: Optional[string]
    NumberOfRecoveryPoints: Optional[long]
    Locked: Optional[Boolean]
    MinRetentionDays: Optional[Long]
    MaxRetentionDays: Optional[Long]
    LockDate: Optional[timestamp]


class DescribeCopyJobInput(ServiceRequest):
    CopyJobId: string


class DescribeCopyJobOutput(TypedDict, total=False):
    CopyJob: Optional[CopyJob]


class DescribeFrameworkInput(ServiceRequest):
    FrameworkName: FrameworkName


class DescribeFrameworkOutput(TypedDict, total=False):
    FrameworkName: Optional[FrameworkName]
    FrameworkArn: Optional[ARN]
    FrameworkDescription: Optional[FrameworkDescription]
    FrameworkControls: Optional[FrameworkControls]
    CreationTime: Optional[timestamp]
    DeploymentStatus: Optional[string]
    FrameworkStatus: Optional[string]
    IdempotencyToken: Optional[string]


class DescribeGlobalSettingsInput(ServiceRequest):
    pass


GlobalSettings = Dict[GlobalSettingsName, GlobalSettingsValue]


class DescribeGlobalSettingsOutput(TypedDict, total=False):
    GlobalSettings: Optional[GlobalSettings]
    LastUpdateTime: Optional[timestamp]


class DescribeProtectedResourceInput(ServiceRequest):
    ResourceArn: ARN


class DescribeProtectedResourceOutput(TypedDict, total=False):
    ResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    LastBackupTime: Optional[timestamp]
    ResourceName: Optional[string]
    LastBackupVaultArn: Optional[ARN]
    LastRecoveryPointArn: Optional[ARN]
    LatestRestoreExecutionTimeMinutes: Optional[Long]
    LatestRestoreJobCreationDate: Optional[timestamp]
    LatestRestoreRecoveryPointCreationDate: Optional[timestamp]


class DescribeRecoveryPointInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN
    BackupVaultAccountId: Optional[AccountId]


class DescribeRecoveryPointOutput(TypedDict, total=False):
    RecoveryPointArn: Optional[ARN]
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    SourceBackupVaultArn: Optional[ARN]
    ResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    CreatedBy: Optional[RecoveryPointCreator]
    IamRoleArn: Optional[IAMRoleArn]
    Status: Optional[RecoveryPointStatus]
    StatusMessage: Optional[string]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    BackupSizeInBytes: Optional[Long]
    CalculatedLifecycle: Optional[CalculatedLifecycle]
    Lifecycle: Optional[Lifecycle]
    EncryptionKeyArn: Optional[ARN]
    IsEncrypted: Optional[boolean]
    StorageClass: Optional[StorageClass]
    LastRestoreTime: Optional[timestamp]
    ParentRecoveryPointArn: Optional[ARN]
    CompositeMemberIdentifier: Optional[string]
    IsParent: Optional[boolean]
    ResourceName: Optional[string]
    VaultType: Optional[VaultType]
    IndexStatus: Optional[IndexStatus]
    IndexStatusMessage: Optional[string]


class DescribeRegionSettingsInput(ServiceRequest):
    pass


ResourceTypeManagementPreference = Dict[ResourceType, IsEnabled]
ResourceTypeOptInPreference = Dict[ResourceType, IsEnabled]


class DescribeRegionSettingsOutput(TypedDict, total=False):
    ResourceTypeOptInPreference: Optional[ResourceTypeOptInPreference]
    ResourceTypeManagementPreference: Optional[ResourceTypeManagementPreference]


class DescribeReportJobInput(ServiceRequest):
    ReportJobId: ReportJobId


class ReportDestination(TypedDict, total=False):
    """Contains information from your report job about your report destination."""

    S3BucketName: Optional[string]
    S3Keys: Optional[stringList]


class ReportJob(TypedDict, total=False):
    """Contains detailed information about a report job. A report job compiles
    a report based on a report plan and publishes it to Amazon S3.
    """

    ReportJobId: Optional[ReportJobId]
    ReportPlanArn: Optional[ARN]
    ReportTemplate: Optional[string]
    CreationTime: Optional[timestamp]
    CompletionTime: Optional[timestamp]
    Status: Optional[string]
    StatusMessage: Optional[string]
    ReportDestination: Optional[ReportDestination]


class DescribeReportJobOutput(TypedDict, total=False):
    ReportJob: Optional[ReportJob]


class DescribeReportPlanInput(ServiceRequest):
    ReportPlanName: ReportPlanName


class ReportPlan(TypedDict, total=False):
    """Contains detailed information about a report plan."""

    ReportPlanArn: Optional[ARN]
    ReportPlanName: Optional[ReportPlanName]
    ReportPlanDescription: Optional[ReportPlanDescription]
    ReportSetting: Optional[ReportSetting]
    ReportDeliveryChannel: Optional[ReportDeliveryChannel]
    DeploymentStatus: Optional[string]
    CreationTime: Optional[timestamp]
    LastAttemptedExecutionTime: Optional[timestamp]
    LastSuccessfulExecutionTime: Optional[timestamp]


class DescribeReportPlanOutput(TypedDict, total=False):
    ReportPlan: Optional[ReportPlan]


class DescribeRestoreJobInput(ServiceRequest):
    RestoreJobId: RestoreJobId


class RestoreJobCreator(TypedDict, total=False):
    """Contains information about the restore testing plan that Backup used to
    initiate the restore job.
    """

    RestoreTestingPlanArn: Optional[ARN]


class DescribeRestoreJobOutput(TypedDict, total=False):
    AccountId: Optional[AccountId]
    RestoreJobId: Optional[string]
    RecoveryPointArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    Status: Optional[RestoreJobStatus]
    StatusMessage: Optional[string]
    PercentDone: Optional[string]
    BackupSizeInBytes: Optional[Long]
    IamRoleArn: Optional[IAMRoleArn]
    ExpectedCompletionTimeMinutes: Optional[Long]
    CreatedResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    RecoveryPointCreationDate: Optional[timestamp]
    CreatedBy: Optional[RestoreJobCreator]
    ValidationStatus: Optional[RestoreValidationStatus]
    ValidationStatusMessage: Optional[string]
    DeletionStatus: Optional[RestoreDeletionStatus]
    DeletionStatusMessage: Optional[string]


class DisassociateRecoveryPointFromParentInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN


class DisassociateRecoveryPointInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN


class ExportBackupPlanTemplateInput(ServiceRequest):
    BackupPlanId: string


class ExportBackupPlanTemplateOutput(TypedDict, total=False):
    BackupPlanTemplateJson: Optional[string]


class Framework(TypedDict, total=False):
    """Contains detailed information about a framework. Frameworks contain
    controls, which evaluate and report on your backup events and resources.
    Frameworks generate daily compliance results.
    """

    FrameworkName: Optional[FrameworkName]
    FrameworkArn: Optional[ARN]
    FrameworkDescription: Optional[FrameworkDescription]
    NumberOfControls: Optional[integer]
    CreationTime: Optional[timestamp]
    DeploymentStatus: Optional[string]


FrameworkList = List[Framework]


class GetBackupPlanFromJSONInput(ServiceRequest):
    BackupPlanTemplateJson: string


class GetBackupPlanFromJSONOutput(TypedDict, total=False):
    BackupPlan: Optional[BackupPlan]


class GetBackupPlanFromTemplateInput(ServiceRequest):
    BackupPlanTemplateId: string


class GetBackupPlanFromTemplateOutput(TypedDict, total=False):
    BackupPlanDocument: Optional[BackupPlan]


class GetBackupPlanInput(ServiceRequest):
    BackupPlanId: string
    VersionId: Optional[string]


class GetBackupPlanOutput(TypedDict, total=False):
    BackupPlan: Optional[BackupPlan]
    BackupPlanId: Optional[string]
    BackupPlanArn: Optional[ARN]
    VersionId: Optional[string]
    CreatorRequestId: Optional[string]
    CreationDate: Optional[timestamp]
    DeletionDate: Optional[timestamp]
    LastExecutionDate: Optional[timestamp]
    AdvancedBackupSettings: Optional[AdvancedBackupSettings]


class GetBackupSelectionInput(ServiceRequest):
    BackupPlanId: string
    SelectionId: string


class GetBackupSelectionOutput(TypedDict, total=False):
    BackupSelection: Optional[BackupSelection]
    SelectionId: Optional[string]
    BackupPlanId: Optional[string]
    CreationDate: Optional[timestamp]
    CreatorRequestId: Optional[string]


class GetBackupVaultAccessPolicyInput(ServiceRequest):
    BackupVaultName: BackupVaultName


class GetBackupVaultAccessPolicyOutput(TypedDict, total=False):
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    Policy: Optional[IAMPolicy]


class GetBackupVaultNotificationsInput(ServiceRequest):
    BackupVaultName: BackupVaultName


class GetBackupVaultNotificationsOutput(TypedDict, total=False):
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    SNSTopicArn: Optional[ARN]
    BackupVaultEvents: Optional[BackupVaultEvents]


class GetLegalHoldInput(ServiceRequest):
    LegalHoldId: string


class GetLegalHoldOutput(TypedDict, total=False):
    Title: Optional[string]
    Status: Optional[LegalHoldStatus]
    Description: Optional[string]
    CancelDescription: Optional[string]
    LegalHoldId: Optional[string]
    LegalHoldArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CancellationDate: Optional[timestamp]
    RetainRecordUntil: Optional[timestamp]
    RecoveryPointSelection: Optional[RecoveryPointSelection]


class GetRecoveryPointIndexDetailsInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN


class GetRecoveryPointIndexDetailsOutput(TypedDict, total=False):
    RecoveryPointArn: Optional[ARN]
    BackupVaultArn: Optional[ARN]
    SourceResourceArn: Optional[ARN]
    IndexCreationDate: Optional[timestamp]
    IndexDeletionDate: Optional[timestamp]
    IndexCompletionDate: Optional[timestamp]
    IndexStatus: Optional[IndexStatus]
    IndexStatusMessage: Optional[string]
    TotalItemsIndexed: Optional[Long]


class GetRecoveryPointRestoreMetadataInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN
    BackupVaultAccountId: Optional[AccountId]


Metadata = Dict[MetadataKey, MetadataValue]


class GetRecoveryPointRestoreMetadataOutput(TypedDict, total=False):
    BackupVaultArn: Optional[ARN]
    RecoveryPointArn: Optional[ARN]
    RestoreMetadata: Optional[Metadata]
    ResourceType: Optional[ResourceType]


class GetRestoreJobMetadataInput(ServiceRequest):
    RestoreJobId: RestoreJobId


class GetRestoreJobMetadataOutput(TypedDict, total=False):
    RestoreJobId: Optional[RestoreJobId]
    Metadata: Optional[Metadata]


class GetRestoreTestingInferredMetadataInput(ServiceRequest):
    BackupVaultAccountId: Optional[String]
    BackupVaultName: String
    RecoveryPointArn: String


class GetRestoreTestingInferredMetadataOutput(TypedDict, total=False):
    InferredMetadata: stringMap


class GetRestoreTestingPlanInput(ServiceRequest):
    RestoreTestingPlanName: String


class RestoreTestingPlanForGet(TypedDict, total=False):
    """This contains metadata about a restore testing plan."""

    CreationTime: Timestamp
    CreatorRequestId: Optional[String]
    LastExecutionTime: Optional[Timestamp]
    LastUpdateTime: Optional[Timestamp]
    RecoveryPointSelection: RestoreTestingRecoveryPointSelection
    RestoreTestingPlanArn: String
    RestoreTestingPlanName: String
    ScheduleExpression: String
    ScheduleExpressionTimezone: Optional[String]
    StartWindowHours: Optional[integer]


class GetRestoreTestingPlanOutput(TypedDict, total=False):
    RestoreTestingPlan: RestoreTestingPlanForGet


class GetRestoreTestingSelectionInput(ServiceRequest):
    RestoreTestingPlanName: String
    RestoreTestingSelectionName: String


class RestoreTestingSelectionForGet(TypedDict, total=False):
    """This contains metadata about a restore testing selection."""

    CreationTime: Timestamp
    CreatorRequestId: Optional[String]
    IamRoleArn: String
    ProtectedResourceArns: Optional[stringList]
    ProtectedResourceConditions: Optional[ProtectedResourceConditions]
    ProtectedResourceType: String
    RestoreMetadataOverrides: Optional[SensitiveStringMap]
    RestoreTestingPlanName: String
    RestoreTestingSelectionName: String
    ValidationWindowHours: Optional[integer]


class GetRestoreTestingSelectionOutput(TypedDict, total=False):
    RestoreTestingSelection: RestoreTestingSelectionForGet


class GetSupportedResourceTypesOutput(TypedDict, total=False):
    ResourceTypes: Optional[ResourceTypes]


class IndexedRecoveryPoint(TypedDict, total=False):
    """This is a recovery point that has an associated backup index.

    Only recovery points with a backup index can be included in a search.
    """

    RecoveryPointArn: Optional[ARN]
    SourceResourceArn: Optional[ARN]
    IamRoleArn: Optional[ARN]
    BackupCreationDate: Optional[timestamp]
    ResourceType: Optional[ResourceType]
    IndexCreationDate: Optional[timestamp]
    IndexStatus: Optional[IndexStatus]
    IndexStatusMessage: Optional[string]
    BackupVaultArn: Optional[ARN]


IndexedRecoveryPointList = List[IndexedRecoveryPoint]


class LegalHold(TypedDict, total=False):
    """A legal hold is an administrative tool that helps prevent backups from
    being deleted while under a hold. While the hold is in place, backups
    under a hold cannot be deleted and lifecycle policies that would alter
    the backup status (such as transition to cold storage) are delayed until
    the legal hold is removed. A backup can have more than one legal hold.
    Legal holds are applied to one or more backups (also known as recovery
    points). These backups can be filtered by resource types and by resource
    IDs.
    """

    Title: Optional[string]
    Status: Optional[LegalHoldStatus]
    Description: Optional[string]
    LegalHoldId: Optional[string]
    LegalHoldArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CancellationDate: Optional[timestamp]


LegalHoldsList = List[LegalHold]


class ListBackupJobSummariesInput(ServiceRequest):
    AccountId: Optional[AccountId]
    State: Optional[BackupJobStatus]
    ResourceType: Optional[ResourceType]
    MessageCategory: Optional[MessageCategory]
    AggregationPeriod: Optional[AggregationPeriod]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[string]


class ListBackupJobSummariesOutput(TypedDict, total=False):
    BackupJobSummaries: Optional[BackupJobSummaryList]
    AggregationPeriod: Optional[string]
    NextToken: Optional[string]


class ListBackupJobsInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    ByResourceArn: Optional[ARN]
    ByState: Optional[BackupJobState]
    ByBackupVaultName: Optional[BackupVaultName]
    ByCreatedBefore: Optional[timestamp]
    ByCreatedAfter: Optional[timestamp]
    ByResourceType: Optional[ResourceType]
    ByAccountId: Optional[AccountId]
    ByCompleteAfter: Optional[timestamp]
    ByCompleteBefore: Optional[timestamp]
    ByParentJobId: Optional[string]
    ByMessageCategory: Optional[string]


class ListBackupJobsOutput(TypedDict, total=False):
    BackupJobs: Optional[BackupJobsList]
    NextToken: Optional[string]


class ListBackupPlanTemplatesInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListBackupPlanTemplatesOutput(TypedDict, total=False):
    NextToken: Optional[string]
    BackupPlanTemplatesList: Optional[BackupPlanTemplatesList]


class ListBackupPlanVersionsInput(ServiceRequest):
    BackupPlanId: string
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListBackupPlanVersionsOutput(TypedDict, total=False):
    NextToken: Optional[string]
    BackupPlanVersionsList: Optional[BackupPlanVersionsList]


class ListBackupPlansInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    IncludeDeleted: Optional[Boolean]


class ListBackupPlansOutput(TypedDict, total=False):
    NextToken: Optional[string]
    BackupPlansList: Optional[BackupPlansList]


class ListBackupSelectionsInput(ServiceRequest):
    BackupPlanId: string
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListBackupSelectionsOutput(TypedDict, total=False):
    NextToken: Optional[string]
    BackupSelectionsList: Optional[BackupSelectionsList]


class ListBackupVaultsInput(ServiceRequest):
    ByVaultType: Optional[VaultType]
    ByShared: Optional[boolean]
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListBackupVaultsOutput(TypedDict, total=False):
    BackupVaultList: Optional[BackupVaultList]
    NextToken: Optional[string]


class ListCopyJobSummariesInput(ServiceRequest):
    AccountId: Optional[AccountId]
    State: Optional[CopyJobStatus]
    ResourceType: Optional[ResourceType]
    MessageCategory: Optional[MessageCategory]
    AggregationPeriod: Optional[AggregationPeriod]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[string]


class ListCopyJobSummariesOutput(TypedDict, total=False):
    CopyJobSummaries: Optional[CopyJobSummaryList]
    AggregationPeriod: Optional[string]
    NextToken: Optional[string]


class ListCopyJobsInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    ByResourceArn: Optional[ARN]
    ByState: Optional[CopyJobState]
    ByCreatedBefore: Optional[timestamp]
    ByCreatedAfter: Optional[timestamp]
    ByResourceType: Optional[ResourceType]
    ByDestinationVaultArn: Optional[string]
    ByAccountId: Optional[AccountId]
    ByCompleteBefore: Optional[timestamp]
    ByCompleteAfter: Optional[timestamp]
    ByParentJobId: Optional[string]
    ByMessageCategory: Optional[string]


class ListCopyJobsOutput(TypedDict, total=False):
    CopyJobs: Optional[CopyJobsList]
    NextToken: Optional[string]


class ListFrameworksInput(ServiceRequest):
    MaxResults: Optional[MaxFrameworkInputs]
    NextToken: Optional[string]


class ListFrameworksOutput(TypedDict, total=False):
    Frameworks: Optional[FrameworkList]
    NextToken: Optional[string]


class ListIndexedRecoveryPointsInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    SourceResourceArn: Optional[ARN]
    CreatedBefore: Optional[timestamp]
    CreatedAfter: Optional[timestamp]
    ResourceType: Optional[ResourceType]
    IndexStatus: Optional[IndexStatus]


class ListIndexedRecoveryPointsOutput(TypedDict, total=False):
    IndexedRecoveryPoints: Optional[IndexedRecoveryPointList]
    NextToken: Optional[string]


class ListLegalHoldsInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListLegalHoldsOutput(TypedDict, total=False):
    NextToken: Optional[string]
    LegalHolds: Optional[LegalHoldsList]


class ListProtectedResourcesByBackupVaultInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    BackupVaultAccountId: Optional[AccountId]
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ProtectedResource(TypedDict, total=False):
    """A structure that contains information about a backed-up resource."""

    ResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    LastBackupTime: Optional[timestamp]
    ResourceName: Optional[string]
    LastBackupVaultArn: Optional[ARN]
    LastRecoveryPointArn: Optional[ARN]


ProtectedResourcesList = List[ProtectedResource]


class ListProtectedResourcesByBackupVaultOutput(TypedDict, total=False):
    Results: Optional[ProtectedResourcesList]
    NextToken: Optional[string]


class ListProtectedResourcesInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListProtectedResourcesOutput(TypedDict, total=False):
    Results: Optional[ProtectedResourcesList]
    NextToken: Optional[string]


class ListRecoveryPointsByBackupVaultInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    BackupVaultAccountId: Optional[AccountId]
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    ByResourceArn: Optional[ARN]
    ByResourceType: Optional[ResourceType]
    ByBackupPlanId: Optional[string]
    ByCreatedBefore: Optional[timestamp]
    ByCreatedAfter: Optional[timestamp]
    ByParentRecoveryPointArn: Optional[ARN]


class RecoveryPointByBackupVault(TypedDict, total=False):
    """Contains detailed information about the recovery points stored in a
    backup vault.
    """

    RecoveryPointArn: Optional[ARN]
    BackupVaultName: Optional[BackupVaultName]
    BackupVaultArn: Optional[ARN]
    SourceBackupVaultArn: Optional[ARN]
    ResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    CreatedBy: Optional[RecoveryPointCreator]
    IamRoleArn: Optional[IAMRoleArn]
    Status: Optional[RecoveryPointStatus]
    StatusMessage: Optional[string]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    BackupSizeInBytes: Optional[Long]
    CalculatedLifecycle: Optional[CalculatedLifecycle]
    Lifecycle: Optional[Lifecycle]
    EncryptionKeyArn: Optional[ARN]
    IsEncrypted: Optional[boolean]
    LastRestoreTime: Optional[timestamp]
    ParentRecoveryPointArn: Optional[ARN]
    CompositeMemberIdentifier: Optional[string]
    IsParent: Optional[boolean]
    ResourceName: Optional[string]
    VaultType: Optional[VaultType]
    IndexStatus: Optional[IndexStatus]
    IndexStatusMessage: Optional[string]


RecoveryPointByBackupVaultList = List[RecoveryPointByBackupVault]


class ListRecoveryPointsByBackupVaultOutput(TypedDict, total=False):
    NextToken: Optional[string]
    RecoveryPoints: Optional[RecoveryPointByBackupVaultList]


class ListRecoveryPointsByLegalHoldInput(ServiceRequest):
    LegalHoldId: string
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class RecoveryPointMember(TypedDict, total=False):
    """This is a recovery point which is a child (nested) recovery point of a
    parent (composite) recovery point. These recovery points can be
    disassociated from their parent (composite) recovery point, in which
    case they will no longer be a member.
    """

    RecoveryPointArn: Optional[ARN]
    ResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    BackupVaultName: Optional[BackupVaultName]


RecoveryPointsList = List[RecoveryPointMember]


class ListRecoveryPointsByLegalHoldOutput(TypedDict, total=False):
    RecoveryPoints: Optional[RecoveryPointsList]
    NextToken: Optional[string]


class ListRecoveryPointsByResourceInput(ServiceRequest):
    ResourceArn: ARN
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    ManagedByAWSBackupOnly: Optional[boolean]


class RecoveryPointByResource(TypedDict, total=False):
    """Contains detailed information about a saved recovery point."""

    RecoveryPointArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    Status: Optional[RecoveryPointStatus]
    StatusMessage: Optional[string]
    EncryptionKeyArn: Optional[ARN]
    BackupSizeBytes: Optional[Long]
    BackupVaultName: Optional[BackupVaultName]
    IsParent: Optional[boolean]
    ParentRecoveryPointArn: Optional[ARN]
    ResourceName: Optional[string]
    VaultType: Optional[VaultType]
    IndexStatus: Optional[IndexStatus]
    IndexStatusMessage: Optional[string]


RecoveryPointByResourceList = List[RecoveryPointByResource]


class ListRecoveryPointsByResourceOutput(TypedDict, total=False):
    NextToken: Optional[string]
    RecoveryPoints: Optional[RecoveryPointByResourceList]


class ListReportJobsInput(ServiceRequest):
    ByReportPlanName: Optional[ReportPlanName]
    ByCreationBefore: Optional[timestamp]
    ByCreationAfter: Optional[timestamp]
    ByStatus: Optional[string]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[string]


ReportJobList = List[ReportJob]


class ListReportJobsOutput(TypedDict, total=False):
    ReportJobs: Optional[ReportJobList]
    NextToken: Optional[string]


class ListReportPlansInput(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[string]


ReportPlanList = List[ReportPlan]


class ListReportPlansOutput(TypedDict, total=False):
    ReportPlans: Optional[ReportPlanList]
    NextToken: Optional[string]


class ListRestoreJobSummariesInput(ServiceRequest):
    AccountId: Optional[AccountId]
    State: Optional[RestoreJobState]
    ResourceType: Optional[ResourceType]
    AggregationPeriod: Optional[AggregationPeriod]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[string]


class RestoreJobSummary(TypedDict, total=False):
    """This is a summary of restore jobs created or running within the most
    recent 30 days.

    The returned summary may contain the following: Region, Account, State,
    ResourceType, MessageCategory, StartTime, EndTime, and Count of included
    jobs.
    """

    Region: Optional[Region]
    AccountId: Optional[AccountId]
    State: Optional[RestoreJobState]
    ResourceType: Optional[ResourceType]
    Count: Optional[integer]
    StartTime: Optional[timestamp]
    EndTime: Optional[timestamp]


RestoreJobSummaryList = List[RestoreJobSummary]


class ListRestoreJobSummariesOutput(TypedDict, total=False):
    RestoreJobSummaries: Optional[RestoreJobSummaryList]
    AggregationPeriod: Optional[string]
    NextToken: Optional[string]


class ListRestoreJobsByProtectedResourceInput(ServiceRequest):
    ResourceArn: ARN
    ByStatus: Optional[RestoreJobStatus]
    ByRecoveryPointCreationDateAfter: Optional[timestamp]
    ByRecoveryPointCreationDateBefore: Optional[timestamp]
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class RestoreJobsListMember(TypedDict, total=False):
    """Contains metadata about a restore job."""

    AccountId: Optional[AccountId]
    RestoreJobId: Optional[string]
    RecoveryPointArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    CompletionDate: Optional[timestamp]
    Status: Optional[RestoreJobStatus]
    StatusMessage: Optional[string]
    PercentDone: Optional[string]
    BackupSizeInBytes: Optional[Long]
    IamRoleArn: Optional[IAMRoleArn]
    ExpectedCompletionTimeMinutes: Optional[Long]
    CreatedResourceArn: Optional[ARN]
    ResourceType: Optional[ResourceType]
    RecoveryPointCreationDate: Optional[timestamp]
    CreatedBy: Optional[RestoreJobCreator]
    ValidationStatus: Optional[RestoreValidationStatus]
    ValidationStatusMessage: Optional[string]
    DeletionStatus: Optional[RestoreDeletionStatus]
    DeletionStatusMessage: Optional[string]


RestoreJobsList = List[RestoreJobsListMember]


class ListRestoreJobsByProtectedResourceOutput(TypedDict, total=False):
    RestoreJobs: Optional[RestoreJobsList]
    NextToken: Optional[string]


class ListRestoreJobsInput(ServiceRequest):
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]
    ByAccountId: Optional[AccountId]
    ByResourceType: Optional[ResourceType]
    ByCreatedBefore: Optional[timestamp]
    ByCreatedAfter: Optional[timestamp]
    ByStatus: Optional[RestoreJobStatus]
    ByCompleteBefore: Optional[timestamp]
    ByCompleteAfter: Optional[timestamp]
    ByRestoreTestingPlanArn: Optional[ARN]


class ListRestoreJobsOutput(TypedDict, total=False):
    RestoreJobs: Optional[RestoreJobsList]
    NextToken: Optional[string]


class ListRestoreTestingPlansInput(ServiceRequest):
    MaxResults: Optional[ListRestoreTestingPlansInputMaxResultsInteger]
    NextToken: Optional[String]


class RestoreTestingPlanForList(TypedDict, total=False):
    """This contains metadata about a restore testing plan."""

    CreationTime: Timestamp
    LastExecutionTime: Optional[Timestamp]
    LastUpdateTime: Optional[Timestamp]
    RestoreTestingPlanArn: String
    RestoreTestingPlanName: String
    ScheduleExpression: String
    ScheduleExpressionTimezone: Optional[String]
    StartWindowHours: Optional[integer]


RestoreTestingPlans = List[RestoreTestingPlanForList]


class ListRestoreTestingPlansOutput(TypedDict, total=False):
    NextToken: Optional[String]
    RestoreTestingPlans: RestoreTestingPlans


class ListRestoreTestingSelectionsInput(ServiceRequest):
    MaxResults: Optional[ListRestoreTestingSelectionsInputMaxResultsInteger]
    NextToken: Optional[String]
    RestoreTestingPlanName: String


class RestoreTestingSelectionForList(TypedDict, total=False):
    """This contains metadata about a restore testing selection."""

    CreationTime: Timestamp
    IamRoleArn: String
    ProtectedResourceType: String
    RestoreTestingPlanName: String
    RestoreTestingSelectionName: String
    ValidationWindowHours: Optional[integer]


RestoreTestingSelections = List[RestoreTestingSelectionForList]


class ListRestoreTestingSelectionsOutput(TypedDict, total=False):
    NextToken: Optional[String]
    RestoreTestingSelections: RestoreTestingSelections


class ListTagsInput(ServiceRequest):
    ResourceArn: ARN
    NextToken: Optional[string]
    MaxResults: Optional[MaxResults]


class ListTagsOutput(TypedDict, total=False):
    NextToken: Optional[string]
    Tags: Optional[Tags]


class PutBackupVaultAccessPolicyInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    Policy: Optional[IAMPolicy]


class PutBackupVaultLockConfigurationInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    MinRetentionDays: Optional[Long]
    MaxRetentionDays: Optional[Long]
    ChangeableForDays: Optional[Long]


class PutBackupVaultNotificationsInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    SNSTopicArn: ARN
    BackupVaultEvents: BackupVaultEvents


class PutRestoreValidationResultInput(ServiceRequest):
    RestoreJobId: RestoreJobId
    ValidationStatus: RestoreValidationStatus
    ValidationStatusMessage: Optional[string]


class RestoreTestingPlanForUpdate(TypedDict, total=False):
    """This contains metadata about a restore testing plan."""

    RecoveryPointSelection: Optional[RestoreTestingRecoveryPointSelection]
    ScheduleExpression: Optional[String]
    ScheduleExpressionTimezone: Optional[String]
    StartWindowHours: Optional[integer]


class RestoreTestingSelectionForUpdate(TypedDict, total=False):
    """This contains metadata about a restore testing selection."""

    IamRoleArn: Optional[String]
    ProtectedResourceArns: Optional[stringList]
    ProtectedResourceConditions: Optional[ProtectedResourceConditions]
    RestoreMetadataOverrides: Optional[SensitiveStringMap]
    ValidationWindowHours: Optional[integer]


class StartBackupJobInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    ResourceArn: ARN
    IamRoleArn: IAMRoleArn
    IdempotencyToken: Optional[string]
    StartWindowMinutes: Optional[WindowMinutes]
    CompleteWindowMinutes: Optional[WindowMinutes]
    Lifecycle: Optional[Lifecycle]
    RecoveryPointTags: Optional[Tags]
    BackupOptions: Optional[BackupOptions]
    Index: Optional[Index]


class StartBackupJobOutput(TypedDict, total=False):
    BackupJobId: Optional[string]
    RecoveryPointArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    IsParent: Optional[boolean]


class StartCopyJobInput(ServiceRequest):
    RecoveryPointArn: ARN
    SourceBackupVaultName: BackupVaultName
    DestinationBackupVaultArn: ARN
    IamRoleArn: IAMRoleArn
    IdempotencyToken: Optional[string]
    Lifecycle: Optional[Lifecycle]


class StartCopyJobOutput(TypedDict, total=False):
    CopyJobId: Optional[string]
    CreationDate: Optional[timestamp]
    IsParent: Optional[boolean]


class StartReportJobInput(ServiceRequest):
    ReportPlanName: ReportPlanName
    IdempotencyToken: Optional[string]


class StartReportJobOutput(TypedDict, total=False):
    ReportJobId: Optional[ReportJobId]


class StartRestoreJobInput(ServiceRequest):
    RecoveryPointArn: ARN
    Metadata: Metadata
    IamRoleArn: Optional[IAMRoleArn]
    IdempotencyToken: Optional[string]
    ResourceType: Optional[ResourceType]
    CopySourceTagsToRestoredResource: Optional[boolean]


class StartRestoreJobOutput(TypedDict, total=False):
    RestoreJobId: Optional[RestoreJobId]


class StopBackupJobInput(ServiceRequest):
    BackupJobId: string


TagKeyList = List[string]


class TagResourceInput(ServiceRequest):
    ResourceArn: ARN
    Tags: Tags


class UntagResourceInput(ServiceRequest):
    ResourceArn: ARN
    TagKeyList: TagKeyList


class UpdateBackupPlanInput(ServiceRequest):
    BackupPlanId: string
    BackupPlan: BackupPlanInput


class UpdateBackupPlanOutput(TypedDict, total=False):
    BackupPlanId: Optional[string]
    BackupPlanArn: Optional[ARN]
    CreationDate: Optional[timestamp]
    VersionId: Optional[string]
    AdvancedBackupSettings: Optional[AdvancedBackupSettings]


class UpdateFrameworkInput(ServiceRequest):
    FrameworkName: FrameworkName
    FrameworkDescription: Optional[FrameworkDescription]
    FrameworkControls: Optional[FrameworkControls]
    IdempotencyToken: Optional[string]


class UpdateFrameworkOutput(TypedDict, total=False):
    FrameworkName: Optional[FrameworkName]
    FrameworkArn: Optional[ARN]
    CreationTime: Optional[timestamp]


class UpdateGlobalSettingsInput(ServiceRequest):
    GlobalSettings: Optional[GlobalSettings]


class UpdateRecoveryPointIndexSettingsInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN
    IamRoleArn: Optional[IAMRoleArn]
    Index: Index


class UpdateRecoveryPointIndexSettingsOutput(TypedDict, total=False):
    BackupVaultName: Optional[BackupVaultName]
    RecoveryPointArn: Optional[ARN]
    IndexStatus: Optional[IndexStatus]
    Index: Optional[Index]


class UpdateRecoveryPointLifecycleInput(ServiceRequest):
    BackupVaultName: BackupVaultName
    RecoveryPointArn: ARN
    Lifecycle: Optional[Lifecycle]


class UpdateRecoveryPointLifecycleOutput(TypedDict, total=False):
    BackupVaultArn: Optional[ARN]
    RecoveryPointArn: Optional[ARN]
    Lifecycle: Optional[Lifecycle]
    CalculatedLifecycle: Optional[CalculatedLifecycle]


class UpdateRegionSettingsInput(ServiceRequest):
    ResourceTypeOptInPreference: Optional[ResourceTypeOptInPreference]
    ResourceTypeManagementPreference: Optional[ResourceTypeManagementPreference]


class UpdateReportPlanInput(ServiceRequest):
    ReportPlanName: ReportPlanName
    ReportPlanDescription: Optional[ReportPlanDescription]
    ReportDeliveryChannel: Optional[ReportDeliveryChannel]
    ReportSetting: Optional[ReportSetting]
    IdempotencyToken: Optional[string]


class UpdateReportPlanOutput(TypedDict, total=False):
    ReportPlanName: Optional[ReportPlanName]
    ReportPlanArn: Optional[ARN]
    CreationTime: Optional[timestamp]


class UpdateRestoreTestingPlanInput(ServiceRequest):
    RestoreTestingPlan: RestoreTestingPlanForUpdate
    RestoreTestingPlanName: String


class UpdateRestoreTestingPlanOutput(TypedDict, total=False):
    CreationTime: Timestamp
    RestoreTestingPlanArn: String
    RestoreTestingPlanName: String
    UpdateTime: Timestamp


class UpdateRestoreTestingSelectionInput(ServiceRequest):
    RestoreTestingPlanName: String
    RestoreTestingSelection: RestoreTestingSelectionForUpdate
    RestoreTestingSelectionName: String


class UpdateRestoreTestingSelectionOutput(TypedDict, total=False):
    CreationTime: Timestamp
    RestoreTestingPlanArn: String
    RestoreTestingPlanName: String
    RestoreTestingSelectionName: String
    UpdateTime: Timestamp


class BackupApi:
    service = "backup"
    version = "2018-11-15"

    @handler("CancelLegalHold")
    def cancel_legal_hold(
        self,
        context: RequestContext,
        legal_hold_id: string,
        cancel_description: string,
        retain_record_in_days: Long | None = None,
        **kwargs,
    ) -> CancelLegalHoldOutput:
        """Removes the specified legal hold on a recovery point. This action can
        only be performed by a user with sufficient permissions.

        :param legal_hold_id: The ID of the legal hold.
        :param cancel_description: A string the describes the reason for removing the legal hold.
        :param retain_record_in_days: The integer amount, in days, after which to remove legal hold.
        :returns: CancelLegalHoldOutput
        :raises InvalidParameterValueException:
        :raises InvalidResourceStateException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("CreateBackupPlan")
    def create_backup_plan(
        self,
        context: RequestContext,
        backup_plan: BackupPlanInput,
        backup_plan_tags: Tags | None = None,
        creator_request_id: string | None = None,
        **kwargs,
    ) -> CreateBackupPlanOutput:
        """Creates a backup plan using a backup plan name and backup rules. A
        backup plan is a document that contains information that Backup uses to
        schedule tasks that create recovery points for resources.

        If you call ``CreateBackupPlan`` with a plan that already exists, you
        receive an ``AlreadyExistsException`` exception.

        :param backup_plan: The body of a backup plan.
        :param backup_plan_tags: The tags to assign to the backup plan.
        :param creator_request_id: Identifies the request and allows failed requests to be retried without
        the risk of running the operation twice.
        :returns: CreateBackupPlanOutput
        :raises LimitExceededException:
        :raises AlreadyExistsException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreateBackupSelection")
    def create_backup_selection(
        self,
        context: RequestContext,
        backup_plan_id: string,
        backup_selection: BackupSelection,
        creator_request_id: string | None = None,
        **kwargs,
    ) -> CreateBackupSelectionOutput:
        """Creates a JSON document that specifies a set of resources to assign to a
        backup plan. For examples, see `Assigning resources
        programmatically <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-json>`__.

        :param backup_plan_id: The ID of the backup plan.
        :param backup_selection: The body of a request to assign a set of resources to a backup plan.
        :param creator_request_id: A unique string that identifies the request and allows failed requests
        to be retried without the risk of running the operation twice.
        :returns: CreateBackupSelectionOutput
        :raises LimitExceededException:
        :raises AlreadyExistsException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreateBackupVault")
    def create_backup_vault(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        backup_vault_tags: Tags | None = None,
        encryption_key_arn: ARN | None = None,
        creator_request_id: string | None = None,
        **kwargs,
    ) -> CreateBackupVaultOutput:
        """Creates a logical container where backups are stored. A
        ``CreateBackupVault`` request includes a name, optionally one or more
        resource tags, an encryption key, and a request ID.

        Do not include sensitive data, such as passport numbers, in the name of
        a backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param backup_vault_tags: The tags to assign to the backup vault.
        :param encryption_key_arn: The server-side encryption key that is used to protect your backups; for
        example,
        ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``.
        :param creator_request_id: A unique string that identifies the request and allows failed requests
        to be retried without the risk of running the operation twice.
        :returns: CreateBackupVaultOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises LimitExceededException:
        :raises AlreadyExistsException:
        """
        raise NotImplementedError

    @handler("CreateFramework")
    def create_framework(
        self,
        context: RequestContext,
        framework_name: FrameworkName,
        framework_controls: FrameworkControls,
        framework_description: FrameworkDescription | None = None,
        idempotency_token: string | None = None,
        framework_tags: stringMap | None = None,
        **kwargs,
    ) -> CreateFrameworkOutput:
        """Creates a framework with one or more controls. A framework is a
        collection of controls that you can use to evaluate your backup
        practices. By using pre-built customizable controls to define your
        policies, you can evaluate whether your backup practices comply with
        your policies and which resources are not yet in compliance.

        :param framework_name: The unique name of the framework.
        :param framework_controls: The controls that make up the framework.
        :param framework_description: An optional description of the framework with a maximum of 1,024
        characters.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``CreateFrameworkInput``.
        :param framework_tags: The tags to assign to the framework.
        :returns: CreateFrameworkOutput
        :raises AlreadyExistsException:
        :raises LimitExceededException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreateLegalHold")
    def create_legal_hold(
        self,
        context: RequestContext,
        title: string,
        description: string,
        idempotency_token: string | None = None,
        recovery_point_selection: RecoveryPointSelection | None = None,
        tags: Tags | None = None,
        **kwargs,
    ) -> CreateLegalHoldOutput:
        """Creates a legal hold on a recovery point (backup). A legal hold is a
        restraint on altering or deleting a backup until an authorized user
        cancels the legal hold. Any actions to delete or disassociate a recovery
        point will fail with an error if one or more active legal holds are on
        the recovery point.

        :param title: The title of the legal hold.
        :param description: The description of the legal hold.
        :param idempotency_token: This is a user-chosen string used to distinguish between otherwise
        identical calls.
        :param recovery_point_selection: The criteria to assign a set of resources, such as resource types or
        backup vaults.
        :param tags: Optional tags to include.
        :returns: CreateLegalHoldOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateLogicallyAirGappedBackupVault")
    def create_logically_air_gapped_backup_vault(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        min_retention_days: Long,
        max_retention_days: Long,
        backup_vault_tags: Tags | None = None,
        creator_request_id: string | None = None,
        **kwargs,
    ) -> CreateLogicallyAirGappedBackupVaultOutput:
        """Creates a logical container to where backups may be copied.

        This request includes a name, the Region, the maximum number of
        retention days, the minimum number of retention days, and optionally can
        include tags and a creator request ID.

        Do not include sensitive data, such as passport numbers, in the name of
        a backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param min_retention_days: This setting specifies the minimum retention period that the vault
        retains its recovery points.
        :param max_retention_days: The maximum retention period that the vault retains its recovery points.
        :param backup_vault_tags: The tags to assign to the vault.
        :param creator_request_id: The ID of the creation request.
        :returns: CreateLogicallyAirGappedBackupVaultOutput
        :raises AlreadyExistsException:
        :raises InvalidParameterValueException:
        :raises LimitExceededException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("CreateReportPlan")
    def create_report_plan(
        self,
        context: RequestContext,
        report_plan_name: ReportPlanName,
        report_delivery_channel: ReportDeliveryChannel,
        report_setting: ReportSetting,
        report_plan_description: ReportPlanDescription | None = None,
        report_plan_tags: stringMap | None = None,
        idempotency_token: string | None = None,
        **kwargs,
    ) -> CreateReportPlanOutput:
        """Creates a report plan. A report plan is a document that contains
        information about the contents of the report and where Backup will
        deliver it.

        If you call ``CreateReportPlan`` with a plan that already exists, you
        receive an ``AlreadyExistsException`` exception.

        :param report_plan_name: The unique name of the report plan.
        :param report_delivery_channel: A structure that contains information about where and how to deliver
        your reports, specifically your Amazon S3 bucket name, S3 key prefix,
        and the formats of your reports.
        :param report_setting: Identifies the report template for the report.
        :param report_plan_description: An optional description of the report plan with a maximum of 1,024
        characters.
        :param report_plan_tags: The tags to assign to the report plan.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``CreateReportPlanInput``.
        :returns: CreateReportPlanOutput
        :raises AlreadyExistsException:
        :raises LimitExceededException:
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        :raises MissingParameterValueException:
        """
        raise NotImplementedError

    @handler("CreateRestoreTestingPlan")
    def create_restore_testing_plan(
        self,
        context: RequestContext,
        restore_testing_plan: RestoreTestingPlanForCreate,
        creator_request_id: String | None = None,
        tags: SensitiveStringMap | None = None,
        **kwargs,
    ) -> CreateRestoreTestingPlanOutput:
        """Creates a restore testing plan.

        The first of two steps to create a restore testing plan. After this
        request is successful, finish the procedure using
        CreateRestoreTestingSelection.

        :param restore_testing_plan: A restore testing plan must contain a unique ``RestoreTestingPlanName``
        string you create and must contain a ``ScheduleExpression`` cron.
        :param creator_request_id: This is a unique string that identifies the request and allows failed
        requests to be retriedwithout the risk of running the operation twice.
        :param tags: The tags to assign to the restore testing plan.
        :returns: CreateRestoreTestingPlanOutput
        :raises AlreadyExistsException:
        :raises ConflictException:
        :raises InvalidParameterValueException:
        :raises LimitExceededException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreateRestoreTestingSelection")
    def create_restore_testing_selection(
        self,
        context: RequestContext,
        restore_testing_plan_name: String,
        restore_testing_selection: RestoreTestingSelectionForCreate,
        creator_request_id: String | None = None,
        **kwargs,
    ) -> CreateRestoreTestingSelectionOutput:
        """This request can be sent after CreateRestoreTestingPlan request returns
        successfully. This is the second part of creating a resource testing
        plan, and it must be completed sequentially.

        This consists of ``RestoreTestingSelectionName``,
        ``ProtectedResourceType``, and one of the following:

        -  ``ProtectedResourceArns``

        -  ``ProtectedResourceConditions``

        Each protected resource type can have one single value.

        A restore testing selection can include a wildcard value ("*") for
        ``ProtectedResourceArns`` along with ``ProtectedResourceConditions``.
        Alternatively, you can include up to 30 specific protected resource ARNs
        in ``ProtectedResourceArns``.

        Cannot select by both protected resource types AND specific ARNs.
        Request will fail if both are included.

        :param restore_testing_plan_name: Input the restore testing plan name that was returned from the related
        CreateRestoreTestingPlan request.
        :param restore_testing_selection: This consists of ``RestoreTestingSelectionName``,
        ``ProtectedResourceType``, and one of the following:

        -  ``ProtectedResourceArns``

        -  ``ProtectedResourceConditions``

        Each protected resource type can have one single value.
        :param creator_request_id: This is an optional unique string that identifies the request and allows
        failed requests to be retried without the risk of running the operation
        twice.
        :returns: CreateRestoreTestingSelectionOutput
        :raises AlreadyExistsException:
        :raises InvalidParameterValueException:
        :raises LimitExceededException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteBackupPlan")
    def delete_backup_plan(
        self, context: RequestContext, backup_plan_id: string, **kwargs
    ) -> DeleteBackupPlanOutput:
        """Deletes a backup plan. A backup plan can only be deleted after all
        associated selections of resources have been deleted. Deleting a backup
        plan deletes the current version of a backup plan. Previous versions, if
        any, will still exist.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :returns: DeleteBackupPlanOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DeleteBackupSelection")
    def delete_backup_selection(
        self, context: RequestContext, backup_plan_id: string, selection_id: string, **kwargs
    ) -> None:
        """Deletes the resource selection associated with a backup plan that is
        specified by the ``SelectionId``.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param selection_id: Uniquely identifies the body of a request to assign a set of resources
        to a backup plan.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteBackupVault")
    def delete_backup_vault(
        self, context: RequestContext, backup_vault_name: string, **kwargs
    ) -> None:
        """Deletes the backup vault identified by its name. A vault can be deleted
        only if it is empty.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DeleteBackupVaultAccessPolicy")
    def delete_backup_vault_access_policy(
        self, context: RequestContext, backup_vault_name: BackupVaultName, **kwargs
    ) -> None:
        """Deletes the policy document that manages permissions on a backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteBackupVaultLockConfiguration")
    def delete_backup_vault_lock_configuration(
        self, context: RequestContext, backup_vault_name: BackupVaultName, **kwargs
    ) -> None:
        """Deletes Backup Vault Lock from a backup vault specified by a backup
        vault name.

        If the Vault Lock configuration is immutable, then you cannot delete
        Vault Lock using API operations, and you will receive an
        ``InvalidRequestException`` if you attempt to do so. For more
        information, see `Vault
        Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`__
        in the *Backup Developer Guide*.

        :param backup_vault_name: The name of the backup vault from which to delete Backup Vault Lock.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises InvalidRequestException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteBackupVaultNotifications")
    def delete_backup_vault_notifications(
        self, context: RequestContext, backup_vault_name: BackupVaultName, **kwargs
    ) -> None:
        """Deletes event notifications for the specified backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteFramework")
    def delete_framework(
        self, context: RequestContext, framework_name: FrameworkName, **kwargs
    ) -> None:
        """Deletes the framework specified by a framework name.

        :param framework_name: The unique name of a framework.
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        :raises ConflictException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteRecoveryPoint")
    def delete_recovery_point(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        **kwargs,
    ) -> None:
        """Deletes the recovery point specified by a recovery point ID.

        If the recovery point ID belongs to a continuous backup, calling this
        endpoint deletes the existing continuous backup and stops future
        continuous backup.

        When an IAM role's permissions are insufficient to call this API, the
        service sends back an HTTP 200 response with an empty HTTP body, but the
        recovery point is not deleted. Instead, it enters an ``EXPIRED`` state.

        ``EXPIRED`` recovery points can be deleted with this API once the IAM
        role has the ``iam:CreateServiceLinkedRole`` action. To learn more about
        adding this role, see `Troubleshooting manual
        deletions <https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html#deleting-backups-troubleshooting>`__.

        If the user or role is deleted or the permission within the role is
        removed, the deletion will not be successful and will enter an
        ``EXPIRED`` state.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point;
        for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises InvalidResourceStateException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DeleteReportPlan")
    def delete_report_plan(
        self, context: RequestContext, report_plan_name: ReportPlanName, **kwargs
    ) -> None:
        """Deletes the report plan specified by a report plan name.

        :param report_plan_name: The unique name of a report plan.
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        :raises ConflictException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteRestoreTestingPlan")
    def delete_restore_testing_plan(
        self, context: RequestContext, restore_testing_plan_name: String, **kwargs
    ) -> None:
        """This request deletes the specified restore testing plan.

        Deletion can only successfully occur if all associated restore testing
        selections are deleted first.

        :param restore_testing_plan_name: Required unique name of the restore testing plan you wish to delete.
        :raises InvalidRequestException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteRestoreTestingSelection")
    def delete_restore_testing_selection(
        self,
        context: RequestContext,
        restore_testing_plan_name: String,
        restore_testing_selection_name: String,
        **kwargs,
    ) -> None:
        """Input the Restore Testing Plan name and Restore Testing Selection name.

        All testing selections associated with a restore testing plan must be
        deleted before the restore testing plan can be deleted.

        :param restore_testing_plan_name: Required unique name of the restore testing plan that contains the
        restore testing selection you wish to delete.
        :param restore_testing_selection_name: Required unique name of the restore testing selection you wish to
        delete.
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeBackupJob")
    def describe_backup_job(
        self, context: RequestContext, backup_job_id: string, **kwargs
    ) -> DescribeBackupJobOutput:
        """Returns backup job details for the specified ``BackupJobId``.

        :param backup_job_id: Uniquely identifies a request to Backup to back up a resource.
        :returns: DescribeBackupJobOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises DependencyFailureException:
        """
        raise NotImplementedError

    @handler("DescribeBackupVault")
    def describe_backup_vault(
        self,
        context: RequestContext,
        backup_vault_name: string,
        backup_vault_account_id: string | None = None,
        **kwargs,
    ) -> DescribeBackupVaultOutput:
        """Returns metadata about a backup vault specified by its name.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param backup_vault_account_id: The account ID of the specified backup vault.
        :returns: DescribeBackupVaultOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeCopyJob")
    def describe_copy_job(
        self, context: RequestContext, copy_job_id: string, **kwargs
    ) -> DescribeCopyJobOutput:
        """Returns metadata associated with creating a copy of a resource.

        :param copy_job_id: Uniquely identifies a copy job.
        :returns: DescribeCopyJobOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeFramework")
    def describe_framework(
        self, context: RequestContext, framework_name: FrameworkName, **kwargs
    ) -> DescribeFrameworkOutput:
        """Returns the framework details for the specified ``FrameworkName``.

        :param framework_name: The unique name of a framework.
        :returns: DescribeFrameworkOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeGlobalSettings")
    def describe_global_settings(
        self, context: RequestContext, **kwargs
    ) -> DescribeGlobalSettingsOutput:
        """Describes whether the Amazon Web Services account is opted in to
        cross-account backup. Returns an error if the account is not a member of
        an Organizations organization. Example:
        ``describe-global-settings --region us-west-2``

        :returns: DescribeGlobalSettingsOutput
        :raises InvalidRequestException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeProtectedResource")
    def describe_protected_resource(
        self, context: RequestContext, resource_arn: ARN, **kwargs
    ) -> DescribeProtectedResourceOutput:
        """Returns information about a saved resource, including the last time it
        was backed up, its Amazon Resource Name (ARN), and the Amazon Web
        Services service type of the saved resource.

        :param resource_arn: An Amazon Resource Name (ARN) that uniquely identifies a resource.
        :returns: DescribeProtectedResourceOutput
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeRecoveryPoint")
    def describe_recovery_point(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        backup_vault_account_id: AccountId | None = None,
        **kwargs,
    ) -> DescribeRecoveryPointOutput:
        """Returns metadata associated with a recovery point, including ID, status,
        encryption, and lifecycle.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point;
        for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :param backup_vault_account_id: The account ID of the specified backup vault.
        :returns: DescribeRecoveryPointOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeRegionSettings")
    def describe_region_settings(
        self, context: RequestContext, **kwargs
    ) -> DescribeRegionSettingsOutput:
        """Returns the current service opt-in settings for the Region. If service
        opt-in is enabled for a service, Backup tries to protect that service's
        resources in this Region, when the resource is included in an on-demand
        backup or scheduled backup plan. Otherwise, Backup does not try to
        protect that service's resources in this Region.

        :returns: DescribeRegionSettingsOutput
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeReportJob")
    def describe_report_job(
        self, context: RequestContext, report_job_id: ReportJobId, **kwargs
    ) -> DescribeReportJobOutput:
        """Returns the details associated with creating a report as specified by
        its ``ReportJobId``.

        :param report_job_id: The identifier of the report job.
        :returns: DescribeReportJobOutput
        :raises ServiceUnavailableException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeReportPlan")
    def describe_report_plan(
        self, context: RequestContext, report_plan_name: ReportPlanName, **kwargs
    ) -> DescribeReportPlanOutput:
        """Returns a list of all report plans for an Amazon Web Services account
        and Amazon Web Services Region.

        :param report_plan_name: The unique name of a report plan.
        :returns: DescribeReportPlanOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeRestoreJob")
    def describe_restore_job(
        self, context: RequestContext, restore_job_id: RestoreJobId, **kwargs
    ) -> DescribeRestoreJobOutput:
        """Returns metadata associated with a restore job that is specified by a
        job ID.

        :param restore_job_id: Uniquely identifies the job that restores a recovery point.
        :returns: DescribeRestoreJobOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises DependencyFailureException:
        """
        raise NotImplementedError

    @handler("DisassociateRecoveryPoint")
    def disassociate_recovery_point(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        **kwargs,
    ) -> None:
        """Deletes the specified continuous backup recovery point from Backup and
        releases control of that continuous backup to the source service, such
        as Amazon RDS. The source service will continue to create and retain
        continuous backups using the lifecycle that you specified in your
        original backup plan.

        Does not support snapshot backup recovery points.

        :param backup_vault_name: The unique name of an Backup vault.
        :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies an Backup
        recovery point.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises InvalidResourceStateException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DisassociateRecoveryPointFromParent")
    def disassociate_recovery_point_from_parent(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        **kwargs,
    ) -> None:
        """This action to a specific child (nested) recovery point removes the
        relationship between the specified recovery point and its parent
        (composite) recovery point.

        :param backup_vault_name: The name of a logical container where the child (nested) recovery point
        is stored.
        :param recovery_point_arn: The Amazon Resource Name (ARN) that uniquely identifies the child
        (nested) recovery point; for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("ExportBackupPlanTemplate")
    def export_backup_plan_template(
        self, context: RequestContext, backup_plan_id: string, **kwargs
    ) -> ExportBackupPlanTemplateOutput:
        """Returns the backup plan that is specified by the plan ID as a backup
        template.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :returns: ExportBackupPlanTemplateOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetBackupPlan")
    def get_backup_plan(
        self,
        context: RequestContext,
        backup_plan_id: string,
        version_id: string | None = None,
        **kwargs,
    ) -> GetBackupPlanOutput:
        """Returns ``BackupPlan`` details for the specified ``BackupPlanId``. The
        details are the body of a backup plan in JSON format, in addition to
        plan metadata.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param version_id: Unique, randomly generated, Unicode, UTF-8 encoded strings that are at
        most 1,024 bytes long.
        :returns: GetBackupPlanOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetBackupPlanFromJSON")
    def get_backup_plan_from_json(
        self, context: RequestContext, backup_plan_template_json: string, **kwargs
    ) -> GetBackupPlanFromJSONOutput:
        """Returns a valid JSON document specifying a backup plan or an error.

        :param backup_plan_template_json: A customer-supplied backup plan document in JSON format.
        :returns: GetBackupPlanFromJSONOutput
        :raises LimitExceededException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("GetBackupPlanFromTemplate")
    def get_backup_plan_from_template(
        self, context: RequestContext, backup_plan_template_id: string, **kwargs
    ) -> GetBackupPlanFromTemplateOutput:
        """Returns the template specified by its ``templateId`` as a backup plan.

        :param backup_plan_template_id: Uniquely identifies a stored backup plan template.
        :returns: GetBackupPlanFromTemplateOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetBackupSelection")
    def get_backup_selection(
        self, context: RequestContext, backup_plan_id: string, selection_id: string, **kwargs
    ) -> GetBackupSelectionOutput:
        """Returns selection metadata and a document in JSON format that specifies
        a list of resources that are associated with a backup plan.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param selection_id: Uniquely identifies the body of a request to assign a set of resources
        to a backup plan.
        :returns: GetBackupSelectionOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetBackupVaultAccessPolicy")
    def get_backup_vault_access_policy(
        self, context: RequestContext, backup_vault_name: BackupVaultName, **kwargs
    ) -> GetBackupVaultAccessPolicyOutput:
        """Returns the access policy document that is associated with the named
        backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :returns: GetBackupVaultAccessPolicyOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetBackupVaultNotifications")
    def get_backup_vault_notifications(
        self, context: RequestContext, backup_vault_name: BackupVaultName, **kwargs
    ) -> GetBackupVaultNotificationsOutput:
        """Returns event notifications for the specified backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :returns: GetBackupVaultNotificationsOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetLegalHold")
    def get_legal_hold(
        self, context: RequestContext, legal_hold_id: string, **kwargs
    ) -> GetLegalHoldOutput:
        """This action returns details for a specified legal hold. The details are
        the body of a legal hold in JSON format, in addition to metadata.

        :param legal_hold_id: The ID of the legal hold.
        :returns: GetLegalHoldOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetRecoveryPointIndexDetails")
    def get_recovery_point_index_details(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        **kwargs,
    ) -> GetRecoveryPointIndexDetailsOutput:
        """This operation returns the metadata and details specific to the backup
        index associated with the specified recovery point.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An ARN that uniquely identifies a recovery point; for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :returns: GetRecoveryPointIndexDetailsOutput
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetRecoveryPointRestoreMetadata")
    def get_recovery_point_restore_metadata(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        backup_vault_account_id: AccountId | None = None,
        **kwargs,
    ) -> GetRecoveryPointRestoreMetadataOutput:
        """Returns a set of metadata key-value pairs that were used to create the
        backup.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point;
        for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :param backup_vault_account_id: The account ID of the specified backup vault.
        :returns: GetRecoveryPointRestoreMetadataOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetRestoreJobMetadata")
    def get_restore_job_metadata(
        self, context: RequestContext, restore_job_id: RestoreJobId, **kwargs
    ) -> GetRestoreJobMetadataOutput:
        """This request returns the metadata for the specified restore job.

        :param restore_job_id: This is a unique identifier of a restore job within Backup.
        :returns: GetRestoreJobMetadataOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetRestoreTestingInferredMetadata")
    def get_restore_testing_inferred_metadata(
        self,
        context: RequestContext,
        backup_vault_name: String,
        recovery_point_arn: String,
        backup_vault_account_id: String | None = None,
        **kwargs,
    ) -> GetRestoreTestingInferredMetadataOutput:
        """This request returns the minimal required set of metadata needed to
        start a restore job with secure default settings. ``BackupVaultName``
        and ``RecoveryPointArn`` are required parameters.
        ``BackupVaultAccountId`` is an optional parameter.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point;
        for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :param backup_vault_account_id: The account ID of the specified backup vault.
        :returns: GetRestoreTestingInferredMetadataOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetRestoreTestingPlan")
    def get_restore_testing_plan(
        self, context: RequestContext, restore_testing_plan_name: String, **kwargs
    ) -> GetRestoreTestingPlanOutput:
        """Returns ``RestoreTestingPlan`` details for the specified
        ``RestoreTestingPlanName``. The details are the body of a restore
        testing plan in JSON format, in addition to plan metadata.

        :param restore_testing_plan_name: Required unique name of the restore testing plan.
        :returns: GetRestoreTestingPlanOutput
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetRestoreTestingSelection")
    def get_restore_testing_selection(
        self,
        context: RequestContext,
        restore_testing_plan_name: String,
        restore_testing_selection_name: String,
        **kwargs,
    ) -> GetRestoreTestingSelectionOutput:
        """Returns RestoreTestingSelection, which displays resources and elements
        of the restore testing plan.

        :param restore_testing_plan_name: Required unique name of the restore testing plan.
        :param restore_testing_selection_name: Required unique name of the restore testing selection.
        :returns: GetRestoreTestingSelectionOutput
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetSupportedResourceTypes")
    def get_supported_resource_types(
        self, context: RequestContext, **kwargs
    ) -> GetSupportedResourceTypesOutput:
        """Returns the Amazon Web Services resource types supported by Backup.

        :returns: GetSupportedResourceTypesOutput
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListBackupJobSummaries")
    def list_backup_job_summaries(
        self,
        context: RequestContext,
        account_id: AccountId | None = None,
        state: BackupJobStatus | None = None,
        resource_type: ResourceType | None = None,
        message_category: MessageCategory | None = None,
        aggregation_period: AggregationPeriod | None = None,
        max_results: MaxResults | None = None,
        next_token: string | None = None,
        **kwargs,
    ) -> ListBackupJobSummariesOutput:
        """This is a request for a summary of backup jobs created or running within
        the most recent 30 days. You can include parameters AccountID, State,
        ResourceType, MessageCategory, AggregationPeriod, MaxResults, or
        NextToken to filter results.

        This request returns a summary that contains Region, Account, State,
        ResourceType, MessageCategory, StartTime, EndTime, and Count of included
        jobs.

        :param account_id: Returns the job count for the specified account.
        :param state: This parameter returns the job count for jobs with the specified state.
        :param resource_type: Returns the job count for the specified resource type.
        :param message_category: This parameter returns the job count for the specified message category.
        :param aggregation_period: The period for the returned results.
        :param max_results: The maximum number of items to be returned.
        :param next_token: The next item following a partial list of returned resources.
        :returns: ListBackupJobSummariesOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListBackupJobs")
    def list_backup_jobs(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        by_resource_arn: ARN | None = None,
        by_state: BackupJobState | None = None,
        by_backup_vault_name: BackupVaultName | None = None,
        by_created_before: timestamp | None = None,
        by_created_after: timestamp | None = None,
        by_resource_type: ResourceType | None = None,
        by_account_id: AccountId | None = None,
        by_complete_after: timestamp | None = None,
        by_complete_before: timestamp | None = None,
        by_parent_job_id: string | None = None,
        by_message_category: string | None = None,
        **kwargs,
    ) -> ListBackupJobsOutput:
        """Returns a list of existing backup jobs for an authenticated account for
        the last 30 days. For a longer period of time, consider using these
        `monitoring
        tools <https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html>`__.

        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :param by_resource_arn: Returns only backup jobs that match the specified resource Amazon
        Resource Name (ARN).
        :param by_state: Returns only backup jobs that are in the specified state.
        :param by_backup_vault_name: Returns only backup jobs that will be stored in the specified backup
        vault.
        :param by_created_before: Returns only backup jobs that were created before the specified date.
        :param by_created_after: Returns only backup jobs that were created after the specified date.
        :param by_resource_type: Returns only backup jobs for the specified resources:

        -  ``Aurora`` for Amazon Aurora

        -  ``CloudFormation`` for CloudFormation

        -  ``DocumentDB`` for Amazon DocumentDB (with MongoDB compatibility)

        -  ``DynamoDB`` for Amazon DynamoDB

        -  ``EBS`` for Amazon Elastic Block Store

        -  ``EC2`` for Amazon Elastic Compute Cloud

        -  ``EFS`` for Amazon Elastic File System

        -  ``FSx`` for Amazon FSx

        -  ``Neptune`` for Amazon Neptune

        -  ``RDS`` for Amazon Relational Database Service

        -  ``Redshift`` for Amazon Redshift

        -  ``S3`` for Amazon Simple Storage Service (Amazon S3)

        -  ``SAP HANA on Amazon EC2`` for SAP HANA databases on Amazon Elastic
           Compute Cloud instances

        -  ``Storage Gateway`` for Storage Gateway

        -  ``Timestream`` for Amazon Timestream

        -  ``VirtualMachine`` for VMware virtual machines.
        :param by_account_id: The account ID to list the jobs from.
        :param by_complete_after: Returns only backup jobs completed after a date expressed in Unix format
        and Coordinated Universal Time (UTC).
        :param by_complete_before: Returns only backup jobs completed before a date expressed in Unix
        format and Coordinated Universal Time (UTC).
        :param by_parent_job_id: This is a filter to list child (nested) jobs based on parent job ID.
        :param by_message_category: This is an optional parameter that can be used to filter out jobs with a
        MessageCategory which matches the value you input.
        :returns: ListBackupJobsOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListBackupPlanTemplates")
    def list_backup_plan_templates(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListBackupPlanTemplatesOutput:
        """Lists the backup plan templates.

        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to return.
        :returns: ListBackupPlanTemplatesOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListBackupPlanVersions")
    def list_backup_plan_versions(
        self,
        context: RequestContext,
        backup_plan_id: string,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListBackupPlanVersionsOutput:
        """Returns version metadata of your backup plans, including Amazon Resource
        Names (ARNs), backup plan IDs, creation and deletion dates, plan names,
        and version IDs.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListBackupPlanVersionsOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListBackupPlans")
    def list_backup_plans(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        include_deleted: Boolean | None = None,
        **kwargs,
    ) -> ListBackupPlansOutput:
        """Lists the active backup plans for the account.

        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :param include_deleted: A Boolean value with a default value of ``FALSE`` that returns deleted
        backup plans when set to ``TRUE``.
        :returns: ListBackupPlansOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListBackupSelections")
    def list_backup_selections(
        self,
        context: RequestContext,
        backup_plan_id: string,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListBackupSelectionsOutput:
        """Returns an array containing metadata of the resources associated with
        the target backup plan.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListBackupSelectionsOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListBackupVaults")
    def list_backup_vaults(
        self,
        context: RequestContext,
        by_vault_type: VaultType | None = None,
        by_shared: boolean | None = None,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListBackupVaultsOutput:
        """Returns a list of recovery point storage containers along with
        information about them.

        :param by_vault_type: This parameter will sort the list of vaults by vault type.
        :param by_shared: This parameter will sort the list of vaults by shared vaults.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListBackupVaultsOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListCopyJobSummaries")
    def list_copy_job_summaries(
        self,
        context: RequestContext,
        account_id: AccountId | None = None,
        state: CopyJobStatus | None = None,
        resource_type: ResourceType | None = None,
        message_category: MessageCategory | None = None,
        aggregation_period: AggregationPeriod | None = None,
        max_results: MaxResults | None = None,
        next_token: string | None = None,
        **kwargs,
    ) -> ListCopyJobSummariesOutput:
        """This request obtains a list of copy jobs created or running within the
        the most recent 30 days. You can include parameters AccountID, State,
        ResourceType, MessageCategory, AggregationPeriod, MaxResults, or
        NextToken to filter results.

        This request returns a summary that contains Region, Account, State,
        RestourceType, MessageCategory, StartTime, EndTime, and Count of
        included jobs.

        :param account_id: Returns the job count for the specified account.
        :param state: This parameter returns the job count for jobs with the specified state.
        :param resource_type: Returns the job count for the specified resource type.
        :param message_category: This parameter returns the job count for the specified message category.
        :param aggregation_period: The period for the returned results.
        :param max_results: This parameter sets the maximum number of items to be returned.
        :param next_token: The next item following a partial list of returned resources.
        :returns: ListCopyJobSummariesOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListCopyJobs")
    def list_copy_jobs(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        by_resource_arn: ARN | None = None,
        by_state: CopyJobState | None = None,
        by_created_before: timestamp | None = None,
        by_created_after: timestamp | None = None,
        by_resource_type: ResourceType | None = None,
        by_destination_vault_arn: string | None = None,
        by_account_id: AccountId | None = None,
        by_complete_before: timestamp | None = None,
        by_complete_after: timestamp | None = None,
        by_parent_job_id: string | None = None,
        by_message_category: string | None = None,
        **kwargs,
    ) -> ListCopyJobsOutput:
        """Returns metadata about your copy jobs.

        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :param by_resource_arn: Returns only copy jobs that match the specified resource Amazon Resource
        Name (ARN).
        :param by_state: Returns only copy jobs that are in the specified state.
        :param by_created_before: Returns only copy jobs that were created before the specified date.
        :param by_created_after: Returns only copy jobs that were created after the specified date.
        :param by_resource_type: Returns only backup jobs for the specified resources:

        -  ``Aurora`` for Amazon Aurora

        -  ``CloudFormation`` for CloudFormation

        -  ``DocumentDB`` for Amazon DocumentDB (with MongoDB compatibility)

        -  ``DynamoDB`` for Amazon DynamoDB

        -  ``EBS`` for Amazon Elastic Block Store

        -  ``EC2`` for Amazon Elastic Compute Cloud

        -  ``EFS`` for Amazon Elastic File System

        -  ``FSx`` for Amazon FSx

        -  ``Neptune`` for Amazon Neptune

        -  ``RDS`` for Amazon Relational Database Service

        -  ``Redshift`` for Amazon Redshift

        -  ``S3`` for Amazon Simple Storage Service (Amazon S3)

        -  ``SAP HANA on Amazon EC2`` for SAP HANA databases on Amazon Elastic
           Compute Cloud instances

        -  ``Storage Gateway`` for Storage Gateway

        -  ``Timestream`` for Amazon Timestream

        -  ``VirtualMachine`` for VMware virtual machines.
        :param by_destination_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies a source backup
        vault to copy from; for example,
        ``arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault``.
        :param by_account_id: The account ID to list the jobs from.
        :param by_complete_before: Returns only copy jobs completed before a date expressed in Unix format
        and Coordinated Universal Time (UTC).
        :param by_complete_after: Returns only copy jobs completed after a date expressed in Unix format
        and Coordinated Universal Time (UTC).
        :param by_parent_job_id: This is a filter to list child (nested) jobs based on parent job ID.
        :param by_message_category: This is an optional parameter that can be used to filter out jobs with a
        MessageCategory which matches the value you input.
        :returns: ListCopyJobsOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListFrameworks")
    def list_frameworks(
        self,
        context: RequestContext,
        max_results: MaxFrameworkInputs | None = None,
        next_token: string | None = None,
        **kwargs,
    ) -> ListFrameworksOutput:
        """Returns a list of all frameworks for an Amazon Web Services account and
        Amazon Web Services Region.

        :param max_results: The number of desired results from 1 to 1000.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which can be used to return the next set of items in the
        list.
        :returns: ListFrameworksOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListIndexedRecoveryPoints")
    def list_indexed_recovery_points(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        source_resource_arn: ARN | None = None,
        created_before: timestamp | None = None,
        created_after: timestamp | None = None,
        resource_type: ResourceType | None = None,
        index_status: IndexStatus | None = None,
        **kwargs,
    ) -> ListIndexedRecoveryPointsOutput:
        """This operation returns a list of recovery points that have an associated
        index, belonging to the specified account.

        Optional parameters you can include are: MaxResults; NextToken;
        SourceResourceArns; CreatedBefore; CreatedAfter; and ResourceType.

        :param next_token: The next item following a partial list of returned recovery points.
        :param max_results: The maximum number of resource list items to be returned.
        :param source_resource_arn: A string of the Amazon Resource Name (ARN) that uniquely identifies the
        source resource.
        :param created_before: Returns only indexed recovery points that were created before the
        specified date.
        :param created_after: Returns only indexed recovery points that were created after the
        specified date.
        :param resource_type: Returns a list of indexed recovery points for the specified resource
        type(s).
        :param index_status: Include this parameter to filter the returned list by the indicated
        statuses.
        :returns: ListIndexedRecoveryPointsOutput
        :raises InvalidParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListLegalHolds")
    def list_legal_holds(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListLegalHoldsOutput:
        """This action returns metadata about active and previous legal holds.

        :param next_token: The next item following a partial list of returned resources.
        :param max_results: The maximum number of resource list items to be returned.
        :returns: ListLegalHoldsOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListProtectedResources")
    def list_protected_resources(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListProtectedResourcesOutput:
        """Returns an array of resources successfully backed up by Backup,
        including the time the resource was saved, an Amazon Resource Name (ARN)
        of the resource, and a resource type.

        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListProtectedResourcesOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListProtectedResourcesByBackupVault")
    def list_protected_resources_by_backup_vault(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        backup_vault_account_id: AccountId | None = None,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListProtectedResourcesByBackupVaultOutput:
        """This request lists the protected resources corresponding to each backup
        vault.

        :param backup_vault_name: The list of protected resources by backup vault within the vault(s) you
        specify by name.
        :param backup_vault_account_id: The list of protected resources by backup vault within the vault(s) you
        specify by account ID.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListProtectedResourcesByBackupVaultOutput
        :raises InvalidParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRecoveryPointsByBackupVault")
    def list_recovery_points_by_backup_vault(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        backup_vault_account_id: AccountId | None = None,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        by_resource_arn: ARN | None = None,
        by_resource_type: ResourceType | None = None,
        by_backup_plan_id: string | None = None,
        by_created_before: timestamp | None = None,
        by_created_after: timestamp | None = None,
        by_parent_recovery_point_arn: ARN | None = None,
        **kwargs,
    ) -> ListRecoveryPointsByBackupVaultOutput:
        """Returns detailed information about the recovery points stored in a
        backup vault.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param backup_vault_account_id: This parameter will sort the list of recovery points by account ID.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :param by_resource_arn: Returns only recovery points that match the specified resource Amazon
        Resource Name (ARN).
        :param by_resource_type: Returns only recovery points that match the specified resource type(s):

        -  ``Aurora`` for Amazon Aurora

        -  ``CloudFormation`` for CloudFormation

        -  ``DocumentDB`` for Amazon DocumentDB (with MongoDB compatibility)

        -  ``DynamoDB`` for Amazon DynamoDB

        -  ``EBS`` for Amazon Elastic Block Store

        -  ``EC2`` for Amazon Elastic Compute Cloud

        -  ``EFS`` for Amazon Elastic File System

        -  ``FSx`` for Amazon FSx

        -  ``Neptune`` for Amazon Neptune

        -  ``RDS`` for Amazon Relational Database Service

        -  ``Redshift`` for Amazon Redshift

        -  ``S3`` for Amazon Simple Storage Service (Amazon S3)

        -  ``SAP HANA on Amazon EC2`` for SAP HANA databases on Amazon Elastic
           Compute Cloud instances

        -  ``Storage Gateway`` for Storage Gateway

        -  ``Timestream`` for Amazon Timestream

        -  ``VirtualMachine`` for VMware virtual machines.
        :param by_backup_plan_id: Returns only recovery points that match the specified backup plan ID.
        :param by_created_before: Returns only recovery points that were created before the specified
        timestamp.
        :param by_created_after: Returns only recovery points that were created after the specified
        timestamp.
        :param by_parent_recovery_point_arn: This returns only recovery points that match the specified parent
        (composite) recovery point Amazon Resource Name (ARN).
        :returns: ListRecoveryPointsByBackupVaultOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRecoveryPointsByLegalHold")
    def list_recovery_points_by_legal_hold(
        self,
        context: RequestContext,
        legal_hold_id: string,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListRecoveryPointsByLegalHoldOutput:
        """This action returns recovery point ARNs (Amazon Resource Names) of the
        specified legal hold.

        :param legal_hold_id: The ID of the legal hold.
        :param next_token: The next item following a partial list of returned resources.
        :param max_results: The maximum number of resource list items to be returned.
        :returns: ListRecoveryPointsByLegalHoldOutput
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRecoveryPointsByResource")
    def list_recovery_points_by_resource(
        self,
        context: RequestContext,
        resource_arn: ARN,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        managed_by_aws_backup_only: boolean | None = None,
        **kwargs,
    ) -> ListRecoveryPointsByResourceOutput:
        """The information about the recovery points of the type specified by a
        resource Amazon Resource Name (ARN).

        For Amazon EFS and Amazon EC2, this action only lists recovery points
        created by Backup.

        :param resource_arn: An ARN that uniquely identifies a resource.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :param managed_by_aws_backup_only: This attribute filters recovery points based on ownership.
        :returns: ListRecoveryPointsByResourceOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListReportJobs")
    def list_report_jobs(
        self,
        context: RequestContext,
        by_report_plan_name: ReportPlanName | None = None,
        by_creation_before: timestamp | None = None,
        by_creation_after: timestamp | None = None,
        by_status: string | None = None,
        max_results: MaxResults | None = None,
        next_token: string | None = None,
        **kwargs,
    ) -> ListReportJobsOutput:
        """Returns details about your report jobs.

        :param by_report_plan_name: Returns only report jobs with the specified report plan name.
        :param by_creation_before: Returns only report jobs that were created before the date and time
        specified in Unix format and Coordinated Universal Time (UTC).
        :param by_creation_after: Returns only report jobs that were created after the date and time
        specified in Unix format and Coordinated Universal Time (UTC).
        :param by_status: Returns only report jobs that are in the specified status.
        :param max_results: The number of desired results from 1 to 1000.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which can be used to return the next set of items in the
        list.
        :returns: ListReportJobsOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListReportPlans")
    def list_report_plans(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: string | None = None,
        **kwargs,
    ) -> ListReportPlansOutput:
        """Returns a list of your report plans. For detailed information about a
        single report plan, use ``DescribeReportPlan``.

        :param max_results: The number of desired results from 1 to 1000.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which can be used to return the next set of items in the
        list.
        :returns: ListReportPlansOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRestoreJobSummaries")
    def list_restore_job_summaries(
        self,
        context: RequestContext,
        account_id: AccountId | None = None,
        state: RestoreJobState | None = None,
        resource_type: ResourceType | None = None,
        aggregation_period: AggregationPeriod | None = None,
        max_results: MaxResults | None = None,
        next_token: string | None = None,
        **kwargs,
    ) -> ListRestoreJobSummariesOutput:
        """This request obtains a summary of restore jobs created or running within
        the the most recent 30 days. You can include parameters AccountID,
        State, ResourceType, AggregationPeriod, MaxResults, or NextToken to
        filter results.

        This request returns a summary that contains Region, Account, State,
        RestourceType, MessageCategory, StartTime, EndTime, and Count of
        included jobs.

        :param account_id: Returns the job count for the specified account.
        :param state: This parameter returns the job count for jobs with the specified state.
        :param resource_type: Returns the job count for the specified resource type.
        :param aggregation_period: The period for the returned results.
        :param max_results: This parameter sets the maximum number of items to be returned.
        :param next_token: The next item following a partial list of returned resources.
        :returns: ListRestoreJobSummariesOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRestoreJobs")
    def list_restore_jobs(
        self,
        context: RequestContext,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        by_account_id: AccountId | None = None,
        by_resource_type: ResourceType | None = None,
        by_created_before: timestamp | None = None,
        by_created_after: timestamp | None = None,
        by_status: RestoreJobStatus | None = None,
        by_complete_before: timestamp | None = None,
        by_complete_after: timestamp | None = None,
        by_restore_testing_plan_arn: ARN | None = None,
        **kwargs,
    ) -> ListRestoreJobsOutput:
        """Returns a list of jobs that Backup initiated to restore a saved
        resource, including details about the recovery process.

        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :param by_account_id: The account ID to list the jobs from.
        :param by_resource_type: Include this parameter to return only restore jobs for the specified
        resources:

        -  ``Aurora`` for Amazon Aurora

        -  ``CloudFormation`` for CloudFormation

        -  ``DocumentDB`` for Amazon DocumentDB (with MongoDB compatibility)

        -  ``DynamoDB`` for Amazon DynamoDB

        -  ``EBS`` for Amazon Elastic Block Store

        -  ``EC2`` for Amazon Elastic Compute Cloud

        -  ``EFS`` for Amazon Elastic File System

        -  ``FSx`` for Amazon FSx

        -  ``Neptune`` for Amazon Neptune

        -  ``RDS`` for Amazon Relational Database Service

        -  ``Redshift`` for Amazon Redshift

        -  ``S3`` for Amazon Simple Storage Service (Amazon S3)

        -  ``SAP HANA on Amazon EC2`` for SAP HANA databases on Amazon Elastic
           Compute Cloud instances

        -  ``Storage Gateway`` for Storage Gateway

        -  ``Timestream`` for Amazon Timestream

        -  ``VirtualMachine`` for VMware virtual machines.
        :param by_created_before: Returns only restore jobs that were created before the specified date.
        :param by_created_after: Returns only restore jobs that were created after the specified date.
        :param by_status: Returns only restore jobs associated with the specified job status.
        :param by_complete_before: Returns only copy jobs completed before a date expressed in Unix format
        and Coordinated Universal Time (UTC).
        :param by_complete_after: Returns only copy jobs completed after a date expressed in Unix format
        and Coordinated Universal Time (UTC).
        :param by_restore_testing_plan_arn: This returns only restore testing jobs that match the specified resource
        Amazon Resource Name (ARN).
        :returns: ListRestoreJobsOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRestoreJobsByProtectedResource")
    def list_restore_jobs_by_protected_resource(
        self,
        context: RequestContext,
        resource_arn: ARN,
        by_status: RestoreJobStatus | None = None,
        by_recovery_point_creation_date_after: timestamp | None = None,
        by_recovery_point_creation_date_before: timestamp | None = None,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListRestoreJobsByProtectedResourceOutput:
        """This returns restore jobs that contain the specified protected resource.

        You must include ``ResourceArn``. You can optionally include
        ``NextToken``, ``ByStatus``, ``MaxResults``,
        ``ByRecoveryPointCreationDateAfter`` , and
        ``ByRecoveryPointCreationDateBefore``.

        :param resource_arn: Returns only restore jobs that match the specified resource Amazon
        Resource Name (ARN).
        :param by_status: Returns only restore jobs associated with the specified job status.
        :param by_recovery_point_creation_date_after: Returns only restore jobs of recovery points that were created after the
        specified date.
        :param by_recovery_point_creation_date_before: Returns only restore jobs of recovery points that were created before
        the specified date.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListRestoreJobsByProtectedResourceOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRestoreTestingPlans")
    def list_restore_testing_plans(
        self,
        context: RequestContext,
        max_results: ListRestoreTestingPlansInputMaxResultsInteger | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListRestoreTestingPlansOutput:
        """Returns a list of restore testing plans.

        :param max_results: The maximum number of items to be returned.
        :param next_token: The next item following a partial list of returned items.
        :returns: ListRestoreTestingPlansOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListRestoreTestingSelections")
    def list_restore_testing_selections(
        self,
        context: RequestContext,
        restore_testing_plan_name: String,
        max_results: ListRestoreTestingSelectionsInputMaxResultsInteger | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListRestoreTestingSelectionsOutput:
        """Returns a list of restore testing selections. Can be filtered by
        ``MaxResults`` and ``RestoreTestingPlanName``.

        :param restore_testing_plan_name: Returns restore testing selections by the specified restore testing plan
        name.
        :param max_results: The maximum number of items to be returned.
        :param next_token: The next item following a partial list of returned items.
        :returns: ListRestoreTestingSelectionsOutput
        :raises InvalidParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListTags")
    def list_tags(
        self,
        context: RequestContext,
        resource_arn: ARN,
        next_token: string | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListTagsOutput:
        """Returns the tags assigned to the resource, such as a target recovery
        point, backup plan, or backup vault.

        :param resource_arn: An Amazon Resource Name (ARN) that uniquely identifies a resource.
        :param next_token: The next item following a partial list of returned items.
        :param max_results: The maximum number of items to be returned.
        :returns: ListTagsOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("PutBackupVaultAccessPolicy")
    def put_backup_vault_access_policy(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        policy: IAMPolicy | None = None,
        **kwargs,
    ) -> None:
        """Sets a resource-based policy that is used to manage access permissions
        on the target backup vault. Requires a backup vault name and an access
        policy document in JSON format.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param policy: The backup vault access policy document in JSON format.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("PutBackupVaultLockConfiguration")
    def put_backup_vault_lock_configuration(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        min_retention_days: Long | None = None,
        max_retention_days: Long | None = None,
        changeable_for_days: Long | None = None,
        **kwargs,
    ) -> None:
        """Applies Backup Vault Lock to a backup vault, preventing attempts to
        delete any recovery point stored in or created in a backup vault. Vault
        Lock also prevents attempts to update the lifecycle policy that controls
        the retention period of any recovery point currently stored in a backup
        vault. If specified, Vault Lock enforces a minimum and maximum retention
        period for future backup and copy jobs that target a backup vault.

        Backup Vault Lock has been assessed by Cohasset Associates for use in
        environments that are subject to SEC 17a-4, CFTC, and FINRA regulations.
        For more information about how Backup Vault Lock relates to these
        regulations, see the `Cohasset Associates Compliance
        Assessment. <https://docs.aws.amazon.com/aws-backup/latest/devguide/samples/cohassetreport.zip>`__

        For more information, see `Backup Vault
        Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`__.

        :param backup_vault_name: The Backup Vault Lock configuration that specifies the name of the
        backup vault it protects.
        :param min_retention_days: The Backup Vault Lock configuration that specifies the minimum retention
        period that the vault retains its recovery points.
        :param max_retention_days: The Backup Vault Lock configuration that specifies the maximum retention
        period that the vault retains its recovery points.
        :param changeable_for_days: The Backup Vault Lock configuration that specifies the number of days
        before the lock date.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises InvalidRequestException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("PutBackupVaultNotifications")
    def put_backup_vault_notifications(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        sns_topic_arn: ARN,
        backup_vault_events: BackupVaultEvents,
        **kwargs,
    ) -> None:
        """Turns on notifications on a backup vault for the specified topic and
        events.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param sns_topic_arn: The Amazon Resource Name (ARN) that specifies the topic for a backup
        vault’s events; for example,
        ``arn:aws:sns:us-west-2:111122223333:MyVaultTopic``.
        :param backup_vault_events: An array of events that indicate the status of jobs to back up resources
        to the backup vault.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("PutRestoreValidationResult")
    def put_restore_validation_result(
        self,
        context: RequestContext,
        restore_job_id: RestoreJobId,
        validation_status: RestoreValidationStatus,
        validation_status_message: string | None = None,
        **kwargs,
    ) -> None:
        """This request allows you to send your independent self-run restore test
        validation results. ``RestoreJobId`` and ``ValidationStatus`` are
        required. Optionally, you can input a ``ValidationStatusMessage``.

        :param restore_job_id: This is a unique identifier of a restore job within Backup.
        :param validation_status: The status of your restore validation.
        :param validation_status_message: This is an optional message string you can input to describe the
        validation status for the restore test validation.
        :raises InvalidParameterValueException:
        :raises InvalidRequestException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("StartBackupJob")
    def start_backup_job(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        resource_arn: ARN,
        iam_role_arn: IAMRoleArn,
        idempotency_token: string | None = None,
        start_window_minutes: WindowMinutes | None = None,
        complete_window_minutes: WindowMinutes | None = None,
        lifecycle: Lifecycle | None = None,
        recovery_point_tags: Tags | None = None,
        backup_options: BackupOptions | None = None,
        index: Index | None = None,
        **kwargs,
    ) -> StartBackupJobOutput:
        """Starts an on-demand backup job for the specified resource.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param resource_arn: An Amazon Resource Name (ARN) that uniquely identifies a resource.
        :param iam_role_arn: Specifies the IAM role ARN used to create the target recovery point; for
        example, ``arn:aws:iam::123456789012:role/S3Access``.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``StartBackupJob``.
        :param start_window_minutes: A value in minutes after a backup is scheduled before a job will be
        canceled if it doesn't start successfully.
        :param complete_window_minutes: A value in minutes during which a successfully started backup must
        complete, or else Backup will cancel the job.
        :param lifecycle: The lifecycle defines when a protected resource is transitioned to cold
        storage and when it expires.
        :param recovery_point_tags: The tags to assign to the resources.
        :param backup_options: The backup option for a selected resource.
        :param index: Include this parameter to enable index creation if your backup job has a
        resource type that supports backup indexes.
        :returns: StartBackupJobOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises InvalidRequestException:
        :raises ServiceUnavailableException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("StartCopyJob")
    def start_copy_job(
        self,
        context: RequestContext,
        recovery_point_arn: ARN,
        source_backup_vault_name: BackupVaultName,
        destination_backup_vault_arn: ARN,
        iam_role_arn: IAMRoleArn,
        idempotency_token: string | None = None,
        lifecycle: Lifecycle | None = None,
        **kwargs,
    ) -> StartCopyJobOutput:
        """Starts a job to create a one-time copy of the specified resource.

        Does not support continuous backups.

        :param recovery_point_arn: An ARN that uniquely identifies a recovery point to use for the copy
        job; for example,
        arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.
        :param source_backup_vault_name: The name of a logical source container where backups are stored.
        :param destination_backup_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies a destination
        backup vault to copy to; for example,
        ``arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault``.
        :param iam_role_arn: Specifies the IAM role ARN used to copy the target recovery point; for
        example, ``arn:aws:iam::123456789012:role/S3Access``.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``StartCopyJob``.
        :param lifecycle: Specifies the time period, in days, before a recovery point transitions
        to cold storage or is deleted.
        :returns: StartCopyJobOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises LimitExceededException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("StartReportJob")
    def start_report_job(
        self,
        context: RequestContext,
        report_plan_name: ReportPlanName,
        idempotency_token: string | None = None,
        **kwargs,
    ) -> StartReportJobOutput:
        """Starts an on-demand report job for the specified report plan.

        :param report_plan_name: The unique name of a report plan.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``StartReportJobInput``.
        :returns: StartReportJobOutput
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("StartRestoreJob")
    def start_restore_job(
        self,
        context: RequestContext,
        recovery_point_arn: ARN,
        metadata: Metadata,
        iam_role_arn: IAMRoleArn | None = None,
        idempotency_token: string | None = None,
        resource_type: ResourceType | None = None,
        copy_source_tags_to_restored_resource: boolean | None = None,
        **kwargs,
    ) -> StartRestoreJobOutput:
        """Recovers the saved resource identified by an Amazon Resource Name (ARN).

        :param recovery_point_arn: An ARN that uniquely identifies a recovery point; for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :param metadata: A set of metadata key-value pairs.
        :param iam_role_arn: The Amazon Resource Name (ARN) of the IAM role that Backup uses to
        create the target resource; for example:
        ``arn:aws:iam::123456789012:role/S3Access``.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``StartRestoreJob``.
        :param resource_type: Starts a job to restore a recovery point for one of the following
        resources:

        -  ``Aurora`` - Amazon Aurora

        -  ``DocumentDB`` - Amazon DocumentDB

        -  ``CloudFormation`` - CloudFormation

        -  ``DynamoDB`` - Amazon DynamoDB

        -  ``EBS`` - Amazon Elastic Block Store

        -  ``EC2`` - Amazon Elastic Compute Cloud

        -  ``EFS`` - Amazon Elastic File System

        -  ``FSx`` - Amazon FSx

        -  ``Neptune`` - Amazon Neptune

        -  ``RDS`` - Amazon Relational Database Service

        -  ``Redshift`` - Amazon Redshift

        -  ``Storage Gateway`` - Storage Gateway

        -  ``S3`` - Amazon Simple Storage Service

        -  ``Timestream`` - Amazon Timestream

        -  ``VirtualMachine`` - Virtual machines.
        :param copy_source_tags_to_restored_resource: This is an optional parameter.
        :returns: StartRestoreJobOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("StopBackupJob")
    def stop_backup_job(self, context: RequestContext, backup_job_id: string, **kwargs) -> None:
        """Attempts to cancel a job to create a one-time backup of a resource.

        This action is not supported for the following services: Amazon FSx for
        Windows File Server, Amazon FSx for Lustre, Amazon FSx for NetApp ONTAP,
        Amazon FSx for OpenZFS, Amazon DocumentDB (with MongoDB compatibility),
        Amazon RDS, Amazon Aurora, and Amazon Neptune.

        :param backup_job_id: Uniquely identifies a request to Backup to back up a resource.
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises InvalidRequestException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ARN, tags: Tags, **kwargs
    ) -> None:
        """Assigns a set of key-value pairs to a recovery point, backup plan, or
        backup vault identified by an Amazon Resource Name (ARN).

        This API is supported for recovery points for resource types including
        Aurora, Amazon DocumentDB. Amazon EBS, Amazon FSx, Neptune, and Amazon
        RDS.

        :param resource_arn: An ARN that uniquely identifies a resource.
        :param tags: Key-value pairs that are used to help organize your resources.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ARN, tag_key_list: TagKeyList, **kwargs
    ) -> None:
        """Removes a set of key-value pairs from a recovery point, backup plan, or
        backup vault identified by an Amazon Resource Name (ARN)

        This API is not supported for recovery points for resource types
        including Aurora, Amazon DocumentDB. Amazon EBS, Amazon FSx, Neptune,
        and Amazon RDS.

        :param resource_arn: An ARN that uniquely identifies a resource.
        :param tag_key_list: The keys to identify which key-value tags to remove from a resource.
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("UpdateBackupPlan")
    def update_backup_plan(
        self,
        context: RequestContext,
        backup_plan_id: string,
        backup_plan: BackupPlanInput,
        **kwargs,
    ) -> UpdateBackupPlanOutput:
        """Updates the specified backup plan. The new version is uniquely
        identified by its ID.

        :param backup_plan_id: The ID of the backup plan.
        :param backup_plan: The body of a backup plan.
        :returns: UpdateBackupPlanOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("UpdateFramework")
    def update_framework(
        self,
        context: RequestContext,
        framework_name: FrameworkName,
        framework_description: FrameworkDescription | None = None,
        framework_controls: FrameworkControls | None = None,
        idempotency_token: string | None = None,
        **kwargs,
    ) -> UpdateFrameworkOutput:
        """Updates the specified framework.

        :param framework_name: The unique name of a framework.
        :param framework_description: An optional description of the framework with a maximum 1,024
        characters.
        :param framework_controls: The controls that make up the framework.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``UpdateFrameworkInput``.
        :returns: UpdateFrameworkOutput
        :raises AlreadyExistsException:
        :raises ResourceNotFoundException:
        :raises LimitExceededException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ConflictException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("UpdateGlobalSettings")
    def update_global_settings(
        self, context: RequestContext, global_settings: GlobalSettings | None = None, **kwargs
    ) -> None:
        """Updates whether the Amazon Web Services account is opted in to
        cross-account backup. Returns an error if the account is not an
        Organizations management account. Use the ``DescribeGlobalSettings`` API
        to determine the current settings.

        :param global_settings: A value for ``isCrossAccountBackupEnabled`` and a Region.
        :raises ServiceUnavailableException:
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("UpdateRecoveryPointIndexSettings")
    def update_recovery_point_index_settings(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        index: Index,
        iam_role_arn: IAMRoleArn | None = None,
        **kwargs,
    ) -> UpdateRecoveryPointIndexSettingsOutput:
        """This operation updates the settings of a recovery point index.

        Required: BackupVaultName, RecoveryPointArn, and IAMRoleArn

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An ARN that uniquely identifies a recovery point; for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :param index: Index can have 1 of 2 possible values, either ``ENABLED`` or
        ``DISABLED``.
        :param iam_role_arn: This specifies the IAM role ARN used for this operation.
        :returns: UpdateRecoveryPointIndexSettingsOutput
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("UpdateRecoveryPointLifecycle")
    def update_recovery_point_lifecycle(
        self,
        context: RequestContext,
        backup_vault_name: BackupVaultName,
        recovery_point_arn: ARN,
        lifecycle: Lifecycle | None = None,
        **kwargs,
    ) -> UpdateRecoveryPointLifecycleOutput:
        """Sets the transition lifecycle of a recovery point.

        The lifecycle defines when a protected resource is transitioned to cold
        storage and when it expires. Backup transitions and expires backups
        automatically according to the lifecycle that you define.

        Resource types that can transition to cold storage are listed in the
        `Feature availability by
        resource <https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource>`__
        table. Backup ignores this expression for other resource types.

        Backups transitioned to cold storage must be stored in cold storage for
        a minimum of 90 days. Therefore, the “retention” setting must be 90 days
        greater than the “transition to cold after days” setting. The
        “transition to cold after days” setting cannot be changed after a backup
        has been transitioned to cold.

        If your lifecycle currently uses the parameters ``DeleteAfterDays`` and
        ``MoveToColdStorageAfterDays``, include these parameters and their
        values when you call this operation. Not including them may result in
        your plan updating with null values.

        This operation does not support continuous backups.

        :param backup_vault_name: The name of a logical container where backups are stored.
        :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point;
        for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``.
        :param lifecycle: The lifecycle defines when a protected resource is transitioned to cold
        storage and when it expires.
        :returns: UpdateRecoveryPointLifecycleOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises InvalidRequestException:
        :raises MissingParameterValueException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("UpdateRegionSettings")
    def update_region_settings(
        self,
        context: RequestContext,
        resource_type_opt_in_preference: ResourceTypeOptInPreference | None = None,
        resource_type_management_preference: ResourceTypeManagementPreference | None = None,
        **kwargs,
    ) -> None:
        """Updates the current service opt-in settings for the Region.

        Use the ``DescribeRegionSettings`` API to determine the resource types
        that are supported.

        :param resource_type_opt_in_preference: Updates the list of services along with the opt-in preferences for the
        Region.
        :param resource_type_management_preference: Enables or disables full Backup management of backups for a resource
        type.
        :raises ServiceUnavailableException:
        :raises MissingParameterValueException:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("UpdateReportPlan")
    def update_report_plan(
        self,
        context: RequestContext,
        report_plan_name: ReportPlanName,
        report_plan_description: ReportPlanDescription | None = None,
        report_delivery_channel: ReportDeliveryChannel | None = None,
        report_setting: ReportSetting | None = None,
        idempotency_token: string | None = None,
        **kwargs,
    ) -> UpdateReportPlanOutput:
        """Updates the specified report plan.

        :param report_plan_name: The unique name of the report plan.
        :param report_plan_description: An optional description of the report plan with a maximum 1,024
        characters.
        :param report_delivery_channel: The information about where to deliver your reports, specifically your
        Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param report_setting: The report template for the report.
        :param idempotency_token: A customer-chosen string that you can use to distinguish between
        otherwise identical calls to ``UpdateReportPlanInput``.
        :returns: UpdateReportPlanOutput
        :raises ResourceNotFoundException:
        :raises InvalidParameterValueException:
        :raises ServiceUnavailableException:
        :raises MissingParameterValueException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateRestoreTestingPlan")
    def update_restore_testing_plan(
        self,
        context: RequestContext,
        restore_testing_plan: RestoreTestingPlanForUpdate,
        restore_testing_plan_name: String,
        **kwargs,
    ) -> UpdateRestoreTestingPlanOutput:
        """This request will send changes to your specified restore testing plan.
        ``RestoreTestingPlanName`` cannot be updated after it is created.

        ``RecoveryPointSelection`` can contain:

        -  ``Algorithm``

        -  ``ExcludeVaults``

        -  ``IncludeVaults``

        -  ``RecoveryPointTypes``

        -  ``SelectionWindowDays``

        :param restore_testing_plan: Specifies the body of a restore testing plan.
        :param restore_testing_plan_name: The name of the restore testing plan name.
        :returns: UpdateRestoreTestingPlanOutput
        :raises ConflictException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("UpdateRestoreTestingSelection")
    def update_restore_testing_selection(
        self,
        context: RequestContext,
        restore_testing_plan_name: String,
        restore_testing_selection: RestoreTestingSelectionForUpdate,
        restore_testing_selection_name: String,
        **kwargs,
    ) -> UpdateRestoreTestingSelectionOutput:
        """Updates the specified restore testing selection.

        Most elements except the ``RestoreTestingSelectionName`` can be updated
        with this request.

        You can use either protected resource ARNs or conditions, but not both.

        :param restore_testing_plan_name: The restore testing plan name is required to update the indicated
        testing plan.
        :param restore_testing_selection: To update your restore testing selection, you can use either protected
        resource ARNs or conditions, but not both.
        :param restore_testing_selection_name: The required restore testing selection name of the restore testing
        selection you wish to update.
        :returns: UpdateRestoreTestingSelectionOutput
        :raises ConflictException:
        :raises InvalidParameterValueException:
        :raises MissingParameterValueException:
        :raises ResourceNotFoundException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError
