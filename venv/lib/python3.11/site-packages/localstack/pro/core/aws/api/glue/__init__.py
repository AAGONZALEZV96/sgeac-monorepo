from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AWSManagedClientApplicationReference = str
AccessToken = str
AccountId = str
AllowedValueDescriptionString = str
AllowedValueValueString = str
ApiVersion = str
ArnString = str
AttemptCount = int
AuditContextString = str
AuthTokenString = str
AuthorizationCode = str
BatchSize = int
BatchWindow = int
BlueprintParameterSpec = str
BlueprintParameters = str
Bool = bool
Boolean = bool
BooleanNullable = bool
BooleanValue = bool
BoxedBoolean = bool
BoxedDoubleFraction = float
BoxedNonNegativeInt = int
BoxedPositiveInt = int
CatalogGetterPageSize = int
CatalogIdString = str
CatalogNameString = str
Category = str
Classification = str
CodeGenArgName = str
CodeGenArgValue = str
CodeGenIdentifier = str
CodeGenNodeType = str
ColumnNameString = str
ColumnTypeString = str
ColumnValuesString = str
CommentString = str
CommitIdString = str
ComputeEnvironmentConfigurationDescriptionString = str
ComputeEnvironmentName = str
ConfigValueString = str
ConnectionName = str
ConnectionSchemaVersion = int
ConnectionString = str
ContextKey = str
ContextValue = str
CrawlId = str
CrawlerConfiguration = str
CrawlerSecurityConfiguration = str
CreatedTimestamp = str
CredentialKey = str
CredentialValue = str
CronExpression = str
CsvColumnDelimiter = str
CsvQuoteSymbol = str
CustomPatterns = str
DQDLString = str
DataLakePrincipalString = str
DataQualityObservationDescription = str
DataQualityRuleResultDescription = str
DataQualityRulesetString = str
DatabaseName = str
DatabrewCondition = str
DatabrewConditionValue = str
Description = str
DescriptionString = str
DescriptionStringRemovable = str
DisplayName = str
Double = float
DoubleValue = float
EnclosedInStringProperty = str
EnclosedInStringPropertyWithQuote = str
EntityDescription = str
EntityFieldName = str
EntityLabel = str
EntityName = str
ErrorCodeString = str
ErrorMessageString = str
ErrorString = str
EventQueueArn = str
ExecutionTime = int
ExtendedString = str
FederationIdentifier = str
FieldDescription = str
FieldLabel = str
FieldType = str
FilterPredicate = str
FilterString = str
FormatString = str
Generic512CharString = str
GenericBoundedDouble = float
GenericLimitedString = str
GenericString = str
GlueResourceArn = str
GlueStudioColumnNameString = str
GlueVersionString = str
GrokPattern = str
HashString = str
IAMRoleArn = str
IdString = str
IdleTimeout = int
Integer = int
IntegerFlag = int
IntegerValue = int
IntegrationDescription = str
IntegrationErrorMessage = str
IntegrationInteger = int
IntegrationString = str
IsParentEntity = bool
IsVersionValid = bool
JobName = str
JsonPath = str
JsonValue = str
JwtToken = str
KeyString = str
KmsKeyArn = str
LabelCount = int
LatestSchemaVersionBoolean = bool
ListTableOptimizerRunsToken = str
LocationString = str
LogGroup = str
LogStream = str
LongValueString = str
MaintenanceWindow = str
MaskValue = str
MaxConcurrentRuns = int
MaxListTableOptimizerRunsTokenResults = int
MaxResults = int
MaxResultsNumber = int
MaxRetries = int
MessagePrefix = str
MessageString = str
MetadataKeyString = str
MetadataValueString = str
NameString = str
NextToken = str
NodeId = str
NodeName = str
NonNegativeDouble = float
NonNegativeInt = int
NonNegativeInteger = int
NotifyDelayAfter = int
NullableBoolean = bool
NullableDouble = float
NullableInteger = int
NullableString = str
NumberTargetPartitionsString = str
Operation = str
OptionKey = str
OptionValue = str
OrchestrationArgumentsValue = str
OrchestrationIAMRoleArn = str
OrchestrationMessageString = str
OrchestrationNameString = str
OrchestrationPageSize200 = int
OrchestrationPageSize25 = int
OrchestrationRoleArn = str
OrchestrationS3Location = str
OrchestrationStatementCodeString = str
OrchestrationToken = str
PageSize = int
PaginationToken = str
ParameterName = str
ParameterValue = str
ParametersMapValue = str
Password = str
Path = str
PolicyJsonString = str
PositiveInteger = int
PredicateString = str
Prob = float
PropertyDescriptionString = str
PropertyKey = str
PropertyName = str
PropertyValue = str
PythonScript = str
PythonVersionString = str
QuerySchemaVersionMetadataMaxResults = int
RecipeVersion = str
RedirectUri = str
RefreshToken = str
ReplaceBoolean = bool
ResourceArnString = str
Role = str
RoleArn = str
RoleString = str
RowTag = str
RunId = str
RuntimeNameString = str
SampleSizePercentage = float
ScalaCode = str
SchemaDefinitionDiff = str
SchemaDefinitionString = str
SchemaPathString = str
SchemaRegistryNameString = str
SchemaRegistryTokenString = str
SchemaValidationError = str
SchemaVersionIdString = str
ScriptLocationString = str
SecretArn = str
SqlQuery = str
StatisticNameString = str
String = str
String128 = str
String2048 = str
TableName = str
TablePrefix = str
TableTypeString = str
TagKey = str
TagValue = str
TargetColumn = str
Timeout = int
Token = str
TokenUrl = str
TokenUrlParameterKey = str
TokenUrlParameterValue = str
Topk = int
TotalSegmentsInteger = int
TransactionIdString = str
TypeString = str
URI = str
UpdatedTimestamp = str
UriString = str
UrlString = str
UserManagedClientApplicationClientId = str
UserManagedClientApplicationClientSecret = str
Username = str
ValueString = str
Vendor = str
VersionString = str
VersionsString = str
ViewDialectVersionString = str
ViewTextString = str
WorkflowDescriptionString = str
databaseNameString = str
double = float
dpuCounts = int
dpuDurationInHour = float
dpuHours = float
glueConnectionNameString = str
tableNameString = str


class AdditionalOptionKeys(StrEnum):
    performanceTuning_caching = "performanceTuning.caching"
    observations_scope = "observations.scope"


class AggFunction(StrEnum):
    avg = "avg"
    countDistinct = "countDistinct"
    count = "count"
    first = "first"
    last = "last"
    kurtosis = "kurtosis"
    max = "max"
    min = "min"
    skewness = "skewness"
    stddev_samp = "stddev_samp"
    stddev_pop = "stddev_pop"
    sum = "sum"
    sumDistinct = "sumDistinct"
    var_samp = "var_samp"
    var_pop = "var_pop"


class AllowFullTableExternalDataAccessEnum(StrEnum):
    True_ = "True"
    False_ = "False"


class AuthenticationType(StrEnum):
    BASIC = "BASIC"
    OAUTH2 = "OAUTH2"
    CUSTOM = "CUSTOM"
    IAM = "IAM"


class BackfillErrorCode(StrEnum):
    ENCRYPTED_PARTITION_ERROR = "ENCRYPTED_PARTITION_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    INVALID_PARTITION_TYPE_DATA_ERROR = "INVALID_PARTITION_TYPE_DATA_ERROR"
    MISSING_PARTITION_VALUE_ERROR = "MISSING_PARTITION_VALUE_ERROR"
    UNSUPPORTED_PARTITION_CHARACTER_ERROR = "UNSUPPORTED_PARTITION_CHARACTER_ERROR"


class BlueprintRunState(StrEnum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    ROLLING_BACK = "ROLLING_BACK"


class BlueprintStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    FAILED = "FAILED"


class CatalogEncryptionMode(StrEnum):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"
    SSE_KMS_WITH_SERVICE_ROLE = "SSE-KMS-WITH-SERVICE-ROLE"


class CloudWatchEncryptionMode(StrEnum):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


class ColumnStatisticsState(StrEnum):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class ColumnStatisticsType(StrEnum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DOUBLE = "DOUBLE"
    LONG = "LONG"
    STRING = "STRING"
    BINARY = "BINARY"


class Comparator(StrEnum):
    EQUALS = "EQUALS"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_EQUALS = "GREATER_THAN_EQUALS"
    LESS_THAN_EQUALS = "LESS_THAN_EQUALS"


class Compatibility(StrEnum):
    NONE = "NONE"
    DISABLED = "DISABLED"
    BACKWARD = "BACKWARD"
    BACKWARD_ALL = "BACKWARD_ALL"
    FORWARD = "FORWARD"
    FORWARD_ALL = "FORWARD_ALL"
    FULL = "FULL"
    FULL_ALL = "FULL_ALL"


class CompressionType(StrEnum):
    gzip = "gzip"
    bzip2 = "bzip2"


class ComputationType(StrEnum):
    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"


class ComputeEnvironment(StrEnum):
    SPARK = "SPARK"
    ATHENA = "ATHENA"
    PYTHON = "PYTHON"


class ConnectionPropertyKey(StrEnum):
    HOST = "HOST"
    PORT = "PORT"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    ENCRYPTED_PASSWORD = "ENCRYPTED_PASSWORD"
    JDBC_DRIVER_JAR_URI = "JDBC_DRIVER_JAR_URI"
    JDBC_DRIVER_CLASS_NAME = "JDBC_DRIVER_CLASS_NAME"
    JDBC_ENGINE = "JDBC_ENGINE"
    JDBC_ENGINE_VERSION = "JDBC_ENGINE_VERSION"
    CONFIG_FILES = "CONFIG_FILES"
    INSTANCE_ID = "INSTANCE_ID"
    JDBC_CONNECTION_URL = "JDBC_CONNECTION_URL"
    JDBC_ENFORCE_SSL = "JDBC_ENFORCE_SSL"
    CUSTOM_JDBC_CERT = "CUSTOM_JDBC_CERT"
    SKIP_CUSTOM_JDBC_CERT_VALIDATION = "SKIP_CUSTOM_JDBC_CERT_VALIDATION"
    CUSTOM_JDBC_CERT_STRING = "CUSTOM_JDBC_CERT_STRING"
    CONNECTION_URL = "CONNECTION_URL"
    KAFKA_BOOTSTRAP_SERVERS = "KAFKA_BOOTSTRAP_SERVERS"
    KAFKA_SSL_ENABLED = "KAFKA_SSL_ENABLED"
    KAFKA_CUSTOM_CERT = "KAFKA_CUSTOM_CERT"
    KAFKA_SKIP_CUSTOM_CERT_VALIDATION = "KAFKA_SKIP_CUSTOM_CERT_VALIDATION"
    KAFKA_CLIENT_KEYSTORE = "KAFKA_CLIENT_KEYSTORE"
    KAFKA_CLIENT_KEYSTORE_PASSWORD = "KAFKA_CLIENT_KEYSTORE_PASSWORD"
    KAFKA_CLIENT_KEY_PASSWORD = "KAFKA_CLIENT_KEY_PASSWORD"
    ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD = "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD"
    ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD = "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD"
    KAFKA_SASL_MECHANISM = "KAFKA_SASL_MECHANISM"
    KAFKA_SASL_PLAIN_USERNAME = "KAFKA_SASL_PLAIN_USERNAME"
    KAFKA_SASL_PLAIN_PASSWORD = "KAFKA_SASL_PLAIN_PASSWORD"
    ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD = "ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD"
    KAFKA_SASL_SCRAM_USERNAME = "KAFKA_SASL_SCRAM_USERNAME"
    KAFKA_SASL_SCRAM_PASSWORD = "KAFKA_SASL_SCRAM_PASSWORD"
    KAFKA_SASL_SCRAM_SECRETS_ARN = "KAFKA_SASL_SCRAM_SECRETS_ARN"
    ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD = "ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD"
    KAFKA_SASL_GSSAPI_KEYTAB = "KAFKA_SASL_GSSAPI_KEYTAB"
    KAFKA_SASL_GSSAPI_KRB5_CONF = "KAFKA_SASL_GSSAPI_KRB5_CONF"
    KAFKA_SASL_GSSAPI_SERVICE = "KAFKA_SASL_GSSAPI_SERVICE"
    KAFKA_SASL_GSSAPI_PRINCIPAL = "KAFKA_SASL_GSSAPI_PRINCIPAL"
    SECRET_ID = "SECRET_ID"
    CONNECTOR_URL = "CONNECTOR_URL"
    CONNECTOR_TYPE = "CONNECTOR_TYPE"
    CONNECTOR_CLASS_NAME = "CONNECTOR_CLASS_NAME"
    ENDPOINT = "ENDPOINT"
    ENDPOINT_TYPE = "ENDPOINT_TYPE"
    ROLE_ARN = "ROLE_ARN"
    REGION = "REGION"
    WORKGROUP_NAME = "WORKGROUP_NAME"
    CLUSTER_IDENTIFIER = "CLUSTER_IDENTIFIER"
    DATABASE = "DATABASE"


class ConnectionStatus(StrEnum):
    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class ConnectionType(StrEnum):
    JDBC = "JDBC"
    SFTP = "SFTP"
    MONGODB = "MONGODB"
    KAFKA = "KAFKA"
    NETWORK = "NETWORK"
    MARKETPLACE = "MARKETPLACE"
    CUSTOM = "CUSTOM"
    SALESFORCE = "SALESFORCE"
    VIEW_VALIDATION_REDSHIFT = "VIEW_VALIDATION_REDSHIFT"
    VIEW_VALIDATION_ATHENA = "VIEW_VALIDATION_ATHENA"
    GOOGLEADS = "GOOGLEADS"
    GOOGLESHEETS = "GOOGLESHEETS"
    GOOGLEANALYTICS4 = "GOOGLEANALYTICS4"
    SERVICENOW = "SERVICENOW"
    MARKETO = "MARKETO"
    SAPODATA = "SAPODATA"
    ZENDESK = "ZENDESK"
    JIRACLOUD = "JIRACLOUD"
    NETSUITEERP = "NETSUITEERP"
    HUBSPOT = "HUBSPOT"
    FACEBOOKADS = "FACEBOOKADS"
    INSTAGRAMADS = "INSTAGRAMADS"
    ZOHOCRM = "ZOHOCRM"
    SALESFORCEPARDOT = "SALESFORCEPARDOT"
    SALESFORCEMARKETINGCLOUD = "SALESFORCEMARKETINGCLOUD"
    SLACK = "SLACK"
    STRIPE = "STRIPE"
    INTERCOM = "INTERCOM"
    SNAPCHATADS = "SNAPCHATADS"


class CrawlState(StrEnum):
    RUNNING = "RUNNING"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    ERROR = "ERROR"


class CrawlerHistoryState(StrEnum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOPPED = "STOPPED"


class CrawlerLineageSettings(StrEnum):
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class CrawlerState(StrEnum):
    READY = "READY"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"


class CsvHeaderOption(StrEnum):
    UNKNOWN = "UNKNOWN"
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"


class CsvSerdeOption(StrEnum):
    OpenCSVSerDe = "OpenCSVSerDe"
    LazySimpleSerDe = "LazySimpleSerDe"
    None_ = "None"


class DQCompositeRuleEvaluationMethod(StrEnum):
    COLUMN = "COLUMN"
    ROW = "ROW"


class DQStopJobOnFailureTiming(StrEnum):
    Immediate = "Immediate"
    AfterDataLoad = "AfterDataLoad"


class DQTransformOutput(StrEnum):
    PrimaryInput = "PrimaryInput"
    EvaluationResults = "EvaluationResults"


class DataFormat(StrEnum):
    AVRO = "AVRO"
    JSON = "JSON"
    PROTOBUF = "PROTOBUF"


class DataOperation(StrEnum):
    READ = "READ"
    WRITE = "WRITE"


class DataQualityEncryptionMode(StrEnum):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


class DataQualityModelStatus(StrEnum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class DataQualityRuleResultStatus(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"


class DatabaseAttributes(StrEnum):
    NAME = "NAME"


class DeleteBehavior(StrEnum):
    LOG = "LOG"
    DELETE_FROM_DATABASE = "DELETE_FROM_DATABASE"
    DEPRECATE_IN_DATABASE = "DEPRECATE_IN_DATABASE"


class DeltaTargetCompressionType(StrEnum):
    uncompressed = "uncompressed"
    snappy = "snappy"


class EnableHybridValues(StrEnum):
    TRUE = "TRUE"
    FALSE = "FALSE"


class ExecutionClass(StrEnum):
    FLEX = "FLEX"
    STANDARD = "STANDARD"


class ExecutionStatus(StrEnum):
    FAILED = "FAILED"
    STARTED = "STARTED"


class ExistCondition(StrEnum):
    MUST_EXIST = "MUST_EXIST"
    NOT_EXIST = "NOT_EXIST"
    NONE = "NONE"


class FederationSourceErrorCode(StrEnum):
    AccessDeniedException = "AccessDeniedException"
    EntityNotFoundException = "EntityNotFoundException"
    InvalidCredentialsException = "InvalidCredentialsException"
    InvalidInputException = "InvalidInputException"
    InvalidResponseException = "InvalidResponseException"
    OperationTimeoutException = "OperationTimeoutException"
    OperationNotSupportedException = "OperationNotSupportedException"
    InternalServiceException = "InternalServiceException"
    PartialFailureException = "PartialFailureException"
    ThrottlingException = "ThrottlingException"


class FieldDataType(StrEnum):
    INT = "INT"
    SMALLINT = "SMALLINT"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    LONG = "LONG"
    DATE = "DATE"
    BOOLEAN = "BOOLEAN"
    MAP = "MAP"
    ARRAY = "ARRAY"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    DECIMAL = "DECIMAL"
    BYTE = "BYTE"
    SHORT = "SHORT"
    DOUBLE = "DOUBLE"
    STRUCT = "STRUCT"


class FieldFilterOperator(StrEnum):
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    BETWEEN = "BETWEEN"
    EQUAL_TO = "EQUAL_TO"
    NOT_EQUAL_TO = "NOT_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    CONTAINS = "CONTAINS"
    ORDER_BY = "ORDER_BY"


class FieldName(StrEnum):
    CRAWL_ID = "CRAWL_ID"
    STATE = "STATE"
    START_TIME = "START_TIME"
    END_TIME = "END_TIME"
    DPU_HOUR = "DPU_HOUR"


class FilterLogicalOperator(StrEnum):
    AND = "AND"
    OR = "OR"


class FilterOperation(StrEnum):
    EQ = "EQ"
    LT = "LT"
    GT = "GT"
    LTE = "LTE"
    GTE = "GTE"
    REGEX = "REGEX"
    ISNULL = "ISNULL"


class FilterOperator(StrEnum):
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"
    EQ = "EQ"
    NE = "NE"


class FilterValueType(StrEnum):
    COLUMNEXTRACTED = "COLUMNEXTRACTED"
    CONSTANT = "CONSTANT"


class GlueRecordType(StrEnum):
    DATE = "DATE"
    STRING = "STRING"
    TIMESTAMP = "TIMESTAMP"
    INT = "INT"
    FLOAT = "FLOAT"
    LONG = "LONG"
    BIGDECIMAL = "BIGDECIMAL"
    BYTE = "BYTE"
    SHORT = "SHORT"
    DOUBLE = "DOUBLE"


class HudiTargetCompressionType(StrEnum):
    gzip = "gzip"
    lzo = "lzo"
    uncompressed = "uncompressed"
    snappy = "snappy"


class HyperTargetCompressionType(StrEnum):
    uncompressed = "uncompressed"


class IcebergTargetCompressionType(StrEnum):
    gzip = "gzip"
    lzo = "lzo"
    uncompressed = "uncompressed"
    snappy = "snappy"


class InclusionAnnotationValue(StrEnum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class IntegrationStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    MODIFYING = "MODIFYING"
    FAILED = "FAILED"
    DELETING = "DELETING"
    SYNCING = "SYNCING"
    NEEDS_ATTENTION = "NEEDS_ATTENTION"


class JDBCConnectionType(StrEnum):
    sqlserver = "sqlserver"
    mysql = "mysql"
    oracle = "oracle"
    postgresql = "postgresql"
    redshift = "redshift"


class JDBCDataType(StrEnum):
    ARRAY = "ARRAY"
    BIGINT = "BIGINT"
    BINARY = "BINARY"
    BIT = "BIT"
    BLOB = "BLOB"
    BOOLEAN = "BOOLEAN"
    CHAR = "CHAR"
    CLOB = "CLOB"
    DATALINK = "DATALINK"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    DISTINCT = "DISTINCT"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    JAVA_OBJECT = "JAVA_OBJECT"
    LONGNVARCHAR = "LONGNVARCHAR"
    LONGVARBINARY = "LONGVARBINARY"
    LONGVARCHAR = "LONGVARCHAR"
    NCHAR = "NCHAR"
    NCLOB = "NCLOB"
    NULL = "NULL"
    NUMERIC = "NUMERIC"
    NVARCHAR = "NVARCHAR"
    OTHER = "OTHER"
    REAL = "REAL"
    REF = "REF"
    REF_CURSOR = "REF_CURSOR"
    ROWID = "ROWID"
    SMALLINT = "SMALLINT"
    SQLXML = "SQLXML"
    STRUCT = "STRUCT"
    TIME = "TIME"
    TIME_WITH_TIMEZONE = "TIME_WITH_TIMEZONE"
    TIMESTAMP = "TIMESTAMP"
    TIMESTAMP_WITH_TIMEZONE = "TIMESTAMP_WITH_TIMEZONE"
    TINYINT = "TINYINT"
    VARBINARY = "VARBINARY"
    VARCHAR = "VARCHAR"


class JdbcMetadataEntry(StrEnum):
    COMMENTS = "COMMENTS"
    RAWTYPES = "RAWTYPES"


class JobBookmarksEncryptionMode(StrEnum):
    DISABLED = "DISABLED"
    CSE_KMS = "CSE-KMS"


class JobMode(StrEnum):
    SCRIPT = "SCRIPT"
    VISUAL = "VISUAL"
    NOTEBOOK = "NOTEBOOK"


class JobRunState(StrEnum):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    ERROR = "ERROR"
    WAITING = "WAITING"
    EXPIRED = "EXPIRED"


class JoinType(StrEnum):
    equijoin = "equijoin"
    left = "left"
    right = "right"
    outer = "outer"
    leftsemi = "leftsemi"
    leftanti = "leftanti"


class Language(StrEnum):
    PYTHON = "PYTHON"
    SCALA = "SCALA"


class LastCrawlStatus(StrEnum):
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class Logical(StrEnum):
    AND = "AND"
    ANY = "ANY"


class LogicalOperator(StrEnum):
    EQUALS = "EQUALS"


class MLUserDataEncryptionModeString(StrEnum):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"


class MetadataOperation(StrEnum):
    CREATE = "CREATE"


class NodeType(StrEnum):
    CRAWLER = "CRAWLER"
    JOB = "JOB"
    TRIGGER = "TRIGGER"


class OAuth2GrantType(StrEnum):
    AUTHORIZATION_CODE = "AUTHORIZATION_CODE"
    CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"
    JWT_BEARER = "JWT_BEARER"


class ParamType(StrEnum):
    str = "str"
    int = "int"
    float = "float"
    complex = "complex"
    bool = "bool"
    list = "list"
    null = "null"


class ParquetCompressionType(StrEnum):
    snappy = "snappy"
    lzo = "lzo"
    gzip = "gzip"
    brotli = "brotli"
    lz4 = "lz4"
    uncompressed = "uncompressed"
    none = "none"


class PartitionIndexStatus(StrEnum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    FAILED = "FAILED"


class Permission(StrEnum):
    ALL = "ALL"
    SELECT = "SELECT"
    ALTER = "ALTER"
    DROP = "DROP"
    DELETE = "DELETE"
    INSERT = "INSERT"
    CREATE_DATABASE = "CREATE_DATABASE"
    CREATE_TABLE = "CREATE_TABLE"
    DATA_LOCATION_ACCESS = "DATA_LOCATION_ACCESS"


class PermissionType(StrEnum):
    COLUMN_PERMISSION = "COLUMN_PERMISSION"
    CELL_FILTER_PERMISSION = "CELL_FILTER_PERMISSION"
    NESTED_PERMISSION = "NESTED_PERMISSION"
    NESTED_CELL_PERMISSION = "NESTED_CELL_PERMISSION"


class PiiType(StrEnum):
    RowAudit = "RowAudit"
    RowMasking = "RowMasking"
    ColumnAudit = "ColumnAudit"
    ColumnMasking = "ColumnMasking"


class PrincipalType(StrEnum):
    USER = "USER"
    ROLE = "ROLE"
    GROUP = "GROUP"


class PropertyType(StrEnum):
    USER_INPUT = "USER_INPUT"
    SECRET = "SECRET"
    READ_ONLY = "READ_ONLY"
    UNUSED = "UNUSED"
    SECRET_OR_USER_INPUT = "SECRET_OR_USER_INPUT"


class QuoteChar(StrEnum):
    quote = "quote"
    quillemet = "quillemet"
    single_quote = "single_quote"
    disabled = "disabled"


class RecrawlBehavior(StrEnum):
    CRAWL_EVERYTHING = "CRAWL_EVERYTHING"
    CRAWL_NEW_FOLDERS_ONLY = "CRAWL_NEW_FOLDERS_ONLY"
    CRAWL_EVENT_MODE = "CRAWL_EVENT_MODE"


class RegistryStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"


class ResourceAction(StrEnum):
    UPDATE = "UPDATE"
    CREATE = "CREATE"


class ResourceShareType(StrEnum):
    FOREIGN = "FOREIGN"
    ALL = "ALL"
    FEDERATED = "FEDERATED"


class ResourceState(StrEnum):
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


class ResourceType(StrEnum):
    JAR = "JAR"
    FILE = "FILE"
    ARCHIVE = "ARCHIVE"


class S3EncryptionMode(StrEnum):
    DISABLED = "DISABLED"
    SSE_KMS = "SSE-KMS"
    SSE_S3 = "SSE-S3"


class ScheduleState(StrEnum):
    SCHEDULED = "SCHEDULED"
    NOT_SCHEDULED = "NOT_SCHEDULED"
    TRANSITIONING = "TRANSITIONING"


class ScheduleType(StrEnum):
    CRON = "CRON"
    AUTO = "AUTO"


class SchemaDiffType(StrEnum):
    SYNTAX_DIFF = "SYNTAX_DIFF"


class SchemaStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    DELETING = "DELETING"


class SchemaVersionStatus(StrEnum):
    AVAILABLE = "AVAILABLE"
    PENDING = "PENDING"
    FAILURE = "FAILURE"
    DELETING = "DELETING"


class Separator(StrEnum):
    comma = "comma"
    ctrla = "ctrla"
    pipe = "pipe"
    semicolon = "semicolon"
    tab = "tab"


class SessionStatus(StrEnum):
    PROVISIONING = "PROVISIONING"
    READY = "READY"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class SettingSource(StrEnum):
    CATALOG = "CATALOG"
    TABLE = "TABLE"


class Sort(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


class SortDirectionType(StrEnum):
    DESCENDING = "DESCENDING"
    ASCENDING = "ASCENDING"


class SourceControlAuthStrategy(StrEnum):
    PERSONAL_ACCESS_TOKEN = "PERSONAL_ACCESS_TOKEN"
    AWS_SECRETS_MANAGER = "AWS_SECRETS_MANAGER"


class SourceControlProvider(StrEnum):
    GITHUB = "GITHUB"
    GITLAB = "GITLAB"
    BITBUCKET = "BITBUCKET"
    AWS_CODE_COMMIT = "AWS_CODE_COMMIT"


class StartingPosition(StrEnum):
    latest = "latest"
    trim_horizon = "trim_horizon"
    earliest = "earliest"
    timestamp = "timestamp"


class StatementState(StrEnum):
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    AVAILABLE = "AVAILABLE"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    ERROR = "ERROR"


class StatisticEvaluationLevel(StrEnum):
    Dataset = "Dataset"
    Column = "Column"
    Multicolumn = "Multicolumn"


class TableAttributes(StrEnum):
    NAME = "NAME"
    TABLE_TYPE = "TABLE_TYPE"


class TableOptimizerEventType(StrEnum):
    starting = "starting"
    completed = "completed"
    failed = "failed"
    in_progress = "in_progress"


class TableOptimizerType(StrEnum):
    compaction = "compaction"
    retention = "retention"
    orphan_file_deletion = "orphan_file_deletion"


class TargetFormat(StrEnum):
    json = "json"
    csv = "csv"
    avro = "avro"
    orc = "orc"
    parquet = "parquet"
    hudi = "hudi"
    delta = "delta"
    iceberg = "iceberg"
    hyper = "hyper"
    xml = "xml"


class TaskRunSortColumnType(StrEnum):
    TASK_RUN_TYPE = "TASK_RUN_TYPE"
    STATUS = "STATUS"
    STARTED = "STARTED"


class TaskStatusType(StrEnum):
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"


class TaskType(StrEnum):
    EVALUATION = "EVALUATION"
    LABELING_SET_GENERATION = "LABELING_SET_GENERATION"
    IMPORT_LABELS = "IMPORT_LABELS"
    EXPORT_LABELS = "EXPORT_LABELS"
    FIND_MATCHES = "FIND_MATCHES"


class TransformSortColumnType(StrEnum):
    NAME = "NAME"
    TRANSFORM_TYPE = "TRANSFORM_TYPE"
    STATUS = "STATUS"
    CREATED = "CREATED"
    LAST_MODIFIED = "LAST_MODIFIED"


class TransformStatusType(StrEnum):
    NOT_READY = "NOT_READY"
    READY = "READY"
    DELETING = "DELETING"


class TransformType(StrEnum):
    FIND_MATCHES = "FIND_MATCHES"


class TriggerState(StrEnum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    ACTIVATING = "ACTIVATING"
    ACTIVATED = "ACTIVATED"
    DEACTIVATING = "DEACTIVATING"
    DEACTIVATED = "DEACTIVATED"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


class TriggerType(StrEnum):
    SCHEDULED = "SCHEDULED"
    CONDITIONAL = "CONDITIONAL"
    ON_DEMAND = "ON_DEMAND"
    EVENT = "EVENT"


class UnionType(StrEnum):
    ALL = "ALL"
    DISTINCT = "DISTINCT"


class UnnestSpec(StrEnum):
    TOPLEVEL = "TOPLEVEL"
    FULL = "FULL"
    NOUNNEST = "NOUNNEST"


class UpdateBehavior(StrEnum):
    LOG = "LOG"
    UPDATE_IN_DATABASE = "UPDATE_IN_DATABASE"


class UpdateCatalogBehavior(StrEnum):
    UPDATE_IN_DATABASE = "UPDATE_IN_DATABASE"
    LOG = "LOG"


class ViewDialect(StrEnum):
    REDSHIFT = "REDSHIFT"
    ATHENA = "ATHENA"
    SPARK = "SPARK"


class ViewUpdateAction(StrEnum):
    ADD = "ADD"
    REPLACE = "REPLACE"
    ADD_OR_REPLACE = "ADD_OR_REPLACE"
    DROP = "DROP"


class WorkerType(StrEnum):
    Standard = "Standard"
    G_1X = "G.1X"
    G_2X = "G.2X"
    G_025X = "G.025X"
    G_4X = "G.4X"
    G_8X = "G.8X"
    Z_2X = "Z.2X"


class WorkflowRunStatus(StrEnum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


class AccessDeniedException(ServiceException):
    """Access to a resource was denied."""

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class AlreadyExistsException(ServiceException):
    """A resource to be created or added already exists."""

    code: str = "AlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400


class ColumnStatisticsTaskNotRunningException(ServiceException):
    """An exception thrown when you try to stop a task run when there is no
    task running.
    """

    code: str = "ColumnStatisticsTaskNotRunningException"
    sender_fault: bool = False
    status_code: int = 400


class ColumnStatisticsTaskRunningException(ServiceException):
    """An exception thrown when you try to start another job while running a
    column stats generation job.
    """

    code: str = "ColumnStatisticsTaskRunningException"
    sender_fault: bool = False
    status_code: int = 400


class ColumnStatisticsTaskStoppingException(ServiceException):
    """An exception thrown when you try to stop a task run."""

    code: str = "ColumnStatisticsTaskStoppingException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentModificationException(ServiceException):
    """Two processes are trying to modify a resource simultaneously."""

    code: str = "ConcurrentModificationException"
    sender_fault: bool = False
    status_code: int = 400


class ConcurrentRunsExceededException(ServiceException):
    """Too many jobs are being run concurrently."""

    code: str = "ConcurrentRunsExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ConditionCheckFailureException(ServiceException):
    """A specified condition was not satisfied."""

    code: str = "ConditionCheckFailureException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """The ``CreatePartitions`` API was called on a table that has indexes
    enabled.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class CrawlerNotRunningException(ServiceException):
    """The specified crawler is not running."""

    code: str = "CrawlerNotRunningException"
    sender_fault: bool = False
    status_code: int = 400


class CrawlerRunningException(ServiceException):
    """The operation cannot be performed because the crawler is already
    running.
    """

    code: str = "CrawlerRunningException"
    sender_fault: bool = False
    status_code: int = 400


class CrawlerStoppingException(ServiceException):
    """The specified crawler is stopping."""

    code: str = "CrawlerStoppingException"
    sender_fault: bool = False
    status_code: int = 400


class EntityNotFoundException(ServiceException):
    """A specified entity does not exist"""

    code: str = "EntityNotFoundException"
    sender_fault: bool = False
    status_code: int = 400
    FromFederationSource: Optional[NullableBoolean]


class FederatedResourceAlreadyExistsException(ServiceException):
    """A federated resource already exists."""

    code: str = "FederatedResourceAlreadyExistsException"
    sender_fault: bool = False
    status_code: int = 400
    AssociatedGlueResource: Optional[GlueResourceArn]


class FederationSourceException(ServiceException):
    """A federation source failed."""

    code: str = "FederationSourceException"
    sender_fault: bool = False
    status_code: int = 400
    FederationSourceErrorCode: Optional[FederationSourceErrorCode]


class FederationSourceRetryableException(ServiceException):
    """A federation source failed, but the operation may be retried."""

    code: str = "FederationSourceRetryableException"
    sender_fault: bool = False
    status_code: int = 400


class GlueEncryptionException(ServiceException):
    """An encryption operation failed."""

    code: str = "GlueEncryptionException"
    sender_fault: bool = False
    status_code: int = 400


class IdempotentParameterMismatchException(ServiceException):
    """The same unique identifier was associated with two different records."""

    code: str = "IdempotentParameterMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class IllegalBlueprintStateException(ServiceException):
    """The blueprint is in an invalid state to perform a requested operation."""

    code: str = "IllegalBlueprintStateException"
    sender_fault: bool = False
    status_code: int = 400


class IllegalSessionStateException(ServiceException):
    """The session is in an invalid state to perform a requested operation."""

    code: str = "IllegalSessionStateException"
    sender_fault: bool = False
    status_code: int = 400


class IllegalWorkflowStateException(ServiceException):
    """The workflow is in an invalid state to perform a requested operation."""

    code: str = "IllegalWorkflowStateException"
    sender_fault: bool = False
    status_code: int = 400


class IntegrationConflictOperationFault(ServiceException):
    """The requested operation conflicts with another operation."""

    code: str = "IntegrationConflictOperationFault"
    sender_fault: bool = False
    status_code: int = 400


class IntegrationNotFoundFault(ServiceException):
    """The specified integration could not be found."""

    code: str = "IntegrationNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class IntegrationQuotaExceededFault(ServiceException):
    """The data processed through your integration exceeded your quota."""

    code: str = "IntegrationQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class InternalServerException(ServiceException):
    """An internal server error occurred."""

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 400


class InternalServiceException(ServiceException):
    """An internal service error occurred."""

    code: str = "InternalServiceException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidInputException(ServiceException):
    """The input provided was not valid."""

    code: str = "InvalidInputException"
    sender_fault: bool = False
    status_code: int = 400
    FromFederationSource: Optional[NullableBoolean]


class InvalidIntegrationStateFault(ServiceException):
    """The integration is in an invalid state."""

    code: str = "InvalidIntegrationStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidStateException(ServiceException):
    """An error that indicates your data is in an invalid state."""

    code: str = "InvalidStateException"
    sender_fault: bool = False
    status_code: int = 400


class KMSKeyNotAccessibleFault(ServiceException):
    """The KMS key specified is not accessible."""

    code: str = "KMSKeyNotAccessibleFault"
    sender_fault: bool = False
    status_code: int = 400


class MLTransformNotReadyException(ServiceException):
    """The machine learning transform is not ready to run."""

    code: str = "MLTransformNotReadyException"
    sender_fault: bool = False
    status_code: int = 400


class NoScheduleException(ServiceException):
    """There is no applicable schedule."""

    code: str = "NoScheduleException"
    sender_fault: bool = False
    status_code: int = 400


class OperationNotSupportedException(ServiceException):
    """The operation is not available in the region."""

    code: str = "OperationNotSupportedException"
    sender_fault: bool = False
    status_code: int = 400


class OperationTimeoutException(ServiceException):
    """The operation timed out."""

    code: str = "OperationTimeoutException"
    sender_fault: bool = False
    status_code: int = 400


class PermissionTypeMismatchException(ServiceException):
    """The operation timed out."""

    code: str = "PermissionTypeMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """The resource could not be found."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotReadyException(ServiceException):
    """A resource was not ready for a transaction."""

    code: str = "ResourceNotReadyException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNumberLimitExceededException(ServiceException):
    """A resource numerical limit was exceeded."""

    code: str = "ResourceNumberLimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class SchedulerNotRunningException(ServiceException):
    """The specified scheduler is not running."""

    code: str = "SchedulerNotRunningException"
    sender_fault: bool = False
    status_code: int = 400


class SchedulerRunningException(ServiceException):
    """The specified scheduler is already running."""

    code: str = "SchedulerRunningException"
    sender_fault: bool = False
    status_code: int = 400


class SchedulerTransitioningException(ServiceException):
    """The specified scheduler is transitioning."""

    code: str = "SchedulerTransitioningException"
    sender_fault: bool = False
    status_code: int = 400


class TargetResourceNotFound(ServiceException):
    """The target resource could not be found."""

    code: str = "TargetResourceNotFound"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """The throttling threshhold was exceeded."""

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class ValidationException(ServiceException):
    """A value could not be validated."""

    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400


class VersionMismatchException(ServiceException):
    """There was a version conflict."""

    code: str = "VersionMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class NotificationProperty(TypedDict, total=False):
    """Specifies configuration properties of a notification."""

    NotifyDelayAfter: Optional[NotifyDelayAfter]


GenericMap = Dict[GenericString, GenericString]


class Action(TypedDict, total=False):
    """Defines an action to be initiated by a trigger."""

    JobName: Optional[NameString]
    Arguments: Optional[GenericMap]
    Timeout: Optional[Timeout]
    SecurityConfiguration: Optional[NameString]
    NotificationProperty: Optional[NotificationProperty]
    CrawlerName: Optional[NameString]


ActionList = List[Action]
AdditionalContextMap = Dict[ContextKey, ContextValue]
AdditionalOptions = Dict[EnclosedInStringProperty, EnclosedInStringProperty]
AdditionalPlanOptionsMap = Dict[GenericString, GenericString]
EnclosedInStringProperties = List[EnclosedInStringProperty]


class AggregateOperation(TypedDict, total=False):
    """Specifies the set of parameters needed to perform aggregation in the
    aggregate transform.
    """

    Column: EnclosedInStringProperties
    AggFunc: AggFunction


AggregateOperations = List[AggregateOperation]
GlueStudioPathList = List[EnclosedInStringProperties]
OneInput = List[NodeId]


class Aggregate(TypedDict, total=False):
    """Specifies a transform that groups rows by chosen fields and computes the
    aggregated value by specified function.
    """

    Name: NodeName
    Inputs: OneInput
    Groups: GlueStudioPathList
    Aggs: AggregateOperations


class AllowedValue(TypedDict, total=False):
    """An object representing a value allowed for a property."""

    Description: Optional[AllowedValueDescriptionString]
    Value: AllowedValueValueString


AllowedValues = List[AllowedValue]
AllowedValuesStringList = List[ConfigValueString]


class AmazonRedshiftAdvancedOption(TypedDict, total=False):
    """Specifies an optional value when connecting to the Redshift cluster."""

    Key: Optional[GenericString]
    Value: Optional[GenericString]


AmazonRedshiftAdvancedOptions = List[AmazonRedshiftAdvancedOption]


class Option(TypedDict, total=False):
    """Specifies an option value."""

    Value: Optional[EnclosedInStringProperty]
    Label: Optional[EnclosedInStringProperty]
    Description: Optional[EnclosedInStringProperty]


OptionList = List[Option]


class AmazonRedshiftNodeData(TypedDict, total=False):
    """Specifies an Amazon Redshift node."""

    AccessType: Optional[GenericLimitedString]
    SourceType: Optional[GenericLimitedString]
    Connection: Optional[Option]
    Schema: Optional[Option]
    Table: Optional[Option]
    CatalogDatabase: Optional[Option]
    CatalogTable: Optional[Option]
    CatalogRedshiftSchema: Optional[GenericString]
    CatalogRedshiftTable: Optional[GenericString]
    TempDir: Optional[EnclosedInStringProperty]
    IamRole: Optional[Option]
    AdvancedOptions: Optional[AmazonRedshiftAdvancedOptions]
    SampleQuery: Optional[GenericString]
    PreAction: Optional[GenericString]
    PostAction: Optional[GenericString]
    Action: Optional[GenericString]
    TablePrefix: Optional[GenericLimitedString]
    Upsert: Optional[BooleanValue]
    MergeAction: Optional[GenericLimitedString]
    MergeWhenMatched: Optional[GenericLimitedString]
    MergeWhenNotMatched: Optional[GenericLimitedString]
    MergeClause: Optional[GenericString]
    CrawlerConnection: Optional[GenericString]
    TableSchema: Optional[OptionList]
    StagingTable: Optional[GenericString]
    SelectedColumns: Optional[OptionList]


class AmazonRedshiftSource(TypedDict, total=False):
    """Specifies an Amazon Redshift source."""

    Name: Optional[NodeName]
    Data: Optional[AmazonRedshiftNodeData]


class AmazonRedshiftTarget(TypedDict, total=False):
    """Specifies an Amazon Redshift target."""

    Name: Optional[NodeName]
    Data: Optional[AmazonRedshiftNodeData]
    Inputs: Optional[OneInput]


class AnnotationError(TypedDict, total=False):
    """A failed annotation."""

    ProfileId: Optional[HashString]
    StatisticId: Optional[HashString]
    FailureReason: Optional[DescriptionString]


AnnotationErrorList = List[AnnotationError]
Timestamp = datetime


class TimestampedInclusionAnnotation(TypedDict, total=False):
    """A timestamped inclusion annotation."""

    Value: Optional[InclusionAnnotationValue]
    LastModifiedOn: Optional[Timestamp]


class StatisticAnnotation(TypedDict, total=False):
    """A Statistic Annotation."""

    ProfileId: Optional[HashString]
    StatisticId: Optional[HashString]
    StatisticRecordedOn: Optional[Timestamp]
    InclusionAnnotation: Optional[TimestampedInclusionAnnotation]


AnnotationList = List[StatisticAnnotation]
Mappings = List["Mapping"]


class Mapping(TypedDict, total=False):
    """Specifies the mapping of data property keys."""

    ToKey: Optional[EnclosedInStringProperty]
    FromPath: Optional[EnclosedInStringProperties]
    FromType: Optional[EnclosedInStringProperty]
    ToType: Optional[EnclosedInStringProperty]
    Dropped: Optional[BoxedBoolean]
    Children: Optional[Mappings]


class ApplyMapping(TypedDict, total=False):
    """Specifies a transform that maps data property keys in the data source to
    data property keys in the data target. You can rename keys, modify the
    data types for keys, and choose which keys to drop from the dataset.
    """

    Name: NodeName
    Inputs: OneInput
    Mapping: Mappings


class GlueStudioSchemaColumn(TypedDict, total=False):
    """Specifies a single column in a Glue schema definition."""

    Name: GlueStudioColumnNameString
    Type: Optional[ColumnTypeString]


GlueStudioSchemaColumnList = List[GlueStudioSchemaColumn]


class GlueSchema(TypedDict, total=False):
    """Specifies a user-defined schema when a schema cannot be determined by
    Glue.
    """

    Columns: Optional[GlueStudioSchemaColumnList]


GlueSchemas = List[GlueSchema]


class AthenaConnectorSource(TypedDict, total=False):
    """Specifies a connector to an Amazon Athena data source."""

    Name: NodeName
    ConnectionName: EnclosedInStringProperty
    ConnectorName: EnclosedInStringProperty
    ConnectionType: EnclosedInStringProperty
    ConnectionTable: Optional[EnclosedInStringPropertyWithQuote]
    SchemaName: EnclosedInStringProperty
    OutputSchemas: Optional[GlueSchemas]


AuditColumnNamesList = List[ColumnNameString]


class AuditContext(TypedDict, total=False):
    """A structure containing the Lake Formation audit context."""

    AdditionalAuditContext: Optional[AuditContextString]
    RequestedColumns: Optional[AuditColumnNamesList]
    AllColumnsRequested: Optional[NullableBoolean]


DataOperations = List[DataOperation]
PropertyTypes = List[PropertyType]


class Property(TypedDict, total=False):
    """An object that defines a connection type for a compute environment."""

    Name: PropertyName
    Description: PropertyDescriptionString
    Required: Bool
    DefaultValue: Optional[String]
    PropertyTypes: PropertyTypes
    AllowedValues: Optional[AllowedValues]
    DataOperationScopes: Optional[DataOperations]


PropertiesMap = Dict[PropertyName, Property]


class AuthConfiguration(TypedDict, total=False):
    """The authentication configuration for a connection returned by the
    ``DescribeConnectionType`` API.
    """

    AuthenticationType: Property
    SecretArn: Optional[Property]
    OAuth2Properties: Optional[PropertiesMap]
    BasicAuthenticationProperties: Optional[PropertiesMap]
    CustomAuthenticationProperties: Optional[PropertiesMap]


TokenUrlParametersMap = Dict[TokenUrlParameterKey, TokenUrlParameterValue]


class OAuth2ClientApplication(TypedDict, total=False):
    """The OAuth2 client app used for the connection."""

    UserManagedClientApplicationClientId: Optional[UserManagedClientApplicationClientId]
    AWSManagedClientApplicationReference: Optional[AWSManagedClientApplicationReference]


class OAuth2Properties(TypedDict, total=False):
    """A structure containing properties for OAuth2 authentication."""

    OAuth2GrantType: Optional[OAuth2GrantType]
    OAuth2ClientApplication: Optional[OAuth2ClientApplication]
    TokenUrl: Optional[TokenUrl]
    TokenUrlParametersMap: Optional[TokenUrlParametersMap]


class AuthenticationConfiguration(TypedDict, total=False):
    """A structure containing the authentication configuration."""

    AuthenticationType: Optional[AuthenticationType]
    SecretArn: Optional[SecretArn]
    OAuth2Properties: Optional[OAuth2Properties]


CredentialMap = Dict[CredentialKey, CredentialValue]


class BasicAuthenticationCredentials(TypedDict, total=False):
    """For supplying basic auth credentials when not providing a ``SecretArn``
    value.
    """

    Username: Optional[Username]
    Password: Optional[Password]


class OAuth2Credentials(TypedDict, total=False):
    """The credentials used when the authentication type is OAuth2
    authentication.
    """

    UserManagedClientApplicationClientSecret: Optional[UserManagedClientApplicationClientSecret]
    AccessToken: Optional[AccessToken]
    RefreshToken: Optional[RefreshToken]
    JwtToken: Optional[JwtToken]


class AuthorizationCodeProperties(TypedDict, total=False):
    """The set of properties required for the the OAuth2 ``AUTHORIZATION_CODE``
    grant type workflow.
    """

    AuthorizationCode: Optional[AuthorizationCode]
    RedirectUri: Optional[RedirectUri]


class OAuth2PropertiesInput(TypedDict, total=False):
    """A structure containing properties for OAuth2 in the CreateConnection
    request.
    """

    OAuth2GrantType: Optional[OAuth2GrantType]
    OAuth2ClientApplication: Optional[OAuth2ClientApplication]
    TokenUrl: Optional[TokenUrl]
    TokenUrlParametersMap: Optional[TokenUrlParametersMap]
    AuthorizationCodeProperties: Optional[AuthorizationCodeProperties]
    OAuth2Credentials: Optional[OAuth2Credentials]


class AuthenticationConfigurationInput(TypedDict, total=False):
    """A structure containing the authentication configuration in the
    CreateConnection request.
    """

    AuthenticationType: Optional[AuthenticationType]
    OAuth2Properties: Optional[OAuth2PropertiesInput]
    SecretArn: Optional[SecretArn]
    KmsKeyArn: Optional[KmsKeyArn]
    BasicAuthenticationCredentials: Optional[BasicAuthenticationCredentials]
    CustomAuthenticationCredentials: Optional[CredentialMap]


AuthenticationTypes = List[AuthenticationType]
ValueStringList = List[ValueString]


class PartitionValueList(TypedDict, total=False):
    """Contains a list of values defining partitions."""

    Values: ValueStringList


BackfillErroredPartitionsList = List[PartitionValueList]


class BackfillError(TypedDict, total=False):
    """A list of errors that can occur when registering partition indexes for
    an existing table.

    These errors give the details about why an index registration failed and
    provide a limited number of partitions in the response, so that you can
    fix the partitions at fault and try registering the index again. The
    most common set of errors that can occur are categorized as follows:

    -  EncryptedPartitionError: The partitions are encrypted.

    -  InvalidPartitionTypeDataError: The partition value doesn't match the
       data type for that partition column.

    -  MissingPartitionValueError: The partitions are encrypted.

    -  UnsupportedPartitionCharacterError: Characters inside the partition
       value are not supported. For example: U+0000 , U+0001, U+0002.

    -  InternalError: Any error which does not belong to other error codes.
    """

    Code: Optional[BackfillErrorCode]
    Partitions: Optional[BackfillErroredPartitionsList]


BackfillErrors = List[BackfillError]


class BasicCatalogTarget(TypedDict, total=False):
    """Specifies a target that uses a Glue Data Catalog table."""

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


ParametersMap = Dict[KeyString, ParametersMapValue]
VersionLongNumber = int


class SchemaId(TypedDict, total=False):
    """The unique ID of the schema in the Glue schema registry."""

    SchemaArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    RegistryName: Optional[SchemaRegistryNameString]


class SchemaReference(TypedDict, total=False):
    """An object that references a schema stored in the Glue Schema Registry."""

    SchemaId: Optional[SchemaId]
    SchemaVersionId: Optional[SchemaVersionIdString]
    SchemaVersionNumber: Optional[VersionLongNumber]


LocationMap = Dict[ColumnValuesString, ColumnValuesString]
ColumnValueStringList = List[ColumnValuesString]
NameStringList = List[NameString]


class SkewedInfo(TypedDict, total=False):
    """Specifies skewed values in a table. Skewed values are those that occur
    with very high frequency.
    """

    SkewedColumnNames: Optional[NameStringList]
    SkewedColumnValues: Optional[ColumnValueStringList]
    SkewedColumnValueLocationMaps: Optional[LocationMap]


class Order(TypedDict, total=False):
    """Specifies the sort order of a sorted column."""

    Column: NameString
    SortOrder: IntegerFlag


OrderList = List[Order]


class SerDeInfo(TypedDict, total=False):
    """Information about a serialization/deserialization program (SerDe) that
    serves as an extractor and loader.
    """

    Name: Optional[NameString]
    SerializationLibrary: Optional[NameString]
    Parameters: Optional[ParametersMap]


LocationStringList = List[LocationString]


class Column(TypedDict, total=False):
    """A column in a ``Table``."""

    Name: NameString
    Type: Optional[ColumnTypeString]
    Comment: Optional[CommentString]
    Parameters: Optional[ParametersMap]


ColumnList = List[Column]


class StorageDescriptor(TypedDict, total=False):
    """Describes the physical storage of table data."""

    Columns: Optional[ColumnList]
    Location: Optional[LocationString]
    AdditionalLocations: Optional[LocationStringList]
    InputFormat: Optional[FormatString]
    OutputFormat: Optional[FormatString]
    Compressed: Optional[Boolean]
    NumberOfBuckets: Optional[Integer]
    SerdeInfo: Optional[SerDeInfo]
    BucketColumns: Optional[NameStringList]
    SortColumns: Optional[OrderList]
    Parameters: Optional[ParametersMap]
    SkewedInfo: Optional[SkewedInfo]
    StoredAsSubDirectories: Optional[Boolean]
    SchemaReference: Optional[SchemaReference]


class PartitionInput(TypedDict, total=False):
    """The structure used to create and update a partition."""

    Values: Optional[ValueStringList]
    LastAccessTime: Optional[Timestamp]
    StorageDescriptor: Optional[StorageDescriptor]
    Parameters: Optional[ParametersMap]
    LastAnalyzedTime: Optional[Timestamp]


PartitionInputList = List[PartitionInput]


class BatchCreatePartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionInputList: PartitionInputList


class ErrorDetail(TypedDict, total=False):
    """Contains details about an error."""

    ErrorCode: Optional[NameString]
    ErrorMessage: Optional[DescriptionString]


class PartitionError(TypedDict, total=False):
    """Contains information about a partition error."""

    PartitionValues: Optional[ValueStringList]
    ErrorDetail: Optional[ErrorDetail]


PartitionErrors = List[PartitionError]


class BatchCreatePartitionResponse(TypedDict, total=False):
    Errors: Optional[PartitionErrors]


DeleteConnectionNameList = List[NameString]


class BatchDeleteConnectionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    ConnectionNameList: DeleteConnectionNameList


ErrorByName = Dict[NameString, ErrorDetail]


class BatchDeleteConnectionResponse(TypedDict, total=False):
    Succeeded: Optional[NameStringList]
    Errors: Optional[ErrorByName]


BatchDeletePartitionValueList = List[PartitionValueList]


class BatchDeletePartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionsToDelete: BatchDeletePartitionValueList


class BatchDeletePartitionResponse(TypedDict, total=False):
    Errors: Optional[PartitionErrors]


BatchDeleteTableNameList = List[NameString]


class BatchDeleteTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TablesToDelete: BatchDeleteTableNameList
    TransactionId: Optional[TransactionIdString]


class TableError(TypedDict, total=False):
    """An error record for table operations."""

    TableName: Optional[NameString]
    ErrorDetail: Optional[ErrorDetail]


TableErrors = List[TableError]


class BatchDeleteTableResponse(TypedDict, total=False):
    Errors: Optional[TableErrors]


BatchDeleteTableVersionList = List[VersionString]


class BatchDeleteTableVersionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    VersionIds: BatchDeleteTableVersionList


class TableVersionError(TypedDict, total=False):
    """An error record for table-version operations."""

    TableName: Optional[NameString]
    VersionId: Optional[VersionString]
    ErrorDetail: Optional[ErrorDetail]


TableVersionErrors = List[TableVersionError]


class BatchDeleteTableVersionResponse(TypedDict, total=False):
    Errors: Optional[TableVersionErrors]


BatchGetBlueprintNames = List[OrchestrationNameString]


class BatchGetBlueprintsRequest(ServiceRequest):
    Names: BatchGetBlueprintNames
    IncludeBlueprint: Optional[NullableBoolean]
    IncludeParameterSpec: Optional[NullableBoolean]


BlueprintNames = List[OrchestrationNameString]
TimestampValue = datetime


class LastActiveDefinition(TypedDict, total=False):
    """When there are multiple versions of a blueprint and the latest version
    has some errors, this attribute indicates the last successful blueprint
    definition that is available with the service.
    """

    Description: Optional[Generic512CharString]
    LastModifiedOn: Optional[TimestampValue]
    ParameterSpec: Optional[BlueprintParameterSpec]
    BlueprintLocation: Optional[GenericString]
    BlueprintServiceLocation: Optional[GenericString]


class Blueprint(TypedDict, total=False):
    """The details of a blueprint."""

    Name: Optional[OrchestrationNameString]
    Description: Optional[Generic512CharString]
    CreatedOn: Optional[TimestampValue]
    LastModifiedOn: Optional[TimestampValue]
    ParameterSpec: Optional[BlueprintParameterSpec]
    BlueprintLocation: Optional[GenericString]
    BlueprintServiceLocation: Optional[GenericString]
    Status: Optional[BlueprintStatus]
    ErrorMessage: Optional[ErrorString]
    LastActiveDefinition: Optional[LastActiveDefinition]


Blueprints = List[Blueprint]


class BatchGetBlueprintsResponse(TypedDict, total=False):
    Blueprints: Optional[Blueprints]
    MissingBlueprints: Optional[BlueprintNames]


CrawlerNameList = List[NameString]


class BatchGetCrawlersRequest(ServiceRequest):
    CrawlerNames: CrawlerNameList


class LakeFormationConfiguration(TypedDict, total=False):
    """Specifies Lake Formation configuration settings for the crawler."""

    UseLakeFormationCredentials: Optional[NullableBoolean]
    AccountId: Optional[AccountId]


VersionId = int


class LastCrawlInfo(TypedDict, total=False):
    """Status and error information about the most recent crawl."""

    Status: Optional[LastCrawlStatus]
    ErrorMessage: Optional[DescriptionString]
    LogGroup: Optional[LogGroup]
    LogStream: Optional[LogStream]
    MessagePrefix: Optional[MessagePrefix]
    StartTime: Optional[Timestamp]


MillisecondsCount = int


class Schedule(TypedDict, total=False):
    """A scheduling object using a ``cron`` statement to schedule an event."""

    ScheduleExpression: Optional[CronExpression]
    State: Optional[ScheduleState]


class LineageConfiguration(TypedDict, total=False):
    """Specifies data lineage configuration settings for the crawler."""

    CrawlerLineageSettings: Optional[CrawlerLineageSettings]


class SchemaChangePolicy(TypedDict, total=False):
    """A policy that specifies update and deletion behaviors for the crawler."""

    UpdateBehavior: Optional[UpdateBehavior]
    DeleteBehavior: Optional[DeleteBehavior]


class RecrawlPolicy(TypedDict, total=False):
    """When crawling an Amazon S3 data source after the first crawl is
    complete, specifies whether to crawl the entire dataset again or to
    crawl only folders that were added since the last crawler run. For more
    information, see `Incremental Crawls in
    Glue <https://docs.aws.amazon.com/glue/latest/dg/incremental-crawls.html>`__
    in the developer guide.
    """

    RecrawlBehavior: Optional[RecrawlBehavior]


ClassifierNameList = List[NameString]
PathList = List[Path]


class HudiTarget(TypedDict, total=False):
    """Specifies an Apache Hudi data source."""

    Paths: Optional[PathList]
    ConnectionName: Optional[ConnectionName]
    Exclusions: Optional[PathList]
    MaximumTraversalDepth: Optional[NullableInteger]


HudiTargetList = List[HudiTarget]


class IcebergTarget(TypedDict, total=False):
    """Specifies an Apache Iceberg data source where Iceberg tables are stored
    in Amazon S3.
    """

    Paths: Optional[PathList]
    ConnectionName: Optional[ConnectionName]
    Exclusions: Optional[PathList]
    MaximumTraversalDepth: Optional[NullableInteger]


IcebergTargetList = List[IcebergTarget]


class DeltaTarget(TypedDict, total=False):
    """Specifies a Delta data store to crawl one or more Delta tables."""

    DeltaTables: Optional[PathList]
    ConnectionName: Optional[ConnectionName]
    WriteManifest: Optional[NullableBoolean]
    CreateNativeDeltaTable: Optional[NullableBoolean]


DeltaTargetList = List[DeltaTarget]
CatalogTablesList = List[NameString]


class CatalogTarget(TypedDict, total=False):
    """Specifies an Glue Data Catalog target."""

    DatabaseName: NameString
    Tables: CatalogTablesList
    ConnectionName: Optional[ConnectionName]
    EventQueueArn: Optional[EventQueueArn]
    DlqEventQueueArn: Optional[EventQueueArn]


CatalogTargetList = List[CatalogTarget]


class DynamoDBTarget(TypedDict, total=False):
    """Specifies an Amazon DynamoDB table to crawl."""

    Path: Optional[Path]
    scanAll: Optional[NullableBoolean]
    scanRate: Optional[NullableDouble]


DynamoDBTargetList = List[DynamoDBTarget]


class MongoDBTarget(TypedDict, total=False):
    """Specifies an Amazon DocumentDB or MongoDB data store to crawl."""

    ConnectionName: Optional[ConnectionName]
    Path: Optional[Path]
    ScanAll: Optional[NullableBoolean]


MongoDBTargetList = List[MongoDBTarget]
EnableAdditionalMetadata = List[JdbcMetadataEntry]


class JdbcTarget(TypedDict, total=False):
    """Specifies a JDBC data store to crawl."""

    ConnectionName: Optional[ConnectionName]
    Path: Optional[Path]
    Exclusions: Optional[PathList]
    EnableAdditionalMetadata: Optional[EnableAdditionalMetadata]


JdbcTargetList = List[JdbcTarget]


class S3Target(TypedDict, total=False):
    """Specifies a data store in Amazon Simple Storage Service (Amazon S3)."""

    Path: Optional[Path]
    Exclusions: Optional[PathList]
    ConnectionName: Optional[ConnectionName]
    SampleSize: Optional[NullableInteger]
    EventQueueArn: Optional[EventQueueArn]
    DlqEventQueueArn: Optional[EventQueueArn]


S3TargetList = List[S3Target]


class CrawlerTargets(TypedDict, total=False):
    """Specifies data stores to crawl."""

    S3Targets: Optional[S3TargetList]
    JdbcTargets: Optional[JdbcTargetList]
    MongoDBTargets: Optional[MongoDBTargetList]
    DynamoDBTargets: Optional[DynamoDBTargetList]
    CatalogTargets: Optional[CatalogTargetList]
    DeltaTargets: Optional[DeltaTargetList]
    IcebergTargets: Optional[IcebergTargetList]
    HudiTargets: Optional[HudiTargetList]


class Crawler(TypedDict, total=False):
    """Specifies a crawler program that examines a data source and uses
    classifiers to try to determine its schema. If successful, the crawler
    records metadata concerning the data source in the Glue Data Catalog.
    """

    Name: Optional[NameString]
    Role: Optional[Role]
    Targets: Optional[CrawlerTargets]
    DatabaseName: Optional[DatabaseName]
    Description: Optional[DescriptionString]
    Classifiers: Optional[ClassifierNameList]
    RecrawlPolicy: Optional[RecrawlPolicy]
    SchemaChangePolicy: Optional[SchemaChangePolicy]
    LineageConfiguration: Optional[LineageConfiguration]
    State: Optional[CrawlerState]
    TablePrefix: Optional[TablePrefix]
    Schedule: Optional[Schedule]
    CrawlElapsedTime: Optional[MillisecondsCount]
    CreationTime: Optional[Timestamp]
    LastUpdated: Optional[Timestamp]
    LastCrawl: Optional[LastCrawlInfo]
    Version: Optional[VersionId]
    Configuration: Optional[CrawlerConfiguration]
    CrawlerSecurityConfiguration: Optional[CrawlerSecurityConfiguration]
    LakeFormationConfiguration: Optional[LakeFormationConfiguration]


CrawlerList = List[Crawler]


class BatchGetCrawlersResponse(TypedDict, total=False):
    Crawlers: Optional[CrawlerList]
    CrawlersNotFound: Optional[CrawlerNameList]


CustomEntityTypeNames = List[NameString]


class BatchGetCustomEntityTypesRequest(ServiceRequest):
    Names: CustomEntityTypeNames


ContextWords = List[NameString]


class CustomEntityType(TypedDict, total=False):
    """An object representing a custom pattern for detecting sensitive data
    across the columns and rows of your structured data.
    """

    Name: NameString
    RegexString: NameString
    ContextWords: Optional[ContextWords]


CustomEntityTypes = List[CustomEntityType]


class BatchGetCustomEntityTypesResponse(TypedDict, total=False):
    CustomEntityTypes: Optional[CustomEntityTypes]
    CustomEntityTypesNotFound: Optional[CustomEntityTypeNames]


DataQualityResultIds = List[HashString]


class BatchGetDataQualityResultRequest(ServiceRequest):
    ResultIds: DataQualityResultIds


NewRules = List[NameString]


class DataQualityMetricValues(TypedDict, total=False):
    """Describes the data quality metric value according to the analysis of
    historical data.
    """

    ActualValue: Optional[NullableDouble]
    ExpectedValue: Optional[NullableDouble]
    LowerLimit: Optional[NullableDouble]
    UpperLimit: Optional[NullableDouble]


class MetricBasedObservation(TypedDict, total=False):
    """Describes the metric based observation generated based on evaluated data
    quality metrics.
    """

    MetricName: Optional[NameString]
    StatisticId: Optional[HashString]
    MetricValues: Optional[DataQualityMetricValues]
    NewRules: Optional[NewRules]


class DataQualityObservation(TypedDict, total=False):
    """Describes the observation generated after evaluating the rules and
    analyzers.
    """

    Description: Optional[DataQualityObservationDescription]
    MetricBasedObservation: Optional[MetricBasedObservation]


DataQualityObservations = List[DataQualityObservation]
EvaluatedMetricsMap = Dict[NameString, NullableDouble]


class DataQualityAnalyzerResult(TypedDict, total=False):
    """Describes the result of the evaluation of a data quality analyzer."""

    Name: Optional[NameString]
    Description: Optional[DataQualityRuleResultDescription]
    EvaluationMessage: Optional[DataQualityRuleResultDescription]
    EvaluatedMetrics: Optional[EvaluatedMetricsMap]


DataQualityAnalyzerResults = List[DataQualityAnalyzerResult]


class DataQualityRuleResult(TypedDict, total=False):
    """Describes the result of the evaluation of a data quality rule."""

    Name: Optional[NameString]
    Description: Optional[DataQualityRuleResultDescription]
    EvaluationMessage: Optional[DataQualityRuleResultDescription]
    Result: Optional[DataQualityRuleResultStatus]
    EvaluatedMetrics: Optional[EvaluatedMetricsMap]
    EvaluatedRule: Optional[DataQualityRuleResultDescription]


DataQualityRuleResults = List[DataQualityRuleResult]
GlueTableAdditionalOptions = Dict[NameString, DescriptionString]


class GlueTable(TypedDict, total=False):
    """The database and table in the Glue Data Catalog that is used for input
    or output data.
    """

    DatabaseName: NameString
    TableName: NameString
    CatalogId: Optional[NameString]
    ConnectionName: Optional[NameString]
    AdditionalOptions: Optional[GlueTableAdditionalOptions]


class DataSource(TypedDict, total=False):
    """A data source (an Glue table) for which you want data quality results."""

    GlueTable: GlueTable


class DataQualityResult(TypedDict, total=False):
    """Describes a data quality result."""

    ResultId: Optional[HashString]
    ProfileId: Optional[HashString]
    Score: Optional[GenericBoundedDouble]
    DataSource: Optional[DataSource]
    RulesetName: Optional[NameString]
    EvaluationContext: Optional[GenericString]
    StartedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    JobName: Optional[NameString]
    JobRunId: Optional[HashString]
    RulesetEvaluationRunId: Optional[HashString]
    RuleResults: Optional[DataQualityRuleResults]
    AnalyzerResults: Optional[DataQualityAnalyzerResults]
    Observations: Optional[DataQualityObservations]


DataQualityResultsList = List[DataQualityResult]


class BatchGetDataQualityResultResponse(TypedDict, total=False):
    Results: DataQualityResultsList
    ResultsNotFound: Optional[DataQualityResultIds]


DevEndpointNames = List[GenericString]


class BatchGetDevEndpointsRequest(ServiceRequest):
    DevEndpointNames: DevEndpointNames


MapValue = Dict[GenericString, GenericString]
PublicKeysList = List[GenericString]
StringList = List[GenericString]


class DevEndpoint(TypedDict, total=False):
    """A development endpoint where a developer can remotely debug extract,
    transform, and load (ETL) scripts.
    """

    EndpointName: Optional[GenericString]
    RoleArn: Optional[RoleArn]
    SecurityGroupIds: Optional[StringList]
    SubnetId: Optional[GenericString]
    YarnEndpointAddress: Optional[GenericString]
    PrivateAddress: Optional[GenericString]
    ZeppelinRemoteSparkInterpreterPort: Optional[IntegerValue]
    PublicAddress: Optional[GenericString]
    Status: Optional[GenericString]
    WorkerType: Optional[WorkerType]
    GlueVersion: Optional[GlueVersionString]
    NumberOfWorkers: Optional[NullableInteger]
    NumberOfNodes: Optional[IntegerValue]
    AvailabilityZone: Optional[GenericString]
    VpcId: Optional[GenericString]
    ExtraPythonLibsS3Path: Optional[GenericString]
    ExtraJarsS3Path: Optional[GenericString]
    FailureReason: Optional[GenericString]
    LastUpdateStatus: Optional[GenericString]
    CreatedTimestamp: Optional[TimestampValue]
    LastModifiedTimestamp: Optional[TimestampValue]
    PublicKey: Optional[GenericString]
    PublicKeys: Optional[PublicKeysList]
    SecurityConfiguration: Optional[NameString]
    Arguments: Optional[MapValue]


DevEndpointList = List[DevEndpoint]


class BatchGetDevEndpointsResponse(TypedDict, total=False):
    DevEndpoints: Optional[DevEndpointList]
    DevEndpointsNotFound: Optional[DevEndpointNames]


JobNameList = List[NameString]


class BatchGetJobsRequest(ServiceRequest):
    JobNames: JobNameList


class SourceControlDetails(TypedDict, total=False):
    """The details for a source control configuration for a job, allowing
    synchronization of job artifacts to or from a remote repository.
    """

    Provider: Optional[SourceControlProvider]
    Repository: Optional[Generic512CharString]
    Owner: Optional[Generic512CharString]
    Branch: Optional[Generic512CharString]
    Folder: Optional[Generic512CharString]
    LastCommitId: Optional[Generic512CharString]
    AuthStrategy: Optional[SourceControlAuthStrategy]
    AuthToken: Optional[Generic512CharString]


ConnectorOptions = Dict[GenericString, GenericString]


class ConnectorDataTarget(TypedDict, total=False):
    """Specifies a target generated with standard connection options."""

    Name: NodeName
    ConnectionType: EnclosedInStringProperty
    Data: ConnectorOptions
    Inputs: Optional[OneInput]


class ConnectorDataSource(TypedDict, total=False):
    """Specifies a source generated with standard connection options."""

    Name: NodeName
    ConnectionType: EnclosedInStringProperty
    Data: ConnectorOptions
    OutputSchemas: Optional[GlueSchemas]


class SnowflakeNodeData(TypedDict, total=False):
    """Specifies configuration for Snowflake nodes in Glue Studio."""

    SourceType: Optional[GenericLimitedString]
    Connection: Optional[Option]
    Schema: Optional[GenericString]
    Table: Optional[GenericString]
    Database: Optional[GenericString]
    TempDir: Optional[EnclosedInStringProperty]
    IamRole: Optional[Option]
    AdditionalOptions: Optional[AdditionalOptions]
    SampleQuery: Optional[GenericString]
    PreAction: Optional[GenericString]
    PostAction: Optional[GenericString]
    Action: Optional[GenericString]
    Upsert: Optional[BooleanValue]
    MergeAction: Optional[GenericLimitedString]
    MergeWhenMatched: Optional[GenericLimitedString]
    MergeWhenNotMatched: Optional[GenericLimitedString]
    MergeClause: Optional[GenericString]
    StagingTable: Optional[GenericString]
    SelectedColumns: Optional[OptionList]
    AutoPushdown: Optional[BooleanValue]
    TableSchema: Optional[OptionList]


class SnowflakeTarget(TypedDict, total=False):
    """Specifies a Snowflake target."""

    Name: NodeName
    Data: SnowflakeNodeData
    Inputs: Optional[OneInput]


class SnowflakeSource(TypedDict, total=False):
    """Specifies a Snowflake data source."""

    Name: NodeName
    Data: SnowflakeNodeData
    OutputSchemas: Optional[GlueSchemas]


class ConditionExpression(TypedDict, total=False):
    """Condition expression defined in the Glue Studio data preparation recipe
    node.
    """

    Condition: DatabrewCondition
    Value: Optional[DatabrewConditionValue]
    TargetColumn: TargetColumn


ConditionExpressionList = List[ConditionExpression]
ParameterMap = Dict[ParameterName, ParameterValue]


class RecipeAction(TypedDict, total=False):
    """Actions defined in the Glue Studio data preparation recipe node."""

    Operation: Operation
    Parameters: Optional[ParameterMap]


class RecipeStep(TypedDict, total=False):
    """A recipe step used in a Glue Studio data preparation recipe node."""

    Action: RecipeAction
    ConditionExpressions: Optional[ConditionExpressionList]


RecipeSteps = List[RecipeStep]


class RecipeReference(TypedDict, total=False):
    """A reference to a Glue DataBrew recipe."""

    RecipeArn: EnclosedInStringProperty
    RecipeVersion: RecipeVersion


class Recipe(TypedDict, total=False):
    """A Glue Studio node that uses a Glue DataBrew recipe in Glue jobs."""

    Name: NodeName
    Inputs: OneInput
    RecipeReference: Optional[RecipeReference]
    RecipeSteps: Optional[RecipeSteps]


class DQStopJobOnFailureOptions(TypedDict, total=False):
    """Options to configure how your job will stop if your data quality
    evaluation fails.
    """

    StopJobOnFailureTiming: Optional[DQStopJobOnFailureTiming]


DQAdditionalOptions = Dict[AdditionalOptionKeys, GenericString]


class DQResultsPublishingOptions(TypedDict, total=False):
    """Options to configure how your data quality evaluation results are
    published.
    """

    EvaluationContext: Optional[GenericLimitedString]
    ResultsS3Prefix: Optional[EnclosedInStringProperty]
    CloudWatchMetricsEnabled: Optional[BoxedBoolean]
    ResultsPublishingEnabled: Optional[BoxedBoolean]


DQDLAliases = Dict[NodeName, EnclosedInStringProperty]
ManyInputs = List[NodeId]


class EvaluateDataQualityMultiFrame(TypedDict, total=False):
    """Specifies your data quality evaluation criteria."""

    Name: NodeName
    Inputs: ManyInputs
    AdditionalDataSources: Optional[DQDLAliases]
    Ruleset: DQDLString
    PublishingOptions: Optional[DQResultsPublishingOptions]
    AdditionalOptions: Optional[DQAdditionalOptions]
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptions]


class DirectSchemaChangePolicy(TypedDict, total=False):
    """A policy that specifies update behavior for the crawler."""

    EnableUpdateCatalog: Optional[BoxedBoolean]
    UpdateBehavior: Optional[UpdateCatalogBehavior]
    Table: Optional[EnclosedInStringProperty]
    Database: Optional[EnclosedInStringProperty]


class S3DeltaDirectTarget(TypedDict, total=False):
    """Specifies a target that writes to a Delta Lake data source in Amazon S3."""

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Path: EnclosedInStringProperty
    Compression: DeltaTargetCompressionType
    NumberTargetPartitions: Optional[NumberTargetPartitionsString]
    Format: TargetFormat
    AdditionalOptions: Optional[AdditionalOptions]
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy]


class CatalogSchemaChangePolicy(TypedDict, total=False):
    """A policy that specifies update behavior for the crawler."""

    EnableUpdateCatalog: Optional[BoxedBoolean]
    UpdateBehavior: Optional[UpdateCatalogBehavior]


class S3DeltaCatalogTarget(TypedDict, total=False):
    """Specifies a target that writes to a Delta Lake data source in the Glue
    Data Catalog.
    """

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Table: EnclosedInStringProperty
    Database: EnclosedInStringProperty
    AdditionalOptions: Optional[AdditionalOptions]
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy]


BoxedLong = int


class S3DirectSourceAdditionalOptions(TypedDict, total=False):
    """Specifies additional connection options for the Amazon S3 data store."""

    BoundedSize: Optional[BoxedLong]
    BoundedFiles: Optional[BoxedLong]
    EnableSamplePath: Optional[BoxedBoolean]
    SamplePath: Optional[EnclosedInStringProperty]


class S3DeltaSource(TypedDict, total=False):
    """Specifies a Delta Lake data source stored in Amazon S3."""

    Name: NodeName
    Paths: EnclosedInStringProperties
    AdditionalDeltaOptions: Optional[AdditionalOptions]
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class CatalogDeltaSource(TypedDict, total=False):
    """Specifies a Delta Lake data source that is registered in the Glue Data
    Catalog.
    """

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    AdditionalDeltaOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class S3CatalogDeltaSource(TypedDict, total=False):
    """Specifies a Delta Lake data source that is registered in the Glue Data
    Catalog. The data source must be stored in Amazon S3.
    """

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    AdditionalDeltaOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class DirectJDBCSource(TypedDict, total=False):
    """Specifies the direct JDBC source connection."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    ConnectionName: EnclosedInStringProperty
    ConnectionType: JDBCConnectionType
    RedshiftTmpDir: Optional[EnclosedInStringProperty]


class S3HudiDirectTarget(TypedDict, total=False):
    """Specifies a target that writes to a Hudi data source in Amazon S3."""

    Name: NodeName
    Inputs: OneInput
    Path: EnclosedInStringProperty
    Compression: HudiTargetCompressionType
    NumberTargetPartitions: Optional[NumberTargetPartitionsString]
    PartitionKeys: Optional[GlueStudioPathList]
    Format: TargetFormat
    AdditionalOptions: AdditionalOptions
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy]


class S3HudiCatalogTarget(TypedDict, total=False):
    """Specifies a target that writes to a Hudi data source in the Glue Data
    Catalog.
    """

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Table: EnclosedInStringProperty
    Database: EnclosedInStringProperty
    AdditionalOptions: AdditionalOptions
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy]


class S3HudiSource(TypedDict, total=False):
    """Specifies a Hudi data source stored in Amazon S3."""

    Name: NodeName
    Paths: EnclosedInStringProperties
    AdditionalHudiOptions: Optional[AdditionalOptions]
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class CatalogHudiSource(TypedDict, total=False):
    """Specifies a Hudi data source that is registered in the Glue Data
    Catalog.
    """

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    AdditionalHudiOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class S3CatalogHudiSource(TypedDict, total=False):
    """Specifies a Hudi data source that is registered in the Glue Data
    Catalog. The Hudi data source must be stored in Amazon S3.
    """

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    AdditionalHudiOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class EvaluateDataQuality(TypedDict, total=False):
    """Specifies your data quality evaluation criteria."""

    Name: NodeName
    Inputs: OneInput
    Ruleset: DQDLString
    Output: Optional[DQTransformOutput]
    PublishingOptions: Optional[DQResultsPublishingOptions]
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptions]


class TransformConfigParameter(TypedDict, total=False):
    """Specifies the parameters in the config file of the dynamic transform."""

    Name: EnclosedInStringProperty
    Type: ParamType
    ValidationRule: Optional[EnclosedInStringProperty]
    ValidationMessage: Optional[EnclosedInStringProperty]
    Value: Optional[EnclosedInStringProperties]
    ListType: Optional[ParamType]
    IsOptional: Optional[BoxedBoolean]


TransformConfigParameterList = List[TransformConfigParameter]


class DynamicTransform(TypedDict, total=False):
    """Specifies the set of parameters needed to perform the dynamic transform."""

    Name: EnclosedInStringProperty
    TransformName: EnclosedInStringProperty
    Inputs: OneInput
    Parameters: Optional[TransformConfigParameterList]
    FunctionName: EnclosedInStringProperty
    Path: EnclosedInStringProperty
    Version: Optional[EnclosedInStringProperty]
    OutputSchemas: Optional[GlueSchemas]


class PostgreSQLCatalogTarget(TypedDict, total=False):
    """Specifies a target that uses Postgres SQL."""

    Name: NodeName
    Inputs: OneInput
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class OracleSQLCatalogTarget(TypedDict, total=False):
    """Specifies a target that uses Oracle SQL."""

    Name: NodeName
    Inputs: OneInput
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class MySQLCatalogTarget(TypedDict, total=False):
    """Specifies a target that uses MySQL."""

    Name: NodeName
    Inputs: OneInput
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class MicrosoftSQLServerCatalogTarget(TypedDict, total=False):
    """Specifies a target that uses Microsoft SQL."""

    Name: NodeName
    Inputs: OneInput
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class PostgreSQLCatalogSource(TypedDict, total=False):
    """Specifies a PostgresSQL data source in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class OracleSQLCatalogSource(TypedDict, total=False):
    """Specifies an Oracle data source in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class MySQLCatalogSource(TypedDict, total=False):
    """Specifies a MySQL data source in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class MicrosoftSQLServerCatalogSource(TypedDict, total=False):
    """Specifies a Microsoft SQL server data source in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class S3SourceAdditionalOptions(TypedDict, total=False):
    """Specifies additional connection options for the Amazon S3 data store."""

    BoundedSize: Optional[BoxedLong]
    BoundedFiles: Optional[BoxedLong]


class GovernedCatalogSource(TypedDict, total=False):
    """Specifies the data store in the governed Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    PartitionPredicate: Optional[EnclosedInStringProperty]
    AdditionalOptions: Optional[S3SourceAdditionalOptions]


class GovernedCatalogTarget(TypedDict, total=False):
    """Specifies a data target that writes to Amazon S3 using the Glue Data
    Catalog.
    """

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Table: EnclosedInStringProperty
    Database: EnclosedInStringProperty
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy]


LimitedStringList = List[GenericLimitedString]
LimitedPathList = List[LimitedStringList]


class DropDuplicates(TypedDict, total=False):
    """Specifies a transform that removes rows of repeating data from a data
    set.
    """

    Name: NodeName
    Inputs: OneInput
    Columns: Optional[LimitedPathList]


class PIIDetection(TypedDict, total=False):
    """Specifies a transform that identifies, removes or masks PII data."""

    Name: NodeName
    Inputs: OneInput
    PiiType: PiiType
    EntityTypesToDetect: EnclosedInStringProperties
    OutputColumnName: Optional[EnclosedInStringProperty]
    SampleFraction: Optional[BoxedDoubleFraction]
    ThresholdFraction: Optional[BoxedDoubleFraction]
    MaskValue: Optional[MaskValue]


TwoInputs = List[NodeId]


class Union_(TypedDict, total=False):
    """Specifies a transform that combines the rows from two or more datasets
    into a single result.
    """

    Name: NodeName
    Inputs: TwoInputs
    UnionType: UnionType


class Merge(TypedDict, total=False):
    """Specifies a transform that merges a ``DynamicFrame`` with a staging
    ``DynamicFrame`` based on the specified primary keys to identify
    records. Duplicate records (records with the same primary keys) are not
    de-duplicated.
    """

    Name: NodeName
    Inputs: TwoInputs
    Source: NodeId
    PrimaryKeys: GlueStudioPathList


class Datatype(TypedDict, total=False):
    """A structure representing the datatype of the value."""

    Id: GenericLimitedString
    Label: GenericLimitedString


class NullValueField(TypedDict, total=False):
    """Represents a custom null value such as a zeros or other value being used
    as a null placeholder unique to the dataset.
    """

    Value: EnclosedInStringProperty
    Datatype: Datatype


NullValueFields = List[NullValueField]


class NullCheckBoxList(TypedDict, total=False):
    """Represents whether certain values are recognized as null values for
    removal.
    """

    IsEmpty: Optional[BoxedBoolean]
    IsNullString: Optional[BoxedBoolean]
    IsNegOne: Optional[BoxedBoolean]


class DropNullFields(TypedDict, total=False):
    """Specifies a transform that removes columns from the dataset if all
    values in the column are 'null'. By default, Glue Studio will recognize
    null objects, but some values such as empty strings, strings that are
    "null", -1 integers or other placeholders such as zeros, are not
    automatically recognized as nulls.
    """

    Name: NodeName
    Inputs: OneInput
    NullCheckBoxList: Optional[NullCheckBoxList]
    NullTextList: Optional[NullValueFields]


PositiveLong = int
PollingTime = int


class StreamingDataPreviewOptions(TypedDict, total=False):
    """Specifies options related to data preview for viewing a sample of your
    data.
    """

    PollingTime: Optional[PollingTime]
    RecordPollingLimit: Optional[PositiveLong]


Iso8601DateTime = datetime
BoxedNonNegativeLong = int


class KafkaStreamingSourceOptions(TypedDict, total=False):
    """Additional options for streaming."""

    BootstrapServers: Optional[EnclosedInStringProperty]
    SecurityProtocol: Optional[EnclosedInStringProperty]
    ConnectionName: Optional[EnclosedInStringProperty]
    TopicName: Optional[EnclosedInStringProperty]
    Assign: Optional[EnclosedInStringProperty]
    SubscribePattern: Optional[EnclosedInStringProperty]
    Classification: Optional[EnclosedInStringProperty]
    Delimiter: Optional[EnclosedInStringProperty]
    StartingOffsets: Optional[EnclosedInStringProperty]
    EndingOffsets: Optional[EnclosedInStringProperty]
    PollTimeoutMs: Optional[BoxedNonNegativeLong]
    NumRetries: Optional[BoxedNonNegativeInt]
    RetryIntervalMs: Optional[BoxedNonNegativeLong]
    MaxOffsetsPerTrigger: Optional[BoxedNonNegativeLong]
    MinPartitions: Optional[BoxedNonNegativeInt]
    IncludeHeaders: Optional[BoxedBoolean]
    AddRecordTimestamp: Optional[EnclosedInStringProperty]
    EmitConsumerLagMetrics: Optional[EnclosedInStringProperty]
    StartingTimestamp: Optional[Iso8601DateTime]


class CatalogKafkaSource(TypedDict, total=False):
    """Specifies an Apache Kafka data store in the Data Catalog."""

    Name: NodeName
    WindowSize: Optional[BoxedPositiveInt]
    DetectSchema: Optional[BoxedBoolean]
    Table: EnclosedInStringProperty
    Database: EnclosedInStringProperty
    StreamingOptions: Optional[KafkaStreamingSourceOptions]
    DataPreviewOptions: Optional[StreamingDataPreviewOptions]


class KinesisStreamingSourceOptions(TypedDict, total=False):
    """Additional options for the Amazon Kinesis streaming data source."""

    EndpointUrl: Optional[EnclosedInStringProperty]
    StreamName: Optional[EnclosedInStringProperty]
    Classification: Optional[EnclosedInStringProperty]
    Delimiter: Optional[EnclosedInStringProperty]
    StartingPosition: Optional[StartingPosition]
    MaxFetchTimeInMs: Optional[BoxedNonNegativeLong]
    MaxFetchRecordsPerShard: Optional[BoxedNonNegativeLong]
    MaxRecordPerRead: Optional[BoxedNonNegativeLong]
    AddIdleTimeBetweenReads: Optional[BoxedBoolean]
    IdleTimeBetweenReadsInMs: Optional[BoxedNonNegativeLong]
    DescribeShardInterval: Optional[BoxedNonNegativeLong]
    NumRetries: Optional[BoxedNonNegativeInt]
    RetryIntervalMs: Optional[BoxedNonNegativeLong]
    MaxRetryIntervalMs: Optional[BoxedNonNegativeLong]
    AvoidEmptyBatches: Optional[BoxedBoolean]
    StreamArn: Optional[EnclosedInStringProperty]
    RoleArn: Optional[EnclosedInStringProperty]
    RoleSessionName: Optional[EnclosedInStringProperty]
    AddRecordTimestamp: Optional[EnclosedInStringProperty]
    EmitConsumerLagMetrics: Optional[EnclosedInStringProperty]
    StartingTimestamp: Optional[Iso8601DateTime]


class CatalogKinesisSource(TypedDict, total=False):
    """Specifies a Kinesis data source in the Glue Data Catalog."""

    Name: NodeName
    WindowSize: Optional[BoxedPositiveInt]
    DetectSchema: Optional[BoxedBoolean]
    Table: EnclosedInStringProperty
    Database: EnclosedInStringProperty
    StreamingOptions: Optional[KinesisStreamingSourceOptions]
    DataPreviewOptions: Optional[StreamingDataPreviewOptions]


class DirectKafkaSource(TypedDict, total=False):
    """Specifies an Apache Kafka data store."""

    Name: NodeName
    StreamingOptions: Optional[KafkaStreamingSourceOptions]
    WindowSize: Optional[BoxedPositiveInt]
    DetectSchema: Optional[BoxedBoolean]
    DataPreviewOptions: Optional[StreamingDataPreviewOptions]


class DirectKinesisSource(TypedDict, total=False):
    """Specifies a direct Amazon Kinesis data source."""

    Name: NodeName
    WindowSize: Optional[BoxedPositiveInt]
    DetectSchema: Optional[BoxedBoolean]
    StreamingOptions: Optional[KinesisStreamingSourceOptions]
    DataPreviewOptions: Optional[StreamingDataPreviewOptions]


class SqlAlias(TypedDict, total=False):
    """Represents a single entry in the list of values for ``SqlAliases``."""

    From: NodeId
    Alias: EnclosedInStringPropertyWithQuote


SqlAliases = List[SqlAlias]


class SparkSQL(TypedDict, total=False):
    """Specifies a transform where you enter a SQL query using Spark SQL syntax
    to transform the data. The output is a single ``DynamicFrame``.
    """

    Name: NodeName
    Inputs: ManyInputs
    SqlQuery: SqlQuery
    SqlAliases: SqlAliases
    OutputSchemas: Optional[GlueSchemas]


class CustomCode(TypedDict, total=False):
    """Specifies a transform that uses custom code you provide to perform the
    data transformation. The output is a collection of DynamicFrames.
    """

    Name: NodeName
    Inputs: ManyInputs
    Code: ExtendedString
    ClassName: EnclosedInStringProperty
    OutputSchemas: Optional[GlueSchemas]


class FilterValue(TypedDict, total=False):
    """Represents a single entry in the list of values for a
    ``FilterExpression``.
    """

    Type: FilterValueType
    Value: EnclosedInStringProperties


FilterValues = List[FilterValue]


class FilterExpression(TypedDict, total=False):
    """Specifies a filter expression."""

    Operation: FilterOperation
    Negated: Optional[BoxedBoolean]
    Values: FilterValues


FilterExpressions = List[FilterExpression]


class Filter(TypedDict, total=False):
    """Specifies a transform that splits a dataset into two, based on a filter
    condition.
    """

    Name: NodeName
    Inputs: OneInput
    LogicalOperator: FilterLogicalOperator
    Filters: FilterExpressions


class FillMissingValues(TypedDict, total=False):
    """Specifies a transform that locates records in the dataset that have
    missing values and adds a new field with a value determined by
    imputation. The input data set is used to train the machine learning
    model that determines what the missing value should be.
    """

    Name: NodeName
    Inputs: OneInput
    ImputedPath: EnclosedInStringProperty
    FilledPath: Optional[EnclosedInStringProperty]


class SelectFromCollection(TypedDict, total=False):
    """Specifies a transform that chooses one ``DynamicFrame`` from a
    collection of ``DynamicFrames``. The output is the selected
    ``DynamicFrame``
    """

    Name: NodeName
    Inputs: OneInput
    Index: NonNegativeInt


class SplitFields(TypedDict, total=False):
    """Specifies a transform that splits data property keys into two
    ``DynamicFrames``. The output is a collection of ``DynamicFrames``: one
    with selected data property keys, and one with the remaining data
    property keys.
    """

    Name: NodeName
    Inputs: OneInput
    Paths: GlueStudioPathList


class JoinColumn(TypedDict, total=False):
    """Specifies a column to be joined."""

    From: EnclosedInStringProperty
    Keys: GlueStudioPathList


JoinColumns = List[JoinColumn]


class Join(TypedDict, total=False):
    """Specifies a transform that joins two datasets into one dataset using a
    comparison phrase on the specified data property keys. You can use
    inner, outer, left, right, left semi, and left anti joins.
    """

    Name: NodeName
    Inputs: TwoInputs
    JoinType: JoinType
    Columns: JoinColumns


class Spigot(TypedDict, total=False):
    """Specifies a transform that writes samples of the data to an Amazon S3
    bucket.
    """

    Name: NodeName
    Inputs: OneInput
    Path: EnclosedInStringProperty
    Topk: Optional[Topk]
    Prob: Optional[Prob]


class RenameField(TypedDict, total=False):
    """Specifies a transform that renames a single data property key."""

    Name: NodeName
    Inputs: OneInput
    SourcePath: EnclosedInStringProperties
    TargetPath: EnclosedInStringProperties


class DropFields(TypedDict, total=False):
    """Specifies a transform that chooses the data property keys that you want
    to drop.
    """

    Name: NodeName
    Inputs: OneInput
    Paths: GlueStudioPathList


class SelectFields(TypedDict, total=False):
    """Specifies a transform that chooses the data property keys that you want
    to keep.
    """

    Name: NodeName
    Inputs: OneInput
    Paths: GlueStudioPathList


class S3IcebergDirectTarget(TypedDict, total=False):
    """Specifies a target that writes to an Iceberg data source in Amazon S3."""

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Path: EnclosedInStringProperty
    Format: TargetFormat
    AdditionalOptions: Optional[AdditionalOptions]
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy]
    Compression: IcebergTargetCompressionType
    NumberTargetPartitions: Optional[NumberTargetPartitionsString]


class S3DirectTarget(TypedDict, total=False):
    """Specifies a data target that writes to Amazon S3."""

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Path: EnclosedInStringProperty
    Compression: Optional[EnclosedInStringProperty]
    NumberTargetPartitions: Optional[NumberTargetPartitionsString]
    Format: TargetFormat
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy]


class S3HyperDirectTarget(TypedDict, total=False):
    """Specifies a HyperDirect data target that writes to Amazon S3."""

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Path: EnclosedInStringProperty
    Compression: Optional[HyperTargetCompressionType]
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy]


class S3GlueParquetTarget(TypedDict, total=False):
    """Specifies a data target that writes to Amazon S3 in Apache Parquet
    columnar storage.
    """

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Path: EnclosedInStringProperty
    Compression: Optional[ParquetCompressionType]
    NumberTargetPartitions: Optional[NumberTargetPartitionsString]
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy]


class S3CatalogTarget(TypedDict, total=False):
    """Specifies a data target that writes to Amazon S3 using the Glue Data
    Catalog.
    """

    Name: NodeName
    Inputs: OneInput
    PartitionKeys: Optional[GlueStudioPathList]
    Table: EnclosedInStringProperty
    Database: EnclosedInStringProperty
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy]


EnclosedInStringPropertiesMinOne = List[EnclosedInStringProperty]


class UpsertRedshiftTargetOptions(TypedDict, total=False):
    """The options to configure an upsert operation when writing to a Redshift
    target .
    """

    TableLocation: Optional[EnclosedInStringProperty]
    ConnectionName: Optional[EnclosedInStringProperty]
    UpsertKeys: Optional[EnclosedInStringPropertiesMinOne]


class RedshiftTarget(TypedDict, total=False):
    """Specifies a target that uses Amazon Redshift."""

    Name: NodeName
    Inputs: OneInput
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    RedshiftTmpDir: Optional[EnclosedInStringProperty]
    TmpDirIAMRole: Optional[EnclosedInStringProperty]
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptions]


class SparkConnectorTarget(TypedDict, total=False):
    """Specifies a target that uses an Apache Spark connector."""

    Name: NodeName
    Inputs: OneInput
    ConnectionName: EnclosedInStringProperty
    ConnectorName: EnclosedInStringProperty
    ConnectionType: EnclosedInStringProperty
    AdditionalOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class JDBCConnectorTarget(TypedDict, total=False):
    """Specifies a data target that writes to Amazon S3 in Apache Parquet
    columnar storage.
    """

    Name: NodeName
    Inputs: OneInput
    ConnectionName: EnclosedInStringProperty
    ConnectionTable: EnclosedInStringPropertyWithQuote
    ConnectorName: EnclosedInStringProperty
    ConnectionType: EnclosedInStringProperty
    AdditionalOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class DynamoDBCatalogSource(TypedDict, total=False):
    """Specifies a DynamoDB data source in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class RelationalCatalogSource(TypedDict, total=False):
    """Specifies a Relational database data source in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class S3ParquetSource(TypedDict, total=False):
    """Specifies an Apache Parquet data store stored in Amazon S3."""

    Name: NodeName
    Paths: EnclosedInStringProperties
    CompressionType: Optional[ParquetCompressionType]
    Exclusions: Optional[EnclosedInStringProperties]
    GroupSize: Optional[EnclosedInStringProperty]
    GroupFiles: Optional[EnclosedInStringProperty]
    Recurse: Optional[BoxedBoolean]
    MaxBand: Optional[BoxedNonNegativeInt]
    MaxFilesInBand: Optional[BoxedNonNegativeInt]
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


class S3JsonSource(TypedDict, total=False):
    """Specifies a JSON data store stored in Amazon S3."""

    Name: NodeName
    Paths: EnclosedInStringProperties
    CompressionType: Optional[CompressionType]
    Exclusions: Optional[EnclosedInStringProperties]
    GroupSize: Optional[EnclosedInStringProperty]
    GroupFiles: Optional[EnclosedInStringProperty]
    Recurse: Optional[BoxedBoolean]
    MaxBand: Optional[BoxedNonNegativeInt]
    MaxFilesInBand: Optional[BoxedNonNegativeInt]
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions]
    JsonPath: Optional[EnclosedInStringProperty]
    Multiline: Optional[BoxedBoolean]
    OutputSchemas: Optional[GlueSchemas]


class S3ExcelSource(TypedDict, total=False):
    """Specifies an S3 Excel data source."""

    Name: NodeName
    Paths: EnclosedInStringProperties
    CompressionType: Optional[ParquetCompressionType]
    Exclusions: Optional[EnclosedInStringProperties]
    GroupSize: Optional[EnclosedInStringProperty]
    GroupFiles: Optional[EnclosedInStringProperty]
    Recurse: Optional[BoxedBoolean]
    MaxBand: Optional[BoxedNonNegativeInt]
    MaxFilesInBand: Optional[BoxedNonNegativeInt]
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions]
    NumberRows: Optional[BoxedLong]
    SkipFooter: Optional[BoxedNonNegativeInt]
    OutputSchemas: Optional[GlueSchemas]


class S3CsvSource(TypedDict, total=False):
    """Specifies a command-separated value (CSV) data store stored in Amazon
    S3.
    """

    Name: NodeName
    Paths: EnclosedInStringProperties
    CompressionType: Optional[CompressionType]
    Exclusions: Optional[EnclosedInStringProperties]
    GroupSize: Optional[EnclosedInStringProperty]
    GroupFiles: Optional[EnclosedInStringProperty]
    Recurse: Optional[BoxedBoolean]
    MaxBand: Optional[BoxedNonNegativeInt]
    MaxFilesInBand: Optional[BoxedNonNegativeInt]
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions]
    Separator: Separator
    Escaper: Optional[EnclosedInStringPropertyWithQuote]
    QuoteChar: QuoteChar
    Multiline: Optional[BoxedBoolean]
    WithHeader: Optional[BoxedBoolean]
    WriteHeader: Optional[BoxedBoolean]
    SkipFirst: Optional[BoxedBoolean]
    OptimizePerformance: Optional[BooleanValue]
    OutputSchemas: Optional[GlueSchemas]


class S3CatalogSource(TypedDict, total=False):
    """Specifies an Amazon S3 data store in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    PartitionPredicate: Optional[EnclosedInStringProperty]
    AdditionalOptions: Optional[S3SourceAdditionalOptions]


class RedshiftSource(TypedDict, total=False):
    """Specifies an Amazon Redshift data store."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty
    RedshiftTmpDir: Optional[EnclosedInStringProperty]
    TmpDirIAMRole: Optional[EnclosedInStringProperty]


class CatalogSource(TypedDict, total=False):
    """Specifies a data store in the Glue Data Catalog."""

    Name: NodeName
    Database: EnclosedInStringProperty
    Table: EnclosedInStringProperty


class SparkConnectorSource(TypedDict, total=False):
    """Specifies a connector to an Apache Spark data source."""

    Name: NodeName
    ConnectionName: EnclosedInStringProperty
    ConnectorName: EnclosedInStringProperty
    ConnectionType: EnclosedInStringProperty
    AdditionalOptions: Optional[AdditionalOptions]
    OutputSchemas: Optional[GlueSchemas]


JDBCDataTypeMapping = Dict[JDBCDataType, GlueRecordType]


class JDBCConnectorOptions(TypedDict, total=False):
    """Additional connection options for the connector."""

    FilterPredicate: Optional[EnclosedInStringProperty]
    PartitionColumn: Optional[EnclosedInStringProperty]
    LowerBound: Optional[BoxedNonNegativeLong]
    UpperBound: Optional[BoxedNonNegativeLong]
    NumPartitions: Optional[BoxedNonNegativeLong]
    JobBookmarkKeys: Optional[EnclosedInStringProperties]
    JobBookmarkKeysSortOrder: Optional[EnclosedInStringProperty]
    DataTypeMapping: Optional[JDBCDataTypeMapping]


class JDBCConnectorSource(TypedDict, total=False):
    """Specifies a connector to a JDBC data source."""

    Name: NodeName
    ConnectionName: EnclosedInStringProperty
    ConnectorName: EnclosedInStringProperty
    ConnectionType: EnclosedInStringProperty
    AdditionalOptions: Optional[JDBCConnectorOptions]
    ConnectionTable: Optional[EnclosedInStringPropertyWithQuote]
    Query: Optional[SqlQuery]
    OutputSchemas: Optional[GlueSchemas]


CodeGenConfigurationNode = TypedDict(
    "CodeGenConfigurationNode",
    {
        "AthenaConnectorSource": Optional[AthenaConnectorSource],
        "JDBCConnectorSource": Optional[JDBCConnectorSource],
        "SparkConnectorSource": Optional[SparkConnectorSource],
        "CatalogSource": Optional[CatalogSource],
        "RedshiftSource": Optional[RedshiftSource],
        "S3CatalogSource": Optional[S3CatalogSource],
        "S3CsvSource": Optional[S3CsvSource],
        "S3ExcelSource": Optional[S3ExcelSource],
        "S3JsonSource": Optional[S3JsonSource],
        "S3ParquetSource": Optional[S3ParquetSource],
        "RelationalCatalogSource": Optional[RelationalCatalogSource],
        "DynamoDBCatalogSource": Optional[DynamoDBCatalogSource],
        "JDBCConnectorTarget": Optional[JDBCConnectorTarget],
        "SparkConnectorTarget": Optional[SparkConnectorTarget],
        "CatalogTarget": Optional[BasicCatalogTarget],
        "RedshiftTarget": Optional[RedshiftTarget],
        "S3CatalogTarget": Optional[S3CatalogTarget],
        "S3GlueParquetTarget": Optional[S3GlueParquetTarget],
        "S3HyperDirectTarget": Optional[S3HyperDirectTarget],
        "S3DirectTarget": Optional[S3DirectTarget],
        "S3IcebergDirectTarget": Optional[S3IcebergDirectTarget],
        "ApplyMapping": Optional[ApplyMapping],
        "SelectFields": Optional[SelectFields],
        "DropFields": Optional[DropFields],
        "RenameField": Optional[RenameField],
        "Spigot": Optional[Spigot],
        "Join": Optional[Join],
        "SplitFields": Optional[SplitFields],
        "SelectFromCollection": Optional[SelectFromCollection],
        "FillMissingValues": Optional[FillMissingValues],
        "Filter": Optional[Filter],
        "CustomCode": Optional[CustomCode],
        "SparkSQL": Optional[SparkSQL],
        "DirectKinesisSource": Optional[DirectKinesisSource],
        "DirectKafkaSource": Optional[DirectKafkaSource],
        "CatalogKinesisSource": Optional[CatalogKinesisSource],
        "CatalogKafkaSource": Optional[CatalogKafkaSource],
        "DropNullFields": Optional[DropNullFields],
        "Merge": Optional[Merge],
        "Union": Optional[Union_],
        "PIIDetection": Optional[PIIDetection],
        "Aggregate": Optional[Aggregate],
        "DropDuplicates": Optional[DropDuplicates],
        "GovernedCatalogTarget": Optional[GovernedCatalogTarget],
        "GovernedCatalogSource": Optional[GovernedCatalogSource],
        "MicrosoftSQLServerCatalogSource": Optional[MicrosoftSQLServerCatalogSource],
        "MySQLCatalogSource": Optional[MySQLCatalogSource],
        "OracleSQLCatalogSource": Optional[OracleSQLCatalogSource],
        "PostgreSQLCatalogSource": Optional[PostgreSQLCatalogSource],
        "MicrosoftSQLServerCatalogTarget": Optional[MicrosoftSQLServerCatalogTarget],
        "MySQLCatalogTarget": Optional[MySQLCatalogTarget],
        "OracleSQLCatalogTarget": Optional[OracleSQLCatalogTarget],
        "PostgreSQLCatalogTarget": Optional[PostgreSQLCatalogTarget],
        "DynamicTransform": Optional[DynamicTransform],
        "EvaluateDataQuality": Optional[EvaluateDataQuality],
        "S3CatalogHudiSource": Optional[S3CatalogHudiSource],
        "CatalogHudiSource": Optional[CatalogHudiSource],
        "S3HudiSource": Optional[S3HudiSource],
        "S3HudiCatalogTarget": Optional[S3HudiCatalogTarget],
        "S3HudiDirectTarget": Optional[S3HudiDirectTarget],
        "DirectJDBCSource": Optional[DirectJDBCSource],
        "S3CatalogDeltaSource": Optional[S3CatalogDeltaSource],
        "CatalogDeltaSource": Optional[CatalogDeltaSource],
        "S3DeltaSource": Optional[S3DeltaSource],
        "S3DeltaCatalogTarget": Optional[S3DeltaCatalogTarget],
        "S3DeltaDirectTarget": Optional[S3DeltaDirectTarget],
        "AmazonRedshiftSource": Optional[AmazonRedshiftSource],
        "AmazonRedshiftTarget": Optional[AmazonRedshiftTarget],
        "EvaluateDataQualityMultiFrame": Optional[EvaluateDataQualityMultiFrame],
        "Recipe": Optional[Recipe],
        "SnowflakeSource": Optional[SnowflakeSource],
        "SnowflakeTarget": Optional[SnowflakeTarget],
        "ConnectorDataSource": Optional[ConnectorDataSource],
        "ConnectorDataTarget": Optional[ConnectorDataTarget],
    },
    total=False,
)
CodeGenConfigurationNodes = Dict[NodeId, CodeGenConfigurationNode]
ConnectionStringList = List[ConnectionString]


class ConnectionsList(TypedDict, total=False):
    """Specifies the connections used by a job."""

    Connections: Optional[ConnectionStringList]


class JobCommand(TypedDict, total=False):
    """Specifies code that runs when a job is run."""

    Name: Optional[GenericString]
    ScriptLocation: Optional[ScriptLocationString]
    PythonVersion: Optional[PythonVersionString]
    Runtime: Optional[RuntimeNameString]


class ExecutionProperty(TypedDict, total=False):
    """An execution property of a job."""

    MaxConcurrentRuns: Optional[MaxConcurrentRuns]


class Job(TypedDict, total=False):
    """Specifies a job definition."""

    Name: Optional[NameString]
    JobMode: Optional[JobMode]
    JobRunQueuingEnabled: Optional[NullableBoolean]
    Description: Optional[DescriptionString]
    LogUri: Optional[UriString]
    Role: Optional[RoleString]
    CreatedOn: Optional[TimestampValue]
    LastModifiedOn: Optional[TimestampValue]
    ExecutionProperty: Optional[ExecutionProperty]
    Command: Optional[JobCommand]
    DefaultArguments: Optional[GenericMap]
    NonOverridableArguments: Optional[GenericMap]
    Connections: Optional[ConnectionsList]
    MaxRetries: Optional[MaxRetries]
    AllocatedCapacity: Optional[IntegerValue]
    Timeout: Optional[Timeout]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    SecurityConfiguration: Optional[NameString]
    NotificationProperty: Optional[NotificationProperty]
    GlueVersion: Optional[GlueVersionString]
    CodeGenConfigurationNodes: Optional[CodeGenConfigurationNodes]
    ExecutionClass: Optional[ExecutionClass]
    SourceControlDetails: Optional[SourceControlDetails]
    MaintenanceWindow: Optional[MaintenanceWindow]
    ProfileName: Optional[NameString]


JobList = List[Job]


class BatchGetJobsResponse(TypedDict, total=False):
    Jobs: Optional[JobList]
    JobsNotFound: Optional[JobNameList]


BatchGetPartitionValueList = List[PartitionValueList]


class BatchGetPartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionsToGet: BatchGetPartitionValueList


class Partition(TypedDict, total=False):
    """Represents a slice of table data."""

    Values: Optional[ValueStringList]
    DatabaseName: Optional[NameString]
    TableName: Optional[NameString]
    CreationTime: Optional[Timestamp]
    LastAccessTime: Optional[Timestamp]
    StorageDescriptor: Optional[StorageDescriptor]
    Parameters: Optional[ParametersMap]
    LastAnalyzedTime: Optional[Timestamp]
    CatalogId: Optional[CatalogIdString]


PartitionList = List[Partition]


class BatchGetPartitionResponse(TypedDict, total=False):
    Partitions: Optional[PartitionList]
    UnprocessedKeys: Optional[BatchGetPartitionValueList]


BatchGetTableOptimizerEntry = TypedDict(
    "BatchGetTableOptimizerEntry",
    {
        "catalogId": Optional[CatalogIdString],
        "databaseName": Optional[databaseNameString],
        "tableName": Optional[tableNameString],
        "type": Optional[TableOptimizerType],
    },
    total=False,
)
BatchGetTableOptimizerEntries = List[BatchGetTableOptimizerEntry]
BatchGetTableOptimizerError = TypedDict(
    "BatchGetTableOptimizerError",
    {
        "error": Optional[ErrorDetail],
        "catalogId": Optional[CatalogIdString],
        "databaseName": Optional[databaseNameString],
        "tableName": Optional[tableNameString],
        "type": Optional[TableOptimizerType],
    },
    total=False,
)
BatchGetTableOptimizerErrors = List[BatchGetTableOptimizerError]


class BatchGetTableOptimizerRequest(ServiceRequest):
    Entries: BatchGetTableOptimizerEntries


metricCounts = int


class IcebergOrphanFileDeletionMetrics(TypedDict, total=False):
    """Orphan file deletion metrics for Iceberg for the optimizer run."""

    NumberOfOrphanFilesDeleted: Optional[metricCounts]
    DpuHours: Optional[dpuHours]
    NumberOfDpus: Optional[dpuCounts]
    JobDurationInHour: Optional[dpuDurationInHour]


class OrphanFileDeletionMetrics(TypedDict, total=False):
    """A structure that contains orphan file deletion metrics for the optimizer
    run.
    """

    IcebergMetrics: Optional[IcebergOrphanFileDeletionMetrics]


class IcebergRetentionMetrics(TypedDict, total=False):
    """Snapshot retention metrics for Iceberg for the optimizer run."""

    NumberOfDataFilesDeleted: Optional[metricCounts]
    NumberOfManifestFilesDeleted: Optional[metricCounts]
    NumberOfManifestListsDeleted: Optional[metricCounts]
    DpuHours: Optional[dpuHours]
    NumberOfDpus: Optional[dpuCounts]
    JobDurationInHour: Optional[dpuDurationInHour]


class RetentionMetrics(TypedDict, total=False):
    """A structure that contains retention metrics for the optimizer run."""

    IcebergMetrics: Optional[IcebergRetentionMetrics]


class IcebergCompactionMetrics(TypedDict, total=False):
    """Compaction metrics for Iceberg for the optimizer run."""

    NumberOfBytesCompacted: Optional[metricCounts]
    NumberOfFilesCompacted: Optional[metricCounts]
    DpuHours: Optional[dpuHours]
    NumberOfDpus: Optional[dpuCounts]
    JobDurationInHour: Optional[dpuDurationInHour]


class CompactionMetrics(TypedDict, total=False):
    """A structure that contains compaction metrics for the optimizer run."""

    IcebergMetrics: Optional[IcebergCompactionMetrics]


class RunMetrics(TypedDict, total=False):
    """Metrics for the optimizer run.

    This structure is deprecated. See the individual metric members for
    compaction, retention, and orphan file deletion.
    """

    NumberOfBytesCompacted: Optional[MessageString]
    NumberOfFilesCompacted: Optional[MessageString]
    NumberOfDpus: Optional[MessageString]
    JobDurationInHour: Optional[MessageString]


TableOptimizerRunTimestamp = datetime


class TableOptimizerRun(TypedDict, total=False):
    """Contains details for a table optimizer run."""

    eventType: Optional[TableOptimizerEventType]
    startTimestamp: Optional[TableOptimizerRunTimestamp]
    endTimestamp: Optional[TableOptimizerRunTimestamp]
    metrics: Optional[RunMetrics]
    error: Optional[MessageString]
    compactionMetrics: Optional[CompactionMetrics]
    retentionMetrics: Optional[RetentionMetrics]
    orphanFileDeletionMetrics: Optional[OrphanFileDeletionMetrics]


class IcebergOrphanFileDeletionConfiguration(TypedDict, total=False):
    """The configuration for an Iceberg orphan file deletion optimizer."""

    orphanFileRetentionPeriodInDays: Optional[NullableInteger]
    location: Optional[MessageString]


class OrphanFileDeletionConfiguration(TypedDict, total=False):
    """The configuration for an orphan file deletion optimizer."""

    icebergConfiguration: Optional[IcebergOrphanFileDeletionConfiguration]


class IcebergRetentionConfiguration(TypedDict, total=False):
    """The configuration for an Iceberg snapshot retention optimizer."""

    snapshotRetentionPeriodInDays: Optional[NullableInteger]
    numberOfSnapshotsToRetain: Optional[NullableInteger]
    cleanExpiredFiles: Optional[NullableBoolean]


class RetentionConfiguration(TypedDict, total=False):
    """The configuration for a snapshot retention optimizer."""

    icebergConfiguration: Optional[IcebergRetentionConfiguration]


class TableOptimizerVpcConfiguration(TypedDict, total=False):
    """An object that describes the VPC configuration for a table optimizer.

    This configuration is necessary to perform optimization on tables that
    are in a customer VPC.
    """

    glueConnectionName: Optional[glueConnectionNameString]


class TableOptimizerConfiguration(TypedDict, total=False):
    """Contains details on the configuration of a table optimizer. You pass
    this configuration when creating or updating a table optimizer.
    """

    roleArn: Optional[ArnString]
    enabled: Optional[NullableBoolean]
    vpcConfiguration: Optional[TableOptimizerVpcConfiguration]
    retentionConfiguration: Optional[RetentionConfiguration]
    orphanFileDeletionConfiguration: Optional[OrphanFileDeletionConfiguration]


TableOptimizer = TypedDict(
    "TableOptimizer",
    {
        "type": Optional[TableOptimizerType],
        "configuration": Optional[TableOptimizerConfiguration],
        "lastRun": Optional[TableOptimizerRun],
    },
    total=False,
)


class BatchTableOptimizer(TypedDict, total=False):
    """Contains details for one of the table optimizers returned by the
    ``BatchGetTableOptimizer`` operation.
    """

    catalogId: Optional[CatalogIdString]
    databaseName: Optional[databaseNameString]
    tableName: Optional[tableNameString]
    tableOptimizer: Optional[TableOptimizer]


BatchTableOptimizers = List[BatchTableOptimizer]


class BatchGetTableOptimizerResponse(TypedDict, total=False):
    TableOptimizers: Optional[BatchTableOptimizers]
    Failures: Optional[BatchGetTableOptimizerErrors]


TriggerNameList = List[NameString]


class BatchGetTriggersRequest(ServiceRequest):
    TriggerNames: TriggerNameList


class EventBatchingCondition(TypedDict, total=False):
    """Batch condition that must be met (specified number of events received or
    batch time window expired) before EventBridge event trigger fires.
    """

    BatchSize: BatchSize
    BatchWindow: Optional[BatchWindow]


class Condition(TypedDict, total=False):
    """Defines a condition under which a trigger fires."""

    LogicalOperator: Optional[LogicalOperator]
    JobName: Optional[NameString]
    State: Optional[JobRunState]
    CrawlerName: Optional[NameString]
    CrawlState: Optional[CrawlState]


ConditionList = List[Condition]


class Predicate(TypedDict, total=False):
    """Defines the predicate of the trigger, which determines when it fires."""

    Logical: Optional[Logical]
    Conditions: Optional[ConditionList]


class Trigger(TypedDict, total=False):
    """Information about a specific trigger."""

    Name: Optional[NameString]
    WorkflowName: Optional[NameString]
    Id: Optional[IdString]
    Type: Optional[TriggerType]
    State: Optional[TriggerState]
    Description: Optional[DescriptionString]
    Schedule: Optional[GenericString]
    Actions: Optional[ActionList]
    Predicate: Optional[Predicate]
    EventBatchingCondition: Optional[EventBatchingCondition]


TriggerList = List[Trigger]


class BatchGetTriggersResponse(TypedDict, total=False):
    Triggers: Optional[TriggerList]
    TriggersNotFound: Optional[TriggerNameList]


WorkflowNames = List[NameString]


class BatchGetWorkflowsRequest(ServiceRequest):
    Names: WorkflowNames
    IncludeGraph: Optional[NullableBoolean]


class BlueprintDetails(TypedDict, total=False):
    """The details of a blueprint."""

    BlueprintName: Optional[OrchestrationNameString]
    RunId: Optional[IdString]


class Edge(TypedDict, total=False):
    """An edge represents a directed connection between two Glue components
    that are part of the workflow the edge belongs to.
    """

    SourceId: Optional[NameString]
    DestinationId: Optional[NameString]


EdgeList = List[Edge]


class Crawl(TypedDict, total=False):
    """The details of a crawl in the workflow."""

    State: Optional[CrawlState]
    StartedOn: Optional[TimestampValue]
    CompletedOn: Optional[TimestampValue]
    ErrorMessage: Optional[DescriptionString]
    LogGroup: Optional[LogGroup]
    LogStream: Optional[LogStream]


CrawlList = List[Crawl]


class CrawlerNodeDetails(TypedDict, total=False):
    """The details of a Crawler node present in the workflow."""

    Crawls: Optional[CrawlList]


class Predecessor(TypedDict, total=False):
    """A job run that was used in the predicate of a conditional trigger that
    triggered this job run.
    """

    JobName: Optional[NameString]
    RunId: Optional[IdString]


PredecessorList = List[Predecessor]


class JobRun(TypedDict, total=False):
    """Contains information about a job run."""

    Id: Optional[IdString]
    Attempt: Optional[AttemptCount]
    PreviousRunId: Optional[IdString]
    TriggerName: Optional[NameString]
    JobName: Optional[NameString]
    JobMode: Optional[JobMode]
    JobRunQueuingEnabled: Optional[NullableBoolean]
    StartedOn: Optional[TimestampValue]
    LastModifiedOn: Optional[TimestampValue]
    CompletedOn: Optional[TimestampValue]
    JobRunState: Optional[JobRunState]
    Arguments: Optional[GenericMap]
    ErrorMessage: Optional[ErrorString]
    PredecessorRuns: Optional[PredecessorList]
    AllocatedCapacity: Optional[IntegerValue]
    ExecutionTime: Optional[ExecutionTime]
    Timeout: Optional[Timeout]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    SecurityConfiguration: Optional[NameString]
    LogGroupName: Optional[GenericString]
    NotificationProperty: Optional[NotificationProperty]
    GlueVersion: Optional[GlueVersionString]
    DPUSeconds: Optional[NullableDouble]
    ExecutionClass: Optional[ExecutionClass]
    MaintenanceWindow: Optional[MaintenanceWindow]
    ProfileName: Optional[NameString]
    StateDetail: Optional[OrchestrationMessageString]


JobRunList = List[JobRun]


class JobNodeDetails(TypedDict, total=False):
    """The details of a Job node present in the workflow."""

    JobRuns: Optional[JobRunList]


class TriggerNodeDetails(TypedDict, total=False):
    """The details of a Trigger node present in the workflow."""

    Trigger: Optional[Trigger]


class Node(TypedDict, total=False):
    """A node represents an Glue component (trigger, crawler, or job) on a
    workflow graph.
    """

    Type: Optional[NodeType]
    Name: Optional[NameString]
    UniqueId: Optional[NameString]
    TriggerDetails: Optional[TriggerNodeDetails]
    JobDetails: Optional[JobNodeDetails]
    CrawlerDetails: Optional[CrawlerNodeDetails]


NodeList = List[Node]


class WorkflowGraph(TypedDict, total=False):
    """A workflow graph represents the complete workflow containing all the
    Glue components present in the workflow and all the directed connections
    between them.
    """

    Nodes: Optional[NodeList]
    Edges: Optional[EdgeList]


class StartingEventBatchCondition(TypedDict, total=False):
    """The batch condition that started the workflow run. Either the number of
    events in the batch size arrived, in which case the BatchSize member is
    non-zero, or the batch window expired, in which case the BatchWindow
    member is non-zero.
    """

    BatchSize: Optional[NullableInteger]
    BatchWindow: Optional[NullableInteger]


class WorkflowRunStatistics(TypedDict, total=False):
    """Workflow run statistics provides statistics about the workflow run."""

    TotalActions: Optional[IntegerValue]
    TimeoutActions: Optional[IntegerValue]
    FailedActions: Optional[IntegerValue]
    StoppedActions: Optional[IntegerValue]
    SucceededActions: Optional[IntegerValue]
    RunningActions: Optional[IntegerValue]
    ErroredActions: Optional[IntegerValue]
    WaitingActions: Optional[IntegerValue]


WorkflowRunProperties = Dict[IdString, GenericString]


class WorkflowRun(TypedDict, total=False):
    """A workflow run is an execution of a workflow providing all the runtime
    information.
    """

    Name: Optional[NameString]
    WorkflowRunId: Optional[IdString]
    PreviousRunId: Optional[IdString]
    WorkflowRunProperties: Optional[WorkflowRunProperties]
    StartedOn: Optional[TimestampValue]
    CompletedOn: Optional[TimestampValue]
    Status: Optional[WorkflowRunStatus]
    ErrorMessage: Optional[ErrorString]
    Statistics: Optional[WorkflowRunStatistics]
    Graph: Optional[WorkflowGraph]
    StartingEventBatchCondition: Optional[StartingEventBatchCondition]


class Workflow(TypedDict, total=False):
    """A workflow is a collection of multiple dependent Glue jobs and crawlers
    that are run to complete a complex ETL task. A workflow manages the
    execution and monitoring of all its jobs and crawlers.
    """

    Name: Optional[NameString]
    Description: Optional[GenericString]
    DefaultRunProperties: Optional[WorkflowRunProperties]
    CreatedOn: Optional[TimestampValue]
    LastModifiedOn: Optional[TimestampValue]
    LastRun: Optional[WorkflowRun]
    Graph: Optional[WorkflowGraph]
    MaxConcurrentRuns: Optional[NullableInteger]
    BlueprintDetails: Optional[BlueprintDetails]


Workflows = List[Workflow]


class BatchGetWorkflowsResponse(TypedDict, total=False):
    Workflows: Optional[Workflows]
    MissingWorkflows: Optional[WorkflowNames]


class DatapointInclusionAnnotation(TypedDict, total=False):
    """An Inclusion Annotation."""

    ProfileId: Optional[HashString]
    StatisticId: Optional[HashString]
    InclusionAnnotation: Optional[InclusionAnnotationValue]


InclusionAnnotationList = List[DatapointInclusionAnnotation]


class BatchPutDataQualityStatisticAnnotationRequest(ServiceRequest):
    InclusionAnnotations: InclusionAnnotationList
    ClientToken: Optional[HashString]


class BatchPutDataQualityStatisticAnnotationResponse(TypedDict, total=False):
    FailedInclusionAnnotations: Optional[AnnotationErrorList]


class BatchStopJobRunError(TypedDict, total=False):
    """Records an error that occurred when attempting to stop a specified job
    run.
    """

    JobName: Optional[NameString]
    JobRunId: Optional[IdString]
    ErrorDetail: Optional[ErrorDetail]


BatchStopJobRunErrorList = List[BatchStopJobRunError]
BatchStopJobRunJobRunIdList = List[IdString]


class BatchStopJobRunRequest(ServiceRequest):
    JobName: NameString
    JobRunIds: BatchStopJobRunJobRunIdList


class BatchStopJobRunSuccessfulSubmission(TypedDict, total=False):
    """Records a successful request to stop a specified ``JobRun``."""

    JobName: Optional[NameString]
    JobRunId: Optional[IdString]


BatchStopJobRunSuccessfulSubmissionList = List[BatchStopJobRunSuccessfulSubmission]


class BatchStopJobRunResponse(TypedDict, total=False):
    SuccessfulSubmissions: Optional[BatchStopJobRunSuccessfulSubmissionList]
    Errors: Optional[BatchStopJobRunErrorList]


BoundedPartitionValueList = List[ValueString]


class BatchUpdatePartitionFailureEntry(TypedDict, total=False):
    """Contains information about a batch update partition error."""

    PartitionValueList: Optional[BoundedPartitionValueList]
    ErrorDetail: Optional[ErrorDetail]


BatchUpdatePartitionFailureList = List[BatchUpdatePartitionFailureEntry]


class BatchUpdatePartitionRequestEntry(TypedDict, total=False):
    """A structure that contains the values and structure used to update a
    partition.
    """

    PartitionValueList: BoundedPartitionValueList
    PartitionInput: PartitionInput


BatchUpdatePartitionRequestEntryList = List[BatchUpdatePartitionRequestEntry]


class BatchUpdatePartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    Entries: BatchUpdatePartitionRequestEntryList


class BatchUpdatePartitionResponse(TypedDict, total=False):
    Errors: Optional[BatchUpdatePartitionFailureList]


NonNegativeLong = int


class BinaryColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for bit sequence data values."""

    MaximumLength: NonNegativeLong
    AverageLength: NonNegativeDouble
    NumberOfNulls: NonNegativeLong


Blob = bytes


class BlueprintRun(TypedDict, total=False):
    """The details of a blueprint run."""

    BlueprintName: Optional[OrchestrationNameString]
    RunId: Optional[IdString]
    WorkflowName: Optional[NameString]
    State: Optional[BlueprintRunState]
    StartedOn: Optional[TimestampValue]
    CompletedOn: Optional[TimestampValue]
    ErrorMessage: Optional[MessageString]
    RollbackErrorMessage: Optional[MessageString]
    Parameters: Optional[BlueprintParameters]
    RoleArn: Optional[OrchestrationIAMRoleArn]


BlueprintRuns = List[BlueprintRun]


class BooleanColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for Boolean data columns."""

    NumberOfTrues: NonNegativeLong
    NumberOfFalses: NonNegativeLong
    NumberOfNulls: NonNegativeLong


class CancelDataQualityRuleRecommendationRunRequest(ServiceRequest):
    RunId: HashString


class CancelDataQualityRuleRecommendationRunResponse(TypedDict, total=False):
    pass


class CancelDataQualityRulesetEvaluationRunRequest(ServiceRequest):
    RunId: HashString


class CancelDataQualityRulesetEvaluationRunResponse(TypedDict, total=False):
    pass


class CancelMLTaskRunRequest(ServiceRequest):
    TransformId: HashString
    TaskRunId: HashString


class CancelMLTaskRunResponse(TypedDict, total=False):
    TransformId: Optional[HashString]
    TaskRunId: Optional[HashString]
    Status: Optional[TaskStatusType]


class CancelStatementRequest(ServiceRequest):
    SessionId: NameString
    Id: IntegerValue
    RequestOrigin: Optional[OrchestrationNameString]


class CancelStatementResponse(TypedDict, total=False):
    pass


ComputeEnvironments = List[ComputeEnvironment]


class Capabilities(TypedDict, total=False):
    """Specifies the supported authentication types returned by the
    ``DescribeConnectionType`` API.
    """

    SupportedAuthenticationTypes: AuthenticationTypes
    SupportedDataOperations: DataOperations
    SupportedComputeEnvironments: ComputeEnvironments


PermissionList = List[Permission]


class DataLakePrincipal(TypedDict, total=False):
    """The Lake Formation principal."""

    DataLakePrincipalIdentifier: Optional[DataLakePrincipalString]


class PrincipalPermissions(TypedDict, total=False):
    """Permissions granted to a principal."""

    Principal: Optional[DataLakePrincipal]
    Permissions: Optional[PermissionList]


PrincipalPermissionsList = List[PrincipalPermissions]


class DataLakeAccessPropertiesOutput(TypedDict, total=False):
    """The output properties of the data lake access configuration for your
    catalog resource in the Glue Data Catalog.
    """

    DataLakeAccess: Optional[Boolean]
    DataTransferRole: Optional[IAMRoleArn]
    KmsKey: Optional[ResourceArnString]
    ManagedWorkgroupName: Optional[NameString]
    ManagedWorkgroupStatus: Optional[NameString]
    RedshiftDatabaseName: Optional[NameString]
    StatusMessage: Optional[NameString]
    CatalogType: Optional[NameString]


class CatalogPropertiesOutput(TypedDict, total=False):
    """Property attributes that include configuration properties for the
    catalog resource.
    """

    DataLakeAccessProperties: Optional[DataLakeAccessPropertiesOutput]
    CustomProperties: Optional[ParametersMap]


class FederatedCatalog(TypedDict, total=False):
    """A catalog that points to an entity outside the Glue Data Catalog."""

    Identifier: Optional[FederationIdentifier]
    ConnectionName: Optional[NameString]


class TargetRedshiftCatalog(TypedDict, total=False):
    """A structure that describes a target catalog for resource linking."""

    CatalogArn: ResourceArnString


class Catalog(TypedDict, total=False):
    """The catalog object represents a logical grouping of databases in the
    Glue Data Catalog or a federated source. You can now create a
    Redshift-federated catalog or a catalog containing resource links to
    Redshift databases in another account or region.
    """

    CatalogId: Optional[CatalogIdString]
    Name: CatalogNameString
    ResourceArn: Optional[ResourceArnString]
    Description: Optional[DescriptionString]
    Parameters: Optional[ParametersMap]
    CreateTime: Optional[Timestamp]
    UpdateTime: Optional[Timestamp]
    TargetRedshiftCatalog: Optional[TargetRedshiftCatalog]
    FederatedCatalog: Optional[FederatedCatalog]
    CatalogProperties: Optional[CatalogPropertiesOutput]
    CreateTableDefaultPermissions: Optional[PrincipalPermissionsList]
    CreateDatabaseDefaultPermissions: Optional[PrincipalPermissionsList]
    AllowFullTableExternalDataAccess: Optional[AllowFullTableExternalDataAccessEnum]


class CatalogEntry(TypedDict, total=False):
    """Specifies a table definition in the Glue Data Catalog."""

    DatabaseName: NameString
    TableName: NameString


CatalogEntries = List[CatalogEntry]


class CatalogImportStatus(TypedDict, total=False):
    """A structure containing migration status information."""

    ImportCompleted: Optional[Boolean]
    ImportTime: Optional[Timestamp]
    ImportedBy: Optional[NameString]


class DataLakeAccessProperties(TypedDict, total=False):
    """Input properties to configure data lake access for your catalog resource
    in the Glue Data Catalog.
    """

    DataLakeAccess: Optional[Boolean]
    DataTransferRole: Optional[IAMRoleArn]
    KmsKey: Optional[ResourceArnString]
    CatalogType: Optional[NameString]


class CatalogProperties(TypedDict, total=False):
    """A structure that specifies data lake access properties and other custom
    properties.
    """

    DataLakeAccessProperties: Optional[DataLakeAccessProperties]
    CustomProperties: Optional[ParametersMap]


class CatalogInput(TypedDict, total=False):
    """A structure that describes catalog properties."""

    Description: Optional[DescriptionString]
    FederatedCatalog: Optional[FederatedCatalog]
    Parameters: Optional[ParametersMap]
    TargetRedshiftCatalog: Optional[TargetRedshiftCatalog]
    CatalogProperties: Optional[CatalogProperties]
    CreateTableDefaultPermissions: Optional[PrincipalPermissionsList]
    CreateDatabaseDefaultPermissions: Optional[PrincipalPermissionsList]
    AllowFullTableExternalDataAccess: Optional[AllowFullTableExternalDataAccessEnum]


CatalogList = List[Catalog]


class CheckSchemaVersionValidityInput(ServiceRequest):
    DataFormat: DataFormat
    SchemaDefinition: SchemaDefinitionString


class CheckSchemaVersionValidityResponse(TypedDict, total=False):
    Valid: Optional[IsVersionValid]
    Error: Optional[SchemaValidationError]


CustomDatatypes = List[NameString]
CsvHeader = List[NameString]


class CsvClassifier(TypedDict, total=False):
    """A classifier for custom ``CSV`` content."""

    Name: NameString
    CreationTime: Optional[Timestamp]
    LastUpdated: Optional[Timestamp]
    Version: Optional[VersionId]
    Delimiter: Optional[CsvColumnDelimiter]
    QuoteSymbol: Optional[CsvQuoteSymbol]
    ContainsHeader: Optional[CsvHeaderOption]
    Header: Optional[CsvHeader]
    DisableValueTrimming: Optional[NullableBoolean]
    AllowSingleColumn: Optional[NullableBoolean]
    CustomDatatypeConfigured: Optional[NullableBoolean]
    CustomDatatypes: Optional[CustomDatatypes]
    Serde: Optional[CsvSerdeOption]


class JsonClassifier(TypedDict, total=False):
    """A classifier for ``JSON`` content."""

    Name: NameString
    CreationTime: Optional[Timestamp]
    LastUpdated: Optional[Timestamp]
    Version: Optional[VersionId]
    JsonPath: JsonPath


class XMLClassifier(TypedDict, total=False):
    """A classifier for ``XML`` content."""

    Name: NameString
    Classification: Classification
    CreationTime: Optional[Timestamp]
    LastUpdated: Optional[Timestamp]
    Version: Optional[VersionId]
    RowTag: Optional[RowTag]


class GrokClassifier(TypedDict, total=False):
    """A classifier that uses ``grok`` patterns."""

    Name: NameString
    Classification: Classification
    CreationTime: Optional[Timestamp]
    LastUpdated: Optional[Timestamp]
    Version: Optional[VersionId]
    GrokPattern: GrokPattern
    CustomPatterns: Optional[CustomPatterns]


class Classifier(TypedDict, total=False):
    """Classifiers are triggered during a crawl task. A classifier checks
    whether a given file is in a format it can handle. If it is, the
    classifier creates a schema in the form of a ``StructType`` object that
    matches that data format.

    You can use the standard classifiers that Glue provides, or you can
    write your own classifiers to best categorize your data sources and
    specify the appropriate schemas to use for them. A classifier can be a
    ``grok`` classifier, an ``XML`` classifier, a ``JSON`` classifier, or a
    custom ``CSV`` classifier, as specified in one of the fields in the
    ``Classifier`` object.
    """

    GrokClassifier: Optional[GrokClassifier]
    XMLClassifier: Optional[XMLClassifier]
    JsonClassifier: Optional[JsonClassifier]
    CsvClassifier: Optional[CsvClassifier]


ClassifierList = List[Classifier]


class CloudWatchEncryption(TypedDict, total=False):
    """Specifies how Amazon CloudWatch data should be encrypted."""

    CloudWatchEncryptionMode: Optional[CloudWatchEncryptionMode]
    KmsKeyArn: Optional[KmsKeyArn]


class CodeGenEdge(TypedDict, total=False):
    """Represents a directional edge in a directed acyclic graph (DAG)."""

    Source: CodeGenIdentifier
    Target: CodeGenIdentifier
    TargetParameter: Optional[CodeGenArgName]


class CodeGenNodeArg(TypedDict, total=False):
    """An argument or property of a node."""

    Name: CodeGenArgName
    Value: CodeGenArgValue
    Param: Optional[Boolean]


CodeGenNodeArgs = List[CodeGenNodeArg]


class CodeGenNode(TypedDict, total=False):
    """Represents a node in a directed acyclic graph (DAG)"""

    Id: CodeGenIdentifier
    NodeType: CodeGenNodeType
    Args: CodeGenNodeArgs
    LineNumber: Optional[Integer]


class ColumnError(TypedDict, total=False):
    """Encapsulates a column name that failed and the reason for failure."""

    ColumnName: Optional[NameString]
    Error: Optional[ErrorDetail]


ColumnErrors = List[ColumnError]


class ColumnImportance(TypedDict, total=False):
    """A structure containing the column name and column importance score for a
    column.

    Column importance helps you understand how columns contribute to your
    model, by identifying which columns in your records are more important
    than others.
    """

    ColumnName: Optional[NameString]
    Importance: Optional[GenericBoundedDouble]


ColumnImportanceList = List[ColumnImportance]
ColumnNameList = List[NameString]


class ColumnRowFilter(TypedDict, total=False):
    """A filter that uses both column-level and row-level filtering."""

    ColumnName: Optional[NameString]
    RowFilterExpression: Optional[PredicateString]


ColumnRowFilterList = List[ColumnRowFilter]


class StringColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for character sequence data values."""

    MaximumLength: NonNegativeLong
    AverageLength: NonNegativeDouble
    NumberOfNulls: NonNegativeLong
    NumberOfDistinctValues: NonNegativeLong


Long = int


class LongColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for integer data columns."""

    MinimumValue: Optional[Long]
    MaximumValue: Optional[Long]
    NumberOfNulls: NonNegativeLong
    NumberOfDistinctValues: NonNegativeLong


class DoubleColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for floating-point number data
    columns.
    """

    MinimumValue: Optional[Double]
    MaximumValue: Optional[Double]
    NumberOfNulls: NonNegativeLong
    NumberOfDistinctValues: NonNegativeLong


class DecimalNumber(TypedDict, total=False):
    """Contains a numeric value in decimal format."""

    UnscaledValue: Blob
    Scale: Integer


class DecimalColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for fixed-point number data columns."""

    MinimumValue: Optional[DecimalNumber]
    MaximumValue: Optional[DecimalNumber]
    NumberOfNulls: NonNegativeLong
    NumberOfDistinctValues: NonNegativeLong


class DateColumnStatisticsData(TypedDict, total=False):
    """Defines column statistics supported for timestamp data columns."""

    MinimumValue: Optional[Timestamp]
    MaximumValue: Optional[Timestamp]
    NumberOfNulls: NonNegativeLong
    NumberOfDistinctValues: NonNegativeLong


class ColumnStatisticsData(TypedDict, total=False):
    """Contains the individual types of column statistics data. Only one data
    object should be set and indicated by the ``Type`` attribute.
    """

    Type: ColumnStatisticsType
    BooleanColumnStatisticsData: Optional[BooleanColumnStatisticsData]
    DateColumnStatisticsData: Optional[DateColumnStatisticsData]
    DecimalColumnStatisticsData: Optional[DecimalColumnStatisticsData]
    DoubleColumnStatisticsData: Optional[DoubleColumnStatisticsData]
    LongColumnStatisticsData: Optional[LongColumnStatisticsData]
    StringColumnStatisticsData: Optional[StringColumnStatisticsData]
    BinaryColumnStatisticsData: Optional[BinaryColumnStatisticsData]


class ColumnStatistics(TypedDict, total=False):
    """Represents the generated column-level statistics for a table or
    partition.
    """

    ColumnName: NameString
    ColumnType: TypeString
    AnalyzedTime: Timestamp
    StatisticsData: ColumnStatisticsData


class ColumnStatisticsError(TypedDict, total=False):
    """Encapsulates a ``ColumnStatistics`` object that failed and the reason
    for failure.
    """

    ColumnStatistics: Optional[ColumnStatistics]
    Error: Optional[ErrorDetail]


ColumnStatisticsErrors = List[ColumnStatisticsError]
ColumnStatisticsList = List[ColumnStatistics]


class ColumnStatisticsTaskRun(TypedDict, total=False):
    """The object that shows the details of the column stats run."""

    CustomerId: Optional[AccountId]
    ColumnStatisticsTaskRunId: Optional[HashString]
    DatabaseName: Optional[DatabaseName]
    TableName: Optional[TableName]
    ColumnNameList: Optional[ColumnNameList]
    CatalogID: Optional[CatalogIdString]
    Role: Optional[Role]
    SampleSize: Optional[SampleSizePercentage]
    SecurityConfiguration: Optional[CrawlerSecurityConfiguration]
    NumberOfWorkers: Optional[PositiveInteger]
    WorkerType: Optional[NameString]
    ComputationType: Optional[ComputationType]
    Status: Optional[ColumnStatisticsState]
    CreationTime: Optional[Timestamp]
    LastUpdated: Optional[Timestamp]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    ErrorMessage: Optional[DescriptionString]
    DPUSeconds: Optional[NonNegativeDouble]


ColumnStatisticsTaskRunIdList = List[HashString]
ColumnStatisticsTaskRunsList = List[ColumnStatisticsTaskRun]


class ExecutionAttempt(TypedDict, total=False):
    """A run attempt for a column statistics task run."""

    Status: Optional[ExecutionStatus]
    ColumnStatisticsTaskRunId: Optional[HashString]
    ExecutionTimestamp: Optional[Timestamp]
    ErrorMessage: Optional[DescriptionString]


class ColumnStatisticsTaskSettings(TypedDict, total=False):
    """The settings for a column statistics task."""

    DatabaseName: Optional[DatabaseName]
    TableName: Optional[TableName]
    Schedule: Optional[Schedule]
    ColumnNameList: Optional[ColumnNameList]
    CatalogID: Optional[CatalogIdString]
    Role: Optional[Role]
    SampleSize: Optional[SampleSizePercentage]
    SecurityConfiguration: Optional[CrawlerSecurityConfiguration]
    ScheduleType: Optional[ScheduleType]
    SettingSource: Optional[SettingSource]
    LastExecutionAttempt: Optional[ExecutionAttempt]


ListOfString = List[String]
PropertyNameOverrides = Dict[PropertyName, PropertyName]


class ComputeEnvironmentConfiguration(TypedDict, total=False):
    """An object containing configuration for a compute environment (such as
    Spark, Python or Athena) returned by the ``DescribeConnectionType`` API.
    """

    Name: ComputeEnvironmentName
    Description: ComputeEnvironmentConfigurationDescriptionString
    ComputeEnvironment: ComputeEnvironment
    SupportedAuthenticationTypes: AuthenticationTypes
    ConnectionOptions: PropertiesMap
    ConnectionPropertyNameOverrides: PropertyNameOverrides
    ConnectionOptionNameOverrides: PropertyNameOverrides
    ConnectionPropertiesRequiredOverrides: ListOfString
    PhysicalConnectionPropertiesRequired: Optional[Bool]


ComputeEnvironmentConfigurationMap = Dict[ComputeEnvironmentName, ComputeEnvironmentConfiguration]
ComputeEnvironmentList = List[ComputeEnvironment]


class ConfigurationObject(TypedDict, total=False):
    """Specifies the values that an admin sets for each job or session
    parameter configured in a Glue usage profile.
    """

    DefaultValue: Optional[ConfigValueString]
    AllowedValues: Optional[AllowedValuesStringList]
    MinValue: Optional[ConfigValueString]
    MaxValue: Optional[ConfigValueString]


ConfigurationMap = Dict[NameString, ConfigurationObject]
RecordsCount = int


class ConfusionMatrix(TypedDict, total=False):
    """The confusion matrix shows you what your transform is predicting
    accurately and what types of errors it is making.

    For more information, see `Confusion
    matrix <https://en.wikipedia.org/wiki/Confusion_matrix>`__ in Wikipedia.
    """

    NumTruePositives: Optional[RecordsCount]
    NumFalsePositives: Optional[RecordsCount]
    NumTrueNegatives: Optional[RecordsCount]
    NumFalseNegatives: Optional[RecordsCount]


SecurityGroupIdList = List[NameString]


class PhysicalConnectionRequirements(TypedDict, total=False):
    """The OAuth client app in GetConnection response."""

    SubnetId: Optional[NameString]
    SecurityGroupIdList: Optional[SecurityGroupIdList]
    AvailabilityZone: Optional[NameString]


PropertyMap = Dict[PropertyKey, PropertyValue]
ConnectionProperties = Dict[ConnectionPropertyKey, ValueString]
MatchCriteria = List[NameString]


class Connection(TypedDict, total=False):
    """Defines a connection to a data source."""

    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    ConnectionType: Optional[ConnectionType]
    MatchCriteria: Optional[MatchCriteria]
    ConnectionProperties: Optional[ConnectionProperties]
    SparkProperties: Optional[PropertyMap]
    AthenaProperties: Optional[PropertyMap]
    PythonProperties: Optional[PropertyMap]
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirements]
    CreationTime: Optional[Timestamp]
    LastUpdatedTime: Optional[Timestamp]
    LastUpdatedBy: Optional[NameString]
    Status: Optional[ConnectionStatus]
    StatusReason: Optional[LongValueString]
    LastConnectionValidationTime: Optional[Timestamp]
    AuthenticationConfiguration: Optional[AuthenticationConfiguration]
    ConnectionSchemaVersion: Optional[ConnectionSchemaVersion]
    CompatibleComputeEnvironments: Optional[ComputeEnvironmentList]


class ConnectionInput(TypedDict, total=False):
    """A structure that is used to specify a connection to create or update."""

    Name: NameString
    Description: Optional[DescriptionString]
    ConnectionType: ConnectionType
    MatchCriteria: Optional[MatchCriteria]
    ConnectionProperties: ConnectionProperties
    SparkProperties: Optional[PropertyMap]
    AthenaProperties: Optional[PropertyMap]
    PythonProperties: Optional[PropertyMap]
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirements]
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInput]
    ValidateCredentials: Optional[Boolean]
    ValidateForComputeEnvironments: Optional[ComputeEnvironmentList]


ConnectionList = List[Connection]
ConnectionOptions = Dict[OptionKey, OptionValue]


class ConnectionPasswordEncryption(TypedDict, total=False):
    """The data structure used by the Data Catalog to encrypt the password as
    part of ``CreateConnection`` or ``UpdateConnection`` and store it in the
    ``ENCRYPTED_PASSWORD`` field in the connection properties. You can
    enable catalog encryption or only password encryption.

    When a ``CreationConnection`` request arrives containing a password, the
    Data Catalog first encrypts the password using your KMS key. It then
    encrypts the whole connection object again if catalog encryption is also
    enabled.

    This encryption requires that you set KMS key permissions to enable or
    restrict access on the password key according to your security
    requirements. For example, you might want only administrators to have
    decrypt permission on the password key.
    """

    ReturnConnectionPasswordEncrypted: Boolean
    AwsKmsKeyId: Optional[NameString]


class ConnectionTypeVariant(TypedDict, total=False):
    """Represents a variant of a connection type in Glue Data Catalog.
    Connection type variants provide specific configurations and behaviors
    for different implementations of the same general connection type.
    """

    ConnectionTypeVariantName: Optional[DisplayName]
    DisplayName: Optional[DisplayName]
    Description: Optional[Description]
    LogoUrl: Optional[UrlString]


ConnectionTypeVariantList = List[ConnectionTypeVariant]


class ConnectionTypeBrief(TypedDict, total=False):
    """Brief information about a supported connection type returned by the
    ``ListConnectionTypes`` API.
    """

    ConnectionType: Optional[ConnectionType]
    DisplayName: Optional[DisplayName]
    Vendor: Optional[Vendor]
    Description: Optional[Description]
    Categories: Optional[ListOfString]
    Capabilities: Optional[Capabilities]
    LogoUrl: Optional[UrlString]
    ConnectionTypeVariants: Optional[ConnectionTypeVariantList]


ConnectionTypeList = List[ConnectionTypeBrief]


class CrawlerHistory(TypedDict, total=False):
    """Contains the information for a run of a crawler."""

    CrawlId: Optional[CrawlId]
    State: Optional[CrawlerHistoryState]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    Summary: Optional[NameString]
    ErrorMessage: Optional[DescriptionString]
    LogGroup: Optional[LogGroup]
    LogStream: Optional[LogStream]
    MessagePrefix: Optional[MessagePrefix]
    DPUHour: Optional[NonNegativeDouble]


CrawlerHistoryList = List[CrawlerHistory]


class CrawlerMetrics(TypedDict, total=False):
    """Metrics for a specified crawler."""

    CrawlerName: Optional[NameString]
    TimeLeftSeconds: Optional[NonNegativeDouble]
    StillEstimating: Optional[Boolean]
    LastRuntimeSeconds: Optional[NonNegativeDouble]
    MedianRuntimeSeconds: Optional[NonNegativeDouble]
    TablesCreated: Optional[NonNegativeInteger]
    TablesUpdated: Optional[NonNegativeInteger]
    TablesDeleted: Optional[NonNegativeInteger]


CrawlerMetricsList = List[CrawlerMetrics]


class CrawlsFilter(TypedDict, total=False):
    """A list of fields, comparators and value that you can use to filter the
    crawler runs for a specified crawler.
    """

    FieldName: Optional[FieldName]
    FilterOperator: Optional[FilterOperator]
    FieldValue: Optional[GenericString]


CrawlsFilterList = List[CrawlsFilter]
TagsMap = Dict[TagKey, TagValue]


class CreateBlueprintRequest(ServiceRequest):
    Name: OrchestrationNameString
    Description: Optional[Generic512CharString]
    BlueprintLocation: OrchestrationS3Location
    Tags: Optional[TagsMap]


class CreateBlueprintResponse(TypedDict, total=False):
    Name: Optional[NameString]


class CreateCatalogRequest(ServiceRequest):
    Name: CatalogNameString
    CatalogInput: CatalogInput
    Tags: Optional[TagsMap]


class CreateCatalogResponse(TypedDict, total=False):
    pass


class CreateCsvClassifierRequest(TypedDict, total=False):
    """Specifies a custom CSV classifier for ``CreateClassifier`` to create."""

    Name: NameString
    Delimiter: Optional[CsvColumnDelimiter]
    QuoteSymbol: Optional[CsvQuoteSymbol]
    ContainsHeader: Optional[CsvHeaderOption]
    Header: Optional[CsvHeader]
    DisableValueTrimming: Optional[NullableBoolean]
    AllowSingleColumn: Optional[NullableBoolean]
    CustomDatatypeConfigured: Optional[NullableBoolean]
    CustomDatatypes: Optional[CustomDatatypes]
    Serde: Optional[CsvSerdeOption]


class CreateJsonClassifierRequest(TypedDict, total=False):
    """Specifies a JSON classifier for ``CreateClassifier`` to create."""

    Name: NameString
    JsonPath: JsonPath


class CreateXMLClassifierRequest(TypedDict, total=False):
    """Specifies an XML classifier for ``CreateClassifier`` to create."""

    Classification: Classification
    Name: NameString
    RowTag: Optional[RowTag]


class CreateGrokClassifierRequest(TypedDict, total=False):
    """Specifies a ``grok`` classifier for ``CreateClassifier`` to create."""

    Classification: Classification
    Name: NameString
    GrokPattern: GrokPattern
    CustomPatterns: Optional[CustomPatterns]


class CreateClassifierRequest(ServiceRequest):
    GrokClassifier: Optional[CreateGrokClassifierRequest]
    XMLClassifier: Optional[CreateXMLClassifierRequest]
    JsonClassifier: Optional[CreateJsonClassifierRequest]
    CsvClassifier: Optional[CreateCsvClassifierRequest]


class CreateClassifierResponse(TypedDict, total=False):
    pass


class CreateColumnStatisticsTaskSettingsRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString
    Role: NameString
    Schedule: Optional[CronExpression]
    ColumnNameList: Optional[ColumnNameList]
    SampleSize: Optional[SampleSizePercentage]
    CatalogID: Optional[NameString]
    SecurityConfiguration: Optional[NameString]
    Tags: Optional[TagsMap]


class CreateColumnStatisticsTaskSettingsResponse(TypedDict, total=False):
    pass


class CreateConnectionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    ConnectionInput: ConnectionInput
    Tags: Optional[TagsMap]


class CreateConnectionResponse(TypedDict, total=False):
    CreateConnectionStatus: Optional[ConnectionStatus]


class CreateCrawlerRequest(ServiceRequest):
    Name: NameString
    Role: Role
    DatabaseName: Optional[DatabaseName]
    Description: Optional[DescriptionString]
    Targets: CrawlerTargets
    Schedule: Optional[CronExpression]
    Classifiers: Optional[ClassifierNameList]
    TablePrefix: Optional[TablePrefix]
    SchemaChangePolicy: Optional[SchemaChangePolicy]
    RecrawlPolicy: Optional[RecrawlPolicy]
    LineageConfiguration: Optional[LineageConfiguration]
    LakeFormationConfiguration: Optional[LakeFormationConfiguration]
    Configuration: Optional[CrawlerConfiguration]
    CrawlerSecurityConfiguration: Optional[CrawlerSecurityConfiguration]
    Tags: Optional[TagsMap]


class CreateCrawlerResponse(TypedDict, total=False):
    pass


class CreateCustomEntityTypeRequest(ServiceRequest):
    Name: NameString
    RegexString: NameString
    ContextWords: Optional[ContextWords]
    Tags: Optional[TagsMap]


class CreateCustomEntityTypeResponse(TypedDict, total=False):
    Name: Optional[NameString]


class DataQualityTargetTable(TypedDict, total=False):
    """An object representing an Glue table."""

    TableName: NameString
    DatabaseName: NameString
    CatalogId: Optional[NameString]


class CreateDataQualityRulesetRequest(ServiceRequest):
    Name: NameString
    Description: Optional[DescriptionString]
    Ruleset: DataQualityRulesetString
    Tags: Optional[TagsMap]
    TargetTable: Optional[DataQualityTargetTable]
    DataQualitySecurityConfiguration: Optional[NameString]
    ClientToken: Optional[HashString]


class CreateDataQualityRulesetResponse(TypedDict, total=False):
    Name: Optional[NameString]


class FederatedDatabase(TypedDict, total=False):
    """A database that points to an entity outside the Glue Data Catalog."""

    Identifier: Optional[FederationIdentifier]
    ConnectionName: Optional[NameString]


class DatabaseIdentifier(TypedDict, total=False):
    """A structure that describes a target database for resource linking."""

    CatalogId: Optional[CatalogIdString]
    DatabaseName: Optional[NameString]
    Region: Optional[NameString]


class DatabaseInput(TypedDict, total=False):
    """The structure used to create or update a database."""

    Name: NameString
    Description: Optional[DescriptionString]
    LocationUri: Optional[URI]
    Parameters: Optional[ParametersMap]
    CreateTableDefaultPermissions: Optional[PrincipalPermissionsList]
    TargetDatabase: Optional[DatabaseIdentifier]
    FederatedDatabase: Optional[FederatedDatabase]


class CreateDatabaseRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseInput: DatabaseInput
    Tags: Optional[TagsMap]


class CreateDatabaseResponse(TypedDict, total=False):
    pass


class CreateDevEndpointRequest(ServiceRequest):
    EndpointName: GenericString
    RoleArn: RoleArn
    SecurityGroupIds: Optional[StringList]
    SubnetId: Optional[GenericString]
    PublicKey: Optional[GenericString]
    PublicKeys: Optional[PublicKeysList]
    NumberOfNodes: Optional[IntegerValue]
    WorkerType: Optional[WorkerType]
    GlueVersion: Optional[GlueVersionString]
    NumberOfWorkers: Optional[NullableInteger]
    ExtraPythonLibsS3Path: Optional[GenericString]
    ExtraJarsS3Path: Optional[GenericString]
    SecurityConfiguration: Optional[NameString]
    Tags: Optional[TagsMap]
    Arguments: Optional[MapValue]


class CreateDevEndpointResponse(TypedDict, total=False):
    EndpointName: Optional[GenericString]
    Status: Optional[GenericString]
    SecurityGroupIds: Optional[StringList]
    SubnetId: Optional[GenericString]
    RoleArn: Optional[RoleArn]
    YarnEndpointAddress: Optional[GenericString]
    ZeppelinRemoteSparkInterpreterPort: Optional[IntegerValue]
    NumberOfNodes: Optional[IntegerValue]
    WorkerType: Optional[WorkerType]
    GlueVersion: Optional[GlueVersionString]
    NumberOfWorkers: Optional[NullableInteger]
    AvailabilityZone: Optional[GenericString]
    VpcId: Optional[GenericString]
    ExtraPythonLibsS3Path: Optional[GenericString]
    ExtraJarsS3Path: Optional[GenericString]
    FailureReason: Optional[GenericString]
    SecurityConfiguration: Optional[NameString]
    CreatedTimestamp: Optional[TimestampValue]
    Arguments: Optional[MapValue]


class IntegrationConfig(TypedDict, total=False):
    """Properties associated with the integration."""

    RefreshInterval: Optional[String128]


class Tag(TypedDict, total=False):
    """The ``Tag`` object represents a label that you can assign to an Amazon
    Web Services resource. Each tag consists of a key and an optional value,
    both of which you define.

    For more information about tags, and controlling access to resources in
    Glue, see `Amazon Web Services Tags in
    Glue <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__
    and `Specifying Glue Resource
    ARNs <https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html>`__
    in the developer guide.
    """

    key: Optional[TagKey]
    value: Optional[TagValue]


IntegrationTagsList = List[Tag]
IntegrationAdditionalEncryptionContextMap = Dict[IntegrationString, IntegrationString]


class CreateIntegrationRequest(ServiceRequest):
    IntegrationName: String128
    SourceArn: String128
    TargetArn: String128
    Description: Optional[IntegrationDescription]
    DataFilter: Optional[String2048]
    KmsKeyId: Optional[String2048]
    AdditionalEncryptionContext: Optional[IntegrationAdditionalEncryptionContextMap]
    Tags: Optional[IntegrationTagsList]
    IntegrationConfig: Optional[IntegrationConfig]


class TargetProcessingProperties(TypedDict, total=False):
    """The resource properties associated with the integration target."""

    RoleArn: Optional[String128]
    KmsArn: Optional[String2048]
    ConnectionName: Optional[String128]
    EventBusArn: Optional[String2048]


class SourceProcessingProperties(TypedDict, total=False):
    """The resource properties associated with the integration source."""

    RoleArn: Optional[String128]


class CreateIntegrationResourcePropertyRequest(ServiceRequest):
    ResourceArn: String128
    SourceProcessingProperties: Optional[SourceProcessingProperties]
    TargetProcessingProperties: Optional[TargetProcessingProperties]


class CreateIntegrationResourcePropertyResponse(TypedDict, total=False):
    ResourceArn: String128
    SourceProcessingProperties: Optional[SourceProcessingProperties]
    TargetProcessingProperties: Optional[TargetProcessingProperties]


class IntegrationError(TypedDict, total=False):
    """An error associated with a zero-ETL integration."""

    ErrorCode: Optional[String128]
    ErrorMessage: Optional[String2048]


IntegrationErrorList = List[IntegrationError]
IntegrationTimestamp = datetime


class CreateIntegrationResponse(TypedDict, total=False):
    SourceArn: String128
    TargetArn: String128
    IntegrationName: String128
    Description: Optional[IntegrationDescription]
    IntegrationArn: String128
    KmsKeyId: Optional[String2048]
    AdditionalEncryptionContext: Optional[IntegrationAdditionalEncryptionContextMap]
    Tags: Optional[IntegrationTagsList]
    Status: IntegrationStatus
    CreateTime: IntegrationTimestamp
    Errors: Optional[IntegrationErrorList]
    DataFilter: Optional[String2048]
    IntegrationConfig: Optional[IntegrationConfig]


class IntegrationPartition(TypedDict, total=False):
    """A structure that describes how data is partitioned on the target."""

    FieldName: Optional[String128]
    FunctionSpec: Optional[String128]
    ConversionSpec: Optional[String128]


IntegrationPartitionSpecList = List[IntegrationPartition]


class TargetTableConfig(TypedDict, total=False):
    """Properties used by the target leg to partition the data on the target."""

    UnnestSpec: Optional[UnnestSpec]
    PartitionSpec: Optional[IntegrationPartitionSpecList]
    TargetTableName: Optional[String128]


PrimaryKeyList = List[String128]
SourceTableFieldsList = List[String128]


class SourceTableConfig(TypedDict, total=False):
    """Properties used by the source leg to process data from the source."""

    Fields: Optional[SourceTableFieldsList]
    FilterPredicate: Optional[String128]
    PrimaryKey: Optional[PrimaryKeyList]
    RecordUpdateField: Optional[String128]


class CreateIntegrationTablePropertiesRequest(ServiceRequest):
    ResourceArn: String128
    TableName: String128
    SourceTableConfig: Optional[SourceTableConfig]
    TargetTableConfig: Optional[TargetTableConfig]


class CreateIntegrationTablePropertiesResponse(TypedDict, total=False):
    pass


class CreateJobRequest(ServiceRequest):
    Name: NameString
    JobMode: Optional[JobMode]
    JobRunQueuingEnabled: Optional[NullableBoolean]
    Description: Optional[DescriptionString]
    LogUri: Optional[UriString]
    Role: RoleString
    ExecutionProperty: Optional[ExecutionProperty]
    Command: JobCommand
    DefaultArguments: Optional[GenericMap]
    NonOverridableArguments: Optional[GenericMap]
    Connections: Optional[ConnectionsList]
    MaxRetries: Optional[MaxRetries]
    AllocatedCapacity: Optional[IntegerValue]
    Timeout: Optional[Timeout]
    MaxCapacity: Optional[NullableDouble]
    SecurityConfiguration: Optional[NameString]
    Tags: Optional[TagsMap]
    NotificationProperty: Optional[NotificationProperty]
    GlueVersion: Optional[GlueVersionString]
    NumberOfWorkers: Optional[NullableInteger]
    WorkerType: Optional[WorkerType]
    CodeGenConfigurationNodes: Optional[CodeGenConfigurationNodes]
    ExecutionClass: Optional[ExecutionClass]
    SourceControlDetails: Optional[SourceControlDetails]
    MaintenanceWindow: Optional[MaintenanceWindow]


class CreateJobResponse(TypedDict, total=False):
    Name: Optional[NameString]


class MLUserDataEncryption(TypedDict, total=False):
    """The encryption-at-rest settings of the transform that apply to accessing
    user data.
    """

    MlUserDataEncryptionMode: MLUserDataEncryptionModeString
    KmsKeyId: Optional[NameString]


class TransformEncryption(TypedDict, total=False):
    """The encryption-at-rest settings of the transform that apply to accessing
    user data. Machine learning transforms can access user data encrypted in
    Amazon S3 using KMS.

    Additionally, imported labels and trained transforms can now be
    encrypted using a customer provided KMS key.
    """

    MlUserDataEncryption: Optional[MLUserDataEncryption]
    TaskRunSecurityConfigurationName: Optional[NameString]


class FindMatchesParameters(TypedDict, total=False):
    """The parameters to configure the find matches transform."""

    PrimaryKeyColumnName: Optional[ColumnNameString]
    PrecisionRecallTradeoff: Optional[GenericBoundedDouble]
    AccuracyCostTradeoff: Optional[GenericBoundedDouble]
    EnforceProvidedLabels: Optional[NullableBoolean]


class TransformParameters(TypedDict, total=False):
    """The algorithm-specific parameters that are associated with the machine
    learning transform.
    """

    TransformType: TransformType
    FindMatchesParameters: Optional[FindMatchesParameters]


GlueTables = List[GlueTable]


class CreateMLTransformRequest(ServiceRequest):
    Name: NameString
    Description: Optional[DescriptionString]
    InputRecordTables: GlueTables
    Parameters: TransformParameters
    Role: RoleString
    GlueVersion: Optional[GlueVersionString]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    MaxRetries: Optional[NullableInteger]
    Tags: Optional[TagsMap]
    TransformEncryption: Optional[TransformEncryption]


class CreateMLTransformResponse(TypedDict, total=False):
    TransformId: Optional[HashString]


KeyList = List[NameString]


class PartitionIndex(TypedDict, total=False):
    """A structure for a partition index."""

    Keys: KeyList
    IndexName: NameString


class CreatePartitionIndexRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionIndex: PartitionIndex


class CreatePartitionIndexResponse(TypedDict, total=False):
    pass


class CreatePartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionInput: PartitionInput


class CreatePartitionResponse(TypedDict, total=False):
    pass


class CreateRegistryInput(ServiceRequest):
    RegistryName: SchemaRegistryNameString
    Description: Optional[DescriptionString]
    Tags: Optional[TagsMap]


class CreateRegistryResponse(TypedDict, total=False):
    RegistryArn: Optional[GlueResourceArn]
    RegistryName: Optional[SchemaRegistryNameString]
    Description: Optional[DescriptionString]
    Tags: Optional[TagsMap]


class RegistryId(TypedDict, total=False):
    """A wrapper structure that may contain the registry name and Amazon
    Resource Name (ARN).
    """

    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]


class CreateSchemaInput(ServiceRequest):
    RegistryId: Optional[RegistryId]
    SchemaName: SchemaRegistryNameString
    DataFormat: DataFormat
    Compatibility: Optional[Compatibility]
    Description: Optional[DescriptionString]
    Tags: Optional[TagsMap]
    SchemaDefinition: Optional[SchemaDefinitionString]


SchemaCheckpointNumber = int


class CreateSchemaResponse(TypedDict, total=False):
    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    SchemaArn: Optional[GlueResourceArn]
    Description: Optional[DescriptionString]
    DataFormat: Optional[DataFormat]
    Compatibility: Optional[Compatibility]
    SchemaCheckpoint: Optional[SchemaCheckpointNumber]
    LatestSchemaVersion: Optional[VersionLongNumber]
    NextSchemaVersion: Optional[VersionLongNumber]
    SchemaStatus: Optional[SchemaStatus]
    Tags: Optional[TagsMap]
    SchemaVersionId: Optional[SchemaVersionIdString]
    SchemaVersionStatus: Optional[SchemaVersionStatus]


DagEdges = List[CodeGenEdge]
DagNodes = List[CodeGenNode]


class CreateScriptRequest(ServiceRequest):
    DagNodes: Optional[DagNodes]
    DagEdges: Optional[DagEdges]
    Language: Optional[Language]


class CreateScriptResponse(TypedDict, total=False):
    PythonScript: Optional[PythonScript]
    ScalaCode: Optional[ScalaCode]


class DataQualityEncryption(TypedDict, total=False):
    """Specifies how Data Quality assets in your account should be encrypted."""

    DataQualityEncryptionMode: Optional[DataQualityEncryptionMode]
    KmsKeyArn: Optional[KmsKeyArn]


class JobBookmarksEncryption(TypedDict, total=False):
    """Specifies how job bookmark data should be encrypted."""

    JobBookmarksEncryptionMode: Optional[JobBookmarksEncryptionMode]
    KmsKeyArn: Optional[KmsKeyArn]


class S3Encryption(TypedDict, total=False):
    """Specifies how Amazon Simple Storage Service (Amazon S3) data should be
    encrypted.
    """

    S3EncryptionMode: Optional[S3EncryptionMode]
    KmsKeyArn: Optional[KmsKeyArn]


S3EncryptionList = List[S3Encryption]


class EncryptionConfiguration(TypedDict, total=False):
    """Specifies an encryption configuration."""

    S3Encryption: Optional[S3EncryptionList]
    CloudWatchEncryption: Optional[CloudWatchEncryption]
    JobBookmarksEncryption: Optional[JobBookmarksEncryption]
    DataQualityEncryption: Optional[DataQualityEncryption]


class CreateSecurityConfigurationRequest(ServiceRequest):
    Name: NameString
    EncryptionConfiguration: EncryptionConfiguration


class CreateSecurityConfigurationResponse(TypedDict, total=False):
    Name: Optional[NameString]
    CreatedTimestamp: Optional[TimestampValue]


OrchestrationArgumentsMap = Dict[OrchestrationNameString, OrchestrationArgumentsValue]


class SessionCommand(TypedDict, total=False):
    """The ``SessionCommand`` that runs the job."""

    Name: Optional[NameString]
    PythonVersion: Optional[PythonVersionString]


class CreateSessionRequest(ServiceRequest):
    """Request to create a new session."""

    Id: NameString
    Description: Optional[DescriptionString]
    Role: OrchestrationRoleArn
    Command: SessionCommand
    Timeout: Optional[Timeout]
    IdleTimeout: Optional[Timeout]
    DefaultArguments: Optional[OrchestrationArgumentsMap]
    Connections: Optional[ConnectionsList]
    MaxCapacity: Optional[NullableDouble]
    NumberOfWorkers: Optional[NullableInteger]
    WorkerType: Optional[WorkerType]
    SecurityConfiguration: Optional[NameString]
    GlueVersion: Optional[GlueVersionString]
    Tags: Optional[TagsMap]
    RequestOrigin: Optional[OrchestrationNameString]


class Session(TypedDict, total=False):
    """The period in which a remote Spark runtime environment is running."""

    Id: Optional[NameString]
    CreatedOn: Optional[TimestampValue]
    Status: Optional[SessionStatus]
    ErrorMessage: Optional[DescriptionString]
    Description: Optional[DescriptionString]
    Role: Optional[OrchestrationRoleArn]
    Command: Optional[SessionCommand]
    DefaultArguments: Optional[OrchestrationArgumentsMap]
    Connections: Optional[ConnectionsList]
    Progress: Optional[DoubleValue]
    MaxCapacity: Optional[NullableDouble]
    SecurityConfiguration: Optional[NameString]
    GlueVersion: Optional[GlueVersionString]
    NumberOfWorkers: Optional[NullableInteger]
    WorkerType: Optional[WorkerType]
    CompletedOn: Optional[TimestampValue]
    ExecutionTime: Optional[NullableDouble]
    DPUSeconds: Optional[NullableDouble]
    IdleTimeout: Optional[IdleTimeout]
    ProfileName: Optional[NameString]


class CreateSessionResponse(TypedDict, total=False):
    Session: Optional[Session]


class CreateTableOptimizerRequest(ServiceRequest):
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    Type: TableOptimizerType
    TableOptimizerConfiguration: TableOptimizerConfiguration


class CreateTableOptimizerResponse(TypedDict, total=False):
    pass


class IcebergInput(TypedDict, total=False):
    """A structure that defines an Apache Iceberg metadata table to create in
    the catalog.
    """

    MetadataOperation: MetadataOperation
    Version: Optional[VersionString]


class OpenTableFormatInput(TypedDict, total=False):
    """A structure representing an open format table."""

    IcebergInput: Optional[IcebergInput]


PartitionIndexList = List[PartitionIndex]
ViewSubObjectsList = List[ArnString]


class ViewRepresentationInput(TypedDict, total=False):
    """A structure containing details of a representation to update or create a
    Lake Formation view.
    """

    Dialect: Optional[ViewDialect]
    DialectVersion: Optional[ViewDialectVersionString]
    ViewOriginalText: Optional[ViewTextString]
    ValidationConnection: Optional[NameString]
    ViewExpandedText: Optional[ViewTextString]


ViewRepresentationInputList = List[ViewRepresentationInput]


class ViewDefinitionInput(TypedDict, total=False):
    """A structure containing details for creating or updating an Glue view."""

    IsProtected: Optional[NullableBoolean]
    Definer: Optional[ArnString]
    Representations: Optional[ViewRepresentationInputList]
    SubObjects: Optional[ViewSubObjectsList]


class TableIdentifier(TypedDict, total=False):
    """A structure that describes a target table for resource linking."""

    CatalogId: Optional[CatalogIdString]
    DatabaseName: Optional[NameString]
    Name: Optional[NameString]
    Region: Optional[NameString]


class TableInput(TypedDict, total=False):
    """A structure used to define a table."""

    Name: NameString
    Description: Optional[DescriptionString]
    Owner: Optional[NameString]
    LastAccessTime: Optional[Timestamp]
    LastAnalyzedTime: Optional[Timestamp]
    Retention: Optional[NonNegativeInteger]
    StorageDescriptor: Optional[StorageDescriptor]
    PartitionKeys: Optional[ColumnList]
    ViewOriginalText: Optional[ViewTextString]
    ViewExpandedText: Optional[ViewTextString]
    TableType: Optional[TableTypeString]
    Parameters: Optional[ParametersMap]
    TargetTable: Optional[TableIdentifier]
    ViewDefinition: Optional[ViewDefinitionInput]


class CreateTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableInput: TableInput
    PartitionIndexes: Optional[PartitionIndexList]
    TransactionId: Optional[TransactionIdString]
    OpenTableFormatInput: Optional[OpenTableFormatInput]


class CreateTableResponse(TypedDict, total=False):
    pass


class CreateTriggerRequest(ServiceRequest):
    Name: NameString
    WorkflowName: Optional[NameString]
    Type: TriggerType
    Schedule: Optional[GenericString]
    Predicate: Optional[Predicate]
    Actions: ActionList
    Description: Optional[DescriptionString]
    StartOnCreation: Optional[BooleanValue]
    Tags: Optional[TagsMap]
    EventBatchingCondition: Optional[EventBatchingCondition]


class CreateTriggerResponse(TypedDict, total=False):
    Name: Optional[NameString]


class ProfileConfiguration(TypedDict, total=False):
    """Specifies the job and session values that an admin configures in an Glue
    usage profile.
    """

    SessionConfiguration: Optional[ConfigurationMap]
    JobConfiguration: Optional[ConfigurationMap]


class CreateUsageProfileRequest(ServiceRequest):
    Name: NameString
    Description: Optional[DescriptionString]
    Configuration: ProfileConfiguration
    Tags: Optional[TagsMap]


class CreateUsageProfileResponse(TypedDict, total=False):
    Name: Optional[NameString]


class ResourceUri(TypedDict, total=False):
    """The URIs for function resources."""

    ResourceType: Optional[ResourceType]
    Uri: Optional[URI]


ResourceUriList = List[ResourceUri]


class UserDefinedFunctionInput(TypedDict, total=False):
    """A structure used to create or update a user-defined function."""

    FunctionName: Optional[NameString]
    ClassName: Optional[NameString]
    OwnerName: Optional[NameString]
    OwnerType: Optional[PrincipalType]
    ResourceUris: Optional[ResourceUriList]


class CreateUserDefinedFunctionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    FunctionInput: UserDefinedFunctionInput


class CreateUserDefinedFunctionResponse(TypedDict, total=False):
    pass


class CreateWorkflowRequest(ServiceRequest):
    Name: NameString
    Description: Optional[WorkflowDescriptionString]
    DefaultRunProperties: Optional[WorkflowRunProperties]
    Tags: Optional[TagsMap]
    MaxConcurrentRuns: Optional[NullableInteger]


class CreateWorkflowResponse(TypedDict, total=False):
    Name: Optional[NameString]


CustomProperties = Dict[String, String]


class EncryptionAtRest(TypedDict, total=False):
    """Specifies the encryption-at-rest configuration for the Data Catalog."""

    CatalogEncryptionMode: CatalogEncryptionMode
    SseAwsKmsKeyId: Optional[NameString]
    CatalogEncryptionServiceRole: Optional[IAMRoleArn]


class DataCatalogEncryptionSettings(TypedDict, total=False):
    """Contains configuration information for maintaining Data Catalog
    security.
    """

    EncryptionAtRest: Optional[EncryptionAtRest]
    ConnectionPasswordEncryption: Optional[ConnectionPasswordEncryption]


class DataQualityEvaluationRunAdditionalRunOptions(TypedDict, total=False):
    """Additional run options you can specify for an evaluation run."""

    CloudWatchMetricsEnabled: Optional[NullableBoolean]
    ResultsS3Prefix: Optional[UriString]
    CompositeRuleEvaluationMethod: Optional[DQCompositeRuleEvaluationMethod]


class DataQualityResultDescription(TypedDict, total=False):
    """Describes a data quality result."""

    ResultId: Optional[HashString]
    DataSource: Optional[DataSource]
    JobName: Optional[NameString]
    JobRunId: Optional[HashString]
    StartedOn: Optional[Timestamp]


DataQualityResultDescriptionList = List[DataQualityResultDescription]


class DataQualityResultFilterCriteria(TypedDict, total=False):
    """Criteria used to return data quality results."""

    DataSource: Optional[DataSource]
    JobName: Optional[NameString]
    JobRunId: Optional[HashString]
    StartedAfter: Optional[Timestamp]
    StartedBefore: Optional[Timestamp]


DataQualityResultIdList = List[HashString]


class DataQualityRuleRecommendationRunDescription(TypedDict, total=False):
    """Describes the result of a data quality rule recommendation run."""

    RunId: Optional[HashString]
    Status: Optional[TaskStatusType]
    StartedOn: Optional[Timestamp]
    DataSource: Optional[DataSource]


class DataQualityRuleRecommendationRunFilter(TypedDict, total=False):
    """A filter for listing data quality recommendation runs."""

    DataSource: DataSource
    StartedBefore: Optional[Timestamp]
    StartedAfter: Optional[Timestamp]


DataQualityRuleRecommendationRunList = List[DataQualityRuleRecommendationRunDescription]


class DataQualityRulesetEvaluationRunDescription(TypedDict, total=False):
    """Describes the result of a data quality ruleset evaluation run."""

    RunId: Optional[HashString]
    Status: Optional[TaskStatusType]
    StartedOn: Optional[Timestamp]
    DataSource: Optional[DataSource]


class DataQualityRulesetEvaluationRunFilter(TypedDict, total=False):
    """The filter criteria."""

    DataSource: DataSource
    StartedBefore: Optional[Timestamp]
    StartedAfter: Optional[Timestamp]


DataQualityRulesetEvaluationRunList = List[DataQualityRulesetEvaluationRunDescription]


class DataQualityRulesetFilterCriteria(TypedDict, total=False):
    """The criteria used to filter data quality rulesets."""

    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    CreatedBefore: Optional[Timestamp]
    CreatedAfter: Optional[Timestamp]
    LastModifiedBefore: Optional[Timestamp]
    LastModifiedAfter: Optional[Timestamp]
    TargetTable: Optional[DataQualityTargetTable]


class DataQualityRulesetListDetails(TypedDict, total=False):
    """Describes a data quality ruleset returned by ``GetDataQualityRuleset``."""

    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    CreatedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    TargetTable: Optional[DataQualityTargetTable]
    RecommendationRunId: Optional[HashString]
    RuleCount: Optional[NullableInteger]


DataQualityRulesetList = List[DataQualityRulesetListDetails]
DataSourceMap = Dict[NameString, DataSource]


class Database(TypedDict, total=False):
    """The ``Database`` object represents a logical grouping of tables that
    might reside in a Hive metastore or an RDBMS.
    """

    Name: NameString
    Description: Optional[DescriptionString]
    LocationUri: Optional[URI]
    Parameters: Optional[ParametersMap]
    CreateTime: Optional[Timestamp]
    CreateTableDefaultPermissions: Optional[PrincipalPermissionsList]
    TargetDatabase: Optional[DatabaseIdentifier]
    CatalogId: Optional[CatalogIdString]
    FederatedDatabase: Optional[FederatedDatabase]


DatabaseAttributesList = List[DatabaseAttributes]
DatabaseList = List[Database]


class DeleteBlueprintRequest(ServiceRequest):
    Name: NameString


class DeleteBlueprintResponse(TypedDict, total=False):
    Name: Optional[NameString]


class DeleteCatalogRequest(ServiceRequest):
    CatalogId: CatalogIdString


class DeleteCatalogResponse(TypedDict, total=False):
    pass


class DeleteClassifierRequest(ServiceRequest):
    Name: NameString


class DeleteClassifierResponse(TypedDict, total=False):
    pass


class DeleteColumnStatisticsForPartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionValues: ValueStringList
    ColumnName: NameString


class DeleteColumnStatisticsForPartitionResponse(TypedDict, total=False):
    pass


class DeleteColumnStatisticsForTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    ColumnName: NameString


class DeleteColumnStatisticsForTableResponse(TypedDict, total=False):
    pass


class DeleteColumnStatisticsTaskSettingsRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString


class DeleteColumnStatisticsTaskSettingsResponse(TypedDict, total=False):
    pass


class DeleteConnectionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    ConnectionName: NameString


class DeleteConnectionResponse(TypedDict, total=False):
    pass


class DeleteCrawlerRequest(ServiceRequest):
    Name: NameString


class DeleteCrawlerResponse(TypedDict, total=False):
    pass


class DeleteCustomEntityTypeRequest(ServiceRequest):
    Name: NameString


class DeleteCustomEntityTypeResponse(TypedDict, total=False):
    Name: Optional[NameString]


class DeleteDataQualityRulesetRequest(ServiceRequest):
    Name: NameString


class DeleteDataQualityRulesetResponse(TypedDict, total=False):
    pass


class DeleteDatabaseRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    Name: NameString


class DeleteDatabaseResponse(TypedDict, total=False):
    pass


class DeleteDevEndpointRequest(ServiceRequest):
    EndpointName: GenericString


class DeleteDevEndpointResponse(TypedDict, total=False):
    pass


class DeleteIntegrationRequest(ServiceRequest):
    IntegrationIdentifier: String128


class DeleteIntegrationResponse(TypedDict, total=False):
    SourceArn: String128
    TargetArn: String128
    IntegrationName: String128
    Description: Optional[IntegrationDescription]
    IntegrationArn: String128
    KmsKeyId: Optional[String2048]
    AdditionalEncryptionContext: Optional[IntegrationAdditionalEncryptionContextMap]
    Tags: Optional[IntegrationTagsList]
    Status: IntegrationStatus
    CreateTime: IntegrationTimestamp
    Errors: Optional[IntegrationErrorList]
    DataFilter: Optional[String2048]


class DeleteIntegrationTablePropertiesRequest(ServiceRequest):
    ResourceArn: String128
    TableName: String128


class DeleteIntegrationTablePropertiesResponse(TypedDict, total=False):
    pass


class DeleteJobRequest(ServiceRequest):
    JobName: NameString


class DeleteJobResponse(TypedDict, total=False):
    JobName: Optional[NameString]


class DeleteMLTransformRequest(ServiceRequest):
    TransformId: HashString


class DeleteMLTransformResponse(TypedDict, total=False):
    TransformId: Optional[HashString]


class DeletePartitionIndexRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    IndexName: NameString


class DeletePartitionIndexResponse(TypedDict, total=False):
    pass


class DeletePartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionValues: ValueStringList


class DeletePartitionResponse(TypedDict, total=False):
    pass


class DeleteRegistryInput(ServiceRequest):
    RegistryId: RegistryId


class DeleteRegistryResponse(TypedDict, total=False):
    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]
    Status: Optional[RegistryStatus]


class DeleteResourcePolicyRequest(ServiceRequest):
    PolicyHashCondition: Optional[HashString]
    ResourceArn: Optional[GlueResourceArn]


class DeleteResourcePolicyResponse(TypedDict, total=False):
    pass


class DeleteSchemaInput(ServiceRequest):
    SchemaId: SchemaId


class DeleteSchemaResponse(TypedDict, total=False):
    SchemaArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    Status: Optional[SchemaStatus]


class DeleteSchemaVersionsInput(ServiceRequest):
    SchemaId: SchemaId
    Versions: VersionsString


class ErrorDetails(TypedDict, total=False):
    """An object containing error details."""

    ErrorCode: Optional[ErrorCodeString]
    ErrorMessage: Optional[ErrorMessageString]


class SchemaVersionErrorItem(TypedDict, total=False):
    """An object that contains the error details for an operation on a schema
    version.
    """

    VersionNumber: Optional[VersionLongNumber]
    ErrorDetails: Optional[ErrorDetails]


SchemaVersionErrorList = List[SchemaVersionErrorItem]


class DeleteSchemaVersionsResponse(TypedDict, total=False):
    SchemaVersionErrors: Optional[SchemaVersionErrorList]


class DeleteSecurityConfigurationRequest(ServiceRequest):
    Name: NameString


class DeleteSecurityConfigurationResponse(TypedDict, total=False):
    pass


class DeleteSessionRequest(ServiceRequest):
    Id: NameString
    RequestOrigin: Optional[OrchestrationNameString]


class DeleteSessionResponse(TypedDict, total=False):
    Id: Optional[NameString]


class DeleteTableOptimizerRequest(ServiceRequest):
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    Type: TableOptimizerType


class DeleteTableOptimizerResponse(TypedDict, total=False):
    pass


class DeleteTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    Name: NameString
    TransactionId: Optional[TransactionIdString]


class DeleteTableResponse(TypedDict, total=False):
    pass


class DeleteTableVersionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    VersionId: VersionString


class DeleteTableVersionResponse(TypedDict, total=False):
    pass


class DeleteTriggerRequest(ServiceRequest):
    Name: NameString


class DeleteTriggerResponse(TypedDict, total=False):
    Name: Optional[NameString]


class DeleteUsageProfileRequest(ServiceRequest):
    Name: NameString


class DeleteUsageProfileResponse(TypedDict, total=False):
    pass


class DeleteUserDefinedFunctionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    FunctionName: NameString


class DeleteUserDefinedFunctionResponse(TypedDict, total=False):
    pass


class DeleteWorkflowRequest(ServiceRequest):
    Name: NameString


class DeleteWorkflowResponse(TypedDict, total=False):
    Name: Optional[NameString]


class DescribeConnectionTypeRequest(ServiceRequest):
    ConnectionType: NameString


class DescribeConnectionTypeResponse(TypedDict, total=False):
    ConnectionType: Optional[NameString]
    Description: Optional[Description]
    Capabilities: Optional[Capabilities]
    ConnectionProperties: Optional[PropertiesMap]
    ConnectionOptions: Optional[PropertiesMap]
    AuthenticationConfiguration: Optional[AuthConfiguration]
    ComputeEnvironmentConfigurations: Optional[ComputeEnvironmentConfigurationMap]
    PhysicalConnectionRequirements: Optional[PropertiesMap]
    AthenaConnectionProperties: Optional[PropertiesMap]
    PythonConnectionProperties: Optional[PropertiesMap]
    SparkConnectionProperties: Optional[PropertiesMap]


class DescribeEntityRequest(ServiceRequest):
    ConnectionName: NameString
    CatalogId: Optional[CatalogIdString]
    EntityName: EntityName
    NextToken: Optional[NextToken]
    DataStoreApiVersion: Optional[ApiVersion]


FieldFilterOperatorsList = List[FieldFilterOperator]


class Field(TypedDict, total=False):
    """The ``Field`` object has information about the different properties
    associated with a field in the connector.
    """

    FieldName: Optional[EntityFieldName]
    Label: Optional[FieldLabel]
    Description: Optional[FieldDescription]
    FieldType: Optional[FieldDataType]
    IsPrimaryKey: Optional[Bool]
    IsNullable: Optional[Bool]
    IsRetrievable: Optional[Bool]
    IsFilterable: Optional[Bool]
    IsPartitionable: Optional[Bool]
    IsCreateable: Optional[Bool]
    IsUpdateable: Optional[Bool]
    IsUpsertable: Optional[Bool]
    IsDefaultOnCreate: Optional[Bool]
    SupportedValues: Optional[ListOfString]
    SupportedFilterOperators: Optional[FieldFilterOperatorsList]
    ParentField: Optional[String]
    NativeDataType: Optional[String]
    CustomProperties: Optional[CustomProperties]


FieldsList = List[Field]


class DescribeEntityResponse(TypedDict, total=False):
    Fields: Optional[FieldsList]
    NextToken: Optional[NextToken]


class DescribeInboundIntegrationsRequest(ServiceRequest):
    IntegrationArn: Optional[String128]
    Marker: Optional[String128]
    MaxRecords: Optional[IntegrationInteger]
    TargetArn: Optional[String128]


class InboundIntegration(TypedDict, total=False):
    """A structure for an integration that writes data into a resource."""

    SourceArn: String128
    TargetArn: String128
    IntegrationArn: String128
    Status: IntegrationStatus
    CreateTime: IntegrationTimestamp
    IntegrationConfig: Optional[IntegrationConfig]
    Errors: Optional[IntegrationErrorList]


InboundIntegrationsList = List[InboundIntegration]


class DescribeInboundIntegrationsResponse(TypedDict, total=False):
    InboundIntegrations: Optional[InboundIntegrationsList]
    Marker: Optional[String128]


IntegrationFilterValues = List[String128]


class IntegrationFilter(TypedDict, total=False):
    """A filter that can be used when invoking a ``DescribeIntegrations``
    request.
    """

    Name: Optional[String128]
    Values: Optional[IntegrationFilterValues]


IntegrationFilterList = List[IntegrationFilter]


class DescribeIntegrationsRequest(ServiceRequest):
    IntegrationIdentifier: Optional[String128]
    Marker: Optional[String128]
    MaxRecords: Optional[IntegrationInteger]
    Filters: Optional[IntegrationFilterList]


class Integration(TypedDict, total=False):
    """Describes a zero-ETL integration."""

    SourceArn: String128
    TargetArn: String128
    Description: Optional[IntegrationDescription]
    IntegrationName: String128
    IntegrationArn: String128
    KmsKeyId: Optional[String2048]
    AdditionalEncryptionContext: Optional[IntegrationAdditionalEncryptionContextMap]
    Tags: Optional[IntegrationTagsList]
    Status: IntegrationStatus
    CreateTime: IntegrationTimestamp
    IntegrationConfig: Optional[IntegrationConfig]
    Errors: Optional[IntegrationErrorList]
    DataFilter: Optional[String2048]


IntegrationsList = List[Integration]


class DescribeIntegrationsResponse(TypedDict, total=False):
    Integrations: Optional[IntegrationsList]
    Marker: Optional[String128]


class DevEndpointCustomLibraries(TypedDict, total=False):
    """Custom libraries to be loaded into a development endpoint."""

    ExtraPythonLibsS3Path: Optional[GenericString]
    ExtraJarsS3Path: Optional[GenericString]


DevEndpointNameList = List[NameString]


class Entity(TypedDict, total=False):
    """An entity supported by a given ``ConnectionType``."""

    EntityName: Optional[EntityName]
    Label: Optional[EntityLabel]
    IsParentEntity: Optional[IsParentEntity]
    Description: Optional[EntityDescription]
    Category: Optional[Category]
    CustomProperties: Optional[CustomProperties]


EntityList = List[Entity]


class FindMatchesMetrics(TypedDict, total=False):
    """The evaluation metrics for the find matches algorithm. The quality of
    your machine learning transform is measured by getting your transform to
    predict some matches and comparing the results to known matches from the
    same dataset. The quality metrics are based on a subset of your data, so
    they are not precise.
    """

    AreaUnderPRCurve: Optional[GenericBoundedDouble]
    Precision: Optional[GenericBoundedDouble]
    Recall: Optional[GenericBoundedDouble]
    F1: Optional[GenericBoundedDouble]
    ConfusionMatrix: Optional[ConfusionMatrix]
    ColumnImportances: Optional[ColumnImportanceList]


class EvaluationMetrics(TypedDict, total=False):
    """Evaluation metrics provide an estimate of the quality of your machine
    learning transform.
    """

    TransformType: TransformType
    FindMatchesMetrics: Optional[FindMatchesMetrics]


class ExportLabelsTaskRunProperties(TypedDict, total=False):
    """Specifies configuration properties for an exporting labels task run."""

    OutputS3Path: Optional[UriString]


class FederatedTable(TypedDict, total=False):
    """A table that points to an entity outside the Glue Data Catalog."""

    Identifier: Optional[FederationIdentifier]
    DatabaseIdentifier: Optional[FederationIdentifier]
    ConnectionName: Optional[NameString]


class FindMatchesTaskRunProperties(TypedDict, total=False):
    """Specifies configuration properties for a Find Matches task run."""

    JobId: Optional[HashString]
    JobName: Optional[NameString]
    JobRunId: Optional[HashString]


class GetBlueprintRequest(ServiceRequest):
    Name: NameString
    IncludeBlueprint: Optional[NullableBoolean]
    IncludeParameterSpec: Optional[NullableBoolean]


class GetBlueprintResponse(TypedDict, total=False):
    Blueprint: Optional[Blueprint]


class GetBlueprintRunRequest(ServiceRequest):
    BlueprintName: OrchestrationNameString
    RunId: IdString


class GetBlueprintRunResponse(TypedDict, total=False):
    BlueprintRun: Optional[BlueprintRun]


class GetBlueprintRunsRequest(ServiceRequest):
    BlueprintName: NameString
    NextToken: Optional[GenericString]
    MaxResults: Optional[PageSize]


class GetBlueprintRunsResponse(TypedDict, total=False):
    BlueprintRuns: Optional[BlueprintRuns]
    NextToken: Optional[GenericString]


class GetCatalogImportStatusRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]


class GetCatalogImportStatusResponse(TypedDict, total=False):
    ImportStatus: Optional[CatalogImportStatus]


class GetCatalogRequest(ServiceRequest):
    CatalogId: CatalogIdString


class GetCatalogResponse(TypedDict, total=False):
    Catalog: Optional[Catalog]


class GetCatalogsRequest(ServiceRequest):
    ParentCatalogId: Optional[CatalogIdString]
    NextToken: Optional[Token]
    MaxResults: Optional[PageSize]
    Recursive: Optional[Boolean]
    IncludeRoot: Optional[NullableBoolean]


class GetCatalogsResponse(TypedDict, total=False):
    CatalogList: CatalogList
    NextToken: Optional[Token]


class GetClassifierRequest(ServiceRequest):
    Name: NameString


class GetClassifierResponse(TypedDict, total=False):
    Classifier: Optional[Classifier]


class GetClassifiersRequest(ServiceRequest):
    MaxResults: Optional[PageSize]
    NextToken: Optional[Token]


class GetClassifiersResponse(TypedDict, total=False):
    Classifiers: Optional[ClassifierList]
    NextToken: Optional[Token]


GetColumnNamesList = List[NameString]


class GetColumnStatisticsForPartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionValues: ValueStringList
    ColumnNames: GetColumnNamesList


class GetColumnStatisticsForPartitionResponse(TypedDict, total=False):
    ColumnStatisticsList: Optional[ColumnStatisticsList]
    Errors: Optional[ColumnErrors]


class GetColumnStatisticsForTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    ColumnNames: GetColumnNamesList


class GetColumnStatisticsForTableResponse(TypedDict, total=False):
    ColumnStatisticsList: Optional[ColumnStatisticsList]
    Errors: Optional[ColumnErrors]


class GetColumnStatisticsTaskRunRequest(ServiceRequest):
    ColumnStatisticsTaskRunId: HashString


class GetColumnStatisticsTaskRunResponse(TypedDict, total=False):
    ColumnStatisticsTaskRun: Optional[ColumnStatisticsTaskRun]


class GetColumnStatisticsTaskRunsRequest(ServiceRequest):
    DatabaseName: DatabaseName
    TableName: NameString
    MaxResults: Optional[PageSize]
    NextToken: Optional[Token]


class GetColumnStatisticsTaskRunsResponse(TypedDict, total=False):
    ColumnStatisticsTaskRuns: Optional[ColumnStatisticsTaskRunsList]
    NextToken: Optional[Token]


class GetColumnStatisticsTaskSettingsRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString


class GetColumnStatisticsTaskSettingsResponse(TypedDict, total=False):
    ColumnStatisticsTaskSettings: Optional[ColumnStatisticsTaskSettings]


class GetConnectionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    Name: NameString
    HidePassword: Optional[Boolean]
    ApplyOverrideForComputeEnvironment: Optional[ComputeEnvironment]


class GetConnectionResponse(TypedDict, total=False):
    Connection: Optional[Connection]


class GetConnectionsFilter(TypedDict, total=False):
    """Filters the connection definitions that are returned by the
    ``GetConnections`` API operation.
    """

    MatchCriteria: Optional[MatchCriteria]
    ConnectionType: Optional[ConnectionType]
    ConnectionSchemaVersion: Optional[ConnectionSchemaVersion]


class GetConnectionsRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    Filter: Optional[GetConnectionsFilter]
    HidePassword: Optional[Boolean]
    NextToken: Optional[Token]
    MaxResults: Optional[PageSize]


class GetConnectionsResponse(TypedDict, total=False):
    ConnectionList: Optional[ConnectionList]
    NextToken: Optional[Token]


class GetCrawlerMetricsRequest(ServiceRequest):
    CrawlerNameList: Optional[CrawlerNameList]
    MaxResults: Optional[PageSize]
    NextToken: Optional[Token]


class GetCrawlerMetricsResponse(TypedDict, total=False):
    CrawlerMetricsList: Optional[CrawlerMetricsList]
    NextToken: Optional[Token]


class GetCrawlerRequest(ServiceRequest):
    Name: NameString


class GetCrawlerResponse(TypedDict, total=False):
    Crawler: Optional[Crawler]


class GetCrawlersRequest(ServiceRequest):
    MaxResults: Optional[PageSize]
    NextToken: Optional[Token]


class GetCrawlersResponse(TypedDict, total=False):
    Crawlers: Optional[CrawlerList]
    NextToken: Optional[Token]


class GetCustomEntityTypeRequest(ServiceRequest):
    Name: NameString


class GetCustomEntityTypeResponse(TypedDict, total=False):
    Name: Optional[NameString]
    RegexString: Optional[NameString]
    ContextWords: Optional[ContextWords]


class GetDataCatalogEncryptionSettingsRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]


class GetDataCatalogEncryptionSettingsResponse(TypedDict, total=False):
    DataCatalogEncryptionSettings: Optional[DataCatalogEncryptionSettings]


class GetDataQualityModelRequest(ServiceRequest):
    StatisticId: Optional[HashString]
    ProfileId: HashString


class GetDataQualityModelResponse(TypedDict, total=False):
    Status: Optional[DataQualityModelStatus]
    StartedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    FailureReason: Optional[HashString]


class GetDataQualityModelResultRequest(ServiceRequest):
    StatisticId: HashString
    ProfileId: HashString


class StatisticModelResult(TypedDict, total=False):
    """The statistic model result."""

    LowerBound: Optional[NullableDouble]
    UpperBound: Optional[NullableDouble]
    PredictedValue: Optional[NullableDouble]
    ActualValue: Optional[NullableDouble]
    Date: Optional[Timestamp]
    InclusionAnnotation: Optional[InclusionAnnotationValue]


StatisticModelResults = List[StatisticModelResult]


class GetDataQualityModelResultResponse(TypedDict, total=False):
    CompletedOn: Optional[Timestamp]
    Model: Optional[StatisticModelResults]


class GetDataQualityResultRequest(ServiceRequest):
    ResultId: HashString


class GetDataQualityResultResponse(TypedDict, total=False):
    ResultId: Optional[HashString]
    ProfileId: Optional[HashString]
    Score: Optional[GenericBoundedDouble]
    DataSource: Optional[DataSource]
    RulesetName: Optional[NameString]
    EvaluationContext: Optional[GenericString]
    StartedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    JobName: Optional[NameString]
    JobRunId: Optional[HashString]
    RulesetEvaluationRunId: Optional[HashString]
    RuleResults: Optional[DataQualityRuleResults]
    AnalyzerResults: Optional[DataQualityAnalyzerResults]
    Observations: Optional[DataQualityObservations]


class GetDataQualityRuleRecommendationRunRequest(ServiceRequest):
    RunId: HashString


class GetDataQualityRuleRecommendationRunResponse(TypedDict, total=False):
    RunId: Optional[HashString]
    DataSource: Optional[DataSource]
    Role: Optional[RoleString]
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    Status: Optional[TaskStatusType]
    ErrorString: Optional[GenericString]
    StartedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    ExecutionTime: Optional[ExecutionTime]
    RecommendedRuleset: Optional[DataQualityRulesetString]
    CreatedRulesetName: Optional[NameString]
    DataQualitySecurityConfiguration: Optional[NameString]


class GetDataQualityRulesetEvaluationRunRequest(ServiceRequest):
    RunId: HashString


RulesetNames = List[NameString]


class GetDataQualityRulesetEvaluationRunResponse(TypedDict, total=False):
    RunId: Optional[HashString]
    DataSource: Optional[DataSource]
    Role: Optional[RoleString]
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    AdditionalRunOptions: Optional[DataQualityEvaluationRunAdditionalRunOptions]
    Status: Optional[TaskStatusType]
    ErrorString: Optional[GenericString]
    StartedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    ExecutionTime: Optional[ExecutionTime]
    RulesetNames: Optional[RulesetNames]
    ResultIds: Optional[DataQualityResultIdList]
    AdditionalDataSources: Optional[DataSourceMap]


class GetDataQualityRulesetRequest(ServiceRequest):
    Name: NameString


class GetDataQualityRulesetResponse(TypedDict, total=False):
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Ruleset: Optional[DataQualityRulesetString]
    TargetTable: Optional[DataQualityTargetTable]
    CreatedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    RecommendationRunId: Optional[HashString]
    DataQualitySecurityConfiguration: Optional[NameString]


class GetDatabaseRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    Name: NameString


class GetDatabaseResponse(TypedDict, total=False):
    Database: Optional[Database]


class GetDatabasesRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    NextToken: Optional[Token]
    MaxResults: Optional[CatalogGetterPageSize]
    ResourceShareType: Optional[ResourceShareType]
    AttributesToGet: Optional[DatabaseAttributesList]


class GetDatabasesResponse(TypedDict, total=False):
    DatabaseList: DatabaseList
    NextToken: Optional[Token]


class GetDataflowGraphRequest(ServiceRequest):
    PythonScript: Optional[PythonScript]


class GetDataflowGraphResponse(TypedDict, total=False):
    DagNodes: Optional[DagNodes]
    DagEdges: Optional[DagEdges]


class GetDevEndpointRequest(ServiceRequest):
    EndpointName: GenericString


class GetDevEndpointResponse(TypedDict, total=False):
    DevEndpoint: Optional[DevEndpoint]


class GetDevEndpointsRequest(ServiceRequest):
    MaxResults: Optional[PageSize]
    NextToken: Optional[GenericString]


class GetDevEndpointsResponse(TypedDict, total=False):
    DevEndpoints: Optional[DevEndpointList]
    NextToken: Optional[GenericString]


SelectedFields = List[EntityFieldName]
Limit = int


class GetEntityRecordsRequest(ServiceRequest):
    ConnectionName: Optional[NameString]
    CatalogId: Optional[CatalogIdString]
    EntityName: EntityName
    NextToken: Optional[NextToken]
    DataStoreApiVersion: Optional[ApiVersion]
    ConnectionOptions: Optional[ConnectionOptions]
    FilterPredicate: Optional[FilterPredicate]
    Limit: Limit
    OrderBy: Optional[String]
    SelectedFields: Optional[SelectedFields]


class Record(TypedDict, total=False):
    pass


Records = List[Record]


class GetEntityRecordsResponse(TypedDict, total=False):
    Records: Optional[Records]
    NextToken: Optional[NextToken]


class GetIntegrationResourcePropertyRequest(ServiceRequest):
    ResourceArn: String128


class GetIntegrationResourcePropertyResponse(TypedDict, total=False):
    ResourceArn: Optional[String128]
    SourceProcessingProperties: Optional[SourceProcessingProperties]
    TargetProcessingProperties: Optional[TargetProcessingProperties]


class GetIntegrationTablePropertiesRequest(ServiceRequest):
    ResourceArn: String128
    TableName: String128


class GetIntegrationTablePropertiesResponse(TypedDict, total=False):
    ResourceArn: Optional[String128]
    TableName: Optional[String128]
    SourceTableConfig: Optional[SourceTableConfig]
    TargetTableConfig: Optional[TargetTableConfig]


class GetJobBookmarkRequest(ServiceRequest):
    JobName: JobName
    RunId: Optional[RunId]


class JobBookmarkEntry(TypedDict, total=False):
    """Defines a point that a job can resume processing."""

    JobName: Optional[JobName]
    Version: Optional[IntegerValue]
    Run: Optional[IntegerValue]
    Attempt: Optional[IntegerValue]
    PreviousRunId: Optional[RunId]
    RunId: Optional[RunId]
    JobBookmark: Optional[JsonValue]


class GetJobBookmarkResponse(TypedDict, total=False):
    JobBookmarkEntry: Optional[JobBookmarkEntry]


class GetJobRequest(ServiceRequest):
    JobName: NameString


class GetJobResponse(TypedDict, total=False):
    Job: Optional[Job]


class GetJobRunRequest(ServiceRequest):
    JobName: NameString
    RunId: IdString
    PredecessorsIncluded: Optional[BooleanValue]


class GetJobRunResponse(TypedDict, total=False):
    JobRun: Optional[JobRun]


class GetJobRunsRequest(ServiceRequest):
    JobName: NameString
    NextToken: Optional[GenericString]
    MaxResults: Optional[OrchestrationPageSize200]


class GetJobRunsResponse(TypedDict, total=False):
    JobRuns: Optional[JobRunList]
    NextToken: Optional[GenericString]


class GetJobsRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    MaxResults: Optional[PageSize]


class GetJobsResponse(TypedDict, total=False):
    Jobs: Optional[JobList]
    NextToken: Optional[GenericString]


class GetMLTaskRunRequest(ServiceRequest):
    TransformId: HashString
    TaskRunId: HashString


class LabelingSetGenerationTaskRunProperties(TypedDict, total=False):
    """Specifies configuration properties for a labeling set generation task
    run.
    """

    OutputS3Path: Optional[UriString]


class ImportLabelsTaskRunProperties(TypedDict, total=False):
    """Specifies configuration properties for an importing labels task run."""

    InputS3Path: Optional[UriString]
    Replace: Optional[ReplaceBoolean]


class TaskRunProperties(TypedDict, total=False):
    """The configuration properties for the task run."""

    TaskType: Optional[TaskType]
    ImportLabelsTaskRunProperties: Optional[ImportLabelsTaskRunProperties]
    ExportLabelsTaskRunProperties: Optional[ExportLabelsTaskRunProperties]
    LabelingSetGenerationTaskRunProperties: Optional[LabelingSetGenerationTaskRunProperties]
    FindMatchesTaskRunProperties: Optional[FindMatchesTaskRunProperties]


class GetMLTaskRunResponse(TypedDict, total=False):
    TransformId: Optional[HashString]
    TaskRunId: Optional[HashString]
    Status: Optional[TaskStatusType]
    LogGroupName: Optional[GenericString]
    Properties: Optional[TaskRunProperties]
    ErrorString: Optional[GenericString]
    StartedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    ExecutionTime: Optional[ExecutionTime]


class TaskRunSortCriteria(TypedDict, total=False):
    """The sorting criteria that are used to sort the list of task runs for the
    machine learning transform.
    """

    Column: TaskRunSortColumnType
    SortDirection: SortDirectionType


class TaskRunFilterCriteria(TypedDict, total=False):
    """The criteria that are used to filter the task runs for the machine
    learning transform.
    """

    TaskRunType: Optional[TaskType]
    Status: Optional[TaskStatusType]
    StartedBefore: Optional[Timestamp]
    StartedAfter: Optional[Timestamp]


class GetMLTaskRunsRequest(ServiceRequest):
    TransformId: HashString
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]
    Filter: Optional[TaskRunFilterCriteria]
    Sort: Optional[TaskRunSortCriteria]


class TaskRun(TypedDict, total=False):
    """The sampling parameters that are associated with the machine learning
    transform.
    """

    TransformId: Optional[HashString]
    TaskRunId: Optional[HashString]
    Status: Optional[TaskStatusType]
    LogGroupName: Optional[GenericString]
    Properties: Optional[TaskRunProperties]
    ErrorString: Optional[GenericString]
    StartedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    CompletedOn: Optional[Timestamp]
    ExecutionTime: Optional[ExecutionTime]


TaskRunList = List[TaskRun]


class GetMLTaskRunsResponse(TypedDict, total=False):
    TaskRuns: Optional[TaskRunList]
    NextToken: Optional[PaginationToken]


class GetMLTransformRequest(ServiceRequest):
    TransformId: HashString


class SchemaColumn(TypedDict, total=False):
    """A key-value pair representing a column and data type that this transform
    can run against. The ``Schema`` parameter of the ``MLTransform`` may
    contain up to 100 of these structures.
    """

    Name: Optional[ColumnNameString]
    DataType: Optional[ColumnTypeString]


TransformSchema = List[SchemaColumn]


class GetMLTransformResponse(TypedDict, total=False):
    TransformId: Optional[HashString]
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Status: Optional[TransformStatusType]
    CreatedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    InputRecordTables: Optional[GlueTables]
    Parameters: Optional[TransformParameters]
    EvaluationMetrics: Optional[EvaluationMetrics]
    LabelCount: Optional[LabelCount]
    Schema: Optional[TransformSchema]
    Role: Optional[RoleString]
    GlueVersion: Optional[GlueVersionString]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    MaxRetries: Optional[NullableInteger]
    TransformEncryption: Optional[TransformEncryption]


class TransformSortCriteria(TypedDict, total=False):
    """The sorting criteria that are associated with the machine learning
    transform.
    """

    Column: TransformSortColumnType
    SortDirection: SortDirectionType


class TransformFilterCriteria(TypedDict, total=False):
    """The criteria used to filter the machine learning transforms."""

    Name: Optional[NameString]
    TransformType: Optional[TransformType]
    Status: Optional[TransformStatusType]
    GlueVersion: Optional[GlueVersionString]
    CreatedBefore: Optional[Timestamp]
    CreatedAfter: Optional[Timestamp]
    LastModifiedBefore: Optional[Timestamp]
    LastModifiedAfter: Optional[Timestamp]
    Schema: Optional[TransformSchema]


class GetMLTransformsRequest(ServiceRequest):
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]
    Filter: Optional[TransformFilterCriteria]
    Sort: Optional[TransformSortCriteria]


class MLTransform(TypedDict, total=False):
    """A structure for a machine learning transform."""

    TransformId: Optional[HashString]
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Status: Optional[TransformStatusType]
    CreatedOn: Optional[Timestamp]
    LastModifiedOn: Optional[Timestamp]
    InputRecordTables: Optional[GlueTables]
    Parameters: Optional[TransformParameters]
    EvaluationMetrics: Optional[EvaluationMetrics]
    LabelCount: Optional[LabelCount]
    Schema: Optional[TransformSchema]
    Role: Optional[RoleString]
    GlueVersion: Optional[GlueVersionString]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    MaxRetries: Optional[NullableInteger]
    TransformEncryption: Optional[TransformEncryption]


TransformList = List[MLTransform]


class GetMLTransformsResponse(TypedDict, total=False):
    Transforms: TransformList
    NextToken: Optional[PaginationToken]


class Location(TypedDict, total=False):
    """The location of resources."""

    Jdbc: Optional[CodeGenNodeArgs]
    S3: Optional[CodeGenNodeArgs]
    DynamoDB: Optional[CodeGenNodeArgs]


class GetMappingRequest(ServiceRequest):
    Source: CatalogEntry
    Sinks: Optional[CatalogEntries]
    Location: Optional[Location]


class MappingEntry(TypedDict, total=False):
    """Defines a mapping."""

    SourceTable: Optional[TableName]
    SourcePath: Optional[SchemaPathString]
    SourceType: Optional[FieldType]
    TargetTable: Optional[TableName]
    TargetPath: Optional[SchemaPathString]
    TargetType: Optional[FieldType]


MappingList = List[MappingEntry]


class GetMappingResponse(TypedDict, total=False):
    Mapping: MappingList


class GetPartitionIndexesRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    NextToken: Optional[Token]


class KeySchemaElement(TypedDict, total=False):
    """A partition key pair consisting of a name and a type."""

    Name: NameString
    Type: ColumnTypeString


KeySchemaElementList = List[KeySchemaElement]


class PartitionIndexDescriptor(TypedDict, total=False):
    """A descriptor for a partition index in a table."""

    IndexName: NameString
    Keys: KeySchemaElementList
    IndexStatus: PartitionIndexStatus
    BackfillErrors: Optional[BackfillErrors]


PartitionIndexDescriptorList = List[PartitionIndexDescriptor]


class GetPartitionIndexesResponse(TypedDict, total=False):
    PartitionIndexDescriptorList: Optional[PartitionIndexDescriptorList]
    NextToken: Optional[Token]


class GetPartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionValues: ValueStringList


class GetPartitionResponse(TypedDict, total=False):
    Partition: Optional[Partition]


class Segment(TypedDict, total=False):
    """Defines a non-overlapping region of a table's partitions, allowing
    multiple requests to be run in parallel.
    """

    SegmentNumber: NonNegativeInteger
    TotalSegments: TotalSegmentsInteger


class GetPartitionsRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    Expression: Optional[PredicateString]
    NextToken: Optional[Token]
    Segment: Optional[Segment]
    MaxResults: Optional[PageSize]
    ExcludeColumnSchema: Optional[BooleanNullable]
    TransactionId: Optional[TransactionIdString]
    QueryAsOfTime: Optional[Timestamp]


class GetPartitionsResponse(TypedDict, total=False):
    Partitions: Optional[PartitionList]
    NextToken: Optional[Token]


class GetPlanRequest(ServiceRequest):
    Mapping: MappingList
    Source: CatalogEntry
    Sinks: Optional[CatalogEntries]
    Location: Optional[Location]
    Language: Optional[Language]
    AdditionalPlanOptionsMap: Optional[AdditionalPlanOptionsMap]


class GetPlanResponse(TypedDict, total=False):
    PythonScript: Optional[PythonScript]
    ScalaCode: Optional[ScalaCode]


class GetRegistryInput(ServiceRequest):
    RegistryId: RegistryId


class GetRegistryResponse(TypedDict, total=False):
    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]
    Description: Optional[DescriptionString]
    Status: Optional[RegistryStatus]
    CreatedTime: Optional[CreatedTimestamp]
    UpdatedTime: Optional[UpdatedTimestamp]


class GetResourcePoliciesRequest(ServiceRequest):
    NextToken: Optional[Token]
    MaxResults: Optional[PageSize]


class GluePolicy(TypedDict, total=False):
    """A structure for returning a resource policy."""

    PolicyInJson: Optional[PolicyJsonString]
    PolicyHash: Optional[HashString]
    CreateTime: Optional[Timestamp]
    UpdateTime: Optional[Timestamp]


GetResourcePoliciesResponseList = List[GluePolicy]


class GetResourcePoliciesResponse(TypedDict, total=False):
    GetResourcePoliciesResponseList: Optional[GetResourcePoliciesResponseList]
    NextToken: Optional[Token]


class GetResourcePolicyRequest(ServiceRequest):
    ResourceArn: Optional[GlueResourceArn]


class GetResourcePolicyResponse(TypedDict, total=False):
    PolicyInJson: Optional[PolicyJsonString]
    PolicyHash: Optional[HashString]
    CreateTime: Optional[Timestamp]
    UpdateTime: Optional[Timestamp]


class GetSchemaByDefinitionInput(ServiceRequest):
    SchemaId: SchemaId
    SchemaDefinition: SchemaDefinitionString


class GetSchemaByDefinitionResponse(TypedDict, total=False):
    SchemaVersionId: Optional[SchemaVersionIdString]
    SchemaArn: Optional[GlueResourceArn]
    DataFormat: Optional[DataFormat]
    Status: Optional[SchemaVersionStatus]
    CreatedTime: Optional[CreatedTimestamp]


class GetSchemaInput(ServiceRequest):
    SchemaId: SchemaId


class GetSchemaResponse(TypedDict, total=False):
    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    SchemaArn: Optional[GlueResourceArn]
    Description: Optional[DescriptionString]
    DataFormat: Optional[DataFormat]
    Compatibility: Optional[Compatibility]
    SchemaCheckpoint: Optional[SchemaCheckpointNumber]
    LatestSchemaVersion: Optional[VersionLongNumber]
    NextSchemaVersion: Optional[VersionLongNumber]
    SchemaStatus: Optional[SchemaStatus]
    CreatedTime: Optional[CreatedTimestamp]
    UpdatedTime: Optional[UpdatedTimestamp]


class SchemaVersionNumber(TypedDict, total=False):
    """A structure containing the schema version information."""

    LatestVersion: Optional[LatestSchemaVersionBoolean]
    VersionNumber: Optional[VersionLongNumber]


class GetSchemaVersionInput(ServiceRequest):
    SchemaId: Optional[SchemaId]
    SchemaVersionId: Optional[SchemaVersionIdString]
    SchemaVersionNumber: Optional[SchemaVersionNumber]


class GetSchemaVersionResponse(TypedDict, total=False):
    SchemaVersionId: Optional[SchemaVersionIdString]
    SchemaDefinition: Optional[SchemaDefinitionString]
    DataFormat: Optional[DataFormat]
    SchemaArn: Optional[GlueResourceArn]
    VersionNumber: Optional[VersionLongNumber]
    Status: Optional[SchemaVersionStatus]
    CreatedTime: Optional[CreatedTimestamp]


class GetSchemaVersionsDiffInput(ServiceRequest):
    SchemaId: SchemaId
    FirstSchemaVersionNumber: SchemaVersionNumber
    SecondSchemaVersionNumber: SchemaVersionNumber
    SchemaDiffType: SchemaDiffType


class GetSchemaVersionsDiffResponse(TypedDict, total=False):
    Diff: Optional[SchemaDefinitionDiff]


class GetSecurityConfigurationRequest(ServiceRequest):
    Name: NameString


class SecurityConfiguration(TypedDict, total=False):
    """Specifies a security configuration."""

    Name: Optional[NameString]
    CreatedTimeStamp: Optional[TimestampValue]
    EncryptionConfiguration: Optional[EncryptionConfiguration]


class GetSecurityConfigurationResponse(TypedDict, total=False):
    SecurityConfiguration: Optional[SecurityConfiguration]


class GetSecurityConfigurationsRequest(ServiceRequest):
    MaxResults: Optional[PageSize]
    NextToken: Optional[GenericString]


SecurityConfigurationList = List[SecurityConfiguration]


class GetSecurityConfigurationsResponse(TypedDict, total=False):
    SecurityConfigurations: Optional[SecurityConfigurationList]
    NextToken: Optional[GenericString]


class GetSessionRequest(ServiceRequest):
    Id: NameString
    RequestOrigin: Optional[OrchestrationNameString]


class GetSessionResponse(TypedDict, total=False):
    Session: Optional[Session]


class GetStatementRequest(ServiceRequest):
    SessionId: NameString
    Id: IntegerValue
    RequestOrigin: Optional[OrchestrationNameString]


LongValue = int
OrchestrationStringList = List[GenericString]


class StatementOutputData(TypedDict, total=False):
    """The code execution output in JSON format."""

    TextPlain: Optional[GenericString]


class StatementOutput(TypedDict, total=False):
    """The code execution output in JSON format."""

    Data: Optional[StatementOutputData]
    ExecutionCount: Optional[IntegerValue]
    Status: Optional[StatementState]
    ErrorName: Optional[GenericString]
    ErrorValue: Optional[GenericString]
    Traceback: Optional[OrchestrationStringList]


class Statement(TypedDict, total=False):
    """The statement or request for a particular action to occur in a session."""

    Id: Optional[IntegerValue]
    Code: Optional[GenericString]
    State: Optional[StatementState]
    Output: Optional[StatementOutput]
    Progress: Optional[DoubleValue]
    StartedOn: Optional[LongValue]
    CompletedOn: Optional[LongValue]


class GetStatementResponse(TypedDict, total=False):
    Statement: Optional[Statement]


class GetTableOptimizerRequest(ServiceRequest):
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    Type: TableOptimizerType


class GetTableOptimizerResponse(TypedDict, total=False):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: Optional[NameString]
    TableName: Optional[NameString]
    TableOptimizer: Optional[TableOptimizer]


class GetTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    Name: NameString
    TransactionId: Optional[TransactionIdString]
    QueryAsOfTime: Optional[Timestamp]
    IncludeStatusDetails: Optional[BooleanNullable]


class ViewValidation(TypedDict, total=False):
    """A structure that contains information for an analytical engine to
    validate a view, prior to persisting the view metadata. Used in the case
    of direct ``UpdateTable`` or ``CreateTable`` API calls.
    """

    Dialect: Optional[ViewDialect]
    DialectVersion: Optional[ViewDialectVersionString]
    ViewValidationText: Optional[ViewTextString]
    UpdateTime: Optional[Timestamp]
    State: Optional[ResourceState]
    Error: Optional[ErrorDetail]


ViewValidationList = List[ViewValidation]


class Table(TypedDict, total=False):
    """Represents a collection of related data organized in columns and rows."""

    Name: "NameString"
    DatabaseName: Optional["NameString"]
    Description: Optional["DescriptionString"]
    Owner: Optional["NameString"]
    CreateTime: Optional["Timestamp"]
    UpdateTime: Optional["Timestamp"]
    LastAccessTime: Optional["Timestamp"]
    LastAnalyzedTime: Optional["Timestamp"]
    Retention: Optional["NonNegativeInteger"]
    StorageDescriptor: Optional["StorageDescriptor"]
    PartitionKeys: Optional["ColumnList"]
    ViewOriginalText: Optional["ViewTextString"]
    ViewExpandedText: Optional["ViewTextString"]
    TableType: Optional["TableTypeString"]
    Parameters: Optional["ParametersMap"]
    CreatedBy: Optional["NameString"]
    IsRegisteredWithLakeFormation: Optional["Boolean"]
    TargetTable: Optional["TableIdentifier"]
    CatalogId: Optional["CatalogIdString"]
    VersionId: Optional["VersionString"]
    FederatedTable: Optional["FederatedTable"]
    ViewDefinition: Optional["ViewDefinition"]
    IsMultiDialectView: Optional["NullableBoolean"]
    Status: Optional["TableStatus"]


class StatusDetails(TypedDict, total=False):
    """A structure containing information about an asynchronous change to a
    table.
    """

    RequestedChange: Optional[Table]
    ViewValidations: Optional[ViewValidationList]


class TableStatus(TypedDict, total=False):
    """A structure containing information about the state of an asynchronous
    change to a table.
    """

    RequestedBy: Optional[NameString]
    UpdatedBy: Optional[NameString]
    RequestTime: Optional[Timestamp]
    UpdateTime: Optional[Timestamp]
    Action: Optional[ResourceAction]
    State: Optional[ResourceState]
    Error: Optional[ErrorDetail]
    Details: Optional[StatusDetails]


class ViewRepresentation(TypedDict, total=False):
    """A structure that contains the dialect of the view, and the query that
    defines the view.
    """

    Dialect: Optional[ViewDialect]
    DialectVersion: Optional[ViewDialectVersionString]
    ViewOriginalText: Optional[ViewTextString]
    ViewExpandedText: Optional[ViewTextString]
    ValidationConnection: Optional[NameString]
    IsStale: Optional[NullableBoolean]


ViewRepresentationList = List[ViewRepresentation]


class ViewDefinition(TypedDict, total=False):
    """A structure containing details for representations."""

    IsProtected: Optional[NullableBoolean]
    Definer: Optional[ArnString]
    SubObjects: Optional[ViewSubObjectsList]
    Representations: Optional[ViewRepresentationList]


class GetTableResponse(TypedDict, total=False):
    Table: Optional[Table]


class GetTableVersionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    VersionId: Optional[VersionString]


class TableVersion(TypedDict, total=False):
    """Specifies a version of a table."""

    Table: Optional[Table]
    VersionId: Optional[VersionString]


class GetTableVersionResponse(TypedDict, total=False):
    TableVersion: Optional[TableVersion]


GetTableVersionsList = List[TableVersion]


class GetTableVersionsRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    NextToken: Optional[Token]
    MaxResults: Optional[CatalogGetterPageSize]


class GetTableVersionsResponse(TypedDict, total=False):
    TableVersions: Optional[GetTableVersionsList]
    NextToken: Optional[Token]


TableAttributesList = List[TableAttributes]


class GetTablesRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    Expression: Optional[FilterString]
    NextToken: Optional[Token]
    MaxResults: Optional[CatalogGetterPageSize]
    TransactionId: Optional[TransactionIdString]
    QueryAsOfTime: Optional[Timestamp]
    IncludeStatusDetails: Optional[BooleanNullable]
    AttributesToGet: Optional[TableAttributesList]


TableList = List[Table]


class GetTablesResponse(TypedDict, total=False):
    TableList: Optional[TableList]
    NextToken: Optional[Token]


class GetTagsRequest(ServiceRequest):
    ResourceArn: GlueResourceArn


class GetTagsResponse(TypedDict, total=False):
    Tags: Optional[TagsMap]


class GetTriggerRequest(ServiceRequest):
    Name: NameString


class GetTriggerResponse(TypedDict, total=False):
    Trigger: Optional[Trigger]


class GetTriggersRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    DependentJobName: Optional[NameString]
    MaxResults: Optional[OrchestrationPageSize200]


class GetTriggersResponse(TypedDict, total=False):
    Triggers: Optional[TriggerList]
    NextToken: Optional[GenericString]


class QuerySessionContext(TypedDict, total=False):
    """A structure used as a protocol between query engines and Lake Formation
    or Glue. Contains both a Lake Formation generated authorization
    identifier and information from the request's authorization context.
    """

    QueryId: Optional[HashString]
    QueryStartTime: Optional[Timestamp]
    ClusterId: Optional[NullableString]
    QueryAuthorizationId: Optional[HashString]
    AdditionalContext: Optional[AdditionalContextMap]


PermissionTypeList = List[PermissionType]


class GetUnfilteredPartitionMetadataRequest(ServiceRequest):
    Region: Optional[ValueString]
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    PartitionValues: ValueStringList
    AuditContext: Optional[AuditContext]
    SupportedPermissionTypes: PermissionTypeList
    QuerySessionContext: Optional[QuerySessionContext]


class GetUnfilteredPartitionMetadataResponse(TypedDict, total=False):
    Partition: Optional[Partition]
    AuthorizedColumns: Optional[NameStringList]
    IsRegisteredWithLakeFormation: Optional[Boolean]


class GetUnfilteredPartitionsMetadataRequest(ServiceRequest):
    Region: Optional[ValueString]
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    Expression: Optional[PredicateString]
    AuditContext: Optional[AuditContext]
    SupportedPermissionTypes: PermissionTypeList
    NextToken: Optional[Token]
    Segment: Optional[Segment]
    MaxResults: Optional[PageSize]
    QuerySessionContext: Optional[QuerySessionContext]


class UnfilteredPartition(TypedDict, total=False):
    """A partition that contains unfiltered metadata."""

    Partition: Optional[Partition]
    AuthorizedColumns: Optional[NameStringList]
    IsRegisteredWithLakeFormation: Optional[Boolean]


UnfilteredPartitionList = List[UnfilteredPartition]


class GetUnfilteredPartitionsMetadataResponse(TypedDict, total=False):
    UnfilteredPartitions: Optional[UnfilteredPartitionList]
    NextToken: Optional[Token]


class SupportedDialect(TypedDict, total=False):
    """A structure specifying the dialect and dialect version used by the query
    engine.
    """

    Dialect: Optional[ViewDialect]
    DialectVersion: Optional[ViewDialectVersionString]


class GetUnfilteredTableMetadataRequest(ServiceRequest):
    Region: Optional[ValueString]
    CatalogId: CatalogIdString
    DatabaseName: NameString
    Name: NameString
    AuditContext: Optional[AuditContext]
    SupportedPermissionTypes: PermissionTypeList
    ParentResourceArn: Optional[ArnString]
    RootResourceArn: Optional[ArnString]
    SupportedDialect: Optional[SupportedDialect]
    Permissions: Optional[PermissionList]
    QuerySessionContext: Optional[QuerySessionContext]


class GetUnfilteredTableMetadataResponse(TypedDict, total=False):
    Table: Optional[Table]
    AuthorizedColumns: Optional[NameStringList]
    IsRegisteredWithLakeFormation: Optional[Boolean]
    CellFilters: Optional[ColumnRowFilterList]
    QueryAuthorizationId: Optional[HashString]
    IsMultiDialectView: Optional[Boolean]
    ResourceArn: Optional[ArnString]
    IsProtected: Optional[Boolean]
    Permissions: Optional[PermissionList]
    RowFilter: Optional[PredicateString]


class GetUsageProfileRequest(ServiceRequest):
    Name: NameString


class GetUsageProfileResponse(TypedDict, total=False):
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Configuration: Optional[ProfileConfiguration]
    CreatedOn: Optional[TimestampValue]
    LastModifiedOn: Optional[TimestampValue]


class GetUserDefinedFunctionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    FunctionName: NameString


class UserDefinedFunction(TypedDict, total=False):
    """Represents the equivalent of a Hive user-defined function (``UDF``)
    definition.
    """

    FunctionName: Optional[NameString]
    DatabaseName: Optional[NameString]
    ClassName: Optional[NameString]
    OwnerName: Optional[NameString]
    OwnerType: Optional[PrincipalType]
    CreateTime: Optional[Timestamp]
    ResourceUris: Optional[ResourceUriList]
    CatalogId: Optional[CatalogIdString]


class GetUserDefinedFunctionResponse(TypedDict, total=False):
    UserDefinedFunction: Optional[UserDefinedFunction]


class GetUserDefinedFunctionsRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: Optional[NameString]
    Pattern: NameString
    NextToken: Optional[Token]
    MaxResults: Optional[CatalogGetterPageSize]


UserDefinedFunctionList = List[UserDefinedFunction]


class GetUserDefinedFunctionsResponse(TypedDict, total=False):
    UserDefinedFunctions: Optional[UserDefinedFunctionList]
    NextToken: Optional[Token]


class GetWorkflowRequest(ServiceRequest):
    Name: NameString
    IncludeGraph: Optional[NullableBoolean]


class GetWorkflowResponse(TypedDict, total=False):
    Workflow: Optional[Workflow]


class GetWorkflowRunPropertiesRequest(ServiceRequest):
    Name: NameString
    RunId: IdString


class GetWorkflowRunPropertiesResponse(TypedDict, total=False):
    RunProperties: Optional[WorkflowRunProperties]


class GetWorkflowRunRequest(ServiceRequest):
    Name: NameString
    RunId: IdString
    IncludeGraph: Optional[NullableBoolean]


class GetWorkflowRunResponse(TypedDict, total=False):
    Run: Optional[WorkflowRun]


class GetWorkflowRunsRequest(ServiceRequest):
    Name: NameString
    IncludeGraph: Optional[NullableBoolean]
    NextToken: Optional[GenericString]
    MaxResults: Optional[PageSize]


WorkflowRuns = List[WorkflowRun]


class GetWorkflowRunsResponse(TypedDict, total=False):
    Runs: Optional[WorkflowRuns]
    NextToken: Optional[GenericString]


class ImportCatalogToGlueRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]


class ImportCatalogToGlueResponse(TypedDict, total=False):
    pass


class JobUpdate(TypedDict, total=False):
    """Specifies information used to update an existing job definition. The
    previous job definition is completely overwritten by this information.
    """

    JobMode: Optional[JobMode]
    JobRunQueuingEnabled: Optional[NullableBoolean]
    Description: Optional[DescriptionString]
    LogUri: Optional[UriString]
    Role: Optional[RoleString]
    ExecutionProperty: Optional[ExecutionProperty]
    Command: Optional[JobCommand]
    DefaultArguments: Optional[GenericMap]
    NonOverridableArguments: Optional[GenericMap]
    Connections: Optional[ConnectionsList]
    MaxRetries: Optional[MaxRetries]
    AllocatedCapacity: Optional[IntegerValue]
    Timeout: Optional[Timeout]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    SecurityConfiguration: Optional[NameString]
    NotificationProperty: Optional[NotificationProperty]
    GlueVersion: Optional[GlueVersionString]
    CodeGenConfigurationNodes: Optional[CodeGenConfigurationNodes]
    ExecutionClass: Optional[ExecutionClass]
    SourceControlDetails: Optional[SourceControlDetails]
    MaintenanceWindow: Optional[MaintenanceWindow]


class ListBlueprintsRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    MaxResults: Optional[OrchestrationPageSize25]
    Tags: Optional[TagsMap]


class ListBlueprintsResponse(TypedDict, total=False):
    Blueprints: Optional[BlueprintNames]
    NextToken: Optional[GenericString]


class ListColumnStatisticsTaskRunsRequest(ServiceRequest):
    MaxResults: Optional[PageSize]
    NextToken: Optional[Token]


class ListColumnStatisticsTaskRunsResponse(TypedDict, total=False):
    ColumnStatisticsTaskRunIds: Optional[ColumnStatisticsTaskRunIdList]
    NextToken: Optional[Token]


class ListConnectionTypesRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListConnectionTypesResponse(TypedDict, total=False):
    ConnectionTypes: Optional[ConnectionTypeList]
    NextToken: Optional[NextToken]


class ListCrawlersRequest(ServiceRequest):
    MaxResults: Optional[PageSize]
    NextToken: Optional[Token]
    Tags: Optional[TagsMap]


class ListCrawlersResponse(TypedDict, total=False):
    CrawlerNames: Optional[CrawlerNameList]
    NextToken: Optional[Token]


class ListCrawlsRequest(ServiceRequest):
    CrawlerName: NameString
    MaxResults: Optional[PageSize]
    Filters: Optional[CrawlsFilterList]
    NextToken: Optional[Token]


class ListCrawlsResponse(TypedDict, total=False):
    Crawls: Optional[CrawlerHistoryList]
    NextToken: Optional[Token]


class ListCustomEntityTypesRequest(ServiceRequest):
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]
    Tags: Optional[TagsMap]


class ListCustomEntityTypesResponse(TypedDict, total=False):
    CustomEntityTypes: Optional[CustomEntityTypes]
    NextToken: Optional[PaginationToken]


class ListDataQualityResultsRequest(ServiceRequest):
    Filter: Optional[DataQualityResultFilterCriteria]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]


class ListDataQualityResultsResponse(TypedDict, total=False):
    Results: DataQualityResultDescriptionList
    NextToken: Optional[PaginationToken]


class ListDataQualityRuleRecommendationRunsRequest(ServiceRequest):
    Filter: Optional[DataQualityRuleRecommendationRunFilter]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]


class ListDataQualityRuleRecommendationRunsResponse(TypedDict, total=False):
    Runs: Optional[DataQualityRuleRecommendationRunList]
    NextToken: Optional[PaginationToken]


class ListDataQualityRulesetEvaluationRunsRequest(ServiceRequest):
    Filter: Optional[DataQualityRulesetEvaluationRunFilter]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]


class ListDataQualityRulesetEvaluationRunsResponse(TypedDict, total=False):
    Runs: Optional[DataQualityRulesetEvaluationRunList]
    NextToken: Optional[PaginationToken]


class ListDataQualityRulesetsRequest(ServiceRequest):
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]
    Filter: Optional[DataQualityRulesetFilterCriteria]
    Tags: Optional[TagsMap]


class ListDataQualityRulesetsResponse(TypedDict, total=False):
    Rulesets: Optional[DataQualityRulesetList]
    NextToken: Optional[PaginationToken]


class TimestampFilter(TypedDict, total=False):
    """A timestamp filter."""

    RecordedBefore: Optional[Timestamp]
    RecordedAfter: Optional[Timestamp]


class ListDataQualityStatisticAnnotationsRequest(ServiceRequest):
    StatisticId: Optional[HashString]
    ProfileId: Optional[HashString]
    TimestampFilter: Optional[TimestampFilter]
    MaxResults: Optional[PageSize]
    NextToken: Optional[PaginationToken]


class ListDataQualityStatisticAnnotationsResponse(TypedDict, total=False):
    Annotations: Optional[AnnotationList]
    NextToken: Optional[PaginationToken]


class ListDataQualityStatisticsRequest(ServiceRequest):
    StatisticId: Optional[HashString]
    ProfileId: Optional[HashString]
    TimestampFilter: Optional[TimestampFilter]
    MaxResults: Optional[PageSize]
    NextToken: Optional[PaginationToken]


StatisticPropertiesMap = Dict[NameString, DescriptionString]
ReferenceDatasetsList = List[NameString]


class RunIdentifier(TypedDict, total=False):
    """A run identifier."""

    RunId: Optional[HashString]
    JobRunId: Optional[HashString]


class StatisticSummary(TypedDict, total=False):
    """Summary information about a statistic."""

    StatisticId: Optional[HashString]
    ProfileId: Optional[HashString]
    RunIdentifier: Optional[RunIdentifier]
    StatisticName: Optional[StatisticNameString]
    DoubleValue: Optional[double]
    EvaluationLevel: Optional[StatisticEvaluationLevel]
    ColumnsReferenced: Optional[ColumnNameList]
    ReferencedDatasets: Optional[ReferenceDatasetsList]
    StatisticProperties: Optional[StatisticPropertiesMap]
    RecordedOn: Optional[Timestamp]
    InclusionAnnotation: Optional[TimestampedInclusionAnnotation]


StatisticSummaryList = List[StatisticSummary]


class ListDataQualityStatisticsResponse(TypedDict, total=False):
    Statistics: Optional[StatisticSummaryList]
    NextToken: Optional[PaginationToken]


class ListDevEndpointsRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    MaxResults: Optional[PageSize]
    Tags: Optional[TagsMap]


class ListDevEndpointsResponse(TypedDict, total=False):
    DevEndpointNames: Optional[DevEndpointNameList]
    NextToken: Optional[GenericString]


class ListEntitiesRequest(ServiceRequest):
    ConnectionName: Optional[NameString]
    CatalogId: Optional[CatalogIdString]
    ParentEntityName: Optional[EntityName]
    NextToken: Optional[NextToken]
    DataStoreApiVersion: Optional[ApiVersion]


class ListEntitiesResponse(TypedDict, total=False):
    Entities: Optional[EntityList]
    NextToken: Optional[NextToken]


class ListJobsRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    MaxResults: Optional[PageSize]
    Tags: Optional[TagsMap]


class ListJobsResponse(TypedDict, total=False):
    JobNames: Optional[JobNameList]
    NextToken: Optional[GenericString]


class ListMLTransformsRequest(ServiceRequest):
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[PageSize]
    Filter: Optional[TransformFilterCriteria]
    Sort: Optional[TransformSortCriteria]
    Tags: Optional[TagsMap]


TransformIdList = List[HashString]


class ListMLTransformsResponse(TypedDict, total=False):
    TransformIds: TransformIdList
    NextToken: Optional[PaginationToken]


class ListRegistriesInput(ServiceRequest):
    MaxResults: Optional[MaxResultsNumber]
    NextToken: Optional[SchemaRegistryTokenString]


class RegistryListItem(TypedDict, total=False):
    """A structure containing the details for a registry."""

    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]
    Description: Optional[DescriptionString]
    Status: Optional[RegistryStatus]
    CreatedTime: Optional[CreatedTimestamp]
    UpdatedTime: Optional[UpdatedTimestamp]


RegistryListDefinition = List[RegistryListItem]


class ListRegistriesResponse(TypedDict, total=False):
    Registries: Optional[RegistryListDefinition]
    NextToken: Optional[SchemaRegistryTokenString]


class ListSchemaVersionsInput(ServiceRequest):
    SchemaId: SchemaId
    MaxResults: Optional[MaxResultsNumber]
    NextToken: Optional[SchemaRegistryTokenString]


class SchemaVersionListItem(TypedDict, total=False):
    """An object containing the details about a schema version."""

    SchemaArn: Optional[GlueResourceArn]
    SchemaVersionId: Optional[SchemaVersionIdString]
    VersionNumber: Optional[VersionLongNumber]
    Status: Optional[SchemaVersionStatus]
    CreatedTime: Optional[CreatedTimestamp]


SchemaVersionList = List[SchemaVersionListItem]


class ListSchemaVersionsResponse(TypedDict, total=False):
    Schemas: Optional[SchemaVersionList]
    NextToken: Optional[SchemaRegistryTokenString]


class ListSchemasInput(ServiceRequest):
    RegistryId: Optional[RegistryId]
    MaxResults: Optional[MaxResultsNumber]
    NextToken: Optional[SchemaRegistryTokenString]


class SchemaListItem(TypedDict, total=False):
    """An object that contains minimal details for a schema."""

    RegistryName: Optional[SchemaRegistryNameString]
    SchemaName: Optional[SchemaRegistryNameString]
    SchemaArn: Optional[GlueResourceArn]
    Description: Optional[DescriptionString]
    SchemaStatus: Optional[SchemaStatus]
    CreatedTime: Optional[CreatedTimestamp]
    UpdatedTime: Optional[UpdatedTimestamp]


SchemaListDefinition = List[SchemaListItem]


class ListSchemasResponse(TypedDict, total=False):
    Schemas: Optional[SchemaListDefinition]
    NextToken: Optional[SchemaRegistryTokenString]


class ListSessionsRequest(ServiceRequest):
    NextToken: Optional[OrchestrationToken]
    MaxResults: Optional[PageSize]
    Tags: Optional[TagsMap]
    RequestOrigin: Optional[OrchestrationNameString]


SessionList = List[Session]
SessionIdList = List[NameString]


class ListSessionsResponse(TypedDict, total=False):
    Ids: Optional[SessionIdList]
    Sessions: Optional[SessionList]
    NextToken: Optional[OrchestrationToken]


class ListStatementsRequest(ServiceRequest):
    SessionId: NameString
    RequestOrigin: Optional[OrchestrationNameString]
    NextToken: Optional[OrchestrationToken]


StatementList = List[Statement]


class ListStatementsResponse(TypedDict, total=False):
    Statements: Optional[StatementList]
    NextToken: Optional[OrchestrationToken]


class ListTableOptimizerRunsRequest(ServiceRequest):
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    Type: TableOptimizerType
    MaxResults: Optional[MaxListTableOptimizerRunsTokenResults]
    NextToken: Optional[ListTableOptimizerRunsToken]


TableOptimizerRuns = List[TableOptimizerRun]


class ListTableOptimizerRunsResponse(TypedDict, total=False):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: Optional[NameString]
    TableName: Optional[NameString]
    NextToken: Optional[ListTableOptimizerRunsToken]
    TableOptimizerRuns: Optional[TableOptimizerRuns]


class ListTriggersRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    DependentJobName: Optional[NameString]
    MaxResults: Optional[OrchestrationPageSize200]
    Tags: Optional[TagsMap]


class ListTriggersResponse(TypedDict, total=False):
    TriggerNames: Optional[TriggerNameList]
    NextToken: Optional[GenericString]


class ListUsageProfilesRequest(ServiceRequest):
    NextToken: Optional[OrchestrationToken]
    MaxResults: Optional[OrchestrationPageSize200]


class UsageProfileDefinition(TypedDict, total=False):
    """Describes an Glue usage profile."""

    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    CreatedOn: Optional[TimestampValue]
    LastModifiedOn: Optional[TimestampValue]


UsageProfileDefinitionList = List[UsageProfileDefinition]


class ListUsageProfilesResponse(TypedDict, total=False):
    Profiles: Optional[UsageProfileDefinitionList]
    NextToken: Optional[OrchestrationToken]


class ListWorkflowsRequest(ServiceRequest):
    NextToken: Optional[GenericString]
    MaxResults: Optional[OrchestrationPageSize25]


class ListWorkflowsResponse(TypedDict, total=False):
    Workflows: Optional[WorkflowNames]
    NextToken: Optional[GenericString]


class OtherMetadataValueListItem(TypedDict, total=False):
    """A structure containing other metadata for a schema version belonging to
    the same metadata key.
    """

    MetadataValue: Optional[MetadataValueString]
    CreatedTime: Optional[CreatedTimestamp]


OtherMetadataValueList = List[OtherMetadataValueListItem]


class MetadataInfo(TypedDict, total=False):
    """A structure containing metadata information for a schema version."""

    MetadataValue: Optional[MetadataValueString]
    CreatedTime: Optional[CreatedTimestamp]
    OtherMetadataValueList: Optional[OtherMetadataValueList]


MetadataInfoMap = Dict[MetadataKeyString, MetadataInfo]


class MetadataKeyValuePair(TypedDict, total=False):
    """A structure containing a key value pair for metadata."""

    MetadataKey: Optional[MetadataKeyString]
    MetadataValue: Optional[MetadataValueString]


MetadataList = List[MetadataKeyValuePair]


class ModifyIntegrationRequest(ServiceRequest):
    IntegrationIdentifier: String128
    Description: Optional[IntegrationDescription]
    DataFilter: Optional[String2048]
    IntegrationName: Optional[String128]


class ModifyIntegrationResponse(TypedDict, total=False):
    SourceArn: String128
    TargetArn: String128
    IntegrationName: String128
    Description: Optional[IntegrationDescription]
    IntegrationArn: String128
    KmsKeyId: Optional[String2048]
    AdditionalEncryptionContext: Optional[IntegrationAdditionalEncryptionContextMap]
    Tags: Optional[IntegrationTagsList]
    Status: IntegrationStatus
    CreateTime: IntegrationTimestamp
    Errors: Optional[IntegrationErrorList]
    DataFilter: Optional[String2048]


NodeIdList = List[NameString]


class PropertyPredicate(TypedDict, total=False):
    """Defines a property predicate."""

    Key: Optional[ValueString]
    Value: Optional[ValueString]
    Comparator: Optional[Comparator]


class PutDataCatalogEncryptionSettingsRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettings


class PutDataCatalogEncryptionSettingsResponse(TypedDict, total=False):
    pass


class PutDataQualityProfileAnnotationRequest(ServiceRequest):
    ProfileId: HashString
    InclusionAnnotation: InclusionAnnotationValue


class PutDataQualityProfileAnnotationResponse(TypedDict, total=False):
    """Left blank."""

    pass


class PutResourcePolicyRequest(ServiceRequest):
    PolicyInJson: PolicyJsonString
    ResourceArn: Optional[GlueResourceArn]
    PolicyHashCondition: Optional[HashString]
    PolicyExistsCondition: Optional[ExistCondition]
    EnableHybrid: Optional[EnableHybridValues]


class PutResourcePolicyResponse(TypedDict, total=False):
    PolicyHash: Optional[HashString]


class PutSchemaVersionMetadataInput(ServiceRequest):
    SchemaId: Optional[SchemaId]
    SchemaVersionNumber: Optional[SchemaVersionNumber]
    SchemaVersionId: Optional[SchemaVersionIdString]
    MetadataKeyValue: MetadataKeyValuePair


class PutSchemaVersionMetadataResponse(TypedDict, total=False):
    SchemaArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    RegistryName: Optional[SchemaRegistryNameString]
    LatestVersion: Optional[LatestSchemaVersionBoolean]
    VersionNumber: Optional[VersionLongNumber]
    SchemaVersionId: Optional[SchemaVersionIdString]
    MetadataKey: Optional[MetadataKeyString]
    MetadataValue: Optional[MetadataValueString]


class PutWorkflowRunPropertiesRequest(ServiceRequest):
    Name: NameString
    RunId: IdString
    RunProperties: WorkflowRunProperties


class PutWorkflowRunPropertiesResponse(TypedDict, total=False):
    pass


class QuerySchemaVersionMetadataInput(ServiceRequest):
    SchemaId: Optional[SchemaId]
    SchemaVersionNumber: Optional[SchemaVersionNumber]
    SchemaVersionId: Optional[SchemaVersionIdString]
    MetadataList: Optional[MetadataList]
    MaxResults: Optional[QuerySchemaVersionMetadataMaxResults]
    NextToken: Optional[SchemaRegistryTokenString]


class QuerySchemaVersionMetadataResponse(TypedDict, total=False):
    MetadataInfoMap: Optional[MetadataInfoMap]
    SchemaVersionId: Optional[SchemaVersionIdString]
    NextToken: Optional[SchemaRegistryTokenString]


class RegisterSchemaVersionInput(ServiceRequest):
    SchemaId: SchemaId
    SchemaDefinition: SchemaDefinitionString


class RegisterSchemaVersionResponse(TypedDict, total=False):
    SchemaVersionId: Optional[SchemaVersionIdString]
    VersionNumber: Optional[VersionLongNumber]
    Status: Optional[SchemaVersionStatus]


class RemoveSchemaVersionMetadataInput(ServiceRequest):
    SchemaId: Optional[SchemaId]
    SchemaVersionNumber: Optional[SchemaVersionNumber]
    SchemaVersionId: Optional[SchemaVersionIdString]
    MetadataKeyValue: MetadataKeyValuePair


class RemoveSchemaVersionMetadataResponse(TypedDict, total=False):
    SchemaArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    RegistryName: Optional[SchemaRegistryNameString]
    LatestVersion: Optional[LatestSchemaVersionBoolean]
    VersionNumber: Optional[VersionLongNumber]
    SchemaVersionId: Optional[SchemaVersionIdString]
    MetadataKey: Optional[MetadataKeyString]
    MetadataValue: Optional[MetadataValueString]


class ResetJobBookmarkRequest(ServiceRequest):
    JobName: JobName
    RunId: Optional[RunId]


class ResetJobBookmarkResponse(TypedDict, total=False):
    JobBookmarkEntry: Optional[JobBookmarkEntry]


class ResumeWorkflowRunRequest(ServiceRequest):
    Name: NameString
    RunId: IdString
    NodeIds: NodeIdList


class ResumeWorkflowRunResponse(TypedDict, total=False):
    RunId: Optional[IdString]
    NodeIds: Optional[NodeIdList]


class RunStatementRequest(ServiceRequest):
    SessionId: NameString
    Code: OrchestrationStatementCodeString
    RequestOrigin: Optional[OrchestrationNameString]


class RunStatementResponse(TypedDict, total=False):
    Id: Optional[IntegerValue]


SearchPropertyPredicates = List[PropertyPredicate]


class SortCriterion(TypedDict, total=False):
    """Specifies a field to sort by and a sort order."""

    FieldName: Optional[ValueString]
    Sort: Optional[Sort]


SortCriteria = List[SortCriterion]


class SearchTablesRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    NextToken: Optional[Token]
    Filters: Optional[SearchPropertyPredicates]
    SearchText: Optional[ValueString]
    SortCriteria: Optional[SortCriteria]
    MaxResults: Optional[PageSize]
    ResourceShareType: Optional[ResourceShareType]
    IncludeStatusDetails: Optional[BooleanNullable]


class SearchTablesResponse(TypedDict, total=False):
    NextToken: Optional[Token]
    TableList: Optional[TableList]


class StartBlueprintRunRequest(ServiceRequest):
    BlueprintName: OrchestrationNameString
    Parameters: Optional[BlueprintParameters]
    RoleArn: OrchestrationIAMRoleArn


class StartBlueprintRunResponse(TypedDict, total=False):
    RunId: Optional[IdString]


class StartColumnStatisticsTaskRunRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString
    ColumnNameList: Optional[ColumnNameList]
    Role: NameString
    SampleSize: Optional[SampleSizePercentage]
    CatalogID: Optional[NameString]
    SecurityConfiguration: Optional[NameString]


class StartColumnStatisticsTaskRunResponse(TypedDict, total=False):
    ColumnStatisticsTaskRunId: Optional[HashString]


class StartColumnStatisticsTaskRunScheduleRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString


class StartColumnStatisticsTaskRunScheduleResponse(TypedDict, total=False):
    pass


class StartCrawlerRequest(ServiceRequest):
    Name: NameString


class StartCrawlerResponse(TypedDict, total=False):
    pass


class StartCrawlerScheduleRequest(ServiceRequest):
    CrawlerName: NameString


class StartCrawlerScheduleResponse(TypedDict, total=False):
    pass


class StartDataQualityRuleRecommendationRunRequest(ServiceRequest):
    DataSource: DataSource
    Role: RoleString
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    CreatedRulesetName: Optional[NameString]
    DataQualitySecurityConfiguration: Optional[NameString]
    ClientToken: Optional[HashString]


class StartDataQualityRuleRecommendationRunResponse(TypedDict, total=False):
    RunId: Optional[HashString]


class StartDataQualityRulesetEvaluationRunRequest(ServiceRequest):
    DataSource: DataSource
    Role: RoleString
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    ClientToken: Optional[HashString]
    AdditionalRunOptions: Optional[DataQualityEvaluationRunAdditionalRunOptions]
    RulesetNames: RulesetNames
    AdditionalDataSources: Optional[DataSourceMap]


class StartDataQualityRulesetEvaluationRunResponse(TypedDict, total=False):
    RunId: Optional[HashString]


class StartExportLabelsTaskRunRequest(ServiceRequest):
    TransformId: HashString
    OutputS3Path: UriString


class StartExportLabelsTaskRunResponse(TypedDict, total=False):
    TaskRunId: Optional[HashString]


class StartImportLabelsTaskRunRequest(ServiceRequest):
    TransformId: HashString
    InputS3Path: UriString
    ReplaceAllLabels: Optional[ReplaceBoolean]


class StartImportLabelsTaskRunResponse(TypedDict, total=False):
    TaskRunId: Optional[HashString]


class StartJobRunRequest(ServiceRequest):
    JobName: NameString
    JobRunQueuingEnabled: Optional[NullableBoolean]
    JobRunId: Optional[IdString]
    Arguments: Optional[GenericMap]
    AllocatedCapacity: Optional[IntegerValue]
    Timeout: Optional[Timeout]
    MaxCapacity: Optional[NullableDouble]
    SecurityConfiguration: Optional[NameString]
    NotificationProperty: Optional[NotificationProperty]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    ExecutionClass: Optional[ExecutionClass]


class StartJobRunResponse(TypedDict, total=False):
    JobRunId: Optional[IdString]


class StartMLEvaluationTaskRunRequest(ServiceRequest):
    TransformId: HashString


class StartMLEvaluationTaskRunResponse(TypedDict, total=False):
    TaskRunId: Optional[HashString]


class StartMLLabelingSetGenerationTaskRunRequest(ServiceRequest):
    TransformId: HashString
    OutputS3Path: UriString


class StartMLLabelingSetGenerationTaskRunResponse(TypedDict, total=False):
    TaskRunId: Optional[HashString]


class StartTriggerRequest(ServiceRequest):
    Name: NameString


class StartTriggerResponse(TypedDict, total=False):
    Name: Optional[NameString]


class StartWorkflowRunRequest(ServiceRequest):
    Name: NameString
    RunProperties: Optional[WorkflowRunProperties]


class StartWorkflowRunResponse(TypedDict, total=False):
    RunId: Optional[IdString]


class StopColumnStatisticsTaskRunRequest(ServiceRequest):
    DatabaseName: DatabaseName
    TableName: NameString


class StopColumnStatisticsTaskRunResponse(TypedDict, total=False):
    pass


class StopColumnStatisticsTaskRunScheduleRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString


class StopColumnStatisticsTaskRunScheduleResponse(TypedDict, total=False):
    pass


class StopCrawlerRequest(ServiceRequest):
    Name: NameString


class StopCrawlerResponse(TypedDict, total=False):
    pass


class StopCrawlerScheduleRequest(ServiceRequest):
    CrawlerName: NameString


class StopCrawlerScheduleResponse(TypedDict, total=False):
    pass


class StopSessionRequest(ServiceRequest):
    Id: NameString
    RequestOrigin: Optional[OrchestrationNameString]


class StopSessionResponse(TypedDict, total=False):
    Id: Optional[NameString]


class StopTriggerRequest(ServiceRequest):
    Name: NameString


class StopTriggerResponse(TypedDict, total=False):
    Name: Optional[NameString]


class StopWorkflowRunRequest(ServiceRequest):
    Name: NameString
    RunId: IdString


class StopWorkflowRunResponse(TypedDict, total=False):
    pass


TagKeysList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    ResourceArn: GlueResourceArn
    TagsToAdd: TagsMap


class TagResourceResponse(TypedDict, total=False):
    pass


class TestConnectionInput(TypedDict, total=False):
    """A structure that is used to specify testing a connection to a service."""

    ConnectionType: ConnectionType
    ConnectionProperties: ConnectionProperties
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInput]


class TestConnectionRequest(ServiceRequest):
    ConnectionName: Optional[NameString]
    CatalogId: Optional[CatalogIdString]
    TestConnectionInput: Optional[TestConnectionInput]


class TestConnectionResponse(TypedDict, total=False):
    pass


class TriggerUpdate(TypedDict, total=False):
    """A structure used to provide information used to update a trigger. This
    object updates the previous trigger definition by overwriting it
    completely.
    """

    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Schedule: Optional[GenericString]
    Actions: Optional[ActionList]
    Predicate: Optional[Predicate]
    EventBatchingCondition: Optional[EventBatchingCondition]


class UntagResourceRequest(ServiceRequest):
    ResourceArn: GlueResourceArn
    TagsToRemove: TagKeysList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateBlueprintRequest(ServiceRequest):
    Name: OrchestrationNameString
    Description: Optional[Generic512CharString]
    BlueprintLocation: OrchestrationS3Location


class UpdateBlueprintResponse(TypedDict, total=False):
    Name: Optional[NameString]


class UpdateCatalogRequest(ServiceRequest):
    CatalogId: CatalogIdString
    CatalogInput: CatalogInput


class UpdateCatalogResponse(TypedDict, total=False):
    pass


class UpdateCsvClassifierRequest(TypedDict, total=False):
    """Specifies a custom CSV classifier to be updated."""

    Name: NameString
    Delimiter: Optional[CsvColumnDelimiter]
    QuoteSymbol: Optional[CsvQuoteSymbol]
    ContainsHeader: Optional[CsvHeaderOption]
    Header: Optional[CsvHeader]
    DisableValueTrimming: Optional[NullableBoolean]
    AllowSingleColumn: Optional[NullableBoolean]
    CustomDatatypeConfigured: Optional[NullableBoolean]
    CustomDatatypes: Optional[CustomDatatypes]
    Serde: Optional[CsvSerdeOption]


class UpdateJsonClassifierRequest(TypedDict, total=False):
    """Specifies a JSON classifier to be updated."""

    Name: NameString
    JsonPath: Optional[JsonPath]


class UpdateXMLClassifierRequest(TypedDict, total=False):
    """Specifies an XML classifier to be updated."""

    Name: NameString
    Classification: Optional[Classification]
    RowTag: Optional[RowTag]


class UpdateGrokClassifierRequest(TypedDict, total=False):
    """Specifies a grok classifier to update when passed to
    ``UpdateClassifier``.
    """

    Name: NameString
    Classification: Optional[Classification]
    GrokPattern: Optional[GrokPattern]
    CustomPatterns: Optional[CustomPatterns]


class UpdateClassifierRequest(ServiceRequest):
    GrokClassifier: Optional[UpdateGrokClassifierRequest]
    XMLClassifier: Optional[UpdateXMLClassifierRequest]
    JsonClassifier: Optional[UpdateJsonClassifierRequest]
    CsvClassifier: Optional[UpdateCsvClassifierRequest]


class UpdateClassifierResponse(TypedDict, total=False):
    pass


UpdateColumnStatisticsList = List[ColumnStatistics]


class UpdateColumnStatisticsForPartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionValues: ValueStringList
    ColumnStatisticsList: UpdateColumnStatisticsList


class UpdateColumnStatisticsForPartitionResponse(TypedDict, total=False):
    Errors: Optional[ColumnStatisticsErrors]


class UpdateColumnStatisticsForTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    ColumnStatisticsList: UpdateColumnStatisticsList


class UpdateColumnStatisticsForTableResponse(TypedDict, total=False):
    Errors: Optional[ColumnStatisticsErrors]


class UpdateColumnStatisticsTaskSettingsRequest(ServiceRequest):
    DatabaseName: NameString
    TableName: NameString
    Role: Optional[NameString]
    Schedule: Optional[CronExpression]
    ColumnNameList: Optional[ColumnNameList]
    SampleSize: Optional[SampleSizePercentage]
    CatalogID: Optional[NameString]
    SecurityConfiguration: Optional[NameString]


class UpdateColumnStatisticsTaskSettingsResponse(TypedDict, total=False):
    pass


class UpdateConnectionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    Name: NameString
    ConnectionInput: ConnectionInput


class UpdateConnectionResponse(TypedDict, total=False):
    pass


class UpdateCrawlerRequest(ServiceRequest):
    Name: NameString
    Role: Optional[Role]
    DatabaseName: Optional[DatabaseName]
    Description: Optional[DescriptionStringRemovable]
    Targets: Optional[CrawlerTargets]
    Schedule: Optional[CronExpression]
    Classifiers: Optional[ClassifierNameList]
    TablePrefix: Optional[TablePrefix]
    SchemaChangePolicy: Optional[SchemaChangePolicy]
    RecrawlPolicy: Optional[RecrawlPolicy]
    LineageConfiguration: Optional[LineageConfiguration]
    LakeFormationConfiguration: Optional[LakeFormationConfiguration]
    Configuration: Optional[CrawlerConfiguration]
    CrawlerSecurityConfiguration: Optional[CrawlerSecurityConfiguration]


class UpdateCrawlerResponse(TypedDict, total=False):
    pass


class UpdateCrawlerScheduleRequest(ServiceRequest):
    CrawlerName: NameString
    Schedule: Optional[CronExpression]


class UpdateCrawlerScheduleResponse(TypedDict, total=False):
    pass


class UpdateDataQualityRulesetRequest(ServiceRequest):
    Name: NameString
    Description: Optional[DescriptionString]
    Ruleset: Optional[DataQualityRulesetString]


class UpdateDataQualityRulesetResponse(TypedDict, total=False):
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Ruleset: Optional[DataQualityRulesetString]


class UpdateDatabaseRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    Name: NameString
    DatabaseInput: DatabaseInput


class UpdateDatabaseResponse(TypedDict, total=False):
    pass


class UpdateDevEndpointRequest(ServiceRequest):
    EndpointName: GenericString
    PublicKey: Optional[GenericString]
    AddPublicKeys: Optional[PublicKeysList]
    DeletePublicKeys: Optional[PublicKeysList]
    CustomLibraries: Optional[DevEndpointCustomLibraries]
    UpdateEtlLibraries: Optional[BooleanValue]
    DeleteArguments: Optional[StringList]
    AddArguments: Optional[MapValue]


class UpdateDevEndpointResponse(TypedDict, total=False):
    pass


class UpdateIntegrationResourcePropertyRequest(ServiceRequest):
    ResourceArn: String128
    SourceProcessingProperties: Optional[SourceProcessingProperties]
    TargetProcessingProperties: Optional[TargetProcessingProperties]


class UpdateIntegrationResourcePropertyResponse(TypedDict, total=False):
    ResourceArn: Optional[String128]
    SourceProcessingProperties: Optional[SourceProcessingProperties]
    TargetProcessingProperties: Optional[TargetProcessingProperties]


class UpdateIntegrationTablePropertiesRequest(ServiceRequest):
    ResourceArn: String128
    TableName: String128
    SourceTableConfig: Optional[SourceTableConfig]
    TargetTableConfig: Optional[TargetTableConfig]


class UpdateIntegrationTablePropertiesResponse(TypedDict, total=False):
    pass


class UpdateJobFromSourceControlRequest(ServiceRequest):
    JobName: Optional[NameString]
    Provider: Optional[SourceControlProvider]
    RepositoryName: Optional[NameString]
    RepositoryOwner: Optional[NameString]
    BranchName: Optional[NameString]
    Folder: Optional[NameString]
    CommitId: Optional[CommitIdString]
    AuthStrategy: Optional[SourceControlAuthStrategy]
    AuthToken: Optional[AuthTokenString]


class UpdateJobFromSourceControlResponse(TypedDict, total=False):
    JobName: Optional[NameString]


class UpdateJobRequest(ServiceRequest):
    JobName: NameString
    JobUpdate: JobUpdate


class UpdateJobResponse(TypedDict, total=False):
    JobName: Optional[NameString]


class UpdateMLTransformRequest(ServiceRequest):
    TransformId: HashString
    Name: Optional[NameString]
    Description: Optional[DescriptionString]
    Parameters: Optional[TransformParameters]
    Role: Optional[RoleString]
    GlueVersion: Optional[GlueVersionString]
    MaxCapacity: Optional[NullableDouble]
    WorkerType: Optional[WorkerType]
    NumberOfWorkers: Optional[NullableInteger]
    Timeout: Optional[Timeout]
    MaxRetries: Optional[NullableInteger]


class UpdateMLTransformResponse(TypedDict, total=False):
    TransformId: Optional[HashString]


class UpdatePartitionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableName: NameString
    PartitionValueList: BoundedPartitionValueList
    PartitionInput: PartitionInput


class UpdatePartitionResponse(TypedDict, total=False):
    pass


class UpdateRegistryInput(ServiceRequest):
    RegistryId: RegistryId
    Description: DescriptionString


class UpdateRegistryResponse(TypedDict, total=False):
    RegistryName: Optional[SchemaRegistryNameString]
    RegistryArn: Optional[GlueResourceArn]


class UpdateSchemaInput(ServiceRequest):
    SchemaId: SchemaId
    SchemaVersionNumber: Optional[SchemaVersionNumber]
    Compatibility: Optional[Compatibility]
    Description: Optional[DescriptionString]


class UpdateSchemaResponse(TypedDict, total=False):
    SchemaArn: Optional[GlueResourceArn]
    SchemaName: Optional[SchemaRegistryNameString]
    RegistryName: Optional[SchemaRegistryNameString]


class UpdateSourceControlFromJobRequest(ServiceRequest):
    JobName: Optional[NameString]
    Provider: Optional[SourceControlProvider]
    RepositoryName: Optional[NameString]
    RepositoryOwner: Optional[NameString]
    BranchName: Optional[NameString]
    Folder: Optional[NameString]
    CommitId: Optional[CommitIdString]
    AuthStrategy: Optional[SourceControlAuthStrategy]
    AuthToken: Optional[AuthTokenString]


class UpdateSourceControlFromJobResponse(TypedDict, total=False):
    JobName: Optional[NameString]


class UpdateTableOptimizerRequest(ServiceRequest):
    CatalogId: CatalogIdString
    DatabaseName: NameString
    TableName: NameString
    Type: TableOptimizerType
    TableOptimizerConfiguration: TableOptimizerConfiguration


class UpdateTableOptimizerResponse(TypedDict, total=False):
    pass


class UpdateTableRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    TableInput: TableInput
    SkipArchive: Optional[BooleanNullable]
    TransactionId: Optional[TransactionIdString]
    VersionId: Optional[VersionString]
    ViewUpdateAction: Optional[ViewUpdateAction]
    Force: Optional[Boolean]


class UpdateTableResponse(TypedDict, total=False):
    pass


class UpdateTriggerRequest(ServiceRequest):
    Name: NameString
    TriggerUpdate: TriggerUpdate


class UpdateTriggerResponse(TypedDict, total=False):
    Trigger: Optional[Trigger]


class UpdateUsageProfileRequest(ServiceRequest):
    Name: NameString
    Description: Optional[DescriptionString]
    Configuration: ProfileConfiguration


class UpdateUsageProfileResponse(TypedDict, total=False):
    Name: Optional[NameString]


class UpdateUserDefinedFunctionRequest(ServiceRequest):
    CatalogId: Optional[CatalogIdString]
    DatabaseName: NameString
    FunctionName: NameString
    FunctionInput: UserDefinedFunctionInput


class UpdateUserDefinedFunctionResponse(TypedDict, total=False):
    pass


class UpdateWorkflowRequest(ServiceRequest):
    Name: NameString
    Description: Optional[WorkflowDescriptionString]
    DefaultRunProperties: Optional[WorkflowRunProperties]
    MaxConcurrentRuns: Optional[NullableInteger]


class UpdateWorkflowResponse(TypedDict, total=False):
    Name: Optional[NameString]


class GlueApi:
    service = "glue"
    version = "2017-03-31"

    @handler("BatchCreatePartition")
    def batch_create_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_input_list: PartitionInputList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> BatchCreatePartitionResponse:
        """Creates one or more partitions in a batch operation.

        :param database_name: The name of the metadata database in which the partition is to be
        created.
        :param table_name: The name of the metadata table in which the partition is to be created.
        :param partition_input_list: A list of ``PartitionInput`` structures that define the partitions to be
        created.
        :param catalog_id: The ID of the catalog in which the partition is to be created.
        :returns: BatchCreatePartitionResponse
        :raises InvalidInputException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("BatchDeleteConnection")
    def batch_delete_connection(
        self,
        context: RequestContext,
        connection_name_list: DeleteConnectionNameList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> BatchDeleteConnectionResponse:
        """Deletes a list of connection definitions from the Data Catalog.

        :param connection_name_list: A list of names of the connections to delete.
        :param catalog_id: The ID of the Data Catalog in which the connections reside.
        :returns: BatchDeleteConnectionResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("BatchDeletePartition")
    def batch_delete_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partitions_to_delete: BatchDeletePartitionValueList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> BatchDeletePartitionResponse:
        """Deletes one or more partitions in a batch operation.

        :param database_name: The name of the catalog database in which the table in question resides.
        :param table_name: The name of the table that contains the partitions to be deleted.
        :param partitions_to_delete: A list of ``PartitionInput`` structures that define the partitions to be
        deleted.
        :param catalog_id: The ID of the Data Catalog where the partition to be deleted resides.
        :returns: BatchDeletePartitionResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("BatchDeleteTable")
    def batch_delete_table(
        self,
        context: RequestContext,
        database_name: NameString,
        tables_to_delete: BatchDeleteTableNameList,
        catalog_id: CatalogIdString | None = None,
        transaction_id: TransactionIdString | None = None,
        **kwargs,
    ) -> BatchDeleteTableResponse:
        """Deletes multiple tables at once.

        After completing this operation, you no longer have access to the table
        versions and partitions that belong to the deleted table. Glue deletes
        these "orphaned" resources asynchronously in a timely manner, at the
        discretion of the service.

        To ensure the immediate deletion of all related resources, before
        calling ``BatchDeleteTable``, use ``DeleteTableVersion`` or
        ``BatchDeleteTableVersion``, and ``DeletePartition`` or
        ``BatchDeletePartition``, to delete any resources that belong to the
        table.

        :param database_name: The name of the catalog database in which the tables to delete reside.
        :param tables_to_delete: A list of the table to delete.
        :param catalog_id: The ID of the Data Catalog where the table resides.
        :param transaction_id: The transaction ID at which to delete the table contents.
        :returns: BatchDeleteTableResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ResourceNotReadyException:
        """
        raise NotImplementedError

    @handler("BatchDeleteTableVersion")
    def batch_delete_table_version(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        version_ids: BatchDeleteTableVersionList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> BatchDeleteTableVersionResponse:
        """Deletes a specified batch of versions of a table.

        :param database_name: The database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param version_ids: A list of the IDs of versions to be deleted.
        :param catalog_id: The ID of the Data Catalog where the tables reside.
        :returns: BatchDeleteTableVersionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("BatchGetBlueprints")
    def batch_get_blueprints(
        self,
        context: RequestContext,
        names: BatchGetBlueprintNames,
        include_blueprint: NullableBoolean | None = None,
        include_parameter_spec: NullableBoolean | None = None,
        **kwargs,
    ) -> BatchGetBlueprintsResponse:
        """Retrieves information about a list of blueprints.

        :param names: A list of blueprint names.
        :param include_blueprint: Specifies whether or not to include the blueprint in the response.
        :param include_parameter_spec: Specifies whether or not to include the parameters, as a JSON string,
        for the blueprint in the response.
        :returns: BatchGetBlueprintsResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetCrawlers")
    def batch_get_crawlers(
        self, context: RequestContext, crawler_names: CrawlerNameList, **kwargs
    ) -> BatchGetCrawlersResponse:
        """Returns a list of resource metadata for a given list of crawler names.
        After calling the ``ListCrawlers`` operation, you can call this
        operation to access the data to which you have been granted permissions.
        This operation supports all IAM permissions, including permission
        conditions that uses tags.

        :param crawler_names: A list of crawler names, which might be the names returned from the
        ``ListCrawlers`` operation.
        :returns: BatchGetCrawlersResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("BatchGetCustomEntityTypes")
    def batch_get_custom_entity_types(
        self, context: RequestContext, names: CustomEntityTypeNames, **kwargs
    ) -> BatchGetCustomEntityTypesResponse:
        """Retrieves the details for the custom patterns specified by a list of
        names.

        :param names: A list of names of the custom patterns that you want to retrieve.
        :returns: BatchGetCustomEntityTypesResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("BatchGetDataQualityResult")
    def batch_get_data_quality_result(
        self, context: RequestContext, result_ids: DataQualityResultIds, **kwargs
    ) -> BatchGetDataQualityResultResponse:
        """Retrieves a list of data quality results for the specified result IDs.

        :param result_ids: A list of unique result IDs for the data quality results.
        :returns: BatchGetDataQualityResultResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("BatchGetDevEndpoints")
    def batch_get_dev_endpoints(
        self, context: RequestContext, dev_endpoint_names: DevEndpointNames, **kwargs
    ) -> BatchGetDevEndpointsResponse:
        """Returns a list of resource metadata for a given list of development
        endpoint names. After calling the ``ListDevEndpoints`` operation, you
        can call this operation to access the data to which you have been
        granted permissions. This operation supports all IAM permissions,
        including permission conditions that uses tags.

        :param dev_endpoint_names: The list of ``DevEndpoint`` names, which might be the names returned
        from the ``ListDevEndpoint`` operation.
        :returns: BatchGetDevEndpointsResponse
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetJobs")
    def batch_get_jobs(
        self, context: RequestContext, job_names: JobNameList, **kwargs
    ) -> BatchGetJobsResponse:
        """Returns a list of resource metadata for a given list of job names. After
        calling the ``ListJobs`` operation, you can call this operation to
        access the data to which you have been granted permissions. This
        operation supports all IAM permissions, including permission conditions
        that uses tags.

        :param job_names: A list of job names, which might be the names returned from the
        ``ListJobs`` operation.
        :returns: BatchGetJobsResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetPartition")
    def batch_get_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partitions_to_get: BatchGetPartitionValueList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> BatchGetPartitionResponse:
        """Retrieves partitions in a batch request.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param partitions_to_get: A list of partition values identifying the partitions to retrieve.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: BatchGetPartitionResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises GlueEncryptionException:
        :raises InvalidStateException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("BatchGetTableOptimizer")
    def batch_get_table_optimizer(
        self, context: RequestContext, entries: BatchGetTableOptimizerEntries, **kwargs
    ) -> BatchGetTableOptimizerResponse:
        """Returns the configuration for the specified table optimizers.

        :param entries: A list of ``BatchGetTableOptimizerEntry`` objects specifying the table
        optimizers to retrieve.
        :returns: BatchGetTableOptimizerResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("BatchGetTriggers")
    def batch_get_triggers(
        self, context: RequestContext, trigger_names: TriggerNameList, **kwargs
    ) -> BatchGetTriggersResponse:
        """Returns a list of resource metadata for a given list of trigger names.
        After calling the ``ListTriggers`` operation, you can call this
        operation to access the data to which you have been granted permissions.
        This operation supports all IAM permissions, including permission
        conditions that uses tags.

        :param trigger_names: A list of trigger names, which may be the names returned from the
        ``ListTriggers`` operation.
        :returns: BatchGetTriggersResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchGetWorkflows")
    def batch_get_workflows(
        self,
        context: RequestContext,
        names: WorkflowNames,
        include_graph: NullableBoolean | None = None,
        **kwargs,
    ) -> BatchGetWorkflowsResponse:
        """Returns a list of resource metadata for a given list of workflow names.
        After calling the ``ListWorkflows`` operation, you can call this
        operation to access the data to which you have been granted permissions.
        This operation supports all IAM permissions, including permission
        conditions that uses tags.

        :param names: A list of workflow names, which may be the names returned from the
        ``ListWorkflows`` operation.
        :param include_graph: Specifies whether to include a graph when returning the workflow
        resource metadata.
        :returns: BatchGetWorkflowsResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("BatchPutDataQualityStatisticAnnotation")
    def batch_put_data_quality_statistic_annotation(
        self,
        context: RequestContext,
        inclusion_annotations: InclusionAnnotationList,
        client_token: HashString | None = None,
        **kwargs,
    ) -> BatchPutDataQualityStatisticAnnotationResponse:
        """Annotate datapoints over time for a specific data quality statistic.

        :param inclusion_annotations: A list of ``DatapointInclusionAnnotation``'s.
        :param client_token: Client Token.
        :returns: BatchPutDataQualityStatisticAnnotationResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("BatchStopJobRun")
    def batch_stop_job_run(
        self,
        context: RequestContext,
        job_name: NameString,
        job_run_ids: BatchStopJobRunJobRunIdList,
        **kwargs,
    ) -> BatchStopJobRunResponse:
        """Stops one or more job runs for a specified job definition.

        :param job_name: The name of the job definition for which to stop job runs.
        :param job_run_ids: A list of the ``JobRunIds`` that should be stopped for that job
        definition.
        :returns: BatchStopJobRunResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("BatchUpdatePartition")
    def batch_update_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        entries: BatchUpdatePartitionRequestEntryList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> BatchUpdatePartitionResponse:
        """Updates one or more partitions in a batch operation.

        :param database_name: The name of the metadata database in which the partition is to be
        updated.
        :param table_name: The name of the metadata table in which the partition is to be updated.
        :param entries: A list of up to 100 ``BatchUpdatePartitionRequestEntry`` objects to
        update.
        :param catalog_id: The ID of the catalog in which the partition is to be updated.
        :returns: BatchUpdatePartitionResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("CancelDataQualityRuleRecommendationRun")
    def cancel_data_quality_rule_recommendation_run(
        self, context: RequestContext, run_id: HashString, **kwargs
    ) -> CancelDataQualityRuleRecommendationRunResponse:
        """Cancels the specified recommendation run that was being used to generate
        rules.

        :param run_id: The unique run identifier associated with this run.
        :returns: CancelDataQualityRuleRecommendationRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("CancelDataQualityRulesetEvaluationRun")
    def cancel_data_quality_ruleset_evaluation_run(
        self, context: RequestContext, run_id: HashString, **kwargs
    ) -> CancelDataQualityRulesetEvaluationRunResponse:
        """Cancels a run where a ruleset is being evaluated against a data source.

        :param run_id: The unique run identifier associated with this run.
        :returns: CancelDataQualityRulesetEvaluationRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("CancelMLTaskRun")
    def cancel_ml_task_run(
        self, context: RequestContext, transform_id: HashString, task_run_id: HashString, **kwargs
    ) -> CancelMLTaskRunResponse:
        """Cancels (stops) a task run. Machine learning task runs are asynchronous
        tasks that Glue runs on your behalf as part of various machine learning
        workflows. You can cancel a machine learning task run at any time by
        calling ``CancelMLTaskRun`` with a task run's parent transform's
        ``TransformID`` and the task run's ``TaskRunId``.

        :param transform_id: The unique identifier of the machine learning transform.
        :param task_run_id: A unique identifier for the task run.
        :returns: CancelMLTaskRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("CancelStatement")
    def cancel_statement(
        self,
        context: RequestContext,
        session_id: NameString,
        id: IntegerValue,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> CancelStatementResponse:
        """Cancels the statement.

        :param session_id: The Session ID of the statement to be cancelled.
        :param id: The ID of the statement to be cancelled.
        :param request_origin: The origin of the request to cancel the statement.
        :returns: CancelStatementResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises IllegalSessionStateException:
        """
        raise NotImplementedError

    @handler("CheckSchemaVersionValidity")
    def check_schema_version_validity(
        self,
        context: RequestContext,
        data_format: DataFormat,
        schema_definition: SchemaDefinitionString,
        **kwargs,
    ) -> CheckSchemaVersionValidityResponse:
        """Validates the supplied schema. This call has no side effects, it simply
        validates using the supplied schema using ``DataFormat`` as the format.
        Since it does not take a schema set name, no compatibility checks are
        performed.

        :param data_format: The data format of the schema definition.
        :param schema_definition: The definition of the schema that has to be validated.
        :returns: CheckSchemaVersionValidityResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("CreateBlueprint")
    def create_blueprint(
        self,
        context: RequestContext,
        name: OrchestrationNameString,
        blueprint_location: OrchestrationS3Location,
        description: Generic512CharString | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateBlueprintResponse:
        """Registers a blueprint with Glue.

        :param name: The name of the blueprint.
        :param blueprint_location: Specifies a path in Amazon S3 where the blueprint is published.
        :param description: A description of the blueprint.
        :param tags: The tags to be applied to this blueprint.
        :returns: CreateBlueprintResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateCatalog")
    def create_catalog(
        self,
        context: RequestContext,
        name: CatalogNameString,
        catalog_input: CatalogInput,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateCatalogResponse:
        """Creates a new catalog in the Glue Data Catalog.

        :param name: The name of the catalog to create.
        :param catalog_input: A ``CatalogInput`` object that defines the metadata for the catalog.
        :param tags: A map array of key-value pairs, not more than 50 pairs.
        :returns: CreateCatalogResponse
        :raises InvalidInputException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ConcurrentModificationException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises FederatedResourceAlreadyExistsException:
        :raises FederationSourceException:
        """
        raise NotImplementedError

    @handler("CreateClassifier")
    def create_classifier(
        self,
        context: RequestContext,
        grok_classifier: CreateGrokClassifierRequest | None = None,
        xml_classifier: CreateXMLClassifierRequest | None = None,
        json_classifier: CreateJsonClassifierRequest | None = None,
        csv_classifier: CreateCsvClassifierRequest | None = None,
        **kwargs,
    ) -> CreateClassifierResponse:
        """Creates a classifier in the user's account. This can be a
        ``GrokClassifier``, an ``XMLClassifier``, a ``JsonClassifier``, or a
        ``CsvClassifier``, depending on which field of the request is present.

        :param grok_classifier: A ``GrokClassifier`` object specifying the classifier to create.
        :param xml_classifier: An ``XMLClassifier`` object specifying the classifier to create.
        :param json_classifier: A ``JsonClassifier`` object specifying the classifier to create.
        :param csv_classifier: A ``CsvClassifier`` object specifying the classifier to create.
        :returns: CreateClassifierResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("CreateColumnStatisticsTaskSettings")
    def create_column_statistics_task_settings(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        role: NameString,
        schedule: CronExpression | None = None,
        column_name_list: ColumnNameList | None = None,
        sample_size: SampleSizePercentage | None = None,
        catalog_id: NameString | None = None,
        security_configuration: NameString | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateColumnStatisticsTaskSettingsResponse:
        """Creates settings for a column statistics task.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table for which to generate column statistics.
        :param role: The role used for running the column statistics.
        :param schedule: A schedule for running the column statistics, specified in CRON syntax.
        :param column_name_list: A list of column names for which to run statistics.
        :param sample_size: The percentage of data to sample.
        :param catalog_id: The ID of the Data Catalog in which the database resides.
        :param security_configuration: Name of the security configuration that is used to encrypt CloudWatch
        logs.
        :param tags: A map of tags.
        :returns: CreateColumnStatisticsTaskSettingsResponse
        :raises AlreadyExistsException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ColumnStatisticsTaskRunningException:
        """
        raise NotImplementedError

    @handler("CreateConnection")
    def create_connection(
        self,
        context: RequestContext,
        connection_input: ConnectionInput,
        catalog_id: CatalogIdString | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateConnectionResponse:
        """Creates a connection definition in the Data Catalog.

        Connections used for creating federated resources require the IAM
        ``glue:PassConnection`` permission.

        :param connection_input: A ``ConnectionInput`` object defining the connection to create.
        :param catalog_id: The ID of the Data Catalog in which to create the connection.
        :param tags: The tags you assign to the connection.
        :returns: CreateConnectionResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("CreateCrawler")
    def create_crawler(
        self,
        context: RequestContext,
        name: NameString,
        role: Role,
        targets: CrawlerTargets,
        database_name: DatabaseName | None = None,
        description: DescriptionString | None = None,
        schedule: CronExpression | None = None,
        classifiers: ClassifierNameList | None = None,
        table_prefix: TablePrefix | None = None,
        schema_change_policy: SchemaChangePolicy | None = None,
        recrawl_policy: RecrawlPolicy | None = None,
        lineage_configuration: LineageConfiguration | None = None,
        lake_formation_configuration: LakeFormationConfiguration | None = None,
        configuration: CrawlerConfiguration | None = None,
        crawler_security_configuration: CrawlerSecurityConfiguration | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateCrawlerResponse:
        """Creates a new crawler with specified targets, role, configuration, and
        optional schedule. At least one crawl target must be specified, in the
        ``s3Targets`` field, the ``jdbcTargets`` field, or the
        ``DynamoDBTargets`` field.

        :param name: Name of the new crawler.
        :param role: The IAM role or Amazon Resource Name (ARN) of an IAM role used by the
        new crawler to access customer resources.
        :param targets: A list of collection of targets to crawl.
        :param database_name: The Glue database where results are written, such as:
        ``arn:aws:daylight:us-east-1::database/sometable/*``.
        :param description: A description of the new crawler.
        :param schedule: A ``cron`` expression used to specify the schedule (see `Time-Based
        Schedules for Jobs and
        Crawlers <https://docs.
        :param classifiers: A list of custom classifiers that the user has registered.
        :param table_prefix: The table prefix used for catalog tables that are created.
        :param schema_change_policy: The policy for the crawler's update and deletion behavior.
        :param recrawl_policy: A policy that specifies whether to crawl the entire dataset again, or to
        crawl only folders that were added since the last crawler run.
        :param lineage_configuration: Specifies data lineage configuration settings for the crawler.
        :param lake_formation_configuration: Specifies Lake Formation configuration settings for the crawler.
        :param configuration: Crawler configuration information.
        :param crawler_security_configuration: The name of the ``SecurityConfiguration`` structure to be used by this
        crawler.
        :param tags: The tags to use with this crawler request.
        :returns: CreateCrawlerResponse
        :raises InvalidInputException:
        :raises AlreadyExistsException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateCustomEntityType")
    def create_custom_entity_type(
        self,
        context: RequestContext,
        name: NameString,
        regex_string: NameString,
        context_words: ContextWords | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateCustomEntityTypeResponse:
        """Creates a custom pattern that is used to detect sensitive data across
        the columns and rows of your structured data.

        Each custom pattern you create specifies a regular expression and an
        optional list of context words. If no context words are passed only a
        regular expression is checked.

        :param name: A name for the custom pattern that allows it to be retrieved or deleted
        later.
        :param regex_string: A regular expression string that is used for detecting sensitive data in
        a custom pattern.
        :param context_words: A list of context words.
        :param tags: A list of tags applied to the custom entity type.
        :returns: CreateCustomEntityTypeResponse
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises IdempotentParameterMismatchException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateDataQualityRuleset")
    def create_data_quality_ruleset(
        self,
        context: RequestContext,
        name: NameString,
        ruleset: DataQualityRulesetString,
        description: DescriptionString | None = None,
        tags: TagsMap | None = None,
        target_table: DataQualityTargetTable | None = None,
        data_quality_security_configuration: NameString | None = None,
        client_token: HashString | None = None,
        **kwargs,
    ) -> CreateDataQualityRulesetResponse:
        """Creates a data quality ruleset with DQDL rules applied to a specified
        Glue table.

        You create the ruleset using the Data Quality Definition Language
        (DQDL). For more information, see the Glue developer guide.

        :param name: A unique name for the data quality ruleset.
        :param ruleset: A Data Quality Definition Language (DQDL) ruleset.
        :param description: A description of the data quality ruleset.
        :param tags: A list of tags applied to the data quality ruleset.
        :param target_table: A target table associated with the data quality ruleset.
        :param data_quality_security_configuration: The name of the security configuration created with the data quality
        encryption option.
        :param client_token: Used for idempotency and is recommended to be set to a random ID (such
        as a UUID) to avoid creating or starting multiple instances of the same
        resource.
        :returns: CreateDataQualityRulesetResponse
        :raises InvalidInputException:
        :raises AlreadyExistsException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateDatabase")
    def create_database(
        self,
        context: RequestContext,
        database_input: DatabaseInput,
        catalog_id: CatalogIdString | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateDatabaseResponse:
        """Creates a new database in a Data Catalog.

        :param database_input: The metadata for the database.
        :param catalog_id: The ID of the Data Catalog in which to create the database.
        :param tags: The tags you assign to the database.
        :returns: CreateDatabaseResponse
        :raises InvalidInputException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ConcurrentModificationException:
        :raises FederatedResourceAlreadyExistsException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("CreateDevEndpoint")
    def create_dev_endpoint(
        self,
        context: RequestContext,
        endpoint_name: GenericString,
        role_arn: RoleArn,
        security_group_ids: StringList | None = None,
        subnet_id: GenericString | None = None,
        public_key: GenericString | None = None,
        public_keys: PublicKeysList | None = None,
        number_of_nodes: IntegerValue | None = None,
        worker_type: WorkerType | None = None,
        glue_version: GlueVersionString | None = None,
        number_of_workers: NullableInteger | None = None,
        extra_python_libs_s3_path: GenericString | None = None,
        extra_jars_s3_path: GenericString | None = None,
        security_configuration: NameString | None = None,
        tags: TagsMap | None = None,
        arguments: MapValue | None = None,
        **kwargs,
    ) -> CreateDevEndpointResponse:
        """Creates a new development endpoint.

        :param endpoint_name: The name to be assigned to the new ``DevEndpoint``.
        :param role_arn: The IAM role for the ``DevEndpoint``.
        :param security_group_ids: Security group IDs for the security groups to be used by the new
        ``DevEndpoint``.
        :param subnet_id: The subnet ID for the new ``DevEndpoint`` to use.
        :param public_key: The public key to be used by this ``DevEndpoint`` for authentication.
        :param public_keys: A list of public keys to be used by the development endpoints for
        authentication.
        :param number_of_nodes: The number of Glue Data Processing Units (DPUs) to allocate to this
        ``DevEndpoint``.
        :param worker_type: The type of predefined worker that is allocated to the development
        endpoint.
        :param glue_version: Glue version determines the versions of Apache Spark and Python that
        Glue supports.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated to
        the development endpoint.
        :param extra_python_libs_s3_path: The paths to one or more Python libraries in an Amazon S3 bucket that
        should be loaded in your ``DevEndpoint``.
        :param extra_jars_s3_path: The path to one or more Java ``.
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this
        ``DevEndpoint``.
        :param tags: The tags to use with this DevEndpoint.
        :param arguments: A map of arguments used to configure the ``DevEndpoint``.
        :returns: CreateDevEndpointResponse
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises IdempotentParameterMismatchException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises ValidationException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateIntegration")
    def create_integration(
        self,
        context: RequestContext,
        integration_name: String128,
        source_arn: String128,
        target_arn: String128,
        description: IntegrationDescription | None = None,
        data_filter: String2048 | None = None,
        kms_key_id: String2048 | None = None,
        additional_encryption_context: IntegrationAdditionalEncryptionContextMap | None = None,
        tags: IntegrationTagsList | None = None,
        integration_config: IntegrationConfig | None = None,
        **kwargs,
    ) -> CreateIntegrationResponse:
        """Creates a Zero-ETL integration in the caller's account between two
        resources with Amazon Resource Names (ARNs): the ``SourceArn`` and
        ``TargetArn``.

        :param integration_name: A unique name for an integration in Glue.
        :param source_arn: The ARN of the source resource for the integration.
        :param target_arn: The ARN of the target resource for the integration.
        :param description: A description of the integration.
        :param data_filter: Selects source tables for the integration using Maxwell filter syntax.
        :param kms_key_id: The ARN of a KMS key used for encrypting the channel.
        :param additional_encryption_context: An optional set of non-secret key–value pairs that contains additional
        contextual information for encryption.
        :param tags: Metadata assigned to the resource consisting of a list of key-value
        pairs.
        :param integration_config: The configuration settings.
        :returns: CreateIntegrationResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises IntegrationConflictOperationFault:
        :raises IntegrationQuotaExceededFault:
        :raises KMSKeyNotAccessibleFault:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises ConflictException:
        :raises ResourceNumberLimitExceededException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("CreateIntegrationResourceProperty")
    def create_integration_resource_property(
        self,
        context: RequestContext,
        resource_arn: String128,
        source_processing_properties: SourceProcessingProperties | None = None,
        target_processing_properties: TargetProcessingProperties | None = None,
        **kwargs,
    ) -> CreateIntegrationResourcePropertyResponse:
        """This API can be used for setting up the ``ResourceProperty`` of the Glue
        connection (for the source) or Glue database ARN (for the target). These
        properties can include the role to access the connection or database. To
        set both source and target properties the same API needs to be invoked
        with the Glue connection ARN as ``ResourceArn`` with
        ``SourceProcessingProperties`` and the Glue database ARN as
        ``ResourceArn`` with ``TargetProcessingProperties`` respectively.

        :param resource_arn: The connection ARN of the source, or the database ARN of the target.
        :param source_processing_properties: The resource properties associated with the integration source.
        :param target_processing_properties: The resource properties associated with the integration target.
        :returns: CreateIntegrationResourcePropertyResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("CreateIntegrationTableProperties")
    def create_integration_table_properties(
        self,
        context: RequestContext,
        resource_arn: String128,
        table_name: String128,
        source_table_config: SourceTableConfig | None = None,
        target_table_config: TargetTableConfig | None = None,
        **kwargs,
    ) -> CreateIntegrationTablePropertiesResponse:
        """This API is used to provide optional override properties for the the
        tables that need to be replicated. These properties can include
        properties for filtering and partitioning for the source and target
        tables. To set both source and target properties the same API need to be
        invoked with the Glue connection ARN as ``ResourceArn`` with
        ``SourceTableConfig``, and the Glue database ARN as ``ResourceArn`` with
        ``TargetTableConfig`` respectively.

        :param resource_arn: The Amazon Resource Name (ARN) of the target table for which to create
        integration table properties.
        :param table_name: The name of the table to be replicated.
        :param source_table_config: A structure for the source table configuration.
        :param target_table_config: A structure for the target table configuration.
        :returns: CreateIntegrationTablePropertiesResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("CreateJob")
    def create_job(
        self,
        context: RequestContext,
        name: NameString,
        role: RoleString,
        command: JobCommand,
        job_mode: JobMode | None = None,
        job_run_queuing_enabled: NullableBoolean | None = None,
        description: DescriptionString | None = None,
        log_uri: UriString | None = None,
        execution_property: ExecutionProperty | None = None,
        default_arguments: GenericMap | None = None,
        non_overridable_arguments: GenericMap | None = None,
        connections: ConnectionsList | None = None,
        max_retries: MaxRetries | None = None,
        allocated_capacity: IntegerValue | None = None,
        timeout: Timeout | None = None,
        max_capacity: NullableDouble | None = None,
        security_configuration: NameString | None = None,
        tags: TagsMap | None = None,
        notification_property: NotificationProperty | None = None,
        glue_version: GlueVersionString | None = None,
        number_of_workers: NullableInteger | None = None,
        worker_type: WorkerType | None = None,
        code_gen_configuration_nodes: CodeGenConfigurationNodes | None = None,
        execution_class: ExecutionClass | None = None,
        source_control_details: SourceControlDetails | None = None,
        maintenance_window: MaintenanceWindow | None = None,
        **kwargs,
    ) -> CreateJobResponse:
        """Creates a new job definition.

        :param name: The name you assign to this job definition.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role associated with
        this job.
        :param command: The ``JobCommand`` that runs this job.
        :param job_mode: A mode that describes how a job was created.
        :param job_run_queuing_enabled: Specifies whether job run queuing is enabled for the job runs for this
        job.
        :param description: Description of the job being defined.
        :param log_uri: This field is reserved for future use.
        :param execution_property: An ``ExecutionProperty`` specifying the maximum number of concurrent
        runs allowed for this job.
        :param default_arguments: The default arguments for every run of this job, specified as name-value
        pairs.
        :param non_overridable_arguments: Arguments for this job that are not overridden when providing job
        arguments in a job run, specified as name-value pairs.
        :param connections: The connections used for this job.
        :param max_retries: The maximum number of times to retry this job if it fails.
        :param allocated_capacity: This parameter is deprecated.
        :param timeout: The job timeout in minutes.
        :param max_capacity: For Glue version 1.
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this
        job.
        :param tags: The tags to use with this job.
        :param notification_property: Specifies configuration properties of a job notification.
        :param glue_version: In Spark jobs, ``GlueVersion`` determines the versions of Apache Spark
        and Python that Glue available in a job.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated
        when a job runs.
        :param worker_type: The type of predefined worker that is allocated when a job runs.
        :param code_gen_configuration_nodes: The representation of a directed acyclic graph on which both the Glue
        Studio visual component and Glue Studio code generation is based.
        :param execution_class: Indicates whether the job is run with a standard or flexible execution
        class.
        :param source_control_details: The details for a source control configuration for a job, allowing
        synchronization of job artifacts to or from a remote repository.
        :param maintenance_window: This field specifies a day of the week and hour for a maintenance window
        for streaming jobs.
        :returns: CreateJobResponse
        :raises InvalidInputException:
        :raises IdempotentParameterMismatchException:
        :raises AlreadyExistsException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("CreateMLTransform")
    def create_ml_transform(
        self,
        context: RequestContext,
        name: NameString,
        input_record_tables: GlueTables,
        parameters: TransformParameters,
        role: RoleString,
        description: DescriptionString | None = None,
        glue_version: GlueVersionString | None = None,
        max_capacity: NullableDouble | None = None,
        worker_type: WorkerType | None = None,
        number_of_workers: NullableInteger | None = None,
        timeout: Timeout | None = None,
        max_retries: NullableInteger | None = None,
        tags: TagsMap | None = None,
        transform_encryption: TransformEncryption | None = None,
        **kwargs,
    ) -> CreateMLTransformResponse:
        """Creates an Glue machine learning transform. This operation creates the
        transform and all the necessary parameters to train it.

        Call this operation as the first step in the process of using a machine
        learning transform (such as the ``FindMatches`` transform) for
        deduplicating data. You can provide an optional ``Description``, in
        addition to the parameters that you want to use for your algorithm.

        You must also specify certain parameters for the tasks that Glue runs on
        your behalf as part of learning from your data and creating a
        high-quality machine learning transform. These parameters include
        ``Role``, and optionally, ``AllocatedCapacity``, ``Timeout``, and
        ``MaxRetries``. For more information, see
        `Jobs <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html>`__.

        :param name: The unique name that you give the transform when you create it.
        :param input_record_tables: A list of Glue table definitions used by the transform.
        :param parameters: The algorithmic parameters that are specific to the transform type used.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role with the required
        permissions.
        :param description: A description of the machine learning transform that is being defined.
        :param glue_version: This value determines which version of Glue this machine learning
        transform is compatible with.
        :param max_capacity: The number of Glue data processing units (DPUs) that are allocated to
        task runs for this transform.
        :param worker_type: The type of predefined worker that is allocated when this task runs.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated
        when this task runs.
        :param timeout: The timeout of the task run for this transform in minutes.
        :param max_retries: The maximum number of times to retry a task for this transform after a
        task run fails.
        :param tags: The tags to use with this machine learning transform.
        :param transform_encryption: The encryption-at-rest settings of the transform that apply to accessing
        user data.
        :returns: CreateMLTransformResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises AccessDeniedException:
        :raises ResourceNumberLimitExceededException:
        :raises IdempotentParameterMismatchException:
        """
        raise NotImplementedError

    @handler("CreatePartition")
    def create_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_input: PartitionInput,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> CreatePartitionResponse:
        """Creates a new partition.

        :param database_name: The name of the metadata database in which the partition is to be
        created.
        :param table_name: The name of the metadata table in which the partition is to be created.
        :param partition_input: A ``PartitionInput`` structure defining the partition to be created.
        :param catalog_id: The Amazon Web Services account ID of the catalog in which the partition
        is to be created.
        :returns: CreatePartitionResponse
        :raises InvalidInputException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("CreatePartitionIndex")
    def create_partition_index(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_index: PartitionIndex,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> CreatePartitionIndexResponse:
        """Creates a specified partition index in an existing table.

        :param database_name: Specifies the name of a database in which you want to create a partition
        index.
        :param table_name: Specifies the name of a table in which you want to create a partition
        index.
        :param partition_index: Specifies a ``PartitionIndex`` structure to create a partition index in
        an existing table.
        :param catalog_id: The catalog ID where the table resides.
        :returns: CreatePartitionIndexResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("CreateRegistry")
    def create_registry(
        self,
        context: RequestContext,
        registry_name: SchemaRegistryNameString,
        description: DescriptionString | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateRegistryResponse:
        """Creates a new registry which may be used to hold a collection of
        schemas.

        :param registry_name: Name of the registry to be created of max length of 255, and may only
        contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.
        :param description: A description of the registry.
        :param tags: Amazon Web Services tags that contain a key value pair and may be
        searched by console, command line, or API.
        :returns: CreateRegistryResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("CreateSchema")
    def create_schema(
        self,
        context: RequestContext,
        schema_name: SchemaRegistryNameString,
        data_format: DataFormat,
        registry_id: RegistryId | None = None,
        compatibility: Compatibility | None = None,
        description: DescriptionString | None = None,
        tags: TagsMap | None = None,
        schema_definition: SchemaDefinitionString | None = None,
        **kwargs,
    ) -> CreateSchemaResponse:
        """Creates a new schema set and registers the schema definition. Returns an
        error if the schema set already exists without actually registering the
        version.

        When the schema set is created, a version checkpoint will be set to the
        first version. Compatibility mode "DISABLED" restricts any additional
        schema versions from being added after the first schema version. For all
        other compatibility modes, validation of compatibility settings will be
        applied only from the second version onwards when the
        ``RegisterSchemaVersion`` API is used.

        When this API is called without a ``RegistryId``, this will create an
        entry for a "default-registry" in the registry database tables, if it is
        not already present.

        :param schema_name: Name of the schema to be created of max length of 255, and may only
        contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.
        :param data_format: The data format of the schema definition.
        :param registry_id: This is a wrapper shape to contain the registry identity fields.
        :param compatibility: The compatibility mode of the schema.
        :param description: An optional description of the schema.
        :param tags: Amazon Web Services tags that contain a key value pair and may be
        searched by console, command line, or API.
        :param schema_definition: The schema definition using the ``DataFormat`` setting for
        ``SchemaName``.
        :returns: CreateSchemaResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("CreateScript")
    def create_script(
        self,
        context: RequestContext,
        dag_nodes: DagNodes | None = None,
        dag_edges: DagEdges | None = None,
        language: Language | None = None,
        **kwargs,
    ) -> CreateScriptResponse:
        """Transforms a directed acyclic graph (DAG) into code.

        :param dag_nodes: A list of the nodes in the DAG.
        :param dag_edges: A list of the edges in the DAG.
        :param language: The programming language of the resulting code from the DAG.
        :returns: CreateScriptResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("CreateSecurityConfiguration")
    def create_security_configuration(
        self,
        context: RequestContext,
        name: NameString,
        encryption_configuration: EncryptionConfiguration,
        **kwargs,
    ) -> CreateSecurityConfigurationResponse:
        """Creates a new security configuration. A security configuration is a set
        of security properties that can be used by Glue. You can use a security
        configuration to encrypt data at rest. For information about using
        security configurations in Glue, see `Encrypting Data Written by
        Crawlers, Jobs, and Development
        Endpoints <https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html>`__.

        :param name: The name for the new security configuration.
        :param encryption_configuration: The encryption configuration for the new security configuration.
        :returns: CreateSecurityConfigurationResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateSession")
    def create_session(
        self,
        context: RequestContext,
        id: NameString,
        role: OrchestrationRoleArn,
        command: SessionCommand,
        description: DescriptionString | None = None,
        timeout: Timeout | None = None,
        idle_timeout: Timeout | None = None,
        default_arguments: OrchestrationArgumentsMap | None = None,
        connections: ConnectionsList | None = None,
        max_capacity: NullableDouble | None = None,
        number_of_workers: NullableInteger | None = None,
        worker_type: WorkerType | None = None,
        security_configuration: NameString | None = None,
        glue_version: GlueVersionString | None = None,
        tags: TagsMap | None = None,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> CreateSessionResponse:
        """Creates a new session.

        :param id: The ID of the session request.
        :param role: The IAM Role ARN.
        :param command: The ``SessionCommand`` that runs the job.
        :param description: The description of the session.
        :param timeout: The number of minutes before session times out.
        :param idle_timeout: The number of minutes when idle before session times out.
        :param default_arguments: A map array of key-value pairs.
        :param connections: The number of connections to use for the session.
        :param max_capacity: The number of Glue data processing units (DPUs) that can be allocated
        when the job runs.
        :param number_of_workers: The number of workers of a defined ``WorkerType`` to use for the
        session.
        :param worker_type: The type of predefined worker that is allocated when a job runs.
        :param security_configuration: The name of the SecurityConfiguration structure to be used with the
        session.
        :param glue_version: The Glue version determines the versions of Apache Spark and Python that
        Glue supports.
        :param tags: The map of key value pairs (tags) belonging to the session.
        :param request_origin: The origin of the request.
        :returns: CreateSessionResponse
        :raises AccessDeniedException:
        :raises IdempotentParameterMismatchException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises ValidationException:
        :raises AlreadyExistsException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateTable")
    def create_table(
        self,
        context: RequestContext,
        database_name: NameString,
        table_input: TableInput,
        catalog_id: CatalogIdString | None = None,
        partition_indexes: PartitionIndexList | None = None,
        transaction_id: TransactionIdString | None = None,
        open_table_format_input: OpenTableFormatInput | None = None,
        **kwargs,
    ) -> CreateTableResponse:
        """Creates a new table definition in the Data Catalog.

        :param database_name: The catalog database in which to create the new table.
        :param table_input: The ``TableInput`` object that defines the metadata table to create in
        the catalog.
        :param catalog_id: The ID of the Data Catalog in which to create the ``Table``.
        :param partition_indexes: A list of partition indexes, ``PartitionIndex`` structures, to create in
        the table.
        :param transaction_id: The ID of the transaction.
        :param open_table_format_input: Specifies an ``OpenTableFormatInput`` structure when creating an open
        format table.
        :returns: CreateTableResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ConcurrentModificationException:
        :raises ResourceNotReadyException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("CreateTableOptimizer", expand=False)
    def create_table_optimizer(
        self, context: RequestContext, request: CreateTableOptimizerRequest, **kwargs
    ) -> CreateTableOptimizerResponse:
        """Creates a new table optimizer for a specific function.

        :param catalog_id: The Catalog ID of the table.
        :param database_name: The name of the database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param type: The type of table optimizer.
        :param table_optimizer_configuration: A ``TableOptimizerConfiguration`` object representing the configuration
        of a table optimizer.
        :returns: CreateTableOptimizerResponse
        :raises EntityNotFoundException:
        :raises ValidationException:
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises InternalServiceException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateTrigger", expand=False)
    def create_trigger(
        self, context: RequestContext, request: CreateTriggerRequest, **kwargs
    ) -> CreateTriggerResponse:
        """Creates a new trigger.

        Job arguments may be logged. Do not pass plaintext secrets as arguments.
        Retrieve secrets from a Glue Connection, Amazon Web Services Secrets
        Manager or other secret management mechanism if you intend to keep them
        within the Job.

        :param name: The name of the trigger.
        :param type: The type of the new trigger.
        :param actions: The actions initiated by this trigger when it fires.
        :param workflow_name: The name of the workflow associated with the trigger.
        :param schedule: A ``cron`` expression used to specify the schedule (see `Time-Based
        Schedules for Jobs and
        Crawlers <https://docs.
        :param predicate: A predicate to specify when the new trigger should fire.
        :param description: A description of the new trigger.
        :param start_on_creation: Set to ``true`` to start ``SCHEDULED`` and ``CONDITIONAL`` triggers when
        created.
        :param tags: The tags to use with this trigger.
        :param event_batching_condition: Batch condition that must be met (specified number of events received or
        batch time window expired) before EventBridge event trigger fires.
        :returns: CreateTriggerResponse
        :raises AlreadyExistsException:
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises IdempotentParameterMismatchException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("CreateUsageProfile")
    def create_usage_profile(
        self,
        context: RequestContext,
        name: NameString,
        configuration: ProfileConfiguration,
        description: DescriptionString | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> CreateUsageProfileResponse:
        """Creates an Glue usage profile.

        :param name: The name of the usage profile.
        :param configuration: A ``ProfileConfiguration`` object specifying the job and session values
        for the profile.
        :param description: A description of the usage profile.
        :param tags: A list of tags applied to the usage profile.
        :returns: CreateUsageProfileResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises AlreadyExistsException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises OperationNotSupportedException:
        """
        raise NotImplementedError

    @handler("CreateUserDefinedFunction")
    def create_user_defined_function(
        self,
        context: RequestContext,
        database_name: NameString,
        function_input: UserDefinedFunctionInput,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> CreateUserDefinedFunctionResponse:
        """Creates a new function definition in the Data Catalog.

        :param database_name: The name of the catalog database in which to create the function.
        :param function_input: A ``FunctionInput`` object that defines the function to create in the
        Data Catalog.
        :param catalog_id: The ID of the Data Catalog in which to create the function.
        :returns: CreateUserDefinedFunctionResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("CreateWorkflow")
    def create_workflow(
        self,
        context: RequestContext,
        name: NameString,
        description: WorkflowDescriptionString | None = None,
        default_run_properties: WorkflowRunProperties | None = None,
        tags: TagsMap | None = None,
        max_concurrent_runs: NullableInteger | None = None,
        **kwargs,
    ) -> CreateWorkflowResponse:
        """Creates a new workflow.

        :param name: The name to be assigned to the workflow.
        :param description: A description of the workflow.
        :param default_run_properties: A collection of properties to be used as part of each execution of the
        workflow.
        :param tags: The tags to be used with this workflow.
        :param max_concurrent_runs: You can use this parameter to prevent unwanted multiple updates to data,
        to control costs, or in some cases, to prevent exceeding the maximum
        number of concurrent runs of any of the component jobs.
        :returns: CreateWorkflowResponse
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteBlueprint")
    def delete_blueprint(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteBlueprintResponse:
        """Deletes an existing blueprint.

        :param name: The name of the blueprint to delete.
        :returns: DeleteBlueprintResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("DeleteCatalog")
    def delete_catalog(
        self, context: RequestContext, catalog_id: CatalogIdString, **kwargs
    ) -> DeleteCatalogResponse:
        """Removes the specified catalog from the Glue Data Catalog.

        After completing this operation, you no longer have access to the
        databases, tables (and all table versions and partitions that might
        belong to the tables) and the user-defined functions in the deleted
        catalog. Glue deletes these "orphaned" resources asynchronously in a
        timely manner, at the discretion of the service.

        To ensure the immediate deletion of all related resources before calling
        the ``DeleteCatalog`` operation, use ``DeleteTableVersion`` (or
        ``BatchDeleteTableVersion``), ``DeletePartition`` (or
        ``BatchDeletePartition``), ``DeleteTable`` (or ``BatchDeleteTable``),
        ``DeleteUserDefinedFunction`` and ``DeleteDatabase`` to delete any
        resources that belong to the catalog.

        :param catalog_id: The ID of the catalog.
        :returns: DeleteCatalogResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ConcurrentModificationException:
        :raises AccessDeniedException:
        :raises FederationSourceException:
        """
        raise NotImplementedError

    @handler("DeleteClassifier")
    def delete_classifier(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteClassifierResponse:
        """Removes a classifier from the Data Catalog.

        :param name: Name of the classifier to remove.
        :returns: DeleteClassifierResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteColumnStatisticsForPartition")
    def delete_column_statistics_for_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_values: ValueStringList,
        column_name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeleteColumnStatisticsForPartitionResponse:
        """Delete the partition column statistics of a column.

        The Identity and Access Management (IAM) permission required for this
        operation is ``DeletePartition``.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param partition_values: A list of partition values identifying the partition.
        :param column_name: Name of the column.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: DeleteColumnStatisticsForPartitionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("DeleteColumnStatisticsForTable")
    def delete_column_statistics_for_table(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        column_name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeleteColumnStatisticsForTableResponse:
        """Retrieves table statistics of columns.

        The Identity and Access Management (IAM) permission required for this
        operation is ``DeleteTable``.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param column_name: The name of the column.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: DeleteColumnStatisticsForTableResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("DeleteColumnStatisticsTaskSettings")
    def delete_column_statistics_task_settings(
        self, context: RequestContext, database_name: NameString, table_name: NameString, **kwargs
    ) -> DeleteColumnStatisticsTaskSettingsResponse:
        """Deletes settings for a column statistics task.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table for which to delete column statistics.
        :returns: DeleteColumnStatisticsTaskSettingsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteConnection")
    def delete_connection(
        self,
        context: RequestContext,
        connection_name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeleteConnectionResponse:
        """Deletes a connection from the Data Catalog.

        :param connection_name: The name of the connection to delete.
        :param catalog_id: The ID of the Data Catalog in which the connection resides.
        :returns: DeleteConnectionResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteCrawler")
    def delete_crawler(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteCrawlerResponse:
        """Removes a specified crawler from the Glue Data Catalog, unless the
        crawler state is ``RUNNING``.

        :param name: The name of the crawler to remove.
        :returns: DeleteCrawlerResponse
        :raises EntityNotFoundException:
        :raises CrawlerRunningException:
        :raises SchedulerTransitioningException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteCustomEntityType")
    def delete_custom_entity_type(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteCustomEntityTypeResponse:
        """Deletes a custom pattern by specifying its name.

        :param name: The name of the custom pattern that you want to delete.
        :returns: DeleteCustomEntityTypeResponse
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteDataQualityRuleset")
    def delete_data_quality_ruleset(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteDataQualityRulesetResponse:
        """Deletes a data quality ruleset.

        :param name: A name for the data quality ruleset.
        :returns: DeleteDataQualityRulesetResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("DeleteDatabase")
    def delete_database(
        self,
        context: RequestContext,
        name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeleteDatabaseResponse:
        """Removes a specified database from a Data Catalog.

        After completing this operation, you no longer have access to the tables
        (and all table versions and partitions that might belong to the tables)
        and the user-defined functions in the deleted database. Glue deletes
        these "orphaned" resources asynchronously in a timely manner, at the
        discretion of the service.

        To ensure the immediate deletion of all related resources, before
        calling ``DeleteDatabase``, use ``DeleteTableVersion`` or
        ``BatchDeleteTableVersion``, ``DeletePartition`` or
        ``BatchDeletePartition``, ``DeleteUserDefinedFunction``, and
        ``DeleteTable`` or ``BatchDeleteTable``, to delete any resources that
        belong to the database.

        :param name: The name of the database to delete.
        :param catalog_id: The ID of the Data Catalog in which the database resides.
        :returns: DeleteDatabaseResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("DeleteDevEndpoint")
    def delete_dev_endpoint(
        self, context: RequestContext, endpoint_name: GenericString, **kwargs
    ) -> DeleteDevEndpointResponse:
        """Deletes a specified development endpoint.

        :param endpoint_name: The name of the ``DevEndpoint``.
        :returns: DeleteDevEndpointResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteIntegration")
    def delete_integration(
        self, context: RequestContext, integration_identifier: String128, **kwargs
    ) -> DeleteIntegrationResponse:
        """Deletes the specified Zero-ETL integration.

        :param integration_identifier: The Amazon Resource Name (ARN) for the integration.
        :returns: DeleteIntegrationResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises IntegrationNotFoundFault:
        :raises IntegrationConflictOperationFault:
        :raises InvalidIntegrationStateFault:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises ConflictException:
        :raises InvalidStateException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteIntegrationTableProperties")
    def delete_integration_table_properties(
        self, context: RequestContext, resource_arn: String128, table_name: String128, **kwargs
    ) -> DeleteIntegrationTablePropertiesResponse:
        """Deletes the table properties that have been created for the tables that
        need to be replicated.

        :param resource_arn: The connection ARN of the source, or the database ARN of the target.
        :param table_name: The name of the table to be replicated.
        :returns: DeleteIntegrationTablePropertiesResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DeleteJob")
    def delete_job(
        self, context: RequestContext, job_name: NameString, **kwargs
    ) -> DeleteJobResponse:
        """Deletes a specified job definition. If the job definition is not found,
        no exception is thrown.

        :param job_name: The name of the job definition to delete.
        :returns: DeleteJobResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteMLTransform")
    def delete_ml_transform(
        self, context: RequestContext, transform_id: HashString, **kwargs
    ) -> DeleteMLTransformResponse:
        """Deletes an Glue machine learning transform. Machine learning transforms
        are a special type of transform that use machine learning to learn the
        details of the transformation to be performed by learning from examples
        provided by humans. These transformations are then saved by Glue. If you
        no longer need a transform, you can delete it by calling
        ``DeleteMLTransforms``. However, any Glue jobs that still reference the
        deleted transform will no longer succeed.

        :param transform_id: The unique identifier of the transform to delete.
        :returns: DeleteMLTransformResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("DeletePartition")
    def delete_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_values: ValueStringList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeletePartitionResponse:
        """Deletes a specified partition.

        :param database_name: The name of the catalog database in which the table in question resides.
        :param table_name: The name of the table that contains the partition to be deleted.
        :param partition_values: The values that define the partition.
        :param catalog_id: The ID of the Data Catalog where the partition to be deleted resides.
        :returns: DeletePartitionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeletePartitionIndex")
    def delete_partition_index(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        index_name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeletePartitionIndexResponse:
        """Deletes a specified partition index from an existing table.

        :param database_name: Specifies the name of a database from which you want to delete a
        partition index.
        :param table_name: Specifies the name of a table from which you want to delete a partition
        index.
        :param index_name: The name of the partition index to be deleted.
        :param catalog_id: The catalog ID where the table resides.
        :returns: DeletePartitionIndexResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises ConflictException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("DeleteRegistry")
    def delete_registry(
        self, context: RequestContext, registry_id: RegistryId, **kwargs
    ) -> DeleteRegistryResponse:
        """Delete the entire registry including schema and all of its versions. To
        get the status of the delete operation, you can call the ``GetRegistry``
        API after the asynchronous call. Deleting a registry will deactivate all
        online operations for the registry such as the ``UpdateRegistry``,
        ``CreateSchema``, ``UpdateSchema``, and ``RegisterSchemaVersion`` APIs.

        :param registry_id: This is a wrapper structure that may contain the registry name and
        Amazon Resource Name (ARN).
        :returns: DeleteRegistryResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteResourcePolicy")
    def delete_resource_policy(
        self,
        context: RequestContext,
        policy_hash_condition: HashString | None = None,
        resource_arn: GlueResourceArn | None = None,
        **kwargs,
    ) -> DeleteResourcePolicyResponse:
        """Deletes a specified policy.

        :param policy_hash_condition: The hash value returned when this policy was set.
        :param resource_arn: The ARN of the Glue resource for the resource policy to be deleted.
        :returns: DeleteResourcePolicyResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises ConditionCheckFailureException:
        """
        raise NotImplementedError

    @handler("DeleteSchema")
    def delete_schema(
        self, context: RequestContext, schema_id: SchemaId, **kwargs
    ) -> DeleteSchemaResponse:
        """Deletes the entire schema set, including the schema set and all of its
        versions. To get the status of the delete operation, you can call
        ``GetSchema`` API after the asynchronous call. Deleting a registry will
        deactivate all online operations for the schema, such as the
        ``GetSchemaByDefinition``, and ``RegisterSchemaVersion`` APIs.

        :param schema_id: This is a wrapper structure that may contain the schema name and Amazon
        Resource Name (ARN).
        :returns: DeleteSchemaResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteSchemaVersions")
    def delete_schema_versions(
        self, context: RequestContext, schema_id: SchemaId, versions: VersionsString, **kwargs
    ) -> DeleteSchemaVersionsResponse:
        """Remove versions from the specified schema. A version number or range may
        be supplied. If the compatibility mode forbids deleting of a version
        that is necessary, such as BACKWARDS_FULL, an error is returned. Calling
        the ``GetSchemaVersions`` API after this call will list the status of
        the deleted versions.

        When the range of version numbers contain check pointed version, the API
        will return a 409 conflict and will not proceed with the deletion. You
        have to remove the checkpoint first using the ``DeleteSchemaCheckpoint``
        API before using this API.

        You cannot use the ``DeleteSchemaVersions`` API to delete the first
        schema version in the schema set. The first schema version can only be
        deleted by the ``DeleteSchema`` API. This operation will also delete the
        attached ``SchemaVersionMetadata`` under the schema versions. Hard
        deletes will be enforced on the database.

        If the compatibility mode forbids deleting of a version that is
        necessary, such as BACKWARDS_FULL, an error is returned.

        :param schema_id: This is a wrapper structure that may contain the schema name and Amazon
        Resource Name (ARN).
        :param versions: A version range may be supplied which may be of the format:

        -  a single version number, 5

        -  a range, 5-8 : deletes versions 5, 6, 7, 8.
        :returns: DeleteSchemaVersionsResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteSecurityConfiguration")
    def delete_security_configuration(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteSecurityConfigurationResponse:
        """Deletes a specified security configuration.

        :param name: The name of the security configuration to delete.
        :returns: DeleteSecurityConfigurationResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteSession")
    def delete_session(
        self,
        context: RequestContext,
        id: NameString,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> DeleteSessionResponse:
        """Deletes the session.

        :param id: The ID of the session to be deleted.
        :param request_origin: The name of the origin of the delete session request.
        :returns: DeleteSessionResponse
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises IllegalSessionStateException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteTable")
    def delete_table(
        self,
        context: RequestContext,
        database_name: NameString,
        name: NameString,
        catalog_id: CatalogIdString | None = None,
        transaction_id: TransactionIdString | None = None,
        **kwargs,
    ) -> DeleteTableResponse:
        """Removes a table definition from the Data Catalog.

        After completing this operation, you no longer have access to the table
        versions and partitions that belong to the deleted table. Glue deletes
        these "orphaned" resources asynchronously in a timely manner, at the
        discretion of the service.

        To ensure the immediate deletion of all related resources, before
        calling ``DeleteTable``, use ``DeleteTableVersion`` or
        ``BatchDeleteTableVersion``, and ``DeletePartition`` or
        ``BatchDeletePartition``, to delete any resources that belong to the
        table.

        :param database_name: The name of the catalog database in which the table resides.
        :param name: The name of the table to be deleted.
        :param catalog_id: The ID of the Data Catalog where the table resides.
        :param transaction_id: The transaction ID at which to delete the table contents.
        :returns: DeleteTableResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        :raises ResourceNotReadyException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("DeleteTableOptimizer", expand=False)
    def delete_table_optimizer(
        self, context: RequestContext, request: DeleteTableOptimizerRequest, **kwargs
    ) -> DeleteTableOptimizerResponse:
        """Deletes an optimizer and all associated metadata for a table. The
        optimization will no longer be performed on the table.

        :param catalog_id: The Catalog ID of the table.
        :param database_name: The name of the database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param type: The type of table optimizer.
        :returns: DeleteTableOptimizerResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("DeleteTableVersion")
    def delete_table_version(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        version_id: VersionString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeleteTableVersionResponse:
        """Deletes a specified version of a table.

        :param database_name: The database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param version_id: The ID of the table version to be deleted.
        :param catalog_id: The ID of the Data Catalog where the tables reside.
        :returns: DeleteTableVersionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteTrigger")
    def delete_trigger(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteTriggerResponse:
        """Deletes a specified trigger. If the trigger is not found, no exception
        is thrown.

        :param name: The name of the trigger to delete.
        :returns: DeleteTriggerResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DeleteUsageProfile")
    def delete_usage_profile(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteUsageProfileResponse:
        """Deletes the Glue specified usage profile.

        :param name: The name of the usage profile to delete.
        :returns: DeleteUsageProfileResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises OperationNotSupportedException:
        """
        raise NotImplementedError

    @handler("DeleteUserDefinedFunction")
    def delete_user_defined_function(
        self,
        context: RequestContext,
        database_name: NameString,
        function_name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> DeleteUserDefinedFunctionResponse:
        """Deletes an existing function definition from the Data Catalog.

        :param database_name: The name of the catalog database where the function is located.
        :param function_name: The name of the function definition to be deleted.
        :param catalog_id: The ID of the Data Catalog where the function to be deleted is located.
        :returns: DeleteUserDefinedFunctionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("DeleteWorkflow")
    def delete_workflow(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> DeleteWorkflowResponse:
        """Deletes a workflow.

        :param name: Name of the workflow to be deleted.
        :returns: DeleteWorkflowResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("DescribeConnectionType")
    def describe_connection_type(
        self, context: RequestContext, connection_type: NameString, **kwargs
    ) -> DescribeConnectionTypeResponse:
        """The ``DescribeConnectionType`` API provides full details of the
        supported options for a given connection type in Glue.

        :param connection_type: The name of the connection type to be described.
        :returns: DescribeConnectionTypeResponse
        :raises ValidationException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DescribeEntity")
    def describe_entity(
        self,
        context: RequestContext,
        connection_name: NameString,
        entity_name: EntityName,
        catalog_id: CatalogIdString | None = None,
        next_token: NextToken | None = None,
        data_store_api_version: ApiVersion | None = None,
        **kwargs,
    ) -> DescribeEntityResponse:
        """Provides details regarding the entity used with the connection type,
        with a description of the data model for each field in the selected
        entity.

        The response includes all the fields which make up the entity.

        :param connection_name: The name of the connection that contains the connection type
        credentials.
        :param entity_name: The name of the entity that you want to describe from the connection
        type.
        :param catalog_id: The catalog ID of the catalog that contains the connection.
        :param next_token: A continuation token, included if this is a continuation call.
        :param data_store_api_version: The version of the API used for the data store.
        :returns: DescribeEntityResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        :raises ValidationException:
        :raises FederationSourceException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("DescribeInboundIntegrations")
    def describe_inbound_integrations(
        self,
        context: RequestContext,
        integration_arn: String128 | None = None,
        marker: String128 | None = None,
        max_records: IntegrationInteger | None = None,
        target_arn: String128 | None = None,
        **kwargs,
    ) -> DescribeInboundIntegrationsResponse:
        """Returns a list of inbound integrations for the specified integration.

        :param integration_arn: The Amazon Resource Name (ARN) of the integration.
        :param marker: A token to specify where to start paginating.
        :param max_records: The total number of items to return in the output.
        :param target_arn: The Amazon Resource Name (ARN) of the target resource in the
        integration.
        :returns: DescribeInboundIntegrationsResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises IntegrationNotFoundFault:
        :raises TargetResourceNotFound:
        :raises OperationNotSupportedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("DescribeIntegrations")
    def describe_integrations(
        self,
        context: RequestContext,
        integration_identifier: String128 | None = None,
        marker: String128 | None = None,
        max_records: IntegrationInteger | None = None,
        filters: IntegrationFilterList | None = None,
        **kwargs,
    ) -> DescribeIntegrationsResponse:
        """The API is used to retrieve a list of integrations.

        :param integration_identifier: The Amazon Resource Name (ARN) for the integration.
        :param marker: A value that indicates the starting point for the next set of response
        records in a subsequent request.
        :param max_records: The total number of items to return in the output.
        :param filters: A list of key and values, to filter down the results.
        :returns: DescribeIntegrationsResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises IntegrationNotFoundFault:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetBlueprint")
    def get_blueprint(
        self,
        context: RequestContext,
        name: NameString,
        include_blueprint: NullableBoolean | None = None,
        include_parameter_spec: NullableBoolean | None = None,
        **kwargs,
    ) -> GetBlueprintResponse:
        """Retrieves the details of a blueprint.

        :param name: The name of the blueprint.
        :param include_blueprint: Specifies whether or not to include the blueprint in the response.
        :param include_parameter_spec: Specifies whether or not to include the parameter specification.
        :returns: GetBlueprintResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetBlueprintRun")
    def get_blueprint_run(
        self,
        context: RequestContext,
        blueprint_name: OrchestrationNameString,
        run_id: IdString,
        **kwargs,
    ) -> GetBlueprintRunResponse:
        """Retrieves the details of a blueprint run.

        :param blueprint_name: The name of the blueprint.
        :param run_id: The run ID for the blueprint run you want to retrieve.
        :returns: GetBlueprintRunResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetBlueprintRuns")
    def get_blueprint_runs(
        self,
        context: RequestContext,
        blueprint_name: NameString,
        next_token: GenericString | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> GetBlueprintRunsResponse:
        """Retrieves the details of blueprint runs for a specified blueprint.

        :param blueprint_name: The name of the blueprint.
        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :returns: GetBlueprintRunsResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetCatalog")
    def get_catalog(
        self, context: RequestContext, catalog_id: CatalogIdString, **kwargs
    ) -> GetCatalogResponse:
        """The name of the Catalog to retrieve. This should be all lowercase.

        :param catalog_id: The ID of the parent catalog in which the catalog resides.
        :returns: GetCatalogResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetCatalogImportStatus")
    def get_catalog_import_status(
        self, context: RequestContext, catalog_id: CatalogIdString | None = None, **kwargs
    ) -> GetCatalogImportStatusResponse:
        """Retrieves the status of a migration operation.

        :param catalog_id: The ID of the catalog to migrate.
        :returns: GetCatalogImportStatusResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetCatalogs")
    def get_catalogs(
        self,
        context: RequestContext,
        parent_catalog_id: CatalogIdString | None = None,
        next_token: Token | None = None,
        max_results: PageSize | None = None,
        recursive: Boolean | None = None,
        include_root: NullableBoolean | None = None,
        **kwargs,
    ) -> GetCatalogsResponse:
        """Retrieves all catalogs defined in a catalog in the Glue Data Catalog.
        For a Redshift-federated catalog use case, this operation returns the
        list of catalogs mapped to Redshift databases in the Redshift namespace
        catalog.

        :param parent_catalog_id: The ID of the parent catalog in which the catalog resides.
        :param next_token: A continuation token, if this is a continuation call.
        :param max_results: The maximum number of catalogs to return in one response.
        :param recursive: Whether to list all catalogs across the catalog hierarchy, starting from
        the ``ParentCatalogId``.
        :param include_root: Whether to list the default catalog in the account and region in the
        response.
        :returns: GetCatalogsResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetClassifier")
    def get_classifier(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetClassifierResponse:
        """Retrieve a classifier by name.

        :param name: Name of the classifier to retrieve.
        :returns: GetClassifierResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetClassifiers")
    def get_classifiers(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> GetClassifiersResponse:
        """Lists all classifier objects in the Data Catalog.

        :param max_results: The size of the list to return (optional).
        :param next_token: An optional continuation token.
        :returns: GetClassifiersResponse
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetColumnStatisticsForPartition")
    def get_column_statistics_for_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_values: ValueStringList,
        column_names: GetColumnNamesList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> GetColumnStatisticsForPartitionResponse:
        """Retrieves partition statistics of columns.

        The Identity and Access Management (IAM) permission required for this
        operation is ``GetPartition``.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param partition_values: A list of partition values identifying the partition.
        :param column_names: A list of the column names.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: GetColumnStatisticsForPartitionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetColumnStatisticsForTable")
    def get_column_statistics_for_table(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        column_names: GetColumnNamesList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> GetColumnStatisticsForTableResponse:
        """Retrieves table statistics of columns.

        The Identity and Access Management (IAM) permission required for this
        operation is ``GetTable``.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param column_names: A list of the column names.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: GetColumnStatisticsForTableResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetColumnStatisticsTaskRun")
    def get_column_statistics_task_run(
        self, context: RequestContext, column_statistics_task_run_id: HashString, **kwargs
    ) -> GetColumnStatisticsTaskRunResponse:
        """Get the associated metadata/information for a task run, given a task run
        ID.

        :param column_statistics_task_run_id: The identifier for the particular column statistics task run.
        :returns: GetColumnStatisticsTaskRunResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetColumnStatisticsTaskRuns")
    def get_column_statistics_task_runs(
        self,
        context: RequestContext,
        database_name: DatabaseName,
        table_name: NameString,
        max_results: PageSize | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> GetColumnStatisticsTaskRunsResponse:
        """Retrieves information about all runs associated with the specified
        table.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table.
        :param max_results: The maximum size of the response.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: GetColumnStatisticsTaskRunsResponse
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetColumnStatisticsTaskSettings")
    def get_column_statistics_task_settings(
        self, context: RequestContext, database_name: NameString, table_name: NameString, **kwargs
    ) -> GetColumnStatisticsTaskSettingsResponse:
        """Gets settings for a column statistics task.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table for which to retrieve column statistics.
        :returns: GetColumnStatisticsTaskSettingsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetConnection")
    def get_connection(
        self,
        context: RequestContext,
        name: NameString,
        catalog_id: CatalogIdString | None = None,
        hide_password: Boolean | None = None,
        apply_override_for_compute_environment: ComputeEnvironment | None = None,
        **kwargs,
    ) -> GetConnectionResponse:
        """Retrieves a connection definition from the Data Catalog.

        :param name: The name of the connection definition to retrieve.
        :param catalog_id: The ID of the Data Catalog in which the connection resides.
        :param hide_password: Allows you to retrieve the connection metadata without returning the
        password.
        :param apply_override_for_compute_environment: For connections that may be used in multiple services, specifies
        returning properties for the specified compute environment.
        :returns: GetConnectionResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetConnections")
    def get_connections(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString | None = None,
        filter: GetConnectionsFilter | None = None,
        hide_password: Boolean | None = None,
        next_token: Token | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> GetConnectionsResponse:
        """Retrieves a list of connection definitions from the Data Catalog.

        :param catalog_id: The ID of the Data Catalog in which the connections reside.
        :param filter: A filter that controls which connections are returned.
        :param hide_password: Allows you to retrieve the connection metadata without returning the
        password.
        :param next_token: A continuation token, if this is a continuation call.
        :param max_results: The maximum number of connections to return in one response.
        :returns: GetConnectionsResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetCrawler")
    def get_crawler(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetCrawlerResponse:
        """Retrieves metadata for a specified crawler.

        :param name: The name of the crawler to retrieve metadata for.
        :returns: GetCrawlerResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetCrawlerMetrics")
    def get_crawler_metrics(
        self,
        context: RequestContext,
        crawler_name_list: CrawlerNameList | None = None,
        max_results: PageSize | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> GetCrawlerMetricsResponse:
        """Retrieves metrics about specified crawlers.

        :param crawler_name_list: A list of the names of crawlers about which to retrieve metrics.
        :param max_results: The maximum size of a list to return.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: GetCrawlerMetricsResponse
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetCrawlers")
    def get_crawlers(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> GetCrawlersResponse:
        """Retrieves metadata for all crawlers defined in the customer account.

        :param max_results: The number of crawlers to return on each call.
        :param next_token: A continuation token, if this is a continuation request.
        :returns: GetCrawlersResponse
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetCustomEntityType")
    def get_custom_entity_type(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetCustomEntityTypeResponse:
        """Retrieves the details of a custom pattern by specifying its name.

        :param name: The name of the custom pattern that you want to retrieve.
        :returns: GetCustomEntityTypeResponse
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetDataCatalogEncryptionSettings")
    def get_data_catalog_encryption_settings(
        self, context: RequestContext, catalog_id: CatalogIdString | None = None, **kwargs
    ) -> GetDataCatalogEncryptionSettingsResponse:
        """Retrieves the security configuration for a specified catalog.

        :param catalog_id: The ID of the Data Catalog to retrieve the security configuration for.
        :returns: GetDataCatalogEncryptionSettingsResponse
        :raises InternalServiceException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetDataQualityModel")
    def get_data_quality_model(
        self,
        context: RequestContext,
        profile_id: HashString,
        statistic_id: HashString | None = None,
        **kwargs,
    ) -> GetDataQualityModelResponse:
        """Retrieve the training status of the model along with more information
        (CompletedOn, StartedOn, FailureReason).

        :param profile_id: The Profile ID.
        :param statistic_id: The Statistic ID.
        :returns: GetDataQualityModelResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetDataQualityModelResult")
    def get_data_quality_model_result(
        self, context: RequestContext, statistic_id: HashString, profile_id: HashString, **kwargs
    ) -> GetDataQualityModelResultResponse:
        """Retrieve a statistic's predictions for a given Profile ID.

        :param statistic_id: The Statistic ID.
        :param profile_id: The Profile ID.
        :returns: GetDataQualityModelResultResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetDataQualityResult")
    def get_data_quality_result(
        self, context: RequestContext, result_id: HashString, **kwargs
    ) -> GetDataQualityResultResponse:
        """Retrieves the result of a data quality rule evaluation.

        :param result_id: A unique result ID for the data quality result.
        :returns: GetDataQualityResultResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("GetDataQualityRuleRecommendationRun")
    def get_data_quality_rule_recommendation_run(
        self, context: RequestContext, run_id: HashString, **kwargs
    ) -> GetDataQualityRuleRecommendationRunResponse:
        """Gets the specified recommendation run that was used to generate rules.

        :param run_id: The unique run identifier associated with this run.
        :returns: GetDataQualityRuleRecommendationRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetDataQualityRuleset")
    def get_data_quality_ruleset(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetDataQualityRulesetResponse:
        """Returns an existing ruleset by identifier or name.

        :param name: The name of the ruleset.
        :returns: GetDataQualityRulesetResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetDataQualityRulesetEvaluationRun")
    def get_data_quality_ruleset_evaluation_run(
        self, context: RequestContext, run_id: HashString, **kwargs
    ) -> GetDataQualityRulesetEvaluationRunResponse:
        """Retrieves a specific run where a ruleset is evaluated against a data
        source.

        :param run_id: The unique run identifier associated with this run.
        :returns: GetDataQualityRulesetEvaluationRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetDatabase")
    def get_database(
        self,
        context: RequestContext,
        name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> GetDatabaseResponse:
        """Retrieves the definition of a specified database.

        :param name: The name of the database to retrieve.
        :param catalog_id: The ID of the Data Catalog in which the database resides.
        :returns: GetDatabaseResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetDatabases")
    def get_databases(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString | None = None,
        next_token: Token | None = None,
        max_results: CatalogGetterPageSize | None = None,
        resource_share_type: ResourceShareType | None = None,
        attributes_to_get: DatabaseAttributesList | None = None,
        **kwargs,
    ) -> GetDatabasesResponse:
        """Retrieves all databases defined in a given Data Catalog.

        :param catalog_id: The ID of the Data Catalog from which to retrieve ``Databases``.
        :param next_token: A continuation token, if this is a continuation call.
        :param max_results: The maximum number of databases to return in one response.
        :param resource_share_type: Allows you to specify that you want to list the databases shared with
        your account.
        :param attributes_to_get: Specifies the database fields returned by the ``GetDatabases`` call.
        :returns: GetDatabasesResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises EntityNotFoundException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetDataflowGraph")
    def get_dataflow_graph(
        self, context: RequestContext, python_script: PythonScript | None = None, **kwargs
    ) -> GetDataflowGraphResponse:
        """Transforms a Python script into a directed acyclic graph (DAG).

        :param python_script: The Python script to transform.
        :returns: GetDataflowGraphResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetDevEndpoint")
    def get_dev_endpoint(
        self, context: RequestContext, endpoint_name: GenericString, **kwargs
    ) -> GetDevEndpointResponse:
        """Retrieves information about a specified development endpoint.

        When you create a development endpoint in a virtual private cloud (VPC),
        Glue returns only a private IP address, and the public IP address field
        is not populated. When you create a non-VPC development endpoint, Glue
        returns only a public IP address.

        :param endpoint_name: Name of the ``DevEndpoint`` to retrieve information for.
        :returns: GetDevEndpointResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetDevEndpoints")
    def get_dev_endpoints(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        next_token: GenericString | None = None,
        **kwargs,
    ) -> GetDevEndpointsResponse:
        """Retrieves all the development endpoints in this Amazon Web Services
        account.

        When you create a development endpoint in a virtual private cloud (VPC),
        Glue returns only a private IP address and the public IP address field
        is not populated. When you create a non-VPC development endpoint, Glue
        returns only a public IP address.

        :param max_results: The maximum size of information to return.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: GetDevEndpointsResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetEntityRecords")
    def get_entity_records(
        self,
        context: RequestContext,
        entity_name: EntityName,
        limit: Limit,
        connection_name: NameString | None = None,
        catalog_id: CatalogIdString | None = None,
        next_token: NextToken | None = None,
        data_store_api_version: ApiVersion | None = None,
        connection_options: ConnectionOptions | None = None,
        filter_predicate: FilterPredicate | None = None,
        order_by: String | None = None,
        selected_fields: SelectedFields | None = None,
        **kwargs,
    ) -> GetEntityRecordsResponse:
        """This API is used to query preview data from a given connection type or
        from a native Amazon S3 based Glue Data Catalog.

        Returns records as an array of JSON blobs. Each record is formatted
        using Jackson JsonNode based on the field type defined by the
        ``DescribeEntity`` API.

        Spark connectors generate schemas according to the same data type
        mapping as in the ``DescribeEntity`` API. Spark connectors convert data
        to the appropriate data types matching the schema when returning rows.

        :param entity_name: Name of the entity that we want to query the preview data from the given
        connection type.
        :param limit: Limits the number of records fetched with the request.
        :param connection_name: The name of the connection that contains the connection type
        credentials.
        :param catalog_id: The catalog ID of the catalog that contains the connection.
        :param next_token: A continuation token, included if this is a continuation call.
        :param data_store_api_version: The API version of the SaaS connector.
        :param connection_options: Connector options that are required to query the data.
        :param filter_predicate: A filter predicate that you can apply in the query request.
        :param order_by: A parameter that orders the response preview data.
        :param selected_fields: List of fields that we want to fetch as part of preview data.
        :returns: GetEntityRecordsResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        :raises ValidationException:
        :raises FederationSourceException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("GetIntegrationResourceProperty")
    def get_integration_resource_property(
        self, context: RequestContext, resource_arn: String128, **kwargs
    ) -> GetIntegrationResourcePropertyResponse:
        """This API is used for fetching the ``ResourceProperty`` of the Glue
        connection (for the source) or Glue database ARN (for the target)

        :param resource_arn: The connection ARN of the source, or the database ARN of the target.
        :returns: GetIntegrationResourcePropertyResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetIntegrationTableProperties")
    def get_integration_table_properties(
        self, context: RequestContext, resource_arn: String128, table_name: String128, **kwargs
    ) -> GetIntegrationTablePropertiesResponse:
        """This API is used to retrieve optional override properties for the tables
        that need to be replicated. These properties can include properties for
        filtering and partition for source and target tables.

        :param resource_arn: The Amazon Resource Name (ARN) of the target table for which to retrieve
        integration table properties.
        :param table_name: The name of the table to be replicated.
        :returns: GetIntegrationTablePropertiesResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetJob")
    def get_job(self, context: RequestContext, job_name: NameString, **kwargs) -> GetJobResponse:
        """Retrieves an existing job definition.

        :param job_name: The name of the job definition to retrieve.
        :returns: GetJobResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetJobBookmark")
    def get_job_bookmark(
        self, context: RequestContext, job_name: JobName, run_id: RunId | None = None, **kwargs
    ) -> GetJobBookmarkResponse:
        """Returns information on a job bookmark entry.

        For more information about enabling and using job bookmarks, see:

        -  `Tracking processed data using job
           bookmarks <https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html>`__

        -  `Job parameters used by
           Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__

        -  `Job
           structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job>`__

        :param job_name: The name of the job in question.
        :param run_id: The unique run identifier associated with this job run.
        :returns: GetJobBookmarkResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("GetJobRun")
    def get_job_run(
        self,
        context: RequestContext,
        job_name: NameString,
        run_id: IdString,
        predecessors_included: BooleanValue | None = None,
        **kwargs,
    ) -> GetJobRunResponse:
        """Retrieves the metadata for a given job run. Job run history is
        accessible for 365 days for your workflow and job run.

        :param job_name: Name of the job definition being run.
        :param run_id: The ID of the job run.
        :param predecessors_included: True if a list of predecessor runs should be returned.
        :returns: GetJobRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetJobRuns")
    def get_job_runs(
        self,
        context: RequestContext,
        job_name: NameString,
        next_token: GenericString | None = None,
        max_results: OrchestrationPageSize200 | None = None,
        **kwargs,
    ) -> GetJobRunsResponse:
        """Retrieves metadata for all runs of a given job definition.

        ``GetJobRuns`` returns the job runs in chronological order, with the
        newest jobs returned first.

        :param job_name: The name of the job definition for which to retrieve all job runs.
        :param next_token: A continuation token, if this is a continuation call.
        :param max_results: The maximum size of the response.
        :returns: GetJobRunsResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetJobs")
    def get_jobs(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> GetJobsResponse:
        """Retrieves all current job definitions.

        :param next_token: A continuation token, if this is a continuation call.
        :param max_results: The maximum size of the response.
        :returns: GetJobsResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetMLTaskRun")
    def get_ml_task_run(
        self, context: RequestContext, transform_id: HashString, task_run_id: HashString, **kwargs
    ) -> GetMLTaskRunResponse:
        """Gets details for a specific task run on a machine learning transform.
        Machine learning task runs are asynchronous tasks that Glue runs on your
        behalf as part of various machine learning workflows. You can check the
        stats of any task run by calling ``GetMLTaskRun`` with the ``TaskRunID``
        and its parent transform's ``TransformID``.

        :param transform_id: The unique identifier of the machine learning transform.
        :param task_run_id: The unique identifier of the task run.
        :returns: GetMLTaskRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetMLTaskRuns")
    def get_ml_task_runs(
        self,
        context: RequestContext,
        transform_id: HashString,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        filter: TaskRunFilterCriteria | None = None,
        sort: TaskRunSortCriteria | None = None,
        **kwargs,
    ) -> GetMLTaskRunsResponse:
        """Gets a list of runs for a machine learning transform. Machine learning
        task runs are asynchronous tasks that Glue runs on your behalf as part
        of various machine learning workflows. You can get a sortable,
        filterable list of machine learning task runs by calling
        ``GetMLTaskRuns`` with their parent transform's ``TransformID`` and
        other optional parameters as documented in this section.

        This operation returns a list of historic runs and must be paginated.

        :param transform_id: The unique identifier of the machine learning transform.
        :param next_token: A token for pagination of the results.
        :param max_results: The maximum number of results to return.
        :param filter: The filter criteria, in the ``TaskRunFilterCriteria`` structure, for the
        task run.
        :param sort: The sorting criteria, in the ``TaskRunSortCriteria`` structure, for the
        task run.
        :returns: GetMLTaskRunsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetMLTransform")
    def get_ml_transform(
        self, context: RequestContext, transform_id: HashString, **kwargs
    ) -> GetMLTransformResponse:
        """Gets an Glue machine learning transform artifact and all its
        corresponding metadata. Machine learning transforms are a special type
        of transform that use machine learning to learn the details of the
        transformation to be performed by learning from examples provided by
        humans. These transformations are then saved by Glue. You can retrieve
        their metadata by calling ``GetMLTransform``.

        :param transform_id: The unique identifier of the transform, generated at the time that the
        transform was created.
        :returns: GetMLTransformResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetMLTransforms")
    def get_ml_transforms(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        filter: TransformFilterCriteria | None = None,
        sort: TransformSortCriteria | None = None,
        **kwargs,
    ) -> GetMLTransformsResponse:
        """Gets a sortable, filterable list of existing Glue machine learning
        transforms. Machine learning transforms are a special type of transform
        that use machine learning to learn the details of the transformation to
        be performed by learning from examples provided by humans. These
        transformations are then saved by Glue, and you can retrieve their
        metadata by calling ``GetMLTransforms``.

        :param next_token: A paginated token to offset the results.
        :param max_results: The maximum number of results to return.
        :param filter: The filter transformation criteria.
        :param sort: The sorting criteria.
        :returns: GetMLTransformsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetMapping")
    def get_mapping(
        self,
        context: RequestContext,
        source: CatalogEntry,
        sinks: CatalogEntries | None = None,
        location: Location | None = None,
        **kwargs,
    ) -> GetMappingResponse:
        """Creates mappings.

        :param source: Specifies the source table.
        :param sinks: A list of target tables.
        :param location: Parameters for the mapping.
        :returns: GetMappingResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("GetPartition")
    def get_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_values: ValueStringList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> GetPartitionResponse:
        """Retrieves information about a specified partition.

        :param database_name: The name of the catalog database where the partition resides.
        :param table_name: The name of the partition's table.
        :param partition_values: The values that define the partition.
        :param catalog_id: The ID of the Data Catalog where the partition in question resides.
        :returns: GetPartitionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetPartitionIndexes")
    def get_partition_indexes(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        catalog_id: CatalogIdString | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> GetPartitionIndexesResponse:
        """Retrieves the partition indexes associated with a table.

        :param database_name: Specifies the name of a database from which you want to retrieve
        partition indexes.
        :param table_name: Specifies the name of a table for which you want to retrieve the
        partition indexes.
        :param catalog_id: The catalog ID where the table resides.
        :param next_token: A continuation token, included if this is a continuation call.
        :returns: GetPartitionIndexesResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("GetPartitions")
    def get_partitions(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        catalog_id: CatalogIdString | None = None,
        expression: PredicateString | None = None,
        next_token: Token | None = None,
        segment: Segment | None = None,
        max_results: PageSize | None = None,
        exclude_column_schema: BooleanNullable | None = None,
        transaction_id: TransactionIdString | None = None,
        query_as_of_time: Timestamp | None = None,
        **kwargs,
    ) -> GetPartitionsResponse:
        """Retrieves information about the partitions in a table.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :param expression: An expression that filters the partitions to be returned.
        :param next_token: A continuation token, if this is not the first call to retrieve these
        partitions.
        :param segment: The segment of the table's partitions to scan in this request.
        :param max_results: The maximum number of partitions to return in a single response.
        :param exclude_column_schema: When true, specifies not returning the partition column schema.
        :param transaction_id: The transaction ID at which to read the partition contents.
        :param query_as_of_time: The time as of when to read the partition contents.
        :returns: GetPartitionsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises GlueEncryptionException:
        :raises InvalidStateException:
        :raises ResourceNotReadyException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetPlan")
    def get_plan(
        self,
        context: RequestContext,
        mapping: MappingList,
        source: CatalogEntry,
        sinks: CatalogEntries | None = None,
        location: Location | None = None,
        language: Language | None = None,
        additional_plan_options_map: AdditionalPlanOptionsMap | None = None,
        **kwargs,
    ) -> GetPlanResponse:
        """Gets code to perform a specified mapping.

        :param mapping: The list of mappings from a source table to target tables.
        :param source: The source table.
        :param sinks: The target tables.
        :param location: The parameters for the mapping.
        :param language: The programming language of the code to perform the mapping.
        :param additional_plan_options_map: A map to hold additional optional key-value parameters.
        :returns: GetPlanResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetRegistry")
    def get_registry(
        self, context: RequestContext, registry_id: RegistryId, **kwargs
    ) -> GetRegistryResponse:
        """Describes the specified registry in detail.

        :param registry_id: This is a wrapper structure that may contain the registry name and
        Amazon Resource Name (ARN).
        :returns: GetRegistryResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetResourcePolicies")
    def get_resource_policies(
        self,
        context: RequestContext,
        next_token: Token | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> GetResourcePoliciesResponse:
        """Retrieves the resource policies set on individual resources by Resource
        Access Manager during cross-account permission grants. Also retrieves
        the Data Catalog resource policy.

        If you enabled metadata encryption in Data Catalog settings, and you do
        not have permission on the KMS key, the operation can't return the Data
        Catalog resource policy.

        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :returns: GetResourcePoliciesResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetResourcePolicy")
    def get_resource_policy(
        self, context: RequestContext, resource_arn: GlueResourceArn | None = None, **kwargs
    ) -> GetResourcePolicyResponse:
        """Retrieves a specified resource policy.

        :param resource_arn: The ARN of the Glue resource for which to retrieve the resource policy.
        :returns: GetResourcePolicyResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetSchema")
    def get_schema(
        self, context: RequestContext, schema_id: SchemaId, **kwargs
    ) -> GetSchemaResponse:
        """Describes the specified schema in detail.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :returns: GetSchemaResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetSchemaByDefinition")
    def get_schema_by_definition(
        self,
        context: RequestContext,
        schema_id: SchemaId,
        schema_definition: SchemaDefinitionString,
        **kwargs,
    ) -> GetSchemaByDefinitionResponse:
        """Retrieves a schema by the ``SchemaDefinition``. The schema definition is
        sent to the Schema Registry, canonicalized, and hashed. If the hash is
        matched within the scope of the ``SchemaName`` or ARN (or the default
        registry, if none is supplied), that schema’s metadata is returned.
        Otherwise, a 404 or NotFound error is returned. Schema versions in
        ``Deleted`` statuses will not be included in the results.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :param schema_definition: The definition of the schema for which schema details are required.
        :returns: GetSchemaByDefinitionResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetSchemaVersion")
    def get_schema_version(
        self,
        context: RequestContext,
        schema_id: SchemaId | None = None,
        schema_version_id: SchemaVersionIdString | None = None,
        schema_version_number: SchemaVersionNumber | None = None,
        **kwargs,
    ) -> GetSchemaVersionResponse:
        """Get the specified schema by its unique ID assigned when a version of the
        schema is created or registered. Schema versions in Deleted status will
        not be included in the results.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :param schema_version_id: The ``SchemaVersionId`` of the schema version.
        :param schema_version_number: The version number of the schema.
        :returns: GetSchemaVersionResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetSchemaVersionsDiff")
    def get_schema_versions_diff(
        self,
        context: RequestContext,
        schema_id: SchemaId,
        first_schema_version_number: SchemaVersionNumber,
        second_schema_version_number: SchemaVersionNumber,
        schema_diff_type: SchemaDiffType,
        **kwargs,
    ) -> GetSchemaVersionsDiffResponse:
        """Fetches the schema version difference in the specified difference type
        between two stored schema versions in the Schema Registry.

        This API allows you to compare two schema versions between two schema
        definitions under the same schema.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :param first_schema_version_number: The first of the two schema versions to be compared.
        :param second_schema_version_number: The second of the two schema versions to be compared.
        :param schema_diff_type: Refers to ``SYNTAX_DIFF``, which is the currently supported diff type.
        :returns: GetSchemaVersionsDiffResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("GetSecurityConfiguration")
    def get_security_configuration(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetSecurityConfigurationResponse:
        """Retrieves a specified security configuration.

        :param name: The name of the security configuration to retrieve.
        :returns: GetSecurityConfigurationResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetSecurityConfigurations")
    def get_security_configurations(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        next_token: GenericString | None = None,
        **kwargs,
    ) -> GetSecurityConfigurationsResponse:
        """Retrieves a list of all security configurations.

        :param max_results: The maximum number of results to return.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: GetSecurityConfigurationsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetSession")
    def get_session(
        self,
        context: RequestContext,
        id: NameString,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> GetSessionResponse:
        """Retrieves the session.

        :param id: The ID of the session.
        :param request_origin: The origin of the request.
        :returns: GetSessionResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("GetStatement")
    def get_statement(
        self,
        context: RequestContext,
        session_id: NameString,
        id: IntegerValue,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> GetStatementResponse:
        """Retrieves the statement.

        :param session_id: The Session ID of the statement.
        :param id: The Id of the statement.
        :param request_origin: The origin of the request.
        :returns: GetStatementResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises IllegalSessionStateException:
        """
        raise NotImplementedError

    @handler("GetTable")
    def get_table(
        self,
        context: RequestContext,
        database_name: NameString,
        name: NameString,
        catalog_id: CatalogIdString | None = None,
        transaction_id: TransactionIdString | None = None,
        query_as_of_time: Timestamp | None = None,
        include_status_details: BooleanNullable | None = None,
        **kwargs,
    ) -> GetTableResponse:
        """Retrieves the ``Table`` definition in a Data Catalog for a specified
        table.

        :param database_name: The name of the database in the catalog in which the table resides.
        :param name: The name of the table for which to retrieve the definition.
        :param catalog_id: The ID of the Data Catalog where the table resides.
        :param transaction_id: The transaction ID at which to read the table contents.
        :param query_as_of_time: The time as of when to read the table contents.
        :param include_status_details: Specifies whether to include status details related to a request to
        create or update an Glue Data Catalog view.
        :returns: GetTableResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ResourceNotReadyException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetTableOptimizer", expand=False)
    def get_table_optimizer(
        self, context: RequestContext, request: GetTableOptimizerRequest, **kwargs
    ) -> GetTableOptimizerResponse:
        """Returns the configuration of all optimizers associated with a specified
        table.

        :param catalog_id: The Catalog ID of the table.
        :param database_name: The name of the database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param type: The type of table optimizer.
        :returns: GetTableOptimizerResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetTableVersion")
    def get_table_version(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        catalog_id: CatalogIdString | None = None,
        version_id: VersionString | None = None,
        **kwargs,
    ) -> GetTableVersionResponse:
        """Retrieves a specified version of a table.

        :param database_name: The database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param catalog_id: The ID of the Data Catalog where the tables reside.
        :param version_id: The ID value of the table version to be retrieved.
        :returns: GetTableVersionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetTableVersions")
    def get_table_versions(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        catalog_id: CatalogIdString | None = None,
        next_token: Token | None = None,
        max_results: CatalogGetterPageSize | None = None,
        **kwargs,
    ) -> GetTableVersionsResponse:
        """Retrieves a list of strings that identify available versions of a
        specified table.

        :param database_name: The database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param catalog_id: The ID of the Data Catalog where the tables reside.
        :param next_token: A continuation token, if this is not the first call.
        :param max_results: The maximum number of table versions to return in one response.
        :returns: GetTableVersionsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetTables")
    def get_tables(
        self,
        context: RequestContext,
        database_name: NameString,
        catalog_id: CatalogIdString | None = None,
        expression: FilterString | None = None,
        next_token: Token | None = None,
        max_results: CatalogGetterPageSize | None = None,
        transaction_id: TransactionIdString | None = None,
        query_as_of_time: Timestamp | None = None,
        include_status_details: BooleanNullable | None = None,
        attributes_to_get: TableAttributesList | None = None,
        **kwargs,
    ) -> GetTablesResponse:
        """Retrieves the definitions of some or all of the tables in a given
        ``Database``.

        :param database_name: The database in the catalog whose tables to list.
        :param catalog_id: The ID of the Data Catalog where the tables reside.
        :param expression: A regular expression pattern.
        :param next_token: A continuation token, included if this is a continuation call.
        :param max_results: The maximum number of tables to return in a single response.
        :param transaction_id: The transaction ID at which to read the table contents.
        :param query_as_of_time: The time as of when to read the table contents.
        :param include_status_details: Specifies whether to include status details related to a request to
        create or update an Glue Data Catalog view.
        :param attributes_to_get: Specifies the table fields returned by the ``GetTables`` call.
        :returns: GetTablesResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises GlueEncryptionException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetTags")
    def get_tags(
        self, context: RequestContext, resource_arn: GlueResourceArn, **kwargs
    ) -> GetTagsResponse:
        """Retrieves a list of tags associated with a resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource for which to retrieve
        tags.
        :returns: GetTagsResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("GetTrigger")
    def get_trigger(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetTriggerResponse:
        """Retrieves the definition of a trigger.

        :param name: The name of the trigger to retrieve.
        :returns: GetTriggerResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetTriggers")
    def get_triggers(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        dependent_job_name: NameString | None = None,
        max_results: OrchestrationPageSize200 | None = None,
        **kwargs,
    ) -> GetTriggersResponse:
        """Gets all the triggers associated with a job.

        :param next_token: A continuation token, if this is a continuation call.
        :param dependent_job_name: The name of the job to retrieve triggers for.
        :param max_results: The maximum size of the response.
        :returns: GetTriggersResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetUnfilteredPartitionMetadata")
    def get_unfiltered_partition_metadata(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString,
        database_name: NameString,
        table_name: NameString,
        partition_values: ValueStringList,
        supported_permission_types: PermissionTypeList,
        region: ValueString | None = None,
        audit_context: AuditContext | None = None,
        query_session_context: QuerySessionContext | None = None,
        **kwargs,
    ) -> GetUnfilteredPartitionMetadataResponse:
        """Retrieves partition metadata from the Data Catalog that contains
        unfiltered metadata.

        For IAM authorization, the public IAM action associated with this API is
        ``glue:GetPartition``.

        :param catalog_id: The catalog ID where the partition resides.
        :param database_name: (Required) Specifies the name of a database that contains the partition.
        :param table_name: (Required) Specifies the name of a table that contains the partition.
        :param partition_values: (Required) A list of partition key values.
        :param supported_permission_types: (Required) A list of supported permission types.
        :param region: Specified only if the base tables belong to a different Amazon Web
        Services Region.
        :param audit_context: A structure containing Lake Formation audit context information.
        :param query_session_context: A structure used as a protocol between query engines and Lake Formation
        or Glue.
        :returns: GetUnfilteredPartitionMetadataResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises PermissionTypeMismatchException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetUnfilteredPartitionsMetadata")
    def get_unfiltered_partitions_metadata(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString,
        database_name: NameString,
        table_name: NameString,
        supported_permission_types: PermissionTypeList,
        region: ValueString | None = None,
        expression: PredicateString | None = None,
        audit_context: AuditContext | None = None,
        next_token: Token | None = None,
        segment: Segment | None = None,
        max_results: PageSize | None = None,
        query_session_context: QuerySessionContext | None = None,
        **kwargs,
    ) -> GetUnfilteredPartitionsMetadataResponse:
        """Retrieves partition metadata from the Data Catalog that contains
        unfiltered metadata.

        For IAM authorization, the public IAM action associated with this API is
        ``glue:GetPartitions``.

        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the table that contains the partition.
        :param supported_permission_types: A list of supported permission types.
        :param region: Specified only if the base tables belong to a different Amazon Web
        Services Region.
        :param expression: An expression that filters the partitions to be returned.
        :param audit_context: A structure containing Lake Formation audit context information.
        :param next_token: A continuation token, if this is not the first call to retrieve these
        partitions.
        :param segment: The segment of the table's partitions to scan in this request.
        :param max_results: The maximum number of partitions to return in a single response.
        :param query_session_context: A structure used as a protocol between query engines and Lake Formation
        or Glue.
        :returns: GetUnfilteredPartitionsMetadataResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises PermissionTypeMismatchException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetUnfilteredTableMetadata")
    def get_unfiltered_table_metadata(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString,
        database_name: NameString,
        name: NameString,
        supported_permission_types: PermissionTypeList,
        region: ValueString | None = None,
        audit_context: AuditContext | None = None,
        parent_resource_arn: ArnString | None = None,
        root_resource_arn: ArnString | None = None,
        supported_dialect: SupportedDialect | None = None,
        permissions: PermissionList | None = None,
        query_session_context: QuerySessionContext | None = None,
        **kwargs,
    ) -> GetUnfilteredTableMetadataResponse:
        """Allows a third-party analytical engine to retrieve unfiltered table
        metadata from the Data Catalog.

        For IAM authorization, the public IAM action associated with this API is
        ``glue:GetTable``.

        :param catalog_id: The catalog ID where the table resides.
        :param database_name: (Required) Specifies the name of a database that contains the table.
        :param name: (Required) Specifies the name of a table for which you are requesting
        metadata.
        :param supported_permission_types: Indicates the level of filtering a third-party analytical engine is
        capable of enforcing when calling the ``GetUnfilteredTableMetadata`` API
        operation.
        :param region: Specified only if the base tables belong to a different Amazon Web
        Services Region.
        :param audit_context: A structure containing Lake Formation audit context information.
        :param parent_resource_arn: The resource ARN of the view.
        :param root_resource_arn: The resource ARN of the root view in a chain of nested views.
        :param supported_dialect: A structure specifying the dialect and dialect version used by the query
        engine.
        :param permissions: The Lake Formation data permissions of the caller on the table.
        :param query_session_context: A structure used as a protocol between query engines and Lake Formation
        or Glue.
        :returns: GetUnfilteredTableMetadataResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises PermissionTypeMismatchException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        """
        raise NotImplementedError

    @handler("GetUsageProfile")
    def get_usage_profile(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> GetUsageProfileResponse:
        """Retrieves information about the specified Glue usage profile.

        :param name: The name of the usage profile to retrieve.
        :returns: GetUsageProfileResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises OperationNotSupportedException:
        """
        raise NotImplementedError

    @handler("GetUserDefinedFunction")
    def get_user_defined_function(
        self,
        context: RequestContext,
        database_name: NameString,
        function_name: NameString,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> GetUserDefinedFunctionResponse:
        """Retrieves a specified function definition from the Data Catalog.

        :param database_name: The name of the catalog database where the function is located.
        :param function_name: The name of the function.
        :param catalog_id: The ID of the Data Catalog where the function to be retrieved is
        located.
        :returns: GetUserDefinedFunctionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetUserDefinedFunctions")
    def get_user_defined_functions(
        self,
        context: RequestContext,
        pattern: NameString,
        catalog_id: CatalogIdString | None = None,
        database_name: NameString | None = None,
        next_token: Token | None = None,
        max_results: CatalogGetterPageSize | None = None,
        **kwargs,
    ) -> GetUserDefinedFunctionsResponse:
        """Retrieves multiple function definitions from the Data Catalog.

        :param pattern: An optional function-name pattern string that filters the function
        definitions returned.
        :param catalog_id: The ID of the Data Catalog where the functions to be retrieved are
        located.
        :param database_name: The name of the catalog database where the functions are located.
        :param next_token: A continuation token, if this is a continuation call.
        :param max_results: The maximum number of functions to return in one response.
        :returns: GetUserDefinedFunctionsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("GetWorkflow")
    def get_workflow(
        self,
        context: RequestContext,
        name: NameString,
        include_graph: NullableBoolean | None = None,
        **kwargs,
    ) -> GetWorkflowResponse:
        """Retrieves resource metadata for a workflow.

        :param name: The name of the workflow to retrieve.
        :param include_graph: Specifies whether to include a graph when returning the workflow
        resource metadata.
        :returns: GetWorkflowResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetWorkflowRun")
    def get_workflow_run(
        self,
        context: RequestContext,
        name: NameString,
        run_id: IdString,
        include_graph: NullableBoolean | None = None,
        **kwargs,
    ) -> GetWorkflowRunResponse:
        """Retrieves the metadata for a given workflow run. Job run history is
        accessible for 90 days for your workflow and job run.

        :param name: Name of the workflow being run.
        :param run_id: The ID of the workflow run.
        :param include_graph: Specifies whether to include the workflow graph in response or not.
        :returns: GetWorkflowRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetWorkflowRunProperties")
    def get_workflow_run_properties(
        self, context: RequestContext, name: NameString, run_id: IdString, **kwargs
    ) -> GetWorkflowRunPropertiesResponse:
        """Retrieves the workflow run properties which were set during the run.

        :param name: Name of the workflow which was run.
        :param run_id: The ID of the workflow run whose run properties should be returned.
        :returns: GetWorkflowRunPropertiesResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("GetWorkflowRuns")
    def get_workflow_runs(
        self,
        context: RequestContext,
        name: NameString,
        include_graph: NullableBoolean | None = None,
        next_token: GenericString | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> GetWorkflowRunsResponse:
        """Retrieves metadata for all runs of a given workflow.

        :param name: Name of the workflow whose metadata of runs should be returned.
        :param include_graph: Specifies whether to include the workflow graph in response or not.
        :param next_token: The maximum size of the response.
        :param max_results: The maximum number of workflow runs to be included in the response.
        :returns: GetWorkflowRunsResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ImportCatalogToGlue")
    def import_catalog_to_glue(
        self, context: RequestContext, catalog_id: CatalogIdString | None = None, **kwargs
    ) -> ImportCatalogToGlueResponse:
        """Imports an existing Amazon Athena Data Catalog to Glue.

        :param catalog_id: The ID of the catalog to import.
        :returns: ImportCatalogToGlueResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListBlueprints")
    def list_blueprints(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        max_results: OrchestrationPageSize25 | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListBlueprintsResponse:
        """Lists all the blueprint names in an account.

        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :param tags: Filters the list by an Amazon Web Services resource tag.
        :returns: ListBlueprintsResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListColumnStatisticsTaskRuns")
    def list_column_statistics_task_runs(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListColumnStatisticsTaskRunsResponse:
        """List all task runs for a particular account.

        :param max_results: The maximum size of the response.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListColumnStatisticsTaskRunsResponse
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListConnectionTypes")
    def list_connection_types(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListConnectionTypesResponse:
        """The ``ListConnectionTypes`` API provides a discovery mechanism to learn
        available connection types in Glue. The response contains a list of
        connection types with high-level details of what is supported for each
        connection type. The connection types listed are the set of supported
        options for the ``ConnectionType`` value in the ``CreateConnection``
        API.

        :param max_results: The maximum number of results to return.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListConnectionTypesResponse
        :raises InternalServiceException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("ListCrawlers")
    def list_crawlers(
        self,
        context: RequestContext,
        max_results: PageSize | None = None,
        next_token: Token | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListCrawlersResponse:
        """Retrieves the names of all crawler resources in this Amazon Web Services
        account, or the resources with the specified tag. This operation allows
        you to see which resources are available in your account, and their
        names.

        This operation takes the optional ``Tags`` field, which you can use as a
        filter on the response so that tagged resources can be retrieved as a
        group. If you choose to use tags filtering, only resources with the tag
        are retrieved.

        :param max_results: The maximum size of a list to return.
        :param next_token: A continuation token, if this is a continuation request.
        :param tags: Specifies to return only these tagged resources.
        :returns: ListCrawlersResponse
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListCrawls")
    def list_crawls(
        self,
        context: RequestContext,
        crawler_name: NameString,
        max_results: PageSize | None = None,
        filters: CrawlsFilterList | None = None,
        next_token: Token | None = None,
        **kwargs,
    ) -> ListCrawlsResponse:
        """Returns all the crawls of a specified crawler. Returns only the crawls
        that have occurred since the launch date of the crawler history feature,
        and only retains up to 12 months of crawls. Older crawls will not be
        returned.

        You may use this API to:

        -  Retrive all the crawls of a specified crawler.

        -  Retrieve all the crawls of a specified crawler within a limited
           count.

        -  Retrieve all the crawls of a specified crawler in a specific time
           range.

        -  Retrieve all the crawls of a specified crawler with a particular
           state, crawl ID, or DPU hour value.

        :param crawler_name: The name of the crawler whose runs you want to retrieve.
        :param max_results: The maximum number of results to return.
        :param filters: Filters the crawls by the criteria you specify in a list of
        ``CrawlsFilter`` objects.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListCrawlsResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("ListCustomEntityTypes")
    def list_custom_entity_types(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListCustomEntityTypesResponse:
        """Lists all the custom patterns that have been created.

        :param next_token: A paginated token to offset the results.
        :param max_results: The maximum number of results to return.
        :param tags: A list of key-value pair tags.
        :returns: ListCustomEntityTypesResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDataQualityResults")
    def list_data_quality_results(
        self,
        context: RequestContext,
        filter: DataQualityResultFilterCriteria | None = None,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> ListDataQualityResultsResponse:
        """Returns all data quality execution results for your account.

        :param filter: The filter criteria.
        :param next_token: A paginated token to offset the results.
        :param max_results: The maximum number of results to return.
        :returns: ListDataQualityResultsResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDataQualityRuleRecommendationRuns")
    def list_data_quality_rule_recommendation_runs(
        self,
        context: RequestContext,
        filter: DataQualityRuleRecommendationRunFilter | None = None,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> ListDataQualityRuleRecommendationRunsResponse:
        """Lists the recommendation runs meeting the filter criteria.

        :param filter: The filter criteria.
        :param next_token: A paginated token to offset the results.
        :param max_results: The maximum number of results to return.
        :returns: ListDataQualityRuleRecommendationRunsResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDataQualityRulesetEvaluationRuns")
    def list_data_quality_ruleset_evaluation_runs(
        self,
        context: RequestContext,
        filter: DataQualityRulesetEvaluationRunFilter | None = None,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        **kwargs,
    ) -> ListDataQualityRulesetEvaluationRunsResponse:
        """Lists all the runs meeting the filter criteria, where a ruleset is
        evaluated against a data source.

        :param filter: The filter criteria.
        :param next_token: A paginated token to offset the results.
        :param max_results: The maximum number of results to return.
        :returns: ListDataQualityRulesetEvaluationRunsResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDataQualityRulesets")
    def list_data_quality_rulesets(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        filter: DataQualityRulesetFilterCriteria | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListDataQualityRulesetsResponse:
        """Returns a paginated list of rulesets for the specified list of Glue
        tables.

        :param next_token: A paginated token to offset the results.
        :param max_results: The maximum number of results to return.
        :param filter: The filter criteria.
        :param tags: A list of key-value pair tags.
        :returns: ListDataQualityRulesetsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDataQualityStatisticAnnotations")
    def list_data_quality_statistic_annotations(
        self,
        context: RequestContext,
        statistic_id: HashString | None = None,
        profile_id: HashString | None = None,
        timestamp_filter: TimestampFilter | None = None,
        max_results: PageSize | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListDataQualityStatisticAnnotationsResponse:
        """Retrieve annotations for a data quality statistic.

        :param statistic_id: The Statistic ID.
        :param profile_id: The Profile ID.
        :param timestamp_filter: A timestamp filter.
        :param max_results: The maximum number of results to return in this request.
        :param next_token: A pagination token to retrieve the next set of results.
        :returns: ListDataQualityStatisticAnnotationsResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDataQualityStatistics")
    def list_data_quality_statistics(
        self,
        context: RequestContext,
        statistic_id: HashString | None = None,
        profile_id: HashString | None = None,
        timestamp_filter: TimestampFilter | None = None,
        max_results: PageSize | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListDataQualityStatisticsResponse:
        """Retrieves a list of data quality statistics.

        :param statistic_id: The Statistic ID.
        :param profile_id: The Profile ID.
        :param timestamp_filter: A timestamp filter.
        :param max_results: The maximum number of results to return in this request.
        :param next_token: A pagination token to request the next page of results.
        :returns: ListDataQualityStatisticsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListDevEndpoints")
    def list_dev_endpoints(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        max_results: PageSize | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListDevEndpointsResponse:
        """Retrieves the names of all ``DevEndpoint`` resources in this Amazon Web
        Services account, or the resources with the specified tag. This
        operation allows you to see which resources are available in your
        account, and their names.

        This operation takes the optional ``Tags`` field, which you can use as a
        filter on the response so that tagged resources can be retrieved as a
        group. If you choose to use tags filtering, only resources with the tag
        are retrieved.

        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :param tags: Specifies to return only these tagged resources.
        :returns: ListDevEndpointsResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListEntities")
    def list_entities(
        self,
        context: RequestContext,
        connection_name: NameString | None = None,
        catalog_id: CatalogIdString | None = None,
        parent_entity_name: EntityName | None = None,
        next_token: NextToken | None = None,
        data_store_api_version: ApiVersion | None = None,
        **kwargs,
    ) -> ListEntitiesResponse:
        """Returns the available entities supported by the connection type.

        :param connection_name: A name for the connection that has required credentials to query any
        connection type.
        :param catalog_id: The catalog ID of the catalog that contains the connection.
        :param parent_entity_name: Name of the parent entity for which you want to list the children.
        :param next_token: A continuation token, included if this is a continuation call.
        :param data_store_api_version: The API version of the SaaS connector.
        :returns: ListEntitiesResponse
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        :raises ValidationException:
        :raises FederationSourceException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("ListJobs")
    def list_jobs(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        max_results: PageSize | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListJobsResponse:
        """Retrieves the names of all job resources in this Amazon Web Services
        account, or the resources with the specified tag. This operation allows
        you to see which resources are available in your account, and their
        names.

        This operation takes the optional ``Tags`` field, which you can use as a
        filter on the response so that tagged resources can be retrieved as a
        group. If you choose to use tags filtering, only resources with the tag
        are retrieved.

        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :param tags: Specifies to return only these tagged resources.
        :returns: ListJobsResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListMLTransforms")
    def list_ml_transforms(
        self,
        context: RequestContext,
        next_token: PaginationToken | None = None,
        max_results: PageSize | None = None,
        filter: TransformFilterCriteria | None = None,
        sort: TransformSortCriteria | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListMLTransformsResponse:
        """Retrieves a sortable, filterable list of existing Glue machine learning
        transforms in this Amazon Web Services account, or the resources with
        the specified tag. This operation takes the optional ``Tags`` field,
        which you can use as a filter of the responses so that tagged resources
        can be retrieved as a group. If you choose to use tag filtering, only
        resources with the tags are retrieved.

        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :param filter: A ``TransformFilterCriteria`` used to filter the machine learning
        transforms.
        :param sort: A ``TransformSortCriteria`` used to sort the machine learning
        transforms.
        :param tags: Specifies to return only these tagged resources.
        :returns: ListMLTransformsResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListRegistries")
    def list_registries(
        self,
        context: RequestContext,
        max_results: MaxResultsNumber | None = None,
        next_token: SchemaRegistryTokenString | None = None,
        **kwargs,
    ) -> ListRegistriesResponse:
        """Returns a list of registries that you have created, with minimal
        registry information. Registries in the ``Deleting`` status will not be
        included in the results. Empty results will be returned if there are no
        registries available.

        :param max_results: Maximum number of results required per page.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListRegistriesResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListSchemaVersions")
    def list_schema_versions(
        self,
        context: RequestContext,
        schema_id: SchemaId,
        max_results: MaxResultsNumber | None = None,
        next_token: SchemaRegistryTokenString | None = None,
        **kwargs,
    ) -> ListSchemaVersionsResponse:
        """Returns a list of schema versions that you have created, with minimal
        information. Schema versions in Deleted status will not be included in
        the results. Empty results will be returned if there are no schema
        versions available.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :param max_results: Maximum number of results required per page.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListSchemaVersionsResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListSchemas")
    def list_schemas(
        self,
        context: RequestContext,
        registry_id: RegistryId | None = None,
        max_results: MaxResultsNumber | None = None,
        next_token: SchemaRegistryTokenString | None = None,
        **kwargs,
    ) -> ListSchemasResponse:
        """Returns a list of schemas with minimal details. Schemas in Deleting
        status will not be included in the results. Empty results will be
        returned if there are no schemas available.

        When the ``RegistryId`` is not provided, all the schemas across
        registries will be part of the API response.

        :param registry_id: A wrapper structure that may contain the registry name and Amazon
        Resource Name (ARN).
        :param max_results: Maximum number of results required per page.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListSchemasResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("ListSessions")
    def list_sessions(
        self,
        context: RequestContext,
        next_token: OrchestrationToken | None = None,
        max_results: PageSize | None = None,
        tags: TagsMap | None = None,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> ListSessionsResponse:
        """Retrieve a list of sessions.

        :param next_token: The token for the next set of results, or null if there are no more
        result.
        :param max_results: The maximum number of results.
        :param tags: Tags belonging to the session.
        :param request_origin: The origin of the request.
        :returns: ListSessionsResponse
        :raises AccessDeniedException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListStatements")
    def list_statements(
        self,
        context: RequestContext,
        session_id: NameString,
        request_origin: OrchestrationNameString | None = None,
        next_token: OrchestrationToken | None = None,
        **kwargs,
    ) -> ListStatementsResponse:
        """Lists statements for the session.

        :param session_id: The Session ID of the statements.
        :param request_origin: The origin of the request to list statements.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListStatementsResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises IllegalSessionStateException:
        """
        raise NotImplementedError

    @handler("ListTableOptimizerRuns", expand=False)
    def list_table_optimizer_runs(
        self, context: RequestContext, request: ListTableOptimizerRunsRequest, **kwargs
    ) -> ListTableOptimizerRunsResponse:
        """Lists the history of previous optimizer runs for a specific table.

        :param catalog_id: The Catalog ID of the table.
        :param database_name: The name of the database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param type: The type of table optimizer.
        :param max_results: The maximum number of optimizer runs to return on each call.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: ListTableOptimizerRunsResponse
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises InvalidInputException:
        :raises ValidationException:
        :raises InternalServiceException:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("ListTriggers")
    def list_triggers(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        dependent_job_name: NameString | None = None,
        max_results: OrchestrationPageSize200 | None = None,
        tags: TagsMap | None = None,
        **kwargs,
    ) -> ListTriggersResponse:
        """Retrieves the names of all trigger resources in this Amazon Web Services
        account, or the resources with the specified tag. This operation allows
        you to see which resources are available in your account, and their
        names.

        This operation takes the optional ``Tags`` field, which you can use as a
        filter on the response so that tagged resources can be retrieved as a
        group. If you choose to use tags filtering, only resources with the tag
        are retrieved.

        :param next_token: A continuation token, if this is a continuation request.
        :param dependent_job_name: The name of the job for which to retrieve triggers.
        :param max_results: The maximum size of a list to return.
        :param tags: Specifies to return only these tagged resources.
        :returns: ListTriggersResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ListUsageProfiles")
    def list_usage_profiles(
        self,
        context: RequestContext,
        next_token: OrchestrationToken | None = None,
        max_results: OrchestrationPageSize200 | None = None,
        **kwargs,
    ) -> ListUsageProfilesResponse:
        """List all the Glue usage profiles.

        :param next_token: A continuation token, included if this is a continuation call.
        :param max_results: The maximum number of usage profiles to return in a single response.
        :returns: ListUsageProfilesResponse
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises OperationNotSupportedException:
        """
        raise NotImplementedError

    @handler("ListWorkflows")
    def list_workflows(
        self,
        context: RequestContext,
        next_token: GenericString | None = None,
        max_results: OrchestrationPageSize25 | None = None,
        **kwargs,
    ) -> ListWorkflowsResponse:
        """Lists names of workflows created in the account.

        :param next_token: A continuation token, if this is a continuation request.
        :param max_results: The maximum size of a list to return.
        :returns: ListWorkflowsResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ModifyIntegration")
    def modify_integration(
        self,
        context: RequestContext,
        integration_identifier: String128,
        description: IntegrationDescription | None = None,
        data_filter: String2048 | None = None,
        integration_name: String128 | None = None,
        **kwargs,
    ) -> ModifyIntegrationResponse:
        """Modifies a Zero-ETL integration in the caller's account.

        :param integration_identifier: The Amazon Resource Name (ARN) for the integration.
        :param description: A description of the integration.
        :param data_filter: Selects source tables for the integration using Maxwell filter syntax.
        :param integration_name: A unique name for an integration in Glue.
        :returns: ModifyIntegrationResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises IntegrationNotFoundFault:
        :raises IntegrationConflictOperationFault:
        :raises InvalidIntegrationStateFault:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises ConflictException:
        :raises InvalidStateException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("PutDataCatalogEncryptionSettings")
    def put_data_catalog_encryption_settings(
        self,
        context: RequestContext,
        data_catalog_encryption_settings: DataCatalogEncryptionSettings,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> PutDataCatalogEncryptionSettingsResponse:
        """Sets the security configuration for a specified catalog. After the
        configuration has been set, the specified encryption is applied to every
        catalog write thereafter.

        :param data_catalog_encryption_settings: The security configuration to set.
        :param catalog_id: The ID of the Data Catalog to set the security configuration for.
        :returns: PutDataCatalogEncryptionSettingsResponse
        :raises InternalServiceException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("PutDataQualityProfileAnnotation")
    def put_data_quality_profile_annotation(
        self,
        context: RequestContext,
        profile_id: HashString,
        inclusion_annotation: InclusionAnnotationValue,
        **kwargs,
    ) -> PutDataQualityProfileAnnotationResponse:
        """Annotate all datapoints for a Profile.

        :param profile_id: The ID of the data quality monitoring profile to annotate.
        :param inclusion_annotation: The inclusion annotation value to apply to the profile.
        :returns: PutDataQualityProfileAnnotationResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("PutResourcePolicy")
    def put_resource_policy(
        self,
        context: RequestContext,
        policy_in_json: PolicyJsonString,
        resource_arn: GlueResourceArn | None = None,
        policy_hash_condition: HashString | None = None,
        policy_exists_condition: ExistCondition | None = None,
        enable_hybrid: EnableHybridValues | None = None,
        **kwargs,
    ) -> PutResourcePolicyResponse:
        """Sets the Data Catalog resource policy for access control.

        :param policy_in_json: Contains the policy document to set, in JSON format.
        :param resource_arn: Do not use.
        :param policy_hash_condition: The hash value returned when the previous policy was set using
        ``PutResourcePolicy``.
        :param policy_exists_condition: A value of ``MUST_EXIST`` is used to update a policy.
        :param enable_hybrid: If ``'TRUE'``, indicates that you are using both methods to grant
        cross-account access to Data Catalog resources:

        -  By directly updating the resource policy with ``PutResourePolicy``

        -  By using the **Grant permissions** command on the Amazon Web Services
           Management Console.
        :returns: PutResourcePolicyResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises ConditionCheckFailureException:
        """
        raise NotImplementedError

    @handler("PutSchemaVersionMetadata")
    def put_schema_version_metadata(
        self,
        context: RequestContext,
        metadata_key_value: MetadataKeyValuePair,
        schema_id: SchemaId | None = None,
        schema_version_number: SchemaVersionNumber | None = None,
        schema_version_id: SchemaVersionIdString | None = None,
        **kwargs,
    ) -> PutSchemaVersionMetadataResponse:
        """Puts the metadata key value pair for a specified schema version ID. A
        maximum of 10 key value pairs will be allowed per schema version. They
        can be added over one or more calls.

        :param metadata_key_value: The metadata key's corresponding value.
        :param schema_id: The unique ID for the schema.
        :param schema_version_number: The version number of the schema.
        :param schema_version_id: The unique version ID of the schema version.
        :returns: PutSchemaVersionMetadataResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises EntityNotFoundException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("PutWorkflowRunProperties")
    def put_workflow_run_properties(
        self,
        context: RequestContext,
        name: NameString,
        run_id: IdString,
        run_properties: WorkflowRunProperties,
        **kwargs,
    ) -> PutWorkflowRunPropertiesResponse:
        """Puts the specified workflow run properties for the given workflow run.
        If a property already exists for the specified run, then it overrides
        the value otherwise adds the property to existing properties.

        :param name: Name of the workflow which was run.
        :param run_id: The ID of the workflow run for which the run properties should be
        updated.
        :param run_properties: The properties to put for the specified run.
        :returns: PutWorkflowRunPropertiesResponse
        :raises AlreadyExistsException:
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("QuerySchemaVersionMetadata")
    def query_schema_version_metadata(
        self,
        context: RequestContext,
        schema_id: SchemaId | None = None,
        schema_version_number: SchemaVersionNumber | None = None,
        schema_version_id: SchemaVersionIdString | None = None,
        metadata_list: MetadataList | None = None,
        max_results: QuerySchemaVersionMetadataMaxResults | None = None,
        next_token: SchemaRegistryTokenString | None = None,
        **kwargs,
    ) -> QuerySchemaVersionMetadataResponse:
        """Queries for the schema version metadata information.

        :param schema_id: A wrapper structure that may contain the schema name and Amazon Resource
        Name (ARN).
        :param schema_version_number: The version number of the schema.
        :param schema_version_id: The unique version ID of the schema version.
        :param metadata_list: Search key-value pairs for metadata, if they are not provided all the
        metadata information will be fetched.
        :param max_results: Maximum number of results required per page.
        :param next_token: A continuation token, if this is a continuation call.
        :returns: QuerySchemaVersionMetadataResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("RegisterSchemaVersion")
    def register_schema_version(
        self,
        context: RequestContext,
        schema_id: SchemaId,
        schema_definition: SchemaDefinitionString,
        **kwargs,
    ) -> RegisterSchemaVersionResponse:
        """Adds a new version to the existing schema. Returns an error if new
        version of schema does not meet the compatibility requirements of the
        schema set. This API will not create a new schema set and will return a
        404 error if the schema set is not already present in the Schema
        Registry.

        If this is the first schema definition to be registered in the Schema
        Registry, this API will store the schema version and return immediately.
        Otherwise, this call has the potential to run longer than other
        operations due to compatibility modes. You can call the
        ``GetSchemaVersion`` API with the ``SchemaVersionId`` to check
        compatibility modes.

        If the same schema definition is already stored in Schema Registry as a
        version, the schema ID of the existing schema is returned to the caller.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :param schema_definition: The schema definition using the ``DataFormat`` setting for the
        ``SchemaName``.
        :returns: RegisterSchemaVersionResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentModificationException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("RemoveSchemaVersionMetadata")
    def remove_schema_version_metadata(
        self,
        context: RequestContext,
        metadata_key_value: MetadataKeyValuePair,
        schema_id: SchemaId | None = None,
        schema_version_number: SchemaVersionNumber | None = None,
        schema_version_id: SchemaVersionIdString | None = None,
        **kwargs,
    ) -> RemoveSchemaVersionMetadataResponse:
        """Removes a key value pair from the schema version metadata for the
        specified schema version ID.

        :param metadata_key_value: The value of the metadata key.
        :param schema_id: A wrapper structure that may contain the schema name and Amazon Resource
        Name (ARN).
        :param schema_version_number: The version number of the schema.
        :param schema_version_id: The unique version ID of the schema version.
        :returns: RemoveSchemaVersionMetadataResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("ResetJobBookmark")
    def reset_job_bookmark(
        self, context: RequestContext, job_name: JobName, run_id: RunId | None = None, **kwargs
    ) -> ResetJobBookmarkResponse:
        """Resets a bookmark entry.

        For more information about enabling and using job bookmarks, see:

        -  `Tracking processed data using job
           bookmarks <https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html>`__

        -  `Job parameters used by
           Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__

        -  `Job
           structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job>`__

        :param job_name: The name of the job in question.
        :param run_id: The unique run identifier associated with this job run.
        :returns: ResetJobBookmarkResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("ResumeWorkflowRun")
    def resume_workflow_run(
        self,
        context: RequestContext,
        name: NameString,
        run_id: IdString,
        node_ids: NodeIdList,
        **kwargs,
    ) -> ResumeWorkflowRunResponse:
        """Restarts selected nodes of a previous partially completed workflow run
        and resumes the workflow run. The selected nodes and all nodes that are
        downstream from the selected nodes are run.

        :param name: The name of the workflow to resume.
        :param run_id: The ID of the workflow run to resume.
        :param node_ids: A list of the node IDs for the nodes you want to restart.
        :returns: ResumeWorkflowRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentRunsExceededException:
        :raises IllegalWorkflowStateException:
        """
        raise NotImplementedError

    @handler("RunStatement")
    def run_statement(
        self,
        context: RequestContext,
        session_id: NameString,
        code: OrchestrationStatementCodeString,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> RunStatementResponse:
        """Executes the statement.

        :param session_id: The Session Id of the statement to be run.
        :param code: The statement code to be run.
        :param request_origin: The origin of the request.
        :returns: RunStatementResponse
        :raises EntityNotFoundException:
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises ValidationException:
        :raises ResourceNumberLimitExceededException:
        :raises IllegalSessionStateException:
        """
        raise NotImplementedError

    @handler("SearchTables")
    def search_tables(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString | None = None,
        next_token: Token | None = None,
        filters: SearchPropertyPredicates | None = None,
        search_text: ValueString | None = None,
        sort_criteria: SortCriteria | None = None,
        max_results: PageSize | None = None,
        resource_share_type: ResourceShareType | None = None,
        include_status_details: BooleanNullable | None = None,
        **kwargs,
    ) -> SearchTablesResponse:
        """Searches a set of tables based on properties in the table metadata as
        well as on the parent database. You can search against text or filter
        conditions.

        You can only get tables that you have access to based on the security
        policies defined in Lake Formation. You need at least a read-only access
        to the table for it to be returned. If you do not have access to all the
        columns in the table, these columns will not be searched against when
        returning the list of tables back to you. If you have access to the
        columns but not the data in the columns, those columns and the
        associated metadata for those columns will be included in the search.

        :param catalog_id: A unique identifier, consisting of ``account_id``.
        :param next_token: A continuation token, included if this is a continuation call.
        :param filters: A list of key-value pairs, and a comparator used to filter the search
        results.
        :param search_text: A string used for a text search.
        :param sort_criteria: A list of criteria for sorting the results by a field name, in an
        ascending or descending order.
        :param max_results: The maximum number of tables to return in a single response.
        :param resource_share_type: Allows you to specify that you want to search the tables shared with
        your account.
        :param include_status_details: Specifies whether to include status details related to a request to
        create or update an Glue Data Catalog view.
        :returns: SearchTablesResponse
        :raises InternalServiceException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StartBlueprintRun")
    def start_blueprint_run(
        self,
        context: RequestContext,
        blueprint_name: OrchestrationNameString,
        role_arn: OrchestrationIAMRoleArn,
        parameters: BlueprintParameters | None = None,
        **kwargs,
    ) -> StartBlueprintRunResponse:
        """Starts a new run of the specified blueprint.

        :param blueprint_name: The name of the blueprint.
        :param role_arn: Specifies the IAM role used to create the workflow.
        :param parameters: Specifies the parameters as a ``BlueprintParameters`` object.
        :returns: StartBlueprintRunResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ResourceNumberLimitExceededException:
        :raises EntityNotFoundException:
        :raises IllegalBlueprintStateException:
        """
        raise NotImplementedError

    @handler("StartColumnStatisticsTaskRun")
    def start_column_statistics_task_run(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        role: NameString,
        column_name_list: ColumnNameList | None = None,
        sample_size: SampleSizePercentage | None = None,
        catalog_id: NameString | None = None,
        security_configuration: NameString | None = None,
        **kwargs,
    ) -> StartColumnStatisticsTaskRunResponse:
        """Starts a column statistics task run, for a specified table and columns.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table to generate statistics.
        :param role: The IAM role that the service assumes to generate statistics.
        :param column_name_list: A list of the column names to generate statistics.
        :param sample_size: The percentage of rows used to generate statistics.
        :param catalog_id: The ID of the Data Catalog where the table reside.
        :param security_configuration: Name of the security configuration that is used to encrypt CloudWatch
        logs for the column stats task run.
        :returns: StartColumnStatisticsTaskRunResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises ColumnStatisticsTaskRunningException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("StartColumnStatisticsTaskRunSchedule")
    def start_column_statistics_task_run_schedule(
        self, context: RequestContext, database_name: NameString, table_name: NameString, **kwargs
    ) -> StartColumnStatisticsTaskRunScheduleResponse:
        """Starts a column statistics task run schedule.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table for which to start a column statistic task run
        schedule.
        :returns: StartColumnStatisticsTaskRunScheduleResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StartCrawler")
    def start_crawler(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> StartCrawlerResponse:
        """Starts a crawl using the specified crawler, regardless of what is
        scheduled. If the crawler is already running, returns a
        `CrawlerRunningException <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-exceptions.html#aws-glue-api-exceptions-CrawlerRunningException>`__.

        :param name: Name of the crawler to start.
        :returns: StartCrawlerResponse
        :raises EntityNotFoundException:
        :raises CrawlerRunningException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StartCrawlerSchedule")
    def start_crawler_schedule(
        self, context: RequestContext, crawler_name: NameString, **kwargs
    ) -> StartCrawlerScheduleResponse:
        """Changes the schedule state of the specified crawler to ``SCHEDULED``,
        unless the crawler is already running or the schedule state is already
        ``SCHEDULED``.

        :param crawler_name: Name of the crawler to schedule.
        :returns: StartCrawlerScheduleResponse
        :raises EntityNotFoundException:
        :raises SchedulerRunningException:
        :raises SchedulerTransitioningException:
        :raises NoScheduleException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StartDataQualityRuleRecommendationRun")
    def start_data_quality_rule_recommendation_run(
        self,
        context: RequestContext,
        data_source: DataSource,
        role: RoleString,
        number_of_workers: NullableInteger | None = None,
        timeout: Timeout | None = None,
        created_ruleset_name: NameString | None = None,
        data_quality_security_configuration: NameString | None = None,
        client_token: HashString | None = None,
        **kwargs,
    ) -> StartDataQualityRuleRecommendationRunResponse:
        """Starts a recommendation run that is used to generate rules when you
        don't know what rules to write. Glue Data Quality analyzes the data and
        comes up with recommendations for a potential ruleset. You can then
        triage the ruleset and modify the generated ruleset to your liking.

        Recommendation runs are automatically deleted after 90 days.

        :param data_source: The data source (Glue table) associated with this run.
        :param role: An IAM role supplied to encrypt the results of the run.
        :param number_of_workers: The number of ``G.
        :param timeout: The timeout for a run in minutes.
        :param created_ruleset_name: A name for the ruleset.
        :param data_quality_security_configuration: The name of the security configuration created with the data quality
        encryption option.
        :param client_token: Used for idempotency and is recommended to be set to a random ID (such
        as a UUID) to avoid creating or starting multiple instances of the same
        resource.
        :returns: StartDataQualityRuleRecommendationRunResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("StartDataQualityRulesetEvaluationRun")
    def start_data_quality_ruleset_evaluation_run(
        self,
        context: RequestContext,
        data_source: DataSource,
        role: RoleString,
        ruleset_names: RulesetNames,
        number_of_workers: NullableInteger | None = None,
        timeout: Timeout | None = None,
        client_token: HashString | None = None,
        additional_run_options: DataQualityEvaluationRunAdditionalRunOptions | None = None,
        additional_data_sources: DataSourceMap | None = None,
        **kwargs,
    ) -> StartDataQualityRulesetEvaluationRunResponse:
        """Once you have a ruleset definition (either recommended or your own), you
        call this operation to evaluate the ruleset against a data source (Glue
        table). The evaluation computes results which you can retrieve with the
        ``GetDataQualityResult`` API.

        :param data_source: The data source (Glue table) associated with this run.
        :param role: An IAM role supplied to encrypt the results of the run.
        :param ruleset_names: A list of ruleset names.
        :param number_of_workers: The number of ``G.
        :param timeout: The timeout for a run in minutes.
        :param client_token: Used for idempotency and is recommended to be set to a random ID (such
        as a UUID) to avoid creating or starting multiple instances of the same
        resource.
        :param additional_run_options: Additional run options you can specify for an evaluation run.
        :param additional_data_sources: A map of reference strings to additional data sources you can specify
        for an evaluation run.
        :returns: StartDataQualityRulesetEvaluationRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("StartExportLabelsTaskRun")
    def start_export_labels_task_run(
        self, context: RequestContext, transform_id: HashString, output_s3_path: UriString, **kwargs
    ) -> StartExportLabelsTaskRunResponse:
        """Begins an asynchronous task to export all labeled data for a particular
        transform. This task is the only label-related API call that is not part
        of the typical active learning workflow. You typically use
        ``StartExportLabelsTaskRun`` when you want to work with all of your
        existing labels at the same time, such as when you want to remove or
        change labels that were previously submitted as truth. This API
        operation accepts the ``TransformId`` whose labels you want to export
        and an Amazon Simple Storage Service (Amazon S3) path to export the
        labels to. The operation returns a ``TaskRunId``. You can check on the
        status of your task run by calling the ``GetMLTaskRun`` API.

        :param transform_id: The unique identifier of the machine learning transform.
        :param output_s3_path: The Amazon S3 path where you export the labels.
        :returns: StartExportLabelsTaskRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("StartImportLabelsTaskRun")
    def start_import_labels_task_run(
        self,
        context: RequestContext,
        transform_id: HashString,
        input_s3_path: UriString,
        replace_all_labels: ReplaceBoolean | None = None,
        **kwargs,
    ) -> StartImportLabelsTaskRunResponse:
        """Enables you to provide additional labels (examples of truth) to be used
        to teach the machine learning transform and improve its quality. This
        API operation is generally used as part of the active learning workflow
        that starts with the ``StartMLLabelingSetGenerationTaskRun`` call and
        that ultimately results in improving the quality of your machine
        learning transform.

        After the ``StartMLLabelingSetGenerationTaskRun`` finishes, Glue machine
        learning will have generated a series of questions for humans to answer.
        (Answering these questions is often called 'labeling' in the machine
        learning workflows). In the case of the ``FindMatches`` transform, these
        questions are of the form, “What is the correct way to group these rows
        together into groups composed entirely of matching records?” After the
        labeling process is finished, users upload their answers/labels with a
        call to ``StartImportLabelsTaskRun``. After ``StartImportLabelsTaskRun``
        finishes, all future runs of the machine learning transform use the new
        and improved labels and perform a higher-quality transformation.

        By default, ``StartMLLabelingSetGenerationTaskRun`` continually learns
        from and combines all labels that you upload unless you set ``Replace``
        to true. If you set ``Replace`` to true, ``StartImportLabelsTaskRun``
        deletes and forgets all previously uploaded labels and learns only from
        the exact set that you upload. Replacing labels can be helpful if you
        realize that you previously uploaded incorrect labels, and you believe
        that they are having a negative effect on your transform quality.

        You can check on the status of your task run by calling the
        ``GetMLTaskRun`` operation.

        :param transform_id: The unique identifier of the machine learning transform.
        :param input_s3_path: The Amazon Simple Storage Service (Amazon S3) path from where you import
        the labels.
        :param replace_all_labels: Indicates whether to overwrite your existing labels.
        :returns: StartImportLabelsTaskRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("StartJobRun")
    def start_job_run(
        self,
        context: RequestContext,
        job_name: NameString,
        job_run_queuing_enabled: NullableBoolean | None = None,
        job_run_id: IdString | None = None,
        arguments: GenericMap | None = None,
        allocated_capacity: IntegerValue | None = None,
        timeout: Timeout | None = None,
        max_capacity: NullableDouble | None = None,
        security_configuration: NameString | None = None,
        notification_property: NotificationProperty | None = None,
        worker_type: WorkerType | None = None,
        number_of_workers: NullableInteger | None = None,
        execution_class: ExecutionClass | None = None,
        **kwargs,
    ) -> StartJobRunResponse:
        """Starts a job run using a job definition.

        :param job_name: The name of the job definition to use.
        :param job_run_queuing_enabled: Specifies whether job run queuing is enabled for the job run.
        :param job_run_id: The ID of a previous ``JobRun`` to retry.
        :param arguments: The job arguments associated with this run.
        :param allocated_capacity: This field is deprecated.
        :param timeout: The ``JobRun`` timeout in minutes.
        :param max_capacity: For Glue version 1.
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this
        job run.
        :param notification_property: Specifies configuration properties of a job run notification.
        :param worker_type: The type of predefined worker that is allocated when a job runs.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated
        when a job runs.
        :param execution_class: Indicates whether the job is run with a standard or flexible execution
        class.
        :returns: StartJobRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentRunsExceededException:
        """
        raise NotImplementedError

    @handler("StartMLEvaluationTaskRun")
    def start_ml_evaluation_task_run(
        self, context: RequestContext, transform_id: HashString, **kwargs
    ) -> StartMLEvaluationTaskRunResponse:
        """Starts a task to estimate the quality of the transform.

        When you provide label sets as examples of truth, Glue machine learning
        uses some of those examples to learn from them. The rest of the labels
        are used as a test to estimate quality.

        Returns a unique identifier for the run. You can call ``GetMLTaskRun``
        to get more information about the stats of the ``EvaluationTaskRun``.

        :param transform_id: The unique identifier of the machine learning transform.
        :returns: StartMLEvaluationTaskRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ConcurrentRunsExceededException:
        :raises MLTransformNotReadyException:
        """
        raise NotImplementedError

    @handler("StartMLLabelingSetGenerationTaskRun")
    def start_ml_labeling_set_generation_task_run(
        self, context: RequestContext, transform_id: HashString, output_s3_path: UriString, **kwargs
    ) -> StartMLLabelingSetGenerationTaskRunResponse:
        """Starts the active learning workflow for your machine learning transform
        to improve the transform's quality by generating label sets and adding
        labels.

        When the ``StartMLLabelingSetGenerationTaskRun`` finishes, Glue will
        have generated a "labeling set" or a set of questions for humans to
        answer.

        In the case of the ``FindMatches`` transform, these questions are of the
        form, “What is the correct way to group these rows together into groups
        composed entirely of matching records?”

        After the labeling process is finished, you can upload your labels with
        a call to ``StartImportLabelsTaskRun``. After
        ``StartImportLabelsTaskRun`` finishes, all future runs of the machine
        learning transform will use the new and improved labels and perform a
        higher-quality transformation.

        :param transform_id: The unique identifier of the machine learning transform.
        :param output_s3_path: The Amazon Simple Storage Service (Amazon S3) path where you generate
        the labeling set.
        :returns: StartMLLabelingSetGenerationTaskRunResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ConcurrentRunsExceededException:
        """
        raise NotImplementedError

    @handler("StartTrigger")
    def start_trigger(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> StartTriggerResponse:
        """Starts an existing trigger. See `Triggering
        Jobs <https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html>`__
        for information about how different types of trigger are started.

        :param name: The name of the trigger to start.
        :returns: StartTriggerResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentRunsExceededException:
        """
        raise NotImplementedError

    @handler("StartWorkflowRun")
    def start_workflow_run(
        self,
        context: RequestContext,
        name: NameString,
        run_properties: WorkflowRunProperties | None = None,
        **kwargs,
    ) -> StartWorkflowRunResponse:
        """Starts a new run of the specified workflow.

        :param name: The name of the workflow to start.
        :param run_properties: The workflow run properties for the new workflow run.
        :returns: StartWorkflowRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises ConcurrentRunsExceededException:
        """
        raise NotImplementedError

    @handler("StopColumnStatisticsTaskRun")
    def stop_column_statistics_task_run(
        self, context: RequestContext, database_name: DatabaseName, table_name: NameString, **kwargs
    ) -> StopColumnStatisticsTaskRunResponse:
        """Stops a task run for the specified table.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table.
        :returns: StopColumnStatisticsTaskRunResponse
        :raises EntityNotFoundException:
        :raises ColumnStatisticsTaskNotRunningException:
        :raises ColumnStatisticsTaskStoppingException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StopColumnStatisticsTaskRunSchedule")
    def stop_column_statistics_task_run_schedule(
        self, context: RequestContext, database_name: NameString, table_name: NameString, **kwargs
    ) -> StopColumnStatisticsTaskRunScheduleResponse:
        """Stops a column statistics task run schedule.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table for which to stop a column statistic task run
        schedule.
        :returns: StopColumnStatisticsTaskRunScheduleResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StopCrawler")
    def stop_crawler(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> StopCrawlerResponse:
        """If the specified crawler is running, stops the crawl.

        :param name: Name of the crawler to stop.
        :returns: StopCrawlerResponse
        :raises EntityNotFoundException:
        :raises CrawlerNotRunningException:
        :raises CrawlerStoppingException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StopCrawlerSchedule")
    def stop_crawler_schedule(
        self, context: RequestContext, crawler_name: NameString, **kwargs
    ) -> StopCrawlerScheduleResponse:
        """Sets the schedule state of the specified crawler to ``NOT_SCHEDULED``,
        but does not stop the crawler if it is already running.

        :param crawler_name: Name of the crawler whose schedule state to set.
        :returns: StopCrawlerScheduleResponse
        :raises EntityNotFoundException:
        :raises SchedulerNotRunningException:
        :raises SchedulerTransitioningException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("StopSession")
    def stop_session(
        self,
        context: RequestContext,
        id: NameString,
        request_origin: OrchestrationNameString | None = None,
        **kwargs,
    ) -> StopSessionResponse:
        """Stops the session.

        :param id: The ID of the session to be stopped.
        :param request_origin: The origin of the request.
        :returns: StopSessionResponse
        :raises AccessDeniedException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises IllegalSessionStateException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("StopTrigger")
    def stop_trigger(
        self, context: RequestContext, name: NameString, **kwargs
    ) -> StopTriggerResponse:
        """Stops a specified trigger.

        :param name: The name of the trigger to stop.
        :returns: StopTriggerResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("StopWorkflowRun")
    def stop_workflow_run(
        self, context: RequestContext, name: NameString, run_id: IdString, **kwargs
    ) -> StopWorkflowRunResponse:
        """Stops the execution of the specified workflow run.

        :param name: The name of the workflow to stop.
        :param run_id: The ID of the workflow run to stop.
        :returns: StopWorkflowRunResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises IllegalWorkflowStateException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: GlueResourceArn, tags_to_add: TagsMap, **kwargs
    ) -> TagResourceResponse:
        """Adds tags to a resource. A tag is a label you can assign to an Amazon
        Web Services resource. In Glue, you can tag only certain resources. For
        information about what resources you can tag, see `Amazon Web Services
        Tags in
        Glue <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`__.

        :param resource_arn: The ARN of the Glue resource to which to add the tags.
        :param tags_to_add: Tags to add to this resource.
        :returns: TagResourceResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("TestConnection")
    def test_connection(
        self,
        context: RequestContext,
        connection_name: NameString | None = None,
        catalog_id: CatalogIdString | None = None,
        test_connection_input: TestConnectionInput | None = None,
        **kwargs,
    ) -> TestConnectionResponse:
        """Tests a connection to a service to validate the service credentials that
        you provide.

        You can either provide an existing connection name or a
        ``TestConnectionInput`` for testing a non-existing connection input.
        Providing both at the same time will cause an error.

        If the action is successful, the service sends back an HTTP 200
        response.

        :param connection_name: Optional.
        :param catalog_id: The catalog ID where the connection resides.
        :param test_connection_input: A structure that is used to specify testing a connection to a service.
        :returns: TestConnectionResponse
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises ResourceNumberLimitExceededException:
        :raises GlueEncryptionException:
        :raises FederationSourceException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises ConflictException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: GlueResourceArn,
        tags_to_remove: TagKeysList,
        **kwargs,
    ) -> UntagResourceResponse:
        """Removes tags from a resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource from which to remove the
        tags.
        :param tags_to_remove: Tags to remove from this resource.
        :returns: UntagResourceResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises EntityNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateBlueprint")
    def update_blueprint(
        self,
        context: RequestContext,
        name: OrchestrationNameString,
        blueprint_location: OrchestrationS3Location,
        description: Generic512CharString | None = None,
        **kwargs,
    ) -> UpdateBlueprintResponse:
        """Updates a registered blueprint.

        :param name: The name of the blueprint.
        :param blueprint_location: Specifies a path in Amazon S3 where the blueprint is published.
        :param description: A description of the blueprint.
        :returns: UpdateBlueprintResponse
        :raises EntityNotFoundException:
        :raises ConcurrentModificationException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises IllegalBlueprintStateException:
        """
        raise NotImplementedError

    @handler("UpdateCatalog")
    def update_catalog(
        self,
        context: RequestContext,
        catalog_id: CatalogIdString,
        catalog_input: CatalogInput,
        **kwargs,
    ) -> UpdateCatalogResponse:
        """Updates an existing catalog's properties in the Glue Data Catalog.

        :param catalog_id: The ID of the catalog.
        :param catalog_input: A ``CatalogInput`` object specifying the new properties of an existing
        catalog.
        :returns: UpdateCatalogResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ConcurrentModificationException:
        :raises AccessDeniedException:
        :raises FederationSourceException:
        """
        raise NotImplementedError

    @handler("UpdateClassifier")
    def update_classifier(
        self,
        context: RequestContext,
        grok_classifier: UpdateGrokClassifierRequest | None = None,
        xml_classifier: UpdateXMLClassifierRequest | None = None,
        json_classifier: UpdateJsonClassifierRequest | None = None,
        csv_classifier: UpdateCsvClassifierRequest | None = None,
        **kwargs,
    ) -> UpdateClassifierResponse:
        """Modifies an existing classifier (a ``GrokClassifier``, an
        ``XMLClassifier``, a ``JsonClassifier``, or a ``CsvClassifier``,
        depending on which field is present).

        :param grok_classifier: A ``GrokClassifier`` object with updated fields.
        :param xml_classifier: An ``XMLClassifier`` object with updated fields.
        :param json_classifier: A ``JsonClassifier`` object with updated fields.
        :param csv_classifier: A ``CsvClassifier`` object with updated fields.
        :returns: UpdateClassifierResponse
        :raises InvalidInputException:
        :raises VersionMismatchException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("UpdateColumnStatisticsForPartition")
    def update_column_statistics_for_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_values: ValueStringList,
        column_statistics_list: UpdateColumnStatisticsList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> UpdateColumnStatisticsForPartitionResponse:
        """Creates or updates partition statistics of columns.

        The Identity and Access Management (IAM) permission required for this
        operation is ``UpdatePartition``.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param partition_values: A list of partition values identifying the partition.
        :param column_statistics_list: A list of the column statistics.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: UpdateColumnStatisticsForPartitionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("UpdateColumnStatisticsForTable")
    def update_column_statistics_for_table(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        column_statistics_list: UpdateColumnStatisticsList,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> UpdateColumnStatisticsForTableResponse:
        """Creates or updates table statistics of columns.

        The Identity and Access Management (IAM) permission required for this
        operation is ``UpdateTable``.

        :param database_name: The name of the catalog database where the partitions reside.
        :param table_name: The name of the partitions' table.
        :param column_statistics_list: A list of the column statistics.
        :param catalog_id: The ID of the Data Catalog where the partitions in question reside.
        :returns: UpdateColumnStatisticsForTableResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("UpdateColumnStatisticsTaskSettings")
    def update_column_statistics_task_settings(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        role: NameString | None = None,
        schedule: CronExpression | None = None,
        column_name_list: ColumnNameList | None = None,
        sample_size: SampleSizePercentage | None = None,
        catalog_id: NameString | None = None,
        security_configuration: NameString | None = None,
        **kwargs,
    ) -> UpdateColumnStatisticsTaskSettingsResponse:
        """Updates settings for a column statistics task.

        :param database_name: The name of the database where the table resides.
        :param table_name: The name of the table for which to generate column statistics.
        :param role: The role used for running the column statistics.
        :param schedule: A schedule for running the column statistics, specified in CRON syntax.
        :param column_name_list: A list of column names for which to run statistics.
        :param sample_size: The percentage of data to sample.
        :param catalog_id: The ID of the Data Catalog in which the database resides.
        :param security_configuration: Name of the security configuration that is used to encrypt CloudWatch
        logs.
        :returns: UpdateColumnStatisticsTaskSettingsResponse
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises VersionMismatchException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("UpdateConnection")
    def update_connection(
        self,
        context: RequestContext,
        name: NameString,
        connection_input: ConnectionInput,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> UpdateConnectionResponse:
        """Updates a connection definition in the Data Catalog.

        :param name: The name of the connection definition to update.
        :param connection_input: A ``ConnectionInput`` object that redefines the connection in question.
        :param catalog_id: The ID of the Data Catalog in which the connection resides.
        :returns: UpdateConnectionResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("UpdateCrawler")
    def update_crawler(
        self,
        context: RequestContext,
        name: NameString,
        role: Role | None = None,
        database_name: DatabaseName | None = None,
        description: DescriptionStringRemovable | None = None,
        targets: CrawlerTargets | None = None,
        schedule: CronExpression | None = None,
        classifiers: ClassifierNameList | None = None,
        table_prefix: TablePrefix | None = None,
        schema_change_policy: SchemaChangePolicy | None = None,
        recrawl_policy: RecrawlPolicy | None = None,
        lineage_configuration: LineageConfiguration | None = None,
        lake_formation_configuration: LakeFormationConfiguration | None = None,
        configuration: CrawlerConfiguration | None = None,
        crawler_security_configuration: CrawlerSecurityConfiguration | None = None,
        **kwargs,
    ) -> UpdateCrawlerResponse:
        """Updates a crawler. If a crawler is running, you must stop it using
        ``StopCrawler`` before updating it.

        :param name: Name of the new crawler.
        :param role: The IAM role or Amazon Resource Name (ARN) of an IAM role that is used
        by the new crawler to access customer resources.
        :param database_name: The Glue database where results are stored, such as:
        ``arn:aws:daylight:us-east-1::database/sometable/*``.
        :param description: A description of the new crawler.
        :param targets: A list of targets to crawl.
        :param schedule: A ``cron`` expression used to specify the schedule (see `Time-Based
        Schedules for Jobs and
        Crawlers <https://docs.
        :param classifiers: A list of custom classifiers that the user has registered.
        :param table_prefix: The table prefix used for catalog tables that are created.
        :param schema_change_policy: The policy for the crawler's update and deletion behavior.
        :param recrawl_policy: A policy that specifies whether to crawl the entire dataset again, or to
        crawl only folders that were added since the last crawler run.
        :param lineage_configuration: Specifies data lineage configuration settings for the crawler.
        :param lake_formation_configuration: Specifies Lake Formation configuration settings for the crawler.
        :param configuration: Crawler configuration information.
        :param crawler_security_configuration: The name of the ``SecurityConfiguration`` structure to be used by this
        crawler.
        :returns: UpdateCrawlerResponse
        :raises InvalidInputException:
        :raises VersionMismatchException:
        :raises EntityNotFoundException:
        :raises CrawlerRunningException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("UpdateCrawlerSchedule")
    def update_crawler_schedule(
        self,
        context: RequestContext,
        crawler_name: NameString,
        schedule: CronExpression | None = None,
        **kwargs,
    ) -> UpdateCrawlerScheduleResponse:
        """Updates the schedule of a crawler using a ``cron`` expression.

        :param crawler_name: The name of the crawler whose schedule to update.
        :param schedule: The updated ``cron`` expression used to specify the schedule (see
        `Time-Based Schedules for Jobs and
        Crawlers <https://docs.
        :returns: UpdateCrawlerScheduleResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises VersionMismatchException:
        :raises SchedulerTransitioningException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("UpdateDataQualityRuleset")
    def update_data_quality_ruleset(
        self,
        context: RequestContext,
        name: NameString,
        description: DescriptionString | None = None,
        ruleset: DataQualityRulesetString | None = None,
        **kwargs,
    ) -> UpdateDataQualityRulesetResponse:
        """Updates the specified data quality ruleset.

        :param name: The name of the data quality ruleset.
        :param description: A description of the ruleset.
        :param ruleset: A Data Quality Definition Language (DQDL) ruleset.
        :returns: UpdateDataQualityRulesetResponse
        :raises EntityNotFoundException:
        :raises AlreadyExistsException:
        :raises IdempotentParameterMismatchException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises ResourceNumberLimitExceededException:
        """
        raise NotImplementedError

    @handler("UpdateDatabase")
    def update_database(
        self,
        context: RequestContext,
        name: NameString,
        database_input: DatabaseInput,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> UpdateDatabaseResponse:
        """Updates an existing database definition in a Data Catalog.

        :param name: The name of the database to update in the catalog.
        :param database_input: A ``DatabaseInput`` object specifying the new definition of the metadata
        database in the catalog.
        :param catalog_id: The ID of the Data Catalog in which the metadata database resides.
        :returns: UpdateDatabaseResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        :raises ConcurrentModificationException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        :raises AlreadyExistsException:
        """
        raise NotImplementedError

    @handler("UpdateDevEndpoint")
    def update_dev_endpoint(
        self,
        context: RequestContext,
        endpoint_name: GenericString,
        public_key: GenericString | None = None,
        add_public_keys: PublicKeysList | None = None,
        delete_public_keys: PublicKeysList | None = None,
        custom_libraries: DevEndpointCustomLibraries | None = None,
        update_etl_libraries: BooleanValue | None = None,
        delete_arguments: StringList | None = None,
        add_arguments: MapValue | None = None,
        **kwargs,
    ) -> UpdateDevEndpointResponse:
        """Updates a specified development endpoint.

        :param endpoint_name: The name of the ``DevEndpoint`` to be updated.
        :param public_key: The public key for the ``DevEndpoint`` to use.
        :param add_public_keys: The list of public keys for the ``DevEndpoint`` to use.
        :param delete_public_keys: The list of public keys to be deleted from the ``DevEndpoint``.
        :param custom_libraries: Custom Python or Java libraries to be loaded in the ``DevEndpoint``.
        :param update_etl_libraries: ``True`` if the list of custom libraries to be loaded in the development
        endpoint needs to be updated, or ``False`` if otherwise.
        :param delete_arguments: The list of argument keys to be deleted from the map of arguments used
        to configure the ``DevEndpoint``.
        :param add_arguments: The map of arguments to add the map of arguments used to configure the
        ``DevEndpoint``.
        :returns: UpdateDevEndpointResponse
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises InvalidInputException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("UpdateIntegrationResourceProperty")
    def update_integration_resource_property(
        self,
        context: RequestContext,
        resource_arn: String128,
        source_processing_properties: SourceProcessingProperties | None = None,
        target_processing_properties: TargetProcessingProperties | None = None,
        **kwargs,
    ) -> UpdateIntegrationResourcePropertyResponse:
        """This API can be used for updating the ``ResourceProperty`` of the Glue
        connection (for the source) or Glue database ARN (for the target). These
        properties can include the role to access the connection or database.
        Since the same resource can be used across multiple integrations,
        updating resource properties will impact all the integrations using it.

        :param resource_arn: The connection ARN of the source, or the database ARN of the target.
        :param source_processing_properties: The resource properties associated with the integration source.
        :param target_processing_properties: The resource properties associated with the integration target.
        :returns: UpdateIntegrationResourcePropertyResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises InternalServerException:
        :raises ResourceNotFoundException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("UpdateIntegrationTableProperties")
    def update_integration_table_properties(
        self,
        context: RequestContext,
        resource_arn: String128,
        table_name: String128,
        source_table_config: SourceTableConfig | None = None,
        target_table_config: TargetTableConfig | None = None,
        **kwargs,
    ) -> UpdateIntegrationTablePropertiesResponse:
        """This API is used to provide optional override properties for the tables
        that need to be replicated. These properties can include properties for
        filtering and partitioning for the source and target tables. To set both
        source and target properties the same API need to be invoked with the
        Glue connection ARN as ``ResourceArn`` with ``SourceTableConfig``, and
        the Glue database ARN as ``ResourceArn`` with ``TargetTableConfig``
        respectively.

        The override will be reflected across all the integrations using same
        ``ResourceArn`` and source table.

        :param resource_arn: The connection ARN of the source, or the database ARN of the target.
        :param table_name: The name of the table to be replicated.
        :param source_table_config: A structure for the source table configuration.
        :param target_table_config: A structure for the target table configuration.
        :returns: UpdateIntegrationTablePropertiesResponse
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises InvalidInputException:
        """
        raise NotImplementedError

    @handler("UpdateJob")
    def update_job(
        self, context: RequestContext, job_name: NameString, job_update: JobUpdate, **kwargs
    ) -> UpdateJobResponse:
        """Updates an existing job definition. The previous job definition is
        completely overwritten by this information.

        :param job_name: The name of the job definition to update.
        :param job_update: Specifies the values with which to update the job definition.
        :returns: UpdateJobResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UpdateJobFromSourceControl")
    def update_job_from_source_control(
        self,
        context: RequestContext,
        job_name: NameString | None = None,
        provider: SourceControlProvider | None = None,
        repository_name: NameString | None = None,
        repository_owner: NameString | None = None,
        branch_name: NameString | None = None,
        folder: NameString | None = None,
        commit_id: CommitIdString | None = None,
        auth_strategy: SourceControlAuthStrategy | None = None,
        auth_token: AuthTokenString | None = None,
        **kwargs,
    ) -> UpdateJobFromSourceControlResponse:
        """Synchronizes a job from the source control repository. This operation
        takes the job artifacts that are located in the remote repository and
        updates the Glue internal stores with these artifacts.

        This API supports optional parameters which take in the repository
        information.

        :param job_name: The name of the Glue job to be synchronized to or from the remote
        repository.
        :param provider: The provider for the remote repository.
        :param repository_name: The name of the remote repository that contains the job artifacts.
        :param repository_owner: The owner of the remote repository that contains the job artifacts.
        :param branch_name: An optional branch in the remote repository.
        :param folder: An optional folder in the remote repository.
        :param commit_id: A commit ID for a commit in the remote repository.
        :param auth_strategy: The type of authentication, which can be an authentication token stored
        in Amazon Web Services Secrets Manager, or a personal access token.
        :param auth_token: The value of the authorization token.
        :returns: UpdateJobFromSourceControlResponse
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises ValidationException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("UpdateMLTransform")
    def update_ml_transform(
        self,
        context: RequestContext,
        transform_id: HashString,
        name: NameString | None = None,
        description: DescriptionString | None = None,
        parameters: TransformParameters | None = None,
        role: RoleString | None = None,
        glue_version: GlueVersionString | None = None,
        max_capacity: NullableDouble | None = None,
        worker_type: WorkerType | None = None,
        number_of_workers: NullableInteger | None = None,
        timeout: Timeout | None = None,
        max_retries: NullableInteger | None = None,
        **kwargs,
    ) -> UpdateMLTransformResponse:
        """Updates an existing machine learning transform. Call this operation to
        tune the algorithm parameters to achieve better results.

        After calling this operation, you can call the
        ``StartMLEvaluationTaskRun`` operation to assess how well your new
        parameters achieved your goals (such as improving the quality of your
        machine learning transform, or making it more cost-effective).

        :param transform_id: A unique identifier that was generated when the transform was created.
        :param name: The unique name that you gave the transform when you created it.
        :param description: A description of the transform.
        :param parameters: The configuration parameters that are specific to the transform type
        (algorithm) used.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role with the required
        permissions.
        :param glue_version: This value determines which version of Glue this machine learning
        transform is compatible with.
        :param max_capacity: The number of Glue data processing units (DPUs) that are allocated to
        task runs for this transform.
        :param worker_type: The type of predefined worker that is allocated when this task runs.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated
        when this task runs.
        :param timeout: The timeout for a task run for this transform in minutes.
        :param max_retries: The maximum number of times to retry a task for this transform after a
        task run fails.
        :returns: UpdateMLTransformResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises OperationTimeoutException:
        :raises InternalServiceException:
        :raises AccessDeniedException:
        """
        raise NotImplementedError

    @handler("UpdatePartition")
    def update_partition(
        self,
        context: RequestContext,
        database_name: NameString,
        table_name: NameString,
        partition_value_list: BoundedPartitionValueList,
        partition_input: PartitionInput,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> UpdatePartitionResponse:
        """Updates a partition.

        :param database_name: The name of the catalog database in which the table in question resides.
        :param table_name: The name of the table in which the partition to be updated is located.
        :param partition_value_list: List of partition key values that define the partition to update.
        :param partition_input: The new partition object to update the partition to.
        :param catalog_id: The ID of the Data Catalog where the partition to be updated resides.
        :returns: UpdatePartitionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("UpdateRegistry")
    def update_registry(
        self,
        context: RequestContext,
        registry_id: RegistryId,
        description: DescriptionString,
        **kwargs,
    ) -> UpdateRegistryResponse:
        """Updates an existing registry which is used to hold a collection of
        schemas. The updated properties relate to the registry, and do not
        modify any of the schemas within the registry.

        :param registry_id: This is a wrapper structure that may contain the registry name and
        Amazon Resource Name (ARN).
        :param description: A description of the registry.
        :returns: UpdateRegistryResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises ConcurrentModificationException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("UpdateSchema")
    def update_schema(
        self,
        context: RequestContext,
        schema_id: SchemaId,
        schema_version_number: SchemaVersionNumber | None = None,
        compatibility: Compatibility | None = None,
        description: DescriptionString | None = None,
        **kwargs,
    ) -> UpdateSchemaResponse:
        """Updates the description, compatibility setting, or version checkpoint
        for a schema set.

        For updating the compatibility setting, the call will not validate
        compatibility for the entire set of schema versions with the new
        compatibility setting. If the value for ``Compatibility`` is provided,
        the ``VersionNumber`` (a checkpoint) is also required. The API will
        validate the checkpoint version number for consistency.

        If the value for the ``VersionNumber`` (checkpoint) is provided,
        ``Compatibility`` is optional and this can be used to set/reset a
        checkpoint for the schema.

        This update will happen only if the schema is in the AVAILABLE state.

        :param schema_id: This is a wrapper structure to contain schema identity fields.
        :param schema_version_number: Version number required for check pointing.
        :param compatibility: The new compatibility setting for the schema.
        :param description: The new description for the schema.
        :returns: UpdateSchemaResponse
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises EntityNotFoundException:
        :raises ConcurrentModificationException:
        :raises InternalServiceException:
        """
        raise NotImplementedError

    @handler("UpdateSourceControlFromJob")
    def update_source_control_from_job(
        self,
        context: RequestContext,
        job_name: NameString | None = None,
        provider: SourceControlProvider | None = None,
        repository_name: NameString | None = None,
        repository_owner: NameString | None = None,
        branch_name: NameString | None = None,
        folder: NameString | None = None,
        commit_id: CommitIdString | None = None,
        auth_strategy: SourceControlAuthStrategy | None = None,
        auth_token: AuthTokenString | None = None,
        **kwargs,
    ) -> UpdateSourceControlFromJobResponse:
        """Synchronizes a job to the source control repository. This operation
        takes the job artifacts from the Glue internal stores and makes a commit
        to the remote repository that is configured on the job.

        This API supports optional parameters which take in the repository
        information.

        :param job_name: The name of the Glue job to be synchronized to or from the remote
        repository.
        :param provider: The provider for the remote repository.
        :param repository_name: The name of the remote repository that contains the job artifacts.
        :param repository_owner: The owner of the remote repository that contains the job artifacts.
        :param branch_name: An optional branch in the remote repository.
        :param folder: An optional folder in the remote repository.
        :param commit_id: A commit ID for a commit in the remote repository.
        :param auth_strategy: The type of authentication, which can be an authentication token stored
        in Amazon Web Services Secrets Manager, or a personal access token.
        :param auth_token: The value of the authorization token.
        :returns: UpdateSourceControlFromJobResponse
        :raises AccessDeniedException:
        :raises AlreadyExistsException:
        :raises InvalidInputException:
        :raises ValidationException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        """
        raise NotImplementedError

    @handler("UpdateTable")
    def update_table(
        self,
        context: RequestContext,
        database_name: NameString,
        table_input: TableInput,
        catalog_id: CatalogIdString | None = None,
        skip_archive: BooleanNullable | None = None,
        transaction_id: TransactionIdString | None = None,
        version_id: VersionString | None = None,
        view_update_action: ViewUpdateAction | None = None,
        force: Boolean | None = None,
        **kwargs,
    ) -> UpdateTableResponse:
        """Updates a metadata table in the Data Catalog.

        :param database_name: The name of the catalog database in which the table resides.
        :param table_input: An updated ``TableInput`` object to define the metadata table in the
        catalog.
        :param catalog_id: The ID of the Data Catalog where the table resides.
        :param skip_archive: By default, ``UpdateTable`` always creates an archived version of the
        table before updating it.
        :param transaction_id: The transaction ID at which to update the table contents.
        :param version_id: The version ID at which to update the table contents.
        :param view_update_action: The operation to be performed when updating the view.
        :param force: A flag that can be set to true to ignore matching storage descriptor and
        subobject matching requirements.
        :returns: UpdateTableResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        :raises ResourceNumberLimitExceededException:
        :raises GlueEncryptionException:
        :raises ResourceNotReadyException:
        :raises FederationSourceException:
        :raises FederationSourceRetryableException:
        :raises AlreadyExistsException:
        """
        raise NotImplementedError

    @handler("UpdateTableOptimizer", expand=False)
    def update_table_optimizer(
        self, context: RequestContext, request: UpdateTableOptimizerRequest, **kwargs
    ) -> UpdateTableOptimizerResponse:
        """Updates the configuration for an existing table optimizer.

        :param catalog_id: The Catalog ID of the table.
        :param database_name: The name of the database in the catalog in which the table resides.
        :param table_name: The name of the table.
        :param type: The type of table optimizer.
        :param table_optimizer_configuration: A ``TableOptimizerConfiguration`` object representing the configuration
        of a table optimizer.
        :returns: UpdateTableOptimizerResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises InternalServiceException:
        :raises ThrottlingException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UpdateTrigger")
    def update_trigger(
        self, context: RequestContext, name: NameString, trigger_update: TriggerUpdate, **kwargs
    ) -> UpdateTriggerResponse:
        """Updates a trigger definition.

        Job arguments may be logged. Do not pass plaintext secrets as arguments.
        Retrieve secrets from a Glue Connection, Amazon Web Services Secrets
        Manager or other secret management mechanism if you intend to keep them
        within the Job.

        :param name: The name of the trigger to update.
        :param trigger_update: The new values with which to update the trigger.
        :returns: UpdateTriggerResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UpdateUsageProfile")
    def update_usage_profile(
        self,
        context: RequestContext,
        name: NameString,
        configuration: ProfileConfiguration,
        description: DescriptionString | None = None,
        **kwargs,
    ) -> UpdateUsageProfileResponse:
        """Update an Glue usage profile.

        :param name: The name of the usage profile.
        :param configuration: A ``ProfileConfiguration`` object specifying the job and session values
        for the profile.
        :param description: A description of the usage profile.
        :returns: UpdateUsageProfileResponse
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises EntityNotFoundException:
        :raises OperationTimeoutException:
        :raises OperationNotSupportedException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError

    @handler("UpdateUserDefinedFunction")
    def update_user_defined_function(
        self,
        context: RequestContext,
        database_name: NameString,
        function_name: NameString,
        function_input: UserDefinedFunctionInput,
        catalog_id: CatalogIdString | None = None,
        **kwargs,
    ) -> UpdateUserDefinedFunctionResponse:
        """Updates an existing function definition in the Data Catalog.

        :param database_name: The name of the catalog database where the function to be updated is
        located.
        :param function_name: The name of the function.
        :param function_input: A ``FunctionInput`` object that redefines the function in the Data
        Catalog.
        :param catalog_id: The ID of the Data Catalog where the function to be updated is located.
        :returns: UpdateUserDefinedFunctionResponse
        :raises EntityNotFoundException:
        :raises InvalidInputException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises GlueEncryptionException:
        """
        raise NotImplementedError

    @handler("UpdateWorkflow")
    def update_workflow(
        self,
        context: RequestContext,
        name: NameString,
        description: WorkflowDescriptionString | None = None,
        default_run_properties: WorkflowRunProperties | None = None,
        max_concurrent_runs: NullableInteger | None = None,
        **kwargs,
    ) -> UpdateWorkflowResponse:
        """Updates an existing workflow.

        :param name: Name of the workflow to be updated.
        :param description: The description of the workflow.
        :param default_run_properties: A collection of properties to be used as part of each execution of the
        workflow.
        :param max_concurrent_runs: You can use this parameter to prevent unwanted multiple updates to data,
        to control costs, or in some cases, to prevent exceeding the maximum
        number of concurrent runs of any of the component jobs.
        :returns: UpdateWorkflowResponse
        :raises InvalidInputException:
        :raises EntityNotFoundException:
        :raises InternalServiceException:
        :raises OperationTimeoutException:
        :raises ConcurrentModificationException:
        """
        raise NotImplementedError
