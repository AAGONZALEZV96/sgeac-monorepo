from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Boolean = bool
BoxedBoolean = bool
BoxedInteger = int
Capacity = int
ClusterName = str
DescribeAddonVersionsRequestMaxResults = int
DescribeClusterVersionMaxResults = int
EksAnywhereSubscriptionName = str
FargateProfilesRequestMaxResults = int
Integer = int
ListAccessEntriesRequestMaxResults = int
ListAccessPoliciesRequestMaxResults = int
ListAddonsRequestMaxResults = int
ListAssociatedAccessPoliciesRequestMaxResults = int
ListClustersRequestMaxResults = int
ListEksAnywhereSubscriptionsRequestMaxResults = int
ListIdentityProviderConfigsRequestMaxResults = int
ListInsightsMaxResults = int
ListNodegroupsRequestMaxResults = int
ListPodIdentityAssociationsMaxResults = int
ListUpdatesRequestMaxResults = int
NonZeroInteger = int
PercentCapacity = int
RoleArn = str
String = str
TagKey = str
TagValue = str
ZeroCapacity = int
labelKey = str
labelValue = str
requiredClaimsKey = str
requiredClaimsValue = str
taintKey = str
taintValue = str


class AMITypes(StrEnum):
    AL2_x86_64 = "AL2_x86_64"
    AL2_x86_64_GPU = "AL2_x86_64_GPU"
    AL2_ARM_64 = "AL2_ARM_64"
    CUSTOM = "CUSTOM"
    BOTTLEROCKET_ARM_64 = "BOTTLEROCKET_ARM_64"
    BOTTLEROCKET_x86_64 = "BOTTLEROCKET_x86_64"
    BOTTLEROCKET_ARM_64_FIPS = "BOTTLEROCKET_ARM_64_FIPS"
    BOTTLEROCKET_x86_64_FIPS = "BOTTLEROCKET_x86_64_FIPS"
    BOTTLEROCKET_ARM_64_NVIDIA = "BOTTLEROCKET_ARM_64_NVIDIA"
    BOTTLEROCKET_x86_64_NVIDIA = "BOTTLEROCKET_x86_64_NVIDIA"
    WINDOWS_CORE_2019_x86_64 = "WINDOWS_CORE_2019_x86_64"
    WINDOWS_FULL_2019_x86_64 = "WINDOWS_FULL_2019_x86_64"
    WINDOWS_CORE_2022_x86_64 = "WINDOWS_CORE_2022_x86_64"
    WINDOWS_FULL_2022_x86_64 = "WINDOWS_FULL_2022_x86_64"
    AL2023_x86_64_STANDARD = "AL2023_x86_64_STANDARD"
    AL2023_ARM_64_STANDARD = "AL2023_ARM_64_STANDARD"
    AL2023_x86_64_NEURON = "AL2023_x86_64_NEURON"
    AL2023_x86_64_NVIDIA = "AL2023_x86_64_NVIDIA"
    AL2023_ARM_64_NVIDIA = "AL2023_ARM_64_NVIDIA"


class AccessScopeType(StrEnum):
    cluster = "cluster"
    namespace = "namespace"


class AddonIssueCode(StrEnum):
    AccessDenied = "AccessDenied"
    InternalFailure = "InternalFailure"
    ClusterUnreachable = "ClusterUnreachable"
    InsufficientNumberOfReplicas = "InsufficientNumberOfReplicas"
    ConfigurationConflict = "ConfigurationConflict"
    AdmissionRequestDenied = "AdmissionRequestDenied"
    UnsupportedAddonModification = "UnsupportedAddonModification"
    K8sResourceNotFound = "K8sResourceNotFound"
    AddonSubscriptionNeeded = "AddonSubscriptionNeeded"
    AddonPermissionFailure = "AddonPermissionFailure"


class AddonStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"
    DEGRADED = "DEGRADED"
    UPDATE_FAILED = "UPDATE_FAILED"


class AuthenticationMode(StrEnum):
    API = "API"
    API_AND_CONFIG_MAP = "API_AND_CONFIG_MAP"
    CONFIG_MAP = "CONFIG_MAP"


class CapacityTypes(StrEnum):
    ON_DEMAND = "ON_DEMAND"
    SPOT = "SPOT"
    CAPACITY_BLOCK = "CAPACITY_BLOCK"


class Category(StrEnum):
    UPGRADE_READINESS = "UPGRADE_READINESS"


class ClusterIssueCode(StrEnum):
    AccessDenied = "AccessDenied"
    ClusterUnreachable = "ClusterUnreachable"
    ConfigurationConflict = "ConfigurationConflict"
    InternalFailure = "InternalFailure"
    ResourceLimitExceeded = "ResourceLimitExceeded"
    ResourceNotFound = "ResourceNotFound"
    IamRoleNotFound = "IamRoleNotFound"
    VpcNotFound = "VpcNotFound"
    InsufficientFreeAddresses = "InsufficientFreeAddresses"
    Ec2ServiceNotSubscribed = "Ec2ServiceNotSubscribed"
    Ec2SubnetNotFound = "Ec2SubnetNotFound"
    Ec2SecurityGroupNotFound = "Ec2SecurityGroupNotFound"
    KmsGrantRevoked = "KmsGrantRevoked"
    KmsKeyNotFound = "KmsKeyNotFound"
    KmsKeyMarkedForDeletion = "KmsKeyMarkedForDeletion"
    KmsKeyDisabled = "KmsKeyDisabled"
    StsRegionalEndpointDisabled = "StsRegionalEndpointDisabled"
    UnsupportedVersion = "UnsupportedVersion"
    Other = "Other"


class ClusterStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    UPDATING = "UPDATING"
    PENDING = "PENDING"


class ClusterVersionStatus(StrEnum):
    unsupported = "unsupported"
    standard_support = "standard-support"
    extended_support = "extended-support"


class ConnectorConfigProvider(StrEnum):
    EKS_ANYWHERE = "EKS_ANYWHERE"
    ANTHOS = "ANTHOS"
    GKE = "GKE"
    AKS = "AKS"
    OPENSHIFT = "OPENSHIFT"
    TANZU = "TANZU"
    RANCHER = "RANCHER"
    EC2 = "EC2"
    OTHER = "OTHER"


class EksAnywhereSubscriptionLicenseType(StrEnum):
    Cluster = "Cluster"


class EksAnywhereSubscriptionStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    EXPIRING = "EXPIRING"
    EXPIRED = "EXPIRED"
    DELETING = "DELETING"


class EksAnywhereSubscriptionTermUnit(StrEnum):
    MONTHS = "MONTHS"


class ErrorCode(StrEnum):
    SubnetNotFound = "SubnetNotFound"
    SecurityGroupNotFound = "SecurityGroupNotFound"
    EniLimitReached = "EniLimitReached"
    IpNotAvailable = "IpNotAvailable"
    AccessDenied = "AccessDenied"
    OperationNotPermitted = "OperationNotPermitted"
    VpcIdNotFound = "VpcIdNotFound"
    Unknown = "Unknown"
    NodeCreationFailure = "NodeCreationFailure"
    PodEvictionFailure = "PodEvictionFailure"
    InsufficientFreeAddresses = "InsufficientFreeAddresses"
    ClusterUnreachable = "ClusterUnreachable"
    InsufficientNumberOfReplicas = "InsufficientNumberOfReplicas"
    ConfigurationConflict = "ConfigurationConflict"
    AdmissionRequestDenied = "AdmissionRequestDenied"
    UnsupportedAddonModification = "UnsupportedAddonModification"
    K8sResourceNotFound = "K8sResourceNotFound"


class FargateProfileIssueCode(StrEnum):
    PodExecutionRoleAlreadyInUse = "PodExecutionRoleAlreadyInUse"
    AccessDenied = "AccessDenied"
    ClusterUnreachable = "ClusterUnreachable"
    InternalFailure = "InternalFailure"


class FargateProfileStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"


class InsightStatusValue(StrEnum):
    PASSING = "PASSING"
    WARNING = "WARNING"
    ERROR = "ERROR"
    UNKNOWN = "UNKNOWN"


class IpFamily(StrEnum):
    ipv4 = "ipv4"
    ipv6 = "ipv6"


class LogType(StrEnum):
    api = "api"
    audit = "audit"
    authenticator = "authenticator"
    controllerManager = "controllerManager"
    scheduler = "scheduler"


class NodegroupIssueCode(StrEnum):
    AutoScalingGroupNotFound = "AutoScalingGroupNotFound"
    AutoScalingGroupInvalidConfiguration = "AutoScalingGroupInvalidConfiguration"
    Ec2SecurityGroupNotFound = "Ec2SecurityGroupNotFound"
    Ec2SecurityGroupDeletionFailure = "Ec2SecurityGroupDeletionFailure"
    Ec2LaunchTemplateNotFound = "Ec2LaunchTemplateNotFound"
    Ec2LaunchTemplateVersionMismatch = "Ec2LaunchTemplateVersionMismatch"
    Ec2SubnetNotFound = "Ec2SubnetNotFound"
    Ec2SubnetInvalidConfiguration = "Ec2SubnetInvalidConfiguration"
    IamInstanceProfileNotFound = "IamInstanceProfileNotFound"
    Ec2SubnetMissingIpv6Assignment = "Ec2SubnetMissingIpv6Assignment"
    IamLimitExceeded = "IamLimitExceeded"
    IamNodeRoleNotFound = "IamNodeRoleNotFound"
    NodeCreationFailure = "NodeCreationFailure"
    AsgInstanceLaunchFailures = "AsgInstanceLaunchFailures"
    InstanceLimitExceeded = "InstanceLimitExceeded"
    InsufficientFreeAddresses = "InsufficientFreeAddresses"
    AccessDenied = "AccessDenied"
    InternalFailure = "InternalFailure"
    ClusterUnreachable = "ClusterUnreachable"
    AmiIdNotFound = "AmiIdNotFound"
    AutoScalingGroupOptInRequired = "AutoScalingGroupOptInRequired"
    AutoScalingGroupRateLimitExceeded = "AutoScalingGroupRateLimitExceeded"
    Ec2LaunchTemplateDeletionFailure = "Ec2LaunchTemplateDeletionFailure"
    Ec2LaunchTemplateInvalidConfiguration = "Ec2LaunchTemplateInvalidConfiguration"
    Ec2LaunchTemplateMaxLimitExceeded = "Ec2LaunchTemplateMaxLimitExceeded"
    Ec2SubnetListTooLong = "Ec2SubnetListTooLong"
    IamThrottling = "IamThrottling"
    NodeTerminationFailure = "NodeTerminationFailure"
    PodEvictionFailure = "PodEvictionFailure"
    SourceEc2LaunchTemplateNotFound = "SourceEc2LaunchTemplateNotFound"
    LimitExceeded = "LimitExceeded"
    Unknown = "Unknown"
    AutoScalingGroupInstanceRefreshActive = "AutoScalingGroupInstanceRefreshActive"
    KubernetesLabelInvalid = "KubernetesLabelInvalid"
    Ec2LaunchTemplateVersionMaxLimitExceeded = "Ec2LaunchTemplateVersionMaxLimitExceeded"
    Ec2InstanceTypeDoesNotExist = "Ec2InstanceTypeDoesNotExist"


class NodegroupStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    DEGRADED = "DEGRADED"


class NodegroupUpdateStrategies(StrEnum):
    DEFAULT = "DEFAULT"
    MINIMAL = "MINIMAL"


class ResolveConflicts(StrEnum):
    OVERWRITE = "OVERWRITE"
    NONE = "NONE"
    PRESERVE = "PRESERVE"


class SupportType(StrEnum):
    STANDARD = "STANDARD"
    EXTENDED = "EXTENDED"


class TaintEffect(StrEnum):
    NO_SCHEDULE = "NO_SCHEDULE"
    NO_EXECUTE = "NO_EXECUTE"
    PREFER_NO_SCHEDULE = "PREFER_NO_SCHEDULE"


class UpdateParamType(StrEnum):
    Version = "Version"
    PlatformVersion = "PlatformVersion"
    EndpointPrivateAccess = "EndpointPrivateAccess"
    EndpointPublicAccess = "EndpointPublicAccess"
    ClusterLogging = "ClusterLogging"
    DesiredSize = "DesiredSize"
    LabelsToAdd = "LabelsToAdd"
    LabelsToRemove = "LabelsToRemove"
    TaintsToAdd = "TaintsToAdd"
    TaintsToRemove = "TaintsToRemove"
    MaxSize = "MaxSize"
    MinSize = "MinSize"
    ReleaseVersion = "ReleaseVersion"
    PublicAccessCidrs = "PublicAccessCidrs"
    LaunchTemplateName = "LaunchTemplateName"
    LaunchTemplateVersion = "LaunchTemplateVersion"
    IdentityProviderConfig = "IdentityProviderConfig"
    EncryptionConfig = "EncryptionConfig"
    AddonVersion = "AddonVersion"
    ServiceAccountRoleArn = "ServiceAccountRoleArn"
    ResolveConflicts = "ResolveConflicts"
    MaxUnavailable = "MaxUnavailable"
    MaxUnavailablePercentage = "MaxUnavailablePercentage"
    NodeRepairEnabled = "NodeRepairEnabled"
    UpdateStrategy = "UpdateStrategy"
    ConfigurationValues = "ConfigurationValues"
    SecurityGroups = "SecurityGroups"
    Subnets = "Subnets"
    AuthenticationMode = "AuthenticationMode"
    PodIdentityAssociations = "PodIdentityAssociations"
    UpgradePolicy = "UpgradePolicy"
    ZonalShiftConfig = "ZonalShiftConfig"
    ComputeConfig = "ComputeConfig"
    StorageConfig = "StorageConfig"
    KubernetesNetworkConfig = "KubernetesNetworkConfig"
    RemoteNetworkConfig = "RemoteNetworkConfig"


class UpdateStatus(StrEnum):
    InProgress = "InProgress"
    Failed = "Failed"
    Cancelled = "Cancelled"
    Successful = "Successful"


class UpdateType(StrEnum):
    VersionUpdate = "VersionUpdate"
    EndpointAccessUpdate = "EndpointAccessUpdate"
    LoggingUpdate = "LoggingUpdate"
    ConfigUpdate = "ConfigUpdate"
    AssociateIdentityProviderConfig = "AssociateIdentityProviderConfig"
    DisassociateIdentityProviderConfig = "DisassociateIdentityProviderConfig"
    AssociateEncryptionConfig = "AssociateEncryptionConfig"
    AddonUpdate = "AddonUpdate"
    VpcConfigUpdate = "VpcConfigUpdate"
    AccessConfigUpdate = "AccessConfigUpdate"
    UpgradePolicyUpdate = "UpgradePolicyUpdate"
    ZonalShiftConfigUpdate = "ZonalShiftConfigUpdate"
    AutoModeUpdate = "AutoModeUpdate"
    RemoteNetworkConfigUpdate = "RemoteNetworkConfigUpdate"


class VersionStatus(StrEnum):
    UNSUPPORTED = "UNSUPPORTED"
    STANDARD_SUPPORT = "STANDARD_SUPPORT"
    EXTENDED_SUPPORT = "EXTENDED_SUPPORT"


class configStatus(StrEnum):
    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


class AccessDeniedException(ServiceException):
    """You don't have permissions to perform the requested operation. The `IAM
    principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html>`__
    making the request must have at least one IAM permissions policy
    attached that grants the required permissions. For more information, see
    `Access
    management <https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html>`__
    in the *IAM User Guide*.
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 403


class BadRequestException(ServiceException):
    """This exception is thrown if the request contains a semantic error. The
    precise meaning will depend on the API, and will be documented in the
    error message.
    """

    code: str = "BadRequestException"
    sender_fault: bool = False
    status_code: int = 400


class ClientException(ServiceException):
    """These errors are usually caused by a client action. Actions can include
    using an action or resource on behalf of an `IAM
    principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html>`__
    that doesn't have permissions to use the action or resource or
    specifying an identifier that is not valid.
    """

    code: str = "ClientException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    addonName: Optional[String]
    subscriptionId: Optional[String]


class InvalidParameterException(ServiceException):
    """The specified parameter is invalid. Review the available parameters for
    the API request.
    """

    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    fargateProfileName: Optional[String]
    addonName: Optional[String]
    subscriptionId: Optional[String]


class InvalidRequestException(ServiceException):
    """The request is invalid given the state of the cluster. Check the state
    of the cluster and the associated operations.
    """

    code: str = "InvalidRequestException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    addonName: Optional[String]
    subscriptionId: Optional[String]


class InvalidStateException(ServiceException):
    """Amazon EKS detected upgrade readiness issues. Call the
    ```ListInsights`` <https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html>`__
    API to view detected upgrade blocking issues. Pass the
    ```force`` <https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html#API_UpdateClusterVersion_RequestBody>`__
    flag when updating to override upgrade readiness errors.
    """

    code: str = "InvalidStateException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: Optional[String]


class NotFoundException(ServiceException):
    """A service resource associated with the request could not be found.
    Clients should not retry such requests.
    """

    code: str = "NotFoundException"
    sender_fault: bool = False
    status_code: int = 404


class ResourceInUseException(ServiceException):
    """The specified resource is in use."""

    code: str = "ResourceInUseException"
    sender_fault: bool = False
    status_code: int = 409
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    addonName: Optional[String]


class ResourceLimitExceededException(ServiceException):
    """You have encountered a service limit on the specified resource."""

    code: str = "ResourceLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    subscriptionId: Optional[String]


class ResourceNotFoundException(ServiceException):
    """The specified resource could not be found. You can view your available
    clusters with ``ListClusters``. You can view your available managed node
    groups with ``ListNodegroups``. Amazon EKS clusters and node groups are
    Amazon Web Services Region specific.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 404
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    fargateProfileName: Optional[String]
    addonName: Optional[String]
    subscriptionId: Optional[String]


class ResourcePropagationDelayException(ServiceException):
    """Required resources (such as service-linked roles) were created and are
    still propagating. Retry later.
    """

    code: str = "ResourcePropagationDelayException"
    sender_fault: bool = False
    status_code: int = 428


class ServerException(ServiceException):
    """These errors are usually caused by a server-side issue."""

    code: str = "ServerException"
    sender_fault: bool = False
    status_code: int = 500
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    addonName: Optional[String]
    subscriptionId: Optional[String]


class ServiceUnavailableException(ServiceException):
    """The service is unavailable. Back off and retry the operation."""

    code: str = "ServiceUnavailableException"
    sender_fault: bool = False
    status_code: int = 503


class ThrottlingException(ServiceException):
    """The request or operation couldn't be performed because a service is
    throttling requests.
    """

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 429
    clusterName: Optional[String]


StringList = List[String]


class UnsupportedAvailabilityZoneException(ServiceException):
    """At least one of your specified cluster subnets is in an Availability
    Zone that does not support Amazon EKS. The exception output specifies
    the supported Availability Zones for your account, from which you can
    choose subnets for your cluster.
    """

    code: str = "UnsupportedAvailabilityZoneException"
    sender_fault: bool = False
    status_code: int = 400
    clusterName: Optional[String]
    nodegroupName: Optional[String]
    validZones: Optional[StringList]


class AccessConfigResponse(TypedDict, total=False):
    """The access configuration for the cluster."""

    bootstrapClusterCreatorAdminPermissions: Optional[BoxedBoolean]
    authenticationMode: Optional[AuthenticationMode]


TagMap = Dict[TagKey, TagValue]
Timestamp = datetime
AccessEntry = TypedDict(
    "AccessEntry",
    {
        "clusterName": Optional[String],
        "principalArn": Optional[String],
        "kubernetesGroups": Optional[StringList],
        "accessEntryArn": Optional[String],
        "createdAt": Optional[Timestamp],
        "modifiedAt": Optional[Timestamp],
        "tags": Optional[TagMap],
        "username": Optional[String],
        "type": Optional[String],
    },
    total=False,
)


class AccessPolicy(TypedDict, total=False):
    """An access policy includes permissions that allow Amazon EKS to authorize
    an IAM principal to work with Kubernetes objects on your cluster. The
    policies are managed by Amazon EKS, but they're not IAM policies. You
    can't view the permissions in the policies using the API. The
    permissions for many of the policies are similar to the Kubernetes
    ``cluster-admin``, ``admin``, ``edit``, and ``view`` cluster roles. For
    more information about these cluster roles, see `User-facing
    roles <https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles>`__
    in the Kubernetes documentation. To view the contents of the policies,
    see `Access policy
    permissions <https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html#access-policy-permissions>`__
    in the *Amazon EKS User Guide*.
    """

    name: Optional[String]
    arn: Optional[String]


AccessPoliciesList = List[AccessPolicy]
AccessScope = TypedDict(
    "AccessScope",
    {
        "type": Optional[AccessScopeType],
        "namespaces": Optional[StringList],
    },
    total=False,
)
AdditionalInfoMap = Dict[String, String]


class MarketplaceInformation(TypedDict, total=False):
    """Information about an Amazon EKS add-on from the Amazon Web Services
    Marketplace.
    """

    productId: Optional[String]
    productUrl: Optional[String]


class AddonIssue(TypedDict, total=False):
    """An issue related to an add-on."""

    code: Optional[AddonIssueCode]
    message: Optional[String]
    resourceIds: Optional[StringList]


AddonIssueList = List[AddonIssue]


class AddonHealth(TypedDict, total=False):
    """The health of the add-on."""

    issues: Optional[AddonIssueList]


class Addon(TypedDict, total=False):
    """An Amazon EKS add-on. For more information, see `Amazon EKS
    add-ons <https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html>`__
    in the *Amazon EKS User Guide*.
    """

    addonName: Optional[String]
    clusterName: Optional[ClusterName]
    status: Optional[AddonStatus]
    addonVersion: Optional[String]
    health: Optional[AddonHealth]
    addonArn: Optional[String]
    createdAt: Optional[Timestamp]
    modifiedAt: Optional[Timestamp]
    serviceAccountRoleArn: Optional[String]
    tags: Optional[TagMap]
    publisher: Optional[String]
    owner: Optional[String]
    marketplaceInformation: Optional[MarketplaceInformation]
    configurationValues: Optional[String]
    podIdentityAssociations: Optional[StringList]


class AddonCompatibilityDetail(TypedDict, total=False):
    """The summary information about the Amazon EKS add-on compatibility for
    the next Kubernetes version for an insight check in the
    ``UPGRADE_READINESS`` category.
    """

    name: Optional[String]
    compatibleVersions: Optional[StringList]


AddonCompatibilityDetails = List[AddonCompatibilityDetail]


class Compatibility(TypedDict, total=False):
    """Compatibility information."""

    clusterVersion: Optional[String]
    platformVersions: Optional[StringList]
    defaultVersion: Optional[Boolean]


Compatibilities = List[Compatibility]


class AddonVersionInfo(TypedDict, total=False):
    """Information about an add-on version."""

    addonVersion: Optional[String]
    architecture: Optional[StringList]
    computeTypes: Optional[StringList]
    compatibilities: Optional[Compatibilities]
    requiresConfiguration: Optional[Boolean]
    requiresIamPermissions: Optional[Boolean]


AddonVersionInfoList = List[AddonVersionInfo]
AddonInfo = TypedDict(
    "AddonInfo",
    {
        "addonName": Optional[String],
        "type": Optional[String],
        "addonVersions": Optional[AddonVersionInfoList],
        "publisher": Optional[String],
        "owner": Optional[String],
        "marketplaceInformation": Optional[MarketplaceInformation],
    },
    total=False,
)


class AddonPodIdentityAssociations(TypedDict, total=False):
    """A type of Pod Identity Association owned by an Amazon EKS Add-on.

    Each EKS Pod Identity Association maps a role to a service account in a
    namespace in the cluster.

    For more information, see `Attach an IAM Role to an Amazon EKS add-on
    using Pod
    Identity <https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html>`__
    in the *Amazon EKS User Guide*.
    """

    serviceAccount: String
    roleArn: String


AddonPodIdentityAssociationsList = List[AddonPodIdentityAssociations]


class AddonPodIdentityConfiguration(TypedDict, total=False):
    """Information about how to configure IAM for an Addon."""

    serviceAccount: Optional[String]
    recommendedManagedPolicies: Optional[StringList]


AddonPodIdentityConfigurationList = List[AddonPodIdentityConfiguration]
Addons = List[AddonInfo]


class AssociateAccessPolicyRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    policyArn: String
    accessScope: AccessScope


class AssociatedAccessPolicy(TypedDict, total=False):
    """An access policy association."""

    policyArn: Optional[String]
    accessScope: Optional[AccessScope]
    associatedAt: Optional[Timestamp]
    modifiedAt: Optional[Timestamp]


class AssociateAccessPolicyResponse(TypedDict, total=False):
    clusterName: Optional[String]
    principalArn: Optional[String]
    associatedAccessPolicy: Optional[AssociatedAccessPolicy]


class Provider(TypedDict, total=False):
    """Identifies the Key Management Service (KMS) key used to encrypt the
    secrets.
    """

    keyArn: Optional[String]


class EncryptionConfig(TypedDict, total=False):
    """The encryption configuration for the cluster."""

    resources: Optional[StringList]
    provider: Optional[Provider]


EncryptionConfigList = List[EncryptionConfig]


class AssociateEncryptionConfigRequest(ServiceRequest):
    clusterName: String
    encryptionConfig: EncryptionConfigList
    clientRequestToken: Optional[String]


class ErrorDetail(TypedDict, total=False):
    """An object representing an error when an asynchronous operation fails."""

    errorCode: Optional[ErrorCode]
    errorMessage: Optional[String]
    resourceIds: Optional[StringList]


ErrorDetails = List[ErrorDetail]
UpdateParam = TypedDict(
    "UpdateParam",
    {
        "type": Optional[UpdateParamType],
        "value": Optional[String],
    },
    total=False,
)
UpdateParams = List[UpdateParam]
Update = TypedDict(
    "Update",
    {
        "id": Optional[String],
        "status": Optional[UpdateStatus],
        "type": Optional[UpdateType],
        "params": Optional[UpdateParams],
        "createdAt": Optional[Timestamp],
        "errors": Optional[ErrorDetails],
    },
    total=False,
)


class AssociateEncryptionConfigResponse(TypedDict, total=False):
    update: Optional[Update]


requiredClaimsMap = Dict[requiredClaimsKey, requiredClaimsValue]


class OidcIdentityProviderConfigRequest(TypedDict, total=False):
    """An object representing an OpenID Connect (OIDC) configuration. Before
    associating an OIDC identity provider to your cluster, review the
    considerations in `Authenticating users for your cluster from an OIDC
    identity
    provider <https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html>`__
    in the *Amazon EKS User Guide*.
    """

    identityProviderConfigName: String
    issuerUrl: String
    clientId: String
    usernameClaim: Optional[String]
    usernamePrefix: Optional[String]
    groupsClaim: Optional[String]
    groupsPrefix: Optional[String]
    requiredClaims: Optional[requiredClaimsMap]


class AssociateIdentityProviderConfigRequest(ServiceRequest):
    clusterName: String
    oidc: OidcIdentityProviderConfigRequest
    tags: Optional[TagMap]
    clientRequestToken: Optional[String]


class AssociateIdentityProviderConfigResponse(TypedDict, total=False):
    update: Optional[Update]
    tags: Optional[TagMap]


AssociatedAccessPoliciesList = List[AssociatedAccessPolicy]


class AutoScalingGroup(TypedDict, total=False):
    """An Auto Scaling group that is associated with an Amazon EKS managed node
    group.
    """

    name: Optional[String]


AutoScalingGroupList = List[AutoScalingGroup]


class BlockStorage(TypedDict, total=False):
    """Indicates the current configuration of the block storage capability on
    your EKS Auto Mode cluster. For example, if the capability is enabled or
    disabled. If the block storage capability is enabled, EKS Auto Mode will
    create and delete EBS volumes in your Amazon Web Services account. For
    more information, see EKS Auto Mode block storage capability in the
    *Amazon EKS User Guide*.
    """

    enabled: Optional[BoxedBoolean]


CategoryList = List[Category]


class Certificate(TypedDict, total=False):
    """An object representing the ``certificate-authority-data`` for your
    cluster.
    """

    data: Optional[String]


class ClientStat(TypedDict, total=False):
    """Details about clients using the deprecated resources."""

    userAgent: Optional[String]
    numberOfRequestsLast30Days: Optional[Integer]
    lastRequestTime: Optional[Timestamp]


ClientStats = List[ClientStat]


class StorageConfigResponse(TypedDict, total=False):
    """Indicates the status of the request to update the block storage
    capability of your EKS Auto Mode cluster.
    """

    blockStorage: Optional[BlockStorage]


class ComputeConfigResponse(TypedDict, total=False):
    """Indicates the status of the request to update the compute capability of
    your EKS Auto Mode cluster.
    """

    enabled: Optional[BoxedBoolean]
    nodePools: Optional[StringList]
    nodeRoleArn: Optional[String]


class RemotePodNetwork(TypedDict, total=False):
    """A network CIDR that can contain pods that run Kubernetes webhooks on
    hybrid nodes.

    These CIDR blocks are determined by configuring your Container Network
    Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note
    that the Amazon VPC CNI plugin for Kubernetes isn't available for
    on-premises and edge locations.

    Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for
    example, ``10.2.0.0/16``).

    It must satisfy the following requirements:

    -  Each block must be within an ``IPv4`` RFC-1918 network range. Minimum
       allowed size is /24, maximum allowed size is /8. Publicly-routable
       addresses aren't supported.

    -  Each block cannot overlap with the range of the VPC CIDR blocks for
       your EKS resources, or the block of the Kubernetes service IP range.
    """

    cidrs: Optional[StringList]


RemotePodNetworkList = List[RemotePodNetwork]


class RemoteNodeNetwork(TypedDict, total=False):
    """A network CIDR that can contain hybrid nodes.

    These CIDR blocks define the expected IP address range of the hybrid
    nodes that join the cluster. These blocks are typically determined by
    your network administrator.

    Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for
    example, ``10.2.0.0/16``).

    It must satisfy the following requirements:

    -  Each block must be within an ``IPv4`` RFC-1918 network range. Minimum
       allowed size is /24, maximum allowed size is /8. Publicly-routable
       addresses aren't supported.

    -  Each block cannot overlap with the range of the VPC CIDR blocks for
       your EKS resources, or the block of the Kubernetes service IP range.

    -  Each block must have a route to the VPC that uses the VPC CIDR
       blocks, not public IPs or Elastic IPs. There are many options
       including Transit Gateway, Site-to-Site VPN, or Direct Connect.

    -  Each host must allow outbound connection to the EKS cluster control
       plane on TCP ports ``443`` and ``10250``.

    -  Each host must allow inbound connection from the EKS cluster control
       plane on TCP port 10250 for logs, exec and port-forward operations.

    -  Each host must allow TCP and UDP network connectivity to and from
       other hosts that are running ``CoreDNS`` on UDP port ``53`` for
       service and pod DNS names.
    """

    cidrs: Optional[StringList]


RemoteNodeNetworkList = List[RemoteNodeNetwork]


class RemoteNetworkConfigResponse(TypedDict, total=False):
    """The configuration in the cluster for EKS Hybrid Nodes. You can add,
    change, or remove this configuration after the cluster is created.
    """

    remoteNodeNetworks: Optional[RemoteNodeNetworkList]
    remotePodNetworks: Optional[RemotePodNetworkList]


class ZonalShiftConfigResponse(TypedDict, total=False):
    """The status of zonal shift configuration for the cluster"""

    enabled: Optional[BoxedBoolean]


class UpgradePolicyResponse(TypedDict, total=False):
    """This value indicates if extended support is enabled or disabled for the
    cluster.

    `Learn more about EKS Extended Support in the Amazon EKS User
    Guide. <https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html>`__
    """

    supportType: Optional[SupportType]


class ControlPlanePlacementResponse(TypedDict, total=False):
    """The placement configuration for all the control plane instances of your
    local Amazon EKS cluster on an Amazon Web Services Outpost. For more
    information, see `Capacity
    considerations <https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html>`__
    in the *Amazon EKS User Guide*.
    """

    groupName: Optional[String]


class OutpostConfigResponse(TypedDict, total=False):
    """An object representing the configuration of your local Amazon EKS
    cluster on an Amazon Web Services Outpost. This API isn't available for
    Amazon EKS clusters on the Amazon Web Services cloud.
    """

    outpostArns: StringList
    controlPlaneInstanceType: String
    controlPlanePlacement: Optional[ControlPlanePlacementResponse]


class ClusterIssue(TypedDict, total=False):
    """An issue with your Amazon EKS cluster."""

    code: Optional[ClusterIssueCode]
    message: Optional[String]
    resourceIds: Optional[StringList]


ClusterIssueList = List[ClusterIssue]


class ClusterHealth(TypedDict, total=False):
    """An object representing the health of your Amazon EKS cluster."""

    issues: Optional[ClusterIssueList]


class ConnectorConfigResponse(TypedDict, total=False):
    """The full description of your connected cluster."""

    activationId: Optional[String]
    activationCode: Optional[String]
    activationExpiry: Optional[Timestamp]
    provider: Optional[String]
    roleArn: Optional[String]


class OIDC(TypedDict, total=False):
    """An object representing the `OpenID
    Connect <https://openid.net/connect/>`__ (OIDC) identity provider
    information for the cluster.
    """

    issuer: Optional[String]


class Identity(TypedDict, total=False):
    """An object representing an identity provider."""

    oidc: Optional[OIDC]


LogTypes = List[LogType]


class LogSetup(TypedDict, total=False):
    """An object representing the enabled or disabled Kubernetes control plane
    logs for your cluster.
    """

    types: Optional[LogTypes]
    enabled: Optional[BoxedBoolean]


LogSetups = List[LogSetup]


class Logging(TypedDict, total=False):
    """An object representing the logging configuration for resources in your
    cluster.
    """

    clusterLogging: Optional[LogSetups]


class ElasticLoadBalancing(TypedDict, total=False):
    """Indicates the current configuration of the load balancing capability on
    your EKS Auto Mode cluster. For example, if the capability is enabled or
    disabled. For more information, see EKS Auto Mode load balancing
    capability in the *Amazon EKS User Guide*.
    """

    enabled: Optional[BoxedBoolean]


class KubernetesNetworkConfigResponse(TypedDict, total=False):
    """The Kubernetes network configuration for the cluster. The response
    contains a value for **serviceIpv6Cidr** or **serviceIpv4Cidr**, but not
    both.
    """

    serviceIpv4Cidr: Optional[String]
    serviceIpv6Cidr: Optional[String]
    ipFamily: Optional[IpFamily]
    elasticLoadBalancing: Optional[ElasticLoadBalancing]


class VpcConfigResponse(TypedDict, total=False):
    """An object representing an Amazon EKS cluster VPC configuration response."""

    subnetIds: Optional[StringList]
    securityGroupIds: Optional[StringList]
    clusterSecurityGroupId: Optional[String]
    vpcId: Optional[String]
    endpointPublicAccess: Optional[Boolean]
    endpointPrivateAccess: Optional[Boolean]
    publicAccessCidrs: Optional[StringList]


class Cluster(TypedDict, total=False):
    """An object representing an Amazon EKS cluster."""

    name: Optional[String]
    arn: Optional[String]
    createdAt: Optional[Timestamp]
    version: Optional[String]
    endpoint: Optional[String]
    roleArn: Optional[String]
    resourcesVpcConfig: Optional[VpcConfigResponse]
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigResponse]
    logging: Optional[Logging]
    identity: Optional[Identity]
    status: Optional[ClusterStatus]
    certificateAuthority: Optional[Certificate]
    clientRequestToken: Optional[String]
    platformVersion: Optional[String]
    tags: Optional[TagMap]
    encryptionConfig: Optional[EncryptionConfigList]
    connectorConfig: Optional[ConnectorConfigResponse]
    id: Optional[String]
    health: Optional[ClusterHealth]
    outpostConfig: Optional[OutpostConfigResponse]
    accessConfig: Optional[AccessConfigResponse]
    upgradePolicy: Optional[UpgradePolicyResponse]
    zonalShiftConfig: Optional[ZonalShiftConfigResponse]
    remoteNetworkConfig: Optional[RemoteNetworkConfigResponse]
    computeConfig: Optional[ComputeConfigResponse]
    storageConfig: Optional[StorageConfigResponse]


class ClusterVersionInformation(TypedDict, total=False):
    """Contains details about a specific EKS cluster version."""

    clusterVersion: Optional[String]
    clusterType: Optional[String]
    defaultPlatformVersion: Optional[String]
    defaultVersion: Optional[Boolean]
    releaseDate: Optional[Timestamp]
    endOfStandardSupportDate: Optional[Timestamp]
    endOfExtendedSupportDate: Optional[Timestamp]
    status: Optional[ClusterVersionStatus]
    versionStatus: Optional[VersionStatus]
    kubernetesPatchVersion: Optional[String]


ClusterVersionList = List[ClusterVersionInformation]


class ComputeConfigRequest(TypedDict, total=False):
    """Request to update the configuration of the compute capability of your
    EKS Auto Mode cluster. For example, enable the capability. For more
    information, see EKS Auto Mode compute capability in the *Amazon EKS
    User Guide*.
    """

    enabled: Optional[BoxedBoolean]
    nodePools: Optional[StringList]
    nodeRoleArn: Optional[String]


class ConnectorConfigRequest(TypedDict, total=False):
    """The configuration sent to a cluster for configuration."""

    roleArn: String
    provider: ConnectorConfigProvider


class ControlPlanePlacementRequest(TypedDict, total=False):
    """The placement configuration for all the control plane instances of your
    local Amazon EKS cluster on an Amazon Web Services Outpost. For more
    information, see `Capacity
    considerations <https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html>`__
    in the *Amazon EKS User Guide*.
    """

    groupName: Optional[String]


class CreateAccessConfigRequest(TypedDict, total=False):
    """The access configuration information for the cluster."""

    bootstrapClusterCreatorAdminPermissions: Optional[BoxedBoolean]
    authenticationMode: Optional[AuthenticationMode]


CreateAccessEntryRequest = TypedDict(
    "CreateAccessEntryRequest",
    {
        "clusterName": String,
        "principalArn": String,
        "kubernetesGroups": Optional[StringList],
        "tags": Optional[TagMap],
        "clientRequestToken": Optional[String],
        "username": Optional[String],
        "type": Optional[String],
    },
    total=False,
)


class CreateAccessEntryResponse(TypedDict, total=False):
    accessEntry: Optional[AccessEntry]


class CreateAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String
    addonVersion: Optional[String]
    serviceAccountRoleArn: Optional[RoleArn]
    resolveConflicts: Optional[ResolveConflicts]
    clientRequestToken: Optional[String]
    tags: Optional[TagMap]
    configurationValues: Optional[String]
    podIdentityAssociations: Optional[AddonPodIdentityAssociationsList]


class CreateAddonResponse(TypedDict, total=False):
    addon: Optional[Addon]


class StorageConfigRequest(TypedDict, total=False):
    """Request to update the configuration of the storage capability of your
    EKS Auto Mode cluster. For example, enable the capability. For more
    information, see EKS Auto Mode block storage capability in the *Amazon
    EKS User Guide*.
    """

    blockStorage: Optional[BlockStorage]


class RemoteNetworkConfigRequest(TypedDict, total=False):
    """The configuration in the cluster for EKS Hybrid Nodes. You can add,
    change, or remove this configuration after the cluster is created.
    """

    remoteNodeNetworks: Optional[RemoteNodeNetworkList]
    remotePodNetworks: Optional[RemotePodNetworkList]


class ZonalShiftConfigRequest(TypedDict, total=False):
    """The configuration for zonal shift for the cluster."""

    enabled: Optional[BoxedBoolean]


class UpgradePolicyRequest(TypedDict, total=False):
    """The support policy to use for the cluster. Extended support allows you
    to remain on specific Kubernetes versions for longer. Clusters in
    extended support have higher costs. The default value is ``EXTENDED``.
    Use ``STANDARD`` to disable extended support.

    `Learn more about EKS Extended Support in the Amazon EKS User
    Guide. <https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html>`__
    """

    supportType: Optional[SupportType]


class OutpostConfigRequest(TypedDict, total=False):
    """The configuration of your local Amazon EKS cluster on an Amazon Web
    Services Outpost. Before creating a cluster on an Outpost, review
    `Creating a local cluster on an
    Outpost <https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-create.html>`__
    in the *Amazon EKS User Guide*. This API isn't available for Amazon EKS
    clusters on the Amazon Web Services cloud.
    """

    outpostArns: StringList
    controlPlaneInstanceType: String
    controlPlanePlacement: Optional[ControlPlanePlacementRequest]


class KubernetesNetworkConfigRequest(TypedDict, total=False):
    """The Kubernetes network configuration for the cluster."""

    serviceIpv4Cidr: Optional[String]
    ipFamily: Optional[IpFamily]
    elasticLoadBalancing: Optional[ElasticLoadBalancing]


class VpcConfigRequest(TypedDict, total=False):
    """An object representing the VPC configuration to use for an Amazon EKS
    cluster.
    """

    subnetIds: Optional[StringList]
    securityGroupIds: Optional[StringList]
    endpointPublicAccess: Optional[BoxedBoolean]
    endpointPrivateAccess: Optional[BoxedBoolean]
    publicAccessCidrs: Optional[StringList]


class CreateClusterRequest(ServiceRequest):
    name: ClusterName
    version: Optional[String]
    roleArn: String
    resourcesVpcConfig: VpcConfigRequest
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequest]
    logging: Optional[Logging]
    clientRequestToken: Optional[String]
    tags: Optional[TagMap]
    encryptionConfig: Optional[EncryptionConfigList]
    outpostConfig: Optional[OutpostConfigRequest]
    accessConfig: Optional[CreateAccessConfigRequest]
    bootstrapSelfManagedAddons: Optional[BoxedBoolean]
    upgradePolicy: Optional[UpgradePolicyRequest]
    zonalShiftConfig: Optional[ZonalShiftConfigRequest]
    remoteNetworkConfig: Optional[RemoteNetworkConfigRequest]
    computeConfig: Optional[ComputeConfigRequest]
    storageConfig: Optional[StorageConfigRequest]


class CreateClusterResponse(TypedDict, total=False):
    cluster: Optional[Cluster]


class EksAnywhereSubscriptionTerm(TypedDict, total=False):
    """An object representing the term duration and term unit type of your
    subscription. This determines the term length of your subscription.
    Valid values are MONTHS for term unit and 12 or 36 for term duration,
    indicating a 12 month or 36 month subscription.
    """

    duration: Optional[Integer]
    unit: Optional[EksAnywhereSubscriptionTermUnit]


class CreateEksAnywhereSubscriptionRequest(ServiceRequest):
    name: EksAnywhereSubscriptionName
    term: EksAnywhereSubscriptionTerm
    licenseQuantity: Optional[Integer]
    licenseType: Optional[EksAnywhereSubscriptionLicenseType]
    autoRenew: Optional[Boolean]
    clientRequestToken: Optional[String]
    tags: Optional[TagMap]


class License(TypedDict, total=False):
    """An EKS Anywhere license associated with a subscription."""

    id: Optional[String]
    token: Optional[String]


LicenseList = List[License]


class EksAnywhereSubscription(TypedDict, total=False):
    """An EKS Anywhere subscription authorizing the customer to support for
    licensed clusters and access to EKS Anywhere Curated Packages.
    """

    id: Optional[String]
    arn: Optional[String]
    createdAt: Optional[Timestamp]
    effectiveDate: Optional[Timestamp]
    expirationDate: Optional[Timestamp]
    licenseQuantity: Optional[Integer]
    licenseType: Optional[EksAnywhereSubscriptionLicenseType]
    term: Optional[EksAnywhereSubscriptionTerm]
    status: Optional[String]
    autoRenew: Optional[Boolean]
    licenseArns: Optional[StringList]
    licenses: Optional[LicenseList]
    tags: Optional[TagMap]


class CreateEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: Optional[EksAnywhereSubscription]


FargateProfileLabel = Dict[String, String]


class FargateProfileSelector(TypedDict, total=False):
    """An object representing an Fargate profile selector."""

    namespace: Optional[String]
    labels: Optional[FargateProfileLabel]


FargateProfileSelectors = List[FargateProfileSelector]


class CreateFargateProfileRequest(ServiceRequest):
    fargateProfileName: String
    clusterName: String
    podExecutionRoleArn: String
    subnets: Optional[StringList]
    selectors: Optional[FargateProfileSelectors]
    clientRequestToken: Optional[String]
    tags: Optional[TagMap]


class FargateProfileIssue(TypedDict, total=False):
    """An issue that is associated with the Fargate profile."""

    code: Optional[FargateProfileIssueCode]
    message: Optional[String]
    resourceIds: Optional[StringList]


FargateProfileIssueList = List[FargateProfileIssue]


class FargateProfileHealth(TypedDict, total=False):
    """The health status of the Fargate profile. If there are issues with your
    Fargate profile's health, they are listed here.
    """

    issues: Optional[FargateProfileIssueList]


class FargateProfile(TypedDict, total=False):
    """An object representing an Fargate profile."""

    fargateProfileName: Optional[String]
    fargateProfileArn: Optional[String]
    clusterName: Optional[String]
    createdAt: Optional[Timestamp]
    podExecutionRoleArn: Optional[String]
    subnets: Optional[StringList]
    selectors: Optional[FargateProfileSelectors]
    status: Optional[FargateProfileStatus]
    tags: Optional[TagMap]
    health: Optional[FargateProfileHealth]


class CreateFargateProfileResponse(TypedDict, total=False):
    fargateProfile: Optional[FargateProfile]


class NodeRepairConfig(TypedDict, total=False):
    """The node auto repair configuration for the node group."""

    enabled: Optional[BoxedBoolean]


class NodegroupUpdateConfig(TypedDict, total=False):
    """The node group update configuration. An Amazon EKS managed node group
    updates by replacing nodes with new nodes of newer AMI versions in
    parallel. You choose the *maximum unavailable* and the *update
    strategy*.
    """

    maxUnavailable: Optional[NonZeroInteger]
    maxUnavailablePercentage: Optional[PercentCapacity]
    updateStrategy: Optional[NodegroupUpdateStrategies]


class LaunchTemplateSpecification(TypedDict, total=False):
    """An object representing a node group launch template specification. The
    launch template can't include
    ```SubnetId`` <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html>`__
    ,
    ```IamInstanceProfile`` <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html>`__
    ,
    ```RequestSpotInstances`` <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__
    ,
    ```HibernationOptions`` <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html>`__
    , or
    ```TerminateInstances`` <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html>`__
    , or the node group deployment or update will fail. For more information
    about launch templates, see
    ```CreateLaunchTemplate`` <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html>`__
    in the Amazon EC2 API Reference. For more information about using launch
    templates with Amazon EKS, see `Customizing managed nodes with launch
    templates <https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html>`__
    in the *Amazon EKS User Guide*.

    You must specify either the launch template ID or the launch template
    name in the request, but not both.
    """

    name: Optional[String]
    version: Optional[String]
    id: Optional[String]


class Taint(TypedDict, total=False):
    """A property that allows a node to repel a ``Pod``. For more information,
    see `Node taints on managed node
    groups <https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html>`__
    in the *Amazon EKS User Guide*.
    """

    key: Optional[taintKey]
    value: Optional[taintValue]
    effect: Optional[TaintEffect]


taintsList = List[Taint]
labelsMap = Dict[labelKey, labelValue]


class RemoteAccessConfig(TypedDict, total=False):
    """An object representing the remote access configuration for the managed
    node group.
    """

    ec2SshKey: Optional[String]
    sourceSecurityGroups: Optional[StringList]


class NodegroupScalingConfig(TypedDict, total=False):
    """An object representing the scaling configuration details for the Auto
    Scaling group that is associated with your node group. When creating a
    node group, you must specify all or none of the properties. When
    updating a node group, you can specify any or none of the properties.
    """

    minSize: Optional[ZeroCapacity]
    maxSize: Optional[Capacity]
    desiredSize: Optional[ZeroCapacity]


class CreateNodegroupRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String
    scalingConfig: Optional[NodegroupScalingConfig]
    diskSize: Optional[BoxedInteger]
    subnets: StringList
    instanceTypes: Optional[StringList]
    amiType: Optional[AMITypes]
    remoteAccess: Optional[RemoteAccessConfig]
    nodeRole: String
    labels: Optional[labelsMap]
    taints: Optional[taintsList]
    tags: Optional[TagMap]
    clientRequestToken: Optional[String]
    launchTemplate: Optional[LaunchTemplateSpecification]
    updateConfig: Optional[NodegroupUpdateConfig]
    nodeRepairConfig: Optional[NodeRepairConfig]
    capacityType: Optional[CapacityTypes]
    version: Optional[String]
    releaseVersion: Optional[String]


class Issue(TypedDict, total=False):
    """An object representing an issue with an Amazon EKS resource."""

    code: Optional[NodegroupIssueCode]
    message: Optional[String]
    resourceIds: Optional[StringList]


IssueList = List[Issue]


class NodegroupHealth(TypedDict, total=False):
    """An object representing the health status of the node group."""

    issues: Optional[IssueList]


class NodegroupResources(TypedDict, total=False):
    """An object representing the resources associated with the node group,
    such as Auto Scaling groups and security groups for remote access.
    """

    autoScalingGroups: Optional[AutoScalingGroupList]
    remoteAccessSecurityGroup: Optional[String]


class Nodegroup(TypedDict, total=False):
    """An object representing an Amazon EKS managed node group."""

    nodegroupName: Optional[String]
    nodegroupArn: Optional[String]
    clusterName: Optional[String]
    version: Optional[String]
    releaseVersion: Optional[String]
    createdAt: Optional[Timestamp]
    modifiedAt: Optional[Timestamp]
    status: Optional[NodegroupStatus]
    capacityType: Optional[CapacityTypes]
    scalingConfig: Optional[NodegroupScalingConfig]
    instanceTypes: Optional[StringList]
    subnets: Optional[StringList]
    remoteAccess: Optional[RemoteAccessConfig]
    amiType: Optional[AMITypes]
    nodeRole: Optional[String]
    labels: Optional[labelsMap]
    taints: Optional[taintsList]
    resources: Optional[NodegroupResources]
    diskSize: Optional[BoxedInteger]
    health: Optional[NodegroupHealth]
    updateConfig: Optional[NodegroupUpdateConfig]
    nodeRepairConfig: Optional[NodeRepairConfig]
    launchTemplate: Optional[LaunchTemplateSpecification]
    tags: Optional[TagMap]


class CreateNodegroupResponse(TypedDict, total=False):
    nodegroup: Optional[Nodegroup]


class CreatePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    namespace: String
    serviceAccount: String
    roleArn: String
    clientRequestToken: Optional[String]
    tags: Optional[TagMap]


class PodIdentityAssociation(TypedDict, total=False):
    """Amazon EKS Pod Identity associations provide the ability to manage
    credentials for your applications, similar to the way that Amazon EC2
    instance profiles provide credentials to Amazon EC2 instances.
    """

    clusterName: Optional[String]
    namespace: Optional[String]
    serviceAccount: Optional[String]
    roleArn: Optional[String]
    associationArn: Optional[String]
    associationId: Optional[String]
    tags: Optional[TagMap]
    createdAt: Optional[Timestamp]
    modifiedAt: Optional[Timestamp]
    ownerArn: Optional[String]


class CreatePodIdentityAssociationResponse(TypedDict, total=False):
    association: Optional[PodIdentityAssociation]


class DeleteAccessEntryRequest(ServiceRequest):
    clusterName: String
    principalArn: String


class DeleteAccessEntryResponse(TypedDict, total=False):
    pass


class DeleteAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String
    preserve: Optional[Boolean]


class DeleteAddonResponse(TypedDict, total=False):
    addon: Optional[Addon]


class DeleteClusterRequest(ServiceRequest):
    name: String


class DeleteClusterResponse(TypedDict, total=False):
    cluster: Optional[Cluster]


class DeleteEksAnywhereSubscriptionRequest(ServiceRequest):
    id: String


class DeleteEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: Optional[EksAnywhereSubscription]


class DeleteFargateProfileRequest(ServiceRequest):
    clusterName: String
    fargateProfileName: String


class DeleteFargateProfileResponse(TypedDict, total=False):
    fargateProfile: Optional[FargateProfile]


class DeleteNodegroupRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String


class DeleteNodegroupResponse(TypedDict, total=False):
    nodegroup: Optional[Nodegroup]


class DeletePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    associationId: String


class DeletePodIdentityAssociationResponse(TypedDict, total=False):
    association: Optional[PodIdentityAssociation]


class DeprecationDetail(TypedDict, total=False):
    """The summary information about deprecated resource usage for an insight
    check in the ``UPGRADE_READINESS`` category.
    """

    usage: Optional[String]
    replacedWith: Optional[String]
    stopServingVersion: Optional[String]
    startServingReplacementVersion: Optional[String]
    clientStats: Optional[ClientStats]


DeprecationDetails = List[DeprecationDetail]


class DeregisterClusterRequest(ServiceRequest):
    name: String


class DeregisterClusterResponse(TypedDict, total=False):
    cluster: Optional[Cluster]


class DescribeAccessEntryRequest(ServiceRequest):
    clusterName: String
    principalArn: String


class DescribeAccessEntryResponse(TypedDict, total=False):
    accessEntry: Optional[AccessEntry]


class DescribeAddonConfigurationRequest(ServiceRequest):
    addonName: String
    addonVersion: String


class DescribeAddonConfigurationResponse(TypedDict, total=False):
    addonName: Optional[String]
    addonVersion: Optional[String]
    configurationSchema: Optional[String]
    podIdentityConfiguration: Optional[AddonPodIdentityConfigurationList]


class DescribeAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String


class DescribeAddonResponse(TypedDict, total=False):
    addon: Optional[Addon]


class DescribeAddonVersionsRequest(ServiceRequest):
    kubernetesVersion: Optional[String]
    maxResults: Optional[DescribeAddonVersionsRequestMaxResults]
    nextToken: Optional[String]
    addonName: Optional[String]
    types: Optional[StringList]
    publishers: Optional[StringList]
    owners: Optional[StringList]


class DescribeAddonVersionsResponse(TypedDict, total=False):
    addons: Optional[Addons]
    nextToken: Optional[String]


class DescribeClusterRequest(ServiceRequest):
    name: String


class DescribeClusterResponse(TypedDict, total=False):
    cluster: Optional[Cluster]


class DescribeClusterVersionsRequest(ServiceRequest):
    clusterType: Optional[String]
    maxResults: Optional[DescribeClusterVersionMaxResults]
    nextToken: Optional[String]
    defaultOnly: Optional[BoxedBoolean]
    includeAll: Optional[BoxedBoolean]
    clusterVersions: Optional[StringList]
    status: Optional[ClusterVersionStatus]
    versionStatus: Optional[VersionStatus]


class DescribeClusterVersionsResponse(TypedDict, total=False):
    nextToken: Optional[String]
    clusterVersions: Optional[ClusterVersionList]


class DescribeEksAnywhereSubscriptionRequest(ServiceRequest):
    id: String


class DescribeEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: Optional[EksAnywhereSubscription]


class DescribeFargateProfileRequest(ServiceRequest):
    clusterName: String
    fargateProfileName: String


class DescribeFargateProfileResponse(TypedDict, total=False):
    fargateProfile: Optional[FargateProfile]


IdentityProviderConfig = TypedDict(
    "IdentityProviderConfig",
    {
        "type": String,
        "name": String,
    },
    total=False,
)


class DescribeIdentityProviderConfigRequest(ServiceRequest):
    clusterName: String
    identityProviderConfig: IdentityProviderConfig


class OidcIdentityProviderConfig(TypedDict, total=False):
    """An object representing the configuration for an OpenID Connect (OIDC)
    identity provider.
    """

    identityProviderConfigName: Optional[String]
    identityProviderConfigArn: Optional[String]
    clusterName: Optional[String]
    issuerUrl: Optional[String]
    clientId: Optional[String]
    usernameClaim: Optional[String]
    usernamePrefix: Optional[String]
    groupsClaim: Optional[String]
    groupsPrefix: Optional[String]
    requiredClaims: Optional[requiredClaimsMap]
    tags: Optional[TagMap]
    status: Optional[configStatus]


class IdentityProviderConfigResponse(TypedDict, total=False):
    """The full description of your identity configuration."""

    oidc: Optional[OidcIdentityProviderConfig]


class DescribeIdentityProviderConfigResponse(TypedDict, total=False):
    identityProviderConfig: Optional[IdentityProviderConfigResponse]


class DescribeInsightRequest(ServiceRequest):
    clusterName: String
    id: String


class InsightCategorySpecificSummary(TypedDict, total=False):
    """Summary information that relates to the category of the insight.
    Currently only returned with certain insights having category
    ``UPGRADE_READINESS``.
    """

    deprecationDetails: Optional[DeprecationDetails]
    addonCompatibilityDetails: Optional[AddonCompatibilityDetails]


class InsightStatus(TypedDict, total=False):
    """The status of the insight."""

    status: Optional[InsightStatusValue]
    reason: Optional[String]


class InsightResourceDetail(TypedDict, total=False):
    """Returns information about the resource being evaluated."""

    insightStatus: Optional[InsightStatus]
    kubernetesResourceUri: Optional[String]
    arn: Optional[String]


InsightResourceDetails = List[InsightResourceDetail]


class Insight(TypedDict, total=False):
    """A check that provides recommendations to remedy potential
    upgrade-impacting issues.
    """

    id: Optional[String]
    name: Optional[String]
    category: Optional[Category]
    kubernetesVersion: Optional[String]
    lastRefreshTime: Optional[Timestamp]
    lastTransitionTime: Optional[Timestamp]
    description: Optional[String]
    insightStatus: Optional[InsightStatus]
    recommendation: Optional[String]
    additionalInfo: Optional[AdditionalInfoMap]
    resources: Optional[InsightResourceDetails]
    categorySpecificSummary: Optional[InsightCategorySpecificSummary]


class DescribeInsightResponse(TypedDict, total=False):
    insight: Optional[Insight]


class DescribeNodegroupRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String


class DescribeNodegroupResponse(TypedDict, total=False):
    nodegroup: Optional[Nodegroup]


class DescribePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    associationId: String


class DescribePodIdentityAssociationResponse(TypedDict, total=False):
    association: Optional[PodIdentityAssociation]


class DescribeUpdateRequest(ServiceRequest):
    """Describes an update request."""

    name: String
    updateId: String
    nodegroupName: Optional[String]
    addonName: Optional[String]


class DescribeUpdateResponse(TypedDict, total=False):
    update: Optional[Update]


class DisassociateAccessPolicyRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    policyArn: String


class DisassociateAccessPolicyResponse(TypedDict, total=False):
    pass


class DisassociateIdentityProviderConfigRequest(ServiceRequest):
    clusterName: String
    identityProviderConfig: IdentityProviderConfig
    clientRequestToken: Optional[String]


class DisassociateIdentityProviderConfigResponse(TypedDict, total=False):
    update: Optional[Update]


EksAnywhereSubscriptionList = List[EksAnywhereSubscription]
EksAnywhereSubscriptionStatusValues = List[EksAnywhereSubscriptionStatus]
IdentityProviderConfigs = List[IdentityProviderConfig]
IncludeClustersList = List[String]
InsightStatusValueList = List[InsightStatusValue]


class InsightSummary(TypedDict, total=False):
    """The summarized description of the insight."""

    id: Optional[String]
    name: Optional[String]
    category: Optional[Category]
    kubernetesVersion: Optional[String]
    lastRefreshTime: Optional[Timestamp]
    lastTransitionTime: Optional[Timestamp]
    description: Optional[String]
    insightStatus: Optional[InsightStatus]


InsightSummaries = List[InsightSummary]


class InsightsFilter(TypedDict, total=False):
    """The criteria to use for the insights."""

    categories: Optional[CategoryList]
    kubernetesVersions: Optional[StringList]
    statuses: Optional[InsightStatusValueList]


class ListAccessEntriesRequest(ServiceRequest):
    clusterName: String
    associatedPolicyArn: Optional[String]
    maxResults: Optional[ListAccessEntriesRequestMaxResults]
    nextToken: Optional[String]


class ListAccessEntriesResponse(TypedDict, total=False):
    accessEntries: Optional[StringList]
    nextToken: Optional[String]


class ListAccessPoliciesRequest(ServiceRequest):
    maxResults: Optional[ListAccessPoliciesRequestMaxResults]
    nextToken: Optional[String]


class ListAccessPoliciesResponse(TypedDict, total=False):
    accessPolicies: Optional[AccessPoliciesList]
    nextToken: Optional[String]


class ListAddonsRequest(ServiceRequest):
    clusterName: ClusterName
    maxResults: Optional[ListAddonsRequestMaxResults]
    nextToken: Optional[String]


class ListAddonsResponse(TypedDict, total=False):
    addons: Optional[StringList]
    nextToken: Optional[String]


class ListAssociatedAccessPoliciesRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    maxResults: Optional[ListAssociatedAccessPoliciesRequestMaxResults]
    nextToken: Optional[String]


class ListAssociatedAccessPoliciesResponse(TypedDict, total=False):
    clusterName: Optional[String]
    principalArn: Optional[String]
    nextToken: Optional[String]
    associatedAccessPolicies: Optional[AssociatedAccessPoliciesList]


class ListClustersRequest(ServiceRequest):
    maxResults: Optional[ListClustersRequestMaxResults]
    nextToken: Optional[String]
    include: Optional[IncludeClustersList]


class ListClustersResponse(TypedDict, total=False):
    clusters: Optional[StringList]
    nextToken: Optional[String]


class ListEksAnywhereSubscriptionsRequest(ServiceRequest):
    maxResults: Optional[ListEksAnywhereSubscriptionsRequestMaxResults]
    nextToken: Optional[String]
    includeStatus: Optional[EksAnywhereSubscriptionStatusValues]


class ListEksAnywhereSubscriptionsResponse(TypedDict, total=False):
    subscriptions: Optional[EksAnywhereSubscriptionList]
    nextToken: Optional[String]


class ListFargateProfilesRequest(ServiceRequest):
    clusterName: String
    maxResults: Optional[FargateProfilesRequestMaxResults]
    nextToken: Optional[String]


class ListFargateProfilesResponse(TypedDict, total=False):
    fargateProfileNames: Optional[StringList]
    nextToken: Optional[String]


class ListIdentityProviderConfigsRequest(ServiceRequest):
    clusterName: String
    maxResults: Optional[ListIdentityProviderConfigsRequestMaxResults]
    nextToken: Optional[String]


class ListIdentityProviderConfigsResponse(TypedDict, total=False):
    identityProviderConfigs: Optional[IdentityProviderConfigs]
    nextToken: Optional[String]


class ListInsightsRequest(ServiceRequest):
    clusterName: String
    filter: Optional[InsightsFilter]
    maxResults: Optional[ListInsightsMaxResults]
    nextToken: Optional[String]


class ListInsightsResponse(TypedDict, total=False):
    insights: Optional[InsightSummaries]
    nextToken: Optional[String]


class ListNodegroupsRequest(ServiceRequest):
    clusterName: String
    maxResults: Optional[ListNodegroupsRequestMaxResults]
    nextToken: Optional[String]


class ListNodegroupsResponse(TypedDict, total=False):
    nodegroups: Optional[StringList]
    nextToken: Optional[String]


class ListPodIdentityAssociationsRequest(ServiceRequest):
    clusterName: String
    namespace: Optional[String]
    serviceAccount: Optional[String]
    maxResults: Optional[ListPodIdentityAssociationsMaxResults]
    nextToken: Optional[String]


class PodIdentityAssociationSummary(TypedDict, total=False):
    """The summarized description of the association.

    Each summary is simplified by removing these fields compared to the full
    ```PodIdentityAssociation`` <https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html>`__
    :

    -  The IAM role: ``roleArn``

    -  The timestamp that the association was created at: ``createdAt``

    -  The most recent timestamp that the association was modified at:.
       ``modifiedAt``

    -  The tags on the association: ``tags``
    """

    clusterName: Optional[String]
    namespace: Optional[String]
    serviceAccount: Optional[String]
    associationArn: Optional[String]
    associationId: Optional[String]
    ownerArn: Optional[String]


PodIdentityAssociationSummaries = List[PodIdentityAssociationSummary]


class ListPodIdentityAssociationsResponse(TypedDict, total=False):
    associations: Optional[PodIdentityAssociationSummaries]
    nextToken: Optional[String]


class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: String


class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Optional[TagMap]


class ListUpdatesRequest(ServiceRequest):
    name: String
    nodegroupName: Optional[String]
    addonName: Optional[String]
    nextToken: Optional[String]
    maxResults: Optional[ListUpdatesRequestMaxResults]


class ListUpdatesResponse(TypedDict, total=False):
    updateIds: Optional[StringList]
    nextToken: Optional[String]


class RegisterClusterRequest(ServiceRequest):
    name: ClusterName
    connectorConfig: ConnectorConfigRequest
    clientRequestToken: Optional[String]
    tags: Optional[TagMap]


class RegisterClusterResponse(TypedDict, total=False):
    cluster: Optional[Cluster]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    resourceArn: String
    tags: TagMap


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    resourceArn: String
    tagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateAccessConfigRequest(TypedDict, total=False):
    """The access configuration information for the cluster."""

    authenticationMode: Optional[AuthenticationMode]


class UpdateAccessEntryRequest(ServiceRequest):
    clusterName: String
    principalArn: String
    kubernetesGroups: Optional[StringList]
    clientRequestToken: Optional[String]
    username: Optional[String]


class UpdateAccessEntryResponse(TypedDict, total=False):
    accessEntry: Optional[AccessEntry]


class UpdateAddonRequest(ServiceRequest):
    clusterName: ClusterName
    addonName: String
    addonVersion: Optional[String]
    serviceAccountRoleArn: Optional[RoleArn]
    resolveConflicts: Optional[ResolveConflicts]
    clientRequestToken: Optional[String]
    configurationValues: Optional[String]
    podIdentityAssociations: Optional[AddonPodIdentityAssociationsList]


class UpdateAddonResponse(TypedDict, total=False):
    update: Optional[Update]


class UpdateClusterConfigRequest(ServiceRequest):
    name: String
    resourcesVpcConfig: Optional[VpcConfigRequest]
    logging: Optional[Logging]
    clientRequestToken: Optional[String]
    accessConfig: Optional[UpdateAccessConfigRequest]
    upgradePolicy: Optional[UpgradePolicyRequest]
    zonalShiftConfig: Optional[ZonalShiftConfigRequest]
    computeConfig: Optional[ComputeConfigRequest]
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequest]
    storageConfig: Optional[StorageConfigRequest]
    remoteNetworkConfig: Optional[RemoteNetworkConfigRequest]


class UpdateClusterConfigResponse(TypedDict, total=False):
    update: Optional[Update]


class UpdateClusterVersionRequest(ServiceRequest):
    name: String
    version: String
    clientRequestToken: Optional[String]
    force: Optional[Boolean]


class UpdateClusterVersionResponse(TypedDict, total=False):
    update: Optional[Update]


class UpdateEksAnywhereSubscriptionRequest(ServiceRequest):
    id: String
    autoRenew: Boolean
    clientRequestToken: Optional[String]


class UpdateEksAnywhereSubscriptionResponse(TypedDict, total=False):
    subscription: Optional[EksAnywhereSubscription]


labelsKeyList = List[String]


class UpdateLabelsPayload(TypedDict, total=False):
    """An object representing a Kubernetes ``label`` change for a managed node
    group.
    """

    addOrUpdateLabels: Optional[labelsMap]
    removeLabels: Optional[labelsKeyList]


class UpdateTaintsPayload(TypedDict, total=False):
    """An object representing the details of an update to a taints payload. For
    more information, see `Node taints on managed node
    groups <https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html>`__
    in the *Amazon EKS User Guide*.
    """

    addOrUpdateTaints: Optional[taintsList]
    removeTaints: Optional[taintsList]


class UpdateNodegroupConfigRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String
    labels: Optional[UpdateLabelsPayload]
    taints: Optional[UpdateTaintsPayload]
    scalingConfig: Optional[NodegroupScalingConfig]
    updateConfig: Optional[NodegroupUpdateConfig]
    nodeRepairConfig: Optional[NodeRepairConfig]
    clientRequestToken: Optional[String]


class UpdateNodegroupConfigResponse(TypedDict, total=False):
    update: Optional[Update]


class UpdateNodegroupVersionRequest(ServiceRequest):
    clusterName: String
    nodegroupName: String
    version: Optional[String]
    releaseVersion: Optional[String]
    launchTemplate: Optional[LaunchTemplateSpecification]
    force: Optional[Boolean]
    clientRequestToken: Optional[String]


class UpdateNodegroupVersionResponse(TypedDict, total=False):
    update: Optional[Update]


class UpdatePodIdentityAssociationRequest(ServiceRequest):
    clusterName: String
    associationId: String
    roleArn: Optional[String]
    clientRequestToken: Optional[String]


class UpdatePodIdentityAssociationResponse(TypedDict, total=False):
    association: Optional[PodIdentityAssociation]


class EksApi:
    service = "eks"
    version = "2017-11-01"

    @handler("AssociateAccessPolicy")
    def associate_access_policy(
        self,
        context: RequestContext,
        cluster_name: String,
        principal_arn: String,
        policy_arn: String,
        access_scope: AccessScope,
        **kwargs,
    ) -> AssociateAccessPolicyResponse:
        """Associates an access policy and its scope to an access entry. For more
        information about associating access policies, see `Associating and
        disassociating access policies to and from access
        entries <https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html>`__
        in the *Amazon EKS User Guide*.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The Amazon Resource Name (ARN) of the IAM user or role for the
        ``AccessEntry`` that you're associating the access policy to.
        :param policy_arn: The ARN of the ``AccessPolicy`` that you're associating.
        :param access_scope: The scope for the ``AccessPolicy``.
        :returns: AssociateAccessPolicyResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("AssociateEncryptionConfig")
    def associate_encryption_config(
        self,
        context: RequestContext,
        cluster_name: String,
        encryption_config: EncryptionConfigList,
        client_request_token: String | None = None,
        **kwargs,
    ) -> AssociateEncryptionConfigResponse:
        """Associates an encryption configuration to an existing cluster.

        Use this API to enable encryption on existing clusters that don't
        already have encryption enabled. This allows you to implement a
        defense-in-depth security strategy without migrating applications to new
        Amazon EKS clusters.

        :param cluster_name: The name of your cluster.
        :param encryption_config: The configuration you are using for encryption.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: AssociateEncryptionConfigResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("AssociateIdentityProviderConfig")
    def associate_identity_provider_config(
        self,
        context: RequestContext,
        cluster_name: String,
        oidc: OidcIdentityProviderConfigRequest,
        tags: TagMap | None = None,
        client_request_token: String | None = None,
        **kwargs,
    ) -> AssociateIdentityProviderConfigResponse:
        """Associates an identity provider configuration to a cluster.

        If you want to authenticate identities using an identity provider, you
        can create an identity provider configuration and associate it to your
        cluster. After configuring authentication to your cluster you can create
        Kubernetes ``Role`` and ``ClusterRole`` objects, assign permissions to
        them, and then bind them to the identities using Kubernetes
        ``RoleBinding`` and ``ClusterRoleBinding`` objects. For more information
        see `Using RBAC
        Authorization <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>`__
        in the Kubernetes documentation.

        :param cluster_name: The name of your cluster.
        :param oidc: An object representing an OpenID Connect (OIDC) identity provider
        configuration.
        :param tags: Metadata that assists with categorization and organization.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: AssociateIdentityProviderConfigResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateAccessEntry", expand=False)
    def create_access_entry(
        self, context: RequestContext, request: CreateAccessEntryRequest, **kwargs
    ) -> CreateAccessEntryResponse:
        """Creates an access entry.

        An access entry allows an IAM principal to access your cluster. Access
        entries can replace the need to maintain entries in the ``aws-auth``
        ``ConfigMap`` for authentication. You have the following options for
        authorizing an IAM principal to access Kubernetes objects on your
        cluster: Kubernetes role-based access control (RBAC), Amazon EKS, or
        both. Kubernetes RBAC authorization requires you to create and manage
        Kubernetes ``Role``, ``ClusterRole``, ``RoleBinding``, and
        ``ClusterRoleBinding`` objects, in addition to managing access entries.
        If you use Amazon EKS authorization exclusively, you don't need to
        create and manage Kubernetes ``Role``, ``ClusterRole``, ``RoleBinding``,
        and ``ClusterRoleBinding`` objects.

        For more information about access entries, see `Access
        entries <https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html>`__
        in the *Amazon EKS User Guide*.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The ARN of the IAM principal for the ``AccessEntry``.
        :param kubernetes_groups: The value for ``name`` that you've specified for ``kind: Group`` as a
        ``subject`` in a Kubernetes ``RoleBinding`` or ``ClusterRoleBinding``
        object.
        :param tags: Metadata that assists with categorization and organization.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param username: The username to authenticate to Kubernetes with.
        :param type: The type of the new access entry.
        :returns: CreateAccessEntryResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        :raises ResourceLimitExceededException:
        :raises ResourceInUseException:
        """
        raise NotImplementedError

    @handler("CreateAddon")
    def create_addon(
        self,
        context: RequestContext,
        cluster_name: ClusterName,
        addon_name: String,
        addon_version: String | None = None,
        service_account_role_arn: RoleArn | None = None,
        resolve_conflicts: ResolveConflicts | None = None,
        client_request_token: String | None = None,
        tags: TagMap | None = None,
        configuration_values: String | None = None,
        pod_identity_associations: AddonPodIdentityAssociationsList | None = None,
        **kwargs,
    ) -> CreateAddonResponse:
        """Creates an Amazon EKS add-on.

        Amazon EKS add-ons help to automate the provisioning and lifecycle
        management of common operational software for Amazon EKS clusters. For
        more information, see `Amazon EKS
        add-ons <https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html>`__
        in the *Amazon EKS User Guide*.

        :param cluster_name: The name of your cluster.
        :param addon_name: The name of the add-on.
        :param addon_version: The version of the add-on.
        :param service_account_role_arn: The Amazon Resource Name (ARN) of an existing IAM role to bind to the
        add-on's service account.
        :param resolve_conflicts: How to resolve field value conflicts for an Amazon EKS add-on.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: Metadata that assists with categorization and organization.
        :param configuration_values: The set of configuration values for the add-on that's created.
        :param pod_identity_associations: An array of Pod Identity Assocations to be created.
        :returns: CreateAddonResponse
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ResourceInUseException:
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("CreateCluster")
    def create_cluster(
        self,
        context: RequestContext,
        name: ClusterName,
        role_arn: String,
        resources_vpc_config: VpcConfigRequest,
        version: String | None = None,
        kubernetes_network_config: KubernetesNetworkConfigRequest | None = None,
        logging: Logging | None = None,
        client_request_token: String | None = None,
        tags: TagMap | None = None,
        encryption_config: EncryptionConfigList | None = None,
        outpost_config: OutpostConfigRequest | None = None,
        access_config: CreateAccessConfigRequest | None = None,
        bootstrap_self_managed_addons: BoxedBoolean | None = None,
        upgrade_policy: UpgradePolicyRequest | None = None,
        zonal_shift_config: ZonalShiftConfigRequest | None = None,
        remote_network_config: RemoteNetworkConfigRequest | None = None,
        compute_config: ComputeConfigRequest | None = None,
        storage_config: StorageConfigRequest | None = None,
        **kwargs,
    ) -> CreateClusterResponse:
        """Creates an Amazon EKS control plane.

        The Amazon EKS control plane consists of control plane instances that
        run the Kubernetes software, such as ``etcd`` and the API server. The
        control plane runs in an account managed by Amazon Web Services, and the
        Kubernetes API is exposed by the Amazon EKS API server endpoint. Each
        Amazon EKS cluster control plane is single tenant and unique. It runs on
        its own set of Amazon EC2 instances.

        The cluster control plane is provisioned across multiple Availability
        Zones and fronted by an Elastic Load Balancing Network Load Balancer.
        Amazon EKS also provisions elastic network interfaces in your VPC
        subnets to provide connectivity from the control plane instances to the
        nodes (for example, to support ``kubectl exec``, ``logs``, and ``proxy``
        data flows).

        Amazon EKS nodes run in your Amazon Web Services account and connect to
        your cluster's control plane over the Kubernetes API server endpoint and
        a certificate file that is created for your cluster.

        You can use the ``endpointPublicAccess`` and ``endpointPrivateAccess``
        parameters to enable or disable public and private access to your
        cluster's Kubernetes API server endpoint. By default, public access is
        enabled, and private access is disabled. For more information, see
        `Amazon EKS Cluster Endpoint Access
        Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__
        in the *Amazon EKS User Guide* .

        You can use the ``logging`` parameter to enable or disable exporting the
        Kubernetes control plane logs for your cluster to CloudWatch Logs. By
        default, cluster control plane logs aren't exported to CloudWatch Logs.
        For more information, see `Amazon EKS Cluster Control Plane
        Logs <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__
        in the *Amazon EKS User Guide* .

        CloudWatch Logs ingestion, archive storage, and data scanning rates
        apply to exported control plane logs. For more information, see
        `CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__.

        In most cases, it takes several minutes to create a cluster. After you
        create an Amazon EKS cluster, you must configure your Kubernetes tooling
        to communicate with the API server and launch nodes into your cluster.
        For more information, see `Allowing users to access your
        cluster <https://docs.aws.amazon.com/eks/latest/userguide/cluster-auth.html>`__
        and `Launching Amazon EKS
        nodes <https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html>`__
        in the *Amazon EKS User Guide*.

        :param name: The unique name to give to your cluster.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that provides permissions
        for the Kubernetes control plane to make calls to Amazon Web Services
        API operations on your behalf.
        :param resources_vpc_config: The VPC configuration that's used by the cluster control plane.
        :param version: The desired Kubernetes version for your cluster.
        :param kubernetes_network_config: The Kubernetes network configuration for the cluster.
        :param logging: Enable or disable exporting the Kubernetes control plane logs for your
        cluster to CloudWatch Logs .
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: Metadata that assists with categorization and organization.
        :param encryption_config: The encryption configuration for the cluster.
        :param outpost_config: An object representing the configuration of your local Amazon EKS
        cluster on an Amazon Web Services Outpost.
        :param access_config: The access configuration for the cluster.
        :param bootstrap_self_managed_addons: If you set this value to ``False`` when creating a cluster, the default
        networking add-ons will not be installed.
        :param upgrade_policy: New clusters, by default, have extended support enabled.
        :param zonal_shift_config: Enable or disable ARC zonal shift for the cluster.
        :param remote_network_config: The configuration in the cluster for EKS Hybrid Nodes.
        :param compute_config: Enable or disable the compute capability of EKS Auto Mode when creating
        your EKS Auto Mode cluster.
        :param storage_config: Enable or disable the block storage capability of EKS Auto Mode when
        creating your EKS Auto Mode cluster.
        :returns: CreateClusterResponse
        :raises ResourceInUseException:
        :raises ResourceLimitExceededException:
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        :raises UnsupportedAvailabilityZoneException:
        """
        raise NotImplementedError

    @handler("CreateEksAnywhereSubscription")
    def create_eks_anywhere_subscription(
        self,
        context: RequestContext,
        name: EksAnywhereSubscriptionName,
        term: EksAnywhereSubscriptionTerm,
        license_quantity: Integer | None = None,
        license_type: EksAnywhereSubscriptionLicenseType | None = None,
        auto_renew: Boolean | None = None,
        client_request_token: String | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreateEksAnywhereSubscriptionResponse:
        """Creates an EKS Anywhere subscription. When a subscription is created, it
        is a contract agreement for the length of the term specified in the
        request. Licenses that are used to validate support are provisioned in
        Amazon Web Services License Manager and the caller account is granted
        access to EKS Anywhere Curated Packages.

        :param name: The unique name for your subscription.
        :param term: An object representing the term duration and term unit type of your
        subscription.
        :param license_quantity: The number of licenses to purchase with the subscription.
        :param license_type: The license type for all licenses in the subscription.
        :param auto_renew: A boolean indicating whether the subscription auto renews at the end of
        the term.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: The metadata for a subscription to assist with categorization and
        organization.
        :returns: CreateEksAnywhereSubscriptionResponse
        :raises ResourceLimitExceededException:
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreateFargateProfile")
    def create_fargate_profile(
        self,
        context: RequestContext,
        fargate_profile_name: String,
        cluster_name: String,
        pod_execution_role_arn: String,
        subnets: StringList | None = None,
        selectors: FargateProfileSelectors | None = None,
        client_request_token: String | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreateFargateProfileResponse:
        """Creates an Fargate profile for your Amazon EKS cluster. You must have at
        least one Fargate profile in a cluster to be able to run pods on
        Fargate.

        The Fargate profile allows an administrator to declare which pods run on
        Fargate and specify which pods run on which Fargate profile. This
        declaration is done through the profile's selectors. Each profile can
        have up to five selectors that contain a namespace and labels. A
        namespace is required for every selector. The label field consists of
        multiple optional key-value pairs. Pods that match the selectors are
        scheduled on Fargate. If a to-be-scheduled pod matches any of the
        selectors in the Fargate profile, then that pod is run on Fargate.

        When you create a Fargate profile, you must specify a pod execution role
        to use with the pods that are scheduled with the profile. This role is
        added to the cluster's Kubernetes `Role Based Access
        Control <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>`__
        (RBAC) for authorization so that the ``kubelet`` that is running on the
        Fargate infrastructure can register with your Amazon EKS cluster so that
        it can appear in your cluster as a node. The pod execution role also
        provides IAM permissions to the Fargate infrastructure to allow read
        access to Amazon ECR image repositories. For more information, see `Pod
        Execution
        Role <https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html>`__
        in the *Amazon EKS User Guide*.

        Fargate profiles are immutable. However, you can create a new updated
        profile to replace an existing profile and then delete the original
        after the updated profile has finished creating.

        If any Fargate profiles in a cluster are in the ``DELETING`` status, you
        must wait for that Fargate profile to finish deleting before you can
        create any other profiles in that cluster.

        For more information, see `Fargate
        profile <https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html>`__
        in the *Amazon EKS User Guide*.

        :param fargate_profile_name: The name of the Fargate profile.
        :param cluster_name: The name of your cluster.
        :param pod_execution_role_arn: The Amazon Resource Name (ARN) of the ``Pod`` execution role to use for
        a ``Pod`` that matches the selectors in the Fargate profile.
        :param subnets: The IDs of subnets to launch a ``Pod`` into.
        :param selectors: The selectors to match for a ``Pod`` to use this Fargate profile.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: Metadata that assists with categorization and organization.
        :returns: CreateFargateProfileResponse
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceLimitExceededException:
        :raises UnsupportedAvailabilityZoneException:
        """
        raise NotImplementedError

    @handler("CreateNodegroup")
    def create_nodegroup(
        self,
        context: RequestContext,
        cluster_name: String,
        nodegroup_name: String,
        subnets: StringList,
        node_role: String,
        scaling_config: NodegroupScalingConfig | None = None,
        disk_size: BoxedInteger | None = None,
        instance_types: StringList | None = None,
        ami_type: AMITypes | None = None,
        remote_access: RemoteAccessConfig | None = None,
        labels: labelsMap | None = None,
        taints: taintsList | None = None,
        tags: TagMap | None = None,
        client_request_token: String | None = None,
        launch_template: LaunchTemplateSpecification | None = None,
        update_config: NodegroupUpdateConfig | None = None,
        node_repair_config: NodeRepairConfig | None = None,
        capacity_type: CapacityTypes | None = None,
        version: String | None = None,
        release_version: String | None = None,
        **kwargs,
    ) -> CreateNodegroupResponse:
        """Creates a managed node group for an Amazon EKS cluster.

        You can only create a node group for your cluster that is equal to the
        current Kubernetes version for the cluster. All node groups are created
        with the latest AMI release version for the respective minor Kubernetes
        version of the cluster, unless you deploy a custom AMI using a launch
        template.

        For later updates, you will only be able to update a node group using a
        launch template only if it was originally deployed with a launch
        template. Additionally, the launch template ID or name must match what
        was used when the node group was created. You can update the launch
        template version with necessary changes. For more information about
        using launch templates, see `Customizing managed nodes with launch
        templates <https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html>`__.

        An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and
        associated Amazon EC2 instances that are managed by Amazon Web Services
        for an Amazon EKS cluster. For more information, see `Managed node
        groups <https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html>`__
        in the *Amazon EKS User Guide*.

        Windows AMI types are only supported for commercial Amazon Web Services
        Regions that support Windows on Amazon EKS.

        :param cluster_name: The name of your cluster.
        :param nodegroup_name: The unique name to give your node group.
        :param subnets: The subnets to use for the Auto Scaling group that is created for your
        node group.
        :param node_role: The Amazon Resource Name (ARN) of the IAM role to associate with your
        node group.
        :param scaling_config: The scaling configuration details for the Auto Scaling group that is
        created for your node group.
        :param disk_size: The root device disk size (in GiB) for your node group instances.
        :param instance_types: Specify the instance types for a node group.
        :param ami_type: The AMI type for your node group.
        :param remote_access: The remote access configuration to use with your node group.
        :param labels: The Kubernetes ``labels`` to apply to the nodes in the node group when
        they are created.
        :param taints: The Kubernetes taints to be applied to the nodes in the node group.
        :param tags: Metadata that assists with categorization and organization.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param launch_template: An object representing a node group's launch template specification.
        :param update_config: The node group update configuration.
        :param node_repair_config: The node auto repair configuration for the node group.
        :param capacity_type: The capacity type for your node group.
        :param version: The Kubernetes version to use for your managed nodes.
        :param release_version: The AMI version of the Amazon EKS optimized AMI to use with your node
        group.
        :returns: CreateNodegroupResponse
        :raises ResourceInUseException:
        :raises ResourceLimitExceededException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreatePodIdentityAssociation")
    def create_pod_identity_association(
        self,
        context: RequestContext,
        cluster_name: String,
        namespace: String,
        service_account: String,
        role_arn: String,
        client_request_token: String | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreatePodIdentityAssociationResponse:
        """Creates an EKS Pod Identity association between a service account in an
        Amazon EKS cluster and an IAM role with *EKS Pod Identity*. Use EKS Pod
        Identity to give temporary IAM credentials to pods and the credentials
        are rotated automatically.

        Amazon EKS Pod Identity associations provide the ability to manage
        credentials for your applications, similar to the way that Amazon EC2
        instance profiles provide credentials to Amazon EC2 instances.

        If a pod uses a service account that has an association, Amazon EKS sets
        environment variables in the containers of the pod. The environment
        variables configure the Amazon Web Services SDKs, including the Command
        Line Interface, to use the EKS Pod Identity credentials.

        Pod Identity is a simpler method than *IAM roles for service accounts*,
        as this method doesn't use OIDC identity providers. Additionally, you
        can configure a role for Pod Identity once, and reuse it across
        clusters.

        :param cluster_name: The name of the cluster to create the association in.
        :param namespace: The name of the Kubernetes namespace inside the cluster to create the
        association in.
        :param service_account: The name of the Kubernetes service account inside the cluster to
        associate the IAM credentials with.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to associate with the
        service account.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: Metadata that assists with categorization and organization.
        :returns: CreatePodIdentityAssociationResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        :raises ResourceLimitExceededException:
        :raises ResourceInUseException:
        """
        raise NotImplementedError

    @handler("DeleteAccessEntry")
    def delete_access_entry(
        self, context: RequestContext, cluster_name: String, principal_arn: String, **kwargs
    ) -> DeleteAccessEntryResponse:
        """Deletes an access entry.

        Deleting an access entry of a type other than ``Standard`` can cause
        your cluster to function improperly. If you delete an access entry in
        error, you can recreate it.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The ARN of the IAM principal for the ``AccessEntry``.
        :returns: DeleteAccessEntryResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DeleteAddon")
    def delete_addon(
        self,
        context: RequestContext,
        cluster_name: ClusterName,
        addon_name: String,
        preserve: Boolean | None = None,
        **kwargs,
    ) -> DeleteAddonResponse:
        """Deletes an Amazon EKS add-on.

        When you remove an add-on, it's deleted from the cluster. You can always
        manually start an add-on on the cluster using the Kubernetes API.

        :param cluster_name: The name of your cluster.
        :param addon_name: The name of the add-on.
        :param preserve: Specifying this option preserves the add-on software on your cluster but
        Amazon EKS stops managing any settings for the add-on.
        :returns: DeleteAddonResponse
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeleteCluster")
    def delete_cluster(
        self, context: RequestContext, name: String, **kwargs
    ) -> DeleteClusterResponse:
        """Deletes an Amazon EKS cluster control plane.

        If you have active services in your cluster that are associated with a
        load balancer, you must delete those services before deleting the
        cluster so that the load balancers are deleted properly. Otherwise, you
        can have orphaned resources in your VPC that prevent you from being able
        to delete the VPC. For more information, see `Deleting a
        cluster <https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html>`__
        in the *Amazon EKS User Guide*.

        If you have managed node groups or Fargate profiles attached to the
        cluster, you must delete them first. For more information, see
        ``DeleteNodgroup`` and ``DeleteFargateProfile``.

        :param name: The name of the cluster to delete.
        :returns: DeleteClusterResponse
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteEksAnywhereSubscription")
    def delete_eks_anywhere_subscription(
        self, context: RequestContext, id: String, **kwargs
    ) -> DeleteEksAnywhereSubscriptionResponse:
        """Deletes an expired or inactive subscription. Deleting inactive
        subscriptions removes them from the Amazon Web Services Management
        Console view and from list/describe API responses. Subscriptions can
        only be cancelled within 7 days of creation and are cancelled by
        creating a ticket in the Amazon Web Services Support Center.

        :param id: The ID of the subscription.
        :returns: DeleteEksAnywhereSubscriptionResponse
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises InvalidRequestException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeleteFargateProfile")
    def delete_fargate_profile(
        self, context: RequestContext, cluster_name: String, fargate_profile_name: String, **kwargs
    ) -> DeleteFargateProfileResponse:
        """Deletes an Fargate profile.

        When you delete a Fargate profile, any ``Pod`` running on Fargate that
        was created with the profile is deleted. If the ``Pod`` matches another
        Fargate profile, then it is scheduled on Fargate with that profile. If
        it no longer matches any Fargate profiles, then it's not scheduled on
        Fargate and may remain in a pending state.

        Only one Fargate profile in a cluster can be in the ``DELETING`` status
        at a time. You must wait for a Fargate profile to finish deleting before
        you can delete any other profiles in that cluster.

        :param cluster_name: The name of your cluster.
        :param fargate_profile_name: The name of the Fargate profile to delete.
        :returns: DeleteFargateProfileResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteNodegroup")
    def delete_nodegroup(
        self, context: RequestContext, cluster_name: String, nodegroup_name: String, **kwargs
    ) -> DeleteNodegroupResponse:
        """Deletes a managed node group.

        :param cluster_name: The name of your cluster.
        :param nodegroup_name: The name of the node group to delete.
        :returns: DeleteNodegroupResponse
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeletePodIdentityAssociation")
    def delete_pod_identity_association(
        self, context: RequestContext, cluster_name: String, association_id: String, **kwargs
    ) -> DeletePodIdentityAssociationResponse:
        """Deletes a EKS Pod Identity association.

        The temporary Amazon Web Services credentials from the previous IAM role
        session might still be valid until the session expiry. If you need to
        immediately revoke the temporary session credentials, then go to the
        role in the IAM console.

        :param cluster_name: The cluster name that.
        :param association_id: The ID of the association to be deleted.
        :returns: DeletePodIdentityAssociationResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("DeregisterCluster")
    def deregister_cluster(
        self, context: RequestContext, name: String, **kwargs
    ) -> DeregisterClusterResponse:
        """Deregisters a connected cluster to remove it from the Amazon EKS control
        plane.

        A connected cluster is a Kubernetes cluster that you've connected to
        your control plane using the `Amazon EKS
        Connector <https://docs.aws.amazon.com/eks/latest/userguide/eks-connector.html>`__.

        :param name: The name of the connected cluster to deregister.
        :returns: DeregisterClusterResponse
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DescribeAccessEntry")
    def describe_access_entry(
        self, context: RequestContext, cluster_name: String, principal_arn: String, **kwargs
    ) -> DescribeAccessEntryResponse:
        """Describes an access entry.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The ARN of the IAM principal for the ``AccessEntry``.
        :returns: DescribeAccessEntryResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DescribeAddon")
    def describe_addon(
        self, context: RequestContext, cluster_name: ClusterName, addon_name: String, **kwargs
    ) -> DescribeAddonResponse:
        """Describes an Amazon EKS add-on.

        :param cluster_name: The name of your cluster.
        :param addon_name: The name of the add-on.
        :returns: DescribeAddonResponse
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeAddonConfiguration")
    def describe_addon_configuration(
        self, context: RequestContext, addon_name: String, addon_version: String, **kwargs
    ) -> DescribeAddonConfigurationResponse:
        """Returns configuration options.

        :param addon_name: The name of the add-on.
        :param addon_version: The version of the add-on.
        :returns: DescribeAddonConfigurationResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("DescribeAddonVersions")
    def describe_addon_versions(
        self,
        context: RequestContext,
        kubernetes_version: String | None = None,
        max_results: DescribeAddonVersionsRequestMaxResults | None = None,
        next_token: String | None = None,
        addon_name: String | None = None,
        types: StringList | None = None,
        publishers: StringList | None = None,
        owners: StringList | None = None,
        **kwargs,
    ) -> DescribeAddonVersionsResponse:
        """Describes the versions for an add-on.

        Information such as the Kubernetes versions that you can use the add-on
        with, the ``owner``, ``publisher``, and the ``type`` of the add-on are
        returned.

        :param kubernetes_version: The Kubernetes versions that you can use the add-on with.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :param addon_name: The name of the add-on.
        :param types: The type of the add-on.
        :param publishers: The publisher of the add-on.
        :param owners: The owner of the add-on.
        :returns: DescribeAddonVersionsResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("DescribeCluster")
    def describe_cluster(
        self, context: RequestContext, name: String, **kwargs
    ) -> DescribeClusterResponse:
        """Describes an Amazon EKS cluster.

        The API server endpoint and certificate authority data returned by this
        operation are required for ``kubelet`` and ``kubectl`` to communicate
        with your Kubernetes API server. For more information, see `Creating or
        updating a ``kubeconfig`` file for an Amazon EKS
        cluster <https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html>`__.

        The API server endpoint and certificate authority data aren't available
        until the cluster reaches the ``ACTIVE`` state.

        :param name: The name of your cluster.
        :returns: DescribeClusterResponse
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeClusterVersions")
    def describe_cluster_versions(
        self,
        context: RequestContext,
        cluster_type: String | None = None,
        max_results: DescribeClusterVersionMaxResults | None = None,
        next_token: String | None = None,
        default_only: BoxedBoolean | None = None,
        include_all: BoxedBoolean | None = None,
        cluster_versions: StringList | None = None,
        status: ClusterVersionStatus | None = None,
        version_status: VersionStatus | None = None,
        **kwargs,
    ) -> DescribeClusterVersionsResponse:
        """Lists available Kubernetes versions for Amazon EKS clusters.

        :param cluster_type: The type of cluster to filter versions by.
        :param max_results: Maximum number of results to return.
        :param next_token: Pagination token for the next set of results.
        :param default_only: Filter to show only default versions.
        :param include_all: Include all available versions in the response.
        :param cluster_versions: List of specific cluster versions to describe.
        :param status: This field is deprecated.
        :param version_status: Filter versions by their current status.
        :returns: DescribeClusterVersionsResponse
        :raises ServerException:
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DescribeEksAnywhereSubscription")
    def describe_eks_anywhere_subscription(
        self, context: RequestContext, id: String, **kwargs
    ) -> DescribeEksAnywhereSubscriptionResponse:
        """Returns descriptive information about a subscription.

        :param id: The ID of the subscription.
        :returns: DescribeEksAnywhereSubscriptionResponse
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeFargateProfile")
    def describe_fargate_profile(
        self, context: RequestContext, cluster_name: String, fargate_profile_name: String, **kwargs
    ) -> DescribeFargateProfileResponse:
        """Describes an Fargate profile.

        :param cluster_name: The name of your cluster.
        :param fargate_profile_name: The name of the Fargate profile to describe.
        :returns: DescribeFargateProfileResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeIdentityProviderConfig")
    def describe_identity_provider_config(
        self,
        context: RequestContext,
        cluster_name: String,
        identity_provider_config: IdentityProviderConfig,
        **kwargs,
    ) -> DescribeIdentityProviderConfigResponse:
        """Describes an identity provider configuration.

        :param cluster_name: The name of your cluster.
        :param identity_provider_config: An object representing an identity provider configuration.
        :returns: DescribeIdentityProviderConfigResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribeInsight")
    def describe_insight(
        self, context: RequestContext, cluster_name: String, id: String, **kwargs
    ) -> DescribeInsightResponse:
        """Returns details about an insight that you specify using its ID.

        :param cluster_name: The name of the cluster to describe the insight for.
        :param id: The identity of the insight to describe.
        :returns: DescribeInsightResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("DescribeNodegroup")
    def describe_nodegroup(
        self, context: RequestContext, cluster_name: String, nodegroup_name: String, **kwargs
    ) -> DescribeNodegroupResponse:
        """Describes a managed node group.

        :param cluster_name: The name of your cluster.
        :param nodegroup_name: The name of the node group to describe.
        :returns: DescribeNodegroupResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("DescribePodIdentityAssociation")
    def describe_pod_identity_association(
        self, context: RequestContext, cluster_name: String, association_id: String, **kwargs
    ) -> DescribePodIdentityAssociationResponse:
        """Returns descriptive information about an EKS Pod Identity association.

        This action requires the ID of the association. You can get the ID from
        the response to the ``CreatePodIdentityAssocation`` for newly created
        associations. Or, you can list the IDs for associations with
        ``ListPodIdentityAssociations`` and filter the list by namespace or
        service account.

        :param cluster_name: The name of the cluster that the association is in.
        :param association_id: The ID of the association that you want the description of.
        :returns: DescribePodIdentityAssociationResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("DescribeUpdate")
    def describe_update(
        self,
        context: RequestContext,
        name: String,
        update_id: String,
        nodegroup_name: String | None = None,
        addon_name: String | None = None,
        **kwargs,
    ) -> DescribeUpdateResponse:
        """Describes an update to an Amazon EKS resource.

        When the status of the update is ``Successful``, the update is complete.
        If an update fails, the status is ``Failed``, and an error detail
        explains the reason for the failure.

        :param name: The name of the Amazon EKS cluster associated with the update.
        :param update_id: The ID of the update to describe.
        :param nodegroup_name: The name of the Amazon EKS node group associated with the update.
        :param addon_name: The name of the add-on.
        :returns: DescribeUpdateResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DisassociateAccessPolicy")
    def disassociate_access_policy(
        self,
        context: RequestContext,
        cluster_name: String,
        principal_arn: String,
        policy_arn: String,
        **kwargs,
    ) -> DisassociateAccessPolicyResponse:
        """Disassociates an access policy from an access entry.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The ARN of the IAM principal for the ``AccessEntry``.
        :param policy_arn: The ARN of the policy to disassociate from the access entry.
        :returns: DisassociateAccessPolicyResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("DisassociateIdentityProviderConfig")
    def disassociate_identity_provider_config(
        self,
        context: RequestContext,
        cluster_name: String,
        identity_provider_config: IdentityProviderConfig,
        client_request_token: String | None = None,
        **kwargs,
    ) -> DisassociateIdentityProviderConfigResponse:
        """Disassociates an identity provider configuration from a cluster.

        If you disassociate an identity provider from your cluster, users
        included in the provider can no longer access the cluster. However, you
        can still access the cluster with IAM principals.

        :param cluster_name: The name of your cluster.
        :param identity_provider_config: An object representing an identity provider configuration.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: DisassociateIdentityProviderConfigResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListAccessEntries")
    def list_access_entries(
        self,
        context: RequestContext,
        cluster_name: String,
        associated_policy_arn: String | None = None,
        max_results: ListAccessEntriesRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListAccessEntriesResponse:
        """Lists the access entries for your cluster.

        :param cluster_name: The name of your cluster.
        :param associated_policy_arn: The ARN of an ``AccessPolicy``.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListAccessEntriesResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("ListAccessPolicies")
    def list_access_policies(
        self,
        context: RequestContext,
        max_results: ListAccessPoliciesRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListAccessPoliciesResponse:
        """Lists the available access policies.

        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListAccessPoliciesResponse
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListAddons")
    def list_addons(
        self,
        context: RequestContext,
        cluster_name: ClusterName,
        max_results: ListAddonsRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListAddonsResponse:
        """Lists the installed add-ons.

        :param cluster_name: The name of your cluster.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListAddonsResponse
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        :raises ClientException:
        :raises ResourceNotFoundException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListAssociatedAccessPolicies")
    def list_associated_access_policies(
        self,
        context: RequestContext,
        cluster_name: String,
        principal_arn: String,
        max_results: ListAssociatedAccessPoliciesRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListAssociatedAccessPoliciesResponse:
        """Lists the access policies associated with an access entry.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The ARN of the IAM principal for the ``AccessEntry``.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListAssociatedAccessPoliciesResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("ListClusters")
    def list_clusters(
        self,
        context: RequestContext,
        max_results: ListClustersRequestMaxResults | None = None,
        next_token: String | None = None,
        include: IncludeClustersList | None = None,
        **kwargs,
    ) -> ListClustersResponse:
        """Lists the Amazon EKS clusters in your Amazon Web Services account in the
        specified Amazon Web Services Region.

        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :param include: Indicates whether external clusters are included in the returned list.
        :returns: ListClustersResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListEksAnywhereSubscriptions")
    def list_eks_anywhere_subscriptions(
        self,
        context: RequestContext,
        max_results: ListEksAnywhereSubscriptionsRequestMaxResults | None = None,
        next_token: String | None = None,
        include_status: EksAnywhereSubscriptionStatusValues | None = None,
        **kwargs,
    ) -> ListEksAnywhereSubscriptionsResponse:
        """Displays the full description of the subscription.

        :param max_results: The maximum number of cluster results returned by
        ListEksAnywhereSubscriptions in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``ListEksAnywhereSubscriptions`` request where ``maxResults`` was used
        and the results exceeded the value of that parameter.
        :param include_status: An array of subscription statuses to filter on.
        :returns: ListEksAnywhereSubscriptionsResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        """
        raise NotImplementedError

    @handler("ListFargateProfiles")
    def list_fargate_profiles(
        self,
        context: RequestContext,
        cluster_name: String,
        max_results: FargateProfilesRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListFargateProfilesResponse:
        """Lists the Fargate profiles associated with the specified cluster in your
        Amazon Web Services account in the specified Amazon Web Services Region.

        :param cluster_name: The name of your cluster.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListFargateProfilesResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListIdentityProviderConfigs")
    def list_identity_provider_configs(
        self,
        context: RequestContext,
        cluster_name: String,
        max_results: ListIdentityProviderConfigsRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListIdentityProviderConfigsResponse:
        """Lists the identity provider configurations for your cluster.

        :param cluster_name: The name of your cluster.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListIdentityProviderConfigsResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListInsights")
    def list_insights(
        self,
        context: RequestContext,
        cluster_name: String,
        filter: InsightsFilter | None = None,
        max_results: ListInsightsMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListInsightsResponse:
        """Returns a list of all insights checked for against the specified
        cluster. You can filter which insights are returned by category,
        associated Kubernetes version, and status.

        :param cluster_name: The name of the Amazon EKS cluster associated with the insights.
        :param filter: The criteria to filter your list of insights for your cluster.
        :param max_results: The maximum number of identity provider configurations returned by
        ``ListInsights`` in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``ListInsights`` request.
        :returns: ListInsightsResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("ListNodegroups")
    def list_nodegroups(
        self,
        context: RequestContext,
        cluster_name: String,
        max_results: ListNodegroupsRequestMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListNodegroupsResponse:
        """Lists the managed node groups associated with the specified cluster in
        your Amazon Web Services account in the specified Amazon Web Services
        Region. Self-managed node groups aren't listed.

        :param cluster_name: The name of your cluster.
        :param max_results: The maximum number of results, returned in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :returns: ListNodegroupsResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListPodIdentityAssociations")
    def list_pod_identity_associations(
        self,
        context: RequestContext,
        cluster_name: String,
        namespace: String | None = None,
        service_account: String | None = None,
        max_results: ListPodIdentityAssociationsMaxResults | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListPodIdentityAssociationsResponse:
        """List the EKS Pod Identity associations in a cluster. You can filter the
        list by the namespace that the association is in or the service account
        that the association uses.

        :param cluster_name: The name of the cluster that the associations are in.
        :param namespace: The name of the Kubernetes namespace inside the cluster that the
        associations are in.
        :param service_account: The name of the Kubernetes service account that the associations use.
        :param max_results: The maximum number of EKS Pod Identity association results returned by
        ``ListPodIdentityAssociations`` in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``ListUpdates`` request where ``maxResults`` was used and the results
        exceeded the value of that parameter.
        :returns: ListPodIdentityAssociationsResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: String, **kwargs
    ) -> ListTagsForResourceResponse:
        """List the tags for an Amazon EKS resource.

        :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource to list tags
        for.
        :returns: ListTagsForResourceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("ListUpdates")
    def list_updates(
        self,
        context: RequestContext,
        name: String,
        nodegroup_name: String | None = None,
        addon_name: String | None = None,
        next_token: String | None = None,
        max_results: ListUpdatesRequestMaxResults | None = None,
        **kwargs,
    ) -> ListUpdatesResponse:
        """Lists the updates associated with an Amazon EKS resource in your Amazon
        Web Services account, in the specified Amazon Web Services Region.

        :param name: The name of the Amazon EKS cluster to list updates for.
        :param nodegroup_name: The name of the Amazon EKS managed node group to list updates for.
        :param addon_name: The names of the installed add-ons that have available updates.
        :param next_token: The ``nextToken`` value returned from a previous paginated request,
        where ``maxResults`` was used and the results exceeded the value of that
        parameter.
        :param max_results: The maximum number of results, returned in paginated output.
        :returns: ListUpdatesResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("RegisterCluster")
    def register_cluster(
        self,
        context: RequestContext,
        name: ClusterName,
        connector_config: ConnectorConfigRequest,
        client_request_token: String | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> RegisterClusterResponse:
        """Connects a Kubernetes cluster to the Amazon EKS control plane.

        Any Kubernetes cluster can be connected to the Amazon EKS control plane
        to view current information about the cluster and its nodes.

        Cluster connection requires two steps. First, send a
        ```RegisterClusterRequest`` <https://docs.aws.amazon.com/eks/latest/APIReference/API_RegisterClusterRequest.html>`__
        to add it to the Amazon EKS control plane.

        Second, a
        `Manifest <https://amazon-eks.s3.us-west-2.amazonaws.com/eks-connector/manifests/eks-connector/latest/eks-connector.yaml>`__
        containing the ``activationID`` and ``activationCode`` must be applied
        to the Kubernetes cluster through it's native provider to provide
        visibility.

        After the manifest is updated and applied, the connected cluster is
        visible to the Amazon EKS control plane. If the manifest isn't applied
        within three days, the connected cluster will no longer be visible and
        must be deregistered using ``DeregisterCluster``.

        :param name: A unique name for this cluster in your Amazon Web Services Region.
        :param connector_config: The configuration settings required to connect the Kubernetes cluster to
        the Amazon EKS control plane.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param tags: Metadata that assists with categorization and organization.
        :returns: RegisterClusterResponse
        :raises ResourceLimitExceededException:
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ServiceUnavailableException:
        :raises AccessDeniedException:
        :raises ResourceInUseException:
        :raises ResourcePropagationDelayException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: String, tags: TagMap, **kwargs
    ) -> TagResourceResponse:
        """Associates the specified tags to an Amazon EKS resource with the
        specified ``resourceArn``. If existing tags on a resource are not
        specified in the request parameters, they aren't changed. When a
        resource is deleted, the tags associated with that resource are also
        deleted. Tags that you create for Amazon EKS resources don't propagate
        to any other resources associated with the cluster. For example, if you
        tag a cluster with this operation, that tag doesn't automatically
        propagate to the subnets and nodes associated with the cluster.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to add tags to.
        :param tags: Metadata that assists with categorization and organization.
        :returns: TagResourceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: String, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResponse:
        """Deletes specified tags from an Amazon EKS resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to delete tags from.
        :param tag_keys: The keys of the tags to remove.
        :returns: UntagResourceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateAccessEntry")
    def update_access_entry(
        self,
        context: RequestContext,
        cluster_name: String,
        principal_arn: String,
        kubernetes_groups: StringList | None = None,
        client_request_token: String | None = None,
        username: String | None = None,
        **kwargs,
    ) -> UpdateAccessEntryResponse:
        """Updates an access entry.

        :param cluster_name: The name of your cluster.
        :param principal_arn: The ARN of the IAM principal for the ``AccessEntry``.
        :param kubernetes_groups: The value for ``name`` that you've specified for ``kind: Group`` as a
        ``subject`` in a Kubernetes ``RoleBinding`` or ``ClusterRoleBinding``
        object.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param username: The username to authenticate to Kubernetes with.
        :returns: UpdateAccessEntryResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError

    @handler("UpdateAddon")
    def update_addon(
        self,
        context: RequestContext,
        cluster_name: ClusterName,
        addon_name: String,
        addon_version: String | None = None,
        service_account_role_arn: RoleArn | None = None,
        resolve_conflicts: ResolveConflicts | None = None,
        client_request_token: String | None = None,
        configuration_values: String | None = None,
        pod_identity_associations: AddonPodIdentityAssociationsList | None = None,
        **kwargs,
    ) -> UpdateAddonResponse:
        """Updates an Amazon EKS add-on.

        :param cluster_name: The name of your cluster.
        :param addon_name: The name of the add-on.
        :param addon_version: The version of the add-on.
        :param service_account_role_arn: The Amazon Resource Name (ARN) of an existing IAM role to bind to the
        add-on's service account.
        :param resolve_conflicts: How to resolve field value conflicts for an Amazon EKS add-on if you've
        changed a value from the Amazon EKS default value.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param configuration_values: The set of configuration values for the add-on that's created.
        :param pod_identity_associations: An array of Pod Identity Assocations to be updated.
        :returns: UpdateAddonResponse
        :raises InvalidParameterException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ResourceInUseException:
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("UpdateClusterConfig")
    def update_cluster_config(
        self,
        context: RequestContext,
        name: String,
        resources_vpc_config: VpcConfigRequest | None = None,
        logging: Logging | None = None,
        client_request_token: String | None = None,
        access_config: UpdateAccessConfigRequest | None = None,
        upgrade_policy: UpgradePolicyRequest | None = None,
        zonal_shift_config: ZonalShiftConfigRequest | None = None,
        compute_config: ComputeConfigRequest | None = None,
        kubernetes_network_config: KubernetesNetworkConfigRequest | None = None,
        storage_config: StorageConfigRequest | None = None,
        remote_network_config: RemoteNetworkConfigRequest | None = None,
        **kwargs,
    ) -> UpdateClusterConfigResponse:
        """Updates an Amazon EKS cluster configuration. Your cluster continues to
        function during the update. The response output includes an update ID
        that you can use to track the status of your cluster update with
        ``DescribeUpdate``.

        You can use this operation to do the following actions:

        -  You can use this API operation to enable or disable exporting the
           Kubernetes control plane logs for your cluster to CloudWatch Logs. By
           default, cluster control plane logs aren't exported to CloudWatch
           Logs. For more information, see `Amazon EKS Cluster control plane
           logs <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__
           in the *Amazon EKS User Guide* .

           CloudWatch Logs ingestion, archive storage, and data scanning rates
           apply to exported control plane logs. For more information, see
           `CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__.

        -  You can also use this API operation to enable or disable public and
           private access to your cluster's Kubernetes API server endpoint. By
           default, public access is enabled, and private access is disabled.
           For more information, see `Amazon EKS cluster endpoint access
           control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__
           in the *Amazon EKS User Guide* .

        -  You can also use this API operation to choose different subnets and
           security groups for the cluster. You must specify at least two
           subnets that are in different Availability Zones. You can't change
           which VPC the subnets are from, the subnets must be in the same VPC
           as the subnets that the cluster was created with. For more
           information about the VPC requirements, see
           https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html in
           the *Amazon EKS User Guide* .

        -  You can also use this API operation to enable or disable ARC zonal
           shift. If zonal shift is enabled, Amazon Web Services configures
           zonal autoshift for the cluster.

        -  You can also use this API operation to add, change, or remove the
           configuration in the cluster for EKS Hybrid Nodes. To remove the
           configuration, use the ``remoteNetworkConfig`` key with an object
           containing both subkeys with empty arrays for each. Here is an inline
           example:
           ``"remoteNetworkConfig": { "remoteNodeNetworks": [], "remotePodNetworks": [] }``.

        Cluster updates are asynchronous, and they should finish within a few
        minutes. During an update, the cluster status moves to ``UPDATING``
        (this status transition is eventually consistent). When the update is
        complete (either ``Failed`` or ``Successful``), the cluster status moves
        to ``Active``.

        :param name: The name of the Amazon EKS cluster to update.
        :param resources_vpc_config: An object representing the VPC configuration to use for an Amazon EKS
        cluster.
        :param logging: Enable or disable exporting the Kubernetes control plane logs for your
        cluster to CloudWatch Logs .
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param access_config: The access configuration for the cluster.
        :param upgrade_policy: You can enable or disable extended support for clusters currently on
        standard support.
        :param zonal_shift_config: Enable or disable ARC zonal shift for the cluster.
        :param compute_config: Update the configuration of the compute capability of your EKS Auto Mode
        cluster.
        :param kubernetes_network_config: The Kubernetes network configuration for the cluster.
        :param storage_config: Update the configuration of the block storage capability of your EKS
        Auto Mode cluster.
        :param remote_network_config: The configuration in the cluster for EKS Hybrid Nodes.
        :returns: UpdateClusterConfigResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateClusterVersion")
    def update_cluster_version(
        self,
        context: RequestContext,
        name: String,
        version: String,
        client_request_token: String | None = None,
        force: Boolean | None = None,
        **kwargs,
    ) -> UpdateClusterVersionResponse:
        """Updates an Amazon EKS cluster to the specified Kubernetes version. Your
        cluster continues to function during the update. The response output
        includes an update ID that you can use to track the status of your
        cluster update with the
        ```DescribeUpdate`` <https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html>`__
        API operation.

        Cluster updates are asynchronous, and they should finish within a few
        minutes. During an update, the cluster status moves to ``UPDATING``
        (this status transition is eventually consistent). When the update is
        complete (either ``Failed`` or ``Successful``), the cluster status moves
        to ``Active``.

        If your cluster has managed node groups attached to it, all of your node
        groups' Kubernetes versions must match the cluster's Kubernetes version
        in order to update the cluster to a new Kubernetes version.

        :param name: The name of the Amazon EKS cluster to update.
        :param version: The desired Kubernetes version following a successful update.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :param force: Set this value to ``true`` to override upgrade-blocking readiness checks
        when updating a cluster.
        :returns: UpdateClusterVersionResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises ThrottlingException:
        :raises InvalidStateException:
        """
        raise NotImplementedError

    @handler("UpdateEksAnywhereSubscription")
    def update_eks_anywhere_subscription(
        self,
        context: RequestContext,
        id: String,
        auto_renew: Boolean,
        client_request_token: String | None = None,
        **kwargs,
    ) -> UpdateEksAnywhereSubscriptionResponse:
        """Update an EKS Anywhere Subscription. Only auto renewal and tags can be
        updated after subscription creation.

        :param id: The ID of the subscription.
        :param auto_renew: A boolean indicating whether or not to automatically renew the
        subscription.
        :param client_request_token: Unique, case-sensitive identifier to ensure the idempotency of the
        request.
        :returns: UpdateEksAnywhereSubscriptionResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("UpdateNodegroupConfig")
    def update_nodegroup_config(
        self,
        context: RequestContext,
        cluster_name: String,
        nodegroup_name: String,
        labels: UpdateLabelsPayload | None = None,
        taints: UpdateTaintsPayload | None = None,
        scaling_config: NodegroupScalingConfig | None = None,
        update_config: NodegroupUpdateConfig | None = None,
        node_repair_config: NodeRepairConfig | None = None,
        client_request_token: String | None = None,
        **kwargs,
    ) -> UpdateNodegroupConfigResponse:
        """Updates an Amazon EKS managed node group configuration. Your node group
        continues to function during the update. The response output includes an
        update ID that you can use to track the status of your node group update
        with the
        ```DescribeUpdate`` <https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html>`__
        API operation. You can update the Kubernetes labels and taints for a
        node group and the scaling and version update configuration.

        :param cluster_name: The name of your cluster.
        :param nodegroup_name: The name of the managed node group to update.
        :param labels: The Kubernetes ``labels`` to apply to the nodes in the node group after
        the update.
        :param taints: The Kubernetes taints to be applied to the nodes in the node group after
        the update.
        :param scaling_config: The scaling configuration details for the Auto Scaling group after the
        update.
        :param update_config: The node group update configuration.
        :param node_repair_config: The node auto repair configuration for the node group.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: UpdateNodegroupConfigResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("UpdateNodegroupVersion")
    def update_nodegroup_version(
        self,
        context: RequestContext,
        cluster_name: String,
        nodegroup_name: String,
        version: String | None = None,
        release_version: String | None = None,
        launch_template: LaunchTemplateSpecification | None = None,
        force: Boolean | None = None,
        client_request_token: String | None = None,
        **kwargs,
    ) -> UpdateNodegroupVersionResponse:
        """Updates the Kubernetes version or AMI version of an Amazon EKS managed
        node group.

        You can update a node group using a launch template only if the node
        group was originally deployed with a launch template. Additionally, the
        launch template ID or name must match what was used when the node group
        was created. You can update the launch template version with necessary
        changes.

        If you need to update a custom AMI in a node group that was deployed
        with a launch template, then update your custom AMI, specify the new ID
        in a new version of the launch template, and then update the node group
        to the new version of the launch template.

        If you update without a launch template, then you can update to the
        latest available AMI version of a node group's current Kubernetes
        version by not specifying a Kubernetes version in the request. You can
        update to the latest AMI version of your cluster's current Kubernetes
        version by specifying your cluster's Kubernetes version in the request.
        For information about Linux versions, see `Amazon EKS optimized Amazon
        Linux AMI
        versions <https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html>`__
        in the *Amazon EKS User Guide*. For information about Windows versions,
        see `Amazon EKS optimized Windows AMI
        versions <https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html>`__
        in the *Amazon EKS User Guide*.

        You cannot roll back a node group to an earlier Kubernetes version or
        AMI version.

        When a node in a managed node group is terminated due to a scaling
        action or update, every ``Pod`` on that node is drained first. Amazon
        EKS attempts to drain the nodes gracefully and will fail if it is unable
        to do so. You can ``force`` the update if Amazon EKS is unable to drain
        the nodes as a result of a ``Pod`` disruption budget issue.

        :param cluster_name: The name of your cluster.
        :param nodegroup_name: The name of the managed node group to update.
        :param version: The Kubernetes version to update to.
        :param release_version: The AMI version of the Amazon EKS optimized AMI to use for the update.
        :param launch_template: An object representing a node group's launch template specification.
        :param force: Force the update if any ``Pod`` on the existing node group can't be
        drained due to a ``Pod`` disruption budget issue.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: UpdateNodegroupVersionResponse
        :raises InvalidParameterException:
        :raises ClientException:
        :raises ServerException:
        :raises ResourceInUseException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        """
        raise NotImplementedError

    @handler("UpdatePodIdentityAssociation")
    def update_pod_identity_association(
        self,
        context: RequestContext,
        cluster_name: String,
        association_id: String,
        role_arn: String | None = None,
        client_request_token: String | None = None,
        **kwargs,
    ) -> UpdatePodIdentityAssociationResponse:
        """Updates a EKS Pod Identity association. Only the IAM role can be
        changed; an association can't be moved between clusters, namespaces, or
        service accounts. If you need to edit the namespace or service account,
        you need to delete the association and then create a new association
        with your desired settings.

        :param cluster_name: The name of the cluster that you want to update the association in.
        :param association_id: The ID of the association to be updated.
        :param role_arn: The new IAM role to change the.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the request.
        :returns: UpdatePodIdentityAssociationResponse
        :raises ServerException:
        :raises ResourceNotFoundException:
        :raises InvalidRequestException:
        :raises InvalidParameterException:
        """
        raise NotImplementedError
