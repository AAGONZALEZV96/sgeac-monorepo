from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AdditionalDeploymentStatusInfo = str
AlarmName = str
ApplicationId = str
ApplicationName = str
Arn = str
AutoScalingGroupHook = str
AutoScalingGroupName = str
Boolean = bool
CloudFormationResourceType = str
CommitId = str
DeploymentConfigId = str
DeploymentConfigName = str
DeploymentGroupId = str
DeploymentGroupName = str
DeploymentId = str
Description = str
Duration = int
ECSClusterName = str
ECSServiceName = str
ECSTaskSetIdentifier = str
ECSTaskSetStatus = str
ELBName = str
ETag = str
ErrorMessage = str
ExternalId = str
FilterValue = str
GitHubAccountTokenName = str
IamSessionArn = str
IamUserArn = str
InstanceArn = str
InstanceId = str
InstanceName = str
Key = str
LambdaFunctionAlias = str
LambdaFunctionName = str
LifecycleEventHookExecutionId = str
LifecycleEventName = str
LifecycleMessage = str
ListenerArn = str
LogTail = str
Message = str
MinimumHealthyHostsPerZoneValue = int
MinimumHealthyHostsValue = int
NextToken = str
NullableBoolean = bool
Percentage = int
RawStringContent = str
RawStringSha256 = str
Repository = str
Role = str
S3Bucket = str
S3Key = str
ScriptName = str
TargetArn = str
TargetGroupName = str
TargetId = str
TrafficWeight = float
TriggerName = str
TriggerTargetArn = str
Value = str
Version = str
VersionId = str
WaitTimeInMins = int


class ApplicationRevisionSortBy(StrEnum):
    registerTime = "registerTime"
    firstUsedTime = "firstUsedTime"
    lastUsedTime = "lastUsedTime"


class AutoRollbackEvent(StrEnum):
    DEPLOYMENT_FAILURE = "DEPLOYMENT_FAILURE"
    DEPLOYMENT_STOP_ON_ALARM = "DEPLOYMENT_STOP_ON_ALARM"
    DEPLOYMENT_STOP_ON_REQUEST = "DEPLOYMENT_STOP_ON_REQUEST"


class BundleType(StrEnum):
    tar = "tar"
    tgz = "tgz"
    zip = "zip"
    YAML = "YAML"
    JSON = "JSON"


class ComputePlatform(StrEnum):
    Server = "Server"
    Lambda = "Lambda"
    ECS = "ECS"


class DeploymentCreator(StrEnum):
    user = "user"
    autoscaling = "autoscaling"
    codeDeployRollback = "codeDeployRollback"
    CodeDeploy = "CodeDeploy"
    CodeDeployAutoUpdate = "CodeDeployAutoUpdate"
    CloudFormation = "CloudFormation"
    CloudFormationRollback = "CloudFormationRollback"
    autoscalingTermination = "autoscalingTermination"


class DeploymentOption(StrEnum):
    WITH_TRAFFIC_CONTROL = "WITH_TRAFFIC_CONTROL"
    WITHOUT_TRAFFIC_CONTROL = "WITHOUT_TRAFFIC_CONTROL"


class DeploymentReadyAction(StrEnum):
    CONTINUE_DEPLOYMENT = "CONTINUE_DEPLOYMENT"
    STOP_DEPLOYMENT = "STOP_DEPLOYMENT"


class DeploymentStatus(StrEnum):
    Created = "Created"
    Queued = "Queued"
    InProgress = "InProgress"
    Baking = "Baking"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Stopped = "Stopped"
    Ready = "Ready"


class DeploymentTargetType(StrEnum):
    InstanceTarget = "InstanceTarget"
    LambdaTarget = "LambdaTarget"
    ECSTarget = "ECSTarget"
    CloudFormationTarget = "CloudFormationTarget"


class DeploymentType(StrEnum):
    IN_PLACE = "IN_PLACE"
    BLUE_GREEN = "BLUE_GREEN"


class DeploymentWaitType(StrEnum):
    READY_WAIT = "READY_WAIT"
    TERMINATION_WAIT = "TERMINATION_WAIT"


class EC2TagFilterType(StrEnum):
    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


class ErrorCode(StrEnum):
    AGENT_ISSUE = "AGENT_ISSUE"
    ALARM_ACTIVE = "ALARM_ACTIVE"
    APPLICATION_MISSING = "APPLICATION_MISSING"
    AUTOSCALING_VALIDATION_ERROR = "AUTOSCALING_VALIDATION_ERROR"
    AUTO_SCALING_CONFIGURATION = "AUTO_SCALING_CONFIGURATION"
    AUTO_SCALING_IAM_ROLE_PERMISSIONS = "AUTO_SCALING_IAM_ROLE_PERMISSIONS"
    CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND = "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND"
    CUSTOMER_APPLICATION_UNHEALTHY = "CUSTOMER_APPLICATION_UNHEALTHY"
    DEPLOYMENT_GROUP_MISSING = "DEPLOYMENT_GROUP_MISSING"
    ECS_UPDATE_ERROR = "ECS_UPDATE_ERROR"
    ELASTIC_LOAD_BALANCING_INVALID = "ELASTIC_LOAD_BALANCING_INVALID"
    ELB_INVALID_INSTANCE = "ELB_INVALID_INSTANCE"
    HEALTH_CONSTRAINTS = "HEALTH_CONSTRAINTS"
    HEALTH_CONSTRAINTS_INVALID = "HEALTH_CONSTRAINTS_INVALID"
    HOOK_EXECUTION_FAILURE = "HOOK_EXECUTION_FAILURE"
    IAM_ROLE_MISSING = "IAM_ROLE_MISSING"
    IAM_ROLE_PERMISSIONS = "IAM_ROLE_PERMISSIONS"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_ECS_SERVICE = "INVALID_ECS_SERVICE"
    INVALID_LAMBDA_CONFIGURATION = "INVALID_LAMBDA_CONFIGURATION"
    INVALID_LAMBDA_FUNCTION = "INVALID_LAMBDA_FUNCTION"
    INVALID_REVISION = "INVALID_REVISION"
    MANUAL_STOP = "MANUAL_STOP"
    MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION = "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION"
    MISSING_ELB_INFORMATION = "MISSING_ELB_INFORMATION"
    MISSING_GITHUB_TOKEN = "MISSING_GITHUB_TOKEN"
    NO_EC2_SUBSCRIPTION = "NO_EC2_SUBSCRIPTION"
    NO_INSTANCES = "NO_INSTANCES"
    OVER_MAX_INSTANCES = "OVER_MAX_INSTANCES"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    REVISION_MISSING = "REVISION_MISSING"
    THROTTLED = "THROTTLED"
    TIMEOUT = "TIMEOUT"
    CLOUDFORMATION_STACK_FAILURE = "CLOUDFORMATION_STACK_FAILURE"


class FileExistsBehavior(StrEnum):
    DISALLOW = "DISALLOW"
    OVERWRITE = "OVERWRITE"
    RETAIN = "RETAIN"


class GreenFleetProvisioningAction(StrEnum):
    DISCOVER_EXISTING = "DISCOVER_EXISTING"
    COPY_AUTO_SCALING_GROUP = "COPY_AUTO_SCALING_GROUP"


class InstanceAction(StrEnum):
    TERMINATE = "TERMINATE"
    KEEP_ALIVE = "KEEP_ALIVE"


class InstanceStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"
    Ready = "Ready"


class InstanceType(StrEnum):
    Blue = "Blue"
    Green = "Green"


class LifecycleErrorCode(StrEnum):
    Success = "Success"
    ScriptMissing = "ScriptMissing"
    ScriptNotExecutable = "ScriptNotExecutable"
    ScriptTimedOut = "ScriptTimedOut"
    ScriptFailed = "ScriptFailed"
    UnknownError = "UnknownError"


class LifecycleEventStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"


class ListStateFilterAction(StrEnum):
    include = "include"
    exclude = "exclude"
    ignore = "ignore"


class MinimumHealthyHostsPerZoneType(StrEnum):
    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


class MinimumHealthyHostsType(StrEnum):
    HOST_COUNT = "HOST_COUNT"
    FLEET_PERCENT = "FLEET_PERCENT"


class OutdatedInstancesStrategy(StrEnum):
    UPDATE = "UPDATE"
    IGNORE = "IGNORE"


class RegistrationStatus(StrEnum):
    Registered = "Registered"
    Deregistered = "Deregistered"


class RevisionLocationType(StrEnum):
    S3 = "S3"
    GitHub = "GitHub"
    String = "String"
    AppSpecContent = "AppSpecContent"


class SortOrder(StrEnum):
    ascending = "ascending"
    descending = "descending"


class StopStatus(StrEnum):
    Pending = "Pending"
    Succeeded = "Succeeded"


class TagFilterType(StrEnum):
    KEY_ONLY = "KEY_ONLY"
    VALUE_ONLY = "VALUE_ONLY"
    KEY_AND_VALUE = "KEY_AND_VALUE"


class TargetFilterName(StrEnum):
    TargetStatus = "TargetStatus"
    ServerInstanceLabel = "ServerInstanceLabel"


class TargetLabel(StrEnum):
    Blue = "Blue"
    Green = "Green"


class TargetStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Skipped = "Skipped"
    Unknown = "Unknown"
    Ready = "Ready"


class TrafficRoutingType(StrEnum):
    TimeBasedCanary = "TimeBasedCanary"
    TimeBasedLinear = "TimeBasedLinear"
    AllAtOnce = "AllAtOnce"


class TriggerEventType(StrEnum):
    DeploymentStart = "DeploymentStart"
    DeploymentSuccess = "DeploymentSuccess"
    DeploymentFailure = "DeploymentFailure"
    DeploymentStop = "DeploymentStop"
    DeploymentRollback = "DeploymentRollback"
    DeploymentReady = "DeploymentReady"
    InstanceStart = "InstanceStart"
    InstanceSuccess = "InstanceSuccess"
    InstanceFailure = "InstanceFailure"
    InstanceReady = "InstanceReady"


class AlarmsLimitExceededException(ServiceException):
    """The maximum number of alarms for a deployment group (10) was exceeded."""

    code: str = "AlarmsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationAlreadyExistsException(ServiceException):
    """An application with the specified name with the user or Amazon Web
    Services account already exists.
    """

    code: str = "ApplicationAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationDoesNotExistException(ServiceException):
    """The application does not exist with the user or Amazon Web Services
    account.
    """

    code: str = "ApplicationDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationLimitExceededException(ServiceException):
    """More applications were attempted to be created than are allowed."""

    code: str = "ApplicationLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ApplicationNameRequiredException(ServiceException):
    """The minimum number of required application names was not specified."""

    code: str = "ApplicationNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class ArnNotSupportedException(ServiceException):
    """The specified ARN is not supported. For example, it might be an ARN for
    a resource that is not expected.
    """

    code: str = "ArnNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class BatchLimitExceededException(ServiceException):
    """The maximum number of names or IDs allowed for this request (100) was
    exceeded.
    """

    code: str = "BatchLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class BucketNameFilterRequiredException(ServiceException):
    """A bucket name is required, but was not provided."""

    code: str = "BucketNameFilterRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentAlreadyCompletedException(ServiceException):
    """The deployment is already complete."""

    code: str = "DeploymentAlreadyCompletedException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentAlreadyStartedException(ServiceException):
    """A deployment to a target was attempted while another deployment was in
    progress.
    """

    code: str = "DeploymentAlreadyStartedException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigAlreadyExistsException(ServiceException):
    """A deployment configuration with the specified name with the user or
    Amazon Web Services account already exists.
    """

    code: str = "DeploymentConfigAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigDoesNotExistException(ServiceException):
    """The deployment configuration does not exist with the user or Amazon Web
    Services account.
    """

    code: str = "DeploymentConfigDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigInUseException(ServiceException):
    """The deployment configuration is still in use."""

    code: str = "DeploymentConfigInUseException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigLimitExceededException(ServiceException):
    """The deployment configurations limit was exceeded."""

    code: str = "DeploymentConfigLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentConfigNameRequiredException(ServiceException):
    """The deployment configuration name was not specified."""

    code: str = "DeploymentConfigNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentDoesNotExistException(ServiceException):
    """The deployment with the user or Amazon Web Services account does not
    exist.
    """

    code: str = "DeploymentDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupAlreadyExistsException(ServiceException):
    """A deployment group with the specified name with the user or Amazon Web
    Services account already exists.
    """

    code: str = "DeploymentGroupAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupDoesNotExistException(ServiceException):
    """The named deployment group with the user or Amazon Web Services account
    does not exist.
    """

    code: str = "DeploymentGroupDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupLimitExceededException(ServiceException):
    """The deployment groups limit was exceeded."""

    code: str = "DeploymentGroupLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentGroupNameRequiredException(ServiceException):
    """The deployment group name was not specified."""

    code: str = "DeploymentGroupNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentIdRequiredException(ServiceException):
    """At least one deployment ID must be specified."""

    code: str = "DeploymentIdRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentIsNotInReadyStateException(ServiceException):
    """The deployment does not have a status of Ready and can't continue yet."""

    code: str = "DeploymentIsNotInReadyStateException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentLimitExceededException(ServiceException):
    """The number of allowed deployments was exceeded."""

    code: str = "DeploymentLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentNotStartedException(ServiceException):
    """The specified deployment has not started."""

    code: str = "DeploymentNotStartedException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentTargetDoesNotExistException(ServiceException):
    """The provided target ID does not belong to the attempted deployment."""

    code: str = "DeploymentTargetDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentTargetIdRequiredException(ServiceException):
    """A deployment target ID was not provided."""

    code: str = "DeploymentTargetIdRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class DeploymentTargetListSizeExceededException(ServiceException):
    """The maximum number of targets that can be associated with an Amazon ECS
    or Lambda deployment was exceeded. The target list of both types of
    deployments must have exactly one item. This exception does not apply to
    EC2/On-premises deployments.
    """

    code: str = "DeploymentTargetListSizeExceededException"
    sender_fault: bool = False
    status_code: int = 400


class DescriptionTooLongException(ServiceException):
    """The description is too long."""

    code: str = "DescriptionTooLongException"
    sender_fault: bool = False
    status_code: int = 400


class ECSServiceMappingLimitExceededException(ServiceException):
    """The Amazon ECS service is associated with more than one deployment
    groups. An Amazon ECS service can be associated with only one deployment
    group.
    """

    code: str = "ECSServiceMappingLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class GitHubAccountTokenDoesNotExistException(ServiceException):
    """No GitHub account connection exists with the named specified in the
    call.
    """

    code: str = "GitHubAccountTokenDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class GitHubAccountTokenNameRequiredException(ServiceException):
    """The call is missing a required GitHub account connection name."""

    code: str = "GitHubAccountTokenNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class IamArnRequiredException(ServiceException):
    """No IAM ARN was included in the request. You must use an IAM session ARN
    or user ARN in the request.
    """

    code: str = "IamArnRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class IamSessionArnAlreadyRegisteredException(ServiceException):
    """The request included an IAM session ARN that has already been used to
    register a different instance.
    """

    code: str = "IamSessionArnAlreadyRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class IamUserArnAlreadyRegisteredException(ServiceException):
    """The specified user ARN is already registered with an on-premises
    instance.
    """

    code: str = "IamUserArnAlreadyRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class IamUserArnRequiredException(ServiceException):
    """An user ARN was not specified."""

    code: str = "IamUserArnRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceDoesNotExistException(ServiceException):
    """The specified instance does not exist in the deployment group."""

    code: str = "InstanceDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceIdRequiredException(ServiceException):
    """The instance ID was not specified."""

    code: str = "InstanceIdRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceLimitExceededException(ServiceException):
    """The maximum number of allowed on-premises instances in a single call was
    exceeded.
    """

    code: str = "InstanceLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceNameAlreadyRegisteredException(ServiceException):
    """The specified on-premises instance name is already registered."""

    code: str = "InstanceNameAlreadyRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceNameRequiredException(ServiceException):
    """An on-premises instance name was not specified."""

    code: str = "InstanceNameRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class InstanceNotRegisteredException(ServiceException):
    """The specified on-premises instance is not registered."""

    code: str = "InstanceNotRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidAlarmConfigException(ServiceException):
    """The format of the alarm configuration is invalid. Possible causes
    include:

    -  The alarm list is null.

    -  The alarm object is null.

    -  The alarm name is empty or null or exceeds the limit of 255
       characters.

    -  Two alarms with the same name have been specified.

    -  The alarm configuration is enabled, but the alarm list is empty.
    """

    code: str = "InvalidAlarmConfigException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidApplicationNameException(ServiceException):
    """The application name was specified in an invalid format."""

    code: str = "InvalidApplicationNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidArnException(ServiceException):
    """The specified ARN is not in a valid format."""

    code: str = "InvalidArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidAutoRollbackConfigException(ServiceException):
    """The automatic rollback configuration was specified in an invalid format.
    For example, automatic rollback is enabled, but an invalid triggering
    event type or no event types were listed.
    """

    code: str = "InvalidAutoRollbackConfigException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidAutoScalingGroupException(ServiceException):
    """The Auto Scaling group was specified in an invalid format or does not
    exist.
    """

    code: str = "InvalidAutoScalingGroupException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidBlueGreenDeploymentConfigurationException(ServiceException):
    """The configuration for the blue/green deployment group was provided in an
    invalid format. For information about deployment configuration format,
    see CreateDeploymentConfig.
    """

    code: str = "InvalidBlueGreenDeploymentConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidBucketNameFilterException(ServiceException):
    """The bucket name either doesn't exist or was specified in an invalid
    format.
    """

    code: str = "InvalidBucketNameFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidComputePlatformException(ServiceException):
    """The computePlatform is invalid. The computePlatform should be
    ``Lambda``, ``Server``, or ``ECS``.
    """

    code: str = "InvalidComputePlatformException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeployedStateFilterException(ServiceException):
    """The deployed state filter was specified in an invalid format."""

    code: str = "InvalidDeployedStateFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentConfigNameException(ServiceException):
    """The deployment configuration name was specified in an invalid format."""

    code: str = "InvalidDeploymentConfigNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentGroupNameException(ServiceException):
    """The deployment group name was specified in an invalid format."""

    code: str = "InvalidDeploymentGroupNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentIdException(ServiceException):
    """At least one of the deployment IDs was specified in an invalid format."""

    code: str = "InvalidDeploymentIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentInstanceTypeException(ServiceException):
    """An instance type was specified for an in-place deployment. Instance
    types are supported for blue/green deployments only.
    """

    code: str = "InvalidDeploymentInstanceTypeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentStatusException(ServiceException):
    """The specified deployment status doesn't exist or cannot be determined."""

    code: str = "InvalidDeploymentStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentStyleException(ServiceException):
    """An invalid deployment style was specified. Valid deployment types
    include "IN_PLACE" and "BLUE_GREEN." Valid deployment options include
    "WITH_TRAFFIC_CONTROL" and "WITHOUT_TRAFFIC_CONTROL."
    """

    code: str = "InvalidDeploymentStyleException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentTargetIdException(ServiceException):
    """The target ID provided was not valid."""

    code: str = "InvalidDeploymentTargetIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDeploymentWaitTypeException(ServiceException):
    """The wait type is invalid."""

    code: str = "InvalidDeploymentWaitTypeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEC2TagCombinationException(ServiceException):
    """A call was submitted that specified both Ec2TagFilters and Ec2TagSet,
    but only one of these data types can be used in a single call.
    """

    code: str = "InvalidEC2TagCombinationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEC2TagException(ServiceException):
    """The tag was specified in an invalid format."""

    code: str = "InvalidEC2TagException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidECSServiceException(ServiceException):
    """The Amazon ECS service identifier is not valid."""

    code: str = "InvalidECSServiceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidExternalIdException(ServiceException):
    """The external ID was specified in an invalid format."""

    code: str = "InvalidExternalIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidFileExistsBehaviorException(ServiceException):
    """An invalid fileExistsBehavior option was specified to determine how
    CodeDeploy handles files or directories that already exist in a
    deployment target location, but weren't part of the previous successful
    deployment. Valid values include "DISALLOW," "OVERWRITE," and "RETAIN."
    """

    code: str = "InvalidFileExistsBehaviorException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidGitHubAccountTokenException(ServiceException):
    """The GitHub token is not valid."""

    code: str = "InvalidGitHubAccountTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidGitHubAccountTokenNameException(ServiceException):
    """The format of the specified GitHub account connection name is invalid."""

    code: str = "InvalidGitHubAccountTokenNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidIamSessionArnException(ServiceException):
    """The IAM session ARN was specified in an invalid format."""

    code: str = "InvalidIamSessionArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidIamUserArnException(ServiceException):
    """The user ARN was specified in an invalid format."""

    code: str = "InvalidIamUserArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidIgnoreApplicationStopFailuresValueException(ServiceException):
    """The IgnoreApplicationStopFailures value is invalid. For Lambda
    deployments, ``false`` is expected. For EC2/On-premises deployments,
    ``true`` or ``false`` is expected.
    """

    code: str = "InvalidIgnoreApplicationStopFailuresValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInputException(ServiceException):
    """The input was specified in an invalid format."""

    code: str = "InvalidInputException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceIdException(ServiceException):
    code: str = "InvalidInstanceIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceNameException(ServiceException):
    """The on-premises instance name was specified in an invalid format."""

    code: str = "InvalidInstanceNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceStatusException(ServiceException):
    """The specified instance status does not exist."""

    code: str = "InvalidInstanceStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInstanceTypeException(ServiceException):
    """An invalid instance type was specified for instances in a blue/green
    deployment. Valid values include "Blue" for an original environment and
    "Green" for a replacement environment.
    """

    code: str = "InvalidInstanceTypeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidKeyPrefixFilterException(ServiceException):
    """The specified key prefix filter was specified in an invalid format."""

    code: str = "InvalidKeyPrefixFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLifecycleEventHookExecutionIdException(ServiceException):
    """A lifecycle event hook is invalid. Review the ``hooks`` section in your
    AppSpec file to ensure the lifecycle events and ``hooks`` functions are
    valid.
    """

    code: str = "InvalidLifecycleEventHookExecutionIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLifecycleEventHookExecutionStatusException(ServiceException):
    """The result of a Lambda validation function that verifies a lifecycle
    event is invalid. It should return ``Succeeded`` or ``Failed``.
    """

    code: str = "InvalidLifecycleEventHookExecutionStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLoadBalancerInfoException(ServiceException):
    """An invalid load balancer name, or no load balancer name, was specified."""

    code: str = "InvalidLoadBalancerInfoException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidMinimumHealthyHostValueException(ServiceException):
    """The minimum healthy instance value was specified in an invalid format."""

    code: str = "InvalidMinimumHealthyHostValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNextTokenException(ServiceException):
    """The next token was specified in an invalid format."""

    code: str = "InvalidNextTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOnPremisesTagCombinationException(ServiceException):
    """A call was submitted that specified both OnPremisesTagFilters and
    OnPremisesTagSet, but only one of these data types can be used in a
    single call.
    """

    code: str = "InvalidOnPremisesTagCombinationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOperationException(ServiceException):
    """An invalid operation was detected."""

    code: str = "InvalidOperationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRegistrationStatusException(ServiceException):
    """The registration status was specified in an invalid format."""

    code: str = "InvalidRegistrationStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRevisionException(ServiceException):
    """The revision was specified in an invalid format."""

    code: str = "InvalidRevisionException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidRoleException(ServiceException):
    """The service role ARN was specified in an invalid format. Or, if an Auto
    Scaling group was specified, the specified service role does not grant
    the appropriate permissions to Amazon EC2 Auto Scaling.
    """

    code: str = "InvalidRoleException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSortByException(ServiceException):
    """The column name to sort by is either not present or was specified in an
    invalid format.
    """

    code: str = "InvalidSortByException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSortOrderException(ServiceException):
    """The sort order was specified in an invalid format."""

    code: str = "InvalidSortOrderException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagException(ServiceException):
    """The tag was specified in an invalid format."""

    code: str = "InvalidTagException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagFilterException(ServiceException):
    """The tag filter was specified in an invalid format."""

    code: str = "InvalidTagFilterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagsToAddException(ServiceException):
    """The specified tags are not valid."""

    code: str = "InvalidTagsToAddException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetException(ServiceException):
    """A target is not valid."""

    code: str = "InvalidTargetException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetFilterNameException(ServiceException):
    """The target filter name is invalid."""

    code: str = "InvalidTargetFilterNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetGroupPairException(ServiceException):
    """A target group pair associated with this deployment is not valid."""

    code: str = "InvalidTargetGroupPairException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTargetInstancesException(ServiceException):
    """The target instance configuration is invalid. Possible causes include:

    -  Configuration data for target instances was entered for an in-place
       deployment.

    -  The limit of 10 tags for a tag type was exceeded.

    -  The combined length of the tag names exceeded the limit.

    -  A specified tag is not currently applied to any instances.
    """

    code: str = "InvalidTargetInstancesException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTimeRangeException(ServiceException):
    """The specified time range was specified in an invalid format."""

    code: str = "InvalidTimeRangeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTrafficRoutingConfigurationException(ServiceException):
    """The configuration that specifies how traffic is routed during a
    deployment is invalid.
    """

    code: str = "InvalidTrafficRoutingConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTriggerConfigException(ServiceException):
    """The trigger was specified in an invalid format."""

    code: str = "InvalidTriggerConfigException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidUpdateOutdatedInstancesOnlyValueException(ServiceException):
    """The UpdateOutdatedInstancesOnly value is invalid. For Lambda
    deployments, ``false`` is expected. For EC2/On-premises deployments,
    ``true`` or ``false`` is expected.
    """

    code: str = "InvalidUpdateOutdatedInstancesOnlyValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidZonalDeploymentConfigurationException(ServiceException):
    """The ``ZonalConfig`` object is not valid."""

    code: str = "InvalidZonalDeploymentConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class LifecycleEventAlreadyCompletedException(ServiceException):
    """An attempt to return the status of an already completed lifecycle event
    occurred.
    """

    code: str = "LifecycleEventAlreadyCompletedException"
    sender_fault: bool = False
    status_code: int = 400


class LifecycleHookLimitExceededException(ServiceException):
    """The limit for lifecycle hooks was exceeded."""

    code: str = "LifecycleHookLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class MultipleIamArnsProvidedException(ServiceException):
    """Both an user ARN and an IAM session ARN were included in the request.
    Use only one ARN type.
    """

    code: str = "MultipleIamArnsProvidedException"
    sender_fault: bool = False
    status_code: int = 400


class OperationNotSupportedException(ServiceException):
    """The API used does not support the deployment."""

    code: str = "OperationNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceArnRequiredException(ServiceException):
    """The ARN of a resource is required, but was not found."""

    code: str = "ResourceArnRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceValidationException(ServiceException):
    """The specified resource could not be validated."""

    code: str = "ResourceValidationException"
    sender_fault: bool = False
    status_code: int = 400


class RevisionDoesNotExistException(ServiceException):
    """The named revision does not exist with the user or Amazon Web Services
    account.
    """

    code: str = "RevisionDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class RevisionRequiredException(ServiceException):
    """The revision ID was not specified."""

    code: str = "RevisionRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class RoleRequiredException(ServiceException):
    """The role ID was not specified."""

    code: str = "RoleRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class TagLimitExceededException(ServiceException):
    """The maximum allowed number of tags was exceeded."""

    code: str = "TagLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class TagRequiredException(ServiceException):
    """A tag was not specified."""

    code: str = "TagRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class TagSetListLimitExceededException(ServiceException):
    """The number of tag groups included in the tag set list exceeded the
    maximum allowed limit of 3.
    """

    code: str = "TagSetListLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """An API function was called too frequently."""

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class TriggerTargetsLimitExceededException(ServiceException):
    """The maximum allowed number of triggers was exceeded."""

    code: str = "TriggerTargetsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedActionForDeploymentTypeException(ServiceException):
    """A call was submitted that is not supported for the specified deployment
    type.
    """

    code: str = "UnsupportedActionForDeploymentTypeException"
    sender_fault: bool = False
    status_code: int = 400


InstanceNameList = List[InstanceName]


class Tag(TypedDict, total=False):
    """Information about a tag."""

    Key: Optional[Key]
    Value: Optional[Value]


TagList = List[Tag]


class AddTagsToOnPremisesInstancesInput(ServiceRequest):
    """Represents the input of, and adds tags to, an on-premises instance
    operation.
    """

    tags: TagList
    instanceNames: InstanceNameList


class Alarm(TypedDict, total=False):
    """Information about an alarm."""

    name: Optional[AlarmName]


AlarmList = List[Alarm]


class AlarmConfiguration(TypedDict, total=False):
    """Information about alarms associated with a deployment or deployment
    group.
    """

    enabled: Optional[Boolean]
    ignorePollAlarmFailure: Optional[Boolean]
    alarms: Optional[AlarmList]


class AppSpecContent(TypedDict, total=False):
    """A revision for an Lambda or Amazon ECS deployment that is a
    YAML-formatted or JSON-formatted string. For Lambda and Amazon ECS
    deployments, the revision is the same as the AppSpec file. This method
    replaces the deprecated ``RawString`` data type.
    """

    content: Optional[RawStringContent]
    sha256: Optional[RawStringSha256]


Timestamp = datetime


class ApplicationInfo(TypedDict, total=False):
    """Information about an application."""

    applicationId: Optional[ApplicationId]
    applicationName: Optional[ApplicationName]
    createTime: Optional[Timestamp]
    linkedToGitHub: Optional[Boolean]
    gitHubAccountName: Optional[GitHubAccountTokenName]
    computePlatform: Optional[ComputePlatform]


ApplicationsInfoList = List[ApplicationInfo]
ApplicationsList = List[ApplicationName]
AutoRollbackEventsList = List[AutoRollbackEvent]


class AutoRollbackConfiguration(TypedDict, total=False):
    """Information about a configuration for automatically rolling back to a
    previous version of an application revision when a deployment is not
    completed successfully.
    """

    enabled: Optional[Boolean]
    events: Optional[AutoRollbackEventsList]


class AutoScalingGroup(TypedDict, total=False):
    """Information about an Auto Scaling group."""

    name: Optional[AutoScalingGroupName]
    hook: Optional[AutoScalingGroupHook]
    terminationHook: Optional[AutoScalingGroupHook]


AutoScalingGroupList = List[AutoScalingGroup]
AutoScalingGroupNameList = List[AutoScalingGroupName]


class RawString(TypedDict, total=False):
    """A revision for an Lambda deployment that is a YAML-formatted or
    JSON-formatted string. For Lambda deployments, the revision is the same
    as the AppSpec file.
    """

    content: Optional[RawStringContent]
    sha256: Optional[RawStringSha256]


class GitHubLocation(TypedDict, total=False):
    """Information about the location of application artifacts stored in
    GitHub.
    """

    repository: Optional[Repository]
    commitId: Optional[CommitId]


class S3Location(TypedDict, total=False):
    """Information about the location of application artifacts stored in Amazon
    S3.
    """

    bucket: Optional[S3Bucket]
    key: Optional[S3Key]
    bundleType: Optional[BundleType]
    version: Optional[VersionId]
    eTag: Optional[ETag]


class RevisionLocation(TypedDict, total=False):
    """Information about the location of an application revision."""

    revisionType: Optional[RevisionLocationType]
    s3Location: Optional[S3Location]
    gitHubLocation: Optional[GitHubLocation]
    string: Optional[RawString]
    appSpecContent: Optional[AppSpecContent]


RevisionLocationList = List[RevisionLocation]


class BatchGetApplicationRevisionsInput(ServiceRequest):
    """Represents the input of a ``BatchGetApplicationRevisions`` operation."""

    applicationName: ApplicationName
    revisions: RevisionLocationList


DeploymentGroupsList = List[DeploymentGroupName]


class GenericRevisionInfo(TypedDict, total=False):
    """Information about an application revision."""

    description: Optional[Description]
    deploymentGroups: Optional[DeploymentGroupsList]
    firstUsedTime: Optional[Timestamp]
    lastUsedTime: Optional[Timestamp]
    registerTime: Optional[Timestamp]


class RevisionInfo(TypedDict, total=False):
    """Information about an application revision."""

    revisionLocation: Optional[RevisionLocation]
    genericRevisionInfo: Optional[GenericRevisionInfo]


RevisionInfoList = List[RevisionInfo]


class BatchGetApplicationRevisionsOutput(TypedDict, total=False):
    """Represents the output of a ``BatchGetApplicationRevisions`` operation."""

    applicationName: Optional[ApplicationName]
    errorMessage: Optional[ErrorMessage]
    revisions: Optional[RevisionInfoList]


class BatchGetApplicationsInput(ServiceRequest):
    """Represents the input of a ``BatchGetApplications`` operation."""

    applicationNames: ApplicationsList


class BatchGetApplicationsOutput(TypedDict, total=False):
    """Represents the output of a ``BatchGetApplications`` operation."""

    applicationsInfo: Optional[ApplicationsInfoList]


class BatchGetDeploymentGroupsInput(ServiceRequest):
    """Represents the input of a ``BatchGetDeploymentGroups`` operation."""

    applicationName: ApplicationName
    deploymentGroupNames: DeploymentGroupsList


class ECSService(TypedDict, total=False):
    """Contains the service and cluster names used to identify an Amazon ECS
    deployment's target.
    """

    serviceName: Optional[ECSServiceName]
    clusterName: Optional[ECSClusterName]


ECSServiceList = List[ECSService]


class TagFilter(TypedDict, total=False):
    """Information about an on-premises instance tag filter."""

    Key: Optional[Key]
    Value: Optional[Value]
    Type: Optional[TagFilterType]


TagFilterList = List[TagFilter]
OnPremisesTagSetList = List[TagFilterList]


class OnPremisesTagSet(TypedDict, total=False):
    """Information about groups of on-premises instance tags."""

    onPremisesTagSetList: Optional[OnPremisesTagSetList]


class EC2TagFilter(TypedDict, total=False):
    """Information about an EC2 tag filter."""

    Key: Optional[Key]
    Value: Optional[Value]
    Type: Optional[EC2TagFilterType]


EC2TagFilterList = List[EC2TagFilter]
EC2TagSetList = List[EC2TagFilterList]


class EC2TagSet(TypedDict, total=False):
    """Information about groups of Amazon EC2 instance tags."""

    ec2TagSetList: Optional[EC2TagSetList]


class LastDeploymentInfo(TypedDict, total=False):
    """Information about the most recent attempted or successful deployment to
    a deployment group.
    """

    deploymentId: Optional[DeploymentId]
    status: Optional[DeploymentStatus]
    endTime: Optional[Timestamp]
    createTime: Optional[Timestamp]


ListenerArnList = List[ListenerArn]


class TrafficRoute(TypedDict, total=False):
    """Information about a listener. The listener contains the path used to
    route traffic that is received from the load balancer to a target group.
    """

    listenerArns: Optional[ListenerArnList]


class TargetGroupInfo(TypedDict, total=False):
    """Information about a target group in Elastic Load Balancing to use in a
    deployment. Instances are registered as targets in a target group, and
    traffic is routed to the target group.
    """

    name: Optional[TargetGroupName]


TargetGroupInfoList = List[TargetGroupInfo]


class TargetGroupPairInfo(TypedDict, total=False):
    """Information about two target groups and how traffic is routed during an
    Amazon ECS deployment. An optional test traffic route can be specified.
    """

    targetGroups: Optional[TargetGroupInfoList]
    prodTrafficRoute: Optional[TrafficRoute]
    testTrafficRoute: Optional[TrafficRoute]


TargetGroupPairInfoList = List[TargetGroupPairInfo]


class ELBInfo(TypedDict, total=False):
    """Information about a Classic Load Balancer in Elastic Load Balancing to
    use in a deployment. Instances are registered directly with a load
    balancer, and traffic is routed to the load balancer.
    """

    name: Optional[ELBName]


ELBInfoList = List[ELBInfo]


class LoadBalancerInfo(TypedDict, total=False):
    """Information about the Elastic Load Balancing load balancer or target
    group used in a deployment.

    You can use load balancers and target groups in combination. For
    example, if you have two Classic Load Balancers, and five target groups
    tied to an Application Load Balancer, you can specify the two Classic
    Load Balancers in ``elbInfoList``, and the five target groups in
    ``targetGroupInfoList``.
    """

    elbInfoList: Optional[ELBInfoList]
    targetGroupInfoList: Optional[TargetGroupInfoList]
    targetGroupPairInfoList: Optional[TargetGroupPairInfoList]


class GreenFleetProvisioningOption(TypedDict, total=False):
    """Information about the instances that belong to the replacement
    environment in a blue/green deployment.
    """

    action: Optional[GreenFleetProvisioningAction]


class DeploymentReadyOption(TypedDict, total=False):
    """Information about how traffic is rerouted to instances in a replacement
    environment in a blue/green deployment.
    """

    actionOnTimeout: Optional[DeploymentReadyAction]
    waitTimeInMinutes: Optional[Duration]


class BlueInstanceTerminationOption(TypedDict, total=False):
    """Information about whether instances in the original environment are
    terminated when a blue/green deployment is successful.
    ``BlueInstanceTerminationOption`` does not apply to Lambda deployments.
    """

    action: Optional[InstanceAction]
    terminationWaitTimeInMinutes: Optional[Duration]


class BlueGreenDeploymentConfiguration(TypedDict, total=False):
    """Information about blue/green deployment options for a deployment group."""

    terminateBlueInstancesOnDeploymentSuccess: Optional[BlueInstanceTerminationOption]
    deploymentReadyOption: Optional[DeploymentReadyOption]
    greenFleetProvisioningOption: Optional[GreenFleetProvisioningOption]


class DeploymentStyle(TypedDict, total=False):
    """Information about the type of deployment, either in-place or blue/green,
    you want to run and whether to route deployment traffic behind a load
    balancer.
    """

    deploymentType: Optional[DeploymentType]
    deploymentOption: Optional[DeploymentOption]


TriggerEventTypeList = List[TriggerEventType]


class TriggerConfig(TypedDict, total=False):
    """Information about notification triggers for the deployment group."""

    triggerName: Optional[TriggerName]
    triggerTargetArn: Optional[TriggerTargetArn]
    triggerEvents: Optional[TriggerEventTypeList]


TriggerConfigList = List[TriggerConfig]


class DeploymentGroupInfo(TypedDict, total=False):
    """Information about a deployment group."""

    applicationName: Optional[ApplicationName]
    deploymentGroupId: Optional[DeploymentGroupId]
    deploymentGroupName: Optional[DeploymentGroupName]
    deploymentConfigName: Optional[DeploymentConfigName]
    ec2TagFilters: Optional[EC2TagFilterList]
    onPremisesInstanceTagFilters: Optional[TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupList]
    serviceRoleArn: Optional[Role]
    targetRevision: Optional[RevisionLocation]
    triggerConfigurations: Optional[TriggerConfigList]
    alarmConfiguration: Optional[AlarmConfiguration]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    deploymentStyle: Optional[DeploymentStyle]
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategy]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    lastSuccessfulDeployment: Optional[LastDeploymentInfo]
    lastAttemptedDeployment: Optional[LastDeploymentInfo]
    ec2TagSet: Optional[EC2TagSet]
    onPremisesTagSet: Optional[OnPremisesTagSet]
    computePlatform: Optional[ComputePlatform]
    ecsServices: Optional[ECSServiceList]
    terminationHookEnabled: Optional[Boolean]


DeploymentGroupInfoList = List[DeploymentGroupInfo]


class BatchGetDeploymentGroupsOutput(TypedDict, total=False):
    """Represents the output of a ``BatchGetDeploymentGroups`` operation."""

    deploymentGroupsInfo: Optional[DeploymentGroupInfoList]
    errorMessage: Optional[ErrorMessage]


InstancesList = List[InstanceId]


class BatchGetDeploymentInstancesInput(ServiceRequest):
    """Represents the input of a ``BatchGetDeploymentInstances`` operation."""

    deploymentId: DeploymentId
    instanceIds: InstancesList


class Diagnostics(TypedDict, total=False):
    """Diagnostic information about executable scripts that are part of a
    deployment.
    """

    errorCode: Optional[LifecycleErrorCode]
    scriptName: Optional[ScriptName]
    message: Optional[LifecycleMessage]
    logTail: Optional[LogTail]


class LifecycleEvent(TypedDict, total=False):
    """Information about a deployment lifecycle event."""

    lifecycleEventName: Optional[LifecycleEventName]
    diagnostics: Optional[Diagnostics]
    startTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    status: Optional[LifecycleEventStatus]


LifecycleEventList = List[LifecycleEvent]


class InstanceSummary(TypedDict, total=False):
    """Information about an instance in a deployment."""

    deploymentId: Optional[DeploymentId]
    instanceId: Optional[InstanceId]
    status: Optional[InstanceStatus]
    lastUpdatedAt: Optional[Timestamp]
    lifecycleEvents: Optional[LifecycleEventList]
    instanceType: Optional[InstanceType]


InstanceSummaryList = List[InstanceSummary]


class BatchGetDeploymentInstancesOutput(TypedDict, total=False):
    """Represents the output of a ``BatchGetDeploymentInstances`` operation."""

    instancesSummary: Optional[InstanceSummaryList]
    errorMessage: Optional[ErrorMessage]


TargetIdList = List[TargetId]


class BatchGetDeploymentTargetsInput(ServiceRequest):
    deploymentId: DeploymentId
    targetIds: TargetIdList


Time = datetime


class CloudFormationTarget(TypedDict, total=False):
    """Information about the target to be updated by an CloudFormation
    blue/green deployment. This target type is used for all deployments
    initiated by a CloudFormation stack update.
    """

    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    status: Optional[TargetStatus]
    resourceType: Optional[CloudFormationResourceType]
    targetVersionWeight: Optional[TrafficWeight]


ECSTaskSetCount = int


class ECSTaskSet(TypedDict, total=False):
    """Information about a set of Amazon ECS tasks in an CodeDeploy deployment.
    An Amazon ECS task set includes details such as the desired number of
    tasks, how many tasks are running, and whether the task set serves
    production traffic. An CodeDeploy application that uses the Amazon ECS
    compute platform deploys a containerized application in an Amazon ECS
    service as a task set.
    """

    identifer: Optional[ECSTaskSetIdentifier]
    desiredCount: Optional[ECSTaskSetCount]
    pendingCount: Optional[ECSTaskSetCount]
    runningCount: Optional[ECSTaskSetCount]
    status: Optional[ECSTaskSetStatus]
    trafficWeight: Optional[TrafficWeight]
    targetGroup: Optional[TargetGroupInfo]
    taskSetLabel: Optional[TargetLabel]


ECSTaskSetList = List[ECSTaskSet]


class ECSTarget(TypedDict, total=False):
    """Information about the target of an Amazon ECS deployment."""

    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    targetArn: Optional[TargetArn]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    status: Optional[TargetStatus]
    taskSetsInfo: Optional[ECSTaskSetList]


class LambdaFunctionInfo(TypedDict, total=False):
    """Information about a Lambda function specified in a deployment."""

    functionName: Optional[LambdaFunctionName]
    functionAlias: Optional[LambdaFunctionAlias]
    currentVersion: Optional[Version]
    targetVersion: Optional[Version]
    targetVersionWeight: Optional[TrafficWeight]


class LambdaTarget(TypedDict, total=False):
    """Information about the target Lambda function during an Lambda
    deployment.
    """

    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    targetArn: Optional[TargetArn]
    status: Optional[TargetStatus]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    lambdaFunctionInfo: Optional[LambdaFunctionInfo]


class InstanceTarget(TypedDict, total=False):
    """A target Amazon EC2 or on-premises instance during a deployment that
    uses the EC2/On-premises compute platform.
    """

    deploymentId: Optional[DeploymentId]
    targetId: Optional[TargetId]
    targetArn: Optional[TargetArn]
    status: Optional[TargetStatus]
    lastUpdatedAt: Optional[Time]
    lifecycleEvents: Optional[LifecycleEventList]
    instanceLabel: Optional[TargetLabel]


class DeploymentTarget(TypedDict, total=False):
    """Information about the deployment target."""

    deploymentTargetType: Optional[DeploymentTargetType]
    instanceTarget: Optional[InstanceTarget]
    lambdaTarget: Optional[LambdaTarget]
    ecsTarget: Optional[ECSTarget]
    cloudFormationTarget: Optional[CloudFormationTarget]


DeploymentTargetList = List[DeploymentTarget]


class BatchGetDeploymentTargetsOutput(TypedDict, total=False):
    deploymentTargets: Optional[DeploymentTargetList]


DeploymentsList = List[DeploymentId]


class BatchGetDeploymentsInput(ServiceRequest):
    """Represents the input of a ``BatchGetDeployments`` operation."""

    deploymentIds: DeploymentsList


class RelatedDeployments(TypedDict, total=False):
    """Information about deployments related to the specified deployment."""

    autoUpdateOutdatedInstancesRootDeploymentId: Optional[DeploymentId]
    autoUpdateOutdatedInstancesDeploymentIds: Optional[DeploymentsList]


DeploymentStatusMessageList = List[ErrorMessage]


class TargetInstances(TypedDict, total=False):
    """Information about the instances to be used in the replacement
    environment in a blue/green deployment.
    """

    tagFilters: Optional[EC2TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupNameList]
    ec2TagSet: Optional[EC2TagSet]


class RollbackInfo(TypedDict, total=False):
    """Information about a deployment rollback."""

    rollbackDeploymentId: Optional[DeploymentId]
    rollbackTriggeringDeploymentId: Optional[DeploymentId]
    rollbackMessage: Optional[Description]


InstanceCount = int


class DeploymentOverview(TypedDict, total=False):
    """Information about the deployment status of the instances in the
    deployment.
    """

    Pending: Optional[InstanceCount]
    InProgress: Optional[InstanceCount]
    Succeeded: Optional[InstanceCount]
    Failed: Optional[InstanceCount]
    Skipped: Optional[InstanceCount]
    Ready: Optional[InstanceCount]


class ErrorInformation(TypedDict, total=False):
    """Information about a deployment error."""

    code: Optional[ErrorCode]
    message: Optional[ErrorMessage]


class DeploymentInfo(TypedDict, total=False):
    """Information about a deployment."""

    applicationName: Optional[ApplicationName]
    deploymentGroupName: Optional[DeploymentGroupName]
    deploymentConfigName: Optional[DeploymentConfigName]
    deploymentId: Optional[DeploymentId]
    previousRevision: Optional[RevisionLocation]
    revision: Optional[RevisionLocation]
    status: Optional[DeploymentStatus]
    errorInformation: Optional[ErrorInformation]
    createTime: Optional[Timestamp]
    startTime: Optional[Timestamp]
    completeTime: Optional[Timestamp]
    deploymentOverview: Optional[DeploymentOverview]
    description: Optional[Description]
    creator: Optional[DeploymentCreator]
    ignoreApplicationStopFailures: Optional[Boolean]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    updateOutdatedInstancesOnly: Optional[Boolean]
    rollbackInfo: Optional[RollbackInfo]
    deploymentStyle: Optional[DeploymentStyle]
    targetInstances: Optional[TargetInstances]
    instanceTerminationWaitTimeStarted: Optional[Boolean]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    additionalDeploymentStatusInfo: Optional[AdditionalDeploymentStatusInfo]
    fileExistsBehavior: Optional[FileExistsBehavior]
    deploymentStatusMessages: Optional[DeploymentStatusMessageList]
    computePlatform: Optional[ComputePlatform]
    externalId: Optional[ExternalId]
    relatedDeployments: Optional[RelatedDeployments]
    overrideAlarmConfiguration: Optional[AlarmConfiguration]


DeploymentsInfoList = List[DeploymentInfo]


class BatchGetDeploymentsOutput(TypedDict, total=False):
    """Represents the output of a ``BatchGetDeployments`` operation."""

    deploymentsInfo: Optional[DeploymentsInfoList]


class BatchGetOnPremisesInstancesInput(ServiceRequest):
    """Represents the input of a ``BatchGetOnPremisesInstances`` operation."""

    instanceNames: InstanceNameList


class InstanceInfo(TypedDict, total=False):
    """Information about an on-premises instance."""

    instanceName: Optional[InstanceName]
    iamSessionArn: Optional[IamSessionArn]
    iamUserArn: Optional[IamUserArn]
    instanceArn: Optional[InstanceArn]
    registerTime: Optional[Timestamp]
    deregisterTime: Optional[Timestamp]
    tags: Optional[TagList]


InstanceInfoList = List[InstanceInfo]


class BatchGetOnPremisesInstancesOutput(TypedDict, total=False):
    """Represents the output of a ``BatchGetOnPremisesInstances`` operation."""

    instanceInfos: Optional[InstanceInfoList]


class ContinueDeploymentInput(ServiceRequest):
    deploymentId: Optional[DeploymentId]
    deploymentWaitType: Optional[DeploymentWaitType]


class CreateApplicationInput(ServiceRequest):
    """Represents the input of a ``CreateApplication`` operation."""

    applicationName: ApplicationName
    computePlatform: Optional[ComputePlatform]
    tags: Optional[TagList]


class CreateApplicationOutput(TypedDict, total=False):
    """Represents the output of a ``CreateApplication`` operation."""

    applicationId: Optional[ApplicationId]


MinimumHealthyHostsPerZone = TypedDict(
    "MinimumHealthyHostsPerZone",
    {
        "type": Optional[MinimumHealthyHostsPerZoneType],
        "value": Optional[MinimumHealthyHostsPerZoneValue],
    },
    total=False,
)
WaitTimeInSeconds = int


class ZonalConfig(TypedDict, total=False):
    """Configure the ``ZonalConfig`` object if you want CodeDeploy to deploy
    your application to one `Availability
    Zone <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones>`__
    at a time, within an Amazon Web Services Region. By deploying to one
    Availability Zone at a time, you can expose your deployment to a
    progressively larger audience as confidence in the deployment's
    performance and viability grows. If you don't configure the
    ``ZonalConfig`` object, CodeDeploy deploys your application to a random
    selection of hosts across a Region.

    For more information about the zonal configuration feature, see `zonal
    configuration <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config>`__
    in the *CodeDeploy User Guide*.
    """

    firstZoneMonitorDurationInSeconds: Optional[WaitTimeInSeconds]
    monitorDurationInSeconds: Optional[WaitTimeInSeconds]
    minimumHealthyHostsPerZone: Optional[MinimumHealthyHostsPerZone]


class TimeBasedLinear(TypedDict, total=False):
    """A configuration that shifts traffic from one version of a Lambda
    function or ECS task set to another in equal increments, with an equal
    number of minutes between each increment. The original and target Lambda
    function versions or ECS task sets are specified in the deployment's
    AppSpec file.
    """

    linearPercentage: Optional[Percentage]
    linearInterval: Optional[WaitTimeInMins]


class TimeBasedCanary(TypedDict, total=False):
    """A configuration that shifts traffic from one version of a Lambda
    function or Amazon ECS task set to another in two increments. The
    original and target Lambda function versions or ECS task sets are
    specified in the deployment's AppSpec file.
    """

    canaryPercentage: Optional[Percentage]
    canaryInterval: Optional[WaitTimeInMins]


TrafficRoutingConfig = TypedDict(
    "TrafficRoutingConfig",
    {
        "type": Optional[TrafficRoutingType],
        "timeBasedCanary": Optional[TimeBasedCanary],
        "timeBasedLinear": Optional[TimeBasedLinear],
    },
    total=False,
)
MinimumHealthyHosts = TypedDict(
    "MinimumHealthyHosts",
    {
        "type": Optional[MinimumHealthyHostsType],
        "value": Optional[MinimumHealthyHostsValue],
    },
    total=False,
)


class CreateDeploymentConfigInput(ServiceRequest):
    """Represents the input of a ``CreateDeploymentConfig`` operation."""

    deploymentConfigName: DeploymentConfigName
    minimumHealthyHosts: Optional[MinimumHealthyHosts]
    trafficRoutingConfig: Optional[TrafficRoutingConfig]
    computePlatform: Optional[ComputePlatform]
    zonalConfig: Optional[ZonalConfig]


class CreateDeploymentConfigOutput(TypedDict, total=False):
    """Represents the output of a ``CreateDeploymentConfig`` operation."""

    deploymentConfigId: Optional[DeploymentConfigId]


class CreateDeploymentGroupInput(ServiceRequest):
    """Represents the input of a ``CreateDeploymentGroup`` operation."""

    applicationName: ApplicationName
    deploymentGroupName: DeploymentGroupName
    deploymentConfigName: Optional[DeploymentConfigName]
    ec2TagFilters: Optional[EC2TagFilterList]
    onPremisesInstanceTagFilters: Optional[TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupNameList]
    serviceRoleArn: Role
    triggerConfigurations: Optional[TriggerConfigList]
    alarmConfiguration: Optional[AlarmConfiguration]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategy]
    deploymentStyle: Optional[DeploymentStyle]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    ec2TagSet: Optional[EC2TagSet]
    ecsServices: Optional[ECSServiceList]
    onPremisesTagSet: Optional[OnPremisesTagSet]
    tags: Optional[TagList]
    terminationHookEnabled: Optional[NullableBoolean]


class CreateDeploymentGroupOutput(TypedDict, total=False):
    """Represents the output of a ``CreateDeploymentGroup`` operation."""

    deploymentGroupId: Optional[DeploymentGroupId]


class CreateDeploymentInput(ServiceRequest):
    """Represents the input of a ``CreateDeployment`` operation."""

    applicationName: ApplicationName
    deploymentGroupName: Optional[DeploymentGroupName]
    revision: Optional[RevisionLocation]
    deploymentConfigName: Optional[DeploymentConfigName]
    description: Optional[Description]
    ignoreApplicationStopFailures: Optional[Boolean]
    targetInstances: Optional[TargetInstances]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    updateOutdatedInstancesOnly: Optional[Boolean]
    fileExistsBehavior: Optional[FileExistsBehavior]
    overrideAlarmConfiguration: Optional[AlarmConfiguration]


class CreateDeploymentOutput(TypedDict, total=False):
    """Represents the output of a ``CreateDeployment`` operation."""

    deploymentId: Optional[DeploymentId]


class DeleteApplicationInput(ServiceRequest):
    """Represents the input of a ``DeleteApplication`` operation."""

    applicationName: ApplicationName


class DeleteDeploymentConfigInput(ServiceRequest):
    """Represents the input of a ``DeleteDeploymentConfig`` operation."""

    deploymentConfigName: DeploymentConfigName


class DeleteDeploymentGroupInput(ServiceRequest):
    """Represents the input of a ``DeleteDeploymentGroup`` operation."""

    applicationName: ApplicationName
    deploymentGroupName: DeploymentGroupName


class DeleteDeploymentGroupOutput(TypedDict, total=False):
    """Represents the output of a ``DeleteDeploymentGroup`` operation."""

    hooksNotCleanedUp: Optional[AutoScalingGroupList]


class DeleteGitHubAccountTokenInput(ServiceRequest):
    """Represents the input of a ``DeleteGitHubAccount`` operation."""

    tokenName: Optional[GitHubAccountTokenName]


class DeleteGitHubAccountTokenOutput(TypedDict, total=False):
    """Represents the output of a ``DeleteGitHubAccountToken`` operation."""

    tokenName: Optional[GitHubAccountTokenName]


class DeleteResourcesByExternalIdInput(ServiceRequest):
    externalId: Optional[ExternalId]


class DeleteResourcesByExternalIdOutput(TypedDict, total=False):
    pass


class DeploymentConfigInfo(TypedDict, total=False):
    """Information about a deployment configuration."""

    deploymentConfigId: Optional[DeploymentConfigId]
    deploymentConfigName: Optional[DeploymentConfigName]
    minimumHealthyHosts: Optional[MinimumHealthyHosts]
    createTime: Optional[Timestamp]
    computePlatform: Optional[ComputePlatform]
    trafficRoutingConfig: Optional[TrafficRoutingConfig]
    zonalConfig: Optional[ZonalConfig]


DeploymentConfigsList = List[DeploymentConfigName]
DeploymentStatusList = List[DeploymentStatus]


class DeregisterOnPremisesInstanceInput(ServiceRequest):
    """Represents the input of a ``DeregisterOnPremisesInstance`` operation."""

    instanceName: InstanceName


FilterValueList = List[FilterValue]


class GetApplicationInput(ServiceRequest):
    """Represents the input of a ``GetApplication`` operation."""

    applicationName: ApplicationName


class GetApplicationOutput(TypedDict, total=False):
    """Represents the output of a ``GetApplication`` operation."""

    application: Optional[ApplicationInfo]


class GetApplicationRevisionInput(ServiceRequest):
    """Represents the input of a ``GetApplicationRevision`` operation."""

    applicationName: ApplicationName
    revision: RevisionLocation


class GetApplicationRevisionOutput(TypedDict, total=False):
    """Represents the output of a ``GetApplicationRevision`` operation."""

    applicationName: Optional[ApplicationName]
    revision: Optional[RevisionLocation]
    revisionInfo: Optional[GenericRevisionInfo]


class GetDeploymentConfigInput(ServiceRequest):
    """Represents the input of a ``GetDeploymentConfig`` operation."""

    deploymentConfigName: DeploymentConfigName


class GetDeploymentConfigOutput(TypedDict, total=False):
    """Represents the output of a ``GetDeploymentConfig`` operation."""

    deploymentConfigInfo: Optional[DeploymentConfigInfo]


class GetDeploymentGroupInput(ServiceRequest):
    """Represents the input of a ``GetDeploymentGroup`` operation."""

    applicationName: ApplicationName
    deploymentGroupName: DeploymentGroupName


class GetDeploymentGroupOutput(TypedDict, total=False):
    """Represents the output of a ``GetDeploymentGroup`` operation."""

    deploymentGroupInfo: Optional[DeploymentGroupInfo]


class GetDeploymentInput(ServiceRequest):
    """Represents the input of a ``GetDeployment`` operation."""

    deploymentId: DeploymentId


class GetDeploymentInstanceInput(ServiceRequest):
    """Represents the input of a ``GetDeploymentInstance`` operation."""

    deploymentId: DeploymentId
    instanceId: InstanceId


class GetDeploymentInstanceOutput(TypedDict, total=False):
    """Represents the output of a ``GetDeploymentInstance`` operation."""

    instanceSummary: Optional[InstanceSummary]


class GetDeploymentOutput(TypedDict, total=False):
    """Represents the output of a ``GetDeployment`` operation."""

    deploymentInfo: Optional[DeploymentInfo]


class GetDeploymentTargetInput(ServiceRequest):
    deploymentId: DeploymentId
    targetId: TargetId


class GetDeploymentTargetOutput(TypedDict, total=False):
    deploymentTarget: Optional[DeploymentTarget]


class GetOnPremisesInstanceInput(ServiceRequest):
    """Represents the input of a ``GetOnPremisesInstance`` operation."""

    instanceName: InstanceName


class GetOnPremisesInstanceOutput(TypedDict, total=False):
    """Represents the output of a ``GetOnPremisesInstance`` operation."""

    instanceInfo: Optional[InstanceInfo]


GitHubAccountTokenNameList = List[GitHubAccountTokenName]
InstanceStatusList = List[InstanceStatus]
InstanceTypeList = List[InstanceType]


class ListApplicationRevisionsInput(ServiceRequest):
    """Represents the input of a ``ListApplicationRevisions`` operation."""

    applicationName: ApplicationName
    sortBy: Optional[ApplicationRevisionSortBy]
    sortOrder: Optional[SortOrder]
    s3Bucket: Optional[S3Bucket]
    s3KeyPrefix: Optional[S3Key]
    deployed: Optional[ListStateFilterAction]
    nextToken: Optional[NextToken]


class ListApplicationRevisionsOutput(TypedDict, total=False):
    """Represents the output of a ``ListApplicationRevisions`` operation."""

    revisions: Optional[RevisionLocationList]
    nextToken: Optional[NextToken]


class ListApplicationsInput(ServiceRequest):
    """Represents the input of a ``ListApplications`` operation."""

    nextToken: Optional[NextToken]


class ListApplicationsOutput(TypedDict, total=False):
    """Represents the output of a ListApplications operation."""

    applications: Optional[ApplicationsList]
    nextToken: Optional[NextToken]


class ListDeploymentConfigsInput(ServiceRequest):
    """Represents the input of a ``ListDeploymentConfigs`` operation."""

    nextToken: Optional[NextToken]


class ListDeploymentConfigsOutput(TypedDict, total=False):
    """Represents the output of a ``ListDeploymentConfigs`` operation."""

    deploymentConfigsList: Optional[DeploymentConfigsList]
    nextToken: Optional[NextToken]


class ListDeploymentGroupsInput(ServiceRequest):
    """Represents the input of a ``ListDeploymentGroups`` operation."""

    applicationName: ApplicationName
    nextToken: Optional[NextToken]


class ListDeploymentGroupsOutput(TypedDict, total=False):
    """Represents the output of a ``ListDeploymentGroups`` operation."""

    applicationName: Optional[ApplicationName]
    deploymentGroups: Optional[DeploymentGroupsList]
    nextToken: Optional[NextToken]


class ListDeploymentInstancesInput(ServiceRequest):
    """Represents the input of a ``ListDeploymentInstances`` operation."""

    deploymentId: DeploymentId
    nextToken: Optional[NextToken]
    instanceStatusFilter: Optional[InstanceStatusList]
    instanceTypeFilter: Optional[InstanceTypeList]


class ListDeploymentInstancesOutput(TypedDict, total=False):
    """Represents the output of a ``ListDeploymentInstances`` operation."""

    instancesList: Optional[InstancesList]
    nextToken: Optional[NextToken]


TargetFilters = Dict[TargetFilterName, FilterValueList]


class ListDeploymentTargetsInput(ServiceRequest):
    deploymentId: DeploymentId
    nextToken: Optional[NextToken]
    targetFilters: Optional[TargetFilters]


class ListDeploymentTargetsOutput(TypedDict, total=False):
    targetIds: Optional[TargetIdList]
    nextToken: Optional[NextToken]


class TimeRange(TypedDict, total=False):
    """Information about a time range."""

    start: Optional[Timestamp]
    end: Optional[Timestamp]


class ListDeploymentsInput(ServiceRequest):
    """Represents the input of a ``ListDeployments`` operation."""

    applicationName: Optional[ApplicationName]
    deploymentGroupName: Optional[DeploymentGroupName]
    externalId: Optional[ExternalId]
    includeOnlyStatuses: Optional[DeploymentStatusList]
    createTimeRange: Optional[TimeRange]
    nextToken: Optional[NextToken]


class ListDeploymentsOutput(TypedDict, total=False):
    """Represents the output of a ``ListDeployments`` operation."""

    deployments: Optional[DeploymentsList]
    nextToken: Optional[NextToken]


class ListGitHubAccountTokenNamesInput(ServiceRequest):
    """Represents the input of a ``ListGitHubAccountTokenNames`` operation."""

    nextToken: Optional[NextToken]


class ListGitHubAccountTokenNamesOutput(TypedDict, total=False):
    """Represents the output of a ``ListGitHubAccountTokenNames`` operation."""

    tokenNameList: Optional[GitHubAccountTokenNameList]
    nextToken: Optional[NextToken]


class ListOnPremisesInstancesInput(ServiceRequest):
    """Represents the input of a ``ListOnPremisesInstances`` operation."""

    registrationStatus: Optional[RegistrationStatus]
    tagFilters: Optional[TagFilterList]
    nextToken: Optional[NextToken]


class ListOnPremisesInstancesOutput(TypedDict, total=False):
    """Represents the output of the list on-premises instances operation."""

    instanceNames: Optional[InstanceNameList]
    nextToken: Optional[NextToken]


class ListTagsForResourceInput(ServiceRequest):
    ResourceArn: Arn
    NextToken: Optional[NextToken]


class ListTagsForResourceOutput(TypedDict, total=False):
    Tags: Optional[TagList]
    NextToken: Optional[NextToken]


class PutLifecycleEventHookExecutionStatusInput(ServiceRequest):
    deploymentId: Optional[DeploymentId]
    lifecycleEventHookExecutionId: Optional[LifecycleEventHookExecutionId]
    status: Optional[LifecycleEventStatus]


class PutLifecycleEventHookExecutionStatusOutput(TypedDict, total=False):
    lifecycleEventHookExecutionId: Optional[LifecycleEventHookExecutionId]


class RegisterApplicationRevisionInput(ServiceRequest):
    """Represents the input of a RegisterApplicationRevision operation."""

    applicationName: ApplicationName
    description: Optional[Description]
    revision: RevisionLocation


class RegisterOnPremisesInstanceInput(ServiceRequest):
    """Represents the input of the register on-premises instance operation."""

    instanceName: InstanceName
    iamSessionArn: Optional[IamSessionArn]
    iamUserArn: Optional[IamUserArn]


class RemoveTagsFromOnPremisesInstancesInput(ServiceRequest):
    """Represents the input of a ``RemoveTagsFromOnPremisesInstances``
    operation.
    """

    tags: TagList
    instanceNames: InstanceNameList


class SkipWaitTimeForInstanceTerminationInput(ServiceRequest):
    deploymentId: Optional[DeploymentId]


class StopDeploymentInput(ServiceRequest):
    """Represents the input of a ``StopDeployment`` operation."""

    deploymentId: DeploymentId
    autoRollbackEnabled: Optional[NullableBoolean]


class StopDeploymentOutput(TypedDict, total=False):
    """Represents the output of a ``StopDeployment`` operation."""

    status: Optional[StopStatus]
    statusMessage: Optional[Message]


TagKeyList = List[Key]


class TagResourceInput(ServiceRequest):
    ResourceArn: Arn
    Tags: TagList


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    ResourceArn: Arn
    TagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateApplicationInput(ServiceRequest):
    """Represents the input of an ``UpdateApplication`` operation."""

    applicationName: Optional[ApplicationName]
    newApplicationName: Optional[ApplicationName]


class UpdateDeploymentGroupInput(ServiceRequest):
    """Represents the input of an ``UpdateDeploymentGroup`` operation."""

    applicationName: ApplicationName
    currentDeploymentGroupName: DeploymentGroupName
    newDeploymentGroupName: Optional[DeploymentGroupName]
    deploymentConfigName: Optional[DeploymentConfigName]
    ec2TagFilters: Optional[EC2TagFilterList]
    onPremisesInstanceTagFilters: Optional[TagFilterList]
    autoScalingGroups: Optional[AutoScalingGroupNameList]
    serviceRoleArn: Optional[Role]
    triggerConfigurations: Optional[TriggerConfigList]
    alarmConfiguration: Optional[AlarmConfiguration]
    autoRollbackConfiguration: Optional[AutoRollbackConfiguration]
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategy]
    deploymentStyle: Optional[DeploymentStyle]
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration]
    loadBalancerInfo: Optional[LoadBalancerInfo]
    ec2TagSet: Optional[EC2TagSet]
    ecsServices: Optional[ECSServiceList]
    onPremisesTagSet: Optional[OnPremisesTagSet]
    terminationHookEnabled: Optional[NullableBoolean]


class UpdateDeploymentGroupOutput(TypedDict, total=False):
    """Represents the output of an ``UpdateDeploymentGroup`` operation."""

    hooksNotCleanedUp: Optional[AutoScalingGroupList]


class CodedeployApi:
    service = "codedeploy"
    version = "2014-10-06"

    @handler("AddTagsToOnPremisesInstances")
    def add_tags_to_on_premises_instances(
        self, context: RequestContext, tags: TagList, instance_names: InstanceNameList, **kwargs
    ) -> None:
        """Adds tags to on-premises instances.

        :param tags: The tag key-value pairs to add to the on-premises instances.
        :param instance_names: The names of the on-premises instances to which to add tags.
        :raises InstanceNameRequiredException:
        :raises InvalidInstanceNameException:
        :raises TagRequiredException:
        :raises InvalidTagException:
        :raises TagLimitExceededException:
        :raises InstanceLimitExceededException:
        :raises InstanceNotRegisteredException:
        """
        raise NotImplementedError

    @handler("BatchGetApplicationRevisions")
    def batch_get_application_revisions(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        revisions: RevisionLocationList,
        **kwargs,
    ) -> BatchGetApplicationRevisionsOutput:
        """Gets information about one or more application revisions. The maximum
        number of application revisions that can be returned is 25.

        :param application_name: The name of an CodeDeploy application about which to get revision
        information.
        :param revisions: An array of ``RevisionLocation`` objects that specify information to get
        about the application revisions, including type and location.
        :returns: BatchGetApplicationRevisionsOutput
        :raises ApplicationDoesNotExistException:
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises RevisionRequiredException:
        :raises InvalidRevisionException:
        :raises BatchLimitExceededException:
        """
        raise NotImplementedError

    @handler("BatchGetApplications")
    def batch_get_applications(
        self, context: RequestContext, application_names: ApplicationsList, **kwargs
    ) -> BatchGetApplicationsOutput:
        """Gets information about one or more applications. The maximum number of
        applications that can be returned is 100.

        :param application_names: A list of application names separated by spaces.
        :returns: BatchGetApplicationsOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises BatchLimitExceededException:
        """
        raise NotImplementedError

    @handler("BatchGetDeploymentGroups")
    def batch_get_deployment_groups(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_names: DeploymentGroupsList,
        **kwargs,
    ) -> BatchGetDeploymentGroupsOutput:
        """Gets information about one or more deployment groups.

        :param application_name: The name of an CodeDeploy application associated with the applicable
        user or Amazon Web Services account.
        :param deployment_group_names: The names of the deployment groups.
        :returns: BatchGetDeploymentGroupsOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises DeploymentGroupNameRequiredException:
        :raises InvalidDeploymentGroupNameException:
        :raises BatchLimitExceededException:
        :raises DeploymentConfigDoesNotExistException:
        """
        raise NotImplementedError

    @handler("BatchGetDeploymentInstances")
    def batch_get_deployment_instances(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        instance_ids: InstancesList,
        **kwargs,
    ) -> BatchGetDeploymentInstancesOutput:
        """This method works, but is deprecated. Use ``BatchGetDeploymentTargets``
        instead.

        Returns an array of one or more instances associated with a deployment.
        This method works with EC2/On-premises and Lambda compute platforms. The
        newer ``BatchGetDeploymentTargets`` works with all compute platforms.
        The maximum number of instances that can be returned is 25.

        :param deployment_id: The unique ID of a deployment.
        :param instance_ids: The unique IDs of instances used in the deployment.
        :returns: BatchGetDeploymentInstancesOutput
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises InstanceIdRequiredException:
        :raises InvalidDeploymentIdException:
        :raises InvalidInstanceNameException:
        :raises BatchLimitExceededException:
        :raises InvalidComputePlatformException:
        """
        raise NotImplementedError

    @handler("BatchGetDeploymentTargets")
    def batch_get_deployment_targets(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        target_ids: TargetIdList,
        **kwargs,
    ) -> BatchGetDeploymentTargetsOutput:
        """Returns an array of one or more targets associated with a deployment.
        This method works with all compute types and should be used instead of
        the deprecated ``BatchGetDeploymentInstances``. The maximum number of
        targets that can be returned is 25.

        The type of targets returned depends on the deployment's compute
        platform or deployment method:

        -  **EC2/On-premises**: Information about Amazon EC2 instance targets.

        -  **Lambda**: Information about Lambda functions targets.

        -  **Amazon ECS**: Information about Amazon ECS service targets.

        -  **CloudFormation**: Information about targets of blue/green
           deployments initiated by a CloudFormation stack update.

        :param deployment_id: The unique ID of a deployment.
        :param target_ids: The unique IDs of the deployment targets.
        :returns: BatchGetDeploymentTargetsOutput
        :raises InvalidDeploymentIdException:
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentNotStartedException:
        :raises DeploymentTargetIdRequiredException:
        :raises InvalidDeploymentTargetIdException:
        :raises DeploymentTargetDoesNotExistException:
        :raises DeploymentTargetListSizeExceededException:
        :raises InstanceDoesNotExistException:
        """
        raise NotImplementedError

    @handler("BatchGetDeployments")
    def batch_get_deployments(
        self, context: RequestContext, deployment_ids: DeploymentsList, **kwargs
    ) -> BatchGetDeploymentsOutput:
        """Gets information about one or more deployments. The maximum number of
        deployments that can be returned is 25.

        :param deployment_ids: A list of deployment IDs, separated by spaces.
        :returns: BatchGetDeploymentsOutput
        :raises DeploymentIdRequiredException:
        :raises InvalidDeploymentIdException:
        :raises BatchLimitExceededException:
        """
        raise NotImplementedError

    @handler("BatchGetOnPremisesInstances")
    def batch_get_on_premises_instances(
        self, context: RequestContext, instance_names: InstanceNameList, **kwargs
    ) -> BatchGetOnPremisesInstancesOutput:
        """Gets information about one or more on-premises instances. The maximum
        number of on-premises instances that can be returned is 25.

        :param instance_names: The names of the on-premises instances about which to get information.
        :returns: BatchGetOnPremisesInstancesOutput
        :raises InstanceNameRequiredException:
        :raises InvalidInstanceNameException:
        :raises BatchLimitExceededException:
        """
        raise NotImplementedError

    @handler("ContinueDeployment")
    def continue_deployment(
        self,
        context: RequestContext,
        deployment_id: DeploymentId | None = None,
        deployment_wait_type: DeploymentWaitType | None = None,
        **kwargs,
    ) -> None:
        """For a blue/green deployment, starts the process of rerouting traffic
        from instances in the original environment to instances in the
        replacement environment without waiting for a specified wait time to
        elapse. (Traffic rerouting, which is achieved by registering instances
        in the replacement environment with the load balancer, can start as soon
        as all instances have a status of Ready.)

        :param deployment_id: The unique ID of a blue/green deployment for which you want to start
        rerouting traffic to the replacement environment.
        :param deployment_wait_type: The status of the deployment's waiting period.
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentAlreadyCompletedException:
        :raises InvalidDeploymentIdException:
        :raises DeploymentIsNotInReadyStateException:
        :raises UnsupportedActionForDeploymentTypeException:
        :raises InvalidDeploymentWaitTypeException:
        :raises InvalidDeploymentStatusException:
        """
        raise NotImplementedError

    @handler("CreateApplication")
    def create_application(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        compute_platform: ComputePlatform | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateApplicationOutput:
        """Creates an application.

        :param application_name: The name of the application.
        :param compute_platform: The destination platform type for the deployment (``Lambda``,
        ``Server``, or ``ECS``).
        :param tags: The metadata that you apply to CodeDeploy applications to help you
        organize and categorize them.
        :returns: CreateApplicationOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationAlreadyExistsException:
        :raises ApplicationLimitExceededException:
        :raises InvalidComputePlatformException:
        :raises InvalidTagsToAddException:
        """
        raise NotImplementedError

    @handler("CreateDeployment")
    def create_deployment(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName | None = None,
        revision: RevisionLocation | None = None,
        deployment_config_name: DeploymentConfigName | None = None,
        description: Description | None = None,
        ignore_application_stop_failures: Boolean | None = None,
        target_instances: TargetInstances | None = None,
        auto_rollback_configuration: AutoRollbackConfiguration | None = None,
        update_outdated_instances_only: Boolean | None = None,
        file_exists_behavior: FileExistsBehavior | None = None,
        override_alarm_configuration: AlarmConfiguration | None = None,
        **kwargs,
    ) -> CreateDeploymentOutput:
        """Deploys an application revision through the specified deployment group.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param deployment_group_name: The name of the deployment group.
        :param revision: The type and location of the revision to deploy.
        :param deployment_config_name: The name of a deployment configuration associated with the user or
        Amazon Web Services account.
        :param description: A comment about the deployment.
        :param ignore_application_stop_failures: If true, then if an ``ApplicationStop``, ``BeforeBlockTraffic``, or
        ``AfterBlockTraffic`` deployment lifecycle event to an instance fails,
        then the deployment continues to the next deployment lifecycle event.
        :param target_instances: Information about the instances that belong to the replacement
        environment in a blue/green deployment.
        :param auto_rollback_configuration: Configuration information for an automatic rollback that is added when a
        deployment is created.
        :param update_outdated_instances_only: Indicates whether to deploy to all instances or only to instances that
        are not running the latest application revision.
        :param file_exists_behavior: Information about how CodeDeploy handles files that already exist in a
        deployment target location but weren't part of the previous successful
        deployment.
        :param override_alarm_configuration: Allows you to specify information about alarms associated with a
        deployment.
        :returns: CreateDeploymentOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises DeploymentGroupNameRequiredException:
        :raises InvalidDeploymentGroupNameException:
        :raises DeploymentGroupDoesNotExistException:
        :raises RevisionRequiredException:
        :raises RevisionDoesNotExistException:
        :raises InvalidRevisionException:
        :raises InvalidDeploymentConfigNameException:
        :raises DeploymentConfigDoesNotExistException:
        :raises DescriptionTooLongException:
        :raises DeploymentLimitExceededException:
        :raises InvalidTargetInstancesException:
        :raises InvalidAlarmConfigException:
        :raises AlarmsLimitExceededException:
        :raises InvalidAutoRollbackConfigException:
        :raises InvalidLoadBalancerInfoException:
        :raises InvalidFileExistsBehaviorException:
        :raises InvalidRoleException:
        :raises InvalidAutoScalingGroupException:
        :raises ThrottlingException:
        :raises InvalidUpdateOutdatedInstancesOnlyValueException:
        :raises InvalidIgnoreApplicationStopFailuresValueException:
        :raises InvalidGitHubAccountTokenException:
        :raises InvalidTrafficRoutingConfigurationException:
        """
        raise NotImplementedError

    @handler("CreateDeploymentConfig")
    def create_deployment_config(
        self,
        context: RequestContext,
        deployment_config_name: DeploymentConfigName,
        minimum_healthy_hosts: MinimumHealthyHosts | None = None,
        traffic_routing_config: TrafficRoutingConfig | None = None,
        compute_platform: ComputePlatform | None = None,
        zonal_config: ZonalConfig | None = None,
        **kwargs,
    ) -> CreateDeploymentConfigOutput:
        """Creates a deployment configuration.

        :param deployment_config_name: The name of the deployment configuration to create.
        :param minimum_healthy_hosts: The minimum number of healthy instances that should be available at any
        time during the deployment.
        :param traffic_routing_config: The configuration that specifies how the deployment traffic is routed.
        :param compute_platform: The destination platform type for the deployment (``Lambda``,
        ``Server``, or ``ECS``).
        :param zonal_config: Configure the ``ZonalConfig`` object if you want CodeDeploy to deploy
        your application to one `Availability
        Zone <https://docs.
        :returns: CreateDeploymentConfigOutput
        :raises InvalidDeploymentConfigNameException:
        :raises DeploymentConfigNameRequiredException:
        :raises DeploymentConfigAlreadyExistsException:
        :raises InvalidMinimumHealthyHostValueException:
        :raises DeploymentConfigLimitExceededException:
        :raises InvalidComputePlatformException:
        :raises InvalidTrafficRoutingConfigurationException:
        :raises InvalidZonalDeploymentConfigurationException:
        """
        raise NotImplementedError

    @handler("CreateDeploymentGroup")
    def create_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName,
        service_role_arn: Role,
        deployment_config_name: DeploymentConfigName | None = None,
        ec2_tag_filters: EC2TagFilterList | None = None,
        on_premises_instance_tag_filters: TagFilterList | None = None,
        auto_scaling_groups: AutoScalingGroupNameList | None = None,
        trigger_configurations: TriggerConfigList | None = None,
        alarm_configuration: AlarmConfiguration | None = None,
        auto_rollback_configuration: AutoRollbackConfiguration | None = None,
        outdated_instances_strategy: OutdatedInstancesStrategy | None = None,
        deployment_style: DeploymentStyle | None = None,
        blue_green_deployment_configuration: BlueGreenDeploymentConfiguration | None = None,
        load_balancer_info: LoadBalancerInfo | None = None,
        ec2_tag_set: EC2TagSet | None = None,
        ecs_services: ECSServiceList | None = None,
        on_premises_tag_set: OnPremisesTagSet | None = None,
        tags: TagList | None = None,
        termination_hook_enabled: NullableBoolean | None = None,
        **kwargs,
    ) -> CreateDeploymentGroupOutput:
        """Creates a deployment group to which application revisions are deployed.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param deployment_group_name: The name of a new deployment group for the specified application.
        :param service_role_arn: A service role Amazon Resource Name (ARN) that allows CodeDeploy to act
        on the user's behalf when interacting with Amazon Web Services services.
        :param deployment_config_name: If specified, the deployment configuration name can be either one of the
        predefined configurations provided with CodeDeploy or a custom
        deployment configuration that you create by calling the create
        deployment configuration operation.
        :param ec2_tag_filters: The Amazon EC2 tags on which to filter.
        :param on_premises_instance_tag_filters: The on-premises instance tags on which to filter.
        :param auto_scaling_groups: A list of associated Amazon EC2 Auto Scaling groups.
        :param trigger_configurations: Information about triggers to create when the deployment group is
        created.
        :param alarm_configuration: Information to add about Amazon CloudWatch alarms when the deployment
        group is created.
        :param auto_rollback_configuration: Configuration information for an automatic rollback that is added when a
        deployment group is created.
        :param outdated_instances_strategy: Indicates what happens when new Amazon EC2 instances are launched
        mid-deployment and do not receive the deployed application revision.
        :param deployment_style: Information about the type of deployment, in-place or blue/green, that
        you want to run and whether to route deployment traffic behind a load
        balancer.
        :param blue_green_deployment_configuration: Information about blue/green deployment options for a deployment group.
        :param load_balancer_info: Information about the load balancer used in a deployment.
        :param ec2_tag_set: Information about groups of tags applied to Amazon EC2 instances.
        :param ecs_services: The target Amazon ECS services in the deployment group.
        :param on_premises_tag_set: Information about groups of tags applied to on-premises instances.
        :param tags: The metadata that you apply to CodeDeploy deployment groups to help you
        organize and categorize them.
        :param termination_hook_enabled: This parameter only applies if you are using CodeDeploy with Amazon EC2
        Auto Scaling.
        :returns: CreateDeploymentGroupOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises DeploymentGroupNameRequiredException:
        :raises InvalidDeploymentGroupNameException:
        :raises DeploymentGroupAlreadyExistsException:
        :raises InvalidEC2TagException:
        :raises InvalidTagException:
        :raises InvalidAutoScalingGroupException:
        :raises InvalidDeploymentConfigNameException:
        :raises DeploymentConfigDoesNotExistException:
        :raises RoleRequiredException:
        :raises InvalidRoleException:
        :raises DeploymentGroupLimitExceededException:
        :raises LifecycleHookLimitExceededException:
        :raises InvalidTriggerConfigException:
        :raises TriggerTargetsLimitExceededException:
        :raises InvalidAlarmConfigException:
        :raises AlarmsLimitExceededException:
        :raises InvalidAutoRollbackConfigException:
        :raises InvalidLoadBalancerInfoException:
        :raises InvalidDeploymentStyleException:
        :raises InvalidBlueGreenDeploymentConfigurationException:
        :raises InvalidEC2TagCombinationException:
        :raises InvalidOnPremisesTagCombinationException:
        :raises TagSetListLimitExceededException:
        :raises InvalidInputException:
        :raises ThrottlingException:
        :raises InvalidECSServiceException:
        :raises InvalidTargetGroupPairException:
        :raises ECSServiceMappingLimitExceededException:
        :raises InvalidTagsToAddException:
        :raises InvalidTrafficRoutingConfigurationException:
        """
        raise NotImplementedError

    @handler("DeleteApplication")
    def delete_application(
        self, context: RequestContext, application_name: ApplicationName, **kwargs
    ) -> None:
        """Deletes an application.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises InvalidRoleException:
        """
        raise NotImplementedError

    @handler("DeleteDeploymentConfig")
    def delete_deployment_config(
        self, context: RequestContext, deployment_config_name: DeploymentConfigName, **kwargs
    ) -> None:
        """Deletes a deployment configuration.

        A deployment configuration cannot be deleted if it is currently in use.
        Predefined configurations cannot be deleted.

        :param deployment_config_name: The name of a deployment configuration associated with the user or
        Amazon Web Services account.
        :raises InvalidDeploymentConfigNameException:
        :raises DeploymentConfigNameRequiredException:
        :raises DeploymentConfigInUseException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteDeploymentGroup")
    def delete_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName,
        **kwargs,
    ) -> DeleteDeploymentGroupOutput:
        """Deletes a deployment group.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param deployment_group_name: The name of a deployment group for the specified application.
        :returns: DeleteDeploymentGroupOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises DeploymentGroupNameRequiredException:
        :raises InvalidDeploymentGroupNameException:
        :raises InvalidRoleException:
        """
        raise NotImplementedError

    @handler("DeleteGitHubAccountToken")
    def delete_git_hub_account_token(
        self, context: RequestContext, token_name: GitHubAccountTokenName | None = None, **kwargs
    ) -> DeleteGitHubAccountTokenOutput:
        """Deletes a GitHub account connection.

        :param token_name: The name of the GitHub account connection to delete.
        :returns: DeleteGitHubAccountTokenOutput
        :raises GitHubAccountTokenNameRequiredException:
        :raises GitHubAccountTokenDoesNotExistException:
        :raises InvalidGitHubAccountTokenNameException:
        :raises ResourceValidationException:
        :raises OperationNotSupportedException:
        """
        raise NotImplementedError

    @handler("DeleteResourcesByExternalId")
    def delete_resources_by_external_id(
        self, context: RequestContext, external_id: ExternalId | None = None, **kwargs
    ) -> DeleteResourcesByExternalIdOutput:
        """Deletes resources linked to an external ID. This action only applies if
        you have configured blue/green deployments through CloudFormation.

        It is not necessary to call this action directly. CloudFormation calls
        it on your behalf when it needs to delete stack resources. This action
        is offered publicly in case you need to delete resources to comply with
        General Data Protection Regulation (GDPR) requirements.

        :param external_id: The unique ID of an external resource (for example, a CloudFormation
        stack ID) that is linked to one or more CodeDeploy resources.
        :returns: DeleteResourcesByExternalIdOutput
        """
        raise NotImplementedError

    @handler("DeregisterOnPremisesInstance")
    def deregister_on_premises_instance(
        self, context: RequestContext, instance_name: InstanceName, **kwargs
    ) -> None:
        """Deregisters an on-premises instance.

        :param instance_name: The name of the on-premises instance to deregister.
        :raises InstanceNameRequiredException:
        :raises InvalidInstanceNameException:
        """
        raise NotImplementedError

    @handler("GetApplication")
    def get_application(
        self, context: RequestContext, application_name: ApplicationName, **kwargs
    ) -> GetApplicationOutput:
        """Gets information about an application.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :returns: GetApplicationOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        """
        raise NotImplementedError

    @handler("GetApplicationRevision")
    def get_application_revision(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        revision: RevisionLocation,
        **kwargs,
    ) -> GetApplicationRevisionOutput:
        """Gets information about an application revision.

        :param application_name: The name of the application that corresponds to the revision.
        :param revision: Information about the application revision to get, including type and
        location.
        :returns: GetApplicationRevisionOutput
        :raises ApplicationDoesNotExistException:
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises RevisionDoesNotExistException:
        :raises RevisionRequiredException:
        :raises InvalidRevisionException:
        """
        raise NotImplementedError

    @handler("GetDeployment")
    def get_deployment(
        self, context: RequestContext, deployment_id: DeploymentId, **kwargs
    ) -> GetDeploymentOutput:
        """Gets information about a deployment.

        The ``content`` property of the ``appSpecContent`` object in the
        returned revision is always null. Use ``GetApplicationRevision`` and the
        ``sha256`` property of the returned ``appSpecContent`` object to get the
        content of the deployment’s AppSpec file.

        :param deployment_id: The unique ID of a deployment associated with the user or Amazon Web
        Services account.
        :returns: GetDeploymentOutput
        :raises DeploymentIdRequiredException:
        :raises InvalidDeploymentIdException:
        :raises DeploymentDoesNotExistException:
        """
        raise NotImplementedError

    @handler("GetDeploymentConfig")
    def get_deployment_config(
        self, context: RequestContext, deployment_config_name: DeploymentConfigName, **kwargs
    ) -> GetDeploymentConfigOutput:
        """Gets information about a deployment configuration.

        :param deployment_config_name: The name of a deployment configuration associated with the user or
        Amazon Web Services account.
        :returns: GetDeploymentConfigOutput
        :raises InvalidDeploymentConfigNameException:
        :raises DeploymentConfigNameRequiredException:
        :raises DeploymentConfigDoesNotExistException:
        :raises InvalidComputePlatformException:
        """
        raise NotImplementedError

    @handler("GetDeploymentGroup")
    def get_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        deployment_group_name: DeploymentGroupName,
        **kwargs,
    ) -> GetDeploymentGroupOutput:
        """Gets information about a deployment group.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param deployment_group_name: The name of a deployment group for the specified application.
        :returns: GetDeploymentGroupOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises DeploymentGroupNameRequiredException:
        :raises InvalidDeploymentGroupNameException:
        :raises DeploymentGroupDoesNotExistException:
        :raises DeploymentConfigDoesNotExistException:
        """
        raise NotImplementedError

    @handler("GetDeploymentInstance")
    def get_deployment_instance(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        instance_id: InstanceId,
        **kwargs,
    ) -> GetDeploymentInstanceOutput:
        """Gets information about an instance as part of a deployment.

        :param deployment_id: The unique ID of a deployment.
        :param instance_id: The unique ID of an instance in the deployment group.
        :returns: GetDeploymentInstanceOutput
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises InstanceIdRequiredException:
        :raises InvalidDeploymentIdException:
        :raises InstanceDoesNotExistException:
        :raises InvalidInstanceNameException:
        :raises InvalidComputePlatformException:
        """
        raise NotImplementedError

    @handler("GetDeploymentTarget")
    def get_deployment_target(
        self, context: RequestContext, deployment_id: DeploymentId, target_id: TargetId, **kwargs
    ) -> GetDeploymentTargetOutput:
        """Returns information about a deployment target.

        :param deployment_id: The unique ID of a deployment.
        :param target_id: The unique ID of a deployment target.
        :returns: GetDeploymentTargetOutput
        :raises InvalidDeploymentIdException:
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentNotStartedException:
        :raises DeploymentTargetIdRequiredException:
        :raises InvalidDeploymentTargetIdException:
        :raises DeploymentTargetDoesNotExistException:
        :raises InvalidInstanceNameException:
        """
        raise NotImplementedError

    @handler("GetOnPremisesInstance")
    def get_on_premises_instance(
        self, context: RequestContext, instance_name: InstanceName, **kwargs
    ) -> GetOnPremisesInstanceOutput:
        """Gets information about an on-premises instance.

        :param instance_name: The name of the on-premises instance about which to get information.
        :returns: GetOnPremisesInstanceOutput
        :raises InstanceNameRequiredException:
        :raises InstanceNotRegisteredException:
        :raises InvalidInstanceNameException:
        """
        raise NotImplementedError

    @handler("ListApplicationRevisions")
    def list_application_revisions(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        sort_by: ApplicationRevisionSortBy | None = None,
        sort_order: SortOrder | None = None,
        s3_bucket: S3Bucket | None = None,
        s3_key_prefix: S3Key | None = None,
        deployed: ListStateFilterAction | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListApplicationRevisionsOutput:
        """Lists information about revisions for an application.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param sort_by: The column name to use to sort the list results:

        -  ``registerTime``: Sort by the time the revisions were registered with
           CodeDeploy.
        :param sort_order: The order in which to sort the list results:

        -  ``ascending``: ascending order.
        :param s3_bucket: An Amazon S3 bucket name to limit the search for revisions.
        :param s3_key_prefix: A key prefix for the set of Amazon S3 objects to limit the search for
        revisions.
        :param deployed: Whether to list revisions based on whether the revision is the target
        revision of a deployment group:

        -  ``include``: List revisions that are target revisions of a deployment
           group.
        :param next_token: An identifier returned from the previous ``ListApplicationRevisions``
        call.
        :returns: ListApplicationRevisionsOutput
        :raises ApplicationDoesNotExistException:
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises InvalidSortByException:
        :raises InvalidSortOrderException:
        :raises InvalidBucketNameFilterException:
        :raises InvalidKeyPrefixFilterException:
        :raises BucketNameFilterRequiredException:
        :raises InvalidDeployedStateFilterException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListApplications")
    def list_applications(
        self, context: RequestContext, next_token: NextToken | None = None, **kwargs
    ) -> ListApplicationsOutput:
        """Lists the applications registered with the user or Amazon Web Services
        account.

        :param next_token: An identifier returned from the previous list applications call.
        :returns: ListApplicationsOutput
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListDeploymentConfigs")
    def list_deployment_configs(
        self, context: RequestContext, next_token: NextToken | None = None, **kwargs
    ) -> ListDeploymentConfigsOutput:
        """Lists the deployment configurations with the user or Amazon Web Services
        account.

        :param next_token: An identifier returned from the previous ``ListDeploymentConfigs`` call.
        :returns: ListDeploymentConfigsOutput
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListDeploymentGroups")
    def list_deployment_groups(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListDeploymentGroupsOutput:
        """Lists the deployment groups for an application registered with the
        Amazon Web Services user or Amazon Web Services account.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param next_token: An identifier returned from the previous list deployment groups call.
        :returns: ListDeploymentGroupsOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListDeploymentInstances")
    def list_deployment_instances(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        next_token: NextToken | None = None,
        instance_status_filter: InstanceStatusList | None = None,
        instance_type_filter: InstanceTypeList | None = None,
        **kwargs,
    ) -> ListDeploymentInstancesOutput:
        """The newer ``BatchGetDeploymentTargets`` should be used instead because
        it works with all compute types. ``ListDeploymentInstances`` throws an
        exception if it is used with a compute platform other than
        EC2/On-premises or Lambda.

        Lists the instance for a deployment associated with the user or Amazon
        Web Services account.

        :param deployment_id: The unique ID of a deployment.
        :param next_token: An identifier returned from the previous list deployment instances call.
        :param instance_status_filter: A subset of instances to list by status:

        -  ``Pending``: Include those instances with pending deployments.
        :param instance_type_filter: The set of instances in a blue/green deployment, either those in the
        original environment ("BLUE") or those in the replacement environment
        ("GREEN"), for which you want to view instance information.
        :returns: ListDeploymentInstancesOutput
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentNotStartedException:
        :raises InvalidNextTokenException:
        :raises InvalidDeploymentIdException:
        :raises InvalidInstanceStatusException:
        :raises InvalidInstanceTypeException:
        :raises InvalidDeploymentInstanceTypeException:
        :raises InvalidTargetFilterNameException:
        :raises InvalidComputePlatformException:
        """
        raise NotImplementedError

    @handler("ListDeploymentTargets")
    def list_deployment_targets(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        next_token: NextToken | None = None,
        target_filters: TargetFilters | None = None,
        **kwargs,
    ) -> ListDeploymentTargetsOutput:
        """Returns an array of target IDs that are associated a deployment.

        :param deployment_id: The unique ID of a deployment.
        :param next_token: A token identifier returned from the previous ``ListDeploymentTargets``
        call.
        :param target_filters: A key used to filter the returned targets.
        :returns: ListDeploymentTargetsOutput
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentNotStartedException:
        :raises InvalidNextTokenException:
        :raises InvalidDeploymentIdException:
        :raises InvalidInstanceStatusException:
        :raises InvalidInstanceTypeException:
        :raises InvalidDeploymentInstanceTypeException:
        :raises InvalidTargetFilterNameException:
        """
        raise NotImplementedError

    @handler("ListDeployments")
    def list_deployments(
        self,
        context: RequestContext,
        application_name: ApplicationName | None = None,
        deployment_group_name: DeploymentGroupName | None = None,
        external_id: ExternalId | None = None,
        include_only_statuses: DeploymentStatusList | None = None,
        create_time_range: TimeRange | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListDeploymentsOutput:
        """Lists the deployments in a deployment group for an application
        registered with the user or Amazon Web Services account.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param deployment_group_name: The name of a deployment group for the specified application.
        :param external_id: The unique ID of an external resource for returning deployments linked
        to the external resource.
        :param include_only_statuses: A subset of deployments to list by status:

        -  ``Created``: Include created deployments in the resulting list.
        :param create_time_range: A time range (start and end) for returning a subset of the list of
        deployments.
        :param next_token: An identifier returned from the previous list deployments call.
        :returns: ListDeploymentsOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises InvalidDeploymentGroupNameException:
        :raises DeploymentGroupDoesNotExistException:
        :raises DeploymentGroupNameRequiredException:
        :raises InvalidTimeRangeException:
        :raises InvalidDeploymentStatusException:
        :raises InvalidNextTokenException:
        :raises InvalidExternalIdException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListGitHubAccountTokenNames")
    def list_git_hub_account_token_names(
        self, context: RequestContext, next_token: NextToken | None = None, **kwargs
    ) -> ListGitHubAccountTokenNamesOutput:
        """Lists the names of stored connections to GitHub accounts.

        :param next_token: An identifier returned from the previous ``ListGitHubAccountTokenNames``
        call.
        :returns: ListGitHubAccountTokenNamesOutput
        :raises InvalidNextTokenException:
        :raises ResourceValidationException:
        :raises OperationNotSupportedException:
        """
        raise NotImplementedError

    @handler("ListOnPremisesInstances")
    def list_on_premises_instances(
        self,
        context: RequestContext,
        registration_status: RegistrationStatus | None = None,
        tag_filters: TagFilterList | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListOnPremisesInstancesOutput:
        """Gets a list of names for one or more on-premises instances.

        Unless otherwise specified, both registered and deregistered on-premises
        instance names are listed. To list only registered or deregistered
        on-premises instance names, use the registration status parameter.

        :param registration_status: The registration status of the on-premises instances:

        -  ``Deregistered``: Include deregistered on-premises instances in the
           resulting list.
        :param tag_filters: The on-premises instance tags that are used to restrict the on-premises
        instance names returned.
        :param next_token: An identifier returned from the previous list on-premises instances
        call.
        :returns: ListOnPremisesInstancesOutput
        :raises InvalidRegistrationStatusException:
        :raises InvalidTagFilterException:
        :raises InvalidNextTokenException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_arn: Arn,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListTagsForResourceOutput:
        """Returns a list of tags for the resource identified by a specified Amazon
        Resource Name (ARN). Tags are used to organize and categorize your
        CodeDeploy resources.

        :param resource_arn: The ARN of a CodeDeploy resource.
        :param next_token: An identifier returned from the previous ``ListTagsForResource`` call.
        :returns: ListTagsForResourceOutput
        :raises ArnNotSupportedException:
        :raises InvalidArnException:
        :raises ResourceArnRequiredException:
        """
        raise NotImplementedError

    @handler("PutLifecycleEventHookExecutionStatus")
    def put_lifecycle_event_hook_execution_status(
        self,
        context: RequestContext,
        deployment_id: DeploymentId | None = None,
        lifecycle_event_hook_execution_id: LifecycleEventHookExecutionId | None = None,
        status: LifecycleEventStatus | None = None,
        **kwargs,
    ) -> PutLifecycleEventHookExecutionStatusOutput:
        """Sets the result of a Lambda validation function. The function validates
        lifecycle hooks during a deployment that uses the Lambda or Amazon ECS
        compute platform. For Lambda deployments, the available lifecycle hooks
        are ``BeforeAllowTraffic`` and ``AfterAllowTraffic``. For Amazon ECS
        deployments, the available lifecycle hooks are ``BeforeInstall``,
        ``AfterInstall``, ``AfterAllowTestTraffic``, ``BeforeAllowTraffic``, and
        ``AfterAllowTraffic``. Lambda validation functions return ``Succeeded``
        or ``Failed``. For more information, see `AppSpec 'hooks' Section for an
        Lambda
        Deployment <https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-lambda>`__
        and `AppSpec 'hooks' Section for an Amazon ECS
        Deployment <https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-ecs>`__.

        :param deployment_id: The unique ID of a deployment.
        :param lifecycle_event_hook_execution_id: The execution ID of a deployment's lifecycle hook.
        :param status: The result of a Lambda function that validates a deployment lifecycle
        event.
        :returns: PutLifecycleEventHookExecutionStatusOutput
        :raises InvalidLifecycleEventHookExecutionStatusException:
        :raises InvalidLifecycleEventHookExecutionIdException:
        :raises LifecycleEventAlreadyCompletedException:
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises InvalidDeploymentIdException:
        :raises UnsupportedActionForDeploymentTypeException:
        """
        raise NotImplementedError

    @handler("RegisterApplicationRevision")
    def register_application_revision(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        revision: RevisionLocation,
        description: Description | None = None,
        **kwargs,
    ) -> None:
        """Registers with CodeDeploy a revision for the specified application.

        :param application_name: The name of an CodeDeploy application associated with the user or Amazon
        Web Services account.
        :param revision: Information about the application revision to register, including type
        and location.
        :param description: A comment about the revision.
        :raises ApplicationDoesNotExistException:
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises DescriptionTooLongException:
        :raises RevisionRequiredException:
        :raises InvalidRevisionException:
        """
        raise NotImplementedError

    @handler("RegisterOnPremisesInstance")
    def register_on_premises_instance(
        self,
        context: RequestContext,
        instance_name: InstanceName,
        iam_session_arn: IamSessionArn | None = None,
        iam_user_arn: IamUserArn | None = None,
        **kwargs,
    ) -> None:
        """Registers an on-premises instance.

        Only one IAM ARN (an IAM session ARN or IAM user ARN) is supported in
        the request. You cannot use both.

        :param instance_name: The name of the on-premises instance to register.
        :param iam_session_arn: The ARN of the IAM session to associate with the on-premises instance.
        :param iam_user_arn: The ARN of the user to associate with the on-premises instance.
        :raises InstanceNameAlreadyRegisteredException:
        :raises IamArnRequiredException:
        :raises IamSessionArnAlreadyRegisteredException:
        :raises IamUserArnAlreadyRegisteredException:
        :raises InstanceNameRequiredException:
        :raises IamUserArnRequiredException:
        :raises InvalidInstanceNameException:
        :raises InvalidIamSessionArnException:
        :raises InvalidIamUserArnException:
        :raises MultipleIamArnsProvidedException:
        """
        raise NotImplementedError

    @handler("RemoveTagsFromOnPremisesInstances")
    def remove_tags_from_on_premises_instances(
        self, context: RequestContext, tags: TagList, instance_names: InstanceNameList, **kwargs
    ) -> None:
        """Removes one or more tags from one or more on-premises instances.

        :param tags: The tag key-value pairs to remove from the on-premises instances.
        :param instance_names: The names of the on-premises instances from which to remove tags.
        :raises InstanceNameRequiredException:
        :raises InvalidInstanceNameException:
        :raises TagRequiredException:
        :raises InvalidTagException:
        :raises TagLimitExceededException:
        :raises InstanceLimitExceededException:
        :raises InstanceNotRegisteredException:
        """
        raise NotImplementedError

    @handler("SkipWaitTimeForInstanceTermination")
    def skip_wait_time_for_instance_termination(
        self, context: RequestContext, deployment_id: DeploymentId | None = None, **kwargs
    ) -> None:
        """In a blue/green deployment, overrides any specified wait time and starts
        terminating instances immediately after the traffic routing is complete.

        :param deployment_id: The unique ID of a blue/green deployment for which you want to skip the
        instance termination wait time.
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentAlreadyCompletedException:
        :raises InvalidDeploymentIdException:
        :raises DeploymentNotStartedException:
        :raises UnsupportedActionForDeploymentTypeException:
        """
        raise NotImplementedError

    @handler("StopDeployment")
    def stop_deployment(
        self,
        context: RequestContext,
        deployment_id: DeploymentId,
        auto_rollback_enabled: NullableBoolean | None = None,
        **kwargs,
    ) -> StopDeploymentOutput:
        """Attempts to stop an ongoing deployment.

        :param deployment_id: The unique ID of a deployment.
        :param auto_rollback_enabled: Indicates, when a deployment is stopped, whether instances that have
        been updated should be rolled back to the previous version of the
        application revision.
        :returns: StopDeploymentOutput
        :raises DeploymentIdRequiredException:
        :raises DeploymentDoesNotExistException:
        :raises DeploymentGroupDoesNotExistException:
        :raises DeploymentAlreadyCompletedException:
        :raises InvalidDeploymentIdException:
        :raises UnsupportedActionForDeploymentTypeException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: Arn, tags: TagList, **kwargs
    ) -> TagResourceOutput:
        """Associates the list of tags in the input ``Tags`` parameter with the
        resource identified by the ``ResourceArn`` input parameter.

        :param resource_arn: The ARN of a resource, such as a CodeDeploy application or deployment
        group.
        :param tags: A list of tags that ``TagResource`` associates with a resource.
        :returns: TagResourceOutput
        :raises ResourceArnRequiredException:
        :raises ApplicationDoesNotExistException:
        :raises DeploymentGroupDoesNotExistException:
        :raises DeploymentConfigDoesNotExistException:
        :raises TagRequiredException:
        :raises InvalidTagsToAddException:
        :raises ArnNotSupportedException:
        :raises InvalidArnException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: Arn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceOutput:
        """Disassociates a resource from a list of tags. The resource is identified
        by the ``ResourceArn`` input parameter. The tags are identified by the
        list of keys in the ``TagKeys`` input parameter.

        :param resource_arn: The Amazon Resource Name (ARN) that specifies from which resource to
        disassociate the tags with the keys in the ``TagKeys`` input parameter.
        :param tag_keys: A list of keys of ``Tag`` objects.
        :returns: UntagResourceOutput
        :raises ResourceArnRequiredException:
        :raises ApplicationDoesNotExistException:
        :raises DeploymentGroupDoesNotExistException:
        :raises DeploymentConfigDoesNotExistException:
        :raises TagRequiredException:
        :raises InvalidTagsToAddException:
        :raises ArnNotSupportedException:
        :raises InvalidArnException:
        """
        raise NotImplementedError

    @handler("UpdateApplication")
    def update_application(
        self,
        context: RequestContext,
        application_name: ApplicationName | None = None,
        new_application_name: ApplicationName | None = None,
        **kwargs,
    ) -> None:
        """Changes the name of an application.

        :param application_name: The current name of the application you want to change.
        :param new_application_name: The new name to give the application.
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationAlreadyExistsException:
        :raises ApplicationDoesNotExistException:
        """
        raise NotImplementedError

    @handler("UpdateDeploymentGroup")
    def update_deployment_group(
        self,
        context: RequestContext,
        application_name: ApplicationName,
        current_deployment_group_name: DeploymentGroupName,
        new_deployment_group_name: DeploymentGroupName | None = None,
        deployment_config_name: DeploymentConfigName | None = None,
        ec2_tag_filters: EC2TagFilterList | None = None,
        on_premises_instance_tag_filters: TagFilterList | None = None,
        auto_scaling_groups: AutoScalingGroupNameList | None = None,
        service_role_arn: Role | None = None,
        trigger_configurations: TriggerConfigList | None = None,
        alarm_configuration: AlarmConfiguration | None = None,
        auto_rollback_configuration: AutoRollbackConfiguration | None = None,
        outdated_instances_strategy: OutdatedInstancesStrategy | None = None,
        deployment_style: DeploymentStyle | None = None,
        blue_green_deployment_configuration: BlueGreenDeploymentConfiguration | None = None,
        load_balancer_info: LoadBalancerInfo | None = None,
        ec2_tag_set: EC2TagSet | None = None,
        ecs_services: ECSServiceList | None = None,
        on_premises_tag_set: OnPremisesTagSet | None = None,
        termination_hook_enabled: NullableBoolean | None = None,
        **kwargs,
    ) -> UpdateDeploymentGroupOutput:
        """Changes information about a deployment group.

        :param application_name: The application name that corresponds to the deployment group to update.
        :param current_deployment_group_name: The current name of the deployment group.
        :param new_deployment_group_name: The new name of the deployment group, if you want to change it.
        :param deployment_config_name: The replacement deployment configuration name to use, if you want to
        change it.
        :param ec2_tag_filters: The replacement set of Amazon EC2 tags on which to filter, if you want
        to change them.
        :param on_premises_instance_tag_filters: The replacement set of on-premises instance tags on which to filter, if
        you want to change them.
        :param auto_scaling_groups: The replacement list of Auto Scaling groups to be included in the
        deployment group, if you want to change them.
        :param service_role_arn: A replacement ARN for the service role, if you want to change it.
        :param trigger_configurations: Information about triggers to change when the deployment group is
        updated.
        :param alarm_configuration: Information to add or change about Amazon CloudWatch alarms when the
        deployment group is updated.
        :param auto_rollback_configuration: Information for an automatic rollback configuration that is added or
        changed when a deployment group is updated.
        :param outdated_instances_strategy: Indicates what happens when new Amazon EC2 instances are launched
        mid-deployment and do not receive the deployed application revision.
        :param deployment_style: Information about the type of deployment, either in-place or blue/green,
        you want to run and whether to route deployment traffic behind a load
        balancer.
        :param blue_green_deployment_configuration: Information about blue/green deployment options for a deployment group.
        :param load_balancer_info: Information about the load balancer used in a deployment.
        :param ec2_tag_set: Information about groups of tags applied to on-premises instances.
        :param ecs_services: The target Amazon ECS services in the deployment group.
        :param on_premises_tag_set: Information about an on-premises instance tag set.
        :param termination_hook_enabled: This parameter only applies if you are using CodeDeploy with Amazon EC2
        Auto Scaling.
        :returns: UpdateDeploymentGroupOutput
        :raises ApplicationNameRequiredException:
        :raises InvalidApplicationNameException:
        :raises ApplicationDoesNotExistException:
        :raises InvalidDeploymentGroupNameException:
        :raises DeploymentGroupAlreadyExistsException:
        :raises DeploymentGroupNameRequiredException:
        :raises DeploymentGroupDoesNotExistException:
        :raises InvalidEC2TagException:
        :raises InvalidTagException:
        :raises InvalidAutoScalingGroupException:
        :raises InvalidDeploymentConfigNameException:
        :raises DeploymentConfigDoesNotExistException:
        :raises InvalidRoleException:
        :raises LifecycleHookLimitExceededException:
        :raises InvalidTriggerConfigException:
        :raises TriggerTargetsLimitExceededException:
        :raises InvalidAlarmConfigException:
        :raises AlarmsLimitExceededException:
        :raises InvalidAutoRollbackConfigException:
        :raises InvalidLoadBalancerInfoException:
        :raises InvalidDeploymentStyleException:
        :raises InvalidBlueGreenDeploymentConfigurationException:
        :raises InvalidEC2TagCombinationException:
        :raises InvalidOnPremisesTagCombinationException:
        :raises TagSetListLimitExceededException:
        :raises InvalidInputException:
        :raises ThrottlingException:
        :raises InvalidECSServiceException:
        :raises InvalidTargetGroupPairException:
        :raises ECSServiceMappingLimitExceededException:
        :raises InvalidTrafficRoutingConfigurationException:
        """
        raise NotImplementedError
