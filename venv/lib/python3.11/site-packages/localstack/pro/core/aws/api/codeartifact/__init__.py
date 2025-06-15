from datetime import datetime
from enum import StrEnum
from typing import IO, Dict, Iterable, List, Optional, TypedDict, Union

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccountId = str
Arn = str
AssetName = str
BooleanOptional = bool
Description = str
DomainName = str
ErrorMessage = str
ExternalConnectionName = str
HashValue = str
Integer = int
ListAllowedRepositoriesForGroupMaxResults = int
ListDomainsMaxResults = int
ListPackageGroupsMaxResults = int
ListPackageVersionAssetsMaxResults = int
ListPackageVersionsMaxResults = int
ListPackagesMaxResults = int
ListRepositoriesInDomainMaxResults = int
ListRepositoriesMaxResults = int
PackageGroupContactInfo = str
PackageGroupPattern = str
PackageGroupPatternPrefix = str
PackageName = str
PackageNamespace = str
PackageVersion = str
PackageVersionRevision = str
PaginationToken = str
PolicyDocument = str
PolicyRevision = str
RepositoryName = str
RetryAfterSeconds = int
SHA256 = str
String = str
String255 = str
TagKey = str
TagValue = str


class AllowPublish(StrEnum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"


class AllowUpstream(StrEnum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"


class DomainStatus(StrEnum):
    Active = "Active"
    Deleted = "Deleted"


class EndpointType(StrEnum):
    dualstack = "dualstack"
    ipv4 = "ipv4"


class ExternalConnectionStatus(StrEnum):
    Available = "Available"


class HashAlgorithm(StrEnum):
    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"


class PackageFormat(StrEnum):
    npm = "npm"
    pypi = "pypi"
    maven = "maven"
    nuget = "nuget"
    generic = "generic"
    ruby = "ruby"
    swift = "swift"
    cargo = "cargo"


class PackageGroupAllowedRepositoryUpdateType(StrEnum):
    ADDED = "ADDED"
    REMOVED = "REMOVED"


class PackageGroupAssociationType(StrEnum):
    STRONG = "STRONG"
    WEAK = "WEAK"


class PackageGroupOriginRestrictionMode(StrEnum):
    ALLOW = "ALLOW"
    ALLOW_SPECIFIC_REPOSITORIES = "ALLOW_SPECIFIC_REPOSITORIES"
    BLOCK = "BLOCK"
    INHERIT = "INHERIT"


class PackageGroupOriginRestrictionType(StrEnum):
    EXTERNAL_UPSTREAM = "EXTERNAL_UPSTREAM"
    INTERNAL_UPSTREAM = "INTERNAL_UPSTREAM"
    PUBLISH = "PUBLISH"


class PackageVersionErrorCode(StrEnum):
    ALREADY_EXISTS = "ALREADY_EXISTS"
    MISMATCHED_REVISION = "MISMATCHED_REVISION"
    MISMATCHED_STATUS = "MISMATCHED_STATUS"
    NOT_ALLOWED = "NOT_ALLOWED"
    NOT_FOUND = "NOT_FOUND"
    SKIPPED = "SKIPPED"


class PackageVersionOriginType(StrEnum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    UNKNOWN = "UNKNOWN"


class PackageVersionSortType(StrEnum):
    PUBLISHED_TIME = "PUBLISHED_TIME"


class PackageVersionStatus(StrEnum):
    Published = "Published"
    Unfinished = "Unfinished"
    Unlisted = "Unlisted"
    Archived = "Archived"
    Disposed = "Disposed"
    Deleted = "Deleted"


class ResourceType(StrEnum):
    domain = "domain"
    repository = "repository"
    package = "package"
    package_version = "package-version"
    asset = "asset"


class ValidationExceptionReason(StrEnum):
    CANNOT_PARSE = "CANNOT_PARSE"
    ENCRYPTION_KEY_ERROR = "ENCRYPTION_KEY_ERROR"
    FIELD_VALIDATION_FAILED = "FIELD_VALIDATION_FAILED"
    UNKNOWN_OPERATION = "UNKNOWN_OPERATION"
    OTHER = "OTHER"


class AccessDeniedException(ServiceException):
    """The operation did not succeed because of an unauthorized access attempt."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 403


class ConflictException(ServiceException):
    """The operation did not succeed because prerequisites are not met."""

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 409
    resourceId: Optional[String]
    resourceType: Optional[ResourceType]


class InternalServerException(ServiceException):
    """The operation did not succeed because of an error that occurred inside
    CodeArtifact.
    """

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500


class ResourceNotFoundException(ServiceException):
    """The operation did not succeed because the resource requested is not
    found in the service.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 404
    resourceId: Optional[String]
    resourceType: Optional[ResourceType]


class ServiceQuotaExceededException(ServiceException):
    """The operation did not succeed because it would have exceeded a service
    limit for your account.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 402
    resourceId: Optional[String]
    resourceType: Optional[ResourceType]


class ThrottlingException(ServiceException):
    """The operation did not succeed because too many requests are sent to the
    service.
    """

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 429
    retryAfterSeconds: Optional[RetryAfterSeconds]


class ValidationException(ServiceException):
    """The operation did not succeed because a parameter in the request was
    sent with an invalid value.
    """

    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400
    reason: Optional[ValidationExceptionReason]


Asset = bytes
AssetHashes = Dict[HashAlgorithm, HashValue]
LongOptional = int


class AssetSummary(TypedDict, total=False):
    """Contains details about a package version asset."""

    name: AssetName
    size: Optional[LongOptional]
    hashes: Optional[AssetHashes]


AssetSummaryList = List[AssetSummary]


class AssociateExternalConnectionRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    externalConnection: ExternalConnectionName


Timestamp = datetime


class RepositoryExternalConnectionInfo(TypedDict, total=False):
    """Contains information about the external connection of a repository."""

    externalConnectionName: Optional[ExternalConnectionName]
    packageFormat: Optional[PackageFormat]
    status: Optional[ExternalConnectionStatus]


RepositoryExternalConnectionInfoList = List[RepositoryExternalConnectionInfo]


class UpstreamRepositoryInfo(TypedDict, total=False):
    """Information about an upstream repository."""

    repositoryName: Optional[RepositoryName]


UpstreamRepositoryInfoList = List[UpstreamRepositoryInfo]


class RepositoryDescription(TypedDict, total=False):
    """The details of a repository stored in CodeArtifact. A CodeArtifact
    repository contains a set of package versions, each of which maps to a
    set of assets. Repositories are polyglot—a single repository can contain
    packages of any supported type. Each repository exposes endpoints for
    fetching and publishing packages using tools like the ``npm`` CLI, the
    Maven CLI (``mvn``), and ``pip``. You can create up to 100 repositories
    per Amazon Web Services account.
    """

    name: Optional[RepositoryName]
    administratorAccount: Optional[AccountId]
    domainName: Optional[DomainName]
    domainOwner: Optional[AccountId]
    arn: Optional[Arn]
    description: Optional[Description]
    upstreams: Optional[UpstreamRepositoryInfoList]
    externalConnections: Optional[RepositoryExternalConnectionInfoList]
    createdTime: Optional[Timestamp]


class AssociateExternalConnectionResult(TypedDict, total=False):
    repository: Optional[RepositoryDescription]


class AssociatedPackage(TypedDict, total=False):
    """A package associated with a package group."""

    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    associationType: Optional[PackageGroupAssociationType]


AssociatedPackageList = List[AssociatedPackage]
AuthorizationTokenDurationSeconds = int
PackageVersionRevisionMap = Dict[PackageVersion, PackageVersionRevision]
PackageVersionList = List[PackageVersion]


class CopyPackageVersionsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    sourceRepository: RepositoryName
    destinationRepository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    versions: Optional[PackageVersionList]
    versionRevisions: Optional[PackageVersionRevisionMap]
    allowOverwrite: Optional[BooleanOptional]
    includeFromUpstream: Optional[BooleanOptional]


class PackageVersionError(TypedDict, total=False):
    """l An error associated with package."""

    errorCode: Optional[PackageVersionErrorCode]
    errorMessage: Optional[ErrorMessage]


PackageVersionErrorMap = Dict[PackageVersion, PackageVersionError]


class SuccessfulPackageVersionInfo(TypedDict, total=False):
    """Contains the revision and status of a package version."""

    revision: Optional[String]
    status: Optional[PackageVersionStatus]


SuccessfulPackageVersionInfoMap = Dict[PackageVersion, SuccessfulPackageVersionInfo]


class CopyPackageVersionsResult(TypedDict, total=False):
    successfulVersions: Optional[SuccessfulPackageVersionInfoMap]
    failedVersions: Optional[PackageVersionErrorMap]


class Tag(TypedDict, total=False):
    """A tag is a key-value pair that can be used to manage, search for, or
    filter resources in CodeArtifact.
    """

    key: TagKey
    value: TagValue


TagList = List[Tag]


class CreateDomainRequest(ServiceRequest):
    domain: DomainName
    encryptionKey: Optional[Arn]
    tags: Optional[TagList]


Long = int


class DomainDescription(TypedDict, total=False):
    """Information about a domain. A domain is a container for repositories.
    When you create a domain, it is empty until you add one or more
    repositories.
    """

    name: Optional[DomainName]
    owner: Optional[AccountId]
    arn: Optional[Arn]
    status: Optional[DomainStatus]
    createdTime: Optional[Timestamp]
    encryptionKey: Optional[Arn]
    repositoryCount: Optional[Integer]
    assetSizeBytes: Optional[Long]
    s3BucketArn: Optional[Arn]


class CreateDomainResult(TypedDict, total=False):
    domain: Optional[DomainDescription]


class CreatePackageGroupRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern
    contactInfo: Optional[PackageGroupContactInfo]
    description: Optional[Description]
    tags: Optional[TagList]


class PackageGroupReference(TypedDict, total=False):
    """Information about the identifiers of a package group."""

    arn: Optional[Arn]
    pattern: Optional[PackageGroupPattern]


class PackageGroupOriginRestriction(TypedDict, total=False):
    """Contains information about the configured restrictions of the origin
    controls of a package group.
    """

    mode: Optional[PackageGroupOriginRestrictionMode]
    effectiveMode: Optional[PackageGroupOriginRestrictionMode]
    inheritedFrom: Optional[PackageGroupReference]
    repositoriesCount: Optional[LongOptional]


PackageGroupOriginRestrictions = Dict[
    PackageGroupOriginRestrictionType, PackageGroupOriginRestriction
]


class PackageGroupOriginConfiguration(TypedDict, total=False):
    """The package group origin configuration that determines how package
    versions can enter repositories.
    """

    restrictions: Optional[PackageGroupOriginRestrictions]


class PackageGroupDescription(TypedDict, total=False):
    """The description of the package group."""

    arn: Optional[Arn]
    pattern: Optional[PackageGroupPattern]
    domainName: Optional[DomainName]
    domainOwner: Optional[AccountId]
    createdTime: Optional[Timestamp]
    contactInfo: Optional[PackageGroupContactInfo]
    description: Optional[Description]
    originConfiguration: Optional[PackageGroupOriginConfiguration]
    parent: Optional[PackageGroupReference]


class CreatePackageGroupResult(TypedDict, total=False):
    packageGroup: Optional[PackageGroupDescription]


class UpstreamRepository(TypedDict, total=False):
    """Information about an upstream repository. A list of
    ``UpstreamRepository`` objects is an input parameter to
    `CreateRepository <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html>`__
    and
    `UpdateRepository <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateRepository.html>`__.
    """

    repositoryName: RepositoryName


UpstreamRepositoryList = List[UpstreamRepository]


class CreateRepositoryRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    description: Optional[Description]
    upstreams: Optional[UpstreamRepositoryList]
    tags: Optional[TagList]


class CreateRepositoryResult(TypedDict, total=False):
    repository: Optional[RepositoryDescription]


class DeleteDomainPermissionsPolicyRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    policyRevision: Optional[PolicyRevision]


class ResourcePolicy(TypedDict, total=False):
    """An CodeArtifact resource policy that contains a resource ARN, document
    details, and a revision.
    """

    resourceArn: Optional[Arn]
    revision: Optional[PolicyRevision]
    document: Optional[PolicyDocument]


class DeleteDomainPermissionsPolicyResult(TypedDict, total=False):
    policy: Optional[ResourcePolicy]


class DeleteDomainRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]


class DeleteDomainResult(TypedDict, total=False):
    domain: Optional[DomainDescription]


class DeletePackageGroupRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: String


class DeletePackageGroupResult(TypedDict, total=False):
    packageGroup: Optional[PackageGroupDescription]


class DeletePackageRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName


class PackageOriginRestrictions(TypedDict, total=False):
    """Details about the origin restrictions set on the package. The package
    origin restrictions determine how new versions of a package can be added
    to a specific repository.
    """

    publish: AllowPublish
    upstream: AllowUpstream


class PackageOriginConfiguration(TypedDict, total=False):
    """Details about the package origin configuration of a package."""

    restrictions: Optional[PackageOriginRestrictions]


class PackageSummary(TypedDict, total=False):
    """Details about a package, including its format, namespace, and name."""

    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    originConfiguration: Optional[PackageOriginConfiguration]


class DeletePackageResult(TypedDict, total=False):
    deletedPackage: Optional[PackageSummary]


class DeletePackageVersionsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    versions: PackageVersionList
    expectedStatus: Optional[PackageVersionStatus]


class DeletePackageVersionsResult(TypedDict, total=False):
    successfulVersions: Optional[SuccessfulPackageVersionInfoMap]
    failedVersions: Optional[PackageVersionErrorMap]


class DeleteRepositoryPermissionsPolicyRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    policyRevision: Optional[PolicyRevision]


class DeleteRepositoryPermissionsPolicyResult(TypedDict, total=False):
    policy: Optional[ResourcePolicy]


class DeleteRepositoryRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName


class DeleteRepositoryResult(TypedDict, total=False):
    repository: Optional[RepositoryDescription]


class DescribeDomainRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]


class DescribeDomainResult(TypedDict, total=False):
    domain: Optional[DomainDescription]


class DescribePackageGroupRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern


class DescribePackageGroupResult(TypedDict, total=False):
    packageGroup: Optional[PackageGroupDescription]


class DescribePackageRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName


class PackageDescription(TypedDict, total=False):
    """Details about a package."""

    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    name: Optional[PackageName]
    originConfiguration: Optional[PackageOriginConfiguration]


class DescribePackageResult(TypedDict, total=False):
    package: PackageDescription


class DescribePackageVersionRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    packageVersion: PackageVersion


class DomainEntryPoint(TypedDict, total=False):
    """Information about how a package originally entered the CodeArtifact
    domain. For packages published directly to CodeArtifact, the entry point
    is the repository it was published to. For packages ingested from an
    external repository, the entry point is the external connection that it
    was ingested from. An external connection is a CodeArtifact repository
    that is connected to an external repository such as the npm registry or
    NuGet gallery.

    If a package version exists in a repository and is updated, for example
    if a package of the same version is added with additional assets, the
    package version's ``DomainEntryPoint`` will not change from the original
    package version's value.
    """

    repositoryName: Optional[RepositoryName]
    externalConnectionName: Optional[ExternalConnectionName]


class PackageVersionOrigin(TypedDict, total=False):
    """Information about how a package version was added to a repository."""

    domainEntryPoint: Optional[DomainEntryPoint]
    originType: Optional[PackageVersionOriginType]


class LicenseInfo(TypedDict, total=False):
    """Details of the license data."""

    name: Optional[String]
    url: Optional[String]


LicenseInfoList = List[LicenseInfo]


class PackageVersionDescription(TypedDict, total=False):
    """Details about a package version."""

    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    packageName: Optional[PackageName]
    displayName: Optional[String255]
    version: Optional[PackageVersion]
    summary: Optional[String]
    homePage: Optional[String]
    sourceCodeRepository: Optional[String]
    publishedTime: Optional[Timestamp]
    licenses: Optional[LicenseInfoList]
    revision: Optional[PackageVersionRevision]
    status: Optional[PackageVersionStatus]
    origin: Optional[PackageVersionOrigin]


class DescribePackageVersionResult(TypedDict, total=False):
    packageVersion: PackageVersionDescription


class DescribeRepositoryRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName


class DescribeRepositoryResult(TypedDict, total=False):
    repository: Optional[RepositoryDescription]


class DisassociateExternalConnectionRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    externalConnection: ExternalConnectionName


class DisassociateExternalConnectionResult(TypedDict, total=False):
    repository: Optional[RepositoryDescription]


class DisposePackageVersionsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    versions: PackageVersionList
    versionRevisions: Optional[PackageVersionRevisionMap]
    expectedStatus: Optional[PackageVersionStatus]


class DisposePackageVersionsResult(TypedDict, total=False):
    successfulVersions: Optional[SuccessfulPackageVersionInfoMap]
    failedVersions: Optional[PackageVersionErrorMap]


class DomainSummary(TypedDict, total=False):
    """Information about a domain, including its name, Amazon Resource Name
    (ARN), and status. The
    `ListDomains <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html>`__
    operation returns a list of ``DomainSummary`` objects.
    """

    name: Optional[DomainName]
    owner: Optional[AccountId]
    arn: Optional[Arn]
    status: Optional[DomainStatus]
    createdTime: Optional[Timestamp]
    encryptionKey: Optional[Arn]


DomainSummaryList = List[DomainSummary]


class GetAssociatedPackageGroupRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName


class GetAssociatedPackageGroupResult(TypedDict, total=False):
    packageGroup: Optional[PackageGroupDescription]
    associationType: Optional[PackageGroupAssociationType]


class GetAuthorizationTokenRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    durationSeconds: Optional[AuthorizationTokenDurationSeconds]


class GetAuthorizationTokenResult(TypedDict, total=False):
    authorizationToken: Optional[String]
    expiration: Optional[Timestamp]


class GetDomainPermissionsPolicyRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]


class GetDomainPermissionsPolicyResult(TypedDict, total=False):
    policy: Optional[ResourcePolicy]


class GetPackageVersionAssetRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    packageVersion: PackageVersion
    asset: AssetName
    packageVersionRevision: Optional[PackageVersionRevision]


class GetPackageVersionAssetResult(TypedDict, total=False):
    asset: Optional[Union[Asset, IO[Asset], Iterable[Asset]]]
    assetName: Optional[AssetName]
    packageVersion: Optional[PackageVersion]
    packageVersionRevision: Optional[PackageVersionRevision]


class GetPackageVersionReadmeRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    packageVersion: PackageVersion


class GetPackageVersionReadmeResult(TypedDict, total=False):
    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    version: Optional[PackageVersion]
    versionRevision: Optional[PackageVersionRevision]
    readme: Optional[String]


class GetRepositoryEndpointRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    endpointType: Optional[EndpointType]


class GetRepositoryEndpointResult(TypedDict, total=False):
    repositoryEndpoint: Optional[String]


class GetRepositoryPermissionsPolicyRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName


class GetRepositoryPermissionsPolicyResult(TypedDict, total=False):
    policy: Optional[ResourcePolicy]


class ListAllowedRepositoriesForGroupRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern
    originRestrictionType: PackageGroupOriginRestrictionType
    maxResults: Optional[ListAllowedRepositoriesForGroupMaxResults]
    nextToken: Optional[PaginationToken]


RepositoryNameList = List[RepositoryName]


class ListAllowedRepositoriesForGroupResult(TypedDict, total=False):
    allowedRepositories: Optional[RepositoryNameList]
    nextToken: Optional[PaginationToken]


class ListAssociatedPackagesRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern
    maxResults: Optional[ListPackagesMaxResults]
    nextToken: Optional[PaginationToken]
    preview: Optional[BooleanOptional]


class ListAssociatedPackagesResult(TypedDict, total=False):
    packages: Optional[AssociatedPackageList]
    nextToken: Optional[PaginationToken]


class ListDomainsRequest(ServiceRequest):
    maxResults: Optional[ListDomainsMaxResults]
    nextToken: Optional[PaginationToken]


class ListDomainsResult(TypedDict, total=False):
    domains: Optional[DomainSummaryList]
    nextToken: Optional[PaginationToken]


class ListPackageGroupsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    maxResults: Optional[ListPackageGroupsMaxResults]
    nextToken: Optional[PaginationToken]
    prefix: Optional[PackageGroupPatternPrefix]


class PackageGroupSummary(TypedDict, total=False):
    """Details about a package group."""

    arn: Optional[Arn]
    pattern: Optional[PackageGroupPattern]
    domainName: Optional[DomainName]
    domainOwner: Optional[AccountId]
    createdTime: Optional[Timestamp]
    contactInfo: Optional[PackageGroupContactInfo]
    description: Optional[Description]
    originConfiguration: Optional[PackageGroupOriginConfiguration]
    parent: Optional[PackageGroupReference]


PackageGroupSummaryList = List[PackageGroupSummary]


class ListPackageGroupsResult(TypedDict, total=False):
    packageGroups: Optional[PackageGroupSummaryList]
    nextToken: Optional[PaginationToken]


class ListPackageVersionAssetsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    packageVersion: PackageVersion
    maxResults: Optional[ListPackageVersionAssetsMaxResults]
    nextToken: Optional[PaginationToken]


class ListPackageVersionAssetsResult(TypedDict, total=False):
    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    version: Optional[PackageVersion]
    versionRevision: Optional[PackageVersionRevision]
    nextToken: Optional[PaginationToken]
    assets: Optional[AssetSummaryList]


class ListPackageVersionDependenciesRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    packageVersion: PackageVersion
    nextToken: Optional[PaginationToken]


class PackageDependency(TypedDict, total=False):
    """Details about a package dependency."""

    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    dependencyType: Optional[String]
    versionRequirement: Optional[String]


PackageDependencyList = List[PackageDependency]


class ListPackageVersionDependenciesResult(TypedDict, total=False):
    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    version: Optional[PackageVersion]
    versionRevision: Optional[PackageVersionRevision]
    nextToken: Optional[PaginationToken]
    dependencies: Optional[PackageDependencyList]


class ListPackageVersionsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    status: Optional[PackageVersionStatus]
    sortBy: Optional[PackageVersionSortType]
    maxResults: Optional[ListPackageVersionsMaxResults]
    nextToken: Optional[PaginationToken]
    originType: Optional[PackageVersionOriginType]


class PackageVersionSummary(TypedDict, total=False):
    """Details about a package version, including its status, version, and
    revision. The
    `ListPackageVersions <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html>`__
    operation returns a list of ``PackageVersionSummary`` objects.
    """

    version: PackageVersion
    revision: Optional[PackageVersionRevision]
    status: PackageVersionStatus
    origin: Optional[PackageVersionOrigin]


PackageVersionSummaryList = List[PackageVersionSummary]


class ListPackageVersionsResult(TypedDict, total=False):
    defaultDisplayVersion: Optional[PackageVersion]
    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    versions: Optional[PackageVersionSummaryList]
    nextToken: Optional[PaginationToken]


class ListPackagesRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    packagePrefix: Optional[PackageName]
    maxResults: Optional[ListPackagesMaxResults]
    nextToken: Optional[PaginationToken]
    publish: Optional[AllowPublish]
    upstream: Optional[AllowUpstream]


PackageSummaryList = List[PackageSummary]


class ListPackagesResult(TypedDict, total=False):
    packages: Optional[PackageSummaryList]
    nextToken: Optional[PaginationToken]


class ListRepositoriesInDomainRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    administratorAccount: Optional[AccountId]
    repositoryPrefix: Optional[RepositoryName]
    maxResults: Optional[ListRepositoriesInDomainMaxResults]
    nextToken: Optional[PaginationToken]


class RepositorySummary(TypedDict, total=False):
    """Details about a repository, including its Amazon Resource Name (ARN),
    description, and domain information. The
    `ListRepositories <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html>`__
    operation returns a list of ``RepositorySummary`` objects.
    """

    name: Optional[RepositoryName]
    administratorAccount: Optional[AccountId]
    domainName: Optional[DomainName]
    domainOwner: Optional[AccountId]
    arn: Optional[Arn]
    description: Optional[Description]
    createdTime: Optional[Timestamp]


RepositorySummaryList = List[RepositorySummary]


class ListRepositoriesInDomainResult(TypedDict, total=False):
    repositories: Optional[RepositorySummaryList]
    nextToken: Optional[PaginationToken]


class ListRepositoriesRequest(ServiceRequest):
    repositoryPrefix: Optional[RepositoryName]
    maxResults: Optional[ListRepositoriesMaxResults]
    nextToken: Optional[PaginationToken]


class ListRepositoriesResult(TypedDict, total=False):
    repositories: Optional[RepositorySummaryList]
    nextToken: Optional[PaginationToken]


class ListSubPackageGroupsRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern
    maxResults: Optional[ListPackageGroupsMaxResults]
    nextToken: Optional[PaginationToken]


class ListSubPackageGroupsResult(TypedDict, total=False):
    packageGroups: Optional[PackageGroupSummaryList]
    nextToken: Optional[PaginationToken]


class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: Arn


class ListTagsForResourceResult(TypedDict, total=False):
    tags: Optional[TagList]


OriginRestrictions = Dict[PackageGroupOriginRestrictionType, PackageGroupOriginRestrictionMode]


class PackageGroupAllowedRepository(TypedDict, total=False):
    """Details about an allowed repository for a package group, including its
    name and origin configuration.
    """

    repositoryName: Optional[RepositoryName]
    originRestrictionType: Optional[PackageGroupOriginRestrictionType]


PackageGroupAllowedRepositoryList = List[PackageGroupAllowedRepository]
PackageGroupAllowedRepositoryUpdate = Dict[
    PackageGroupAllowedRepositoryUpdateType, RepositoryNameList
]
PackageGroupAllowedRepositoryUpdates = Dict[
    PackageGroupOriginRestrictionType, PackageGroupAllowedRepositoryUpdate
]


class PublishPackageVersionRequest(ServiceRequest):
    assetContent: IO[Asset]
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    packageVersion: PackageVersion
    assetName: AssetName
    assetSHA256: SHA256
    unfinished: Optional[BooleanOptional]


class PublishPackageVersionResult(TypedDict, total=False):
    format: Optional[PackageFormat]
    namespace: Optional[PackageNamespace]
    package: Optional[PackageName]
    version: Optional[PackageVersion]
    versionRevision: Optional[PackageVersionRevision]
    status: Optional[PackageVersionStatus]
    asset: Optional[AssetSummary]


class PutDomainPermissionsPolicyRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    policyRevision: Optional[PolicyRevision]
    policyDocument: PolicyDocument


class PutDomainPermissionsPolicyResult(TypedDict, total=False):
    policy: Optional[ResourcePolicy]


class PutPackageOriginConfigurationRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    restrictions: PackageOriginRestrictions


class PutPackageOriginConfigurationResult(TypedDict, total=False):
    originConfiguration: Optional[PackageOriginConfiguration]


class PutRepositoryPermissionsPolicyRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    policyRevision: Optional[PolicyRevision]
    policyDocument: PolicyDocument


class PutRepositoryPermissionsPolicyResult(TypedDict, total=False):
    policy: Optional[ResourcePolicy]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    resourceArn: Arn
    tags: TagList


class TagResourceResult(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    resourceArn: Arn
    tagKeys: TagKeyList


class UntagResourceResult(TypedDict, total=False):
    pass


class UpdatePackageGroupOriginConfigurationRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern
    restrictions: Optional[OriginRestrictions]
    addAllowedRepositories: Optional[PackageGroupAllowedRepositoryList]
    removeAllowedRepositories: Optional[PackageGroupAllowedRepositoryList]


class UpdatePackageGroupOriginConfigurationResult(TypedDict, total=False):
    packageGroup: Optional[PackageGroupDescription]
    allowedRepositoryUpdates: Optional[PackageGroupAllowedRepositoryUpdates]


class UpdatePackageGroupRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    packageGroup: PackageGroupPattern
    contactInfo: Optional[PackageGroupContactInfo]
    description: Optional[Description]


class UpdatePackageGroupResult(TypedDict, total=False):
    packageGroup: Optional[PackageGroupDescription]


class UpdatePackageVersionsStatusRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    format: PackageFormat
    namespace: Optional[PackageNamespace]
    package: PackageName
    versions: PackageVersionList
    versionRevisions: Optional[PackageVersionRevisionMap]
    expectedStatus: Optional[PackageVersionStatus]
    targetStatus: PackageVersionStatus


class UpdatePackageVersionsStatusResult(TypedDict, total=False):
    successfulVersions: Optional[SuccessfulPackageVersionInfoMap]
    failedVersions: Optional[PackageVersionErrorMap]


class UpdateRepositoryRequest(ServiceRequest):
    domain: DomainName
    domainOwner: Optional[AccountId]
    repository: RepositoryName
    description: Optional[Description]
    upstreams: Optional[UpstreamRepositoryList]


class UpdateRepositoryResult(TypedDict, total=False):
    repository: Optional[RepositoryDescription]


class CodeartifactApi:
    service = "codeartifact"
    version = "2018-09-22"

    @handler("AssociateExternalConnection")
    def associate_external_connection(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        external_connection: ExternalConnectionName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> AssociateExternalConnectionResult:
        """Adds an existing external connection to a repository. One external
        connection is allowed per repository.

        A repository can have one or more upstream repositories, or an external
        connection.

        :param domain: The name of the domain that contains the repository.
        :param repository: The name of the repository to which the external connection is added.
        :param external_connection: The name of the external connection to add to the repository.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: AssociateExternalConnectionResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("CopyPackageVersions")
    def copy_package_versions(
        self,
        context: RequestContext,
        domain: DomainName,
        source_repository: RepositoryName,
        destination_repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        versions: PackageVersionList | None = None,
        version_revisions: PackageVersionRevisionMap | None = None,
        allow_overwrite: BooleanOptional | None = None,
        include_from_upstream: BooleanOptional | None = None,
        **kwargs,
    ) -> CopyPackageVersionsResult:
        """Copies package versions from one repository to another repository in the
        same domain.

        You must specify ``versions`` or ``versionRevisions``. You cannot
        specify both.

        :param domain: The name of the domain that contains the source and destination
        repositories.
        :param source_repository: The name of the repository that contains the package versions to be
        copied.
        :param destination_repository: The name of the repository into which package versions are copied.
        :param format: The format of the package versions to be copied.
        :param package: The name of the package that contains the versions to be copied.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package versions to be copied.
        :param versions: The versions of the package to be copied.
        :param version_revisions: A list of key-value pairs.
        :param allow_overwrite: Set to true to overwrite a package version that already exists in the
        destination repository.
        :param include_from_upstream: Set to true to copy packages from repositories that are upstream from
        the source repository to the destination repository.
        :returns: CopyPackageVersionsResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("CreateDomain")
    def create_domain(
        self,
        context: RequestContext,
        domain: DomainName,
        encryption_key: Arn | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDomainResult:
        """Creates a domain. CodeArtifact *domains* make it easier to manage
        multiple repositories across an organization. You can use a domain to
        apply permissions across many repositories owned by different Amazon Web
        Services accounts. An asset is stored only once in a domain, even if
        it's in multiple repositories.

        Although you can have multiple domains, we recommend a single production
        domain that contains all published artifacts so that your development
        teams can find and share packages. You can use a second pre-production
        domain to test changes to the production domain configuration.

        :param domain: The name of the domain to create.
        :param encryption_key: The encryption key for the domain.
        :param tags: One or more tag key-value pairs for the domain.
        :returns: CreateDomainResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("CreatePackageGroup")
    def create_package_group(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        domain_owner: AccountId | None = None,
        contact_info: PackageGroupContactInfo | None = None,
        description: Description | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreatePackageGroupResult:
        """Creates a package group. For more information about creating package
        groups, including example CLI commands, see `Create a package
        group <https://docs.aws.amazon.com/codeartifact/latest/ug/create-package-group.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain in which you want to create a package group.
        :param package_group: The pattern of the package group to create.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param contact_info: The contact information for the created package group.
        :param description: A description of the package group.
        :param tags: One or more tag key-value pairs for the package group.
        :returns: CreatePackageGroupResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("CreateRepository")
    def create_repository(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        description: Description | None = None,
        upstreams: UpstreamRepositoryList | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateRepositoryResult:
        """Creates a repository.

        :param domain: The name of the domain that contains the created repository.
        :param repository: The name of the repository to create.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param description: A description of the created repository.
        :param upstreams: A list of upstream repositories to associate with the repository.
        :param tags: One or more tag key-value pairs for the repository.
        :returns: CreateRepositoryResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeleteDomain")
    def delete_domain(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DeleteDomainResult:
        """Deletes a domain. You cannot delete a domain that contains repositories.
        If you want to delete a domain with repositories, first delete its
        repositories.

        :param domain: The name of the domain to delete.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DeleteDomainResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeleteDomainPermissionsPolicy")
    def delete_domain_permissions_policy(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        policy_revision: PolicyRevision | None = None,
        **kwargs,
    ) -> DeleteDomainPermissionsPolicyResult:
        """Deletes the resource policy set on a domain.

        :param domain: The name of the domain associated with the resource policy to be
        deleted.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param policy_revision: The current revision of the resource policy to be deleted.
        :returns: DeleteDomainPermissionsPolicyResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeletePackage")
    def delete_package(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        **kwargs,
    ) -> DeletePackageResult:
        """Deletes a package and all associated package versions. A deleted package
        cannot be restored. To delete one or more package versions, use the
        `DeletePackageVersions <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html>`__
        API.

        :param domain: The name of the domain that contains the package to delete.
        :param repository: The name of the repository that contains the package to delete.
        :param format: The format of the requested package to delete.
        :param package: The name of the package to delete.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package to delete.
        :returns: DeletePackageResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeletePackageGroup")
    def delete_package_group(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: String,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DeletePackageGroupResult:
        """Deletes a package group. Deleting a package group does not delete
        packages or package versions associated with the package group. When a
        package group is deleted, the direct child package groups will become
        children of the package group's direct parent package group. Therefore,
        if any of the child groups are inheriting any settings from the parent,
        those settings could change.

        :param domain: The domain that contains the package group to be deleted.
        :param package_group: The pattern of the package group to be deleted.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DeletePackageGroupResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeletePackageVersions")
    def delete_package_versions(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        versions: PackageVersionList,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        expected_status: PackageVersionStatus | None = None,
        **kwargs,
    ) -> DeletePackageVersionsResult:
        """Deletes one or more versions of a package. A deleted package version
        cannot be restored in your repository. If you want to remove a package
        version from your repository and be able to restore it later, set its
        status to ``Archived``. Archived packages cannot be downloaded from a
        repository and don't show up with list package APIs (for example,
        `ListPackageVersions <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html>`__),
        but you can restore them using
        `UpdatePackageVersionsStatus <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html>`__.

        :param domain: The name of the domain that contains the package to delete.
        :param repository: The name of the repository that contains the package versions to delete.
        :param format: The format of the package versions to delete.
        :param package: The name of the package with the versions to delete.
        :param versions: An array of strings that specify the versions of the package to delete.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package versions to be deleted.
        :param expected_status: The expected status of the package version to delete.
        :returns: DeletePackageVersionsResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeleteRepository")
    def delete_repository(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DeleteRepositoryResult:
        """Deletes a repository.

        :param domain: The name of the domain that contains the repository to delete.
        :param repository: The name of the repository to delete.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DeleteRepositoryResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DeleteRepositoryPermissionsPolicy")
    def delete_repository_permissions_policy(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        policy_revision: PolicyRevision | None = None,
        **kwargs,
    ) -> DeleteRepositoryPermissionsPolicyResult:
        """Deletes the resource policy that is set on a repository. After a
        resource policy is deleted, the permissions allowed and denied by the
        deleted policy are removed. The effect of deleting a resource policy
        might not be immediate.

        Use ``DeleteRepositoryPermissionsPolicy`` with caution. After a policy
        is deleted, Amazon Web Services users, roles, and accounts lose
        permissions to perform the repository actions granted by the deleted
        policy.

        :param domain: The name of the domain that contains the repository associated with the
        resource policy to be deleted.
        :param repository: The name of the repository that is associated with the resource policy
        to be deleted.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param policy_revision: The revision of the repository's resource policy to be deleted.
        :returns: DeleteRepositoryPermissionsPolicyResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeDomain")
    def describe_domain(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DescribeDomainResult:
        """Returns a
        `DomainDescription <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html>`__
        object that contains information about the requested domain.

        :param domain: A string that specifies the name of the requested domain.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DescribeDomainResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribePackage")
    def describe_package(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        **kwargs,
    ) -> DescribePackageResult:
        """Returns a
        `PackageDescription <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html>`__
        object that contains information about the requested package.

        :param domain: The name of the domain that contains the repository that contains the
        package.
        :param repository: The name of the repository that contains the requested package.
        :param format: A format that specifies the type of the requested package.
        :param package: The name of the requested package.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the requested package.
        :returns: DescribePackageResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribePackageGroup")
    def describe_package_group(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DescribePackageGroupResult:
        """Returns a
        `PackageGroupDescription <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html>`__
        object that contains information about the requested package group.

        :param domain: The name of the domain that contains the package group.
        :param package_group: The pattern of the requested package group.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DescribePackageGroupResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribePackageVersion")
    def describe_package_version(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        package_version: PackageVersion,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        **kwargs,
    ) -> DescribePackageVersionResult:
        """Returns a
        `PackageVersionDescription <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html>`__
        object that contains information about the requested package version.

        :param domain: The name of the domain that contains the repository that contains the
        package version.
        :param repository: The name of the repository that contains the package version.
        :param format: A format that specifies the type of the requested package version.
        :param package: The name of the requested package version.
        :param package_version: A string that contains the package version (for example, ``3.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the requested package version.
        :returns: DescribePackageVersionResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeRepository")
    def describe_repository(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DescribeRepositoryResult:
        """Returns a ``RepositoryDescription`` object that contains detailed
        information about the requested repository.

        :param domain: The name of the domain that contains the repository to describe.
        :param repository: A string that specifies the name of the requested repository.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DescribeRepositoryResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DisassociateExternalConnection")
    def disassociate_external_connection(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        external_connection: ExternalConnectionName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> DisassociateExternalConnectionResult:
        """Removes an existing external connection from a repository.

        :param domain: The name of the domain that contains the repository from which to remove
        the external repository.
        :param repository: The name of the repository from which the external connection will be
        removed.
        :param external_connection: The name of the external connection to be removed from the repository.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: DisassociateExternalConnectionResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DisposePackageVersions")
    def dispose_package_versions(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        versions: PackageVersionList,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        version_revisions: PackageVersionRevisionMap | None = None,
        expected_status: PackageVersionStatus | None = None,
        **kwargs,
    ) -> DisposePackageVersionsResult:
        """Deletes the assets in package versions and sets the package versions'
        status to ``Disposed``. A disposed package version cannot be restored in
        your repository because its assets are deleted.

        To view all disposed package versions in a repository, use
        `ListPackageVersions <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html>`__
        and set the
        `status <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax>`__
        parameter to ``Disposed``.

        To view information about a disposed package version, use
        `DescribePackageVersion <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html>`__.

        :param domain: The name of the domain that contains the repository you want to dispose.
        :param repository: The name of the repository that contains the package versions you want
        to dispose.
        :param format: A format that specifies the type of package versions you want to
        dispose.
        :param package: The name of the package with the versions you want to dispose.
        :param versions: The versions of the package you want to dispose.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package versions to be disposed.
        :param version_revisions: The revisions of the package versions you want to dispose.
        :param expected_status: The expected status of the package version to dispose.
        :returns: DisposePackageVersionsResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetAssociatedPackageGroup")
    def get_associated_package_group(
        self,
        context: RequestContext,
        domain: DomainName,
        format: PackageFormat,
        package: PackageName,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        **kwargs,
    ) -> GetAssociatedPackageGroupResult:
        """Returns the most closely associated package group to the specified
        package. This API does not require that the package exist in any
        repository in the domain. As such, ``GetAssociatedPackageGroup`` can be
        used to see which package group's origin configuration applies to a
        package before that package is in a repository. This can be helpful to
        check if public packages are blocked without ingesting them.

        For information package group association and matching, see `Package
        group definition syntax and matching
        behavior <https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain that contains the package from which to get the
        associated package group.
        :param format: The format of the package from which to get the associated package
        group.
        :param package: The package from which to get the associated package group.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package from which to get the associated package
        group.
        :returns: GetAssociatedPackageGroupResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetAuthorizationToken")
    def get_authorization_token(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        duration_seconds: AuthorizationTokenDurationSeconds | None = None,
        **kwargs,
    ) -> GetAuthorizationTokenResult:
        """Generates a temporary authorization token for accessing repositories in
        the domain. This API requires the ``codeartifact:GetAuthorizationToken``
        and ``sts:GetServiceBearerToken`` permissions. For more information
        about authorization tokens, see `CodeArtifact authentication and
        tokens <https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html>`__.

        CodeArtifact authorization tokens are valid for a period of 12 hours
        when created with the ``login`` command. You can call ``login``
        periodically to refresh the token. When you create an authorization
        token with the ``GetAuthorizationToken`` API, you can set a custom
        authorization period, up to a maximum of 12 hours, with the
        ``durationSeconds`` parameter.

        The authorization period begins after ``login`` or
        ``GetAuthorizationToken`` is called. If ``login`` or
        ``GetAuthorizationToken`` is called while assuming a role, the token
        lifetime is independent of the maximum session duration of the role. For
        example, if you call ``sts assume-role`` and specify a session duration
        of 15 minutes, then generate a CodeArtifact authorization token, the
        token will be valid for the full authorization period even though this
        is longer than the 15-minute session duration.

        See `Using IAM
        Roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`__
        for more information on controlling session duration.

        :param domain: The name of the domain that is in scope for the generated authorization
        token.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param duration_seconds: The time, in seconds, that the generated authorization token is valid.
        :returns: GetAuthorizationTokenResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetDomainPermissionsPolicy")
    def get_domain_permissions_policy(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> GetDomainPermissionsPolicyResult:
        """Returns the resource policy attached to the specified domain.

        The policy is a resource-based policy, not an identity-based policy. For
        more information, see `Identity-based policies and resource-based
        policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html>`__
        in the *IAM User Guide*.

        :param domain: The name of the domain to which the resource policy is attached.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: GetDomainPermissionsPolicyResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetPackageVersionAsset")
    def get_package_version_asset(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        package_version: PackageVersion,
        asset: AssetName,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        package_version_revision: PackageVersionRevision | None = None,
        **kwargs,
    ) -> GetPackageVersionAssetResult:
        """Returns an asset (or file) that is in a package. For example, for a
        Maven package version, use ``GetPackageVersionAsset`` to download a
        ``JAR`` file, a ``POM`` file, or any other assets in the package
        version.

        :param domain: The name of the domain that contains the repository that contains the
        package version with the requested asset.
        :param repository: The repository that contains the package version with the requested
        asset.
        :param format: A format that specifies the type of the package version with the
        requested asset file.
        :param package: The name of the package that contains the requested asset.
        :param package_version: A string that contains the package version (for example, ``3.
        :param asset: The name of the requested asset.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package version with the requested asset file.
        :param package_version_revision: The name of the package version revision that contains the requested
        asset.
        :returns: GetPackageVersionAssetResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetPackageVersionReadme")
    def get_package_version_readme(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        package_version: PackageVersion,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        **kwargs,
    ) -> GetPackageVersionReadmeResult:
        """Gets the readme file or descriptive text for a package version.

        The returned text might contain formatting. For example, it might
        contain formatting for Markdown or reStructuredText.

        :param domain: The name of the domain that contains the repository that contains the
        package version with the requested readme file.
        :param repository: The repository that contains the package with the requested readme file.
        :param format: A format that specifies the type of the package version with the
        requested readme file.
        :param package: The name of the package version that contains the requested readme file.
        :param package_version: A string that contains the package version (for example, ``3.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package version with the requested readme file.
        :returns: GetPackageVersionReadmeResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetRepositoryEndpoint")
    def get_repository_endpoint(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        domain_owner: AccountId | None = None,
        endpoint_type: EndpointType | None = None,
        **kwargs,
    ) -> GetRepositoryEndpointResult:
        """Returns the endpoint of a repository for a specific package format. A
        repository has one endpoint for each package format:

        -  ``cargo``

        -  ``generic``

        -  ``maven``

        -  ``npm``

        -  ``nuget``

        -  ``pypi``

        -  ``ruby``

        -  ``swift``

        :param domain: The name of the domain that contains the repository.
        :param repository: The name of the repository.
        :param format: Returns which endpoint of a repository to return.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain that contains the repository.
        :param endpoint_type: A string that specifies the type of endpoint.
        :returns: GetRepositoryEndpointResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetRepositoryPermissionsPolicy")
    def get_repository_permissions_policy(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        **kwargs,
    ) -> GetRepositoryPermissionsPolicyResult:
        """Returns the resource policy that is set on a repository.

        :param domain: The name of the domain containing the repository whose associated
        resource policy is to be retrieved.
        :param repository: The name of the repository whose associated resource policy is to be
        retrieved.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :returns: GetRepositoryPermissionsPolicyResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListAllowedRepositoriesForGroup")
    def list_allowed_repositories_for_group(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        origin_restriction_type: PackageGroupOriginRestrictionType,
        domain_owner: AccountId | None = None,
        max_results: ListAllowedRepositoriesForGroupMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListAllowedRepositoriesForGroupResult:
        """Lists the repositories in the added repositories list of the specified
        restriction type for a package group. For more information about
        restriction types and added repository lists, see `Package group origin
        controls <https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain that contains the package group from which to
        list allowed repositories.
        :param package_group: The pattern of the package group from which to list allowed
        repositories.
        :param origin_restriction_type: The origin configuration restriction type of which to list allowed
        repositories.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :returns: ListAllowedRepositoriesForGroupResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListAssociatedPackages")
    def list_associated_packages(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        domain_owner: AccountId | None = None,
        max_results: ListPackagesMaxResults | None = None,
        next_token: PaginationToken | None = None,
        preview: BooleanOptional | None = None,
        **kwargs,
    ) -> ListAssociatedPackagesResult:
        """Returns a list of packages associated with the requested package group.
        For information package group association and matching, see `Package
        group definition syntax and matching
        behavior <https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain that contains the package group from which to
        list associated packages.
        :param package_group: The pattern of the package group from which to list associated packages.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :param preview: When this flag is included, ``ListAssociatedPackages`` will return a
        list of packages that would be associated with a package group, even if
        it does not exist.
        :returns: ListAssociatedPackagesResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListDomains")
    def list_domains(
        self,
        context: RequestContext,
        max_results: ListDomainsMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListDomainsResult:
        """Returns a list of
        `DomainSummary <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html>`__
        objects for all domains owned by the Amazon Web Services account that
        makes this call. Each returned ``DomainSummary`` object contains
        information about a domain.

        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :returns: ListDomainsResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPackageGroups")
    def list_package_groups(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        max_results: ListPackageGroupsMaxResults | None = None,
        next_token: PaginationToken | None = None,
        prefix: PackageGroupPatternPrefix | None = None,
        **kwargs,
    ) -> ListPackageGroupsResult:
        """Returns a list of package groups in the requested domain.

        :param domain: The domain for which you want to list package groups.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :param prefix: A prefix for which to search package groups.
        :returns: ListPackageGroupsResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListPackageVersionAssets")
    def list_package_version_assets(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        package_version: PackageVersion,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        max_results: ListPackageVersionAssetsMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListPackageVersionAssetsResult:
        """Returns a list of
        `AssetSummary <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html>`__
        objects for assets in a package version.

        :param domain: The name of the domain that contains the repository associated with the
        package version assets.
        :param repository: The name of the repository that contains the package that contains the
        requested package version assets.
        :param format: The format of the package that contains the requested package version
        assets.
        :param package: The name of the package that contains the requested package version
        assets.
        :param package_version: A string that contains the package version (for example, ``3.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package version that contains the requested package
        version assets.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :returns: ListPackageVersionAssetsResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPackageVersionDependencies")
    def list_package_version_dependencies(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        package_version: PackageVersion,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListPackageVersionDependenciesResult:
        """Returns the direct dependencies for a package version. The dependencies
        are returned as
        `PackageDependency <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html>`__
        objects. CodeArtifact extracts the dependencies for a package version
        from the metadata file for the package format (for example, the
        ``package.json`` file for npm packages and the ``pom.xml`` file for
        Maven). Any package version dependencies that are not listed in the
        configuration file are not returned.

        :param domain: The name of the domain that contains the repository that contains the
        requested package version dependencies.
        :param repository: The name of the repository that contains the requested package version.
        :param format: The format of the package with the requested dependencies.
        :param package: The name of the package versions' package.
        :param package_version: A string that contains the package version (for example, ``3.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package version with the requested dependencies.
        :param next_token: The token for the next set of results.
        :returns: ListPackageVersionDependenciesResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPackageVersions")
    def list_package_versions(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        status: PackageVersionStatus | None = None,
        sort_by: PackageVersionSortType | None = None,
        max_results: ListPackageVersionsMaxResults | None = None,
        next_token: PaginationToken | None = None,
        origin_type: PackageVersionOriginType | None = None,
        **kwargs,
    ) -> ListPackageVersionsResult:
        """Returns a list of
        `PackageVersionSummary <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html>`__
        objects for package versions in a repository that match the request
        parameters. Package versions of all statuses will be returned by default
        when calling ``list-package-versions`` with no ``--status`` parameter.

        :param domain: The name of the domain that contains the repository that contains the
        requested package versions.
        :param repository: The name of the repository that contains the requested package versions.
        :param format: The format of the package versions you want to list.
        :param package: The name of the package for which you want to request package versions.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package that contains the requested package
        versions.
        :param status: A string that filters the requested package versions by status.
        :param sort_by: How to sort the requested list of package versions.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :param origin_type: The ``originType`` used to filter package versions.
        :returns: ListPackageVersionsResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPackages")
    def list_packages(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        format: PackageFormat | None = None,
        namespace: PackageNamespace | None = None,
        package_prefix: PackageName | None = None,
        max_results: ListPackagesMaxResults | None = None,
        next_token: PaginationToken | None = None,
        publish: AllowPublish | None = None,
        upstream: AllowUpstream | None = None,
        **kwargs,
    ) -> ListPackagesResult:
        """Returns a list of
        `PackageSummary <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html>`__
        objects for packages in a repository that match the request parameters.

        :param domain: The name of the domain that contains the repository that contains the
        requested packages.
        :param repository: The name of the repository that contains the requested packages.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param format: The format used to filter requested packages.
        :param namespace: The namespace prefix used to filter requested packages.
        :param package_prefix: A prefix used to filter requested packages.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :param publish: The value of the ``Publish`` package origin control restriction used to
        filter requested packages.
        :param upstream: The value of the ``Upstream`` package origin control restriction used to
        filter requested packages.
        :returns: ListPackagesResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListRepositories")
    def list_repositories(
        self,
        context: RequestContext,
        repository_prefix: RepositoryName | None = None,
        max_results: ListRepositoriesMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListRepositoriesResult:
        """Returns a list of
        `RepositorySummary <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html>`__
        objects. Each ``RepositorySummary`` contains information about a
        repository in the specified Amazon Web Services account and that matches
        the input parameters.

        :param repository_prefix: A prefix used to filter returned repositories.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :returns: ListRepositoriesResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListRepositoriesInDomain")
    def list_repositories_in_domain(
        self,
        context: RequestContext,
        domain: DomainName,
        domain_owner: AccountId | None = None,
        administrator_account: AccountId | None = None,
        repository_prefix: RepositoryName | None = None,
        max_results: ListRepositoriesInDomainMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListRepositoriesInDomainResult:
        """Returns a list of
        `RepositorySummary <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html>`__
        objects. Each ``RepositorySummary`` contains information about a
        repository in the specified domain and that matches the input
        parameters.

        :param domain: The name of the domain that contains the returned list of repositories.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param administrator_account: Filter the list of repositories to only include those that are managed
        by the Amazon Web Services account ID.
        :param repository_prefix: A prefix used to filter returned repositories.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :returns: ListRepositoriesInDomainResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListSubPackageGroups")
    def list_sub_package_groups(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        domain_owner: AccountId | None = None,
        max_results: ListPackageGroupsMaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListSubPackageGroupsResult:
        """Returns a list of direct children of the specified package group.

        For information package group hierarchy, see `Package group definition
        syntax and matching
        behavior <https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain which contains the package group from which to
        list sub package groups.
        :param package_group: The pattern of the package group from which to list sub package groups.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param max_results: The maximum number of results to return per page.
        :param next_token: The token for the next set of results.
        :returns: ListSubPackageGroupsResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: Arn, **kwargs
    ) -> ListTagsForResourceResult:
        """Gets information about Amazon Web Services tags for a specified Amazon
        Resource Name (ARN) in CodeArtifact.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to get tags for.
        :returns: ListTagsForResourceResult
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("PublishPackageVersion")
    def publish_package_version(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        package_version: PackageVersion,
        asset_content: IO[Asset],
        asset_name: AssetName,
        asset_sha256: SHA256,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        unfinished: BooleanOptional | None = None,
        **kwargs,
    ) -> PublishPackageVersionResult:
        """Creates a new package version containing one or more assets (or files).

        The ``unfinished`` flag can be used to keep the package version in the
        ``Unfinished`` state until all of its assets have been uploaded (see
        `Package version
        status <https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status>`__
        in the *CodeArtifact user guide*). To set the package version’s status
        to ``Published``, omit the ``unfinished`` flag when uploading the final
        asset, or set the status using
        `UpdatePackageVersionStatus <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html>`__.
        Once a package version’s status is set to ``Published``, it cannot
        change back to ``Unfinished``.

        Only generic packages can be published using this API. For more
        information, see `Using generic
        packages <https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain that contains the repository that contains the
        package version to publish.
        :param repository: The name of the repository that the package version will be published
        to.
        :param format: A format that specifies the type of the package version with the
        requested asset file.
        :param package: The name of the package version to publish.
        :param package_version: The package version to publish (for example, ``3.
        :param asset_content: The content of the asset to publish.
        :param asset_name: The name of the asset to publish.
        :param asset_sha256: The SHA256 hash of the ``assetContent`` to publish.
        :param domain_owner: The 12-digit account number of the AWS account that owns the domain.
        :param namespace: The namespace of the package version to publish.
        :param unfinished: Specifies whether the package version should remain in the
        ``unfinished`` state.
        :returns: PublishPackageVersionResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("PutDomainPermissionsPolicy")
    def put_domain_permissions_policy(
        self,
        context: RequestContext,
        domain: DomainName,
        policy_document: PolicyDocument,
        domain_owner: AccountId | None = None,
        policy_revision: PolicyRevision | None = None,
        **kwargs,
    ) -> PutDomainPermissionsPolicyResult:
        """Sets a resource policy on a domain that specifies permissions to access
        it.

        When you call ``PutDomainPermissionsPolicy``, the resource policy on the
        domain is ignored when evaluting permissions. This ensures that the
        owner of a domain cannot lock themselves out of the domain, which would
        prevent them from being able to update the resource policy.

        :param domain: The name of the domain on which to set the resource policy.
        :param policy_document: A valid displayable JSON Aspen policy string to be set as the access
        control resource policy on the provided domain.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param policy_revision: The current revision of the resource policy to be set.
        :returns: PutDomainPermissionsPolicyResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("PutPackageOriginConfiguration")
    def put_package_origin_configuration(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        restrictions: PackageOriginRestrictions,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        **kwargs,
    ) -> PutPackageOriginConfigurationResult:
        """Sets the package origin configuration for a package.

        The package origin configuration determines how new versions of a
        package can be added to a repository. You can allow or block direct
        publishing of new package versions, or ingestion and retaining of new
        package versions from an external connection or upstream source. For
        more information about package origin controls and configuration, see
        `Editing package origin
        controls <https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html>`__
        in the *CodeArtifact User Guide*.

        ``PutPackageOriginConfiguration`` can be called on a package that
        doesn't yet exist in the repository. When called on a package that does
        not exist, a package is created in the repository with no versions and
        the requested restrictions are set on the package. This can be used to
        preemptively block ingesting or retaining any versions from external
        connections or upstream repositories, or to block publishing any
        versions of the package into the repository before connecting any
        package managers or publishers to the repository.

        :param domain: The name of the domain that contains the repository that contains the
        package.
        :param repository: The name of the repository that contains the package.
        :param format: A format that specifies the type of the package to be updated.
        :param package: The name of the package to be updated.
        :param restrictions: A
        `PackageOriginRestrictions <https://docs.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package to be updated.
        :returns: PutPackageOriginConfigurationResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("PutRepositoryPermissionsPolicy")
    def put_repository_permissions_policy(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        policy_document: PolicyDocument,
        domain_owner: AccountId | None = None,
        policy_revision: PolicyRevision | None = None,
        **kwargs,
    ) -> PutRepositoryPermissionsPolicyResult:
        """Sets the resource policy on a repository that specifies permissions to
        access it.

        When you call ``PutRepositoryPermissionsPolicy``, the resource policy on
        the repository is ignored when evaluting permissions. This ensures that
        the owner of a repository cannot lock themselves out of the repository,
        which would prevent them from being able to update the resource policy.

        :param domain: The name of the domain containing the repository to set the resource
        policy on.
        :param repository: The name of the repository to set the resource policy on.
        :param policy_document: A valid displayable JSON Aspen policy string to be set as the access
        control resource policy on the provided repository.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param policy_revision: Sets the revision of the resource policy that specifies permissions to
        access the repository.
        :returns: PutRepositoryPermissionsPolicyResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: Arn, tags: TagList, **kwargs
    ) -> TagResourceResult:
        """Adds or updates tags for a resource in CodeArtifact.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to add or
        update tags for.
        :param tags: The tags you want to modify or add to the resource.
        :returns: TagResourceResult
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: Arn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResult:
        """Removes tags from a resource in CodeArtifact.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to remove
        tags from.
        :param tag_keys: The tag key for each tag that you want to remove from the resource.
        :returns: UntagResourceResult
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("UpdatePackageGroup")
    def update_package_group(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        domain_owner: AccountId | None = None,
        contact_info: PackageGroupContactInfo | None = None,
        description: Description | None = None,
        **kwargs,
    ) -> UpdatePackageGroupResult:
        """Updates a package group. This API cannot be used to update a package
        group's origin configuration or pattern. To update a package group's
        origin configuration, use
        `UpdatePackageGroupOriginConfiguration <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroupOriginConfiguration.html>`__.

        :param domain: The name of the domain which contains the package group to be updated.
        :param package_group: The pattern of the package group to be updated.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param contact_info: Contact information which you want to update the requested package group
        with.
        :param description: The description you want to update the requested package group with.
        :returns: UpdatePackageGroupResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdatePackageGroupOriginConfiguration")
    def update_package_group_origin_configuration(
        self,
        context: RequestContext,
        domain: DomainName,
        package_group: PackageGroupPattern,
        domain_owner: AccountId | None = None,
        restrictions: OriginRestrictions | None = None,
        add_allowed_repositories: PackageGroupAllowedRepositoryList | None = None,
        remove_allowed_repositories: PackageGroupAllowedRepositoryList | None = None,
        **kwargs,
    ) -> UpdatePackageGroupOriginConfigurationResult:
        """Updates the package origin configuration for a package group.

        The package origin configuration determines how new versions of a
        package can be added to a repository. You can allow or block direct
        publishing of new package versions, or ingestion and retaining of new
        package versions from an external connection or upstream source. For
        more information about package group origin controls and configuration,
        see `Package group origin
        controls <https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html>`__
        in the *CodeArtifact User Guide*.

        :param domain: The name of the domain which contains the package group for which to
        update the origin configuration.
        :param package_group: The pattern of the package group for which to update the origin
        configuration.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param restrictions: The origin configuration settings that determine how package versions
        can enter repositories.
        :param add_allowed_repositories: The repository name and restrictions to add to the allowed repository
        list of the specified package group.
        :param remove_allowed_repositories: The repository name and restrictions to remove from the allowed
        repository list of the specified package group.
        :returns: UpdatePackageGroupOriginConfigurationResult
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdatePackageVersionsStatus")
    def update_package_versions_status(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        format: PackageFormat,
        package: PackageName,
        versions: PackageVersionList,
        target_status: PackageVersionStatus,
        domain_owner: AccountId | None = None,
        namespace: PackageNamespace | None = None,
        version_revisions: PackageVersionRevisionMap | None = None,
        expected_status: PackageVersionStatus | None = None,
        **kwargs,
    ) -> UpdatePackageVersionsStatusResult:
        """Updates the status of one or more versions of a package. Using
        ``UpdatePackageVersionsStatus``, you can update the status of package
        versions to ``Archived``, ``Published``, or ``Unlisted``. To set the
        status of a package version to ``Disposed``, use
        `DisposePackageVersions <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html>`__.

        :param domain: The name of the domain that contains the repository that contains the
        package versions with a status to be updated.
        :param repository: The repository that contains the package versions with the status you
        want to update.
        :param format: A format that specifies the type of the package with the statuses to
        update.
        :param package: The name of the package with the version statuses to update.
        :param versions: An array of strings that specify the versions of the package with the
        statuses to update.
        :param target_status: The status you want to change the package version status to.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param namespace: The namespace of the package version to be updated.
        :param version_revisions: A map of package versions and package version revisions.
        :param expected_status: The package version’s expected status before it is updated.
        :returns: UpdatePackageVersionsStatusResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("UpdateRepository")
    def update_repository(
        self,
        context: RequestContext,
        domain: DomainName,
        repository: RepositoryName,
        domain_owner: AccountId | None = None,
        description: Description | None = None,
        upstreams: UpstreamRepositoryList | None = None,
        **kwargs,
    ) -> UpdateRepositoryResult:
        """Update the properties of a repository.

        :param domain: The name of the domain associated with the repository to update.
        :param repository: The name of the repository to update.
        :param domain_owner: The 12-digit account number of the Amazon Web Services account that owns
        the domain.
        :param description: An updated repository description.
        :param upstreams: A list of upstream repositories to associate with the repository.
        :returns: UpdateRepositoryResult
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError
