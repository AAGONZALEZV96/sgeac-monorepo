from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

ActionId = str
ActionType = str
AmazonResourceName = str
Audience = str
Boolean = bool
BooleanAttribute = bool
CedarJson = str
Claim = str
ClientId = str
Decimal = str
DiscoveryUrl = str
EntityId = str
EntityIdPrefix = str
EntityType = str
GroupEntityType = str
IdempotencyToken = str
IdentitySourceId = str
IpAddr = str
Issuer = str
ListIdentitySourcesMaxResults = int
MaxResults = int
Namespace = str
NextToken = str
PolicyId = str
PolicyStatement = str
PolicyStoreDescription = str
PolicyStoreId = str
PolicyTemplateDescription = str
PolicyTemplateId = str
PrincipalEntityType = str
ResourceArn = str
SchemaJson = str
StaticPolicyDescription = str
String = str
StringAttribute = str
TagKey = str
TagValue = str
Token = str
UserPoolArn = str


class BatchGetPolicyErrorCode(StrEnum):
    POLICY_STORE_NOT_FOUND = "POLICY_STORE_NOT_FOUND"
    POLICY_NOT_FOUND = "POLICY_NOT_FOUND"


class CedarVersion(StrEnum):
    CEDAR_2 = "CEDAR_2"
    CEDAR_4 = "CEDAR_4"


class Decision(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"


class DeletionProtection(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OpenIdIssuer(StrEnum):
    COGNITO = "COGNITO"


class PolicyEffect(StrEnum):
    Permit = "Permit"
    Forbid = "Forbid"


class PolicyType(StrEnum):
    STATIC = "STATIC"
    TEMPLATE_LINKED = "TEMPLATE_LINKED"


class ResourceType(StrEnum):
    IDENTITY_SOURCE = "IDENTITY_SOURCE"
    POLICY_STORE = "POLICY_STORE"
    POLICY = "POLICY"
    POLICY_TEMPLATE = "POLICY_TEMPLATE"
    SCHEMA = "SCHEMA"


class ValidationMode(StrEnum):
    OFF = "OFF"
    STRICT = "STRICT"


class AccessDeniedException(ServiceException):
    """You don't have sufficient access to perform this action."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceConflict(TypedDict, total=False):
    """Contains information about a resource conflict."""

    resourceId: String
    resourceType: ResourceType


ResourceConflictList = List[ResourceConflict]


class ConflictException(ServiceException):
    """The request failed because another request to modify a resource occurred
    at the same.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400
    resources: ResourceConflictList


class InternalServerException(ServiceException):
    """The request failed because of an internal error. Try your request again
    later
    """

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidStateException(ServiceException):
    """The policy store can't be deleted because deletion protection is
    enabled. To delete this policy store, disable deletion protection.
    """

    code: str = "InvalidStateException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """The request failed because it references a resource that doesn't exist."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400
    resourceId: String
    resourceType: ResourceType


class ServiceQuotaExceededException(ServiceException):
    """The request failed because it would cause a service quota to be
    exceeded.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 400
    resourceId: Optional[String]
    resourceType: ResourceType
    serviceCode: Optional[String]
    quotaCode: Optional[String]


class ThrottlingException(ServiceException):
    """The request failed because it exceeded a throttling quota."""

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400
    serviceCode: Optional[String]
    quotaCode: Optional[String]


class TooManyTagsException(ServiceException):
    """No more tags be added because the limit (50) has been reached. To add
    new tags, use ``UntagResource`` to remove existing tags.
    """

    code: str = "TooManyTagsException"
    sender_fault: bool = False
    status_code: int = 400
    resourceName: Optional[AmazonResourceName]


class ValidationExceptionField(TypedDict, total=False):
    """Details about a field that failed policy validation."""

    path: String
    message: String


ValidationExceptionFieldList = List[ValidationExceptionField]


class ValidationException(ServiceException):
    """The request failed because one or more input parameters don't satisfy
    their constraint requirements. The output is provided as a list of
    fields and a reason for each field that isn't valid.

    The possible reasons include the following:

    -  **UnrecognizedEntityType**

       The policy includes an entity type that isn't found in the schema.

    -  **UnrecognizedActionId**

       The policy includes an action id that isn't found in the schema.

    -  **InvalidActionApplication**

       The policy includes an action that, according to the schema, doesn't
       support the specified principal and resource.

    -  **UnexpectedType**

       The policy included an operand that isn't a valid type for the
       specified operation.

    -  **IncompatibleTypes**

       The types of elements included in a ``set``, or the types of
       expressions used in an ``if...then...else`` clause aren't compatible
       in this context.

    -  **MissingAttribute**

       The policy attempts to access a record or entity attribute that isn't
       specified in the schema. Test for the existence of the attribute
       first before attempting to access its value. For more information,
       see the `has (presence of attribute test)
       operator <https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test>`__
       in the *Cedar Policy Language Guide*.

    -  **UnsafeOptionalAttributeAccess**

       The policy attempts to access a record or entity attribute that is
       optional and isn't guaranteed to be present. Test for the existence
       of the attribute first before attempting to access its value. For
       more information, see the `has (presence of attribute test)
       operator <https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test>`__
       in the *Cedar Policy Language Guide*.

    -  **ImpossiblePolicy**

       Cedar has determined that a policy condition always evaluates to
       false. If the policy is always false, it can never apply to any
       query, and so it can never affect an authorization decision.

    -  **WrongNumberArguments**

       The policy references an extension type with the wrong number of
       arguments.

    -  **FunctionArgumentValidationError**

       Cedar couldn't parse the argument passed to an extension type. For
       example, a string that is to be parsed as an IPv4 address can contain
       only digits and the period character.
    """

    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400
    fieldList: Optional[ValidationExceptionFieldList]


class ActionIdentifier(TypedDict, total=False):
    """Contains information about an action for a request for which an
    authorization decision is made.

    This data type is used as a request parameter to the
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__,
    `BatchIsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html>`__,
    and
    `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
    operations.

    Example: ``{ "actionId": "<action name>", "actionType": "Action" }``
    """

    actionType: ActionType
    actionId: ActionId


ActionIdentifierList = List[ActionIdentifier]


class AttributeValue(TypedDict, total=False):
    """The value of an attribute.

    Contains information about the runtime context for a request for which
    an authorization decision is made.

    This data type is used as a member of the
    `ContextDefinition <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html>`__
    structure which is uses as a request parameter for the
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__,
    `BatchIsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html>`__,
    and
    `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
    operations.
    """

    boolean: Optional["BooleanAttribute"]
    entityIdentifier: Optional["EntityIdentifier"]
    long: Optional["LongAttribute"]
    string: Optional["StringAttribute"]
    set: Optional["SetAttribute"]
    record: Optional["RecordAttribute"]
    ipaddr: Optional["IpAddr"]
    decimal: Optional["Decimal"]


RecordAttribute = Dict[String, AttributeValue]
SetAttribute = List[AttributeValue]
LongAttribute = int


class EntityIdentifier(TypedDict, total=False):
    """Contains the identifier of an entity, including its ID and type.

    This data type is used as a request parameter for
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__
    operation, and as a response parameter for the
    `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`__,
    `GetPolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html>`__,
    and
    `UpdatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html>`__
    operations.

    Example: ``{"entityId":"string","entityType":"string"}``
    """

    entityType: EntityType
    entityId: EntityId


Audiences = List[Audience]


class BatchGetPolicyErrorItem(TypedDict, total=False):
    """Contains the information about an error resulting from a
    ``BatchGetPolicy`` API call.
    """

    code: BatchGetPolicyErrorCode
    policyStoreId: String
    policyId: String
    message: String


BatchGetPolicyErrorList = List[BatchGetPolicyErrorItem]


class BatchGetPolicyInputItem(TypedDict, total=False):
    """Information about a policy that you include in a ``BatchGetPolicy`` API
    request.
    """

    policyStoreId: PolicyStoreId
    policyId: PolicyId


BatchGetPolicyInputList = List[BatchGetPolicyInputItem]


class BatchGetPolicyInput(ServiceRequest):
    requests: BatchGetPolicyInputList


TimestampFormat = datetime


class TemplateLinkedPolicyDefinitionDetail(TypedDict, total=False):
    """Contains information about a policy that was created by instantiating a
    policy template.
    """

    policyTemplateId: PolicyTemplateId
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]


class StaticPolicyDefinitionDetail(TypedDict, total=False):
    """A structure that contains details about a static policy. It includes the
    description and policy body.

    This data type is used within a
    `PolicyDefinition <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinition.html>`__
    structure as part of a request parameter for the
    `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`__
    operation.
    """

    description: Optional[StaticPolicyDescription]
    statement: PolicyStatement


class PolicyDefinitionDetail(TypedDict, total=False):
    """A structure that describes a policy definition. It must always have
    either an ``static`` or a ``templateLinked`` element.

    This data type is used as a response parameter for the
    `GetPolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html>`__
    operation.
    """

    static: Optional[StaticPolicyDefinitionDetail]
    templateLinked: Optional[TemplateLinkedPolicyDefinitionDetail]


class BatchGetPolicyOutputItem(TypedDict, total=False):
    """Contains information about a policy returned from a ``BatchGetPolicy``
    API request.
    """

    policyStoreId: PolicyStoreId
    policyId: PolicyId
    policyType: PolicyType
    definition: PolicyDefinitionDetail
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


BatchGetPolicyOutputList = List[BatchGetPolicyOutputItem]


class BatchGetPolicyOutput(TypedDict, total=False):
    results: BatchGetPolicyOutputList
    errors: BatchGetPolicyErrorList


ContextMap = Dict[String, AttributeValue]


class ContextDefinition(TypedDict, total=False):
    """Contains additional details about the context of the request. Verified
    Permissions evaluates this information in an authorization request as
    part of the ``when`` and ``unless`` clauses in a policy.

    This data type is used as a request parameter for the
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__,
    `BatchIsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html>`__,
    and
    `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
    operations.

    If you're passing context as part of the request, exactly one instance
    of ``context`` must be passed. If you don't want to pass context, omit
    the ``context`` parameter from your request rather than sending
    ``context {}``.

    Example:
    ``"context":{"contextMap":{"<KeyName1>":{"boolean":true},"<KeyName2>":{"long":1234}}}``
    """

    contextMap: Optional[ContextMap]
    cedarJson: Optional[CedarJson]


class BatchIsAuthorizedInputItem(TypedDict, total=False):
    """An authorization request that you include in a ``BatchIsAuthorized`` API
    request.
    """

    principal: Optional[EntityIdentifier]
    action: Optional[ActionIdentifier]
    resource: Optional[EntityIdentifier]
    context: Optional[ContextDefinition]


BatchIsAuthorizedInputList = List[BatchIsAuthorizedInputItem]
ParentList = List[EntityIdentifier]
EntityAttributes = Dict[String, AttributeValue]


class EntityItem(TypedDict, total=False):
    """Contains information about an entity that can be referenced in a Cedar
    policy.

    This data type is used as one of the fields in the
    `EntitiesDefinition <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html>`__
    structure.

    ``{ "identifier": { "entityType": "Photo", "entityId": "VacationPhoto94.jpg" }, "attributes": {}, "parents": [ { "entityType": "Album", "entityId": "alice_folder" } ] }``
    """

    identifier: EntityIdentifier
    attributes: Optional[EntityAttributes]
    parents: Optional[ParentList]


EntityList = List[EntityItem]


class EntitiesDefinition(TypedDict, total=False):
    """Contains the list of entities to be considered during an authorization
    request. This includes all principals, resources, and actions required
    to successfully evaluate the request.

    This data type is used as a field in the response parameter for the
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__
    and
    `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
    operations.
    """

    entityList: Optional[EntityList]
    cedarJson: Optional[CedarJson]


class BatchIsAuthorizedInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    entities: Optional[EntitiesDefinition]
    requests: BatchIsAuthorizedInputList


class EvaluationErrorItem(TypedDict, total=False):
    """Contains a description of an evaluation error.

    This data type is a response parameter of the
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__,
    `BatchIsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html>`__,
    and
    `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
    operations.
    """

    errorDescription: String


EvaluationErrorList = List[EvaluationErrorItem]


class DeterminingPolicyItem(TypedDict, total=False):
    """Contains information about one of the policies that determined an
    authorization decision.

    This data type is used as an element in a response parameter for the
    `IsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html>`__,
    `BatchIsAuthorized <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html>`__,
    and
    `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
    operations.

    Example:
    ``"determiningPolicies":[{"policyId":"SPEXAMPLEabcdefg111111"}]``
    """

    policyId: PolicyId


DeterminingPolicyList = List[DeterminingPolicyItem]


class BatchIsAuthorizedOutputItem(TypedDict, total=False):
    """The decision, based on policy evaluation, from an individual
    authorization request in a ``BatchIsAuthorized`` API request.
    """

    request: BatchIsAuthorizedInputItem
    decision: Decision
    determiningPolicies: DeterminingPolicyList
    errors: EvaluationErrorList


BatchIsAuthorizedOutputList = List[BatchIsAuthorizedOutputItem]


class BatchIsAuthorizedOutput(TypedDict, total=False):
    results: BatchIsAuthorizedOutputList


class BatchIsAuthorizedWithTokenInputItem(TypedDict, total=False):
    """An authorization request that you include in a
    ``BatchIsAuthorizedWithToken`` API request.
    """

    action: Optional[ActionIdentifier]
    resource: Optional[EntityIdentifier]
    context: Optional[ContextDefinition]


BatchIsAuthorizedWithTokenInputList = List[BatchIsAuthorizedWithTokenInputItem]


class BatchIsAuthorizedWithTokenInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    identityToken: Optional[Token]
    accessToken: Optional[Token]
    entities: Optional[EntitiesDefinition]
    requests: BatchIsAuthorizedWithTokenInputList


class BatchIsAuthorizedWithTokenOutputItem(TypedDict, total=False):
    """The decision, based on policy evaluation, from an individual
    authorization request in a ``BatchIsAuthorizedWithToken`` API request.
    """

    request: BatchIsAuthorizedWithTokenInputItem
    decision: Decision
    determiningPolicies: DeterminingPolicyList
    errors: EvaluationErrorList


BatchIsAuthorizedWithTokenOutputList = List[BatchIsAuthorizedWithTokenOutputItem]


class BatchIsAuthorizedWithTokenOutput(TypedDict, total=False):
    principal: Optional[EntityIdentifier]
    results: BatchIsAuthorizedWithTokenOutputList


ClientIds = List[ClientId]


class CognitoGroupConfiguration(TypedDict, total=False):
    """The type of entity that a policy store maps to groups from an Amazon
    Cognito user pool identity source.

    This data type is part of a
    `CognitoUserPoolConfiguration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfiguration.html>`__
    structure and is a request parameter in
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.
    """

    groupEntityType: GroupEntityType


class CognitoGroupConfigurationDetail(TypedDict, total=False):
    """The type of entity that a policy store maps to groups from an Amazon
    Cognito user pool identity source.

    This data type is part of an
    `CognitoUserPoolConfigurationDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfigurationItem.html>`__
    structure and is a response parameter to
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.
    """

    groupEntityType: Optional[GroupEntityType]


class CognitoGroupConfigurationItem(TypedDict, total=False):
    """The type of entity that a policy store maps to groups from an Amazon
    Cognito user pool identity source.

    This data type is part of an
    `CognitoUserPoolConfigurationItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfigurationDetail.html>`__
    structure and is a response parameter to
    `ListIdentitySources <http://forums.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.
    """

    groupEntityType: Optional[GroupEntityType]


class CognitoUserPoolConfiguration(TypedDict, total=False):
    """The configuration for an identity source that represents a connection to
    an Amazon Cognito user pool used as an identity provider for Verified
    Permissions.

    This data type part of a
    `Configuration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html>`__
    structure that is used as a parameter to
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.

    Example:``"CognitoUserPoolConfiguration":{"UserPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","ClientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}``
    """

    userPoolArn: UserPoolArn
    clientIds: Optional[ClientIds]
    groupConfiguration: Optional[CognitoGroupConfiguration]


class CognitoUserPoolConfigurationDetail(TypedDict, total=False):
    """The configuration for an identity source that represents a connection to
    an Amazon Cognito user pool used as an identity provider for Verified
    Permissions.

    This data type is used as a field that is part of an
    `ConfigurationDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationDetail.html>`__
    structure that is part of the response to
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.

    Example:``"CognitoUserPoolConfiguration":{"UserPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","ClientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}``
    """

    userPoolArn: UserPoolArn
    clientIds: ClientIds
    issuer: Issuer
    groupConfiguration: Optional[CognitoGroupConfigurationDetail]


class CognitoUserPoolConfigurationItem(TypedDict, total=False):
    """The configuration for an identity source that represents a connection to
    an Amazon Cognito user pool used as an identity provider for Verified
    Permissions.

    This data type is used as a field that is part of the
    `ConfigurationItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationItem.html>`__
    structure that is part of the response to
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.

    Example:``"CognitoUserPoolConfiguration":{"UserPoolArn":"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5","ClientIds": ["a1b2c3d4e5f6g7h8i9j0kalbmc"],"groupConfiguration": {"groupEntityType": "MyCorp::Group"}}``
    """

    userPoolArn: UserPoolArn
    clientIds: ClientIds
    issuer: Issuer
    groupConfiguration: Optional[CognitoGroupConfigurationItem]


class OpenIdConnectIdentityTokenConfiguration(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling identity (ID) token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `OpenIdConnectTokenSelection <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html>`__
    structure, which is a parameter of
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.
    """

    principalIdClaim: Optional[Claim]
    clientIds: Optional[ClientIds]


class OpenIdConnectAccessTokenConfiguration(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling access token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `OpenIdConnectTokenSelection <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelection.html>`__
    structure, which is a parameter of
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.
    """

    principalIdClaim: Optional[Claim]
    audiences: Optional[Audiences]


class OpenIdConnectTokenSelection(TypedDict, total=False):
    """The token type that you want to process from your OIDC identity
    provider. Your policy store can process either identity (ID) or access
    tokens from a given OIDC identity source.

    This data type is part of a
    `OpenIdConnectConfiguration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfiguration.html>`__
    structure, which is a parameter of
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.
    """

    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfiguration]
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfiguration]


class OpenIdConnectGroupConfiguration(TypedDict, total=False):
    """The claim in OIDC identity provider tokens that indicates a user's group
    membership, and the entity type that you want to map it to. For example,
    this object can map the contents of a ``groups`` claim to
    ``MyCorp::UserGroup``.

    This data type is part of a
    `OpenIdConnectConfiguration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfiguration.html>`__
    structure, which is a parameter of
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.
    """

    groupClaim: Claim
    groupEntityType: GroupEntityType


class OpenIdConnectConfiguration(TypedDict, total=False):
    """Contains configuration details of an OpenID Connect (OIDC) identity
    provider, or identity source, that Verified Permissions can use to
    generate entities from authenticated identities. It specifies the issuer
    URL, token type that you want to use, and policy store entity details.

    This data type is part of a
    `Configuration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html>`__
    structure, which is a parameter to
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__.
    """

    issuer: Issuer
    entityIdPrefix: Optional[EntityIdPrefix]
    groupConfiguration: Optional[OpenIdConnectGroupConfiguration]
    tokenSelection: OpenIdConnectTokenSelection


class Configuration(TypedDict, total=False):
    """Contains configuration information used when creating a new identity
    source.

    This data type is used as a request parameter for the
    `CreateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html>`__
    operation.
    """

    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfiguration]
    openIdConnectConfiguration: Optional[OpenIdConnectConfiguration]


class OpenIdConnectIdentityTokenConfigurationDetail(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling identity (ID) token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `OpenIdConnectTokenSelectionDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionDetail.html>`__
    structure, which is a parameter of
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.
    """

    principalIdClaim: Optional[Claim]
    clientIds: Optional[ClientIds]


class OpenIdConnectAccessTokenConfigurationDetail(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling access token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `OpenIdConnectTokenSelectionDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionDetail.html>`__
    structure, which is a parameter of
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.
    """

    principalIdClaim: Optional[Claim]
    audiences: Optional[Audiences]


class OpenIdConnectTokenSelectionDetail(TypedDict, total=False):
    """The token type that you want to process from your OIDC identity
    provider. Your policy store can process either identity (ID) or access
    tokens from a given OIDC identity source.

    This data type is part of a
    `OpenIdConnectConfigurationDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationDetail.html>`__
    structure, which is a parameter of
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.
    """

    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationDetail]
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationDetail]


class OpenIdConnectGroupConfigurationDetail(TypedDict, total=False):
    """The claim in OIDC identity provider tokens that indicates a user's group
    membership, and the entity type that you want to map it to. For example,
    this object can map the contents of a ``groups`` claim to
    ``MyCorp::UserGroup``.

    This data type is part of a
    `OpenIdConnectConfigurationDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationDetail.html>`__
    structure, which is a parameter of
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.
    """

    groupClaim: Claim
    groupEntityType: GroupEntityType


class OpenIdConnectConfigurationDetail(TypedDict, total=False):
    """Contains configuration details of an OpenID Connect (OIDC) identity
    provider, or identity source, that Verified Permissions can use to
    generate entities from authenticated identities. It specifies the issuer
    URL, token type that you want to use, and policy store entity details.

    This data type is part of a
    `ConfigurationDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationDetail.html>`__
    structure, which is a parameter to
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__.
    """

    issuer: Issuer
    entityIdPrefix: Optional[EntityIdPrefix]
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationDetail]
    tokenSelection: OpenIdConnectTokenSelectionDetail


class ConfigurationDetail(TypedDict, total=False):
    """Contains configuration information about an identity source.

    This data type is a response parameter to the
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__
    operation.
    """

    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationDetail]
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationDetail]


class OpenIdConnectIdentityTokenConfigurationItem(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling identity (ID) token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `OpenIdConnectTokenSelectionItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionItem.html>`__
    structure, which is a parameter of
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.
    """

    principalIdClaim: Optional[Claim]
    clientIds: Optional[ClientIds]


class OpenIdConnectAccessTokenConfigurationItem(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling access token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `OpenIdConnectTokenSelectionItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectTokenSelectionItem.html>`__
    structure, which is a parameter of
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.
    """

    principalIdClaim: Optional[Claim]
    audiences: Optional[Audiences]


class OpenIdConnectTokenSelectionItem(TypedDict, total=False):
    """The token type that you want to process from your OIDC identity
    provider. Your policy store can process either identity (ID) or access
    tokens from a given OIDC identity source.

    This data type is part of a
    `OpenIdConnectConfigurationItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationItem.html>`__
    structure, which is a parameter of
    `ListIdentitySources <http://amazonaws.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.
    """

    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationItem]
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationItem]


class OpenIdConnectGroupConfigurationItem(TypedDict, total=False):
    """The claim in OIDC identity provider tokens that indicates a user's group
    membership, and the entity type that you want to map it to. For example,
    this object can map the contents of a ``groups`` claim to
    ``MyCorp::UserGroup``.

    This data type is part of a
    `OpenIdConnectConfigurationItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_OpenIdConnectConfigurationItem.html>`__
    structure, which is a parameter of
    `ListIdentitySourcea <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.
    """

    groupClaim: Claim
    groupEntityType: GroupEntityType


class OpenIdConnectConfigurationItem(TypedDict, total=False):
    """Contains configuration details of an OpenID Connect (OIDC) identity
    provider, or identity source, that Verified Permissions can use to
    generate entities from authenticated identities. It specifies the issuer
    URL, token type that you want to use, and policy store entity details.

    This data type is part of a
    `ConfigurationItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationDetail.html>`__
    structure, which is a parameter to
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__.
    """

    issuer: Issuer
    entityIdPrefix: Optional[EntityIdPrefix]
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationItem]
    tokenSelection: OpenIdConnectTokenSelectionItem


class ConfigurationItem(TypedDict, total=False):
    """Contains configuration information about an identity source.

    This data type is a response parameter to the
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__
    operation.
    """

    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationItem]
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationItem]


class CreateIdentitySourceInput(ServiceRequest):
    clientToken: Optional[IdempotencyToken]
    policyStoreId: PolicyStoreId
    configuration: Configuration
    principalEntityType: Optional[PrincipalEntityType]


class CreateIdentitySourceOutput(TypedDict, total=False):
    createdDate: TimestampFormat
    identitySourceId: IdentitySourceId
    lastUpdatedDate: TimestampFormat
    policyStoreId: PolicyStoreId


class TemplateLinkedPolicyDefinition(TypedDict, total=False):
    """Contains information about a policy created by instantiating a policy
    template.
    """

    policyTemplateId: PolicyTemplateId
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]


class StaticPolicyDefinition(TypedDict, total=False):
    """Contains information about a static policy.

    This data type is used as a field that is part of the
    `PolicyDefinitionDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinitionDetail.html>`__
    type.
    """

    description: Optional[StaticPolicyDescription]
    statement: PolicyStatement


class PolicyDefinition(TypedDict, total=False):
    """A structure that contains the details for a Cedar policy definition. It
    includes the policy type, a description, and a policy body. This is a
    top level data type used to create a policy.

    This data type is used as a request parameter for the
    `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`__
    operation. This structure must always have either an ``static`` or a
    ``templateLinked`` element.
    """

    static: Optional[StaticPolicyDefinition]
    templateLinked: Optional[TemplateLinkedPolicyDefinition]


class CreatePolicyInput(ServiceRequest):
    clientToken: Optional[IdempotencyToken]
    policyStoreId: PolicyStoreId
    definition: PolicyDefinition


class CreatePolicyOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    policyId: PolicyId
    policyType: PolicyType
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]
    actions: Optional[ActionIdentifierList]
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat
    effect: Optional[PolicyEffect]


TagMap = Dict[TagKey, TagValue]


class ValidationSettings(TypedDict, total=False):
    """A structure that contains Cedar policy validation settings for the
    policy store. The validation mode determines which validation failures
    that Cedar considers serious enough to block acceptance of a new or
    edited static policy or policy template.

    This data type is used as a request parameter in the
    `CreatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html>`__
    and
    `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html>`__
    operations.
    """

    mode: ValidationMode


class CreatePolicyStoreInput(ServiceRequest):
    clientToken: Optional[IdempotencyToken]
    validationSettings: ValidationSettings
    description: Optional[PolicyStoreDescription]
    deletionProtection: Optional[DeletionProtection]
    tags: Optional[TagMap]


class CreatePolicyStoreOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    arn: ResourceArn
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


class CreatePolicyTemplateInput(ServiceRequest):
    clientToken: Optional[IdempotencyToken]
    policyStoreId: PolicyStoreId
    description: Optional[PolicyTemplateDescription]
    statement: PolicyStatement


class CreatePolicyTemplateOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


class DeleteIdentitySourceInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    identitySourceId: IdentitySourceId


class DeleteIdentitySourceOutput(TypedDict, total=False):
    pass


class DeletePolicyInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    policyId: PolicyId


class DeletePolicyOutput(TypedDict, total=False):
    pass


class DeletePolicyStoreInput(ServiceRequest):
    policyStoreId: PolicyStoreId


class DeletePolicyStoreOutput(TypedDict, total=False):
    pass


class DeletePolicyTemplateInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId


class DeletePolicyTemplateOutput(TypedDict, total=False):
    pass


class EntityReference(TypedDict, total=False):
    """Contains information about a principal or resource that can be
    referenced in a Cedar policy.

    This data type is used as part of the
    `PolicyFilter <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyFilter.html>`__
    structure that is used as a request parameter for the
    `ListPolicies <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html>`__
    operation..
    """

    unspecified: Optional[Boolean]
    identifier: Optional[EntityIdentifier]


class GetIdentitySourceInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    identitySourceId: IdentitySourceId


class IdentitySourceDetails(TypedDict, total=False):
    """A structure that contains configuration of the identity source.

    This data type was a response parameter for the
    `GetIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html>`__
    operation. Replaced by
    `ConfigurationDetail <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationDetail.html>`__.
    """

    clientIds: Optional[ClientIds]
    userPoolArn: Optional[UserPoolArn]
    discoveryUrl: Optional[DiscoveryUrl]
    openIdIssuer: Optional[OpenIdIssuer]


class GetIdentitySourceOutput(TypedDict, total=False):
    createdDate: TimestampFormat
    details: Optional[IdentitySourceDetails]
    identitySourceId: IdentitySourceId
    lastUpdatedDate: TimestampFormat
    policyStoreId: PolicyStoreId
    principalEntityType: PrincipalEntityType
    configuration: Optional[ConfigurationDetail]


class GetPolicyInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    policyId: PolicyId


class GetPolicyOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    policyId: PolicyId
    policyType: PolicyType
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]
    actions: Optional[ActionIdentifierList]
    definition: PolicyDefinitionDetail
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat
    effect: Optional[PolicyEffect]


class GetPolicyStoreInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    tags: Optional[Boolean]


class GetPolicyStoreOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    arn: ResourceArn
    validationSettings: ValidationSettings
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat
    description: Optional[PolicyStoreDescription]
    deletionProtection: Optional[DeletionProtection]
    cedarVersion: Optional[CedarVersion]
    tags: Optional[TagMap]


class GetPolicyTemplateInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId


class GetPolicyTemplateOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId
    description: Optional[PolicyTemplateDescription]
    statement: PolicyStatement
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


class GetSchemaInput(ServiceRequest):
    policyStoreId: PolicyStoreId


NamespaceList = List[Namespace]


class GetSchemaOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    schema: SchemaJson
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat
    namespaces: Optional[NamespaceList]


class IdentitySourceFilter(TypedDict, total=False):
    """A structure that defines characteristics of an identity source that you
    can use to filter.

    This data type is a request parameter for the
    `ListIdentityStores <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentityStores.html>`__
    operation.
    """

    principalEntityType: Optional[PrincipalEntityType]


IdentitySourceFilters = List[IdentitySourceFilter]


class IdentitySourceItemDetails(TypedDict, total=False):
    """A structure that contains configuration of the identity source.

    This data type was a response parameter for the
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__
    operation. Replaced by
    `ConfigurationItem <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationItem.html>`__.
    """

    clientIds: Optional[ClientIds]
    userPoolArn: Optional[UserPoolArn]
    discoveryUrl: Optional[DiscoveryUrl]
    openIdIssuer: Optional[OpenIdIssuer]


class IdentitySourceItem(TypedDict, total=False):
    """A structure that defines an identity source.

    This data type is a response parameter to the
    `ListIdentitySources <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html>`__
    operation.
    """

    createdDate: TimestampFormat
    details: Optional[IdentitySourceItemDetails]
    identitySourceId: IdentitySourceId
    lastUpdatedDate: TimestampFormat
    policyStoreId: PolicyStoreId
    principalEntityType: PrincipalEntityType
    configuration: Optional[ConfigurationItem]


IdentitySources = List[IdentitySourceItem]


class IsAuthorizedInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    principal: Optional[EntityIdentifier]
    action: Optional[ActionIdentifier]
    resource: Optional[EntityIdentifier]
    context: Optional[ContextDefinition]
    entities: Optional[EntitiesDefinition]


class IsAuthorizedOutput(TypedDict, total=False):
    decision: Decision
    determiningPolicies: DeterminingPolicyList
    errors: EvaluationErrorList


class IsAuthorizedWithTokenInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    identityToken: Optional[Token]
    accessToken: Optional[Token]
    action: Optional[ActionIdentifier]
    resource: Optional[EntityIdentifier]
    context: Optional[ContextDefinition]
    entities: Optional[EntitiesDefinition]


class IsAuthorizedWithTokenOutput(TypedDict, total=False):
    decision: Decision
    determiningPolicies: DeterminingPolicyList
    errors: EvaluationErrorList
    principal: Optional[EntityIdentifier]


class ListIdentitySourcesInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    nextToken: Optional[NextToken]
    maxResults: Optional[ListIdentitySourcesMaxResults]
    filters: Optional[IdentitySourceFilters]


class ListIdentitySourcesOutput(TypedDict, total=False):
    nextToken: Optional[NextToken]
    identitySources: IdentitySources


class PolicyFilter(TypedDict, total=False):
    """Contains information about a filter to refine policies returned in a
    query.

    This data type is used as a response parameter for the
    `ListPolicies <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html>`__
    operation.
    """

    principal: Optional[EntityReference]
    resource: Optional[EntityReference]
    policyType: Optional[PolicyType]
    policyTemplateId: Optional[PolicyTemplateId]


class ListPoliciesInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    nextToken: Optional[NextToken]
    maxResults: Optional[MaxResults]
    filter: Optional[PolicyFilter]


class TemplateLinkedPolicyDefinitionItem(TypedDict, total=False):
    """Contains information about a policy created by instantiating a policy
    template.

    This
    """

    policyTemplateId: PolicyTemplateId
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]


class StaticPolicyDefinitionItem(TypedDict, total=False):
    """A structure that contains details about a static policy. It includes the
    description and policy statement.

    This data type is used within a
    `PolicyDefinition <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinition.html>`__
    structure as part of a request parameter for the
    `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`__
    operation.
    """

    description: Optional[StaticPolicyDescription]


class PolicyDefinitionItem(TypedDict, total=False):
    """A structure that describes a
    `PolicyDefinintion <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinintion.html>`__.
    It will always have either an ``StaticPolicy`` or a
    ``TemplateLinkedPolicy`` element.

    This data type is used as a response parameter for the
    `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`__
    and
    `ListPolicies <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html>`__
    operations.
    """

    static: Optional[StaticPolicyDefinitionItem]
    templateLinked: Optional[TemplateLinkedPolicyDefinitionItem]


class PolicyItem(TypedDict, total=False):
    """Contains information about a policy.

    This data type is used as a response parameter for the
    `ListPolicies <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html>`__
    operation.
    """

    policyStoreId: PolicyStoreId
    policyId: PolicyId
    policyType: PolicyType
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]
    actions: Optional[ActionIdentifierList]
    definition: PolicyDefinitionItem
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat
    effect: Optional[PolicyEffect]


PolicyList = List[PolicyItem]


class ListPoliciesOutput(TypedDict, total=False):
    nextToken: Optional[NextToken]
    policies: PolicyList


class ListPolicyStoresInput(ServiceRequest):
    nextToken: Optional[NextToken]
    maxResults: Optional[MaxResults]


class PolicyStoreItem(TypedDict, total=False):
    """Contains information about a policy store.

    This data type is used as a response parameter for the
    `ListPolicyStores <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStores.html>`__
    operation.
    """

    policyStoreId: PolicyStoreId
    arn: ResourceArn
    createdDate: TimestampFormat
    lastUpdatedDate: Optional[TimestampFormat]
    description: Optional[PolicyStoreDescription]


PolicyStoreList = List[PolicyStoreItem]


class ListPolicyStoresOutput(TypedDict, total=False):
    nextToken: Optional[NextToken]
    policyStores: PolicyStoreList


class ListPolicyTemplatesInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    nextToken: Optional[NextToken]
    maxResults: Optional[MaxResults]


class PolicyTemplateItem(TypedDict, total=False):
    """Contains details about a policy template

    This data type is used as a response parameter for the
    `ListPolicyTemplates <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyTemplates.html>`__
    operation.
    """

    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId
    description: Optional[PolicyTemplateDescription]
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


PolicyTemplatesList = List[PolicyTemplateItem]


class ListPolicyTemplatesOutput(TypedDict, total=False):
    nextToken: Optional[NextToken]
    policyTemplates: PolicyTemplatesList


class ListTagsForResourceInput(ServiceRequest):
    resourceArn: AmazonResourceName


class ListTagsForResourceOutput(TypedDict, total=False):
    tags: Optional[TagMap]


class SchemaDefinition(TypedDict, total=False):
    """Contains a list of principal types, resource types, and actions that can
    be specified in policies stored in the same policy store. If the
    validation mode for the policy store is set to ``STRICT``, then policies
    that can't be validated by this schema are rejected by Verified
    Permissions and can't be stored in the policy store.
    """

    cedarJson: Optional[SchemaJson]


class PutSchemaInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    definition: SchemaDefinition


class PutSchemaOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    namespaces: NamespaceList
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


TagKeyList = List[TagKey]


class TagResourceInput(ServiceRequest):
    resourceArn: AmazonResourceName
    tags: TagMap


class TagResourceOutput(TypedDict, total=False):
    pass


class UntagResourceInput(ServiceRequest):
    resourceArn: AmazonResourceName
    tagKeys: TagKeyList


class UntagResourceOutput(TypedDict, total=False):
    pass


class UpdateCognitoGroupConfiguration(TypedDict, total=False):
    """The user group entities from an Amazon Cognito user pool identity
    source.
    """

    groupEntityType: GroupEntityType


class UpdateCognitoUserPoolConfiguration(TypedDict, total=False):
    """Contains configuration details of a Amazon Cognito user pool for use
    with an identity source.
    """

    userPoolArn: UserPoolArn
    clientIds: Optional[ClientIds]
    groupConfiguration: Optional[UpdateCognitoGroupConfiguration]


class UpdateOpenIdConnectIdentityTokenConfiguration(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling identity (ID) token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `UpdateOpenIdConnectTokenSelection <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectTokenSelection.html>`__
    structure, which is a parameter to
    `UpdateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html>`__.
    """

    principalIdClaim: Optional[Claim]
    clientIds: Optional[ClientIds]


class UpdateOpenIdConnectAccessTokenConfiguration(TypedDict, total=False):
    """The configuration of an OpenID Connect (OIDC) identity source for
    handling access token claims. Contains the claim that you want to
    identify as the principal in an authorization request, and the values of
    the ``aud`` claim, or audiences, that you want to accept.

    This data type is part of a
    `UpdateOpenIdConnectTokenSelection <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectTokenSelection.html>`__
    structure, which is a parameter to
    `UpdateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html>`__.
    """

    principalIdClaim: Optional[Claim]
    audiences: Optional[Audiences]


class UpdateOpenIdConnectTokenSelection(TypedDict, total=False):
    """The token type that you want to process from your OIDC identity
    provider. Your policy store can process either identity (ID) or access
    tokens from a given OIDC identity source.

    This data type is part of a
    `UpdateOpenIdConnectConfiguration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectConfiguration.html>`__
    structure, which is a parameter to
    `UpdateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html>`__.
    """

    accessTokenOnly: Optional[UpdateOpenIdConnectAccessTokenConfiguration]
    identityTokenOnly: Optional[UpdateOpenIdConnectIdentityTokenConfiguration]


class UpdateOpenIdConnectGroupConfiguration(TypedDict, total=False):
    """The claim in OIDC identity provider tokens that indicates a user's group
    membership, and the entity type that you want to map it to. For example,
    this object can map the contents of a ``groups`` claim to
    ``MyCorp::UserGroup``.

    This data type is part of a
    `UpdateOpenIdConnectConfiguration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateOpenIdConnectConfiguration.html>`__
    structure, which is a parameter to
    `UpdateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html>`__.
    """

    groupClaim: Claim
    groupEntityType: GroupEntityType


class UpdateOpenIdConnectConfiguration(TypedDict, total=False):
    """Contains configuration details of an OpenID Connect (OIDC) identity
    provider, or identity source, that Verified Permissions can use to
    generate entities from authenticated identities. It specifies the issuer
    URL, token type that you want to use, and policy store entity details.

    This data type is part of a
    `UpdateConfiguration <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateConfiguration.html>`__
    structure, which is a parameter to
    `UpdateIdentitySource <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html>`__.
    """

    issuer: Issuer
    entityIdPrefix: Optional[EntityIdPrefix]
    groupConfiguration: Optional[UpdateOpenIdConnectGroupConfiguration]
    tokenSelection: UpdateOpenIdConnectTokenSelection


class UpdateConfiguration(TypedDict, total=False):
    """Contains an update to replace the configuration in an existing identity
    source.
    """

    cognitoUserPoolConfiguration: Optional[UpdateCognitoUserPoolConfiguration]
    openIdConnectConfiguration: Optional[UpdateOpenIdConnectConfiguration]


class UpdateIdentitySourceInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    identitySourceId: IdentitySourceId
    updateConfiguration: UpdateConfiguration
    principalEntityType: Optional[PrincipalEntityType]


class UpdateIdentitySourceOutput(TypedDict, total=False):
    createdDate: TimestampFormat
    identitySourceId: IdentitySourceId
    lastUpdatedDate: TimestampFormat
    policyStoreId: PolicyStoreId


class UpdateStaticPolicyDefinition(TypedDict, total=False):
    """Contains information about an update to a static policy."""

    description: Optional[StaticPolicyDescription]
    statement: PolicyStatement


class UpdatePolicyDefinition(TypedDict, total=False):
    """Contains information about updates to be applied to a policy.

    This data type is used as a request parameter in the
    `UpdatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html>`__
    operation.
    """

    static: Optional[UpdateStaticPolicyDefinition]


class UpdatePolicyInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    policyId: PolicyId
    definition: UpdatePolicyDefinition


class UpdatePolicyOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    policyId: PolicyId
    policyType: PolicyType
    principal: Optional[EntityIdentifier]
    resource: Optional[EntityIdentifier]
    actions: Optional[ActionIdentifierList]
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat
    effect: Optional[PolicyEffect]


class UpdatePolicyStoreInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    validationSettings: ValidationSettings
    deletionProtection: Optional[DeletionProtection]
    description: Optional[PolicyStoreDescription]


class UpdatePolicyStoreOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    arn: ResourceArn
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


class UpdatePolicyTemplateInput(ServiceRequest):
    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId
    description: Optional[PolicyTemplateDescription]
    statement: PolicyStatement


class UpdatePolicyTemplateOutput(TypedDict, total=False):
    policyStoreId: PolicyStoreId
    policyTemplateId: PolicyTemplateId
    createdDate: TimestampFormat
    lastUpdatedDate: TimestampFormat


class VerifiedpermissionsApi:
    service = "verifiedpermissions"
    version = "2021-12-01"

    @handler("BatchGetPolicy")
    def batch_get_policy(
        self, context: RequestContext, requests: BatchGetPolicyInputList, **kwargs
    ) -> BatchGetPolicyOutput:
        """Retrieves information about a group (batch) of policies.

        The ``BatchGetPolicy`` operation doesn't have its own IAM permission. To
        authorize this operation for Amazon Web Services principals, include the
        permission ``verifiedpermissions:GetPolicy`` in their IAM policies.

        :param requests: An array of up to 100 policies you want information about.
        :returns: BatchGetPolicyOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("BatchIsAuthorized")
    def batch_is_authorized(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        requests: BatchIsAuthorizedInputList,
        entities: EntitiesDefinition | None = None,
        **kwargs,
    ) -> BatchIsAuthorizedOutput:
        """Makes a series of decisions about multiple authorization requests for
        one principal or resource. Each request contains the equivalent content
        of an ``IsAuthorized`` request: principal, action, resource, and
        context. Either the ``principal`` or the ``resource`` parameter must be
        identical across all requests. For example, Verified Permissions won't
        evaluate a pair of requests where ``bob`` views ``photo1`` and ``alice``
        views ``photo2``. Authorization of ``bob`` to view ``photo1`` and
        ``photo2``, or ``bob`` and ``alice`` to view ``photo1``, are valid
        batches.

        The request is evaluated against all policies in the specified policy
        store that match the entities that you declare. The result of the
        decisions is a series of ``Allow`` or ``Deny`` responses, along with the
        IDs of the policies that produced each decision.

        The ``entities`` of a ``BatchIsAuthorized`` API request can contain up
        to 100 principals and up to 100 resources. The ``requests`` of a
        ``BatchIsAuthorized`` API request can contain up to 30 requests.

        The ``BatchIsAuthorized`` operation doesn't have its own IAM permission.
        To authorize this operation for Amazon Web Services principals, include
        the permission ``verifiedpermissions:IsAuthorized`` in their IAM
        policies.

        :param policy_store_id: Specifies the ID of the policy store.
        :param requests: An array of up to 30 requests that you want Verified Permissions to
        evaluate.
        :param entities: (Optional) Specifies the list of resources and principals and their
        associated attributes that Verified Permissions can examine when
        evaluating the policies.
        :returns: BatchIsAuthorizedOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("BatchIsAuthorizedWithToken")
    def batch_is_authorized_with_token(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        requests: BatchIsAuthorizedWithTokenInputList,
        identity_token: Token | None = None,
        access_token: Token | None = None,
        entities: EntitiesDefinition | None = None,
        **kwargs,
    ) -> BatchIsAuthorizedWithTokenOutput:
        """Makes a series of decisions about multiple authorization requests for
        one token. The principal in this request comes from an external identity
        source in the form of an identity or access token, formatted as a `JSON
        web token (JWT) <https://wikipedia.org/wiki/JSON_Web_Token>`__. The
        information in the parameters can also define additional context that
        Verified Permissions can include in the evaluations.

        The request is evaluated against all policies in the specified policy
        store that match the entities that you provide in the entities
        declaration and in the token. The result of the decisions is a series of
        ``Allow`` or ``Deny`` responses, along with the IDs of the policies that
        produced each decision.

        The ``entities`` of a ``BatchIsAuthorizedWithToken`` API request can
        contain up to 100 resources and up to 99 user groups. The ``requests``
        of a ``BatchIsAuthorizedWithToken`` API request can contain up to 30
        requests.

        The ``BatchIsAuthorizedWithToken`` operation doesn't have its own IAM
        permission. To authorize this operation for Amazon Web Services
        principals, include the permission
        ``verifiedpermissions:IsAuthorizedWithToken`` in their IAM policies.

        :param policy_store_id: Specifies the ID of the policy store.
        :param requests: An array of up to 30 requests that you want Verified Permissions to
        evaluate.
        :param identity_token: Specifies an identity (ID) token for the principal that you want to
        authorize in each request.
        :param access_token: Specifies an access token for the principal that you want to authorize
        in each request.
        :param entities: (Optional) Specifies the list of resources and their associated
        attributes that Verified Permissions can examine when evaluating the
        policies.
        :returns: BatchIsAuthorizedWithTokenOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("CreateIdentitySource")
    def create_identity_source(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        configuration: Configuration,
        client_token: IdempotencyToken | None = None,
        principal_entity_type: PrincipalEntityType | None = None,
        **kwargs,
    ) -> CreateIdentitySourceOutput:
        """Adds an identity source to a policy store–an Amazon Cognito user pool or
        OpenID Connect (OIDC) identity provider (IdP).

        After you create an identity source, you can use the identities provided
        by the IdP as proxies for the principal in authorization queries that
        use the
        `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__
        or
        `BatchIsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html>`__
        API operations. These identities take the form of tokens that contain
        claims about the user, such as IDs, attributes and group memberships.
        Identity sources provide identity (ID) tokens and access tokens.
        Verified Permissions derives information about your user and session
        from token claims. Access tokens provide action ``context`` to your
        policies, and ID tokens provide principal ``Attributes``.

        Tokens from an identity source user continue to be usable until they
        expire. Token revocation and resource deletion have no effect on the
        validity of a token in your policy store

        To reference a user from this identity source in your Cedar policies,
        refer to the following syntax examples.

        -  Amazon Cognito user pool:
           ``Namespace::[Entity type]::[User pool ID]|[user principal attribute]``,
           for example
           ``MyCorp::User::us-east-1_EXAMPLE|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``.

        -  OpenID Connect (OIDC) provider:
           ``Namespace::[Entity type]::[entityIdPrefix]|[user principal attribute]``,
           for example
           ``MyCorp::User::MyOIDCProvider|a1b2c3d4-5678-90ab-cdef-EXAMPLE22222``.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ID of the policy store in which you want to store this
        identity source.
        :param configuration: Specifies the details required to communicate with the identity provider
        (IdP) associated with this identity source.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :param principal_entity_type: Specifies the namespace and data type of the principals generated for
        identities authenticated by the new identity source.
        :returns: CreateIdentitySourceOutput
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("CreatePolicy")
    def create_policy(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        definition: PolicyDefinition,
        client_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> CreatePolicyOutput:
        """Creates a Cedar policy and saves it in the specified policy store. You
        can create either a static policy or a policy linked to a policy
        template.

        -  To create a static policy, provide the Cedar policy text in the
           ``StaticPolicy`` section of the ``PolicyDefinition``.

        -  To create a policy that is dynamically linked to a policy template,
           specify the policy template ID and the principal and resource to
           associate with this policy in the ``templateLinked`` section of the
           ``PolicyDefinition``. If the policy template is ever updated, any
           policies linked to the policy template automatically use the updated
           template.

        Creating a policy causes it to be validated against the schema in the
        policy store. If the policy doesn't pass validation, the operation fails
        and the policy isn't stored.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ``PolicyStoreId`` of the policy store you want to store
        the policy in.
        :param definition: A structure that specifies the policy type and content to use for the
        new policy.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :returns: CreatePolicyOutput
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("CreatePolicyStore")
    def create_policy_store(
        self,
        context: RequestContext,
        validation_settings: ValidationSettings,
        client_token: IdempotencyToken | None = None,
        description: PolicyStoreDescription | None = None,
        deletion_protection: DeletionProtection | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreatePolicyStoreOutput:
        """Creates a policy store. A policy store is a container for policy
        resources.

        Although `Cedar supports multiple
        namespaces <https://docs.cedarpolicy.com/schema/schema.html#namespace>`__,
        Verified Permissions currently supports only one namespace per policy
        store.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param validation_settings: Specifies the validation setting for this policy store.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :param description: Descriptive text that you can provide to help with identification of the
        current policy store.
        :param deletion_protection: Specifies whether the policy store can be deleted.
        :param tags: The list of key-value pairs to associate with the policy store.
        :returns: CreatePolicyStoreOutput
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("CreatePolicyTemplate")
    def create_policy_template(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        statement: PolicyStatement,
        client_token: IdempotencyToken | None = None,
        description: PolicyTemplateDescription | None = None,
        **kwargs,
    ) -> CreatePolicyTemplateOutput:
        """Creates a policy template. A template can use placeholders for the
        principal and resource. A template must be instantiated into a policy by
        associating it with specific principals and resources to use for the
        placeholders. That instantiated policy can then be considered in
        authorization decisions. The instantiated policy works identically to
        any other policy, except that it is dynamically linked to the template.
        If the template changes, then any policies that are linked to that
        template are immediately updated as well.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: The ID of the policy store in which to create the policy template.
        :param statement: Specifies the content that you want to use for the new policy template,
        written in the Cedar policy language.
        :param client_token: Specifies a unique, case-sensitive ID that you provide to ensure the
        idempotency of the request.
        :param description: Specifies a description for the policy template.
        :returns: CreatePolicyTemplateOutput
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DeleteIdentitySource")
    def delete_identity_source(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        identity_source_id: IdentitySourceId,
        **kwargs,
    ) -> DeleteIdentitySourceOutput:
        """Deletes an identity source that references an identity provider (IdP)
        such as Amazon Cognito. After you delete the identity source, you can no
        longer use tokens for identities from that identity source to represent
        principals in authorization queries made using
        `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`__.
        operations.

        :param policy_store_id: Specifies the ID of the policy store that contains the identity source
        that you want to delete.
        :param identity_source_id: Specifies the ID of the identity source that you want to delete.
        :returns: DeleteIdentitySourceOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DeletePolicy")
    def delete_policy(
        self, context: RequestContext, policy_store_id: PolicyStoreId, policy_id: PolicyId, **kwargs
    ) -> DeletePolicyOutput:
        """Deletes the specified policy from the policy store.

        This operation is idempotent; if you specify a policy that doesn't
        exist, the request response returns a successful ``HTTP 200`` status
        code.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy that you
        want to delete.
        :param policy_id: Specifies the ID of the policy that you want to delete.
        :returns: DeletePolicyOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DeletePolicyStore")
    def delete_policy_store(
        self, context: RequestContext, policy_store_id: PolicyStoreId, **kwargs
    ) -> DeletePolicyStoreOutput:
        """Deletes the specified policy store.

        This operation is idempotent. If you specify a policy store that does
        not exist, the request response will still return a successful HTTP 200
        status code.

        :param policy_store_id: Specifies the ID of the policy store that you want to delete.
        :returns: DeletePolicyStoreOutput
        :raises ValidationException:
        :raises InvalidStateException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DeletePolicyTemplate")
    def delete_policy_template(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        policy_template_id: PolicyTemplateId,
        **kwargs,
    ) -> DeletePolicyTemplateOutput:
        """Deletes the specified policy template from the policy store.

        This operation also deletes any policies that were created from the
        specified policy template. Those policies are immediately removed from
        all future API responses, and are asynchronously deleted from the policy
        store.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy template
        that you want to delete.
        :param policy_template_id: Specifies the ID of the policy template that you want to delete.
        :returns: DeletePolicyTemplateOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetIdentitySource")
    def get_identity_source(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        identity_source_id: IdentitySourceId,
        **kwargs,
    ) -> GetIdentitySourceOutput:
        """Retrieves the details about the specified identity source.

        :param policy_store_id: Specifies the ID of the policy store that contains the identity source
        you want information about.
        :param identity_source_id: Specifies the ID of the identity source you want information about.
        :returns: GetIdentitySourceOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetPolicy")
    def get_policy(
        self, context: RequestContext, policy_store_id: PolicyStoreId, policy_id: PolicyId, **kwargs
    ) -> GetPolicyOutput:
        """Retrieves information about the specified policy.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy that you
        want information about.
        :param policy_id: Specifies the ID of the policy you want information about.
        :returns: GetPolicyOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetPolicyStore")
    def get_policy_store(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        tags: Boolean | None = None,
        **kwargs,
    ) -> GetPolicyStoreOutput:
        """Retrieves details about a policy store.

        :param policy_store_id: Specifies the ID of the policy store that you want information about.
        :param tags: Specifies whether to return the tags that are attached to the policy
        store.
        :returns: GetPolicyStoreOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetPolicyTemplate")
    def get_policy_template(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        policy_template_id: PolicyTemplateId,
        **kwargs,
    ) -> GetPolicyTemplateOutput:
        """Retrieve the details for the specified policy template in the specified
        policy store.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy template
        that you want information about.
        :param policy_template_id: Specifies the ID of the policy template that you want information about.
        :returns: GetPolicyTemplateOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetSchema")
    def get_schema(
        self, context: RequestContext, policy_store_id: PolicyStoreId, **kwargs
    ) -> GetSchemaOutput:
        """Retrieve the details for the specified schema in the specified policy
        store.

        :param policy_store_id: Specifies the ID of the policy store that contains the schema.
        :returns: GetSchemaOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("IsAuthorized", expand=False)
    def is_authorized(
        self, context: RequestContext, request: IsAuthorizedInput, **kwargs
    ) -> IsAuthorizedOutput:
        """Makes an authorization decision about a service request described in the
        parameters. The information in the parameters can also define additional
        context that Verified Permissions can include in the evaluation. The
        request is evaluated against all matching policies in the specified
        policy store. The result of the decision is either ``Allow`` or
        ``Deny``, along with a list of the policies that resulted in the
        decision.

        :param policy_store_id: Specifies the ID of the policy store.
        :param principal: Specifies the principal for which the authorization decision is to be
        made.
        :param action: Specifies the requested action to be authorized.
        :param resource: Specifies the resource for which the authorization decision is to be
        made.
        :param context: Specifies additional context that can be used to make more granular
        authorization decisions.
        :param entities: (Optional) Specifies the list of resources and principals and their
        associated attributes that Verified Permissions can examine when
        evaluating the policies.
        :returns: IsAuthorizedOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("IsAuthorizedWithToken", expand=False)
    def is_authorized_with_token(
        self, context: RequestContext, request: IsAuthorizedWithTokenInput, **kwargs
    ) -> IsAuthorizedWithTokenOutput:
        """Makes an authorization decision about a service request described in the
        parameters. The principal in this request comes from an external
        identity source in the form of an identity token formatted as a `JSON
        web token (JWT) <https://wikipedia.org/wiki/JSON_Web_Token>`__. The
        information in the parameters can also define additional context that
        Verified Permissions can include in the evaluation. The request is
        evaluated against all matching policies in the specified policy store.
        The result of the decision is either ``Allow`` or ``Deny``, along with a
        list of the policies that resulted in the decision.

        Verified Permissions validates each token that is specified in a request
        by checking its expiration date and its signature.

        Tokens from an identity source user continue to be usable until they
        expire. Token revocation and resource deletion have no effect on the
        validity of a token in your policy store

        :param policy_store_id: Specifies the ID of the policy store.
        :param identity_token: Specifies an identity token for the principal to be authorized.
        :param access_token: Specifies an access token for the principal to be authorized.
        :param action: Specifies the requested action to be authorized.
        :param resource: Specifies the resource for which the authorization decision is made.
        :param context: Specifies additional context that can be used to make more granular
        authorization decisions.
        :param entities: (Optional) Specifies the list of resources and their associated
        attributes that Verified Permissions can examine when evaluating the
        policies.
        :returns: IsAuthorizedWithTokenOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListIdentitySources")
    def list_identity_sources(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        next_token: NextToken | None = None,
        max_results: ListIdentitySourcesMaxResults | None = None,
        filters: IdentitySourceFilters | None = None,
        **kwargs,
    ) -> ListIdentitySourcesOutput:
        """Returns a paginated list of all of the identity sources defined in the
        specified policy store.

        :param policy_store_id: Specifies the ID of the policy store that contains the identity sources
        that you want to list.
        :param next_token: Specifies that you want to receive the next page of results.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param filters: Specifies characteristics of an identity source that you can use to
        limit the output to matching identity sources.
        :returns: ListIdentitySourcesOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListPolicies")
    def list_policies(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        filter: PolicyFilter | None = None,
        **kwargs,
    ) -> ListPoliciesOutput:
        """Returns a paginated list of all policies stored in the specified policy
        store.

        :param policy_store_id: Specifies the ID of the policy store you want to list policies from.
        :param next_token: Specifies that you want to receive the next page of results.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :param filter: Specifies a filter that limits the response to only policies that match
        the specified criteria.
        :returns: ListPoliciesOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListPolicyStores")
    def list_policy_stores(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListPolicyStoresOutput:
        """Returns a paginated list of all policy stores in the calling Amazon Web
        Services account.

        :param next_token: Specifies that you want to receive the next page of results.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :returns: ListPolicyStoresOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListPolicyTemplates")
    def list_policy_templates(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListPolicyTemplatesOutput:
        """Returns a paginated list of all policy templates in the specified policy
        store.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy templates
        you want to list.
        :param next_token: Specifies that you want to receive the next page of results.
        :param max_results: Specifies the total number of results that you want included in each
        response.
        :returns: ListPolicyTemplatesOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, **kwargs
    ) -> ListTagsForResourceOutput:
        """Returns the tags associated with the specified Amazon Verified
        Permissions resource. In Verified Permissions, policy stores can be
        tagged.

        :param resource_arn: The ARN of the resource for which you want to view tags.
        :returns: ListTagsForResourceOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("PutSchema")
    def put_schema(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        definition: SchemaDefinition,
        **kwargs,
    ) -> PutSchemaOutput:
        """Creates or updates the policy schema in the specified policy store. The
        schema is used to validate any Cedar policies and policy templates
        submitted to the policy store. Any changes to the schema validate only
        policies and templates submitted after the schema change. Existing
        policies and templates are not re-evaluated against the changed schema.
        If you later update a policy, then it is evaluated against the new
        schema at that time.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ID of the policy store in which to place the schema.
        :param definition: Specifies the definition of the schema to be stored.
        :returns: PutSchemaOutput
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, tags: TagMap, **kwargs
    ) -> TagResourceOutput:
        """Assigns one or more tags (key-value pairs) to the specified Amazon
        Verified Permissions resource. Tags can help you organize and categorize
        your resources. You can also use them to scope user permissions by
        granting a user permission to access or change only resources with
        certain tag values. In Verified Permissions, policy stores can be
        tagged.

        Tags don't have any semantic meaning to Amazon Web Services and are
        interpreted strictly as strings of characters.

        You can use the TagResource action with a resource that already has
        tags. If you specify a new tag key, this tag is appended to the list of
        tags associated with the resource. If you specify a tag key that is
        already associated with the resource, the new tag value that you specify
        replaces the previous value for that tag.

        You can associate as many as 50 tags with a resource.

        :param resource_arn: The ARN of the resource that you're adding tags to.
        :param tags: The list of key-value pairs to associate with the resource.
        :returns: TagResourceOutput
        :raises ValidationException:
        :raises TooManyTagsException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
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
        """Removes one or more tags from the specified Amazon Verified Permissions
        resource. In Verified Permissions, policy stores can be tagged.

        :param resource_arn: The ARN of the resource from which you are removing tags.
        :param tag_keys: The list of tag keys to remove from the resource.
        :returns: UntagResourceOutput
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("UpdateIdentitySource")
    def update_identity_source(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        identity_source_id: IdentitySourceId,
        update_configuration: UpdateConfiguration,
        principal_entity_type: PrincipalEntityType | None = None,
        **kwargs,
    ) -> UpdateIdentitySourceOutput:
        """Updates the specified identity source to use a new identity provider
        (IdP), or to change the mapping of identities from the IdP to a
        different principal entity type.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ID of the policy store that contains the identity source
        that you want to update.
        :param identity_source_id: Specifies the ID of the identity source that you want to update.
        :param update_configuration: Specifies the details required to communicate with the identity provider
        (IdP) associated with this identity source.
        :param principal_entity_type: Specifies the data type of principals generated for identities
        authenticated by the identity source.
        :returns: UpdateIdentitySourceOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("UpdatePolicy")
    def update_policy(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        policy_id: PolicyId,
        definition: UpdatePolicyDefinition,
        **kwargs,
    ) -> UpdatePolicyOutput:
        """Modifies a Cedar static policy in the specified policy store. You can
        change only certain elements of the
        `UpdatePolicyDefinition <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyInput.html#amazonverifiedpermissions-UpdatePolicy-request-UpdatePolicyDefinition>`__
        parameter. You can directly update only static policies. To change a
        template-linked policy, you must update the template instead, using
        `UpdatePolicyTemplate <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html>`__.

        -  If policy validation is enabled in the policy store, then updating a
           static policy causes Verified Permissions to validate the policy
           against the schema in the policy store. If the updated static policy
           doesn't pass validation, the operation fails and the update isn't
           stored.

        -  When you edit a static policy, you can change only certain elements
           of a static policy:

           -  The action referenced by the policy.

           -  A condition clause, such as when and unless.

           You can't change these elements of a static policy:

           -  Changing a policy from a static policy to a template-linked
              policy.

           -  Changing the effect of a static policy from permit or forbid.

           -  The principal referenced by a static policy.

           -  The resource referenced by a static policy.

        -  To update a template-linked policy, you must update the template
           instead.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy that you
        want to update.
        :param policy_id: Specifies the ID of the policy that you want to update.
        :param definition: Specifies the updated policy content that you want to replace on the
        specified policy.
        :returns: UpdatePolicyOutput
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("UpdatePolicyStore")
    def update_policy_store(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        validation_settings: ValidationSettings,
        deletion_protection: DeletionProtection | None = None,
        description: PolicyStoreDescription | None = None,
        **kwargs,
    ) -> UpdatePolicyStoreOutput:
        """Modifies the validation setting for a policy store.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ID of the policy store that you want to update.
        :param validation_settings: A structure that defines the validation settings that want to enable for
        the policy store.
        :param deletion_protection: Specifies whether the policy store can be deleted.
        :param description: Descriptive text that you can provide to help with identification of the
        current policy store.
        :returns: UpdatePolicyStoreOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("UpdatePolicyTemplate")
    def update_policy_template(
        self,
        context: RequestContext,
        policy_store_id: PolicyStoreId,
        policy_template_id: PolicyTemplateId,
        statement: PolicyStatement,
        description: PolicyTemplateDescription | None = None,
        **kwargs,
    ) -> UpdatePolicyTemplateOutput:
        """Updates the specified policy template. You can update only the
        description and the some elements of the
        `policyBody <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html#amazonverifiedpermissions-UpdatePolicyTemplate-request-policyBody>`__.

        Changes you make to the policy template content are immediately (within
        the constraints of eventual consistency) reflected in authorization
        decisions that involve all template-linked policies instantiated from
        this template.

        Verified Permissions is `eventually
        consistent <https://wikipedia.org/wiki/Eventual_consistency>`__ . It can
        take a few seconds for a new or changed element to propagate through the
        service and be visible in the results of other Verified Permissions
        operations.

        :param policy_store_id: Specifies the ID of the policy store that contains the policy template
        that you want to update.
        :param policy_template_id: Specifies the ID of the policy template that you want to update.
        :param statement: Specifies new statement content written in Cedar policy language to
        replace the current body of the policy template.
        :param description: Specifies a new description to apply to the policy template.
        :returns: UpdatePolicyTemplateOutput
        :raises ValidationException:
        :raises ConflictException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        """
        raise NotImplementedError
