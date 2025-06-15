from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AWSAccountIdType = str
AccessTokenValidityType = int
AccountTakeoverActionNotifyType = bool
AdminCreateUserUnusedAccountValidityDaysType = int
ArnType = str
AttributeMappingKeyType = str
AttributeNameType = str
AttributeValueType = str
AuthSessionValidityType = int
BooleanType = bool
CSSType = str
CSSVersionType = str
ClientIdType = str
ClientNameType = str
ClientPermissionType = str
ClientSecretType = str
CompletionMessageType = str
ConfirmationCodeType = str
CustomAttributeNameType = str
DescriptionType = str
DeviceKeyType = str
DeviceNameType = str
DomainType = str
DomainVersionType = str
EmailAddressType = str
EmailInviteMessageType = str
EmailMfaMessageType = str
EmailMfaSubjectType = str
EmailNotificationBodyType = str
EmailNotificationSubjectType = str
EmailVerificationMessageByLinkType = str
EmailVerificationMessageType = str
EmailVerificationSubjectByLinkType = str
EmailVerificationSubjectType = str
EventIdType = str
ForceAliasCreation = bool
GenerateSecret = bool
GroupNameType = str
HexStringType = str
IdTokenValidityType = int
IdpIdentifierType = str
ImageUrlType = str
IntegerType = int
InvalidParameterExceptionReasonCodeType = str
ListProvidersLimitType = int
ListResourceServersLimitType = int
ManagedLoginBrandingIdType = str
MessageType = str
PaginationKey = str
PaginationKeyType = str
PasswordHistorySizeType = int
PasswordPolicyMinLengthType = int
PasswordType = str
PoolQueryLimitType = int
PreSignedUrlType = str
PrecedenceType = int
PriorityType = int
ProviderNameType = str
ProviderNameTypeV2 = str
QueryLimit = int
QueryLimitType = int
RedirectUrlType = str
RefreshTokenValidityType = int
RegionCodeType = str
RelyingPartyIdType = str
ResourceIdType = str
ResourceServerIdentifierType = str
ResourceServerNameType = str
ResourceServerScopeDescriptionType = str
ResourceServerScopeNameType = str
RetryGracePeriodSecondsType = int
S3ArnType = str
S3BucketType = str
SESConfigurationSet = str
ScopeType = str
SearchPaginationTokenType = str
SecretCodeType = str
SecretHashType = str
SessionType = str
SmsInviteMessageType = str
SmsVerificationMessageType = str
SoftwareTokenMFAUserCodeType = str
StringType = str
TagKeysType = str
TagValueType = str
TemporaryPasswordValidityDaysType = int
TokenModelType = str
UserFilterType = str
UserImportJobIdType = str
UserImportJobNameType = str
UserPoolIdType = str
UserPoolNameType = str
UsernameType = str
WebAuthnAuthenticatorAttachmentType = str
WebAuthnAuthenticatorTransportType = str
WebAuthnCredentialsQueryLimitType = int
WrappedBooleanType = bool
WrappedIntegerType = int


class AccountTakeoverEventActionType(StrEnum):
    BLOCK = "BLOCK"
    MFA_IF_CONFIGURED = "MFA_IF_CONFIGURED"
    MFA_REQUIRED = "MFA_REQUIRED"
    NO_ACTION = "NO_ACTION"


class AdvancedSecurityEnabledModeType(StrEnum):
    AUDIT = "AUDIT"
    ENFORCED = "ENFORCED"


class AdvancedSecurityModeType(StrEnum):
    OFF = "OFF"
    AUDIT = "AUDIT"
    ENFORCED = "ENFORCED"


class AliasAttributeType(StrEnum):
    phone_number = "phone_number"
    email = "email"
    preferred_username = "preferred_username"


class AssetCategoryType(StrEnum):
    FAVICON_ICO = "FAVICON_ICO"
    FAVICON_SVG = "FAVICON_SVG"
    EMAIL_GRAPHIC = "EMAIL_GRAPHIC"
    SMS_GRAPHIC = "SMS_GRAPHIC"
    AUTH_APP_GRAPHIC = "AUTH_APP_GRAPHIC"
    PASSWORD_GRAPHIC = "PASSWORD_GRAPHIC"
    PASSKEY_GRAPHIC = "PASSKEY_GRAPHIC"
    PAGE_HEADER_LOGO = "PAGE_HEADER_LOGO"
    PAGE_HEADER_BACKGROUND = "PAGE_HEADER_BACKGROUND"
    PAGE_FOOTER_LOGO = "PAGE_FOOTER_LOGO"
    PAGE_FOOTER_BACKGROUND = "PAGE_FOOTER_BACKGROUND"
    PAGE_BACKGROUND = "PAGE_BACKGROUND"
    FORM_BACKGROUND = "FORM_BACKGROUND"
    FORM_LOGO = "FORM_LOGO"
    IDP_BUTTON_ICON = "IDP_BUTTON_ICON"


class AssetExtensionType(StrEnum):
    ICO = "ICO"
    JPEG = "JPEG"
    PNG = "PNG"
    SVG = "SVG"
    WEBP = "WEBP"


class AttributeDataType(StrEnum):
    String = "String"
    Number = "Number"
    DateTime = "DateTime"
    Boolean = "Boolean"


class AuthFactorType(StrEnum):
    PASSWORD = "PASSWORD"
    EMAIL_OTP = "EMAIL_OTP"
    SMS_OTP = "SMS_OTP"
    WEB_AUTHN = "WEB_AUTHN"


class AuthFlowType(StrEnum):
    USER_SRP_AUTH = "USER_SRP_AUTH"
    REFRESH_TOKEN_AUTH = "REFRESH_TOKEN_AUTH"
    REFRESH_TOKEN = "REFRESH_TOKEN"
    CUSTOM_AUTH = "CUSTOM_AUTH"
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"
    ADMIN_USER_PASSWORD_AUTH = "ADMIN_USER_PASSWORD_AUTH"
    USER_AUTH = "USER_AUTH"


class ChallengeName(StrEnum):
    Password = "Password"
    Mfa = "Mfa"


class ChallengeNameType(StrEnum):
    SMS_MFA = "SMS_MFA"
    EMAIL_OTP = "EMAIL_OTP"
    SOFTWARE_TOKEN_MFA = "SOFTWARE_TOKEN_MFA"
    SELECT_MFA_TYPE = "SELECT_MFA_TYPE"
    MFA_SETUP = "MFA_SETUP"
    PASSWORD_VERIFIER = "PASSWORD_VERIFIER"
    CUSTOM_CHALLENGE = "CUSTOM_CHALLENGE"
    SELECT_CHALLENGE = "SELECT_CHALLENGE"
    DEVICE_SRP_AUTH = "DEVICE_SRP_AUTH"
    DEVICE_PASSWORD_VERIFIER = "DEVICE_PASSWORD_VERIFIER"
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    NEW_PASSWORD_REQUIRED = "NEW_PASSWORD_REQUIRED"
    SMS_OTP = "SMS_OTP"
    PASSWORD = "PASSWORD"
    WEB_AUTHN = "WEB_AUTHN"
    PASSWORD_SRP = "PASSWORD_SRP"


class ChallengeResponse(StrEnum):
    Success = "Success"
    Failure = "Failure"


class ColorSchemeModeType(StrEnum):
    LIGHT = "LIGHT"
    DARK = "DARK"
    DYNAMIC = "DYNAMIC"


class CompromisedCredentialsEventActionType(StrEnum):
    BLOCK = "BLOCK"
    NO_ACTION = "NO_ACTION"


class CustomEmailSenderLambdaVersionType(StrEnum):
    V1_0 = "V1_0"


class CustomSMSSenderLambdaVersionType(StrEnum):
    V1_0 = "V1_0"


class DefaultEmailOptionType(StrEnum):
    CONFIRM_WITH_LINK = "CONFIRM_WITH_LINK"
    CONFIRM_WITH_CODE = "CONFIRM_WITH_CODE"


class DeletionProtectionType(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class DeliveryMediumType(StrEnum):
    SMS = "SMS"
    EMAIL = "EMAIL"


class DeviceRememberedStatusType(StrEnum):
    remembered = "remembered"
    not_remembered = "not_remembered"


class DomainStatusType(StrEnum):
    CREATING = "CREATING"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class EmailSendingAccountType(StrEnum):
    COGNITO_DEFAULT = "COGNITO_DEFAULT"
    DEVELOPER = "DEVELOPER"


class EventFilterType(StrEnum):
    SIGN_IN = "SIGN_IN"
    PASSWORD_CHANGE = "PASSWORD_CHANGE"
    SIGN_UP = "SIGN_UP"


class EventResponseType(StrEnum):
    Pass = "Pass"
    Fail = "Fail"
    InProgress = "InProgress"


class EventSourceName(StrEnum):
    userNotification = "userNotification"
    userAuthEvents = "userAuthEvents"


class EventType(StrEnum):
    SignIn = "SignIn"
    SignUp = "SignUp"
    ForgotPassword = "ForgotPassword"
    PasswordChange = "PasswordChange"
    ResendCode = "ResendCode"


class ExplicitAuthFlowsType(StrEnum):
    ADMIN_NO_SRP_AUTH = "ADMIN_NO_SRP_AUTH"
    CUSTOM_AUTH_FLOW_ONLY = "CUSTOM_AUTH_FLOW_ONLY"
    USER_PASSWORD_AUTH = "USER_PASSWORD_AUTH"
    ALLOW_ADMIN_USER_PASSWORD_AUTH = "ALLOW_ADMIN_USER_PASSWORD_AUTH"
    ALLOW_CUSTOM_AUTH = "ALLOW_CUSTOM_AUTH"
    ALLOW_USER_PASSWORD_AUTH = "ALLOW_USER_PASSWORD_AUTH"
    ALLOW_USER_SRP_AUTH = "ALLOW_USER_SRP_AUTH"
    ALLOW_REFRESH_TOKEN_AUTH = "ALLOW_REFRESH_TOKEN_AUTH"
    ALLOW_USER_AUTH = "ALLOW_USER_AUTH"


class FeatureType(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FeedbackValueType(StrEnum):
    Valid = "Valid"
    Invalid = "Invalid"


class IdentityProviderTypeType(StrEnum):
    SAML = "SAML"
    Facebook = "Facebook"
    Google = "Google"
    LoginWithAmazon = "LoginWithAmazon"
    SignInWithApple = "SignInWithApple"
    OIDC = "OIDC"


class LogLevel(StrEnum):
    ERROR = "ERROR"
    INFO = "INFO"


class MessageActionType(StrEnum):
    RESEND = "RESEND"
    SUPPRESS = "SUPPRESS"


class OAuthFlowType(StrEnum):
    code = "code"
    implicit = "implicit"
    client_credentials = "client_credentials"


class PreTokenGenerationLambdaVersionType(StrEnum):
    V1_0 = "V1_0"
    V2_0 = "V2_0"
    V3_0 = "V3_0"


class PreventUserExistenceErrorTypes(StrEnum):
    LEGACY = "LEGACY"
    ENABLED = "ENABLED"


class RecoveryOptionNameType(StrEnum):
    verified_email = "verified_email"
    verified_phone_number = "verified_phone_number"
    admin_only = "admin_only"


class RiskDecisionType(StrEnum):
    NoRisk = "NoRisk"
    AccountTakeover = "AccountTakeover"
    Block = "Block"


class RiskLevelType(StrEnum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class StatusType(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class TimeUnitsType(StrEnum):
    seconds = "seconds"
    minutes = "minutes"
    hours = "hours"
    days = "days"


class UserImportJobStatusType(StrEnum):
    Created = "Created"
    Pending = "Pending"
    InProgress = "InProgress"
    Stopping = "Stopping"
    Expired = "Expired"
    Stopped = "Stopped"
    Failed = "Failed"
    Succeeded = "Succeeded"


class UserPoolMfaType(StrEnum):
    OFF = "OFF"
    ON = "ON"
    OPTIONAL = "OPTIONAL"


class UserPoolTierType(StrEnum):
    LITE = "LITE"
    ESSENTIALS = "ESSENTIALS"
    PLUS = "PLUS"


class UserStatusType(StrEnum):
    UNCONFIRMED = "UNCONFIRMED"
    CONFIRMED = "CONFIRMED"
    ARCHIVED = "ARCHIVED"
    COMPROMISED = "COMPROMISED"
    UNKNOWN = "UNKNOWN"
    RESET_REQUIRED = "RESET_REQUIRED"
    FORCE_CHANGE_PASSWORD = "FORCE_CHANGE_PASSWORD"
    EXTERNAL_PROVIDER = "EXTERNAL_PROVIDER"


class UserVerificationType(StrEnum):
    required = "required"
    preferred = "preferred"


class UsernameAttributeType(StrEnum):
    phone_number = "phone_number"
    email = "email"


class VerifiedAttributeType(StrEnum):
    phone_number = "phone_number"
    email = "email"


class VerifySoftwareTokenResponseType(StrEnum):
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class AliasExistsException(ServiceException):
    """This exception is thrown when a user tries to confirm the account with
    an email address or phone number that has already been supplied as an
    alias for a different user profile. This exception indicates that an
    account with this email address or phone already exists in a user pool
    that you've configured to use email address or phone number as a sign-in
    alias.
    """

    code: str = "AliasExistsException"
    sender_fault: bool = False
    status_code: int = 400


class CodeDeliveryFailureException(ServiceException):
    """This exception is thrown when a verification code fails to deliver
    successfully.
    """

    code: str = "CodeDeliveryFailureException"
    sender_fault: bool = False
    status_code: int = 400


class CodeMismatchException(ServiceException):
    """This exception is thrown if the provided code doesn't match what the
    server was expecting.
    """

    code: str = "CodeMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentModificationException(ServiceException):
    """This exception is thrown if two or more modifications are happening
    concurrently.
    """

    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 400


class DeviceKeyExistsException(ServiceException):
    """This exception is thrown when a user attempts to confirm a device with a
    device key that already exists.
    """

    code: str = "DeviceKeyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class DuplicateProviderException(ServiceException):
    """This exception is thrown when the provider is already supported by the
    user pool.
    """

    code: str = "DuplicateProviderException"
    sender_fault: bool = False
    status_code: int = 400


class EnableSoftwareTokenMFAException(ServiceException):
    """This exception is thrown when there is a code mismatch and the service
    fails to configure the software token TOTP multi-factor authentication
    (MFA).
    """

    code: str = "EnableSoftwareTokenMFAException"
    sender_fault: bool = False
    status_code: int = 400


class ExpiredCodeException(ServiceException):
    """This exception is thrown if a code has expired."""

    code: str = "ExpiredCodeException"
    sender_fault: bool = False
    status_code: int = 400


class FeatureUnavailableInTierException(ServiceException):
    """This exception is thrown when a feature you attempted to configure isn't
    available in your current feature plan.
    """

    code: str = "FeatureUnavailableInTierException"
    sender_fault: bool = False
    status_code: int = 400


class ForbiddenException(ServiceException):
    """This exception is thrown when WAF doesn't allow your request based on a
    web ACL that's associated with your user pool.
    """

    code: str = "ForbiddenException"
    sender_fault: bool = False
    status_code: int = 400


class GroupExistsException(ServiceException):
    """This exception is thrown when Amazon Cognito encounters a group that
    already exists in the user pool.
    """

    code: str = "GroupExistsException"
    sender_fault: bool = False
    status_code: int = 400


class InternalErrorException(ServiceException):
    """This exception is thrown when Amazon Cognito encounters an internal
    error.
    """

    code: str = "InternalErrorException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidEmailRoleAccessPolicyException(ServiceException):
    """This exception is thrown when Amazon Cognito isn't allowed to use your
    email identity. HTTP status code: 400.
    """

    code: str = "InvalidEmailRoleAccessPolicyException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidLambdaResponseException(ServiceException):
    """This exception is thrown when Amazon Cognito encounters an invalid
    Lambda response.
    """

    code: str = "InvalidLambdaResponseException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOAuthFlowException(ServiceException):
    """This exception is thrown when the specified OAuth flow is not valid."""

    code: str = "InvalidOAuthFlowException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterException(ServiceException):
    """This exception is thrown when the Amazon Cognito service encounters an
    invalid parameter.
    """

    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400
    reasonCode: Optional[InvalidParameterExceptionReasonCodeType]


class InvalidPasswordException(ServiceException):
    """This exception is thrown when Amazon Cognito encounters an invalid
    password.
    """

    code: str = "InvalidPasswordException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSmsRoleAccessPolicyException(ServiceException):
    """This exception is returned when the role provided for SMS configuration
    doesn't have permission to publish using Amazon SNS.
    """

    code: str = "InvalidSmsRoleAccessPolicyException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSmsRoleTrustRelationshipException(ServiceException):
    """This exception is thrown when the trust relationship is not valid for
    the role provided for SMS configuration. This can happen if you don't
    trust ``cognito-idp.amazonaws.com`` or the external ID provided in the
    role does not match what is provided in the SMS configuration for the
    user pool.
    """

    code: str = "InvalidSmsRoleTrustRelationshipException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidUserPoolConfigurationException(ServiceException):
    """This exception is thrown when the user pool configuration is not valid."""

    code: str = "InvalidUserPoolConfigurationException"
    sender_fault: bool = False
    status_code: int = 400


class LimitExceededException(ServiceException):
    """This exception is thrown when a user exceeds the limit for a requested
    Amazon Web Services resource.
    """

    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class MFAMethodNotFoundException(ServiceException):
    """This exception is thrown when Amazon Cognito can't find a multi-factor
    authentication (MFA) method.
    """

    code: str = "MFAMethodNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ManagedLoginBrandingExistsException(ServiceException):
    """This exception is thrown when you attempt to apply a managed login
    branding style to an app client that already has an assigned style.
    """

    code: str = "ManagedLoginBrandingExistsException"
    sender_fault: bool = False
    status_code: int = 400


class NotAuthorizedException(ServiceException):
    """This exception is thrown when a user isn't authorized."""

    code: str = "NotAuthorizedException"
    sender_fault: bool = False
    status_code: int = 400


class PasswordHistoryPolicyViolationException(ServiceException):
    """The message returned when a user's new password matches a previous
    password and doesn't comply with the password-history policy.
    """

    code: str = "PasswordHistoryPolicyViolationException"
    sender_fault: bool = False
    status_code: int = 400


class PasswordResetRequiredException(ServiceException):
    """This exception is thrown when a password reset is required."""

    code: str = "PasswordResetRequiredException"
    sender_fault: bool = False
    status_code: int = 400


class PreconditionNotMetException(ServiceException):
    """This exception is thrown when a precondition is not met."""

    code: str = "PreconditionNotMetException"
    sender_fault: bool = False
    status_code: int = 400


class RefreshTokenReuseException(ServiceException):
    """This exception is throw when your application requests token refresh
    with a refresh token that has been invalidated by refresh-token
    rotation.
    """

    code: str = "RefreshTokenReuseException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """This exception is thrown when the Amazon Cognito service can't find the
    requested resource.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ScopeDoesNotExistException(ServiceException):
    """This exception is thrown when the specified scope doesn't exist."""

    code: str = "ScopeDoesNotExistException"
    sender_fault: bool = False
    status_code: int = 400


class SoftwareTokenMFANotFoundException(ServiceException):
    """This exception is thrown when the software token time-based one-time
    password (TOTP) multi-factor authentication (MFA) isn't activated for
    the user pool.
    """

    code: str = "SoftwareTokenMFANotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class TierChangeNotAllowedException(ServiceException):
    """This exception is thrown when you've attempted to change your feature
    plan but the operation isn't permitted.
    """

    code: str = "TierChangeNotAllowedException"
    sender_fault: bool = False
    status_code: int = 400


class TooManyFailedAttemptsException(ServiceException):
    """This exception is thrown when the user has made too many failed attempts
    for a given action, such as sign-in.
    """

    code: str = "TooManyFailedAttemptsException"
    sender_fault: bool = False
    status_code: int = 400


class TooManyRequestsException(ServiceException):
    """This exception is thrown when the user has made too many requests for a
    given operation.
    """

    code: str = "TooManyRequestsException"
    sender_fault: bool = False
    status_code: int = 400


class UnauthorizedException(ServiceException):
    """Exception that is thrown when the request isn't authorized. This can
    happen due to an invalid access token in the request.
    """

    code: str = "UnauthorizedException"
    sender_fault: bool = False
    status_code: int = 400


class UnexpectedLambdaException(ServiceException):
    """This exception is thrown when Amazon Cognito encounters an unexpected
    exception with Lambda.
    """

    code: str = "UnexpectedLambdaException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedIdentityProviderException(ServiceException):
    """This exception is thrown when the specified identifier isn't supported."""

    code: str = "UnsupportedIdentityProviderException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedOperationException(ServiceException):
    """Exception that is thrown when you attempt to perform an operation that
    isn't enabled for the user pool client.
    """

    code: str = "UnsupportedOperationException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedTokenTypeException(ServiceException):
    """Exception that is thrown when an unsupported token is passed to an
    operation.
    """

    code: str = "UnsupportedTokenTypeException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedUserStateException(ServiceException):
    """The request failed because the user is in an unsupported state."""

    code: str = "UnsupportedUserStateException"
    sender_fault: bool = False
    status_code: int = 400


class UserImportInProgressException(ServiceException):
    """This exception is thrown when you're trying to modify a user pool while
    a user import job is in progress for that pool.
    """

    code: str = "UserImportInProgressException"
    sender_fault: bool = False
    status_code: int = 400


class UserLambdaValidationException(ServiceException):
    """This exception is thrown when the Amazon Cognito service encounters a
    user validation exception with the Lambda service.
    """

    code: str = "UserLambdaValidationException"
    sender_fault: bool = False
    status_code: int = 400


class UserNotConfirmedException(ServiceException):
    """This exception is thrown when a user isn't confirmed successfully."""

    code: str = "UserNotConfirmedException"
    sender_fault: bool = False
    status_code: int = 400


class UserNotFoundException(ServiceException):
    """This exception is thrown when a user isn't found."""

    code: str = "UserNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class UserPoolAddOnNotEnabledException(ServiceException):
    """This exception is thrown when user pool add-ons aren't enabled."""

    code: str = "UserPoolAddOnNotEnabledException"
    sender_fault: bool = False
    status_code: int = 400


class UserPoolTaggingException(ServiceException):
    """This exception is thrown when a user pool tag can't be set or updated."""

    code: str = "UserPoolTaggingException"
    sender_fault: bool = False
    status_code: int = 400


class UsernameExistsException(ServiceException):
    """This exception is thrown when Amazon Cognito encounters a user name that
    already exists in the user pool.
    """

    code: str = "UsernameExistsException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnChallengeNotFoundException(ServiceException):
    """This exception is thrown when the challenge from ``StartWebAuthn``
    registration has expired.
    """

    code: str = "WebAuthnChallengeNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnClientMismatchException(ServiceException):
    """This exception is thrown when the access token is for a different client
    than the one in the original ``StartWebAuthnRegistration`` request.
    """

    code: str = "WebAuthnClientMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnConfigurationMissingException(ServiceException):
    """This exception is thrown when a user pool doesn't have a configured
    relying party id or a user pool domain.
    """

    code: str = "WebAuthnConfigurationMissingException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnCredentialNotSupportedException(ServiceException):
    """This exception is thrown when a user presents passkey credentials from
    an unsupported device or provider.
    """

    code: str = "WebAuthnCredentialNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnNotEnabledException(ServiceException):
    """This exception is thrown when the passkey feature isn't enabled for the
    user pool.
    """

    code: str = "WebAuthnNotEnabledException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnOriginNotAllowedException(ServiceException):
    """This exception is thrown when the passkey credential's registration
    origin does not align with the user pool relying party id.
    """

    code: str = "WebAuthnOriginNotAllowedException"
    sender_fault: bool = False
    status_code: int = 400


class WebAuthnRelyingPartyMismatchException(ServiceException):
    """This exception is thrown when the given passkey credential is associated
    with a different relying party ID than the user pool relying party ID.
    """

    code: str = "WebAuthnRelyingPartyMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class RecoveryOptionType(TypedDict, total=False):
    """A recovery option for a user. The ``AccountRecoverySettingType`` data
    type is an array of this object. Each ``RecoveryOptionType`` has a
    priority property that determines whether it is a primary or secondary
    option.

    For example, if ``verified_email`` has a priority of ``1`` and
    ``verified_phone_number`` has a priority of ``2``, your user pool sends
    account-recovery messages to a verified email address but falls back to
    an SMS message if the user has a verified phone number. The
    ``admin_only`` option prevents self-service account recovery.
    """

    Priority: PriorityType
    Name: RecoveryOptionNameType


RecoveryMechanismsType = List[RecoveryOptionType]


class AccountRecoverySettingType(TypedDict, total=False):
    """The settings for user message delivery in forgot-password operations.
    Contains preference for email or SMS message delivery of password reset
    codes, or for admin-only password reset.
    """

    RecoveryMechanisms: Optional[RecoveryMechanismsType]


class AccountTakeoverActionType(TypedDict, total=False):
    """The automated response to a risk level for adaptive authentication in
    full-function, or ``ENFORCED``, mode. You can assign an action to each
    risk level that threat protection evaluates.
    """

    Notify: AccountTakeoverActionNotifyType
    EventAction: AccountTakeoverEventActionType


class AccountTakeoverActionsType(TypedDict, total=False):
    """A list of account-takeover actions for each level of risk that Amazon
    Cognito might assess with threat protection features.
    """

    LowAction: Optional[AccountTakeoverActionType]
    MediumAction: Optional[AccountTakeoverActionType]
    HighAction: Optional[AccountTakeoverActionType]


class NotifyEmailType(TypedDict, total=False):
    """The template for email messages that threat protection sends to a user
    when your threat protection automated response has a *Notify* action.
    """

    Subject: EmailNotificationSubjectType
    HtmlBody: Optional[EmailNotificationBodyType]
    TextBody: Optional[EmailNotificationBodyType]


class NotifyConfigurationType(TypedDict, total=False):
    """The configuration for Amazon SES email messages that threat protection
    sends to a user when your adaptive authentication automated response has
    a *Notify* action.
    """

    From: Optional[StringType]
    ReplyTo: Optional[StringType]
    SourceArn: ArnType
    BlockEmail: Optional[NotifyEmailType]
    NoActionEmail: Optional[NotifyEmailType]
    MfaEmail: Optional[NotifyEmailType]


class AccountTakeoverRiskConfigurationType(TypedDict, total=False):
    """The settings for automated responses and notification templates for
    adaptive authentication with threat protection features.
    """

    NotifyConfiguration: Optional[NotifyConfigurationType]
    Actions: AccountTakeoverActionsType


class StringAttributeConstraintsType(TypedDict, total=False):
    """The minimum and maximum length values of an attribute that is of the
    string type, for example ``custom:department``.
    """

    MinLength: Optional[StringType]
    MaxLength: Optional[StringType]


class NumberAttributeConstraintsType(TypedDict, total=False):
    """The minimum and maximum values of an attribute that is of the number
    type, for example ``custom:age``.
    """

    MinValue: Optional[StringType]
    MaxValue: Optional[StringType]


class SchemaAttributeType(TypedDict, total=False):
    """A list of the user attributes and their properties in your user pool.
    The attribute schema contains standard attributes, custom attributes
    with a ``custom:`` prefix, and developer attributes with a ``dev:``
    prefix. For more information, see `User pool
    attributes <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html>`__.

    Developer-only ``dev:`` attributes are a legacy feature of user pools,
    and are read-only to all app clients. You can create and update
    developer-only attributes only with IAM-authenticated API operations.
    Use app client read/write permissions instead.
    """

    Name: Optional[CustomAttributeNameType]
    AttributeDataType: Optional[AttributeDataType]
    DeveloperOnlyAttribute: Optional[BooleanType]
    Mutable: Optional[BooleanType]
    Required: Optional[BooleanType]
    NumberAttributeConstraints: Optional[NumberAttributeConstraintsType]
    StringAttributeConstraints: Optional[StringAttributeConstraintsType]


CustomAttributesListType = List[SchemaAttributeType]


class AddCustomAttributesRequest(ServiceRequest):
    """Represents the request to add custom attributes."""

    UserPoolId: UserPoolIdType
    CustomAttributes: CustomAttributesListType


class AddCustomAttributesResponse(TypedDict, total=False):
    """Represents the response from the server for the request to add custom
    attributes.
    """

    pass


class AdminAddUserToGroupRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Username: UsernameType
    GroupName: GroupNameType


ClientMetadataType = Dict[StringType, StringType]


class AdminConfirmSignUpRequest(ServiceRequest):
    """Confirm a user's registration as a user pool administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    ClientMetadata: Optional[ClientMetadataType]


class AdminConfirmSignUpResponse(TypedDict, total=False):
    """Represents the response from the server for the request to confirm
    registration.
    """

    pass


class MessageTemplateType(TypedDict, total=False):
    """The message template structure."""

    SMSMessage: Optional[SmsInviteMessageType]
    EmailMessage: Optional[EmailInviteMessageType]
    EmailSubject: Optional[EmailVerificationSubjectType]


class AdminCreateUserConfigType(TypedDict, total=False):
    """The settings for administrator creation of users in a user pool.
    Contains settings for allowing user sign-up, customizing invitation
    messages to new users, and the amount of time before temporary passwords
    expire.
    """

    AllowAdminCreateUserOnly: Optional[BooleanType]
    UnusedAccountValidityDays: Optional[AdminCreateUserUnusedAccountValidityDaysType]
    InviteMessageTemplate: Optional[MessageTemplateType]


DeliveryMediumListType = List[DeliveryMediumType]


class AttributeType(TypedDict, total=False):
    """The name and value of a user attribute."""

    Name: AttributeNameType
    Value: Optional[AttributeValueType]


AttributeListType = List[AttributeType]


class AdminCreateUserRequest(ServiceRequest):
    """Creates a new user in the specified user pool."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    UserAttributes: Optional[AttributeListType]
    ValidationData: Optional[AttributeListType]
    TemporaryPassword: Optional[PasswordType]
    ForceAliasCreation: Optional[ForceAliasCreation]
    MessageAction: Optional[MessageActionType]
    DesiredDeliveryMediums: Optional[DeliveryMediumListType]
    ClientMetadata: Optional[ClientMetadataType]


class MFAOptionType(TypedDict, total=False):
    """*This data type is no longer supported.* Applies only to SMS
    multi-factor authentication (MFA) configurations. Does not apply to
    time-based one-time password (TOTP) software token MFA configurations.
    """

    DeliveryMedium: Optional[DeliveryMediumType]
    AttributeName: Optional[AttributeNameType]


MFAOptionListType = List[MFAOptionType]
DateType = datetime


class UserType(TypedDict, total=False):
    """A user profile in a Amazon Cognito user pool."""

    Username: Optional[UsernameType]
    Attributes: Optional[AttributeListType]
    UserCreateDate: Optional[DateType]
    UserLastModifiedDate: Optional[DateType]
    Enabled: Optional[BooleanType]
    UserStatus: Optional[UserStatusType]
    MFAOptions: Optional[MFAOptionListType]


class AdminCreateUserResponse(TypedDict, total=False):
    """Represents the response from the server to the request to create the
    user.
    """

    User: Optional[UserType]


AttributeNameListType = List[AttributeNameType]


class AdminDeleteUserAttributesRequest(ServiceRequest):
    """Represents the request to delete user attributes as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    UserAttributeNames: AttributeNameListType


class AdminDeleteUserAttributesResponse(TypedDict, total=False):
    """Represents the response received from the server for a request to delete
    user attributes.
    """

    pass


class AdminDeleteUserRequest(ServiceRequest):
    """Represents the request to delete a user as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType


class ProviderUserIdentifierType(TypedDict, total=False):
    """The characteristics of a source or destination user for linking a
    federated user profile to a local user profile.
    """

    ProviderName: Optional[ProviderNameType]
    ProviderAttributeName: Optional[StringType]
    ProviderAttributeValue: Optional[StringType]


class AdminDisableProviderForUserRequest(ServiceRequest):
    UserPoolId: StringType
    User: ProviderUserIdentifierType


class AdminDisableProviderForUserResponse(TypedDict, total=False):
    pass


class AdminDisableUserRequest(ServiceRequest):
    """Represents the request to disable the user as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType


class AdminDisableUserResponse(TypedDict, total=False):
    """Represents the response received from the server to disable the user as
    an administrator.
    """

    pass


class AdminEnableUserRequest(ServiceRequest):
    """Represents the request that enables the user as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType


class AdminEnableUserResponse(TypedDict, total=False):
    """Represents the response from the server for the request to enable a user
    as an administrator.
    """

    pass


class AdminForgetDeviceRequest(ServiceRequest):
    """Sends the forgot device request, as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    DeviceKey: DeviceKeyType


class AdminGetDeviceRequest(ServiceRequest):
    """Represents the request to get the device, as an administrator."""

    DeviceKey: DeviceKeyType
    UserPoolId: UserPoolIdType
    Username: UsernameType


class DeviceType(TypedDict, total=False):
    """Information about a user's device that they've registered for device SRP
    authentication in your application. For more information, see `Working
    with user devices in your user
    pool <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.
    """

    DeviceKey: Optional[DeviceKeyType]
    DeviceAttributes: Optional[AttributeListType]
    DeviceCreateDate: Optional[DateType]
    DeviceLastModifiedDate: Optional[DateType]
    DeviceLastAuthenticatedDate: Optional[DateType]


class AdminGetDeviceResponse(TypedDict, total=False):
    """Gets the device response, as an administrator."""

    Device: DeviceType


class AdminGetUserRequest(ServiceRequest):
    """Represents the request to get the specified user as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType


UserMFASettingListType = List[StringType]


class AdminGetUserResponse(TypedDict, total=False):
    """Represents the response from the server from the request to get the
    specified user as an administrator.
    """

    Username: UsernameType
    UserAttributes: Optional[AttributeListType]
    UserCreateDate: Optional[DateType]
    UserLastModifiedDate: Optional[DateType]
    Enabled: Optional[BooleanType]
    UserStatus: Optional[UserStatusType]
    MFAOptions: Optional[MFAOptionListType]
    PreferredMfaSetting: Optional[StringType]
    UserMFASettingList: Optional[UserMFASettingListType]


class HttpHeader(TypedDict, total=False):
    """The HTTP header in the ``ContextData`` parameter."""

    headerName: Optional[StringType]
    headerValue: Optional[StringType]


HttpHeaderList = List[HttpHeader]


class ContextDataType(TypedDict, total=False):
    """Contextual user data used for evaluating the risk of an authentication
    event by user pool threat protection.
    """

    IpAddress: StringType
    ServerName: StringType
    ServerPath: StringType
    HttpHeaders: HttpHeaderList
    EncodedData: Optional[StringType]


class AnalyticsMetadataType(TypedDict, total=False):
    """Information that your application adds to authentication requests.
    Applies an endpoint ID to the analytics data that your user pool sends
    to Amazon Pinpoint.

    An endpoint ID uniquely identifies a mobile device, email address or
    phone number that can receive messages from Amazon Pinpoint analytics.
    For more information about Amazon Web Services Regions that can contain
    Amazon Pinpoint resources for use with Amazon Cognito user pools, see
    `Using Amazon Pinpoint analytics with Amazon Cognito user
    pools <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html>`__.
    """

    AnalyticsEndpointId: Optional[StringType]


AuthParametersType = Dict[StringType, StringType]


class AdminInitiateAuthRequest(ServiceRequest):
    """Initiates the authorization request, as an administrator."""

    UserPoolId: UserPoolIdType
    ClientId: ClientIdType
    AuthFlow: AuthFlowType
    AuthParameters: Optional[AuthParametersType]
    ClientMetadata: Optional[ClientMetadataType]
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    ContextData: Optional[ContextDataType]
    Session: Optional[SessionType]


AvailableChallengeListType = List[ChallengeNameType]


class NewDeviceMetadataType(TypedDict, total=False):
    """Information that your user pool responds with in
    ``AuthenticationResult`` when you configure it to remember devices and
    a user signs in with an unrecognized device. Amazon Cognito presents a
    new device key that you can use to set up `device
    authentication <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__
    in a "Remember me on this device" authentication model.
    """

    DeviceKey: Optional[DeviceKeyType]
    DeviceGroupKey: Optional[StringType]


class AuthenticationResultType(TypedDict, total=False):
    """The object that your application receives after authentication. Contains
    tokens and information for device authentication.
    """

    AccessToken: Optional[TokenModelType]
    ExpiresIn: Optional[IntegerType]
    TokenType: Optional[StringType]
    RefreshToken: Optional[TokenModelType]
    IdToken: Optional[TokenModelType]
    NewDeviceMetadata: Optional[NewDeviceMetadataType]


ChallengeParametersType = Dict[StringType, StringType]


class AdminInitiateAuthResponse(TypedDict, total=False):
    """Initiates the authentication response, as an administrator."""

    ChallengeName: Optional[ChallengeNameType]
    Session: Optional[SessionType]
    ChallengeParameters: Optional[ChallengeParametersType]
    AuthenticationResult: Optional[AuthenticationResultType]
    AvailableChallenges: Optional[AvailableChallengeListType]


class AdminLinkProviderForUserRequest(ServiceRequest):
    UserPoolId: StringType
    DestinationUser: ProviderUserIdentifierType
    SourceUser: ProviderUserIdentifierType


class AdminLinkProviderForUserResponse(TypedDict, total=False):
    pass


class AdminListDevicesRequest(ServiceRequest):
    """Represents the request to list devices, as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    Limit: Optional[QueryLimitType]
    PaginationToken: Optional[SearchPaginationTokenType]


DeviceListType = List[DeviceType]


class AdminListDevicesResponse(TypedDict, total=False):
    """Lists the device's response, as an administrator."""

    Devices: Optional[DeviceListType]
    PaginationToken: Optional[SearchPaginationTokenType]


class AdminListGroupsForUserRequest(ServiceRequest):
    Username: UsernameType
    UserPoolId: UserPoolIdType
    Limit: Optional[QueryLimitType]
    NextToken: Optional[PaginationKey]


class GroupType(TypedDict, total=False):
    """A user pool group. Contains details about the group and the way that it
    contributes to IAM role decisions with identity pools. Identity pools
    can make decisions about the IAM role to assign based on groups: users
    get credentials for the role associated with their highest-priority
    group.
    """

    GroupName: Optional[GroupNameType]
    UserPoolId: Optional[UserPoolIdType]
    Description: Optional[DescriptionType]
    RoleArn: Optional[ArnType]
    Precedence: Optional[PrecedenceType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]


GroupListType = List[GroupType]


class AdminListGroupsForUserResponse(TypedDict, total=False):
    Groups: Optional[GroupListType]
    NextToken: Optional[PaginationKey]


class AdminListUserAuthEventsRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Username: UsernameType
    MaxResults: Optional[QueryLimitType]
    NextToken: Optional[PaginationKey]


class EventFeedbackType(TypedDict, total=False):
    """The feedback that your application submitted to a threat protection
    event log, as displayed in an ``AdminListUserAuthEvents`` response.
    """

    FeedbackValue: FeedbackValueType
    Provider: StringType
    FeedbackDate: Optional[DateType]


class EventContextDataType(TypedDict, total=False):
    """The context data that your application submitted in an authentication
    request with threat protection, as displayed in an
    ``AdminListUserAuthEvents`` response.
    """

    IpAddress: Optional[StringType]
    DeviceName: Optional[StringType]
    Timezone: Optional[StringType]
    City: Optional[StringType]
    Country: Optional[StringType]


class ChallengeResponseType(TypedDict, total=False):
    """The responses to the challenge that you received in the previous
    request. Each challenge has its own required response parameters. The
    following examples are partial JSON request bodies that highlight
    challenge-response parameters.

    You must provide a SECRET_HASH parameter in all challenge responses to
    an app client that has a client secret. Include a ``DEVICE_KEY`` for
    device authentication.

    SELECT_CHALLENGE
       ``"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "USERNAME": "[username]", "ANSWER": "[Challenge name]"}``

       Available challenges are ``PASSWORD``, ``PASSWORD_SRP``,
       ``EMAIL_OTP``, ``SMS_OTP``, and ``WEB_AUTHN``.

       Complete authentication in the ``SELECT_CHALLENGE`` response for
       ``PASSWORD``, ``PASSWORD_SRP``, and ``WEB_AUTHN``:

       -  ``"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "WEB_AUTHN", "USERNAME": "[username]", "CREDENTIAL": "[AuthenticationResponseJSON]"}``

          See
          `AuthenticationResponseJSON <https://www.w3.org/TR/WebAuthn-3/#dictdef-authenticationresponsejson>`__.

       -  ``"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "PASSWORD", "USERNAME": "[username]", "PASSWORD": "[password]"}``

       -  ``"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "PASSWORD_SRP", "USERNAME": "[username]", "SRP_A": "[SRP_A]"}``

       For ``SMS_OTP`` and ``EMAIL_OTP``, respond with the username and
       answer. Your user pool will send a code for the user to submit in the
       next challenge response.

       -  ``"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "SMS_OTP", "USERNAME": "[username]"}``

       -  ``"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "EMAIL_OTP", "USERNAME": "[username]"}``

    SMS_OTP
       ``"ChallengeName": "SMS_OTP", "ChallengeResponses": {"SMS_OTP_CODE": "[code]", "USERNAME": "[username]"}``

    EMAIL_OTP
       ``"ChallengeName": "EMAIL_OTP", "ChallengeResponses": {"EMAIL_OTP_CODE": "[code]", "USERNAME": "[username]"}``

    SMS_MFA
       ``"ChallengeName": "SMS_MFA", "ChallengeResponses": {"SMS_MFA_CODE": "[code]", "USERNAME": "[username]"}``

    PASSWORD_VERIFIER
       This challenge response is part of the SRP flow. Amazon Cognito
       requires that your application respond to this challenge within a few
       seconds. When the response time exceeds this period, your user pool
       returns a ``NotAuthorizedException`` error.

       ``"ChallengeName": "PASSWORD_VERIFIER", "ChallengeResponses": {"PASSWORD_CLAIM_SIGNATURE": "[claim_signature]", "PASSWORD_CLAIM_SECRET_BLOCK": "[secret_block]", "TIMESTAMP": [timestamp], "USERNAME": "[username]"}``

       Add ``"DEVICE_KEY"`` when you sign in with a remembered device.

    CUSTOM_CHALLENGE
       ``"ChallengeName": "CUSTOM_CHALLENGE", "ChallengeResponses": {"USERNAME": "[username]", "ANSWER": "[challenge_answer]"}``

       Add ``"DEVICE_KEY"`` when you sign in with a remembered device.

    NEW_PASSWORD_REQUIRED
       ``"ChallengeName": "NEW_PASSWORD_REQUIRED", "ChallengeResponses": {"NEW_PASSWORD": "[new_password]", "USERNAME": "[username]"}``

       To set any required attributes that ``InitiateAuth`` returned in an
       ``requiredAttributes`` parameter, add
       ``"userAttributes.[attribute_name]": "[attribute_value]"``. This
       parameter can also set values for writable attributes that aren't
       required by your user pool.

       In a ``NEW_PASSWORD_REQUIRED`` challenge response, you can't modify a
       required attribute that already has a value. In
       ``AdminRespondToAuthChallenge`` or ``RespondToAuthChallenge``, set a
       value for any keys that Amazon Cognito returned in the
       ``requiredAttributes`` parameter, then use the
       ``AdminUpdateUserAttributes`` or ``UpdateUserAttributes`` API
       operation to modify the value of any additional attributes.

    SOFTWARE_TOKEN_MFA
       ``"ChallengeName": "SOFTWARE_TOKEN_MFA", "ChallengeResponses": {"USERNAME": "[username]", "SOFTWARE_TOKEN_MFA_CODE": [authenticator_code]}``

    DEVICE_SRP_AUTH
       ``"ChallengeName": "DEVICE_SRP_AUTH", "ChallengeResponses": {"USERNAME": "[username]", "DEVICE_KEY": "[device_key]", "SRP_A": "[srp_a]"}``

    DEVICE_PASSWORD_VERIFIER
       ``"ChallengeName": "DEVICE_PASSWORD_VERIFIER", "ChallengeResponses": {"DEVICE_KEY": "[device_key]", "PASSWORD_CLAIM_SIGNATURE": "[claim_signature]", "PASSWORD_CLAIM_SECRET_BLOCK": "[secret_block]", "TIMESTAMP": [timestamp], "USERNAME": "[username]"}``

    MFA_SETUP
       ``"ChallengeName": "MFA_SETUP", "ChallengeResponses": {"USERNAME": "[username]"}, "SESSION": "[Session ID from VerifySoftwareToken]"``

    SELECT_MFA_TYPE
       ``"ChallengeName": "SELECT_MFA_TYPE", "ChallengeResponses": {"USERNAME": "[username]", "ANSWER": "[SMS_MFA or SOFTWARE_TOKEN_MFA]"}``

    For more information about ``SECRET_HASH``, see `Computing secret hash
    values <https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash>`__.
    For information about ``DEVICE_KEY``, see `Working with user devices in
    your user
    pool <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.
    """

    ChallengeName: Optional[ChallengeName]
    ChallengeResponse: Optional[ChallengeResponse]


ChallengeResponseListType = List[ChallengeResponseType]


class EventRiskType(TypedDict, total=False):
    """The risk evaluation by adaptive authentication, as displayed in an
    ``AdminListUserAuthEvents`` response. Contains evaluations of
    compromised-credentials detection and assessed risk level and action
    taken by adaptive authentication.
    """

    RiskDecision: Optional[RiskDecisionType]
    RiskLevel: Optional[RiskLevelType]
    CompromisedCredentialsDetected: Optional[WrappedBooleanType]


class AuthEventType(TypedDict, total=False):
    """One authentication event that Amazon Cognito logged in a user pool with
    threat protection active. Contains user and device metadata and a risk
    assessment from your user pool.
    """

    EventId: Optional[StringType]
    EventType: Optional[EventType]
    CreationDate: Optional[DateType]
    EventResponse: Optional[EventResponseType]
    EventRisk: Optional[EventRiskType]
    ChallengeResponses: Optional[ChallengeResponseListType]
    EventContextData: Optional[EventContextDataType]
    EventFeedback: Optional[EventFeedbackType]


AuthEventsType = List[AuthEventType]


class AdminListUserAuthEventsResponse(TypedDict, total=False):
    AuthEvents: Optional[AuthEventsType]
    NextToken: Optional[PaginationKey]


class AdminRemoveUserFromGroupRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Username: UsernameType
    GroupName: GroupNameType


class AdminResetUserPasswordRequest(ServiceRequest):
    """Represents the request to reset a user's password as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    ClientMetadata: Optional[ClientMetadataType]


class AdminResetUserPasswordResponse(TypedDict, total=False):
    """Represents the response from the server to reset a user password as an
    administrator.
    """

    pass


ChallengeResponsesType = Dict[StringType, StringType]


class AdminRespondToAuthChallengeRequest(ServiceRequest):
    """The request to respond to the authentication challenge, as an
    administrator.
    """

    UserPoolId: UserPoolIdType
    ClientId: ClientIdType
    ChallengeName: ChallengeNameType
    ChallengeResponses: Optional[ChallengeResponsesType]
    Session: Optional[SessionType]
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    ContextData: Optional[ContextDataType]
    ClientMetadata: Optional[ClientMetadataType]


class AdminRespondToAuthChallengeResponse(TypedDict, total=False):
    """Responds to the authentication challenge, as an administrator."""

    ChallengeName: Optional[ChallengeNameType]
    Session: Optional[SessionType]
    ChallengeParameters: Optional[ChallengeParametersType]
    AuthenticationResult: Optional[AuthenticationResultType]


class EmailMfaSettingsType(TypedDict, total=False):
    """User preferences for multi-factor authentication with email messages.
    Activates or deactivates email MFA and sets it as the preferred MFA
    method when multiple methods are available. To activate this setting,
    your user pool must be in the `Essentials
    tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html>`__
    or higher.
    """

    Enabled: Optional[BooleanType]
    PreferredMfa: Optional[BooleanType]


class SoftwareTokenMfaSettingsType(TypedDict, total=False):
    """A user's preference for using time-based one-time password (TOTP)
    multi-factor authentication (MFA). Turns TOTP MFA on and off, and can
    set TOTP as preferred when other MFA options are available. You can't
    turn off TOTP MFA for any of your users when MFA is required in your
    user pool; you can only set the type that your user prefers.
    """

    Enabled: Optional[BooleanType]
    PreferredMfa: Optional[BooleanType]


class SMSMfaSettingsType(TypedDict, total=False):
    """A user's preference for using SMS message multi-factor authentication
    (MFA). Turns SMS MFA on and off, and can set SMS as preferred when other
    MFA options are available. You can't turn off SMS MFA for any of your
    users when MFA is required in your user pool; you can only set the type
    that your user prefers.
    """

    Enabled: Optional[BooleanType]
    PreferredMfa: Optional[BooleanType]


class AdminSetUserMFAPreferenceRequest(ServiceRequest):
    SMSMfaSettings: Optional[SMSMfaSettingsType]
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsType]
    EmailMfaSettings: Optional[EmailMfaSettingsType]
    Username: UsernameType
    UserPoolId: UserPoolIdType


class AdminSetUserMFAPreferenceResponse(TypedDict, total=False):
    pass


class AdminSetUserPasswordRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Username: UsernameType
    Password: PasswordType
    Permanent: Optional[BooleanType]


class AdminSetUserPasswordResponse(TypedDict, total=False):
    pass


class AdminSetUserSettingsRequest(ServiceRequest):
    """You can use this parameter to set an MFA configuration that uses the SMS
    delivery medium.
    """

    UserPoolId: UserPoolIdType
    Username: UsernameType
    MFAOptions: MFAOptionListType


class AdminSetUserSettingsResponse(TypedDict, total=False):
    """Represents the response from the server to set user settings as an
    administrator.
    """

    pass


class AdminUpdateAuthEventFeedbackRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Username: UsernameType
    EventId: EventIdType
    FeedbackValue: FeedbackValueType


class AdminUpdateAuthEventFeedbackResponse(TypedDict, total=False):
    pass


class AdminUpdateDeviceStatusRequest(ServiceRequest):
    """The request to update the device status, as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType
    DeviceKey: DeviceKeyType
    DeviceRememberedStatus: Optional[DeviceRememberedStatusType]


class AdminUpdateDeviceStatusResponse(TypedDict, total=False):
    """The status response to the request to update the device, as an
    administrator.
    """

    pass


class AdminUpdateUserAttributesRequest(ServiceRequest):
    """Represents the request to update the user's attributes as an
    administrator.
    """

    UserPoolId: UserPoolIdType
    Username: UsernameType
    UserAttributes: AttributeListType
    ClientMetadata: Optional[ClientMetadataType]


class AdminUpdateUserAttributesResponse(TypedDict, total=False):
    """Represents the response from the server for the request to update user
    attributes as an administrator.
    """

    pass


class AdminUserGlobalSignOutRequest(ServiceRequest):
    """The request to sign out of all devices, as an administrator."""

    UserPoolId: UserPoolIdType
    Username: UsernameType


class AdminUserGlobalSignOutResponse(TypedDict, total=False):
    """The global sign-out response, as an administrator."""

    pass


class AdvancedSecurityAdditionalFlowsType(TypedDict, total=False):
    """Threat protection configuration options for additional authentication
    types in your user pool, including custom authentication.
    """

    CustomAuthMode: Optional[AdvancedSecurityEnabledModeType]


AliasAttributesListType = List[AliasAttributeType]
AllowedFirstAuthFactorsListType = List[AuthFactorType]


class AnalyticsConfigurationType(TypedDict, total=False):
    """The settings for Amazon Pinpoint analytics configuration. With an
    analytics configuration, your application can collect user-activity
    metrics for user notifications with a Amazon Pinpoint campaign.

    Amazon Pinpoint isn't available in all Amazon Web Services Regions. For
    a list of available Regions, see `Amazon Cognito and Amazon Pinpoint
    Region
    availability <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html#cognito-user-pools-find-region-mappings>`__.
    """

    ApplicationId: Optional[HexStringType]
    ApplicationArn: Optional[ArnType]
    RoleArn: Optional[ArnType]
    ExternalId: Optional[StringType]
    UserDataShared: Optional[BooleanType]


AssetBytesType = bytes


class AssetType(TypedDict, total=False):
    """An image file from a managed login branding style in a user pool."""

    Category: AssetCategoryType
    ColorMode: ColorSchemeModeType
    Extension: AssetExtensionType
    Bytes: Optional[AssetBytesType]
    ResourceId: Optional[ResourceIdType]


AssetListType = List[AssetType]


class AssociateSoftwareTokenRequest(ServiceRequest):
    AccessToken: Optional[TokenModelType]
    Session: Optional[SessionType]


class AssociateSoftwareTokenResponse(TypedDict, total=False):
    SecretCode: Optional[SecretCodeType]
    Session: Optional[SessionType]


AttributeMappingType = Dict[AttributeMappingKeyType, StringType]
AttributesRequireVerificationBeforeUpdateType = List[VerifiedAttributeType]
BlockedIPRangeListType = List[StringType]
CallbackURLsListType = List[RedirectUrlType]


class ChangePasswordRequest(ServiceRequest):
    """Represents the request to change a user password."""

    PreviousPassword: Optional[PasswordType]
    ProposedPassword: PasswordType
    AccessToken: TokenModelType


class ChangePasswordResponse(TypedDict, total=False):
    """The response from the server to the change password request."""

    pass


ClientPermissionListType = List[ClientPermissionType]


class CloudWatchLogsConfigurationType(TypedDict, total=False):
    """Configuration for the CloudWatch log group destination of user pool
    detailed activity logging, or of user activity log export with threat
    protection.
    """

    LogGroupArn: Optional[ArnType]


class CodeDeliveryDetailsType(TypedDict, total=False):
    """The delivery details for an email or SMS message that Amazon Cognito
    sent for authentication or verification.
    """

    Destination: Optional[StringType]
    DeliveryMedium: Optional[DeliveryMediumType]
    AttributeName: Optional[AttributeNameType]


CodeDeliveryDetailsListType = List[CodeDeliveryDetailsType]


class Document(TypedDict, total=False):
    pass


class CompleteWebAuthnRegistrationRequest(ServiceRequest):
    AccessToken: TokenModelType
    Credential: Document


class CompleteWebAuthnRegistrationResponse(TypedDict, total=False):
    pass


class CompromisedCredentialsActionsType(TypedDict, total=False):
    """Settings for user pool actions when Amazon Cognito detects compromised
    credentials with threat protection in full-function ``ENFORCED`` mode.
    """

    EventAction: CompromisedCredentialsEventActionType


EventFiltersType = List[EventFilterType]


class CompromisedCredentialsRiskConfigurationType(TypedDict, total=False):
    """Settings for compromised-credentials actions and authentication-event
    sources with threat protection in full-function ``ENFORCED`` mode.
    """

    EventFilter: Optional[EventFiltersType]
    Actions: CompromisedCredentialsActionsType


ConfiguredUserAuthFactorsListType = List[AuthFactorType]


class DeviceSecretVerifierConfigType(TypedDict, total=False):
    """A Secure Remote Password (SRP) value that your application generates
    when you register a user's device. For more information, see `Getting a
    device
    key <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-getting-a-device-key>`__.
    """

    PasswordVerifier: Optional[StringType]
    Salt: Optional[StringType]


class ConfirmDeviceRequest(ServiceRequest):
    """The confirm-device request."""

    AccessToken: TokenModelType
    DeviceKey: DeviceKeyType
    DeviceSecretVerifierConfig: Optional[DeviceSecretVerifierConfigType]
    DeviceName: Optional[DeviceNameType]


class ConfirmDeviceResponse(TypedDict, total=False):
    """The confirm-device response."""

    UserConfirmationNecessary: Optional[BooleanType]


class UserContextDataType(TypedDict, total=False):
    """Contextual data, such as the user's device fingerprint, IP address, or
    location, used for evaluating the risk of an unexpected event by Amazon
    Cognito threat protection.
    """

    IpAddress: Optional[StringType]
    EncodedData: Optional[StringType]


class ConfirmForgotPasswordRequest(ServiceRequest):
    """The request representing the confirmation for a password reset."""

    ClientId: ClientIdType
    SecretHash: Optional[SecretHashType]
    Username: UsernameType
    ConfirmationCode: ConfirmationCodeType
    Password: PasswordType
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    UserContextData: Optional[UserContextDataType]
    ClientMetadata: Optional[ClientMetadataType]


class ConfirmForgotPasswordResponse(TypedDict, total=False):
    """The response from the server that results from a user's request to
    retrieve a forgotten password.
    """

    pass


class ConfirmSignUpRequest(ServiceRequest):
    """Represents the request to confirm registration of a user."""

    ClientId: ClientIdType
    SecretHash: Optional[SecretHashType]
    Username: UsernameType
    ConfirmationCode: ConfirmationCodeType
    ForceAliasCreation: Optional[ForceAliasCreation]
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    UserContextData: Optional[UserContextDataType]
    ClientMetadata: Optional[ClientMetadataType]
    Session: Optional[SessionType]


class ConfirmSignUpResponse(TypedDict, total=False):
    """Represents the response from the server for the registration
    confirmation.
    """

    Session: Optional[SessionType]


class CreateGroupRequest(ServiceRequest):
    GroupName: GroupNameType
    UserPoolId: UserPoolIdType
    Description: Optional[DescriptionType]
    RoleArn: Optional[ArnType]
    Precedence: Optional[PrecedenceType]


class CreateGroupResponse(TypedDict, total=False):
    Group: Optional[GroupType]


IdpIdentifiersListType = List[IdpIdentifierType]
ProviderDetailsType = Dict[StringType, StringType]


class CreateIdentityProviderRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ProviderName: ProviderNameTypeV2
    ProviderType: IdentityProviderTypeType
    ProviderDetails: ProviderDetailsType
    AttributeMapping: Optional[AttributeMappingType]
    IdpIdentifiers: Optional[IdpIdentifiersListType]


class IdentityProviderType(TypedDict, total=False):
    """A user pool identity provider (IdP). Contains information about a
    third-party IdP to a user pool, the attributes that it populates to user
    profiles, and the trust relationship between the IdP and your user pool.
    """

    UserPoolId: Optional[UserPoolIdType]
    ProviderName: Optional[ProviderNameType]
    ProviderType: Optional[IdentityProviderTypeType]
    ProviderDetails: Optional[ProviderDetailsType]
    AttributeMapping: Optional[AttributeMappingType]
    IdpIdentifiers: Optional[IdpIdentifiersListType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]


class CreateIdentityProviderResponse(TypedDict, total=False):
    IdentityProvider: IdentityProviderType


class CreateManagedLoginBrandingRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ClientId: ClientIdType
    UseCognitoProvidedValues: Optional[BooleanType]
    Settings: Optional[Document]
    Assets: Optional[AssetListType]


class ManagedLoginBrandingType(TypedDict, total=False):
    """A managed login branding style that's assigned to a user pool app
    client.
    """

    ManagedLoginBrandingId: Optional[ManagedLoginBrandingIdType]
    UserPoolId: Optional[UserPoolIdType]
    UseCognitoProvidedValues: Optional[BooleanType]
    Settings: Optional[Document]
    Assets: Optional[AssetListType]
    CreationDate: Optional[DateType]
    LastModifiedDate: Optional[DateType]


class CreateManagedLoginBrandingResponse(TypedDict, total=False):
    ManagedLoginBranding: Optional[ManagedLoginBrandingType]


class ResourceServerScopeType(TypedDict, total=False):
    """One custom scope associated with a user pool resource server. This data
    type is a member of ``ResourceServerScopeType``. For more information,
    see `Scopes, M2M, and API authorization with resource
    servers <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html>`__.
    """

    ScopeName: ResourceServerScopeNameType
    ScopeDescription: ResourceServerScopeDescriptionType


ResourceServerScopeListType = List[ResourceServerScopeType]


class CreateResourceServerRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Identifier: ResourceServerIdentifierType
    Name: ResourceServerNameType
    Scopes: Optional[ResourceServerScopeListType]


class ResourceServerType(TypedDict, total=False):
    """The details of a resource server configuration and associated custom
    scopes in a user pool.
    """

    UserPoolId: Optional[UserPoolIdType]
    Identifier: Optional[ResourceServerIdentifierType]
    Name: Optional[ResourceServerNameType]
    Scopes: Optional[ResourceServerScopeListType]


class CreateResourceServerResponse(TypedDict, total=False):
    ResourceServer: ResourceServerType


class CreateUserImportJobRequest(ServiceRequest):
    """Represents the request to create the user import job."""

    JobName: UserImportJobNameType
    UserPoolId: UserPoolIdType
    CloudWatchLogsRoleArn: ArnType


LongType = int


class UserImportJobType(TypedDict, total=False):
    """A user import job in a user pool. Describes the status of user import
    with a CSV file. For more information, see `Importing users into user
    pools from a CSV
    file <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html>`__.
    """

    JobName: Optional[UserImportJobNameType]
    JobId: Optional[UserImportJobIdType]
    UserPoolId: Optional[UserPoolIdType]
    PreSignedUrl: Optional[PreSignedUrlType]
    CreationDate: Optional[DateType]
    StartDate: Optional[DateType]
    CompletionDate: Optional[DateType]
    Status: Optional[UserImportJobStatusType]
    CloudWatchLogsRoleArn: Optional[ArnType]
    ImportedUsers: Optional[LongType]
    SkippedUsers: Optional[LongType]
    FailedUsers: Optional[LongType]
    CompletionMessage: Optional[CompletionMessageType]


class CreateUserImportJobResponse(TypedDict, total=False):
    """Represents the response from the server to the request to create the
    user import job.
    """

    UserImportJob: Optional[UserImportJobType]


class RefreshTokenRotationType(TypedDict, total=False):
    """The configuration of your app client for refresh token rotation. When
    enabled, your app client issues new ID, access, and refresh tokens when
    users renew their sessions with refresh tokens. When disabled, token
    refresh issues only ID and access tokens.
    """

    Feature: FeatureType
    RetryGracePeriodSeconds: Optional[RetryGracePeriodSecondsType]


ScopeListType = List[ScopeType]
OAuthFlowsType = List[OAuthFlowType]
LogoutURLsListType = List[RedirectUrlType]
SupportedIdentityProvidersListType = List[ProviderNameType]
ExplicitAuthFlowsListType = List[ExplicitAuthFlowsType]


class TokenValidityUnitsType(TypedDict, total=False):
    """The time units that, with ``IdTokenValidity``, ``AccessTokenValidity``,
    and ``RefreshTokenValidity``, set and display the duration of ID,
    access, and refresh tokens for an app client. You can assign a separate
    token validity unit to each type of token.
    """

    AccessToken: Optional[TimeUnitsType]
    IdToken: Optional[TimeUnitsType]
    RefreshToken: Optional[TimeUnitsType]


class CreateUserPoolClientRequest(ServiceRequest):
    """Represents the request to create a user pool client."""

    UserPoolId: UserPoolIdType
    ClientName: ClientNameType
    GenerateSecret: Optional[GenerateSecret]
    RefreshTokenValidity: Optional[RefreshTokenValidityType]
    AccessTokenValidity: Optional[AccessTokenValidityType]
    IdTokenValidity: Optional[IdTokenValidityType]
    TokenValidityUnits: Optional[TokenValidityUnitsType]
    ReadAttributes: Optional[ClientPermissionListType]
    WriteAttributes: Optional[ClientPermissionListType]
    ExplicitAuthFlows: Optional[ExplicitAuthFlowsListType]
    SupportedIdentityProviders: Optional[SupportedIdentityProvidersListType]
    CallbackURLs: Optional[CallbackURLsListType]
    LogoutURLs: Optional[LogoutURLsListType]
    DefaultRedirectURI: Optional[RedirectUrlType]
    AllowedOAuthFlows: Optional[OAuthFlowsType]
    AllowedOAuthScopes: Optional[ScopeListType]
    AllowedOAuthFlowsUserPoolClient: Optional[BooleanType]
    AnalyticsConfiguration: Optional[AnalyticsConfigurationType]
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypes]
    EnableTokenRevocation: Optional[WrappedBooleanType]
    EnablePropagateAdditionalUserContextData: Optional[WrappedBooleanType]
    AuthSessionValidity: Optional[AuthSessionValidityType]
    RefreshTokenRotation: Optional[RefreshTokenRotationType]


class UserPoolClientType(TypedDict, total=False):
    """The configuration of a user pool client."""

    UserPoolId: Optional[UserPoolIdType]
    ClientName: Optional[ClientNameType]
    ClientId: Optional[ClientIdType]
    ClientSecret: Optional[ClientSecretType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]
    RefreshTokenValidity: Optional[RefreshTokenValidityType]
    AccessTokenValidity: Optional[AccessTokenValidityType]
    IdTokenValidity: Optional[IdTokenValidityType]
    TokenValidityUnits: Optional[TokenValidityUnitsType]
    ReadAttributes: Optional[ClientPermissionListType]
    WriteAttributes: Optional[ClientPermissionListType]
    ExplicitAuthFlows: Optional[ExplicitAuthFlowsListType]
    SupportedIdentityProviders: Optional[SupportedIdentityProvidersListType]
    CallbackURLs: Optional[CallbackURLsListType]
    LogoutURLs: Optional[LogoutURLsListType]
    DefaultRedirectURI: Optional[RedirectUrlType]
    AllowedOAuthFlows: Optional[OAuthFlowsType]
    AllowedOAuthScopes: Optional[ScopeListType]
    AllowedOAuthFlowsUserPoolClient: Optional[BooleanType]
    AnalyticsConfiguration: Optional[AnalyticsConfigurationType]
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypes]
    EnableTokenRevocation: Optional[WrappedBooleanType]
    EnablePropagateAdditionalUserContextData: Optional[WrappedBooleanType]
    AuthSessionValidity: Optional[AuthSessionValidityType]
    RefreshTokenRotation: Optional[RefreshTokenRotationType]


class CreateUserPoolClientResponse(TypedDict, total=False):
    """Represents the response from the server to create a user pool client."""

    UserPoolClient: Optional[UserPoolClientType]


class CustomDomainConfigType(TypedDict, total=False):
    """The configuration for a hosted UI custom domain."""

    CertificateArn: ArnType


class CreateUserPoolDomainRequest(ServiceRequest):
    Domain: DomainType
    UserPoolId: UserPoolIdType
    ManagedLoginVersion: Optional[WrappedIntegerType]
    CustomDomainConfig: Optional[CustomDomainConfigType]


class CreateUserPoolDomainResponse(TypedDict, total=False):
    ManagedLoginVersion: Optional[WrappedIntegerType]
    CloudFrontDomain: Optional[DomainType]


class UsernameConfigurationType(TypedDict, total=False):
    """The configuration of a user pool for username case sensitivity."""

    CaseSensitive: WrappedBooleanType


class UserPoolAddOnsType(TypedDict, total=False):
    """Contains settings for activation of threat protection, including the
    operating mode and additional authentication types. To log user security
    information but take no action, set to ``AUDIT``. To configure automatic
    security responses to potentially unwanted traffic to your user pool,
    set to ``ENFORCED``.

    For more information, see `Adding advanced security to a user
    pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html>`__.
    To activate this setting, your user pool must be on the `Plus
    tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html>`__.
    """

    AdvancedSecurityMode: AdvancedSecurityModeType
    AdvancedSecurityAdditionalFlows: Optional[AdvancedSecurityAdditionalFlowsType]


SchemaAttributesListType = List[SchemaAttributeType]
UserPoolTagsType = Dict[TagKeysType, TagValueType]


class SmsConfigurationType(TypedDict, total=False):
    """User pool configuration for delivery of SMS messages with Amazon Simple
    Notification Service. To send SMS messages with Amazon SNS in the Amazon
    Web Services Region that you want, the Amazon Cognito user pool uses an
    Identity and Access Management (IAM) role in your Amazon Web Services
    account.
    """

    SnsCallerArn: ArnType
    ExternalId: Optional[StringType]
    SnsRegion: Optional[RegionCodeType]


class EmailConfigurationType(TypedDict, total=False):
    """The email configuration of your user pool. The email configuration type
    sets your preferred sending method, Amazon Web Services Region, and
    sender for messages from your user pool.

    Amazon Cognito can send email messages with Amazon Simple Email Service
    resources in the Amazon Web Services Region where you created your user
    pool, and in alternate Regions in some cases. For more information on
    the supported Regions, see `Email settings for Amazon Cognito user
    pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-email.html>`__.
    """

    SourceArn: Optional[ArnType]
    ReplyToEmailAddress: Optional[EmailAddressType]
    EmailSendingAccount: Optional[EmailSendingAccountType]
    From: Optional[StringType]
    ConfigurationSet: Optional[SESConfigurationSet]


class DeviceConfigurationType(TypedDict, total=False):
    """The device-remembering configuration for a user pool.

    When you provide a value for any property of ``DeviceConfiguration``,
    you activate the device remembering for the user pool.
    """

    ChallengeRequiredOnNewDevice: Optional[BooleanType]
    DeviceOnlyRememberedOnUserPrompt: Optional[BooleanType]


class UserAttributeUpdateSettingsType(TypedDict, total=False):
    """The settings for updates to user attributes. These settings include the
    property ``AttributesRequireVerificationBeforeUpdate``, a user-pool
    setting that tells Amazon Cognito how to handle changes to the value of
    your users' email address and phone number attributes. For more
    information, see `Verifying updates to email addresses and phone
    numbers <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates>`__.
    """

    AttributesRequireVerificationBeforeUpdate: Optional[
        AttributesRequireVerificationBeforeUpdateType
    ]


class VerificationMessageTemplateType(TypedDict, total=False):
    """The template for the verification message that your user pool delivers
    to users who set an email address or phone number attribute.
    """

    SmsMessage: Optional[SmsVerificationMessageType]
    EmailMessage: Optional[EmailVerificationMessageType]
    EmailSubject: Optional[EmailVerificationSubjectType]
    EmailMessageByLink: Optional[EmailVerificationMessageByLinkType]
    EmailSubjectByLink: Optional[EmailVerificationSubjectByLinkType]
    DefaultEmailOption: Optional[DefaultEmailOptionType]


UsernameAttributesListType = List[UsernameAttributeType]
VerifiedAttributesListType = List[VerifiedAttributeType]


class CustomEmailLambdaVersionConfigType(TypedDict, total=False):
    """The properties of a custom email sender Lambda trigger."""

    LambdaVersion: CustomEmailSenderLambdaVersionType
    LambdaArn: ArnType


class CustomSMSLambdaVersionConfigType(TypedDict, total=False):
    """The properties of a custom SMS sender Lambda trigger."""

    LambdaVersion: CustomSMSSenderLambdaVersionType
    LambdaArn: ArnType


class PreTokenGenerationVersionConfigType(TypedDict, total=False):
    """The properties of a pre token generation Lambda trigger."""

    LambdaVersion: PreTokenGenerationLambdaVersionType
    LambdaArn: ArnType


class LambdaConfigType(TypedDict, total=False):
    """A collection of user pool Lambda triggers. Amazon Cognito invokes
    triggers at several possible stages of user pool operations. Triggers
    can modify the outcome of the operations that invoked them.
    """

    PreSignUp: Optional[ArnType]
    CustomMessage: Optional[ArnType]
    PostConfirmation: Optional[ArnType]
    PreAuthentication: Optional[ArnType]
    PostAuthentication: Optional[ArnType]
    DefineAuthChallenge: Optional[ArnType]
    CreateAuthChallenge: Optional[ArnType]
    VerifyAuthChallengeResponse: Optional[ArnType]
    PreTokenGeneration: Optional[ArnType]
    UserMigration: Optional[ArnType]
    PreTokenGenerationConfig: Optional[PreTokenGenerationVersionConfigType]
    CustomSMSSender: Optional[CustomSMSLambdaVersionConfigType]
    CustomEmailSender: Optional[CustomEmailLambdaVersionConfigType]
    KMSKeyID: Optional[ArnType]


class SignInPolicyType(TypedDict, total=False):
    """The policy for allowed types of authentication in a user pool. To
    activate this setting, your user pool must be in the `Essentials
    tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html>`__
    or higher.
    """

    AllowedFirstAuthFactors: Optional[AllowedFirstAuthFactorsListType]


class PasswordPolicyType(TypedDict, total=False):
    """The password policy settings for a user pool, including complexity,
    history, and length requirements.
    """

    MinimumLength: Optional[PasswordPolicyMinLengthType]
    RequireUppercase: Optional[BooleanType]
    RequireLowercase: Optional[BooleanType]
    RequireNumbers: Optional[BooleanType]
    RequireSymbols: Optional[BooleanType]
    PasswordHistorySize: Optional[PasswordHistorySizeType]
    TemporaryPasswordValidityDays: Optional[TemporaryPasswordValidityDaysType]


class UserPoolPolicyType(TypedDict, total=False):
    """A list of user pool policies. Contains the policy that sets
    password-complexity requirements.
    """

    PasswordPolicy: Optional[PasswordPolicyType]
    SignInPolicy: Optional[SignInPolicyType]


class CreateUserPoolRequest(ServiceRequest):
    """Represents the request to create a user pool."""

    PoolName: UserPoolNameType
    Policies: Optional[UserPoolPolicyType]
    DeletionProtection: Optional[DeletionProtectionType]
    LambdaConfig: Optional[LambdaConfigType]
    AutoVerifiedAttributes: Optional[VerifiedAttributesListType]
    AliasAttributes: Optional[AliasAttributesListType]
    UsernameAttributes: Optional[UsernameAttributesListType]
    SmsVerificationMessage: Optional[SmsVerificationMessageType]
    EmailVerificationMessage: Optional[EmailVerificationMessageType]
    EmailVerificationSubject: Optional[EmailVerificationSubjectType]
    VerificationMessageTemplate: Optional[VerificationMessageTemplateType]
    SmsAuthenticationMessage: Optional[SmsVerificationMessageType]
    MfaConfiguration: Optional[UserPoolMfaType]
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsType]
    DeviceConfiguration: Optional[DeviceConfigurationType]
    EmailConfiguration: Optional[EmailConfigurationType]
    SmsConfiguration: Optional[SmsConfigurationType]
    UserPoolTags: Optional[UserPoolTagsType]
    AdminCreateUserConfig: Optional[AdminCreateUserConfigType]
    Schema: Optional[SchemaAttributesListType]
    UserPoolAddOns: Optional[UserPoolAddOnsType]
    UsernameConfiguration: Optional[UsernameConfigurationType]
    AccountRecoverySetting: Optional[AccountRecoverySettingType]
    UserPoolTier: Optional[UserPoolTierType]


class UserPoolType(TypedDict, total=False):
    """The configuration of a user pool."""

    Id: Optional[UserPoolIdType]
    Name: Optional[UserPoolNameType]
    Policies: Optional[UserPoolPolicyType]
    DeletionProtection: Optional[DeletionProtectionType]
    LambdaConfig: Optional[LambdaConfigType]
    Status: Optional[StatusType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]
    SchemaAttributes: Optional[SchemaAttributesListType]
    AutoVerifiedAttributes: Optional[VerifiedAttributesListType]
    AliasAttributes: Optional[AliasAttributesListType]
    UsernameAttributes: Optional[UsernameAttributesListType]
    SmsVerificationMessage: Optional[SmsVerificationMessageType]
    EmailVerificationMessage: Optional[EmailVerificationMessageType]
    EmailVerificationSubject: Optional[EmailVerificationSubjectType]
    VerificationMessageTemplate: Optional[VerificationMessageTemplateType]
    SmsAuthenticationMessage: Optional[SmsVerificationMessageType]
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsType]
    MfaConfiguration: Optional[UserPoolMfaType]
    DeviceConfiguration: Optional[DeviceConfigurationType]
    EstimatedNumberOfUsers: Optional[IntegerType]
    EmailConfiguration: Optional[EmailConfigurationType]
    SmsConfiguration: Optional[SmsConfigurationType]
    UserPoolTags: Optional[UserPoolTagsType]
    SmsConfigurationFailure: Optional[StringType]
    EmailConfigurationFailure: Optional[StringType]
    Domain: Optional[DomainType]
    CustomDomain: Optional[DomainType]
    AdminCreateUserConfig: Optional[AdminCreateUserConfigType]
    UserPoolAddOns: Optional[UserPoolAddOnsType]
    UsernameConfiguration: Optional[UsernameConfigurationType]
    Arn: Optional[ArnType]
    AccountRecoverySetting: Optional[AccountRecoverySettingType]
    UserPoolTier: Optional[UserPoolTierType]


class CreateUserPoolResponse(TypedDict, total=False):
    """Represents the response from the server for the request to create a user
    pool.
    """

    UserPool: Optional[UserPoolType]


class DeleteGroupRequest(ServiceRequest):
    GroupName: GroupNameType
    UserPoolId: UserPoolIdType


class DeleteIdentityProviderRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ProviderName: ProviderNameType


class DeleteManagedLoginBrandingRequest(ServiceRequest):
    ManagedLoginBrandingId: ManagedLoginBrandingIdType
    UserPoolId: UserPoolIdType


class DeleteResourceServerRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Identifier: ResourceServerIdentifierType


class DeleteUserAttributesRequest(ServiceRequest):
    """Represents the request to delete user attributes."""

    UserAttributeNames: AttributeNameListType
    AccessToken: TokenModelType


class DeleteUserAttributesResponse(TypedDict, total=False):
    """Represents the response from the server to delete user attributes."""

    pass


class DeleteUserPoolClientRequest(ServiceRequest):
    """Represents the request to delete a user pool client."""

    UserPoolId: UserPoolIdType
    ClientId: ClientIdType


class DeleteUserPoolDomainRequest(ServiceRequest):
    Domain: DomainType
    UserPoolId: UserPoolIdType


class DeleteUserPoolDomainResponse(TypedDict, total=False):
    pass


class DeleteUserPoolRequest(ServiceRequest):
    """Represents the request to delete a user pool."""

    UserPoolId: UserPoolIdType


class DeleteUserRequest(ServiceRequest):
    """Represents the request to delete a user."""

    AccessToken: TokenModelType


class DeleteWebAuthnCredentialRequest(ServiceRequest):
    AccessToken: TokenModelType
    CredentialId: StringType


class DeleteWebAuthnCredentialResponse(TypedDict, total=False):
    pass


class DescribeIdentityProviderRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ProviderName: ProviderNameType


class DescribeIdentityProviderResponse(TypedDict, total=False):
    IdentityProvider: IdentityProviderType


class DescribeManagedLoginBrandingByClientRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ClientId: ClientIdType
    ReturnMergedResources: Optional[BooleanType]


class DescribeManagedLoginBrandingByClientResponse(TypedDict, total=False):
    ManagedLoginBranding: Optional[ManagedLoginBrandingType]


class DescribeManagedLoginBrandingRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ManagedLoginBrandingId: ManagedLoginBrandingIdType
    ReturnMergedResources: Optional[BooleanType]


class DescribeManagedLoginBrandingResponse(TypedDict, total=False):
    ManagedLoginBranding: Optional[ManagedLoginBrandingType]


class DescribeResourceServerRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Identifier: ResourceServerIdentifierType


class DescribeResourceServerResponse(TypedDict, total=False):
    ResourceServer: ResourceServerType


class DescribeRiskConfigurationRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ClientId: Optional[ClientIdType]


SkippedIPRangeListType = List[StringType]


class RiskExceptionConfigurationType(TypedDict, total=False):
    """Exceptions to the risk evaluation configuration, including always-allow
    and always-block IP address ranges.
    """

    BlockedIPRangeList: Optional[BlockedIPRangeListType]
    SkippedIPRangeList: Optional[SkippedIPRangeListType]


class RiskConfigurationType(TypedDict, total=False):
    """The settings of risk configuration for threat protection with threat
    protection in a user pool.
    """

    UserPoolId: Optional[UserPoolIdType]
    ClientId: Optional[ClientIdType]
    CompromisedCredentialsRiskConfiguration: Optional[CompromisedCredentialsRiskConfigurationType]
    AccountTakeoverRiskConfiguration: Optional[AccountTakeoverRiskConfigurationType]
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationType]
    LastModifiedDate: Optional[DateType]


class DescribeRiskConfigurationResponse(TypedDict, total=False):
    RiskConfiguration: RiskConfigurationType


class DescribeUserImportJobRequest(ServiceRequest):
    """Represents the request to describe the user import job."""

    UserPoolId: UserPoolIdType
    JobId: UserImportJobIdType


class DescribeUserImportJobResponse(TypedDict, total=False):
    """Represents the response from the server to the request to describe the
    user import job.
    """

    UserImportJob: Optional[UserImportJobType]


class DescribeUserPoolClientRequest(ServiceRequest):
    """Represents the request to describe a user pool client."""

    UserPoolId: UserPoolIdType
    ClientId: ClientIdType


class DescribeUserPoolClientResponse(TypedDict, total=False):
    """Represents the response from the server from a request to describe the
    user pool client.
    """

    UserPoolClient: Optional[UserPoolClientType]


class DescribeUserPoolDomainRequest(ServiceRequest):
    Domain: DomainType


class DomainDescriptionType(TypedDict, total=False):
    """A container for information about the user pool domain associated with
    the hosted UI and OAuth endpoints.
    """

    UserPoolId: Optional[UserPoolIdType]
    AWSAccountId: Optional[AWSAccountIdType]
    Domain: Optional[DomainType]
    S3Bucket: Optional[S3BucketType]
    CloudFrontDistribution: Optional[StringType]
    Version: Optional[DomainVersionType]
    Status: Optional[DomainStatusType]
    CustomDomainConfig: Optional[CustomDomainConfigType]
    ManagedLoginVersion: Optional[WrappedIntegerType]


class DescribeUserPoolDomainResponse(TypedDict, total=False):
    DomainDescription: Optional[DomainDescriptionType]


class DescribeUserPoolRequest(ServiceRequest):
    """Represents the request to describe the user pool."""

    UserPoolId: UserPoolIdType


class DescribeUserPoolResponse(TypedDict, total=False):
    """Represents the response to describe the user pool."""

    UserPool: Optional[UserPoolType]


class EmailMfaConfigType(TypedDict, total=False):
    """Sets or shows configuration for user pool email message MFA and sign-in
    with one-time passwords (OTPs). Includes the subject and body of the
    email message template for sign-in and MFA messages. To activate this
    setting, your user pool must be in the `Essentials
    tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html>`__
    or higher.
    """

    Message: Optional[EmailMfaMessageType]
    Subject: Optional[EmailMfaSubjectType]


class FirehoseConfigurationType(TypedDict, total=False):
    """Configuration for the Amazon Data Firehose stream destination of user
    activity log export with threat protection.
    """

    StreamArn: Optional[ArnType]


class ForgetDeviceRequest(ServiceRequest):
    """Represents the request to forget the device."""

    AccessToken: Optional[TokenModelType]
    DeviceKey: DeviceKeyType


class ForgotPasswordRequest(ServiceRequest):
    """Represents the request to reset a user's password."""

    ClientId: ClientIdType
    SecretHash: Optional[SecretHashType]
    UserContextData: Optional[UserContextDataType]
    Username: UsernameType
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    ClientMetadata: Optional[ClientMetadataType]


class ForgotPasswordResponse(TypedDict, total=False):
    """The response from Amazon Cognito to a request to reset a password."""

    CodeDeliveryDetails: Optional[CodeDeliveryDetailsType]


class GetCSVHeaderRequest(ServiceRequest):
    """Represents the request to get the header information of the CSV file for
    the user import job.
    """

    UserPoolId: UserPoolIdType


ListOfStringTypes = List[StringType]


class GetCSVHeaderResponse(TypedDict, total=False):
    """Represents the response from the server to the request to get the header
    information of the CSV file for the user import job.
    """

    UserPoolId: Optional[UserPoolIdType]
    CSVHeader: Optional[ListOfStringTypes]


class GetDeviceRequest(ServiceRequest):
    """Represents the request to get the device."""

    DeviceKey: DeviceKeyType
    AccessToken: Optional[TokenModelType]


class GetDeviceResponse(TypedDict, total=False):
    """Gets the device response."""

    Device: DeviceType


class GetGroupRequest(ServiceRequest):
    GroupName: GroupNameType
    UserPoolId: UserPoolIdType


class GetGroupResponse(TypedDict, total=False):
    Group: Optional[GroupType]


class GetIdentityProviderByIdentifierRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    IdpIdentifier: IdpIdentifierType


class GetIdentityProviderByIdentifierResponse(TypedDict, total=False):
    IdentityProvider: IdentityProviderType


class GetLogDeliveryConfigurationRequest(ServiceRequest):
    UserPoolId: UserPoolIdType


class S3ConfigurationType(TypedDict, total=False):
    """Configuration for the Amazon S3 bucket destination of user activity log
    export with threat protection.
    """

    BucketArn: Optional[S3ArnType]


class LogConfigurationType(TypedDict, total=False):
    """The configuration of user event logs to an external Amazon Web Services
    service like Amazon Data Firehose, Amazon S3, or Amazon CloudWatch Logs.
    """

    LogLevel: LogLevel
    EventSource: EventSourceName
    CloudWatchLogsConfiguration: Optional[CloudWatchLogsConfigurationType]
    S3Configuration: Optional[S3ConfigurationType]
    FirehoseConfiguration: Optional[FirehoseConfigurationType]


LogConfigurationListType = List[LogConfigurationType]


class LogDeliveryConfigurationType(TypedDict, total=False):
    """The logging parameters of a user pool, as returned in the response to a
    ``GetLogDeliveryConfiguration`` request.
    """

    UserPoolId: UserPoolIdType
    LogConfigurations: LogConfigurationListType


class GetLogDeliveryConfigurationResponse(TypedDict, total=False):
    LogDeliveryConfiguration: Optional[LogDeliveryConfigurationType]


class GetSigningCertificateRequest(ServiceRequest):
    """Request to get a signing certificate from Amazon Cognito."""

    UserPoolId: UserPoolIdType


class GetSigningCertificateResponse(TypedDict, total=False):
    """Response from Amazon Cognito for a signing certificate request."""

    Certificate: Optional[StringType]


class GetTokensFromRefreshTokenRequest(ServiceRequest):
    RefreshToken: TokenModelType
    ClientId: ClientIdType
    ClientSecret: Optional[ClientSecretType]
    DeviceKey: Optional[DeviceKeyType]
    ClientMetadata: Optional[ClientMetadataType]


class GetTokensFromRefreshTokenResponse(TypedDict, total=False):
    AuthenticationResult: Optional[AuthenticationResultType]


class GetUICustomizationRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ClientId: Optional[ClientIdType]


class UICustomizationType(TypedDict, total=False):
    """A container for the UI customization information for the hosted UI in a
    user pool.
    """

    UserPoolId: Optional[UserPoolIdType]
    ClientId: Optional[ClientIdType]
    ImageUrl: Optional[ImageUrlType]
    CSS: Optional[CSSType]
    CSSVersion: Optional[CSSVersionType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]


class GetUICustomizationResponse(TypedDict, total=False):
    UICustomization: UICustomizationType


class GetUserAttributeVerificationCodeRequest(ServiceRequest):
    """Represents the request to get user attribute verification."""

    AccessToken: TokenModelType
    AttributeName: AttributeNameType
    ClientMetadata: Optional[ClientMetadataType]


class GetUserAttributeVerificationCodeResponse(TypedDict, total=False):
    """The verification code response returned by the server response to get
    the user attribute verification code.
    """

    CodeDeliveryDetails: Optional[CodeDeliveryDetailsType]


class GetUserAuthFactorsRequest(ServiceRequest):
    AccessToken: TokenModelType


class GetUserAuthFactorsResponse(TypedDict, total=False):
    Username: UsernameType
    PreferredMfaSetting: Optional[StringType]
    UserMFASettingList: Optional[UserMFASettingListType]
    ConfiguredUserAuthFactors: Optional[ConfiguredUserAuthFactorsListType]


class GetUserPoolMfaConfigRequest(ServiceRequest):
    UserPoolId: UserPoolIdType


class WebAuthnConfigurationType(TypedDict, total=False):
    """Settings for authentication (MFA) with passkey, or webauthN, biometric
    and security-key devices in a user pool. Configures the following:

    -  Configuration for requiring user-verification support in passkeys.

    -  The user pool relying-party ID. This is the domain, typically your
       user pool domain, that user's passkey providers should trust as a
       receiver of passkey authentication.

    -  The providers that you want to allow as origins for passkey
       authentication.
    """

    RelyingPartyId: Optional[RelyingPartyIdType]
    UserVerification: Optional[UserVerificationType]


class SoftwareTokenMfaConfigType(TypedDict, total=False):
    """Settings for time-based one-time password (TOTP) multi-factor
    authentication (MFA) in a user pool. Enables and disables availability
    of this feature.
    """

    Enabled: Optional[BooleanType]


class SmsMfaConfigType(TypedDict, total=False):
    """The configuration of multi-factor authentication (MFA) with SMS messages
    in a user pool.
    """

    SmsAuthenticationMessage: Optional[SmsVerificationMessageType]
    SmsConfiguration: Optional[SmsConfigurationType]


class GetUserPoolMfaConfigResponse(TypedDict, total=False):
    SmsMfaConfiguration: Optional[SmsMfaConfigType]
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigType]
    EmailMfaConfiguration: Optional[EmailMfaConfigType]
    MfaConfiguration: Optional[UserPoolMfaType]
    WebAuthnConfiguration: Optional[WebAuthnConfigurationType]


class GetUserRequest(ServiceRequest):
    """Represents the request to get information about the user."""

    AccessToken: TokenModelType


class GetUserResponse(TypedDict, total=False):
    """Represents the response from the server from the request to get
    information about the user.
    """

    Username: UsernameType
    UserAttributes: AttributeListType
    MFAOptions: Optional[MFAOptionListType]
    PreferredMfaSetting: Optional[StringType]
    UserMFASettingList: Optional[UserMFASettingListType]


class GlobalSignOutRequest(ServiceRequest):
    """Represents the request to sign out all devices."""

    AccessToken: TokenModelType


class GlobalSignOutResponse(TypedDict, total=False):
    """The response to the request to sign out all devices."""

    pass


ImageFileType = bytes


class InitiateAuthRequest(ServiceRequest):
    """Initiates the authentication request."""

    AuthFlow: AuthFlowType
    AuthParameters: Optional[AuthParametersType]
    ClientMetadata: Optional[ClientMetadataType]
    ClientId: ClientIdType
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    UserContextData: Optional[UserContextDataType]
    Session: Optional[SessionType]


class InitiateAuthResponse(TypedDict, total=False):
    """Initiates the authentication response."""

    ChallengeName: Optional[ChallengeNameType]
    Session: Optional[SessionType]
    ChallengeParameters: Optional[ChallengeParametersType]
    AuthenticationResult: Optional[AuthenticationResultType]
    AvailableChallenges: Optional[AvailableChallengeListType]


class ListDevicesRequest(ServiceRequest):
    """Represents the request to list the devices."""

    AccessToken: TokenModelType
    Limit: Optional[QueryLimitType]
    PaginationToken: Optional[SearchPaginationTokenType]


class ListDevicesResponse(TypedDict, total=False):
    """Represents the response to list devices."""

    Devices: Optional[DeviceListType]
    PaginationToken: Optional[SearchPaginationTokenType]


class ListGroupsRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Limit: Optional[QueryLimitType]
    NextToken: Optional[PaginationKey]


class ListGroupsResponse(TypedDict, total=False):
    Groups: Optional[GroupListType]
    NextToken: Optional[PaginationKey]


class ListIdentityProvidersRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    MaxResults: Optional[ListProvidersLimitType]
    NextToken: Optional[PaginationKeyType]


class ProviderDescription(TypedDict, total=False):
    """The details of a user pool identity provider (IdP), including name and
    type.
    """

    ProviderName: Optional[ProviderNameType]
    ProviderType: Optional[IdentityProviderTypeType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]


ProvidersListType = List[ProviderDescription]


class ListIdentityProvidersResponse(TypedDict, total=False):
    Providers: ProvidersListType
    NextToken: Optional[PaginationKeyType]


class ListResourceServersRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    MaxResults: Optional[ListResourceServersLimitType]
    NextToken: Optional[PaginationKeyType]


ResourceServersListType = List[ResourceServerType]


class ListResourceServersResponse(TypedDict, total=False):
    ResourceServers: ResourceServersListType
    NextToken: Optional[PaginationKeyType]


class ListTagsForResourceRequest(ServiceRequest):
    ResourceArn: ArnType


class ListTagsForResourceResponse(TypedDict, total=False):
    Tags: Optional[UserPoolTagsType]


class ListUserImportJobsRequest(ServiceRequest):
    """Represents the request to list the user import jobs."""

    UserPoolId: UserPoolIdType
    MaxResults: PoolQueryLimitType
    PaginationToken: Optional[PaginationKeyType]


UserImportJobsListType = List[UserImportJobType]


class ListUserImportJobsResponse(TypedDict, total=False):
    """Represents the response from the server to the request to list the user
    import jobs.
    """

    UserImportJobs: Optional[UserImportJobsListType]
    PaginationToken: Optional[PaginationKeyType]


class ListUserPoolClientsRequest(ServiceRequest):
    """Represents the request to list the user pool clients."""

    UserPoolId: UserPoolIdType
    MaxResults: Optional[QueryLimit]
    NextToken: Optional[PaginationKey]


class UserPoolClientDescription(TypedDict, total=False):
    """A short description of a user pool app client."""

    ClientId: Optional[ClientIdType]
    UserPoolId: Optional[UserPoolIdType]
    ClientName: Optional[ClientNameType]


UserPoolClientListType = List[UserPoolClientDescription]


class ListUserPoolClientsResponse(TypedDict, total=False):
    """Represents the response from the server that lists user pool clients."""

    UserPoolClients: Optional[UserPoolClientListType]
    NextToken: Optional[PaginationKey]


class ListUserPoolsRequest(ServiceRequest):
    """Represents the request to list user pools."""

    NextToken: Optional[PaginationKeyType]
    MaxResults: PoolQueryLimitType


class UserPoolDescriptionType(TypedDict, total=False):
    """A short description of a user pool."""

    Id: Optional[UserPoolIdType]
    Name: Optional[UserPoolNameType]
    LambdaConfig: Optional[LambdaConfigType]
    Status: Optional[StatusType]
    LastModifiedDate: Optional[DateType]
    CreationDate: Optional[DateType]


UserPoolListType = List[UserPoolDescriptionType]


class ListUserPoolsResponse(TypedDict, total=False):
    """Represents the response to list user pools."""

    UserPools: Optional[UserPoolListType]
    NextToken: Optional[PaginationKeyType]


class ListUsersInGroupRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    GroupName: GroupNameType
    Limit: Optional[QueryLimitType]
    NextToken: Optional[PaginationKey]


UsersListType = List[UserType]


class ListUsersInGroupResponse(TypedDict, total=False):
    Users: Optional[UsersListType]
    NextToken: Optional[PaginationKey]


SearchedAttributeNamesListType = List[AttributeNameType]


class ListUsersRequest(ServiceRequest):
    """Represents the request to list users."""

    UserPoolId: UserPoolIdType
    AttributesToGet: Optional[SearchedAttributeNamesListType]
    Limit: Optional[QueryLimitType]
    PaginationToken: Optional[SearchPaginationTokenType]
    Filter: Optional[UserFilterType]


class ListUsersResponse(TypedDict, total=False):
    """The response from the request to list users."""

    Users: Optional[UsersListType]
    PaginationToken: Optional[SearchPaginationTokenType]


class ListWebAuthnCredentialsRequest(ServiceRequest):
    AccessToken: TokenModelType
    NextToken: Optional[PaginationKey]
    MaxResults: Optional[WebAuthnCredentialsQueryLimitType]


WebAuthnAuthenticatorTransportsList = List[WebAuthnAuthenticatorTransportType]


class WebAuthnCredentialDescription(TypedDict, total=False):
    """The details of a passkey, or webauthN, biometric or security-key
    authentication factor for a user.
    """

    CredentialId: StringType
    FriendlyCredentialName: StringType
    RelyingPartyId: StringType
    AuthenticatorAttachment: Optional[WebAuthnAuthenticatorAttachmentType]
    AuthenticatorTransports: WebAuthnAuthenticatorTransportsList
    CreatedAt: DateType


WebAuthnCredentialDescriptionListType = List[WebAuthnCredentialDescription]


class ListWebAuthnCredentialsResponse(TypedDict, total=False):
    Credentials: WebAuthnCredentialDescriptionListType
    NextToken: Optional[PaginationKey]


class ResendConfirmationCodeRequest(ServiceRequest):
    """Represents the request to resend the confirmation code."""

    ClientId: ClientIdType
    SecretHash: Optional[SecretHashType]
    UserContextData: Optional[UserContextDataType]
    Username: UsernameType
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    ClientMetadata: Optional[ClientMetadataType]


class ResendConfirmationCodeResponse(TypedDict, total=False):
    """The response from the server when Amazon Cognito makes the request to
    resend a confirmation code.
    """

    CodeDeliveryDetails: Optional[CodeDeliveryDetailsType]


class RespondToAuthChallengeRequest(ServiceRequest):
    """The request to respond to an authentication challenge."""

    ClientId: ClientIdType
    ChallengeName: ChallengeNameType
    Session: Optional[SessionType]
    ChallengeResponses: Optional[ChallengeResponsesType]
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    UserContextData: Optional[UserContextDataType]
    ClientMetadata: Optional[ClientMetadataType]


class RespondToAuthChallengeResponse(TypedDict, total=False):
    """The response to respond to the authentication challenge."""

    ChallengeName: Optional[ChallengeNameType]
    Session: Optional[SessionType]
    ChallengeParameters: Optional[ChallengeParametersType]
    AuthenticationResult: Optional[AuthenticationResultType]


class RevokeTokenRequest(ServiceRequest):
    Token: TokenModelType
    ClientId: ClientIdType
    ClientSecret: Optional[ClientSecretType]


class RevokeTokenResponse(TypedDict, total=False):
    pass


class SetLogDeliveryConfigurationRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    LogConfigurations: LogConfigurationListType


class SetLogDeliveryConfigurationResponse(TypedDict, total=False):
    LogDeliveryConfiguration: Optional[LogDeliveryConfigurationType]


class SetRiskConfigurationRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ClientId: Optional[ClientIdType]
    CompromisedCredentialsRiskConfiguration: Optional[CompromisedCredentialsRiskConfigurationType]
    AccountTakeoverRiskConfiguration: Optional[AccountTakeoverRiskConfigurationType]
    RiskExceptionConfiguration: Optional[RiskExceptionConfigurationType]


class SetRiskConfigurationResponse(TypedDict, total=False):
    RiskConfiguration: RiskConfigurationType


class SetUICustomizationRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ClientId: Optional[ClientIdType]
    CSS: Optional[CSSType]
    ImageFile: Optional[ImageFileType]


class SetUICustomizationResponse(TypedDict, total=False):
    UICustomization: UICustomizationType


class SetUserMFAPreferenceRequest(ServiceRequest):
    SMSMfaSettings: Optional[SMSMfaSettingsType]
    SoftwareTokenMfaSettings: Optional[SoftwareTokenMfaSettingsType]
    EmailMfaSettings: Optional[EmailMfaSettingsType]
    AccessToken: TokenModelType


class SetUserMFAPreferenceResponse(TypedDict, total=False):
    pass


class SetUserPoolMfaConfigRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    SmsMfaConfiguration: Optional[SmsMfaConfigType]
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigType]
    EmailMfaConfiguration: Optional[EmailMfaConfigType]
    MfaConfiguration: Optional[UserPoolMfaType]
    WebAuthnConfiguration: Optional[WebAuthnConfigurationType]


class SetUserPoolMfaConfigResponse(TypedDict, total=False):
    SmsMfaConfiguration: Optional[SmsMfaConfigType]
    SoftwareTokenMfaConfiguration: Optional[SoftwareTokenMfaConfigType]
    EmailMfaConfiguration: Optional[EmailMfaConfigType]
    MfaConfiguration: Optional[UserPoolMfaType]
    WebAuthnConfiguration: Optional[WebAuthnConfigurationType]


class SetUserSettingsRequest(ServiceRequest):
    """Represents the request to set user settings."""

    AccessToken: TokenModelType
    MFAOptions: MFAOptionListType


class SetUserSettingsResponse(TypedDict, total=False):
    """The response from the server for a set user settings request."""

    pass


class SignUpRequest(ServiceRequest):
    """Represents the request to register a user."""

    ClientId: ClientIdType
    SecretHash: Optional[SecretHashType]
    Username: UsernameType
    Password: Optional[PasswordType]
    UserAttributes: Optional[AttributeListType]
    ValidationData: Optional[AttributeListType]
    AnalyticsMetadata: Optional[AnalyticsMetadataType]
    UserContextData: Optional[UserContextDataType]
    ClientMetadata: Optional[ClientMetadataType]


class SignUpResponse(TypedDict, total=False):
    """The response from the server for a registration request."""

    UserConfirmed: BooleanType
    CodeDeliveryDetails: Optional[CodeDeliveryDetailsType]
    UserSub: StringType
    Session: Optional[SessionType]


class StartUserImportJobRequest(ServiceRequest):
    """Represents the request to start the user import job."""

    UserPoolId: UserPoolIdType
    JobId: UserImportJobIdType


class StartUserImportJobResponse(TypedDict, total=False):
    """Represents the response from the server to the request to start the user
    import job.
    """

    UserImportJob: Optional[UserImportJobType]


class StartWebAuthnRegistrationRequest(ServiceRequest):
    AccessToken: TokenModelType


class StartWebAuthnRegistrationResponse(TypedDict, total=False):
    CredentialCreationOptions: Document


class StopUserImportJobRequest(ServiceRequest):
    """Represents the request to stop the user import job."""

    UserPoolId: UserPoolIdType
    JobId: UserImportJobIdType


class StopUserImportJobResponse(TypedDict, total=False):
    """Represents the response from the server to the request to stop the user
    import job.
    """

    UserImportJob: Optional[UserImportJobType]


class TagResourceRequest(ServiceRequest):
    ResourceArn: ArnType
    Tags: UserPoolTagsType


class TagResourceResponse(TypedDict, total=False):
    pass


UserPoolTagsListType = List[TagKeysType]


class UntagResourceRequest(ServiceRequest):
    ResourceArn: ArnType
    TagKeys: UserPoolTagsListType


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateAuthEventFeedbackRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Username: UsernameType
    EventId: EventIdType
    FeedbackToken: TokenModelType
    FeedbackValue: FeedbackValueType


class UpdateAuthEventFeedbackResponse(TypedDict, total=False):
    pass


class UpdateDeviceStatusRequest(ServiceRequest):
    """Represents the request to update the device status."""

    AccessToken: TokenModelType
    DeviceKey: DeviceKeyType
    DeviceRememberedStatus: Optional[DeviceRememberedStatusType]


class UpdateDeviceStatusResponse(TypedDict, total=False):
    """The response to the request to update the device status."""

    pass


class UpdateGroupRequest(ServiceRequest):
    GroupName: GroupNameType
    UserPoolId: UserPoolIdType
    Description: Optional[DescriptionType]
    RoleArn: Optional[ArnType]
    Precedence: Optional[PrecedenceType]


class UpdateGroupResponse(TypedDict, total=False):
    Group: Optional[GroupType]


class UpdateIdentityProviderRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    ProviderName: ProviderNameType
    ProviderDetails: Optional[ProviderDetailsType]
    AttributeMapping: Optional[AttributeMappingType]
    IdpIdentifiers: Optional[IdpIdentifiersListType]


class UpdateIdentityProviderResponse(TypedDict, total=False):
    IdentityProvider: IdentityProviderType


class UpdateManagedLoginBrandingRequest(ServiceRequest):
    UserPoolId: Optional[UserPoolIdType]
    ManagedLoginBrandingId: Optional[ManagedLoginBrandingIdType]
    UseCognitoProvidedValues: Optional[BooleanType]
    Settings: Optional[Document]
    Assets: Optional[AssetListType]


class UpdateManagedLoginBrandingResponse(TypedDict, total=False):
    ManagedLoginBranding: Optional[ManagedLoginBrandingType]


class UpdateResourceServerRequest(ServiceRequest):
    UserPoolId: UserPoolIdType
    Identifier: ResourceServerIdentifierType
    Name: ResourceServerNameType
    Scopes: Optional[ResourceServerScopeListType]


class UpdateResourceServerResponse(TypedDict, total=False):
    ResourceServer: ResourceServerType


class UpdateUserAttributesRequest(ServiceRequest):
    """Represents the request to update user attributes."""

    UserAttributes: AttributeListType
    AccessToken: TokenModelType
    ClientMetadata: Optional[ClientMetadataType]


class UpdateUserAttributesResponse(TypedDict, total=False):
    """Represents the response from the server for the request to update user
    attributes.
    """

    CodeDeliveryDetailsList: Optional[CodeDeliveryDetailsListType]


class UpdateUserPoolClientRequest(ServiceRequest):
    """Represents the request to update the user pool client."""

    UserPoolId: UserPoolIdType
    ClientId: ClientIdType
    ClientName: Optional[ClientNameType]
    RefreshTokenValidity: Optional[RefreshTokenValidityType]
    AccessTokenValidity: Optional[AccessTokenValidityType]
    IdTokenValidity: Optional[IdTokenValidityType]
    TokenValidityUnits: Optional[TokenValidityUnitsType]
    ReadAttributes: Optional[ClientPermissionListType]
    WriteAttributes: Optional[ClientPermissionListType]
    ExplicitAuthFlows: Optional[ExplicitAuthFlowsListType]
    SupportedIdentityProviders: Optional[SupportedIdentityProvidersListType]
    CallbackURLs: Optional[CallbackURLsListType]
    LogoutURLs: Optional[LogoutURLsListType]
    DefaultRedirectURI: Optional[RedirectUrlType]
    AllowedOAuthFlows: Optional[OAuthFlowsType]
    AllowedOAuthScopes: Optional[ScopeListType]
    AllowedOAuthFlowsUserPoolClient: Optional[BooleanType]
    AnalyticsConfiguration: Optional[AnalyticsConfigurationType]
    PreventUserExistenceErrors: Optional[PreventUserExistenceErrorTypes]
    EnableTokenRevocation: Optional[WrappedBooleanType]
    EnablePropagateAdditionalUserContextData: Optional[WrappedBooleanType]
    AuthSessionValidity: Optional[AuthSessionValidityType]
    RefreshTokenRotation: Optional[RefreshTokenRotationType]


class UpdateUserPoolClientResponse(TypedDict, total=False):
    """Represents the response from the server to the request to update the
    user pool client.
    """

    UserPoolClient: Optional[UserPoolClientType]


class UpdateUserPoolDomainRequest(ServiceRequest):
    """The UpdateUserPoolDomain request input."""

    Domain: DomainType
    UserPoolId: UserPoolIdType
    ManagedLoginVersion: Optional[WrappedIntegerType]
    CustomDomainConfig: Optional[CustomDomainConfigType]


class UpdateUserPoolDomainResponse(TypedDict, total=False):
    """The UpdateUserPoolDomain response output."""

    ManagedLoginVersion: Optional[WrappedIntegerType]
    CloudFrontDomain: Optional[DomainType]


class UpdateUserPoolRequest(ServiceRequest):
    """Represents the request to update the user pool."""

    UserPoolId: UserPoolIdType
    Policies: Optional[UserPoolPolicyType]
    DeletionProtection: Optional[DeletionProtectionType]
    LambdaConfig: Optional[LambdaConfigType]
    AutoVerifiedAttributes: Optional[VerifiedAttributesListType]
    SmsVerificationMessage: Optional[SmsVerificationMessageType]
    EmailVerificationMessage: Optional[EmailVerificationMessageType]
    EmailVerificationSubject: Optional[EmailVerificationSubjectType]
    VerificationMessageTemplate: Optional[VerificationMessageTemplateType]
    SmsAuthenticationMessage: Optional[SmsVerificationMessageType]
    UserAttributeUpdateSettings: Optional[UserAttributeUpdateSettingsType]
    MfaConfiguration: Optional[UserPoolMfaType]
    DeviceConfiguration: Optional[DeviceConfigurationType]
    EmailConfiguration: Optional[EmailConfigurationType]
    SmsConfiguration: Optional[SmsConfigurationType]
    UserPoolTags: Optional[UserPoolTagsType]
    AdminCreateUserConfig: Optional[AdminCreateUserConfigType]
    UserPoolAddOns: Optional[UserPoolAddOnsType]
    AccountRecoverySetting: Optional[AccountRecoverySettingType]
    PoolName: Optional[UserPoolNameType]
    UserPoolTier: Optional[UserPoolTierType]


class UpdateUserPoolResponse(TypedDict, total=False):
    """Represents the response from the server when you make a request to
    update the user pool.
    """

    pass


class VerifySoftwareTokenRequest(ServiceRequest):
    AccessToken: Optional[TokenModelType]
    Session: Optional[SessionType]
    UserCode: SoftwareTokenMFAUserCodeType
    FriendlyDeviceName: Optional[StringType]


class VerifySoftwareTokenResponse(TypedDict, total=False):
    Status: Optional[VerifySoftwareTokenResponseType]
    Session: Optional[SessionType]


class VerifyUserAttributeRequest(ServiceRequest):
    """Represents the request to verify user attributes."""

    AccessToken: TokenModelType
    AttributeName: AttributeNameType
    Code: ConfirmationCodeType


class VerifyUserAttributeResponse(TypedDict, total=False):
    """A container representing the response from the server from the request
    to verify user attributes.
    """

    pass


class CognitoIdpApi:
    service = "cognito-idp"
    version = "2016-04-18"

    @handler("AddCustomAttributes")
    def add_custom_attributes(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        custom_attributes: CustomAttributesListType,
        **kwargs,
    ) -> AddCustomAttributesResponse:
        """Adds additional user attributes to the user pool schema. Custom
        attributes can be mutable or immutable and have a ``custom:`` or
        ``dev:`` prefix. For more information, see `Custom
        attributes <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-custom-attributes>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to add custom attributes.
        :param custom_attributes: An array of custom attribute names and other properties.
        :returns: AddCustomAttributesResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserImportInProgressException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminAddUserToGroup")
    def admin_add_user_to_group(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        group_name: GroupNameType,
        **kwargs,
    ) -> None:
        """Adds a user to a group. A user who is in a group can present a
        preferred-role claim to an identity pool, and populates a
        ``cognito:groups`` claim to their access and identity tokens.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that contains the group that you want to add the
        user to.
        :param username: The name of the user that you want to query or modify.
        :param group_name: The name of the group that you want to add your user to.
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminConfirmSignUp")
    def admin_confirm_sign_up(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> AdminConfirmSignUpResponse:
        """Confirms user sign-up as an administrator.

        This request sets a user account active in a user pool that `requires
        confirmation of new user
        accounts <https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#signing-up-users-in-your-app-and-confirming-them-as-admin>`__
        before they can sign in. You can configure your user pool to not send
        confirmation codes to new users and instead confirm them with this API
        operation on the back end.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        To configure your user pool to require administrative confirmation of
        users, set ``AllowAdminCreateUserOnly`` to ``true`` in a
        ``CreateUserPool`` or ``UpdateUserPool`` request.

        :param user_pool_id: The ID of the user pool where you want to confirm a user's sign-up
        request.
        :param username: The name of the user that you want to query or modify.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: AdminConfirmSignUpResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises NotAuthorizedException:
        :raises TooManyFailedAttemptsException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminCreateUser")
    def admin_create_user(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        user_attributes: AttributeListType | None = None,
        validation_data: AttributeListType | None = None,
        temporary_password: PasswordType | None = None,
        force_alias_creation: ForceAliasCreation | None = None,
        message_action: MessageActionType | None = None,
        desired_delivery_mediums: DeliveryMediumListType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> AdminCreateUserResponse:
        """Creates a new user in the specified user pool.

        If ``MessageAction`` isn't set, the default is to send a welcome message
        via email or phone (SMS).

        This message is based on a template that you configured in your call to
        create or update a user pool. This template includes your custom sign-up
        instructions and placeholders for user name and temporary password.

        Alternatively, you can call ``AdminCreateUser`` with ``SUPPRESS`` for
        the ``MessageAction`` parameter, and Amazon Cognito won't send any
        email.

        In either case, if the user has a password, they will be in the
        ``FORCE_CHANGE_PASSWORD`` state until they sign in and set their
        password. Your invitation message template must have the ``{####}``
        password placeholder if your users have passwords. If your template
        doesn't have this placeholder, Amazon Cognito doesn't deliver the
        invitation message. In this case, you must update your message template
        and resend the password with a new ``AdminCreateUser`` request with a
        ``MessageAction`` value of ``RESEND``.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to create a user.
        :param username: The value that you want to set as the username sign-in attribute.
        :param user_attributes: An array of name-value pairs that contain user attributes and attribute
        values to be set for the user to be created.
        :param validation_data: Temporary user attributes that contribute to the outcomes of your pre
        sign-up Lambda trigger.
        :param temporary_password: The user's temporary password.
        :param force_alias_creation: This parameter is used only if the ``phone_number_verified`` or
        ``email_verified`` attribute is set to ``True``.
        :param message_action: Set to ``RESEND`` to resend the invitation message to a user that
        already exists, and to reset the temporary-password duration with a new
        temporary password.
        :param desired_delivery_mediums: Specify ``EMAIL`` if email will be used to send the welcome message.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: AdminCreateUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UserNotFoundException:
        :raises UsernameExistsException:
        :raises InvalidPasswordException:
        :raises CodeDeliveryFailureException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises PreconditionNotMetException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UnsupportedUserStateException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminDeleteUser")
    def admin_delete_user(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        **kwargs,
    ) -> None:
        """Deletes a user profile in your user pool.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to delete the user.
        :param username: The name of the user that you want to query or modify.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminDeleteUserAttributes")
    def admin_delete_user_attributes(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        user_attribute_names: AttributeNameListType,
        **kwargs,
    ) -> AdminDeleteUserAttributesResponse:
        """Deletes attribute values from a user. This operation doesn't affect
        tokens for existing user sessions. The next ID token that the user
        receives will no longer have the deleted attributes.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to delete user attributes.
        :param username: The name of the user that you want to query or modify.
        :param user_attribute_names: An array of strings representing the user attribute names you want to
        delete.
        :returns: AdminDeleteUserAttributesResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminDisableProviderForUser")
    def admin_disable_provider_for_user(
        self,
        context: RequestContext,
        user_pool_id: StringType,
        user: ProviderUserIdentifierType,
        **kwargs,
    ) -> AdminDisableProviderForUserResponse:
        """Prevents the user from signing in with the specified external (SAML or
        social) identity provider (IdP). If the user that you want to deactivate
        is a Amazon Cognito user pools native username + password user, they
        can't use their password to sign in. If the user to deactivate is a
        linked external IdP user, any link between that user and an existing
        user is removed. When the external user signs in again, and the user is
        no longer attached to the previously linked ``DestinationUser``, the
        user must create a new user account.

        The value of ``ProviderName`` must match the name of a user pool IdP.

        To deactivate a local user, set ``ProviderName`` to ``Cognito`` and the
        ``ProviderAttributeName`` to ``Cognito_Subject``. The
        ``ProviderAttributeValue`` must be user's local username.

        The ``ProviderAttributeName`` must always be ``Cognito_Subject`` for
        social IdPs. The ``ProviderAttributeValue`` must always be the exact
        subject that was used when the user was originally linked as a source
        user.

        For de-linking a SAML identity, there are two scenarios. If the linked
        identity has not yet been used to sign in, the ``ProviderAttributeName``
        and ``ProviderAttributeValue`` must be the same values that were used
        for the ``SourceUser`` when the identities were originally linked using
        ``AdminLinkProviderForUser`` call. This is also true if the linking was
        done with ``ProviderAttributeName`` set to ``Cognito_Subject``. If the
        user has already signed in, the ``ProviderAttributeName`` must be
        ``Cognito_Subject`` and ``ProviderAttributeValue`` must be the
        ``NameID`` from their SAML assertion.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to delete the user's linked
        identities.
        :param user: The user profile that you want to delete a linked identity from.
        :returns: AdminDisableProviderForUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises AliasExistsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminDisableUser")
    def admin_disable_user(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        **kwargs,
    ) -> AdminDisableUserResponse:
        """Deactivates a user profile and revokes all access tokens for the user. A
        deactivated user can't sign in, but still appears in the responses to
        ``ListUsers`` API requests.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to disable the user.
        :param username: The name of the user that you want to query or modify.
        :returns: AdminDisableUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminEnableUser")
    def admin_enable_user(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        **kwargs,
    ) -> AdminEnableUserResponse:
        """Activates sign-in for a user profile that previously had sign-in access
        disabled.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to activate sign-in for the user.
        :param username: The name of the user that you want to query or modify.
        :returns: AdminEnableUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminForgetDevice")
    def admin_forget_device(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        device_key: DeviceKeyType,
        **kwargs,
    ) -> None:
        """Forgets, or deletes, a remembered device from a user's profile. After
        you forget the device, the user can no longer complete device
        authentication with that device and when applicable, must submit MFA
        codes again. For more information, see `Working with
        devices <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where the device owner is a user.
        :param username: The name of the user that you want to query or modify.
        :param device_key: The key ID of the device that you want to delete.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminGetDevice")
    def admin_get_device(
        self,
        context: RequestContext,
        device_key: DeviceKeyType,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        **kwargs,
    ) -> AdminGetDeviceResponse:
        """Given the device key, returns details for a user's device. For more
        information, see `Working with
        devices <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param device_key: The key of the device that you want to delete.
        :param user_pool_id: The ID of the user pool where the device owner is a user.
        :param username: The name of the user that you want to query or modify.
        :returns: AdminGetDeviceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises NotAuthorizedException:
        """
        raise NotImplementedError

    @handler("AdminGetUser")
    def admin_get_user(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        **kwargs,
    ) -> AdminGetUserResponse:
        """Given a username, returns details about a user profile in a user pool.
        You can specify alias attributes in the ``Username`` request parameter.

        This operation contributes to your monthly active user (MAU) count for
        the purpose of billing.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to get information about the
        user.
        :param username: The name of the user that you want to query or modify.
        :returns: AdminGetUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminInitiateAuth")
    def admin_initiate_auth(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        auth_flow: AuthFlowType,
        auth_parameters: AuthParametersType | None = None,
        client_metadata: ClientMetadataType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        context_data: ContextDataType | None = None,
        session: SessionType | None = None,
        **kwargs,
    ) -> AdminInitiateAuthResponse:
        """Starts sign-in for applications with a server-side component, for
        example a traditional web application. This operation specifies the
        authentication flow that you'd like to begin. The authentication flow
        that you specify must be supported in your app client configuration. For
        more information about authentication flows, see `Authentication
        flows <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where the user wants to sign in.
        :param client_id: The ID of the app client where the user wants to sign in.
        :param auth_flow: The authentication flow that you want to initiate.
        :param auth_parameters: The authentication parameters.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for
        certain custom workflows that this action triggers.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param session: The optional session ID from a ``ConfirmSignUp`` API request.
        :returns: AdminInitiateAuthResponse
        :raises ResourceNotFoundException:
        :raises UnsupportedOperationException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises UnexpectedLambdaException:
        :raises InvalidUserPoolConfigurationException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises MFAMethodNotFoundException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        """
        raise NotImplementedError

    @handler("AdminLinkProviderForUser")
    def admin_link_provider_for_user(
        self,
        context: RequestContext,
        user_pool_id: StringType,
        destination_user: ProviderUserIdentifierType,
        source_user: ProviderUserIdentifierType,
        **kwargs,
    ) -> AdminLinkProviderForUserResponse:
        """Links an existing user account in a user pool, or ``DestinationUser``,
        to an identity from an external IdP, or ``SourceUser``, based on a
        specified attribute name and value from the external IdP.

        This operation connects a local user profile with a user identity who
        hasn't yet signed in from their third-party IdP. When the user signs in
        with their IdP, they get access-control configuration from the local
        user profile. Linked local users can also sign in with SDK-based API
        operations like ``InitiateAuth`` after they sign in at least once
        through their IdP. For more information, see `Linking federated
        users <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html>`__.

        The maximum number of federated identities linked to a user is five.

        Because this API allows a user with an external federated identity to
        sign in as a local user, it is critical that it only be used with
        external IdPs and linked attributes that you trust.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to link a federated identity.
        :param destination_user: The existing user in the user pool that you want to assign to the
        external IdP user account.
        :param source_user: An external IdP account for a user who doesn't exist yet in the user
        pool.
        :returns: AdminLinkProviderForUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises AliasExistsException:
        :raises LimitExceededException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminListDevices")
    def admin_list_devices(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        limit: QueryLimitType | None = None,
        pagination_token: SearchPaginationTokenType | None = None,
        **kwargs,
    ) -> AdminListDevicesResponse:
        """Lists a user's registered devices. Remembered devices are used in
        authentication services where you offer a "Remember me" option for users
        who you want to permit to sign in without MFA from a trusted device.
        Users can bypass MFA while your application performs device SRP
        authentication on the back end. For more information, see `Working with
        devices <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where the device owner is a user.
        :param username: The name of the user that you want to query or modify.
        :param limit: The maximum number of devices that you want Amazon Cognito to return in
        the response.
        :param pagination_token: This API operation returns a limited number of results.
        :returns: AdminListDevicesResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises NotAuthorizedException:
        """
        raise NotImplementedError

    @handler("AdminListGroupsForUser")
    def admin_list_groups_for_user(
        self,
        context: RequestContext,
        username: UsernameType,
        user_pool_id: UserPoolIdType,
        limit: QueryLimitType | None = None,
        next_token: PaginationKey | None = None,
        **kwargs,
    ) -> AdminListGroupsForUserResponse:
        """Lists the groups that a user belongs to. User pool groups are
        identifiers that you can reference from the contents of ID and access
        tokens, and set preferred IAM roles for identity-pool authentication.
        For more information, see `Adding groups to a user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param username: The name of the user that you want to query or modify.
        :param user_pool_id: The ID of the user pool where you want to view a user's groups.
        :param limit: The maximum number of groups that you want Amazon Cognito to return in
        the response.
        :param next_token: This API operation returns a limited number of results.
        :returns: AdminListGroupsForUserResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminListUserAuthEvents")
    def admin_list_user_auth_events(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        max_results: QueryLimitType | None = None,
        next_token: PaginationKey | None = None,
        **kwargs,
    ) -> AdminListUserAuthEventsResponse:
        """Requests a history of user activity and any risks detected as part of
        Amazon Cognito threat protection. For more information, see `Viewing
        user event
        history <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-event-user-history>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The Id of the user pool that contains the user profile with the logged
        events.
        :param username: The name of the user that you want to query or modify.
        :param max_results: The maximum number of authentication events to return.
        :param next_token: This API operation returns a limited number of results.
        :returns: AdminListUserAuthEventsResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises UserPoolAddOnNotEnabledException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminRemoveUserFromGroup")
    def admin_remove_user_from_group(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        group_name: GroupNameType,
        **kwargs,
    ) -> None:
        """Given a username and a group name, removes them from the group. User
        pool groups are identifiers that you can reference from the contents of
        ID and access tokens, and set preferred IAM roles for identity-pool
        authentication. For more information, see `Adding groups to a user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that contains the group and the user that you
        want to remove.
        :param username: The name of the user that you want to query or modify.
        :param group_name: The name of the group that you want to remove the user from, for example
        ``MyTestGroup``.
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminResetUserPassword")
    def admin_reset_user_password(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> AdminResetUserPasswordResponse:
        """Resets the specified user's password in a user pool. This operation
        doesn't change the user's password, but sends a password-reset code.

        To use this API operation, your user pool must have self-service account
        recovery configured.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to reset the user's password.
        :param username: The name of the user that you want to query or modify.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: AdminResetUserPasswordResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises NotAuthorizedException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises UserNotFoundException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminRespondToAuthChallenge")
    def admin_respond_to_auth_challenge(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        challenge_name: ChallengeNameType,
        challenge_responses: ChallengeResponsesType | None = None,
        session: SessionType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        context_data: ContextDataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> AdminRespondToAuthChallengeResponse:
        """Some API operations in a user pool generate a challenge, like a prompt
        for an MFA code, for device authentication that bypasses MFA, or for a
        custom authentication challenge. An ``AdminRespondToAuthChallenge`` API
        request provides the answer to that challenge, like a code or a secure
        remote password (SRP). The parameters of a response to an authentication
        challenge vary with the type of challenge.

        For more information about custom authentication challenges, see `Custom
        authentication challenge Lambda
        triggers <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to respond to an authentication
        challenge.
        :param client_id: The ID of the app client where you initiated sign-in.
        :param challenge_name: The name of the challenge that you are responding to.
        :param challenge_responses: The responses to the challenge that you received in the previous
        request.
        :param session: The session identifier that maintains the state of authentication
        requests and challenge responses.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: AdminRespondToAuthChallengeResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises CodeMismatchException:
        :raises ExpiredCodeException:
        :raises UnexpectedLambdaException:
        :raises InvalidPasswordException:
        :raises PasswordHistoryPolicyViolationException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises InvalidUserPoolConfigurationException:
        :raises InternalErrorException:
        :raises MFAMethodNotFoundException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises AliasExistsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises SoftwareTokenMFANotFoundException:
        """
        raise NotImplementedError

    @handler("AdminSetUserMFAPreference")
    def admin_set_user_mfa_preference(
        self,
        context: RequestContext,
        username: UsernameType,
        user_pool_id: UserPoolIdType,
        sms_mfa_settings: SMSMfaSettingsType | None = None,
        software_token_mfa_settings: SoftwareTokenMfaSettingsType | None = None,
        email_mfa_settings: EmailMfaSettingsType | None = None,
        **kwargs,
    ) -> AdminSetUserMFAPreferenceResponse:
        """Sets the user's multi-factor authentication (MFA) preference, including
        which MFA options are activated, and if any are preferred. Only one
        factor can be set as preferred. The preferred MFA factor will be used to
        authenticate a user if multiple factors are activated. If multiple
        options are activated and no preference is set, a challenge to choose an
        MFA option will be returned during sign-in.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param username: The name of the user that you want to query or modify.
        :param user_pool_id: The ID of the user pool where you want to set a user's MFA preferences.
        :param sms_mfa_settings: User preferences for SMS message MFA.
        :param software_token_mfa_settings: User preferences for time-based one-time password (TOTP) MFA.
        :param email_mfa_settings: User preferences for email message MFA.
        :returns: AdminSetUserMFAPreferenceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminSetUserPassword")
    def admin_set_user_password(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        password: PasswordType,
        permanent: BooleanType | None = None,
        **kwargs,
    ) -> AdminSetUserPasswordResponse:
        """Sets the specified user's password in a user pool. This operation
        administratively sets a temporary or permanent password for a user. With
        this operation, you can bypass self-service password changes and permit
        immediate sign-in with the password that you set. To do this, set
        ``Permanent`` to ``true``.

        You can also set a new temporary password in this request, send it to a
        user, and require them to choose a new password on their next sign-in.
        To do this, set ``Permanent`` to ``false``.

        If the password is temporary, the user's ``Status`` becomes
        ``FORCE_CHANGE_PASSWORD``. When the user next tries to sign in, the
        ``InitiateAuth`` or ``AdminInitiateAuth`` response includes the
        ``NEW_PASSWORD_REQUIRED`` challenge. If the user doesn't sign in before
        the temporary password expires, they can no longer sign in and you must
        repeat this operation to set a temporary or permanent password for them.

        After the user sets a new password, or if you set a permanent password,
        their status becomes ``Confirmed``.

        ``AdminSetUserPassword`` can set a password for the user profile that
        Amazon Cognito creates for third-party federated users. When you set a
        password, the federated user's status changes from ``EXTERNAL_PROVIDER``
        to ``CONFIRMED``. A user in this state can sign in as a federated user,
        and initiate authentication flows in the API like a linked native user.
        They can also modify their password and attributes in
        token-authenticated API requests like ``ChangePassword`` and
        ``UpdateUserAttributes``. As a best security practice and to keep users
        in sync with your external IdP, don't set passwords on federated user
        profiles. To set up a federated user for native sign-in with a linked
        native user, refer to `Linking federated users to an existing user
        profile <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to set the user's password.
        :param username: The name of the user that you want to query or modify.
        :param password: The new temporary or permanent password that you want to set for the
        user.
        :param permanent: Set to ``true`` to set a password that the user can immediately sign in
        with.
        :returns: AdminSetUserPasswordResponse
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        :raises TooManyRequestsException:
        :raises InvalidParameterException:
        :raises InvalidPasswordException:
        :raises PasswordHistoryPolicyViolationException:
        """
        raise NotImplementedError

    @handler("AdminSetUserSettings")
    def admin_set_user_settings(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        mfa_options: MFAOptionListType,
        **kwargs,
    ) -> AdminSetUserSettingsResponse:
        """*This action is no longer supported.* You can use it to configure only
        SMS MFA. You can't use it to configure time-based one-time password
        (TOTP) software token MFA.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that contains the user whose options you're
        setting.
        :param username: The name of the user that you want to query or modify.
        :param mfa_options: You can use this parameter only to set an SMS configuration that uses
        SMS for delivery.
        :returns: AdminSetUserSettingsResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminUpdateAuthEventFeedback")
    def admin_update_auth_event_feedback(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        event_id: EventIdType,
        feedback_value: FeedbackValueType,
        **kwargs,
    ) -> AdminUpdateAuthEventFeedbackResponse:
        """Provides the feedback for an authentication event generated by threat
        protection features. Your response indicates that you think that the
        event either was from a valid user or was an unwanted authentication
        attempt. This feedback improves the risk evaluation decision for the
        user pool as part of Amazon Cognito threat protection. To activate this
        setting, your user pool must be on the `Plus
        tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html>`__.

        To train the threat-protection model to recognize trusted and untrusted
        sign-in characteristics, configure threat protection in audit-only mode
        and provide a mechanism for users or administrators to submit feedback.
        Your feedback can tell Amazon Cognito that a risk rating was assigned at
        a level you don't agree with.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to submit authentication-event
        feedback.
        :param username: The name of the user that you want to query or modify.
        :param event_id: The ID of the threat protection authentication event that you want to
        update.
        :param feedback_value: Your feedback to the authentication event.
        :returns: AdminUpdateAuthEventFeedbackResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises UserPoolAddOnNotEnabledException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminUpdateDeviceStatus")
    def admin_update_device_status(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        device_key: DeviceKeyType,
        device_remembered_status: DeviceRememberedStatusType | None = None,
        **kwargs,
    ) -> AdminUpdateDeviceStatusResponse:
        """Updates the status of a user's device so that it is marked as remembered
        or not remembered for the purpose of device authentication. Device
        authentication is a "remember me" mechanism that silently completes
        sign-in from trusted devices with a device key instead of a
        user-provided MFA code. This operation changes the status of a device
        without deleting it, so you can enable it again later. For more
        information about device authentication, see `Working with
        devices <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to change a user's device status.
        :param username: The name of the user that you want to query or modify.
        :param device_key: The unique identifier, or device key, of the device that you want to
        update the status for.
        :param device_remembered_status: To enable device authentication with the specified device, set to
        ``remembered``.
        :returns: AdminUpdateDeviceStatusResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AdminUpdateUserAttributes")
    def admin_update_user_attributes(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        user_attributes: AttributeListType,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> AdminUpdateUserAttributesResponse:
        """Updates the specified user's attributes. To delete an attribute from
        your user, submit the attribute in your API request with a blank value.

        For custom attributes, you must add a ``custom:`` prefix to the
        attribute name, for example ``custom:department``.

        This operation can set a user's email address or phone number as
        verified and permit immediate sign-in in user pools that require
        verification of these attributes. To do this, set the ``email_verified``
        or ``phone_number_verified`` attribute to ``true``.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param user_pool_id: The ID of the user pool where you want to update user attributes.
        :param username: The name of the user that you want to query or modify.
        :param user_attributes: An array of name-value pairs representing user attributes.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: AdminUpdateUserAttributesResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises AliasExistsException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        """
        raise NotImplementedError

    @handler("AdminUserGlobalSignOut")
    def admin_user_global_sign_out(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        **kwargs,
    ) -> AdminUserGlobalSignOutResponse:
        """Invalidates the identity, access, and refresh tokens that Amazon Cognito
        issued to a user. Call this operation with your administrative
        credentials when your user signs out of your app. This results in the
        following behavior.

        -  Amazon Cognito no longer accepts *token-authorized* user operations
           that you authorize with a signed-out user's access tokens. For more
           information, see `Using the Amazon Cognito user pools API and user
           pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

           Amazon Cognito returns an ``Access Token has been revoked`` error
           when your app attempts to authorize a user pools API request with a
           revoked access token that contains the scope
           ``aws.cognito.signin.user.admin``.

        -  Amazon Cognito no longer accepts a signed-out user's ID token in a
           `GetId <https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetId.html>`__
           request to an identity pool with ``ServerSideTokenCheck`` enabled for
           its user pool IdP configuration in
           `CognitoIdentityProvider <https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_CognitoIdentityProvider.html>`__.

        -  Amazon Cognito no longer accepts a signed-out user's refresh tokens
           in refresh requests.

        Other requests might be valid until your user's token expires. This
        operation doesn't clear the `managed
        login <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html>`__
        session cookie. To clear the session for a user who signed in with
        managed login or the classic hosted UI, direct their browser session to
        the `logout
        endpoint <https://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to sign out a user.
        :param username: The name of the user that you want to query or modify.
        :returns: AdminUserGlobalSignOutResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("AssociateSoftwareToken")
    def associate_software_token(
        self,
        context: RequestContext,
        access_token: TokenModelType | None = None,
        session: SessionType | None = None,
        **kwargs,
    ) -> AssociateSoftwareTokenResponse:
        """Begins setup of time-based one-time password (TOTP) multi-factor
        authentication (MFA) for a user, with a unique private key that Amazon
        Cognito generates and returns in the API response. You can authorize an
        ``AssociateSoftwareToken`` request with either the user's access token,
        or a session string from a challenge response that you received from
        Amazon Cognito.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param session: The session identifier that maintains the state of authentication
        requests and challenge responses.
        :returns: AssociateSoftwareTokenResponse
        :raises ConcurrentModificationException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises ResourceNotFoundException:
        :raises InternalErrorException:
        :raises SoftwareTokenMFANotFoundException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("ChangePassword")
    def change_password(
        self,
        context: RequestContext,
        proposed_password: PasswordType,
        access_token: TokenModelType,
        previous_password: PasswordType | None = None,
        **kwargs,
    ) -> ChangePasswordResponse:
        """Changes the password for the currently signed-in user.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param proposed_password: A new password that you prompted the user to enter in your application.
        :param access_token: A valid access token that Amazon Cognito issued to the user whose
        password you want to change.
        :param previous_password: The user's previous password.
        :returns: ChangePasswordResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises InvalidPasswordException:
        :raises PasswordHistoryPolicyViolationException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("CompleteWebAuthnRegistration")
    def complete_web_authn_registration(
        self, context: RequestContext, access_token: TokenModelType, credential: Document, **kwargs
    ) -> CompleteWebAuthnRegistrationResponse:
        """Completes registration of a passkey authenticator for the currently
        signed-in user.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param credential: A
        `RegistrationResponseJSON <https://www.
        :returns: CompleteWebAuthnRegistrationResponse
        :raises ForbiddenException:
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises LimitExceededException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises WebAuthnNotEnabledException:
        :raises WebAuthnChallengeNotFoundException:
        :raises WebAuthnRelyingPartyMismatchException:
        :raises WebAuthnClientMismatchException:
        :raises WebAuthnOriginNotAllowedException:
        :raises WebAuthnCredentialNotSupportedException:
        """
        raise NotImplementedError

    @handler("ConfirmDevice")
    def confirm_device(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        device_key: DeviceKeyType,
        device_secret_verifier_config: DeviceSecretVerifierConfigType | None = None,
        device_name: DeviceNameType | None = None,
        **kwargs,
    ) -> ConfirmDeviceResponse:
        """Confirms a device that a user wants to remember. A remembered device is
        a "Remember me on this device" option for user pools that perform
        authentication with the device key of a trusted device in the back end,
        instead of a user-provided MFA code. For more information about device
        authentication, see `Working with user devices in your user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param device_key: The unique identifier, or device key, of the device that you want to
        update the status for.
        :param device_secret_verifier_config: The configuration of the device secret verifier.
        :param device_name: A friendly name for the device, for example ``MyMobilePhone``.
        :returns: ConfirmDeviceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises InvalidPasswordException:
        :raises InvalidLambdaResponseException:
        :raises UsernameExistsException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises DeviceKeyExistsException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("ConfirmForgotPassword")
    def confirm_forgot_password(
        self,
        context: RequestContext,
        client_id: ClientIdType,
        username: UsernameType,
        confirmation_code: ConfirmationCodeType,
        password: PasswordType,
        secret_hash: SecretHashType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        user_context_data: UserContextDataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> ConfirmForgotPasswordResponse:
        """This public API operation accepts a confirmation code that Amazon
        Cognito sent to a user and accepts a new password for that user.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param client_id: The ID of the app client where the user wants to reset their password.
        :param username: The name of the user that you want to query or modify.
        :param confirmation_code: The confirmation code that your user pool delivered when your user
        requested to reset their password.
        :param password: The new password that your user wants to set.
        :param secret_hash: A keyed-hash message authentication code (HMAC) calculated using the
        secret key of a user pool client and username plus the client ID in the
        message.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: ConfirmForgotPasswordResponse
        :raises ResourceNotFoundException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidParameterException:
        :raises InvalidPasswordException:
        :raises PasswordHistoryPolicyViolationException:
        :raises NotAuthorizedException:
        :raises CodeMismatchException:
        :raises ExpiredCodeException:
        :raises TooManyFailedAttemptsException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("ConfirmSignUp")
    def confirm_sign_up(
        self,
        context: RequestContext,
        client_id: ClientIdType,
        username: UsernameType,
        confirmation_code: ConfirmationCodeType,
        secret_hash: SecretHashType | None = None,
        force_alias_creation: ForceAliasCreation | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        user_context_data: UserContextDataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        session: SessionType | None = None,
        **kwargs,
    ) -> ConfirmSignUpResponse:
        """Confirms the account of a new user. This public API operation submits a
        code that Amazon Cognito sent to your user when they signed up in your
        user pool. After your user enters their code, they confirm ownership of
        the email address or phone number that they provided, and their user
        account becomes active. Depending on your user pool configuration, your
        users will receive their confirmation code in an email or SMS message.

        Local users who signed up in your user pool are the only type of user
        who can confirm sign-up with a code. Users who federate through an
        external identity provider (IdP) have already been confirmed by their
        IdP.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param client_id: The ID of the app client associated with the user pool.
        :param username: The name of the user that you want to query or modify.
        :param confirmation_code: The confirmation code that your user pool sent in response to the
        ``SignUp`` request.
        :param secret_hash: A keyed-hash message authentication code (HMAC) calculated using the
        secret key of a user pool client and username plus the client ID in the
        message.
        :param force_alias_creation: When ``true``, forces user confirmation despite any existing aliases.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :param session: The optional session ID from a ``SignUp`` API request.
        :returns: ConfirmSignUpResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises NotAuthorizedException:
        :raises TooManyFailedAttemptsException:
        :raises CodeMismatchException:
        :raises ExpiredCodeException:
        :raises InvalidLambdaResponseException:
        :raises AliasExistsException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("CreateGroup")
    def create_group(
        self,
        context: RequestContext,
        group_name: GroupNameType,
        user_pool_id: UserPoolIdType,
        description: DescriptionType | None = None,
        role_arn: ArnType | None = None,
        precedence: PrecedenceType | None = None,
        **kwargs,
    ) -> CreateGroupResponse:
        """Creates a new group in the specified user pool. For more information
        about user pool groups, see `Adding groups to a user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param group_name: A name for the group.
        :param user_pool_id: The ID of the user pool where you want to create a user group.
        :param description: A description of the group that you're creating.
        :param role_arn: The Amazon Resource Name (ARN) for the IAM role that you want to
        associate with the group.
        :param precedence: A non-negative integer value that specifies the precedence of this group
        relative to the other groups that a user can belong to in the user pool.
        :returns: CreateGroupResponse
        :raises InvalidParameterException:
        :raises GroupExistsException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("CreateIdentityProvider")
    def create_identity_provider(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        provider_name: ProviderNameTypeV2,
        provider_type: IdentityProviderTypeType,
        provider_details: ProviderDetailsType,
        attribute_mapping: AttributeMappingType | None = None,
        idp_identifiers: IdpIdentifiersListType | None = None,
        **kwargs,
    ) -> CreateIdentityProviderResponse:
        """Adds a configuration and trust relationship between a third-party
        identity provider (IdP) and a user pool. Amazon Cognito accepts sign-in
        with third-party identity providers through managed login and OIDC
        relying-party libraries. For more information, see `Third-party IdP
        sign-in <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The Id of the user pool where you want to create an IdP.
        :param provider_name: The name that you want to assign to the IdP.
        :param provider_type: The type of IdP that you want to add.
        :param provider_details: The scopes, URLs, and identifiers for your external identity provider.
        :param attribute_mapping: A mapping of IdP attributes to standard and custom user pool attributes.
        :param idp_identifiers: An array of IdP identifiers, for example
        ``"IdPIdentifiers": [ "MyIdP", "MyIdP2" ]``.
        :returns: CreateIdentityProviderResponse
        :raises InvalidParameterException:
        :raises DuplicateProviderException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("CreateManagedLoginBranding")
    def create_managed_login_branding(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        use_cognito_provided_values: BooleanType | None = None,
        settings: Document | None = None,
        assets: AssetListType | None = None,
        **kwargs,
    ) -> CreateManagedLoginBrandingResponse:
        """Creates a new set of branding settings for a user pool style and
        associates it with an app client. This operation is the programmatic
        option for the creation of a new style in the branding designer.

        Provides values for UI customization in a ``Settings`` JSON object and
        image files in an ``Assets`` array. To send the JSON object ``Document``
        type parameter in ``Settings``, you might need to update to the most
        recent version of your Amazon Web Services SDK. To create a new style
        with default settings, set ``UseCognitoProvidedValues`` to ``true`` and
        don't provide values for any other options.

        This operation has a 2-megabyte request-size limit and include the CSS
        settings and image assets for your app client. Your branding settings
        might exceed 2MB in size. Amazon Cognito doesn't require that you pass
        all parameters in one request and preserves existing style settings that
        you don't specify. If your request is larger than 2MB, separate it into
        multiple requests, each with a size smaller than the limit.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to create a new branding style.
        :param client_id: The app client that you want to create the branding style for.
        :param use_cognito_provided_values: When true, applies the default branding style options.
        :param settings: A JSON file, encoded as a ``Document`` type, with the the settings that
        you want to apply to your style.
        :param assets: An array of image files that you want to apply to functions like
        backgrounds, logos, and icons.
        :returns: CreateManagedLoginBrandingResponse
        :raises ResourceNotFoundException:
        :raises ConcurrentModificationException:
        :raises ManagedLoginBrandingExistsException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises LimitExceededException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("CreateResourceServer")
    def create_resource_server(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        identifier: ResourceServerIdentifierType,
        name: ResourceServerNameType,
        scopes: ResourceServerScopeListType | None = None,
        **kwargs,
    ) -> CreateResourceServerResponse:
        """Creates a new OAuth2.0 resource server and defines custom scopes within
        it. Resource servers are associated with custom scopes and
        machine-to-machine (M2M) authorization. For more information, see
        `Access control with resource
        servers <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to create a resource server.
        :param identifier: A unique resource server identifier for the resource server.
        :param name: A friendly name for the resource server.
        :param scopes: A list of custom scopes.
        :returns: CreateResourceServerResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("CreateUserImportJob")
    def create_user_import_job(
        self,
        context: RequestContext,
        job_name: UserImportJobNameType,
        user_pool_id: UserPoolIdType,
        cloud_watch_logs_role_arn: ArnType,
        **kwargs,
    ) -> CreateUserImportJobResponse:
        """Creates a user import job. You can import users into user pools from a
        comma-separated values (CSV) file without adding Amazon Cognito MAU
        costs to your Amazon Web Services bill.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param job_name: A friendly name for the user import job.
        :param user_pool_id: The ID of the user pool that you want to import users into.
        :param cloud_watch_logs_role_arn: You must specify an IAM role that has permission to log import-job
        results to Amazon CloudWatch Logs.
        :returns: CreateUserImportJobResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises PreconditionNotMetException:
        :raises NotAuthorizedException:
        :raises LimitExceededException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("CreateUserPool")
    def create_user_pool(
        self,
        context: RequestContext,
        pool_name: UserPoolNameType,
        policies: UserPoolPolicyType | None = None,
        deletion_protection: DeletionProtectionType | None = None,
        lambda_config: LambdaConfigType | None = None,
        auto_verified_attributes: VerifiedAttributesListType | None = None,
        alias_attributes: AliasAttributesListType | None = None,
        username_attributes: UsernameAttributesListType | None = None,
        sms_verification_message: SmsVerificationMessageType | None = None,
        email_verification_message: EmailVerificationMessageType | None = None,
        email_verification_subject: EmailVerificationSubjectType | None = None,
        verification_message_template: VerificationMessageTemplateType | None = None,
        sms_authentication_message: SmsVerificationMessageType | None = None,
        mfa_configuration: UserPoolMfaType | None = None,
        user_attribute_update_settings: UserAttributeUpdateSettingsType | None = None,
        device_configuration: DeviceConfigurationType | None = None,
        email_configuration: EmailConfigurationType | None = None,
        sms_configuration: SmsConfigurationType | None = None,
        user_pool_tags: UserPoolTagsType | None = None,
        admin_create_user_config: AdminCreateUserConfigType | None = None,
        schema: SchemaAttributesListType | None = None,
        user_pool_add_ons: UserPoolAddOnsType | None = None,
        username_configuration: UsernameConfigurationType | None = None,
        account_recovery_setting: AccountRecoverySettingType | None = None,
        user_pool_tier: UserPoolTierType | None = None,
        **kwargs,
    ) -> CreateUserPoolResponse:
        """Creates a new Amazon Cognito user pool. This operation sets basic and
        advanced configuration options.

        If you don't provide a value for an attribute, Amazon Cognito sets it to
        its default value.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param pool_name: A friendly name for your user pool.
        :param policies: The password policy and sign-in policy in the user pool.
        :param deletion_protection: When active, ``DeletionProtection`` prevents accidental deletion of your
        user pool.
        :param lambda_config: A collection of user pool Lambda triggers.
        :param auto_verified_attributes: The attributes that you want your user pool to automatically verify.
        :param alias_attributes: Attributes supported as an alias for this user pool.
        :param username_attributes: Specifies whether a user can use an email address or phone number as a
        username when they sign up.
        :param sms_verification_message: This parameter is no longer used.
        :param email_verification_message: This parameter is no longer used.
        :param email_verification_subject: This parameter is no longer used.
        :param verification_message_template: The template for the verification message that your user pool delivers
        to users who set an email address or phone number attribute.
        :param sms_authentication_message: The contents of the SMS message that your user pool sends to users in
        SMS OTP and MFA authentication.
        :param mfa_configuration: Sets multi-factor authentication (MFA) to be on, off, or optional.
        :param user_attribute_update_settings: The settings for updates to user attributes.
        :param device_configuration: The device-remembering configuration for a user pool.
        :param email_configuration: The email configuration of your user pool.
        :param sms_configuration: The settings for your Amazon Cognito user pool to send SMS messages with
        Amazon Simple Notification Service.
        :param user_pool_tags: The tag keys and values to assign to the user pool.
        :param admin_create_user_config: The configuration for administrative creation of users.
        :param schema: An array of attributes for the new user pool.
        :param user_pool_add_ons: Contains settings for activation of threat protection, including the
        operating mode and additional authentication types.
        :param username_configuration: Sets the case sensitivity option for sign-in usernames.
        :param account_recovery_setting: The available verified method a user can use to recover their password
        when they call ``ForgotPassword``.
        :param user_pool_tier: The user pool `feature
        plan <https://docs.
        :returns: CreateUserPoolResponse
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises NotAuthorizedException:
        :raises UserPoolTaggingException:
        :raises InternalErrorException:
        :raises TierChangeNotAllowedException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("CreateUserPoolClient")
    def create_user_pool_client(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_name: ClientNameType,
        generate_secret: GenerateSecret | None = None,
        refresh_token_validity: RefreshTokenValidityType | None = None,
        access_token_validity: AccessTokenValidityType | None = None,
        id_token_validity: IdTokenValidityType | None = None,
        token_validity_units: TokenValidityUnitsType | None = None,
        read_attributes: ClientPermissionListType | None = None,
        write_attributes: ClientPermissionListType | None = None,
        explicit_auth_flows: ExplicitAuthFlowsListType | None = None,
        supported_identity_providers: SupportedIdentityProvidersListType | None = None,
        callback_urls: CallbackURLsListType | None = None,
        logout_urls: LogoutURLsListType | None = None,
        default_redirect_uri: RedirectUrlType | None = None,
        allowed_o_auth_flows: OAuthFlowsType | None = None,
        allowed_o_auth_scopes: ScopeListType | None = None,
        allowed_o_auth_flows_user_pool_client: BooleanType | None = None,
        analytics_configuration: AnalyticsConfigurationType | None = None,
        prevent_user_existence_errors: PreventUserExistenceErrorTypes | None = None,
        enable_token_revocation: WrappedBooleanType | None = None,
        enable_propagate_additional_user_context_data: WrappedBooleanType | None = None,
        auth_session_validity: AuthSessionValidityType | None = None,
        refresh_token_rotation: RefreshTokenRotationType | None = None,
        **kwargs,
    ) -> CreateUserPoolClientResponse:
        """Creates an app client in a user pool. This operation sets basic and
        advanced configuration options.

        Unlike app clients created in the console, Amazon Cognito doesn't
        automatically assign a branding style to app clients that you configure
        with this API operation. Managed login and classic hosted UI pages
        aren't available for your client until after you apply a branding style.

        If you don't provide a value for an attribute, Amazon Cognito sets it to
        its default value.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to create an app client.
        :param client_name: A friendly name for the app client that you want to create.
        :param generate_secret: When ``true``, generates a client secret for the app client.
        :param refresh_token_validity: The refresh token time limit.
        :param access_token_validity: The access token time limit.
        :param id_token_validity: The ID token time limit.
        :param token_validity_units: The units that validity times are represented in.
        :param read_attributes: The list of user attributes that you want your app client to have read
        access to.
        :param write_attributes: The list of user attributes that you want your app client to have write
        access to.
        :param explicit_auth_flows: The `authentication
        flows <https://docs.
        :param supported_identity_providers: A list of provider names for the identity providers (IdPs) that are
        supported on this client.
        :param callback_urls: A list of allowed redirect, or callback, URLs for managed login
        authentication.
        :param logout_urls: A list of allowed logout URLs for managed login authentication.
        :param default_redirect_uri: The default redirect URI.
        :param allowed_o_auth_flows: The OAuth grant types that you want your app client to generate for
        clients in managed login authentication.
        :param allowed_o_auth_scopes: The OAuth, OpenID Connect (OIDC), and custom scopes that you want to
        permit your app client to authorize access with.
        :param allowed_o_auth_flows_user_pool_client: Set to ``true`` to use OAuth 2.
        :param analytics_configuration: The user pool analytics configuration for collecting metrics and sending
        them to your Amazon Pinpoint campaign.
        :param prevent_user_existence_errors: When ``ENABLED``, suppresses messages that might indicate a valid user
        exists when someone attempts sign-in.
        :param enable_token_revocation: Activates or deactivates `token
        revocation <https://docs.
        :param enable_propagate_additional_user_context_data: When ``true``, your application can include additional
        ``UserContextData`` in authentication requests.
        :param auth_session_validity: Amazon Cognito creates a session token for each API request in an
        authentication flow.
        :param refresh_token_rotation: The configuration of your app client for refresh token rotation.
        :returns: CreateUserPoolClientResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises NotAuthorizedException:
        :raises ScopeDoesNotExistException:
        :raises InvalidOAuthFlowException:
        :raises InternalErrorException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("CreateUserPoolDomain")
    def create_user_pool_domain(
        self,
        context: RequestContext,
        domain: DomainType,
        user_pool_id: UserPoolIdType,
        managed_login_version: WrappedIntegerType | None = None,
        custom_domain_config: CustomDomainConfigType | None = None,
        **kwargs,
    ) -> CreateUserPoolDomainResponse:
        """A user pool domain hosts managed login, an authorization server and web
        server for authentication in your application. This operation creates a
        new user pool prefix domain or custom domain and sets the managed login
        branding version. Set the branding version to ``1`` for hosted UI
        (classic) or ``2`` for managed login. When you choose a custom domain,
        you must provide an SSL certificate in the US East (N. Virginia) Amazon
        Web Services Region in your request.

        Your prefix domain might take up to one minute to take effect. Your
        custom domain is online within five minutes, but it can take up to one
        hour to distribute your SSL certificate.

        For more information about adding a custom domain to your user pool, see
        `Configuring a user pool
        domain <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param domain: The domain string.
        :param user_pool_id: The ID of the user pool where you want to add a domain.
        :param managed_login_version: The version of managed login branding that you want to apply to your
        domain.
        :param custom_domain_config: The configuration for a custom domain.
        :returns: CreateUserPoolDomainResponse
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises ConcurrentModificationException:
        :raises ResourceNotFoundException:
        :raises LimitExceededException:
        :raises InternalErrorException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("DeleteGroup")
    def delete_group(
        self,
        context: RequestContext,
        group_name: GroupNameType,
        user_pool_id: UserPoolIdType,
        **kwargs,
    ) -> None:
        """Deletes a group from the specified user pool. When you delete a group,
        that group no longer contributes to users' ``cognito:preferred_group``
        or ``cognito:groups`` claims, and no longer influence access-control
        decision that are based on group membership. For more information about
        user pool groups, see `Adding groups to a user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param group_name: The name of the group that you want to delete.
        :param user_pool_id: The ID of the user pool where you want to delete the group.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteIdentityProvider")
    def delete_identity_provider(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        provider_name: ProviderNameType,
        **kwargs,
    ) -> None:
        """Deletes a user pool identity provider (IdP). After you delete an IdP,
        users can no longer sign in to your user pool through that IdP. For more
        information about user pool IdPs, see `Third-party IdP
        sign-in <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to delete the identity provider.
        :param provider_name: The name of the IdP that you want to delete.
        :raises InvalidParameterException:
        :raises UnsupportedIdentityProviderException:
        :raises ConcurrentModificationException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteManagedLoginBranding")
    def delete_managed_login_branding(
        self,
        context: RequestContext,
        managed_login_branding_id: ManagedLoginBrandingIdType,
        user_pool_id: UserPoolIdType,
        **kwargs,
    ) -> None:
        """Deletes a managed login branding style. When you delete a style, you
        delete the branding association for an app client. When an app client
        doesn't have a style assigned, your managed login pages for that app
        client are nonfunctional until you create a new style or switch the
        domain branding version.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param managed_login_branding_id: The ID of the managed login branding style that you want to delete.
        :param user_pool_id: The ID of the user pool that contains the managed login branding style
        that you want to delete.
        :raises ResourceNotFoundException:
        :raises ConcurrentModificationException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteResourceServer")
    def delete_resource_server(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        identifier: ResourceServerIdentifierType,
        **kwargs,
    ) -> None:
        """Deletes a resource server. After you delete a resource server, users can
        no longer generate access tokens with scopes that are associate with
        that resource server.

        Resource servers are associated with custom scopes and
        machine-to-machine (M2M) authorization. For more information, see
        `Access control with resource
        servers <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to delete the resource server.
        :param identifier: The identifier of the resource server that you want to delete.
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteUser")
    def delete_user(self, context: RequestContext, access_token: TokenModelType, **kwargs) -> None:
        """Deletes the profile of the currently signed-in user. A deleted user
        profile can no longer be used to sign in and can't be restored.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("DeleteUserAttributes")
    def delete_user_attributes(
        self,
        context: RequestContext,
        user_attribute_names: AttributeNameListType,
        access_token: TokenModelType,
        **kwargs,
    ) -> DeleteUserAttributesResponse:
        """Deletes attributes from the currently signed-in user. For example, your
        application can submit a request to this operation when a user wants to
        remove their ``birthdate`` attribute value.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param user_attribute_names: An array of strings representing the user attribute names you want to
        delete.
        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :returns: DeleteUserAttributesResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("DeleteUserPool")
    def delete_user_pool(
        self, context: RequestContext, user_pool_id: UserPoolIdType, **kwargs
    ) -> None:
        """Deletes a user pool. After you delete a user pool, users can no longer
        sign in to any associated applications.

        When you delete a user pool, it's no longer visible or operational in
        your Amazon Web Services account. Amazon Cognito retains deleted user
        pools in an inactive state for 14 days, then begins a cleanup process
        that fully removes them from Amazon Web Services systems. In case of
        accidental deletion, contact Amazon Web ServicesSupport within 14 days
        for restoration assistance.

        Amazon Cognito begins full deletion of all resources from deleted user
        pools after 14 days. In the case of large user pools, the cleanup
        process might take significant additional time before all user data is
        permanently deleted.

        :param user_pool_id: The ID of the user pool that you want to delete.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserImportInProgressException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteUserPoolClient")
    def delete_user_pool_client(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        **kwargs,
    ) -> None:
        """Deletes a user pool app client. After you delete an app client, users
        can no longer sign in to the associated application.

        :param user_pool_id: The ID of the user pool where you want to delete the client.
        :param client_id: The ID of the user pool app client that you want to delete.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises ConcurrentModificationException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteUserPoolDomain")
    def delete_user_pool_domain(
        self, context: RequestContext, domain: DomainType, user_pool_id: UserPoolIdType, **kwargs
    ) -> DeleteUserPoolDomainResponse:
        """Given a user pool ID and domain identifier, deletes a user pool domain.
        After you delete a user pool domain, your managed login pages and
        authorization server are no longer available.

        :param domain: The domain that you want to delete.
        :param user_pool_id: The ID of the user pool where you want to delete the domain.
        :returns: DeleteUserPoolDomainResponse
        :raises NotAuthorizedException:
        :raises InvalidParameterException:
        :raises ConcurrentModificationException:
        :raises ResourceNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DeleteWebAuthnCredential")
    def delete_web_authn_credential(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        credential_id: StringType,
        **kwargs,
    ) -> DeleteWebAuthnCredentialResponse:
        """Deletes a registered passkey, or WebAuthn, authenticator for the
        currently signed-in user.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param credential_id: The unique identifier of the passkey that you want to delete.
        :returns: DeleteWebAuthnCredentialResponse
        :raises ForbiddenException:
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises NotAuthorizedException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeIdentityProvider")
    def describe_identity_provider(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        provider_name: ProviderNameType,
        **kwargs,
    ) -> DescribeIdentityProviderResponse:
        """Given a user pool ID and identity provider (IdP) name, returns details
        about the IdP.

        :param user_pool_id: The ID of the user pool that has the IdP that you want to describe.
        :param provider_name: The name of the IdP that you want to describe.
        :returns: DescribeIdentityProviderResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeManagedLoginBranding")
    def describe_managed_login_branding(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        managed_login_branding_id: ManagedLoginBrandingIdType,
        return_merged_resources: BooleanType | None = None,
        **kwargs,
    ) -> DescribeManagedLoginBrandingResponse:
        """Given the ID of a managed login branding style, returns detailed
        information about the style.

        :param user_pool_id: The ID of the user pool that contains the managed login branding style
        that you want to get information about.
        :param managed_login_branding_id: The ID of the managed login branding style that you want to get more
        information about.
        :param return_merged_resources: When ``true``, returns values for branding options that are unchanged
        from Amazon Cognito defaults.
        :returns: DescribeManagedLoginBrandingResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeManagedLoginBrandingByClient")
    def describe_managed_login_branding_by_client(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        return_merged_resources: BooleanType | None = None,
        **kwargs,
    ) -> DescribeManagedLoginBrandingByClientResponse:
        """Given the ID of a user pool app client, returns detailed information
        about the style assigned to the app client.

        :param user_pool_id: The ID of the user pool that contains the app client where you want more
        information about the managed login branding style.
        :param client_id: The app client that's assigned to the branding style that you want more
        information about.
        :param return_merged_resources: When ``true``, returns values for branding options that are unchanged
        from Amazon Cognito defaults.
        :returns: DescribeManagedLoginBrandingByClientResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeResourceServer")
    def describe_resource_server(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        identifier: ResourceServerIdentifierType,
        **kwargs,
    ) -> DescribeResourceServerResponse:
        """Describes a resource server. For more information about resource
        servers, see `Access control with resource
        servers <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html>`__.

        :param user_pool_id: The ID of the user pool that hosts the resource server.
        :param identifier: A unique resource server identifier for the resource server.
        :returns: DescribeResourceServerResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeRiskConfiguration")
    def describe_risk_configuration(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType | None = None,
        **kwargs,
    ) -> DescribeRiskConfigurationResponse:
        """Given an app client or user pool ID where threat protection is
        configured, describes the risk configuration. This operation returns
        details about adaptive authentication, compromised credentials, and
        IP-address allow- and denylists. For more information about threat
        protection, see `Threat
        protection <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html>`__.

        :param user_pool_id: The ID of the user pool with the risk configuration that you want to
        inspect.
        :param client_id: The ID of the app client with the risk configuration that you want to
        inspect.
        :returns: DescribeRiskConfigurationResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserPoolAddOnNotEnabledException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeUserImportJob")
    def describe_user_import_job(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        job_id: UserImportJobIdType,
        **kwargs,
    ) -> DescribeUserImportJobResponse:
        """Describes a user import job. For more information about user CSV import,
        see `Importing users from a CSV
        file <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html>`__.

        :param user_pool_id: The ID of the user pool that's associated with the import job.
        :param job_id: The Id of the user import job that you want to describe.
        :returns: DescribeUserImportJobResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeUserPool")
    def describe_user_pool(
        self, context: RequestContext, user_pool_id: UserPoolIdType, **kwargs
    ) -> DescribeUserPoolResponse:
        """Given a user pool ID, returns configuration information. This operation
        is useful when you want to inspect an existing user pool and
        programmatically replicate the configuration to another user pool.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool you want to describe.
        :returns: DescribeUserPoolResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserPoolTaggingException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeUserPoolClient")
    def describe_user_pool_client(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        **kwargs,
    ) -> DescribeUserPoolClientResponse:
        """Given an app client ID, returns configuration information. This
        operation is useful when you want to inspect an existing app client and
        programmatically replicate the configuration to another app client. For
        more information about app clients, see `App
        clients <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that contains the app client you want to
        describe.
        :param client_id: The ID of the app client that you want to describe.
        :returns: DescribeUserPoolClientResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("DescribeUserPoolDomain")
    def describe_user_pool_domain(
        self, context: RequestContext, domain: DomainType, **kwargs
    ) -> DescribeUserPoolDomainResponse:
        """Given a user pool domain name, returns information about the domain
        configuration.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param domain: The domain that you want to describe.
        :returns: DescribeUserPoolDomainResponse
        :raises NotAuthorizedException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ForgetDevice")
    def forget_device(
        self,
        context: RequestContext,
        device_key: DeviceKeyType,
        access_token: TokenModelType | None = None,
        **kwargs,
    ) -> None:
        """Given a device key, deletes a remembered device as the currently
        signed-in user. For more information about device authentication, see
        `Working with user devices in your user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param device_key: The unique identifier, or device key, of the device that the user wants
        to forget.
        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InvalidUserPoolConfigurationException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("ForgotPassword")
    def forgot_password(
        self,
        context: RequestContext,
        client_id: ClientIdType,
        username: UsernameType,
        secret_hash: SecretHashType | None = None,
        user_context_data: UserContextDataType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> ForgotPasswordResponse:
        """Sends a password-reset confirmation code for the currently signed-in
        user.

        For the ``Username`` parameter, you can use the username or user alias.

        If neither a verified phone number nor a verified email exists, Amazon
        Cognito responds with an ``InvalidParameterException`` error . If your
        app client has a client secret and you don't provide a ``SECRET_HASH``
        parameter, this API returns ``NotAuthorizedException``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param client_id: The ID of the user pool app client associated with the current signed-in
        user.
        :param username: The name of the user that you want to query or modify.
        :param secret_hash: A keyed-hash message authentication code (HMAC) calculated using the
        secret key of a user pool client and username plus the client ID in the
        message.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: ForgotPasswordResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises NotAuthorizedException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises CodeDeliveryFailureException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("GetCSVHeader")
    def get_csv_header(
        self, context: RequestContext, user_pool_id: UserPoolIdType, **kwargs
    ) -> GetCSVHeaderResponse:
        """Given a user pool ID, generates a comma-separated value (CSV) list
        populated with available user attributes in the user pool. This list is
        the header for the CSV file that determines the users in a user import
        job. Save the content of ``CSVHeader`` in the response as a ``.csv``
        file and populate it with the usernames and attributes of users that you
        want to import. For more information about CSV user import, see
        `Importing users from a CSV
        file <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that you want to import users into.
        :returns: GetCSVHeaderResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("GetDevice")
    def get_device(
        self,
        context: RequestContext,
        device_key: DeviceKeyType,
        access_token: TokenModelType | None = None,
        **kwargs,
    ) -> GetDeviceResponse:
        """Given a device key, returns information about a remembered device for
        the current user. For more information about device authentication, see
        `Working with user devices in your user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param device_key: The key of the device that you want to get information about.
        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :returns: GetDeviceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises InvalidUserPoolConfigurationException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("GetGroup")
    def get_group(
        self,
        context: RequestContext,
        group_name: GroupNameType,
        user_pool_id: UserPoolIdType,
        **kwargs,
    ) -> GetGroupResponse:
        """Given a user pool ID and a group name, returns information about the
        user group.

        For more information about user pool groups, see `Adding groups to a
        user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param group_name: The name of the group that you want to get information about.
        :param user_pool_id: The ID of the user pool that contains the group that you want to query.
        :returns: GetGroupResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("GetIdentityProviderByIdentifier")
    def get_identity_provider_by_identifier(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        idp_identifier: IdpIdentifierType,
        **kwargs,
    ) -> GetIdentityProviderByIdentifierResponse:
        """Given the identifier of an identity provider (IdP), for example
        ``examplecorp``, returns information about the user pool configuration
        for that IdP. For more information about IdPs, see `Third-party IdP
        sign-in <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html>`__.

        :param user_pool_id: The ID of the user pool where you want to get information about the IdP.
        :param idp_identifier: The identifier that you assigned to your user pool.
        :returns: GetIdentityProviderByIdentifierResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("GetLogDeliveryConfiguration")
    def get_log_delivery_configuration(
        self, context: RequestContext, user_pool_id: UserPoolIdType, **kwargs
    ) -> GetLogDeliveryConfigurationResponse:
        """Given a user pool ID, returns the logging configuration. User pools can
        export message-delivery error and threat-protection activity logs to
        external Amazon Web Services services. For more information, see
        `Exporting user pool
        logs <https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that has the logging configuration that you want
        to view.
        :returns: GetLogDeliveryConfigurationResponse
        :raises InvalidParameterException:
        :raises InternalErrorException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetSigningCertificate")
    def get_signing_certificate(
        self, context: RequestContext, user_pool_id: UserPoolIdType, **kwargs
    ) -> GetSigningCertificateResponse:
        """Given a user pool ID, returns the signing certificate for SAML 2.0
        federation.

        Issued certificates are valid for 10 years from the date of issue.
        Amazon Cognito issues and assigns a new signing certificate annually.
        This renewal process returns a new value in the response to
        ``GetSigningCertificate``, but doesn't invalidate the original
        certificate.

        For more information, see `Signing SAML
        requests <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-SAML-signing-encryption.html#cognito-user-pools-SAML-signing>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to view the signing certificate.
        :returns: GetSigningCertificateResponse
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetTokensFromRefreshToken")
    def get_tokens_from_refresh_token(
        self,
        context: RequestContext,
        refresh_token: TokenModelType,
        client_id: ClientIdType,
        client_secret: ClientSecretType | None = None,
        device_key: DeviceKeyType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> GetTokensFromRefreshTokenResponse:
        """Given a refresh token, issues new ID, access, and optionally refresh
        tokens for the user who owns the submitted token. This operation issues
        a new refresh token and invalidates the original refresh token after an
        optional grace period when refresh token rotation is enabled. If refresh
        token rotation is disabled, issues new ID and access tokens only.

        :param refresh_token: A valid refresh token that can authorize the request for new tokens.
        :param client_id: The app client that issued the refresh token to the user who wants to
        request new tokens.
        :param client_secret: The client secret of the requested app client, if the client has a
        secret.
        :param device_key: When you enable device remembering, Amazon Cognito issues a device key
        that you can use for device authentication that bypasses multi-factor
        authentication (MFA).
        :param client_metadata: A map of custom key-value pairs that you can provide as input for
        certain custom workflows that this action triggers.
        :returns: GetTokensFromRefreshTokenResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises UserNotFoundException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises ForbiddenException:
        :raises RefreshTokenReuseException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("GetUICustomization")
    def get_ui_customization(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType | None = None,
        **kwargs,
    ) -> GetUICustomizationResponse:
        """Given a user pool ID or app client, returns information about classic
        hosted UI branding that you applied, if any. Returns user-pool level
        branding information if no app client branding is applied, or if you
        don't specify an app client ID. Returns an empty object if you haven't
        applied hosted UI branding to either the client or the user pool. For
        more information, see `Hosted UI (classic)
        branding <https://docs.aws.amazon.com/cognito/latest/developerguide/hosted-ui-classic-branding.html>`__.

        :param user_pool_id: The ID of the user pool that you want to query for branding settings.
        :param client_id: The ID of the app client that you want to query for branding settings.
        :returns: GetUICustomizationResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("GetUser")
    def get_user(
        self, context: RequestContext, access_token: TokenModelType, **kwargs
    ) -> GetUserResponse:
        """Gets user attributes and and MFA settings for the currently signed-in
        user.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :returns: GetUserResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("GetUserAttributeVerificationCode")
    def get_user_attribute_verification_code(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        attribute_name: AttributeNameType,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> GetUserAttributeVerificationCodeResponse:
        """Given an attribute name, sends a user attribute verification code for
        the specified attribute name to the currently signed-in user.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param attribute_name: The name of the attribute that the user wants to verify, for example
        ``email``.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: GetUserAttributeVerificationCodeResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises CodeDeliveryFailureException:
        :raises LimitExceededException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("GetUserAuthFactors")
    def get_user_auth_factors(
        self, context: RequestContext, access_token: TokenModelType, **kwargs
    ) -> GetUserAuthFactorsResponse:
        """Lists the authentication options for the currently signed-in user.
        Returns the following:

        #. The user's multi-factor authentication (MFA) preferences.

        #. The user's options for choice-based authentication with the
           ``USER_AUTH`` flow.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :returns: GetUserAuthFactorsResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("GetUserPoolMfaConfig")
    def get_user_pool_mfa_config(
        self, context: RequestContext, user_pool_id: UserPoolIdType, **kwargs
    ) -> GetUserPoolMfaConfigResponse:
        """Given a user pool ID, returns configuration for sign-in with WebAuthn
        authenticators and for multi-factor authentication (MFA). This operation
        describes the following:

        -  The WebAuthn relying party (RP) ID and user-verification settings.

        -  The required, optional, or disabled state of MFA for all user pool
           users.

        -  The message templates for email and SMS MFA.

        -  The enabled or disabled state of time-based one-time password (TOTP)
           MFA.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to query WebAuthn and MFA
        configuration.
        :returns: GetUserPoolMfaConfigResponse
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("GlobalSignOut")
    def global_sign_out(
        self, context: RequestContext, access_token: TokenModelType, **kwargs
    ) -> GlobalSignOutResponse:
        """Invalidates the identity, access, and refresh tokens that Amazon Cognito
        issued to a user. Call this operation when your user signs out of your
        app. This results in the following behavior.

        -  Amazon Cognito no longer accepts *token-authorized* user operations
           that you authorize with a signed-out user's access tokens. For more
           information, see `Using the Amazon Cognito user pools API and user
           pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

           Amazon Cognito returns an ``Access Token has been revoked`` error
           when your app attempts to authorize a user pools API request with a
           revoked access token that contains the scope
           ``aws.cognito.signin.user.admin``.

        -  Amazon Cognito no longer accepts a signed-out user's ID token in a
           `GetId <https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetId.html>`__
           request to an identity pool with ``ServerSideTokenCheck`` enabled for
           its user pool IdP configuration in
           `CognitoIdentityProvider <https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_CognitoIdentityProvider.html>`__.

        -  Amazon Cognito no longer accepts a signed-out user's refresh tokens
           in refresh requests.

        Other requests might be valid until your user's token expires. This
        operation doesn't clear the `managed
        login <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html>`__
        session cookie. To clear the session for a user who signed in with
        managed login or the classic hosted UI, direct their browser session to
        the `logout
        endpoint <https://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :returns: GlobalSignOutResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("InitiateAuth")
    def initiate_auth(
        self,
        context: RequestContext,
        auth_flow: AuthFlowType,
        client_id: ClientIdType,
        auth_parameters: AuthParametersType | None = None,
        client_metadata: ClientMetadataType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        user_context_data: UserContextDataType | None = None,
        session: SessionType | None = None,
        **kwargs,
    ) -> InitiateAuthResponse:
        """Declares an authentication flow and initiates sign-in for a user in the
        Amazon Cognito user directory. Amazon Cognito might respond with an
        additional challenge or an ``AuthenticationResult`` that contains the
        outcome of a successful authentication. You can't sign in a user with a
        federated IdP with ``InitiateAuth``. For more information, see
        `Authentication <https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html>`__.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param auth_flow: The authentication flow that you want to initiate.
        :param client_id: The ID of the app client that your user wants to sign in to.
        :param auth_parameters: The authentication parameters.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for
        certain custom workflows that this action triggers.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param session: The optional session ID from a ``ConfirmSignUp`` API request.
        :returns: InitiateAuthResponse
        :raises UnsupportedOperationException:
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises UnexpectedLambdaException:
        :raises InvalidUserPoolConfigurationException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("ListDevices")
    def list_devices(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        limit: QueryLimitType | None = None,
        pagination_token: SearchPaginationTokenType | None = None,
        **kwargs,
    ) -> ListDevicesResponse:
        """Lists the devices that Amazon Cognito has registered to the currently
        signed-in user. For more information about device authentication, see
        `Working with user devices in your user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param limit: The maximum number of devices that you want Amazon Cognito to return in
        the response.
        :param pagination_token: This API operation returns a limited number of results.
        :returns: ListDevicesResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("ListGroups")
    def list_groups(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        limit: QueryLimitType | None = None,
        next_token: PaginationKey | None = None,
        **kwargs,
    ) -> ListGroupsResponse:
        """Given a user pool ID, returns user pool groups and their details.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to list user groups.
        :param limit: The maximum number of groups that you want Amazon Cognito to return in
        the response.
        :param next_token: This API operation returns a limited number of results.
        :returns: ListGroupsResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListIdentityProviders")
    def list_identity_providers(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        max_results: ListProvidersLimitType | None = None,
        next_token: PaginationKeyType | None = None,
        **kwargs,
    ) -> ListIdentityProvidersResponse:
        """Given a user pool ID, returns information about configured identity
        providers (IdPs). For more information about IdPs, see `Third-party IdP
        sign-in <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to list IdPs.
        :param max_results: The maximum number of IdPs that you want Amazon Cognito to return in the
        response.
        :param next_token: This API operation returns a limited number of results.
        :returns: ListIdentityProvidersResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListResourceServers")
    def list_resource_servers(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        max_results: ListResourceServersLimitType | None = None,
        next_token: PaginationKeyType | None = None,
        **kwargs,
    ) -> ListResourceServersResponse:
        """Given a user pool ID, returns all resource servers and their details.
        For more information about resource servers, see `Access control with
        resource
        servers <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to list resource servers.
        :param max_results: The maximum number of resource servers that you want Amazon Cognito to
        return in the response.
        :param next_token: This API operation returns a limited number of results.
        :returns: ListResourceServersResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: ArnType, **kwargs
    ) -> ListTagsForResourceResponse:
        """Lists the tags that are assigned to an Amazon Cognito user pool. For
        more information, see `Tagging
        resources <https://docs.aws.amazon.com/cognito/latest/developerguide/tagging.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the user pool that the tags are
        assigned to.
        :returns: ListTagsForResourceResponse
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InvalidParameterException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListUserImportJobs")
    def list_user_import_jobs(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        max_results: PoolQueryLimitType,
        pagination_token: PaginationKeyType | None = None,
        **kwargs,
    ) -> ListUserImportJobsResponse:
        """Given a user pool ID, returns user import jobs and their details. Import
        jobs are retained in user pool configuration so that you can stage,
        stop, start, review, and delete them. For more information about user
        import, see `Importing users from a CSV
        file <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to list import jobs.
        :param max_results: The maximum number of import jobs that you want Amazon Cognito to return
        in the response.
        :param pagination_token: This API operation returns a limited number of results.
        :returns: ListUserImportJobsResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListUserPoolClients")
    def list_user_pool_clients(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        max_results: QueryLimit | None = None,
        next_token: PaginationKey | None = None,
        **kwargs,
    ) -> ListUserPoolClientsResponse:
        """Given a user pool ID, lists app clients. App clients are sets of rules
        for the access that you want a user pool to grant to one application.
        For more information, see `App
        clients <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to list user pool clients.
        :param max_results: The maximum number of app clients that you want Amazon Cognito to return
        in the response.
        :param next_token: This API operation returns a limited number of results.
        :returns: ListUserPoolClientsResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListUserPools")
    def list_user_pools(
        self,
        context: RequestContext,
        max_results: PoolQueryLimitType,
        next_token: PaginationKeyType | None = None,
        **kwargs,
    ) -> ListUserPoolsResponse:
        """Lists user pools and their details in the current Amazon Web Services
        account.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param max_results: The maximum number of user pools that you want Amazon Cognito to return
        in the response.
        :param next_token: This API operation returns a limited number of results.
        :returns: ListUserPoolsResponse
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListUsers")
    def list_users(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        attributes_to_get: SearchedAttributeNamesListType | None = None,
        limit: QueryLimitType | None = None,
        pagination_token: SearchPaginationTokenType | None = None,
        filter: UserFilterType | None = None,
        **kwargs,
    ) -> ListUsersResponse:
        """Given a user pool ID, returns a list of users and their basic details in
        a user pool.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to display or search for users.
        :param attributes_to_get: A JSON array of user attribute names, for example ``given_name``, that
        you want Amazon Cognito to include in the response for each user.
        :param limit: The maximum number of users that you want Amazon Cognito to return in
        the response.
        :param pagination_token: This API operation returns a limited number of results.
        :param filter: A filter string of the form
        ``"AttributeName Filter-Type "AttributeValue"``.
        :returns: ListUsersResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListUsersInGroup")
    def list_users_in_group(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        group_name: GroupNameType,
        limit: QueryLimitType | None = None,
        next_token: PaginationKey | None = None,
        **kwargs,
    ) -> ListUsersInGroupResponse:
        """Given a user pool ID and a group name, returns a list of users in the
        group. For more information about user pool groups, see `Adding groups
        to a user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to view the membership of the
        requested group.
        :param group_name: The name of the group that you want to query for user membership.
        :param limit: The maximum number of groups that you want Amazon Cognito to return in
        the response.
        :param next_token: This API operation returns a limited number of results.
        :returns: ListUsersInGroupResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("ListWebAuthnCredentials")
    def list_web_authn_credentials(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        next_token: PaginationKey | None = None,
        max_results: WebAuthnCredentialsQueryLimitType | None = None,
        **kwargs,
    ) -> ListWebAuthnCredentialsResponse:
        """Generates a list of the currently signed-in user's registered passkey,
        or WebAuthn, credentials.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param next_token: This API operation returns a limited number of results.
        :param max_results: The maximum number of the user's passkey credentials that you want to
        return.
        :returns: ListWebAuthnCredentialsResponse
        :raises ForbiddenException:
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises NotAuthorizedException:
        """
        raise NotImplementedError

    @handler("ResendConfirmationCode")
    def resend_confirmation_code(
        self,
        context: RequestContext,
        client_id: ClientIdType,
        username: UsernameType,
        secret_hash: SecretHashType | None = None,
        user_context_data: UserContextDataType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> ResendConfirmationCodeResponse:
        """Resends the code that confirms a new account for a user who has signed
        up in your user pool. Amazon Cognito sends confirmation codes to the
        user attribute in the ``AutoVerifiedAttributes`` property of your user
        pool. When you prompt new users for the confirmation code, include a
        "Resend code" option that generates a call to this API operation.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param client_id: The ID of the user pool app client where the user signed up.
        :param username: The name of the user that you want to query or modify.
        :param secret_hash: A keyed-hash message authentication code (HMAC) calculated using the
        secret key of a user pool client and username plus the client ID in the
        message.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: ResendConfirmationCodeResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises NotAuthorizedException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises CodeDeliveryFailureException:
        :raises UserNotFoundException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("RespondToAuthChallenge")
    def respond_to_auth_challenge(
        self,
        context: RequestContext,
        client_id: ClientIdType,
        challenge_name: ChallengeNameType,
        session: SessionType | None = None,
        challenge_responses: ChallengeResponsesType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        user_context_data: UserContextDataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> RespondToAuthChallengeResponse:
        """Some API operations in a user pool generate a challenge, like a prompt
        for an MFA code, for device authentication that bypasses MFA, or for a
        custom authentication challenge. A ``RespondToAuthChallenge`` API
        request provides the answer to that challenge, like a code or a secure
        remote password (SRP). The parameters of a response to an authentication
        challenge vary with the type of challenge.

        For more information about custom authentication challenges, see `Custom
        authentication challenge Lambda
        triggers <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html>`__.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param client_id: The ID of the app client where the user is signing in.
        :param challenge_name: The name of the challenge that you are responding to.
        :param session: The session identifier that maintains the state of authentication
        requests and challenge responses.
        :param challenge_responses: The responses to the challenge that you received in the previous
        request.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: RespondToAuthChallengeResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises CodeMismatchException:
        :raises ExpiredCodeException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidPasswordException:
        :raises PasswordHistoryPolicyViolationException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises InvalidUserPoolConfigurationException:
        :raises MFAMethodNotFoundException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises AliasExistsException:
        :raises InternalErrorException:
        :raises SoftwareTokenMFANotFoundException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("RevokeToken")
    def revoke_token(
        self,
        context: RequestContext,
        token: TokenModelType,
        client_id: ClientIdType,
        client_secret: ClientSecretType | None = None,
        **kwargs,
    ) -> RevokeTokenResponse:
        """Revokes all of the access tokens generated by, and at the same time as,
        the specified refresh token. After a token is revoked, you can't use the
        revoked token to access Amazon Cognito user APIs, or to authorize access
        to your resource server.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param token: The refresh token that you want to revoke.
        :param client_id: The ID of the app client where the token that you want to revoke was
        issued.
        :param client_secret: The client secret of the requested app client, if the client has a
        secret.
        :returns: RevokeTokenResponse
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises UnauthorizedException:
        :raises InvalidParameterException:
        :raises UnsupportedOperationException:
        :raises UnsupportedTokenTypeException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("SetLogDeliveryConfiguration")
    def set_log_delivery_configuration(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        log_configurations: LogConfigurationListType,
        **kwargs,
    ) -> SetLogDeliveryConfigurationResponse:
        """Sets up or modifies the logging configuration of a user pool. User pools
        can export user notification logs and, when threat protection is active,
        user-activity logs. For more information, see `Exporting user pool
        logs <https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html>`__.

        :param user_pool_id: The ID of the user pool where you want to configure logging.
        :param log_configurations: A collection of the logging configurations for a user pool.
        :returns: SetLogDeliveryConfigurationResponse
        :raises InvalidParameterException:
        :raises InternalErrorException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises ResourceNotFoundException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("SetRiskConfiguration")
    def set_risk_configuration(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType | None = None,
        compromised_credentials_risk_configuration: CompromisedCredentialsRiskConfigurationType
        | None = None,
        account_takeover_risk_configuration: AccountTakeoverRiskConfigurationType | None = None,
        risk_exception_configuration: RiskExceptionConfigurationType | None = None,
        **kwargs,
    ) -> SetRiskConfigurationResponse:
        """Configures threat protection for a user pool or app client. Sets
        configuration for the following.

        -  Responses to risks with adaptive authentication

        -  Responses to vulnerable passwords with compromised-credentials
           detection

        -  Notifications to users who have had risky activity detected

        -  IP-address denylist and allowlist

        To set the risk configuration for the user pool to defaults, send this
        request with only the ``UserPoolId`` parameter. To reset the threat
        protection settings of an app client to be inherited from the user pool,
        send ``UserPoolId`` and ``ClientId`` parameters only. To change threat
        protection to audit-only or off, update the value of ``UserPoolAddOns``
        in an ``UpdateUserPool`` request. To activate this setting, your user
        pool must be on the `Plus
        tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html>`__.

        :param user_pool_id: The ID of the user pool where you want to set a risk configuration.
        :param client_id: The ID of the app client where you want to set a risk configuration.
        :param compromised_credentials_risk_configuration: The configuration of automated reactions to detected compromised
        credentials.
        :param account_takeover_risk_configuration: The settings for automated responses and notification templates for
        adaptive authentication with threat protection.
        :param risk_exception_configuration: A set of IP-address overrides to threat protection.
        :returns: SetRiskConfigurationResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserPoolAddOnNotEnabledException:
        :raises CodeDeliveryFailureException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("SetUICustomization")
    def set_ui_customization(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType | None = None,
        css: CSSType | None = None,
        image_file: ImageFileType | None = None,
        **kwargs,
    ) -> SetUICustomizationResponse:
        """Configures UI branding settings for domains with the hosted UI (classic)
        branding version. Your user pool must have a domain. Configure a domain
        with .

        Set the default configuration for all clients with a ``ClientId`` of
        ``ALL``. When the ``ClientId`` value is an app client ID, the settings
        you pass in this request apply to that app client and override the
        default ``ALL`` configuration.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to apply branding to the classic
        hosted UI.
        :param client_id: The ID of the app client that you want to customize.
        :param css: A plaintext CSS file that contains the custom fields that you want to
        apply to your user pool or app client.
        :param image_file: The image that you want to set as your login in the classic hosted UI,
        as a Base64-formatted binary object.
        :returns: SetUICustomizationResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("SetUserMFAPreference")
    def set_user_mfa_preference(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        sms_mfa_settings: SMSMfaSettingsType | None = None,
        software_token_mfa_settings: SoftwareTokenMfaSettingsType | None = None,
        email_mfa_settings: EmailMfaSettingsType | None = None,
        **kwargs,
    ) -> SetUserMFAPreferenceResponse:
        """Set the user's multi-factor authentication (MFA) method preference,
        including which MFA factors are activated and if any are preferred. Only
        one factor can be set as preferred. The preferred MFA factor will be
        used to authenticate a user if multiple factors are activated. If
        multiple options are activated and no preference is set, a challenge to
        choose an MFA option will be returned during sign-in. If an MFA type is
        activated for a user, the user will be prompted for MFA during all
        sign-in attempts unless device tracking is turned on and the device has
        been trusted. If you want MFA to be applied selectively based on the
        assessed risk level of sign-in attempts, deactivate MFA for users and
        turn on Adaptive Authentication for the user pool.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param sms_mfa_settings: User preferences for SMS message MFA.
        :param software_token_mfa_settings: User preferences for time-based one-time password (TOTP) MFA.
        :param email_mfa_settings: User preferences for email message MFA.
        :returns: SetUserMFAPreferenceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("SetUserPoolMfaConfig")
    def set_user_pool_mfa_config(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        sms_mfa_configuration: SmsMfaConfigType | None = None,
        software_token_mfa_configuration: SoftwareTokenMfaConfigType | None = None,
        email_mfa_configuration: EmailMfaConfigType | None = None,
        mfa_configuration: UserPoolMfaType | None = None,
        web_authn_configuration: WebAuthnConfigurationType | None = None,
        **kwargs,
    ) -> SetUserPoolMfaConfigResponse:
        """Sets user pool multi-factor authentication (MFA) and passkey
        configuration. For more information about user pool MFA, see `Adding
        MFA <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html>`__.
        For more information about WebAuthn passkeys see `Authentication
        flows <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param user_pool_id: The user pool ID.
        :param sms_mfa_configuration: Configures user pool SMS messages for MFA.
        :param software_token_mfa_configuration: Configures a user pool for time-based one-time password (TOTP) MFA.
        :param email_mfa_configuration: Sets configuration for user pool email message MFA and sign-in with
        one-time passwords (OTPs).
        :param mfa_configuration: Sets multi-factor authentication (MFA) to be on, off, or optional.
        :param web_authn_configuration: The configuration of your user pool for passkey, or WebAuthn,
        authentication and registration.
        :returns: SetUserPoolMfaConfigResponse
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises ConcurrentModificationException:
        :raises ResourceNotFoundException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("SetUserSettings")
    def set_user_settings(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        mfa_options: MFAOptionListType,
        **kwargs,
    ) -> SetUserSettingsResponse:
        """*This action is no longer supported.* You can use it to configure only
        SMS MFA. You can't use it to configure time-based one-time password
        (TOTP) software token or email MFA.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param mfa_options: You can use this parameter only to set an SMS configuration that uses
        SMS for delivery.
        :returns: SetUserSettingsResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("SignUp")
    def sign_up(
        self,
        context: RequestContext,
        client_id: ClientIdType,
        username: UsernameType,
        secret_hash: SecretHashType | None = None,
        password: PasswordType | None = None,
        user_attributes: AttributeListType | None = None,
        validation_data: AttributeListType | None = None,
        analytics_metadata: AnalyticsMetadataType | None = None,
        user_context_data: UserContextDataType | None = None,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> SignUpResponse:
        """Registers a user with an app client and requests a user name, password,
        and user attributes in the user pool.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        You might receive a ``LimitExceeded`` exception in response to this
        request if you have exceeded a rate quota for email or SMS messages, and
        if your user pool automatically verifies email addresses or phone
        numbers. When you get this exception in the response, the user is
        successfully created and is in an ``UNCONFIRMED`` state.

        :param client_id: The ID of the app client where the user wants to sign up.
        :param username: The username of the user that you want to sign up.
        :param secret_hash: A keyed-hash message authentication code (HMAC) calculated using the
        secret key of a user pool client and username plus the client ID in the
        message.
        :param password: The user's proposed password.
        :param user_attributes: An array of name-value pairs representing user attributes.
        :param validation_data: Temporary user attributes that contribute to the outcomes of your pre
        sign-up Lambda trigger.
        :param analytics_metadata: Information that supports analytics outcomes with Amazon Pinpoint,
        including the user's endpoint ID.
        :param user_context_data: Contextual data about your user session like the device fingerprint, IP
        address, or location.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action triggers.
        :returns: SignUpResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises NotAuthorizedException:
        :raises InvalidPasswordException:
        :raises InvalidLambdaResponseException:
        :raises UsernameExistsException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises LimitExceededException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises CodeDeliveryFailureException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("StartUserImportJob")
    def start_user_import_job(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        job_id: UserImportJobIdType,
        **kwargs,
    ) -> StartUserImportJobResponse:
        """Instructs your user pool to start importing users from a CSV file that
        contains their usernames and attributes. For more information about
        importing users from a CSV file, see `Importing users from a CSV
        file <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html>`__.

        :param user_pool_id: The ID of the user pool that you want to start importing users into.
        :param job_id: The ID of a user import job that you previously created.
        :returns: StartUserImportJobResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises PreconditionNotMetException:
        :raises NotAuthorizedException:
        """
        raise NotImplementedError

    @handler("StartWebAuthnRegistration")
    def start_web_authn_registration(
        self, context: RequestContext, access_token: TokenModelType, **kwargs
    ) -> StartWebAuthnRegistrationResponse:
        """Requests credential creation options from your user pool for the
        currently signed-in user. Returns information about the user pool, the
        user profile, and authentication requirements. Users must provide this
        information in their request to enroll your application with their
        passkey provider.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :returns: StartWebAuthnRegistrationResponse
        :raises ForbiddenException:
        :raises InternalErrorException:
        :raises InvalidParameterException:
        :raises LimitExceededException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises WebAuthnNotEnabledException:
        :raises WebAuthnConfigurationMissingException:
        """
        raise NotImplementedError

    @handler("StopUserImportJob")
    def stop_user_import_job(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        job_id: UserImportJobIdType,
        **kwargs,
    ) -> StopUserImportJobResponse:
        """Instructs your user pool to stop a running job that's importing users
        from a CSV file that contains their usernames and attributes. For more
        information about importing users from a CSV file, see `Importing users
        from a CSV
        file <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html>`__.

        :param user_pool_id: The ID of the user pool that you want to stop.
        :param job_id: The ID of a running user import job.
        :returns: StopUserImportJobResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises PreconditionNotMetException:
        :raises NotAuthorizedException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ArnType, tags: UserPoolTagsType, **kwargs
    ) -> TagResourceResponse:
        """Assigns a set of tags to an Amazon Cognito user pool. A tag is a label
        that you can use to categorize and manage user pools in different ways,
        such as by purpose, owner, environment, or other criteria.

        Each tag consists of a key and value, both of which you define. A key is
        a general category for more specific values. For example, if you have
        two versions of a user pool, one for testing and another for production,
        you might assign an ``Environment`` tag key to both user pools. The
        value of this key might be ``Test`` for one user pool, and
        ``Production`` for the other.

        Tags are useful for cost tracking and access control. You can activate
        your tags so that they appear on the Billing and Cost Management
        console, where you can track the costs associated with your user pools.
        In an Identity and Access Management policy, you can constrain
        permissions for user pools based on specific tags or tag values.

        You can use this action up to 5 times per second, per account. A user
        pool can have as many as 50 tags.

        :param resource_arn: The Amazon Resource Name (ARN) of the user pool to assign the tags to.
        :param tags: An array of tag keys and values that you want to assign to the user
        pool.
        :returns: TagResourceResponse
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InvalidParameterException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: ArnType,
        tag_keys: UserPoolTagsListType,
        **kwargs,
    ) -> UntagResourceResponse:
        """Given tag IDs that you previously assigned to a user pool, removes them.

        :param resource_arn: The Amazon Resource Name (ARN) of the user pool that the tags are
        assigned to.
        :param tag_keys: An array of tag keys that you want to remove from the user pool.
        :returns: UntagResourceResponse
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InvalidParameterException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UpdateAuthEventFeedback")
    def update_auth_event_feedback(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        username: UsernameType,
        event_id: EventIdType,
        feedback_token: TokenModelType,
        feedback_value: FeedbackValueType,
        **kwargs,
    ) -> UpdateAuthEventFeedbackResponse:
        """Provides the feedback for an authentication event generated by threat
        protection features. The user's response indicates that you think that
        the event either was from a valid user or was an unwanted authentication
        attempt. This feedback improves the risk evaluation decision for the
        user pool as part of Amazon Cognito threat protection. To activate this
        setting, your user pool must be on the `Plus
        tier <https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html>`__.

        This operation requires a ``FeedbackToken`` that Amazon Cognito
        generates and adds to notification emails when users have potentially
        suspicious authentication events. Users invoke this operation when they
        select the link that corresponds to ``{one-click-link-valid}`` or
        ``{one-click-link-invalid}`` in your notification template. Because
        ``FeedbackToken`` is a required parameter, you can' make requests to
        ``UpdateAuthEventFeedback`` without the contents of the notification
        email message.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param user_pool_id: The ID of the user pool where you want to update auth event feedback.
        :param username: The name of the user that you want to query or modify.
        :param event_id: The ID of the authentication event that you want to submit feedback for.
        :param feedback_token: The feedback token, an encrypted object generated by Amazon Cognito and
        passed to your user in the notification email message from the event.
        :param feedback_value: Your feedback to the authentication event.
        :returns: UpdateAuthEventFeedbackResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserNotFoundException:
        :raises UserPoolAddOnNotEnabledException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UpdateDeviceStatus")
    def update_device_status(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        device_key: DeviceKeyType,
        device_remembered_status: DeviceRememberedStatusType | None = None,
        **kwargs,
    ) -> UpdateDeviceStatusResponse:
        """Updates the status of a the currently signed-in user's device so that it
        is marked as remembered or not remembered for the purpose of device
        authentication. Device authentication is a "remember me" mechanism that
        silently completes sign-in from trusted devices with a device key
        instead of a user-provided MFA code. This operation changes the status
        of a device without deleting it, so you can enable it again later. For
        more information about device authentication, see `Working with
        devices <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html>`__.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param device_key: The device key of the device you want to update, for example
        ``us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``.
        :param device_remembered_status: To enable device authentication with the specified device, set to
        ``remembered``.
        :returns: UpdateDeviceStatusResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises InvalidUserPoolConfigurationException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("UpdateGroup")
    def update_group(
        self,
        context: RequestContext,
        group_name: GroupNameType,
        user_pool_id: UserPoolIdType,
        description: DescriptionType | None = None,
        role_arn: ArnType | None = None,
        precedence: PrecedenceType | None = None,
        **kwargs,
    ) -> UpdateGroupResponse:
        """Given the name of a user pool group, updates any of the properties for
        precedence, IAM role, or description. For more information about user
        pool groups, see `Adding groups to a user
        pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param group_name: The name of the group that you want to update.
        :param user_pool_id: The ID of the user pool that contains the group you want to update.
        :param description: A new description of the existing group.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that you want to associate
        with the group.
        :param precedence: A non-negative integer value that specifies the precedence of this group
        relative to the other groups that a user can belong to in the user pool.
        :returns: UpdateGroupResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UpdateIdentityProvider")
    def update_identity_provider(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        provider_name: ProviderNameType,
        provider_details: ProviderDetailsType | None = None,
        attribute_mapping: AttributeMappingType | None = None,
        idp_identifiers: IdpIdentifiersListType | None = None,
        **kwargs,
    ) -> UpdateIdentityProviderResponse:
        """Modifies the configuration and trust relationship between a third-party
        identity provider (IdP) and a user pool. Amazon Cognito accepts sign-in
        with third-party identity providers through managed login and OIDC
        relying-party libraries. For more information, see `Third-party IdP
        sign-in <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The Id of the user pool where you want to update your IdP.
        :param provider_name: The name of the IdP that you want to update.
        :param provider_details: The scopes, URLs, and identifiers for your external identity provider.
        :param attribute_mapping: A mapping of IdP attributes to standard and custom user pool attributes.
        :param idp_identifiers: An array of IdP identifiers, for example
        ``"IdPIdentifiers": [ "MyIdP", "MyIdP2" ]``.
        :returns: UpdateIdentityProviderResponse
        :raises InvalidParameterException:
        :raises UnsupportedIdentityProviderException:
        :raises ResourceNotFoundException:
        :raises ConcurrentModificationException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UpdateManagedLoginBranding")
    def update_managed_login_branding(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType | None = None,
        managed_login_branding_id: ManagedLoginBrandingIdType | None = None,
        use_cognito_provided_values: BooleanType | None = None,
        settings: Document | None = None,
        assets: AssetListType | None = None,
        **kwargs,
    ) -> UpdateManagedLoginBrandingResponse:
        """Configures the branding settings for a user pool style. This operation
        is the programmatic option for the configuration of a style in the
        branding designer.

        Provides values for UI customization in a ``Settings`` JSON object and
        image files in an ``Assets`` array.

        This operation has a 2-megabyte request-size limit and include the CSS
        settings and image assets for your app client. Your branding settings
        might exceed 2MB in size. Amazon Cognito doesn't require that you pass
        all parameters in one request and preserves existing style settings that
        you don't specify. If your request is larger than 2MB, separate it into
        multiple requests, each with a size smaller than the limit.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that contains the managed login branding style
        that you want to update.
        :param managed_login_branding_id: The ID of the managed login branding style that you want to update.
        :param use_cognito_provided_values: When ``true``, applies the default branding style options.
        :param settings: A JSON file, encoded as a ``Document`` type, with the the settings that
        you want to apply to your style.
        :param assets: An array of image files that you want to apply to roles like
        backgrounds, logos, and icons.
        :returns: UpdateManagedLoginBrandingResponse
        :raises ResourceNotFoundException:
        :raises ConcurrentModificationException:
        :raises InvalidParameterException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UpdateResourceServer")
    def update_resource_server(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        identifier: ResourceServerIdentifierType,
        name: ResourceServerNameType,
        scopes: ResourceServerScopeListType | None = None,
        **kwargs,
    ) -> UpdateResourceServerResponse:
        """Updates the name and scopes of a resource server. All other fields are
        read-only. For more information about resource servers, see `Access
        control with resource
        servers <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html>`__.

        If you don't provide a value for an attribute, it is set to the default
        value.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool that contains the resource server that you want
        to update.
        :param identifier: A unique resource server identifier for the resource server.
        :param name: The updated name of the resource server.
        :param scopes: An array of updated custom scope names and descriptions that you want to
        associate with your resource server.
        :returns: UpdateResourceServerResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        """
        raise NotImplementedError

    @handler("UpdateUserAttributes")
    def update_user_attributes(
        self,
        context: RequestContext,
        user_attributes: AttributeListType,
        access_token: TokenModelType,
        client_metadata: ClientMetadataType | None = None,
        **kwargs,
    ) -> UpdateUserAttributesResponse:
        """Updates the currently signed-in user's attributes. To delete an
        attribute from the user, submit the attribute in your API request with a
        blank value.

        For custom attributes, you must add a ``custom:`` prefix to the
        attribute name, for example ``custom:department``.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        :param user_attributes: An array of name-value pairs representing user attributes.
        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param client_metadata: A map of custom key-value pairs that you can provide as input for any
        custom workflows that this action initiates.
        :returns: UpdateUserAttributesResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises CodeMismatchException:
        :raises ExpiredCodeException:
        :raises NotAuthorizedException:
        :raises UnexpectedLambdaException:
        :raises UserLambdaValidationException:
        :raises InvalidLambdaResponseException:
        :raises TooManyRequestsException:
        :raises AliasExistsException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises CodeDeliveryFailureException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("UpdateUserPool")
    def update_user_pool(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        policies: UserPoolPolicyType | None = None,
        deletion_protection: DeletionProtectionType | None = None,
        lambda_config: LambdaConfigType | None = None,
        auto_verified_attributes: VerifiedAttributesListType | None = None,
        sms_verification_message: SmsVerificationMessageType | None = None,
        email_verification_message: EmailVerificationMessageType | None = None,
        email_verification_subject: EmailVerificationSubjectType | None = None,
        verification_message_template: VerificationMessageTemplateType | None = None,
        sms_authentication_message: SmsVerificationMessageType | None = None,
        user_attribute_update_settings: UserAttributeUpdateSettingsType | None = None,
        mfa_configuration: UserPoolMfaType | None = None,
        device_configuration: DeviceConfigurationType | None = None,
        email_configuration: EmailConfigurationType | None = None,
        sms_configuration: SmsConfigurationType | None = None,
        user_pool_tags: UserPoolTagsType | None = None,
        admin_create_user_config: AdminCreateUserConfigType | None = None,
        user_pool_add_ons: UserPoolAddOnsType | None = None,
        account_recovery_setting: AccountRecoverySettingType | None = None,
        pool_name: UserPoolNameType | None = None,
        user_pool_tier: UserPoolTierType | None = None,
        **kwargs,
    ) -> UpdateUserPoolResponse:
        """Updates the configuration of a user pool. To avoid setting parameters to
        Amazon Cognito defaults, construct this API request to pass the existing
        configuration of your user pool, modified to include the changes that
        you want to make.

        If you don't provide a value for an attribute, Amazon Cognito sets it to
        its default value.

        This action might generate an SMS text message. Starting June 1, 2021,
        US telecom carriers require you to register an origination phone number
        before you can send SMS messages to US phone numbers. If you use SMS
        text messages in Amazon Cognito, you must register a phone number with
        `Amazon Pinpoint <https://console.aws.amazon.com/pinpoint/home/>`__.
        Amazon Cognito uses the registered number automatically. Otherwise,
        Amazon Cognito users who must receive SMS messages might not be able to
        sign up, activate their accounts, or sign in.

        If you have never used SMS text messages with Amazon Cognito or any
        other Amazon Web Services service, Amazon Simple Notification Service
        might place your account in the SMS sandbox. In `sandbox
        mode <https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html>`__
        , you can send messages only to verified phone numbers. After you test
        your app while in the sandbox environment, you can move out of the
        sandbox and into production. For more information, see `SMS message
        settings for Amazon Cognito user
        pools <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html>`__
        in the *Amazon Cognito Developer Guide*.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool you want to update.
        :param policies: The password policy and sign-in policy in the user pool.
        :param deletion_protection: When active, ``DeletionProtection`` prevents accidental deletion of your
        user pool.
        :param lambda_config: A collection of user pool Lambda triggers.
        :param auto_verified_attributes: The attributes that you want your user pool to automatically verify.
        :param sms_verification_message: This parameter is no longer used.
        :param email_verification_message: This parameter is no longer used.
        :param email_verification_subject: This parameter is no longer used.
        :param verification_message_template: The template for the verification message that your user pool delivers
        to users who set an email address or phone number attribute.
        :param sms_authentication_message: The contents of the SMS message that your user pool sends to users in
        SMS authentication.
        :param user_attribute_update_settings: The settings for updates to user attributes.
        :param mfa_configuration: Sets multi-factor authentication (MFA) to be on, off, or optional.
        :param device_configuration: The device-remembering configuration for a user pool.
        :param email_configuration: The email configuration of your user pool.
        :param sms_configuration: The SMS configuration with the settings for your Amazon Cognito user
        pool to send SMS message with Amazon Simple Notification Service.
        :param user_pool_tags: The tag keys and values to assign to the user pool.
        :param admin_create_user_config: The configuration for administrative creation of users.
        :param user_pool_add_ons: Contains settings for activation of threat protection, including the
        operating mode and additional authentication types.
        :param account_recovery_setting: The available verified method a user can use to recover their password
        when they call ``ForgotPassword``.
        :param pool_name: The updated name of your user pool.
        :param user_pool_tier: The user pool `feature
        plan <https://docs.
        :returns: UpdateUserPoolResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises ConcurrentModificationException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises UserImportInProgressException:
        :raises InternalErrorException:
        :raises InvalidSmsRoleAccessPolicyException:
        :raises InvalidSmsRoleTrustRelationshipException:
        :raises UserPoolTaggingException:
        :raises InvalidEmailRoleAccessPolicyException:
        :raises TierChangeNotAllowedException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("UpdateUserPoolClient")
    def update_user_pool_client(
        self,
        context: RequestContext,
        user_pool_id: UserPoolIdType,
        client_id: ClientIdType,
        client_name: ClientNameType | None = None,
        refresh_token_validity: RefreshTokenValidityType | None = None,
        access_token_validity: AccessTokenValidityType | None = None,
        id_token_validity: IdTokenValidityType | None = None,
        token_validity_units: TokenValidityUnitsType | None = None,
        read_attributes: ClientPermissionListType | None = None,
        write_attributes: ClientPermissionListType | None = None,
        explicit_auth_flows: ExplicitAuthFlowsListType | None = None,
        supported_identity_providers: SupportedIdentityProvidersListType | None = None,
        callback_urls: CallbackURLsListType | None = None,
        logout_urls: LogoutURLsListType | None = None,
        default_redirect_uri: RedirectUrlType | None = None,
        allowed_o_auth_flows: OAuthFlowsType | None = None,
        allowed_o_auth_scopes: ScopeListType | None = None,
        allowed_o_auth_flows_user_pool_client: BooleanType | None = None,
        analytics_configuration: AnalyticsConfigurationType | None = None,
        prevent_user_existence_errors: PreventUserExistenceErrorTypes | None = None,
        enable_token_revocation: WrappedBooleanType | None = None,
        enable_propagate_additional_user_context_data: WrappedBooleanType | None = None,
        auth_session_validity: AuthSessionValidityType | None = None,
        refresh_token_rotation: RefreshTokenRotationType | None = None,
        **kwargs,
    ) -> UpdateUserPoolClientResponse:
        """Given a user pool app client ID, updates the configuration. To avoid
        setting parameters to Amazon Cognito defaults, construct this API
        request to pass the existing configuration of your app client, modified
        to include the changes that you want to make.

        If you don't provide a value for an attribute, Amazon Cognito sets it to
        its default value.

        Unlike app clients created in the console, Amazon Cognito doesn't
        automatically assign a branding style to app clients that you configure
        with this API operation. Managed login and classic hosted UI pages
        aren't available for your client until after you apply a branding style.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param user_pool_id: The ID of the user pool where you want to update the app client.
        :param client_id: The ID of the app client that you want to update.
        :param client_name: A friendly name for the app client.
        :param refresh_token_validity: The refresh token time limit.
        :param access_token_validity: The access token time limit.
        :param id_token_validity: The ID token time limit.
        :param token_validity_units: The units that validity times are represented in.
        :param read_attributes: The list of user attributes that you want your app client to have read
        access to.
        :param write_attributes: The list of user attributes that you want your app client to have write
        access to.
        :param explicit_auth_flows: The `authentication
        flows <https://docs.
        :param supported_identity_providers: A list of provider names for the identity providers (IdPs) that are
        supported on this client.
        :param callback_urls: A list of allowed redirect, or callback, URLs for managed login
        authentication.
        :param logout_urls: A list of allowed logout URLs for managed login authentication.
        :param default_redirect_uri: The default redirect URI.
        :param allowed_o_auth_flows: The OAuth grant types that you want your app client to generate.
        :param allowed_o_auth_scopes: The OAuth, OpenID Connect (OIDC), and custom scopes that you want to
        permit your app client to authorize access with.
        :param allowed_o_auth_flows_user_pool_client: Set to ``true`` to use OAuth 2.
        :param analytics_configuration: The user pool analytics configuration for collecting metrics and sending
        them to your Amazon Pinpoint campaign.
        :param prevent_user_existence_errors: When ``ENABLED``, suppresses messages that might indicate a valid user
        exists when someone attempts sign-in.
        :param enable_token_revocation: Activates or deactivates `token
        revocation <https://docs.
        :param enable_propagate_additional_user_context_data: When ``true``, your application can include additional
        ``UserContextData`` in authentication requests.
        :param auth_session_validity: Amazon Cognito creates a session token for each API request in an
        authentication flow.
        :param refresh_token_rotation: The configuration of your app client for refresh token rotation.
        :returns: UpdateUserPoolClientResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises ConcurrentModificationException:
        :raises TooManyRequestsException:
        :raises NotAuthorizedException:
        :raises ScopeDoesNotExistException:
        :raises InvalidOAuthFlowException:
        :raises InternalErrorException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("UpdateUserPoolDomain")
    def update_user_pool_domain(
        self,
        context: RequestContext,
        domain: DomainType,
        user_pool_id: UserPoolIdType,
        managed_login_version: WrappedIntegerType | None = None,
        custom_domain_config: CustomDomainConfigType | None = None,
        **kwargs,
    ) -> UpdateUserPoolDomainResponse:
        """A user pool domain hosts managed login, an authorization server and web
        server for authentication in your application. This operation updates
        the branding version for user pool domains between ``1`` for hosted UI
        (classic) and ``2`` for managed login. It also updates the SSL
        certificate for user pool custom domains.

        Changes to the domain branding version take up to one minute to take
        effect for a prefix domain and up to five minutes for a custom domain.

        This operation doesn't change the name of your user pool domain. To
        change your domain, delete it with ``DeleteUserPoolDomain`` and create a
        new domain with ``CreateUserPoolDomain``.

        You can pass the ARN of a new Certificate Manager certificate in this
        request. Typically, ACM certificates automatically renew and you user
        pool can continue to use the same ARN. But if you generate a new
        certificate for your custom domain name, replace the original
        configuration with the new ARN in this request.

        ACM certificates for custom domains must be in the US East (N. Virginia)
        Amazon Web Services Region. After you submit your request, Amazon
        Cognito requires up to 1 hour to distribute your new certificate to your
        custom domain.

        For more information about adding a custom domain to your user pool, see
        `Configuring a user pool
        domain <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html>`__.

        Amazon Cognito evaluates Identity and Access Management (IAM) policies
        in requests for this API operation. For this operation, you must use IAM
        credentials to authorize requests, and you must grant yourself the
        corresponding IAM permission in a policy.

        **Learn more**

        -  `Signing Amazon Web Services API
           Requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html>`__

        -  `Using the Amazon Cognito user pools API and user pool
           endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__

        :param domain: The name of the domain that you want to update.
        :param user_pool_id: The ID of the user pool that is associated with the domain you're
        updating.
        :param managed_login_version: A version number that indicates the state of managed login for your
        domain.
        :param custom_domain_config: The configuration for a custom domain that hosts managed login for your
        application.
        :returns: UpdateUserPoolDomainResponse
        :raises InvalidParameterException:
        :raises NotAuthorizedException:
        :raises ConcurrentModificationException:
        :raises ResourceNotFoundException:
        :raises TooManyRequestsException:
        :raises InternalErrorException:
        :raises FeatureUnavailableInTierException:
        """
        raise NotImplementedError

    @handler("VerifySoftwareToken")
    def verify_software_token(
        self,
        context: RequestContext,
        user_code: SoftwareTokenMFAUserCodeType,
        access_token: TokenModelType | None = None,
        session: SessionType | None = None,
        friendly_device_name: StringType | None = None,
        **kwargs,
    ) -> VerifySoftwareTokenResponse:
        """Registers the current user's time-based one-time password (TOTP)
        authenticator with a code generated in their authenticator app from a
        private key that's supplied by your user pool. Marks the user's software
        token MFA status as "verified" if successful. The request takes an
        access token or a session string, but not both.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param user_code: A TOTP that the user generated in their configured authenticator app.
        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param session: The session ID from an ``AssociateSoftwareToken`` request.
        :param friendly_device_name: A friendly name for the device that's running the TOTP authenticator.
        :returns: VerifySoftwareTokenResponse
        :raises InvalidParameterException:
        :raises ResourceNotFoundException:
        :raises InvalidUserPoolConfigurationException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises EnableSoftwareTokenMFAException:
        :raises NotAuthorizedException:
        :raises SoftwareTokenMFANotFoundException:
        :raises CodeMismatchException:
        :raises ForbiddenException:
        """
        raise NotImplementedError

    @handler("VerifyUserAttribute")
    def verify_user_attribute(
        self,
        context: RequestContext,
        access_token: TokenModelType,
        attribute_name: AttributeNameType,
        code: ConfirmationCodeType,
        **kwargs,
    ) -> VerifyUserAttributeResponse:
        """Submits a verification code for a signed-in user who has added or
        changed a value of an auto-verified attribute. When successful, the
        user's attribute becomes verified and the attribute ``email_verified``
        or ``phone_number_verified`` becomes ``true``.

        If your user pool requires verification before Amazon Cognito updates
        the attribute value, this operation updates the affected attribute to
        its pending value.

        Authorize this action with a signed-in user's access token. It must
        include the scope ``aws.cognito.signin.user.admin``.

        Amazon Cognito doesn't evaluate Identity and Access Management (IAM)
        policies in requests for this API operation. For this operation, you
        can't use IAM credentials to authorize requests, and you can't grant IAM
        permissions in policies. For more information about authorization models
        in Amazon Cognito, see `Using the Amazon Cognito user pools API and user
        pool
        endpoints <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html>`__.

        :param access_token: A valid access token that Amazon Cognito issued to the currently
        signed-in user.
        :param attribute_name: The name of the attribute that you want to verify.
        :param code: The verification code that your user pool sent to the added or changed
        attribute, for example the user's email address.
        :returns: VerifyUserAttributeResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises CodeMismatchException:
        :raises ExpiredCodeException:
        :raises NotAuthorizedException:
        :raises TooManyRequestsException:
        :raises LimitExceededException:
        :raises PasswordResetRequiredException:
        :raises UserNotFoundException:
        :raises UserNotConfirmedException:
        :raises InternalErrorException:
        :raises AliasExistsException:
        :raises ForbiddenException:
        """
        raise NotImplementedError
