from datetime import datetime
from enum import StrEnum
from typing import IO, Dict, Iterable, List, Optional, TypedDict, Union

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

ApiName = str
Boolean = bool
BooleanValue = bool
CertificateArn = str
Code = str
CodeErrorColumn = int
CodeErrorLine = int
CodeErrorSpan = int
Context = str
Description = str
DomainName = str
EnvironmentVariableKey = str
EnvironmentVariableValue = str
ErrorMessage = str
EvaluationResult = str
MappingTemplate = str
MaxBatchSize = int
MaxResults = int
Namespace = str
OutErrors = str
OwnerContact = str
PaginationToken = str
QueryDepthLimit = int
RdsDataApiConfigDatabaseName = str
RdsDataApiConfigResourceArn = str
RdsDataApiConfigSecretArn = str
ResolverCountLimit = int
ResourceArn = str
ResourceName = str
Stash = str
String = str
TTL = int
TagKey = str
TagValue = str
Template = str


class ApiCacheStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    CREATING = "CREATING"
    DELETING = "DELETING"
    MODIFYING = "MODIFYING"
    FAILED = "FAILED"


class ApiCacheType(StrEnum):
    T2_SMALL = "T2_SMALL"
    T2_MEDIUM = "T2_MEDIUM"
    R4_LARGE = "R4_LARGE"
    R4_XLARGE = "R4_XLARGE"
    R4_2XLARGE = "R4_2XLARGE"
    R4_4XLARGE = "R4_4XLARGE"
    R4_8XLARGE = "R4_8XLARGE"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"
    LARGE_2X = "LARGE_2X"
    LARGE_4X = "LARGE_4X"
    LARGE_8X = "LARGE_8X"
    LARGE_12X = "LARGE_12X"


class ApiCachingBehavior(StrEnum):
    FULL_REQUEST_CACHING = "FULL_REQUEST_CACHING"
    PER_RESOLVER_CACHING = "PER_RESOLVER_CACHING"
    OPERATION_LEVEL_CACHING = "OPERATION_LEVEL_CACHING"


class AssociationStatus(StrEnum):
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class AuthenticationType(StrEnum):
    API_KEY = "API_KEY"
    AWS_IAM = "AWS_IAM"
    AMAZON_COGNITO_USER_POOLS = "AMAZON_COGNITO_USER_POOLS"
    OPENID_CONNECT = "OPENID_CONNECT"
    AWS_LAMBDA = "AWS_LAMBDA"


class AuthorizationType(StrEnum):
    AWS_IAM = "AWS_IAM"


class BadRequestReason(StrEnum):
    CODE_ERROR = "CODE_ERROR"


class CacheHealthMetricsConfig(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ConflictDetectionType(StrEnum):
    VERSION = "VERSION"
    NONE = "NONE"


class ConflictHandlerType(StrEnum):
    OPTIMISTIC_CONCURRENCY = "OPTIMISTIC_CONCURRENCY"
    LAMBDA = "LAMBDA"
    AUTOMERGE = "AUTOMERGE"
    NONE = "NONE"


class DataSourceIntrospectionStatus(StrEnum):
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class DataSourceLevelMetricsBehavior(StrEnum):
    FULL_REQUEST_DATA_SOURCE_METRICS = "FULL_REQUEST_DATA_SOURCE_METRICS"
    PER_DATA_SOURCE_METRICS = "PER_DATA_SOURCE_METRICS"


class DataSourceLevelMetricsConfig(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DataSourceType(StrEnum):
    AWS_LAMBDA = "AWS_LAMBDA"
    AMAZON_DYNAMODB = "AMAZON_DYNAMODB"
    AMAZON_ELASTICSEARCH = "AMAZON_ELASTICSEARCH"
    NONE = "NONE"
    HTTP = "HTTP"
    RELATIONAL_DATABASE = "RELATIONAL_DATABASE"
    AMAZON_OPENSEARCH_SERVICE = "AMAZON_OPENSEARCH_SERVICE"
    AMAZON_EVENTBRIDGE = "AMAZON_EVENTBRIDGE"
    AMAZON_BEDROCK_RUNTIME = "AMAZON_BEDROCK_RUNTIME"


class DefaultAction(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"


class EventLogLevel(StrEnum):
    NONE = "NONE"
    ERROR = "ERROR"
    ALL = "ALL"
    INFO = "INFO"
    DEBUG = "DEBUG"


class FieldLogLevel(StrEnum):
    NONE = "NONE"
    ERROR = "ERROR"
    ALL = "ALL"
    INFO = "INFO"
    DEBUG = "DEBUG"


class GraphQLApiIntrospectionConfig(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class GraphQLApiType(StrEnum):
    GRAPHQL = "GRAPHQL"
    MERGED = "MERGED"


class GraphQLApiVisibility(StrEnum):
    GLOBAL = "GLOBAL"
    PRIVATE = "PRIVATE"


class HandlerBehavior(StrEnum):
    CODE = "CODE"
    DIRECT = "DIRECT"


class InvokeType(StrEnum):
    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    EVENT = "EVENT"


class MergeType(StrEnum):
    MANUAL_MERGE = "MANUAL_MERGE"
    AUTO_MERGE = "AUTO_MERGE"


class OperationLevelMetricsConfig(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class OutputType(StrEnum):
    SDL = "SDL"
    JSON = "JSON"


class Ownership(StrEnum):
    CURRENT_ACCOUNT = "CURRENT_ACCOUNT"
    OTHER_ACCOUNTS = "OTHER_ACCOUNTS"


class RelationalDatabaseSourceType(StrEnum):
    RDS_HTTP_ENDPOINT = "RDS_HTTP_ENDPOINT"


class ResolverKind(StrEnum):
    UNIT = "UNIT"
    PIPELINE = "PIPELINE"


class ResolverLevelMetricsBehavior(StrEnum):
    FULL_REQUEST_RESOLVER_METRICS = "FULL_REQUEST_RESOLVER_METRICS"
    PER_RESOLVER_METRICS = "PER_RESOLVER_METRICS"


class ResolverLevelMetricsConfig(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RuntimeName(StrEnum):
    APPSYNC_JS = "APPSYNC_JS"


class SchemaStatus(StrEnum):
    PROCESSING = "PROCESSING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class SourceApiAssociationStatus(StrEnum):
    MERGE_SCHEDULED = "MERGE_SCHEDULED"
    MERGE_FAILED = "MERGE_FAILED"
    MERGE_SUCCESS = "MERGE_SUCCESS"
    MERGE_IN_PROGRESS = "MERGE_IN_PROGRESS"
    AUTO_MERGE_SCHEDULE_FAILED = "AUTO_MERGE_SCHEDULE_FAILED"
    DELETION_SCHEDULED = "DELETION_SCHEDULED"
    DELETION_IN_PROGRESS = "DELETION_IN_PROGRESS"
    DELETION_FAILED = "DELETION_FAILED"


class TypeDefinitionFormat(StrEnum):
    SDL = "SDL"
    JSON = "JSON"


class AccessDeniedException(ServiceException):
    """You don't have access to perform this operation on this resource."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 403


class ApiKeyLimitExceededException(ServiceException):
    """The API key exceeded a limit. Try your request again."""

    code: str = "ApiKeyLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ApiKeyValidityOutOfBoundsException(ServiceException):
    """The API key expiration must be set to a value between 1 and 365 days
    from creation (for ``CreateApiKey``) or from update (for
    ``UpdateApiKey``).
    """

    code: str = "ApiKeyValidityOutOfBoundsException"
    sender_fault: bool = False
    status_code: int = 400


class ApiLimitExceededException(ServiceException):
    """The GraphQL API exceeded a limit. Try your request again."""

    code: str = "ApiLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class CodeErrorLocation(TypedDict, total=False):
    """Describes the location of the error in a code sample."""

    line: Optional[CodeErrorLine]
    column: Optional[CodeErrorColumn]
    span: Optional[CodeErrorSpan]


class CodeError(TypedDict, total=False):
    """Describes an AppSync error."""

    errorType: Optional[String]
    value: Optional[String]
    location: Optional[CodeErrorLocation]


CodeErrors = List[CodeError]


class BadRequestDetail(TypedDict, total=False):
    """Provides further details for the reason behind the bad request. For
    reason type ``CODE_ERROR``, the detail will contain a list of code
    errors.
    """

    codeErrors: Optional[CodeErrors]


class BadRequestException(ServiceException):
    """The request is not well formed. For example, a value is invalid or a
    required field is missing. Check the field values, and then try again.
    """

    code: str = "BadRequestException"
    sender_fault: bool = False
    status_code: int = 400
    reason: Optional[BadRequestReason]
    detail: Optional[BadRequestDetail]


class ConcurrentModificationException(ServiceException):
    """Another modification is in progress at this time and it must complete
    before you can make your change.
    """

    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 409


class ConflictException(ServiceException):
    """A conflict with a previous successful update is detected. This typically
    occurs when the previous update did not have time to propagate before
    the next update was made. A retry (with appropriate backoff logic) is
    the recommended response to this exception.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 409


class GraphQLSchemaException(ServiceException):
    """The GraphQL schema is not valid."""

    code: str = "GraphQLSchemaException"
    sender_fault: bool = False
    status_code: int = 400


class InternalFailureException(ServiceException):
    """An internal AppSync error occurred. Try your request again."""

    code: str = "InternalFailureException"
    sender_fault: bool = False
    status_code: int = 500


class LimitExceededException(ServiceException):
    """The request exceeded a limit. Try your request again."""

    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 429


class NotFoundException(ServiceException):
    """The resource specified in the request was not found. Check the resource,
    and then try again.
    """

    code: str = "NotFoundException"
    sender_fault: bool = False
    status_code: int = 404


class ServiceQuotaExceededException(ServiceException):
    """The operation exceeded the service quota for this resource."""

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 402


class UnauthorizedException(ServiceException):
    """You aren't authorized to perform this operation."""

    code: str = "UnauthorizedException"
    sender_fault: bool = False
    status_code: int = 401


class LambdaAuthorizerConfig(TypedDict, total=False):
    """A ``LambdaAuthorizerConfig`` specifies how to authorize AppSync API
    access when using the ``AWS_LAMBDA`` authorizer mode. Be aware that an
    AppSync API can have only one Lambda authorizer configured at a time.
    """

    authorizerResultTtlInSeconds: Optional[TTL]
    authorizerUri: String
    identityValidationExpression: Optional[String]


class CognitoUserPoolConfig(TypedDict, total=False):
    """Describes an Amazon Cognito user pool configuration."""

    userPoolId: String
    awsRegion: String
    appIdClientRegex: Optional[String]


Long = int


class OpenIDConnectConfig(TypedDict, total=False):
    """Describes an OpenID Connect (OIDC) configuration."""

    issuer: String
    clientId: Optional[String]
    iatTTL: Optional[Long]
    authTTL: Optional[Long]


class AdditionalAuthenticationProvider(TypedDict, total=False):
    """Describes an additional authentication provider."""

    authenticationType: Optional[AuthenticationType]
    openIDConnectConfig: Optional[OpenIDConnectConfig]
    userPoolConfig: Optional[CognitoUserPoolConfig]
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig]


AdditionalAuthenticationProviders = List[AdditionalAuthenticationProvider]


class EventLogConfig(TypedDict, total=False):
    """Describes the CloudWatch Logs configuration for the Event API."""

    logLevel: EventLogLevel
    cloudWatchLogsRoleArn: String


class AuthMode(TypedDict, total=False):
    """Describes an authorization configuration. Use ``AuthMode`` to specify
    the publishing and subscription authorization configuration for an Event
    API.
    """

    authType: AuthenticationType


AuthModes = List[AuthMode]


class CognitoConfig(TypedDict, total=False):
    """Describes an Amazon Cognito configuration."""

    userPoolId: String
    awsRegion: String
    appIdClientRegex: Optional[String]


class AuthProvider(TypedDict, total=False):
    """Describes an authorization provider."""

    authType: AuthenticationType
    cognitoConfig: Optional[CognitoConfig]
    openIDConnectConfig: Optional[OpenIDConnectConfig]
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig]


AuthProviders = List[AuthProvider]


class EventConfig(TypedDict, total=False):
    """Describes the authorization configuration for connections, message
    publishing, message subscriptions, and logging for an Event API.
    """

    authProviders: AuthProviders
    connectionAuthModes: AuthModes
    defaultPublishAuthModes: AuthModes
    defaultSubscribeAuthModes: AuthModes
    logConfig: Optional[EventLogConfig]


Timestamp = datetime
MapOfStringToString = Dict[String, String]
TagMap = Dict[TagKey, TagValue]


class Api(TypedDict, total=False):
    """Describes an AppSync API. You can use ``Api`` for an AppSync API with
    your preferred configuration, such as an Event API that provides
    real-time message publishing and message subscriptions over WebSockets.
    """

    apiId: Optional[String]
    name: Optional[ApiName]
    ownerContact: Optional[OwnerContact]
    tags: Optional[TagMap]
    dns: Optional[MapOfStringToString]
    apiArn: Optional[String]
    created: Optional[Timestamp]
    xrayEnabled: Optional[Boolean]
    wafWebAclArn: Optional[String]
    eventConfig: Optional[EventConfig]


class ApiAssociation(TypedDict, total=False):
    """Describes an ``ApiAssociation`` object."""

    domainName: Optional[DomainName]
    apiId: Optional[String]
    associationStatus: Optional[AssociationStatus]
    deploymentDetail: Optional[String]


ApiCache = TypedDict(
    "ApiCache",
    {
        "ttl": Optional[Long],
        "apiCachingBehavior": Optional[ApiCachingBehavior],
        "transitEncryptionEnabled": Optional[Boolean],
        "atRestEncryptionEnabled": Optional[Boolean],
        "type": Optional[ApiCacheType],
        "status": Optional[ApiCacheStatus],
        "healthMetricsConfig": Optional[CacheHealthMetricsConfig],
    },
    total=False,
)


class ApiKey(TypedDict, total=False):
    """Describes an API key.

    Customers invoke AppSync GraphQL API operations with API keys as an
    identity mechanism. There are two key versions:

    **da1**: We introduced this version at launch in November 2017. These
    keys always expire after 7 days. Amazon DynamoDB TTL manages key
    expiration. These keys ceased to be valid after February 21, 2018, and
    they should no longer be used.

    -  ``ListApiKeys`` returns the expiration time in milliseconds.

    -  ``CreateApiKey`` returns the expiration time in milliseconds.

    -  ``UpdateApiKey`` is not available for this key version.

    -  ``DeleteApiKey`` deletes the item from the table.

    -  Expiration is stored in DynamoDB as milliseconds. This results in a
       bug where keys are not automatically deleted because DynamoDB expects
       the TTL to be stored in seconds. As a one-time action, we deleted
       these keys from the table on February 21, 2018.

    **da2**: We introduced this version in February 2018 when AppSync added
    support to extend key expiration.

    -  ``ListApiKeys`` returns the expiration time and deletion time in
       seconds.

    -  ``CreateApiKey`` returns the expiration time and deletion time in
       seconds and accepts a user-provided expiration time in seconds.

    -  ``UpdateApiKey`` returns the expiration time and and deletion time in
       seconds and accepts a user-provided expiration time in seconds.
       Expired API keys are kept for 60 days after the expiration time. You
       can update the key expiration time as long as the key isn't deleted.

    -  ``DeleteApiKey`` deletes the item from the table.

    -  Expiration is stored in DynamoDB as seconds. After the expiration
       time, using the key to authenticate will fail. However, you can
       reinstate the key before deletion.

    -  Deletion is stored in DynamoDB as seconds. The key is deleted after
       deletion time.
    """

    id: Optional[String]
    description: Optional[String]
    expires: Optional[Long]
    deletes: Optional[Long]


ApiKeys = List[ApiKey]
Apis = List[Api]


class AppSyncRuntime(TypedDict, total=False):
    """Describes a runtime used by an Amazon Web Services AppSync pipeline
    resolver or Amazon Web Services AppSync function. Specifies the name and
    version of the runtime to use. Note that if a runtime is specified, code
    must also be specified.
    """

    name: RuntimeName
    runtimeVersion: String


class AssociateApiRequest(ServiceRequest):
    domainName: DomainName
    apiId: String


class AssociateApiResponse(TypedDict, total=False):
    apiAssociation: Optional[ApiAssociation]


class SourceApiAssociationConfig(TypedDict, total=False):
    """Describes properties used to specify configurations related to a source
    API.
    """

    mergeType: Optional[MergeType]


class AssociateMergedGraphqlApiRequest(ServiceRequest):
    sourceApiIdentifier: String
    mergedApiIdentifier: String
    description: Optional[String]
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig]


Date = datetime


class SourceApiAssociation(TypedDict, total=False):
    """Describes the configuration of a source API. A source API is a GraphQL
    API that is linked to a merged API. There can be multiple source APIs
    attached to each merged API. When linked to a merged API, the source
    API's schema, data sources, and resolvers will be combined with other
    linked source API data to form a new, singular API.

    Source APIs can originate from your account or from other accounts via
    Amazon Web Services Resource Access Manager. For more information about
    sharing resources from other accounts, see `What is Amazon Web Services
    Resource Access
    Manager? <https://docs.aws.amazon.com/ram/latest/userguide/what-is.html>`__
    in the *Amazon Web Services Resource Access Manager* guide.
    """

    associationId: Optional[String]
    associationArn: Optional[String]
    sourceApiId: Optional[String]
    sourceApiArn: Optional[String]
    mergedApiArn: Optional[String]
    mergedApiId: Optional[String]
    description: Optional[String]
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig]
    sourceApiAssociationStatus: Optional[SourceApiAssociationStatus]
    sourceApiAssociationStatusDetail: Optional[String]
    lastSuccessfulMergeDate: Optional[Date]


class AssociateMergedGraphqlApiResponse(TypedDict, total=False):
    sourceApiAssociation: Optional[SourceApiAssociation]


class AssociateSourceGraphqlApiRequest(ServiceRequest):
    mergedApiIdentifier: String
    sourceApiIdentifier: String
    description: Optional[String]
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig]


class AssociateSourceGraphqlApiResponse(TypedDict, total=False):
    sourceApiAssociation: Optional[SourceApiAssociation]


class AwsIamConfig(TypedDict, total=False):
    """The Identity and Access Management (IAM) configuration."""

    signingRegion: Optional[String]
    signingServiceName: Optional[String]


class AuthorizationConfig(TypedDict, total=False):
    """The authorization configuration in case the HTTP endpoint requires
    authorization.
    """

    authorizationType: AuthorizationType
    awsIamConfig: Optional[AwsIamConfig]


Blob = bytes
CachingKeys = List[String]


class CachingConfig(TypedDict, total=False):
    """The caching configuration for a resolver that has caching activated."""

    ttl: Long
    cachingKeys: Optional[CachingKeys]


class LambdaConfig(TypedDict, total=False):
    """The configuration for a Lambda data source."""

    invokeType: Optional[InvokeType]


class Integration(TypedDict, total=False):
    """The integration data source configuration for the handler."""

    dataSourceName: String
    lambdaConfig: Optional[LambdaConfig]


class HandlerConfig(TypedDict, total=False):
    """The configuration for a handler."""

    behavior: HandlerBehavior
    integration: Integration


class HandlerConfigs(TypedDict, total=False):
    """The configuration for the ``OnPublish`` and ``OnSubscribe`` handlers."""

    onPublish: Optional[HandlerConfig]
    onSubscribe: Optional[HandlerConfig]


class ChannelNamespace(TypedDict, total=False):
    """Describes a channel namespace associated with an ``Api``. The
    ``ChannelNamespace`` contains the definitions for code handlers for the
    ``Api``.
    """

    apiId: Optional[String]
    name: Optional[Namespace]
    subscribeAuthModes: Optional[AuthModes]
    publishAuthModes: Optional[AuthModes]
    codeHandlers: Optional[Code]
    tags: Optional[TagMap]
    channelNamespaceArn: Optional[String]
    created: Optional[Timestamp]
    lastModified: Optional[Timestamp]
    handlerConfigs: Optional[HandlerConfigs]


ChannelNamespaces = List[ChannelNamespace]
CreateApiCacheRequest = TypedDict(
    "CreateApiCacheRequest",
    {
        "apiId": String,
        "ttl": Long,
        "transitEncryptionEnabled": Optional[Boolean],
        "atRestEncryptionEnabled": Optional[Boolean],
        "apiCachingBehavior": ApiCachingBehavior,
        "type": ApiCacheType,
        "healthMetricsConfig": Optional[CacheHealthMetricsConfig],
    },
    total=False,
)


class CreateApiCacheResponse(TypedDict, total=False):
    """Represents the output of a ``CreateApiCache`` operation."""

    apiCache: Optional[ApiCache]


class CreateApiKeyRequest(ServiceRequest):
    apiId: String
    description: Optional[String]
    expires: Optional[Long]


class CreateApiKeyResponse(TypedDict, total=False):
    apiKey: Optional[ApiKey]


class CreateApiRequest(ServiceRequest):
    name: ApiName
    ownerContact: Optional[String]
    tags: Optional[TagMap]
    eventConfig: Optional[EventConfig]


class CreateApiResponse(TypedDict, total=False):
    api: Optional[Api]


class CreateChannelNamespaceRequest(ServiceRequest):
    apiId: String
    name: Namespace
    subscribeAuthModes: Optional[AuthModes]
    publishAuthModes: Optional[AuthModes]
    codeHandlers: Optional[Code]
    tags: Optional[TagMap]
    handlerConfigs: Optional[HandlerConfigs]


class CreateChannelNamespaceResponse(TypedDict, total=False):
    channelNamespace: Optional[ChannelNamespace]


class EventBridgeDataSourceConfig(TypedDict, total=False):
    """Describes an Amazon EventBridge bus data source configuration."""

    eventBusArn: String


class RdsHttpEndpointConfig(TypedDict, total=False):
    """The Amazon Relational Database Service (Amazon RDS) HTTP endpoint
    configuration.
    """

    awsRegion: Optional[String]
    dbClusterIdentifier: Optional[String]
    databaseName: Optional[String]
    schema: Optional[String]
    awsSecretStoreArn: Optional[String]


class RelationalDatabaseDataSourceConfig(TypedDict, total=False):
    """Describes a relational database data source configuration."""

    relationalDatabaseSourceType: Optional[RelationalDatabaseSourceType]
    rdsHttpEndpointConfig: Optional[RdsHttpEndpointConfig]


class HttpDataSourceConfig(TypedDict, total=False):
    """Describes an HTTP data source configuration."""

    endpoint: Optional[String]
    authorizationConfig: Optional[AuthorizationConfig]


class OpenSearchServiceDataSourceConfig(TypedDict, total=False):
    """Describes an OpenSearch data source configuration."""

    endpoint: String
    awsRegion: String


class ElasticsearchDataSourceConfig(TypedDict, total=False):
    """Describes an OpenSearch data source configuration.

    As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch
    Service. This configuration is deprecated. For new data sources, use
    OpenSearchServiceDataSourceConfig to specify an OpenSearch data source.
    """

    endpoint: String
    awsRegion: String


class LambdaDataSourceConfig(TypedDict, total=False):
    """Describes an Lambda data source configuration."""

    lambdaFunctionArn: String


class DeltaSyncConfig(TypedDict, total=False):
    """Describes a Delta Sync configuration."""

    baseTableTTL: Optional[Long]
    deltaSyncTableName: Optional[String]
    deltaSyncTableTTL: Optional[Long]


class DynamodbDataSourceConfig(TypedDict, total=False):
    """Describes an Amazon DynamoDB data source configuration."""

    tableName: String
    awsRegion: String
    useCallerCredentials: Optional[Boolean]
    deltaSyncConfig: Optional[DeltaSyncConfig]
    versioned: Optional[Boolean]


CreateDataSourceRequest = TypedDict(
    "CreateDataSourceRequest",
    {
        "apiId": String,
        "name": ResourceName,
        "description": Optional[String],
        "type": DataSourceType,
        "serviceRoleArn": Optional[String],
        "dynamodbConfig": Optional[DynamodbDataSourceConfig],
        "lambdaConfig": Optional[LambdaDataSourceConfig],
        "elasticsearchConfig": Optional[ElasticsearchDataSourceConfig],
        "openSearchServiceConfig": Optional[OpenSearchServiceDataSourceConfig],
        "httpConfig": Optional[HttpDataSourceConfig],
        "relationalDatabaseConfig": Optional[RelationalDatabaseDataSourceConfig],
        "eventBridgeConfig": Optional[EventBridgeDataSourceConfig],
        "metricsConfig": Optional[DataSourceLevelMetricsConfig],
    },
    total=False,
)
DataSource = TypedDict(
    "DataSource",
    {
        "dataSourceArn": Optional[String],
        "name": Optional[ResourceName],
        "description": Optional[String],
        "type": Optional[DataSourceType],
        "serviceRoleArn": Optional[String],
        "dynamodbConfig": Optional[DynamodbDataSourceConfig],
        "lambdaConfig": Optional[LambdaDataSourceConfig],
        "elasticsearchConfig": Optional[ElasticsearchDataSourceConfig],
        "openSearchServiceConfig": Optional[OpenSearchServiceDataSourceConfig],
        "httpConfig": Optional[HttpDataSourceConfig],
        "relationalDatabaseConfig": Optional[RelationalDatabaseDataSourceConfig],
        "eventBridgeConfig": Optional[EventBridgeDataSourceConfig],
        "metricsConfig": Optional[DataSourceLevelMetricsConfig],
    },
    total=False,
)


class CreateDataSourceResponse(TypedDict, total=False):
    dataSource: Optional[DataSource]


class CreateDomainNameRequest(ServiceRequest):
    domainName: DomainName
    certificateArn: CertificateArn
    description: Optional[Description]
    tags: Optional[TagMap]


class DomainNameConfig(TypedDict, total=False):
    """Describes a configuration for a custom domain."""

    domainName: Optional[DomainName]
    description: Optional[Description]
    certificateArn: Optional[CertificateArn]
    appsyncDomainName: Optional[String]
    hostedZoneId: Optional[String]
    tags: Optional[TagMap]
    domainNameArn: Optional[String]


class CreateDomainNameResponse(TypedDict, total=False):
    domainNameConfig: Optional[DomainNameConfig]


class LambdaConflictHandlerConfig(TypedDict, total=False):
    """The ``LambdaConflictHandlerConfig`` object when configuring ``LAMBDA``
    as the Conflict Handler.
    """

    lambdaConflictHandlerArn: Optional[String]


class SyncConfig(TypedDict, total=False):
    """Describes a Sync configuration for a resolver.

    Specifies which Conflict Detection strategy and Resolution strategy to
    use when the resolver is invoked.
    """

    conflictHandler: Optional[ConflictHandlerType]
    conflictDetection: Optional[ConflictDetectionType]
    lambdaConflictHandlerConfig: Optional[LambdaConflictHandlerConfig]


class CreateFunctionRequest(ServiceRequest):
    apiId: String
    name: ResourceName
    description: Optional[String]
    dataSourceName: ResourceName
    requestMappingTemplate: Optional[MappingTemplate]
    responseMappingTemplate: Optional[MappingTemplate]
    functionVersion: Optional[String]
    syncConfig: Optional[SyncConfig]
    maxBatchSize: Optional[MaxBatchSize]
    runtime: Optional[AppSyncRuntime]
    code: Optional[Code]


class FunctionConfiguration(TypedDict, total=False):
    """A function is a reusable entity. You can use multiple functions to
    compose the resolver logic.
    """

    functionId: Optional[String]
    functionArn: Optional[String]
    name: Optional[ResourceName]
    description: Optional[String]
    dataSourceName: Optional[ResourceName]
    requestMappingTemplate: Optional[MappingTemplate]
    responseMappingTemplate: Optional[MappingTemplate]
    functionVersion: Optional[String]
    syncConfig: Optional[SyncConfig]
    maxBatchSize: Optional[MaxBatchSize]
    runtime: Optional[AppSyncRuntime]
    code: Optional[Code]


class CreateFunctionResponse(TypedDict, total=False):
    functionConfiguration: Optional[FunctionConfiguration]


class EnhancedMetricsConfig(TypedDict, total=False):
    """Enables and controls the enhanced metrics feature. Enhanced metrics emit
    granular data on API usage and performance such as AppSync request and
    error counts, latency, and cache hits/misses. All enhanced metric data
    is sent to your CloudWatch account, and you can configure the types of
    data that will be sent.

    Enhanced metrics can be configured at the resolver, data source, and
    operation levels. ``EnhancedMetricsConfig`` contains three required
    parameters, each controlling one of these categories:

    #. ``resolverLevelMetricsBehavior``: Controls how resolver metrics will
       be emitted to CloudWatch. Resolver metrics include:

       -  GraphQL errors: The number of GraphQL errors that occurred.

       -  Requests: The number of invocations that occurred during a
          request.

       -  Latency: The time to complete a resolver invocation.

       -  Cache hits: The number of cache hits during a request.

       -  Cache misses: The number of cache misses during a request.

       These metrics can be emitted to CloudWatch per resolver or for all
       resolvers in the request. Metrics will be recorded by API ID and
       resolver name. ``resolverLevelMetricsBehavior`` accepts one of these
       values at a time:

       -  ``FULL_REQUEST_RESOLVER_METRICS``: Records and emits metric data
          for all resolvers in the request.

       -  ``PER_RESOLVER_METRICS``: Records and emits metric data for
          resolvers that have the ``metricsConfig`` value set to
          ``ENABLED``.

    #. ``dataSourceLevelMetricsBehavior``: Controls how data source metrics
       will be emitted to CloudWatch. Data source metrics include:

       -  Requests: The number of invocations that occured during a request.

       -  Latency: The time to complete a data source invocation.

       -  Errors: The number of errors that occurred during a data source
          invocation.

       These metrics can be emitted to CloudWatch per data source or for all
       data sources in the request. Metrics will be recorded by API ID and
       data source name. ``dataSourceLevelMetricsBehavior`` accepts one of
       these values at a time:

       -  ``FULL_REQUEST_DATA_SOURCE_METRICS``: Records and emits metric
          data for all data sources in the request.

       -  ``PER_DATA_SOURCE_METRICS``: Records and emits metric data for
          data sources that have the ``metricsConfig`` value set to
          ``ENABLED``.

    #. ``operationLevelMetricsConfig``: Controls how operation metrics will
       be emitted to CloudWatch. Operation metrics include:

       -  Requests: The number of times a specified GraphQL operation was
          called.

       -  GraphQL errors: The number of GraphQL errors that occurred during
          a specified GraphQL operation.

       Metrics will be recorded by API ID and operation name. You can set
       the value to ``ENABLED`` or ``DISABLED``.
    """

    resolverLevelMetricsBehavior: ResolverLevelMetricsBehavior
    dataSourceLevelMetricsBehavior: DataSourceLevelMetricsBehavior
    operationLevelMetricsConfig: OperationLevelMetricsConfig


class UserPoolConfig(TypedDict, total=False):
    """Describes an Amazon Cognito user pool configuration."""

    userPoolId: String
    awsRegion: String
    defaultAction: DefaultAction
    appIdClientRegex: Optional[String]


class LogConfig(TypedDict, total=False):
    """The Amazon CloudWatch Logs configuration."""

    fieldLogLevel: FieldLogLevel
    cloudWatchLogsRoleArn: String
    excludeVerboseContent: Optional[Boolean]


class CreateGraphqlApiRequest(ServiceRequest):
    name: String
    logConfig: Optional[LogConfig]
    authenticationType: AuthenticationType
    userPoolConfig: Optional[UserPoolConfig]
    openIDConnectConfig: Optional[OpenIDConnectConfig]
    tags: Optional[TagMap]
    additionalAuthenticationProviders: Optional[AdditionalAuthenticationProviders]
    xrayEnabled: Optional[Boolean]
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig]
    apiType: Optional[GraphQLApiType]
    mergedApiExecutionRoleArn: Optional[String]
    visibility: Optional[GraphQLApiVisibility]
    ownerContact: Optional[String]
    introspectionConfig: Optional[GraphQLApiIntrospectionConfig]
    queryDepthLimit: Optional[QueryDepthLimit]
    resolverCountLimit: Optional[ResolverCountLimit]
    enhancedMetricsConfig: Optional[EnhancedMetricsConfig]


class GraphqlApi(TypedDict, total=False):
    """Describes a GraphQL API."""

    name: Optional[ResourceName]
    apiId: Optional[String]
    authenticationType: Optional[AuthenticationType]
    logConfig: Optional[LogConfig]
    userPoolConfig: Optional[UserPoolConfig]
    openIDConnectConfig: Optional[OpenIDConnectConfig]
    arn: Optional[String]
    uris: Optional[MapOfStringToString]
    tags: Optional[TagMap]
    additionalAuthenticationProviders: Optional[AdditionalAuthenticationProviders]
    xrayEnabled: Optional[Boolean]
    wafWebAclArn: Optional[String]
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig]
    dns: Optional[MapOfStringToString]
    visibility: Optional[GraphQLApiVisibility]
    apiType: Optional[GraphQLApiType]
    mergedApiExecutionRoleArn: Optional[String]
    owner: Optional[String]
    ownerContact: Optional[String]
    introspectionConfig: Optional[GraphQLApiIntrospectionConfig]
    queryDepthLimit: Optional[QueryDepthLimit]
    resolverCountLimit: Optional[ResolverCountLimit]
    enhancedMetricsConfig: Optional[EnhancedMetricsConfig]


class CreateGraphqlApiResponse(TypedDict, total=False):
    graphqlApi: Optional[GraphqlApi]


FunctionsIds = List[String]


class PipelineConfig(TypedDict, total=False):
    """The pipeline configuration for a resolver of kind ``PIPELINE``."""

    functions: Optional[FunctionsIds]


class CreateResolverRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName
    fieldName: ResourceName
    dataSourceName: Optional[ResourceName]
    requestMappingTemplate: Optional[MappingTemplate]
    responseMappingTemplate: Optional[MappingTemplate]
    kind: Optional[ResolverKind]
    pipelineConfig: Optional[PipelineConfig]
    syncConfig: Optional[SyncConfig]
    cachingConfig: Optional[CachingConfig]
    maxBatchSize: Optional[MaxBatchSize]
    runtime: Optional[AppSyncRuntime]
    code: Optional[Code]
    metricsConfig: Optional[ResolverLevelMetricsConfig]


class Resolver(TypedDict, total=False):
    """Describes a resolver."""

    typeName: Optional[ResourceName]
    fieldName: Optional[ResourceName]
    dataSourceName: Optional[ResourceName]
    resolverArn: Optional[String]
    requestMappingTemplate: Optional[MappingTemplate]
    responseMappingTemplate: Optional[MappingTemplate]
    kind: Optional[ResolverKind]
    pipelineConfig: Optional[PipelineConfig]
    syncConfig: Optional[SyncConfig]
    cachingConfig: Optional[CachingConfig]
    maxBatchSize: Optional[MaxBatchSize]
    runtime: Optional[AppSyncRuntime]
    code: Optional[Code]
    metricsConfig: Optional[ResolverLevelMetricsConfig]


class CreateResolverResponse(TypedDict, total=False):
    resolver: Optional[Resolver]


class CreateTypeRequest(ServiceRequest):
    apiId: String
    definition: String
    format: TypeDefinitionFormat


class Type(TypedDict, total=False):
    """Describes a type."""

    name: Optional[ResourceName]
    description: Optional[String]
    arn: Optional[String]
    definition: Optional[String]
    format: Optional[TypeDefinitionFormat]


CreateTypeResponse = TypedDict(
    "CreateTypeResponse",
    {
        "type": Optional[Type],
    },
    total=False,
)
DataSourceIntrospectionModelIndexFields = List[String]


class DataSourceIntrospectionModelIndex(TypedDict, total=False):
    """The index that was retrieved from the introspected data."""

    name: Optional[String]
    fields: Optional[DataSourceIntrospectionModelIndexFields]


DataSourceIntrospectionModelIndexes = List[DataSourceIntrospectionModelIndex]
DataSourceIntrospectionModelFieldTypeValues = List[String]
DataSourceIntrospectionModelFieldType = TypedDict(
    "DataSourceIntrospectionModelFieldType",
    {
        "kind": Optional["String"],
        "name": Optional["String"],
        "type": Optional["DataSourceIntrospectionModelFieldType"],
        "values": Optional["DataSourceIntrospectionModelFieldTypeValues"],
    },
    total=False,
)
DataSourceIntrospectionModelField = TypedDict(
    "DataSourceIntrospectionModelField",
    {
        "name": Optional[String],
        "type": Optional[DataSourceIntrospectionModelFieldType],
        "length": Optional[Long],
    },
    total=False,
)
DataSourceIntrospectionModelFields = List[DataSourceIntrospectionModelField]


class DataSourceIntrospectionModel(TypedDict, total=False):
    """Contains the introspected data that was retrieved from the data source."""

    name: Optional[String]
    fields: Optional[DataSourceIntrospectionModelFields]
    primaryKey: Optional[DataSourceIntrospectionModelIndex]
    indexes: Optional[DataSourceIntrospectionModelIndexes]
    sdl: Optional[String]


DataSourceIntrospectionModels = List[DataSourceIntrospectionModel]


class DataSourceIntrospectionResult(TypedDict, total=False):
    """Represents the output of a ``DataSourceIntrospectionResult``. This is
    the populated result of a ``GetDataSourceIntrospection`` operation.
    """

    models: Optional[DataSourceIntrospectionModels]
    nextToken: Optional[PaginationToken]


DataSources = List[DataSource]


class DeleteApiCacheRequest(ServiceRequest):
    """Represents the input of a ``DeleteApiCache`` operation."""

    apiId: String


class DeleteApiCacheResponse(TypedDict, total=False):
    """Represents the output of a ``DeleteApiCache`` operation."""

    pass


class DeleteApiKeyRequest(ServiceRequest):
    apiId: String
    id: String


class DeleteApiKeyResponse(TypedDict, total=False):
    pass


class DeleteApiRequest(ServiceRequest):
    apiId: String


class DeleteApiResponse(TypedDict, total=False):
    pass


class DeleteChannelNamespaceRequest(ServiceRequest):
    apiId: String
    name: Namespace


class DeleteChannelNamespaceResponse(TypedDict, total=False):
    pass


class DeleteDataSourceRequest(ServiceRequest):
    apiId: String
    name: ResourceName


class DeleteDataSourceResponse(TypedDict, total=False):
    pass


class DeleteDomainNameRequest(ServiceRequest):
    domainName: DomainName


class DeleteDomainNameResponse(TypedDict, total=False):
    pass


class DeleteFunctionRequest(ServiceRequest):
    apiId: String
    functionId: ResourceName


class DeleteFunctionResponse(TypedDict, total=False):
    pass


class DeleteGraphqlApiRequest(ServiceRequest):
    apiId: String


class DeleteGraphqlApiResponse(TypedDict, total=False):
    pass


class DeleteResolverRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName
    fieldName: ResourceName


class DeleteResolverResponse(TypedDict, total=False):
    pass


class DeleteTypeRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName


class DeleteTypeResponse(TypedDict, total=False):
    pass


class DisassociateApiRequest(ServiceRequest):
    domainName: DomainName


class DisassociateApiResponse(TypedDict, total=False):
    pass


class DisassociateMergedGraphqlApiRequest(ServiceRequest):
    sourceApiIdentifier: String
    associationId: String


class DisassociateMergedGraphqlApiResponse(TypedDict, total=False):
    sourceApiAssociationStatus: Optional[SourceApiAssociationStatus]


class DisassociateSourceGraphqlApiRequest(ServiceRequest):
    mergedApiIdentifier: String
    associationId: String


class DisassociateSourceGraphqlApiResponse(TypedDict, total=False):
    sourceApiAssociationStatus: Optional[SourceApiAssociationStatus]


DomainNameConfigs = List[DomainNameConfig]
EnvironmentVariableMap = Dict[EnvironmentVariableKey, EnvironmentVariableValue]


class ErrorDetail(TypedDict, total=False):
    """Contains the list of errors generated. When using JavaScript, this will
    apply to the request or response function evaluation.
    """

    message: Optional[ErrorMessage]


class EvaluateCodeErrorDetail(TypedDict, total=False):
    """Contains the list of errors from a code evaluation response."""

    message: Optional[ErrorMessage]
    codeErrors: Optional[CodeErrors]


class EvaluateCodeRequest(ServiceRequest):
    runtime: AppSyncRuntime
    code: Code
    context: Context
    function: Optional[String]


Logs = List[String]


class EvaluateCodeResponse(TypedDict, total=False):
    evaluationResult: Optional[EvaluationResult]
    error: Optional[EvaluateCodeErrorDetail]
    logs: Optional[Logs]
    stash: Optional[Stash]
    outErrors: Optional[OutErrors]


class EvaluateMappingTemplateRequest(ServiceRequest):
    template: Template
    context: Context


class EvaluateMappingTemplateResponse(TypedDict, total=False):
    evaluationResult: Optional[EvaluationResult]
    error: Optional[ErrorDetail]
    logs: Optional[Logs]
    stash: Optional[Stash]
    outErrors: Optional[OutErrors]


class FlushApiCacheRequest(ServiceRequest):
    """Represents the input of a ``FlushApiCache`` operation."""

    apiId: String


class FlushApiCacheResponse(TypedDict, total=False):
    """Represents the output of a ``FlushApiCache`` operation."""

    pass


Functions = List[FunctionConfiguration]


class GetApiAssociationRequest(ServiceRequest):
    domainName: DomainName


class GetApiAssociationResponse(TypedDict, total=False):
    apiAssociation: Optional[ApiAssociation]


class GetApiCacheRequest(ServiceRequest):
    """Represents the input of a ``GetApiCache`` operation."""

    apiId: String


class GetApiCacheResponse(TypedDict, total=False):
    """Represents the output of a ``GetApiCache`` operation."""

    apiCache: Optional[ApiCache]


class GetApiRequest(ServiceRequest):
    apiId: String


class GetApiResponse(TypedDict, total=False):
    api: Optional[Api]


class GetChannelNamespaceRequest(ServiceRequest):
    apiId: String
    name: Namespace


class GetChannelNamespaceResponse(TypedDict, total=False):
    channelNamespace: Optional[ChannelNamespace]


class GetDataSourceIntrospectionRequest(ServiceRequest):
    introspectionId: String
    includeModelsSDL: Optional[Boolean]
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class GetDataSourceIntrospectionResponse(TypedDict, total=False):
    introspectionId: Optional[String]
    introspectionStatus: Optional[DataSourceIntrospectionStatus]
    introspectionStatusDetail: Optional[String]
    introspectionResult: Optional[DataSourceIntrospectionResult]


class GetDataSourceRequest(ServiceRequest):
    apiId: String
    name: ResourceName


class GetDataSourceResponse(TypedDict, total=False):
    dataSource: Optional[DataSource]


class GetDomainNameRequest(ServiceRequest):
    domainName: DomainName


class GetDomainNameResponse(TypedDict, total=False):
    domainNameConfig: Optional[DomainNameConfig]


class GetFunctionRequest(ServiceRequest):
    apiId: String
    functionId: ResourceName


class GetFunctionResponse(TypedDict, total=False):
    functionConfiguration: Optional[FunctionConfiguration]


class GetGraphqlApiEnvironmentVariablesRequest(ServiceRequest):
    apiId: String


class GetGraphqlApiEnvironmentVariablesResponse(TypedDict, total=False):
    environmentVariables: Optional[EnvironmentVariableMap]


class GetGraphqlApiRequest(ServiceRequest):
    apiId: String


class GetGraphqlApiResponse(TypedDict, total=False):
    graphqlApi: Optional[GraphqlApi]


class GetIntrospectionSchemaRequest(ServiceRequest):
    apiId: String
    format: OutputType
    includeDirectives: Optional[BooleanValue]


class GetIntrospectionSchemaResponse(TypedDict, total=False):
    schema: Optional[Union[Blob, IO[Blob], Iterable[Blob]]]


class GetResolverRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName
    fieldName: ResourceName


class GetResolverResponse(TypedDict, total=False):
    resolver: Optional[Resolver]


class GetSchemaCreationStatusRequest(ServiceRequest):
    apiId: String


class GetSchemaCreationStatusResponse(TypedDict, total=False):
    status: Optional[SchemaStatus]
    details: Optional[String]


class GetSourceApiAssociationRequest(ServiceRequest):
    mergedApiIdentifier: String
    associationId: String


class GetSourceApiAssociationResponse(TypedDict, total=False):
    sourceApiAssociation: Optional[SourceApiAssociation]


class GetTypeRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName
    format: TypeDefinitionFormat


GetTypeResponse = TypedDict(
    "GetTypeResponse",
    {
        "type": Optional[Type],
    },
    total=False,
)
GraphqlApis = List[GraphqlApi]


class ListApiKeysRequest(ServiceRequest):
    apiId: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListApiKeysResponse(TypedDict, total=False):
    apiKeys: Optional[ApiKeys]
    nextToken: Optional[PaginationToken]


class ListApisRequest(ServiceRequest):
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListApisResponse(TypedDict, total=False):
    apis: Optional[Apis]
    nextToken: Optional[PaginationToken]


class ListChannelNamespacesRequest(ServiceRequest):
    apiId: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListChannelNamespacesResponse(TypedDict, total=False):
    channelNamespaces: Optional[ChannelNamespaces]
    nextToken: Optional[PaginationToken]


class ListDataSourcesRequest(ServiceRequest):
    apiId: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListDataSourcesResponse(TypedDict, total=False):
    dataSources: Optional[DataSources]
    nextToken: Optional[PaginationToken]


class ListDomainNamesRequest(ServiceRequest):
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListDomainNamesResponse(TypedDict, total=False):
    domainNameConfigs: Optional[DomainNameConfigs]
    nextToken: Optional[PaginationToken]


class ListFunctionsRequest(ServiceRequest):
    apiId: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListFunctionsResponse(TypedDict, total=False):
    functions: Optional[Functions]
    nextToken: Optional[PaginationToken]


class ListGraphqlApisRequest(ServiceRequest):
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]
    apiType: Optional[GraphQLApiType]
    owner: Optional[Ownership]


class ListGraphqlApisResponse(TypedDict, total=False):
    graphqlApis: Optional[GraphqlApis]
    nextToken: Optional[PaginationToken]


class ListResolversByFunctionRequest(ServiceRequest):
    apiId: String
    functionId: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


Resolvers = List[Resolver]


class ListResolversByFunctionResponse(TypedDict, total=False):
    resolvers: Optional[Resolvers]
    nextToken: Optional[PaginationToken]


class ListResolversRequest(ServiceRequest):
    apiId: String
    typeName: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListResolversResponse(TypedDict, total=False):
    resolvers: Optional[Resolvers]
    nextToken: Optional[PaginationToken]


class ListSourceApiAssociationsRequest(ServiceRequest):
    apiId: String
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class SourceApiAssociationSummary(TypedDict, total=False):
    """Describes the ARNs and IDs of associations, Merged APIs, and source
    APIs.
    """

    associationId: Optional[String]
    associationArn: Optional[String]
    sourceApiId: Optional[String]
    sourceApiArn: Optional[String]
    mergedApiId: Optional[String]
    mergedApiArn: Optional[String]
    description: Optional[String]


SourceApiAssociationSummaryList = List[SourceApiAssociationSummary]


class ListSourceApiAssociationsResponse(TypedDict, total=False):
    sourceApiAssociationSummaries: Optional[SourceApiAssociationSummaryList]
    nextToken: Optional[PaginationToken]


class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: ResourceArn


class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Optional[TagMap]


class ListTypesByAssociationRequest(ServiceRequest):
    mergedApiIdentifier: String
    associationId: String
    format: TypeDefinitionFormat
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


TypeList = List[Type]


class ListTypesByAssociationResponse(TypedDict, total=False):
    types: Optional[TypeList]
    nextToken: Optional[PaginationToken]


class ListTypesRequest(ServiceRequest):
    apiId: String
    format: TypeDefinitionFormat
    nextToken: Optional[PaginationToken]
    maxResults: Optional[MaxResults]


class ListTypesResponse(TypedDict, total=False):
    types: Optional[TypeList]
    nextToken: Optional[PaginationToken]


class PutGraphqlApiEnvironmentVariablesRequest(ServiceRequest):
    apiId: String
    environmentVariables: EnvironmentVariableMap


class PutGraphqlApiEnvironmentVariablesResponse(TypedDict, total=False):
    environmentVariables: Optional[EnvironmentVariableMap]


class RdsDataApiConfig(TypedDict, total=False):
    """Contains the metadata required to introspect the RDS cluster."""

    resourceArn: RdsDataApiConfigResourceArn
    secretArn: RdsDataApiConfigSecretArn
    databaseName: RdsDataApiConfigDatabaseName


class StartDataSourceIntrospectionRequest(ServiceRequest):
    rdsDataApiConfig: Optional[RdsDataApiConfig]


class StartDataSourceIntrospectionResponse(TypedDict, total=False):
    introspectionId: Optional[String]
    introspectionStatus: Optional[DataSourceIntrospectionStatus]
    introspectionStatusDetail: Optional[String]


class StartSchemaCreationRequest(ServiceRequest):
    apiId: String
    definition: Blob


class StartSchemaCreationResponse(TypedDict, total=False):
    status: Optional[SchemaStatus]


class StartSchemaMergeRequest(ServiceRequest):
    associationId: String
    mergedApiIdentifier: String


class StartSchemaMergeResponse(TypedDict, total=False):
    sourceApiAssociationStatus: Optional[SourceApiAssociationStatus]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    resourceArn: ResourceArn
    tags: TagMap


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    resourceArn: ResourceArn
    tagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


UpdateApiCacheRequest = TypedDict(
    "UpdateApiCacheRequest",
    {
        "apiId": String,
        "ttl": Long,
        "apiCachingBehavior": ApiCachingBehavior,
        "type": ApiCacheType,
        "healthMetricsConfig": Optional[CacheHealthMetricsConfig],
    },
    total=False,
)


class UpdateApiCacheResponse(TypedDict, total=False):
    """Represents the output of a ``UpdateApiCache`` operation."""

    apiCache: Optional[ApiCache]


class UpdateApiKeyRequest(ServiceRequest):
    apiId: String
    id: String
    description: Optional[String]
    expires: Optional[Long]


class UpdateApiKeyResponse(TypedDict, total=False):
    apiKey: Optional[ApiKey]


class UpdateApiRequest(ServiceRequest):
    apiId: String
    name: ApiName
    ownerContact: Optional[String]
    eventConfig: Optional[EventConfig]


class UpdateApiResponse(TypedDict, total=False):
    api: Optional[Api]


class UpdateChannelNamespaceRequest(ServiceRequest):
    apiId: String
    name: Namespace
    subscribeAuthModes: Optional[AuthModes]
    publishAuthModes: Optional[AuthModes]
    codeHandlers: Optional[Code]
    handlerConfigs: Optional[HandlerConfigs]


class UpdateChannelNamespaceResponse(TypedDict, total=False):
    channelNamespace: Optional[ChannelNamespace]


UpdateDataSourceRequest = TypedDict(
    "UpdateDataSourceRequest",
    {
        "apiId": String,
        "name": ResourceName,
        "description": Optional[String],
        "type": DataSourceType,
        "serviceRoleArn": Optional[String],
        "dynamodbConfig": Optional[DynamodbDataSourceConfig],
        "lambdaConfig": Optional[LambdaDataSourceConfig],
        "elasticsearchConfig": Optional[ElasticsearchDataSourceConfig],
        "openSearchServiceConfig": Optional[OpenSearchServiceDataSourceConfig],
        "httpConfig": Optional[HttpDataSourceConfig],
        "relationalDatabaseConfig": Optional[RelationalDatabaseDataSourceConfig],
        "eventBridgeConfig": Optional[EventBridgeDataSourceConfig],
        "metricsConfig": Optional[DataSourceLevelMetricsConfig],
    },
    total=False,
)


class UpdateDataSourceResponse(TypedDict, total=False):
    dataSource: Optional[DataSource]


class UpdateDomainNameRequest(ServiceRequest):
    domainName: DomainName
    description: Optional[Description]


class UpdateDomainNameResponse(TypedDict, total=False):
    domainNameConfig: Optional[DomainNameConfig]


class UpdateFunctionRequest(ServiceRequest):
    apiId: String
    name: ResourceName
    description: Optional[String]
    functionId: ResourceName
    dataSourceName: ResourceName
    requestMappingTemplate: Optional[MappingTemplate]
    responseMappingTemplate: Optional[MappingTemplate]
    functionVersion: Optional[String]
    syncConfig: Optional[SyncConfig]
    maxBatchSize: Optional[MaxBatchSize]
    runtime: Optional[AppSyncRuntime]
    code: Optional[Code]


class UpdateFunctionResponse(TypedDict, total=False):
    functionConfiguration: Optional[FunctionConfiguration]


class UpdateGraphqlApiRequest(ServiceRequest):
    apiId: String
    name: String
    logConfig: Optional[LogConfig]
    authenticationType: AuthenticationType
    userPoolConfig: Optional[UserPoolConfig]
    openIDConnectConfig: Optional[OpenIDConnectConfig]
    additionalAuthenticationProviders: Optional[AdditionalAuthenticationProviders]
    xrayEnabled: Optional[Boolean]
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig]
    mergedApiExecutionRoleArn: Optional[String]
    ownerContact: Optional[String]
    introspectionConfig: Optional[GraphQLApiIntrospectionConfig]
    queryDepthLimit: Optional[QueryDepthLimit]
    resolverCountLimit: Optional[ResolverCountLimit]
    enhancedMetricsConfig: Optional[EnhancedMetricsConfig]


class UpdateGraphqlApiResponse(TypedDict, total=False):
    graphqlApi: Optional[GraphqlApi]


class UpdateResolverRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName
    fieldName: ResourceName
    dataSourceName: Optional[ResourceName]
    requestMappingTemplate: Optional[MappingTemplate]
    responseMappingTemplate: Optional[MappingTemplate]
    kind: Optional[ResolverKind]
    pipelineConfig: Optional[PipelineConfig]
    syncConfig: Optional[SyncConfig]
    cachingConfig: Optional[CachingConfig]
    maxBatchSize: Optional[MaxBatchSize]
    runtime: Optional[AppSyncRuntime]
    code: Optional[Code]
    metricsConfig: Optional[ResolverLevelMetricsConfig]


class UpdateResolverResponse(TypedDict, total=False):
    resolver: Optional[Resolver]


class UpdateSourceApiAssociationRequest(ServiceRequest):
    associationId: String
    mergedApiIdentifier: String
    description: Optional[String]
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig]


class UpdateSourceApiAssociationResponse(TypedDict, total=False):
    sourceApiAssociation: Optional[SourceApiAssociation]


class UpdateTypeRequest(ServiceRequest):
    apiId: String
    typeName: ResourceName
    definition: Optional[String]
    format: TypeDefinitionFormat


UpdateTypeResponse = TypedDict(
    "UpdateTypeResponse",
    {
        "type": Optional[Type],
    },
    total=False,
)


class AppsyncApi:
    service = "appsync"
    version = "2017-07-25"

    @handler("AssociateApi")
    def associate_api(
        self, context: RequestContext, domain_name: DomainName, api_id: String, **kwargs
    ) -> AssociateApiResponse:
        """Maps an endpoint to your custom domain.

        :param domain_name: The domain name.
        :param api_id: The API ID.
        :returns: AssociateApiResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("AssociateMergedGraphqlApi")
    def associate_merged_graphql_api(
        self,
        context: RequestContext,
        source_api_identifier: String,
        merged_api_identifier: String,
        description: String | None = None,
        source_api_association_config: SourceApiAssociationConfig | None = None,
        **kwargs,
    ) -> AssociateMergedGraphqlApiResponse:
        """Creates an association between a Merged API and source API using the
        source API's identifier.

        :param source_api_identifier: The identifier of the AppSync Source API.
        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :param description: The description field.
        :param source_api_association_config: The ``SourceApiAssociationConfig`` object data.
        :returns: AssociateMergedGraphqlApiResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        :raises LimitExceededException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("AssociateSourceGraphqlApi")
    def associate_source_graphql_api(
        self,
        context: RequestContext,
        merged_api_identifier: String,
        source_api_identifier: String,
        description: String | None = None,
        source_api_association_config: SourceApiAssociationConfig | None = None,
        **kwargs,
    ) -> AssociateSourceGraphqlApiResponse:
        """Creates an association between a Merged API and source API using the
        Merged API's identifier.

        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :param source_api_identifier: The identifier of the AppSync Source API.
        :param description: The description field.
        :param source_api_association_config: The ``SourceApiAssociationConfig`` object data.
        :returns: AssociateSourceGraphqlApiResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        :raises LimitExceededException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("CreateApi")
    def create_api(
        self,
        context: RequestContext,
        name: ApiName,
        owner_contact: String | None = None,
        tags: TagMap | None = None,
        event_config: EventConfig | None = None,
        **kwargs,
    ) -> CreateApiResponse:
        """Creates an ``Api`` object. Use this operation to create an AppSync API
        with your preferred configuration, such as an Event API that provides
        real-time message publishing and message subscriptions over WebSockets.

        :param name: The name for the ``Api``.
        :param owner_contact: The owner contact information for the ``Api``.
        :param tags: A map with keys of ``TagKey`` objects and values of ``TagValue``
        objects.
        :param event_config: The Event API configuration.
        :returns: CreateApiResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises ServiceQuotaExceededException:
        """
        raise NotImplementedError

    @handler("CreateApiCache", expand=False)
    def create_api_cache(
        self, context: RequestContext, request: CreateApiCacheRequest, **kwargs
    ) -> CreateApiCacheResponse:
        """Creates a cache for the GraphQL API.

        :param api_id: The GraphQL API ID.
        :param ttl: TTL in seconds for cache entries.
        :param api_caching_behavior: Caching behavior.
        :param type: The cache instance type.
        :param transit_encryption_enabled: Transit encryption flag when connecting to cache.
        :param at_rest_encryption_enabled: At-rest encryption flag for cache.
        :param health_metrics_config: Controls how cache health metrics will be emitted to CloudWatch.
        :returns: CreateApiCacheResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("CreateApiKey")
    def create_api_key(
        self,
        context: RequestContext,
        api_id: String,
        description: String | None = None,
        expires: Long | None = None,
        **kwargs,
    ) -> CreateApiKeyResponse:
        """Creates a unique key that you can distribute to clients who invoke your
        API.

        :param api_id: The ID for your GraphQL API.
        :param description: A description of the purpose of the API key.
        :param expires: From the creation time, the time after which the API key expires.
        :returns: CreateApiKeyResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises LimitExceededException:
        :raises UnauthorizedException:
        :raises LimitExceededException:
        :raises InternalFailureException:
        :raises ApiKeyLimitExceededException:
        :raises ApiKeyValidityOutOfBoundsException:
        """
        raise NotImplementedError

    @handler("CreateChannelNamespace")
    def create_channel_namespace(
        self,
        context: RequestContext,
        api_id: String,
        name: Namespace,
        subscribe_auth_modes: AuthModes | None = None,
        publish_auth_modes: AuthModes | None = None,
        code_handlers: Code | None = None,
        tags: TagMap | None = None,
        handler_configs: HandlerConfigs | None = None,
        **kwargs,
    ) -> CreateChannelNamespaceResponse:
        """Creates a ``ChannelNamespace`` for an ``Api``.

        :param api_id: The ``Api`` ID.
        :param name: The name of the ``ChannelNamespace``.
        :param subscribe_auth_modes: The authorization mode to use for subscribing to messages on the channel
        namespace.
        :param publish_auth_modes: The authorization mode to use for publishing messages on the channel
        namespace.
        :param code_handlers: The event handler functions that run custom business logic to process
        published events and subscribe requests.
        :param tags: A map with keys of ``TagKey`` objects and values of ``TagValue``
        objects.
        :param handler_configs: The configuration for the ``OnPublish`` and ``OnSubscribe`` handlers.
        :returns: CreateChannelNamespaceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises ConflictException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises ServiceQuotaExceededException:
        """
        raise NotImplementedError

    @handler("CreateDataSource", expand=False)
    def create_data_source(
        self, context: RequestContext, request: CreateDataSourceRequest, **kwargs
    ) -> CreateDataSourceResponse:
        """Creates a ``DataSource`` object.

        :param api_id: The API ID for the GraphQL API for the ``DataSource``.
        :param name: A user-supplied name for the ``DataSource``.
        :param type: The type of the ``DataSource``.
        :param description: A description of the ``DataSource``.
        :param service_role_arn: The Identity and Access Management (IAM) service role Amazon Resource
        Name (ARN) for the data source.
        :param dynamodb_config: Amazon DynamoDB settings.
        :param lambda_config: Lambda settings.
        :param elasticsearch_config: Amazon OpenSearch Service settings.
        :param open_search_service_config: Amazon OpenSearch Service settings.
        :param http_config: HTTP endpoint settings.
        :param relational_database_config: Relational database settings.
        :param event_bridge_config: Amazon EventBridge settings.
        :param metrics_config: Enables or disables enhanced data source metrics for specified data
        sources.
        :returns: CreateDataSourceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("CreateDomainName")
    def create_domain_name(
        self,
        context: RequestContext,
        domain_name: DomainName,
        certificate_arn: CertificateArn,
        description: Description | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreateDomainNameResponse:
        """Creates a custom ``DomainName`` object.

        :param domain_name: The domain name.
        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate.
        :param description: A description of the ``DomainName``.
        :param tags: A map with keys of ``TagKey`` objects and values of ``TagValue``
        objects.
        :returns: CreateDomainNameResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("CreateFunction")
    def create_function(
        self,
        context: RequestContext,
        api_id: String,
        name: ResourceName,
        data_source_name: ResourceName,
        description: String | None = None,
        request_mapping_template: MappingTemplate | None = None,
        response_mapping_template: MappingTemplate | None = None,
        function_version: String | None = None,
        sync_config: SyncConfig | None = None,
        max_batch_size: MaxBatchSize | None = None,
        runtime: AppSyncRuntime | None = None,
        code: Code | None = None,
        **kwargs,
    ) -> CreateFunctionResponse:
        """Creates a ``Function`` object.

        A function is a reusable entity. You can use multiple functions to
        compose the resolver logic.

        :param api_id: The GraphQL API ID.
        :param name: The ``Function`` name.
        :param data_source_name: The ``Function`` ``DataSource`` name.
        :param description: The ``Function`` description.
        :param request_mapping_template: The ``Function`` request mapping template.
        :param response_mapping_template: The ``Function`` response mapping template.
        :param function_version: The ``version`` of the request mapping template.
        :param sync_config: Describes a Sync configuration for a resolver.
        :param max_batch_size: The maximum batching size for a resolver.
        :param runtime: Describes a runtime used by an Amazon Web Services AppSync pipeline
        resolver or Amazon Web Services AppSync function.
        :param code: The ``function`` code that contains the request and response functions.
        :returns: CreateFunctionResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("CreateGraphqlApi")
    def create_graphql_api(
        self,
        context: RequestContext,
        name: String,
        authentication_type: AuthenticationType,
        log_config: LogConfig | None = None,
        user_pool_config: UserPoolConfig | None = None,
        open_id_connect_config: OpenIDConnectConfig | None = None,
        tags: TagMap | None = None,
        additional_authentication_providers: AdditionalAuthenticationProviders | None = None,
        xray_enabled: Boolean | None = None,
        lambda_authorizer_config: LambdaAuthorizerConfig | None = None,
        api_type: GraphQLApiType | None = None,
        merged_api_execution_role_arn: String | None = None,
        visibility: GraphQLApiVisibility | None = None,
        owner_contact: String | None = None,
        introspection_config: GraphQLApiIntrospectionConfig | None = None,
        query_depth_limit: QueryDepthLimit | None = None,
        resolver_count_limit: ResolverCountLimit | None = None,
        enhanced_metrics_config: EnhancedMetricsConfig | None = None,
        **kwargs,
    ) -> CreateGraphqlApiResponse:
        """Creates a ``GraphqlApi`` object.

        :param name: A user-supplied name for the ``GraphqlApi``.
        :param authentication_type: The authentication type: API key, Identity and Access Management (IAM),
        OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda.
        :param log_config: The Amazon CloudWatch Logs configuration.
        :param user_pool_config: The Amazon Cognito user pool configuration.
        :param open_id_connect_config: The OIDC configuration.
        :param tags: A ``TagMap`` object.
        :param additional_authentication_providers: A list of additional authentication providers for the ``GraphqlApi``
        API.
        :param xray_enabled: A flag indicating whether to use X-Ray tracing for the ``GraphqlApi``.
        :param lambda_authorizer_config: Configuration for Lambda function authorization.
        :param api_type: The value that indicates whether the GraphQL API is a standard API
        (``GRAPHQL``) or merged API (``MERGED``).
        :param merged_api_execution_role_arn: The Identity and Access Management service role ARN for a merged API.
        :param visibility: Sets the value of the GraphQL API to public (``GLOBAL``) or private
        (``PRIVATE``).
        :param owner_contact: The owner contact information for an API resource.
        :param introspection_config: Sets the value of the GraphQL API to enable (``ENABLED``) or disable
        (``DISABLED``) introspection.
        :param query_depth_limit: The maximum depth a query can have in a single request.
        :param resolver_count_limit: The maximum number of resolvers that can be invoked in a single request.
        :param enhanced_metrics_config: The ``enhancedMetricsConfig`` object.
        :returns: CreateGraphqlApiResponse
        :raises BadRequestException:
        :raises LimitExceededException:
        :raises ConcurrentModificationException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises ApiLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateResolver")
    def create_resolver(
        self,
        context: RequestContext,
        api_id: String,
        type_name: ResourceName,
        field_name: ResourceName,
        data_source_name: ResourceName | None = None,
        request_mapping_template: MappingTemplate | None = None,
        response_mapping_template: MappingTemplate | None = None,
        kind: ResolverKind | None = None,
        pipeline_config: PipelineConfig | None = None,
        sync_config: SyncConfig | None = None,
        caching_config: CachingConfig | None = None,
        max_batch_size: MaxBatchSize | None = None,
        runtime: AppSyncRuntime | None = None,
        code: Code | None = None,
        metrics_config: ResolverLevelMetricsConfig | None = None,
        **kwargs,
    ) -> CreateResolverResponse:
        """Creates a ``Resolver`` object.

        A resolver converts incoming requests into a format that a data source
        can understand, and converts the data source's responses into GraphQL.

        :param api_id: The ID for the GraphQL API for which the resolver is being created.
        :param type_name: The name of the ``Type``.
        :param field_name: The name of the field to attach the resolver to.
        :param data_source_name: The name of the data source for which the resolver is being created.
        :param request_mapping_template: The mapping template to use for requests.
        :param response_mapping_template: The mapping template to use for responses from the data source.
        :param kind: The resolver type.
        :param pipeline_config: The ``PipelineConfig``.
        :param sync_config: The ``SyncConfig`` for a resolver attached to a versioned data source.
        :param caching_config: The caching configuration for the resolver.
        :param max_batch_size: The maximum batching size for a resolver.
        :param runtime: Describes a runtime used by an Amazon Web Services AppSync pipeline
        resolver or Amazon Web Services AppSync function.
        :param code: The ``resolver`` code that contains the request and response functions.
        :param metrics_config: Enables or disables enhanced resolver metrics for specified resolvers.
        :returns: CreateResolverResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("CreateType")
    def create_type(
        self,
        context: RequestContext,
        api_id: String,
        definition: String,
        format: TypeDefinitionFormat,
        **kwargs,
    ) -> CreateTypeResponse:
        """Creates a ``Type`` object.

        :param api_id: The API ID.
        :param definition: The type definition, in GraphQL Schema Definition Language (SDL) format.
        :param format: The type format: SDL or JSON.
        :returns: CreateTypeResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("DeleteApi")
    def delete_api(self, context: RequestContext, api_id: String, **kwargs) -> DeleteApiResponse:
        """Deletes an ``Api`` object

        :param api_id: The ``Api`` ID.
        :returns: DeleteApiResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DeleteApiCache")
    def delete_api_cache(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> DeleteApiCacheResponse:
        """Deletes an ``ApiCache`` object.

        :param api_id: The API ID.
        :returns: DeleteApiCacheResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("DeleteApiKey")
    def delete_api_key(
        self, context: RequestContext, api_id: String, id: String, **kwargs
    ) -> DeleteApiKeyResponse:
        """Deletes an API key.

        :param api_id: The API ID.
        :param id: The ID for the API key.
        :returns: DeleteApiKeyResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("DeleteChannelNamespace")
    def delete_channel_namespace(
        self, context: RequestContext, api_id: String, name: Namespace, **kwargs
    ) -> DeleteChannelNamespaceResponse:
        """Deletes a ``ChannelNamespace``.

        :param api_id: The ID of the ``Api`` associated with the ``ChannelNamespace``.
        :param name: The name of the ``ChannelNamespace``.
        :returns: DeleteChannelNamespaceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DeleteDataSource")
    def delete_data_source(
        self, context: RequestContext, api_id: String, name: ResourceName, **kwargs
    ) -> DeleteDataSourceResponse:
        """Deletes a ``DataSource`` object.

        :param api_id: The API ID.
        :param name: The name of the data source.
        :returns: DeleteDataSourceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("DeleteDomainName")
    def delete_domain_name(
        self, context: RequestContext, domain_name: DomainName, **kwargs
    ) -> DeleteDomainNameResponse:
        """Deletes a custom ``DomainName`` object.

        :param domain_name: The domain name.
        :returns: DeleteDomainNameResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteFunction")
    def delete_function(
        self, context: RequestContext, api_id: String, function_id: ResourceName, **kwargs
    ) -> DeleteFunctionResponse:
        """Deletes a ``Function``.

        :param api_id: The GraphQL API ID.
        :param function_id: The ``Function`` ID.
        :returns: DeleteFunctionResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteGraphqlApi")
    def delete_graphql_api(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> DeleteGraphqlApiResponse:
        """Deletes a ``GraphqlApi`` object.

        :param api_id: The API ID.
        :returns: DeleteGraphqlApiResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DeleteResolver")
    def delete_resolver(
        self,
        context: RequestContext,
        api_id: String,
        type_name: ResourceName,
        field_name: ResourceName,
        **kwargs,
    ) -> DeleteResolverResponse:
        """Deletes a ``Resolver`` object.

        :param api_id: The API ID.
        :param type_name: The name of the resolver type.
        :param field_name: The resolver field name.
        :returns: DeleteResolverResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("DeleteType")
    def delete_type(
        self, context: RequestContext, api_id: String, type_name: ResourceName, **kwargs
    ) -> DeleteTypeResponse:
        """Deletes a ``Type`` object.

        :param api_id: The API ID.
        :param type_name: The type name.
        :returns: DeleteTypeResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("DisassociateApi")
    def disassociate_api(
        self, context: RequestContext, domain_name: DomainName, **kwargs
    ) -> DisassociateApiResponse:
        """Removes an ``ApiAssociation`` object from a custom domain.

        :param domain_name: The domain name.
        :returns: DisassociateApiResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("DisassociateMergedGraphqlApi")
    def disassociate_merged_graphql_api(
        self,
        context: RequestContext,
        source_api_identifier: String,
        association_id: String,
        **kwargs,
    ) -> DisassociateMergedGraphqlApiResponse:
        """Deletes an association between a Merged API and source API using the
        source API's identifier and the association ID.

        :param source_api_identifier: The identifier of the AppSync Source API.
        :param association_id: The ID generated by the AppSync service for the source API association.
        :returns: DisassociateMergedGraphqlApiResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DisassociateSourceGraphqlApi")
    def disassociate_source_graphql_api(
        self,
        context: RequestContext,
        merged_api_identifier: String,
        association_id: String,
        **kwargs,
    ) -> DisassociateSourceGraphqlApiResponse:
        """Deletes an association between a Merged API and source API using the
        Merged API's identifier and the association ID.

        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :param association_id: The ID generated by the AppSync service for the source API association.
        :returns: DisassociateSourceGraphqlApiResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("EvaluateCode", expand=False)
    def evaluate_code(
        self, context: RequestContext, request: EvaluateCodeRequest, **kwargs
    ) -> EvaluateCodeResponse:
        """Evaluates the given code and returns the response. The code definition
        requirements depend on the specified runtime. For ``APPSYNC_JS``
        runtimes, the code defines the request and response functions. The
        request function takes the incoming request after a GraphQL operation is
        parsed and converts it into a request configuration for the selected
        data source operation. The response function interprets responses from
        the data source and maps it to the shape of the GraphQL field output
        type.

        :param runtime: The runtime to be used when evaluating the code.
        :param code: The code definition to be evaluated.
        :param context: The map that holds all of the contextual information for your resolver
        invocation.
        :param function: The function within the code to be evaluated.
        :returns: EvaluateCodeResponse
        :raises AccessDeniedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("EvaluateMappingTemplate", expand=False)
    def evaluate_mapping_template(
        self, context: RequestContext, request: EvaluateMappingTemplateRequest, **kwargs
    ) -> EvaluateMappingTemplateResponse:
        """Evaluates a given template and returns the response. The mapping
        template can be a request or response template.

        Request templates take the incoming request after a GraphQL operation is
        parsed and convert it into a request configuration for the selected data
        source operation. Response templates interpret responses from the data
        source and map it to the shape of the GraphQL field output type.

        Mapping templates are written in the Apache Velocity Template Language
        (VTL).

        :param template: The mapping template; this can be a request or response template.
        :param context: The map that holds all of the contextual information for your resolver
        invocation.
        :returns: EvaluateMappingTemplateResponse
        :raises AccessDeniedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("FlushApiCache")
    def flush_api_cache(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> FlushApiCacheResponse:
        """Flushes an ``ApiCache`` object.

        :param api_id: The API ID.
        :returns: FlushApiCacheResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("GetApi")
    def get_api(self, context: RequestContext, api_id: String, **kwargs) -> GetApiResponse:
        """Retrieves an ``Api`` object.

        :param api_id: The ``Api`` ID.
        :returns: GetApiResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("GetApiAssociation")
    def get_api_association(
        self, context: RequestContext, domain_name: DomainName, **kwargs
    ) -> GetApiAssociationResponse:
        """Retrieves an ``ApiAssociation`` object.

        :param domain_name: The domain name.
        :returns: GetApiAssociationResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("GetApiCache")
    def get_api_cache(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> GetApiCacheResponse:
        """Retrieves an ``ApiCache`` object.

        :param api_id: The API ID.
        :returns: GetApiCacheResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("GetChannelNamespace")
    def get_channel_namespace(
        self, context: RequestContext, api_id: String, name: Namespace, **kwargs
    ) -> GetChannelNamespaceResponse:
        """Retrieves the channel namespace for a specified ``Api``.

        :param api_id: The ``Api`` ID.
        :param name: The name of the ``ChannelNamespace``.
        :returns: GetChannelNamespaceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("GetDataSource")
    def get_data_source(
        self, context: RequestContext, api_id: String, name: ResourceName, **kwargs
    ) -> GetDataSourceResponse:
        """Retrieves a ``DataSource`` object.

        :param api_id: The API ID.
        :param name: The name of the data source.
        :returns: GetDataSourceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("GetDataSourceIntrospection")
    def get_data_source_introspection(
        self,
        context: RequestContext,
        introspection_id: String,
        include_models_sdl: Boolean | None = None,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> GetDataSourceIntrospectionResponse:
        """Retrieves the record of an existing introspection. If the retrieval is
        successful, the result of the instrospection will also be returned. If
        the retrieval fails the operation, an error message will be returned
        instead.

        :param introspection_id: The introspection ID.
        :param include_models_sdl: A boolean flag that determines whether SDL should be generated for
        introspected types.
        :param next_token: Determines the number of types to be returned in a single response
        before paginating.
        :param max_results: The maximum number of introspected types that will be returned in a
        single response.
        :returns: GetDataSourceIntrospectionResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("GetDomainName")
    def get_domain_name(
        self, context: RequestContext, domain_name: DomainName, **kwargs
    ) -> GetDomainNameResponse:
        """Retrieves a custom ``DomainName`` object.

        :param domain_name: The domain name.
        :returns: GetDomainNameResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("GetFunction")
    def get_function(
        self, context: RequestContext, api_id: String, function_id: ResourceName, **kwargs
    ) -> GetFunctionResponse:
        """Get a ``Function``.

        :param api_id: The GraphQL API ID.
        :param function_id: The ``Function`` ID.
        :returns: GetFunctionResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        """
        raise NotImplementedError

    @handler("GetGraphqlApi")
    def get_graphql_api(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> GetGraphqlApiResponse:
        """Retrieves a ``GraphqlApi`` object.

        :param api_id: The API ID for the GraphQL API.
        :returns: GetGraphqlApiResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("GetGraphqlApiEnvironmentVariables")
    def get_graphql_api_environment_variables(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> GetGraphqlApiEnvironmentVariablesResponse:
        """Retrieves the list of environmental variable key-value pairs associated
        with an API by its ID value.

        :param api_id: The ID of the API from which the environmental variable list will be
        retrieved.
        :returns: GetGraphqlApiEnvironmentVariablesResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("GetIntrospectionSchema")
    def get_introspection_schema(
        self,
        context: RequestContext,
        api_id: String,
        format: OutputType,
        include_directives: BooleanValue | None = None,
        **kwargs,
    ) -> GetIntrospectionSchemaResponse:
        """Retrieves the introspection schema for a GraphQL API.

        :param api_id: The API ID.
        :param format: The schema format: SDL or JSON.
        :param include_directives: A flag that specifies whether the schema introspection should contain
        directives.
        :returns: GetIntrospectionSchemaResponse
        :raises GraphQLSchemaException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("GetResolver")
    def get_resolver(
        self,
        context: RequestContext,
        api_id: String,
        type_name: ResourceName,
        field_name: ResourceName,
        **kwargs,
    ) -> GetResolverResponse:
        """Retrieves a ``Resolver`` object.

        :param api_id: The API ID.
        :param type_name: The resolver type name.
        :param field_name: The resolver field name.
        :returns: GetResolverResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        """
        raise NotImplementedError

    @handler("GetSchemaCreationStatus")
    def get_schema_creation_status(
        self, context: RequestContext, api_id: String, **kwargs
    ) -> GetSchemaCreationStatusResponse:
        """Retrieves the current status of a schema creation operation.

        :param api_id: The API ID.
        :returns: GetSchemaCreationStatusResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("GetSourceApiAssociation")
    def get_source_api_association(
        self,
        context: RequestContext,
        merged_api_identifier: String,
        association_id: String,
        **kwargs,
    ) -> GetSourceApiAssociationResponse:
        """Retrieves a ``SourceApiAssociation`` object.

        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :param association_id: The ID generated by the AppSync service for the source API association.
        :returns: GetSourceApiAssociationResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("GetType")
    def get_type(
        self,
        context: RequestContext,
        api_id: String,
        type_name: ResourceName,
        format: TypeDefinitionFormat,
        **kwargs,
    ) -> GetTypeResponse:
        """Retrieves a ``Type`` object.

        :param api_id: The API ID.
        :param type_name: The type name.
        :param format: The type format: SDL or JSON.
        :returns: GetTypeResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListApiKeys")
    def list_api_keys(
        self,
        context: RequestContext,
        api_id: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListApiKeysResponse:
        """Lists the API keys for a given API.

        API keys are deleted automatically 60 days after they expire. However,
        they may still be included in the response until they have actually been
        deleted. You can safely call ``DeleteApiKey`` to manually delete a key
        before it's automatically deleted.

        :param api_id: The API ID.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListApiKeysResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListApis")
    def list_apis(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListApisResponse:
        """Lists the APIs in your AppSync account.

        ``ListApis`` returns only the high level API details. For more detailed
        information about an API, use ``GetApi``.

        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListApisResponse
        :raises BadRequestException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListChannelNamespaces")
    def list_channel_namespaces(
        self,
        context: RequestContext,
        api_id: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListChannelNamespacesResponse:
        """Lists the channel namespaces for a specified ``Api``.

        ``ListChannelNamespaces`` returns only high level details for the
        channel namespace. To retrieve code handlers, use
        ``GetChannelNamespace``.

        :param api_id: The ``Api`` ID.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListChannelNamespacesResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListDataSources")
    def list_data_sources(
        self,
        context: RequestContext,
        api_id: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListDataSourcesResponse:
        """Lists the data sources for a given API.

        :param api_id: The API ID.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListDataSourcesResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListDomainNames")
    def list_domain_names(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListDomainNamesResponse:
        """Lists multiple custom domain names.

        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListDomainNamesResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListFunctions")
    def list_functions(
        self,
        context: RequestContext,
        api_id: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListFunctionsResponse:
        """List multiple functions.

        :param api_id: The GraphQL API ID.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListFunctionsResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListGraphqlApis")
    def list_graphql_apis(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        api_type: GraphQLApiType | None = None,
        owner: Ownership | None = None,
        **kwargs,
    ) -> ListGraphqlApisResponse:
        """Lists your GraphQL APIs.

        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :param api_type: The value that indicates whether the GraphQL API is a standard API
        (``GRAPHQL``) or merged API (``MERGED``).
        :param owner: The account owner of the GraphQL API.
        :returns: ListGraphqlApisResponse
        :raises BadRequestException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListResolvers")
    def list_resolvers(
        self,
        context: RequestContext,
        api_id: String,
        type_name: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListResolversResponse:
        """Lists the resolvers for a given API and type.

        :param api_id: The API ID.
        :param type_name: The type name.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListResolversResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListResolversByFunction")
    def list_resolvers_by_function(
        self,
        context: RequestContext,
        api_id: String,
        function_id: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListResolversByFunctionResponse:
        """List the resolvers that are associated with a specific function.

        :param api_id: The API ID.
        :param function_id: The function ID.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListResolversByFunctionResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListSourceApiAssociations")
    def list_source_api_associations(
        self,
        context: RequestContext,
        api_id: String,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListSourceApiAssociationsResponse:
        """Lists the ``SourceApiAssociationSummary`` data.

        :param api_id: The API ID.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListSourceApiAssociationsResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: ResourceArn, **kwargs
    ) -> ListTagsForResourceResponse:
        """Lists the tags for a resource.

        :param resource_arn: The ``GraphqlApi`` Amazon Resource Name (ARN).
        :returns: ListTagsForResourceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises LimitExceededException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("ListTypes")
    def list_types(
        self,
        context: RequestContext,
        api_id: String,
        format: TypeDefinitionFormat,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListTypesResponse:
        """Lists the types for a given API.

        :param api_id: The API ID.
        :param format: The type format: SDL or JSON.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListTypesResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("ListTypesByAssociation")
    def list_types_by_association(
        self,
        context: RequestContext,
        merged_api_identifier: String,
        association_id: String,
        format: TypeDefinitionFormat,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListTypesByAssociationResponse:
        """Lists ``Type`` objects by the source API association ID.

        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :param association_id: The ID generated by the AppSync service for the source API association.
        :param format: The format type.
        :param next_token: An identifier that was returned from the previous call to this
        operation, which you can use to return the next set of items in the
        list.
        :param max_results: The maximum number of results that you want the request to return.
        :returns: ListTypesByAssociationResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("PutGraphqlApiEnvironmentVariables")
    def put_graphql_api_environment_variables(
        self,
        context: RequestContext,
        api_id: String,
        environment_variables: EnvironmentVariableMap,
        **kwargs,
    ) -> PutGraphqlApiEnvironmentVariablesResponse:
        """Creates a list of environmental variables in an API by its ID value.

        When creating an environmental variable, it must follow the constraints
        below:

        -  Both JavaScript and VTL templates support environmental variables.

        -  Environmental variables are not evaluated before function invocation.

        -  Environmental variables only support string values.

        -  Any defined value in an environmental variable is considered a string
           literal and not expanded.

        -  Variable evaluations should ideally be performed in the function
           code.

        When creating an environmental variable key-value pair, it must follow
        the additional constraints below:

        -  Keys must begin with a letter.

        -  Keys must be at least two characters long.

        -  Keys can only contain letters, numbers, and the underscore character
           (_).

        -  Values can be up to 512 characters long.

        -  You can configure up to 50 key-value pairs in a GraphQL API.

        You can create a list of environmental variables by adding it to the
        ``environmentVariables`` payload as a list in the format
        ``{"key1":"value1","key2":"value2", …}``. Note that each call of the
        ``PutGraphqlApiEnvironmentVariables`` action will result in the
        overwriting of the existing environmental variable list of that API.
        This means the existing environmental variables will be lost. To avoid
        this, you must include all existing and new environmental variables in
        the list each time you call this action.

        :param api_id: The ID of the API to which the environmental variable list will be
        written.
        :param environment_variables: The list of environmental variables to add to the API.
        :returns: PutGraphqlApiEnvironmentVariablesResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("StartDataSourceIntrospection")
    def start_data_source_introspection(
        self, context: RequestContext, rds_data_api_config: RdsDataApiConfig | None = None, **kwargs
    ) -> StartDataSourceIntrospectionResponse:
        """Creates a new introspection. Returns the ``introspectionId`` of the new
        introspection after its creation.

        :param rds_data_api_config: The ``rdsDataApiConfig`` object data.
        :returns: StartDataSourceIntrospectionResponse
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("StartSchemaCreation")
    def start_schema_creation(
        self, context: RequestContext, api_id: String, definition: Blob, **kwargs
    ) -> StartSchemaCreationResponse:
        """Adds a new schema to your GraphQL API.

        This operation is asynchronous. Use to determine when it has completed.

        :param api_id: The API ID.
        :param definition: The schema definition, in GraphQL schema language format.
        :returns: StartSchemaCreationResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("StartSchemaMerge")
    def start_schema_merge(
        self,
        context: RequestContext,
        association_id: String,
        merged_api_identifier: String,
        **kwargs,
    ) -> StartSchemaMergeResponse:
        """Initiates a merge operation. Returns a status that shows the result of
        the merge operation.

        :param association_id: The ID generated by the AppSync service for the source API association.
        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :returns: StartSchemaMergeResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagMap, **kwargs
    ) -> TagResourceResponse:
        """Tags a resource with user-supplied tags.

        :param resource_arn: The ``GraphqlApi`` Amazon Resource Name (ARN).
        :param tags: A ``TagMap`` object.
        :returns: TagResourceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises LimitExceededException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> UntagResourceResponse:
        """Untags a resource.

        :param resource_arn: The ``GraphqlApi`` Amazon Resource Name (ARN).
        :param tag_keys: A list of ``TagKey`` objects.
        :returns: UntagResourceResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises LimitExceededException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("UpdateApi")
    def update_api(
        self,
        context: RequestContext,
        api_id: String,
        name: ApiName,
        owner_contact: String | None = None,
        event_config: EventConfig | None = None,
        **kwargs,
    ) -> UpdateApiResponse:
        """Updates an ``Api``.

        :param api_id: The ``Api`` ID.
        :param name: The name of the Api.
        :param owner_contact: The owner contact information for the ``Api``.
        :param event_config: The new event configuration.
        :returns: UpdateApiResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("UpdateApiCache", expand=False)
    def update_api_cache(
        self, context: RequestContext, request: UpdateApiCacheRequest, **kwargs
    ) -> UpdateApiCacheResponse:
        """Updates the cache for the GraphQL API.

        :param api_id: The GraphQL API ID.
        :param ttl: TTL in seconds for cache entries.
        :param api_caching_behavior: Caching behavior.
        :param type: The cache instance type.
        :param health_metrics_config: Controls how cache health metrics will be emitted to CloudWatch.
        :returns: UpdateApiCacheResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("UpdateApiKey")
    def update_api_key(
        self,
        context: RequestContext,
        api_id: String,
        id: String,
        description: String | None = None,
        expires: Long | None = None,
        **kwargs,
    ) -> UpdateApiKeyResponse:
        """Updates an API key. You can update the key as long as it's not deleted.

        :param api_id: The ID for the GraphQL API.
        :param id: The API key ID.
        :param description: A description of the purpose of the API key.
        :param expires: From the update time, the time after which the API key expires.
        :returns: UpdateApiKeyResponse
        :raises BadRequestException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises LimitExceededException:
        :raises InternalFailureException:
        :raises ApiKeyValidityOutOfBoundsException:
        """
        raise NotImplementedError

    @handler("UpdateChannelNamespace")
    def update_channel_namespace(
        self,
        context: RequestContext,
        api_id: String,
        name: Namespace,
        subscribe_auth_modes: AuthModes | None = None,
        publish_auth_modes: AuthModes | None = None,
        code_handlers: Code | None = None,
        handler_configs: HandlerConfigs | None = None,
        **kwargs,
    ) -> UpdateChannelNamespaceResponse:
        """Updates a ``ChannelNamespace`` associated with an ``Api``.

        :param api_id: The ``Api`` ID.
        :param name: The name of the ``ChannelNamespace``.
        :param subscribe_auth_modes: The authorization mode to use for subscribing to messages on the channel
        namespace.
        :param publish_auth_modes: The authorization mode to use for publishing messages on the channel
        namespace.
        :param code_handlers: The event handler functions that run custom business logic to process
        published events and subscribe requests.
        :param handler_configs: The configuration for the ``OnPublish`` and ``OnSubscribe`` handlers.
        :returns: UpdateChannelNamespaceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("UpdateDataSource", expand=False)
    def update_data_source(
        self, context: RequestContext, request: UpdateDataSourceRequest, **kwargs
    ) -> UpdateDataSourceResponse:
        """Updates a ``DataSource`` object.

        :param api_id: The API ID.
        :param name: The new name for the data source.
        :param type: The new data source type.
        :param description: The new description for the data source.
        :param service_role_arn: The new service role Amazon Resource Name (ARN) for the data source.
        :param dynamodb_config: The new Amazon DynamoDB configuration.
        :param lambda_config: The new Lambda configuration.
        :param elasticsearch_config: The new OpenSearch configuration.
        :param open_search_service_config: The new OpenSearch configuration.
        :param http_config: The new HTTP endpoint configuration.
        :param relational_database_config: The new relational database configuration.
        :param event_bridge_config: The new Amazon EventBridge settings.
        :param metrics_config: Enables or disables enhanced data source metrics for specified data
        sources.
        :returns: UpdateDataSourceResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError

    @handler("UpdateDomainName")
    def update_domain_name(
        self,
        context: RequestContext,
        domain_name: DomainName,
        description: Description | None = None,
        **kwargs,
    ) -> UpdateDomainNameResponse:
        """Updates a custom ``DomainName`` object.

        :param domain_name: The domain name.
        :param description: A description of the ``DomainName``.
        :returns: UpdateDomainNameResponse
        :raises AccessDeniedException:
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises InternalFailureException:
        :raises NotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateFunction")
    def update_function(
        self,
        context: RequestContext,
        api_id: String,
        name: ResourceName,
        function_id: ResourceName,
        data_source_name: ResourceName,
        description: String | None = None,
        request_mapping_template: MappingTemplate | None = None,
        response_mapping_template: MappingTemplate | None = None,
        function_version: String | None = None,
        sync_config: SyncConfig | None = None,
        max_batch_size: MaxBatchSize | None = None,
        runtime: AppSyncRuntime | None = None,
        code: Code | None = None,
        **kwargs,
    ) -> UpdateFunctionResponse:
        """Updates a ``Function`` object.

        :param api_id: The GraphQL API ID.
        :param name: The ``Function`` name.
        :param function_id: The function ID.
        :param data_source_name: The ``Function`` ``DataSource`` name.
        :param description: The ``Function`` description.
        :param request_mapping_template: The ``Function`` request mapping template.
        :param response_mapping_template: The ``Function`` request mapping template.
        :param function_version: The ``version`` of the request mapping template.
        :param sync_config: Describes a Sync configuration for a resolver.
        :param max_batch_size: The maximum batching size for a resolver.
        :param runtime: Describes a runtime used by an Amazon Web Services AppSync pipeline
        resolver or Amazon Web Services AppSync function.
        :param code: The ``function`` code that contains the request and response functions.
        :returns: UpdateFunctionResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("UpdateGraphqlApi")
    def update_graphql_api(
        self,
        context: RequestContext,
        api_id: String,
        name: String,
        authentication_type: AuthenticationType,
        log_config: LogConfig | None = None,
        user_pool_config: UserPoolConfig | None = None,
        open_id_connect_config: OpenIDConnectConfig | None = None,
        additional_authentication_providers: AdditionalAuthenticationProviders | None = None,
        xray_enabled: Boolean | None = None,
        lambda_authorizer_config: LambdaAuthorizerConfig | None = None,
        merged_api_execution_role_arn: String | None = None,
        owner_contact: String | None = None,
        introspection_config: GraphQLApiIntrospectionConfig | None = None,
        query_depth_limit: QueryDepthLimit | None = None,
        resolver_count_limit: ResolverCountLimit | None = None,
        enhanced_metrics_config: EnhancedMetricsConfig | None = None,
        **kwargs,
    ) -> UpdateGraphqlApiResponse:
        """Updates a ``GraphqlApi`` object.

        :param api_id: The API ID.
        :param name: The new name for the ``GraphqlApi`` object.
        :param authentication_type: The new authentication type for the ``GraphqlApi`` object.
        :param log_config: The Amazon CloudWatch Logs configuration for the ``GraphqlApi`` object.
        :param user_pool_config: The new Amazon Cognito user pool configuration for the ``~GraphqlApi``
        object.
        :param open_id_connect_config: The OpenID Connect configuration for the ``GraphqlApi`` object.
        :param additional_authentication_providers: A list of additional authentication providers for the ``GraphqlApi``
        API.
        :param xray_enabled: A flag indicating whether to use X-Ray tracing for the ``GraphqlApi``.
        :param lambda_authorizer_config: Configuration for Lambda function authorization.
        :param merged_api_execution_role_arn: The Identity and Access Management service role ARN for a merged API.
        :param owner_contact: The owner contact information for an API resource.
        :param introspection_config: Sets the value of the GraphQL API to enable (``ENABLED``) or disable
        (``DISABLED``) introspection.
        :param query_depth_limit: The maximum depth a query can have in a single request.
        :param resolver_count_limit: The maximum number of resolvers that can be invoked in a single request.
        :param enhanced_metrics_config: The ``enhancedMetricsConfig`` object.
        :returns: UpdateGraphqlApiResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("UpdateResolver")
    def update_resolver(
        self,
        context: RequestContext,
        api_id: String,
        type_name: ResourceName,
        field_name: ResourceName,
        data_source_name: ResourceName | None = None,
        request_mapping_template: MappingTemplate | None = None,
        response_mapping_template: MappingTemplate | None = None,
        kind: ResolverKind | None = None,
        pipeline_config: PipelineConfig | None = None,
        sync_config: SyncConfig | None = None,
        caching_config: CachingConfig | None = None,
        max_batch_size: MaxBatchSize | None = None,
        runtime: AppSyncRuntime | None = None,
        code: Code | None = None,
        metrics_config: ResolverLevelMetricsConfig | None = None,
        **kwargs,
    ) -> UpdateResolverResponse:
        """Updates a ``Resolver`` object.

        :param api_id: The API ID.
        :param type_name: The new type name.
        :param field_name: The new field name.
        :param data_source_name: The new data source name.
        :param request_mapping_template: The new request mapping template.
        :param response_mapping_template: The new response mapping template.
        :param kind: The resolver type.
        :param pipeline_config: The ``PipelineConfig``.
        :param sync_config: The ``SyncConfig`` for a resolver attached to a versioned data source.
        :param caching_config: The caching configuration for the resolver.
        :param max_batch_size: The maximum batching size for a resolver.
        :param runtime: Describes a runtime used by an Amazon Web Services AppSync pipeline
        resolver or Amazon Web Services AppSync function.
        :param code: The ``resolver`` code that contains the request and response functions.
        :param metrics_config: Enables or disables enhanced resolver metrics for specified resolvers.
        :returns: UpdateResolverResponse
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        :raises BadRequestException:
        """
        raise NotImplementedError

    @handler("UpdateSourceApiAssociation")
    def update_source_api_association(
        self,
        context: RequestContext,
        association_id: String,
        merged_api_identifier: String,
        description: String | None = None,
        source_api_association_config: SourceApiAssociationConfig | None = None,
        **kwargs,
    ) -> UpdateSourceApiAssociationResponse:
        """Updates some of the configuration choices of a particular source API
        association.

        :param association_id: The ID generated by the AppSync service for the source API association.
        :param merged_api_identifier: The identifier of the AppSync Merged API.
        :param description: The description field.
        :param source_api_association_config: The ``SourceApiAssociationConfig`` object data.
        :returns: UpdateSourceApiAssociationResponse
        :raises UnauthorizedException:
        :raises BadRequestException:
        :raises InternalFailureException:
        :raises NotFoundException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UpdateType")
    def update_type(
        self,
        context: RequestContext,
        api_id: String,
        type_name: ResourceName,
        format: TypeDefinitionFormat,
        definition: String | None = None,
        **kwargs,
    ) -> UpdateTypeResponse:
        """Updates a ``Type`` object.

        :param api_id: The API ID.
        :param type_name: The new type name.
        :param format: The new type format: SDL or JSON.
        :param definition: The new definition.
        :returns: UpdateTypeResponse
        :raises BadRequestException:
        :raises ConcurrentModificationException:
        :raises NotFoundException:
        :raises UnauthorizedException:
        :raises InternalFailureException:
        """
        raise NotImplementedError
