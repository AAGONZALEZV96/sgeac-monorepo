from datetime import datetime
from enum import StrEnum
from typing import List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

ACLName = str
AccessString = str
AwsQueryErrorMessage = str
Boolean = bool
BooleanOptional = bool
Double = float
FilterName = str
FilterValue = str
Integer = int
IntegerOptional = int
KmsKeyId = str
String = str
TargetBucket = str
UserName = str


class AZStatus(StrEnum):
    singleaz = "singleaz"
    multiaz = "multiaz"


class AuthenticationType(StrEnum):
    password = "password"
    no_password = "no-password"
    iam = "iam"


class DataTieringStatus(StrEnum):
    true = "true"
    false = "false"


class InputAuthenticationType(StrEnum):
    password = "password"
    iam = "iam"


class IpDiscovery(StrEnum):
    ipv4 = "ipv4"
    ipv6 = "ipv6"


class NetworkType(StrEnum):
    ipv4 = "ipv4"
    ipv6 = "ipv6"
    dual_stack = "dual_stack"


class ServiceUpdateStatus(StrEnum):
    available = "available"
    in_progress = "in-progress"
    complete = "complete"
    scheduled = "scheduled"


class ServiceUpdateType(StrEnum):
    security_update = "security-update"


class SourceType(StrEnum):
    node = "node"
    parameter_group = "parameter-group"
    subnet_group = "subnet-group"
    cluster = "cluster"
    user = "user"
    acl = "acl"


class UpdateStrategy(StrEnum):
    coordinated = "coordinated"
    uncoordinated = "uncoordinated"


class ACLAlreadyExistsFault(ServiceException):
    code: str = "ACLAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class ACLNotFoundFault(ServiceException):
    code: str = "ACLNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ACLQuotaExceededFault(ServiceException):
    code: str = "ACLQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class APICallRateForCustomerExceededFault(ServiceException):
    code: str = "APICallRateForCustomerExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class ClusterAlreadyExistsFault(ServiceException):
    code: str = "ClusterAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class ClusterNotFoundFault(ServiceException):
    code: str = "ClusterNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ClusterQuotaForCustomerExceededFault(ServiceException):
    code: str = "ClusterQuotaForCustomerExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class DefaultUserRequired(ServiceException):
    code: str = "DefaultUserRequired"
    sender_fault: bool = False
    status_code: int = 400


class DuplicateUserNameFault(ServiceException):
    code: str = "DuplicateUserNameFault"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientClusterCapacityFault(ServiceException):
    code: str = "InsufficientClusterCapacityFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidACLStateFault(ServiceException):
    code: str = "InvalidACLStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidARNFault(ServiceException):
    code: str = "InvalidARNFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidClusterStateFault(ServiceException):
    code: str = "InvalidClusterStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidCredentialsException(ServiceException):
    code: str = "InvalidCredentialsException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidKMSKeyFault(ServiceException):
    code: str = "InvalidKMSKeyFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidMultiRegionClusterStateFault(ServiceException):
    """The requested operation cannot be performed on the multi-Region cluster
    in its current state.
    """

    code: str = "InvalidMultiRegionClusterStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidNodeStateFault(ServiceException):
    code: str = "InvalidNodeStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterCombinationException(ServiceException):
    code: str = "InvalidParameterCombinationException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterGroupStateFault(ServiceException):
    code: str = "InvalidParameterGroupStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterValueException(ServiceException):
    code: str = "InvalidParameterValueException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSnapshotStateFault(ServiceException):
    code: str = "InvalidSnapshotStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSubnet(ServiceException):
    code: str = "InvalidSubnet"
    sender_fault: bool = False
    status_code: int = 400


class InvalidUserStateFault(ServiceException):
    code: str = "InvalidUserStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidVPCNetworkStateFault(ServiceException):
    code: str = "InvalidVPCNetworkStateFault"
    sender_fault: bool = False
    status_code: int = 400


class MultiRegionClusterAlreadyExistsFault(ServiceException):
    """A multi-Region cluster with the specified name already exists."""

    code: str = "MultiRegionClusterAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class MultiRegionClusterNotFoundFault(ServiceException):
    """The specified multi-Region cluster does not exist."""

    code: str = "MultiRegionClusterNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class MultiRegionParameterGroupNotFoundFault(ServiceException):
    """The specified multi-Region parameter group does not exist."""

    code: str = "MultiRegionParameterGroupNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class NoOperationFault(ServiceException):
    code: str = "NoOperationFault"
    sender_fault: bool = False
    status_code: int = 400


class NodeQuotaForClusterExceededFault(ServiceException):
    code: str = "NodeQuotaForClusterExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class NodeQuotaForCustomerExceededFault(ServiceException):
    code: str = "NodeQuotaForCustomerExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class ParameterGroupAlreadyExistsFault(ServiceException):
    code: str = "ParameterGroupAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class ParameterGroupNotFoundFault(ServiceException):
    code: str = "ParameterGroupNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ParameterGroupQuotaExceededFault(ServiceException):
    code: str = "ParameterGroupQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class ReservedNodeAlreadyExistsFault(ServiceException):
    """You already have a reservation with the given identifier."""

    code: str = "ReservedNodeAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class ReservedNodeNotFoundFault(ServiceException):
    """The requested node does not exist."""

    code: str = "ReservedNodeNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ReservedNodeQuotaExceededFault(ServiceException):
    """The request cannot be processed because it would exceed the user's node
    quota.
    """

    code: str = "ReservedNodeQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class ReservedNodesOfferingNotFoundFault(ServiceException):
    """The requested node offering does not exist."""

    code: str = "ReservedNodesOfferingNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ServiceLinkedRoleNotFoundFault(ServiceException):
    code: str = "ServiceLinkedRoleNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ServiceUpdateNotFoundFault(ServiceException):
    code: str = "ServiceUpdateNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ShardNotFoundFault(ServiceException):
    code: str = "ShardNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ShardsPerClusterQuotaExceededFault(ServiceException):
    code: str = "ShardsPerClusterQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class SnapshotAlreadyExistsFault(ServiceException):
    code: str = "SnapshotAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class SnapshotNotFoundFault(ServiceException):
    code: str = "SnapshotNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class SnapshotQuotaExceededFault(ServiceException):
    code: str = "SnapshotQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetGroupAlreadyExistsFault(ServiceException):
    code: str = "SubnetGroupAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetGroupInUseFault(ServiceException):
    code: str = "SubnetGroupInUseFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetGroupNotFoundFault(ServiceException):
    code: str = "SubnetGroupNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetGroupQuotaExceededFault(ServiceException):
    code: str = "SubnetGroupQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetInUse(ServiceException):
    code: str = "SubnetInUse"
    sender_fault: bool = False
    status_code: int = 400


class SubnetNotAllowedFault(ServiceException):
    code: str = "SubnetNotAllowedFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetQuotaExceededFault(ServiceException):
    code: str = "SubnetQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class TagNotFoundFault(ServiceException):
    code: str = "TagNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class TagQuotaPerResourceExceeded(ServiceException):
    code: str = "TagQuotaPerResourceExceeded"
    sender_fault: bool = False
    status_code: int = 400


class TestFailoverNotAvailableFault(ServiceException):
    code: str = "TestFailoverNotAvailableFault"
    sender_fault: bool = False
    status_code: int = 400


class UserAlreadyExistsFault(ServiceException):
    code: str = "UserAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400


class UserNotFoundFault(ServiceException):
    code: str = "UserNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class UserQuotaExceededFault(ServiceException):
    code: str = "UserQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


ACLClusterNameList = List[String]
UserNameList = List[UserName]


class ACLPendingChanges(TypedDict, total=False):
    """Returns the updates being applied to the ACL."""

    UserNamesToRemove: Optional[UserNameList]
    UserNamesToAdd: Optional[UserNameList]


class ACL(TypedDict, total=False):
    """An Access Control List. You can authenticate users with Access Contol
    Lists. ACLs enable you to control cluster access by grouping users.
    These Access control lists are designed as a way to organize access to
    clusters.
    """

    Name: Optional[String]
    Status: Optional[String]
    UserNames: Optional[UserNameList]
    MinimumEngineVersion: Optional[String]
    PendingChanges: Optional[ACLPendingChanges]
    Clusters: Optional[ACLClusterNameList]
    ARN: Optional[String]


ACLList = List[ACL]
ACLNameList = List[ACLName]


class ACLsUpdateStatus(TypedDict, total=False):
    """The status of the ACL update"""

    ACLToApply: Optional[ACLName]


class Authentication(TypedDict, total=False):
    """Denotes the user's authentication properties, such as whether it
    requires a password to authenticate. Used in output responses.
    """

    Type: Optional[AuthenticationType]
    PasswordCount: Optional[IntegerOptional]


PasswordListInput = List[String]


class AuthenticationMode(TypedDict, total=False):
    """Denotes the user's authentication properties, such as whether it
    requires a password to authenticate. Used in output responses.
    """

    Type: Optional[InputAuthenticationType]
    Passwords: Optional[PasswordListInput]


class AvailabilityZone(TypedDict, total=False):
    """Indicates if the cluster has a Multi-AZ configuration (multiaz) or not
    (singleaz).
    """

    Name: Optional[String]


class ServiceUpdateRequest(TypedDict, total=False):
    """A request to apply a service update"""

    ServiceUpdateNameToApply: Optional[String]


ClusterNameList = List[String]


class BatchUpdateClusterRequest(ServiceRequest):
    ClusterNames: ClusterNameList
    ServiceUpdate: Optional[ServiceUpdateRequest]


class UnprocessedCluster(TypedDict, total=False):
    """A cluster whose updates have failed"""

    ClusterName: Optional[String]
    ErrorType: Optional[String]
    ErrorMessage: Optional[String]


UnprocessedClusterList = List[UnprocessedCluster]


class SecurityGroupMembership(TypedDict, total=False):
    """Represents a single security group and its status."""

    SecurityGroupId: Optional[String]
    Status: Optional[String]


SecurityGroupMembershipList = List[SecurityGroupMembership]


class Endpoint(TypedDict, total=False):
    """Represents the information required for client programs to connect to
    the cluster and its nodes.
    """

    Address: Optional[String]
    Port: Optional[Integer]


TStamp = datetime


class Node(TypedDict, total=False):
    """Represents an individual node within a cluster. Each node runs its own
    instance of the cluster's protocol-compliant caching software.
    """

    Name: Optional[String]
    Status: Optional[String]
    AvailabilityZone: Optional[String]
    CreateTime: Optional[TStamp]
    Endpoint: Optional[Endpoint]


NodeList = List[Node]


class Shard(TypedDict, total=False):
    """Represents a collection of nodes in a cluster. One node in the node
    group is the read/write primary node. All the other nodes are read-only
    Replica nodes.
    """

    Name: Optional[String]
    Status: Optional[String]
    Slots: Optional[String]
    Nodes: Optional[NodeList]
    NumberOfNodes: Optional[IntegerOptional]


ShardList = List[Shard]


class PendingModifiedServiceUpdate(TypedDict, total=False):
    """Update action that has yet to be processed for the corresponding
    apply/stop request
    """

    ServiceUpdateName: Optional[String]
    Status: Optional[ServiceUpdateStatus]


PendingModifiedServiceUpdateList = List[PendingModifiedServiceUpdate]


class SlotMigration(TypedDict, total=False):
    """Represents the progress of an online resharding operation."""

    ProgressPercentage: Optional[Double]


class ReshardingStatus(TypedDict, total=False):
    """The status of the online resharding"""

    SlotMigration: Optional[SlotMigration]


class ClusterPendingUpdates(TypedDict, total=False):
    """A list of updates being applied to the cluster"""

    Resharding: Optional[ReshardingStatus]
    ACLs: Optional[ACLsUpdateStatus]
    ServiceUpdates: Optional[PendingModifiedServiceUpdateList]


class Cluster(TypedDict, total=False):
    """Contains all of the attributes of a specific cluster."""

    Name: Optional[String]
    Description: Optional[String]
    Status: Optional[String]
    PendingUpdates: Optional[ClusterPendingUpdates]
    MultiRegionClusterName: Optional[String]
    NumberOfShards: Optional[IntegerOptional]
    Shards: Optional[ShardList]
    AvailabilityMode: Optional[AZStatus]
    ClusterEndpoint: Optional[Endpoint]
    NodeType: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    EnginePatchVersion: Optional[String]
    ParameterGroupName: Optional[String]
    ParameterGroupStatus: Optional[String]
    SecurityGroups: Optional[SecurityGroupMembershipList]
    SubnetGroupName: Optional[String]
    TLSEnabled: Optional[BooleanOptional]
    KmsKeyId: Optional[String]
    ARN: Optional[String]
    SnsTopicArn: Optional[String]
    SnsTopicStatus: Optional[String]
    SnapshotRetentionLimit: Optional[IntegerOptional]
    MaintenanceWindow: Optional[String]
    SnapshotWindow: Optional[String]
    ACLName: Optional[ACLName]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    DataTiering: Optional[DataTieringStatus]
    NetworkType: Optional[NetworkType]
    IpDiscovery: Optional[IpDiscovery]


ClusterList = List[Cluster]


class BatchUpdateClusterResponse(TypedDict, total=False):
    ProcessedClusters: Optional[ClusterList]
    UnprocessedClusters: Optional[UnprocessedClusterList]


class ShardConfiguration(TypedDict, total=False):
    """Shard configuration options. Each shard configuration has the following:
    Slots and ReplicaCount.
    """

    Slots: Optional[String]
    ReplicaCount: Optional[IntegerOptional]


class ShardDetail(TypedDict, total=False):
    """Provides details of a shard in a snapshot"""

    Name: Optional[String]
    Configuration: Optional[ShardConfiguration]
    Size: Optional[String]
    SnapshotCreationTime: Optional[TStamp]


ShardDetails = List[ShardDetail]


class ClusterConfiguration(TypedDict, total=False):
    """A list of cluster configuration options."""

    Name: Optional[String]
    Description: Optional[String]
    NodeType: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    MaintenanceWindow: Optional[String]
    TopicArn: Optional[String]
    Port: Optional[IntegerOptional]
    ParameterGroupName: Optional[String]
    SubnetGroupName: Optional[String]
    VpcId: Optional[String]
    SnapshotRetentionLimit: Optional[IntegerOptional]
    SnapshotWindow: Optional[String]
    NumShards: Optional[IntegerOptional]
    Shards: Optional[ShardDetails]
    MultiRegionParameterGroupName: Optional[String]
    MultiRegionClusterName: Optional[String]


class Tag(TypedDict, total=False):
    """A tag that can be added to an MemoryDB resource. Tags are composed of a
    Key/Value pair. You can use tags to categorize and track all your
    MemoryDB resources. When you add or remove tags on clusters, those
    actions will be replicated to all nodes in the cluster. A tag with a
    null Value is permitted. For more information, see `Tagging your
    MemoryDB
    resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging-resources.html>`__
    """

    Key: Optional[String]
    Value: Optional[String]


TagList = List[Tag]


class CopySnapshotRequest(ServiceRequest):
    SourceSnapshotName: String
    TargetSnapshotName: String
    TargetBucket: Optional[TargetBucket]
    KmsKeyId: Optional[KmsKeyId]
    Tags: Optional[TagList]


class Snapshot(TypedDict, total=False):
    """Represents a copy of an entire cluster as of the time when the snapshot
    was taken.
    """

    Name: Optional[String]
    Status: Optional[String]
    Source: Optional[String]
    KmsKeyId: Optional[String]
    ARN: Optional[String]
    ClusterConfiguration: Optional[ClusterConfiguration]
    DataTiering: Optional[DataTieringStatus]


class CopySnapshotResponse(TypedDict, total=False):
    Snapshot: Optional[Snapshot]


UserNameListInput = List[UserName]


class CreateACLRequest(ServiceRequest):
    ACLName: String
    UserNames: Optional[UserNameListInput]
    Tags: Optional[TagList]


class CreateACLResponse(TypedDict, total=False):
    ACL: Optional[ACL]


SnapshotArnsList = List[String]
SecurityGroupIdsList = List[String]


class CreateClusterRequest(ServiceRequest):
    ClusterName: String
    NodeType: String
    MultiRegionClusterName: Optional[String]
    ParameterGroupName: Optional[String]
    Description: Optional[String]
    NumShards: Optional[IntegerOptional]
    NumReplicasPerShard: Optional[IntegerOptional]
    SubnetGroupName: Optional[String]
    SecurityGroupIds: Optional[SecurityGroupIdsList]
    MaintenanceWindow: Optional[String]
    Port: Optional[IntegerOptional]
    SnsTopicArn: Optional[String]
    TLSEnabled: Optional[BooleanOptional]
    KmsKeyId: Optional[String]
    SnapshotArns: Optional[SnapshotArnsList]
    SnapshotName: Optional[String]
    SnapshotRetentionLimit: Optional[IntegerOptional]
    Tags: Optional[TagList]
    SnapshotWindow: Optional[String]
    ACLName: ACLName
    Engine: Optional[String]
    EngineVersion: Optional[String]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    DataTiering: Optional[BooleanOptional]
    NetworkType: Optional[NetworkType]
    IpDiscovery: Optional[IpDiscovery]


class CreateClusterResponse(TypedDict, total=False):
    Cluster: Optional[Cluster]


class CreateMultiRegionClusterRequest(ServiceRequest):
    MultiRegionClusterNameSuffix: String
    Description: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    NodeType: String
    MultiRegionParameterGroupName: Optional[String]
    NumShards: Optional[IntegerOptional]
    TLSEnabled: Optional[BooleanOptional]
    Tags: Optional[TagList]


class RegionalCluster(TypedDict, total=False):
    """Represents a Regional cluster"""

    ClusterName: Optional[String]
    Region: Optional[String]
    Status: Optional[String]
    ARN: Optional[String]


RegionalClusterList = List[RegionalCluster]


class MultiRegionCluster(TypedDict, total=False):
    """Represents a multi-Region cluster."""

    MultiRegionClusterName: Optional[String]
    Description: Optional[String]
    Status: Optional[String]
    NodeType: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    NumberOfShards: Optional[IntegerOptional]
    Clusters: Optional[RegionalClusterList]
    MultiRegionParameterGroupName: Optional[String]
    TLSEnabled: Optional[BooleanOptional]
    ARN: Optional[String]


class CreateMultiRegionClusterResponse(TypedDict, total=False):
    MultiRegionCluster: Optional[MultiRegionCluster]


class CreateParameterGroupRequest(ServiceRequest):
    ParameterGroupName: String
    Family: String
    Description: Optional[String]
    Tags: Optional[TagList]


class ParameterGroup(TypedDict, total=False):
    """Represents the output of a CreateParameterGroup operation. A parameter
    group represents a combination of specific values for the parameters
    that are passed to the engine software during startup.
    """

    Name: Optional[String]
    Family: Optional[String]
    Description: Optional[String]
    ARN: Optional[String]


class CreateParameterGroupResponse(TypedDict, total=False):
    ParameterGroup: Optional[ParameterGroup]


class CreateSnapshotRequest(ServiceRequest):
    ClusterName: String
    SnapshotName: String
    KmsKeyId: Optional[String]
    Tags: Optional[TagList]


class CreateSnapshotResponse(TypedDict, total=False):
    Snapshot: Optional[Snapshot]


SubnetIdentifierList = List[String]


class CreateSubnetGroupRequest(ServiceRequest):
    SubnetGroupName: String
    Description: Optional[String]
    SubnetIds: SubnetIdentifierList
    Tags: Optional[TagList]


NetworkTypeList = List[NetworkType]


class Subnet(TypedDict, total=False):
    """Represents the subnet associated with a cluster. This parameter refers
    to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used
    with MemoryDB.
    """

    Identifier: Optional[String]
    AvailabilityZone: Optional[AvailabilityZone]
    SupportedNetworkTypes: Optional[NetworkTypeList]


SubnetList = List[Subnet]


class SubnetGroup(TypedDict, total=False):
    """Represents the output of one of the following operations:

    -  CreateSubnetGroup

    -  UpdateSubnetGroup

    A subnet group is a collection of subnets (typically private) that you
    can designate for your clusters running in an Amazon Virtual Private
    Cloud (VPC) environment.
    """

    Name: Optional[String]
    Description: Optional[String]
    VpcId: Optional[String]
    Subnets: Optional[SubnetList]
    ARN: Optional[String]
    SupportedNetworkTypes: Optional[NetworkTypeList]


class CreateSubnetGroupResponse(TypedDict, total=False):
    SubnetGroup: Optional[SubnetGroup]


class CreateUserRequest(ServiceRequest):
    UserName: UserName
    AuthenticationMode: AuthenticationMode
    AccessString: AccessString
    Tags: Optional[TagList]


class User(TypedDict, total=False):
    """You create users and assign them specific permissions by using an access
    string. You assign the users to Access Control Lists aligned with a
    specific role (administrators, human resources) that are then deployed
    to one or more MemoryDB clusters.
    """

    Name: Optional[String]
    Status: Optional[String]
    AccessString: Optional[String]
    ACLNames: Optional[ACLNameList]
    MinimumEngineVersion: Optional[String]
    Authentication: Optional[Authentication]
    ARN: Optional[String]


class CreateUserResponse(TypedDict, total=False):
    User: Optional[User]


class DeleteACLRequest(ServiceRequest):
    ACLName: String


class DeleteACLResponse(TypedDict, total=False):
    ACL: Optional[ACL]


class DeleteClusterRequest(ServiceRequest):
    ClusterName: String
    MultiRegionClusterName: Optional[String]
    FinalSnapshotName: Optional[String]


class DeleteClusterResponse(TypedDict, total=False):
    Cluster: Optional[Cluster]


class DeleteMultiRegionClusterRequest(ServiceRequest):
    MultiRegionClusterName: String


class DeleteMultiRegionClusterResponse(TypedDict, total=False):
    MultiRegionCluster: Optional[MultiRegionCluster]


class DeleteParameterGroupRequest(ServiceRequest):
    ParameterGroupName: String


class DeleteParameterGroupResponse(TypedDict, total=False):
    ParameterGroup: Optional[ParameterGroup]


class DeleteSnapshotRequest(ServiceRequest):
    SnapshotName: String


class DeleteSnapshotResponse(TypedDict, total=False):
    Snapshot: Optional[Snapshot]


class DeleteSubnetGroupRequest(ServiceRequest):
    SubnetGroupName: String


class DeleteSubnetGroupResponse(TypedDict, total=False):
    SubnetGroup: Optional[SubnetGroup]


class DeleteUserRequest(ServiceRequest):
    UserName: UserName


class DeleteUserResponse(TypedDict, total=False):
    User: Optional[User]


class DescribeACLsRequest(ServiceRequest):
    ACLName: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


class DescribeACLsResponse(TypedDict, total=False):
    ACLs: Optional[ACLList]
    NextToken: Optional[String]


class DescribeClustersRequest(ServiceRequest):
    ClusterName: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]
    ShowShardDetails: Optional[BooleanOptional]


class DescribeClustersResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Clusters: Optional[ClusterList]


class DescribeEngineVersionsRequest(ServiceRequest):
    Engine: Optional[String]
    EngineVersion: Optional[String]
    ParameterGroupFamily: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]
    DefaultOnly: Optional[Boolean]


class EngineVersionInfo(TypedDict, total=False):
    """Provides details of the Redis OSS engine version"""

    Engine: Optional[String]
    EngineVersion: Optional[String]
    EnginePatchVersion: Optional[String]
    ParameterGroupFamily: Optional[String]


EngineVersionInfoList = List[EngineVersionInfo]


class DescribeEngineVersionsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    EngineVersions: Optional[EngineVersionInfoList]


class DescribeEventsRequest(ServiceRequest):
    SourceName: Optional[String]
    SourceType: Optional[SourceType]
    StartTime: Optional[TStamp]
    EndTime: Optional[TStamp]
    Duration: Optional[IntegerOptional]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


class Event(TypedDict, total=False):
    """Represents a single occurrence of something interesting within the
    system. Some examples of events are creating a cluster or adding or
    removing a node.
    """

    SourceName: Optional[String]
    SourceType: Optional[SourceType]
    Message: Optional[String]
    Date: Optional[TStamp]


EventList = List[Event]


class DescribeEventsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Events: Optional[EventList]


class DescribeMultiRegionClustersRequest(ServiceRequest):
    MultiRegionClusterName: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]
    ShowClusterDetails: Optional[BooleanOptional]


MultiRegionClusterList = List[MultiRegionCluster]


class DescribeMultiRegionClustersResponse(TypedDict, total=False):
    NextToken: Optional[String]
    MultiRegionClusters: Optional[MultiRegionClusterList]


class DescribeParameterGroupsRequest(ServiceRequest):
    ParameterGroupName: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


ParameterGroupList = List[ParameterGroup]


class DescribeParameterGroupsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    ParameterGroups: Optional[ParameterGroupList]


class DescribeParametersRequest(ServiceRequest):
    ParameterGroupName: String
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


class Parameter(TypedDict, total=False):
    """Describes an individual setting that controls some aspect of MemoryDB
    behavior.
    """

    Name: Optional[String]
    Value: Optional[String]
    Description: Optional[String]
    DataType: Optional[String]
    AllowedValues: Optional[String]
    MinimumEngineVersion: Optional[String]


ParametersList = List[Parameter]


class DescribeParametersResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Parameters: Optional[ParametersList]


class DescribeReservedNodesOfferingsRequest(ServiceRequest):
    ReservedNodesOfferingId: Optional[String]
    NodeType: Optional[String]
    Duration: Optional[String]
    OfferingType: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


class RecurringCharge(TypedDict, total=False):
    """The recurring charge to run this reserved node."""

    RecurringChargeAmount: Optional[Double]
    RecurringChargeFrequency: Optional[String]


RecurringChargeList = List[RecurringCharge]


class ReservedNodesOffering(TypedDict, total=False):
    """The offering type of this node."""

    ReservedNodesOfferingId: Optional[String]
    NodeType: Optional[String]
    Duration: Optional[Integer]
    FixedPrice: Optional[Double]
    OfferingType: Optional[String]
    RecurringCharges: Optional[RecurringChargeList]


ReservedNodesOfferingList = List[ReservedNodesOffering]


class DescribeReservedNodesOfferingsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    ReservedNodesOfferings: Optional[ReservedNodesOfferingList]


class DescribeReservedNodesRequest(ServiceRequest):
    ReservationId: Optional[String]
    ReservedNodesOfferingId: Optional[String]
    NodeType: Optional[String]
    Duration: Optional[String]
    OfferingType: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


class ReservedNode(TypedDict, total=False):
    """Represents the output of a ``PurchaseReservedNodesOffering`` operation."""

    ReservationId: Optional[String]
    ReservedNodesOfferingId: Optional[String]
    NodeType: Optional[String]
    StartTime: Optional[TStamp]
    Duration: Optional[Integer]
    FixedPrice: Optional[Double]
    NodeCount: Optional[Integer]
    OfferingType: Optional[String]
    State: Optional[String]
    RecurringCharges: Optional[RecurringChargeList]
    ARN: Optional[String]


ReservedNodeList = List[ReservedNode]


class DescribeReservedNodesResponse(TypedDict, total=False):
    NextToken: Optional[String]
    ReservedNodes: Optional[ReservedNodeList]


ServiceUpdateStatusList = List[ServiceUpdateStatus]


class DescribeServiceUpdatesRequest(ServiceRequest):
    ServiceUpdateName: Optional[String]
    ClusterNames: Optional[ClusterNameList]
    Status: Optional[ServiceUpdateStatusList]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


class ServiceUpdate(TypedDict, total=False):
    """An update that you can apply to your MemoryDB clusters."""

    ClusterName: Optional[String]
    ServiceUpdateName: Optional[String]
    ReleaseDate: Optional[TStamp]
    Description: Optional[String]
    Status: Optional[ServiceUpdateStatus]
    Type: Optional[ServiceUpdateType]
    Engine: Optional[String]
    NodesUpdated: Optional[String]
    AutoUpdateStartDate: Optional[TStamp]


ServiceUpdateList = List[ServiceUpdate]


class DescribeServiceUpdatesResponse(TypedDict, total=False):
    NextToken: Optional[String]
    ServiceUpdates: Optional[ServiceUpdateList]


class DescribeSnapshotsRequest(ServiceRequest):
    ClusterName: Optional[String]
    SnapshotName: Optional[String]
    Source: Optional[String]
    NextToken: Optional[String]
    MaxResults: Optional[IntegerOptional]
    ShowDetail: Optional[BooleanOptional]


SnapshotList = List[Snapshot]


class DescribeSnapshotsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Snapshots: Optional[SnapshotList]


class DescribeSubnetGroupsRequest(ServiceRequest):
    SubnetGroupName: Optional[String]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


SubnetGroupList = List[SubnetGroup]


class DescribeSubnetGroupsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    SubnetGroups: Optional[SubnetGroupList]


FilterValueList = List[FilterValue]


class Filter(TypedDict, total=False):
    """Used to streamline results of a search based on the property being
    filtered.
    """

    Name: FilterName
    Values: FilterValueList


FilterList = List[Filter]


class DescribeUsersRequest(ServiceRequest):
    UserName: Optional[UserName]
    Filters: Optional[FilterList]
    MaxResults: Optional[IntegerOptional]
    NextToken: Optional[String]


UserList = List[User]


class DescribeUsersResponse(TypedDict, total=False):
    Users: Optional[UserList]
    NextToken: Optional[String]


class FailoverShardRequest(ServiceRequest):
    ClusterName: String
    ShardName: String


class FailoverShardResponse(TypedDict, total=False):
    Cluster: Optional[Cluster]


KeyList = List[String]


class ListAllowedMultiRegionClusterUpdatesRequest(ServiceRequest):
    MultiRegionClusterName: String


NodeTypeList = List[String]


class ListAllowedMultiRegionClusterUpdatesResponse(TypedDict, total=False):
    ScaleUpNodeTypes: Optional[NodeTypeList]
    ScaleDownNodeTypes: Optional[NodeTypeList]


class ListAllowedNodeTypeUpdatesRequest(ServiceRequest):
    ClusterName: String


class ListAllowedNodeTypeUpdatesResponse(TypedDict, total=False):
    ScaleUpNodeTypes: Optional[NodeTypeList]
    ScaleDownNodeTypes: Optional[NodeTypeList]


class ListTagsRequest(ServiceRequest):
    ResourceArn: String


class ListTagsResponse(TypedDict, total=False):
    TagList: Optional[TagList]


ParameterNameList = List[String]


class ParameterNameValue(TypedDict, total=False):
    """Describes a name-value pair that is used to update the value of a
    parameter.
    """

    ParameterName: Optional[String]
    ParameterValue: Optional[String]


ParameterNameValueList = List[ParameterNameValue]


class PurchaseReservedNodesOfferingRequest(ServiceRequest):
    ReservedNodesOfferingId: String
    ReservationId: Optional[String]
    NodeCount: Optional[IntegerOptional]
    Tags: Optional[TagList]


class PurchaseReservedNodesOfferingResponse(TypedDict, total=False):
    ReservedNode: Optional[ReservedNode]


class ReplicaConfigurationRequest(TypedDict, total=False):
    """A request to configure the number of replicas in a shard"""

    ReplicaCount: Optional[Integer]


class ResetParameterGroupRequest(ServiceRequest):
    ParameterGroupName: String
    AllParameters: Optional[Boolean]
    ParameterNames: Optional[ParameterNameList]


class ResetParameterGroupResponse(TypedDict, total=False):
    ParameterGroup: Optional[ParameterGroup]


class ShardConfigurationRequest(TypedDict, total=False):
    """A request to configure the sharding properties of a cluster"""

    ShardCount: Optional[Integer]


class TagResourceRequest(ServiceRequest):
    ResourceArn: String
    Tags: TagList


class TagResourceResponse(TypedDict, total=False):
    TagList: Optional[TagList]


class UntagResourceRequest(ServiceRequest):
    ResourceArn: String
    TagKeys: KeyList


class UntagResourceResponse(TypedDict, total=False):
    TagList: Optional[TagList]


class UpdateACLRequest(ServiceRequest):
    ACLName: String
    UserNamesToAdd: Optional[UserNameListInput]
    UserNamesToRemove: Optional[UserNameListInput]


class UpdateACLResponse(TypedDict, total=False):
    ACL: Optional[ACL]


class UpdateClusterRequest(ServiceRequest):
    ClusterName: String
    Description: Optional[String]
    SecurityGroupIds: Optional[SecurityGroupIdsList]
    MaintenanceWindow: Optional[String]
    SnsTopicArn: Optional[String]
    SnsTopicStatus: Optional[String]
    ParameterGroupName: Optional[String]
    SnapshotWindow: Optional[String]
    SnapshotRetentionLimit: Optional[IntegerOptional]
    NodeType: Optional[String]
    Engine: Optional[String]
    EngineVersion: Optional[String]
    ReplicaConfiguration: Optional[ReplicaConfigurationRequest]
    ShardConfiguration: Optional[ShardConfigurationRequest]
    ACLName: Optional[ACLName]
    IpDiscovery: Optional[IpDiscovery]


class UpdateClusterResponse(TypedDict, total=False):
    Cluster: Optional[Cluster]


class UpdateMultiRegionClusterRequest(ServiceRequest):
    MultiRegionClusterName: String
    NodeType: Optional[String]
    Description: Optional[String]
    EngineVersion: Optional[String]
    ShardConfiguration: Optional[ShardConfigurationRequest]
    MultiRegionParameterGroupName: Optional[String]
    UpdateStrategy: Optional[UpdateStrategy]


class UpdateMultiRegionClusterResponse(TypedDict, total=False):
    MultiRegionCluster: Optional[MultiRegionCluster]


class UpdateParameterGroupRequest(ServiceRequest):
    ParameterGroupName: String
    ParameterNameValues: ParameterNameValueList


class UpdateParameterGroupResponse(TypedDict, total=False):
    ParameterGroup: Optional[ParameterGroup]


class UpdateSubnetGroupRequest(ServiceRequest):
    SubnetGroupName: String
    Description: Optional[String]
    SubnetIds: Optional[SubnetIdentifierList]


class UpdateSubnetGroupResponse(TypedDict, total=False):
    SubnetGroup: Optional[SubnetGroup]


class UpdateUserRequest(ServiceRequest):
    UserName: UserName
    AuthenticationMode: Optional[AuthenticationMode]
    AccessString: Optional[AccessString]


class UpdateUserResponse(TypedDict, total=False):
    User: Optional[User]


class MemorydbApi:
    service = "memorydb"
    version = "2021-01-01"

    @handler("BatchUpdateCluster")
    def batch_update_cluster(
        self,
        context: RequestContext,
        cluster_names: ClusterNameList,
        service_update: ServiceUpdateRequest | None = None,
        **kwargs,
    ) -> BatchUpdateClusterResponse:
        """Apply the service update to a list of clusters supplied. For more
        information on service updates and applying them, see `Applying the
        service
        updates <https://docs.aws.amazon.com/MemoryDB/latest/devguide/managing-updates.html#applying-updates>`__.

        :param cluster_names: The cluster names to apply the updates.
        :param service_update: The unique ID of the service update.
        :returns: BatchUpdateClusterResponse
        :raises ServiceUpdateNotFoundFault:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("CopySnapshot")
    def copy_snapshot(
        self,
        context: RequestContext,
        source_snapshot_name: String,
        target_snapshot_name: String,
        target_bucket: TargetBucket | None = None,
        kms_key_id: KmsKeyId | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CopySnapshotResponse:
        """Makes a copy of an existing snapshot.

        :param source_snapshot_name: The name of an existing snapshot from which to make a copy.
        :param target_snapshot_name: A name for the snapshot copy.
        :param target_bucket: The Amazon S3 bucket to which the snapshot is exported.
        :param kms_key_id: The ID of the KMS key used to encrypt the target snapshot.
        :param tags: A list of tags to be added to this resource.
        :returns: CopySnapshotResponse
        :raises SnapshotAlreadyExistsFault:
        :raises SnapshotNotFoundFault:
        :raises SnapshotQuotaExceededFault:
        :raises InvalidSnapshotStateFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        :raises TagQuotaPerResourceExceeded:
        """
        raise NotImplementedError

    @handler("CreateACL")
    def create_acl(
        self,
        context: RequestContext,
        acl_name: String,
        user_names: UserNameListInput | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateACLResponse:
        """Creates an Access Control List. For more information, see
        `Authenticating users with Access Contol Lists
        (ACLs) <https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html>`__.

        :param acl_name: The name of the Access Control List.
        :param user_names: The list of users that belong to the Access Control List.
        :param tags: A list of tags to be added to this resource.
        :returns: CreateACLResponse
        :raises UserNotFoundFault:
        :raises DuplicateUserNameFault:
        :raises ACLAlreadyExistsFault:
        :raises DefaultUserRequired:
        :raises ACLQuotaExceededFault:
        :raises InvalidParameterValueException:
        :raises TagQuotaPerResourceExceeded:
        """
        raise NotImplementedError

    @handler("CreateCluster")
    def create_cluster(
        self,
        context: RequestContext,
        cluster_name: String,
        node_type: String,
        acl_name: ACLName,
        multi_region_cluster_name: String | None = None,
        parameter_group_name: String | None = None,
        description: String | None = None,
        num_shards: IntegerOptional | None = None,
        num_replicas_per_shard: IntegerOptional | None = None,
        subnet_group_name: String | None = None,
        security_group_ids: SecurityGroupIdsList | None = None,
        maintenance_window: String | None = None,
        port: IntegerOptional | None = None,
        sns_topic_arn: String | None = None,
        tls_enabled: BooleanOptional | None = None,
        kms_key_id: String | None = None,
        snapshot_arns: SnapshotArnsList | None = None,
        snapshot_name: String | None = None,
        snapshot_retention_limit: IntegerOptional | None = None,
        tags: TagList | None = None,
        snapshot_window: String | None = None,
        engine: String | None = None,
        engine_version: String | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        data_tiering: BooleanOptional | None = None,
        network_type: NetworkType | None = None,
        ip_discovery: IpDiscovery | None = None,
        **kwargs,
    ) -> CreateClusterResponse:
        """Creates a cluster. All nodes in the cluster run the same
        protocol-compliant engine software.

        :param cluster_name: The name of the cluster.
        :param node_type: The compute and memory capacity of the nodes in the cluster.
        :param acl_name: The name of the Access Control List to associate with the cluster.
        :param multi_region_cluster_name: The name of the multi-Region cluster to be created.
        :param parameter_group_name: The name of the parameter group associated with the cluster.
        :param description: An optional description of the cluster.
        :param num_shards: The number of shards the cluster will contain.
        :param num_replicas_per_shard: The number of replicas to apply to each shard.
        :param subnet_group_name: The name of the subnet group to be used for the cluster.
        :param security_group_ids: A list of security group names to associate with this cluster.
        :param maintenance_window: Specifies the weekly time range during which maintenance on the cluster
        is performed.
        :param port: The port number on which each of the nodes accepts connections.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service
        (SNS) topic to which notifications are sent.
        :param tls_enabled: A flag to enable in-transit encryption on the cluster.
        :param kms_key_id: The ID of the KMS key used to encrypt the cluster.
        :param snapshot_arns: A list of Amazon Resource Names (ARN) that uniquely identify the RDB
        snapshot files stored in Amazon S3.
        :param snapshot_name: The name of a snapshot from which to restore data into the new cluster.
        :param snapshot_retention_limit: The number of days for which MemoryDB retains automatic snapshots before
        deleting them.
        :param tags: A list of tags to be added to this resource.
        :param snapshot_window: The daily time range (in UTC) during which MemoryDB begins taking a
        daily snapshot of your shard.
        :param engine: The name of the engine to be used for the cluster.
        :param engine_version: The version number of the Redis OSS engine to be used for the cluster.
        :param auto_minor_version_upgrade: When set to true, the cluster will automatically receive minor engine
        version upgrades after launch.
        :param data_tiering: Enables data tiering.
        :param network_type: Specifies the IP address type for the cluster.
        :param ip_discovery: The mechanism for discovering IP addresses for the cluster discovery
        protocol.
        :returns: CreateClusterResponse
        :raises ClusterAlreadyExistsFault:
        :raises SubnetGroupNotFoundFault:
        :raises ClusterQuotaForCustomerExceededFault:
        :raises NodeQuotaForClusterExceededFault:
        :raises NodeQuotaForCustomerExceededFault:
        :raises ParameterGroupNotFoundFault:
        :raises InsufficientClusterCapacityFault:
        :raises InvalidVPCNetworkStateFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises ShardsPerClusterQuotaExceededFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        :raises InvalidCredentialsException:
        :raises TagQuotaPerResourceExceeded:
        :raises ACLNotFoundFault:
        :raises InvalidACLStateFault:
        :raises MultiRegionClusterNotFoundFault:
        :raises InvalidMultiRegionClusterStateFault:
        """
        raise NotImplementedError

    @handler("CreateMultiRegionCluster")
    def create_multi_region_cluster(
        self,
        context: RequestContext,
        multi_region_cluster_name_suffix: String,
        node_type: String,
        description: String | None = None,
        engine: String | None = None,
        engine_version: String | None = None,
        multi_region_parameter_group_name: String | None = None,
        num_shards: IntegerOptional | None = None,
        tls_enabled: BooleanOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateMultiRegionClusterResponse:
        """Creates a new multi-Region cluster.

        :param multi_region_cluster_name_suffix: A suffix to be added to the Multi-Region cluster name.
        :param node_type: The node type to be used for the multi-Region cluster.
        :param description: A description for the multi-Region cluster.
        :param engine: The name of the engine to be used for the multi-Region cluster.
        :param engine_version: The version of the engine to be used for the multi-Region cluster.
        :param multi_region_parameter_group_name: The name of the multi-Region parameter group to be associated with the
        cluster.
        :param num_shards: The number of shards for the multi-Region cluster.
        :param tls_enabled: Whether to enable TLS encryption for the multi-Region cluster.
        :param tags: A list of tags to be applied to the multi-Region cluster.
        :returns: CreateMultiRegionClusterResponse
        :raises MultiRegionClusterAlreadyExistsFault:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterValueException:
        :raises MultiRegionParameterGroupNotFoundFault:
        :raises ClusterQuotaForCustomerExceededFault:
        :raises TagQuotaPerResourceExceeded:
        """
        raise NotImplementedError

    @handler("CreateParameterGroup")
    def create_parameter_group(
        self,
        context: RequestContext,
        parameter_group_name: String,
        family: String,
        description: String | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateParameterGroupResponse:
        """Creates a new MemoryDB parameter group. A parameter group is a
        collection of parameters and their values that are applied to all of the
        nodes in any cluster. For more information, see `Configuring engine
        parameters using parameter
        groups <https://docs.aws.amazon.com/MemoryDB/latest/devguide/parametergroups.html>`__.

        :param parameter_group_name: The name of the parameter group.
        :param family: The name of the parameter group family that the parameter group can be
        used with.
        :param description: An optional description of the parameter group.
        :param tags: A list of tags to be added to this resource.
        :returns: CreateParameterGroupResponse
        :raises ParameterGroupQuotaExceededFault:
        :raises ParameterGroupAlreadyExistsFault:
        :raises InvalidParameterGroupStateFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises TagQuotaPerResourceExceeded:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("CreateSnapshot")
    def create_snapshot(
        self,
        context: RequestContext,
        cluster_name: String,
        snapshot_name: String,
        kms_key_id: String | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateSnapshotResponse:
        """Creates a copy of an entire cluster at a specific moment in time.

        :param cluster_name: The snapshot is created from this cluster.
        :param snapshot_name: A name for the snapshot being created.
        :param kms_key_id: The ID of the KMS key used to encrypt the snapshot.
        :param tags: A list of tags to be added to this resource.
        :returns: CreateSnapshotResponse
        :raises SnapshotAlreadyExistsFault:
        :raises ClusterNotFoundFault:
        :raises InvalidClusterStateFault:
        :raises SnapshotQuotaExceededFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterValueException:
        :raises TagQuotaPerResourceExceeded:
        """
        raise NotImplementedError

    @handler("CreateSubnetGroup")
    def create_subnet_group(
        self,
        context: RequestContext,
        subnet_group_name: String,
        subnet_ids: SubnetIdentifierList,
        description: String | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateSubnetGroupResponse:
        """Creates a subnet group. A subnet group is a collection of subnets
        (typically private) that you can designate for your clusters running in
        an Amazon Virtual Private Cloud (VPC) environment. When you create a
        cluster in an Amazon VPC, you must specify a subnet group. MemoryDB uses
        that subnet group to choose a subnet and IP addresses within that subnet
        to associate with your nodes. For more information, see `Subnets and
        subnet
        groups <https://docs.aws.amazon.com/MemoryDB/latest/devguide/subnetgroups.html>`__.

        :param subnet_group_name: The name of the subnet group.
        :param subnet_ids: A list of VPC subnet IDs for the subnet group.
        :param description: A description for the subnet group.
        :param tags: A list of tags to be added to this resource.
        :returns: CreateSubnetGroupResponse
        :raises SubnetGroupAlreadyExistsFault:
        :raises SubnetGroupQuotaExceededFault:
        :raises SubnetQuotaExceededFault:
        :raises InvalidSubnet:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises SubnetNotAllowedFault:
        :raises TagQuotaPerResourceExceeded:
        """
        raise NotImplementedError

    @handler("CreateUser")
    def create_user(
        self,
        context: RequestContext,
        user_name: UserName,
        authentication_mode: AuthenticationMode,
        access_string: AccessString,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateUserResponse:
        """Creates a MemoryDB user. For more information, see `Authenticating users
        with Access Contol Lists
        (ACLs) <https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html>`__.

        :param user_name: The name of the user.
        :param authentication_mode: Denotes the user's authentication properties, such as whether it
        requires a password to authenticate.
        :param access_string: Access permissions string used for this user.
        :param tags: A list of tags to be added to this resource.
        :returns: CreateUserResponse
        :raises UserAlreadyExistsFault:
        :raises UserQuotaExceededFault:
        :raises DuplicateUserNameFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        :raises TagQuotaPerResourceExceeded:
        """
        raise NotImplementedError

    @handler("DeleteACL")
    def delete_acl(self, context: RequestContext, acl_name: String, **kwargs) -> DeleteACLResponse:
        """Deletes an Access Control List. The ACL must first be disassociated from
        the cluster before it can be deleted. For more information, see
        `Authenticating users with Access Contol Lists
        (ACLs) <https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html>`__.

        :param acl_name: The name of the Access Control List to delete.
        :returns: DeleteACLResponse
        :raises ACLNotFoundFault:
        :raises InvalidACLStateFault:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("DeleteCluster")
    def delete_cluster(
        self,
        context: RequestContext,
        cluster_name: String,
        multi_region_cluster_name: String | None = None,
        final_snapshot_name: String | None = None,
        **kwargs,
    ) -> DeleteClusterResponse:
        """Deletes a cluster. It also deletes all associated nodes and node
        endpoints.

        ``CreateSnapshot`` permission is required to create a final snapshot.
        Without this permission, the API call will fail with an
        ``Access Denied`` exception.

        :param cluster_name: The name of the cluster to be deleted.
        :param multi_region_cluster_name: The name of the multi-Region cluster to be deleted.
        :param final_snapshot_name: The user-supplied name of a final cluster snapshot.
        :returns: DeleteClusterResponse
        :raises ClusterNotFoundFault:
        :raises InvalidClusterStateFault:
        :raises SnapshotAlreadyExistsFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DeleteMultiRegionCluster")
    def delete_multi_region_cluster(
        self, context: RequestContext, multi_region_cluster_name: String, **kwargs
    ) -> DeleteMultiRegionClusterResponse:
        """Deletes an existing multi-Region cluster.

        :param multi_region_cluster_name: The name of the multi-Region cluster to be deleted.
        :returns: DeleteMultiRegionClusterResponse
        :raises MultiRegionClusterNotFoundFault:
        :raises InvalidMultiRegionClusterStateFault:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("DeleteParameterGroup")
    def delete_parameter_group(
        self, context: RequestContext, parameter_group_name: String, **kwargs
    ) -> DeleteParameterGroupResponse:
        """Deletes the specified parameter group. You cannot delete a parameter
        group if it is associated with any clusters. You cannot delete the
        default parameter groups in your account.

        :param parameter_group_name: The name of the parameter group to delete.
        :returns: DeleteParameterGroupResponse
        :raises InvalidParameterGroupStateFault:
        :raises ParameterGroupNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DeleteSnapshot")
    def delete_snapshot(
        self, context: RequestContext, snapshot_name: String, **kwargs
    ) -> DeleteSnapshotResponse:
        """Deletes an existing snapshot. When you receive a successful response
        from this operation, MemoryDB immediately begins deleting the snapshot;
        you cannot cancel or revert this operation.

        :param snapshot_name: The name of the snapshot to delete.
        :returns: DeleteSnapshotResponse
        :raises SnapshotNotFoundFault:
        :raises InvalidSnapshotStateFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DeleteSubnetGroup")
    def delete_subnet_group(
        self, context: RequestContext, subnet_group_name: String, **kwargs
    ) -> DeleteSubnetGroupResponse:
        """Deletes a subnet group. You cannot delete a default subnet group or one
        that is associated with any clusters.

        :param subnet_group_name: The name of the subnet group to delete.
        :returns: DeleteSubnetGroupResponse
        :raises SubnetGroupInUseFault:
        :raises SubnetGroupNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteUser")
    def delete_user(
        self, context: RequestContext, user_name: UserName, **kwargs
    ) -> DeleteUserResponse:
        """Deletes a user. The user will be removed from all ACLs and in turn
        removed from all clusters.

        :param user_name: The name of the user to delete.
        :returns: DeleteUserResponse
        :raises InvalidUserStateFault:
        :raises UserNotFoundFault:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("DescribeACLs")
    def describe_ac_ls(
        self,
        context: RequestContext,
        acl_name: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeACLsResponse:
        """Returns a list of ACLs.

        :param acl_name: The name of the ACL.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeACLsResponse
        :raises ACLNotFoundFault:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeClusters")
    def describe_clusters(
        self,
        context: RequestContext,
        cluster_name: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        show_shard_details: BooleanOptional | None = None,
        **kwargs,
    ) -> DescribeClustersResponse:
        """Returns information about all provisioned clusters if no cluster
        identifier is specified, or about a specific cluster if a cluster name
        is supplied.

        :param cluster_name: The name of the cluster.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :param show_shard_details: An optional flag that can be included in the request to retrieve
        information about the individual shard(s).
        :returns: DescribeClustersResponse
        :raises ClusterNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeEngineVersions")
    def describe_engine_versions(
        self,
        context: RequestContext,
        engine: String | None = None,
        engine_version: String | None = None,
        parameter_group_family: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        default_only: Boolean | None = None,
        **kwargs,
    ) -> DescribeEngineVersionsResponse:
        """Returns a list of the available Redis OSS engine versions.

        :param engine: The name of the engine for which to list available versions.
        :param engine_version: The Redis OSS engine version.
        :param parameter_group_family: The name of a specific parameter group family to return details for.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :param default_only: If true, specifies that only the default version of the specified engine
        or engine and major version combination is to be returned.
        :returns: DescribeEngineVersionsResponse
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeEvents")
    def describe_events(
        self,
        context: RequestContext,
        source_name: String | None = None,
        source_type: SourceType | None = None,
        start_time: TStamp | None = None,
        end_time: TStamp | None = None,
        duration: IntegerOptional | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeEventsResponse:
        """Returns events related to clusters, security groups, and parameter
        groups. You can obtain events specific to a particular cluster, security
        group, or parameter group by providing the name as a parameter. By
        default, only the events occurring within the last hour are returned;
        however, you can retrieve up to 14 days' worth of events if necessary.

        :param source_name: The identifier of the event source for which events are returned.
        :param source_type: The event source to retrieve events for.
        :param start_time: The beginning of the time interval to retrieve events for, specified in
        ISO 8601 format.
        :param end_time: The end of the time interval for which to retrieve events, specified in
        ISO 8601 format.
        :param duration: The number of minutes worth of events to retrieve.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeEventsResponse
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeMultiRegionClusters")
    def describe_multi_region_clusters(
        self,
        context: RequestContext,
        multi_region_cluster_name: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        show_cluster_details: BooleanOptional | None = None,
        **kwargs,
    ) -> DescribeMultiRegionClustersResponse:
        """Returns details about one or more multi-Region clusters.

        :param multi_region_cluster_name: The name of a specific multi-Region cluster to describe.
        :param max_results: The maximum number of results to return.
        :param next_token: A token to specify where to start paginating.
        :param show_cluster_details: Details about the multi-Region cluster.
        :returns: DescribeMultiRegionClustersResponse
        :raises ClusterNotFoundFault:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterValueException:
        :raises MultiRegionClusterNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeParameterGroups")
    def describe_parameter_groups(
        self,
        context: RequestContext,
        parameter_group_name: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeParameterGroupsResponse:
        """Returns a list of parameter group descriptions. If a parameter group
        name is specified, the list contains only the descriptions for that
        group.

        :param parameter_group_name: The name of a specific parameter group to return details for.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeParameterGroupsResponse
        :raises ParameterGroupNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeParameters")
    def describe_parameters(
        self,
        context: RequestContext,
        parameter_group_name: String,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeParametersResponse:
        """Returns the detailed parameter list for a particular parameter group.

        :param parameter_group_name: he name of a specific parameter group to return details for.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeParametersResponse
        :raises ParameterGroupNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeReservedNodes")
    def describe_reserved_nodes(
        self,
        context: RequestContext,
        reservation_id: String | None = None,
        reserved_nodes_offering_id: String | None = None,
        node_type: String | None = None,
        duration: String | None = None,
        offering_type: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeReservedNodesResponse:
        """Returns information about reserved nodes for this account, or about a
        specified reserved node.

        :param reservation_id: The reserved node identifier filter value.
        :param reserved_nodes_offering_id: The offering identifier filter value.
        :param node_type: The node type filter value.
        :param duration: The duration filter value, specified in years or seconds.
        :param offering_type: The offering type filter value.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional marker returned from a prior request.
        :returns: DescribeReservedNodesResponse
        :raises ReservedNodeNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeReservedNodesOfferings")
    def describe_reserved_nodes_offerings(
        self,
        context: RequestContext,
        reserved_nodes_offering_id: String | None = None,
        node_type: String | None = None,
        duration: String | None = None,
        offering_type: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeReservedNodesOfferingsResponse:
        """Lists available reserved node offerings.

        :param reserved_nodes_offering_id: The offering identifier filter value.
        :param node_type: The node type for the reserved nodes.
        :param duration: Duration filter value, specified in years or seconds.
        :param offering_type: The offering type filter value.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional marker returned from a prior request.
        :returns: DescribeReservedNodesOfferingsResponse
        :raises ReservedNodesOfferingNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeServiceUpdates")
    def describe_service_updates(
        self,
        context: RequestContext,
        service_update_name: String | None = None,
        cluster_names: ClusterNameList | None = None,
        status: ServiceUpdateStatusList | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeServiceUpdatesResponse:
        """Returns details of the service updates.

        :param service_update_name: The unique ID of the service update to describe.
        :param cluster_names: The list of cluster names to identify service updates to apply.
        :param status: The status(es) of the service updates to filter on.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeServiceUpdatesResponse
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeSnapshots")
    def describe_snapshots(
        self,
        context: RequestContext,
        cluster_name: String | None = None,
        snapshot_name: String | None = None,
        source: String | None = None,
        next_token: String | None = None,
        max_results: IntegerOptional | None = None,
        show_detail: BooleanOptional | None = None,
        **kwargs,
    ) -> DescribeSnapshotsResponse:
        """Returns information about cluster snapshots. By default,
        DescribeSnapshots lists all of your snapshots; it can optionally
        describe a single snapshot, or just the snapshots associated with a
        particular cluster.

        :param cluster_name: A user-supplied cluster identifier.
        :param snapshot_name: A user-supplied name of the snapshot.
        :param source: If set to system, the output shows snapshots that were automatically
        created by MemoryDB.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :param max_results: The maximum number of records to include in the response.
        :param show_detail: A Boolean value which if true, the shard configuration is included in
        the snapshot description.
        :returns: DescribeSnapshotsResponse
        :raises SnapshotNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("DescribeSubnetGroups")
    def describe_subnet_groups(
        self,
        context: RequestContext,
        subnet_group_name: String | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeSubnetGroupsResponse:
        """Returns a list of subnet group descriptions. If a subnet group name is
        specified, the list contains only the description of that group.

        :param subnet_group_name: The name of the subnet group to return details for.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeSubnetGroupsResponse
        :raises SubnetGroupNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeUsers")
    def describe_users(
        self,
        context: RequestContext,
        user_name: UserName | None = None,
        filters: FilterList | None = None,
        max_results: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeUsersResponse:
        """Returns a list of users.

        :param user_name: The name of the user.
        :param filters: Filter to determine the list of users to return.
        :param max_results: The maximum number of records to include in the response.
        :param next_token: An optional argument to pass in case the total number of records exceeds
        the value of MaxResults.
        :returns: DescribeUsersResponse
        :raises UserNotFoundFault:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("FailoverShard")
    def failover_shard(
        self, context: RequestContext, cluster_name: String, shard_name: String, **kwargs
    ) -> FailoverShardResponse:
        """Used to failover a shard. This API is designed for testing the behavior
        of your application in case of MemoryDB failover. It is not designed to
        be used as a production-level tool for initiating a failover to overcome
        a problem you may have with the cluster. Moreover, in certain conditions
        such as large scale operational events, Amazon may block this API.

        :param cluster_name: The cluster being failed over.
        :param shard_name: The name of the shard.
        :returns: FailoverShardResponse
        :raises APICallRateForCustomerExceededFault:
        :raises InvalidClusterStateFault:
        :raises ShardNotFoundFault:
        :raises ClusterNotFoundFault:
        :raises TestFailoverNotAvailableFault:
        :raises InvalidKMSKeyFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("ListAllowedMultiRegionClusterUpdates")
    def list_allowed_multi_region_cluster_updates(
        self, context: RequestContext, multi_region_cluster_name: String, **kwargs
    ) -> ListAllowedMultiRegionClusterUpdatesResponse:
        """Lists the allowed updates for a multi-Region cluster.

        :param multi_region_cluster_name: The name of the multi-Region cluster.
        :returns: ListAllowedMultiRegionClusterUpdatesResponse
        :raises MultiRegionClusterNotFoundFault:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("ListAllowedNodeTypeUpdates")
    def list_allowed_node_type_updates(
        self, context: RequestContext, cluster_name: String, **kwargs
    ) -> ListAllowedNodeTypeUpdatesResponse:
        """Lists all available node types that you can scale to from your cluster's
        current node type. When you use the UpdateCluster operation to scale
        your cluster, the value of the NodeType parameter must be one of the
        node types returned by this operation.

        :param cluster_name: The name of the cluster you want to scale.
        :returns: ListAllowedNodeTypeUpdatesResponse
        :raises ClusterNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("ListTags")
    def list_tags(
        self, context: RequestContext, resource_arn: String, **kwargs
    ) -> ListTagsResponse:
        """Lists all tags currently on a named resource. A tag is a key-value pair
        where the key and value are case-sensitive. You can use tags to
        categorize and track your MemoryDB resources. For more information, see
        `Tagging your MemoryDB
        resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html>`__.

        When you add or remove tags from multi region clusters, you might not
        immediately see the latest effective tags in the ListTags API response
        due to it being eventually consistent specifically for multi region
        clusters. For more information, see `Tagging your MemoryDB
        resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource for which you want the
        list of tags.
        :returns: ListTagsResponse
        :raises ClusterNotFoundFault:
        :raises InvalidClusterStateFault:
        :raises ParameterGroupNotFoundFault:
        :raises SubnetGroupNotFoundFault:
        :raises SnapshotNotFoundFault:
        :raises InvalidARNFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises UserNotFoundFault:
        :raises ACLNotFoundFault:
        :raises MultiRegionClusterNotFoundFault:
        :raises MultiRegionParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("PurchaseReservedNodesOffering")
    def purchase_reserved_nodes_offering(
        self,
        context: RequestContext,
        reserved_nodes_offering_id: String,
        reservation_id: String | None = None,
        node_count: IntegerOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> PurchaseReservedNodesOfferingResponse:
        """Allows you to purchase a reserved node offering. Reserved nodes are not
        eligible for cancellation and are non-refundable.

        :param reserved_nodes_offering_id: The ID of the reserved node offering to purchase.
        :param reservation_id: A customer-specified identifier to track this reservation.
        :param node_count: The number of node instances to reserve.
        :param tags: A list of tags to be added to this resource.
        :returns: PurchaseReservedNodesOfferingResponse
        :raises ReservedNodesOfferingNotFoundFault:
        :raises ReservedNodeAlreadyExistsFault:
        :raises ReservedNodeQuotaExceededFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises TagQuotaPerResourceExceeded:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("ResetParameterGroup")
    def reset_parameter_group(
        self,
        context: RequestContext,
        parameter_group_name: String,
        all_parameters: Boolean | None = None,
        parameter_names: ParameterNameList | None = None,
        **kwargs,
    ) -> ResetParameterGroupResponse:
        """Modifies the parameters of a parameter group to the engine or system
        default value. You can reset specific parameters by submitting a list of
        parameter names. To reset the entire parameter group, specify the
        AllParameters and ParameterGroupName parameters.

        :param parameter_group_name: The name of the parameter group to reset.
        :param all_parameters: If true, all parameters in the parameter group are reset to their
        default values.
        :param parameter_names: An array of parameter names to reset to their default values.
        :returns: ResetParameterGroupResponse
        :raises InvalidParameterGroupStateFault:
        :raises ParameterGroupNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: String, tags: TagList, **kwargs
    ) -> TagResourceResponse:
        """Use this operation to add tags to a resource. A tag is a key-value pair
        where the key and value are case-sensitive. You can use tags to
        categorize and track all your MemoryDB resources. For more information,
        see `Tagging your MemoryDB
        resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html>`__.

        When you add tags to multi region clusters, you might not immediately
        see the latest effective tags in the ListTags API response due to it
        being eventually consistent specifically for multi region clusters. For
        more information, see `Tagging your MemoryDB
        resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html>`__.

        You can specify cost-allocation tags for your MemoryDB resources, Amazon
        generates a cost allocation report as a comma-separated value (CSV) file
        with your usage and costs aggregated by your tags. You can apply tags
        that represent business categories (such as cost centers, application
        names, or owners) to organize your costs across multiple services. For
        more information, see `Using Cost Allocation
        Tags <https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to which the tags are to
        be added.
        :param tags: A list of tags to be added to this resource.
        :returns: TagResourceResponse
        :raises ClusterNotFoundFault:
        :raises ParameterGroupNotFoundFault:
        :raises SubnetGroupNotFoundFault:
        :raises InvalidClusterStateFault:
        :raises SnapshotNotFoundFault:
        :raises UserNotFoundFault:
        :raises ACLNotFoundFault:
        :raises MultiRegionClusterNotFoundFault:
        :raises MultiRegionParameterGroupNotFoundFault:
        :raises TagQuotaPerResourceExceeded:
        :raises InvalidARNFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: String, tag_keys: KeyList, **kwargs
    ) -> UntagResourceResponse:
        """Use this operation to remove tags on a resource. A tag is a key-value
        pair where the key and value are case-sensitive. You can use tags to
        categorize and track all your MemoryDB resources. For more information,
        see `Tagging your MemoryDB
        resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html>`__.

        When you remove tags from multi region clusters, you might not
        immediately see the latest effective tags in the ListTags API response
        due to it being eventually consistent specifically for multi region
        clusters. For more information, see `Tagging your MemoryDB
        resources <https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html>`__.

        You can specify cost-allocation tags for your MemoryDB resources, Amazon
        generates a cost allocation report as a comma-separated value (CSV) file
        with your usage and costs aggregated by your tags. You can apply tags
        that represent business categories (such as cost centers, application
        names, or owners) to organize your costs across multiple services. For
        more information, see `Using Cost Allocation
        Tags <https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to which the tags are to
        be removed.
        :param tag_keys: The list of keys of the tags that are to be removed.
        :returns: UntagResourceResponse
        :raises ClusterNotFoundFault:
        :raises InvalidClusterStateFault:
        :raises ParameterGroupNotFoundFault:
        :raises SubnetGroupNotFoundFault:
        :raises SnapshotNotFoundFault:
        :raises InvalidARNFault:
        :raises TagNotFoundFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises UserNotFoundFault:
        :raises ACLNotFoundFault:
        :raises InvalidParameterValueException:
        :raises MultiRegionClusterNotFoundFault:
        :raises MultiRegionParameterGroupNotFoundFault:
        """
        raise NotImplementedError

    @handler("UpdateACL")
    def update_acl(
        self,
        context: RequestContext,
        acl_name: String,
        user_names_to_add: UserNameListInput | None = None,
        user_names_to_remove: UserNameListInput | None = None,
        **kwargs,
    ) -> UpdateACLResponse:
        """Changes the list of users that belong to the Access Control List.

        :param acl_name: The name of the Access Control List.
        :param user_names_to_add: The list of users to add to the Access Control List.
        :param user_names_to_remove: The list of users to remove from the Access Control List.
        :returns: UpdateACLResponse
        :raises ACLNotFoundFault:
        :raises UserNotFoundFault:
        :raises DuplicateUserNameFault:
        :raises DefaultUserRequired:
        :raises InvalidACLStateFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("UpdateCluster")
    def update_cluster(
        self,
        context: RequestContext,
        cluster_name: String,
        description: String | None = None,
        security_group_ids: SecurityGroupIdsList | None = None,
        maintenance_window: String | None = None,
        sns_topic_arn: String | None = None,
        sns_topic_status: String | None = None,
        parameter_group_name: String | None = None,
        snapshot_window: String | None = None,
        snapshot_retention_limit: IntegerOptional | None = None,
        node_type: String | None = None,
        engine: String | None = None,
        engine_version: String | None = None,
        replica_configuration: ReplicaConfigurationRequest | None = None,
        shard_configuration: ShardConfigurationRequest | None = None,
        acl_name: ACLName | None = None,
        ip_discovery: IpDiscovery | None = None,
        **kwargs,
    ) -> UpdateClusterResponse:
        """Modifies the settings for a cluster. You can use this operation to
        change one or more cluster configuration settings by specifying the
        settings and the new values.

        :param cluster_name: The name of the cluster to update.
        :param description: The description of the cluster to update.
        :param security_group_ids: The SecurityGroupIds to update.
        :param maintenance_window: Specifies the weekly time range during which maintenance on the cluster
        is performed.
        :param sns_topic_arn: The SNS topic ARN to update.
        :param sns_topic_status: The status of the Amazon SNS notification topic.
        :param parameter_group_name: The name of the parameter group to update.
        :param snapshot_window: The daily time range (in UTC) during which MemoryDB begins taking a
        daily snapshot of your cluster.
        :param snapshot_retention_limit: The number of days for which MemoryDB retains automatic cluster
        snapshots before deleting them.
        :param node_type: A valid node type that you want to scale this cluster up or down to.
        :param engine: The name of the engine to be used for the cluster.
        :param engine_version: The upgraded version of the engine to be run on the nodes.
        :param replica_configuration: The number of replicas that will reside in each shard.
        :param shard_configuration: The number of shards in the cluster.
        :param acl_name: The Access Control List that is associated with the cluster.
        :param ip_discovery: The mechanism for discovering IP addresses for the cluster discovery
        protocol.
        :returns: UpdateClusterResponse
        :raises ClusterNotFoundFault:
        :raises InvalidClusterStateFault:
        :raises InvalidNodeStateFault:
        :raises ParameterGroupNotFoundFault:
        :raises InvalidVPCNetworkStateFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidKMSKeyFault:
        :raises NodeQuotaForClusterExceededFault:
        :raises ClusterQuotaForCustomerExceededFault:
        :raises ShardsPerClusterQuotaExceededFault:
        :raises NodeQuotaForCustomerExceededFault:
        :raises NoOperationFault:
        :raises InvalidACLStateFault:
        :raises ACLNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("UpdateMultiRegionCluster")
    def update_multi_region_cluster(
        self,
        context: RequestContext,
        multi_region_cluster_name: String,
        node_type: String | None = None,
        description: String | None = None,
        engine_version: String | None = None,
        shard_configuration: ShardConfigurationRequest | None = None,
        multi_region_parameter_group_name: String | None = None,
        update_strategy: UpdateStrategy | None = None,
        **kwargs,
    ) -> UpdateMultiRegionClusterResponse:
        """Updates the configuration of an existing multi-Region cluster.

        :param multi_region_cluster_name: The name of the multi-Region cluster to be updated.
        :param node_type: The new node type to be used for the multi-Region cluster.
        :param description: A new description for the multi-Region cluster.
        :param engine_version: The new engine version to be used for the multi-Region cluster.
        :param shard_configuration: A request to configure the sharding properties of a cluster.
        :param multi_region_parameter_group_name: The new multi-Region parameter group to be associated with the cluster.
        :param update_strategy: The strategy to use for the update operation.
        :returns: UpdateMultiRegionClusterResponse
        :raises MultiRegionClusterNotFoundFault:
        :raises MultiRegionParameterGroupNotFoundFault:
        :raises InvalidMultiRegionClusterStateFault:
        :raises InvalidParameterCombinationException:
        :raises InvalidParameterValueException:
        """
        raise NotImplementedError

    @handler("UpdateParameterGroup")
    def update_parameter_group(
        self,
        context: RequestContext,
        parameter_group_name: String,
        parameter_name_values: ParameterNameValueList,
        **kwargs,
    ) -> UpdateParameterGroupResponse:
        """Updates the parameters of a parameter group. You can modify up to 20
        parameters in a single request by submitting a list parameter name and
        value pairs.

        :param parameter_group_name: The name of the parameter group to update.
        :param parameter_name_values: An array of parameter names and values for the parameter update.
        :returns: UpdateParameterGroupResponse
        :raises ParameterGroupNotFoundFault:
        :raises InvalidParameterGroupStateFault:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError

    @handler("UpdateSubnetGroup")
    def update_subnet_group(
        self,
        context: RequestContext,
        subnet_group_name: String,
        description: String | None = None,
        subnet_ids: SubnetIdentifierList | None = None,
        **kwargs,
    ) -> UpdateSubnetGroupResponse:
        """Updates a subnet group. For more information, see `Updating a subnet
        group <https://docs.aws.amazon.com/MemoryDB/latest/devguide/ubnetGroups.Modifying.html>`__

        :param subnet_group_name: The name of the subnet group.
        :param description: A description of the subnet group.
        :param subnet_ids: The EC2 subnet IDs for the subnet group.
        :returns: UpdateSubnetGroupResponse
        :raises SubnetGroupNotFoundFault:
        :raises SubnetQuotaExceededFault:
        :raises SubnetInUse:
        :raises InvalidSubnet:
        :raises ServiceLinkedRoleNotFoundFault:
        :raises SubnetNotAllowedFault:
        """
        raise NotImplementedError

    @handler("UpdateUser")
    def update_user(
        self,
        context: RequestContext,
        user_name: UserName,
        authentication_mode: AuthenticationMode | None = None,
        access_string: AccessString | None = None,
        **kwargs,
    ) -> UpdateUserResponse:
        """Changes user password(s) and/or access string.

        :param user_name: The name of the user.
        :param authentication_mode: Denotes the user's authentication properties, such as whether it
        requires a password to authenticate.
        :param access_string: Access permissions string used for this user.
        :returns: UpdateUserResponse
        :raises UserNotFoundFault:
        :raises InvalidUserStateFault:
        :raises InvalidParameterValueException:
        :raises InvalidParameterCombinationException:
        """
        raise NotImplementedError
