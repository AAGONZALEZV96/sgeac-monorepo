from datetime import datetime
from enum import StrEnum
from typing import List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccountId = str
AmazonResourceName = str
BranchName = str
ConnectionArn = str
ConnectionName = str
CreatedReason = str
DeploymentFilePath = str
Directory = str
ErrorMessage = str
Event = str
ExternalId = str
HostArn = str
HostName = str
HostStatus = str
HostStatusMessage = str
IamRoleArn = str
Id = str
KmsKeyArn = str
MaxResults = int
NextToken = str
OwnerId = str
Parent = str
RepositoryLinkArn = str
RepositoryLinkId = str
RepositoryName = str
ResolvedReason = str
ResourceName = str
SHA = str
SecurityGroupId = str
SharpNextToken = str
SubnetId = str
SyncBlockerContextKey = str
SyncBlockerContextValue = str
TagKey = str
TagValue = str
Target = str
TlsCertificate = str
Type = str
Url = str
VpcId = str


class BlockerStatus(StrEnum):
    ACTIVE = "ACTIVE"
    RESOLVED = "RESOLVED"


class BlockerType(StrEnum):
    AUTOMATED = "AUTOMATED"


class ConnectionStatus(StrEnum):
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    ERROR = "ERROR"


class ProviderType(StrEnum):
    Bitbucket = "Bitbucket"
    GitHub = "GitHub"
    GitHubEnterpriseServer = "GitHubEnterpriseServer"
    GitLab = "GitLab"
    GitLabSelfManaged = "GitLabSelfManaged"


class PublishDeploymentStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class PullRequestComment(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RepositorySyncStatus(StrEnum):
    FAILED = "FAILED"
    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    QUEUED = "QUEUED"


class ResourceSyncStatus(StrEnum):
    FAILED = "FAILED"
    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"


class SyncConfigurationType(StrEnum):
    CFN_STACK_SYNC = "CFN_STACK_SYNC"


class TriggerResourceUpdateOn(StrEnum):
    ANY_CHANGE = "ANY_CHANGE"
    FILE_CHANGE = "FILE_CHANGE"


class AccessDeniedException(ServiceException):
    """You do not have sufficient access to perform this action."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentModificationException(ServiceException):
    """Exception thrown as a result of concurrent modification to an
    application. For example, two individuals attempting to edit the same
    application at the same time.
    """

    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 400


class ConditionalCheckFailedException(ServiceException):
    """The conditional check failed. Try again later."""

    code: str = "ConditionalCheckFailedException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """Two conflicting operations have been made on the same resource."""

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class InternalServerException(ServiceException):
    """Received an internal server exception. Try again later."""

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInputException(ServiceException):
    """The input is not valid. Verify that the action is typed correctly."""

    code: str = "InvalidInputException"
    sender_fault: bool = False
    status_code: int = 400


class LimitExceededException(ServiceException):
    """Exceeded the maximum limit for connections."""

    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceAlreadyExistsException(ServiceException):
    """Unable to create resource. Resource already exists."""

    code: str = "ResourceAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """Resource not found. Verify the connection resource ARN and try again."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceUnavailableException(ServiceException):
    """Resource not found. Verify the ARN for the host resource and try again."""

    code: str = "ResourceUnavailableException"
    sender_fault: bool = False
    status_code: int = 400


class RetryLatestCommitFailedException(ServiceException):
    """Retrying the latest commit failed. Try again later."""

    code: str = "RetryLatestCommitFailedException"
    sender_fault: bool = False
    status_code: int = 400


class SyncBlockerDoesNotExistException(ServiceException):
    """Unable to continue. The sync blocker does not exist."""

    code: str = "SyncBlockerDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class SyncConfigurationStillExistsException(ServiceException):
    """Unable to continue. The sync blocker still exists."""

    code: str = "SyncConfigurationStillExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """The request was denied due to request throttling."""

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedOperationException(ServiceException):
    """The operation is not supported. Check the connection status and try
    again.
    """

    code: str = "UnsupportedOperationException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedProviderTypeException(ServiceException):
    """The specified provider type is not supported for connections."""

    code: str = "UnsupportedProviderTypeException"
    sender_fault: bool = False
    status_code: int = 400


class UpdateOutOfSyncException(ServiceException):
    """The update is out of sync. Try syncing again."""

    code: str = "UpdateOutOfSyncException"
    sender_fault: bool = False
    status_code: int = 400


class Connection(TypedDict, total=False):
    """A resource that is used to connect third-party source providers with
    services like CodePipeline.

    Note: A connection created through CloudFormation, the CLI, or the SDK
    is in \\`PENDING\\` status by default. You can make its status
    \\`AVAILABLE\\` by updating the connection in the console.
    """

    ConnectionName: Optional[ConnectionName]
    ConnectionArn: Optional[ConnectionArn]
    ProviderType: Optional[ProviderType]
    OwnerAccountId: Optional[AccountId]
    ConnectionStatus: Optional[ConnectionStatus]
    HostArn: Optional[HostArn]


ConnectionList = List[Connection]


class Tag(TypedDict, total=False):
    """A tag is a key-value pair that is used to manage the resource.

    This tag is available for use by Amazon Web Services services that
    support tags.
    """

    Key: TagKey
    Value: TagValue


TagList = List[Tag]


class CreateConnectionInput(ServiceRequest):
    ProviderType: Optional[ProviderType]
    ConnectionName: ConnectionName
    Tags: Optional[TagList]
    HostArn: Optional[HostArn]


class CreateConnectionOutput(TypedDict, total=False):
    ConnectionArn: ConnectionArn
    Tags: Optional[TagList]


SecurityGroupIds = List[SecurityGroupId]
SubnetIds = List[SubnetId]


class VpcConfiguration(TypedDict, total=False):
    """The VPC configuration provisioned for the host."""

    VpcId: VpcId
    SubnetIds: SubnetIds
    SecurityGroupIds: SecurityGroupIds
    TlsCertificate: Optional[TlsCertificate]


class CreateHostInput(ServiceRequest):
    Name: HostName
    ProviderType: ProviderType
    ProviderEndpoint: Url
    VpcConfiguration: Optional[VpcConfiguration]
    Tags: Optional[TagList]


class CreateHostOutput(TypedDict, total=False):
    HostArn: Optional[HostArn]
    Tags: Optional[TagList]


class CreateRepositoryLinkInput(ServiceRequest):
    ConnectionArn: ConnectionArn
    OwnerId: OwnerId
    RepositoryName: RepositoryName
    EncryptionKeyArn: Optional[KmsKeyArn]
    Tags: Optional[TagList]


class RepositoryLinkInfo(TypedDict, total=False):
    """Information about the repository link resource, such as the repository
    link ARN, the associated connection ARN, encryption key ARN, and owner
    ID.
    """

    ConnectionArn: ConnectionArn
    EncryptionKeyArn: Optional[KmsKeyArn]
    OwnerId: OwnerId
    ProviderType: ProviderType
    RepositoryLinkArn: RepositoryLinkArn
    RepositoryLinkId: RepositoryLinkId
    RepositoryName: RepositoryName


class CreateRepositoryLinkOutput(TypedDict, total=False):
    RepositoryLinkInfo: RepositoryLinkInfo


class CreateSyncConfigurationInput(ServiceRequest):
    Branch: BranchName
    ConfigFile: DeploymentFilePath
    RepositoryLinkId: RepositoryLinkId
    ResourceName: ResourceName
    RoleArn: IamRoleArn
    SyncType: SyncConfigurationType
    PublishDeploymentStatus: Optional[PublishDeploymentStatus]
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOn]
    PullRequestComment: Optional[PullRequestComment]


class SyncConfiguration(TypedDict, total=False):
    """Information, such as repository, branch, provider, and resource names
    for a specific sync configuration.
    """

    Branch: BranchName
    ConfigFile: Optional[DeploymentFilePath]
    OwnerId: OwnerId
    ProviderType: ProviderType
    RepositoryLinkId: RepositoryLinkId
    RepositoryName: RepositoryName
    ResourceName: ResourceName
    RoleArn: IamRoleArn
    SyncType: SyncConfigurationType
    PublishDeploymentStatus: Optional[PublishDeploymentStatus]
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOn]
    PullRequestComment: Optional[PullRequestComment]


class CreateSyncConfigurationOutput(TypedDict, total=False):
    SyncConfiguration: SyncConfiguration


class DeleteConnectionInput(ServiceRequest):
    ConnectionArn: ConnectionArn


class DeleteConnectionOutput(TypedDict, total=False):
    pass


class DeleteHostInput(ServiceRequest):
    HostArn: HostArn


class DeleteHostOutput(TypedDict, total=False):
    pass


class DeleteRepositoryLinkInput(ServiceRequest):
    RepositoryLinkId: RepositoryLinkId


class DeleteRepositoryLinkOutput(TypedDict, total=False):
    pass


class DeleteSyncConfigurationInput(ServiceRequest):
    SyncType: SyncConfigurationType
    ResourceName: ResourceName


class DeleteSyncConfigurationOutput(TypedDict, total=False):
    pass


class GetConnectionInput(ServiceRequest):
    ConnectionArn: ConnectionArn


class GetConnectionOutput(TypedDict, total=False):
    Connection: Optional[Connection]


class GetHostInput(ServiceRequest):
    HostArn: HostArn


class GetHostOutput(TypedDict, total=False):
    Name: Optional[HostName]
    Status: Optional[HostStatus]
    ProviderType: Optional[ProviderType]
    ProviderEndpoint: Optional[Url]
    VpcConfiguration: Optional[VpcConfiguration]


class GetRepositoryLinkInput(ServiceRequest):
    RepositoryLinkId: RepositoryLinkId


class GetRepositoryLinkOutput(TypedDict, total=False):
    RepositoryLinkInfo: RepositoryLinkInfo


class GetRepositorySyncStatusInput(ServiceRequest):
    Branch: BranchName
    RepositoryLinkId: RepositoryLinkId
    SyncType: SyncConfigurationType


Timestamp = datetime


class RepositorySyncEvent(TypedDict, total=False):
    """Information about a repository sync event."""

    Event: Event
    ExternalId: Optional[ExternalId]
    Time: Timestamp
    Type: Type


RepositorySyncEventList = List[RepositorySyncEvent]


class RepositorySyncAttempt(TypedDict, total=False):
    """Information about a repository sync attempt for a repository with a sync
    configuration.
    """

    StartedAt: Timestamp
    Status: RepositorySyncStatus
    Events: RepositorySyncEventList


class GetRepositorySyncStatusOutput(TypedDict, total=False):
    LatestSync: RepositorySyncAttempt


class GetResourceSyncStatusInput(ServiceRequest):
    ResourceName: ResourceName
    SyncType: SyncConfigurationType


class Revision(TypedDict, total=False):
    """Information about the revision for a specific sync event, such as the
    branch, owner ID, and name of the repository.
    """

    Branch: BranchName
    Directory: Directory
    OwnerId: OwnerId
    RepositoryName: RepositoryName
    ProviderType: ProviderType
    Sha: SHA


class ResourceSyncEvent(TypedDict, total=False):
    """Information about a resource sync event for the resource associated with
    a sync configuration.
    """

    Event: Event
    ExternalId: Optional[ExternalId]
    Time: Timestamp
    Type: Type


ResourceSyncEventList = List[ResourceSyncEvent]


class ResourceSyncAttempt(TypedDict, total=False):
    """Information about a resource sync attempt."""

    Events: ResourceSyncEventList
    InitialRevision: Revision
    StartedAt: Timestamp
    Status: ResourceSyncStatus
    TargetRevision: Revision
    Target: Target


class GetResourceSyncStatusOutput(TypedDict, total=False):
    DesiredState: Optional[Revision]
    LatestSuccessfulSync: Optional[ResourceSyncAttempt]
    LatestSync: ResourceSyncAttempt


class GetSyncBlockerSummaryInput(ServiceRequest):
    SyncType: SyncConfigurationType
    ResourceName: ResourceName


class SyncBlockerContext(TypedDict, total=False):
    """The context for a specific sync blocker."""

    Key: SyncBlockerContextKey
    Value: SyncBlockerContextValue


SyncBlockerContextList = List[SyncBlockerContext]


class SyncBlocker(TypedDict, total=False):
    """Information about a blocker for a sync event."""

    Id: Id
    Type: BlockerType
    Status: BlockerStatus
    CreatedReason: CreatedReason
    CreatedAt: Timestamp
    Contexts: Optional[SyncBlockerContextList]
    ResolvedReason: Optional[ResolvedReason]
    ResolvedAt: Optional[Timestamp]


LatestSyncBlockerList = List[SyncBlocker]


class SyncBlockerSummary(TypedDict, total=False):
    """A summary for sync blockers."""

    ResourceName: ResourceName
    ParentResourceName: Optional[ResourceName]
    LatestBlockers: Optional[LatestSyncBlockerList]


class GetSyncBlockerSummaryOutput(TypedDict, total=False):
    SyncBlockerSummary: SyncBlockerSummary


class GetSyncConfigurationInput(ServiceRequest):
    SyncType: SyncConfigurationType
    ResourceName: ResourceName


class GetSyncConfigurationOutput(TypedDict, total=False):
    SyncConfiguration: SyncConfiguration


class Host(TypedDict, total=False):
    """A resource that represents the infrastructure where a third-party
    provider is installed. The host is used when you create connections to
    an installed third-party provider type, such as GitHub Enterprise
    Server. You create one host for all connections to that provider.

    A host created through the CLI or the SDK is in \\`PENDING\\` status by
    default. You can make its status \\`AVAILABLE\\` by setting up the host in
    the console.
    """

    Name: Optional[HostName]
    HostArn: Optional[HostArn]
    ProviderType: Optional[ProviderType]
    ProviderEndpoint: Optional[Url]
    VpcConfiguration: Optional[VpcConfiguration]
    Status: Optional[HostStatus]
    StatusMessage: Optional[HostStatusMessage]


HostList = List[Host]


class ListConnectionsInput(ServiceRequest):
    ProviderTypeFilter: Optional[ProviderType]
    HostArnFilter: Optional[HostArn]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListConnectionsOutput(TypedDict, total=False):
    Connections: Optional[ConnectionList]
    NextToken: Optional[NextToken]


class ListHostsInput(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListHostsOutput(TypedDict, total=False):
    Hosts: Optional[HostList]
    NextToken: Optional[NextToken]


class ListRepositoryLinksInput(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[SharpNextToken]


RepositoryLinkList = List[RepositoryLinkInfo]


class ListRepositoryLinksOutput(TypedDict, total=False):
    RepositoryLinks: RepositoryLinkList
    NextToken: Optional[SharpNextToken]


class ListRepositorySyncDefinitionsInput(ServiceRequest):
    RepositoryLinkId: RepositoryLinkId
    SyncType: SyncConfigurationType


class RepositorySyncDefinition(TypedDict, total=False):
    """The definition for a repository with a sync configuration."""

    Branch: BranchName
    Directory: Directory
    Parent: Parent
    Target: Target


RepositorySyncDefinitionList = List[RepositorySyncDefinition]


class ListRepositorySyncDefinitionsOutput(TypedDict, total=False):
    RepositorySyncDefinitions: RepositorySyncDefinitionList
    NextToken: Optional[SharpNextToken]


class ListSyncConfigurationsInput(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[SharpNextToken]
    RepositoryLinkId: RepositoryLinkId
    SyncType: SyncConfigurationType


SyncConfigurationList = List[SyncConfiguration]


class ListSyncConfigurationsOutput(TypedDict, total=False):
    SyncConfigurations: SyncConfigurationList
    NextToken: Optional[SharpNextToken]


class ListTagsForResourceInput(ServiceRequest):
    ResourceArn: AmazonResourceName


class ListTagsForResourceOutput(TypedDict, total=False):
    Tags: Optional[TagList]


TagKeyList = List[TagKey]


class TagResourceInput(ServiceRequest):
    ResourceArn: AmazonResourceName
    Tags: TagList


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    ResourceArn: AmazonResourceName
    TagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateHostInput(ServiceRequest):
    HostArn: HostArn
    ProviderEndpoint: Optional[Url]
    VpcConfiguration: Optional[VpcConfiguration]


class UpdateHostOutput(TypedDict, total=False):
    pass


class UpdateRepositoryLinkInput(ServiceRequest):
    ConnectionArn: Optional[ConnectionArn]
    EncryptionKeyArn: Optional[KmsKeyArn]
    RepositoryLinkId: RepositoryLinkId


class UpdateRepositoryLinkOutput(TypedDict, total=False):
    RepositoryLinkInfo: RepositoryLinkInfo


class UpdateSyncBlockerInput(ServiceRequest):
    Id: Id
    SyncType: SyncConfigurationType
    ResourceName: ResourceName
    ResolvedReason: ResolvedReason


class UpdateSyncBlockerOutput(TypedDict, total=False):
    ResourceName: ResourceName
    ParentResourceName: Optional[ResourceName]
    SyncBlocker: SyncBlocker


class UpdateSyncConfigurationInput(ServiceRequest):
    Branch: Optional[BranchName]
    ConfigFile: Optional[DeploymentFilePath]
    RepositoryLinkId: Optional[RepositoryLinkId]
    ResourceName: ResourceName
    RoleArn: Optional[IamRoleArn]
    SyncType: SyncConfigurationType
    PublishDeploymentStatus: Optional[PublishDeploymentStatus]
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOn]
    PullRequestComment: Optional[PullRequestComment]


class UpdateSyncConfigurationOutput(TypedDict, total=False):
    SyncConfiguration: SyncConfiguration


class CodeconnectionsApi:
    service = "codeconnections"
    version = "2023-12-01"

    @handler("CreateConnection")
    def create_connection(
        self,
        context: RequestContext,
        connection_name: ConnectionName,
        provider_type: ProviderType | None = None,
        tags: TagList | None = None,
        host_arn: HostArn | None = None,
        **kwargs,
    ) -> CreateConnectionOutput:
        """Creates a connection that can then be given to other Amazon Web Services
        services like CodePipeline so that it can access third-party code
        repositories. The connection is in pending status until the third-party
        connection handshake is completed from the console.

        :param connection_name: The name of the connection to be created.
        :param provider_type: The name of the external provider where your third-party code repository
        is configured.
        :param tags: The key-value pair to use when tagging the resource.
        :param host_arn: The Amazon Resource Name (ARN) of the host associated with the
        connection to be created.
        :returns: CreateConnectionOutput
        :raises LimitExceededException:
        :raises ResourceNotFoundException:
        :raises ResourceUnavailableException:
        """
        raise NotImplementedError

    @handler("CreateHost")
    def create_host(
        self,
        context: RequestContext,
        name: HostName,
        provider_type: ProviderType,
        provider_endpoint: Url,
        vpc_configuration: VpcConfiguration | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateHostOutput:
        """Creates a resource that represents the infrastructure where a
        third-party provider is installed. The host is used when you create
        connections to an installed third-party provider type, such as GitHub
        Enterprise Server. You create one host for all connections to that
        provider.

        A host created through the CLI or the SDK is in \\`PENDING\\` status by
        default. You can make its status \\`AVAILABLE\\` by setting up the host in
        the console.

        :param name: The name of the host to be created.
        :param provider_type: The name of the installed provider to be associated with your
        connection.
        :param provider_endpoint: The endpoint of the infrastructure to be represented by the host after
        it is created.
        :param vpc_configuration: The VPC configuration to be provisioned for the host.
        :param tags: Tags for the host to be created.
        :returns: CreateHostOutput
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateRepositoryLink")
    def create_repository_link(
        self,
        context: RequestContext,
        connection_arn: ConnectionArn,
        owner_id: OwnerId,
        repository_name: RepositoryName,
        encryption_key_arn: KmsKeyArn | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateRepositoryLinkOutput:
        """Creates a link to a specified external Git repository. A repository link
        allows Git sync to monitor and sync changes to files in a specified Git
        repository.

        :param connection_arn: The Amazon Resource Name (ARN) of the connection to be associated with
        the repository link.
        :param owner_id: The owner ID for the repository associated with a specific sync
        configuration, such as the owner ID in GitHub.
        :param repository_name: The name of the repository to be associated with the repository link.
        :param encryption_key_arn: The Amazon Resource Name (ARN) encryption key for the repository to be
        associated with the repository link.
        :param tags: The tags for the repository to be associated with the repository link.
        :returns: CreateRepositoryLinkOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises LimitExceededException:
        :raises ResourceAlreadyExistsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateSyncConfiguration")
    def create_sync_configuration(
        self,
        context: RequestContext,
        branch: BranchName,
        config_file: DeploymentFilePath,
        repository_link_id: RepositoryLinkId,
        resource_name: ResourceName,
        role_arn: IamRoleArn,
        sync_type: SyncConfigurationType,
        publish_deployment_status: PublishDeploymentStatus | None = None,
        trigger_resource_update_on: TriggerResourceUpdateOn | None = None,
        pull_request_comment: PullRequestComment | None = None,
        **kwargs,
    ) -> CreateSyncConfigurationOutput:
        """Creates a sync configuration which allows Amazon Web Services to sync
        content from a Git repository to update a specified Amazon Web Services
        resource. Parameters for the sync configuration are determined by the
        sync type.

        :param branch: The branch in the repository from which changes will be synced.
        :param config_file: The file name of the configuration file that manages syncing between the
        connection and the repository.
        :param repository_link_id: The ID of the repository link created for the connection.
        :param resource_name: The name of the Amazon Web Services resource (for example, a
        CloudFormation stack in the case of CFN_STACK_SYNC) that will be
        synchronized from the linked repository.
        :param role_arn: The ARN of the IAM role that grants permission for Amazon Web Services
        to use Git sync to update a given Amazon Web Services resource on your
        behalf.
        :param sync_type: The type of sync configuration.
        :param publish_deployment_status: Whether to enable or disable publishing of deployment status to source
        providers.
        :param trigger_resource_update_on: When to trigger Git sync to begin the stack update.
        :param pull_request_comment: A toggle that specifies whether to enable or disable pull request
        comments for the sync configuration to be created.
        :returns: CreateSyncConfigurationOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises LimitExceededException:
        :raises ResourceAlreadyExistsException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteConnection")
    def delete_connection(
        self, context: RequestContext, connection_arn: ConnectionArn, **kwargs
    ) -> DeleteConnectionOutput:
        """The connection to be deleted.

        :param connection_arn: The Amazon Resource Name (ARN) of the connection to be deleted.
        :returns: DeleteConnectionOutput
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteHost")
    def delete_host(self, context: RequestContext, host_arn: HostArn, **kwargs) -> DeleteHostOutput:
        """The host to be deleted. Before you delete a host, all connections
        associated to the host must be deleted.

        A host cannot be deleted if it is in the VPC_CONFIG_INITIALIZING or
        VPC_CONFIG_DELETING state.

        :param host_arn: The Amazon Resource Name (ARN) of the host to be deleted.
        :returns: DeleteHostOutput
        :raises ResourceNotFoundException:
        :raises ResourceUnavailableException:
        """
        raise NotImplementedError

    @handler("DeleteRepositoryLink")
    def delete_repository_link(
        self, context: RequestContext, repository_link_id: RepositoryLinkId, **kwargs
    ) -> DeleteRepositoryLinkOutput:
        """Deletes the association between your connection and a specified external
        Git repository.

        :param repository_link_id: The ID of the repository link to be deleted.
        :returns: DeleteRepositoryLinkOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises SyncConfigurationStillExistsException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises UnsupportedProviderTypeException:
        """
        raise NotImplementedError

    @handler("DeleteSyncConfiguration")
    def delete_sync_configuration(
        self,
        context: RequestContext,
        sync_type: SyncConfigurationType,
        resource_name: ResourceName,
        **kwargs,
    ) -> DeleteSyncConfigurationOutput:
        """Deletes the sync configuration for a specified repository and
        connection.

        :param sync_type: The type of sync configuration to be deleted.
        :param resource_name: The name of the Amazon Web Services resource associated with the sync
        configuration to be deleted.
        :returns: DeleteSyncConfigurationOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises LimitExceededException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetConnection")
    def get_connection(
        self, context: RequestContext, connection_arn: ConnectionArn, **kwargs
    ) -> GetConnectionOutput:
        """Returns the connection ARN and details such as status, owner, and
        provider type.

        :param connection_arn: The Amazon Resource Name (ARN) of a connection.
        :returns: GetConnectionOutput
        :raises ResourceNotFoundException:
        :raises ResourceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetHost")
    def get_host(self, context: RequestContext, host_arn: HostArn, **kwargs) -> GetHostOutput:
        """Returns the host ARN and details such as status, provider type,
        endpoint, and, if applicable, the VPC configuration.

        :param host_arn: The Amazon Resource Name (ARN) of the requested host.
        :returns: GetHostOutput
        :raises ResourceNotFoundException:
        :raises ResourceUnavailableException:
        """
        raise NotImplementedError

    @handler("GetRepositoryLink")
    def get_repository_link(
        self, context: RequestContext, repository_link_id: RepositoryLinkId, **kwargs
    ) -> GetRepositoryLinkOutput:
        """Returns details about a repository link. A repository link allows Git
        sync to monitor and sync changes from files in a specified Git
        repository.

        :param repository_link_id: The ID of the repository link to get.
        :returns: GetRepositoryLinkOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetRepositorySyncStatus")
    def get_repository_sync_status(
        self,
        context: RequestContext,
        branch: BranchName,
        repository_link_id: RepositoryLinkId,
        sync_type: SyncConfigurationType,
        **kwargs,
    ) -> GetRepositorySyncStatusOutput:
        """Returns details about the sync status for a repository. A repository
        sync uses Git sync to push and pull changes from your remote repository.

        :param branch: The branch of the repository link for the requested repository sync
        status.
        :param repository_link_id: The repository link ID for the requested repository sync status.
        :param sync_type: The sync type of the requested sync status.
        :returns: GetRepositorySyncStatusOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetResourceSyncStatus")
    def get_resource_sync_status(
        self,
        context: RequestContext,
        resource_name: ResourceName,
        sync_type: SyncConfigurationType,
        **kwargs,
    ) -> GetResourceSyncStatusOutput:
        """Returns the status of the sync with the Git repository for a specific
        Amazon Web Services resource.

        :param resource_name: The name of the Amazon Web Services resource for the sync status with
        the Git repository.
        :param sync_type: The sync type for the sync status with the Git repository.
        :returns: GetResourceSyncStatusOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetSyncBlockerSummary")
    def get_sync_blocker_summary(
        self,
        context: RequestContext,
        sync_type: SyncConfigurationType,
        resource_name: ResourceName,
        **kwargs,
    ) -> GetSyncBlockerSummaryOutput:
        """Returns a list of the most recent sync blockers.

        :param sync_type: The sync type for the sync blocker summary.
        :param resource_name: The name of the Amazon Web Services resource currently blocked from
        automatically being synced from a Git repository.
        :returns: GetSyncBlockerSummaryOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetSyncConfiguration")
    def get_sync_configuration(
        self,
        context: RequestContext,
        sync_type: SyncConfigurationType,
        resource_name: ResourceName,
        **kwargs,
    ) -> GetSyncConfigurationOutput:
        """Returns details about a sync configuration, including the sync type and
        resource name. A sync configuration allows the configuration to sync
        (push and pull) changes from the remote repository for a specified
        branch in a Git repository.

        :param sync_type: The sync type for the sync configuration for which you want to retrieve
        information.
        :param resource_name: The name of the Amazon Web Services resource for the sync configuration
        for which you want to retrieve information.
        :returns: GetSyncConfigurationOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListConnections")
    def list_connections(
        self,
        context: RequestContext,
        provider_type_filter: ProviderType | None = None,
        host_arn_filter: HostArn | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListConnectionsOutput:
        """Lists the connections associated with your account.

        :param provider_type_filter: Filters the list of connections to those associated with a specified
        provider, such as Bitbucket.
        :param host_arn_filter: Filters the list of connections to those associated with a specified
        host.
        :param max_results: The maximum number of results to return in a single call.
        :param next_token: The token that was returned from the previous ``ListConnections`` call,
        which can be used to return the next set of connections in the list.
        :returns: ListConnectionsOutput
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListHosts")
    def list_hosts(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListHostsOutput:
        """Lists the hosts associated with your account.

        :param max_results: The maximum number of results to return in a single call.
        :param next_token: The token that was returned from the previous ``ListHosts`` call, which
        can be used to return the next set of hosts in the list.
        :returns: ListHostsOutput
        """
        raise NotImplementedError

    @handler("ListRepositoryLinks")
    def list_repository_links(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: SharpNextToken | None = None,
        **kwargs,
    ) -> ListRepositoryLinksOutput:
        """Lists the repository links created for connections in your account.

        :param max_results: A non-zero, non-negative integer used to limit the number of returned
        results.
        :param next_token: An enumeration token that, when provided in a request, returns the next
        batch of the results.
        :returns: ListRepositoryLinksOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListRepositorySyncDefinitions")
    def list_repository_sync_definitions(
        self,
        context: RequestContext,
        repository_link_id: RepositoryLinkId,
        sync_type: SyncConfigurationType,
        **kwargs,
    ) -> ListRepositorySyncDefinitionsOutput:
        """Lists the repository sync definitions for repository links in your
        account.

        :param repository_link_id: The ID of the repository link for the sync definition for which you want
        to retrieve information.
        :param sync_type: The sync type of the repository link for the the sync definition for
        which you want to retrieve information.
        :returns: ListRepositorySyncDefinitionsOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListSyncConfigurations")
    def list_sync_configurations(
        self,
        context: RequestContext,
        repository_link_id: RepositoryLinkId,
        sync_type: SyncConfigurationType,
        max_results: MaxResults | None = None,
        next_token: SharpNextToken | None = None,
        **kwargs,
    ) -> ListSyncConfigurationsOutput:
        """Returns a list of sync configurations for a specified repository.

        :param repository_link_id: The ID of the repository link for the requested list of sync
        configurations.
        :param sync_type: The sync type for the requested list of sync configurations.
        :param max_results: A non-zero, non-negative integer used to limit the number of returned
        results.
        :param next_token: An enumeration token that allows the operation to batch the results of
        the operation.
        :returns: ListSyncConfigurationsOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, **kwargs
    ) -> ListTagsForResourceOutput:
        """Gets the set of key-value pairs (metadata) that are used to manage the
        resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource for which you want to get
        information about tags, if any.
        :returns: ListTagsForResourceOutput
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, tags: TagList, **kwargs
    ) -> TagResourceOutput:
        """Adds to or modifies the tags of the given resource. Tags are metadata
        that can be used to manage a resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to which you want to add
        or update tags.
        :param tags: The tags you want to modify or add to the resource.
        :returns: TagResourceOutput
        :raises ResourceNotFoundException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: AmazonResourceName,
        tag_keys: TagKeyList,
        **kwargs,
    ) -> UntagResourceOutput:
        """Removes tags from an Amazon Web Services resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to remove tags from.
        :param tag_keys: The list of keys for the tags to be removed from the resource.
        :returns: UntagResourceOutput
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateHost")
    def update_host(
        self,
        context: RequestContext,
        host_arn: HostArn,
        provider_endpoint: Url | None = None,
        vpc_configuration: VpcConfiguration | None = None,
        **kwargs,
    ) -> UpdateHostOutput:
        """Updates a specified host with the provided configurations.

        :param host_arn: The Amazon Resource Name (ARN) of the host to be updated.
        :param provider_endpoint: The URL or endpoint of the host to be updated.
        :param vpc_configuration: The VPC configuration of the host to be updated.
        :returns: UpdateHostOutput
        :raises ConflictException:
        :raises ResourceNotFoundException:
        :raises ResourceUnavailableException:
        :raises UnsupportedOperationException:
        """
        raise NotImplementedError

    @handler("UpdateRepositoryLink")
    def update_repository_link(
        self,
        context: RequestContext,
        repository_link_id: RepositoryLinkId,
        connection_arn: ConnectionArn | None = None,
        encryption_key_arn: KmsKeyArn | None = None,
        **kwargs,
    ) -> UpdateRepositoryLinkOutput:
        """Updates the association between your connection and a specified external
        Git repository. A repository link allows Git sync to monitor and sync
        changes to files in a specified Git repository.

        :param repository_link_id: The ID of the repository link to be updated.
        :param connection_arn: The Amazon Resource Name (ARN) of the connection for the repository link
        to be updated.
        :param encryption_key_arn: The Amazon Resource Name (ARN) of the encryption key for the repository
        link to be updated.
        :returns: UpdateRepositoryLinkOutput
        :raises AccessDeniedException:
        :raises ConditionalCheckFailedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises UpdateOutOfSyncException:
        """
        raise NotImplementedError

    @handler("UpdateSyncBlocker")
    def update_sync_blocker(
        self,
        context: RequestContext,
        id: Id,
        sync_type: SyncConfigurationType,
        resource_name: ResourceName,
        resolved_reason: ResolvedReason,
        **kwargs,
    ) -> UpdateSyncBlockerOutput:
        """Allows you to update the status of a sync blocker, resolving the blocker
        and allowing syncing to continue.

        :param id: The ID of the sync blocker to be updated.
        :param sync_type: The sync type of the sync blocker to be updated.
        :param resource_name: The name of the resource for the sync blocker to be updated.
        :param resolved_reason: The reason for resolving the sync blocker.
        :returns: UpdateSyncBlockerOutput
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises RetryLatestCommitFailedException:
        :raises SyncBlockerDoesNotExistException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("UpdateSyncConfiguration")
    def update_sync_configuration(
        self,
        context: RequestContext,
        resource_name: ResourceName,
        sync_type: SyncConfigurationType,
        branch: BranchName | None = None,
        config_file: DeploymentFilePath | None = None,
        repository_link_id: RepositoryLinkId | None = None,
        role_arn: IamRoleArn | None = None,
        publish_deployment_status: PublishDeploymentStatus | None = None,
        trigger_resource_update_on: TriggerResourceUpdateOn | None = None,
        pull_request_comment: PullRequestComment | None = None,
        **kwargs,
    ) -> UpdateSyncConfigurationOutput:
        """Updates the sync configuration for your connection and a specified
        external Git repository.

        :param resource_name: The name of the Amazon Web Services resource for the sync configuration
        to be updated.
        :param sync_type: The sync type for the sync configuration to be updated.
        :param branch: The branch for the sync configuration to be updated.
        :param config_file: The configuration file for the sync configuration to be updated.
        :param repository_link_id: The ID of the repository link for the sync configuration to be updated.
        :param role_arn: The ARN of the IAM role for the sync configuration to be updated.
        :param publish_deployment_status: Whether to enable or disable publishing of deployment status to source
        providers.
        :param trigger_resource_update_on: When to trigger Git sync to begin the stack update.
        :param pull_request_comment: TA toggle that specifies whether to enable or disable pull request
        comments for the sync configuration to be updated.
        :returns: UpdateSyncConfigurationOutput
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        :raises InternalServerException:
        :raises InvalidInputException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises UpdateOutOfSyncException:
        """
        raise NotImplementedError
