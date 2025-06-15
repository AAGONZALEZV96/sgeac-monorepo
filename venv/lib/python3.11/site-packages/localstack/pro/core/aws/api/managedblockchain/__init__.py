from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccessorBillingTokenString = str
AccessorListMaxResults = int
ArnString = str
AvailabilityZoneString = str
ClientRequestTokenString = str
DescriptionString = str
Enabled = bool
ExceptionMessage = str
FrameworkVersionString = str
InstanceTypeString = str
IsOwned = bool
MemberListMaxResults = int
NameString = str
NetworkListMaxResults = int
NetworkMemberNameString = str
NodeListMaxResults = int
PaginationToken = str
PasswordString = str
PrincipalString = str
ProposalDurationInt = int
ProposalListMaxResults = int
ResourceIdString = str
String = str
TagKey = str
TagValue = str
ThresholdPercentageInt = int
UsernameString = str
VoteCount = int


class AccessorNetworkType(StrEnum):
    ETHEREUM_GOERLI = "ETHEREUM_GOERLI"
    ETHEREUM_MAINNET = "ETHEREUM_MAINNET"
    ETHEREUM_MAINNET_AND_GOERLI = "ETHEREUM_MAINNET_AND_GOERLI"
    POLYGON_MAINNET = "POLYGON_MAINNET"
    POLYGON_MUMBAI = "POLYGON_MUMBAI"


class AccessorStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    PENDING_DELETION = "PENDING_DELETION"
    DELETED = "DELETED"


class AccessorType(StrEnum):
    BILLING_TOKEN = "BILLING_TOKEN"


class Edition(StrEnum):
    STARTER = "STARTER"
    STANDARD = "STANDARD"


class Framework(StrEnum):
    HYPERLEDGER_FABRIC = "HYPERLEDGER_FABRIC"
    ETHEREUM = "ETHEREUM"


class InvitationStatus(StrEnum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    ACCEPTING = "ACCEPTING"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class MemberStatus(StrEnum):
    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    INACCESSIBLE_ENCRYPTION_KEY = "INACCESSIBLE_ENCRYPTION_KEY"


class NetworkStatus(StrEnum):
    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class NodeStatus(StrEnum):
    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    UNHEALTHY = "UNHEALTHY"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED = "FAILED"
    INACCESSIBLE_ENCRYPTION_KEY = "INACCESSIBLE_ENCRYPTION_KEY"


class ProposalStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    ACTION_FAILED = "ACTION_FAILED"


class StateDBType(StrEnum):
    LevelDB = "LevelDB"
    CouchDB = "CouchDB"


class ThresholdComparator(StrEnum):
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class VoteValue(StrEnum):
    YES = "YES"
    NO = "NO"


class AccessDeniedException(ServiceException):
    """You don't have sufficient access to perform this action."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 403


class IllegalActionException(ServiceException):
    code: str = "IllegalActionException"
    sender_fault: bool = False
    status_code: int = 400


class InternalServiceErrorException(ServiceException):
    """The request processing has failed because of an unknown error, exception
    or failure.
    """

    code: str = "InternalServiceErrorException"
    sender_fault: bool = False
    status_code: int = 500


class InvalidRequestException(ServiceException):
    """The action or operation requested is invalid. Verify that the action is
    typed correctly.
    """

    code: str = "InvalidRequestException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceAlreadyExistsException(ServiceException):
    """A resource request is issued for a resource that already exists."""

    code: str = "ResourceAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 409


class ResourceLimitExceededException(ServiceException):
    """The maximum number of resources of that type already exist. Ensure the
    resources requested are within the boundaries of the service edition and
    your account limits.
    """

    code: str = "ResourceLimitExceededException"
    sender_fault: bool = False
    status_code: int = 429


class ResourceNotFoundException(ServiceException):
    """A requested resource doesn't exist. It may have been deleted or
    referenced incorrectly.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 404
    ResourceName: Optional[ArnString]


class ResourceNotReadyException(ServiceException):
    """The requested resource exists but isn't in a status that can complete
    the operation.
    """

    code: str = "ResourceNotReadyException"
    sender_fault: bool = False
    status_code: int = 409


class ThrottlingException(ServiceException):
    """The request or operation couldn't be performed because a service is
    throttling requests. The most common source of throttling errors is
    creating resources that exceed your service limit for this resource
    type. Request a limit increase or delete unused resources if possible.
    """

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 429


class TooManyTagsException(ServiceException):
    code: str = "TooManyTagsException"
    sender_fault: bool = False
    status_code: int = 400
    ResourceName: Optional[ArnString]


OutputTagMap = Dict[TagKey, TagValue]
Timestamp = datetime


class Accessor(TypedDict, total=False):
    """The properties of the Accessor."""

    Id: Optional[ResourceIdString]
    Type: Optional[AccessorType]
    BillingToken: Optional[AccessorBillingTokenString]
    Status: Optional[AccessorStatus]
    CreationDate: Optional[Timestamp]
    Arn: Optional[ArnString]
    Tags: Optional[OutputTagMap]
    NetworkType: Optional[AccessorNetworkType]


class AccessorSummary(TypedDict, total=False):
    """A summary of accessor properties."""

    Id: Optional[ResourceIdString]
    Type: Optional[AccessorType]
    Status: Optional[AccessorStatus]
    CreationDate: Optional[Timestamp]
    Arn: Optional[ArnString]
    NetworkType: Optional[AccessorNetworkType]


AccessorSummaryList = List[AccessorSummary]


class ApprovalThresholdPolicy(TypedDict, total=False):
    """A policy type that defines the voting rules for the network. The rules
    decide if a proposal is approved. Approval may be based on criteria such
    as the percentage of ``YES`` votes and the duration of the proposal. The
    policy applies to all proposals and is specified when the network is
    created.

    Applies only to Hyperledger Fabric.
    """

    ThresholdPercentage: Optional[ThresholdPercentageInt]
    ProposalDurationInHours: Optional[ProposalDurationInt]
    ThresholdComparator: Optional[ThresholdComparator]


InputTagMap = Dict[TagKey, TagValue]


class CreateAccessorInput(ServiceRequest):
    ClientRequestToken: ClientRequestTokenString
    AccessorType: AccessorType
    Tags: Optional[InputTagMap]
    NetworkType: Optional[AccessorNetworkType]


class CreateAccessorOutput(TypedDict, total=False):
    AccessorId: Optional[ResourceIdString]
    BillingToken: Optional[AccessorBillingTokenString]
    NetworkType: Optional[AccessorNetworkType]


class LogConfiguration(TypedDict, total=False):
    """A configuration for logging events."""

    Enabled: Optional[Enabled]


class LogConfigurations(TypedDict, total=False):
    """A collection of log configurations."""

    Cloudwatch: Optional[LogConfiguration]


class MemberFabricLogPublishingConfiguration(TypedDict, total=False):
    """Configuration properties for logging events associated with a member of
    a Managed Blockchain network using the Hyperledger Fabric framework.
    """

    CaLogs: Optional[LogConfigurations]


class MemberLogPublishingConfiguration(TypedDict, total=False):
    """Configuration properties for logging events associated with a member of
    a Managed Blockchain network.
    """

    Fabric: Optional[MemberFabricLogPublishingConfiguration]


class MemberFabricConfiguration(TypedDict, total=False):
    """Configuration properties for Hyperledger Fabric for a member in a
    Managed Blockchain network that is using the Hyperledger Fabric
    framework.
    """

    AdminUsername: UsernameString
    AdminPassword: PasswordString


class MemberFrameworkConfiguration(TypedDict, total=False):
    """Configuration properties relevant to a member for the blockchain
    framework that the Managed Blockchain network uses.
    """

    Fabric: Optional[MemberFabricConfiguration]


class MemberConfiguration(TypedDict, total=False):
    """Configuration properties of the member.

    Applies only to Hyperledger Fabric.
    """

    Name: NetworkMemberNameString
    Description: Optional[DescriptionString]
    FrameworkConfiguration: MemberFrameworkConfiguration
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration]
    Tags: Optional[InputTagMap]
    KmsKeyArn: Optional[ArnString]


class CreateMemberInput(ServiceRequest):
    ClientRequestToken: ClientRequestTokenString
    InvitationId: ResourceIdString
    NetworkId: ResourceIdString
    MemberConfiguration: MemberConfiguration


class CreateMemberOutput(TypedDict, total=False):
    MemberId: Optional[ResourceIdString]


class VotingPolicy(TypedDict, total=False):
    """The voting rules for the network to decide if a proposal is accepted

    Applies only to Hyperledger Fabric.
    """

    ApprovalThresholdPolicy: Optional[ApprovalThresholdPolicy]


class NetworkFabricConfiguration(TypedDict, total=False):
    """Hyperledger Fabric configuration properties for the network."""

    Edition: Edition


class NetworkFrameworkConfiguration(TypedDict, total=False):
    """Configuration properties relevant to the network for the blockchain
    framework that the network uses.
    """

    Fabric: Optional[NetworkFabricConfiguration]


class CreateNetworkInput(ServiceRequest):
    ClientRequestToken: ClientRequestTokenString
    Name: NameString
    Description: Optional[DescriptionString]
    Framework: Framework
    FrameworkVersion: FrameworkVersionString
    FrameworkConfiguration: Optional[NetworkFrameworkConfiguration]
    VotingPolicy: VotingPolicy
    MemberConfiguration: MemberConfiguration
    Tags: Optional[InputTagMap]


class CreateNetworkOutput(TypedDict, total=False):
    NetworkId: Optional[ResourceIdString]
    MemberId: Optional[ResourceIdString]


class NodeFabricLogPublishingConfiguration(TypedDict, total=False):
    """Configuration properties for logging events associated with a peer node
    owned by a member in a Managed Blockchain network.
    """

    ChaincodeLogs: Optional[LogConfigurations]
    PeerLogs: Optional[LogConfigurations]


class NodeLogPublishingConfiguration(TypedDict, total=False):
    """Configuration properties for logging events associated with a peer node
    on a Hyperledger Fabric network on Managed Blockchain.
    """

    Fabric: Optional[NodeFabricLogPublishingConfiguration]


class NodeConfiguration(TypedDict, total=False):
    """Configuration properties of a node."""

    InstanceType: InstanceTypeString
    AvailabilityZone: Optional[AvailabilityZoneString]
    LogPublishingConfiguration: Optional[NodeLogPublishingConfiguration]
    StateDB: Optional[StateDBType]


class CreateNodeInput(ServiceRequest):
    ClientRequestToken: ClientRequestTokenString
    NetworkId: ResourceIdString
    MemberId: Optional[ResourceIdString]
    NodeConfiguration: NodeConfiguration
    Tags: Optional[InputTagMap]


class CreateNodeOutput(TypedDict, total=False):
    NodeId: Optional[ResourceIdString]


class RemoveAction(TypedDict, total=False):
    """An action to remove a member from a Managed Blockchain network as the
    result of a removal proposal that is ``APPROVED``. The member and all
    associated resources are deleted from the network.

    Applies only to Hyperledger Fabric.
    """

    MemberId: ResourceIdString


RemoveActionList = List[RemoveAction]


class InviteAction(TypedDict, total=False):
    """An action to invite a specific Amazon Web Services account to create a
    member and join the network. The ``InviteAction`` is carried out when a
    ``Proposal`` is ``APPROVED``.

    Applies only to Hyperledger Fabric.
    """

    Principal: PrincipalString


InviteActionList = List[InviteAction]


class ProposalActions(TypedDict, total=False):
    """The actions to carry out if a proposal is ``APPROVED``.

    Applies only to Hyperledger Fabric.
    """

    Invitations: Optional[InviteActionList]
    Removals: Optional[RemoveActionList]


class CreateProposalInput(ServiceRequest):
    ClientRequestToken: ClientRequestTokenString
    NetworkId: ResourceIdString
    MemberId: ResourceIdString
    Actions: ProposalActions
    Description: Optional[DescriptionString]
    Tags: Optional[InputTagMap]


class CreateProposalOutput(TypedDict, total=False):
    ProposalId: Optional[ResourceIdString]


class DeleteAccessorInput(ServiceRequest):
    AccessorId: ResourceIdString


class DeleteAccessorOutput(TypedDict, total=False):
    pass


class DeleteMemberInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: ResourceIdString


class DeleteMemberOutput(TypedDict, total=False):
    pass


class DeleteNodeInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: Optional[ResourceIdString]
    NodeId: ResourceIdString


class DeleteNodeOutput(TypedDict, total=False):
    pass


class GetAccessorInput(ServiceRequest):
    AccessorId: ResourceIdString


class GetAccessorOutput(TypedDict, total=False):
    Accessor: Optional[Accessor]


class GetMemberInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: ResourceIdString


class MemberFabricAttributes(TypedDict, total=False):
    """Attributes of Hyperledger Fabric for a member in a Managed Blockchain
    network using the Hyperledger Fabric framework.
    """

    AdminUsername: Optional[UsernameString]
    CaEndpoint: Optional[String]


class MemberFrameworkAttributes(TypedDict, total=False):
    """Attributes relevant to a member for the blockchain framework that the
    Managed Blockchain network uses.
    """

    Fabric: Optional[MemberFabricAttributes]


class Member(TypedDict, total=False):
    """Member configuration properties.

    Applies only to Hyperledger Fabric.
    """

    NetworkId: Optional[ResourceIdString]
    Id: Optional[ResourceIdString]
    Name: Optional[NetworkMemberNameString]
    Description: Optional[DescriptionString]
    FrameworkAttributes: Optional[MemberFrameworkAttributes]
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration]
    Status: Optional[MemberStatus]
    CreationDate: Optional[Timestamp]
    Tags: Optional[OutputTagMap]
    Arn: Optional[ArnString]
    KmsKeyArn: Optional[String]


class GetMemberOutput(TypedDict, total=False):
    Member: Optional[Member]


class GetNetworkInput(ServiceRequest):
    NetworkId: ResourceIdString


class NetworkEthereumAttributes(TypedDict, total=False):
    """Attributes of Ethereum for a network."""

    ChainId: Optional[String]


class NetworkFabricAttributes(TypedDict, total=False):
    """Attributes of Hyperledger Fabric for a network."""

    OrderingServiceEndpoint: Optional[String]
    Edition: Optional[Edition]


class NetworkFrameworkAttributes(TypedDict, total=False):
    """Attributes relevant to the network for the blockchain framework that the
    network uses.
    """

    Fabric: Optional[NetworkFabricAttributes]
    Ethereum: Optional[NetworkEthereumAttributes]


class Network(TypedDict, total=False):
    """Network configuration properties."""

    Id: Optional[ResourceIdString]
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Framework: Optional[Framework]
    FrameworkVersion: Optional[FrameworkVersionString]
    FrameworkAttributes: Optional[NetworkFrameworkAttributes]
    VpcEndpointServiceName: Optional[String]
    VotingPolicy: Optional[VotingPolicy]
    Status: Optional[NetworkStatus]
    CreationDate: Optional[Timestamp]
    Tags: Optional[OutputTagMap]
    Arn: Optional[ArnString]


class GetNetworkOutput(TypedDict, total=False):
    Network: Optional[Network]


class GetNodeInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: Optional[ResourceIdString]
    NodeId: ResourceIdString


class NodeEthereumAttributes(TypedDict, total=False):
    """Attributes of an Ethereum node."""

    HttpEndpoint: Optional[String]
    WebSocketEndpoint: Optional[String]


class NodeFabricAttributes(TypedDict, total=False):
    """Attributes of Hyperledger Fabric for a peer node on a Hyperledger Fabric
    network on Managed Blockchain.
    """

    PeerEndpoint: Optional[String]
    PeerEventEndpoint: Optional[String]


class NodeFrameworkAttributes(TypedDict, total=False):
    """Attributes relevant to a node on a Managed Blockchain network for the
    blockchain framework that the network uses.
    """

    Fabric: Optional[NodeFabricAttributes]
    Ethereum: Optional[NodeEthereumAttributes]


class Node(TypedDict, total=False):
    """Configuration properties of a node."""

    NetworkId: Optional[ResourceIdString]
    MemberId: Optional[ResourceIdString]
    Id: Optional[ResourceIdString]
    InstanceType: Optional[InstanceTypeString]
    AvailabilityZone: Optional[AvailabilityZoneString]
    FrameworkAttributes: Optional[NodeFrameworkAttributes]
    LogPublishingConfiguration: Optional[NodeLogPublishingConfiguration]
    StateDB: Optional[StateDBType]
    Status: Optional[NodeStatus]
    CreationDate: Optional[Timestamp]
    Tags: Optional[OutputTagMap]
    Arn: Optional[ArnString]
    KmsKeyArn: Optional[String]


class GetNodeOutput(TypedDict, total=False):
    Node: Optional[Node]


class GetProposalInput(ServiceRequest):
    NetworkId: ResourceIdString
    ProposalId: ResourceIdString


class Proposal(TypedDict, total=False):
    """Properties of a proposal on a Managed Blockchain network.

    Applies only to Hyperledger Fabric.
    """

    ProposalId: Optional[ResourceIdString]
    NetworkId: Optional[ResourceIdString]
    Description: Optional[DescriptionString]
    Actions: Optional[ProposalActions]
    ProposedByMemberId: Optional[ResourceIdString]
    ProposedByMemberName: Optional[NetworkMemberNameString]
    Status: Optional[ProposalStatus]
    CreationDate: Optional[Timestamp]
    ExpirationDate: Optional[Timestamp]
    YesVoteCount: Optional[VoteCount]
    NoVoteCount: Optional[VoteCount]
    OutstandingVoteCount: Optional[VoteCount]
    Tags: Optional[OutputTagMap]
    Arn: Optional[ArnString]


class GetProposalOutput(TypedDict, total=False):
    Proposal: Optional[Proposal]


class NetworkSummary(TypedDict, total=False):
    """A summary of network configuration properties."""

    Id: Optional[ResourceIdString]
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Framework: Optional[Framework]
    FrameworkVersion: Optional[FrameworkVersionString]
    Status: Optional[NetworkStatus]
    CreationDate: Optional[Timestamp]
    Arn: Optional[ArnString]


class Invitation(TypedDict, total=False):
    """An invitation to an Amazon Web Services account to create a member and
    join the network.

    Applies only to Hyperledger Fabric.
    """

    InvitationId: Optional[ResourceIdString]
    CreationDate: Optional[Timestamp]
    ExpirationDate: Optional[Timestamp]
    Status: Optional[InvitationStatus]
    NetworkSummary: Optional[NetworkSummary]
    Arn: Optional[ArnString]


InvitationList = List[Invitation]


class ListAccessorsInput(ServiceRequest):
    MaxResults: Optional[AccessorListMaxResults]
    NextToken: Optional[PaginationToken]
    NetworkType: Optional[AccessorNetworkType]


class ListAccessorsOutput(TypedDict, total=False):
    Accessors: Optional[AccessorSummaryList]
    NextToken: Optional[PaginationToken]


class ListInvitationsInput(ServiceRequest):
    MaxResults: Optional[ProposalListMaxResults]
    NextToken: Optional[PaginationToken]


class ListInvitationsOutput(TypedDict, total=False):
    Invitations: Optional[InvitationList]
    NextToken: Optional[PaginationToken]


class ListMembersInput(ServiceRequest):
    NetworkId: ResourceIdString
    Name: Optional[String]
    Status: Optional[MemberStatus]
    IsOwned: Optional[IsOwned]
    MaxResults: Optional[MemberListMaxResults]
    NextToken: Optional[PaginationToken]


class MemberSummary(TypedDict, total=False):
    """A summary of configuration properties for a member.

    Applies only to Hyperledger Fabric.
    """

    Id: Optional[ResourceIdString]
    Name: Optional[NetworkMemberNameString]
    Description: Optional[DescriptionString]
    Status: Optional[MemberStatus]
    CreationDate: Optional[Timestamp]
    IsOwned: Optional[IsOwned]
    Arn: Optional[ArnString]


MemberSummaryList = List[MemberSummary]


class ListMembersOutput(TypedDict, total=False):
    Members: Optional[MemberSummaryList]
    NextToken: Optional[PaginationToken]


class ListNetworksInput(ServiceRequest):
    Name: Optional[String]
    Framework: Optional[Framework]
    Status: Optional[NetworkStatus]
    MaxResults: Optional[NetworkListMaxResults]
    NextToken: Optional[PaginationToken]


NetworkSummaryList = List[NetworkSummary]


class ListNetworksOutput(TypedDict, total=False):
    Networks: Optional[NetworkSummaryList]
    NextToken: Optional[PaginationToken]


class ListNodesInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: Optional[ResourceIdString]
    Status: Optional[NodeStatus]
    MaxResults: Optional[NodeListMaxResults]
    NextToken: Optional[PaginationToken]


class NodeSummary(TypedDict, total=False):
    """A summary of configuration properties for a node."""

    Id: Optional[ResourceIdString]
    Status: Optional[NodeStatus]
    CreationDate: Optional[Timestamp]
    AvailabilityZone: Optional[AvailabilityZoneString]
    InstanceType: Optional[InstanceTypeString]
    Arn: Optional[ArnString]


NodeSummaryList = List[NodeSummary]


class ListNodesOutput(TypedDict, total=False):
    Nodes: Optional[NodeSummaryList]
    NextToken: Optional[PaginationToken]


class ListProposalVotesInput(ServiceRequest):
    NetworkId: ResourceIdString
    ProposalId: ResourceIdString
    MaxResults: Optional[ProposalListMaxResults]
    NextToken: Optional[PaginationToken]


class VoteSummary(TypedDict, total=False):
    """Properties of an individual vote that a member cast for a proposal.

    Applies only to Hyperledger Fabric.
    """

    Vote: Optional[VoteValue]
    MemberName: Optional[NetworkMemberNameString]
    MemberId: Optional[ResourceIdString]


ProposalVoteList = List[VoteSummary]


class ListProposalVotesOutput(TypedDict, total=False):
    ProposalVotes: Optional[ProposalVoteList]
    NextToken: Optional[PaginationToken]


class ListProposalsInput(ServiceRequest):
    NetworkId: ResourceIdString
    MaxResults: Optional[ProposalListMaxResults]
    NextToken: Optional[PaginationToken]


class ProposalSummary(TypedDict, total=False):
    """Properties of a proposal.

    Applies only to Hyperledger Fabric.
    """

    ProposalId: Optional[ResourceIdString]
    Description: Optional[DescriptionString]
    ProposedByMemberId: Optional[ResourceIdString]
    ProposedByMemberName: Optional[NetworkMemberNameString]
    Status: Optional[ProposalStatus]
    CreationDate: Optional[Timestamp]
    ExpirationDate: Optional[Timestamp]
    Arn: Optional[ArnString]


ProposalSummaryList = List[ProposalSummary]


class ListProposalsOutput(TypedDict, total=False):
    Proposals: Optional[ProposalSummaryList]
    NextToken: Optional[PaginationToken]


class ListTagsForResourceRequest(ServiceRequest):
    ResourceArn: ArnString


class ListTagsForResourceResponse(TypedDict, total=False):
    Tags: Optional[OutputTagMap]


class RejectInvitationInput(ServiceRequest):
    InvitationId: ResourceIdString


class RejectInvitationOutput(TypedDict, total=False):
    pass


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    ResourceArn: ArnString
    Tags: InputTagMap


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    ResourceArn: ArnString
    TagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateMemberInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: ResourceIdString
    LogPublishingConfiguration: Optional[MemberLogPublishingConfiguration]


class UpdateMemberOutput(TypedDict, total=False):
    pass


class UpdateNodeInput(ServiceRequest):
    NetworkId: ResourceIdString
    MemberId: Optional[ResourceIdString]
    NodeId: ResourceIdString
    LogPublishingConfiguration: Optional[NodeLogPublishingConfiguration]


class UpdateNodeOutput(TypedDict, total=False):
    pass


class VoteOnProposalInput(ServiceRequest):
    NetworkId: ResourceIdString
    ProposalId: ResourceIdString
    VoterMemberId: ResourceIdString
    Vote: VoteValue


class VoteOnProposalOutput(TypedDict, total=False):
    pass


class ManagedblockchainApi:
    service = "managedblockchain"
    version = "2018-09-24"

    @handler("CreateAccessor")
    def create_accessor(
        self,
        context: RequestContext,
        client_request_token: ClientRequestTokenString,
        accessor_type: AccessorType,
        tags: InputTagMap | None = None,
        network_type: AccessorNetworkType | None = None,
        **kwargs,
    ) -> CreateAccessorOutput:
        """Creates a new accessor for use with Amazon Managed Blockchain service
        that supports token based access. The accessor contains information
        required for token based access.

        :param client_request_token: This is a unique, case-sensitive identifier that you provide to ensure
        the idempotency of the operation.
        :param accessor_type: The type of accessor.
        :param tags: Tags to assign to the Accessor.
        :param network_type: The blockchain network that the ``Accessor`` token is created for.
        :returns: CreateAccessorOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceAlreadyExistsException:
        :raises ThrottlingException:
        :raises ResourceLimitExceededException:
        :raises InternalServiceErrorException:
        :raises TooManyTagsException:
        """
        raise NotImplementedError

    @handler("CreateMember")
    def create_member(
        self,
        context: RequestContext,
        client_request_token: ClientRequestTokenString,
        invitation_id: ResourceIdString,
        network_id: ResourceIdString,
        member_configuration: MemberConfiguration,
        **kwargs,
    ) -> CreateMemberOutput:
        """Creates a member within a Managed Blockchain network.

        Applies only to Hyperledger Fabric.

        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :param invitation_id: The unique identifier of the invitation that is sent to the member to
        join the network.
        :param network_id: The unique identifier of the network in which the member is created.
        :param member_configuration: Member configuration parameters.
        :returns: CreateMemberOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ResourceAlreadyExistsException:
        :raises ResourceNotReadyException:
        :raises ThrottlingException:
        :raises ResourceLimitExceededException:
        :raises InternalServiceErrorException:
        :raises TooManyTagsException:
        """
        raise NotImplementedError

    @handler("CreateNetwork")
    def create_network(
        self,
        context: RequestContext,
        client_request_token: ClientRequestTokenString,
        name: NameString,
        framework: Framework,
        framework_version: FrameworkVersionString,
        voting_policy: VotingPolicy,
        member_configuration: MemberConfiguration,
        description: DescriptionString | None = None,
        framework_configuration: NetworkFrameworkConfiguration | None = None,
        tags: InputTagMap | None = None,
        **kwargs,
    ) -> CreateNetworkOutput:
        """Creates a new blockchain network using Amazon Managed Blockchain.

        Applies only to Hyperledger Fabric.

        :param client_request_token: This is a unique, case-sensitive identifier that you provide to ensure
        the idempotency of the operation.
        :param name: The name of the network.
        :param framework: The blockchain framework that the network uses.
        :param framework_version: The version of the blockchain framework that the network uses.
        :param voting_policy: The voting rules used by the network to determine if a proposal is
        approved.
        :param member_configuration: Configuration properties for the first member within the network.
        :param description: An optional description for the network.
        :param framework_configuration: Configuration properties of the blockchain framework relevant to the
        network configuration.
        :param tags: Tags to assign to the network.
        :returns: CreateNetworkOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceAlreadyExistsException:
        :raises ThrottlingException:
        :raises ResourceLimitExceededException:
        :raises InternalServiceErrorException:
        :raises TooManyTagsException:
        """
        raise NotImplementedError

    @handler("CreateNode")
    def create_node(
        self,
        context: RequestContext,
        client_request_token: ClientRequestTokenString,
        network_id: ResourceIdString,
        node_configuration: NodeConfiguration,
        member_id: ResourceIdString | None = None,
        tags: InputTagMap | None = None,
        **kwargs,
    ) -> CreateNodeOutput:
        """Creates a node on the specified blockchain network.

        Applies to Hyperledger Fabric and Ethereum.

        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :param network_id: The unique identifier of the network for the node.
        :param node_configuration: The properties of a node configuration.
        :param member_id: The unique identifier of the member that owns this node.
        :param tags: Tags to assign to the node.
        :returns: CreateNodeOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ResourceAlreadyExistsException:
        :raises ResourceNotReadyException:
        :raises ThrottlingException:
        :raises ResourceLimitExceededException:
        :raises InternalServiceErrorException:
        :raises TooManyTagsException:
        """
        raise NotImplementedError

    @handler("CreateProposal")
    def create_proposal(
        self,
        context: RequestContext,
        client_request_token: ClientRequestTokenString,
        network_id: ResourceIdString,
        member_id: ResourceIdString,
        actions: ProposalActions,
        description: DescriptionString | None = None,
        tags: InputTagMap | None = None,
        **kwargs,
    ) -> CreateProposalOutput:
        """Creates a proposal for a change to the network that other members of the
        network can vote on, for example, a proposal to add a new member to the
        network. Any member can create a proposal.

        Applies only to Hyperledger Fabric.

        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :param network_id: The unique identifier of the network for which the proposal is made.
        :param member_id: The unique identifier of the member that is creating the proposal.
        :param actions: The type of actions proposed, such as inviting a member or removing a
        member.
        :param description: A description for the proposal that is visible to voting members, for
        example, "Proposal to add Example Corp.
        :param tags: Tags to assign to the proposal.
        :returns: CreateProposalOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ResourceNotReadyException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        :raises TooManyTagsException:
        """
        raise NotImplementedError

    @handler("DeleteAccessor")
    def delete_accessor(
        self, context: RequestContext, accessor_id: ResourceIdString, **kwargs
    ) -> DeleteAccessorOutput:
        """Deletes an accessor that your Amazon Web Services account owns. An
        accessor object is a container that has the information required for
        token based access to your Ethereum nodes including, the
        ``BILLING_TOKEN``. After an accessor is deleted, the status of the
        accessor changes from ``AVAILABLE`` to ``PENDING_DELETION``. An accessor
        in the ``PENDING_DELETION`` state can’t be used for new WebSocket
        requests or HTTP requests. However, WebSocket connections that were
        initiated while the accessor was in the ``AVAILABLE`` state remain open
        until they expire (up to 2 hours).

        :param accessor_id: The unique identifier of the accessor.
        :returns: DeleteAccessorOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("DeleteMember")
    def delete_member(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        member_id: ResourceIdString,
        **kwargs,
    ) -> DeleteMemberOutput:
        """Deletes a member. Deleting a member removes the member and all
        associated resources from the network. ``DeleteMember`` can only be
        called for a specified ``MemberId`` if the principal performing the
        action is associated with the Amazon Web Services account that owns the
        member. In all other cases, the ``DeleteMember`` action is carried out
        as the result of an approved proposal to remove a member. If
        ``MemberId`` is the last member in a network specified by the last
        Amazon Web Services account, the network is deleted also.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network from which the member is removed.
        :param member_id: The unique identifier of the member to remove.
        :returns: DeleteMemberOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ResourceNotReadyException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("DeleteNode")
    def delete_node(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        node_id: ResourceIdString,
        member_id: ResourceIdString | None = None,
        **kwargs,
    ) -> DeleteNodeOutput:
        """Deletes a node that your Amazon Web Services account owns. All data on
        the node is lost and cannot be recovered.

        Applies to Hyperledger Fabric and Ethereum.

        :param network_id: The unique identifier of the network that the node is on.
        :param node_id: The unique identifier of the node.
        :param member_id: The unique identifier of the member that owns this node.
        :returns: DeleteNodeOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ResourceNotReadyException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("GetAccessor")
    def get_accessor(
        self, context: RequestContext, accessor_id: ResourceIdString, **kwargs
    ) -> GetAccessorOutput:
        """Returns detailed information about an accessor. An accessor object is a
        container that has the information required for token based access to
        your Ethereum nodes.

        :param accessor_id: The unique identifier of the accessor.
        :returns: GetAccessorOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("GetMember")
    def get_member(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        member_id: ResourceIdString,
        **kwargs,
    ) -> GetMemberOutput:
        """Returns detailed information about a member.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network to which the member belongs.
        :param member_id: The unique identifier of the member.
        :returns: GetMemberOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("GetNetwork")
    def get_network(
        self, context: RequestContext, network_id: ResourceIdString, **kwargs
    ) -> GetNetworkOutput:
        """Returns detailed information about a network.

        Applies to Hyperledger Fabric and Ethereum.

        :param network_id: The unique identifier of the network to get information about.
        :returns: GetNetworkOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("GetNode")
    def get_node(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        node_id: ResourceIdString,
        member_id: ResourceIdString | None = None,
        **kwargs,
    ) -> GetNodeOutput:
        """Returns detailed information about a node.

        Applies to Hyperledger Fabric and Ethereum.

        :param network_id: The unique identifier of the network that the node is on.
        :param node_id: The unique identifier of the node.
        :param member_id: The unique identifier of the member that owns the node.
        :returns: GetNodeOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("GetProposal")
    def get_proposal(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        proposal_id: ResourceIdString,
        **kwargs,
    ) -> GetProposalOutput:
        """Returns detailed information about a proposal.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network for which the proposal is made.
        :param proposal_id: The unique identifier of the proposal.
        :returns: GetProposalOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListAccessors")
    def list_accessors(
        self,
        context: RequestContext,
        max_results: AccessorListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        network_type: AccessorNetworkType | None = None,
        **kwargs,
    ) -> ListAccessorsOutput:
        """Returns a list of the accessors and their properties. Accessor objects
        are containers that have the information required for token based access
        to your Ethereum nodes.

        :param max_results: The maximum number of accessors to list.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :param network_type: The blockchain network that the ``Accessor`` token is created for.
        :returns: ListAccessorsOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListInvitations")
    def list_invitations(
        self,
        context: RequestContext,
        max_results: ProposalListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListInvitationsOutput:
        """Returns a list of all invitations for the current Amazon Web Services
        account.

        Applies only to Hyperledger Fabric.

        :param max_results: The maximum number of invitations to return.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :returns: ListInvitationsOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ResourceLimitExceededException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListMembers")
    def list_members(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        name: String | None = None,
        status: MemberStatus | None = None,
        is_owned: IsOwned | None = None,
        max_results: MemberListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListMembersOutput:
        """Returns a list of the members in a network and properties of their
        configurations.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network for which to list members.
        :param name: The optional name of the member to list.
        :param status: An optional status specifier.
        :param is_owned: An optional Boolean value.
        :param max_results: The maximum number of members to return in the request.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :returns: ListMembersOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListNetworks")
    def list_networks(
        self,
        context: RequestContext,
        name: String | None = None,
        framework: Framework | None = None,
        status: NetworkStatus | None = None,
        max_results: NetworkListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListNetworksOutput:
        """Returns information about the networks in which the current Amazon Web
        Services account participates.

        Applies to Hyperledger Fabric and Ethereum.

        :param name: The name of the network.
        :param framework: An optional framework specifier.
        :param status: An optional status specifier.
        :param max_results: The maximum number of networks to list.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :returns: ListNetworksOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListNodes")
    def list_nodes(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        member_id: ResourceIdString | None = None,
        status: NodeStatus | None = None,
        max_results: NodeListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListNodesOutput:
        """Returns information about the nodes within a network.

        Applies to Hyperledger Fabric and Ethereum.

        :param network_id: The unique identifier of the network for which to list nodes.
        :param member_id: The unique identifier of the member who owns the nodes to list.
        :param status: An optional status specifier.
        :param max_results: The maximum number of nodes to list.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :returns: ListNodesOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListProposalVotes")
    def list_proposal_votes(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        proposal_id: ResourceIdString,
        max_results: ProposalListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListProposalVotesOutput:
        """Returns the list of votes for a specified proposal, including the value
        of each vote and the unique identifier of the member that cast the vote.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network.
        :param proposal_id: The unique identifier of the proposal.
        :param max_results: The maximum number of votes to return.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :returns: ListProposalVotesOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListProposals")
    def list_proposals(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        max_results: ProposalListMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListProposalsOutput:
        """Returns a list of proposals for the network.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network.
        :param max_results: The maximum number of proposals to return.
        :param next_token: The pagination token that indicates the next set of results to retrieve.
        :returns: ListProposalsOutput
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: ArnString, **kwargs
    ) -> ListTagsForResourceResponse:
        """Returns a list of tags for the specified resource. Each tag consists of
        a key and optional value.

        For more information about tags, see `Tagging
        Resources <https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html>`__
        in the *Amazon Managed Blockchain Ethereum Developer Guide*, or `Tagging
        Resources <https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html>`__
        in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :returns: ListTagsForResourceResponse
        :raises InternalServiceErrorException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ResourceNotReadyException:
        """
        raise NotImplementedError

    @handler("RejectInvitation")
    def reject_invitation(
        self, context: RequestContext, invitation_id: ResourceIdString, **kwargs
    ) -> RejectInvitationOutput:
        """Rejects an invitation to join a network. This action can be called by a
        principal in an Amazon Web Services account that has received an
        invitation to create a member and join a network.

        Applies only to Hyperledger Fabric.

        :param invitation_id: The unique identifier of the invitation to reject.
        :returns: RejectInvitationOutput
        :raises InvalidRequestException:
        :raises IllegalActionException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ArnString, tags: InputTagMap, **kwargs
    ) -> TagResourceResponse:
        """Adds or overwrites the specified tags for the specified Amazon Managed
        Blockchain resource. Each tag consists of a key and optional value.

        When you specify a tag key that already exists, the tag value is
        overwritten with the new value. Use ``UntagResource`` to remove tag
        keys.

        A resource can have up to 50 tags. If you try to create more than 50
        tags for a resource, your request fails and returns an error.

        For more information about tags, see `Tagging
        Resources <https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html>`__
        in the *Amazon Managed Blockchain Ethereum Developer Guide*, or `Tagging
        Resources <https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html>`__
        in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param tags: The tags to assign to the specified resource.
        :returns: TagResourceResponse
        :raises InternalServiceErrorException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises TooManyTagsException:
        :raises ResourceNotReadyException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ArnString, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResponse:
        """Removes the specified tags from the Amazon Managed Blockchain resource.

        For more information about tags, see `Tagging
        Resources <https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html>`__
        in the *Amazon Managed Blockchain Ethereum Developer Guide*, or `Tagging
        Resources <https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html>`__
        in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param tag_keys: The tag keys.
        :returns: UntagResourceResponse
        :raises InternalServiceErrorException:
        :raises InvalidRequestException:
        :raises ResourceNotFoundException:
        :raises ResourceNotReadyException:
        """
        raise NotImplementedError

    @handler("UpdateMember")
    def update_member(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        member_id: ResourceIdString,
        log_publishing_configuration: MemberLogPublishingConfiguration | None = None,
        **kwargs,
    ) -> UpdateMemberOutput:
        """Updates a member configuration with new parameters.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the Managed Blockchain network to which the
        member belongs.
        :param member_id: The unique identifier of the member.
        :param log_publishing_configuration: Configuration properties for publishing to Amazon CloudWatch Logs.
        :returns: UpdateMemberOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("UpdateNode")
    def update_node(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        node_id: ResourceIdString,
        member_id: ResourceIdString | None = None,
        log_publishing_configuration: NodeLogPublishingConfiguration | None = None,
        **kwargs,
    ) -> UpdateNodeOutput:
        """Updates a node configuration with new parameters.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network that the node is on.
        :param node_id: The unique identifier of the node.
        :param member_id: The unique identifier of the member that owns the node.
        :param log_publishing_configuration: Configuration properties for publishing to Amazon CloudWatch Logs.
        :returns: UpdateNodeOutput
        :raises InvalidRequestException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError

    @handler("VoteOnProposal")
    def vote_on_proposal(
        self,
        context: RequestContext,
        network_id: ResourceIdString,
        proposal_id: ResourceIdString,
        voter_member_id: ResourceIdString,
        vote: VoteValue,
        **kwargs,
    ) -> VoteOnProposalOutput:
        """Casts a vote for a specified ``ProposalId`` on behalf of a member. The
        member to vote as, specified by ``VoterMemberId``, must be in the same
        Amazon Web Services account as the principal that calls the action.

        Applies only to Hyperledger Fabric.

        :param network_id: The unique identifier of the network.
        :param proposal_id: The unique identifier of the proposal.
        :param voter_member_id: The unique identifier of the member casting the vote.
        :param vote: The value of the vote.
        :returns: VoteOnProposalOutput
        :raises InvalidRequestException:
        :raises IllegalActionException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServiceErrorException:
        """
        raise NotImplementedError
