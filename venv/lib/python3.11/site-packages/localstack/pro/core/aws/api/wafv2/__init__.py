from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

APIKey = str
APIKeyVersion = int
Action = str
Boolean = bool
Country = str
CreationPathString = str
CustomHTTPHeaderName = str
CustomHTTPHeaderValue = str
DownloadUrl = str
EnableMachineLearning = bool
EntityDescription = str
EntityId = str
EntityName = str
ErrorMessage = str
ErrorReason = str
FailureCode = int
FailureValue = str
FieldIdentifier = str
FieldToMatchData = str
FieldToProtectKeyName = str
ForwardedIPHeaderName = str
HTTPMethod = str
HTTPVersion = str
HeaderName = str
HeaderValue = str
IPAddress = str
IPString = str
JsonPointerPath = str
LabelMatchKey = str
LabelName = str
LabelNamespace = str
LockToken = str
LoginPathString = str
MetricName = str
NextMarker = str
OutputUrl = str
PaginationLimit = int
ParameterExceptionParameter = str
PolicyString = str
ProductDescription = str
ProductId = str
ProductLink = str
ProductTitle = str
RegexPatternString = str
RegistrationPagePathString = str
ReleaseNotes = str
ResourceArn = str
ResponseCode = int
ResponseContent = str
ResponseInspectionHeaderName = str
ResponseStatusCode = int
RulePriority = int
SingleCookieName = str
SourceType = str
String = str
SuccessCode = int
SuccessValue = str
TagKey = str
TagValue = str
TextTransformationPriority = int
TimeWindowDay = int
TokenDomain = str
URIString = str
VendorName = str
VersionKeyString = str


class ActionValue(StrEnum):
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    COUNT = "COUNT"
    CAPTCHA = "CAPTCHA"
    CHALLENGE = "CHALLENGE"
    EXCLUDED_AS_COUNT = "EXCLUDED_AS_COUNT"


class AssociatedResourceType(StrEnum):
    CLOUDFRONT = "CLOUDFRONT"
    API_GATEWAY = "API_GATEWAY"
    COGNITO_USER_POOL = "COGNITO_USER_POOL"
    APP_RUNNER_SERVICE = "APP_RUNNER_SERVICE"
    VERIFIED_ACCESS_INSTANCE = "VERIFIED_ACCESS_INSTANCE"


class BodyParsingFallbackBehavior(StrEnum):
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"
    EVALUATE_AS_STRING = "EVALUATE_AS_STRING"


class ComparisonOperator(StrEnum):
    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"


class CountryCode(StrEnum):
    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    VA = "VA"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    GS = "GS"
    SS = "SS"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TL = "TL"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UM = "UM"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"
    XK = "XK"


class DataProtectionAction(StrEnum):
    SUBSTITUTION = "SUBSTITUTION"
    HASH = "HASH"


class FailureReason(StrEnum):
    TOKEN_MISSING = "TOKEN_MISSING"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    TOKEN_INVALID = "TOKEN_INVALID"
    TOKEN_DOMAIN_MISMATCH = "TOKEN_DOMAIN_MISMATCH"


class FallbackBehavior(StrEnum):
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class FieldToProtectType(StrEnum):
    SINGLE_HEADER = "SINGLE_HEADER"
    SINGLE_COOKIE = "SINGLE_COOKIE"
    SINGLE_QUERY_ARGUMENT = "SINGLE_QUERY_ARGUMENT"
    QUERY_STRING = "QUERY_STRING"
    BODY = "BODY"


class FilterBehavior(StrEnum):
    KEEP = "KEEP"
    DROP = "DROP"


class FilterRequirement(StrEnum):
    MEETS_ALL = "MEETS_ALL"
    MEETS_ANY = "MEETS_ANY"


class ForwardedIPPosition(StrEnum):
    FIRST = "FIRST"
    LAST = "LAST"
    ANY = "ANY"


class IPAddressVersion(StrEnum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"


class InspectionLevel(StrEnum):
    COMMON = "COMMON"
    TARGETED = "TARGETED"


class JsonMatchScope(StrEnum):
    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class LabelMatchScope(StrEnum):
    LABEL = "LABEL"
    NAMESPACE = "NAMESPACE"


class LogScope(StrEnum):
    CUSTOMER = "CUSTOMER"
    SECURITY_LAKE = "SECURITY_LAKE"


class LogType(StrEnum):
    WAF_LOGS = "WAF_LOGS"


class MapMatchScope(StrEnum):
    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class OversizeHandling(StrEnum):
    CONTINUE = "CONTINUE"
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class ParameterExceptionField(StrEnum):
    WEB_ACL = "WEB_ACL"
    RULE_GROUP = "RULE_GROUP"
    REGEX_PATTERN_SET = "REGEX_PATTERN_SET"
    IP_SET = "IP_SET"
    MANAGED_RULE_SET = "MANAGED_RULE_SET"
    RULE = "RULE"
    EXCLUDED_RULE = "EXCLUDED_RULE"
    STATEMENT = "STATEMENT"
    BYTE_MATCH_STATEMENT = "BYTE_MATCH_STATEMENT"
    SQLI_MATCH_STATEMENT = "SQLI_MATCH_STATEMENT"
    XSS_MATCH_STATEMENT = "XSS_MATCH_STATEMENT"
    SIZE_CONSTRAINT_STATEMENT = "SIZE_CONSTRAINT_STATEMENT"
    GEO_MATCH_STATEMENT = "GEO_MATCH_STATEMENT"
    RATE_BASED_STATEMENT = "RATE_BASED_STATEMENT"
    RULE_GROUP_REFERENCE_STATEMENT = "RULE_GROUP_REFERENCE_STATEMENT"
    REGEX_PATTERN_REFERENCE_STATEMENT = "REGEX_PATTERN_REFERENCE_STATEMENT"
    IP_SET_REFERENCE_STATEMENT = "IP_SET_REFERENCE_STATEMENT"
    MANAGED_RULE_SET_STATEMENT = "MANAGED_RULE_SET_STATEMENT"
    LABEL_MATCH_STATEMENT = "LABEL_MATCH_STATEMENT"
    AND_STATEMENT = "AND_STATEMENT"
    OR_STATEMENT = "OR_STATEMENT"
    NOT_STATEMENT = "NOT_STATEMENT"
    IP_ADDRESS = "IP_ADDRESS"
    IP_ADDRESS_VERSION = "IP_ADDRESS_VERSION"
    FIELD_TO_MATCH = "FIELD_TO_MATCH"
    TEXT_TRANSFORMATION = "TEXT_TRANSFORMATION"
    SINGLE_QUERY_ARGUMENT = "SINGLE_QUERY_ARGUMENT"
    SINGLE_HEADER = "SINGLE_HEADER"
    DEFAULT_ACTION = "DEFAULT_ACTION"
    RULE_ACTION = "RULE_ACTION"
    ENTITY_LIMIT = "ENTITY_LIMIT"
    OVERRIDE_ACTION = "OVERRIDE_ACTION"
    SCOPE_VALUE = "SCOPE_VALUE"
    RESOURCE_ARN = "RESOURCE_ARN"
    RESOURCE_TYPE = "RESOURCE_TYPE"
    TAGS = "TAGS"
    TAG_KEYS = "TAG_KEYS"
    METRIC_NAME = "METRIC_NAME"
    FIREWALL_MANAGER_STATEMENT = "FIREWALL_MANAGER_STATEMENT"
    FALLBACK_BEHAVIOR = "FALLBACK_BEHAVIOR"
    POSITION = "POSITION"
    FORWARDED_IP_CONFIG = "FORWARDED_IP_CONFIG"
    IP_SET_FORWARDED_IP_CONFIG = "IP_SET_FORWARDED_IP_CONFIG"
    HEADER_NAME = "HEADER_NAME"
    CUSTOM_REQUEST_HANDLING = "CUSTOM_REQUEST_HANDLING"
    RESPONSE_CONTENT_TYPE = "RESPONSE_CONTENT_TYPE"
    CUSTOM_RESPONSE = "CUSTOM_RESPONSE"
    CUSTOM_RESPONSE_BODY = "CUSTOM_RESPONSE_BODY"
    JSON_MATCH_PATTERN = "JSON_MATCH_PATTERN"
    JSON_MATCH_SCOPE = "JSON_MATCH_SCOPE"
    BODY_PARSING_FALLBACK_BEHAVIOR = "BODY_PARSING_FALLBACK_BEHAVIOR"
    LOGGING_FILTER = "LOGGING_FILTER"
    FILTER_CONDITION = "FILTER_CONDITION"
    EXPIRE_TIMESTAMP = "EXPIRE_TIMESTAMP"
    CHANGE_PROPAGATION_STATUS = "CHANGE_PROPAGATION_STATUS"
    ASSOCIABLE_RESOURCE = "ASSOCIABLE_RESOURCE"
    LOG_DESTINATION = "LOG_DESTINATION"
    MANAGED_RULE_GROUP_CONFIG = "MANAGED_RULE_GROUP_CONFIG"
    PAYLOAD_TYPE = "PAYLOAD_TYPE"
    HEADER_MATCH_PATTERN = "HEADER_MATCH_PATTERN"
    COOKIE_MATCH_PATTERN = "COOKIE_MATCH_PATTERN"
    MAP_MATCH_SCOPE = "MAP_MATCH_SCOPE"
    OVERSIZE_HANDLING = "OVERSIZE_HANDLING"
    CHALLENGE_CONFIG = "CHALLENGE_CONFIG"
    TOKEN_DOMAIN = "TOKEN_DOMAIN"
    ATP_RULE_SET_RESPONSE_INSPECTION = "ATP_RULE_SET_RESPONSE_INSPECTION"
    ASSOCIATED_RESOURCE_TYPE = "ASSOCIATED_RESOURCE_TYPE"
    SCOPE_DOWN = "SCOPE_DOWN"
    CUSTOM_KEYS = "CUSTOM_KEYS"
    ACP_RULE_SET_RESPONSE_INSPECTION = "ACP_RULE_SET_RESPONSE_INSPECTION"
    DATA_PROTECTION_CONFIG = "DATA_PROTECTION_CONFIG"


class PayloadType(StrEnum):
    JSON = "JSON"
    FORM_ENCODED = "FORM_ENCODED"


class Platform(StrEnum):
    IOS = "IOS"
    ANDROID = "ANDROID"


class PositionalConstraint(StrEnum):
    EXACTLY = "EXACTLY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


class RateBasedStatementAggregateKeyType(StrEnum):
    IP = "IP"
    FORWARDED_IP = "FORWARDED_IP"
    CUSTOM_KEYS = "CUSTOM_KEYS"
    CONSTANT = "CONSTANT"


class ResourceType(StrEnum):
    APPLICATION_LOAD_BALANCER = "APPLICATION_LOAD_BALANCER"
    API_GATEWAY = "API_GATEWAY"
    APPSYNC = "APPSYNC"
    COGNITO_USER_POOL = "COGNITO_USER_POOL"
    APP_RUNNER_SERVICE = "APP_RUNNER_SERVICE"
    VERIFIED_ACCESS_INSTANCE = "VERIFIED_ACCESS_INSTANCE"
    AMPLIFY = "AMPLIFY"


class ResponseContentType(StrEnum):
    TEXT_PLAIN = "TEXT_PLAIN"
    TEXT_HTML = "TEXT_HTML"
    APPLICATION_JSON = "APPLICATION_JSON"


class Scope(StrEnum):
    CLOUDFRONT = "CLOUDFRONT"
    REGIONAL = "REGIONAL"


class SensitivityLevel(StrEnum):
    LOW = "LOW"
    HIGH = "HIGH"


class SizeInspectionLimit(StrEnum):
    KB_16 = "KB_16"
    KB_32 = "KB_32"
    KB_48 = "KB_48"
    KB_64 = "KB_64"


class TextTransformationType(StrEnum):
    NONE = "NONE"
    COMPRESS_WHITE_SPACE = "COMPRESS_WHITE_SPACE"
    HTML_ENTITY_DECODE = "HTML_ENTITY_DECODE"
    LOWERCASE = "LOWERCASE"
    CMD_LINE = "CMD_LINE"
    URL_DECODE = "URL_DECODE"
    BASE64_DECODE = "BASE64_DECODE"
    HEX_DECODE = "HEX_DECODE"
    MD5 = "MD5"
    REPLACE_COMMENTS = "REPLACE_COMMENTS"
    ESCAPE_SEQ_DECODE = "ESCAPE_SEQ_DECODE"
    SQL_HEX_DECODE = "SQL_HEX_DECODE"
    CSS_DECODE = "CSS_DECODE"
    JS_DECODE = "JS_DECODE"
    NORMALIZE_PATH = "NORMALIZE_PATH"
    NORMALIZE_PATH_WIN = "NORMALIZE_PATH_WIN"
    REMOVE_NULLS = "REMOVE_NULLS"
    REPLACE_NULLS = "REPLACE_NULLS"
    BASE64_DECODE_EXT = "BASE64_DECODE_EXT"
    URL_DECODE_UNI = "URL_DECODE_UNI"
    UTF8_TO_UNICODE = "UTF8_TO_UNICODE"


class WAFAssociatedItemException(ServiceException):
    """WAF couldn’t perform the operation because your resource is being used
    by another resource or it’s associated with another resource.
    """

    code: str = "WAFAssociatedItemException"
    sender_fault: bool = False
    status_code: int = 400


class WAFConfigurationWarningException(ServiceException):
    """The operation failed because you are inspecting the web request body,
    headers, or cookies without specifying how to handle oversize
    components. Rules that inspect the body must either provide an
    ``OversizeHandling`` configuration or they must be preceded by a
    ``SizeConstraintStatement`` that blocks the body content from being too
    large. Rules that inspect the headers or cookies must provide an
    ``OversizeHandling`` configuration.

    Provide the handling configuration and retry your operation.

    Alternately, you can suppress this warning by adding the following tag
    to the resource that you provide to this operation: ``Tag``
    (key:``WAF:OversizeFieldsHandlingConstraintOptOut``, value:``true``).
    """

    code: str = "WAFConfigurationWarningException"
    sender_fault: bool = False
    status_code: int = 400


class WAFDuplicateItemException(ServiceException):
    """WAF couldn’t perform the operation because the resource that you tried
    to save is a duplicate of an existing one.
    """

    code: str = "WAFDuplicateItemException"
    sender_fault: bool = False
    status_code: int = 400


class WAFExpiredManagedRuleGroupVersionException(ServiceException):
    """The operation failed because the specified version for the managed rule
    group has expired. You can retrieve the available versions for the
    managed rule group by calling ListAvailableManagedRuleGroupVersions.
    """

    code: str = "WAFExpiredManagedRuleGroupVersionException"
    sender_fault: bool = False
    status_code: int = 400


class WAFInternalErrorException(ServiceException):
    """Your request is valid, but WAF couldn’t perform the operation because of
    a system problem. Retry your request.
    """

    code: str = "WAFInternalErrorException"
    sender_fault: bool = False
    status_code: int = 400


class WAFInvalidOperationException(ServiceException):
    """The operation isn't valid."""

    code: str = "WAFInvalidOperationException"
    sender_fault: bool = False
    status_code: int = 400


class WAFInvalidParameterException(ServiceException):
    """The operation failed because WAF didn't recognize a parameter in the
    request. For example:

    -  You specified a parameter name or value that isn't valid.

    -  Your nested statement isn't valid. You might have tried to nest a
       statement that can’t be nested.

    -  You tried to update a ``WebACL`` with a ``DefaultAction`` that isn't
       among the types available at DefaultAction.

    -  Your request references an ARN that is malformed, or corresponds to a
       resource with which a web ACL can't be associated.
    """

    code: str = "WAFInvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400
    Field: Optional[ParameterExceptionField]
    Parameter: Optional[ParameterExceptionParameter]
    Reason: Optional[ErrorReason]


class WAFInvalidPermissionPolicyException(ServiceException):
    """The operation failed because the specified policy isn't in the proper
    format.

    The policy specifications must conform to the following:

    -  The policy must be composed using IAM Policy version 2012-10-17.

    -  The policy must include specifications for ``Effect``, ``Action``,
       and ``Principal``.

    -  ``Effect`` must specify ``Allow``.

    -  ``Action`` must specify ``wafv2:CreateWebACL``,
       ``wafv2:UpdateWebACL``, and ``wafv2:PutFirewallManagerRuleGroups``
       and may optionally specify ``wafv2:GetRuleGroup``. WAF rejects any
       extra actions or wildcard actions in the policy.

    -  The policy must not include a ``Resource`` parameter.

    For more information, see `IAM
    Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html>`__.
    """

    code: str = "WAFInvalidPermissionPolicyException"
    sender_fault: bool = False
    status_code: int = 400


class WAFInvalidResourceException(ServiceException):
    """WAF couldn’t perform the operation because the resource that you
    requested isn’t valid. Check the resource, and try again.
    """

    code: str = "WAFInvalidResourceException"
    sender_fault: bool = False
    status_code: int = 400


class WAFLimitsExceededException(ServiceException):
    """WAF couldn’t perform the operation because you exceeded your resource
    limit. For example, the maximum number of ``WebACL`` objects that you
    can create for an Amazon Web Services account. For more information, see
    `WAF
    quotas <https://docs.aws.amazon.com/waf/latest/developerguide/limits.html>`__
    in the *WAF Developer Guide*.
    """

    code: str = "WAFLimitsExceededException"
    sender_fault: bool = False
    status_code: int = 400
    SourceType: Optional[SourceType]


class WAFLogDestinationPermissionIssueException(ServiceException):
    """The operation failed because you don't have the permissions that your
    logging configuration requires. For information, see `Logging web ACL
    traffic
    information <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__
    in the *WAF Developer Guide*.
    """

    code: str = "WAFLogDestinationPermissionIssueException"
    sender_fault: bool = False
    status_code: int = 400


class WAFNonexistentItemException(ServiceException):
    """WAF couldn’t perform the operation because your resource doesn't exist.
    If you've just created a resource that you're using in this operation,
    you might just need to wait a few minutes. It can take from a few
    seconds to a number of minutes for changes to propagate.
    """

    code: str = "WAFNonexistentItemException"
    sender_fault: bool = False
    status_code: int = 400


class WAFOptimisticLockException(ServiceException):
    """WAF couldn’t save your changes because you tried to update or delete a
    resource that has changed since you last retrieved it. Get the resource
    again, make any changes you need to make to the new copy, and retry your
    operation.
    """

    code: str = "WAFOptimisticLockException"
    sender_fault: bool = False
    status_code: int = 400


class WAFServiceLinkedRoleErrorException(ServiceException):
    """WAF is not able to access the service linked role. This can be caused by
    a previous ``PutLoggingConfiguration`` request, which can lock the
    service linked role for about 20 seconds. Please try your request again.
    The service linked role can also be locked by a previous
    ``DeleteServiceLinkedRole`` request, which can lock the role for 15
    minutes or more. If you recently made a call to
    ``DeleteServiceLinkedRole``, wait at least 15 minutes and try the
    request again. If you receive this same exception again, you will have
    to wait additional time until the role is unlocked.
    """

    code: str = "WAFServiceLinkedRoleErrorException"
    sender_fault: bool = False
    status_code: int = 400


class WAFSubscriptionNotFoundException(ServiceException):
    """You tried to use a managed rule group that's available by subscription,
    but you aren't subscribed to it yet.
    """

    code: str = "WAFSubscriptionNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class WAFTagOperationException(ServiceException):
    """An error occurred during the tagging operation. Retry your request."""

    code: str = "WAFTagOperationException"
    sender_fault: bool = False
    status_code: int = 400


class WAFTagOperationInternalErrorException(ServiceException):
    """WAF couldn’t perform your tagging operation because of an internal
    error. Retry your request.
    """

    code: str = "WAFTagOperationInternalErrorException"
    sender_fault: bool = False
    status_code: int = 400


class WAFUnavailableEntityException(ServiceException):
    """WAF couldn’t retrieve a resource that you specified for this operation.
    If you've just created a resource that you're using in this operation,
    you might just need to wait a few minutes. It can take from a few
    seconds to a number of minutes for changes to propagate. Verify the
    resource specifications in your request parameters and then retry the
    operation.
    """

    code: str = "WAFUnavailableEntityException"
    sender_fault: bool = False
    status_code: int = 400


class WAFUnsupportedAggregateKeyTypeException(ServiceException):
    """The rule that you've named doesn't aggregate solely on the IP address or
    solely on the forwarded IP address. This call is only available for
    rate-based rules with an ``AggregateKeyType`` setting of ``IP`` or
    ``FORWARDED_IP``.
    """

    code: str = "WAFUnsupportedAggregateKeyTypeException"
    sender_fault: bool = False
    status_code: int = 400


Timestamp = datetime
TokenDomains = List[TokenDomain]


class APIKeySummary(TypedDict, total=False):
    """Information for a single API key.

    API keys are required for the integration of the CAPTCHA API in your
    JavaScript client applications. The API lets you customize the placement
    and characteristics of the CAPTCHA puzzle for your end users. For more
    information about the CAPTCHA JavaScript integration, see `WAF client
    application
    integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
    in the *WAF Developer Guide*.
    """

    TokenDomains: Optional[TokenDomains]
    APIKey: Optional[APIKey]
    CreationTimestamp: Optional[Timestamp]
    Version: Optional[APIKeyVersion]


APIKeySummaries = List[APIKeySummary]
APIKeyTokenDomains = List[TokenDomain]
ResponseInspectionJsonFailureValues = List[FailureValue]
ResponseInspectionJsonSuccessValues = List[SuccessValue]


class ResponseInspectionJson(TypedDict, total=False):
    """Configures inspection of the response JSON. WAF can inspect the first
    65,536 bytes (64 KB) of the response JSON. This is part of the
    ``ResponseInspection`` configuration for ``AWSManagedRulesATPRuleSet``
    and ``AWSManagedRulesACFPRuleSet``.

    Response inspection is available only in web ACLs that protect Amazon
    CloudFront distributions.
    """

    Identifier: FieldIdentifier
    SuccessValues: ResponseInspectionJsonSuccessValues
    FailureValues: ResponseInspectionJsonFailureValues


ResponseInspectionBodyContainsFailureStrings = List[FailureValue]
ResponseInspectionBodyContainsSuccessStrings = List[SuccessValue]


class ResponseInspectionBodyContains(TypedDict, total=False):
    """Configures inspection of the response body. WAF can inspect the first
    65,536 bytes (64 KB) of the response body. This is part of the
    ``ResponseInspection`` configuration for ``AWSManagedRulesATPRuleSet``
    and ``AWSManagedRulesACFPRuleSet``.

    Response inspection is available only in web ACLs that protect Amazon
    CloudFront distributions.
    """

    SuccessStrings: ResponseInspectionBodyContainsSuccessStrings
    FailureStrings: ResponseInspectionBodyContainsFailureStrings


ResponseInspectionHeaderFailureValues = List[FailureValue]
ResponseInspectionHeaderSuccessValues = List[SuccessValue]


class ResponseInspectionHeader(TypedDict, total=False):
    """Configures inspection of the response header. This is part of the
    ``ResponseInspection`` configuration for ``AWSManagedRulesATPRuleSet``
    and ``AWSManagedRulesACFPRuleSet``.

    Response inspection is available only in web ACLs that protect Amazon
    CloudFront distributions.
    """

    Name: ResponseInspectionHeaderName
    SuccessValues: ResponseInspectionHeaderSuccessValues
    FailureValues: ResponseInspectionHeaderFailureValues


ResponseInspectionStatusCodeFailureCodes = List[FailureCode]
ResponseInspectionStatusCodeSuccessCodes = List[SuccessCode]


class ResponseInspectionStatusCode(TypedDict, total=False):
    """Configures inspection of the response status code. This is part of the
    ``ResponseInspection`` configuration for ``AWSManagedRulesATPRuleSet``
    and ``AWSManagedRulesACFPRuleSet``.

    Response inspection is available only in web ACLs that protect Amazon
    CloudFront distributions.
    """

    SuccessCodes: ResponseInspectionStatusCodeSuccessCodes
    FailureCodes: ResponseInspectionStatusCodeFailureCodes


class ResponseInspection(TypedDict, total=False):
    """The criteria for inspecting responses to login requests and account
    creation requests, used by the ATP and ACFP rule groups to track login
    and account creation success and failure rates.

    Response inspection is available only in web ACLs that protect Amazon
    CloudFront distributions.

    The rule groups evaluates the responses that your protected resources
    send back to client login and account creation attempts, keeping count
    of successful and failed attempts from each IP address and client
    session. Using this information, the rule group labels and mitigates
    requests from client sessions and IP addresses with too much suspicious
    activity in a short amount of time.

    This is part of the ``AWSManagedRulesATPRuleSet`` and
    ``AWSManagedRulesACFPRuleSet`` configurations in
    ``ManagedRuleGroupConfig``.

    Enable response inspection by configuring exactly one component of the
    response to inspect, for example, ``Header`` or ``StatusCode``. You
    can't configure more than one component for inspection. If you don't
    configure any of the response inspection options, response inspection is
    disabled.
    """

    StatusCode: Optional[ResponseInspectionStatusCode]
    Header: Optional[ResponseInspectionHeader]
    BodyContains: Optional[ResponseInspectionBodyContains]
    Json: Optional[ResponseInspectionJson]


class AddressField(TypedDict, total=False):
    """The name of a field in the request payload that contains part or all of
    your customer's primary physical address.

    This data type is used in the ``RequestInspectionACFP`` data type.
    """

    Identifier: FieldIdentifier


AddressFields = List[AddressField]


class PhoneNumberField(TypedDict, total=False):
    """The name of a field in the request payload that contains part or all of
    your customer's primary phone number.

    This data type is used in the ``RequestInspectionACFP`` data type.
    """

    Identifier: FieldIdentifier


PhoneNumberFields = List[PhoneNumberField]


class EmailField(TypedDict, total=False):
    """The name of the field in the request payload that contains your
    customer's email.

    This data type is used in the ``RequestInspectionACFP`` data type.
    """

    Identifier: FieldIdentifier


class PasswordField(TypedDict, total=False):
    """The name of the field in the request payload that contains your
    customer's password.

    This data type is used in the ``RequestInspection`` and
    ``RequestInspectionACFP`` data types.
    """

    Identifier: FieldIdentifier


class UsernameField(TypedDict, total=False):
    """The name of the field in the request payload that contains your
    customer's username.

    This data type is used in the ``RequestInspection`` and
    ``RequestInspectionACFP`` data types.
    """

    Identifier: FieldIdentifier


class RequestInspectionACFP(TypedDict, total=False):
    """The criteria for inspecting account creation requests, used by the ACFP
    rule group to validate and track account creation attempts.

    This is part of the ``AWSManagedRulesACFPRuleSet`` configuration in
    ``ManagedRuleGroupConfig``.

    In these settings, you specify how your application accepts account
    creation attempts by providing the request payload type and the names of
    the fields within the request body where the username, password, email,
    and primary address and phone number fields are provided.
    """

    PayloadType: PayloadType
    UsernameField: Optional[UsernameField]
    PasswordField: Optional[PasswordField]
    EmailField: Optional[EmailField]
    PhoneNumberFields: Optional[PhoneNumberFields]
    AddressFields: Optional[AddressFields]


class AWSManagedRulesACFPRuleSet(TypedDict, total=False):
    """Details for your use of the account creation fraud prevention managed
    rule group, ``AWSManagedRulesACFPRuleSet``. This configuration is used
    in ``ManagedRuleGroupConfig``.
    """

    CreationPath: CreationPathString
    RegistrationPagePath: RegistrationPagePathString
    RequestInspection: RequestInspectionACFP
    ResponseInspection: Optional[ResponseInspection]
    EnableRegexInPath: Optional[Boolean]


class RequestInspection(TypedDict, total=False):
    """The criteria for inspecting login requests, used by the ATP rule group
    to validate credentials usage.

    This is part of the ``AWSManagedRulesATPRuleSet`` configuration in
    ``ManagedRuleGroupConfig``.

    In these settings, you specify how your application accepts login
    attempts by providing the request payload type and the names of the
    fields within the request body where the username and password are
    provided.
    """

    PayloadType: PayloadType
    UsernameField: UsernameField
    PasswordField: PasswordField


class AWSManagedRulesATPRuleSet(TypedDict, total=False):
    """Details for your use of the account takeover prevention managed rule
    group, ``AWSManagedRulesATPRuleSet``. This configuration is used in
    ``ManagedRuleGroupConfig``.
    """

    LoginPath: String
    RequestInspection: Optional[RequestInspection]
    ResponseInspection: Optional[ResponseInspection]
    EnableRegexInPath: Optional[Boolean]


class AWSManagedRulesBotControlRuleSet(TypedDict, total=False):
    """Details for your use of the Bot Control managed rule group,
    ``AWSManagedRulesBotControlRuleSet``. This configuration is used in
    ``ManagedRuleGroupConfig``.
    """

    InspectionLevel: InspectionLevel
    EnableMachineLearning: Optional[EnableMachineLearning]


class ActionCondition(TypedDict, total=False):
    """A single action condition for a Condition in a logging filter."""

    Action: ActionValue


class All(TypedDict, total=False):
    """Inspect all of the elements that WAF has parsed and extracted from the
    web request component that you've identified in your FieldToMatch
    specifications.

    This is used in the FieldToMatch specification for some web request
    component types.

    JSON specification: ``"All": {}``
    """

    pass


class AllQueryArguments(TypedDict, total=False):
    """Inspect all query arguments of the web request.

    This is used in the FieldToMatch specification for some web request
    component types.

    JSON specification: ``"AllQueryArguments": {}``
    """

    pass


class CustomHTTPHeader(TypedDict, total=False):
    """A custom header for custom request and response handling. This is used
    in CustomResponse and CustomRequestHandling.
    """

    Name: CustomHTTPHeaderName
    Value: CustomHTTPHeaderValue


CustomHTTPHeaders = List[CustomHTTPHeader]


class CustomRequestHandling(TypedDict, total=False):
    """Custom request handling behavior that inserts custom headers into a web
    request. You can add custom request handling for WAF to use when the
    rule action doesn't block the request. For example, ``CaptchaAction``
    for requests with valid t okens, and ``AllowAction``.

    For information about customizing web requests and responses, see
    `Customizing web requests and responses in
    WAF <https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html>`__
    in the *WAF Developer Guide*.
    """

    InsertHeaders: CustomHTTPHeaders


class AllowAction(TypedDict, total=False):
    """Specifies that WAF should allow the request and optionally defines
    additional custom handling for the request.

    This is used in the context of other settings, for example to specify
    values for RuleAction and web ACL DefaultAction.
    """

    CustomRequestHandling: Optional[CustomRequestHandling]


class TextTransformation(TypedDict, total=False):
    """Text transformations eliminate some of the unusual formatting that
    attackers use in web requests in an effort to bypass detection.
    """

    Priority: TextTransformationPriority
    Type: TextTransformationType


TextTransformations = List[TextTransformation]


class UriFragment(TypedDict, total=False):
    """Inspect fragments of the request URI. You can specify the parts of the
    URI fragment to inspect and you can narrow the set of URI fragments to
    inspect by including or excluding specific keys.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.

    Example JSON:
    ``"UriFragment": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }``
    """

    FallbackBehavior: Optional[FallbackBehavior]


class JA4Fingerprint(TypedDict, total=False):
    """Available for use with Amazon CloudFront distributions and Application
    Load Balancers. Match against the request's JA4 fingerprint. The JA4
    fingerprint is a 36-character hash derived from the TLS Client Hello of
    an incoming request. This fingerprint serves as a unique identifier for
    the client's TLS configuration. WAF calculates and logs this fingerprint
    for each request that has enough TLS Client Hello information for the
    calculation. Almost all web requests include this information.

    You can use this choice only with a string match ``ByteMatchStatement``
    with the ``PositionalConstraint`` set to ``EXACTLY``.

    You can obtain the JA4 fingerprint for client requests from the web ACL
    logs. If WAF is able to calculate the fingerprint, it includes it in the
    logs. For information about the logging fields, see `Log
    fields <https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html>`__
    in the *WAF Developer Guide*.

    Provide the JA4 fingerprint string from the logs in your string match
    statement specification, to match with any future requests that have the
    same TLS configuration.
    """

    FallbackBehavior: FallbackBehavior


class JA3Fingerprint(TypedDict, total=False):
    """Available for use with Amazon CloudFront distributions and Application
    Load Balancers. Match against the request's JA3 fingerprint. The JA3
    fingerprint is a 32-character hash derived from the TLS Client Hello of
    an incoming request. This fingerprint serves as a unique identifier for
    the client's TLS configuration. WAF calculates and logs this fingerprint
    for each request that has enough TLS Client Hello information for the
    calculation. Almost all web requests include this information.

    You can use this choice only with a string match ``ByteMatchStatement``
    with the ``PositionalConstraint`` set to ``EXACTLY``.

    You can obtain the JA3 fingerprint for client requests from the web ACL
    logs. If WAF is able to calculate the fingerprint, it includes it in the
    logs. For information about the logging fields, see `Log
    fields <https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html>`__
    in the *WAF Developer Guide*.

    Provide the JA3 fingerprint string from the logs in your string match
    statement specification, to match with any future requests that have the
    same TLS configuration.
    """

    FallbackBehavior: FallbackBehavior


class HeaderOrder(TypedDict, total=False):
    """Inspect a string containing the list of the request's header names,
    ordered as they appear in the web request that WAF receives for
    inspection. WAF generates the string and then uses that as the field to
    match component in its inspection. WAF separates the header names in the
    string using colons and no added spaces, for example
    ``host:user-agent:accept:authorization:referer``.
    """

    OversizeHandling: OversizeHandling


CookieNames = List[SingleCookieName]


class CookieMatchPattern(TypedDict, total=False):
    """The filter to use to identify the subset of cookies to inspect in a web
    request.

    You must specify exactly one setting: either ``All``,
    ``IncludedCookies``, or ``ExcludedCookies``.

    Example JSON:
    ``"MatchPattern": { "IncludedCookies": [ "session-id-time", "session-id" ] }``
    """

    All: Optional[All]
    IncludedCookies: Optional[CookieNames]
    ExcludedCookies: Optional[CookieNames]


class Cookies(TypedDict, total=False):
    """Inspect the cookies in the web request. You can specify the parts of the
    cookies to inspect and you can narrow the set of cookies to inspect by
    including or excluding specific keys.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.

    Example JSON:
    ``"Cookies": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }``
    """

    MatchPattern: CookieMatchPattern
    MatchScope: MapMatchScope
    OversizeHandling: OversizeHandling


HeaderNames = List[FieldToMatchData]


class HeaderMatchPattern(TypedDict, total=False):
    """The filter to use to identify the subset of headers to inspect in a web
    request.

    You must specify exactly one setting: either ``All``,
    ``IncludedHeaders``, or ``ExcludedHeaders``.

    Example JSON:
    ``"MatchPattern": { "ExcludedHeaders": [ "KeyToExclude1", "KeyToExclude2" ] }``
    """

    All: Optional[All]
    IncludedHeaders: Optional[HeaderNames]
    ExcludedHeaders: Optional[HeaderNames]


class Headers(TypedDict, total=False):
    """Inspect all headers in the web request. You can specify the parts of the
    headers to inspect and you can narrow the set of headers to inspect by
    including or excluding specific keys.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.

    If you want to inspect just the value of a single header, use the
    ``SingleHeader`` ``FieldToMatch`` setting instead.

    Example JSON:
    ``"Headers": { "MatchPattern": { "All": {} }, "MatchScope": "KEY", "OversizeHandling": "MATCH" }``
    """

    MatchPattern: HeaderMatchPattern
    MatchScope: MapMatchScope
    OversizeHandling: OversizeHandling


JsonPointerPaths = List[JsonPointerPath]


class JsonMatchPattern(TypedDict, total=False):
    """The patterns to look for in the JSON body. WAF inspects the results of
    these pattern matches against the rule inspection criteria. This is used
    with the FieldToMatch option ``JsonBody``.
    """

    All: Optional[All]
    IncludedPaths: Optional[JsonPointerPaths]


class JsonBody(TypedDict, total=False):
    """Inspect the body of the web request as JSON. The body immediately
    follows the request headers.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.

    Use the specifications in this object to indicate which parts of the
    JSON body to inspect using the rule's inspection criteria. WAF inspects
    only the parts of the JSON that result from the matches that you
    indicate.

    Example JSON:
    ``"JsonBody": { "MatchPattern": { "All": {} }, "MatchScope": "ALL" }``

    For additional information about this request component option, see
    `JSON
    body <https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body>`__
    in the *WAF Developer Guide*.
    """

    MatchPattern: JsonMatchPattern
    MatchScope: JsonMatchScope
    InvalidFallbackBehavior: Optional[BodyParsingFallbackBehavior]
    OversizeHandling: Optional[OversizeHandling]


class Method(TypedDict, total=False):
    """Inspect the HTTP method of the web request. The method indicates the
    type of operation that the request is asking the origin to perform.

    This is used in the FieldToMatch specification for some web request
    component types.

    JSON specification: ``"Method": {}``
    """

    pass


class Body(TypedDict, total=False):
    """Inspect the body of the web request. The body immediately follows the
    request headers.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.
    """

    OversizeHandling: Optional[OversizeHandling]


class QueryString(TypedDict, total=False):
    """Inspect the query string of the web request. This is the part of a URL
    that appears after a ``?`` character, if any.

    This is used in the FieldToMatch specification for some web request
    component types.

    JSON specification: ``"QueryString": {}``
    """

    pass


class UriPath(TypedDict, total=False):
    """Inspect the path component of the URI of the web request. This is the
    part of the web request that identifies a resource. For example,
    ``/images/daily-ad.jpg``.

    This is used in the FieldToMatch specification for some web request
    component types.

    JSON specification: ``"UriPath": {}``
    """

    pass


class SingleQueryArgument(TypedDict, total=False):
    """Inspect one query argument in the web request, identified by name, for
    example *UserName* or *SalesRegion*. The name isn't case sensitive.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.

    Example JSON: ``"SingleQueryArgument": { "Name": "myArgument" }``
    """

    Name: FieldToMatchData


class SingleHeader(TypedDict, total=False):
    """Inspect one of the headers in the web request, identified by name, for
    example, ``User-Agent`` or ``Referer``. The name isn't case sensitive.

    You can filter and inspect all headers with the ``FieldToMatch`` setting
    ``Headers``.

    This is used to indicate the web request component to inspect, in the
    FieldToMatch specification.

    Example JSON: ``"SingleHeader": { "Name": "haystack" }``
    """

    Name: FieldToMatchData


class FieldToMatch(TypedDict, total=False):
    """Specifies a web request component to be used in a rule match statement
    or in a logging configuration.

    -  In a rule statement, this is the part of the web request that you
       want WAF to inspect. Include the single ``FieldToMatch`` type that
       you want to inspect, with additional specifications as needed,
       according to the type. You specify a single request component in
       ``FieldToMatch`` for each rule statement that requires it. To inspect
       more than one component of the web request, create a separate rule
       statement for each component.

       Example JSON for a ``QueryString`` field to match:

       ``"FieldToMatch": { "QueryString": {} }``

       Example JSON for a ``Method`` field to match specification:

       ``"FieldToMatch": { "Method": { "Name": "DELETE" } }``

    -  In a logging configuration, this is used in the ``RedactedFields``
       property to specify a field to redact from the logging records. For
       this use case, note the following:

       -  Even though all ``FieldToMatch`` settings are available, the only
          valid settings for field redaction are ``UriPath``,
          ``QueryString``, ``SingleHeader``, and ``Method``.

       -  In this documentation, the descriptions of the individual fields
          talk about specifying the web request component to inspect, but
          for field redaction, you are specifying the component type to
          redact from the logs.

       -  If you have request sampling enabled, the redacted fields
          configuration for logging has no impact on sampling. You can only
          exclude fields from request sampling by disabling sampling in the
          web ACL visibility configuration or by configuring data protection
          for the web ACL.
    """

    SingleHeader: Optional[SingleHeader]
    SingleQueryArgument: Optional[SingleQueryArgument]
    AllQueryArguments: Optional[AllQueryArguments]
    UriPath: Optional[UriPath]
    QueryString: Optional[QueryString]
    Body: Optional[Body]
    Method: Optional[Method]
    JsonBody: Optional[JsonBody]
    Headers: Optional[Headers]
    Cookies: Optional[Cookies]
    HeaderOrder: Optional[HeaderOrder]
    JA3Fingerprint: Optional[JA3Fingerprint]
    JA4Fingerprint: Optional[JA4Fingerprint]
    UriFragment: Optional[UriFragment]


class RegexMatchStatement(TypedDict, total=False):
    """A rule statement used to search web request components for a match
    against a single regular expression.
    """

    RegexString: RegexPatternString
    FieldToMatch: FieldToMatch
    TextTransformations: TextTransformations


class LabelMatchStatement(TypedDict, total=False):
    """A rule statement to match against labels that have been added to the web
    request by rules that have already run in the web ACL.

    The label match statement provides the label or namespace string to
    search for. The label string can represent a part or all of the fully
    qualified label name that had been added to the web request. Fully
    qualified labels have a prefix, optional namespaces, and label name. The
    prefix identifies the rule group or web ACL context of the rule that
    added the label. If you do not provide the fully qualified name in your
    label match string, WAF performs the search for labels that were added
    in the same context as the label match statement.
    """

    Scope: LabelMatchScope
    Key: LabelMatchKey


class ChallengeAction(TypedDict, total=False):
    """Specifies that WAF should run a ``Challenge`` check against the request
    to verify that the request is coming from a legitimate client session:

    -  If the request includes a valid, unexpired challenge token, WAF
       applies any custom request handling and labels that you've configured
       and then allows the web request inspection to proceed to the next
       rule, similar to a ``CountAction``.

    -  If the request doesn't include a valid, unexpired challenge token,
       WAF discontinues the web ACL evaluation of the request and blocks it
       from going to its intended destination.

       WAF then generates a challenge response that it sends back to the
       client, which includes the following:

       -  The header ``x-amzn-waf-action`` with a value of ``challenge``.

       -  The HTTP status code ``202 Request Accepted``.

       -  If the request contains an ``Accept`` header with a value of
          ``text/html``, the response includes a JavaScript page
          interstitial with a challenge script.

       Challenges run silent browser interrogations in the background, and
       don't generally affect the end user experience.

       A challenge enforces token acquisition using an interstitial
       JavaScript challenge that inspects the client session for legitimate
       behavior. The challenge blocks bots or at least increases the cost of
       operating sophisticated bots.

       After the client session successfully responds to the challenge, it
       receives a new token from WAF, which the challenge script uses to
       resubmit the original request.

    You can configure the expiration time in the ``ChallengeConfig``
    ``ImmunityTimeProperty`` setting at the rule and web ACL level. The rule
    setting overrides the web ACL setting.

    This action option is available for rules. It isn't available for web
    ACL default actions.
    """

    CustomRequestHandling: Optional[CustomRequestHandling]


class CaptchaAction(TypedDict, total=False):
    """Specifies that WAF should run a ``CAPTCHA`` check against the request:

    -  If the request includes a valid, unexpired ``CAPTCHA`` token, WAF
       applies any custom request handling and labels that you've configured
       and then allows the web request inspection to proceed to the next
       rule, similar to a ``CountAction``.

    -  If the request doesn't include a valid, unexpired token, WAF
       discontinues the web ACL evaluation of the request and blocks it from
       going to its intended destination.

       WAF generates a response that it sends back to the client, which
       includes the following:

       -  The header ``x-amzn-waf-action`` with a value of ``captcha``.

       -  The HTTP status code ``405 Method Not Allowed``.

       -  If the request contains an ``Accept`` header with a value of
          ``text/html``, the response includes a ``CAPTCHA`` JavaScript page
          interstitial.

    You can configure the expiration time in the ``CaptchaConfig``
    ``ImmunityTimeProperty`` setting at the rule and web ACL level. The rule
    setting overrides the web ACL setting.

    This action option is available for rules. It isn't available for web
    ACL default actions.
    """

    CustomRequestHandling: Optional[CustomRequestHandling]


class CountAction(TypedDict, total=False):
    """Specifies that WAF should count the request. Optionally defines
    additional custom handling for the request.

    This is used in the context of other settings, for example to specify
    values for RuleAction and web ACL DefaultAction.
    """

    CustomRequestHandling: Optional[CustomRequestHandling]


class CustomResponse(TypedDict, total=False):
    """A custom response to send to the client. You can define a custom
    response for rule actions and default web ACL actions that are set to
    BlockAction.

    For information about customizing web requests and responses, see
    `Customizing web requests and responses in
    WAF <https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html>`__
    in the *WAF Developer Guide*.
    """

    ResponseCode: ResponseStatusCode
    CustomResponseBodyKey: Optional[EntityName]
    ResponseHeaders: Optional[CustomHTTPHeaders]


class BlockAction(TypedDict, total=False):
    """Specifies that WAF should block the request and optionally defines
    additional custom handling for the response to the web request.

    This is used in the context of other settings, for example to specify
    values for RuleAction and web ACL DefaultAction.
    """

    CustomResponse: Optional[CustomResponse]


class RuleAction(TypedDict, total=False):
    """The action that WAF should take on a web request when it matches a
    rule's statement. Settings at the web ACL level can override the rule
    action setting.
    """

    Block: Optional[BlockAction]
    Allow: Optional[AllowAction]
    Count: Optional[CountAction]
    Captcha: Optional[CaptchaAction]
    Challenge: Optional[ChallengeAction]


class RuleActionOverride(TypedDict, total=False):
    """Action setting to use in the place of a rule action that is configured
    inside the rule group. You specify one override for each rule whose
    action you want to change.

    Take care to verify the rule names in your overrides. If you provide a
    rule name that doesn't match the name of any rule in the rule group, WAF
    doesn't return an error and doesn't apply the override setting.

    You can use overrides for testing, for example you can override all of
    rule actions to ``Count`` and then monitor the resulting count metrics
    to understand how the rule group would handle your web traffic. You can
    also permanently override some or all actions, to modify how the rule
    group manages your web traffic.
    """

    Name: EntityName
    ActionToUse: RuleAction


RuleActionOverrides = List[RuleActionOverride]


class ManagedRuleGroupConfig(TypedDict, total=False):
    """Additional information that's used by a managed rule group. Many managed
    rule groups don't require this.

    The rule groups used for intelligent threat mitigation require
    additional configuration:

    -  Use the ``AWSManagedRulesACFPRuleSet`` configuration object to
       configure the account creation fraud prevention managed rule group.
       The configuration includes the registration and sign-up pages of your
       application and the locations in the account creation request payload
       of data, such as the user email and phone number fields.

    -  Use the ``AWSManagedRulesATPRuleSet`` configuration object to
       configure the account takeover prevention managed rule group. The
       configuration includes the sign-in page of your application and the
       locations in the login request payload of data such as the username
       and password.

    -  Use the ``AWSManagedRulesBotControlRuleSet`` configuration object to
       configure the protection level that you want the Bot Control rule
       group to use.

    For example specifications, see the examples section of CreateWebACL.
    """

    LoginPath: Optional[LoginPathString]
    PayloadType: Optional[PayloadType]
    UsernameField: Optional[UsernameField]
    PasswordField: Optional[PasswordField]
    AWSManagedRulesBotControlRuleSet: Optional[AWSManagedRulesBotControlRuleSet]
    AWSManagedRulesATPRuleSet: Optional[AWSManagedRulesATPRuleSet]
    AWSManagedRulesACFPRuleSet: Optional[AWSManagedRulesACFPRuleSet]


ManagedRuleGroupConfigs = List[ManagedRuleGroupConfig]


class Statement(TypedDict, total=False):
    """The processing guidance for a Rule, used by WAF to determine whether a
    web request matches the rule.

    For example specifications, see the examples section of CreateWebACL.
    """

    ByteMatchStatement: Optional["ByteMatchStatement"]
    SqliMatchStatement: Optional["SqliMatchStatement"]
    XssMatchStatement: Optional["XssMatchStatement"]
    SizeConstraintStatement: Optional["SizeConstraintStatement"]
    GeoMatchStatement: Optional["GeoMatchStatement"]
    RuleGroupReferenceStatement: Optional["RuleGroupReferenceStatement"]
    IPSetReferenceStatement: Optional["IPSetReferenceStatement"]
    RegexPatternSetReferenceStatement: Optional["RegexPatternSetReferenceStatement"]
    RateBasedStatement: Optional["RateBasedStatement"]
    AndStatement: Optional["AndStatement"]
    OrStatement: Optional["OrStatement"]
    NotStatement: Optional["NotStatement"]
    ManagedRuleGroupStatement: Optional["ManagedRuleGroupStatement"]
    LabelMatchStatement: Optional["LabelMatchStatement"]
    RegexMatchStatement: Optional["RegexMatchStatement"]


class ExcludedRule(TypedDict, total=False):
    """Specifies a single rule in a rule group whose action you want to
    override to ``Count``.

    Instead of this option, use ``RuleActionOverrides``. It accepts any
    valid action setting, including ``Count``.
    """

    Name: EntityName


ExcludedRules = List[ExcludedRule]


class ManagedRuleGroupStatement(TypedDict, total=False):
    """A rule statement used to run the rules that are defined in a managed
    rule group. To use this, provide the vendor name and the name of the
    rule group in this statement. You can retrieve the required names by
    calling ListAvailableManagedRuleGroups.

    You cannot nest a ``ManagedRuleGroupStatement``, for example for use
    inside a ``NotStatement`` or ``OrStatement``. You cannot use a managed
    rule group inside another rule group. You can only reference a managed
    rule group as a top-level statement within a rule that you define in a
    web ACL.

    You are charged additional fees when you use the WAF Bot Control managed
    rule group ``AWSManagedRulesBotControlRuleSet``, the WAF Fraud Control
    account takeover prevention (ATP) managed rule group
    ``AWSManagedRulesATPRuleSet``, or the WAF Fraud Control account creation
    fraud prevention (ACFP) managed rule group
    ``AWSManagedRulesACFPRuleSet``. For more information, see `WAF
    Pricing <http://aws.amazon.com/waf/pricing/>`__.
    """

    VendorName: VendorName
    Name: EntityName
    Version: Optional[VersionKeyString]
    ExcludedRules: Optional[ExcludedRules]
    ScopeDownStatement: Optional[Statement]
    ManagedRuleGroupConfigs: Optional[ManagedRuleGroupConfigs]
    RuleActionOverrides: Optional[RuleActionOverrides]


class NotStatement(TypedDict, total=False):
    """A logical rule statement used to negate the results of another rule
    statement. You provide one Statement within the ``NotStatement``.
    """

    Statement: Statement


Statements = List[Statement]


class OrStatement(TypedDict, total=False):
    """A logical rule statement used to combine other rule statements with OR
    logic. You provide more than one Statement within the ``OrStatement``.
    """

    Statements: Statements


class AndStatement(TypedDict, total=False):
    """A logical rule statement used to combine other rule statements with AND
    logic. You provide more than one Statement within the ``AndStatement``.
    """

    Statements: Statements


class RateLimitJA4Fingerprint(TypedDict, total=False):
    """Use the request's JA4 fingerprint derived from the TLS Client Hello of
    an incoming request as an aggregate key. If you use a single JA4
    fingerprint as your custom key, then each value fully defines an
    aggregation instance.
    """

    FallbackBehavior: FallbackBehavior


class RateLimitJA3Fingerprint(TypedDict, total=False):
    """Use the request's JA3 fingerprint derived from the TLS Client Hello of
    an incoming request as an aggregate key. If you use a single JA3
    fingerprint as your custom key, then each value fully defines an
    aggregation instance.
    """

    FallbackBehavior: FallbackBehavior


class RateLimitUriPath(TypedDict, total=False):
    """Specifies the request's URI path as an aggregate key for a rate-based
    rule. Each distinct URI path contributes to the aggregation instance. If
    you use just the URI path as your custom key, then each URI path fully
    defines an aggregation instance.
    """

    TextTransformations: TextTransformations


class RateLimitLabelNamespace(TypedDict, total=False):
    """Specifies a label namespace to use as an aggregate key for a rate-based
    rule. Each distinct fully qualified label name that has the specified
    label namespace contributes to the aggregation instance. If you use just
    one label namespace as your custom key, then each label name fully
    defines an aggregation instance.

    This uses only labels that have been added to the request by rules that
    are evaluated before this rate-based rule in the web ACL.

    For information about label namespaces and names, see `Label syntax and
    naming
    requirements <https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-requirements.html>`__
    in the *WAF Developer Guide*.
    """

    Namespace: LabelNamespace


class RateLimitIP(TypedDict, total=False):
    """Specifies the IP address in the web request as an aggregate key for a
    rate-based rule. Each distinct IP address contributes to the aggregation
    instance.

    This setting is used only in the ``RateBasedStatementCustomKey``
    specification of a rate-based rule statement. To use this in the custom
    key settings, you must specify at least one other key to use, along with
    the IP address. To aggregate on only the IP address, in your rate-based
    statement's ``AggregateKeyType``, specify ``IP``.

    JSON specification: ``"RateLimitIP": {}``
    """

    pass


class RateLimitForwardedIP(TypedDict, total=False):
    """Specifies the first IP address in an HTTP header as an aggregate key for
    a rate-based rule. Each distinct forwarded IP address contributes to the
    aggregation instance.

    This setting is used only in the ``RateBasedStatementCustomKey``
    specification of a rate-based rule statement. When you specify an IP or
    forwarded IP in the custom key settings, you must also specify at least
    one other key to use. You can aggregate on only the forwarded IP address
    by specifying ``FORWARDED_IP`` in your rate-based statement's
    ``AggregateKeyType``.

    This data type supports using the forwarded IP address in the web
    request aggregation for a rate-based rule, in
    ``RateBasedStatementCustomKey``. The JSON specification for using the
    forwarded IP address doesn't explicitly use this data type.

    JSON specification: ``"ForwardedIP": {}``

    When you use this specification, you must also configure the forwarded
    IP address in the rate-based statement's ``ForwardedIPConfig``.
    """

    pass


class RateLimitHTTPMethod(TypedDict, total=False):
    """Specifies the request's HTTP method as an aggregate key for a rate-based
    rule. Each distinct HTTP method contributes to the aggregation instance.
    If you use just the HTTP method as your custom key, then each method
    fully defines an aggregation instance.

    JSON specification: ``"RateLimitHTTPMethod": {}``
    """

    pass


class RateLimitQueryString(TypedDict, total=False):
    """Specifies the request's query string as an aggregate key for a
    rate-based rule. Each distinct string contributes to the aggregation
    instance. If you use just the query string as your custom key, then each
    string fully defines an aggregation instance.
    """

    TextTransformations: TextTransformations


class RateLimitQueryArgument(TypedDict, total=False):
    """Specifies a query argument in the request as an aggregate key for a
    rate-based rule. Each distinct value for the named query argument
    contributes to the aggregation instance. If you use a single query
    argument as your custom key, then each value fully defines an
    aggregation instance.
    """

    Name: FieldToMatchData
    TextTransformations: TextTransformations


class RateLimitCookie(TypedDict, total=False):
    """Specifies a cookie as an aggregate key for a rate-based rule. Each
    distinct value in the cookie contributes to the aggregation instance. If
    you use a single cookie as your custom key, then each value fully
    defines an aggregation instance.
    """

    Name: FieldToMatchData
    TextTransformations: TextTransformations


class RateLimitHeader(TypedDict, total=False):
    """Specifies a header as an aggregate key for a rate-based rule. Each
    distinct value in the header contributes to the aggregation instance. If
    you use a single header as your custom key, then each value fully
    defines an aggregation instance.
    """

    Name: FieldToMatchData
    TextTransformations: TextTransformations


class RateBasedStatementCustomKey(TypedDict, total=False):
    """Specifies a single custom aggregate key for a rate-base rule.

    Web requests that are missing any of the components specified in the
    aggregation keys are omitted from the rate-based rule evaluation and
    handling.
    """

    Header: Optional[RateLimitHeader]
    Cookie: Optional[RateLimitCookie]
    QueryArgument: Optional[RateLimitQueryArgument]
    QueryString: Optional[RateLimitQueryString]
    HTTPMethod: Optional[RateLimitHTTPMethod]
    ForwardedIP: Optional[RateLimitForwardedIP]
    IP: Optional[RateLimitIP]
    LabelNamespace: Optional[RateLimitLabelNamespace]
    UriPath: Optional[RateLimitUriPath]
    JA3Fingerprint: Optional[RateLimitJA3Fingerprint]
    JA4Fingerprint: Optional[RateLimitJA4Fingerprint]


RateBasedStatementCustomKeys = List[RateBasedStatementCustomKey]


class ForwardedIPConfig(TypedDict, total=False):
    """The configuration for inspecting IP addresses in an HTTP header that you
    specify, instead of using the IP address that's reported by the web
    request origin. Commonly, this is the X-Forwarded-For (XFF) header, but
    you can specify any header name.

    If the specified header isn't present in the request, WAF doesn't apply
    the rule to the web request at all.

    This configuration is used for GeoMatchStatement and RateBasedStatement.
    For IPSetReferenceStatement, use IPSetForwardedIPConfig instead.

    WAF only evaluates the first IP address found in the specified HTTP
    header.
    """

    HeaderName: ForwardedIPHeaderName
    FallbackBehavior: FallbackBehavior


EvaluationWindowSec = int
RateLimit = int


class RateBasedStatement(TypedDict, total=False):
    """A rate-based rule counts incoming requests and rate limits requests when
    they are coming at too fast a rate. The rule categorizes requests
    according to your aggregation criteria, collects them into aggregation
    instances, and counts and rate limits the requests for each instance.

    If you change any of these settings in a rule that's currently in use,
    the change resets the rule's rate limiting counts. This can pause the
    rule's rate limiting activities for up to a minute.

    You can specify individual aggregation keys, like IP address or HTTP
    method. You can also specify aggregation key combinations, like IP
    address and HTTP method, or HTTP method, query argument, and cookie.

    Each unique set of values for the aggregation keys that you specify is a
    separate aggregation instance, with the value from each key contributing
    to the aggregation instance definition.

    For example, assume the rule evaluates web requests with the following
    IP address and HTTP method values:

    -  IP address 10.1.1.1, HTTP method POST

    -  IP address 10.1.1.1, HTTP method GET

    -  IP address 127.0.0.0, HTTP method POST

    -  IP address 10.1.1.1, HTTP method GET

    The rule would create different aggregation instances according to your
    aggregation criteria, for example:

    -  If the aggregation criteria is just the IP address, then each
       individual address is an aggregation instance, and WAF counts
       requests separately for each. The aggregation instances and request
       counts for our example would be the following:

       -  IP address 10.1.1.1: count 3

       -  IP address 127.0.0.0: count 1

    -  If the aggregation criteria is HTTP method, then each individual HTTP
       method is an aggregation instance. The aggregation instances and
       request counts for our example would be the following:

       -  HTTP method POST: count 2

       -  HTTP method GET: count 2

    -  If the aggregation criteria is IP address and HTTP method, then each
       IP address and each HTTP method would contribute to the combined
       aggregation instance. The aggregation instances and request counts
       for our example would be the following:

       -  IP address 10.1.1.1, HTTP method POST: count 1

       -  IP address 10.1.1.1, HTTP method GET: count 2

       -  IP address 127.0.0.0, HTTP method POST: count 1

    For any n-tuple of aggregation keys, each unique combination of values
    for the keys defines a separate aggregation instance, which WAF counts
    and rate-limits individually.

    You can optionally nest another statement inside the rate-based
    statement, to narrow the scope of the rule so that it only counts and
    rate limits requests that match the nested statement. You can use this
    nested scope-down statement in conjunction with your aggregation key
    specifications or you can just count and rate limit all requests that
    match the scope-down statement, without additional aggregation. When you
    choose to just manage all requests that match a scope-down statement,
    the aggregation instance is singular for the rule.

    You cannot nest a ``RateBasedStatement`` inside another statement, for
    example inside a ``NotStatement`` or ``OrStatement``. You can define a
    ``RateBasedStatement`` inside a web ACL and inside a rule group.

    For additional information about the options, see `Rate limiting web
    requests using rate-based
    rules <https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-rules.html>`__
    in the *WAF Developer Guide*.

    If you only aggregate on the individual IP address or forwarded IP
    address, you can retrieve the list of IP addresses that WAF is currently
    rate limiting for a rule through the API call
    ``GetRateBasedStatementManagedKeys``. This option is not available for
    other aggregation configurations.

    WAF tracks and manages web requests separately for each instance of a
    rate-based rule that you use. For example, if you provide the same
    rate-based rule settings in two web ACLs, each of the two rule
    statements represents a separate instance of the rate-based rule and
    gets its own tracking and management by WAF. If you define a rate-based
    rule inside a rule group, and then use that rule group in multiple
    places, each use creates a separate instance of the rate-based rule that
    gets its own tracking and management by WAF.
    """

    Limit: RateLimit
    EvaluationWindowSec: Optional[EvaluationWindowSec]
    AggregateKeyType: RateBasedStatementAggregateKeyType
    ScopeDownStatement: Optional[Statement]
    ForwardedIPConfig: Optional[ForwardedIPConfig]
    CustomKeys: Optional[RateBasedStatementCustomKeys]


class RegexPatternSetReferenceStatement(TypedDict, total=False):
    """A rule statement used to search web request components for matches with
    regular expressions. To use this, create a RegexPatternSet that
    specifies the expressions that you want to detect, then use the ARN of
    that set in this statement. A web request matches the pattern set rule
    statement if the request component matches any of the patterns in the
    set. To create a regex pattern set, see CreateRegexPatternSet.

    Each regex pattern set rule statement references a regex pattern set.
    You create and maintain the set independent of your rules. This allows
    you to use the single set in multiple rules. When you update the
    referenced set, WAF automatically updates all rules that reference it.
    """

    ARN: ResourceArn
    FieldToMatch: FieldToMatch
    TextTransformations: TextTransformations


class IPSetForwardedIPConfig(TypedDict, total=False):
    """The configuration for inspecting IP addresses in an HTTP header that you
    specify, instead of using the IP address that's reported by the web
    request origin. Commonly, this is the X-Forwarded-For (XFF) header, but
    you can specify any header name.

    If the specified header isn't present in the request, WAF doesn't apply
    the rule to the web request at all.

    This configuration is used only for IPSetReferenceStatement. For
    GeoMatchStatement and RateBasedStatement, use ForwardedIPConfig instead.
    """

    HeaderName: ForwardedIPHeaderName
    FallbackBehavior: FallbackBehavior
    Position: ForwardedIPPosition


class IPSetReferenceStatement(TypedDict, total=False):
    """A rule statement used to detect web requests coming from particular IP
    addresses or address ranges. To use this, create an IPSet that specifies
    the addresses you want to detect, then use the ARN of that set in this
    statement. To create an IP set, see CreateIPSet.

    Each IP set rule statement references an IP set. You create and maintain
    the set independent of your rules. This allows you to use the single set
    in multiple rules. When you update the referenced set, WAF automatically
    updates all rules that reference it.
    """

    ARN: ResourceArn
    IPSetForwardedIPConfig: Optional[IPSetForwardedIPConfig]


class RuleGroupReferenceStatement(TypedDict, total=False):
    """A rule statement used to run the rules that are defined in a RuleGroup.
    To use this, create a rule group with your rules, then provide the ARN
    of the rule group in this statement.

    You cannot nest a ``RuleGroupReferenceStatement``, for example for use
    inside a ``NotStatement`` or ``OrStatement``. You cannot use a rule
    group reference statement inside another rule group. You can only
    reference a rule group as a top-level statement within a rule that you
    define in a web ACL.
    """

    ARN: ResourceArn
    ExcludedRules: Optional[ExcludedRules]
    RuleActionOverrides: Optional[RuleActionOverrides]


CountryCodes = List[CountryCode]


class GeoMatchStatement(TypedDict, total=False):
    """A rule statement that labels web requests by country and region and that
    matches against web requests based on country code. A geo match rule
    labels every request that it inspects regardless of whether it finds a
    match.

    -  To manage requests only by country, you can use this statement by
       itself and specify the countries that you want to match against in
       the ``CountryCodes`` array.

    -  Otherwise, configure your geo match rule with Count action so that it
       only labels requests. Then, add one or more label match rules to run
       after the geo match rule and configure them to match against the
       geographic labels and handle the requests as needed.

    WAF labels requests using the alpha-2 country and region codes from the
    International Organization for Standardization (ISO) 3166 standard. WAF
    determines the codes using either the IP address in the web request
    origin or, if you specify it, the address in the geo match
    ``ForwardedIPConfig``.

    If you use the web request origin, the label formats are
    ``awswaf:clientip:geo:region:<ISO country code>-<ISO region code>`` and
    ``awswaf:clientip:geo:country:<ISO country code>``.

    If you use a forwarded IP address, the label formats are
    ``awswaf:forwardedip:geo:region:<ISO country code>-<ISO region code>``
    and ``awswaf:forwardedip:geo:country:<ISO country code>``.

    For additional details, see `Geographic match rule
    statement <https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-geo-match.html>`__
    in the `WAF Developer
    Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`__.
    """

    CountryCodes: Optional[CountryCodes]
    ForwardedIPConfig: Optional[ForwardedIPConfig]


Size = int


class SizeConstraintStatement(TypedDict, total=False):
    """A rule statement that compares a number of bytes against the size of a
    request component, using a comparison operator, such as greater than (>)
    or less than (<). For example, you can use a size constraint statement
    to look for query strings that are longer than 100 bytes.

    If you configure WAF to inspect the request body, WAF inspects only the
    number of bytes in the body up to the limit for the web ACL and
    protected resource type. If you know that the request body for your web
    requests should never exceed the inspection limit, you can use a size
    constraint statement to block requests that have a larger request body
    size. For more information about the inspection limits, see ``Body`` and
    ``JsonBody`` settings for the ``FieldToMatch`` data type.

    If you choose URI for the value of Part of the request to filter on, the
    slash (/) in the URI counts as one character. For example, the URI
    ``/logo.jpg`` is nine characters long.
    """

    FieldToMatch: FieldToMatch
    ComparisonOperator: ComparisonOperator
    Size: Size
    TextTransformations: TextTransformations


class XssMatchStatement(TypedDict, total=False):
    """A rule statement that inspects for cross-site scripting (XSS) attacks.
    In XSS attacks, the attacker uses vulnerabilities in a benign website as
    a vehicle to inject malicious client-site scripts into other legitimate
    web browsers.
    """

    FieldToMatch: FieldToMatch
    TextTransformations: TextTransformations


class SqliMatchStatement(TypedDict, total=False):
    """A rule statement that inspects for malicious SQL code. Attackers insert
    malicious SQL code into web requests to do things like modify your
    database or extract data from it.
    """

    FieldToMatch: FieldToMatch
    TextTransformations: TextTransformations
    SensitivityLevel: Optional[SensitivityLevel]


SearchString = bytes


class ByteMatchStatement(TypedDict, total=False):
    """A rule statement that defines a string match search for WAF to apply to
    web requests. The byte match statement provides the bytes to search for,
    the location in requests that you want WAF to search, and other
    settings. The bytes to search for are typically a string that
    corresponds with ASCII characters. In the WAF console and the developer
    guide, this is called a string match statement.
    """

    SearchString: SearchString
    FieldToMatch: FieldToMatch
    TextTransformations: TextTransformations
    PositionalConstraint: PositionalConstraint


class AssociateWebACLRequest(ServiceRequest):
    WebACLArn: ResourceArn
    ResourceArn: ResourceArn


class AssociateWebACLResponse(TypedDict, total=False):
    pass


class RequestBodyAssociatedResourceTypeConfig(TypedDict, total=False):
    """Customizes the maximum size of the request body that your protected
    CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access
    resources forward to WAF for inspection. The default size is 16 KB
    (16,384 bytes). You can change the setting for any of the available
    resource types.

    You are charged additional fees when your protected resources forward
    body sizes that are larger than the default. For more information, see
    `WAF Pricing <http://aws.amazon.com/waf/pricing/>`__.

    Example JSON:
    ``{ "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32" }``

    For Application Load Balancer and AppSync, the limit is fixed at 8 KB
    (8,192 bytes).

    This is used in the ``AssociationConfig`` of the web ACL.
    """

    DefaultSizeInspectionLimit: SizeInspectionLimit


RequestBody = Dict[AssociatedResourceType, RequestBodyAssociatedResourceTypeConfig]


class AssociationConfig(TypedDict, total=False):
    """Specifies custom configurations for the associations between the web ACL
    and protected resources.

    Use this to customize the maximum size of the request body that your
    protected resources forward to WAF for inspection. You can customize
    this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or
    Verified Access resources. The default setting is 16 KB (16,384 bytes).

    You are charged additional fees when your protected resources forward
    body sizes that are larger than the default. For more information, see
    `WAF Pricing <http://aws.amazon.com/waf/pricing/>`__.

    For Application Load Balancer and AppSync, the limit is fixed at 8 KB
    (8,192 bytes).
    """

    RequestBody: Optional[RequestBody]


CapacityUnit = int
TimeWindowSecond = int


class ImmunityTimeProperty(TypedDict, total=False):
    """Used for CAPTCHA and challenge token settings. Determines how long a
    ``CAPTCHA`` or challenge timestamp remains valid after WAF updates it
    for a successful ``CAPTCHA`` or challenge response.
    """

    ImmunityTime: TimeWindowSecond


class CaptchaConfig(TypedDict, total=False):
    """Specifies how WAF should handle ``CAPTCHA`` evaluations. This is
    available at the web ACL level and in each rule.
    """

    ImmunityTimeProperty: Optional[ImmunityTimeProperty]


SolveTimestamp = int


class CaptchaResponse(TypedDict, total=False):
    """The result from the inspection of the web request for a valid
    ``CAPTCHA`` token.
    """

    ResponseCode: Optional[ResponseCode]
    SolveTimestamp: Optional[SolveTimestamp]
    FailureReason: Optional[FailureReason]


class ChallengeConfig(TypedDict, total=False):
    """Specifies how WAF should handle ``Challenge`` evaluations. This is
    available at the web ACL level and in each rule.
    """

    ImmunityTimeProperty: Optional[ImmunityTimeProperty]


class ChallengeResponse(TypedDict, total=False):
    """The result from the inspection of the web request for a valid challenge
    token.
    """

    ResponseCode: Optional[ResponseCode]
    SolveTimestamp: Optional[SolveTimestamp]
    FailureReason: Optional[FailureReason]


class VisibilityConfig(TypedDict, total=False):
    """Defines and enables Amazon CloudWatch metrics and web request sample
    collection.
    """

    SampledRequestsEnabled: Boolean
    CloudWatchMetricsEnabled: Boolean
    MetricName: MetricName


class Label(TypedDict, total=False):
    """A single label container. This is used as an element of a label array in
    multiple contexts, for example, in ``RuleLabels`` inside a Rule and in
    ``Labels`` inside a SampledHTTPRequest.
    """

    Name: LabelName


Labels = List[Label]


class NoneAction(TypedDict, total=False):
    """Specifies that WAF should do nothing. This is used for the
    ``OverrideAction`` setting on a Rule when the rule uses a rule group
    reference statement.

    This is used in the context of other settings, for example to specify
    values for RuleAction and web ACL DefaultAction.

    JSON specification: ``"None": {}``
    """

    pass


OverrideAction = TypedDict(
    "OverrideAction",
    {
        "Count": Optional[CountAction],
        "None": Optional[NoneAction],
    },
    total=False,
)


class Rule(TypedDict, total=False):
    """A single rule, which you can use in a WebACL or RuleGroup to identify
    web requests that you want to manage in some way. Each rule includes one
    top-level Statement that WAF uses to identify matching web requests, and
    parameters that govern how WAF handles them.
    """

    Name: EntityName
    Priority: RulePriority
    Statement: Statement
    Action: Optional[RuleAction]
    OverrideAction: Optional[OverrideAction]
    RuleLabels: Optional[Labels]
    VisibilityConfig: VisibilityConfig
    CaptchaConfig: Optional[CaptchaConfig]
    ChallengeConfig: Optional[ChallengeConfig]


Rules = List[Rule]


class CheckCapacityRequest(ServiceRequest):
    Scope: Scope
    Rules: Rules


ConsumedCapacity = int


class CheckCapacityResponse(TypedDict, total=False):
    Capacity: Optional[ConsumedCapacity]


class LabelNameCondition(TypedDict, total=False):
    """A single label name condition for a Condition in a logging filter."""

    LabelName: LabelName


class Condition(TypedDict, total=False):
    """A single match condition for a Filter."""

    ActionCondition: Optional[ActionCondition]
    LabelNameCondition: Optional[LabelNameCondition]


Conditions = List[Condition]


class CreateAPIKeyRequest(ServiceRequest):
    Scope: Scope
    TokenDomains: APIKeyTokenDomains


class CreateAPIKeyResponse(TypedDict, total=False):
    APIKey: Optional[APIKey]


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

    You can tag the Amazon Web Services resources that you manage through
    WAF: web ACLs, rule groups, IP sets, and regex pattern sets. You can't
    manage or view tags through the WAF console.
    """

    Key: TagKey
    Value: TagValue


TagList = List[Tag]
IPAddresses = List[IPAddress]


class CreateIPSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Description: Optional[EntityDescription]
    IPAddressVersion: IPAddressVersion
    Addresses: IPAddresses
    Tags: Optional[TagList]


class IPSetSummary(TypedDict, total=False):
    """High-level information about an IPSet, returned by operations like
    create and list. This provides information like the ID, that you can use
    to retrieve and manage an ``IPSet``, and the ARN, that you provide to
    the IPSetReferenceStatement to use the address set in a Rule.
    """

    Name: Optional[EntityName]
    Id: Optional[EntityId]
    Description: Optional[EntityDescription]
    LockToken: Optional[LockToken]
    ARN: Optional[ResourceArn]


class CreateIPSetResponse(TypedDict, total=False):
    Summary: Optional[IPSetSummary]


class Regex(TypedDict, total=False):
    """A single regular expression. This is used in a RegexPatternSet."""

    RegexString: Optional[RegexPatternString]


RegularExpressionList = List[Regex]


class CreateRegexPatternSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Description: Optional[EntityDescription]
    RegularExpressionList: RegularExpressionList
    Tags: Optional[TagList]


class RegexPatternSetSummary(TypedDict, total=False):
    """High-level information about a RegexPatternSet, returned by operations
    like create and list. This provides information like the ID, that you
    can use to retrieve and manage a ``RegexPatternSet``, and the ARN, that
    you provide to the RegexPatternSetReferenceStatement to use the pattern
    set in a Rule.
    """

    Name: Optional[EntityName]
    Id: Optional[EntityId]
    Description: Optional[EntityDescription]
    LockToken: Optional[LockToken]
    ARN: Optional[ResourceArn]


class CreateRegexPatternSetResponse(TypedDict, total=False):
    Summary: Optional[RegexPatternSetSummary]


class CustomResponseBody(TypedDict, total=False):
    """The response body to use in a custom response to a web request. This is
    referenced by key from CustomResponse ``CustomResponseBodyKey``.
    """

    ContentType: ResponseContentType
    Content: ResponseContent


CustomResponseBodies = Dict[EntityName, CustomResponseBody]


class CreateRuleGroupRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Capacity: CapacityUnit
    Description: Optional[EntityDescription]
    Rules: Optional[Rules]
    VisibilityConfig: VisibilityConfig
    Tags: Optional[TagList]
    CustomResponseBodies: Optional[CustomResponseBodies]


class RuleGroupSummary(TypedDict, total=False):
    """High-level information about a RuleGroup, returned by operations like
    create and list. This provides information like the ID, that you can use
    to retrieve and manage a ``RuleGroup``, and the ARN, that you provide to
    the RuleGroupReferenceStatement to use the rule group in a Rule.
    """

    Name: Optional[EntityName]
    Id: Optional[EntityId]
    Description: Optional[EntityDescription]
    LockToken: Optional[LockToken]
    ARN: Optional[ResourceArn]


class CreateRuleGroupResponse(TypedDict, total=False):
    Summary: Optional[RuleGroupSummary]


FieldToProtectKeys = List[FieldToProtectKeyName]


class FieldToProtect(TypedDict, total=False):
    """Specifies a field type and keys to protect in stored web request data.
    This is part of the data protection configuration for a web ACL.
    """

    FieldType: FieldToProtectType
    FieldKeys: Optional[FieldToProtectKeys]


class DataProtection(TypedDict, total=False):
    """Specifies the protection behavior for a field type. This is part of the
    data protection configuration for a web ACL.
    """

    Field: FieldToProtect
    Action: DataProtectionAction
    ExcludeRuleMatchDetails: Optional[Boolean]
    ExcludeRateBasedDetails: Optional[Boolean]


DataProtections = List[DataProtection]


class DataProtectionConfig(TypedDict, total=False):
    """Specifies data protection to apply to the web request data for the web
    ACL. This is a web ACL level data protection option.

    The data protection that you configure for the web ACL alters the data
    that's available for any other data collection activity, including your
    WAF logging destinations, web ACL request sampling, and Amazon Security
    Lake data collection and management. Your other option for data
    protection is in the logging configuration, which only affects logging.

    This is part of the data protection configuration for a web ACL.
    """

    DataProtections: DataProtections


class DefaultAction(TypedDict, total=False):
    """In a WebACL, this is the action that you want WAF to perform when a web
    request doesn't match any of the rules in the ``WebACL``. The default
    action must be a terminating action.
    """

    Block: Optional[BlockAction]
    Allow: Optional[AllowAction]


class CreateWebACLRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    DefaultAction: DefaultAction
    Description: Optional[EntityDescription]
    Rules: Optional[Rules]
    VisibilityConfig: VisibilityConfig
    DataProtectionConfig: Optional[DataProtectionConfig]
    Tags: Optional[TagList]
    CustomResponseBodies: Optional[CustomResponseBodies]
    CaptchaConfig: Optional[CaptchaConfig]
    ChallengeConfig: Optional[ChallengeConfig]
    TokenDomains: Optional[TokenDomains]
    AssociationConfig: Optional[AssociationConfig]


class WebACLSummary(TypedDict, total=False):
    """High-level information about a WebACL, returned by operations like
    create and list. This provides information like the ID, that you can use
    to retrieve and manage a ``WebACL``, and the ARN, that you provide to
    operations like AssociateWebACL.
    """

    Name: Optional[EntityName]
    Id: Optional[EntityId]
    Description: Optional[EntityDescription]
    LockToken: Optional[LockToken]
    ARN: Optional[ResourceArn]


class CreateWebACLResponse(TypedDict, total=False):
    Summary: Optional[WebACLSummary]


class DeleteAPIKeyRequest(ServiceRequest):
    Scope: Scope
    APIKey: APIKey


class DeleteAPIKeyResponse(TypedDict, total=False):
    pass


class DeleteFirewallManagerRuleGroupsRequest(ServiceRequest):
    WebACLArn: ResourceArn
    WebACLLockToken: LockToken


class DeleteFirewallManagerRuleGroupsResponse(TypedDict, total=False):
    NextWebACLLockToken: Optional[LockToken]


class DeleteIPSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    LockToken: LockToken


class DeleteIPSetResponse(TypedDict, total=False):
    pass


class DeleteLoggingConfigurationRequest(ServiceRequest):
    ResourceArn: ResourceArn
    LogType: Optional[LogType]
    LogScope: Optional[LogScope]


class DeleteLoggingConfigurationResponse(TypedDict, total=False):
    pass


class DeletePermissionPolicyRequest(ServiceRequest):
    ResourceArn: ResourceArn


class DeletePermissionPolicyResponse(TypedDict, total=False):
    pass


class DeleteRegexPatternSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    LockToken: LockToken


class DeleteRegexPatternSetResponse(TypedDict, total=False):
    pass


class DeleteRuleGroupRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    LockToken: LockToken


class DeleteRuleGroupResponse(TypedDict, total=False):
    pass


class DeleteWebACLRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    LockToken: LockToken


class DeleteWebACLResponse(TypedDict, total=False):
    pass


class DescribeAllManagedProductsRequest(ServiceRequest):
    Scope: Scope


class ManagedProductDescriptor(TypedDict, total=False):
    """The properties of a managed product, such as an Amazon Web Services
    Managed Rules rule group or an Amazon Web Services Marketplace managed
    rule group.
    """

    VendorName: Optional[VendorName]
    ManagedRuleSetName: Optional[EntityName]
    ProductId: Optional[ProductId]
    ProductLink: Optional[ProductLink]
    ProductTitle: Optional[ProductTitle]
    ProductDescription: Optional[ProductDescription]
    SnsTopicArn: Optional[ResourceArn]
    IsVersioningSupported: Optional[Boolean]
    IsAdvancedManagedRuleSet: Optional[Boolean]


ManagedProductDescriptors = List[ManagedProductDescriptor]


class DescribeAllManagedProductsResponse(TypedDict, total=False):
    ManagedProducts: Optional[ManagedProductDescriptors]


class DescribeManagedProductsByVendorRequest(ServiceRequest):
    VendorName: VendorName
    Scope: Scope


class DescribeManagedProductsByVendorResponse(TypedDict, total=False):
    ManagedProducts: Optional[ManagedProductDescriptors]


class DescribeManagedRuleGroupRequest(ServiceRequest):
    VendorName: VendorName
    Name: EntityName
    Scope: Scope
    VersionName: Optional[VersionKeyString]


class LabelSummary(TypedDict, total=False):
    """List of labels used by one or more of the rules of a RuleGroup. This
    summary object is used for the following rule group lists:

    -  ``AvailableLabels`` - Labels that rules add to matching requests.
       These labels are defined in the ``RuleLabels`` for a Rule.

    -  ``ConsumedLabels`` - Labels that rules match against. These labels
       are defined in a ``LabelMatchStatement`` specification, in the
       Statement definition of a rule.
    """

    Name: Optional[LabelName]


LabelSummaries = List[LabelSummary]


class RuleSummary(TypedDict, total=False):
    """High-level information about a Rule, returned by operations like
    DescribeManagedRuleGroup. This provides information like the ID, that
    you can use to retrieve and manage a ``RuleGroup``, and the ARN, that
    you provide to the RuleGroupReferenceStatement to use the rule group in
    a Rule.
    """

    Name: Optional[EntityName]
    Action: Optional[RuleAction]


RuleSummaries = List[RuleSummary]


class DescribeManagedRuleGroupResponse(TypedDict, total=False):
    VersionName: Optional[VersionKeyString]
    SnsTopicArn: Optional[ResourceArn]
    Capacity: Optional[CapacityUnit]
    Rules: Optional[RuleSummaries]
    LabelNamespace: Optional[LabelName]
    AvailableLabels: Optional[LabelSummaries]
    ConsumedLabels: Optional[LabelSummaries]


class DisassociateWebACLRequest(ServiceRequest):
    ResourceArn: ResourceArn


class DisassociateWebACLResponse(TypedDict, total=False):
    pass


class Filter(TypedDict, total=False):
    """A single logging filter, used in LoggingFilter."""

    Behavior: FilterBehavior
    Requirement: FilterRequirement
    Conditions: Conditions


Filters = List[Filter]


class FirewallManagerStatement(TypedDict, total=False):
    """The processing guidance for an Firewall Manager rule. This is like a
    regular rule Statement, but it can only contain a single rule group
    reference.
    """

    ManagedRuleGroupStatement: Optional[ManagedRuleGroupStatement]
    RuleGroupReferenceStatement: Optional[RuleGroupReferenceStatement]


class FirewallManagerRuleGroup(TypedDict, total=False):
    """A rule group that's defined for an Firewall Manager WAF policy."""

    Name: EntityName
    Priority: RulePriority
    FirewallManagerStatement: FirewallManagerStatement
    OverrideAction: OverrideAction
    VisibilityConfig: VisibilityConfig


FirewallManagerRuleGroups = List[FirewallManagerRuleGroup]


class GenerateMobileSdkReleaseUrlRequest(ServiceRequest):
    Platform: Platform
    ReleaseVersion: VersionKeyString


class GenerateMobileSdkReleaseUrlResponse(TypedDict, total=False):
    Url: Optional[DownloadUrl]


class GetDecryptedAPIKeyRequest(ServiceRequest):
    Scope: Scope
    APIKey: APIKey


class GetDecryptedAPIKeyResponse(TypedDict, total=False):
    TokenDomains: Optional[TokenDomains]
    CreationTimestamp: Optional[Timestamp]


class GetIPSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId


class IPSet(TypedDict, total=False):
    """Contains zero or more IP addresses or blocks of IP addresses specified
    in Classless Inter-Domain Routing (CIDR) notation. WAF supports all IPv4
    and IPv6 CIDR ranges except for /0. For information about CIDR notation,
    see the Wikipedia entry `Classless Inter-Domain
    Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__.

    WAF assigns an ARN to each ``IPSet`` that you create. To use an IP set
    in a rule, you provide the ARN to the Rule statement
    IPSetReferenceStatement.
    """

    Name: EntityName
    Id: EntityId
    ARN: ResourceArn
    Description: Optional[EntityDescription]
    IPAddressVersion: IPAddressVersion
    Addresses: IPAddresses


class GetIPSetResponse(TypedDict, total=False):
    IPSet: Optional[IPSet]
    LockToken: Optional[LockToken]


class GetLoggingConfigurationRequest(ServiceRequest):
    ResourceArn: ResourceArn
    LogType: Optional[LogType]
    LogScope: Optional[LogScope]


class LoggingFilter(TypedDict, total=False):
    """Filtering that specifies which web requests are kept in the logs and
    which are dropped, defined for a web ACL's LoggingConfiguration.

    You can filter on the rule action and on the web request labels that
    were applied by matching rules during web ACL evaluation.
    """

    Filters: Filters
    DefaultBehavior: FilterBehavior


RedactedFields = List[FieldToMatch]
LogDestinationConfigs = List[ResourceArn]


class LoggingConfiguration(TypedDict, total=False):
    """Defines an association between logging destinations and a web ACL
    resource, for logging from WAF. As part of the association, you can
    specify parts of the standard logging fields to keep out of the logs and
    you can specify filters so that you log only a subset of the logging
    records.

    If you configure data protection for the web ACL, the protection applies
    to the data that WAF sends to the logs.

    You can define one logging destination per web ACL.

    You can access information about the traffic that WAF inspects using the
    following steps:

    #. Create your logging destination. You can use an Amazon CloudWatch
       Logs log group, an Amazon Simple Storage Service (Amazon S3) bucket,
       or an Amazon Kinesis Data Firehose.

       The name that you give the destination must start with
       ``aws-waf-logs-``. Depending on the type of destination, you might
       need to configure additional settings or permissions.

       For configuration requirements and pricing information for each
       destination type, see `Logging web ACL
       traffic <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__
       in the *WAF Developer Guide*.

    #. Associate your logging destination to your web ACL using a
       ``PutLoggingConfiguration`` request.

    When you successfully enable logging using a ``PutLoggingConfiguration``
    request, WAF creates an additional role or policy that is required to
    write logs to the logging destination. For an Amazon CloudWatch Logs log
    group, WAF creates a resource policy on the log group. For an Amazon S3
    bucket, WAF creates a bucket policy. For an Amazon Kinesis Data
    Firehose, WAF creates a service-linked role.

    For additional information about web ACL logging, see `Logging web ACL
    traffic
    information <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__
    in the *WAF Developer Guide*.
    """

    ResourceArn: ResourceArn
    LogDestinationConfigs: LogDestinationConfigs
    RedactedFields: Optional[RedactedFields]
    ManagedByFirewallManager: Optional[Boolean]
    LoggingFilter: Optional[LoggingFilter]
    LogType: Optional[LogType]
    LogScope: Optional[LogScope]


class GetLoggingConfigurationResponse(TypedDict, total=False):
    LoggingConfiguration: Optional[LoggingConfiguration]


class GetManagedRuleSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId


class ManagedRuleSetVersion(TypedDict, total=False):
    """Information for a single version of a managed rule set.

    This is intended for use only by vendors of managed rule sets. Vendors
    are Amazon Web Services and Amazon Web Services Marketplace sellers.

    Vendors, you can use the managed rule set APIs to provide controlled
    rollout of your versioned managed rule group offerings for your
    customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
    ``PutManagedRuleSetVersions``, and
    ``UpdateManagedRuleSetVersionExpiryDate``.
    """

    AssociatedRuleGroupArn: Optional[ResourceArn]
    Capacity: Optional[CapacityUnit]
    ForecastedLifetime: Optional[TimeWindowDay]
    PublishTimestamp: Optional[Timestamp]
    LastUpdateTimestamp: Optional[Timestamp]
    ExpiryTimestamp: Optional[Timestamp]


PublishedVersions = Dict[VersionKeyString, ManagedRuleSetVersion]


class ManagedRuleSet(TypedDict, total=False):
    """A set of rules that is managed by Amazon Web Services and Amazon Web
    Services Marketplace sellers to provide versioned managed rule groups
    for customers of WAF.

    This is intended for use only by vendors of managed rule sets. Vendors
    are Amazon Web Services and Amazon Web Services Marketplace sellers.

    Vendors, you can use the managed rule set APIs to provide controlled
    rollout of your versioned managed rule group offerings for your
    customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
    ``PutManagedRuleSetVersions``, and
    ``UpdateManagedRuleSetVersionExpiryDate``.
    """

    Name: EntityName
    Id: EntityId
    ARN: ResourceArn
    Description: Optional[EntityDescription]
    PublishedVersions: Optional[PublishedVersions]
    RecommendedVersion: Optional[VersionKeyString]
    LabelNamespace: Optional[LabelName]


class GetManagedRuleSetResponse(TypedDict, total=False):
    ManagedRuleSet: Optional[ManagedRuleSet]
    LockToken: Optional[LockToken]


class GetMobileSdkReleaseRequest(ServiceRequest):
    Platform: Platform
    ReleaseVersion: VersionKeyString


class MobileSdkRelease(TypedDict, total=False):
    """Information for a release of the mobile SDK, including release notes and
    tags.

    The mobile SDK is not generally available. Customers who have access to
    the mobile SDK can use it to establish and manage WAF tokens for use in
    HTTP(S) requests from a mobile device to WAF. For more information, see
    `WAF client application
    integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
    in the *WAF Developer Guide*.
    """

    ReleaseVersion: Optional[VersionKeyString]
    Timestamp: Optional[Timestamp]
    ReleaseNotes: Optional[ReleaseNotes]
    Tags: Optional[TagList]


class GetMobileSdkReleaseResponse(TypedDict, total=False):
    MobileSdkRelease: Optional[MobileSdkRelease]


class GetPermissionPolicyRequest(ServiceRequest):
    ResourceArn: ResourceArn


class GetPermissionPolicyResponse(TypedDict, total=False):
    Policy: Optional[PolicyString]


class GetRateBasedStatementManagedKeysRequest(ServiceRequest):
    Scope: Scope
    WebACLName: EntityName
    WebACLId: EntityId
    RuleGroupRuleName: Optional[EntityName]
    RuleName: EntityName


class RateBasedStatementManagedKeysIPSet(TypedDict, total=False):
    """The set of IP addresses that are currently blocked for a
    RateBasedStatement. This is only available for rate-based rules that
    aggregate on just the IP address, with the ``AggregateKeyType`` set to
    ``IP`` or ``FORWARDED_IP``.

    A rate-based rule applies its rule action to requests from IP addresses
    that are in the rule's managed keys list and that match the rule's
    scope-down statement. When a rule has no scope-down statement, it
    applies the action to all requests from the IP addresses that are in the
    list. The rule applies its rule action to rate limit the matching
    requests. The action is usually Block but it can be any valid rule
    action except for Allow.

    The maximum number of IP addresses that can be rate limited by a single
    rate-based rule instance is 10,000. If more than 10,000 addresses exceed
    the rate limit, WAF limits those with the highest rates.
    """

    IPAddressVersion: Optional[IPAddressVersion]
    Addresses: Optional[IPAddresses]


class GetRateBasedStatementManagedKeysResponse(TypedDict, total=False):
    ManagedKeysIPV4: Optional[RateBasedStatementManagedKeysIPSet]
    ManagedKeysIPV6: Optional[RateBasedStatementManagedKeysIPSet]


class GetRegexPatternSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId


class RegexPatternSet(TypedDict, total=False):
    """Contains one or more regular expressions.

    WAF assigns an ARN to each ``RegexPatternSet`` that you create. To use a
    set in a rule, you provide the ARN to the Rule statement
    RegexPatternSetReferenceStatement.
    """

    Name: Optional[EntityName]
    Id: Optional[EntityId]
    ARN: Optional[ResourceArn]
    Description: Optional[EntityDescription]
    RegularExpressionList: Optional[RegularExpressionList]


class GetRegexPatternSetResponse(TypedDict, total=False):
    RegexPatternSet: Optional[RegexPatternSet]
    LockToken: Optional[LockToken]


class GetRuleGroupRequest(ServiceRequest):
    Name: Optional[EntityName]
    Scope: Optional[Scope]
    Id: Optional[EntityId]
    ARN: Optional[ResourceArn]


class RuleGroup(TypedDict, total=False):
    """A rule group defines a collection of rules to inspect and control web
    requests that you can use in a WebACL. When you create a rule group, you
    define an immutable capacity limit. If you update a rule group, you must
    stay within the capacity. This allows others to reuse the rule group
    with confidence in its capacity requirements.
    """

    Name: EntityName
    Id: EntityId
    Capacity: CapacityUnit
    ARN: ResourceArn
    Description: Optional[EntityDescription]
    Rules: Optional[Rules]
    VisibilityConfig: VisibilityConfig
    LabelNamespace: Optional[LabelName]
    CustomResponseBodies: Optional[CustomResponseBodies]
    AvailableLabels: Optional[LabelSummaries]
    ConsumedLabels: Optional[LabelSummaries]


class GetRuleGroupResponse(TypedDict, total=False):
    RuleGroup: Optional[RuleGroup]
    LockToken: Optional[LockToken]


ListMaxItems = int


class TimeWindow(TypedDict, total=False):
    """In a GetSampledRequests request, the ``StartTime`` and ``EndTime``
    objects specify the time range for which you want WAF to return a sample
    of web requests.

    You must specify the times in Coordinated Universal Time (UTC) format.
    UTC format includes the special designator, ``Z``. For example,
    ``"2016-09-27T14:50Z"``. You can specify any time range in the previous
    three hours.

    In a GetSampledRequests response, the ``StartTime`` and ``EndTime``
    objects specify the time range for which WAF actually returned a sample
    of web requests. WAF gets the specified number of requests from among
    the first 5,000 requests that your Amazon Web Services resource receives
    during the specified time period. If your resource receives more than
    5,000 requests during that period, WAF stops sampling after the 5,000th
    request. In that case, ``EndTime`` is the time that WAF received the
    5,000th request.
    """

    StartTime: Timestamp
    EndTime: Timestamp


class GetSampledRequestsRequest(ServiceRequest):
    WebAclArn: ResourceArn
    RuleMetricName: MetricName
    Scope: Scope
    TimeWindow: TimeWindow
    MaxItems: ListMaxItems


PopulationSize = int


class HTTPHeader(TypedDict, total=False):
    """Part of the response from GetSampledRequests. This is a complex type
    that appears as ``Headers`` in the response syntax. ``HTTPHeader``
    contains the names and values of all of the headers that appear in one
    of the web requests.
    """

    Name: Optional[HeaderName]
    Value: Optional[HeaderValue]


HTTPHeaders = List[HTTPHeader]
SampleWeight = int


class HTTPRequest(TypedDict, total=False):
    """Part of the response from GetSampledRequests. This is a complex type
    that appears as ``Request`` in the response syntax. ``HTTPRequest``
    contains information about one of the web requests.
    """

    ClientIP: Optional[IPString]
    Country: Optional[Country]
    URI: Optional[URIString]
    Method: Optional[HTTPMethod]
    HTTPVersion: Optional[HTTPVersion]
    Headers: Optional[HTTPHeaders]


class SampledHTTPRequest(TypedDict, total=False):
    """Represents a single sampled web request. The response from
    GetSampledRequests includes a ``SampledHTTPRequests`` complex type that
    appears as ``SampledRequests`` in the response syntax.
    ``SampledHTTPRequests`` contains an array of ``SampledHTTPRequest``
    objects.
    """

    Request: HTTPRequest
    Weight: SampleWeight
    Timestamp: Optional[Timestamp]
    Action: Optional[Action]
    RuleNameWithinRuleGroup: Optional[EntityName]
    RequestHeadersInserted: Optional[HTTPHeaders]
    ResponseCodeSent: Optional[ResponseStatusCode]
    Labels: Optional[Labels]
    CaptchaResponse: Optional[CaptchaResponse]
    ChallengeResponse: Optional[ChallengeResponse]
    OverriddenAction: Optional[Action]


SampledHTTPRequests = List[SampledHTTPRequest]


class GetSampledRequestsResponse(TypedDict, total=False):
    SampledRequests: Optional[SampledHTTPRequests]
    PopulationSize: Optional[PopulationSize]
    TimeWindow: Optional[TimeWindow]


class GetWebACLForResourceRequest(ServiceRequest):
    ResourceArn: ResourceArn


class WebACL(TypedDict, total=False):
    """A web ACL defines a collection of rules to use to inspect and control
    web requests. Each rule has a statement that defines what to look for in
    web requests and an action that WAF applies to requests that match the
    statement. In the web ACL, you assign a default action to take (allow,
    block) for any request that does not match any of the rules. The rules
    in a web ACL can be a combination of the types Rule, RuleGroup, and
    managed rule group. You can associate a web ACL with one or more Amazon
    Web Services resources to protect. The resource types include Amazon
    CloudFront distribution, Amazon API Gateway REST API, Application Load
    Balancer, AppSync GraphQL API, Amazon Cognito user pool, App Runner
    service, Amplify application, and Amazon Web Services Verified Access
    instance.
    """

    Name: EntityName
    Id: EntityId
    ARN: ResourceArn
    DefaultAction: DefaultAction
    Description: Optional[EntityDescription]
    Rules: Optional[Rules]
    VisibilityConfig: VisibilityConfig
    DataProtectionConfig: Optional[DataProtectionConfig]
    Capacity: Optional[ConsumedCapacity]
    PreProcessFirewallManagerRuleGroups: Optional[FirewallManagerRuleGroups]
    PostProcessFirewallManagerRuleGroups: Optional[FirewallManagerRuleGroups]
    ManagedByFirewallManager: Optional[Boolean]
    LabelNamespace: Optional[LabelName]
    CustomResponseBodies: Optional[CustomResponseBodies]
    CaptchaConfig: Optional[CaptchaConfig]
    ChallengeConfig: Optional[ChallengeConfig]
    TokenDomains: Optional[TokenDomains]
    AssociationConfig: Optional[AssociationConfig]
    RetrofittedByFirewallManager: Optional[Boolean]


class GetWebACLForResourceResponse(TypedDict, total=False):
    WebACL: Optional[WebACL]


class GetWebACLRequest(ServiceRequest):
    Name: Optional[EntityName]
    Scope: Optional[Scope]
    Id: Optional[EntityId]
    ARN: Optional[ResourceArn]


class GetWebACLResponse(TypedDict, total=False):
    WebACL: Optional[WebACL]
    LockToken: Optional[LockToken]
    ApplicationIntegrationURL: Optional[OutputUrl]


IPSetSummaries = List[IPSetSummary]


class ListAPIKeysRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


class ListAPIKeysResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    APIKeySummaries: Optional[APIKeySummaries]
    ApplicationIntegrationURL: Optional[OutputUrl]


class ListAvailableManagedRuleGroupVersionsRequest(ServiceRequest):
    VendorName: VendorName
    Name: EntityName
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


class ManagedRuleGroupVersion(TypedDict, total=False):
    """Describes a single version of a managed rule group."""

    Name: Optional[VersionKeyString]
    LastUpdateTimestamp: Optional[Timestamp]


ManagedRuleGroupVersions = List[ManagedRuleGroupVersion]


class ListAvailableManagedRuleGroupVersionsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    Versions: Optional[ManagedRuleGroupVersions]
    CurrentDefaultVersion: Optional[VersionKeyString]


class ListAvailableManagedRuleGroupsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


class ManagedRuleGroupSummary(TypedDict, total=False):
    """High-level information about a managed rule group, returned by
    ListAvailableManagedRuleGroups. This provides information like the name
    and vendor name, that you provide when you add a
    ManagedRuleGroupStatement to a web ACL. Managed rule groups include
    Amazon Web Services Managed Rules rule groups and Amazon Web Services
    Marketplace managed rule groups. To use any Amazon Web Services
    Marketplace managed rule group, first subscribe to the rule group
    through Amazon Web Services Marketplace.
    """

    VendorName: Optional[VendorName]
    Name: Optional[EntityName]
    VersioningSupported: Optional[Boolean]
    Description: Optional[EntityDescription]


ManagedRuleGroupSummaries = List[ManagedRuleGroupSummary]


class ListAvailableManagedRuleGroupsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    ManagedRuleGroups: Optional[ManagedRuleGroupSummaries]


class ListIPSetsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


class ListIPSetsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    IPSets: Optional[IPSetSummaries]


class ListLoggingConfigurationsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]
    LogScope: Optional[LogScope]


LoggingConfigurations = List[LoggingConfiguration]


class ListLoggingConfigurationsResponse(TypedDict, total=False):
    LoggingConfigurations: Optional[LoggingConfigurations]
    NextMarker: Optional[NextMarker]


class ListManagedRuleSetsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


class ManagedRuleSetSummary(TypedDict, total=False):
    """High-level information for a managed rule set.

    This is intended for use only by vendors of managed rule sets. Vendors
    are Amazon Web Services and Amazon Web Services Marketplace sellers.

    Vendors, you can use the managed rule set APIs to provide controlled
    rollout of your versioned managed rule group offerings for your
    customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
    ``PutManagedRuleSetVersions``, and
    ``UpdateManagedRuleSetVersionExpiryDate``.
    """

    Name: Optional[EntityName]
    Id: Optional[EntityId]
    Description: Optional[EntityDescription]
    LockToken: Optional[LockToken]
    ARN: Optional[ResourceArn]
    LabelNamespace: Optional[LabelName]


ManagedRuleSetSummaries = List[ManagedRuleSetSummary]


class ListManagedRuleSetsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    ManagedRuleSets: Optional[ManagedRuleSetSummaries]


class ListMobileSdkReleasesRequest(ServiceRequest):
    Platform: Platform
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


class ReleaseSummary(TypedDict, total=False):
    """High level information for an SDK release."""

    ReleaseVersion: Optional[VersionKeyString]
    Timestamp: Optional[Timestamp]


ReleaseSummaries = List[ReleaseSummary]


class ListMobileSdkReleasesResponse(TypedDict, total=False):
    ReleaseSummaries: Optional[ReleaseSummaries]
    NextMarker: Optional[NextMarker]


class ListRegexPatternSetsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


RegexPatternSetSummaries = List[RegexPatternSetSummary]


class ListRegexPatternSetsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    RegexPatternSets: Optional[RegexPatternSetSummaries]


class ListResourcesForWebACLRequest(ServiceRequest):
    WebACLArn: ResourceArn
    ResourceType: Optional[ResourceType]


ResourceArns = List[ResourceArn]


class ListResourcesForWebACLResponse(TypedDict, total=False):
    ResourceArns: Optional[ResourceArns]


class ListRuleGroupsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


RuleGroupSummaries = List[RuleGroupSummary]


class ListRuleGroupsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    RuleGroups: Optional[RuleGroupSummaries]


class ListTagsForResourceRequest(ServiceRequest):
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]
    ResourceARN: ResourceArn


class TagInfoForResource(TypedDict, total=False):
    """The collection of tagging definitions for an Amazon Web Services
    resource. Tags are key:value pairs that you can use to categorize and
    manage your resources, for purposes like billing or other management.
    Typically, the tag key represents a category, such as "environment", and
    the tag value represents a specific value within that category, such as
    "test," "development," or "production". Or you might set the tag key to
    "customer" and the value to the customer name or ID. You can specify one
    or more tags to add to each Amazon Web Services resource, up to 50 tags
    for a resource.

    You can tag the Amazon Web Services resources that you manage through
    WAF: web ACLs, rule groups, IP sets, and regex pattern sets. You can't
    manage or view tags through the WAF console.
    """

    ResourceARN: Optional[ResourceArn]
    TagList: Optional[TagList]


class ListTagsForResourceResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    TagInfoForResource: Optional[TagInfoForResource]


class ListWebACLsRequest(ServiceRequest):
    Scope: Scope
    NextMarker: Optional[NextMarker]
    Limit: Optional[PaginationLimit]


WebACLSummaries = List[WebACLSummary]


class ListWebACLsResponse(TypedDict, total=False):
    NextMarker: Optional[NextMarker]
    WebACLs: Optional[WebACLSummaries]


class PutLoggingConfigurationRequest(ServiceRequest):
    LoggingConfiguration: LoggingConfiguration


class PutLoggingConfigurationResponse(TypedDict, total=False):
    LoggingConfiguration: Optional[LoggingConfiguration]


class VersionToPublish(TypedDict, total=False):
    """A version of the named managed rule group, that the rule group's vendor
    publishes for use by customers.

    This is intended for use only by vendors of managed rule sets. Vendors
    are Amazon Web Services and Amazon Web Services Marketplace sellers.

    Vendors, you can use the managed rule set APIs to provide controlled
    rollout of your versioned managed rule group offerings for your
    customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
    ``PutManagedRuleSetVersions``, and
    ``UpdateManagedRuleSetVersionExpiryDate``.
    """

    AssociatedRuleGroupArn: Optional[ResourceArn]
    ForecastedLifetime: Optional[TimeWindowDay]


VersionsToPublish = Dict[VersionKeyString, VersionToPublish]


class PutManagedRuleSetVersionsRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    LockToken: LockToken
    RecommendedVersion: Optional[VersionKeyString]
    VersionsToPublish: Optional[VersionsToPublish]


class PutManagedRuleSetVersionsResponse(TypedDict, total=False):
    NextLockToken: Optional[LockToken]


class PutPermissionPolicyRequest(ServiceRequest):
    ResourceArn: ResourceArn
    Policy: PolicyString


class PutPermissionPolicyResponse(TypedDict, total=False):
    pass


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


class UpdateIPSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    Description: Optional[EntityDescription]
    Addresses: IPAddresses
    LockToken: LockToken


class UpdateIPSetResponse(TypedDict, total=False):
    NextLockToken: Optional[LockToken]


class UpdateManagedRuleSetVersionExpiryDateRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    LockToken: LockToken
    VersionToExpire: VersionKeyString
    ExpiryTimestamp: Timestamp


class UpdateManagedRuleSetVersionExpiryDateResponse(TypedDict, total=False):
    ExpiringVersion: Optional[VersionKeyString]
    ExpiryTimestamp: Optional[Timestamp]
    NextLockToken: Optional[LockToken]


class UpdateRegexPatternSetRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    Description: Optional[EntityDescription]
    RegularExpressionList: RegularExpressionList
    LockToken: LockToken


class UpdateRegexPatternSetResponse(TypedDict, total=False):
    NextLockToken: Optional[LockToken]


class UpdateRuleGroupRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    Description: Optional[EntityDescription]
    Rules: Optional[Rules]
    VisibilityConfig: VisibilityConfig
    LockToken: LockToken
    CustomResponseBodies: Optional[CustomResponseBodies]


class UpdateRuleGroupResponse(TypedDict, total=False):
    NextLockToken: Optional[LockToken]


class UpdateWebACLRequest(ServiceRequest):
    Name: EntityName
    Scope: Scope
    Id: EntityId
    DefaultAction: DefaultAction
    Description: Optional[EntityDescription]
    Rules: Optional[Rules]
    VisibilityConfig: VisibilityConfig
    DataProtectionConfig: Optional[DataProtectionConfig]
    LockToken: LockToken
    CustomResponseBodies: Optional[CustomResponseBodies]
    CaptchaConfig: Optional[CaptchaConfig]
    ChallengeConfig: Optional[ChallengeConfig]
    TokenDomains: Optional[TokenDomains]
    AssociationConfig: Optional[AssociationConfig]


class UpdateWebACLResponse(TypedDict, total=False):
    NextLockToken: Optional[LockToken]


class Wafv2Api:
    service = "wafv2"
    version = "2019-07-29"

    @handler("AssociateWebACL")
    def associate_web_acl(
        self, context: RequestContext, web_acl_arn: ResourceArn, resource_arn: ResourceArn, **kwargs
    ) -> AssociateWebACLResponse:
        """Associates a web ACL with a resource, to protect the resource.

        Use this for all resource types except for Amazon CloudFront
        distributions. For Amazon CloudFront, call ``UpdateDistribution`` for
        the distribution and provide the Amazon Resource Name (ARN) of the web
        ACL in the web ACL ID. For information, see
        `UpdateDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html>`__
        in the *Amazon CloudFront Developer Guide*.

        **Required permissions for customer-managed IAM policies**

        This call requires permissions that are specific to the protected
        resource type. For details, see `Permissions for
        AssociateWebACL <https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL>`__
        in the *WAF Developer Guide*.

        **Temporary inconsistencies during updates**

        When you create or change a web ACL or other WAF resources, the changes
        take a small amount of time to propagate to all areas where the
        resources are stored. The propagation time can be from a few seconds to
        a number of minutes.

        The following are examples of the temporary inconsistencies that you
        might notice during change propagation:

        -  After you create a web ACL, if you try to associate it with a
           resource, you might get an exception indicating that the web ACL is
           unavailable.

        -  After you add a rule group to a web ACL, the new rule group rules
           might be in effect in one area where the web ACL is used and not in
           another.

        -  After you change a rule action setting, you might see the old action
           in some places and the new action in others.

        -  After you add an IP address to an IP set that is in use in a blocking
           rule, the new address might be blocked in one area while still
           allowed in another.

        :param web_acl_arn: The Amazon Resource Name (ARN) of the web ACL that you want to associate
        with the resource.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource to associate with the web
        ACL.
        :returns: AssociateWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFUnavailableEntityException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("CheckCapacity")
    def check_capacity(
        self, context: RequestContext, scope: Scope, rules: Rules, **kwargs
    ) -> CheckCapacityResponse:
        """Returns the web ACL capacity unit (WCU) requirements for a specified
        scope and set of rules. You can use this to check the capacity
        requirements for the rules you want to use in a RuleGroup or WebACL.

        WAF uses WCUs to calculate and control the operating resources that are
        used to run your rules, rule groups, and web ACLs. WAF calculates
        capacity differently for each rule type, to reflect the relative cost of
        each rule. Simple rules that cost little to run use fewer WCUs than more
        complex rules that use more processing power. Rule group capacity is
        fixed at creation, which helps users plan their web ACL WCU usage when
        they use a rule group. For more information, see `WAF web ACL capacity
        units
        (WCU) <https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html>`__
        in the *WAF Developer Guide*.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param rules: An array of Rule that you're configuring to use in a rule group or web
        ACL.
        :returns: CheckCapacityResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFLimitsExceededException:
        :raises WAFInvalidResourceException:
        :raises WAFUnavailableEntityException:
        :raises WAFSubscriptionNotFoundException:
        :raises WAFExpiredManagedRuleGroupVersionException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("CreateAPIKey")
    def create_api_key(
        self, context: RequestContext, scope: Scope, token_domains: APIKeyTokenDomains, **kwargs
    ) -> CreateAPIKeyResponse:
        """Creates an API key that contains a set of token domains.

        API keys are required for the integration of the CAPTCHA API in your
        JavaScript client applications. The API lets you customize the placement
        and characteristics of the CAPTCHA puzzle for your end users. For more
        information about the CAPTCHA JavaScript integration, see `WAF client
        application
        integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
        in the *WAF Developer Guide*.

        You can use a single key for up to 5 domains. After you generate a key,
        you can copy it for use in your JavaScript integration.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param token_domains: The client application domains that you want to use this API key for.
        :returns: CreateAPIKeyResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        :raises WAFLimitsExceededException:
        """
        raise NotImplementedError

    @handler("CreateIPSet")
    def create_ip_set(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        ip_address_version: IPAddressVersion,
        addresses: IPAddresses,
        description: EntityDescription | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateIPSetResponse:
        """Creates an IPSet, which you use to identify web requests that originate
        from specific IP addresses or ranges of IP addresses. For example, if
        you're receiving a lot of requests from a ranges of IP addresses, you
        can configure WAF to block them using an IPSet that lists those IP
        addresses.

        :param name: The name of the IP set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param ip_address_version: The version of the IP addresses, either ``IPV4`` or ``IPV6``.
        :param addresses: Contains an array of strings that specifies zero or more IP addresses or
        blocks of IP addresses that you want WAF to inspect for in incoming
        requests.
        :param description: A description of the IP set that helps with identification.
        :param tags: An array of key:value pairs to associate with the resource.
        :returns: CreateIPSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("CreateRegexPatternSet")
    def create_regex_pattern_set(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        regular_expression_list: RegularExpressionList,
        description: EntityDescription | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateRegexPatternSetResponse:
        """Creates a RegexPatternSet, which you reference in a
        RegexPatternSetReferenceStatement, to have WAF inspect a web request
        component for the specified patterns.

        :param name: The name of the set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param regular_expression_list: Array of regular expression strings.
        :param description: A description of the set that helps with identification.
        :param tags: An array of key:value pairs to associate with the resource.
        :returns: CreateRegexPatternSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("CreateRuleGroup")
    def create_rule_group(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        capacity: CapacityUnit,
        visibility_config: VisibilityConfig,
        description: EntityDescription | None = None,
        rules: Rules | None = None,
        tags: TagList | None = None,
        custom_response_bodies: CustomResponseBodies | None = None,
        **kwargs,
    ) -> CreateRuleGroupResponse:
        """Creates a RuleGroup per the specifications provided.

        A rule group defines a collection of rules to inspect and control web
        requests that you can use in a WebACL. When you create a rule group, you
        define an immutable capacity limit. If you update a rule group, you must
        stay within the capacity. This allows others to reuse the rule group
        with confidence in its capacity requirements.

        :param name: The name of the rule group.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param capacity: The web ACL capacity units (WCUs) required for this rule group.
        :param visibility_config: Defines and enables Amazon CloudWatch metrics and web request sample
        collection.
        :param description: A description of the rule group that helps with identification.
        :param rules: The Rule statements used to identify the web requests that you want to
        manage.
        :param tags: An array of key:value pairs to associate with the resource.
        :param custom_response_bodies: A map of custom response keys and content bodies.
        :returns: CreateRuleGroupResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFUnavailableEntityException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFSubscriptionNotFoundException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("CreateWebACL")
    def create_web_acl(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        default_action: DefaultAction,
        visibility_config: VisibilityConfig,
        description: EntityDescription | None = None,
        rules: Rules | None = None,
        data_protection_config: DataProtectionConfig | None = None,
        tags: TagList | None = None,
        custom_response_bodies: CustomResponseBodies | None = None,
        captcha_config: CaptchaConfig | None = None,
        challenge_config: ChallengeConfig | None = None,
        token_domains: TokenDomains | None = None,
        association_config: AssociationConfig | None = None,
        **kwargs,
    ) -> CreateWebACLResponse:
        """Creates a WebACL per the specifications provided.

        A web ACL defines a collection of rules to use to inspect and control
        web requests. Each rule has a statement that defines what to look for in
        web requests and an action that WAF applies to requests that match the
        statement. In the web ACL, you assign a default action to take (allow,
        block) for any request that does not match any of the rules. The rules
        in a web ACL can be a combination of the types Rule, RuleGroup, and
        managed rule group. You can associate a web ACL with one or more Amazon
        Web Services resources to protect. The resource types include Amazon
        CloudFront distribution, Amazon API Gateway REST API, Application Load
        Balancer, AppSync GraphQL API, Amazon Cognito user pool, App Runner
        service, Amplify application, and Amazon Web Services Verified Access
        instance.

        :param name: The name of the web ACL.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param default_action: The action to perform if none of the ``Rules`` contained in the
        ``WebACL`` match.
        :param visibility_config: Defines and enables Amazon CloudWatch metrics and web request sample
        collection.
        :param description: A description of the web ACL that helps with identification.
        :param rules: The Rule statements used to identify the web requests that you want to
        manage.
        :param data_protection_config: Specifies data protection to apply to the web request data for the web
        ACL.
        :param tags: An array of key:value pairs to associate with the resource.
        :param custom_response_bodies: A map of custom response keys and content bodies.
        :param captcha_config: Specifies how WAF should handle ``CAPTCHA`` evaluations for rules that
        don't have their own ``CaptchaConfig`` settings.
        :param challenge_config: Specifies how WAF should handle challenge evaluations for rules that
        don't have their own ``ChallengeConfig`` settings.
        :param token_domains: Specifies the domains that WAF should accept in a web request token.
        :param association_config: Specifies custom configurations for the associations between the web ACL
        and protected resources.
        :returns: CreateWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFInvalidResourceException:
        :raises WAFUnavailableEntityException:
        :raises WAFNonexistentItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFSubscriptionNotFoundException:
        :raises WAFInvalidOperationException:
        :raises WAFConfigurationWarningException:
        :raises WAFExpiredManagedRuleGroupVersionException:
        """
        raise NotImplementedError

    @handler("DeleteAPIKey")
    def delete_api_key(
        self, context: RequestContext, scope: Scope, api_key: APIKey, **kwargs
    ) -> DeleteAPIKeyResponse:
        """Deletes the specified API key.

        After you delete a key, it can take up to 24 hours for WAF to disallow
        use of the key in all regions.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param api_key: The encrypted API key that you want to delete.
        :returns: DeleteAPIKeyResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteFirewallManagerRuleGroups")
    def delete_firewall_manager_rule_groups(
        self,
        context: RequestContext,
        web_acl_arn: ResourceArn,
        web_acl_lock_token: LockToken,
        **kwargs,
    ) -> DeleteFirewallManagerRuleGroupsResponse:
        """Deletes all rule groups that are managed by Firewall Manager from the
        specified WebACL.

        You can only use this if ``ManagedByFirewallManager`` and
        ``RetrofittedByFirewallManager`` are both false in the web ACL.

        :param web_acl_arn: The Amazon Resource Name (ARN) of the web ACL.
        :param web_acl_lock_token: A token used for optimistic locking.
        :returns: DeleteFirewallManagerRuleGroupsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteIPSet")
    def delete_ip_set(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        lock_token: LockToken,
        **kwargs,
    ) -> DeleteIPSetResponse:
        """Deletes the specified IPSet.

        :param name: The name of the IP set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the set.
        :param lock_token: A token used for optimistic locking.
        :returns: DeleteIPSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFAssociatedItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteLoggingConfiguration")
    def delete_logging_configuration(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        log_type: LogType | None = None,
        log_scope: LogScope | None = None,
        **kwargs,
    ) -> DeleteLoggingConfigurationResponse:
        """Deletes the LoggingConfiguration from the specified web ACL.

        :param resource_arn: The Amazon Resource Name (ARN) of the web ACL from which you want to
        delete the LoggingConfiguration.
        :param log_type: Used to distinguish between various logging options.
        :param log_scope: The owner of the logging configuration, which must be set to
        ``CUSTOMER`` for the configurations that you manage.
        :returns: DeleteLoggingConfigurationResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeletePermissionPolicy")
    def delete_permission_policy(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> DeletePermissionPolicyResponse:
        """Permanently deletes an IAM policy from the specified rule group.

        You must be the owner of the rule group to perform this operation.

        :param resource_arn: The Amazon Resource Name (ARN) of the rule group from which you want to
        delete the policy.
        :returns: DeletePermissionPolicyResponse
        :raises WAFNonexistentItemException:
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        """
        raise NotImplementedError

    @handler("DeleteRegexPatternSet")
    def delete_regex_pattern_set(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        lock_token: LockToken,
        **kwargs,
    ) -> DeleteRegexPatternSetResponse:
        """Deletes the specified RegexPatternSet.

        :param name: The name of the set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the set.
        :param lock_token: A token used for optimistic locking.
        :returns: DeleteRegexPatternSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFAssociatedItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteRuleGroup")
    def delete_rule_group(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        lock_token: LockToken,
        **kwargs,
    ) -> DeleteRuleGroupResponse:
        """Deletes the specified RuleGroup.

        :param name: The name of the rule group.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the rule group.
        :param lock_token: A token used for optimistic locking.
        :returns: DeleteRuleGroupResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFAssociatedItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteWebACL")
    def delete_web_acl(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        lock_token: LockToken,
        **kwargs,
    ) -> DeleteWebACLResponse:
        """Deletes the specified WebACL.

        You can only use this if ``ManagedByFirewallManager`` is false in the
        web ACL.

        Before deleting any web ACL, first disassociate it from all resources.

        -  To retrieve a list of the resources that are associated with a web
           ACL, use the following calls:

           -  For Amazon CloudFront distributions, use the CloudFront call
              ``ListDistributionsByWebACLId``. For information, see
              `ListDistributionsByWebACLId <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html>`__
              in the *Amazon CloudFront API Reference*.

           -  For all other resources, call ListResourcesForWebACL.

        -  To disassociate a resource from a web ACL, use the following calls:

           -  For Amazon CloudFront distributions, provide an empty web ACL ID
              in the CloudFront call ``UpdateDistribution``. For information,
              see
              `UpdateDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html>`__
              in the *Amazon CloudFront API Reference*.

           -  For all other resources, call DisassociateWebACL.

        :param name: The name of the web ACL.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: The unique identifier for the web ACL.
        :param lock_token: A token used for optimistic locking.
        :returns: DeleteWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFAssociatedItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("DescribeAllManagedProducts")
    def describe_all_managed_products(
        self, context: RequestContext, scope: Scope, **kwargs
    ) -> DescribeAllManagedProductsResponse:
        """Provides high-level information for the Amazon Web Services Managed
        Rules rule groups and Amazon Web Services Marketplace managed rule
        groups.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :returns: DescribeAllManagedProductsResponse
        :raises WAFInvalidOperationException:
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        """
        raise NotImplementedError

    @handler("DescribeManagedProductsByVendor")
    def describe_managed_products_by_vendor(
        self, context: RequestContext, vendor_name: VendorName, scope: Scope, **kwargs
    ) -> DescribeManagedProductsByVendorResponse:
        """Provides high-level information for the managed rule groups owned by a
        specific vendor.

        :param vendor_name: The name of the managed rule group vendor.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :returns: DescribeManagedProductsByVendorResponse
        :raises WAFInvalidOperationException:
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        """
        raise NotImplementedError

    @handler("DescribeManagedRuleGroup")
    def describe_managed_rule_group(
        self,
        context: RequestContext,
        vendor_name: VendorName,
        name: EntityName,
        scope: Scope,
        version_name: VersionKeyString | None = None,
        **kwargs,
    ) -> DescribeManagedRuleGroupResponse:
        """Provides high-level information for a managed rule group, including
        descriptions of the rules.

        :param vendor_name: The name of the managed rule group vendor.
        :param name: The name of the managed rule group.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param version_name: The version of the rule group.
        :returns: DescribeManagedRuleGroupResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidResourceException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        :raises WAFExpiredManagedRuleGroupVersionException:
        """
        raise NotImplementedError

    @handler("DisassociateWebACL")
    def disassociate_web_acl(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> DisassociateWebACLResponse:
        """Disassociates the specified resource from its web ACL association, if it
        has one.

        Use this for all resource types except for Amazon CloudFront
        distributions. For Amazon CloudFront, call ``UpdateDistribution`` for
        the distribution and provide an empty web ACL ID. For information, see
        `UpdateDistribution <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html>`__
        in the *Amazon CloudFront API Reference*.

        **Required permissions for customer-managed IAM policies**

        This call requires permissions that are specific to the protected
        resource type. For details, see `Permissions for
        DisassociateWebACL <https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-DisassociateWebACL>`__
        in the *WAF Developer Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to disassociate from the
        web ACL.
        :returns: DisassociateWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GenerateMobileSdkReleaseUrl")
    def generate_mobile_sdk_release_url(
        self,
        context: RequestContext,
        platform: Platform,
        release_version: VersionKeyString,
        **kwargs,
    ) -> GenerateMobileSdkReleaseUrlResponse:
        """Generates a presigned download URL for the specified release of the
        mobile SDK.

        The mobile SDK is not generally available. Customers who have access to
        the mobile SDK can use it to establish and manage WAF tokens for use in
        HTTP(S) requests from a mobile device to WAF. For more information, see
        `WAF client application
        integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
        in the *WAF Developer Guide*.

        :param platform: The device platform.
        :param release_version: The release version.
        :returns: GenerateMobileSdkReleaseUrlResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetDecryptedAPIKey")
    def get_decrypted_api_key(
        self, context: RequestContext, scope: Scope, api_key: APIKey, **kwargs
    ) -> GetDecryptedAPIKeyResponse:
        """Returns your API key in decrypted form. Use this to check the token
        domains that you have defined for the key.

        API keys are required for the integration of the CAPTCHA API in your
        JavaScript client applications. The API lets you customize the placement
        and characteristics of the CAPTCHA puzzle for your end users. For more
        information about the CAPTCHA JavaScript integration, see `WAF client
        application
        integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
        in the *WAF Developer Guide*.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param api_key: The encrypted API key.
        :returns: GetDecryptedAPIKeyResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        :raises WAFInvalidResourceException:
        """
        raise NotImplementedError

    @handler("GetIPSet")
    def get_ip_set(
        self, context: RequestContext, name: EntityName, scope: Scope, id: EntityId, **kwargs
    ) -> GetIPSetResponse:
        """Retrieves the specified IPSet.

        :param name: The name of the IP set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the set.
        :returns: GetIPSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetLoggingConfiguration")
    def get_logging_configuration(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        log_type: LogType | None = None,
        log_scope: LogScope | None = None,
        **kwargs,
    ) -> GetLoggingConfigurationResponse:
        """Returns the LoggingConfiguration for the specified web ACL.

        :param resource_arn: The Amazon Resource Name (ARN) of the web ACL for which you want to get
        the LoggingConfiguration.
        :param log_type: Used to distinguish between various logging options.
        :param log_scope: The owner of the logging configuration, which must be set to
        ``CUSTOMER`` for the configurations that you manage.
        :returns: GetLoggingConfigurationResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetManagedRuleSet")
    def get_managed_rule_set(
        self, context: RequestContext, name: EntityName, scope: Scope, id: EntityId, **kwargs
    ) -> GetManagedRuleSetResponse:
        """Retrieves the specified managed rule set.

        This is intended for use only by vendors of managed rule sets. Vendors
        are Amazon Web Services and Amazon Web Services Marketplace sellers.

        Vendors, you can use the managed rule set APIs to provide controlled
        rollout of your versioned managed rule group offerings for your
        customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
        ``PutManagedRuleSetVersions``, and
        ``UpdateManagedRuleSetVersionExpiryDate``.

        :param name: The name of the managed rule set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the managed rule set.
        :returns: GetManagedRuleSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetMobileSdkRelease")
    def get_mobile_sdk_release(
        self,
        context: RequestContext,
        platform: Platform,
        release_version: VersionKeyString,
        **kwargs,
    ) -> GetMobileSdkReleaseResponse:
        """Retrieves information for the specified mobile SDK release, including
        release notes and tags.

        The mobile SDK is not generally available. Customers who have access to
        the mobile SDK can use it to establish and manage WAF tokens for use in
        HTTP(S) requests from a mobile device to WAF. For more information, see
        `WAF client application
        integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
        in the *WAF Developer Guide*.

        :param platform: The device platform.
        :param release_version: The release version.
        :returns: GetMobileSdkReleaseResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetPermissionPolicy")
    def get_permission_policy(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> GetPermissionPolicyResponse:
        """Returns the IAM policy that is attached to the specified rule group.

        You must be the owner of the rule group to perform this operation.

        :param resource_arn: The Amazon Resource Name (ARN) of the rule group for which you want to
        get the policy.
        :returns: GetPermissionPolicyResponse
        :raises WAFNonexistentItemException:
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        """
        raise NotImplementedError

    @handler("GetRateBasedStatementManagedKeys")
    def get_rate_based_statement_managed_keys(
        self,
        context: RequestContext,
        scope: Scope,
        web_acl_name: EntityName,
        web_acl_id: EntityId,
        rule_name: EntityName,
        rule_group_rule_name: EntityName | None = None,
        **kwargs,
    ) -> GetRateBasedStatementManagedKeysResponse:
        """Retrieves the IP addresses that are currently blocked by a rate-based
        rule instance. This is only available for rate-based rules that
        aggregate solely on the IP address or on the forwarded IP address.

        The maximum number of addresses that can be blocked for a single
        rate-based rule instance is 10,000. If more than 10,000 addresses exceed
        the rate limit, those with the highest rates are blocked.

        For a rate-based rule that you've defined inside a rule group, provide
        the name of the rule group reference statement in your request, in
        addition to the rate-based rule name and the web ACL name.

        WAF monitors web requests and manages keys independently for each unique
        combination of web ACL, optional rule group, and rate-based rule. For
        example, if you define a rate-based rule inside a rule group, and then
        use the rule group in a web ACL, WAF monitors web requests and manages
        keys for that web ACL, rule group reference statement, and rate-based
        rule instance. If you use the same rule group in a second web ACL, WAF
        monitors web requests and manages keys for this second usage completely
        independent of your first.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param web_acl_name: The name of the web ACL.
        :param web_acl_id: The unique identifier for the web ACL.
        :param rule_name: The name of the rate-based rule to get the keys for.
        :param rule_group_rule_name: The name of the rule group reference statement in your web ACL.
        :returns: GetRateBasedStatementManagedKeysResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        :raises WAFUnsupportedAggregateKeyTypeException:
        """
        raise NotImplementedError

    @handler("GetRegexPatternSet")
    def get_regex_pattern_set(
        self, context: RequestContext, name: EntityName, scope: Scope, id: EntityId, **kwargs
    ) -> GetRegexPatternSetResponse:
        """Retrieves the specified RegexPatternSet.

        :param name: The name of the set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the set.
        :returns: GetRegexPatternSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetRuleGroup")
    def get_rule_group(
        self,
        context: RequestContext,
        name: EntityName | None = None,
        scope: Scope | None = None,
        id: EntityId | None = None,
        arn: ResourceArn | None = None,
        **kwargs,
    ) -> GetRuleGroupResponse:
        """Retrieves the specified RuleGroup.

        :param name: The name of the rule group.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the rule group.
        :param arn: The Amazon Resource Name (ARN) of the entity.
        :returns: GetRuleGroupResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetSampledRequests")
    def get_sampled_requests(
        self,
        context: RequestContext,
        web_acl_arn: ResourceArn,
        rule_metric_name: MetricName,
        scope: Scope,
        time_window: TimeWindow,
        max_items: ListMaxItems,
        **kwargs,
    ) -> GetSampledRequestsResponse:
        """Gets detailed information about a specified number of requests--a
        sample--that WAF randomly selects from among the first 5,000 requests
        that your Amazon Web Services resource received during a time range that
        you choose. You can specify a sample size of up to 500 requests, and you
        can specify any time range in the previous three hours.

        ``GetSampledRequests`` returns a time range, which is usually the time
        range that you specified. However, if your resource (such as a
        CloudFront distribution) received 5,000 requests before the specified
        time range elapsed, ``GetSampledRequests`` returns an updated time
        range. This new time range indicates the actual period during which WAF
        selected the requests in the sample.

        :param web_acl_arn: The Amazon resource name (ARN) of the ``WebACL`` for which you want a
        sample of requests.
        :param rule_metric_name: The metric name assigned to the ``Rule`` or ``RuleGroup`` dimension for
        which you want a sample of requests.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param time_window: The start date and time and the end date and time of the range for which
        you want ``GetSampledRequests`` to return a sample of requests.
        :param max_items: The number of requests that you want WAF to return from among the first
        5,000 requests that your Amazon Web Services resource received during
        the time range.
        :returns: GetSampledRequestsResponse
        :raises WAFNonexistentItemException:
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        """
        raise NotImplementedError

    @handler("GetWebACL")
    def get_web_acl(
        self,
        context: RequestContext,
        name: EntityName | None = None,
        scope: Scope | None = None,
        id: EntityId | None = None,
        arn: ResourceArn | None = None,
        **kwargs,
    ) -> GetWebACLResponse:
        """Retrieves the specified WebACL.

        :param name: The name of the web ACL.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: The unique identifier for the web ACL.
        :param arn: The Amazon Resource Name (ARN) of the web ACL that you want to retrieve.
        :returns: GetWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("GetWebACLForResource")
    def get_web_acl_for_resource(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> GetWebACLForResourceResponse:
        """Retrieves the WebACL for the specified resource.

        This call uses ``GetWebACL``, to verify that your account has permission
        to access the retrieved web ACL. If you get an error that indicates that
        your account isn't authorized to perform ``wafv2:GetWebACL`` on the
        resource, that error won't be included in your CloudTrail event history.

        For Amazon CloudFront, don't use this call. Instead, call the CloudFront
        action ``GetDistributionConfig``. For information, see
        `GetDistributionConfig <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistributionConfig.html>`__
        in the *Amazon CloudFront API Reference*.

        **Required permissions for customer-managed IAM policies**

        This call requires permissions that are specific to the protected
        resource type. For details, see `Permissions for
        GetWebACLForResource <https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-GetWebACLForResource>`__
        in the *WAF Developer Guide*.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource whose web ACL you want to
        retrieve.
        :returns: GetWebACLForResourceResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidParameterException:
        :raises WAFUnavailableEntityException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListAPIKeys")
    def list_api_keys(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListAPIKeysResponse:
        """Retrieves a list of the API keys that you've defined for the specified
        scope.

        API keys are required for the integration of the CAPTCHA API in your
        JavaScript client applications. The API lets you customize the placement
        and characteristics of the CAPTCHA puzzle for your end users. For more
        information about the CAPTCHA JavaScript integration, see `WAF client
        application
        integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
        in the *WAF Developer Guide*.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListAPIKeysResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        :raises WAFInvalidResourceException:
        """
        raise NotImplementedError

    @handler("ListAvailableManagedRuleGroupVersions")
    def list_available_managed_rule_group_versions(
        self,
        context: RequestContext,
        vendor_name: VendorName,
        name: EntityName,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListAvailableManagedRuleGroupVersionsResponse:
        """Returns a list of the available versions for the specified managed rule
        group.

        :param vendor_name: The name of the managed rule group vendor.
        :param name: The name of the managed rule group.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListAvailableManagedRuleGroupVersionsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListAvailableManagedRuleGroups")
    def list_available_managed_rule_groups(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListAvailableManagedRuleGroupsResponse:
        """Retrieves an array of managed rule groups that are available for you to
        use. This list includes all Amazon Web Services Managed Rules rule
        groups and all of the Amazon Web Services Marketplace managed rule
        groups that you're subscribed to.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListAvailableManagedRuleGroupsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListIPSets")
    def list_ip_sets(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListIPSetsResponse:
        """Retrieves an array of IPSetSummary objects for the IP sets that you
        manage.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListIPSetsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListLoggingConfigurations")
    def list_logging_configurations(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        log_scope: LogScope | None = None,
        **kwargs,
    ) -> ListLoggingConfigurationsResponse:
        """Retrieves an array of your LoggingConfiguration objects.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :param log_scope: The owner of the logging configuration, which must be set to
        ``CUSTOMER`` for the configurations that you manage.
        :returns: ListLoggingConfigurationsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListManagedRuleSets")
    def list_managed_rule_sets(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListManagedRuleSetsResponse:
        """Retrieves the managed rule sets that you own.

        This is intended for use only by vendors of managed rule sets. Vendors
        are Amazon Web Services and Amazon Web Services Marketplace sellers.

        Vendors, you can use the managed rule set APIs to provide controlled
        rollout of your versioned managed rule group offerings for your
        customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
        ``PutManagedRuleSetVersions``, and
        ``UpdateManagedRuleSetVersionExpiryDate``.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListManagedRuleSetsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListMobileSdkReleases")
    def list_mobile_sdk_releases(
        self,
        context: RequestContext,
        platform: Platform,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListMobileSdkReleasesResponse:
        """Retrieves a list of the available releases for the mobile SDK and the
        specified device platform.

        The mobile SDK is not generally available. Customers who have access to
        the mobile SDK can use it to establish and manage WAF tokens for use in
        HTTP(S) requests from a mobile device to WAF. For more information, see
        `WAF client application
        integration <https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html>`__
        in the *WAF Developer Guide*.

        :param platform: The device platform to retrieve the list for.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListMobileSdkReleasesResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListRegexPatternSets")
    def list_regex_pattern_sets(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListRegexPatternSetsResponse:
        """Retrieves an array of RegexPatternSetSummary objects for the regex
        pattern sets that you manage.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListRegexPatternSetsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListResourcesForWebACL")
    def list_resources_for_web_acl(
        self,
        context: RequestContext,
        web_acl_arn: ResourceArn,
        resource_type: ResourceType | None = None,
        **kwargs,
    ) -> ListResourcesForWebACLResponse:
        """Retrieves an array of the Amazon Resource Names (ARNs) for the resources
        that are associated with the specified web ACL.

        For Amazon CloudFront, don't use this call. Instead, use the CloudFront
        call ``ListDistributionsByWebACLId``. For information, see
        `ListDistributionsByWebACLId <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html>`__
        in the *Amazon CloudFront API Reference*.

        **Required permissions for customer-managed IAM policies**

        This call requires permissions that are specific to the protected
        resource type. For details, see `Permissions for
        ListResourcesForWebACL <https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-ListResourcesForWebACL>`__
        in the *WAF Developer Guide*.

        :param web_acl_arn: The Amazon Resource Name (ARN) of the web ACL.
        :param resource_type: Retrieves the web ACLs that are used by the specified resource type.
        :returns: ListResourcesForWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListRuleGroups")
    def list_rule_groups(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListRuleGroupsResponse:
        """Retrieves an array of RuleGroupSummary objects for the rule groups that
        you manage.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListRuleGroupsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListTagsForResourceResponse:
        """Retrieves the TagInfoForResource for the specified resource. Tags are
        key:value pairs that you can use to categorize and manage your
        resources, for purposes like billing. For example, you might set the tag
        key to "customer" and the value to the customer name or ID. You can
        specify one or more tags to add to each Amazon Web Services resource, up
        to 50 tags for a resource.

        You can tag the Amazon Web Services resources that you manage through
        WAF: web ACLs, rule groups, IP sets, and regex pattern sets. You can't
        manage or view tags through the WAF console.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListTagsForResourceResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("ListWebACLs")
    def list_web_ac_ls(
        self,
        context: RequestContext,
        scope: Scope,
        next_marker: NextMarker | None = None,
        limit: PaginationLimit | None = None,
        **kwargs,
    ) -> ListWebACLsResponse:
        """Retrieves an array of WebACLSummary objects for the web ACLs that you
        manage.

        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param next_marker: When you request a list of objects with a ``Limit`` setting, if the
        number of objects that are still available for retrieval exceeds the
        limit, WAF returns a ``NextMarker`` value in the response.
        :param limit: The maximum number of objects that you want WAF to return for this
        request.
        :returns: ListWebACLsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("PutLoggingConfiguration")
    def put_logging_configuration(
        self, context: RequestContext, logging_configuration: LoggingConfiguration, **kwargs
    ) -> PutLoggingConfigurationResponse:
        """Enables the specified LoggingConfiguration, to start logging from a web
        ACL, according to the configuration provided.

        If you configure data protection for the web ACL, the protection applies
        to the data that WAF sends to the logs.

        This operation completely replaces any mutable specifications that you
        already have for a logging configuration with the ones that you provide
        to this call.

        To modify an existing logging configuration, do the following:

        #. Retrieve it by calling GetLoggingConfiguration

        #. Update its settings as needed

        #. Provide the complete logging configuration specification to this call

        You can define one logging destination per web ACL.

        You can access information about the traffic that WAF inspects using the
        following steps:

        #. Create your logging destination. You can use an Amazon CloudWatch
           Logs log group, an Amazon Simple Storage Service (Amazon S3) bucket,
           or an Amazon Kinesis Data Firehose.

           The name that you give the destination must start with
           ``aws-waf-logs-``. Depending on the type of destination, you might
           need to configure additional settings or permissions.

           For configuration requirements and pricing information for each
           destination type, see `Logging web ACL
           traffic <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__
           in the *WAF Developer Guide*.

        #. Associate your logging destination to your web ACL using a
           ``PutLoggingConfiguration`` request.

        When you successfully enable logging using a ``PutLoggingConfiguration``
        request, WAF creates an additional role or policy that is required to
        write logs to the logging destination. For an Amazon CloudWatch Logs log
        group, WAF creates a resource policy on the log group. For an Amazon S3
        bucket, WAF creates a bucket policy. For an Amazon Kinesis Data
        Firehose, WAF creates a service-linked role.

        For additional information about web ACL logging, see `Logging web ACL
        traffic
        information <https://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__
        in the *WAF Developer Guide*.

        :param logging_configuration: .
        :returns: PutLoggingConfigurationResponse
        :raises WAFInternalErrorException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFServiceLinkedRoleErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidOperationException:
        :raises WAFLimitsExceededException:
        :raises WAFLogDestinationPermissionIssueException:
        """
        raise NotImplementedError

    @handler("PutManagedRuleSetVersions")
    def put_managed_rule_set_versions(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        lock_token: LockToken,
        recommended_version: VersionKeyString | None = None,
        versions_to_publish: VersionsToPublish | None = None,
        **kwargs,
    ) -> PutManagedRuleSetVersionsResponse:
        """Defines the versions of your managed rule set that you are offering to
        the customers. Customers see your offerings as managed rule groups with
        versioning.

        This is intended for use only by vendors of managed rule sets. Vendors
        are Amazon Web Services and Amazon Web Services Marketplace sellers.

        Vendors, you can use the managed rule set APIs to provide controlled
        rollout of your versioned managed rule group offerings for your
        customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
        ``PutManagedRuleSetVersions``, and
        ``UpdateManagedRuleSetVersionExpiryDate``.

        Customers retrieve their managed rule group list by calling
        ListAvailableManagedRuleGroups. The name that you provide here for your
        managed rule set is the name the customer sees for the corresponding
        managed rule group. Customers can retrieve the available versions for a
        managed rule group by calling ListAvailableManagedRuleGroupVersions. You
        provide a rule group specification for each version. For each managed
        rule set, you must specify a version that you recommend using.

        To initiate the expiration of a managed rule group version, use
        UpdateManagedRuleSetVersionExpiryDate.

        :param name: The name of the managed rule set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the managed rule set.
        :param lock_token: A token used for optimistic locking.
        :param recommended_version: The version of the named managed rule group that you'd like your
        customers to choose, from among your version offerings.
        :param versions_to_publish: The versions of the named managed rule group that you want to offer to
        your customers.
        :returns: PutManagedRuleSetVersionsResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("PutPermissionPolicy")
    def put_permission_policy(
        self, context: RequestContext, resource_arn: ResourceArn, policy: PolicyString, **kwargs
    ) -> PutPermissionPolicyResponse:
        """Use this to share a rule group with other accounts.

        This action attaches an IAM policy to the specified resource. You must
        be the owner of the rule group to perform this operation.

        This action is subject to the following restrictions:

        -  You can attach only one policy with each ``PutPermissionPolicy``
           request.

        -  The ARN in the request must be a valid WAF RuleGroup ARN and the rule
           group must exist in the same Region.

        -  The user making the request must be the owner of the rule group.

        If a rule group has been shared with your account, you can access it
        through the call ``GetRuleGroup``, and you can reference it in
        ``CreateWebACL`` and ``UpdateWebACL``. Rule groups that are shared with
        you don't appear in your WAF console rule groups listing.

        :param resource_arn: The Amazon Resource Name (ARN) of the RuleGroup to which you want to
        attach the policy.
        :param policy: The policy to attach to the specified rule group.
        :returns: PutPermissionPolicyResponse
        :raises WAFNonexistentItemException:
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFInvalidPermissionPolicyException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagList, **kwargs
    ) -> TagResourceResponse:
        """Associates tags with the specified Amazon Web Services resource. Tags
        are key:value pairs that you can use to categorize and manage your
        resources, for purposes like billing. For example, you might set the tag
        key to "customer" and the value to the customer name or ID. You can
        specify one or more tags to add to each Amazon Web Services resource, up
        to 50 tags for a resource.

        You can tag the Amazon Web Services resources that you manage through
        WAF: web ACLs, rule groups, IP sets, and regex pattern sets. You can't
        manage or view tags through the WAF console.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param tags: An array of key:value pairs to associate with the resource.
        :returns: TagResourceResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFLimitsExceededException:
        :raises WAFNonexistentItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResponse:
        """Disassociates tags from an Amazon Web Services resource. Tags are
        key:value pairs that you can associate with Amazon Web Services
        resources. For example, the tag key might be "customer" and the tag
        value might be "companyA." You can specify one or more tags to add to
        each container. You can add up to 50 tags to each Amazon Web Services
        resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param tag_keys: An array of keys identifying the tags to disassociate from the resource.
        :returns: UntagResourceResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFTagOperationException:
        :raises WAFTagOperationInternalErrorException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("UpdateIPSet")
    def update_ip_set(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        addresses: IPAddresses,
        lock_token: LockToken,
        description: EntityDescription | None = None,
        **kwargs,
    ) -> UpdateIPSetResponse:
        """Updates the specified IPSet.

        This operation completely replaces the mutable specifications that you
        already have for the IP set with the ones that you provide to this call.

        To modify an IP set, do the following:

        #. Retrieve it by calling GetIPSet

        #. Update its settings as needed

        #. Provide the complete IP set specification to this call

        **Temporary inconsistencies during updates**

        When you create or change a web ACL or other WAF resources, the changes
        take a small amount of time to propagate to all areas where the
        resources are stored. The propagation time can be from a few seconds to
        a number of minutes.

        The following are examples of the temporary inconsistencies that you
        might notice during change propagation:

        -  After you create a web ACL, if you try to associate it with a
           resource, you might get an exception indicating that the web ACL is
           unavailable.

        -  After you add a rule group to a web ACL, the new rule group rules
           might be in effect in one area where the web ACL is used and not in
           another.

        -  After you change a rule action setting, you might see the old action
           in some places and the new action in others.

        -  After you add an IP address to an IP set that is in use in a blocking
           rule, the new address might be blocked in one area while still
           allowed in another.

        :param name: The name of the IP set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the set.
        :param addresses: Contains an array of strings that specifies zero or more IP addresses or
        blocks of IP addresses that you want WAF to inspect for in incoming
        requests.
        :param lock_token: A token used for optimistic locking.
        :param description: A description of the IP set that helps with identification.
        :returns: UpdateIPSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("UpdateManagedRuleSetVersionExpiryDate")
    def update_managed_rule_set_version_expiry_date(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        lock_token: LockToken,
        version_to_expire: VersionKeyString,
        expiry_timestamp: Timestamp,
        **kwargs,
    ) -> UpdateManagedRuleSetVersionExpiryDateResponse:
        """Updates the expiration information for your managed rule set. Use this
        to initiate the expiration of a managed rule group version. After you
        initiate expiration for a version, WAF excludes it from the response to
        ListAvailableManagedRuleGroupVersions for the managed rule group.

        This is intended for use only by vendors of managed rule sets. Vendors
        are Amazon Web Services and Amazon Web Services Marketplace sellers.

        Vendors, you can use the managed rule set APIs to provide controlled
        rollout of your versioned managed rule group offerings for your
        customers. The APIs are ``ListManagedRuleSets``, ``GetManagedRuleSet``,
        ``PutManagedRuleSetVersions``, and
        ``UpdateManagedRuleSetVersionExpiryDate``.

        :param name: The name of the managed rule set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the managed rule set.
        :param lock_token: A token used for optimistic locking.
        :param version_to_expire: The version that you want to remove from your list of offerings for the
        named managed rule group.
        :param expiry_timestamp: The time that you want the version to expire.
        :returns: UpdateManagedRuleSetVersionExpiryDateResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFOptimisticLockException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("UpdateRegexPatternSet")
    def update_regex_pattern_set(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        regular_expression_list: RegularExpressionList,
        lock_token: LockToken,
        description: EntityDescription | None = None,
        **kwargs,
    ) -> UpdateRegexPatternSetResponse:
        """Updates the specified RegexPatternSet.

        This operation completely replaces the mutable specifications that you
        already have for the regex pattern set with the ones that you provide to
        this call.

        To modify a regex pattern set, do the following:

        #. Retrieve it by calling GetRegexPatternSet

        #. Update its settings as needed

        #. Provide the complete regex pattern set specification to this call

        **Temporary inconsistencies during updates**

        When you create or change a web ACL or other WAF resources, the changes
        take a small amount of time to propagate to all areas where the
        resources are stored. The propagation time can be from a few seconds to
        a number of minutes.

        The following are examples of the temporary inconsistencies that you
        might notice during change propagation:

        -  After you create a web ACL, if you try to associate it with a
           resource, you might get an exception indicating that the web ACL is
           unavailable.

        -  After you add a rule group to a web ACL, the new rule group rules
           might be in effect in one area where the web ACL is used and not in
           another.

        -  After you change a rule action setting, you might see the old action
           in some places and the new action in others.

        -  After you add an IP address to an IP set that is in use in a blocking
           rule, the new address might be blocked in one area while still
           allowed in another.

        :param name: The name of the set.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the set.
        :param regular_expression_list: .
        :param lock_token: A token used for optimistic locking.
        :param description: A description of the set that helps with identification.
        :returns: UpdateRegexPatternSetResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFInvalidOperationException:
        """
        raise NotImplementedError

    @handler("UpdateRuleGroup")
    def update_rule_group(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        visibility_config: VisibilityConfig,
        lock_token: LockToken,
        description: EntityDescription | None = None,
        rules: Rules | None = None,
        custom_response_bodies: CustomResponseBodies | None = None,
        **kwargs,
    ) -> UpdateRuleGroupResponse:
        """Updates the specified RuleGroup.

        This operation completely replaces the mutable specifications that you
        already have for the rule group with the ones that you provide to this
        call.

        To modify a rule group, do the following:

        #. Retrieve it by calling GetRuleGroup

        #. Update its settings as needed

        #. Provide the complete rule group specification to this call

        A rule group defines a collection of rules to inspect and control web
        requests that you can use in a WebACL. When you create a rule group, you
        define an immutable capacity limit. If you update a rule group, you must
        stay within the capacity. This allows others to reuse the rule group
        with confidence in its capacity requirements.

        **Temporary inconsistencies during updates**

        When you create or change a web ACL or other WAF resources, the changes
        take a small amount of time to propagate to all areas where the
        resources are stored. The propagation time can be from a few seconds to
        a number of minutes.

        The following are examples of the temporary inconsistencies that you
        might notice during change propagation:

        -  After you create a web ACL, if you try to associate it with a
           resource, you might get an exception indicating that the web ACL is
           unavailable.

        -  After you add a rule group to a web ACL, the new rule group rules
           might be in effect in one area where the web ACL is used and not in
           another.

        -  After you change a rule action setting, you might see the old action
           in some places and the new action in others.

        -  After you add an IP address to an IP set that is in use in a blocking
           rule, the new address might be blocked in one area while still
           allowed in another.

        :param name: The name of the rule group.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: A unique identifier for the rule group.
        :param visibility_config: Defines and enables Amazon CloudWatch metrics and web request sample
        collection.
        :param lock_token: A token used for optimistic locking.
        :param description: A description of the rule group that helps with identification.
        :param rules: The Rule statements used to identify the web requests that you want to
        manage.
        :param custom_response_bodies: A map of custom response keys and content bodies.
        :returns: UpdateRuleGroupResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFUnavailableEntityException:
        :raises WAFSubscriptionNotFoundException:
        :raises WAFInvalidOperationException:
        :raises WAFConfigurationWarningException:
        """
        raise NotImplementedError

    @handler("UpdateWebACL")
    def update_web_acl(
        self,
        context: RequestContext,
        name: EntityName,
        scope: Scope,
        id: EntityId,
        default_action: DefaultAction,
        visibility_config: VisibilityConfig,
        lock_token: LockToken,
        description: EntityDescription | None = None,
        rules: Rules | None = None,
        data_protection_config: DataProtectionConfig | None = None,
        custom_response_bodies: CustomResponseBodies | None = None,
        captcha_config: CaptchaConfig | None = None,
        challenge_config: ChallengeConfig | None = None,
        token_domains: TokenDomains | None = None,
        association_config: AssociationConfig | None = None,
        **kwargs,
    ) -> UpdateWebACLResponse:
        """Updates the specified WebACL. While updating a web ACL, WAF provides
        continuous coverage to the resources that you have associated with the
        web ACL.

        This operation completely replaces the mutable specifications that you
        already have for the web ACL with the ones that you provide to this
        call.

        To modify a web ACL, do the following:

        #. Retrieve it by calling GetWebACL

        #. Update its settings as needed

        #. Provide the complete web ACL specification to this call

        A web ACL defines a collection of rules to use to inspect and control
        web requests. Each rule has a statement that defines what to look for in
        web requests and an action that WAF applies to requests that match the
        statement. In the web ACL, you assign a default action to take (allow,
        block) for any request that does not match any of the rules. The rules
        in a web ACL can be a combination of the types Rule, RuleGroup, and
        managed rule group. You can associate a web ACL with one or more Amazon
        Web Services resources to protect. The resource types include Amazon
        CloudFront distribution, Amazon API Gateway REST API, Application Load
        Balancer, AppSync GraphQL API, Amazon Cognito user pool, App Runner
        service, Amplify application, and Amazon Web Services Verified Access
        instance.

        **Temporary inconsistencies during updates**

        When you create or change a web ACL or other WAF resources, the changes
        take a small amount of time to propagate to all areas where the
        resources are stored. The propagation time can be from a few seconds to
        a number of minutes.

        The following are examples of the temporary inconsistencies that you
        might notice during change propagation:

        -  After you create a web ACL, if you try to associate it with a
           resource, you might get an exception indicating that the web ACL is
           unavailable.

        -  After you add a rule group to a web ACL, the new rule group rules
           might be in effect in one area where the web ACL is used and not in
           another.

        -  After you change a rule action setting, you might see the old action
           in some places and the new action in others.

        -  After you add an IP address to an IP set that is in use in a blocking
           rule, the new address might be blocked in one area while still
           allowed in another.

        :param name: The name of the web ACL.
        :param scope: Specifies whether this is for a global resource type, such as a Amazon
        CloudFront distribution.
        :param id: The unique identifier for the web ACL.
        :param default_action: The action to perform if none of the ``Rules`` contained in the
        ``WebACL`` match.
        :param visibility_config: Defines and enables Amazon CloudWatch metrics and web request sample
        collection.
        :param lock_token: A token used for optimistic locking.
        :param description: A description of the web ACL that helps with identification.
        :param rules: The Rule statements used to identify the web requests that you want to
        manage.
        :param data_protection_config: Specifies data protection to apply to the web request data for the web
        ACL.
        :param custom_response_bodies: A map of custom response keys and content bodies.
        :param captcha_config: Specifies how WAF should handle ``CAPTCHA`` evaluations for rules that
        don't have their own ``CaptchaConfig`` settings.
        :param challenge_config: Specifies how WAF should handle challenge evaluations for rules that
        don't have their own ``ChallengeConfig`` settings.
        :param token_domains: Specifies the domains that WAF should accept in a web request token.
        :param association_config: Specifies custom configurations for the associations between the web ACL
        and protected resources.
        :returns: UpdateWebACLResponse
        :raises WAFInternalErrorException:
        :raises WAFInvalidParameterException:
        :raises WAFNonexistentItemException:
        :raises WAFDuplicateItemException:
        :raises WAFOptimisticLockException:
        :raises WAFLimitsExceededException:
        :raises WAFInvalidResourceException:
        :raises WAFUnavailableEntityException:
        :raises WAFSubscriptionNotFoundException:
        :raises WAFInvalidOperationException:
        :raises WAFExpiredManagedRuleGroupVersionException:
        :raises WAFConfigurationWarningException:
        """
        raise NotImplementedError
