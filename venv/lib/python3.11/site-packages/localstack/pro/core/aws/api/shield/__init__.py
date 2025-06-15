from datetime import datetime
from enum import StrEnum
from typing import List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AttackId = str
ContactNotes = str
Double = float
EmailAddress = str
HealthCheckArn = str
HealthCheckId = str
Integer = int
LimitType = str
LogBucket = str
MaxResults = int
PhoneNumber = str
ProtectionGroupId = str
ProtectionId = str
ProtectionName = str
ResourceArn = str
RoleArn = str
String = str
TagKey = str
TagValue = str
Token = str
errorMessage = str


class ApplicationLayerAutomaticResponseStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AttackLayer(StrEnum):
    NETWORK = "NETWORK"
    APPLICATION = "APPLICATION"


class AttackPropertyIdentifier(StrEnum):
    DESTINATION_URL = "DESTINATION_URL"
    REFERRER = "REFERRER"
    SOURCE_ASN = "SOURCE_ASN"
    SOURCE_COUNTRY = "SOURCE_COUNTRY"
    SOURCE_IP_ADDRESS = "SOURCE_IP_ADDRESS"
    SOURCE_USER_AGENT = "SOURCE_USER_AGENT"
    WORDPRESS_PINGBACK_REFLECTOR = "WORDPRESS_PINGBACK_REFLECTOR"
    WORDPRESS_PINGBACK_SOURCE = "WORDPRESS_PINGBACK_SOURCE"


class AutoRenew(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ProactiveEngagementStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    PENDING = "PENDING"


class ProtectedResourceType(StrEnum):
    CLOUDFRONT_DISTRIBUTION = "CLOUDFRONT_DISTRIBUTION"
    ROUTE_53_HOSTED_ZONE = "ROUTE_53_HOSTED_ZONE"
    ELASTIC_IP_ALLOCATION = "ELASTIC_IP_ALLOCATION"
    CLASSIC_LOAD_BALANCER = "CLASSIC_LOAD_BALANCER"
    APPLICATION_LOAD_BALANCER = "APPLICATION_LOAD_BALANCER"
    GLOBAL_ACCELERATOR = "GLOBAL_ACCELERATOR"


class ProtectionGroupAggregation(StrEnum):
    SUM = "SUM"
    MEAN = "MEAN"
    MAX = "MAX"


class ProtectionGroupPattern(StrEnum):
    ALL = "ALL"
    ARBITRARY = "ARBITRARY"
    BY_RESOURCE_TYPE = "BY_RESOURCE_TYPE"


class SubResourceType(StrEnum):
    IP = "IP"
    URL = "URL"


class SubscriptionState(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Unit(StrEnum):
    BITS = "BITS"
    BYTES = "BYTES"
    PACKETS = "PACKETS"
    REQUESTS = "REQUESTS"


class ValidationExceptionReason(StrEnum):
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    OTHER = "OTHER"


class AccessDeniedException(ServiceException):
    """Exception that indicates the specified ``AttackId`` does not exist, or
    the requester does not have the appropriate permissions to access the
    ``AttackId``.
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class AccessDeniedForDependencyException(ServiceException):
    """In order to grant the necessary access to the Shield Response Team (SRT)
    the user submitting the request must have the ``iam:PassRole``
    permission. This error indicates the user did not have the appropriate
    permissions. For more information, see `Granting a User Permissions to
    Pass a Role to an Amazon Web Services
    Service <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`__.
    """

    code: str = "AccessDeniedForDependencyException"
    sender_fault: bool = False
    status_code: int = 400


class InternalErrorException(ServiceException):
    """Exception that indicates that a problem occurred with the service
    infrastructure. You can retry the request.
    """

    code: str = "InternalErrorException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOperationException(ServiceException):
    """Exception that indicates that the operation would not cause any change
    to occur.
    """

    code: str = "InvalidOperationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidPaginationTokenException(ServiceException):
    """Exception that indicates that the ``NextToken`` specified in the request
    is invalid. Submit the request using the ``NextToken`` value that was
    returned in the prior response.
    """

    code: str = "InvalidPaginationTokenException"
    sender_fault: bool = False
    status_code: int = 400


class ValidationExceptionField(TypedDict, total=False):
    """Provides information about a particular parameter passed inside a
    request that resulted in an exception.
    """

    name: String
    message: String


ValidationExceptionFieldList = List[ValidationExceptionField]


class InvalidParameterException(ServiceException):
    """Exception that indicates that the parameters passed to the API are
    invalid. If available, this exception includes details in additional
    properties.
    """

    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400
    reason: Optional[ValidationExceptionReason]
    fields: Optional[ValidationExceptionFieldList]


class InvalidResourceException(ServiceException):
    """Exception that indicates that the resource is invalid. You might not
    have access to the resource, or the resource might not exist.
    """

    code: str = "InvalidResourceException"
    sender_fault: bool = False
    status_code: int = 400


LimitNumber = int


class LimitsExceededException(ServiceException):
    """Exception that indicates that the operation would exceed a limit."""

    code: str = "LimitsExceededException"
    sender_fault: bool = False
    status_code: int = 400
    Type: Optional[LimitType]
    Limit: Optional[LimitNumber]


class LockedSubscriptionException(ServiceException):
    """You are trying to update a subscription that has not yet completed the
    1-year commitment. You can change the ``AutoRenew`` parameter during the
    last 30 days of your subscription. This exception indicates that you are
    attempting to change ``AutoRenew`` prior to that period.
    """

    code: str = "LockedSubscriptionException"
    sender_fault: bool = False
    status_code: int = 400


class NoAssociatedRoleException(ServiceException):
    """The ARN of the role that you specified does not exist."""

    code: str = "NoAssociatedRoleException"
    sender_fault: bool = False
    status_code: int = 400


class OptimisticLockException(ServiceException):
    """Exception that indicates that the resource state has been modified by
    another client. Retrieve the resource and then retry your request.
    """

    code: str = "OptimisticLockException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceAlreadyExistsException(ServiceException):
    """Exception indicating the specified resource already exists. If
    available, this exception includes details in additional properties.
    """

    code: str = "ResourceAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400
    resourceType: Optional[String]


class ResourceNotFoundException(ServiceException):
    """Exception indicating the specified resource does not exist. If
    available, this exception includes details in additional properties.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400
    resourceType: Optional[String]


class CountAction(TypedDict, total=False):
    """Specifies that Shield Advanced should configure its WAF rules with the
    WAF ``Count`` action.

    This is only used in the context of the ``ResponseAction`` setting.

    JSON specification: ``"Count": {}``
    """

    pass


class BlockAction(TypedDict, total=False):
    """Specifies that Shield Advanced should configure its WAF rules with the
    WAF ``Block`` action.

    This is only used in the context of the ``ResponseAction`` setting.

    JSON specification: ``"Block": {}``
    """

    pass


class ResponseAction(TypedDict, total=False):
    """Specifies the action setting that Shield Advanced should use in the WAF
    rules that it creates on behalf of the protected resource in response to
    DDoS attacks. You specify this as part of the configuration for the
    automatic application layer DDoS mitigation feature, when you enable or
    update automatic mitigation. Shield Advanced creates the WAF rules in a
    Shield Advanced-managed rule group, inside the web ACL that you have
    associated with the resource.
    """

    Block: Optional[BlockAction]
    Count: Optional[CountAction]


class ApplicationLayerAutomaticResponseConfiguration(TypedDict, total=False):
    """The automatic application layer DDoS mitigation settings for a
    Protection. This configuration determines whether Shield Advanced
    automatically manages rules in the web ACL in order to respond to
    application layer events that Shield Advanced determines to be DDoS
    attacks.
    """

    Status: ApplicationLayerAutomaticResponseStatus
    Action: ResponseAction


class AssociateDRTLogBucketRequest(ServiceRequest):
    LogBucket: LogBucket


class AssociateDRTLogBucketResponse(TypedDict, total=False):
    pass


class AssociateDRTRoleRequest(ServiceRequest):
    RoleArn: RoleArn


class AssociateDRTRoleResponse(TypedDict, total=False):
    pass


class AssociateHealthCheckRequest(ServiceRequest):
    ProtectionId: ProtectionId
    HealthCheckArn: HealthCheckArn


class AssociateHealthCheckResponse(TypedDict, total=False):
    pass


class EmergencyContact(TypedDict, total=False):
    """Contact information that the SRT can use to contact you if you have
    proactive engagement enabled, for escalations to the SRT and to initiate
    proactive customer support.
    """

    EmailAddress: EmailAddress
    PhoneNumber: Optional[PhoneNumber]
    ContactNotes: Optional[ContactNotes]


EmergencyContactList = List[EmergencyContact]


class AssociateProactiveEngagementDetailsRequest(ServiceRequest):
    EmergencyContactList: EmergencyContactList


class AssociateProactiveEngagementDetailsResponse(TypedDict, total=False):
    pass


class Mitigation(TypedDict, total=False):
    """The mitigation applied to a DDoS attack."""

    MitigationName: Optional[String]


MitigationList = List[Mitigation]
Long = int


class Contributor(TypedDict, total=False):
    """A contributor to the attack and their contribution."""

    Name: Optional[String]
    Value: Optional[Long]


TopContributors = List[Contributor]


class AttackProperty(TypedDict, total=False):
    """Details of a Shield event. This is provided as part of an AttackDetail."""

    AttackLayer: Optional[AttackLayer]
    AttackPropertyIdentifier: Optional[AttackPropertyIdentifier]
    TopContributors: Optional[TopContributors]
    Unit: Optional[Unit]
    Total: Optional[Long]


AttackProperties = List[AttackProperty]


class SummarizedCounter(TypedDict, total=False):
    """The counter that describes a DDoS attack."""

    Name: Optional[String]
    Max: Optional[Double]
    Average: Optional[Double]
    Sum: Optional[Double]
    N: Optional[Integer]
    Unit: Optional[String]


SummarizedCounterList = List[SummarizedCounter]
AttackTimestamp = datetime


class SummarizedAttackVector(TypedDict, total=False):
    """A summary of information about the attack."""

    VectorType: String
    VectorCounters: Optional[SummarizedCounterList]


SummarizedAttackVectorList = List[SummarizedAttackVector]


class SubResourceSummary(TypedDict, total=False):
    """The attack information for the specified SubResource."""

    Type: Optional[SubResourceType]
    Id: Optional[String]
    AttackVectors: Optional[SummarizedAttackVectorList]
    Counters: Optional[SummarizedCounterList]


SubResourceSummaryList = List[SubResourceSummary]


class AttackDetail(TypedDict, total=False):
    """The details of a DDoS attack."""

    AttackId: Optional[AttackId]
    ResourceArn: Optional[ResourceArn]
    SubResources: Optional[SubResourceSummaryList]
    StartTime: Optional[AttackTimestamp]
    EndTime: Optional[AttackTimestamp]
    AttackCounters: Optional[SummarizedCounterList]
    AttackProperties: Optional[AttackProperties]
    Mitigations: Optional[MitigationList]


class AttackVolumeStatistics(TypedDict, total=False):
    """Statistics objects for the various data types in AttackVolume."""

    Max: Double


class AttackVolume(TypedDict, total=False):
    """Information about the volume of attacks during the time period, included
    in an AttackStatisticsDataItem. If the accompanying ``AttackCount`` in
    the statistics object is zero, this setting might be empty.
    """

    BitsPerSecond: Optional[AttackVolumeStatistics]
    PacketsPerSecond: Optional[AttackVolumeStatistics]
    RequestsPerSecond: Optional[AttackVolumeStatistics]


class AttackStatisticsDataItem(TypedDict, total=False):
    """A single attack statistics data record. This is returned by
    DescribeAttackStatistics along with a time range indicating the time
    period that the attack statistics apply to.
    """

    AttackVolume: Optional[AttackVolume]
    AttackCount: Long


AttackStatisticsDataList = List[AttackStatisticsDataItem]


class AttackVectorDescription(TypedDict, total=False):
    """Describes the attack."""

    VectorType: String


AttackVectorDescriptionList = List[AttackVectorDescription]


class AttackSummary(TypedDict, total=False):
    """Summarizes all DDoS attacks for a specified time period."""

    AttackId: Optional[String]
    ResourceArn: Optional[String]
    StartTime: Optional[AttackTimestamp]
    EndTime: Optional[AttackTimestamp]
    AttackVectors: Optional[AttackVectorDescriptionList]


AttackSummaries = List[AttackSummary]


class Tag(TypedDict, total=False):
    """A tag associated with an Amazon Web Services resource. Tags are
    key:value pairs that you can use to categorize and manage your
    resources, for purposes like billing or other management. Typically, the
    tag key represents a category, such as "environment", and the tag value
    represents a specific value within that category, such as "test,"
    "development," or "production". Or you might set the tag key to
    "customer" and the value to the customer name or ID. You can specify one
    or more tags to add to each Amazon Web Services resource, up to 50 tags
    for a resource.
    """

    Key: Optional[TagKey]
    Value: Optional[TagValue]


TagList = List[Tag]
ProtectionGroupMembers = List[ResourceArn]


class CreateProtectionGroupRequest(ServiceRequest):
    ProtectionGroupId: ProtectionGroupId
    Aggregation: ProtectionGroupAggregation
    Pattern: ProtectionGroupPattern
    ResourceType: Optional[ProtectedResourceType]
    Members: Optional[ProtectionGroupMembers]
    Tags: Optional[TagList]


class CreateProtectionGroupResponse(TypedDict, total=False):
    pass


class CreateProtectionRequest(ServiceRequest):
    Name: ProtectionName
    ResourceArn: ResourceArn
    Tags: Optional[TagList]


class CreateProtectionResponse(TypedDict, total=False):
    ProtectionId: Optional[ProtectionId]


class CreateSubscriptionRequest(ServiceRequest):
    pass


class CreateSubscriptionResponse(TypedDict, total=False):
    pass


class DeleteProtectionGroupRequest(ServiceRequest):
    ProtectionGroupId: ProtectionGroupId


class DeleteProtectionGroupResponse(TypedDict, total=False):
    pass


class DeleteProtectionRequest(ServiceRequest):
    ProtectionId: ProtectionId


class DeleteProtectionResponse(TypedDict, total=False):
    pass


class DeleteSubscriptionRequest(ServiceRequest):
    pass


class DeleteSubscriptionResponse(TypedDict, total=False):
    pass


class DescribeAttackRequest(ServiceRequest):
    AttackId: AttackId


class DescribeAttackResponse(TypedDict, total=False):
    Attack: Optional[AttackDetail]


class DescribeAttackStatisticsRequest(ServiceRequest):
    pass


Timestamp = datetime


class TimeRange(TypedDict, total=False):
    """The time range."""

    FromInclusive: Optional[Timestamp]
    ToExclusive: Optional[Timestamp]


class DescribeAttackStatisticsResponse(TypedDict, total=False):
    TimeRange: TimeRange
    DataItems: AttackStatisticsDataList


class DescribeDRTAccessRequest(ServiceRequest):
    pass


LogBucketList = List[LogBucket]


class DescribeDRTAccessResponse(TypedDict, total=False):
    RoleArn: Optional[RoleArn]
    LogBucketList: Optional[LogBucketList]


class DescribeEmergencyContactSettingsRequest(ServiceRequest):
    pass


class DescribeEmergencyContactSettingsResponse(TypedDict, total=False):
    EmergencyContactList: Optional[EmergencyContactList]


class DescribeProtectionGroupRequest(ServiceRequest):
    ProtectionGroupId: ProtectionGroupId


class ProtectionGroup(TypedDict, total=False):
    """A grouping of protected resources that you and Shield Advanced can
    monitor as a collective. This resource grouping improves the accuracy of
    detection and reduces false positives.
    """

    ProtectionGroupId: ProtectionGroupId
    Aggregation: ProtectionGroupAggregation
    Pattern: ProtectionGroupPattern
    ResourceType: Optional[ProtectedResourceType]
    Members: ProtectionGroupMembers
    ProtectionGroupArn: Optional[ResourceArn]


class DescribeProtectionGroupResponse(TypedDict, total=False):
    ProtectionGroup: ProtectionGroup


class DescribeProtectionRequest(ServiceRequest):
    ProtectionId: Optional[ProtectionId]
    ResourceArn: Optional[ResourceArn]


HealthCheckIds = List[HealthCheckId]


class Protection(TypedDict, total=False):
    """An object that represents a resource that is under DDoS protection."""

    Id: Optional[ProtectionId]
    Name: Optional[ProtectionName]
    ResourceArn: Optional[ResourceArn]
    HealthCheckIds: Optional[HealthCheckIds]
    ProtectionArn: Optional[ResourceArn]
    ApplicationLayerAutomaticResponseConfiguration: Optional[
        ApplicationLayerAutomaticResponseConfiguration
    ]


class DescribeProtectionResponse(TypedDict, total=False):
    Protection: Optional[Protection]


class DescribeSubscriptionRequest(ServiceRequest):
    pass


class ProtectionGroupArbitraryPatternLimits(TypedDict, total=False):
    """Limits settings on protection groups with arbitrary pattern type."""

    MaxMembers: Long


class ProtectionGroupPatternTypeLimits(TypedDict, total=False):
    """Limits settings by pattern type in the protection groups for your
    subscription.
    """

    ArbitraryPatternLimits: ProtectionGroupArbitraryPatternLimits


class ProtectionGroupLimits(TypedDict, total=False):
    """Limits settings on protection groups for your subscription."""

    MaxProtectionGroups: Long
    PatternTypeLimits: ProtectionGroupPatternTypeLimits


class Limit(TypedDict, total=False):
    """Specifies how many protections of a given type you can create."""

    Type: Optional[String]
    Max: Optional[Long]


Limits = List[Limit]


class ProtectionLimits(TypedDict, total=False):
    """Limits settings on protections for your subscription."""

    ProtectedResourceTypeLimits: Limits


class SubscriptionLimits(TypedDict, total=False):
    """Limits settings for your subscription."""

    ProtectionLimits: ProtectionLimits
    ProtectionGroupLimits: ProtectionGroupLimits


DurationInSeconds = int


class Subscription(TypedDict, total=False):
    """Information about the Shield Advanced subscription for an account."""

    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    TimeCommitmentInSeconds: Optional[DurationInSeconds]
    AutoRenew: Optional[AutoRenew]
    Limits: Optional[Limits]
    ProactiveEngagementStatus: Optional[ProactiveEngagementStatus]
    SubscriptionLimits: SubscriptionLimits
    SubscriptionArn: Optional[ResourceArn]


class DescribeSubscriptionResponse(TypedDict, total=False):
    Subscription: Optional[Subscription]


class DisableApplicationLayerAutomaticResponseRequest(ServiceRequest):
    ResourceArn: ResourceArn


class DisableApplicationLayerAutomaticResponseResponse(TypedDict, total=False):
    pass


class DisableProactiveEngagementRequest(ServiceRequest):
    pass


class DisableProactiveEngagementResponse(TypedDict, total=False):
    pass


class DisassociateDRTLogBucketRequest(ServiceRequest):
    LogBucket: LogBucket


class DisassociateDRTLogBucketResponse(TypedDict, total=False):
    pass


class DisassociateDRTRoleRequest(ServiceRequest):
    pass


class DisassociateDRTRoleResponse(TypedDict, total=False):
    pass


class DisassociateHealthCheckRequest(ServiceRequest):
    ProtectionId: ProtectionId
    HealthCheckArn: HealthCheckArn


class DisassociateHealthCheckResponse(TypedDict, total=False):
    pass


class EnableApplicationLayerAutomaticResponseRequest(ServiceRequest):
    ResourceArn: ResourceArn
    Action: ResponseAction


class EnableApplicationLayerAutomaticResponseResponse(TypedDict, total=False):
    pass


class EnableProactiveEngagementRequest(ServiceRequest):
    pass


class EnableProactiveEngagementResponse(TypedDict, total=False):
    pass


class GetSubscriptionStateRequest(ServiceRequest):
    pass


class GetSubscriptionStateResponse(TypedDict, total=False):
    SubscriptionState: SubscriptionState


ProtectedResourceTypeFilters = List[ProtectedResourceType]
ProtectionNameFilters = List[ProtectionName]
ResourceArnFilters = List[ResourceArn]


class InclusionProtectionFilters(TypedDict, total=False):
    """Narrows the set of protections that the call retrieves. You can retrieve
    a single protection by providing its name or the ARN (Amazon Resource
    Name) of its protected resource. You can also retrieve all protections
    for a specific resource type. You can provide up to one criteria per
    filter type. Shield Advanced returns protections that exactly match all
    of the filter criteria that you provide.
    """

    ResourceArns: Optional[ResourceArnFilters]
    ProtectionNames: Optional[ProtectionNameFilters]
    ResourceTypes: Optional[ProtectedResourceTypeFilters]


ProtectionGroupAggregationFilters = List[ProtectionGroupAggregation]
ProtectionGroupPatternFilters = List[ProtectionGroupPattern]
ProtectionGroupIdFilters = List[ProtectionGroupId]


class InclusionProtectionGroupFilters(TypedDict, total=False):
    """Narrows the set of protection groups that the call retrieves. You can
    retrieve a single protection group by its name and you can retrieve all
    protection groups that are configured with a specific pattern,
    aggregation, or resource type. You can provide up to one criteria per
    filter type. Shield Advanced returns the protection groups that exactly
    match all of the search criteria that you provide.
    """

    ProtectionGroupIds: Optional[ProtectionGroupIdFilters]
    Patterns: Optional[ProtectionGroupPatternFilters]
    ResourceTypes: Optional[ProtectedResourceTypeFilters]
    Aggregations: Optional[ProtectionGroupAggregationFilters]


ResourceArnFilterList = List[ResourceArn]


class ListAttacksRequest(ServiceRequest):
    ResourceArns: Optional[ResourceArnFilterList]
    StartTime: Optional[TimeRange]
    EndTime: Optional[TimeRange]
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]


class ListAttacksResponse(TypedDict, total=False):
    AttackSummaries: Optional[AttackSummaries]
    NextToken: Optional[Token]


class ListProtectionGroupsRequest(ServiceRequest):
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]
    InclusionFilters: Optional[InclusionProtectionGroupFilters]


ProtectionGroups = List[ProtectionGroup]


class ListProtectionGroupsResponse(TypedDict, total=False):
    ProtectionGroups: ProtectionGroups
    NextToken: Optional[Token]


class ListProtectionsRequest(ServiceRequest):
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]
    InclusionFilters: Optional[InclusionProtectionFilters]


Protections = List[Protection]


class ListProtectionsResponse(TypedDict, total=False):
    Protections: Optional[Protections]
    NextToken: Optional[Token]


class ListResourcesInProtectionGroupRequest(ServiceRequest):
    ProtectionGroupId: ProtectionGroupId
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]


ResourceArnList = List[ResourceArn]


class ListResourcesInProtectionGroupResponse(TypedDict, total=False):
    ResourceArns: ResourceArnList
    NextToken: Optional[Token]


class ListTagsForResourceRequest(ServiceRequest):
    ResourceARN: ResourceArn


class ListTagsForResourceResponse(TypedDict, total=False):
    Tags: Optional[TagList]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    ResourceARN: ResourceArn
    Tags: TagList


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    ResourceARN: ResourceArn
    TagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateApplicationLayerAutomaticResponseRequest(ServiceRequest):
    ResourceArn: ResourceArn
    Action: ResponseAction


class UpdateApplicationLayerAutomaticResponseResponse(TypedDict, total=False):
    pass


class UpdateEmergencyContactSettingsRequest(ServiceRequest):
    EmergencyContactList: Optional[EmergencyContactList]


class UpdateEmergencyContactSettingsResponse(TypedDict, total=False):
    pass


class UpdateProtectionGroupRequest(ServiceRequest):
    ProtectionGroupId: ProtectionGroupId
    Aggregation: ProtectionGroupAggregation
    Pattern: ProtectionGroupPattern
    ResourceType: Optional[ProtectedResourceType]
    Members: Optional[ProtectionGroupMembers]


class UpdateProtectionGroupResponse(TypedDict, total=False):
    pass


class UpdateSubscriptionRequest(ServiceRequest):
    AutoRenew: Optional[AutoRenew]


class UpdateSubscriptionResponse(TypedDict, total=False):
    pass


class ShieldApi:
    service = "shield"
    version = "2016-06-02"

    @handler("AssociateDRTLogBucket")
    def associate_drt_log_bucket(
        self, context: RequestContext, log_bucket: LogBucket, **kwargs
    ) -> AssociateDRTLogBucketResponse:
        """Authorizes the Shield Response Team (SRT) to access the specified Amazon
        S3 bucket containing log data such as Application Load Balancer access
        logs, CloudFront logs, or logs from third party sources. You can
        associate up to 10 Amazon S3 buckets with your subscription.

        To use the services of the SRT and make an ``AssociateDRTLogBucket``
        request, you must be subscribed to the `Business Support
        plan <http://aws.amazon.com/premiumsupport/business-support/>`__ or the
        `Enterprise Support
        plan <http://aws.amazon.com/premiumsupport/enterprise-support/>`__.

        :param log_bucket: The Amazon S3 bucket that contains the logs that you want to share.
        :returns: AssociateDRTLogBucketResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises NoAssociatedRoleException:
        :raises LimitsExceededException:
        :raises InvalidParameterException:
        :raises AccessDeniedForDependencyException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("AssociateDRTRole")
    def associate_drt_role(
        self, context: RequestContext, role_arn: RoleArn, **kwargs
    ) -> AssociateDRTRoleResponse:
        """Authorizes the Shield Response Team (SRT) using the specified role, to
        access your Amazon Web Services account to assist with DDoS attack
        mitigation during potential attacks. This enables the SRT to inspect
        your WAF configuration and create or update WAF rules and web ACLs.

        You can associate only one ``RoleArn`` with your subscription. If you
        submit an ``AssociateDRTRole`` request for an account that already has
        an associated role, the new ``RoleArn`` will replace the existing
        ``RoleArn``.

        Prior to making the ``AssociateDRTRole`` request, you must attach the
        ``AWSShieldDRTAccessPolicy`` managed policy to the role that you'll
        specify in the request. You can access this policy in the IAM console at
        `AWSShieldDRTAccessPolicy <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy>`__.
        For more information see `Adding and removing IAM identity
        permissions <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`__.
        The role must also trust the service principal
        ``drt.shield.amazonaws.com``. For more information, see `IAM JSON policy
        elements:
        Principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html>`__.

        The SRT will have access only to your WAF and Shield resources. By
        submitting this request, you authorize the SRT to inspect your WAF and
        Shield configuration and create and update WAF rules and web ACLs on
        your behalf. The SRT takes these actions only if explicitly authorized
        by you.

        You must have the ``iam:PassRole`` permission to make an
        ``AssociateDRTRole`` request. For more information, see `Granting a user
        permissions to pass a role to an Amazon Web Services
        service <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`__.

        To use the services of the SRT and make an ``AssociateDRTRole`` request,
        you must be subscribed to the `Business Support
        plan <http://aws.amazon.com/premiumsupport/business-support/>`__ or the
        `Enterprise Support
        plan <http://aws.amazon.com/premiumsupport/enterprise-support/>`__.

        :param role_arn: The Amazon Resource Name (ARN) of the role the SRT will use to access
        your Amazon Web Services account.
        :returns: AssociateDRTRoleResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises InvalidParameterException:
        :raises AccessDeniedForDependencyException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("AssociateHealthCheck")
    def associate_health_check(
        self,
        context: RequestContext,
        protection_id: ProtectionId,
        health_check_arn: HealthCheckArn,
        **kwargs,
    ) -> AssociateHealthCheckResponse:
        """Adds health-based detection to the Shield Advanced protection for a
        resource. Shield Advanced health-based detection uses the health of your
        Amazon Web Services resource to improve responsiveness and accuracy in
        attack detection and response.

        You define the health check in Route 53 and then associate it with your
        Shield Advanced protection. For more information, see `Shield Advanced
        Health-Based
        Detection <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-health-check-option>`__
        in the *WAF Developer Guide*.

        :param protection_id: The unique identifier (ID) for the Protection object to add the health
        check association to.
        :param health_check_arn: The Amazon Resource Name (ARN) of the health check to associate with the
        protection.
        :returns: AssociateHealthCheckResponse
        :raises InternalErrorException:
        :raises LimitsExceededException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises OptimisticLockException:
        :raises InvalidResourceException:
        """
        raise NotImplementedError

    @handler("AssociateProactiveEngagementDetails")
    def associate_proactive_engagement_details(
        self, context: RequestContext, emergency_contact_list: EmergencyContactList, **kwargs
    ) -> AssociateProactiveEngagementDetailsResponse:
        """Initializes proactive engagement and sets the list of contacts for the
        Shield Response Team (SRT) to use. You must provide at least one phone
        number in the emergency contact list.

        After you have initialized proactive engagement using this call, to
        disable or enable proactive engagement, use the calls
        ``DisableProactiveEngagement`` and ``EnableProactiveEngagement``.

        This call defines the list of email addresses and phone numbers that the
        SRT can use to contact you for escalations to the SRT and to initiate
        proactive customer support.

        The contacts that you provide in the request replace any contacts that
        were already defined. If you already have contacts defined and want to
        use them, retrieve the list using ``DescribeEmergencyContactSettings``
        and then provide it to this call.

        :param emergency_contact_list: A list of email addresses and phone numbers that the Shield Response
        Team (SRT) can use to contact you for escalations to the SRT and to
        initiate proactive customer support.
        :returns: AssociateProactiveEngagementDetailsResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        """
        raise NotImplementedError

    @handler("CreateProtection")
    def create_protection(
        self,
        context: RequestContext,
        name: ProtectionName,
        resource_arn: ResourceArn,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateProtectionResponse:
        """Enables Shield Advanced for a specific Amazon Web Services resource. The
        resource can be an Amazon CloudFront distribution, Amazon Route 53
        hosted zone, Global Accelerator standard accelerator, Elastic IP
        Address, Application Load Balancer, or a Classic Load Balancer. You can
        protect Amazon EC2 instances and Network Load Balancers by association
        with protected Amazon EC2 Elastic IP addresses.

        You can add protection to only a single resource with each
        ``CreateProtection`` request. You can add protection to multiple
        resources at once through the Shield Advanced console at
        https://console.aws.amazon.com/wafv2/shieldv2#/. For more information
        see `Getting Started with Shield
        Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html>`__
        and `Adding Shield Advanced protection to Amazon Web Services
        resources <https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html>`__.

        :param name: Friendly name for the ``Protection`` you are creating.
        :param resource_arn: The ARN (Amazon Resource Name) of the resource to be protected.
        :param tags: One or more tag key-value pairs for the Protection object that is
        created.
        :returns: CreateProtectionResponse
        :raises InternalErrorException:
        :raises InvalidResourceException:
        :raises InvalidOperationException:
        :raises LimitsExceededException:
        :raises ResourceAlreadyExistsException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("CreateProtectionGroup")
    def create_protection_group(
        self,
        context: RequestContext,
        protection_group_id: ProtectionGroupId,
        aggregation: ProtectionGroupAggregation,
        pattern: ProtectionGroupPattern,
        resource_type: ProtectedResourceType | None = None,
        members: ProtectionGroupMembers | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateProtectionGroupResponse:
        """Creates a grouping of protected resources so they can be handled as a
        collective. This resource grouping improves the accuracy of detection
        and reduces false positives.

        :param protection_group_id: The name of the protection group.
        :param aggregation: Defines how Shield combines resource data for the group in order to
        detect, mitigate, and report events.
        :param pattern: The criteria to use to choose the protected resources for inclusion in
        the group.
        :param resource_type: The resource type to include in the protection group.
        :param members: The Amazon Resource Names (ARNs) of the resources to include in the
        protection group.
        :param tags: One or more tag key-value pairs for the protection group.
        :returns: CreateProtectionGroupResponse
        :raises InternalErrorException:
        :raises ResourceAlreadyExistsException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises LimitsExceededException:
        """
        raise NotImplementedError

    @handler("CreateSubscription")
    def create_subscription(self, context: RequestContext, **kwargs) -> CreateSubscriptionResponse:
        """Activates Shield Advanced for an account.

        For accounts that are members of an Organizations organization, Shield
        Advanced subscriptions are billed against the organization's payer
        account, regardless of whether the payer account itself is subscribed.

        When you initially create a subscription, your subscription is set to be
        automatically renewed at the end of the existing subscription period.
        You can change this by submitting an ``UpdateSubscription`` request.

        :returns: CreateSubscriptionResponse
        :raises InternalErrorException:
        :raises ResourceAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("DeleteProtection")
    def delete_protection(
        self, context: RequestContext, protection_id: ProtectionId, **kwargs
    ) -> DeleteProtectionResponse:
        """Deletes an Shield Advanced Protection.

        :param protection_id: The unique identifier (ID) for the Protection object to be deleted.
        :returns: DeleteProtectionResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        """
        raise NotImplementedError

    @handler("DeleteProtectionGroup")
    def delete_protection_group(
        self, context: RequestContext, protection_group_id: ProtectionGroupId, **kwargs
    ) -> DeleteProtectionGroupResponse:
        """Removes the specified protection group.

        :param protection_group_id: The name of the protection group.
        :returns: DeleteProtectionGroupResponse
        :raises InternalErrorException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteSubscription")
    def delete_subscription(self, context: RequestContext, **kwargs) -> DeleteSubscriptionResponse:
        """Removes Shield Advanced from an account. Shield Advanced requires a
        1-year subscription commitment. You cannot delete a subscription prior
        to the completion of that commitment.

        :returns: DeleteSubscriptionResponse
        :raises InternalErrorException:
        :raises LockedSubscriptionException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeAttack")
    def describe_attack(
        self, context: RequestContext, attack_id: AttackId, **kwargs
    ) -> DescribeAttackResponse:
        """Describes the details of a DDoS attack.

        :param attack_id: The unique identifier (ID) for the attack.
        :returns: DescribeAttackResponse
        :raises InternalErrorException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DescribeAttackStatistics")
    def describe_attack_statistics(
        self, context: RequestContext, **kwargs
    ) -> DescribeAttackStatisticsResponse:
        """Provides information about the number and type of attacks Shield has
        detected in the last year for all resources that belong to your account,
        regardless of whether you've defined Shield protections for them. This
        operation is available to Shield customers as well as to Shield Advanced
        customers.

        The operation returns data for the time range of midnight UTC, one year
        ago, to midnight UTC, today. For example, if the current time is
        ``2020-10-26 15:39:32 PDT``, equal to ``2020-10-26 22:39:32 UTC``, then
        the time range for the attack data returned is from
        ``2019-10-26 00:00:00 UTC`` to ``2020-10-26 00:00:00 UTC``.

        The time range indicates the period covered by the attack statistics
        data items.

        :returns: DescribeAttackStatisticsResponse
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeDRTAccess")
    def describe_drt_access(self, context: RequestContext, **kwargs) -> DescribeDRTAccessResponse:
        """Returns the current role and list of Amazon S3 log buckets used by the
        Shield Response Team (SRT) to access your Amazon Web Services account
        while assisting with attack mitigation.

        :returns: DescribeDRTAccessResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeEmergencyContactSettings")
    def describe_emergency_contact_settings(
        self, context: RequestContext, **kwargs
    ) -> DescribeEmergencyContactSettingsResponse:
        """A list of email addresses and phone numbers that the Shield Response
        Team (SRT) can use to contact you if you have proactive engagement
        enabled, for escalations to the SRT and to initiate proactive customer
        support.

        :returns: DescribeEmergencyContactSettingsResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeProtection")
    def describe_protection(
        self,
        context: RequestContext,
        protection_id: ProtectionId | None = None,
        resource_arn: ResourceArn | None = None,
        **kwargs,
    ) -> DescribeProtectionResponse:
        """Lists the details of a Protection object.

        :param protection_id: The unique identifier (ID) for the Protection object to describe.
        :param resource_arn: The ARN (Amazon Resource Name) of the protected Amazon Web Services
        resource.
        :returns: DescribeProtectionResponse
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeProtectionGroup")
    def describe_protection_group(
        self, context: RequestContext, protection_group_id: ProtectionGroupId, **kwargs
    ) -> DescribeProtectionGroupResponse:
        """Returns the specification for the specified protection group.

        :param protection_group_id: The name of the protection group.
        :returns: DescribeProtectionGroupResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeSubscription")
    def describe_subscription(
        self, context: RequestContext, **kwargs
    ) -> DescribeSubscriptionResponse:
        """Provides details about the Shield Advanced subscription for an account.

        :returns: DescribeSubscriptionResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DisableApplicationLayerAutomaticResponse")
    def disable_application_layer_automatic_response(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> DisableApplicationLayerAutomaticResponseResponse:
        """Disable the Shield Advanced automatic application layer DDoS mitigation
        feature for the protected resource. This stops Shield Advanced from
        creating, verifying, and applying WAF rules for attacks that it detects
        for the resource.

        :param resource_arn: The ARN (Amazon Resource Name) of the protected resource.
        :returns: DisableApplicationLayerAutomaticResponseResponse
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("DisableProactiveEngagement")
    def disable_proactive_engagement(
        self, context: RequestContext, **kwargs
    ) -> DisableProactiveEngagementResponse:
        """Removes authorization from the Shield Response Team (SRT) to notify
        contacts about escalations to the SRT and to initiate proactive customer
        support.

        :returns: DisableProactiveEngagementResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        """
        raise NotImplementedError

    @handler("DisassociateDRTLogBucket")
    def disassociate_drt_log_bucket(
        self, context: RequestContext, log_bucket: LogBucket, **kwargs
    ) -> DisassociateDRTLogBucketResponse:
        """Removes the Shield Response Team's (SRT) access to the specified Amazon
        S3 bucket containing the logs that you shared previously.

        :param log_bucket: The Amazon S3 bucket that contains the logs that you want to share.
        :returns: DisassociateDRTLogBucketResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises NoAssociatedRoleException:
        :raises AccessDeniedForDependencyException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DisassociateDRTRole")
    def disassociate_drt_role(
        self, context: RequestContext, **kwargs
    ) -> DisassociateDRTRoleResponse:
        """Removes the Shield Response Team's (SRT) access to your Amazon Web
        Services account.

        :returns: DisassociateDRTRoleResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DisassociateHealthCheck")
    def disassociate_health_check(
        self,
        context: RequestContext,
        protection_id: ProtectionId,
        health_check_arn: HealthCheckArn,
        **kwargs,
    ) -> DisassociateHealthCheckResponse:
        """Removes health-based detection from the Shield Advanced protection for a
        resource. Shield Advanced health-based detection uses the health of your
        Amazon Web Services resource to improve responsiveness and accuracy in
        attack detection and response.

        You define the health check in Route 53 and then associate or
        disassociate it with your Shield Advanced protection. For more
        information, see `Shield Advanced Health-Based
        Detection <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-health-check-option>`__
        in the *WAF Developer Guide*.

        :param protection_id: The unique identifier (ID) for the Protection object to remove the
        health check association from.
        :param health_check_arn: The Amazon Resource Name (ARN) of the health check that is associated
        with the protection.
        :returns: DisassociateHealthCheckResponse
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        :raises InvalidResourceException:
        """
        raise NotImplementedError

    @handler("EnableApplicationLayerAutomaticResponse")
    def enable_application_layer_automatic_response(
        self, context: RequestContext, resource_arn: ResourceArn, action: ResponseAction, **kwargs
    ) -> EnableApplicationLayerAutomaticResponseResponse:
        """Enable the Shield Advanced automatic application layer DDoS mitigation
        for the protected resource.

        This feature is available for Amazon CloudFront distributions and
        Application Load Balancers only.

        This causes Shield Advanced to create, verify, and apply WAF rules for
        DDoS attacks that it detects for the resource. Shield Advanced applies
        the rules in a Shield rule group inside the web ACL that you've
        associated with the resource. For information about how automatic
        mitigation works and the requirements for using it, see `Shield Advanced
        automatic application layer DDoS
        mitigation <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-automatic-app-layer-response.html>`__.

        Don't use this action to make changes to automatic mitigation settings
        when it's already enabled for a resource. Instead, use
        UpdateApplicationLayerAutomaticResponse.

        To use this feature, you must associate a web ACL with the protected
        resource. The web ACL must be created using the latest version of WAF
        (v2). You can associate the web ACL through the Shield Advanced console
        at https://console.aws.amazon.com/wafv2/shieldv2#/. For more
        information, see `Getting Started with Shield
        Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html>`__.
        You can also associate the web ACL to the resource through the WAF
        console or the WAF API, but you must manage Shield Advanced automatic
        mitigation through Shield Advanced. For information about WAF, see `WAF
        Developer
        Guide <https://docs.aws.amazon.com/waf/latest/developerguide/>`__.

        :param resource_arn: The ARN (Amazon Resource Name) of the protected resource.
        :param action: Specifies the action setting that Shield Advanced should use in the WAF
        rules that it creates on behalf of the protected resource in response to
        DDoS attacks.
        :returns: EnableApplicationLayerAutomaticResponseResponse
        :raises LimitsExceededException:
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises OptimisticLockException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("EnableProactiveEngagement")
    def enable_proactive_engagement(
        self, context: RequestContext, **kwargs
    ) -> EnableProactiveEngagementResponse:
        """Authorizes the Shield Response Team (SRT) to use email and phone to
        notify contacts about escalations to the SRT and to initiate proactive
        customer support.

        :returns: EnableProactiveEngagementResponse
        :raises InternalErrorException:
        :raises InvalidOperationException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        """
        raise NotImplementedError

    @handler("GetSubscriptionState")
    def get_subscription_state(
        self, context: RequestContext, **kwargs
    ) -> GetSubscriptionStateResponse:
        """Returns the ``SubscriptionState``, either ``Active`` or ``Inactive``.

        :returns: GetSubscriptionStateResponse
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListAttacks")
    def list_attacks(
        self,
        context: RequestContext,
        resource_arns: ResourceArnFilterList | None = None,
        start_time: TimeRange | None = None,
        end_time: TimeRange | None = None,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAttacksResponse:
        """Returns all ongoing DDoS attacks or all DDoS attacks during a specified
        time period.

        :param resource_arns: The ARNs (Amazon Resource Names) of the resources that were attacked.
        :param start_time: The start of the time period for the attacks.
        :param end_time: The end of the time period for the attacks.
        :param next_token: When you request a list of objects from Shield Advanced, if the response
        does not include all of the remaining available objects, Shield Advanced
        includes a ``NextToken`` value in the response.
        :param max_results: The greatest number of objects that you want Shield Advanced to return
        to the list request.
        :returns: ListAttacksResponse
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListProtectionGroups")
    def list_protection_groups(
        self,
        context: RequestContext,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        inclusion_filters: InclusionProtectionGroupFilters | None = None,
        **kwargs,
    ) -> ListProtectionGroupsResponse:
        """Retrieves ProtectionGroup objects for the account. You can retrieve all
        protection groups or you can provide filtering criteria and retrieve
        just the subset of protection groups that match the criteria.

        :param next_token: When you request a list of objects from Shield Advanced, if the response
        does not include all of the remaining available objects, Shield Advanced
        includes a ``NextToken`` value in the response.
        :param max_results: The greatest number of objects that you want Shield Advanced to return
        to the list request.
        :param inclusion_filters: Narrows the set of protection groups that the call retrieves.
        :returns: ListProtectionGroupsResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises InvalidPaginationTokenException:
        """
        raise NotImplementedError

    @handler("ListProtections")
    def list_protections(
        self,
        context: RequestContext,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        inclusion_filters: InclusionProtectionFilters | None = None,
        **kwargs,
    ) -> ListProtectionsResponse:
        """Retrieves Protection objects for the account. You can retrieve all
        protections or you can provide filtering criteria and retrieve just the
        subset of protections that match the criteria.

        :param next_token: When you request a list of objects from Shield Advanced, if the response
        does not include all of the remaining available objects, Shield Advanced
        includes a ``NextToken`` value in the response.
        :param max_results: The greatest number of objects that you want Shield Advanced to return
        to the list request.
        :param inclusion_filters: Narrows the set of protections that the call retrieves.
        :returns: ListProtectionsResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises InvalidPaginationTokenException:
        """
        raise NotImplementedError

    @handler("ListResourcesInProtectionGroup")
    def list_resources_in_protection_group(
        self,
        context: RequestContext,
        protection_group_id: ProtectionGroupId,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListResourcesInProtectionGroupResponse:
        """Retrieves the resources that are included in the protection group.

        :param protection_group_id: The name of the protection group.
        :param next_token: When you request a list of objects from Shield Advanced, if the response
        does not include all of the remaining available objects, Shield Advanced
        includes a ``NextToken`` value in the response.
        :param max_results: The greatest number of objects that you want Shield Advanced to return
        to the list request.
        :returns: ListResourcesInProtectionGroupResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises InvalidPaginationTokenException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> ListTagsForResourceResponse:
        """Gets information about Amazon Web Services tags for a specified Amazon
        Resource Name (ARN) in Shield.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to get tags for.
        :returns: ListTagsForResourceResponse
        :raises InternalErrorException:
        :raises InvalidResourceException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagList, **kwargs
    ) -> TagResourceResponse:
        """Adds or updates tags for a resource in Shield.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to add or
        update tags for.
        :param tags: The tags that you want to modify or add to the resource.
        :returns: TagResourceResponse
        :raises InternalErrorException:
        :raises InvalidResourceException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResponse:
        """Removes tags from a resource in Shield.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to remove
        tags from.
        :param tag_keys: The tag key for each tag that you want to remove from the resource.
        :returns: UntagResourceResponse
        :raises InternalErrorException:
        :raises InvalidResourceException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateApplicationLayerAutomaticResponse")
    def update_application_layer_automatic_response(
        self, context: RequestContext, resource_arn: ResourceArn, action: ResponseAction, **kwargs
    ) -> UpdateApplicationLayerAutomaticResponseResponse:
        """Updates an existing Shield Advanced automatic application layer DDoS
        mitigation configuration for the specified resource.

        :param resource_arn: The ARN (Amazon Resource Name) of the resource.
        :param action: Specifies the action setting that Shield Advanced should use in the WAF
        rules that it creates on behalf of the protected resource in response to
        DDoS attacks.
        :returns: UpdateApplicationLayerAutomaticResponseResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises OptimisticLockException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("UpdateEmergencyContactSettings")
    def update_emergency_contact_settings(
        self,
        context: RequestContext,
        emergency_contact_list: EmergencyContactList | None = None,
        **kwargs,
    ) -> UpdateEmergencyContactSettingsResponse:
        """Updates the details of the list of email addresses and phone numbers
        that the Shield Response Team (SRT) can use to contact you if you have
        proactive engagement enabled, for escalations to the SRT and to initiate
        proactive customer support.

        :param emergency_contact_list: A list of email addresses and phone numbers that the Shield Response
        Team (SRT) can use to contact you if you have proactive engagement
        enabled, for escalations to the SRT and to initiate proactive customer
        support.
        :returns: UpdateEmergencyContactSettingsResponse
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises OptimisticLockException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateProtectionGroup")
    def update_protection_group(
        self,
        context: RequestContext,
        protection_group_id: ProtectionGroupId,
        aggregation: ProtectionGroupAggregation,
        pattern: ProtectionGroupPattern,
        resource_type: ProtectedResourceType | None = None,
        members: ProtectionGroupMembers | None = None,
        **kwargs,
    ) -> UpdateProtectionGroupResponse:
        """Updates an existing protection group. A protection group is a grouping
        of protected resources so they can be handled as a collective. This
        resource grouping improves the accuracy of detection and reduces false
        positives.

        :param protection_group_id: The name of the protection group.
        :param aggregation: Defines how Shield combines resource data for the group in order to
        detect, mitigate, and report events.
        :param pattern: The criteria to use to choose the protected resources for inclusion in
        the group.
        :param resource_type: The resource type to include in the protection group.
        :param members: The Amazon Resource Names (ARNs) of the resources to include in the
        protection group.
        :returns: UpdateProtectionGroupResponse
        :raises InternalErrorException:
        :raises ResourceNotFoundException:
        :raises OptimisticLockException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("UpdateSubscription")
    def update_subscription(
        self, context: RequestContext, auto_renew: AutoRenew | None = None, **kwargs
    ) -> UpdateSubscriptionResponse:
        """Updates the details of an existing subscription. Only enter values for
        parameters you want to change. Empty parameters are not updated.

        For accounts that are members of an Organizations organization, Shield
        Advanced subscriptions are billed against the organization's payer
        account, regardless of whether the payer account itself is subscribed.

        :param auto_renew: When you initally create a subscription, ``AutoRenew`` is set to
        ``ENABLED``.
        :returns: UpdateSubscriptionResponse
        :raises InternalErrorException:
        :raises LockedSubscriptionException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises OptimisticLockException:
        """
        raise NotImplementedError
