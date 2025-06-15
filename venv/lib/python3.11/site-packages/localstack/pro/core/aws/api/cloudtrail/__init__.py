from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccountId = str
Boolean = bool
ChannelArn = str
ChannelName = str
DashboardArn = str
DashboardName = str
DeliveryS3Uri = str
Double = float
ErrorCode = str
ErrorMessage = str
EventDataStoreArn = str
EventDataStoreKmsKeyId = str
EventDataStoreName = str
EventName = str
EventSource = str
FederationRoleArn = str
InsightsMetricMaxResults = int
InsightsMetricNextToken = str
InsightsMetricPeriod = int
Integer = int
ListChannelsMaxResultsCount = int
ListDashboardsMaxResultsCount = int
ListEventDataStoresMaxResultsCount = int
ListImportFailuresMaxResultsCount = int
ListImportsMaxResultsCount = int
ListQueriesMaxResultsCount = int
Location = str
LookupAttributeValue = str
MaxQueryResults = int
MaxResults = int
NextToken = str
OperatorTargetListMember = str
OperatorValue = str
PaginationToken = str
PartitionKeyName = str
PartitionKeyType = str
Prompt = str
QueryAlias = str
QueryParameter = str
QueryParameterKey = str
QueryParameterValue = str
QueryResultKey = str
QueryResultValue = str
QueryStatement = str
RefreshId = str
RefreshScheduleFrequencyValue = int
ResourceArn = str
ResourcePolicy = str
RetentionPeriod = int
SampleQueryDescription = str
SampleQueryName = str
SampleQueryRelevance = float
SampleQuerySQL = str
SearchSampleQueriesMaxResults = int
SearchSampleQueriesSearchPhrase = str
SelectorField = str
SelectorName = str
Source = str
String = str
TagKey = str
TagValue = str
TerminationProtectionEnabled = bool
TimeOfDay = str
UUID = str
ViewPropertiesKey = str
ViewPropertiesValue = str


class BillingMode(StrEnum):
    EXTENDABLE_RETENTION_PRICING = "EXTENDABLE_RETENTION_PRICING"
    FIXED_RETENTION_PRICING = "FIXED_RETENTION_PRICING"


class DashboardStatus(StrEnum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    UPDATING = "UPDATING"
    UPDATED = "UPDATED"
    DELETING = "DELETING"


class DashboardType(StrEnum):
    MANAGED = "MANAGED"
    CUSTOM = "CUSTOM"


class DeliveryStatus(StrEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    FAILED_SIGNING_FILE = "FAILED_SIGNING_FILE"
    PENDING = "PENDING"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    ACCESS_DENIED = "ACCESS_DENIED"
    ACCESS_DENIED_SIGNING_FILE = "ACCESS_DENIED_SIGNING_FILE"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"


class DestinationType(StrEnum):
    EVENT_DATA_STORE = "EVENT_DATA_STORE"
    AWS_SERVICE = "AWS_SERVICE"


class EventCategory(StrEnum):
    insight = "insight"


class EventDataStoreStatus(StrEnum):
    CREATED = "CREATED"
    ENABLED = "ENABLED"
    PENDING_DELETION = "PENDING_DELETION"
    STARTING_INGESTION = "STARTING_INGESTION"
    STOPPING_INGESTION = "STOPPING_INGESTION"
    STOPPED_INGESTION = "STOPPED_INGESTION"


class FederationStatus(StrEnum):
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


class ImportFailureStatus(StrEnum):
    FAILED = "FAILED"
    RETRY = "RETRY"
    SUCCEEDED = "SUCCEEDED"


class ImportStatus(StrEnum):
    INITIALIZING = "INITIALIZING"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    STOPPED = "STOPPED"
    COMPLETED = "COMPLETED"


class InsightType(StrEnum):
    ApiCallRateInsight = "ApiCallRateInsight"
    ApiErrorRateInsight = "ApiErrorRateInsight"


class InsightsMetricDataType(StrEnum):
    FillWithZeros = "FillWithZeros"
    NonZeroData = "NonZeroData"


class LookupAttributeKey(StrEnum):
    EventId = "EventId"
    EventName = "EventName"
    ReadOnly = "ReadOnly"
    Username = "Username"
    ResourceType = "ResourceType"
    ResourceName = "ResourceName"
    EventSource = "EventSource"
    AccessKeyId = "AccessKeyId"


class MaxEventSize(StrEnum):
    Standard = "Standard"
    Large = "Large"


class QueryStatus(StrEnum):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    TIMED_OUT = "TIMED_OUT"


class ReadWriteType(StrEnum):
    ReadOnly = "ReadOnly"
    WriteOnly = "WriteOnly"
    All = "All"


class RefreshScheduleFrequencyUnit(StrEnum):
    HOURS = "HOURS"
    DAYS = "DAYS"


class RefreshScheduleStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Type(StrEnum):
    TagContext = "TagContext"
    RequestContext = "RequestContext"


class AccessDeniedException(ServiceException):
    """You do not have sufficient access to perform this action."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class AccountHasOngoingImportException(ServiceException):
    """This exception is thrown when you start a new import and a previous
    import is still in progress.
    """

    code: str = "AccountHasOngoingImportException"
    sender_fault: bool = False
    status_code: int = 400


class AccountNotFoundException(ServiceException):
    """This exception is thrown when the specified account is not found or not
    part of an organization.
    """

    code: str = "AccountNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class AccountNotRegisteredException(ServiceException):
    """This exception is thrown when the specified account is not registered as
    the CloudTrail delegated administrator.
    """

    code: str = "AccountNotRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class AccountRegisteredException(ServiceException):
    """This exception is thrown when the account is already registered as the
    CloudTrail delegated administrator.
    """

    code: str = "AccountRegisteredException"
    sender_fault: bool = False
    status_code: int = 400


class CannotDelegateManagementAccountException(ServiceException):
    """This exception is thrown when the management account of an organization
    is registered as the CloudTrail delegated administrator.
    """

    code: str = "CannotDelegateManagementAccountException"
    sender_fault: bool = False
    status_code: int = 400


class ChannelARNInvalidException(ServiceException):
    """This exception is thrown when the specified value of ``ChannelARN`` is
    not valid.
    """

    code: str = "ChannelARNInvalidException"
    sender_fault: bool = False
    status_code: int = 400


class ChannelAlreadyExistsException(ServiceException):
    """This exception is thrown when the provided channel already exists."""

    code: str = "ChannelAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ChannelExistsForEDSException(ServiceException):
    """This exception is thrown when the specified event data store cannot yet
    be deleted because it is in use by a channel.
    """

    code: str = "ChannelExistsForEDSException"
    sender_fault: bool = False
    status_code: int = 400


class ChannelMaxLimitExceededException(ServiceException):
    """This exception is thrown when the maximum number of channels limit is
    exceeded.
    """

    code: str = "ChannelMaxLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ChannelNotFoundException(ServiceException):
    """This exception is thrown when CloudTrail cannot find the specified
    channel.
    """

    code: str = "ChannelNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class CloudTrailARNInvalidException(ServiceException):
    """This exception is thrown when an operation is called with an ARN that is
    not valid.

    The following is the format of a trail ARN:
    ``arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail``

    The following is the format of an event data store ARN:
    ``arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE``

    The following is the format of a dashboard ARN:
    ``arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash``

    The following is the format of a channel ARN:
    ``arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890``
    """

    code: str = "CloudTrailARNInvalidException"
    sender_fault: bool = False
    status_code: int = 400


class CloudTrailAccessNotEnabledException(ServiceException):
    """This exception is thrown when trusted access has not been enabled
    between CloudTrail and Organizations. For more information, see `How to
    enable or disable trusted
    access <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access>`__
    in the *Organizations User Guide* and `Prepare For Creating a Trail For
    Your
    Organization <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html>`__
    in the *CloudTrail User Guide*.
    """

    code: str = "CloudTrailAccessNotEnabledException"
    sender_fault: bool = False
    status_code: int = 400


class CloudTrailInvalidClientTokenIdException(ServiceException):
    """This exception is thrown when a call results in the
    ``InvalidClientTokenId`` error code. This can occur when you are
    creating or updating a trail to send notifications to an Amazon SNS
    topic that is in a suspended Amazon Web Services account.
    """

    code: str = "CloudTrailInvalidClientTokenIdException"
    sender_fault: bool = False
    status_code: int = 400


class CloudWatchLogsDeliveryUnavailableException(ServiceException):
    """Cannot set a CloudWatch Logs delivery for this Region."""

    code: str = "CloudWatchLogsDeliveryUnavailableException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentModificationException(ServiceException):
    """You are trying to update a resource when another request is in progress.
    Allow sufficient wait time for the previous request to complete, then
    retry your request.
    """

    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """This exception is thrown when the specified resource is not ready for an
    operation. This can occur when you try to run an operation on a resource
    before CloudTrail has time to fully load the resource, or because
    another operation is modifying the resource. If this exception occurs,
    wait a few minutes, and then try the operation again.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class DelegatedAdminAccountLimitExceededException(ServiceException):
    """This exception is thrown when the maximum number of CloudTrail delegated
    administrators is reached.
    """

    code: str = "DelegatedAdminAccountLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreARNInvalidException(ServiceException):
    """The specified event data store ARN is not valid or does not map to an
    event data store in your account.
    """

    code: str = "EventDataStoreARNInvalidException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreAlreadyExistsException(ServiceException):
    """An event data store with that name already exists."""

    code: str = "EventDataStoreAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreFederationEnabledException(ServiceException):
    """You cannot delete the event data store because Lake query federation is
    enabled. To delete the event data store, run the ``DisableFederation``
    operation to disable Lake query federation on the event data store.
    """

    code: str = "EventDataStoreFederationEnabledException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreHasOngoingImportException(ServiceException):
    """This exception is thrown when you try to update or delete an event data
    store that currently has an import in progress.
    """

    code: str = "EventDataStoreHasOngoingImportException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreMaxLimitExceededException(ServiceException):
    """Your account has used the maximum number of event data stores."""

    code: str = "EventDataStoreMaxLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreNotFoundException(ServiceException):
    """The specified event data store was not found."""

    code: str = "EventDataStoreNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class EventDataStoreTerminationProtectedException(ServiceException):
    """The event data store cannot be deleted because termination protection is
    enabled for it.
    """

    code: str = "EventDataStoreTerminationProtectedException"
    sender_fault: bool = False
    status_code: int = 400


class GenerateResponseException(ServiceException):
    """This exception is thrown when a valid query could not be generated for
    the provided prompt.
    """

    code: str = "GenerateResponseException"
    sender_fault: bool = False
    status_code: int = 400


class ImportNotFoundException(ServiceException):
    """The specified import was not found."""

    code: str = "ImportNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class InactiveEventDataStoreException(ServiceException):
    """The event data store is inactive."""

    code: str = "InactiveEventDataStoreException"
    sender_fault: bool = False
    status_code: int = 400


class InactiveQueryException(ServiceException):
    """The specified query cannot be canceled because it is in the
    ``FINISHED``, ``FAILED``, ``TIMED_OUT``, or ``CANCELLED`` state.
    """

    code: str = "InactiveQueryException"
    sender_fault: bool = False
    status_code: int = 400


class InsightNotEnabledException(ServiceException):
    """If you run ``GetInsightSelectors`` on a trail or event data store that
    does not have Insights events enabled, the operation throws the
    exception ``InsightNotEnabledException``.
    """

    code: str = "InsightNotEnabledException"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientDependencyServiceAccessPermissionException(ServiceException):
    """This exception is thrown when the IAM identity that is used to create
    the organization resource lacks one or more required permissions for
    creating an organization resource in a required service.
    """

    code: str = "InsufficientDependencyServiceAccessPermissionException"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientEncryptionPolicyException(ServiceException):
    """For the ``CreateTrail`` ``PutInsightSelectors``, ``UpdateTrail``,
    ``StartQuery``, and ``StartImport`` operations, this exception is thrown
    when the policy on the S3 bucket or KMS key does not have sufficient
    permissions for the operation.

    For all other operations, this exception is thrown when the policy for
    the KMS key does not have sufficient permissions for the operation.
    """

    code: str = "InsufficientEncryptionPolicyException"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientIAMAccessPermissionException(ServiceException):
    """The task can't be completed because you are signed in with an account
    that lacks permissions to view or create a service-linked role. Sign in
    with an account that has the required permissions and then try again.
    """

    code: str = "InsufficientIAMAccessPermissionException"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientS3BucketPolicyException(ServiceException):
    """This exception is thrown when the policy on the S3 bucket is not
    sufficient.
    """

    code: str = "InsufficientS3BucketPolicyException"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientSnsTopicPolicyException(ServiceException):
    """This exception is thrown when the policy on the Amazon SNS topic is not
    sufficient.
    """

    code: str = "InsufficientSnsTopicPolicyException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidCloudWatchLogsLogGroupArnException(ServiceException):
    """This exception is thrown when the provided CloudWatch Logs log group is
    not valid.
    """

    code: str = "InvalidCloudWatchLogsLogGroupArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidCloudWatchLogsRoleArnException(ServiceException):
    """This exception is thrown when the provided role is not valid."""

    code: str = "InvalidCloudWatchLogsRoleArnException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidDateRangeException(ServiceException):
    """A date range for the query was specified that is not valid. Be sure that
    the start time is chronologically before the end time. For more
    information about writing a query, see `Create or edit a
    query <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-create-edit-query.html>`__
    in the *CloudTrail User Guide*.
    """

    code: str = "InvalidDateRangeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEventCategoryException(ServiceException):
    """Occurs if an event category that is not valid is specified as a value of
    ``EventCategory``.
    """

    code: str = "InvalidEventCategoryException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEventDataStoreCategoryException(ServiceException):
    """This exception is thrown when event categories of specified event data
    stores are not valid.
    """

    code: str = "InvalidEventDataStoreCategoryException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEventDataStoreStatusException(ServiceException):
    """The event data store is not in a status that supports the operation."""

    code: str = "InvalidEventDataStoreStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEventSelectorsException(ServiceException):
    """This exception is thrown when the ``PutEventSelectors`` operation is
    called with a number of event selectors, advanced event selectors, or
    data resources that is not valid. The combination of event selectors or
    advanced event selectors and data resources is not valid. A trail can
    have up to 5 event selectors. If a trail uses advanced event selectors,
    a maximum of 500 total values for all conditions in all advanced event
    selectors is allowed. A trail is limited to 250 data resources. These
    data resources can be distributed across event selectors, but the
    overall total cannot exceed 250.

    You can:

    -  Specify a valid number of event selectors (1 to 5) for a trail.

    -  Specify a valid number of data resources (1 to 250) for an event
       selector. The limit of number of resources on an individual event
       selector is configurable up to 250. However, this upper limit is
       allowed only if the total number of data resources does not exceed
       250 across all event selectors for a trail.

    -  Specify up to 500 values for all conditions in all advanced event
       selectors for a trail.

    -  Specify a valid value for a parameter. For example, specifying the
       ``ReadWriteType`` parameter with a value of ``read-only`` is not
       valid.
    """

    code: str = "InvalidEventSelectorsException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidHomeRegionException(ServiceException):
    """This exception is thrown when an operation is called on a trail from a
    Region other than the Region in which the trail was created.
    """

    code: str = "InvalidHomeRegionException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidImportSourceException(ServiceException):
    """This exception is thrown when the provided source S3 bucket is not valid
    for import.
    """

    code: str = "InvalidImportSourceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInsightSelectorsException(ServiceException):
    """For ``PutInsightSelectors``, this exception is thrown when the
    formatting or syntax of the ``InsightSelectors`` JSON statement is not
    valid, or the specified ``InsightType`` in the ``InsightSelectors``
    statement is not valid. Valid values for ``InsightType`` are
    ``ApiCallRateInsight`` and ``ApiErrorRateInsight``. To enable Insights
    on an event data store, the destination event data store specified by
    the ``InsightsDestination`` parameter must log Insights events and the
    source event data store specified by the ``EventDataStore`` parameter
    must log management events.

    For ``UpdateEventDataStore``, this exception is thrown if Insights are
    enabled on the event data store and the updated advanced event selectors
    are not compatible with the configured ``InsightSelectors``. If the
    ``InsightSelectors`` includes an ``InsightType`` of
    ``ApiCallRateInsight``, the source event data store must log ``write``
    management events. If the ``InsightSelectors`` includes an
    ``InsightType`` of ``ApiErrorRateInsight``, the source event data store
    must log management events.
    """

    code: str = "InvalidInsightSelectorsException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidKmsKeyIdException(ServiceException):
    """This exception is thrown when the KMS key ARN is not valid."""

    code: str = "InvalidKmsKeyIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLookupAttributesException(ServiceException):
    """Occurs when a lookup attribute is specified that is not valid."""

    code: str = "InvalidLookupAttributesException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidMaxResultsException(ServiceException):
    """This exception is thrown if the limit specified is not valid."""

    code: str = "InvalidMaxResultsException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNextTokenException(ServiceException):
    """A token that is not valid, or a token that was previously used in a
    request with different parameters. This exception is thrown if the token
    is not valid.
    """

    code: str = "InvalidNextTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterCombinationException(ServiceException):
    """This exception is thrown when the combination of parameters provided is
    not valid.
    """

    code: str = "InvalidParameterCombinationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterException(ServiceException):
    """The request includes a parameter that is not valid."""

    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidQueryStatementException(ServiceException):
    """The query that was submitted has validation errors, or uses incorrect
    syntax or unsupported keywords. For more information about writing a
    query, see `Create or edit a
    query <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-create-edit-query.html>`__
    in the *CloudTrail User Guide*.
    """

    code: str = "InvalidQueryStatementException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidQueryStatusException(ServiceException):
    """The query status is not valid for the operation."""

    code: str = "InvalidQueryStatusException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidS3BucketNameException(ServiceException):
    """This exception is thrown when the provided S3 bucket name is not valid."""

    code: str = "InvalidS3BucketNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidS3PrefixException(ServiceException):
    """This exception is thrown when the provided S3 prefix is not valid."""

    code: str = "InvalidS3PrefixException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSnsTopicNameException(ServiceException):
    """This exception is thrown when the provided SNS topic name is not valid."""

    code: str = "InvalidSnsTopicNameException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSourceException(ServiceException):
    """This exception is thrown when the specified value of ``Source`` is not
    valid.
    """

    code: str = "InvalidSourceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTagParameterException(ServiceException):
    """This exception is thrown when the specified tag key or values are not
    valid. It can also occur if there are duplicate tags or too many tags on
    the resource.
    """

    code: str = "InvalidTagParameterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTimeRangeException(ServiceException):
    """Occurs if the timestamp values are not valid. Either the start time
    occurs after the end time, or the time range is outside the range of
    possible values.
    """

    code: str = "InvalidTimeRangeException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTokenException(ServiceException):
    """Reserved for future use."""

    code: str = "InvalidTokenException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidTrailNameException(ServiceException):
    """This exception is thrown when the provided trail name is not valid.
    Trail names must meet the following requirements:

    -  Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.),
       underscores (_), or dashes (-)

    -  Start with a letter or number, and end with a letter or number

    -  Be between 3 and 128 characters

    -  Have no adjacent periods, underscores or dashes. Names like
       ``my-_namespace`` and ``my--namespace`` are not valid.

    -  Not be in IP address format (for example, 192.168.5.4)
    """

    code: str = "InvalidTrailNameException"
    sender_fault: bool = False
    status_code: int = 400


class KmsException(ServiceException):
    """This exception is thrown when there is an issue with the specified KMS
    key and the trail or event data store can't be updated.
    """

    code: str = "KmsException"
    sender_fault: bool = False
    status_code: int = 400


class KmsKeyDisabledException(ServiceException):
    """This exception is no longer in use."""

    code: str = "KmsKeyDisabledException"
    sender_fault: bool = False
    status_code: int = 400


class KmsKeyNotFoundException(ServiceException):
    """This exception is thrown when the KMS key does not exist, when the S3
    bucket and the KMS key are not in the same Region, or when the KMS key
    associated with the Amazon SNS topic either does not exist or is not in
    the same Region.
    """

    code: str = "KmsKeyNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class MaxConcurrentQueriesException(ServiceException):
    """You are already running the maximum number of concurrent queries. The
    maximum number of concurrent queries is 10. Wait a minute for some
    queries to finish, and then run the query again.
    """

    code: str = "MaxConcurrentQueriesException"
    sender_fault: bool = False
    status_code: int = 400


class MaximumNumberOfTrailsExceededException(ServiceException):
    """This exception is thrown when the maximum number of trails is reached."""

    code: str = "MaximumNumberOfTrailsExceededException"
    sender_fault: bool = False
    status_code: int = 400


class NoManagementAccountSLRExistsException(ServiceException):
    """This exception is thrown when the management account does not have a
    service-linked role.
    """

    code: str = "NoManagementAccountSLRExistsException"
    sender_fault: bool = False
    status_code: int = 400


class NotOrganizationManagementAccountException(ServiceException):
    """This exception is thrown when the account making the request is not the
    organization's management account.
    """

    code: str = "NotOrganizationManagementAccountException"
    sender_fault: bool = False
    status_code: int = 400


class NotOrganizationMasterAccountException(ServiceException):
    """This exception is thrown when the Amazon Web Services account making the
    request to create or update an organization trail or event data store is
    not the management account for an organization in Organizations. For
    more information, see `Prepare For Creating a Trail For Your
    Organization <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html>`__
    or `Organization event data
    stores <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html>`__.
    """

    code: str = "NotOrganizationMasterAccountException"
    sender_fault: bool = False
    status_code: int = 400


class OperationNotPermittedException(ServiceException):
    """This exception is thrown when the requested operation is not permitted."""

    code: str = "OperationNotPermittedException"
    sender_fault: bool = False
    status_code: int = 400


class OrganizationNotInAllFeaturesModeException(ServiceException):
    """This exception is thrown when Organizations is not configured to support
    all features. All features must be enabled in Organizations to support
    creating an organization trail or event data store.
    """

    code: str = "OrganizationNotInAllFeaturesModeException"
    sender_fault: bool = False
    status_code: int = 400


class OrganizationsNotInUseException(ServiceException):
    """This exception is thrown when the request is made from an Amazon Web
    Services account that is not a member of an organization. To make this
    request, sign in using the credentials of an account that belongs to an
    organization.
    """

    code: str = "OrganizationsNotInUseException"
    sender_fault: bool = False
    status_code: int = 400


class QueryIdNotFoundException(ServiceException):
    """The query ID does not exist or does not map to a query."""

    code: str = "QueryIdNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceARNNotValidException(ServiceException):
    """This exception is thrown when the provided resource does not exist, or
    the ARN format of the resource is not valid.

    The following is the format of an event data store ARN:
    ``arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE``

    The following is the format of a dashboard ARN:
    ``arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash``

    The following is the format of a channel ARN:
    ``arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890``
    """

    code: str = "ResourceARNNotValidException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """This exception is thrown when the specified resource is not found."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ResourcePolicyNotFoundException(ServiceException):
    """This exception is thrown when the specified resource policy is not
    found.
    """

    code: str = "ResourcePolicyNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ResourcePolicyNotValidException(ServiceException):
    """This exception is thrown when the resouce-based policy has syntax
    errors, or contains a principal that is not valid.
    """

    code: str = "ResourcePolicyNotValidException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceTypeNotSupportedException(ServiceException):
    """This exception is thrown when the specified resource type is not
    supported by CloudTrail.
    """

    code: str = "ResourceTypeNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class S3BucketDoesNotExistException(ServiceException):
    """This exception is thrown when the specified S3 bucket does not exist."""

    code: str = "S3BucketDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class ServiceQuotaExceededException(ServiceException):
    """This exception is thrown when the quota is exceeded. For information
    about CloudTrail quotas, see `Service
    quotas <https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail>`__
    in the *Amazon Web Services General Reference*.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 400


class TagsLimitExceededException(ServiceException):
    """The number of tags per trail, event data store, dashboard, or channel
    has exceeded the permitted amount. Currently, the limit is 50.
    """

    code: str = "TagsLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """This exception is thrown when the request rate exceeds the limit."""

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class TrailAlreadyExistsException(ServiceException):
    """This exception is thrown when the specified trail already exists."""

    code: str = "TrailAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class TrailNotFoundException(ServiceException):
    """This exception is thrown when the trail with the given name is not
    found.
    """

    code: str = "TrailNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class TrailNotProvidedException(ServiceException):
    """This exception is no longer in use."""

    code: str = "TrailNotProvidedException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedOperationException(ServiceException):
    """This exception is thrown when the requested operation is not supported."""

    code: str = "UnsupportedOperationException"
    sender_fault: bool = False
    status_code: int = 400


class Tag(TypedDict, total=False):
    """A custom key-value pair associated with a resource such as a CloudTrail
    trail, event data store, dashboard, or channel.
    """

    Key: TagKey
    Value: Optional[TagValue]


TagsList = List[Tag]


class AddTagsRequest(ServiceRequest):
    """Specifies the tags to add to a trail, event data store, dashboard, or
    channel.
    """

    ResourceId: String
    TagsList: TagsList


class AddTagsResponse(TypedDict, total=False):
    """Returns the objects or data if successful. Otherwise, returns an error."""

    pass


Operator = List[OperatorValue]


class AdvancedFieldSelector(TypedDict, total=False):
    """A single selector statement in an advanced event selector."""

    Field: SelectorField
    Equals: Optional[Operator]
    StartsWith: Optional[Operator]
    EndsWith: Optional[Operator]
    NotEquals: Optional[Operator]
    NotStartsWith: Optional[Operator]
    NotEndsWith: Optional[Operator]


AdvancedFieldSelectors = List[AdvancedFieldSelector]


class AdvancedEventSelector(TypedDict, total=False):
    """Advanced event selectors let you create fine-grained selectors for
    CloudTrail management, data, and network activity events. They help you
    control costs by logging only those events that are important to you.
    For more information about configuring advanced event selectors, see the
    `Logging data
    events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`__,
    `Logging network activity
    events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html>`__,
    and `Logging management
    events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`__
    topics in the *CloudTrail User Guide*.

    You cannot apply both event selectors and advanced event selectors to a
    trail.

    For information about configurable advanced event selector fields, see
    `AdvancedEventSelector <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html>`__
    in the *CloudTrail API Reference*.
    """

    Name: Optional[SelectorName]
    FieldSelectors: AdvancedFieldSelectors


AdvancedEventSelectors = List[AdvancedEventSelector]
ByteBuffer = bytes


class CancelQueryRequest(ServiceRequest):
    EventDataStore: Optional[EventDataStoreArn]
    QueryId: UUID
    EventDataStoreOwnerAccountId: Optional[AccountId]


class CancelQueryResponse(TypedDict, total=False):
    QueryId: UUID
    QueryStatus: QueryStatus
    EventDataStoreOwnerAccountId: Optional[AccountId]


class Channel(TypedDict, total=False):
    """Contains information about a returned CloudTrail channel."""

    ChannelArn: Optional[ChannelArn]
    Name: Optional[ChannelName]


Channels = List[Channel]
OperatorTargetList = List[OperatorTargetListMember]


class ContextKeySelector(TypedDict, total=False):
    """An object that contains information types to be included in CloudTrail
    enriched events.
    """

    Type: Type
    Equals: OperatorTargetList


ContextKeySelectors = List[ContextKeySelector]


class Destination(TypedDict, total=False):
    """Contains information about the destination receiving events."""

    Type: DestinationType
    Location: Location


Destinations = List[Destination]


class CreateChannelRequest(ServiceRequest):
    Name: ChannelName
    Source: Source
    Destinations: Destinations
    Tags: Optional[TagsList]


class CreateChannelResponse(TypedDict, total=False):
    ChannelArn: Optional[ChannelArn]
    Name: Optional[ChannelName]
    Source: Optional[Source]
    Destinations: Optional[Destinations]
    Tags: Optional[TagsList]


ViewPropertiesMap = Dict[ViewPropertiesKey, ViewPropertiesValue]
QueryParameters = List[QueryParameter]


class RequestWidget(TypedDict, total=False):
    """Contains information about a widget on a CloudTrail Lake dashboard."""

    QueryStatement: QueryStatement
    QueryParameters: Optional[QueryParameters]
    ViewProperties: ViewPropertiesMap


RequestWidgetList = List[RequestWidget]


class RefreshScheduleFrequency(TypedDict, total=False):
    """Specifies the frequency for a dashboard refresh schedule.

    For a custom dashboard, you can schedule a refresh for every 1, 6, 12,
    or 24 hours, or every day.
    """

    Unit: Optional[RefreshScheduleFrequencyUnit]
    Value: Optional[RefreshScheduleFrequencyValue]


class RefreshSchedule(TypedDict, total=False):
    """The schedule for a dashboard refresh."""

    Frequency: Optional[RefreshScheduleFrequency]
    Status: Optional[RefreshScheduleStatus]
    TimeOfDay: Optional[TimeOfDay]


class CreateDashboardRequest(ServiceRequest):
    Name: DashboardName
    RefreshSchedule: Optional[RefreshSchedule]
    TagsList: Optional[TagsList]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    Widgets: Optional[RequestWidgetList]


class Widget(TypedDict, total=False):
    """A widget on a CloudTrail Lake dashboard."""

    QueryAlias: Optional[QueryAlias]
    QueryStatement: Optional[QueryStatement]
    QueryParameters: Optional[QueryParameters]
    ViewProperties: Optional[ViewPropertiesMap]


WidgetList = List[Widget]


class CreateDashboardResponse(TypedDict, total=False):
    DashboardArn: Optional[DashboardArn]
    Name: Optional[DashboardName]
    Type: Optional[DashboardType]
    Widgets: Optional[WidgetList]
    TagsList: Optional[TagsList]
    RefreshSchedule: Optional[RefreshSchedule]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]


class CreateEventDataStoreRequest(ServiceRequest):
    Name: EventDataStoreName
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    TagsList: Optional[TagsList]
    KmsKeyId: Optional[EventDataStoreKmsKeyId]
    StartIngestion: Optional[Boolean]
    BillingMode: Optional[BillingMode]


Date = datetime


class CreateEventDataStoreResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    Name: Optional[EventDataStoreName]
    Status: Optional[EventDataStoreStatus]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    TagsList: Optional[TagsList]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    KmsKeyId: Optional[EventDataStoreKmsKeyId]
    BillingMode: Optional[BillingMode]


class CreateTrailRequest(ServiceRequest):
    """Specifies the settings for each trail."""

    Name: String
    S3BucketName: String
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    EnableLogFileValidation: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]
    TagsList: Optional[TagsList]


class CreateTrailResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    Name: Optional[String]
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    SnsTopicARN: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    TrailARN: Optional[String]
    LogFileValidationEnabled: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]


class DashboardDetail(TypedDict, total=False):
    """Provides information about a CloudTrail Lake dashboard."""

    DashboardArn: Optional[DashboardArn]
    Type: Optional[DashboardType]


Dashboards = List[DashboardDetail]
DataResourceValues = List[String]


class DataResource(TypedDict, total=False):
    """You can configure the ``DataResource`` in an ``EventSelector`` to log
    data events for the following three resource types:

    -  ``AWS::DynamoDB::Table``

    -  ``AWS::Lambda::Function``

    -  ``AWS::S3::Object``

    To log data events for all other resource types including objects stored
    in `directory
    buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html>`__,
    you must use
    `AdvancedEventSelectors <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html>`__.
    You must also use ``AdvancedEventSelectors`` if you want to filter on
    the ``eventName`` field.

    Configure the ``DataResource`` to specify the resource type and resource
    ARNs for which you want to log data events.

    The total number of allowed data resources is 250. This number can be
    distributed between 1 and 5 event selectors, but the total cannot exceed
    250 across all selectors for the trail.

    The following example demonstrates how logging works when you configure
    logging of all data events for a general purpose bucket named
    ``amzn-s3-demo-bucket1``. In this example, the CloudTrail user specified
    an empty prefix, and the option to log both ``Read`` and ``Write`` data
    events.

    #. A user uploads an image file to ``amzn-s3-demo-bucket1``.

    #. The ``PutObject`` API operation is an Amazon S3 object-level API. It
       is recorded as a data event in CloudTrail. Because the CloudTrail
       user specified an S3 bucket with an empty prefix, events that occur
       on any object in that bucket are logged. The trail processes and logs
       the event.

    #. A user uploads an object to an Amazon S3 bucket named
       ``arn:aws:s3:::amzn-s3-demo-bucket1``.

    #. The ``PutObject`` API operation occurred for an object in an S3
       bucket that the CloudTrail user didn't specify for the trail. The
       trail doesn’t log the event.

    The following example demonstrates how logging works when you configure
    logging of Lambda data events for a Lambda function named
    *MyLambdaFunction*, but not for all Lambda functions.

    #. A user runs a script that includes a call to the *MyLambdaFunction*
       function and the *MyOtherLambdaFunction* function.

    #. The ``Invoke`` API operation on *MyLambdaFunction* is an Lambda API.
       It is recorded as a data event in CloudTrail. Because the CloudTrail
       user specified logging data events for *MyLambdaFunction*, any
       invocations of that function are logged. The trail processes and logs
       the event.

    #. The ``Invoke`` API operation on *MyOtherLambdaFunction* is an Lambda
       API. Because the CloudTrail user did not specify logging data events
       for all Lambda functions, the ``Invoke`` operation for
       *MyOtherLambdaFunction* does not match the function specified for the
       trail. The trail doesn’t log the event.
    """

    Type: Optional[String]
    Values: Optional[DataResourceValues]


DataResources = List[DataResource]


class DeleteChannelRequest(ServiceRequest):
    Channel: ChannelArn


class DeleteChannelResponse(TypedDict, total=False):
    pass


class DeleteDashboardRequest(ServiceRequest):
    DashboardId: DashboardArn


class DeleteDashboardResponse(TypedDict, total=False):
    pass


class DeleteEventDataStoreRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn


class DeleteEventDataStoreResponse(TypedDict, total=False):
    pass


class DeleteResourcePolicyRequest(ServiceRequest):
    ResourceArn: ResourceArn


class DeleteResourcePolicyResponse(TypedDict, total=False):
    pass


class DeleteTrailRequest(ServiceRequest):
    """The request that specifies the name of a trail to delete."""

    Name: String


class DeleteTrailResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    pass


class DeregisterOrganizationDelegatedAdminRequest(ServiceRequest):
    """Removes CloudTrail delegated administrator permissions from a specified
    member account in an organization that is currently designated as a
    delegated administrator.
    """

    DelegatedAdminAccountId: AccountId


class DeregisterOrganizationDelegatedAdminResponse(TypedDict, total=False):
    """Returns the following response if successful. Otherwise, returns an
    error.
    """

    pass


class DescribeQueryRequest(ServiceRequest):
    EventDataStore: Optional[EventDataStoreArn]
    QueryId: Optional[UUID]
    QueryAlias: Optional[QueryAlias]
    RefreshId: Optional[RefreshId]
    EventDataStoreOwnerAccountId: Optional[AccountId]


Long = int


class QueryStatisticsForDescribeQuery(TypedDict, total=False):
    """Gets metadata about a query, including the number of events that were
    matched, the total number of events scanned, the query run time in
    milliseconds, and the query's creation time.
    """

    EventsMatched: Optional[Long]
    EventsScanned: Optional[Long]
    BytesScanned: Optional[Long]
    ExecutionTimeInMillis: Optional[Integer]
    CreationTime: Optional[Date]


class DescribeQueryResponse(TypedDict, total=False):
    QueryId: Optional[UUID]
    QueryString: Optional[QueryStatement]
    QueryStatus: Optional[QueryStatus]
    QueryStatistics: Optional[QueryStatisticsForDescribeQuery]
    ErrorMessage: Optional[ErrorMessage]
    DeliveryS3Uri: Optional[DeliveryS3Uri]
    DeliveryStatus: Optional[DeliveryStatus]
    Prompt: Optional[Prompt]
    EventDataStoreOwnerAccountId: Optional[AccountId]


TrailNameList = List[String]


class DescribeTrailsRequest(ServiceRequest):
    """Returns information about the trail."""

    trailNameList: Optional[TrailNameList]
    includeShadowTrails: Optional[Boolean]


class Trail(TypedDict, total=False):
    """The settings for a trail."""

    Name: Optional[String]
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    SnsTopicARN: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    HomeRegion: Optional[String]
    TrailARN: Optional[String]
    LogFileValidationEnabled: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    HasCustomEventSelectors: Optional[Boolean]
    HasInsightSelectors: Optional[Boolean]
    IsOrganizationTrail: Optional[Boolean]


TrailList = List[Trail]


class DescribeTrailsResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    trailList: Optional[TrailList]


class DisableFederationRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn


class DisableFederationResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    FederationStatus: Optional[FederationStatus]


class EnableFederationRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn
    FederationRoleArn: FederationRoleArn


class EnableFederationResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    FederationStatus: Optional[FederationStatus]
    FederationRoleArn: Optional[FederationRoleArn]


class Resource(TypedDict, total=False):
    """Specifies the type and name of a resource referenced by an event."""

    ResourceType: Optional[String]
    ResourceName: Optional[String]


ResourceList = List[Resource]


class Event(TypedDict, total=False):
    """Contains information about an event that was returned by a lookup
    request. The result includes a representation of a CloudTrail event.
    """

    EventId: Optional[String]
    EventName: Optional[String]
    ReadOnly: Optional[String]
    AccessKeyId: Optional[String]
    EventTime: Optional[Date]
    EventSource: Optional[String]
    Username: Optional[String]
    Resources: Optional[ResourceList]
    CloudTrailEvent: Optional[String]


class EventDataStore(TypedDict, total=False):
    """A storage lake of event data against which you can run complex SQL-based
    queries. An event data store can include events that you have logged on
    your account. To select events for an event data store, use `advanced
    event
    selectors <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors>`__.
    """

    EventDataStoreArn: Optional[EventDataStoreArn]
    Name: Optional[EventDataStoreName]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    Status: Optional[EventDataStoreStatus]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]


EventDataStoreList = List[EventDataStoreArn]
EventDataStores = List[EventDataStore]
ExcludeManagementEventSources = List[String]


class EventSelector(TypedDict, total=False):
    """Use event selectors to further specify the management and data event
    settings for your trail. By default, trails created without specific
    event selectors will be configured to log all read and write management
    events, and no data events. When an event occurs in your account,
    CloudTrail evaluates the event selector for all trails. For each trail,
    if the event matches any event selector, the trail processes and logs
    the event. If the event doesn't match any event selector, the trail
    doesn't log the event.

    You can configure up to five event selectors for a trail.

    You cannot apply both event selectors and advanced event selectors to a
    trail.
    """

    ReadWriteType: Optional[ReadWriteType]
    IncludeManagementEvents: Optional[Boolean]
    DataResources: Optional[DataResources]
    ExcludeManagementEventSources: Optional[ExcludeManagementEventSources]


EventSelectors = List[EventSelector]
EventsList = List[Event]


class GenerateQueryRequest(ServiceRequest):
    EventDataStores: EventDataStoreList
    Prompt: Prompt


class GenerateQueryResponse(TypedDict, total=False):
    QueryStatement: Optional[QueryStatement]
    QueryAlias: Optional[QueryAlias]
    EventDataStoreOwnerAccountId: Optional[AccountId]


class GetChannelRequest(ServiceRequest):
    Channel: ChannelArn


class IngestionStatus(TypedDict, total=False):
    """A table showing information about the most recent successful and failed
    attempts to ingest events.
    """

    LatestIngestionSuccessTime: Optional[Date]
    LatestIngestionSuccessEventID: Optional[UUID]
    LatestIngestionErrorCode: Optional[ErrorMessage]
    LatestIngestionAttemptTime: Optional[Date]
    LatestIngestionAttemptEventID: Optional[UUID]


class SourceConfig(TypedDict, total=False):
    """Contains configuration information about the channel."""

    ApplyToAllRegions: Optional[Boolean]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class GetChannelResponse(TypedDict, total=False):
    ChannelArn: Optional[ChannelArn]
    Name: Optional[ChannelName]
    Source: Optional[Source]
    SourceConfig: Optional[SourceConfig]
    Destinations: Optional[Destinations]
    IngestionStatus: Optional[IngestionStatus]


class GetDashboardRequest(ServiceRequest):
    DashboardId: DashboardArn


class GetDashboardResponse(TypedDict, total=False):
    DashboardArn: Optional[DashboardArn]
    Type: Optional[DashboardType]
    Status: Optional[DashboardStatus]
    Widgets: Optional[WidgetList]
    RefreshSchedule: Optional[RefreshSchedule]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    LastRefreshId: Optional[RefreshId]
    LastRefreshFailureReason: Optional[ErrorMessage]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]


class GetEventConfigurationRequest(ServiceRequest):
    EventDataStore: Optional[String]


class GetEventConfigurationResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    MaxEventSize: Optional[MaxEventSize]
    ContextKeySelectors: Optional[ContextKeySelectors]


class GetEventDataStoreRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn


class PartitionKey(TypedDict, total=False):
    """Contains information about a partition key for an event data store."""

    Name: PartitionKeyName
    Type: PartitionKeyType


PartitionKeyList = List[PartitionKey]


class GetEventDataStoreResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    Name: Optional[EventDataStoreName]
    Status: Optional[EventDataStoreStatus]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    KmsKeyId: Optional[EventDataStoreKmsKeyId]
    BillingMode: Optional[BillingMode]
    FederationStatus: Optional[FederationStatus]
    FederationRoleArn: Optional[FederationRoleArn]
    PartitionKeys: Optional[PartitionKeyList]


class GetEventSelectorsRequest(ServiceRequest):
    TrailName: String


class GetEventSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    EventSelectors: Optional[EventSelectors]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class GetImportRequest(ServiceRequest):
    ImportId: UUID


class ImportStatistics(TypedDict, total=False):
    """Provides statistics for the specified ``ImportID``. CloudTrail does not
    update import statistics in real-time. Returned values for parameters
    such as ``EventsCompleted`` may be lower than the actual value, because
    CloudTrail updates statistics incrementally over the course of the
    import.
    """

    PrefixesFound: Optional[Long]
    PrefixesCompleted: Optional[Long]
    FilesCompleted: Optional[Long]
    EventsCompleted: Optional[Long]
    FailedEntries: Optional[Long]


class S3ImportSource(TypedDict, total=False):
    """The settings for the source S3 bucket."""

    S3LocationUri: String
    S3BucketRegion: String
    S3BucketAccessRoleArn: String


class ImportSource(TypedDict, total=False):
    """The import source."""

    S3: S3ImportSource


ImportDestinations = List[EventDataStoreArn]


class GetImportResponse(TypedDict, total=False):
    ImportId: Optional[UUID]
    Destinations: Optional[ImportDestinations]
    ImportSource: Optional[ImportSource]
    StartEventTime: Optional[Date]
    EndEventTime: Optional[Date]
    ImportStatus: Optional[ImportStatus]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    ImportStatistics: Optional[ImportStatistics]


class GetInsightSelectorsRequest(ServiceRequest):
    TrailName: Optional[String]
    EventDataStore: Optional[EventDataStoreArn]


class InsightSelector(TypedDict, total=False):
    """A JSON string that contains a list of Insights types that are logged on
    a trail or event data store.
    """

    InsightType: Optional[InsightType]


InsightSelectors = List[InsightSelector]


class GetInsightSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    InsightSelectors: Optional[InsightSelectors]
    EventDataStoreArn: Optional[EventDataStoreArn]
    InsightsDestination: Optional[EventDataStoreArn]


class GetQueryResultsRequest(ServiceRequest):
    EventDataStore: Optional[EventDataStoreArn]
    QueryId: UUID
    NextToken: Optional[PaginationToken]
    MaxQueryResults: Optional[MaxQueryResults]
    EventDataStoreOwnerAccountId: Optional[AccountId]


QueryResultColumn = Dict[QueryResultKey, QueryResultValue]
QueryResultRow = List[QueryResultColumn]
QueryResultRows = List[QueryResultRow]


class QueryStatistics(TypedDict, total=False):
    """Metadata about a query, such as the number of results."""

    ResultsCount: Optional[Integer]
    TotalResultsCount: Optional[Integer]
    BytesScanned: Optional[Long]


class GetQueryResultsResponse(TypedDict, total=False):
    QueryStatus: Optional[QueryStatus]
    QueryStatistics: Optional[QueryStatistics]
    QueryResultRows: Optional[QueryResultRows]
    NextToken: Optional[PaginationToken]
    ErrorMessage: Optional[ErrorMessage]


class GetResourcePolicyRequest(ServiceRequest):
    ResourceArn: ResourceArn


class GetResourcePolicyResponse(TypedDict, total=False):
    ResourceArn: Optional[ResourceArn]
    ResourcePolicy: Optional[ResourcePolicy]
    DelegatedAdminResourcePolicy: Optional[ResourcePolicy]


class GetTrailRequest(ServiceRequest):
    Name: String


class GetTrailResponse(TypedDict, total=False):
    Trail: Optional[Trail]


class GetTrailStatusRequest(ServiceRequest):
    """The name of a trail about which you want the current status."""

    Name: String


class GetTrailStatusResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    IsLogging: Optional[Boolean]
    LatestDeliveryError: Optional[String]
    LatestNotificationError: Optional[String]
    LatestDeliveryTime: Optional[Date]
    LatestNotificationTime: Optional[Date]
    StartLoggingTime: Optional[Date]
    StopLoggingTime: Optional[Date]
    LatestCloudWatchLogsDeliveryError: Optional[String]
    LatestCloudWatchLogsDeliveryTime: Optional[Date]
    LatestDigestDeliveryTime: Optional[Date]
    LatestDigestDeliveryError: Optional[String]
    LatestDeliveryAttemptTime: Optional[String]
    LatestNotificationAttemptTime: Optional[String]
    LatestNotificationAttemptSucceeded: Optional[String]
    LatestDeliveryAttemptSucceeded: Optional[String]
    TimeLoggingStarted: Optional[String]
    TimeLoggingStopped: Optional[String]


class ImportFailureListItem(TypedDict, total=False):
    """Provides information about an import failure."""

    Location: Optional[String]
    Status: Optional[ImportFailureStatus]
    ErrorType: Optional[String]
    ErrorMessage: Optional[String]
    LastUpdatedTime: Optional[Date]


ImportFailureList = List[ImportFailureListItem]


class ImportsListItem(TypedDict, total=False):
    """Contains information about an import that was returned by a lookup
    request.
    """

    ImportId: Optional[UUID]
    ImportStatus: Optional[ImportStatus]
    Destinations: Optional[ImportDestinations]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]


ImportsList = List[ImportsListItem]
InsightsMetricValues = List[Double]


class ListChannelsRequest(ServiceRequest):
    MaxResults: Optional[ListChannelsMaxResultsCount]
    NextToken: Optional[PaginationToken]


class ListChannelsResponse(TypedDict, total=False):
    Channels: Optional[Channels]
    NextToken: Optional[PaginationToken]


class ListDashboardsRequest(ServiceRequest):
    NamePrefix: Optional[DashboardName]
    Type: Optional[DashboardType]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[ListDashboardsMaxResultsCount]


class ListDashboardsResponse(TypedDict, total=False):
    Dashboards: Optional[Dashboards]
    NextToken: Optional[PaginationToken]


class ListEventDataStoresRequest(ServiceRequest):
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[ListEventDataStoresMaxResultsCount]


class ListEventDataStoresResponse(TypedDict, total=False):
    EventDataStores: Optional[EventDataStores]
    NextToken: Optional[PaginationToken]


class ListImportFailuresRequest(ServiceRequest):
    ImportId: UUID
    MaxResults: Optional[ListImportFailuresMaxResultsCount]
    NextToken: Optional[PaginationToken]


class ListImportFailuresResponse(TypedDict, total=False):
    Failures: Optional[ImportFailureList]
    NextToken: Optional[PaginationToken]


class ListImportsRequest(ServiceRequest):
    MaxResults: Optional[ListImportsMaxResultsCount]
    Destination: Optional[EventDataStoreArn]
    ImportStatus: Optional[ImportStatus]
    NextToken: Optional[PaginationToken]


class ListImportsResponse(TypedDict, total=False):
    Imports: Optional[ImportsList]
    NextToken: Optional[PaginationToken]


class ListInsightsMetricDataRequest(ServiceRequest):
    EventSource: EventSource
    EventName: EventName
    InsightType: InsightType
    ErrorCode: Optional[ErrorCode]
    StartTime: Optional[Date]
    EndTime: Optional[Date]
    Period: Optional[InsightsMetricPeriod]
    DataType: Optional[InsightsMetricDataType]
    MaxResults: Optional[InsightsMetricMaxResults]
    NextToken: Optional[InsightsMetricNextToken]


Timestamps = List[Date]


class ListInsightsMetricDataResponse(TypedDict, total=False):
    EventSource: Optional[EventSource]
    EventName: Optional[EventName]
    InsightType: Optional[InsightType]
    ErrorCode: Optional[ErrorCode]
    Timestamps: Optional[Timestamps]
    Values: Optional[InsightsMetricValues]
    NextToken: Optional[InsightsMetricNextToken]


class ListPublicKeysRequest(ServiceRequest):
    """Requests the public keys for a specified time range."""

    StartTime: Optional[Date]
    EndTime: Optional[Date]
    NextToken: Optional[String]


class PublicKey(TypedDict, total=False):
    """Contains information about a returned public key."""

    Value: Optional[ByteBuffer]
    ValidityStartTime: Optional[Date]
    ValidityEndTime: Optional[Date]
    Fingerprint: Optional[String]


PublicKeyList = List[PublicKey]


class ListPublicKeysResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    PublicKeyList: Optional[PublicKeyList]
    NextToken: Optional[String]


class ListQueriesRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[ListQueriesMaxResultsCount]
    StartTime: Optional[Date]
    EndTime: Optional[Date]
    QueryStatus: Optional[QueryStatus]


class Query(TypedDict, total=False):
    """A SQL string of criteria about events that you want to collect in an
    event data store.
    """

    QueryId: Optional[UUID]
    QueryStatus: Optional[QueryStatus]
    CreationTime: Optional[Date]


Queries = List[Query]


class ListQueriesResponse(TypedDict, total=False):
    Queries: Optional[Queries]
    NextToken: Optional[PaginationToken]


ResourceIdList = List[String]


class ListTagsRequest(ServiceRequest):
    """Specifies a list of tags to return."""

    ResourceIdList: ResourceIdList
    NextToken: Optional[String]


class ResourceTag(TypedDict, total=False):
    """A resource tag."""

    ResourceId: Optional[String]
    TagsList: Optional[TagsList]


ResourceTagList = List[ResourceTag]


class ListTagsResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    ResourceTagList: Optional[ResourceTagList]
    NextToken: Optional[String]


class ListTrailsRequest(ServiceRequest):
    NextToken: Optional[String]


class TrailInfo(TypedDict, total=False):
    """Information about a CloudTrail trail, including the trail's name, home
    Region, and Amazon Resource Name (ARN).
    """

    TrailARN: Optional[String]
    Name: Optional[String]
    HomeRegion: Optional[String]


Trails = List[TrailInfo]


class ListTrailsResponse(TypedDict, total=False):
    Trails: Optional[Trails]
    NextToken: Optional[String]


class LookupAttribute(TypedDict, total=False):
    """Specifies an attribute and value that filter the events returned."""

    AttributeKey: LookupAttributeKey
    AttributeValue: LookupAttributeValue


LookupAttributesList = List[LookupAttribute]


class LookupEventsRequest(ServiceRequest):
    """Contains a request for LookupEvents."""

    LookupAttributes: Optional[LookupAttributesList]
    StartTime: Optional[Date]
    EndTime: Optional[Date]
    EventCategory: Optional[EventCategory]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class LookupEventsResponse(TypedDict, total=False):
    """Contains a response to a LookupEvents action."""

    Events: Optional[EventsList]
    NextToken: Optional[NextToken]


class PutEventConfigurationRequest(ServiceRequest):
    EventDataStore: Optional[String]
    MaxEventSize: MaxEventSize
    ContextKeySelectors: ContextKeySelectors


class PutEventConfigurationResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    MaxEventSize: Optional[MaxEventSize]
    ContextKeySelectors: Optional[ContextKeySelectors]


class PutEventSelectorsRequest(ServiceRequest):
    TrailName: String
    EventSelectors: Optional[EventSelectors]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class PutEventSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    EventSelectors: Optional[EventSelectors]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class PutInsightSelectorsRequest(ServiceRequest):
    TrailName: Optional[String]
    InsightSelectors: InsightSelectors
    EventDataStore: Optional[EventDataStoreArn]
    InsightsDestination: Optional[EventDataStoreArn]


class PutInsightSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    InsightSelectors: Optional[InsightSelectors]
    EventDataStoreArn: Optional[EventDataStoreArn]
    InsightsDestination: Optional[EventDataStoreArn]


class PutResourcePolicyRequest(ServiceRequest):
    ResourceArn: ResourceArn
    ResourcePolicy: ResourcePolicy


class PutResourcePolicyResponse(TypedDict, total=False):
    ResourceArn: Optional[ResourceArn]
    ResourcePolicy: Optional[ResourcePolicy]
    DelegatedAdminResourcePolicy: Optional[ResourcePolicy]


QueryParameterValues = Dict[QueryParameterKey, QueryParameterValue]


class RegisterOrganizationDelegatedAdminRequest(ServiceRequest):
    """Specifies an organization member account ID as a CloudTrail delegated
    administrator.
    """

    MemberAccountId: AccountId


class RegisterOrganizationDelegatedAdminResponse(TypedDict, total=False):
    """Returns the following response if successful. Otherwise, returns an
    error.
    """

    pass


class RemoveTagsRequest(ServiceRequest):
    """Specifies the tags to remove from a trail, event data store, dashboard,
    or channel.
    """

    ResourceId: String
    TagsList: TagsList


class RemoveTagsResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    pass


class RestoreEventDataStoreRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn


class RestoreEventDataStoreResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    Name: Optional[EventDataStoreName]
    Status: Optional[EventDataStoreStatus]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    KmsKeyId: Optional[EventDataStoreKmsKeyId]
    BillingMode: Optional[BillingMode]


class SearchSampleQueriesRequest(ServiceRequest):
    SearchPhrase: SearchSampleQueriesSearchPhrase
    MaxResults: Optional[SearchSampleQueriesMaxResults]
    NextToken: Optional[PaginationToken]


class SearchSampleQueriesSearchResult(TypedDict, total=False):
    """A search result returned by the ``SearchSampleQueries`` operation."""

    Name: Optional[SampleQueryName]
    Description: Optional[SampleQueryDescription]
    SQL: Optional[SampleQuerySQL]
    Relevance: Optional[SampleQueryRelevance]


SearchSampleQueriesSearchResults = List[SearchSampleQueriesSearchResult]


class SearchSampleQueriesResponse(TypedDict, total=False):
    SearchResults: Optional[SearchSampleQueriesSearchResults]
    NextToken: Optional[PaginationToken]


class StartDashboardRefreshRequest(ServiceRequest):
    DashboardId: DashboardArn
    QueryParameterValues: Optional[QueryParameterValues]


class StartDashboardRefreshResponse(TypedDict, total=False):
    RefreshId: Optional[RefreshId]


class StartEventDataStoreIngestionRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn


class StartEventDataStoreIngestionResponse(TypedDict, total=False):
    pass


class StartImportRequest(ServiceRequest):
    Destinations: Optional[ImportDestinations]
    ImportSource: Optional[ImportSource]
    StartEventTime: Optional[Date]
    EndEventTime: Optional[Date]
    ImportId: Optional[UUID]


class StartImportResponse(TypedDict, total=False):
    ImportId: Optional[UUID]
    Destinations: Optional[ImportDestinations]
    ImportSource: Optional[ImportSource]
    StartEventTime: Optional[Date]
    EndEventTime: Optional[Date]
    ImportStatus: Optional[ImportStatus]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]


class StartLoggingRequest(ServiceRequest):
    """The request to CloudTrail to start logging Amazon Web Services API calls
    for an account.
    """

    Name: String


class StartLoggingResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    pass


class StartQueryRequest(ServiceRequest):
    QueryStatement: Optional[QueryStatement]
    DeliveryS3Uri: Optional[DeliveryS3Uri]
    QueryAlias: Optional[QueryAlias]
    QueryParameters: Optional[QueryParameters]
    EventDataStoreOwnerAccountId: Optional[AccountId]


class StartQueryResponse(TypedDict, total=False):
    QueryId: Optional[UUID]
    EventDataStoreOwnerAccountId: Optional[AccountId]


class StopEventDataStoreIngestionRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn


class StopEventDataStoreIngestionResponse(TypedDict, total=False):
    pass


class StopImportRequest(ServiceRequest):
    ImportId: UUID


class StopImportResponse(TypedDict, total=False):
    ImportId: Optional[UUID]
    ImportSource: Optional[ImportSource]
    Destinations: Optional[ImportDestinations]
    ImportStatus: Optional[ImportStatus]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    StartEventTime: Optional[Date]
    EndEventTime: Optional[Date]
    ImportStatistics: Optional[ImportStatistics]


class StopLoggingRequest(ServiceRequest):
    """Passes the request to CloudTrail to stop logging Amazon Web Services API
    calls for the specified account.
    """

    Name: String


class StopLoggingResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    pass


class UpdateChannelRequest(ServiceRequest):
    Channel: ChannelArn
    Destinations: Optional[Destinations]
    Name: Optional[ChannelName]


class UpdateChannelResponse(TypedDict, total=False):
    ChannelArn: Optional[ChannelArn]
    Name: Optional[ChannelName]
    Source: Optional[Source]
    Destinations: Optional[Destinations]


class UpdateDashboardRequest(ServiceRequest):
    DashboardId: DashboardArn
    Widgets: Optional[RequestWidgetList]
    RefreshSchedule: Optional[RefreshSchedule]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]


class UpdateDashboardResponse(TypedDict, total=False):
    DashboardArn: Optional[DashboardArn]
    Name: Optional[DashboardName]
    Type: Optional[DashboardType]
    Widgets: Optional[WidgetList]
    RefreshSchedule: Optional[RefreshSchedule]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]


class UpdateEventDataStoreRequest(ServiceRequest):
    EventDataStore: EventDataStoreArn
    Name: Optional[EventDataStoreName]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    KmsKeyId: Optional[EventDataStoreKmsKeyId]
    BillingMode: Optional[BillingMode]


class UpdateEventDataStoreResponse(TypedDict, total=False):
    EventDataStoreArn: Optional[EventDataStoreArn]
    Name: Optional[EventDataStoreName]
    Status: Optional[EventDataStoreStatus]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]
    MultiRegionEnabled: Optional[Boolean]
    OrganizationEnabled: Optional[Boolean]
    RetentionPeriod: Optional[RetentionPeriod]
    TerminationProtectionEnabled: Optional[TerminationProtectionEnabled]
    CreatedTimestamp: Optional[Date]
    UpdatedTimestamp: Optional[Date]
    KmsKeyId: Optional[EventDataStoreKmsKeyId]
    BillingMode: Optional[BillingMode]
    FederationStatus: Optional[FederationStatus]
    FederationRoleArn: Optional[FederationRoleArn]


class UpdateTrailRequest(ServiceRequest):
    """Specifies settings to update for the trail."""

    Name: String
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    EnableLogFileValidation: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]


class UpdateTrailResponse(TypedDict, total=False):
    """Returns the objects or data listed below if successful. Otherwise,
    returns an error.
    """

    Name: Optional[String]
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    SnsTopicARN: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    TrailARN: Optional[String]
    LogFileValidationEnabled: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]


class CloudtrailApi:
    service = "cloudtrail"
    version = "2013-11-01"

    @handler("AddTags")
    def add_tags(
        self, context: RequestContext, resource_id: String, tags_list: TagsList, **kwargs
    ) -> AddTagsResponse:
        """Adds one or more tags to a trail, event data store, dashboard, or
        channel, up to a limit of 50. Overwrites an existing tag's value when a
        new value is specified for an existing tag key. Tag key names must be
        unique; you cannot have two keys with the same name but different
        values. If you specify a key without a value, the tag will be created
        with the specified key and a value of null. You can tag a trail or event
        data store that applies to all Amazon Web Services Regions only from the
        Region in which the trail or event data store was created (also known as
        its home Region).

        :param resource_id: Specifies the ARN of the trail, event data store, dashboard, or channel
        to which one or more tags will be added.
        :param tags_list: Contains a list of tags, up to a limit of 50.
        :returns: AddTagsResponse
        :raises ResourceNotFoundException:
        :raises CloudTrailARNInvalidException:
        :raises EventDataStoreARNInvalidException:
        :raises ChannelARNInvalidException:
        :raises ResourceTypeNotSupportedException:
        :raises TagsLimitExceededException:
        :raises InvalidTrailNameException:
        :raises InvalidTagParameterException:
        :raises InactiveEventDataStoreException:
        :raises EventDataStoreNotFoundException:
        :raises ChannelNotFoundException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CancelQuery")
    def cancel_query(
        self,
        context: RequestContext,
        query_id: UUID,
        event_data_store: EventDataStoreArn | None = None,
        event_data_store_owner_account_id: AccountId | None = None,
        **kwargs,
    ) -> CancelQueryResponse:
        """Cancels a query if the query is not in a terminated state, such as
        ``CANCELLED``, ``FAILED``, ``TIMED_OUT``, or ``FINISHED``. You must
        specify an ARN value for ``EventDataStore``. The ID of the query that
        you want to cancel is also required. When you run ``CancelQuery``, the
        query status might show as ``CANCELLED`` even if the operation is not
        yet finished.

        :param query_id: The ID of the query that you want to cancel.
        :param event_data_store: The ARN (or the ID suffix of the ARN) of an event data store on which
        the specified query is running.
        :param event_data_store_owner_account_id: The account ID of the event data store owner.
        :returns: CancelQueryResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InactiveQueryException:
        :raises InvalidParameterException:
        :raises QueryIdNotFoundException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateChannel")
    def create_channel(
        self,
        context: RequestContext,
        name: ChannelName,
        source: Source,
        destinations: Destinations,
        tags: TagsList | None = None,
        **kwargs,
    ) -> CreateChannelResponse:
        """Creates a channel for CloudTrail to ingest events from a partner or
        external source. After you create a channel, a CloudTrail Lake event
        data store can log events from the partner or source that you specify.

        :param name: The name of the channel.
        :param source: The name of the partner or external event source.
        :param destinations: One or more event data stores to which events arriving through a channel
        will be logged.
        :param tags: A list of tags.
        :returns: CreateChannelResponse
        :raises ChannelMaxLimitExceededException:
        :raises InvalidSourceException:
        :raises ChannelAlreadyExistsException:
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreCategoryException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises InvalidTagParameterException:
        :raises TagsLimitExceededException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("CreateDashboard")
    def create_dashboard(
        self,
        context: RequestContext,
        name: DashboardName,
        refresh_schedule: RefreshSchedule | None = None,
        tags_list: TagsList | None = None,
        termination_protection_enabled: TerminationProtectionEnabled | None = None,
        widgets: RequestWidgetList | None = None,
        **kwargs,
    ) -> CreateDashboardResponse:
        """Creates a custom dashboard or the Highlights dashboard.

        -  **Custom dashboards** - Custom dashboards allow you to query events
           in any event data store type. You can add up to 10 widgets to a
           custom dashboard. You can manually refresh a custom dashboard, or you
           can set a refresh schedule.

        -  **Highlights dashboard** - You can create the Highlights dashboard to
           see a summary of key user activities and API usage across all your
           event data stores. CloudTrail Lake manages the Highlights dashboard
           and refreshes the dashboard every 6 hours. To create the Highlights
           dashboard, you must set and enable a refresh schedule.

        CloudTrail runs queries to populate the dashboard's widgets during a
        manual or scheduled refresh. CloudTrail must be granted permissions to
        run the ``StartQuery`` operation on your behalf. To provide permissions,
        run the ``PutResourcePolicy`` operation to attach a resource-based
        policy to each event data store. For more information, see `Example:
        Allow CloudTrail to run queries to populate a
        dashboard <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard>`__
        in the *CloudTrail User Guide*.

        To set a refresh schedule, CloudTrail must be granted permissions to run
        the ``StartDashboardRefresh`` operation to refresh the dashboard on your
        behalf. To provide permissions, run the ``PutResourcePolicy`` operation
        to attach a resource-based policy to the dashboard. For more
        information, see `Resource-based policy example for a
        dashboard <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards>`__
        in the *CloudTrail User Guide*.

        For more information about dashboards, see `CloudTrail Lake
        dashboards <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard.html>`__
        in the *CloudTrail User Guide*.

        :param name: The name of the dashboard.
        :param refresh_schedule: The refresh schedule configuration for the dashboard.
        :param tags_list: A list of tags.
        :param termination_protection_enabled: Specifies whether termination protection is enabled for the dashboard.
        :param widgets: An array of widgets for a custom dashboard.
        :returns: CreateDashboardResponse
        :raises ConflictException:
        :raises InvalidTagParameterException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InsufficientEncryptionPolicyException:
        :raises InvalidQueryStatementException:
        :raises ServiceQuotaExceededException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("CreateEventDataStore")
    def create_event_data_store(
        self,
        context: RequestContext,
        name: EventDataStoreName,
        advanced_event_selectors: AdvancedEventSelectors | None = None,
        multi_region_enabled: Boolean | None = None,
        organization_enabled: Boolean | None = None,
        retention_period: RetentionPeriod | None = None,
        termination_protection_enabled: TerminationProtectionEnabled | None = None,
        tags_list: TagsList | None = None,
        kms_key_id: EventDataStoreKmsKeyId | None = None,
        start_ingestion: Boolean | None = None,
        billing_mode: BillingMode | None = None,
        **kwargs,
    ) -> CreateEventDataStoreResponse:
        """Creates a new event data store.

        :param name: The name of the event data store.
        :param advanced_event_selectors: The advanced event selectors to use to select the events for the data
        store.
        :param multi_region_enabled: Specifies whether the event data store includes events from all Regions,
        or only from the Region in which the event data store is created.
        :param organization_enabled: Specifies whether an event data store collects events logged for an
        organization in Organizations.
        :param retention_period: The retention period of the event data store, in days.
        :param termination_protection_enabled: Specifies whether termination protection is enabled for the event data
        store.
        :param tags_list: A list of tags.
        :param kms_key_id: Specifies the KMS key ID to use to encrypt the events delivered by
        CloudTrail.
        :param start_ingestion: Specifies whether the event data store should start ingesting live
        events.
        :param billing_mode: The billing mode for the event data store determines the cost for
        ingesting events and the default and maximum retention period for the
        event data store.
        :returns: CreateEventDataStoreResponse
        :raises EventDataStoreAlreadyExistsException:
        :raises EventDataStoreMaxLimitExceededException:
        :raises InvalidEventSelectorsException:
        :raises InvalidParameterException:
        :raises InvalidTagParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises ConflictException:
        :raises InsufficientEncryptionPolicyException:
        :raises InvalidKmsKeyIdException:
        :raises KmsKeyNotFoundException:
        :raises KmsException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises NotOrganizationMasterAccountException:
        :raises OrganizationsNotInUseException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("CreateTrail")
    def create_trail(
        self,
        context: RequestContext,
        name: String,
        s3_bucket_name: String,
        s3_key_prefix: String | None = None,
        sns_topic_name: String | None = None,
        include_global_service_events: Boolean | None = None,
        is_multi_region_trail: Boolean | None = None,
        enable_log_file_validation: Boolean | None = None,
        cloud_watch_logs_log_group_arn: String | None = None,
        cloud_watch_logs_role_arn: String | None = None,
        kms_key_id: String | None = None,
        is_organization_trail: Boolean | None = None,
        tags_list: TagsList | None = None,
        **kwargs,
    ) -> CreateTrailResponse:
        """Creates a trail that specifies the settings for delivery of log data to
        an Amazon S3 bucket.

        :param name: Specifies the name of the trail.
        :param s3_bucket_name: Specifies the name of the Amazon S3 bucket designated for publishing log
        files.
        :param s3_key_prefix: Specifies the Amazon S3 key prefix that comes after the name of the
        bucket you have designated for log file delivery.
        :param sns_topic_name: Specifies the name or ARN of the Amazon SNS topic defined for
        notification of log file delivery.
        :param include_global_service_events: Specifies whether the trail is publishing events from global services
        such as IAM to the log files.
        :param is_multi_region_trail: Specifies whether the trail is created in the current Region or in all
        Regions.
        :param enable_log_file_validation: Specifies whether log file integrity validation is enabled.
        :param cloud_watch_logs_log_group_arn: Specifies a log group name using an Amazon Resource Name (ARN), a unique
        identifier that represents the log group to which CloudTrail logs will
        be delivered.
        :param cloud_watch_logs_role_arn: Specifies the role for the CloudWatch Logs endpoint to assume to write
        to a user's log group.
        :param kms_key_id: Specifies the KMS key ID to use to encrypt the logs delivered by
        CloudTrail.
        :param is_organization_trail: Specifies whether the trail is created for all accounts in an
        organization in Organizations, or only for the current Amazon Web
        Services account.
        :param tags_list: A list of tags.
        :returns: CreateTrailResponse
        :raises MaximumNumberOfTrailsExceededException:
        :raises TrailAlreadyExistsException:
        :raises S3BucketDoesNotExistException:
        :raises InsufficientS3BucketPolicyException:
        :raises InsufficientSnsTopicPolicyException:
        :raises InsufficientEncryptionPolicyException:
        :raises InvalidS3BucketNameException:
        :raises InvalidS3PrefixException:
        :raises InvalidSnsTopicNameException:
        :raises InvalidKmsKeyIdException:
        :raises InvalidTrailNameException:
        :raises TrailNotProvidedException:
        :raises TagsLimitExceededException:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterException:
        :raises KmsKeyNotFoundException:
        :raises KmsKeyDisabledException:
        :raises KmsException:
        :raises InvalidCloudWatchLogsLogGroupArnException:
        :raises InvalidCloudWatchLogsRoleArnException:
        :raises CloudWatchLogsDeliveryUnavailableException:
        :raises InvalidTagParameterException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises NotOrganizationMasterAccountException:
        :raises OrganizationsNotInUseException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises NoManagementAccountSLRExistsException:
        :raises CloudTrailInvalidClientTokenIdException:
        :raises ConflictException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteChannel")
    def delete_channel(
        self, context: RequestContext, channel: ChannelArn, **kwargs
    ) -> DeleteChannelResponse:
        """Deletes a channel.

        :param channel: The ARN or the ``UUID`` value of the channel that you want to delete.
        :returns: DeleteChannelResponse
        :raises ChannelARNInvalidException:
        :raises ChannelNotFoundException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("DeleteDashboard")
    def delete_dashboard(
        self, context: RequestContext, dashboard_id: DashboardArn, **kwargs
    ) -> DeleteDashboardResponse:
        """Deletes the specified dashboard. You cannot delete a dashboard that has
        termination protection enabled.

        :param dashboard_id: The name or ARN for the dashboard.
        :returns: DeleteDashboardResponse
        :raises ConflictException:
        :raises ResourceNotFoundException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("DeleteEventDataStore")
    def delete_event_data_store(
        self, context: RequestContext, event_data_store: EventDataStoreArn, **kwargs
    ) -> DeleteEventDataStoreResponse:
        """Disables the event data store specified by ``EventDataStore``, which
        accepts an event data store ARN. After you run ``DeleteEventDataStore``,
        the event data store enters a ``PENDING_DELETION`` state, and is
        automatically deleted after a wait period of seven days.
        ``TerminationProtectionEnabled`` must be set to ``False`` on the event
        data store and the ``FederationStatus`` must be ``DISABLED``. You cannot
        delete an event data store if ``TerminationProtectionEnabled`` is
        ``True`` or the ``FederationStatus`` is ``ENABLED``.

        After you run ``DeleteEventDataStore`` on an event data store, you
        cannot run ``ListQueries``, ``DescribeQuery``, or ``GetQueryResults`` on
        queries that are using an event data store in a ``PENDING_DELETION``
        state. An event data store in the ``PENDING_DELETION`` state does not
        incur costs.

        :param event_data_store: The ARN (or the ID suffix of the ARN) of the event data store to delete.
        :returns: DeleteEventDataStoreResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises EventDataStoreTerminationProtectedException:
        :raises EventDataStoreHasOngoingImportException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises ChannelExistsForEDSException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises ConflictException:
        :raises EventDataStoreFederationEnabledException:
        """
        raise NotImplementedError

    @handler("DeleteResourcePolicy")
    def delete_resource_policy(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> DeleteResourcePolicyResponse:
        """Deletes the resource-based policy attached to the CloudTrail event data
        store, dashboard, or channel.

        :param resource_arn: The Amazon Resource Name (ARN) of the CloudTrail event data store,
        dashboard, or channel you're deleting the resource-based policy from.
        :returns: DeleteResourcePolicyResponse
        :raises ResourceARNNotValidException:
        :raises ResourceNotFoundException:
        :raises ResourcePolicyNotFoundException:
        :raises ResourceTypeNotSupportedException:
        :raises ConflictException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("DeleteTrail")
    def delete_trail(self, context: RequestContext, name: String, **kwargs) -> DeleteTrailResponse:
        """Deletes a trail. This operation must be called from the Region in which
        the trail was created. ``DeleteTrail`` cannot be called on the shadow
        trails (replicated trails in other Regions) of a trail that is enabled
        in all Regions.

        :param name: Specifies the name or the CloudTrail ARN of the trail to be deleted.
        :returns: DeleteTrailResponse
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises ConflictException:
        :raises ThrottlingException:
        :raises InvalidHomeRegionException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        """
        raise NotImplementedError

    @handler("DeregisterOrganizationDelegatedAdmin")
    def deregister_organization_delegated_admin(
        self, context: RequestContext, delegated_admin_account_id: AccountId, **kwargs
    ) -> DeregisterOrganizationDelegatedAdminResponse:
        """Removes CloudTrail delegated administrator permissions from a member
        account in an organization.

        :param delegated_admin_account_id: A delegated administrator account ID.
        :returns: DeregisterOrganizationDelegatedAdminResponse
        :raises AccountNotFoundException:
        :raises AccountNotRegisteredException:
        :raises CloudTrailAccessNotEnabledException:
        :raises ConflictException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises InvalidParameterException:
        :raises NotOrganizationManagementAccountException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises OrganizationsNotInUseException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        """
        raise NotImplementedError

    @handler("DescribeQuery")
    def describe_query(
        self,
        context: RequestContext,
        event_data_store: EventDataStoreArn | None = None,
        query_id: UUID | None = None,
        query_alias: QueryAlias | None = None,
        refresh_id: RefreshId | None = None,
        event_data_store_owner_account_id: AccountId | None = None,
        **kwargs,
    ) -> DescribeQueryResponse:
        """Returns metadata about a query, including query run time in
        milliseconds, number of events scanned and matched, and query status. If
        the query results were delivered to an S3 bucket, the response also
        provides the S3 URI and the delivery status.

        You must specify either ``QueryId`` or ``QueryAlias``. Specifying the
        ``QueryAlias`` parameter returns information about the last query run
        for the alias. You can provide ``RefreshId`` along with ``QueryAlias``
        to view the query results of a dashboard query for the specified
        ``RefreshId``.

        :param event_data_store: The ARN (or the ID suffix of the ARN) of an event data store on which
        the specified query was run.
        :param query_id: The query ID.
        :param query_alias: The alias that identifies a query template.
        :param refresh_id: The ID of the dashboard refresh.
        :param event_data_store_owner_account_id: The account ID of the event data store owner.
        :returns: DescribeQueryResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises QueryIdNotFoundException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("DescribeTrails")
    def describe_trails(
        self,
        context: RequestContext,
        trail_name_list: TrailNameList | None = None,
        include_shadow_trails: Boolean | None = None,
        **kwargs,
    ) -> DescribeTrailsResponse:
        """Retrieves settings for one or more trails associated with the current
        Region for your account.

        :param trail_name_list: Specifies a list of trail names, trail ARNs, or both, of the trails to
        describe.
        :param include_shadow_trails: Specifies whether to include shadow trails in the response.
        :returns: DescribeTrailsResponse
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("DisableFederation")
    def disable_federation(
        self, context: RequestContext, event_data_store: EventDataStoreArn, **kwargs
    ) -> DisableFederationResponse:
        """Disables Lake query federation on the specified event data store. When
        you disable federation, CloudTrail disables the integration with Glue,
        Lake Formation, and Amazon Athena. After disabling Lake query
        federation, you can no longer query your event data in Amazon Athena.

        No CloudTrail Lake data is deleted when you disable federation and you
        can continue to run queries in CloudTrail Lake.

        :param event_data_store: The ARN (or ID suffix of the ARN) of the event data store for which you
        want to disable Lake query federation.
        :returns: DisableFederationResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidParameterException:
        :raises InactiveEventDataStoreException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises OrganizationsNotInUseException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises ConcurrentModificationException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("EnableFederation")
    def enable_federation(
        self,
        context: RequestContext,
        event_data_store: EventDataStoreArn,
        federation_role_arn: FederationRoleArn,
        **kwargs,
    ) -> EnableFederationResponse:
        """Enables Lake query federation on the specified event data store.
        Federating an event data store lets you view the metadata associated
        with the event data store in the Glue `Data
        Catalog <https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro>`__
        and run SQL queries against your event data using Amazon Athena. The
        table metadata stored in the Glue Data Catalog lets the Athena query
        engine know how to find, read, and process the data that you want to
        query.

        When you enable Lake query federation, CloudTrail creates a managed
        database named ``aws:cloudtrail`` (if the database doesn't already
        exist) and a managed federated table in the Glue Data Catalog. The event
        data store ID is used for the table name. CloudTrail registers the role
        ARN and event data store in `Lake
        Formation <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation-lake-formation.html>`__,
        the service responsible for allowing fine-grained access control of the
        federated resources in the Glue Data Catalog.

        For more information about Lake query federation, see `Federate an event
        data
        store <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html>`__.

        :param event_data_store: The ARN (or ID suffix of the ARN) of the event data store for which you
        want to enable Lake query federation.
        :param federation_role_arn: The ARN of the federation role to use for the event data store.
        :returns: EnableFederationResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidParameterException:
        :raises InactiveEventDataStoreException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises OrganizationsNotInUseException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises ConcurrentModificationException:
        :raises AccessDeniedException:
        :raises EventDataStoreFederationEnabledException:
        """
        raise NotImplementedError

    @handler("GenerateQuery")
    def generate_query(
        self,
        context: RequestContext,
        event_data_stores: EventDataStoreList,
        prompt: Prompt,
        **kwargs,
    ) -> GenerateQueryResponse:
        """Generates a query from a natural language prompt. This operation uses
        generative artificial intelligence (generative AI) to produce a
        ready-to-use SQL query from the prompt.

        The prompt can be a question or a statement about the event data in your
        event data store. For example, you can enter prompts like "What are my
        top errors in the past month?" and “Give me a list of users that used
        SNS.”

        The prompt must be in English. For information about limitations,
        permissions, and supported Regions, see `Create CloudTrail Lake queries
        from natural language
        prompts <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html>`__
        in the *CloudTrail* user guide.

        Do not include any personally identifying, confidential, or sensitive
        information in your prompts.

        This feature uses generative AI large language models (LLMs); we
        recommend double-checking the LLM response.

        :param event_data_stores: The ARN (or ID suffix of the ARN) of the event data store that you want
        to query.
        :param prompt: The prompt that you want to use to generate the query.
        :returns: GenerateQueryResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises GenerateResponseException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("GetChannel")
    def get_channel(
        self, context: RequestContext, channel: ChannelArn, **kwargs
    ) -> GetChannelResponse:
        """Returns information about a specific channel.

        :param channel: The ARN or ``UUID`` of a channel.
        :returns: GetChannelResponse
        :raises ChannelARNInvalidException:
        :raises ChannelNotFoundException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("GetDashboard")
    def get_dashboard(
        self, context: RequestContext, dashboard_id: DashboardArn, **kwargs
    ) -> GetDashboardResponse:
        """Returns the specified dashboard.

        :param dashboard_id: The name or ARN for the dashboard.
        :returns: GetDashboardResponse
        :raises ResourceNotFoundException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("GetEventConfiguration")
    def get_event_configuration(
        self, context: RequestContext, event_data_store: String | None = None, **kwargs
    ) -> GetEventConfigurationResponse:
        """Retrieves the current event configuration settings for the specified
        event data store, including details about maximum event size and context
        key selectors configured for the event data store.

        :param event_data_store: The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data
        store for which you want to retrieve event configuration settings.
        :returns: GetEventConfigurationResponse
        :raises CloudTrailARNInvalidException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreStatusException:
        :raises InvalidParameterException:
        :raises InvalidEventDataStoreCategoryException:
        :raises NoManagementAccountSLRExistsException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("GetEventDataStore")
    def get_event_data_store(
        self, context: RequestContext, event_data_store: EventDataStoreArn, **kwargs
    ) -> GetEventDataStoreResponse:
        """Returns information about an event data store specified as either an ARN
        or the ID portion of the ARN.

        :param event_data_store: The ARN (or ID suffix of the ARN) of the event data store about which
        you want information.
        :returns: GetEventDataStoreResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("GetEventSelectors")
    def get_event_selectors(
        self, context: RequestContext, trail_name: String, **kwargs
    ) -> GetEventSelectorsResponse:
        """Describes the settings for the event selectors that you configured for
        your trail. The information returned for your event selectors includes
        the following:

        -  If your event selector includes read-only events, write-only events,
           or all events. This applies to management events, data events, and
           network activity events.

        -  If your event selector includes management events.

        -  If your event selector includes network activity events, the event
           sources for which you are logging network activity events.

        -  If your event selector includes data events, the resources on which
           you are logging data events.

        For more information about logging management, data, and network
        activity events, see the following topics in the *CloudTrail User
        Guide*:

        -  `Logging management
           events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`__

        -  `Logging data
           events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`__

        -  `Logging network activity
           events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html>`__

        :param trail_name: Specifies the name of the trail or trail ARN.
        :returns: GetEventSelectorsResponse
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("GetImport")
    def get_import(self, context: RequestContext, import_id: UUID, **kwargs) -> GetImportResponse:
        """Returns information about a specific import.

        :param import_id: The ID for the import.
        :returns: GetImportResponse
        :raises ImportNotFoundException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("GetInsightSelectors")
    def get_insight_selectors(
        self,
        context: RequestContext,
        trail_name: String | None = None,
        event_data_store: EventDataStoreArn | None = None,
        **kwargs,
    ) -> GetInsightSelectorsResponse:
        """Describes the settings for the Insights event selectors that you
        configured for your trail or event data store. ``GetInsightSelectors``
        shows if CloudTrail Insights event logging is enabled on the trail or
        event data store, and if it is, which Insights types are enabled. If you
        run ``GetInsightSelectors`` on a trail or event data store that does not
        have Insights events enabled, the operation throws the exception
        ``InsightNotEnabledException``

        Specify either the ``EventDataStore`` parameter to get Insights event
        selectors for an event data store, or the ``TrailName`` parameter to the
        get Insights event selectors for a trail. You cannot specify these
        parameters together.

        For more information, see `Working with CloudTrail
        Insights <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html>`__
        in the *CloudTrail User Guide*.

        :param trail_name: Specifies the name of the trail or trail ARN.
        :param event_data_store: Specifies the ARN (or ID suffix of the ARN) of the event data store for
        which you want to get Insights selectors.
        :returns: GetInsightSelectorsResponse
        :raises InvalidParameterException:
        :raises InvalidParameterCombinationException:
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises InsightNotEnabledException:
        :raises NoManagementAccountSLRExistsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetQueryResults")
    def get_query_results(
        self,
        context: RequestContext,
        query_id: UUID,
        event_data_store: EventDataStoreArn | None = None,
        next_token: PaginationToken | None = None,
        max_query_results: MaxQueryResults | None = None,
        event_data_store_owner_account_id: AccountId | None = None,
        **kwargs,
    ) -> GetQueryResultsResponse:
        """Gets event data results of a query. You must specify the ``QueryID``
        value returned by the ``StartQuery`` operation.

        :param query_id: The ID of the query for which you want to get results.
        :param event_data_store: The ARN (or ID suffix of the ARN) of the event data store against which
        the query was run.
        :param next_token: A token you can use to get the next page of query results.
        :param max_query_results: The maximum number of query results to display on a single page.
        :param event_data_store_owner_account_id: The account ID of the event data store owner.
        :returns: GetQueryResultsResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InvalidMaxResultsException:
        :raises InvalidNextTokenException:
        :raises InvalidParameterException:
        :raises QueryIdNotFoundException:
        :raises InsufficientEncryptionPolicyException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("GetResourcePolicy")
    def get_resource_policy(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> GetResourcePolicyResponse:
        """Retrieves the JSON text of the resource-based policy document attached
        to the CloudTrail event data store, dashboard, or channel.

        :param resource_arn: The Amazon Resource Name (ARN) of the CloudTrail event data store,
        dashboard, or channel attached to the resource-based policy.
        :returns: GetResourcePolicyResponse
        :raises ResourceARNNotValidException:
        :raises ResourceNotFoundException:
        :raises ResourcePolicyNotFoundException:
        :raises ResourceTypeNotSupportedException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("GetTrail")
    def get_trail(self, context: RequestContext, name: String, **kwargs) -> GetTrailResponse:
        """Returns settings information for a specified trail.

        :param name: The name or the Amazon Resource Name (ARN) of the trail for which you
        want to retrieve settings information.
        :returns: GetTrailResponse
        :raises CloudTrailARNInvalidException:
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        """
        raise NotImplementedError

    @handler("GetTrailStatus")
    def get_trail_status(
        self, context: RequestContext, name: String, **kwargs
    ) -> GetTrailStatusResponse:
        """Returns a JSON-formatted list of information about the specified trail.
        Fields include information on delivery errors, Amazon SNS and Amazon S3
        errors, and start and stop logging times for each trail. This operation
        returns trail status from a single Region. To return trail status from
        all Regions, you must call the operation on each Region.

        :param name: Specifies the name or the CloudTrail ARN of the trail for which you are
        requesting status.
        :returns: GetTrailStatusResponse
        :raises CloudTrailARNInvalidException:
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        """
        raise NotImplementedError

    @handler("ListChannels")
    def list_channels(
        self,
        context: RequestContext,
        max_results: ListChannelsMaxResultsCount | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListChannelsResponse:
        """Lists the channels in the current account, and their source names.

        :param max_results: The maximum number of CloudTrail channels to display on a single page.
        :param next_token: The token to use to get the next page of results after a previous API
        call.
        :returns: ListChannelsResponse
        :raises InvalidNextTokenException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("ListDashboards", expand=False)
    def list_dashboards(
        self, context: RequestContext, request: ListDashboardsRequest, **kwargs
    ) -> ListDashboardsResponse:
        """Returns information about all dashboards in the account, in the current
        Region.

        :param name_prefix: Specify a name prefix to filter on.
        :param type: Specify a dashboard type to filter on: ``CUSTOM`` or ``MANAGED``.
        :param next_token: A token you can use to get the next page of dashboard results.
        :param max_results: The maximum number of dashboards to display on a single page.
        :returns: ListDashboardsResponse
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("ListEventDataStores")
    def list_event_data_stores(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: ListEventDataStoresMaxResultsCount | None = None,
        **kwargs,
    ) -> ListEventDataStoresResponse:
        """Returns information about all event data stores in the account, in the
        current Region.

        :param next_token: A token you can use to get the next page of event data store results.
        :param max_results: The maximum number of event data stores to display on a single page.
        :returns: ListEventDataStoresResponse
        :raises InvalidMaxResultsException:
        :raises InvalidNextTokenException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("ListImportFailures")
    def list_import_failures(
        self,
        context: RequestContext,
        import_id: UUID,
        max_results: ListImportFailuresMaxResultsCount | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListImportFailuresResponse:
        """Returns a list of failures for the specified import.

        :param import_id: The ID of the import.
        :param max_results: The maximum number of failures to display on a single page.
        :param next_token: A token you can use to get the next page of import failures.
        :returns: ListImportFailuresResponse
        :raises InvalidNextTokenException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("ListImports")
    def list_imports(
        self,
        context: RequestContext,
        max_results: ListImportsMaxResultsCount | None = None,
        destination: EventDataStoreArn | None = None,
        import_status: ImportStatus | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListImportsResponse:
        """Returns information on all imports, or a select set of imports by
        ``ImportStatus`` or ``Destination``.

        :param max_results: The maximum number of imports to display on a single page.
        :param destination: The ARN of the destination event data store.
        :param import_status: The status of the import.
        :param next_token: A token you can use to get the next page of import results.
        :returns: ListImportsResponse
        :raises EventDataStoreARNInvalidException:
        :raises InvalidNextTokenException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("ListInsightsMetricData")
    def list_insights_metric_data(
        self,
        context: RequestContext,
        event_source: EventSource,
        event_name: EventName,
        insight_type: InsightType,
        error_code: ErrorCode | None = None,
        start_time: Date | None = None,
        end_time: Date | None = None,
        period: InsightsMetricPeriod | None = None,
        data_type: InsightsMetricDataType | None = None,
        max_results: InsightsMetricMaxResults | None = None,
        next_token: InsightsMetricNextToken | None = None,
        **kwargs,
    ) -> ListInsightsMetricDataResponse:
        """Returns Insights metrics data for trails that have enabled Insights. The
        request must include the ``EventSource``, ``EventName``, and
        ``InsightType`` parameters.

        If the ``InsightType`` is set to ``ApiErrorRateInsight``, the request
        must also include the ``ErrorCode`` parameter.

        The following are the available time periods for
        ``ListInsightsMetricData``. Each cutoff is inclusive.

        -  Data points with a period of 60 seconds (1-minute) are available for
           15 days.

        -  Data points with a period of 300 seconds (5-minute) are available for
           63 days.

        -  Data points with a period of 3600 seconds (1 hour) are available for
           90 days.

        Access to the ``ListInsightsMetricData`` API operation is linked to the
        ``cloudtrail:LookupEvents`` action. To use this operation, you must have
        permissions to perform the ``cloudtrail:LookupEvents`` action.

        :param event_source: The Amazon Web Services service to which the request was made, such as
        ``iam.
        :param event_name: The name of the event, typically the Amazon Web Services API on which
        unusual levels of activity were recorded.
        :param insight_type: The type of CloudTrail Insights event, which is either
        ``ApiCallRateInsight`` or ``ApiErrorRateInsight``.
        :param error_code: Conditionally required if the ``InsightType`` parameter is set to
        ``ApiErrorRateInsight``.
        :param start_time: Specifies, in UTC, the start time for time-series data.
        :param end_time: Specifies, in UTC, the end time for time-series data.
        :param period: Granularity of data to retrieve, in seconds.
        :param data_type: Type of data points to return.
        :param max_results: The maximum number of data points to return.
        :param next_token: Returned if all datapoints can't be returned in a single call.
        :returns: ListInsightsMetricDataResponse
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("ListPublicKeys")
    def list_public_keys(
        self,
        context: RequestContext,
        start_time: Date | None = None,
        end_time: Date | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListPublicKeysResponse:
        """Returns all public keys whose private keys were used to sign the digest
        files within the specified time range. The public key is needed to
        validate digest files that were signed with its corresponding private
        key.

        CloudTrail uses different private and public key pairs per Region. Each
        digest file is signed with a private key unique to its Region. When you
        validate a digest file from a specific Region, you must look in the same
        Region for its corresponding public key.

        :param start_time: Optionally specifies, in UTC, the start of the time range to look up
        public keys for CloudTrail digest files.
        :param end_time: Optionally specifies, in UTC, the end of the time range to look up
        public keys for CloudTrail digest files.
        :param next_token: Reserved for future use.
        :returns: ListPublicKeysResponse
        :raises InvalidTimeRangeException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises InvalidTokenException:
        """
        raise NotImplementedError

    @handler("ListQueries")
    def list_queries(
        self,
        context: RequestContext,
        event_data_store: EventDataStoreArn,
        next_token: PaginationToken | None = None,
        max_results: ListQueriesMaxResultsCount | None = None,
        start_time: Date | None = None,
        end_time: Date | None = None,
        query_status: QueryStatus | None = None,
        **kwargs,
    ) -> ListQueriesResponse:
        """Returns a list of queries and query statuses for the past seven days.
        You must specify an ARN value for ``EventDataStore``. Optionally, to
        shorten the list of results, you can specify a time range, formatted as
        timestamps, by adding ``StartTime`` and ``EndTime`` parameters, and a
        ``QueryStatus`` value. Valid values for ``QueryStatus`` include
        ``QUEUED``, ``RUNNING``, ``FINISHED``, ``FAILED``, ``TIMED_OUT``, or
        ``CANCELLED``.

        :param event_data_store: The ARN (or the ID suffix of the ARN) of an event data store on which
        queries were run.
        :param next_token: A token you can use to get the next page of results.
        :param max_results: The maximum number of queries to show on a page.
        :param start_time: Use with ``EndTime`` to bound a ``ListQueries`` request, and limit its
        results to only those queries run within a specified time period.
        :param end_time: Use with ``StartTime`` to bound a ``ListQueries`` request, and limit its
        results to only those queries run within a specified time period.
        :param query_status: The status of queries that you want to return in results.
        :returns: ListQueriesResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InvalidDateRangeException:
        :raises InvalidMaxResultsException:
        :raises InvalidNextTokenException:
        :raises InvalidParameterException:
        :raises InvalidQueryStatusException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("ListTags")
    def list_tags(
        self,
        context: RequestContext,
        resource_id_list: ResourceIdList,
        next_token: String | None = None,
        **kwargs,
    ) -> ListTagsResponse:
        """Lists the tags for the specified trails, event data stores, dashboards,
        or channels in the current Region.

        :param resource_id_list: Specifies a list of trail, event data store, dashboard, or channel ARNs
        whose tags will be listed.
        :param next_token: Reserved for future use.
        :returns: ListTagsResponse
        :raises ResourceNotFoundException:
        :raises CloudTrailARNInvalidException:
        :raises EventDataStoreARNInvalidException:
        :raises ChannelARNInvalidException:
        :raises ResourceTypeNotSupportedException:
        :raises InvalidTrailNameException:
        :raises InactiveEventDataStoreException:
        :raises EventDataStoreNotFoundException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises InvalidTokenException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("ListTrails")
    def list_trails(
        self, context: RequestContext, next_token: String | None = None, **kwargs
    ) -> ListTrailsResponse:
        """Lists trails that are in the current account.

        :param next_token: The token to use to get the next page of results after a previous API
        call.
        :returns: ListTrailsResponse
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        """
        raise NotImplementedError

    @handler("LookupEvents")
    def lookup_events(
        self,
        context: RequestContext,
        lookup_attributes: LookupAttributesList | None = None,
        start_time: Date | None = None,
        end_time: Date | None = None,
        event_category: EventCategory | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> LookupEventsResponse:
        """Looks up `management
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events>`__
        or `CloudTrail Insights
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-insights-events>`__
        that are captured by CloudTrail. You can look up events that occurred in
        a Region within the last 90 days.

        ``LookupEvents`` returns recent Insights events for trails that enable
        Insights. To view Insights events for an event data store, you can run
        queries on your Insights event data store, and you can also view the
        Lake dashboard for Insights.

        Lookup supports the following attributes for management events:

        -  Amazon Web Services access key

        -  Event ID

        -  Event name

        -  Event source

        -  Read only

        -  Resource name

        -  Resource type

        -  User name

        Lookup supports the following attributes for Insights events:

        -  Event ID

        -  Event name

        -  Event source

        All attributes are optional. The default number of results returned is
        50, with a maximum of 50 possible. The response includes a token that
        you can use to get the next page of results.

        The rate of lookup requests is limited to two per second, per account,
        per Region. If this limit is exceeded, a throttling error occurs.

        :param lookup_attributes: Contains a list of lookup attributes.
        :param start_time: Specifies that only events that occur after or at the specified time are
        returned.
        :param end_time: Specifies that only events that occur before or at the specified time
        are returned.
        :param event_category: Specifies the event category.
        :param max_results: The number of events to return.
        :param next_token: The token to use to get the next page of results after a previous API
        call.
        :returns: LookupEventsResponse
        :raises InvalidLookupAttributesException:
        :raises InvalidTimeRangeException:
        :raises InvalidMaxResultsException:
        :raises InvalidNextTokenException:
        :raises InvalidEventCategoryException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        """
        raise NotImplementedError

    @handler("PutEventConfiguration")
    def put_event_configuration(
        self,
        context: RequestContext,
        max_event_size: MaxEventSize,
        context_key_selectors: ContextKeySelectors,
        event_data_store: String | None = None,
        **kwargs,
    ) -> PutEventConfigurationResponse:
        """Updates the event configuration settings for the specified event data
        store. You can update the maximum event size and context key selectors.

        :param max_event_size: The maximum allowed size for events to be stored in the specified event
        data store.
        :param context_key_selectors: A list of context key selectors that will be included to provide
        enriched event data.
        :param event_data_store: The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data
        store for which you want to update event configuration settings.
        :returns: PutEventConfigurationResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreStatusException:
        :raises InvalidEventDataStoreCategoryException:
        :raises InactiveEventDataStoreException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises ThrottlingException:
        :raises InvalidParameterException:
        :raises InvalidParameterCombinationException:
        :raises CloudTrailARNInvalidException:
        :raises ConflictException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises InsufficientIAMAccessPermissionException:
        """
        raise NotImplementedError

    @handler("PutEventSelectors")
    def put_event_selectors(
        self,
        context: RequestContext,
        trail_name: String,
        event_selectors: EventSelectors | None = None,
        advanced_event_selectors: AdvancedEventSelectors | None = None,
        **kwargs,
    ) -> PutEventSelectorsResponse:
        """Configures event selectors (also referred to as *basic event selectors*)
        or advanced event selectors for your trail. You can use either
        ``AdvancedEventSelectors`` or ``EventSelectors``, but not both. If you
        apply ``AdvancedEventSelectors`` to a trail, any existing
        ``EventSelectors`` are overwritten.

        You can use ``AdvancedEventSelectors`` to log management events, data
        events for all resource types, and network activity events.

        You can use ``EventSelectors`` to log management events and data events
        for the following resource types:

        -  ``AWS::DynamoDB::Table``

        -  ``AWS::Lambda::Function``

        -  ``AWS::S3::Object``

        You can't use ``EventSelectors`` to log network activity events.

        If you want your trail to log Insights events, be sure the event
        selector or advanced event selector enables logging of the Insights
        event types you want configured for your trail. For more information
        about logging Insights events, see `Working with CloudTrail
        Insights <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html>`__
        in the *CloudTrail User Guide*. By default, trails created without
        specific event selectors are configured to log all read and write
        management events, and no data events or network activity events.

        When an event occurs in your account, CloudTrail evaluates the event
        selectors or advanced event selectors in all trails. For each trail, if
        the event matches any event selector, the trail processes and logs the
        event. If the event doesn't match any event selector, the trail doesn't
        log the event.

        Example

        #. You create an event selector for a trail and specify that you want to
           log write-only events.

        #. The EC2 ``GetConsoleOutput`` and ``RunInstances`` API operations
           occur in your account.

        #. CloudTrail evaluates whether the events match your event selectors.

        #. The ``RunInstances`` is a write-only event and it matches your event
           selector. The trail logs the event.

        #. The ``GetConsoleOutput`` is a read-only event that doesn't match your
           event selector. The trail doesn't log the event.

        The ``PutEventSelectors`` operation must be called from the Region in
        which the trail was created; otherwise, an
        ``InvalidHomeRegionException`` exception is thrown.

        You can configure up to five event selectors for each trail.

        You can add advanced event selectors, and conditions for your advanced
        event selectors, up to a maximum of 500 values for all conditions and
        selectors on a trail. For more information, see `Logging management
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`__,
        `Logging data
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`__,
        `Logging network activity
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html>`__,
        and `Quotas in
        CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`__
        in the *CloudTrail User Guide*.

        :param trail_name: Specifies the name of the trail or trail ARN.
        :param event_selectors: Specifies the settings for your event selectors.
        :param advanced_event_selectors: Specifies the settings for advanced event selectors.
        :returns: PutEventSelectorsResponse
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises InvalidHomeRegionException:
        :raises InvalidEventSelectorsException:
        :raises ConflictException:
        :raises ThrottlingException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        """
        raise NotImplementedError

    @handler("PutInsightSelectors")
    def put_insight_selectors(
        self,
        context: RequestContext,
        insight_selectors: InsightSelectors,
        trail_name: String | None = None,
        event_data_store: EventDataStoreArn | None = None,
        insights_destination: EventDataStoreArn | None = None,
        **kwargs,
    ) -> PutInsightSelectorsResponse:
        """Lets you enable Insights event logging by specifying the Insights
        selectors that you want to enable on an existing trail or event data
        store. You also use ``PutInsightSelectors`` to turn off Insights event
        logging, by passing an empty list of Insights types. The valid Insights
        event types are ``ApiErrorRateInsight`` and ``ApiCallRateInsight``.

        To enable Insights on an event data store, you must specify the ARNs (or
        ID suffix of the ARNs) for the source event data store
        (``EventDataStore``) and the destination event data store
        (``InsightsDestination``). The source event data store logs management
        events and enables Insights. The destination event data store logs
        Insights events based upon the management event activity of the source
        event data store. The source and destination event data stores must
        belong to the same Amazon Web Services account.

        To log Insights events for a trail, you must specify the name
        (``TrailName``) of the CloudTrail trail for which you want to change or
        add Insights selectors.

        To log CloudTrail Insights events on API call volume, the trail or event
        data store must log ``write`` management events. To log CloudTrail
        Insights events on API error rate, the trail or event data store must
        log ``read`` or ``write`` management events. You can call
        ``GetEventSelectors`` on a trail to check whether the trail logs
        management events. You can call ``GetEventDataStore`` on an event data
        store to check whether the event data store logs management events.

        For more information, see `Working with CloudTrail
        Insights <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html>`__
        in the *CloudTrail User Guide*.

        :param insight_selectors: A JSON string that contains the Insights types you want to log on a
        trail or event data store.
        :param trail_name: The name of the CloudTrail trail for which you want to change or add
        Insights selectors.
        :param event_data_store: The ARN (or ID suffix of the ARN) of the source event data store for
        which you want to change or add Insights selectors.
        :param insights_destination: The ARN (or ID suffix of the ARN) of the destination event data store
        that logs Insights events.
        :returns: PutInsightSelectorsResponse
        :raises InvalidParameterException:
        :raises InvalidParameterCombinationException:
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises InvalidHomeRegionException:
        :raises InvalidInsightSelectorsException:
        :raises InsufficientS3BucketPolicyException:
        :raises InsufficientEncryptionPolicyException:
        :raises S3BucketDoesNotExistException:
        :raises KmsException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("PutResourcePolicy")
    def put_resource_policy(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        resource_policy: ResourcePolicy,
        **kwargs,
    ) -> PutResourcePolicyResponse:
        """Attaches a resource-based permission policy to a CloudTrail event data
        store, dashboard, or channel. For more information about resource-based
        policies, see `CloudTrail resource-based policy
        examples <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html>`__
        in the *CloudTrail User Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the CloudTrail event data store,
        dashboard, or channel attached to the resource-based policy.
        :param resource_policy: A JSON-formatted string for an Amazon Web Services resource-based
        policy.
        :returns: PutResourcePolicyResponse
        :raises ResourceARNNotValidException:
        :raises ResourcePolicyNotValidException:
        :raises ResourceNotFoundException:
        :raises ResourceTypeNotSupportedException:
        :raises ConflictException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("RegisterOrganizationDelegatedAdmin")
    def register_organization_delegated_admin(
        self, context: RequestContext, member_account_id: AccountId, **kwargs
    ) -> RegisterOrganizationDelegatedAdminResponse:
        """Registers an organization’s member account as the CloudTrail `delegated
        administrator <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delegated-administrator.html>`__.

        :param member_account_id: An organization member account ID that you want to designate as a
        delegated administrator.
        :returns: RegisterOrganizationDelegatedAdminResponse
        :raises AccountRegisteredException:
        :raises AccountNotFoundException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises InvalidParameterException:
        :raises CannotDelegateManagementAccountException:
        :raises CloudTrailAccessNotEnabledException:
        :raises ConflictException:
        :raises DelegatedAdminAccountLimitExceededException:
        :raises NotOrganizationManagementAccountException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises OrganizationsNotInUseException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises InsufficientIAMAccessPermissionException:
        """
        raise NotImplementedError

    @handler("RemoveTags")
    def remove_tags(
        self, context: RequestContext, resource_id: String, tags_list: TagsList, **kwargs
    ) -> RemoveTagsResponse:
        """Removes the specified tags from a trail, event data store, dashboard, or
        channel.

        :param resource_id: Specifies the ARN of the trail, event data store, dashboard, or channel
        from which tags should be removed.
        :param tags_list: Specifies a list of tags to be removed.
        :returns: RemoveTagsResponse
        :raises ResourceNotFoundException:
        :raises CloudTrailARNInvalidException:
        :raises EventDataStoreARNInvalidException:
        :raises ChannelARNInvalidException:
        :raises ResourceTypeNotSupportedException:
        :raises InvalidTrailNameException:
        :raises InvalidTagParameterException:
        :raises InactiveEventDataStoreException:
        :raises EventDataStoreNotFoundException:
        :raises ChannelNotFoundException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("RestoreEventDataStore")
    def restore_event_data_store(
        self, context: RequestContext, event_data_store: EventDataStoreArn, **kwargs
    ) -> RestoreEventDataStoreResponse:
        """Restores a deleted event data store specified by ``EventDataStore``,
        which accepts an event data store ARN. You can only restore a deleted
        event data store within the seven-day wait period after deletion.
        Restoring an event data store can take several minutes, depending on the
        size of the event data store.

        :param event_data_store: The ARN (or the ID suffix of the ARN) of the event data store that you
        want to restore.
        :returns: RestoreEventDataStoreResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises EventDataStoreMaxLimitExceededException:
        :raises InvalidEventDataStoreStatusException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises OrganizationsNotInUseException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises OrganizationNotInAllFeaturesModeException:
        """
        raise NotImplementedError

    @handler("SearchSampleQueries")
    def search_sample_queries(
        self,
        context: RequestContext,
        search_phrase: SearchSampleQueriesSearchPhrase,
        max_results: SearchSampleQueriesMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> SearchSampleQueriesResponse:
        """Searches sample queries and returns a list of sample queries that are
        sorted by relevance. To search for sample queries, provide a natural
        language ``SearchPhrase`` in English.

        :param search_phrase: The natural language phrase to use for the semantic search.
        :param max_results: The maximum number of results to return on a single page.
        :param next_token: A token you can use to get the next page of results.
        :returns: SearchSampleQueriesResponse
        :raises InvalidParameterException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        """
        raise NotImplementedError

    @handler("StartDashboardRefresh")
    def start_dashboard_refresh(
        self,
        context: RequestContext,
        dashboard_id: DashboardArn,
        query_parameter_values: QueryParameterValues | None = None,
        **kwargs,
    ) -> StartDashboardRefreshResponse:
        """Starts a refresh of the specified dashboard.

        Each time a dashboard is refreshed, CloudTrail runs queries to populate
        the dashboard's widgets. CloudTrail must be granted permissions to run
        the ``StartQuery`` operation on your behalf. To provide permissions, run
        the ``PutResourcePolicy`` operation to attach a resource-based policy to
        each event data store. For more information, see `Example: Allow
        CloudTrail to run queries to populate a
        dashboard <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard>`__
        in the *CloudTrail User Guide*.

        :param dashboard_id: The name or ARN of the dashboard.
        :param query_parameter_values: The query parameter values for the dashboard

        For custom dashboards, the following query parameters are valid:
        ``$StartTime$``, ``$EndTime$``, and ``$Period$``.
        :returns: StartDashboardRefreshResponse
        :raises ResourceNotFoundException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises ServiceQuotaExceededException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("StartEventDataStoreIngestion")
    def start_event_data_store_ingestion(
        self, context: RequestContext, event_data_store: EventDataStoreArn, **kwargs
    ) -> StartEventDataStoreIngestionResponse:
        """Starts the ingestion of live events on an event data store specified as
        either an ARN or the ID portion of the ARN. To start ingestion, the
        event data store ``Status`` must be ``STOPPED_INGESTION`` and the
        ``eventCategory`` must be ``Management``, ``Data``, ``NetworkActivity``,
        or ``ConfigurationItem``.

        :param event_data_store: The ARN (or ID suffix of the ARN) of the event data store for which you
        want to start ingestion.
        :returns: StartEventDataStoreIngestionResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreStatusException:
        :raises InvalidParameterException:
        :raises InvalidEventDataStoreCategoryException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("StartImport")
    def start_import(
        self,
        context: RequestContext,
        destinations: ImportDestinations | None = None,
        import_source: ImportSource | None = None,
        start_event_time: Date | None = None,
        end_event_time: Date | None = None,
        import_id: UUID | None = None,
        **kwargs,
    ) -> StartImportResponse:
        """Starts an import of logged trail events from a source S3 bucket to a
        destination event data store. By default, CloudTrail only imports events
        contained in the S3 bucket's ``CloudTrail`` prefix and the prefixes
        inside the ``CloudTrail`` prefix, and does not check prefixes for other
        Amazon Web Services services. If you want to import CloudTrail events
        contained in another prefix, you must include the prefix in the
        ``S3LocationUri``. For more considerations about importing trail events,
        see `Considerations for copying trail
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake.html#cloudtrail-trail-copy-considerations>`__
        in the *CloudTrail User Guide*.

        When you start a new import, the ``Destinations`` and ``ImportSource``
        parameters are required. Before starting a new import, disable any
        access control lists (ACLs) attached to the source S3 bucket. For more
        information about disabling ACLs, see `Controlling ownership of objects
        and disabling ACLs for your
        bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html>`__.

        When you retry an import, the ``ImportID`` parameter is required.

        If the destination event data store is for an organization, you must use
        the management account to import trail events. You cannot use the
        delegated administrator account for the organization.

        :param destinations: The ARN of the destination event data store.
        :param import_source: The source S3 bucket for the import.
        :param start_event_time: Use with ``EndEventTime`` to bound a ``StartImport`` request, and limit
        imported trail events to only those events logged within a specified
        time period.
        :param end_event_time: Use with ``StartEventTime`` to bound a ``StartImport`` request, and
        limit imported trail events to only those events logged within a
        specified time period.
        :param import_id: The ID of the import.
        :returns: StartImportResponse
        :raises AccountHasOngoingImportException:
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreStatusException:
        :raises InvalidEventDataStoreCategoryException:
        :raises InactiveEventDataStoreException:
        :raises InvalidImportSourceException:
        :raises ImportNotFoundException:
        :raises InvalidParameterException:
        :raises InsufficientEncryptionPolicyException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("StartLogging")
    def start_logging(
        self, context: RequestContext, name: String, **kwargs
    ) -> StartLoggingResponse:
        """Starts the recording of Amazon Web Services API calls and log file
        delivery for a trail. For a trail that is enabled in all Regions, this
        operation must be called from the Region in which the trail was created.
        This operation cannot be called on the shadow trails (replicated trails
        in other Regions) of a trail that is enabled in all Regions.

        :param name: Specifies the name or the CloudTrail ARN of the trail for which
        CloudTrail logs Amazon Web Services API calls.
        :returns: StartLoggingResponse
        :raises CloudTrailARNInvalidException:
        :raises ConflictException:
        :raises ThrottlingException:
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises InvalidHomeRegionException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        """
        raise NotImplementedError

    @handler("StartQuery")
    def start_query(
        self,
        context: RequestContext,
        query_statement: QueryStatement | None = None,
        delivery_s3_uri: DeliveryS3Uri | None = None,
        query_alias: QueryAlias | None = None,
        query_parameters: QueryParameters | None = None,
        event_data_store_owner_account_id: AccountId | None = None,
        **kwargs,
    ) -> StartQueryResponse:
        """Starts a CloudTrail Lake query. Use the ``QueryStatement`` parameter to
        provide your SQL query, enclosed in single quotation marks. Use the
        optional ``DeliveryS3Uri`` parameter to deliver the query results to an
        S3 bucket.

        ``StartQuery`` requires you specify either the ``QueryStatement``
        parameter, or a ``QueryAlias`` and any ``QueryParameters``. In the
        current release, the ``QueryAlias`` and ``QueryParameters`` parameters
        are used only for the queries that populate the CloudTrail Lake
        dashboards.

        :param query_statement: The SQL code of your query.
        :param delivery_s3_uri: The URI for the S3 bucket where CloudTrail delivers the query results.
        :param query_alias: The alias that identifies a query template.
        :param query_parameters: The query parameters for the specified ``QueryAlias``.
        :param event_data_store_owner_account_id: The account ID of the event data store owner.
        :returns: StartQueryResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises InvalidQueryStatementException:
        :raises MaxConcurrentQueriesException:
        :raises InsufficientEncryptionPolicyException:
        :raises InvalidS3PrefixException:
        :raises InvalidS3BucketNameException:
        :raises InsufficientS3BucketPolicyException:
        :raises S3BucketDoesNotExistException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NoManagementAccountSLRExistsException:
        """
        raise NotImplementedError

    @handler("StopEventDataStoreIngestion")
    def stop_event_data_store_ingestion(
        self, context: RequestContext, event_data_store: EventDataStoreArn, **kwargs
    ) -> StopEventDataStoreIngestionResponse:
        """Stops the ingestion of live events on an event data store specified as
        either an ARN or the ID portion of the ARN. To stop ingestion, the event
        data store ``Status`` must be ``ENABLED`` and the ``eventCategory`` must
        be ``Management``, ``Data``, ``NetworkActivity``, or
        ``ConfigurationItem``.

        :param event_data_store: The ARN (or ID suffix of the ARN) of the event data store for which you
        want to stop ingestion.
        :returns: StopEventDataStoreIngestionResponse
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreStatusException:
        :raises InvalidParameterException:
        :raises InvalidEventDataStoreCategoryException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("StopImport")
    def stop_import(self, context: RequestContext, import_id: UUID, **kwargs) -> StopImportResponse:
        """Stops a specified import.

        :param import_id: The ID of the import.
        :returns: StopImportResponse
        :raises ImportNotFoundException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("StopLogging")
    def stop_logging(self, context: RequestContext, name: String, **kwargs) -> StopLoggingResponse:
        """Suspends the recording of Amazon Web Services API calls and log file
        delivery for the specified trail. Under most circumstances, there is no
        need to use this action. You can update a trail without stopping it
        first. This action is the only way to stop recording. For a trail
        enabled in all Regions, this operation must be called from the Region in
        which the trail was created, or an ``InvalidHomeRegionException`` will
        occur. This operation cannot be called on the shadow trails (replicated
        trails in other Regions) of a trail enabled in all Regions.

        :param name: Specifies the name or the CloudTrail ARN of the trail for which
        CloudTrail will stop logging Amazon Web Services API calls.
        :returns: StopLoggingResponse
        :raises TrailNotFoundException:
        :raises InvalidTrailNameException:
        :raises CloudTrailARNInvalidException:
        :raises ConflictException:
        :raises ThrottlingException:
        :raises InvalidHomeRegionException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        """
        raise NotImplementedError

    @handler("UpdateChannel")
    def update_channel(
        self,
        context: RequestContext,
        channel: ChannelArn,
        destinations: Destinations | None = None,
        name: ChannelName | None = None,
        **kwargs,
    ) -> UpdateChannelResponse:
        """Updates a channel specified by a required channel ARN or UUID.

        :param channel: The ARN or ID (the ARN suffix) of the channel that you want to update.
        :param destinations: The ARNs of event data stores that you want to log events arriving
        through the channel.
        :param name: Changes the name of the channel.
        :returns: UpdateChannelResponse
        :raises ChannelARNInvalidException:
        :raises ChannelNotFoundException:
        :raises ChannelAlreadyExistsException:
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventDataStoreCategoryException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("UpdateDashboard")
    def update_dashboard(
        self,
        context: RequestContext,
        dashboard_id: DashboardArn,
        widgets: RequestWidgetList | None = None,
        refresh_schedule: RefreshSchedule | None = None,
        termination_protection_enabled: TerminationProtectionEnabled | None = None,
        **kwargs,
    ) -> UpdateDashboardResponse:
        """Updates the specified dashboard.

        To set a refresh schedule, CloudTrail must be granted permissions to run
        the ``StartDashboardRefresh`` operation to refresh the dashboard on your
        behalf. To provide permissions, run the ``PutResourcePolicy`` operation
        to attach a resource-based policy to the dashboard. For more
        information, see `Resource-based policy example for a
        dashboard <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards>`__
        in the *CloudTrail User Guide*.

        CloudTrail runs queries to populate the dashboard's widgets during a
        manual or scheduled refresh. CloudTrail must be granted permissions to
        run the ``StartQuery`` operation on your behalf. To provide permissions,
        run the ``PutResourcePolicy`` operation to attach a resource-based
        policy to each event data store. For more information, see `Example:
        Allow CloudTrail to run queries to populate a
        dashboard <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard>`__
        in the *CloudTrail User Guide*.

        :param dashboard_id: The name or ARN of the dashboard.
        :param widgets: An array of widgets for the dashboard.
        :param refresh_schedule: The refresh schedule configuration for the dashboard.
        :param termination_protection_enabled: Specifies whether termination protection is enabled for the dashboard.
        :returns: UpdateDashboardResponse
        :raises ConflictException:
        :raises ResourceNotFoundException:
        :raises EventDataStoreNotFoundException:
        :raises InactiveEventDataStoreException:
        :raises InsufficientEncryptionPolicyException:
        :raises InvalidQueryStatementException:
        :raises ServiceQuotaExceededException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("UpdateEventDataStore")
    def update_event_data_store(
        self,
        context: RequestContext,
        event_data_store: EventDataStoreArn,
        name: EventDataStoreName | None = None,
        advanced_event_selectors: AdvancedEventSelectors | None = None,
        multi_region_enabled: Boolean | None = None,
        organization_enabled: Boolean | None = None,
        retention_period: RetentionPeriod | None = None,
        termination_protection_enabled: TerminationProtectionEnabled | None = None,
        kms_key_id: EventDataStoreKmsKeyId | None = None,
        billing_mode: BillingMode | None = None,
        **kwargs,
    ) -> UpdateEventDataStoreResponse:
        """Updates an event data store. The required ``EventDataStore`` value is an
        ARN or the ID portion of the ARN. Other parameters are optional, but at
        least one optional parameter must be specified, or CloudTrail throws an
        error. ``RetentionPeriod`` is in days, and valid values are integers
        between 7 and 3653 if the ``BillingMode`` is set to
        ``EXTENDABLE_RETENTION_PRICING``, or between 7 and 2557 if
        ``BillingMode`` is set to ``FIXED_RETENTION_PRICING``. By default,
        ``TerminationProtection`` is enabled.

        For event data stores for CloudTrail events, ``AdvancedEventSelectors``
        includes or excludes management, data, or network activity events in
        your event data store. For more information about
        ``AdvancedEventSelectors``, see
        `AdvancedEventSelectors <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html>`__.

        For event data stores for CloudTrail Insights events, Config
        configuration items, Audit Manager evidence, or non-Amazon Web Services
        events, ``AdvancedEventSelectors`` includes events of that type in your
        event data store.

        :param event_data_store: The ARN (or the ID suffix of the ARN) of the event data store that you
        want to update.
        :param name: The event data store name.
        :param advanced_event_selectors: The advanced event selectors used to select events for the event data
        store.
        :param multi_region_enabled: Specifies whether an event data store collects events from all Regions,
        or only from the Region in which it was created.
        :param organization_enabled: Specifies whether an event data store collects events logged for an
        organization in Organizations.
        :param retention_period: The retention period of the event data store, in days.
        :param termination_protection_enabled: Indicates that termination protection is enabled and the event data
        store cannot be automatically deleted.
        :param kms_key_id: Specifies the KMS key ID to use to encrypt the events delivered by
        CloudTrail.
        :param billing_mode: You can't change the billing mode from ``EXTENDABLE_RETENTION_PRICING``
        to ``FIXED_RETENTION_PRICING``.
        :returns: UpdateEventDataStoreResponse
        :raises EventDataStoreAlreadyExistsException:
        :raises EventDataStoreARNInvalidException:
        :raises EventDataStoreNotFoundException:
        :raises InvalidEventSelectorsException:
        :raises InvalidInsightSelectorsException:
        :raises EventDataStoreHasOngoingImportException:
        :raises InactiveEventDataStoreException:
        :raises InvalidParameterException:
        :raises OperationNotPermittedException:
        :raises UnsupportedOperationException:
        :raises InsufficientEncryptionPolicyException:
        :raises InvalidKmsKeyIdException:
        :raises KmsKeyNotFoundException:
        :raises KmsException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises OrganizationsNotInUseException:
        :raises NotOrganizationMasterAccountException:
        :raises NoManagementAccountSLRExistsException:
        :raises OrganizationNotInAllFeaturesModeException:
        """
        raise NotImplementedError

    @handler("UpdateTrail")
    def update_trail(
        self,
        context: RequestContext,
        name: String,
        s3_bucket_name: String | None = None,
        s3_key_prefix: String | None = None,
        sns_topic_name: String | None = None,
        include_global_service_events: Boolean | None = None,
        is_multi_region_trail: Boolean | None = None,
        enable_log_file_validation: Boolean | None = None,
        cloud_watch_logs_log_group_arn: String | None = None,
        cloud_watch_logs_role_arn: String | None = None,
        kms_key_id: String | None = None,
        is_organization_trail: Boolean | None = None,
        **kwargs,
    ) -> UpdateTrailResponse:
        """Updates trail settings that control what events you are logging, and how
        to handle log files. Changes to a trail do not require stopping the
        CloudTrail service. Use this action to designate an existing bucket for
        log delivery. If the existing bucket has previously been a target for
        CloudTrail log files, an IAM policy exists for the bucket.
        ``UpdateTrail`` must be called from the Region in which the trail was
        created; otherwise, an ``InvalidHomeRegionException`` is thrown.

        :param name: Specifies the name of the trail or trail ARN.
        :param s3_bucket_name: Specifies the name of the Amazon S3 bucket designated for publishing log
        files.
        :param s3_key_prefix: Specifies the Amazon S3 key prefix that comes after the name of the
        bucket you have designated for log file delivery.
        :param sns_topic_name: Specifies the name or ARN of the Amazon SNS topic defined for
        notification of log file delivery.
        :param include_global_service_events: Specifies whether the trail is publishing events from global services
        such as IAM to the log files.
        :param is_multi_region_trail: Specifies whether the trail applies only to the current Region or to all
        Regions.
        :param enable_log_file_validation: Specifies whether log file validation is enabled.
        :param cloud_watch_logs_log_group_arn: Specifies a log group name using an Amazon Resource Name (ARN), a unique
        identifier that represents the log group to which CloudTrail logs are
        delivered.
        :param cloud_watch_logs_role_arn: Specifies the role for the CloudWatch Logs endpoint to assume to write
        to a user's log group.
        :param kms_key_id: Specifies the KMS key ID to use to encrypt the logs delivered by
        CloudTrail.
        :param is_organization_trail: Specifies whether the trail is applied to all accounts in an
        organization in Organizations, or only for the current Amazon Web
        Services account.
        :returns: UpdateTrailResponse
        :raises S3BucketDoesNotExistException:
        :raises InsufficientS3BucketPolicyException:
        :raises InsufficientSnsTopicPolicyException:
        :raises InsufficientEncryptionPolicyException:
        :raises TrailNotFoundException:
        :raises InvalidS3BucketNameException:
        :raises InvalidS3PrefixException:
        :raises InvalidSnsTopicNameException:
        :raises InvalidKmsKeyIdException:
        :raises InvalidTrailNameException:
        :raises TrailNotProvidedException:
        :raises InvalidEventSelectorsException:
        :raises CloudTrailARNInvalidException:
        :raises ConflictException:
        :raises ThrottlingException:
        :raises InvalidParameterCombinationException:
        :raises InvalidHomeRegionException:
        :raises KmsKeyNotFoundException:
        :raises KmsKeyDisabledException:
        :raises KmsException:
        :raises InvalidCloudWatchLogsLogGroupArnException:
        :raises InvalidCloudWatchLogsRoleArnException:
        :raises CloudWatchLogsDeliveryUnavailableException:
        :raises UnsupportedOperationException:
        :raises OperationNotPermittedException:
        :raises CloudTrailAccessNotEnabledException:
        :raises InsufficientDependencyServiceAccessPermissionException:
        :raises OrganizationsNotInUseException:
        :raises NotOrganizationMasterAccountException:
        :raises OrganizationNotInAllFeaturesModeException:
        :raises NoManagementAccountSLRExistsException:
        :raises CloudTrailInvalidClientTokenIdException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError
