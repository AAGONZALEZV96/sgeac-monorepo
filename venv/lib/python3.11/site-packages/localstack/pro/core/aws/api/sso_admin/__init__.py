from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccessControlAttributeKey = str
AccessControlAttributeValueSource = str
AccessDeniedExceptionMessage = str
AccountId = str
ApplicationArn = str
ApplicationNameType = str
ApplicationProviderArn = str
ApplicationUrl = str
AssignmentRequired = bool
ClaimAttributePath = str
ClientToken = str
ConflictExceptionMessage = str
Description = str
Duration = str
IconUrl = str
Id = str
InstanceAccessControlAttributeConfigurationStatusReason = str
InstanceArn = str
InternalFailureMessage = str
JMESPath = str
ListApplicationAccessScopesRequestMaxResultsInteger = int
ManagedPolicyArn = str
ManagedPolicyName = str
ManagedPolicyPath = str
MaxResults = int
Name = str
NameType = str
PermissionSetArn = str
PermissionSetDescription = str
PermissionSetName = str
PermissionSetPolicyDocument = str
PrincipalId = str
Reason = str
RelayState = str
ResourceNotFoundMessage = str
ResourceServerScope = str
Scope = str
ScopeTarget = str
ServiceQuotaExceededMessage = str
TagKey = str
TagValue = str
TaggableResourceArn = str
TargetId = str
ThrottlingExceptionMessage = str
Token = str
TokenIssuerAudience = str
TrustedTokenIssuerArn = str
TrustedTokenIssuerName = str
TrustedTokenIssuerUrl = str
URI = str
UUId = str
ValidationExceptionMessage = str


class ApplicationStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ApplicationVisibility(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AuthenticationMethodType(StrEnum):
    IAM = "IAM"


class FederationProtocol(StrEnum):
    SAML = "SAML"
    OAUTH = "OAUTH"


class GrantType(StrEnum):
    authorization_code = "authorization_code"
    refresh_token = "refresh_token"
    urn_ietf_params_oauth_grant_type_jwt_bearer = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    urn_ietf_params_oauth_grant_type_token_exchange = (
        "urn:ietf:params:oauth:grant-type:token-exchange"
    )


class InstanceAccessControlAttributeConfigurationStatus(StrEnum):
    ENABLED = "ENABLED"
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_FAILED = "CREATION_FAILED"


class InstanceStatus(StrEnum):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    ACTIVE = "ACTIVE"


class JwksRetrievalOption(StrEnum):
    OPEN_ID_DISCOVERY = "OPEN_ID_DISCOVERY"


class PrincipalType(StrEnum):
    USER = "USER"
    GROUP = "GROUP"


class ProvisionTargetType(StrEnum):
    AWS_ACCOUNT = "AWS_ACCOUNT"
    ALL_PROVISIONED_ACCOUNTS = "ALL_PROVISIONED_ACCOUNTS"


class ProvisioningStatus(StrEnum):
    LATEST_PERMISSION_SET_PROVISIONED = "LATEST_PERMISSION_SET_PROVISIONED"
    LATEST_PERMISSION_SET_NOT_PROVISIONED = "LATEST_PERMISSION_SET_NOT_PROVISIONED"


class SignInOrigin(StrEnum):
    IDENTITY_CENTER = "IDENTITY_CENTER"
    APPLICATION = "APPLICATION"


class StatusValues(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class TargetType(StrEnum):
    AWS_ACCOUNT = "AWS_ACCOUNT"


class TrustedTokenIssuerType(StrEnum):
    OIDC_JWT = "OIDC_JWT"


class AccessDeniedException(ServiceException):
    """You do not have sufficient access to perform this action."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """Occurs when a conflict with a previous successful write is detected.
    This generally occurs when the previous write did not have time to
    propagate to the host serving the current request. A retry (with
    appropriate backoff logic) is the recommended response to this
    exception.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class InternalServerException(ServiceException):
    """The request processing has failed because of an unknown error,
    exception, or failure with an internal server.
    """

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """Indicates that a requested resource is not found."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ServiceQuotaExceededException(ServiceException):
    """Indicates that the principal has crossed the permitted number of
    resources that can be created.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """Indicates that the principal has crossed the throttling limits of the
    API operations.
    """

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class ValidationException(ServiceException):
    """The request failed because it contains a syntax error."""

    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400


AccessControlAttributeValueSourceList = List[AccessControlAttributeValueSource]


class AccessControlAttributeValue(TypedDict, total=False):
    """The value used for mapping a specified attribute to an identity source.
    For more information, see `Attribute
    mappings <https://docs.aws.amazon.com/singlesignon/latest/userguide/attributemappingsconcept.html>`__
    in the *IAM Identity Center User Guide*.
    """

    Source: AccessControlAttributeValueSourceList


class AccessControlAttribute(TypedDict, total=False):
    """These are IAM Identity Center identity store attributes that you can
    configure for use in attributes-based access control (ABAC). You can
    create permissions policies that determine who can access your Amazon
    Web Services resources based upon the configured attribute values. When
    you enable ABAC and specify ``AccessControlAttributes``, IAM Identity
    Center passes the attribute values of the authenticated user into IAM
    for use in policy evaluation.
    """

    Key: AccessControlAttributeKey
    Value: AccessControlAttributeValue


AccessControlAttributeList = List[AccessControlAttribute]


class AccountAssignment(TypedDict, total=False):
    """The assignment that indicates a principal's limited access to a
    specified Amazon Web Services account with a specified permission set.

    The term *principal* here refers to a user or group that is defined in
    IAM Identity Center.
    """

    AccountId: Optional[AccountId]
    PermissionSetArn: Optional[PermissionSetArn]
    PrincipalType: Optional[PrincipalType]
    PrincipalId: Optional[PrincipalId]


class AccountAssignmentForPrincipal(TypedDict, total=False):
    """A structure that describes an assignment of an Amazon Web Services
    account to a principal and the permissions that principal has in the
    account.
    """

    AccountId: Optional[AccountId]
    PermissionSetArn: Optional[PermissionSetArn]
    PrincipalId: Optional[PrincipalId]
    PrincipalType: Optional[PrincipalType]


AccountAssignmentList = List[AccountAssignment]
AccountAssignmentListForPrincipal = List[AccountAssignmentForPrincipal]
Date = datetime


class AccountAssignmentOperationStatus(TypedDict, total=False):
    """The status of the creation or deletion operation of an assignment that a
    principal needs to access an account.
    """

    Status: Optional[StatusValues]
    RequestId: Optional[UUId]
    FailureReason: Optional[Reason]
    TargetId: Optional[TargetId]
    TargetType: Optional[TargetType]
    PermissionSetArn: Optional[PermissionSetArn]
    PrincipalType: Optional[PrincipalType]
    PrincipalId: Optional[PrincipalId]
    CreatedDate: Optional[Date]


class AccountAssignmentOperationStatusMetadata(TypedDict, total=False):
    """Provides information about the AccountAssignment creation request."""

    Status: Optional[StatusValues]
    RequestId: Optional[UUId]
    CreatedDate: Optional[Date]


AccountAssignmentOperationStatusList = List[AccountAssignmentOperationStatusMetadata]
AccountList = List[AccountId]


class ActorPolicyDocument(TypedDict, total=False):
    pass


class SignInOptions(TypedDict, total=False):
    """A structure that describes the sign-in options for an application
    portal.
    """

    Origin: SignInOrigin
    ApplicationUrl: Optional[ApplicationUrl]


class PortalOptions(TypedDict, total=False):
    """A structure that describes the options for the access portal associated
    with an application.
    """

    SignInOptions: Optional[SignInOptions]
    Visibility: Optional[ApplicationVisibility]


class Application(TypedDict, total=False):
    """A structure that describes an application that uses IAM Identity Center
    for access management.
    """

    ApplicationArn: Optional[ApplicationArn]
    ApplicationProviderArn: Optional[ApplicationProviderArn]
    Name: Optional[NameType]
    ApplicationAccount: Optional[AccountId]
    InstanceArn: Optional[InstanceArn]
    Status: Optional[ApplicationStatus]
    PortalOptions: Optional[PortalOptions]
    Description: Optional[Description]
    CreatedDate: Optional[Date]


class ApplicationAssignment(TypedDict, total=False):
    """A structure that describes an assignment of a principal to an
    application.
    """

    ApplicationArn: ApplicationArn
    PrincipalId: PrincipalId
    PrincipalType: PrincipalType


class ApplicationAssignmentForPrincipal(TypedDict, total=False):
    """A structure that describes an application to which a principal is
    assigned.
    """

    ApplicationArn: Optional[ApplicationArn]
    PrincipalId: Optional[PrincipalId]
    PrincipalType: Optional[PrincipalType]


ApplicationAssignmentListForPrincipal = List[ApplicationAssignmentForPrincipal]
ApplicationAssignmentsList = List[ApplicationAssignment]
ApplicationList = List[Application]


class ResourceServerScopeDetails(TypedDict, total=False):
    """A structure that describes details for an IAM Identity Center access
    scope that is associated with a resource server.
    """

    LongDescription: Optional[Description]
    DetailedTitle: Optional[Description]


ResourceServerScopes = Dict[ResourceServerScope, ResourceServerScopeDetails]


class ResourceServerConfig(TypedDict, total=False):
    """A structure that describes the configuration of a resource server."""

    Scopes: Optional[ResourceServerScopes]


class DisplayData(TypedDict, total=False):
    """A structure that describes how the portal represents an application
    provider.
    """

    DisplayName: Optional[Name]
    IconUrl: Optional[IconUrl]
    Description: Optional[Description]


class ApplicationProvider(TypedDict, total=False):
    """A structure that describes a provider that can be used to connect an
    Amazon Web Services managed application or customer managed application
    to IAM Identity Center.
    """

    ApplicationProviderArn: ApplicationProviderArn
    FederationProtocol: Optional[FederationProtocol]
    DisplayData: Optional[DisplayData]
    ResourceServerConfig: Optional[ResourceServerConfig]


ApplicationProviderList = List[ApplicationProvider]


class CustomerManagedPolicyReference(TypedDict, total=False):
    """Specifies the name and path of a customer managed policy. You must have
    an IAM policy that matches the name and path in each Amazon Web Services
    account where you want to deploy your permission set.
    """

    Name: ManagedPolicyName
    Path: Optional[ManagedPolicyPath]


class AttachCustomerManagedPolicyReferenceToPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    CustomerManagedPolicyReference: CustomerManagedPolicyReference


class AttachCustomerManagedPolicyReferenceToPermissionSetResponse(TypedDict, total=False):
    pass


class AttachManagedPolicyToPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    ManagedPolicyArn: ManagedPolicyArn


class AttachManagedPolicyToPermissionSetResponse(TypedDict, total=False):
    pass


class AttachedManagedPolicy(TypedDict, total=False):
    """A structure that stores a list of managed policy ARNs that describe the
    associated Amazon Web Services managed policy.
    """

    Name: Optional[Name]
    Arn: Optional[ManagedPolicyArn]


AttachedManagedPolicyList = List[AttachedManagedPolicy]


class IamAuthenticationMethod(TypedDict, total=False):
    """A structure that describes details for authentication that uses IAM."""

    ActorPolicy: ActorPolicyDocument


class AuthenticationMethod(TypedDict, total=False):
    """A structure that describes an authentication method that can be used by
    an application.
    """

    Iam: Optional[IamAuthenticationMethod]


class AuthenticationMethodItem(TypedDict, total=False):
    """A structure that describes an authentication method and its type."""

    AuthenticationMethodType: Optional[AuthenticationMethodType]
    AuthenticationMethod: Optional[AuthenticationMethod]


AuthenticationMethods = List[AuthenticationMethodItem]
RedirectUris = List[URI]


class AuthorizationCodeGrant(TypedDict, total=False):
    """A structure that defines configuration settings for an application that
    supports the OAuth 2.0 Authorization Code Grant.
    """

    RedirectUris: Optional[RedirectUris]


TokenIssuerAudiences = List[TokenIssuerAudience]


class AuthorizedTokenIssuer(TypedDict, total=False):
    """A structure that describes a trusted token issuer and associates it with
    a set of authorized audiences.
    """

    TrustedTokenIssuerArn: Optional[TrustedTokenIssuerArn]
    AuthorizedAudiences: Optional[TokenIssuerAudiences]


AuthorizedTokenIssuers = List[AuthorizedTokenIssuer]


class CreateAccountAssignmentRequest(ServiceRequest):
    InstanceArn: InstanceArn
    TargetId: TargetId
    TargetType: TargetType
    PermissionSetArn: PermissionSetArn
    PrincipalType: PrincipalType
    PrincipalId: PrincipalId


class CreateAccountAssignmentResponse(TypedDict, total=False):
    AccountAssignmentCreationStatus: Optional[AccountAssignmentOperationStatus]


class CreateApplicationAssignmentRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    PrincipalId: PrincipalId
    PrincipalType: PrincipalType


class CreateApplicationAssignmentResponse(TypedDict, total=False):
    pass


class Tag(TypedDict, total=False):
    """A set of key-value pairs that are used to manage the resource. Tags can
    only be applied to permission sets and cannot be applied to
    corresponding roles that IAM Identity Center creates in Amazon Web
    Services accounts.
    """

    Key: TagKey
    Value: TagValue


TagList = List[Tag]


class CreateApplicationRequest(ServiceRequest):
    InstanceArn: InstanceArn
    ApplicationProviderArn: ApplicationProviderArn
    Name: ApplicationNameType
    Description: Optional[Description]
    PortalOptions: Optional[PortalOptions]
    Tags: Optional[TagList]
    Status: Optional[ApplicationStatus]
    ClientToken: Optional[ClientToken]


class CreateApplicationResponse(TypedDict, total=False):
    ApplicationArn: Optional[ApplicationArn]


class InstanceAccessControlAttributeConfiguration(TypedDict, total=False):
    """Specifies the attributes to add to your attribute-based access control
    (ABAC) configuration.
    """

    AccessControlAttributes: AccessControlAttributeList


class CreateInstanceAccessControlAttributeConfigurationRequest(ServiceRequest):
    InstanceArn: InstanceArn
    InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfiguration


class CreateInstanceAccessControlAttributeConfigurationResponse(TypedDict, total=False):
    pass


class CreateInstanceRequest(ServiceRequest):
    Name: Optional[NameType]
    ClientToken: Optional[ClientToken]
    Tags: Optional[TagList]


class CreateInstanceResponse(TypedDict, total=False):
    InstanceArn: Optional[InstanceArn]


class CreatePermissionSetRequest(ServiceRequest):
    Name: PermissionSetName
    Description: Optional[PermissionSetDescription]
    InstanceArn: InstanceArn
    SessionDuration: Optional[Duration]
    RelayState: Optional[RelayState]
    Tags: Optional[TagList]


class PermissionSet(TypedDict, total=False):
    """An entity that contains IAM policies."""

    Name: Optional[PermissionSetName]
    PermissionSetArn: Optional[PermissionSetArn]
    Description: Optional[PermissionSetDescription]
    CreatedDate: Optional[Date]
    SessionDuration: Optional[Duration]
    RelayState: Optional[RelayState]


class CreatePermissionSetResponse(TypedDict, total=False):
    PermissionSet: Optional[PermissionSet]


class OidcJwtConfiguration(TypedDict, total=False):
    """A structure that describes configuration settings for a trusted token
    issuer that supports OpenID Connect (OIDC) and JSON Web Tokens (JWTs).
    """

    IssuerUrl: TrustedTokenIssuerUrl
    ClaimAttributePath: ClaimAttributePath
    IdentityStoreAttributePath: JMESPath
    JwksRetrievalOption: JwksRetrievalOption


class TrustedTokenIssuerConfiguration(TypedDict, total=False):
    """A structure that describes the configuration of a trusted token issuer.
    The structure and available settings are determined by the type of the
    trusted token issuer.
    """

    OidcJwtConfiguration: Optional[OidcJwtConfiguration]


class CreateTrustedTokenIssuerRequest(ServiceRequest):
    InstanceArn: InstanceArn
    Name: TrustedTokenIssuerName
    TrustedTokenIssuerType: TrustedTokenIssuerType
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfiguration
    ClientToken: Optional[ClientToken]
    Tags: Optional[TagList]


class CreateTrustedTokenIssuerResponse(TypedDict, total=False):
    TrustedTokenIssuerArn: Optional[TrustedTokenIssuerArn]


CustomerManagedPolicyReferenceList = List[CustomerManagedPolicyReference]


class DeleteAccountAssignmentRequest(ServiceRequest):
    InstanceArn: InstanceArn
    TargetId: TargetId
    TargetType: TargetType
    PermissionSetArn: PermissionSetArn
    PrincipalType: PrincipalType
    PrincipalId: PrincipalId


class DeleteAccountAssignmentResponse(TypedDict, total=False):
    AccountAssignmentDeletionStatus: Optional[AccountAssignmentOperationStatus]


class DeleteApplicationAccessScopeRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    Scope: Scope


class DeleteApplicationAssignmentRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    PrincipalId: PrincipalId
    PrincipalType: PrincipalType


class DeleteApplicationAssignmentResponse(TypedDict, total=False):
    pass


class DeleteApplicationAuthenticationMethodRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    AuthenticationMethodType: AuthenticationMethodType


class DeleteApplicationGrantRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    GrantType: GrantType


class DeleteApplicationRequest(ServiceRequest):
    ApplicationArn: ApplicationArn


class DeleteApplicationResponse(TypedDict, total=False):
    pass


class DeleteInlinePolicyFromPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn


class DeleteInlinePolicyFromPermissionSetResponse(TypedDict, total=False):
    pass


class DeleteInstanceAccessControlAttributeConfigurationRequest(ServiceRequest):
    InstanceArn: InstanceArn


class DeleteInstanceAccessControlAttributeConfigurationResponse(TypedDict, total=False):
    pass


class DeleteInstanceRequest(ServiceRequest):
    InstanceArn: InstanceArn


class DeleteInstanceResponse(TypedDict, total=False):
    pass


class DeletePermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn


class DeletePermissionSetResponse(TypedDict, total=False):
    pass


class DeletePermissionsBoundaryFromPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn


class DeletePermissionsBoundaryFromPermissionSetResponse(TypedDict, total=False):
    pass


class DeleteTrustedTokenIssuerRequest(ServiceRequest):
    TrustedTokenIssuerArn: TrustedTokenIssuerArn


class DeleteTrustedTokenIssuerResponse(TypedDict, total=False):
    pass


class DescribeAccountAssignmentCreationStatusRequest(ServiceRequest):
    InstanceArn: InstanceArn
    AccountAssignmentCreationRequestId: UUId


class DescribeAccountAssignmentCreationStatusResponse(TypedDict, total=False):
    AccountAssignmentCreationStatus: Optional[AccountAssignmentOperationStatus]


class DescribeAccountAssignmentDeletionStatusRequest(ServiceRequest):
    InstanceArn: InstanceArn
    AccountAssignmentDeletionRequestId: UUId


class DescribeAccountAssignmentDeletionStatusResponse(TypedDict, total=False):
    AccountAssignmentDeletionStatus: Optional[AccountAssignmentOperationStatus]


class DescribeApplicationAssignmentRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    PrincipalId: PrincipalId
    PrincipalType: PrincipalType


class DescribeApplicationAssignmentResponse(TypedDict, total=False):
    PrincipalType: Optional[PrincipalType]
    PrincipalId: Optional[PrincipalId]
    ApplicationArn: Optional[ApplicationArn]


class DescribeApplicationProviderRequest(ServiceRequest):
    ApplicationProviderArn: ApplicationProviderArn


class DescribeApplicationProviderResponse(TypedDict, total=False):
    ApplicationProviderArn: ApplicationProviderArn
    FederationProtocol: Optional[FederationProtocol]
    DisplayData: Optional[DisplayData]
    ResourceServerConfig: Optional[ResourceServerConfig]


class DescribeApplicationRequest(ServiceRequest):
    ApplicationArn: ApplicationArn


class DescribeApplicationResponse(TypedDict, total=False):
    ApplicationArn: Optional[ApplicationArn]
    ApplicationProviderArn: Optional[ApplicationProviderArn]
    Name: Optional[NameType]
    ApplicationAccount: Optional[AccountId]
    InstanceArn: Optional[InstanceArn]
    Status: Optional[ApplicationStatus]
    PortalOptions: Optional[PortalOptions]
    Description: Optional[Description]
    CreatedDate: Optional[Date]


class DescribeInstanceAccessControlAttributeConfigurationRequest(ServiceRequest):
    InstanceArn: InstanceArn


class DescribeInstanceAccessControlAttributeConfigurationResponse(TypedDict, total=False):
    Status: Optional[InstanceAccessControlAttributeConfigurationStatus]
    StatusReason: Optional[InstanceAccessControlAttributeConfigurationStatusReason]
    InstanceAccessControlAttributeConfiguration: Optional[
        InstanceAccessControlAttributeConfiguration
    ]


class DescribeInstanceRequest(ServiceRequest):
    InstanceArn: InstanceArn


class DescribeInstanceResponse(TypedDict, total=False):
    InstanceArn: Optional[InstanceArn]
    IdentityStoreId: Optional[Id]
    OwnerAccountId: Optional[AccountId]
    Name: Optional[NameType]
    CreatedDate: Optional[Date]
    Status: Optional[InstanceStatus]


class DescribePermissionSetProvisioningStatusRequest(ServiceRequest):
    InstanceArn: InstanceArn
    ProvisionPermissionSetRequestId: UUId


class PermissionSetProvisioningStatus(TypedDict, total=False):
    """A structure that is used to provide the status of the provisioning
    operation for a specified permission set.
    """

    Status: Optional[StatusValues]
    RequestId: Optional[UUId]
    AccountId: Optional[AccountId]
    PermissionSetArn: Optional[PermissionSetArn]
    FailureReason: Optional[Reason]
    CreatedDate: Optional[Date]


class DescribePermissionSetProvisioningStatusResponse(TypedDict, total=False):
    PermissionSetProvisioningStatus: Optional[PermissionSetProvisioningStatus]


class DescribePermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn


class DescribePermissionSetResponse(TypedDict, total=False):
    PermissionSet: Optional[PermissionSet]


class DescribeTrustedTokenIssuerRequest(ServiceRequest):
    TrustedTokenIssuerArn: TrustedTokenIssuerArn


class DescribeTrustedTokenIssuerResponse(TypedDict, total=False):
    TrustedTokenIssuerArn: Optional[TrustedTokenIssuerArn]
    Name: Optional[TrustedTokenIssuerName]
    TrustedTokenIssuerType: Optional[TrustedTokenIssuerType]
    TrustedTokenIssuerConfiguration: Optional[TrustedTokenIssuerConfiguration]


class DetachCustomerManagedPolicyReferenceFromPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    CustomerManagedPolicyReference: CustomerManagedPolicyReference


class DetachCustomerManagedPolicyReferenceFromPermissionSetResponse(TypedDict, total=False):
    pass


class DetachManagedPolicyFromPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    ManagedPolicyArn: ManagedPolicyArn


class DetachManagedPolicyFromPermissionSetResponse(TypedDict, total=False):
    pass


class GetApplicationAccessScopeRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    Scope: Scope


ScopeTargets = List[ScopeTarget]


class GetApplicationAccessScopeResponse(TypedDict, total=False):
    Scope: Scope
    AuthorizedTargets: Optional[ScopeTargets]


class GetApplicationAssignmentConfigurationRequest(ServiceRequest):
    ApplicationArn: ApplicationArn


class GetApplicationAssignmentConfigurationResponse(TypedDict, total=False):
    AssignmentRequired: AssignmentRequired


class GetApplicationAuthenticationMethodRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    AuthenticationMethodType: AuthenticationMethodType


class GetApplicationAuthenticationMethodResponse(TypedDict, total=False):
    AuthenticationMethod: Optional[AuthenticationMethod]


class GetApplicationGrantRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    GrantType: GrantType


class TokenExchangeGrant(TypedDict, total=False):
    """A structure that defines configuration settings for an application that
    supports the OAuth 2.0 Token Exchange Grant. For more information, see
    `RFC 8693 <https://datatracker.ietf.org/doc/html/rfc8693>`__.
    """

    pass


class RefreshTokenGrant(TypedDict, total=False):
    """A structure that defines configuration settings for an application that
    supports the OAuth 2.0 Refresh Token Grant. For more, see `RFC
    6749 <https://datatracker.ietf.org/doc/html/rfc6749#section-1.5>`__.
    """

    pass


class JwtBearerGrant(TypedDict, total=False):
    """A structure that defines configuration settings for an application that
    supports the JWT Bearer Token Authorization Grant. The
    ``AuthorizedAudience`` field is the aud claim. For more information, see
    `RFC 7523 <https://datatracker.ietf.org/doc/html/rfc7523>`__.
    """

    AuthorizedTokenIssuers: Optional[AuthorizedTokenIssuers]


class Grant(TypedDict, total=False):
    """The Grant union represents the set of possible configuration options for
    the selected grant type. Exactly one member of the union must be
    specified, and must match the grant type selected.
    """

    AuthorizationCode: Optional[AuthorizationCodeGrant]
    JwtBearer: Optional[JwtBearerGrant]
    RefreshToken: Optional[RefreshTokenGrant]
    TokenExchange: Optional[TokenExchangeGrant]


class GetApplicationGrantResponse(TypedDict, total=False):
    Grant: Grant


class GetInlinePolicyForPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn


class GetInlinePolicyForPermissionSetResponse(TypedDict, total=False):
    InlinePolicy: Optional[PermissionSetPolicyDocument]


class GetPermissionsBoundaryForPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn


class PermissionsBoundary(TypedDict, total=False):
    """Specifies the configuration of the Amazon Web Services managed or
    customer managed policy that you want to set as a permissions boundary.
    Specify either ``CustomerManagedPolicyReference`` to use the name and
    path of a customer managed policy, or ``ManagedPolicyArn`` to use the
    ARN of an Amazon Web Services managed policy. A permissions boundary
    represents the maximum permissions that any policy can grant your role.
    For more information, see `Permissions boundaries for IAM
    entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide*.

    Policies used as permissions boundaries don't provide permissions. You
    must also attach an IAM policy to the role. To learn how the effective
    permissions for a role are evaluated, see `IAM JSON policy evaluation
    logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`__
    in the *IAM User Guide*.
    """

    CustomerManagedPolicyReference: Optional[CustomerManagedPolicyReference]
    ManagedPolicyArn: Optional[ManagedPolicyArn]


class GetPermissionsBoundaryForPermissionSetResponse(TypedDict, total=False):
    PermissionsBoundary: Optional[PermissionsBoundary]


class GrantItem(TypedDict, total=False):
    """A structure that defines a single grant and its configuration."""

    GrantType: GrantType
    Grant: Grant


Grants = List[GrantItem]


class InstanceMetadata(TypedDict, total=False):
    """Provides information about the IAM Identity Center instance."""

    InstanceArn: Optional[InstanceArn]
    IdentityStoreId: Optional[Id]
    OwnerAccountId: Optional[AccountId]
    Name: Optional[NameType]
    CreatedDate: Optional[Date]
    Status: Optional[InstanceStatus]


InstanceList = List[InstanceMetadata]


class OperationStatusFilter(TypedDict, total=False):
    """Filters the operation status list based on the passed attribute value."""

    Status: Optional[StatusValues]


class ListAccountAssignmentCreationStatusRequest(ServiceRequest):
    InstanceArn: InstanceArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]
    Filter: Optional[OperationStatusFilter]


class ListAccountAssignmentCreationStatusResponse(TypedDict, total=False):
    AccountAssignmentsCreationStatus: Optional[AccountAssignmentOperationStatusList]
    NextToken: Optional[Token]


class ListAccountAssignmentDeletionStatusRequest(ServiceRequest):
    InstanceArn: InstanceArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]
    Filter: Optional[OperationStatusFilter]


class ListAccountAssignmentDeletionStatusResponse(TypedDict, total=False):
    AccountAssignmentsDeletionStatus: Optional[AccountAssignmentOperationStatusList]
    NextToken: Optional[Token]


class ListAccountAssignmentsFilter(TypedDict, total=False):
    """A structure that describes a filter for account assignments."""

    AccountId: Optional[AccountId]


class ListAccountAssignmentsForPrincipalRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PrincipalId: PrincipalId
    PrincipalType: PrincipalType
    Filter: Optional[ListAccountAssignmentsFilter]
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]


class ListAccountAssignmentsForPrincipalResponse(TypedDict, total=False):
    AccountAssignments: Optional[AccountAssignmentListForPrincipal]
    NextToken: Optional[Token]


class ListAccountAssignmentsRequest(ServiceRequest):
    InstanceArn: InstanceArn
    AccountId: TargetId
    PermissionSetArn: PermissionSetArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListAccountAssignmentsResponse(TypedDict, total=False):
    AccountAssignments: Optional[AccountAssignmentList]
    NextToken: Optional[Token]


class ListAccountsForProvisionedPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    ProvisioningStatus: Optional[ProvisioningStatus]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListAccountsForProvisionedPermissionSetResponse(TypedDict, total=False):
    AccountIds: Optional[AccountList]
    NextToken: Optional[Token]


class ListApplicationAccessScopesRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    MaxResults: Optional[ListApplicationAccessScopesRequestMaxResultsInteger]
    NextToken: Optional[Token]


class ScopeDetails(TypedDict, total=False):
    """A structure that describes an IAM Identity Center access scope and its
    authorized targets.
    """

    Scope: Scope
    AuthorizedTargets: Optional[ScopeTargets]


Scopes = List[ScopeDetails]


class ListApplicationAccessScopesResponse(TypedDict, total=False):
    Scopes: Scopes
    NextToken: Optional[Token]


class ListApplicationAssignmentsFilter(TypedDict, total=False):
    """A structure that describes a filter for application assignments."""

    ApplicationArn: Optional[ApplicationArn]


class ListApplicationAssignmentsForPrincipalRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PrincipalId: PrincipalId
    PrincipalType: PrincipalType
    Filter: Optional[ListApplicationAssignmentsFilter]
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]


class ListApplicationAssignmentsForPrincipalResponse(TypedDict, total=False):
    ApplicationAssignments: Optional[ApplicationAssignmentListForPrincipal]
    NextToken: Optional[Token]


class ListApplicationAssignmentsRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListApplicationAssignmentsResponse(TypedDict, total=False):
    ApplicationAssignments: Optional[ApplicationAssignmentsList]
    NextToken: Optional[Token]


class ListApplicationAuthenticationMethodsRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    NextToken: Optional[Token]


class ListApplicationAuthenticationMethodsResponse(TypedDict, total=False):
    AuthenticationMethods: Optional[AuthenticationMethods]
    NextToken: Optional[Token]


class ListApplicationGrantsRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    NextToken: Optional[Token]


class ListApplicationGrantsResponse(TypedDict, total=False):
    Grants: Grants
    NextToken: Optional[Token]


class ListApplicationProvidersRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListApplicationProvidersResponse(TypedDict, total=False):
    ApplicationProviders: Optional[ApplicationProviderList]
    NextToken: Optional[Token]


class ListApplicationsFilter(TypedDict, total=False):
    """A structure that describes a filter for applications."""

    ApplicationAccount: Optional[AccountId]
    ApplicationProvider: Optional[ApplicationProviderArn]


class ListApplicationsRequest(ServiceRequest):
    InstanceArn: InstanceArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]
    Filter: Optional[ListApplicationsFilter]


class ListApplicationsResponse(TypedDict, total=False):
    Applications: Optional[ApplicationList]
    NextToken: Optional[Token]


class ListCustomerManagedPolicyReferencesInPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListCustomerManagedPolicyReferencesInPermissionSetResponse(TypedDict, total=False):
    CustomerManagedPolicyReferences: Optional[CustomerManagedPolicyReferenceList]
    NextToken: Optional[Token]


class ListInstancesRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListInstancesResponse(TypedDict, total=False):
    Instances: Optional[InstanceList]
    NextToken: Optional[Token]


class ListManagedPoliciesInPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class ListManagedPoliciesInPermissionSetResponse(TypedDict, total=False):
    AttachedManagedPolicies: Optional[AttachedManagedPolicyList]
    NextToken: Optional[Token]


class ListPermissionSetProvisioningStatusRequest(ServiceRequest):
    InstanceArn: InstanceArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]
    Filter: Optional[OperationStatusFilter]


class PermissionSetProvisioningStatusMetadata(TypedDict, total=False):
    """Provides information about the permission set provisioning status."""

    Status: Optional[StatusValues]
    RequestId: Optional[UUId]
    CreatedDate: Optional[Date]


PermissionSetProvisioningStatusList = List[PermissionSetProvisioningStatusMetadata]


class ListPermissionSetProvisioningStatusResponse(TypedDict, total=False):
    PermissionSetsProvisioningStatus: Optional[PermissionSetProvisioningStatusList]
    NextToken: Optional[Token]


class ListPermissionSetsProvisionedToAccountRequest(ServiceRequest):
    InstanceArn: InstanceArn
    AccountId: AccountId
    ProvisioningStatus: Optional[ProvisioningStatus]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


PermissionSetList = List[PermissionSetArn]


class ListPermissionSetsProvisionedToAccountResponse(TypedDict, total=False):
    NextToken: Optional[Token]
    PermissionSets: Optional[PermissionSetList]


class ListPermissionSetsRequest(ServiceRequest):
    InstanceArn: InstanceArn
    NextToken: Optional[Token]
    MaxResults: Optional[MaxResults]


class ListPermissionSetsResponse(TypedDict, total=False):
    PermissionSets: Optional[PermissionSetList]
    NextToken: Optional[Token]


class ListTagsForResourceRequest(ServiceRequest):
    InstanceArn: Optional[InstanceArn]
    ResourceArn: TaggableResourceArn
    NextToken: Optional[Token]


class ListTagsForResourceResponse(TypedDict, total=False):
    Tags: Optional[TagList]
    NextToken: Optional[Token]


class ListTrustedTokenIssuersRequest(ServiceRequest):
    InstanceArn: InstanceArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[Token]


class TrustedTokenIssuerMetadata(TypedDict, total=False):
    """A structure that describes a trusted token issuer."""

    TrustedTokenIssuerArn: Optional[TrustedTokenIssuerArn]
    Name: Optional[TrustedTokenIssuerName]
    TrustedTokenIssuerType: Optional[TrustedTokenIssuerType]


TrustedTokenIssuerList = List[TrustedTokenIssuerMetadata]


class ListTrustedTokenIssuersResponse(TypedDict, total=False):
    TrustedTokenIssuers: Optional[TrustedTokenIssuerList]
    NextToken: Optional[Token]


class OidcJwtUpdateConfiguration(TypedDict, total=False):
    """A structure that describes updated configuration settings for a trusted
    token issuer that supports OpenID Connect (OIDC) and JSON Web Tokens
    (JWTs).
    """

    ClaimAttributePath: Optional[ClaimAttributePath]
    IdentityStoreAttributePath: Optional[JMESPath]
    JwksRetrievalOption: Optional[JwksRetrievalOption]


class ProvisionPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    TargetId: Optional[TargetId]
    TargetType: ProvisionTargetType


class ProvisionPermissionSetResponse(TypedDict, total=False):
    PermissionSetProvisioningStatus: Optional[PermissionSetProvisioningStatus]


class PutApplicationAccessScopeRequest(ServiceRequest):
    Scope: Scope
    AuthorizedTargets: Optional[ScopeTargets]
    ApplicationArn: ApplicationArn


class PutApplicationAssignmentConfigurationRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    AssignmentRequired: AssignmentRequired


class PutApplicationAssignmentConfigurationResponse(TypedDict, total=False):
    pass


class PutApplicationAuthenticationMethodRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    AuthenticationMethodType: AuthenticationMethodType
    AuthenticationMethod: AuthenticationMethod


class PutApplicationGrantRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    GrantType: GrantType
    Grant: Grant


class PutInlinePolicyToPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    InlinePolicy: PermissionSetPolicyDocument


class PutInlinePolicyToPermissionSetResponse(TypedDict, total=False):
    pass


class PutPermissionsBoundaryToPermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    PermissionsBoundary: PermissionsBoundary


class PutPermissionsBoundaryToPermissionSetResponse(TypedDict, total=False):
    pass


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    InstanceArn: Optional[InstanceArn]
    ResourceArn: TaggableResourceArn
    Tags: TagList


class TagResourceResponse(TypedDict, total=False):
    pass


class TrustedTokenIssuerUpdateConfiguration(TypedDict, total=False):
    """A structure that contains details to be updated for a trusted token
    issuer configuration. The structure and settings that you can include
    depend on the type of the trusted token issuer being updated.
    """

    OidcJwtConfiguration: Optional[OidcJwtUpdateConfiguration]


class UntagResourceRequest(ServiceRequest):
    InstanceArn: Optional[InstanceArn]
    ResourceArn: TaggableResourceArn
    TagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateApplicationPortalOptions(TypedDict, total=False):
    """A structure that describes the options for the access portal associated
    with an application that can be updated.
    """

    SignInOptions: Optional[SignInOptions]


class UpdateApplicationRequest(ServiceRequest):
    ApplicationArn: ApplicationArn
    Name: Optional[ApplicationNameType]
    Description: Optional[Description]
    Status: Optional[ApplicationStatus]
    PortalOptions: Optional[UpdateApplicationPortalOptions]


class UpdateApplicationResponse(TypedDict, total=False):
    pass


class UpdateInstanceAccessControlAttributeConfigurationRequest(ServiceRequest):
    InstanceArn: InstanceArn
    InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfiguration


class UpdateInstanceAccessControlAttributeConfigurationResponse(TypedDict, total=False):
    pass


class UpdateInstanceRequest(ServiceRequest):
    Name: NameType
    InstanceArn: InstanceArn


class UpdateInstanceResponse(TypedDict, total=False):
    pass


class UpdatePermissionSetRequest(ServiceRequest):
    InstanceArn: InstanceArn
    PermissionSetArn: PermissionSetArn
    Description: Optional[PermissionSetDescription]
    SessionDuration: Optional[Duration]
    RelayState: Optional[RelayState]


class UpdatePermissionSetResponse(TypedDict, total=False):
    pass


class UpdateTrustedTokenIssuerRequest(ServiceRequest):
    TrustedTokenIssuerArn: TrustedTokenIssuerArn
    Name: Optional[TrustedTokenIssuerName]
    TrustedTokenIssuerConfiguration: Optional[TrustedTokenIssuerUpdateConfiguration]


class UpdateTrustedTokenIssuerResponse(TypedDict, total=False):
    pass


class SsoAdminApi:
    service = "sso-admin"
    version = "2020-07-20"

    @handler("AttachCustomerManagedPolicyReferenceToPermissionSet")
    def attach_customer_managed_policy_reference_to_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        customer_managed_policy_reference: CustomerManagedPolicyReference,
        **kwargs,
    ) -> AttachCustomerManagedPolicyReferenceToPermissionSetResponse:
        """Attaches the specified customer managed policy to the specified
        PermissionSet.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the ``PermissionSet``.
        :param customer_managed_policy_reference: Specifies the name and path of a customer managed policy.
        :returns: AttachCustomerManagedPolicyReferenceToPermissionSetResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("AttachManagedPolicyToPermissionSet")
    def attach_managed_policy_to_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        managed_policy_arn: ManagedPolicyArn,
        **kwargs,
    ) -> AttachManagedPolicyToPermissionSetResponse:
        """Attaches an Amazon Web Services managed policy ARN to a permission set.

        If the permission set is already referenced by one or more account
        assignments, you will need to call ``ProvisionPermissionSet`` after this
        operation. Calling ``ProvisionPermissionSet`` applies the corresponding
        IAM policy updates to all assigned accounts.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the PermissionSet that the managed policy should be attached
        to.
        :param managed_policy_arn: The Amazon Web Services managed policy ARN to be attached to a
        permission set.
        :returns: AttachManagedPolicyToPermissionSetResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateAccountAssignment")
    def create_account_assignment(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        target_id: TargetId,
        target_type: TargetType,
        permission_set_arn: PermissionSetArn,
        principal_type: PrincipalType,
        principal_id: PrincipalId,
        **kwargs,
    ) -> CreateAccountAssignmentResponse:
        """Assigns access to a principal for a specified Amazon Web Services
        account using a specified permission set.

        The term *principal* here refers to a user or group that is defined in
        IAM Identity Center.

        As part of a successful ``CreateAccountAssignment`` call, the specified
        permission set will automatically be provisioned to the account in the
        form of an IAM policy. That policy is attached to the IAM role created
        in IAM Identity Center. If the permission set is subsequently updated,
        the corresponding IAM policies attached to roles in your accounts will
        not be updated automatically. In this case, you must call
        ``ProvisionPermissionSet`` to make these updates.

        After a successful response, call
        ``DescribeAccountAssignmentCreationStatus`` to describe the status of an
        assignment creation request.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param target_id: TargetID is an Amazon Web Services account identifier, (For example,
        123456789012).
        :param target_type: The entity type for which the assignment will be created.
        :param permission_set_arn: The ARN of the permission set that the admin wants to grant the
        principal access to.
        :param principal_type: The entity type for which the assignment will be created.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or
        group.
        :returns: CreateAccountAssignmentResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateApplication")
    def create_application(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        application_provider_arn: ApplicationProviderArn,
        name: ApplicationNameType,
        description: Description | None = None,
        portal_options: PortalOptions | None = None,
        tags: TagList | None = None,
        status: ApplicationStatus | None = None,
        client_token: ClientToken | None = None,
        **kwargs,
    ) -> CreateApplicationResponse:
        """Creates an OAuth 2.0 customer managed application in IAM Identity Center
        for the given application provider.

        This API does not support creating SAML 2.0 customer managed
        applications or Amazon Web Services managed applications. To learn how
        to create an Amazon Web Services managed application, see the
        application user guide. You can create a SAML 2.0 customer managed
        application in the Amazon Web Services Management Console only. See
        `Setting up customer managed SAML 2.0
        applications <https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html>`__.
        For more information on these application types, see `Amazon Web
        Services managed
        applications <https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html>`__.

        :param instance_arn: The ARN of the instance of IAM Identity Center under which the operation
        will run.
        :param application_provider_arn: The ARN of the application provider under which the operation will run.
        :param name: The name of the .
        :param description: The description of the .
        :param portal_options: A structure that describes the options for the portal associated with an
        application.
        :param tags: Specifies tags to be attached to the application.
        :param status: Specifies whether the application is enabled or disabled.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :returns: CreateApplicationResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateApplicationAssignment")
    def create_application_assignment(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        principal_id: PrincipalId,
        principal_type: PrincipalType,
        **kwargs,
    ) -> CreateApplicationAssignmentResponse:
        """Grant application access to a user or group.

        :param application_arn: The ARN of the application for which the assignment is created.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or
        group.
        :param principal_type: The entity type for which the assignment will be created.
        :returns: CreateApplicationAssignmentResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateInstance")
    def create_instance(
        self,
        context: RequestContext,
        name: NameType | None = None,
        client_token: ClientToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateInstanceResponse:
        """Creates an instance of IAM Identity Center for a standalone Amazon Web
        Services account that is not managed by Organizations or a member Amazon
        Web Services account in an organization. You can create only one
        instance per account and across all Amazon Web Services Regions.

        The CreateInstance request is rejected if the following apply:

        -  The instance is created within the organization management account.

        -  An instance already exists in the same account.

        :param name: The name of the instance of IAM Identity Center.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :param tags: Specifies tags to be attached to the instance of IAM Identity Center.
        :returns: CreateInstanceResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateInstanceAccessControlAttributeConfiguration")
    def create_instance_access_control_attribute_configuration(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        instance_access_control_attribute_configuration: InstanceAccessControlAttributeConfiguration,
        **kwargs,
    ) -> CreateInstanceAccessControlAttributeConfigurationResponse:
        """Enables the attributes-based access control (ABAC) feature for the
        specified IAM Identity Center instance. You can also specify new
        attributes to add to your ABAC configuration during the enabling
        process. For more information about ABAC, see `Attribute-Based Access
        Control </singlesignon/latest/userguide/abac.html>`__ in the *IAM
        Identity Center User Guide*.

        After a successful response, call
        ``DescribeInstanceAccessControlAttributeConfiguration`` to validate that
        ``InstanceAccessControlAttributeConfiguration`` was created.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param instance_access_control_attribute_configuration: Specifies the IAM Identity Center identity store attributes to add to
        your ABAC configuration.
        :returns: CreateInstanceAccessControlAttributeConfigurationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreatePermissionSet")
    def create_permission_set(
        self,
        context: RequestContext,
        name: PermissionSetName,
        instance_arn: InstanceArn,
        description: PermissionSetDescription | None = None,
        session_duration: Duration | None = None,
        relay_state: RelayState | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreatePermissionSetResponse:
        """Creates a permission set within a specified IAM Identity Center
        instance.

        To grant users and groups access to Amazon Web Services account
        resources, use ``CreateAccountAssignment``.

        :param name: The name of the PermissionSet.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param description: The description of the PermissionSet.
        :param session_duration: The length of time that the application user sessions are valid in the
        ISO-8601 standard.
        :param relay_state: Used to redirect users within the application during the federation
        authentication process.
        :param tags: The tags to attach to the new PermissionSet.
        :returns: CreatePermissionSetResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("CreateTrustedTokenIssuer")
    def create_trusted_token_issuer(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        name: TrustedTokenIssuerName,
        trusted_token_issuer_type: TrustedTokenIssuerType,
        trusted_token_issuer_configuration: TrustedTokenIssuerConfiguration,
        client_token: ClientToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateTrustedTokenIssuerResponse:
        """Creates a connection to a trusted token issuer in an instance of IAM
        Identity Center. A trusted token issuer enables trusted identity
        propagation to be used with applications that authenticate outside of
        Amazon Web Services.

        This trusted token issuer describes an external identity provider (IdP)
        that can generate claims or assertions in the form of access tokens for
        a user. Applications enabled for IAM Identity Center can use these
        tokens for authentication.

        :param instance_arn: Specifies the ARN of the instance of IAM Identity Center to contain the
        new trusted token issuer configuration.
        :param name: Specifies the name of the new trusted token issuer configuration.
        :param trusted_token_issuer_type: Specifies the type of the new trusted token issuer.
        :param trusted_token_issuer_configuration: Specifies settings that apply to the new trusted token issuer
        configuration.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :param tags: Specifies tags to be attached to the new trusted token issuer
        configuration.
        :returns: CreateTrustedTokenIssuerResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteAccountAssignment")
    def delete_account_assignment(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        target_id: TargetId,
        target_type: TargetType,
        permission_set_arn: PermissionSetArn,
        principal_type: PrincipalType,
        principal_id: PrincipalId,
        **kwargs,
    ) -> DeleteAccountAssignmentResponse:
        """Deletes a principal's access from a specified Amazon Web Services
        account using a specified permission set.

        After a successful response, call
        ``DescribeAccountAssignmentDeletionStatus`` to describe the status of an
        assignment deletion request.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param target_id: TargetID is an Amazon Web Services account identifier, (For example,
        123456789012).
        :param target_type: The entity type for which the assignment will be deleted.
        :param permission_set_arn: The ARN of the permission set that will be used to remove access.
        :param principal_type: The entity type for which the assignment will be deleted.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or
        group.
        :returns: DeleteAccountAssignmentResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApplication")
    def delete_application(
        self, context: RequestContext, application_arn: ApplicationArn, **kwargs
    ) -> DeleteApplicationResponse:
        """Deletes the association with the application. The connected service
        resource still exists.

        :param application_arn: Specifies the ARN of the application.
        :returns: DeleteApplicationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApplicationAccessScope")
    def delete_application_access_scope(
        self, context: RequestContext, application_arn: ApplicationArn, scope: Scope, **kwargs
    ) -> None:
        """Deletes an IAM Identity Center access scope from an application.

        :param application_arn: Specifies the ARN of the application with the access scope to delete.
        :param scope: Specifies the name of the access scope to remove from the application.
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApplicationAssignment")
    def delete_application_assignment(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        principal_id: PrincipalId,
        principal_type: PrincipalType,
        **kwargs,
    ) -> DeleteApplicationAssignmentResponse:
        """Revoke application access to an application by deleting application
        assignments for a user or group.

        :param application_arn: Specifies the ARN of the application.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or
        group.
        :param principal_type: The entity type for which the assignment will be deleted.
        :returns: DeleteApplicationAssignmentResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApplicationAuthenticationMethod")
    def delete_application_authentication_method(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        authentication_method_type: AuthenticationMethodType,
        **kwargs,
    ) -> None:
        """Deletes an authentication method from an application.

        :param application_arn: Specifies the ARN of the application with the authentication method to
        delete.
        :param authentication_method_type: Specifies the authentication method type to delete from the application.
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApplicationGrant")
    def delete_application_grant(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        grant_type: GrantType,
        **kwargs,
    ) -> None:
        """Deletes a grant from an application.

        :param application_arn: Specifies the ARN of the application with the grant to delete.
        :param grant_type: Specifies the type of grant to delete from the application.
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteInlinePolicyFromPermissionSet")
    def delete_inline_policy_from_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        **kwargs,
    ) -> DeleteInlinePolicyFromPermissionSetResponse:
        """Deletes the inline policy from a specified permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set that will be used to remove access.
        :returns: DeleteInlinePolicyFromPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteInstance")
    def delete_instance(
        self, context: RequestContext, instance_arn: InstanceArn, **kwargs
    ) -> DeleteInstanceResponse:
        """Deletes the instance of IAM Identity Center. Only the account that owns
        the instance can call this API. Neither the delegated administrator nor
        member account can delete the organization instance, but those roles can
        delete their own instance.

        :param instance_arn: The ARN of the instance of IAM Identity Center under which the operation
        will run.
        :returns: DeleteInstanceResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteInstanceAccessControlAttributeConfiguration")
    def delete_instance_access_control_attribute_configuration(
        self, context: RequestContext, instance_arn: InstanceArn, **kwargs
    ) -> DeleteInstanceAccessControlAttributeConfigurationResponse:
        """Disables the attributes-based access control (ABAC) feature for the
        specified IAM Identity Center instance and deletes all of the attribute
        mappings that have been configured. Once deleted, any attributes that
        are received from an identity source and any custom attributes you have
        previously configured will not be passed. For more information about
        ABAC, see `Attribute-Based Access
        Control </singlesignon/latest/userguide/abac.html>`__ in the *IAM
        Identity Center User Guide*.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :returns: DeleteInstanceAccessControlAttributeConfigurationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeletePermissionSet")
    def delete_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        **kwargs,
    ) -> DeletePermissionSetResponse:
        """Deletes the specified permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set that should be deleted.
        :returns: DeletePermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeletePermissionsBoundaryFromPermissionSet")
    def delete_permissions_boundary_from_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        **kwargs,
    ) -> DeletePermissionsBoundaryFromPermissionSetResponse:
        """Deletes the permissions boundary from a specified PermissionSet.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the ``PermissionSet``.
        :returns: DeletePermissionsBoundaryFromPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteTrustedTokenIssuer")
    def delete_trusted_token_issuer(
        self, context: RequestContext, trusted_token_issuer_arn: TrustedTokenIssuerArn, **kwargs
    ) -> DeleteTrustedTokenIssuerResponse:
        """Deletes a trusted token issuer configuration from an instance of IAM
        Identity Center.

        Deleting this trusted token issuer configuration will cause users to
        lose access to any applications that are configured to use the trusted
        token issuer.

        :param trusted_token_issuer_arn: Specifies the ARN of the trusted token issuer configuration to delete.
        :returns: DeleteTrustedTokenIssuerResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DescribeAccountAssignmentCreationStatus")
    def describe_account_assignment_creation_status(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        account_assignment_creation_request_id: UUId,
        **kwargs,
    ) -> DescribeAccountAssignmentCreationStatusResponse:
        """Describes the status of the assignment creation request.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param account_assignment_creation_request_id: The identifier that is used to track the request operation progress.
        :returns: DescribeAccountAssignmentCreationStatusResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeAccountAssignmentDeletionStatus")
    def describe_account_assignment_deletion_status(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        account_assignment_deletion_request_id: UUId,
        **kwargs,
    ) -> DescribeAccountAssignmentDeletionStatusResponse:
        """Describes the status of the assignment deletion request.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param account_assignment_deletion_request_id: The identifier that is used to track the request operation progress.
        :returns: DescribeAccountAssignmentDeletionStatusResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeApplication")
    def describe_application(
        self, context: RequestContext, application_arn: ApplicationArn, **kwargs
    ) -> DescribeApplicationResponse:
        """Retrieves the details of an application associated with an instance of
        IAM Identity Center.

        :param application_arn: Specifies the ARN of the application.
        :returns: DescribeApplicationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeApplicationAssignment")
    def describe_application_assignment(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        principal_id: PrincipalId,
        principal_type: PrincipalType,
        **kwargs,
    ) -> DescribeApplicationAssignmentResponse:
        """Retrieves a direct assignment of a user or group to an application. If
        the user doesn’t have a direct assignment to the application, the user
        may still have access to the application through a group. Therefore,
        don’t use this API to test access to an application for a user. Instead
        use ListApplicationAssignmentsForPrincipal.

        :param application_arn: Specifies the ARN of the application.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or
        group.
        :param principal_type: The entity type for which the assignment will be created.
        :returns: DescribeApplicationAssignmentResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeApplicationProvider")
    def describe_application_provider(
        self, context: RequestContext, application_provider_arn: ApplicationProviderArn, **kwargs
    ) -> DescribeApplicationProviderResponse:
        """Retrieves details about a provider that can be used to connect an Amazon
        Web Services managed application or customer managed application to IAM
        Identity Center.

        :param application_provider_arn: Specifies the ARN of the application provider for which you want
        details.
        :returns: DescribeApplicationProviderResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeInstance")
    def describe_instance(
        self, context: RequestContext, instance_arn: InstanceArn, **kwargs
    ) -> DescribeInstanceResponse:
        """Returns the details of an instance of IAM Identity Center. The status
        can be one of the following:

        -  ``CREATE_IN_PROGRESS`` - The instance is in the process of being
           created. When the instance is ready for use, DescribeInstance returns
           the status of ``ACTIVE``. While the instance is in the
           ``CREATE_IN_PROGRESS`` state, you can call only DescribeInstance and
           DeleteInstance operations.

        -  ``DELETE_IN_PROGRESS`` - The instance is being deleted. Returns
           ``AccessDeniedException`` after the delete operation completes.

        -  ``ACTIVE`` - The instance is active.

        :param instance_arn: The ARN of the instance of IAM Identity Center under which the operation
        will run.
        :returns: DescribeInstanceResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeInstanceAccessControlAttributeConfiguration")
    def describe_instance_access_control_attribute_configuration(
        self, context: RequestContext, instance_arn: InstanceArn, **kwargs
    ) -> DescribeInstanceAccessControlAttributeConfigurationResponse:
        """Returns the list of IAM Identity Center identity store attributes that
        have been configured to work with attributes-based access control (ABAC)
        for the specified IAM Identity Center instance. This will not return
        attributes configured and sent by an external identity provider. For
        more information about ABAC, see `Attribute-Based Access
        Control </singlesignon/latest/userguide/abac.html>`__ in the *IAM
        Identity Center User Guide*.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :returns: DescribeInstanceAccessControlAttributeConfigurationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribePermissionSet")
    def describe_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        **kwargs,
    ) -> DescribePermissionSetResponse:
        """Gets the details of the permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set.
        :returns: DescribePermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribePermissionSetProvisioningStatus")
    def describe_permission_set_provisioning_status(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        provision_permission_set_request_id: UUId,
        **kwargs,
    ) -> DescribePermissionSetProvisioningStatusResponse:
        """Describes the status for the given permission set provisioning request.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param provision_permission_set_request_id: The identifier that is provided by the ProvisionPermissionSet call to
        retrieve the current status of the provisioning workflow.
        :returns: DescribePermissionSetProvisioningStatusResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DescribeTrustedTokenIssuer")
    def describe_trusted_token_issuer(
        self, context: RequestContext, trusted_token_issuer_arn: TrustedTokenIssuerArn, **kwargs
    ) -> DescribeTrustedTokenIssuerResponse:
        """Retrieves details about a trusted token issuer configuration stored in
        an instance of IAM Identity Center. Details include the name of the
        trusted token issuer, the issuer URL, and the path of the source
        attribute and the destination attribute for a trusted token issuer
        configuration.

        :param trusted_token_issuer_arn: Specifies the ARN of the trusted token issuer configuration that you
        want details about.
        :returns: DescribeTrustedTokenIssuerResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("DetachCustomerManagedPolicyReferenceFromPermissionSet")
    def detach_customer_managed_policy_reference_from_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        customer_managed_policy_reference: CustomerManagedPolicyReference,
        **kwargs,
    ) -> DetachCustomerManagedPolicyReferenceFromPermissionSetResponse:
        """Detaches the specified customer managed policy from the specified
        PermissionSet.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the ``PermissionSet``.
        :param customer_managed_policy_reference: Specifies the name and path of a customer managed policy.
        :returns: DetachCustomerManagedPolicyReferenceFromPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DetachManagedPolicyFromPermissionSet")
    def detach_managed_policy_from_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        managed_policy_arn: ManagedPolicyArn,
        **kwargs,
    ) -> DetachManagedPolicyFromPermissionSetResponse:
        """Detaches the attached Amazon Web Services managed policy ARN from the
        specified permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the PermissionSet from which the policy should be detached.
        :param managed_policy_arn: The Amazon Web Services managed policy ARN to be detached from a
        permission set.
        :returns: DetachManagedPolicyFromPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetApplicationAccessScope")
    def get_application_access_scope(
        self, context: RequestContext, application_arn: ApplicationArn, scope: Scope, **kwargs
    ) -> GetApplicationAccessScopeResponse:
        """Retrieves the authorized targets for an IAM Identity Center access scope
        for an application.

        :param application_arn: Specifies the ARN of the application with the access scope that you want
        to retrieve.
        :param scope: Specifies the name of the access scope for which you want the authorized
        targets.
        :returns: GetApplicationAccessScopeResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetApplicationAssignmentConfiguration")
    def get_application_assignment_configuration(
        self, context: RequestContext, application_arn: ApplicationArn, **kwargs
    ) -> GetApplicationAssignmentConfigurationResponse:
        """Retrieves the configuration of PutApplicationAssignmentConfiguration.

        :param application_arn: Specifies the ARN of the application.
        :returns: GetApplicationAssignmentConfigurationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetApplicationAuthenticationMethod")
    def get_application_authentication_method(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        authentication_method_type: AuthenticationMethodType,
        **kwargs,
    ) -> GetApplicationAuthenticationMethodResponse:
        """Retrieves details about an authentication method used by an application.

        :param application_arn: Specifies the ARN of the application.
        :param authentication_method_type: Specifies the type of authentication method for which you want details.
        :returns: GetApplicationAuthenticationMethodResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetApplicationGrant")
    def get_application_grant(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        grant_type: GrantType,
        **kwargs,
    ) -> GetApplicationGrantResponse:
        """Retrieves details about an application grant.

        :param application_arn: Specifies the ARN of the application that contains the grant.
        :param grant_type: Specifies the type of grant.
        :returns: GetApplicationGrantResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetInlinePolicyForPermissionSet")
    def get_inline_policy_for_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        **kwargs,
    ) -> GetInlinePolicyForPermissionSetResponse:
        """Obtains the inline policy assigned to the permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set.
        :returns: GetInlinePolicyForPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetPermissionsBoundaryForPermissionSet")
    def get_permissions_boundary_for_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        **kwargs,
    ) -> GetPermissionsBoundaryForPermissionSetResponse:
        """Obtains the permissions boundary for a specified PermissionSet.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the ``PermissionSet``.
        :returns: GetPermissionsBoundaryForPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListAccountAssignmentCreationStatus")
    def list_account_assignment_creation_status(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        filter: OperationStatusFilter | None = None,
        **kwargs,
    ) -> ListAccountAssignmentCreationStatusResponse:
        """Lists the status of the Amazon Web Services account assignment creation
        requests for a specified IAM Identity Center instance.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param max_results: The maximum number of results to display for the assignment.
        :param next_token: The pagination token for the list API.
        :param filter: Filters results based on the passed attribute value.
        :returns: ListAccountAssignmentCreationStatusResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListAccountAssignmentDeletionStatus")
    def list_account_assignment_deletion_status(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        filter: OperationStatusFilter | None = None,
        **kwargs,
    ) -> ListAccountAssignmentDeletionStatusResponse:
        """Lists the status of the Amazon Web Services account assignment deletion
        requests for a specified IAM Identity Center instance.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param max_results: The maximum number of results to display for the assignment.
        :param next_token: The pagination token for the list API.
        :param filter: Filters results based on the passed attribute value.
        :returns: ListAccountAssignmentDeletionStatusResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListAccountAssignments")
    def list_account_assignments(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        account_id: TargetId,
        permission_set_arn: PermissionSetArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListAccountAssignmentsResponse:
        """Lists the assignee of the specified Amazon Web Services account with the
        specified permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param account_id: The identifier of the Amazon Web Services account from which to list the
        assignments.
        :param permission_set_arn: The ARN of the permission set from which to list assignments.
        :param max_results: The maximum number of results to display for the assignment.
        :param next_token: The pagination token for the list API.
        :returns: ListAccountAssignmentsResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListAccountAssignmentsForPrincipal")
    def list_account_assignments_for_principal(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        principal_id: PrincipalId,
        principal_type: PrincipalType,
        filter: ListAccountAssignmentsFilter | None = None,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAccountAssignmentsForPrincipalResponse:
        """Retrieves a list of the IAM Identity Center associated Amazon Web
        Services accounts that the principal has access to. This action must be
        called from the management account containing your organization instance
        of IAM Identity Center. This action is not valid for account instances
        of IAM Identity Center.

        :param instance_arn: Specifies the ARN of the instance of IAM Identity Center that contains
        the principal.
        :param principal_id: Specifies the principal for which you want to retrieve the list of
        account assignments.
        :param principal_type: Specifies the type of the principal.
        :param filter: Specifies an Amazon Web Services account ID number.
        :param next_token: Specifies that you want to receive the next page of results.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :returns: ListAccountAssignmentsForPrincipalResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListAccountsForProvisionedPermissionSet")
    def list_accounts_for_provisioned_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        provisioning_status: ProvisioningStatus | None = None,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListAccountsForProvisionedPermissionSetResponse:
        """Lists all the Amazon Web Services accounts where the specified
        permission set is provisioned.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the PermissionSet from which the associated Amazon Web
        Services accounts will be listed.
        :param provisioning_status: The permission set provisioning status for an Amazon Web Services
        account.
        :param max_results: The maximum number of results to display for the PermissionSet.
        :param next_token: The pagination token for the list API.
        :returns: ListAccountsForProvisionedPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplicationAccessScopes")
    def list_application_access_scopes(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        max_results: ListApplicationAccessScopesRequestMaxResultsInteger | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListApplicationAccessScopesResponse:
        """Lists the access scopes and authorized targets associated with an
        application.

        :param application_arn: Specifies the ARN of the application.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param next_token: Specifies that you want to receive the next page of results.
        :returns: ListApplicationAccessScopesResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplicationAssignments")
    def list_application_assignments(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListApplicationAssignmentsResponse:
        """Lists Amazon Web Services account users that are assigned to an
        application.

        :param application_arn: Specifies the ARN of the application.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param next_token: Specifies that you want to receive the next page of results.
        :returns: ListApplicationAssignmentsResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplicationAssignmentsForPrincipal")
    def list_application_assignments_for_principal(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        principal_id: PrincipalId,
        principal_type: PrincipalType,
        filter: ListApplicationAssignmentsFilter | None = None,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListApplicationAssignmentsForPrincipalResponse:
        """Lists the applications to which a specified principal is assigned. You
        must provide a filter when calling this action from a member account
        against your organization instance of IAM Identity Center. A filter is
        not required when called from the management account against an
        organization instance of IAM Identity Center, or from a member account
        against an account instance of IAM Identity Center in the same account.

        :param instance_arn: Specifies the instance of IAM Identity Center that contains principal
        and applications.
        :param principal_id: Specifies the unique identifier of the principal for which you want to
        retrieve its assignments.
        :param principal_type: Specifies the type of the principal for which you want to retrieve its
        assignments.
        :param filter: Filters the output to include only assignments associated with the
        application that has the specified ARN.
        :param next_token: Specifies that you want to receive the next page of results.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :returns: ListApplicationAssignmentsForPrincipalResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplicationAuthenticationMethods")
    def list_application_authentication_methods(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListApplicationAuthenticationMethodsResponse:
        """Lists all of the authentication methods supported by the specified
        application.

        :param application_arn: Specifies the ARN of the application with the authentication methods you
        want to list.
        :param next_token: Specifies that you want to receive the next page of results.
        :returns: ListApplicationAuthenticationMethodsResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplicationGrants")
    def list_application_grants(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListApplicationGrantsResponse:
        """List the grants associated with an application.

        :param application_arn: Specifies the ARN of the application whose grants you want to list.
        :param next_token: Specifies that you want to receive the next page of results.
        :returns: ListApplicationGrantsResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplicationProviders")
    def list_application_providers(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListApplicationProvidersResponse:
        """Lists the application providers configured in the IAM Identity Center
        identity store.

        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param next_token: Specifies that you want to receive the next page of results.
        :returns: ListApplicationProvidersResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListApplications")
    def list_applications(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        filter: ListApplicationsFilter | None = None,
        **kwargs,
    ) -> ListApplicationsResponse:
        """Lists all applications associated with the instance of IAM Identity
        Center. When listing applications for an organization instance in the
        management account, member accounts must use the ``applicationAccount``
        parameter to filter the list to only applications created from that
        account. When listing applications for an account instance in the same
        member account, a filter is not required.

        :param instance_arn: The ARN of the IAM Identity Center application under which the operation
        will run.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param next_token: Specifies that you want to receive the next page of results.
        :param filter: Filters response results.
        :returns: ListApplicationsResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListCustomerManagedPolicyReferencesInPermissionSet")
    def list_customer_managed_policy_references_in_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetResponse:
        """Lists all customer managed policies attached to a specified
        PermissionSet.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the ``PermissionSet``.
        :param max_results: The maximum number of results to display for the list call.
        :param next_token: The pagination token for the list API.
        :returns: ListCustomerManagedPolicyReferencesInPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListInstances")
    def list_instances(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListInstancesResponse:
        """Lists the details of the organization and account instances of IAM
        Identity Center that were created in or visible to the account calling
        this API.

        :param max_results: The maximum number of results to display for the instance.
        :param next_token: The pagination token for the list API.
        :returns: ListInstancesResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListManagedPoliciesInPermissionSet")
    def list_managed_policies_in_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListManagedPoliciesInPermissionSetResponse:
        """Lists the Amazon Web Services managed policy that is attached to a
        specified permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the PermissionSet whose managed policies will be listed.
        :param max_results: The maximum number of results to display for the PermissionSet.
        :param next_token: The pagination token for the list API.
        :returns: ListManagedPoliciesInPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPermissionSetProvisioningStatus")
    def list_permission_set_provisioning_status(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        filter: OperationStatusFilter | None = None,
        **kwargs,
    ) -> ListPermissionSetProvisioningStatusResponse:
        """Lists the status of the permission set provisioning requests for a
        specified IAM Identity Center instance.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param max_results: The maximum number of results to display for the assignment.
        :param next_token: The pagination token for the list API.
        :param filter: Filters results based on the passed attribute value.
        :returns: ListPermissionSetProvisioningStatusResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPermissionSets")
    def list_permission_sets(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        next_token: Token | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListPermissionSetsResponse:
        """Lists the PermissionSets in an IAM Identity Center instance.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param next_token: The pagination token for the list API.
        :param max_results: The maximum number of results to display for the assignment.
        :returns: ListPermissionSetsResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListPermissionSetsProvisionedToAccount")
    def list_permission_sets_provisioned_to_account(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        account_id: AccountId,
        provisioning_status: ProvisioningStatus | None = None,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListPermissionSetsProvisionedToAccountResponse:
        """Lists all the permission sets that are provisioned to a specified Amazon
        Web Services account.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param account_id: The identifier of the Amazon Web Services account from which to list the
        assignments.
        :param provisioning_status: The status object for the permission set provisioning operation.
        :param max_results: The maximum number of results to display for the assignment.
        :param next_token: The pagination token for the list API.
        :returns: ListPermissionSetsProvisionedToAccountResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_arn: TaggableResourceArn,
        instance_arn: InstanceArn | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListTagsForResourceResponse:
        """Lists the tags that are attached to a specified resource.

        :param resource_arn: The ARN of the resource with the tags to be listed.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param next_token: The pagination token for the list API.
        :returns: ListTagsForResourceResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListTrustedTokenIssuers")
    def list_trusted_token_issuers(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        max_results: MaxResults | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListTrustedTokenIssuersResponse:
        """Lists all the trusted token issuers configured in an instance of IAM
        Identity Center.

        :param instance_arn: Specifies the ARN of the instance of IAM Identity Center with the
        trusted token issuer configurations that you want to list.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param next_token: Specifies that you want to receive the next page of results.
        :returns: ListTrustedTokenIssuersResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ProvisionPermissionSet")
    def provision_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        target_type: ProvisionTargetType,
        target_id: TargetId | None = None,
        **kwargs,
    ) -> ProvisionPermissionSetResponse:
        """The process by which a specified permission set is provisioned to the
        specified target.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set.
        :param target_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an Amazon Web Services account identifier, (For example,
        123456789012).
        :returns: ProvisionPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutApplicationAccessScope")
    def put_application_access_scope(
        self,
        context: RequestContext,
        scope: Scope,
        application_arn: ApplicationArn,
        authorized_targets: ScopeTargets | None = None,
        **kwargs,
    ) -> None:
        """Adds or updates the list of authorized targets for an IAM Identity
        Center access scope for an application.

        :param scope: Specifies the name of the access scope to be associated with the
        specified targets.
        :param application_arn: Specifies the ARN of the application with the access scope with the
        targets to add or update.
        :param authorized_targets: Specifies an array list of ARNs that represent the authorized targets
        for this access scope.
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutApplicationAssignmentConfiguration")
    def put_application_assignment_configuration(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        assignment_required: AssignmentRequired,
        **kwargs,
    ) -> PutApplicationAssignmentConfigurationResponse:
        """Configure how users gain access to an application. If
        ``AssignmentsRequired`` is ``true`` (default value), users don’t have
        access to the application unless an assignment is created using the
        `CreateApplicationAssignment
        API <https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html>`__.
        If ``false``, all users have access to the application. If an assignment
        is created using
        `CreateApplicationAssignment <https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html>`__.,
        the user retains access if ``AssignmentsRequired`` is set to ``true``.

        :param application_arn: Specifies the ARN of the application.
        :param assignment_required: If ``AssignmentsRequired`` is ``true`` (default value), users don’t have
        access to the application unless an assignment is created using the
        `CreateApplicationAssignment
        API <https://docs.
        :returns: PutApplicationAssignmentConfigurationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutApplicationAuthenticationMethod")
    def put_application_authentication_method(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        authentication_method_type: AuthenticationMethodType,
        authentication_method: AuthenticationMethod,
        **kwargs,
    ) -> None:
        """Adds or updates an authentication method for an application.

        :param application_arn: Specifies the ARN of the application with the authentication method to
        add or update.
        :param authentication_method_type: Specifies the type of the authentication method that you want to add or
        update.
        :param authentication_method: Specifies a structure that describes the authentication method to add or
        update.
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutApplicationGrant")
    def put_application_grant(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        grant_type: GrantType,
        grant: Grant,
        **kwargs,
    ) -> None:
        """Creates a configuration for an application to use grants. Conceptually
        grants are authorization to request actions related to tokens. This
        configuration will be used when parties are requesting and receiving
        tokens during the trusted identity propagation process. For more
        information on the IAM Identity Center supported grant workflows, see
        `SAML 2.0 and OAuth
        2.0 <https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html>`__.

        A grant is created between your applications and Identity Center
        instance which enables an application to use specified mechanisms to
        obtain tokens. These tokens are used by your applications to gain access
        to Amazon Web Services resources on behalf of users. The following
        elements are within these exchanges:

        -  **Requester** - The application requesting access to Amazon Web
           Services resources.

        -  **Subject** - Typically the user that is requesting access to Amazon
           Web Services resources.

        -  **Grant** - Conceptually, a grant is authorization to access Amazon
           Web Services resources. These grants authorize token generation for
           authenticating access to the requester and for the request to make
           requests on behalf of the subjects. There are four types of grants:

           -  **AuthorizationCode** - Allows an application to request
              authorization through a series of user-agent redirects.

           -  **JWT bearer** - Authorizes an application to exchange a JSON Web
              Token that came from an external identity provider. To learn more,
              see `RFC 6479 <https://datatracker.ietf.org/doc/html/rfc6749>`__.

           -  **Refresh token** - Enables application to request new access
              tokens to replace expiring or expired access tokens.

           -  **Exchange token** - A grant that requests tokens from the
              authorization server by providing a ‘subject’ token with access
              scope authorizing trusted identity propagation to this
              application. To learn more, see `RFC
              8693 <https://datatracker.ietf.org/doc/html/rfc8693>`__.

        -  **Authorization server** - IAM Identity Center requests tokens.

        User credentials are never shared directly within these exchanges.
        Instead, applications use grants to request access tokens from IAM
        Identity Center. For more information, see `RFC
        6479 <https://datatracker.ietf.org/doc/html/rfc6749>`__.

        **Use cases**

        -  Connecting to custom applications.

        -  Configuring an Amazon Web Services service to make calls to another
           Amazon Web Services services using JWT tokens.

        :param application_arn: Specifies the ARN of the application to update.
        :param grant_type: Specifies the type of grant to update.
        :param grant: Specifies a structure that describes the grant to update.
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutInlinePolicyToPermissionSet")
    def put_inline_policy_to_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        inline_policy: PermissionSetPolicyDocument,
        **kwargs,
    ) -> PutInlinePolicyToPermissionSetResponse:
        """Attaches an inline policy to a permission set.

        If the permission set is already referenced by one or more account
        assignments, you will need to call ``ProvisionPermissionSet`` after this
        action to apply the corresponding IAM policy updates to all assigned
        accounts.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set.
        :param inline_policy: The inline policy to attach to a PermissionSet.
        :returns: PutInlinePolicyToPermissionSetResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("PutPermissionsBoundaryToPermissionSet")
    def put_permissions_boundary_to_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        permissions_boundary: PermissionsBoundary,
        **kwargs,
    ) -> PutPermissionsBoundaryToPermissionSetResponse:
        """Attaches an Amazon Web Services managed or customer managed policy to
        the specified PermissionSet as a permissions boundary.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the ``PermissionSet``.
        :param permissions_boundary: The permissions boundary that you want to attach to a ``PermissionSet``.
        :returns: PutPermissionsBoundaryToPermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self,
        context: RequestContext,
        resource_arn: TaggableResourceArn,
        tags: TagList,
        instance_arn: InstanceArn | None = None,
        **kwargs,
    ) -> TagResourceResponse:
        """Associates a set of tags with a specified resource.

        :param resource_arn: The ARN of the resource with the tags to be listed.
        :param tags: A set of key-value pairs that are used to manage the resource.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :returns: TagResourceResponse
        :raises ServiceQuotaExceededException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: TaggableResourceArn,
        tag_keys: TagKeyList,
        instance_arn: InstanceArn | None = None,
        **kwargs,
    ) -> UntagResourceResponse:
        """Disassociates a set of tags from a specified resource.

        :param resource_arn: The ARN of the resource with the tags to be listed.
        :param tag_keys: The keys of tags that are attached to the resource.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :returns: UntagResourceResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateApplication")
    def update_application(
        self,
        context: RequestContext,
        application_arn: ApplicationArn,
        name: ApplicationNameType | None = None,
        description: Description | None = None,
        status: ApplicationStatus | None = None,
        portal_options: UpdateApplicationPortalOptions | None = None,
        **kwargs,
    ) -> UpdateApplicationResponse:
        """Updates application properties.

        :param application_arn: Specifies the ARN of the application.
        :param name: Specifies the updated name for the application.
        :param description: The description of the .
        :param status: Specifies whether the application is enabled or disabled.
        :param portal_options: A structure that describes the options for the portal associated with an
        application.
        :returns: UpdateApplicationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateInstance")
    def update_instance(
        self, context: RequestContext, name: NameType, instance_arn: InstanceArn, **kwargs
    ) -> UpdateInstanceResponse:
        """Update the details for the instance of IAM Identity Center that is owned
        by the Amazon Web Services account.

        :param name: Updates the instance name.
        :param instance_arn: The ARN of the instance of IAM Identity Center under which the operation
        will run.
        :returns: UpdateInstanceResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateInstanceAccessControlAttributeConfiguration")
    def update_instance_access_control_attribute_configuration(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        instance_access_control_attribute_configuration: InstanceAccessControlAttributeConfiguration,
        **kwargs,
    ) -> UpdateInstanceAccessControlAttributeConfigurationResponse:
        """Updates the IAM Identity Center identity store attributes that you can
        use with the IAM Identity Center instance for attributes-based access
        control (ABAC). When using an external identity provider as an identity
        source, you can pass attributes through the SAML assertion as an
        alternative to configuring attributes from the IAM Identity Center
        identity store. If a SAML assertion passes any of these attributes, IAM
        Identity Center replaces the attribute value with the value from the IAM
        Identity Center identity store. For more information about ABAC, see
        `Attribute-Based Access
        Control </singlesignon/latest/userguide/abac.html>`__ in the *IAM
        Identity Center User Guide*.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param instance_access_control_attribute_configuration: Updates the attributes for your ABAC configuration.
        :returns: UpdateInstanceAccessControlAttributeConfigurationResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdatePermissionSet")
    def update_permission_set(
        self,
        context: RequestContext,
        instance_arn: InstanceArn,
        permission_set_arn: PermissionSetArn,
        description: PermissionSetDescription | None = None,
        session_duration: Duration | None = None,
        relay_state: RelayState | None = None,
        **kwargs,
    ) -> UpdatePermissionSetResponse:
        """Updates an existing permission set.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation
        will be executed.
        :param permission_set_arn: The ARN of the permission set.
        :param description: The description of the PermissionSet.
        :param session_duration: The length of time that the application user sessions are valid for in
        the ISO-8601 standard.
        :param relay_state: Used to redirect users within the application during the federation
        authentication process.
        :returns: UpdatePermissionSetResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateTrustedTokenIssuer")
    def update_trusted_token_issuer(
        self,
        context: RequestContext,
        trusted_token_issuer_arn: TrustedTokenIssuerArn,
        name: TrustedTokenIssuerName | None = None,
        trusted_token_issuer_configuration: TrustedTokenIssuerUpdateConfiguration | None = None,
        **kwargs,
    ) -> UpdateTrustedTokenIssuerResponse:
        """Updates the name of the trusted token issuer, or the path of a source
        attribute or destination attribute for a trusted token issuer
        configuration.

        Updating this trusted token issuer configuration might cause users to
        lose access to any applications that are configured to use the trusted
        token issuer.

        :param trusted_token_issuer_arn: Specifies the ARN of the trusted token issuer configuration that you
        want to update.
        :param name: Specifies the updated name to be applied to the trusted token issuer
        configuration.
        :param trusted_token_issuer_configuration: Specifies a structure with settings to apply to the specified trusted
        token issuer.
        :returns: UpdateTrustedTokenIssuerResponse
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        """
        raise NotImplementedError
