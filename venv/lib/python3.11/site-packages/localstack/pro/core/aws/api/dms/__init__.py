from datetime import datetime
from enum import StrEnum
from typing import List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Boolean = bool
BooleanOptional = bool
DoubleOptional = float
ExceptionMessage = str
Integer = int
IntegerOptional = int
Marker = str
MigrationProjectIdentifier = str
ReplicationInstanceClass = str
ResourceArn = str
SecretString = str
String = str


class AssessmentReportType(StrEnum):
    pdf = "pdf"
    csv = "csv"


class AuthMechanismValue(StrEnum):
    default = "default"
    mongodb_cr = "mongodb_cr"
    scram_sha_1 = "scram_sha_1"


class AuthTypeValue(StrEnum):
    no = "no"
    password = "password"


class CannedAclForObjectsValue(StrEnum):
    none = "none"
    private = "private"
    public_read = "public-read"
    public_read_write = "public-read-write"
    authenticated_read = "authenticated-read"
    aws_exec_read = "aws-exec-read"
    bucket_owner_read = "bucket-owner-read"
    bucket_owner_full_control = "bucket-owner-full-control"


class CharLengthSemantics(StrEnum):
    default = "default"
    char = "char"
    byte = "byte"


class CollectorStatus(StrEnum):
    UNREGISTERED = "UNREGISTERED"
    ACTIVE = "ACTIVE"


class CompressionTypeValue(StrEnum):
    none = "none"
    gzip = "gzip"


class DataFormatValue(StrEnum):
    csv = "csv"
    parquet = "parquet"


class DatabaseMode(StrEnum):
    default = "default"
    babelfish = "babelfish"


class DatePartitionDelimiterValue(StrEnum):
    SLASH = "SLASH"
    UNDERSCORE = "UNDERSCORE"
    DASH = "DASH"
    NONE = "NONE"


class DatePartitionSequenceValue(StrEnum):
    YYYYMMDD = "YYYYMMDD"
    YYYYMMDDHH = "YYYYMMDDHH"
    YYYYMM = "YYYYMM"
    MMYYYYDD = "MMYYYYDD"
    DDMMYYYY = "DDMMYYYY"


class DmsSslModeValue(StrEnum):
    none = "none"
    require = "require"
    verify_ca = "verify-ca"
    verify_full = "verify-full"


class EncodingTypeValue(StrEnum):
    plain = "plain"
    plain_dictionary = "plain-dictionary"
    rle_dictionary = "rle-dictionary"


class EncryptionModeValue(StrEnum):
    sse_s3 = "sse-s3"
    sse_kms = "sse-kms"


class EndpointSettingTypeValue(StrEnum):
    string = "string"
    boolean = "boolean"
    integer = "integer"
    enum = "enum"


class KafkaSaslMechanism(StrEnum):
    scram_sha_512 = "scram-sha-512"
    plain = "plain"


class KafkaSecurityProtocol(StrEnum):
    plaintext = "plaintext"
    ssl_authentication = "ssl-authentication"
    ssl_encryption = "ssl-encryption"
    sasl_ssl = "sasl-ssl"


class KafkaSslEndpointIdentificationAlgorithm(StrEnum):
    none = "none"
    https = "https"


class LongVarcharMappingType(StrEnum):
    wstring = "wstring"
    clob = "clob"
    nclob = "nclob"


class MessageFormatValue(StrEnum):
    json = "json"
    json_unformatted = "json-unformatted"


class MigrationTypeValue(StrEnum):
    full_load = "full-load"
    cdc = "cdc"
    full_load_and_cdc = "full-load-and-cdc"


class MySQLAuthenticationMethod(StrEnum):
    password = "password"
    iam = "iam"


class NestingLevelValue(StrEnum):
    none = "none"
    one = "one"


class OracleAuthenticationMethod(StrEnum):
    password = "password"
    kerberos = "kerberos"


class OriginTypeValue(StrEnum):
    SOURCE = "SOURCE"
    TARGET = "TARGET"


class ParquetVersionValue(StrEnum):
    parquet_1_0 = "parquet-1-0"
    parquet_2_0 = "parquet-2-0"


class PluginNameValue(StrEnum):
    no_preference = "no-preference"
    test_decoding = "test-decoding"
    pglogical = "pglogical"


class PostgreSQLAuthenticationMethod(StrEnum):
    password = "password"
    iam = "iam"


class RedisAuthTypeValue(StrEnum):
    none = "none"
    auth_role = "auth-role"
    auth_token = "auth-token"


class RefreshSchemasStatusTypeValue(StrEnum):
    successful = "successful"
    failed = "failed"
    refreshing = "refreshing"


class ReleaseStatusValues(StrEnum):
    beta = "beta"
    prod = "prod"


class ReloadOptionValue(StrEnum):
    data_reload = "data-reload"
    validate_only = "validate-only"


class ReplicationEndpointTypeValue(StrEnum):
    source = "source"
    target = "target"


class SafeguardPolicy(StrEnum):
    rely_on_sql_server_replication_agent = "rely-on-sql-server-replication-agent"
    exclusive_automatic_truncation = "exclusive-automatic-truncation"
    shared_automatic_truncation = "shared-automatic-truncation"


class SourceType(StrEnum):
    replication_instance = "replication-instance"


class SqlServerAuthenticationMethod(StrEnum):
    password = "password"
    kerberos = "kerberos"


class SslSecurityProtocolValue(StrEnum):
    plaintext = "plaintext"
    ssl_encryption = "ssl-encryption"


class StartReplicationMigrationTypeValue(StrEnum):
    reload_target = "reload-target"
    resume_processing = "resume-processing"
    start_replication = "start-replication"


class StartReplicationTaskTypeValue(StrEnum):
    start_replication = "start-replication"
    resume_processing = "resume-processing"
    reload_target = "reload-target"


class TablePreparationMode(StrEnum):
    do_nothing = "do-nothing"
    truncate = "truncate"
    drop_tables_on_target = "drop-tables-on-target"


class TargetDbType(StrEnum):
    specific_database = "specific-database"
    multiple_databases = "multiple-databases"


class TlogAccessMode(StrEnum):
    BackupOnly = "BackupOnly"
    PreferBackup = "PreferBackup"
    PreferTlog = "PreferTlog"
    TlogOnly = "TlogOnly"


class VersionStatus(StrEnum):
    UP_TO_DATE = "UP_TO_DATE"
    OUTDATED = "OUTDATED"
    UNSUPPORTED = "UNSUPPORTED"


class AccessDeniedFault(ServiceException):
    """DMS was denied access to the endpoint. Check that the role is correctly
    configured.
    """

    code: str = "AccessDeniedFault"
    sender_fault: bool = False
    status_code: int = 400


class CollectorNotFoundFault(ServiceException):
    """The specified collector doesn't exist."""

    code: str = "CollectorNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class FailedDependencyFault(ServiceException):
    """A dependency threw an exception."""

    code: str = "FailedDependencyFault"
    sender_fault: bool = False
    status_code: int = 400


class InsufficientResourceCapacityFault(ServiceException):
    """There are not enough resources allocated to the database migration."""

    code: str = "InsufficientResourceCapacityFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidCertificateFault(ServiceException):
    """The certificate was not valid."""

    code: str = "InvalidCertificateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidOperationFault(ServiceException):
    """The action or operation requested isn't valid."""

    code: str = "InvalidOperationFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidResourceStateFault(ServiceException):
    """The resource is in a state that prevents it from being used for database
    migration.
    """

    code: str = "InvalidResourceStateFault"
    sender_fault: bool = False
    status_code: int = 400


class InvalidSubnet(ServiceException):
    """The subnet provided isn't valid."""

    code: str = "InvalidSubnet"
    sender_fault: bool = False
    status_code: int = 400


class KMSAccessDeniedFault(ServiceException):
    """The ciphertext references a key that doesn't exist or that the DMS
    account doesn't have access to.
    """

    code: str = "KMSAccessDeniedFault"
    sender_fault: bool = False
    status_code: int = 400


class KMSDisabledFault(ServiceException):
    """The specified KMS key isn't enabled."""

    code: str = "KMSDisabledFault"
    sender_fault: bool = False
    status_code: int = 400


class KMSFault(ServiceException):
    """An Key Management Service (KMS) error is preventing access to KMS."""

    code: str = "KMSFault"
    sender_fault: bool = False
    status_code: int = 400


class KMSInvalidStateFault(ServiceException):
    """The state of the specified KMS resource isn't valid for this request."""

    code: str = "KMSInvalidStateFault"
    sender_fault: bool = False
    status_code: int = 400


class KMSKeyNotAccessibleFault(ServiceException):
    """DMS cannot access the KMS key."""

    code: str = "KMSKeyNotAccessibleFault"
    sender_fault: bool = False
    status_code: int = 400


class KMSNotFoundFault(ServiceException):
    """The specified KMS entity or resource can't be found."""

    code: str = "KMSNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class KMSThrottlingFault(ServiceException):
    """This request triggered KMS request throttling."""

    code: str = "KMSThrottlingFault"
    sender_fault: bool = False
    status_code: int = 400


class ReplicationSubnetGroupDoesNotCoverEnoughAZs(ServiceException):
    """The replication subnet group does not cover enough Availability Zones
    (AZs). Edit the replication subnet group and add more AZs.
    """

    code: str = "ReplicationSubnetGroupDoesNotCoverEnoughAZs"
    sender_fault: bool = False
    status_code: int = 400


class ResourceAlreadyExistsFault(ServiceException):
    """The resource you are attempting to create already exists."""

    code: str = "ResourceAlreadyExistsFault"
    sender_fault: bool = False
    status_code: int = 400
    resourceArn: Optional[ResourceArn]


class ResourceNotFoundFault(ServiceException):
    """The resource could not be found."""

    code: str = "ResourceNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class ResourceQuotaExceededFault(ServiceException):
    """The quota for this resource quota has been exceeded."""

    code: str = "ResourceQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class S3AccessDeniedFault(ServiceException):
    """Insufficient privileges are preventing access to an Amazon S3 object."""

    code: str = "S3AccessDeniedFault"
    sender_fault: bool = False
    status_code: int = 400


class S3ResourceNotFoundFault(ServiceException):
    """A specified Amazon S3 bucket, bucket folder, or other object can't be
    found.
    """

    code: str = "S3ResourceNotFoundFault"
    sender_fault: bool = False
    status_code: int = 400


class SNSInvalidTopicFault(ServiceException):
    """The SNS topic is invalid."""

    code: str = "SNSInvalidTopicFault"
    sender_fault: bool = False
    status_code: int = 400


class SNSNoAuthorizationFault(ServiceException):
    """You are not authorized for the SNS subscription."""

    code: str = "SNSNoAuthorizationFault"
    sender_fault: bool = False
    status_code: int = 400


class StorageQuotaExceededFault(ServiceException):
    """The storage quota has been exceeded."""

    code: str = "StorageQuotaExceededFault"
    sender_fault: bool = False
    status_code: int = 400


class SubnetAlreadyInUse(ServiceException):
    """The specified subnet is already in use."""

    code: str = "SubnetAlreadyInUse"
    sender_fault: bool = False
    status_code: int = 400


class UpgradeDependencyFailureFault(ServiceException):
    """An upgrade dependency is preventing the database migration."""

    code: str = "UpgradeDependencyFailureFault"
    sender_fault: bool = False
    status_code: int = 400


Long = int


class AccountQuota(TypedDict, total=False):
    """Describes a quota for an Amazon Web Services account, for example the
    number of replication instances allowed.
    """

    AccountQuotaName: Optional[String]
    Used: Optional[Long]
    Max: Optional[Long]


AccountQuotaList = List[AccountQuota]


class Tag(TypedDict, total=False):
    """A user-defined key-value pair that describes metadata added to an DMS
    resource and that is used by operations such as the following:

    -  ``AddTagsToResource``

    -  ``ListTagsForResource``

    -  ``RemoveTagsFromResource``
    """

    Key: Optional[String]
    Value: Optional[String]
    ResourceArn: Optional[String]


TagList = List[Tag]


class AddTagsToResourceMessage(ServiceRequest):
    """Associates a set of tags with an DMS resource."""

    ResourceArn: String
    Tags: TagList


class AddTagsToResourceResponse(TypedDict, total=False):
    pass


class ApplyPendingMaintenanceActionMessage(ServiceRequest):
    ReplicationInstanceArn: String
    ApplyAction: String
    OptInType: String


TStamp = datetime


class PendingMaintenanceAction(TypedDict, total=False):
    """Describes a maintenance action pending for an DMS resource, including
    when and how it will be applied. This data type is a response element to
    the ``DescribePendingMaintenanceActions`` operation.
    """

    Action: Optional[String]
    AutoAppliedAfterDate: Optional[TStamp]
    ForcedApplyDate: Optional[TStamp]
    OptInStatus: Optional[String]
    CurrentApplyDate: Optional[TStamp]
    Description: Optional[String]


PendingMaintenanceActionDetails = List[PendingMaintenanceAction]


class ResourcePendingMaintenanceActions(TypedDict, total=False):
    """Identifies an DMS resource and any pending actions for it."""

    ResourceIdentifier: Optional[String]
    PendingMaintenanceActionDetails: Optional[PendingMaintenanceActionDetails]


class ApplyPendingMaintenanceActionResponse(TypedDict, total=False):
    ResourcePendingMaintenanceActions: Optional[ResourcePendingMaintenanceActions]


ArnList = List[String]
AssessmentReportTypesList = List[AssessmentReportType]


class AvailabilityZone(TypedDict, total=False):
    """The name of an Availability Zone for use during database migration.
    ``AvailabilityZone`` is an optional parameter to the
    ```CreateReplicationInstance`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationInstance.html>`__
    operation, and it’s value relates to the Amazon Web Services Region of
    an endpoint. For example, the availability zone of an endpoint in the
    us-east-1 region might be us-east-1a, us-east-1b, us-east-1c, or
    us-east-1d.
    """

    Name: Optional[String]


AvailabilityZonesList = List[String]
AvailableUpgradesList = List[String]


class BatchStartRecommendationsErrorEntry(TypedDict, total=False):
    """Provides information about the errors that occurred during the analysis
    of the source database.
    """

    DatabaseId: Optional[String]
    Message: Optional[String]
    Code: Optional[String]


BatchStartRecommendationsErrorEntryList = List[BatchStartRecommendationsErrorEntry]


class RecommendationSettings(TypedDict, total=False):
    """Provides information about the required target engine settings."""

    InstanceSizingType: String
    WorkloadType: String


class StartRecommendationsRequestEntry(TypedDict, total=False):
    """Provides information about the source database to analyze and provide
    target recommendations according to the specified requirements.
    """

    DatabaseId: String
    Settings: RecommendationSettings


StartRecommendationsRequestEntryList = List[StartRecommendationsRequestEntry]


class BatchStartRecommendationsRequest(ServiceRequest):
    Data: Optional[StartRecommendationsRequestEntryList]


class BatchStartRecommendationsResponse(TypedDict, total=False):
    ErrorEntries: Optional[BatchStartRecommendationsErrorEntryList]


class CancelReplicationTaskAssessmentRunMessage(ServiceRequest):
    ReplicationTaskAssessmentRunArn: String


class ReplicationTaskAssessmentRunResultStatistic(TypedDict, total=False):
    """The object containing the result statistics for a completed assessment
    run.
    """

    Passed: Optional[Integer]
    Failed: Optional[Integer]
    Error: Optional[Integer]
    Warning: Optional[Integer]
    Cancelled: Optional[Integer]
    Skipped: Optional[Integer]


class ReplicationTaskAssessmentRunProgress(TypedDict, total=False):
    """The progress values reported by the ``AssessmentProgress`` response
    element.
    """

    IndividualAssessmentCount: Optional[Integer]
    IndividualAssessmentCompletedCount: Optional[Integer]


class ReplicationTaskAssessmentRun(TypedDict, total=False):
    """Provides information that describes a premigration assessment run that
    you have started using the ``StartReplicationTaskAssessmentRun``
    operation.

    Some of the information appears based on other operations that can
    return the ``ReplicationTaskAssessmentRun`` object.
    """

    ReplicationTaskAssessmentRunArn: Optional[String]
    ReplicationTaskArn: Optional[String]
    Status: Optional[String]
    ReplicationTaskAssessmentRunCreationDate: Optional[TStamp]
    AssessmentProgress: Optional[ReplicationTaskAssessmentRunProgress]
    LastFailureMessage: Optional[String]
    ServiceAccessRoleArn: Optional[String]
    ResultLocationBucket: Optional[String]
    ResultLocationFolder: Optional[String]
    ResultEncryptionMode: Optional[String]
    ResultKmsKeyArn: Optional[String]
    AssessmentRunName: Optional[String]
    IsLatestTaskAssessmentRun: Optional[Boolean]
    ResultStatistic: Optional[ReplicationTaskAssessmentRunResultStatistic]


class CancelReplicationTaskAssessmentRunResponse(TypedDict, total=False):
    ReplicationTaskAssessmentRun: Optional[ReplicationTaskAssessmentRun]


CertificateWallet = bytes


class Certificate(TypedDict, total=False):
    """The SSL certificate that can be used to encrypt connections between the
    endpoints and the replication instance.
    """

    CertificateIdentifier: Optional[String]
    CertificateCreationDate: Optional[TStamp]
    CertificatePem: Optional[String]
    CertificateWallet: Optional[CertificateWallet]
    CertificateArn: Optional[String]
    CertificateOwner: Optional[String]
    ValidFromDate: Optional[TStamp]
    ValidToDate: Optional[TStamp]
    SigningAlgorithm: Optional[String]
    KeyLength: Optional[IntegerOptional]


CertificateList = List[Certificate]


class CollectorHealthCheck(TypedDict, total=False):
    """Describes the last Fleet Advisor collector health check."""

    CollectorStatus: Optional[CollectorStatus]
    LocalCollectorS3Access: Optional[BooleanOptional]
    WebCollectorS3Access: Optional[BooleanOptional]
    WebCollectorGrantedRoleBasedAccess: Optional[BooleanOptional]


class InventoryData(TypedDict, total=False):
    """Describes a Fleet Advisor collector inventory."""

    NumberOfDatabases: Optional[IntegerOptional]
    NumberOfSchemas: Optional[IntegerOptional]


class CollectorResponse(TypedDict, total=False):
    """Describes a Fleet Advisor collector."""

    CollectorReferencedId: Optional[String]
    CollectorName: Optional[String]
    CollectorVersion: Optional[String]
    VersionStatus: Optional[VersionStatus]
    Description: Optional[String]
    S3BucketName: Optional[String]
    ServiceAccessRoleArn: Optional[String]
    CollectorHealthCheck: Optional[CollectorHealthCheck]
    LastDataReceived: Optional[String]
    RegisteredDate: Optional[String]
    CreatedDate: Optional[String]
    ModifiedDate: Optional[String]
    InventoryData: Optional[InventoryData]


CollectorResponses = List[CollectorResponse]


class CollectorShortInfoResponse(TypedDict, total=False):
    """Briefly describes a Fleet Advisor collector."""

    CollectorReferencedId: Optional[String]
    CollectorName: Optional[String]


CollectorsList = List[CollectorShortInfoResponse]
StringList = List[String]


class ComputeConfig(TypedDict, total=False):
    """Configuration parameters for provisioning an DMS Serverless replication."""

    AvailabilityZone: Optional[String]
    DnsNameServers: Optional[String]
    KmsKeyId: Optional[String]
    MaxCapacityUnits: Optional[IntegerOptional]
    MinCapacityUnits: Optional[IntegerOptional]
    MultiAZ: Optional[BooleanOptional]
    PreferredMaintenanceWindow: Optional[String]
    ReplicationSubnetGroupId: Optional[String]
    VpcSecurityGroupIds: Optional[StringList]


class Connection(TypedDict, total=False):
    """Status of the connection between an endpoint and a replication instance,
    including Amazon Resource Names (ARNs) and the last error message
    issued.
    """

    ReplicationInstanceArn: Optional[String]
    EndpointArn: Optional[String]
    Status: Optional[String]
    LastFailureMessage: Optional[String]
    EndpointIdentifier: Optional[String]
    ReplicationInstanceIdentifier: Optional[String]


ConnectionList = List[Connection]


class TargetDataSetting(TypedDict, total=False):
    """Defines settings for a target data provider for a data migration."""

    TablePreparationMode: Optional[TablePreparationMode]


TargetDataSettings = List[TargetDataSetting]
Iso8601DateTime = datetime


class SourceDataSetting(TypedDict, total=False):
    """Defines settings for a source data provider for a data migration."""

    CDCStartPosition: Optional[String]
    CDCStartTime: Optional[Iso8601DateTime]
    CDCStopTime: Optional[Iso8601DateTime]
    SlotName: Optional[String]


SourceDataSettings = List[SourceDataSetting]


class CreateDataMigrationMessage(ServiceRequest):
    DataMigrationName: Optional[String]
    MigrationProjectIdentifier: String
    DataMigrationType: MigrationTypeValue
    ServiceAccessRoleArn: String
    EnableCloudwatchLogs: Optional[BooleanOptional]
    SourceDataSettings: Optional[SourceDataSettings]
    TargetDataSettings: Optional[TargetDataSettings]
    NumberOfJobs: Optional[IntegerOptional]
    Tags: Optional[TagList]
    SelectionRules: Optional[SecretString]


DataMigrationCidrBlock = List[String]
PublicIpAddressList = List[String]


class DataMigrationStatistics(TypedDict, total=False):
    """Information about the data migration run, including start and stop time,
    latency, and migration progress.
    """

    TablesLoaded: Optional[Integer]
    ElapsedTimeMillis: Optional[Long]
    TablesLoading: Optional[Integer]
    FullLoadPercentage: Optional[Integer]
    CDCLatency: Optional[Integer]
    TablesQueued: Optional[Integer]
    TablesErrored: Optional[Integer]
    StartTime: Optional[Iso8601DateTime]
    StopTime: Optional[Iso8601DateTime]


class DataMigrationSettings(TypedDict, total=False):
    """Options for configuring a data migration, including whether to enable
    CloudWatch logs, and the selection rules to use to include or exclude
    database objects from the migration.
    """

    NumberOfJobs: Optional[IntegerOptional]
    CloudwatchLogsEnabled: Optional[BooleanOptional]
    SelectionRules: Optional[SecretString]


class DataMigration(TypedDict, total=False):
    """This object provides information about a DMS data migration."""

    DataMigrationName: Optional[String]
    DataMigrationArn: Optional[String]
    DataMigrationCreateTime: Optional[Iso8601DateTime]
    DataMigrationStartTime: Optional[Iso8601DateTime]
    DataMigrationEndTime: Optional[Iso8601DateTime]
    ServiceAccessRoleArn: Optional[String]
    MigrationProjectArn: Optional[String]
    DataMigrationType: Optional[MigrationTypeValue]
    DataMigrationSettings: Optional[DataMigrationSettings]
    SourceDataSettings: Optional[SourceDataSettings]
    TargetDataSettings: Optional[TargetDataSettings]
    DataMigrationStatistics: Optional[DataMigrationStatistics]
    DataMigrationStatus: Optional[String]
    PublicIpAddresses: Optional[PublicIpAddressList]
    DataMigrationCidrBlocks: Optional[DataMigrationCidrBlock]
    LastFailureMessage: Optional[String]
    StopReason: Optional[String]


class CreateDataMigrationResponse(TypedDict, total=False):
    DataMigration: Optional[DataMigration]


class MongoDbDataProviderSettings(TypedDict, total=False):
    """Provides information that defines a MongoDB data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]
    AuthType: Optional[AuthTypeValue]
    AuthSource: Optional[String]
    AuthMechanism: Optional[AuthMechanismValue]


class IbmDb2zOsDataProviderSettings(TypedDict, total=False):
    """Provides information about an IBM DB2 for z/OS data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class IbmDb2LuwDataProviderSettings(TypedDict, total=False):
    """Provides information about an IBM DB2 LUW data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class MariaDbDataProviderSettings(TypedDict, total=False):
    """Provides information that defines a MariaDB data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class DocDbDataProviderSettings(TypedDict, total=False):
    """Provides information that defines a DocumentDB data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class MicrosoftSqlServerDataProviderSettings(TypedDict, total=False):
    """Provides information that defines a Microsoft SQL Server data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class OracleDataProviderSettings(TypedDict, total=False):
    """Provides information that defines an Oracle data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]
    AsmServer: Optional[String]
    SecretsManagerOracleAsmSecretId: Optional[String]
    SecretsManagerOracleAsmAccessRoleArn: Optional[String]
    SecretsManagerSecurityDbEncryptionSecretId: Optional[String]
    SecretsManagerSecurityDbEncryptionAccessRoleArn: Optional[String]


class MySqlDataProviderSettings(TypedDict, total=False):
    """Provides information that defines a MySQL data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class PostgreSqlDataProviderSettings(TypedDict, total=False):
    """Provides information that defines a PostgreSQL data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    CertificateArn: Optional[String]


class RedshiftDataProviderSettings(TypedDict, total=False):
    """Provides information that defines an Amazon Redshift data provider."""

    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]


class DataProviderSettings(TypedDict, total=False):
    """Provides information that defines a data provider."""

    RedshiftSettings: Optional[RedshiftDataProviderSettings]
    PostgreSqlSettings: Optional[PostgreSqlDataProviderSettings]
    MySqlSettings: Optional[MySqlDataProviderSettings]
    OracleSettings: Optional[OracleDataProviderSettings]
    MicrosoftSqlServerSettings: Optional[MicrosoftSqlServerDataProviderSettings]
    DocDbSettings: Optional[DocDbDataProviderSettings]
    MariaDbSettings: Optional[MariaDbDataProviderSettings]
    IbmDb2LuwSettings: Optional[IbmDb2LuwDataProviderSettings]
    IbmDb2zOsSettings: Optional[IbmDb2zOsDataProviderSettings]
    MongoDbSettings: Optional[MongoDbDataProviderSettings]


class CreateDataProviderMessage(ServiceRequest):
    DataProviderName: Optional[String]
    Description: Optional[String]
    Engine: String
    Settings: DataProviderSettings
    Tags: Optional[TagList]


class DataProvider(TypedDict, total=False):
    """Provides information that defines a data provider."""

    DataProviderName: Optional[String]
    DataProviderArn: Optional[String]
    DataProviderCreationTime: Optional[Iso8601DateTime]
    Description: Optional[String]
    Engine: Optional[String]
    Settings: Optional[DataProviderSettings]


class CreateDataProviderResponse(TypedDict, total=False):
    DataProvider: Optional[DataProvider]


class TimestreamSettings(TypedDict, total=False):
    """Provides information that defines an Amazon Timestream endpoint."""

    DatabaseName: String
    MemoryDuration: IntegerOptional
    MagneticDuration: IntegerOptional
    CdcInsertsAndUpdates: Optional[BooleanOptional]
    EnableMagneticStoreWrites: Optional[BooleanOptional]


class GcpMySQLSettings(TypedDict, total=False):
    """Settings in JSON format for the source GCP MySQL endpoint."""

    AfterConnectScript: Optional[String]
    CleanSourceMetadataOnMismatch: Optional[BooleanOptional]
    DatabaseName: Optional[String]
    EventsPollInterval: Optional[IntegerOptional]
    TargetDbType: Optional[TargetDbType]
    MaxFileSize: Optional[IntegerOptional]
    ParallelLoadThreads: Optional[IntegerOptional]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    ServerName: Optional[String]
    ServerTimezone: Optional[String]
    Username: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]


class RedisSettings(TypedDict, total=False):
    """Provides information that defines a Redis target endpoint."""

    ServerName: String
    Port: Integer
    SslSecurityProtocol: Optional[SslSecurityProtocolValue]
    AuthType: Optional[RedisAuthTypeValue]
    AuthUserName: Optional[String]
    AuthPassword: Optional[SecretString]
    SslCaCertificateArn: Optional[String]


class DocDbSettings(TypedDict, total=False):
    """Provides information that defines a DocumentDB endpoint."""

    Username: Optional[String]
    Password: Optional[SecretString]
    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    NestingLevel: Optional[NestingLevelValue]
    ExtractDocId: Optional[BooleanOptional]
    DocsToInvestigate: Optional[IntegerOptional]
    KmsKeyId: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    UseUpdateLookUp: Optional[BooleanOptional]
    ReplicateShardCollections: Optional[BooleanOptional]


class IBMDb2Settings(TypedDict, total=False):
    """Provides information that defines an IBM Db2 LUW endpoint."""

    DatabaseName: Optional[String]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    ServerName: Optional[String]
    SetDataCaptureChanges: Optional[BooleanOptional]
    CurrentLsn: Optional[String]
    MaxKBytesPerRead: Optional[IntegerOptional]
    Username: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    LoadTimeout: Optional[IntegerOptional]
    WriteBufferSize: Optional[IntegerOptional]
    MaxFileSize: Optional[IntegerOptional]
    KeepCsvFiles: Optional[BooleanOptional]


class MicrosoftSQLServerSettings(TypedDict, total=False):
    """Provides information that defines a Microsoft SQL Server endpoint."""

    Port: Optional[IntegerOptional]
    BcpPacketSize: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    ControlTablesFileGroup: Optional[String]
    Password: Optional[SecretString]
    QuerySingleAlwaysOnNode: Optional[BooleanOptional]
    ReadBackupOnly: Optional[BooleanOptional]
    SafeguardPolicy: Optional[SafeguardPolicy]
    ServerName: Optional[String]
    Username: Optional[String]
    UseBcpFullLoad: Optional[BooleanOptional]
    UseThirdPartyBackupDevice: Optional[BooleanOptional]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    TrimSpaceInChar: Optional[BooleanOptional]
    TlogAccessMode: Optional[TlogAccessMode]
    ForceLobLookup: Optional[BooleanOptional]
    AuthenticationMethod: Optional[SqlServerAuthenticationMethod]


class SybaseSettings(TypedDict, total=False):
    """Provides information that defines a SAP ASE endpoint."""

    DatabaseName: Optional[String]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    ServerName: Optional[String]
    Username: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]


IntegerList = List[Integer]


class OracleSettings(TypedDict, total=False):
    """Provides information that defines an Oracle endpoint."""

    AddSupplementalLogging: Optional[BooleanOptional]
    ArchivedLogDestId: Optional[IntegerOptional]
    AdditionalArchivedLogDestId: Optional[IntegerOptional]
    ExtraArchivedLogDestIds: Optional[IntegerList]
    AllowSelectNestedTables: Optional[BooleanOptional]
    ParallelAsmReadThreads: Optional[IntegerOptional]
    ReadAheadBlocks: Optional[IntegerOptional]
    AccessAlternateDirectly: Optional[BooleanOptional]
    UseAlternateFolderForOnline: Optional[BooleanOptional]
    OraclePathPrefix: Optional[String]
    UsePathPrefix: Optional[String]
    ReplacePathPrefix: Optional[BooleanOptional]
    EnableHomogenousTablespace: Optional[BooleanOptional]
    DirectPathNoLog: Optional[BooleanOptional]
    ArchivedLogsOnly: Optional[BooleanOptional]
    AsmPassword: Optional[SecretString]
    AsmServer: Optional[String]
    AsmUser: Optional[String]
    CharLengthSemantics: Optional[CharLengthSemantics]
    DatabaseName: Optional[String]
    DirectPathParallelLoad: Optional[BooleanOptional]
    FailTasksOnLobTruncation: Optional[BooleanOptional]
    NumberDatatypeScale: Optional[IntegerOptional]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    ReadTableSpaceName: Optional[BooleanOptional]
    RetryInterval: Optional[IntegerOptional]
    SecurityDbEncryption: Optional[SecretString]
    SecurityDbEncryptionName: Optional[String]
    ServerName: Optional[String]
    SpatialDataOptionToGeoJsonFunctionName: Optional[String]
    StandbyDelayTime: Optional[IntegerOptional]
    Username: Optional[String]
    UseBFile: Optional[BooleanOptional]
    UseDirectPathFullLoad: Optional[BooleanOptional]
    UseLogminerReader: Optional[BooleanOptional]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    SecretsManagerOracleAsmAccessRoleArn: Optional[String]
    SecretsManagerOracleAsmSecretId: Optional[String]
    TrimSpaceInChar: Optional[BooleanOptional]
    ConvertTimestampWithZoneToUTC: Optional[BooleanOptional]
    OpenTransactionWindow: Optional[IntegerOptional]
    AuthenticationMethod: Optional[OracleAuthenticationMethod]


class MySQLSettings(TypedDict, total=False):
    """Provides information that defines a MySQL endpoint."""

    AfterConnectScript: Optional[String]
    CleanSourceMetadataOnMismatch: Optional[BooleanOptional]
    DatabaseName: Optional[String]
    EventsPollInterval: Optional[IntegerOptional]
    TargetDbType: Optional[TargetDbType]
    MaxFileSize: Optional[IntegerOptional]
    ParallelLoadThreads: Optional[IntegerOptional]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    ServerName: Optional[String]
    ServerTimezone: Optional[String]
    Username: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    ExecuteTimeout: Optional[IntegerOptional]
    ServiceAccessRoleArn: Optional[String]
    AuthenticationMethod: Optional[MySQLAuthenticationMethod]


class PostgreSQLSettings(TypedDict, total=False):
    """Provides information that defines a PostgreSQL endpoint."""

    AfterConnectScript: Optional[String]
    CaptureDdls: Optional[BooleanOptional]
    MaxFileSize: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    DdlArtifactsSchema: Optional[String]
    ExecuteTimeout: Optional[IntegerOptional]
    FailTasksOnLobTruncation: Optional[BooleanOptional]
    HeartbeatEnable: Optional[BooleanOptional]
    HeartbeatSchema: Optional[String]
    HeartbeatFrequency: Optional[IntegerOptional]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    ServerName: Optional[String]
    Username: Optional[String]
    SlotName: Optional[String]
    PluginName: Optional[PluginNameValue]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    TrimSpaceInChar: Optional[BooleanOptional]
    MapBooleanAsBoolean: Optional[BooleanOptional]
    MapJsonbAsClob: Optional[BooleanOptional]
    MapLongVarcharAs: Optional[LongVarcharMappingType]
    DatabaseMode: Optional[DatabaseMode]
    BabelfishDatabaseName: Optional[String]
    DisableUnicodeSourceFilter: Optional[BooleanOptional]
    ServiceAccessRoleArn: Optional[String]
    AuthenticationMethod: Optional[PostgreSQLAuthenticationMethod]


class RedshiftSettings(TypedDict, total=False):
    """Provides information that defines an Amazon Redshift endpoint."""

    AcceptAnyDate: Optional[BooleanOptional]
    AfterConnectScript: Optional[String]
    BucketFolder: Optional[String]
    BucketName: Optional[String]
    CaseSensitiveNames: Optional[BooleanOptional]
    CompUpdate: Optional[BooleanOptional]
    ConnectionTimeout: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    DateFormat: Optional[String]
    EmptyAsNull: Optional[BooleanOptional]
    EncryptionMode: Optional[EncryptionModeValue]
    ExplicitIds: Optional[BooleanOptional]
    FileTransferUploadStreams: Optional[IntegerOptional]
    LoadTimeout: Optional[IntegerOptional]
    MaxFileSize: Optional[IntegerOptional]
    Password: Optional[SecretString]
    Port: Optional[IntegerOptional]
    RemoveQuotes: Optional[BooleanOptional]
    ReplaceInvalidChars: Optional[String]
    ReplaceChars: Optional[String]
    ServerName: Optional[String]
    ServiceAccessRoleArn: Optional[String]
    ServerSideEncryptionKmsKeyId: Optional[String]
    TimeFormat: Optional[String]
    TrimBlanks: Optional[BooleanOptional]
    TruncateColumns: Optional[BooleanOptional]
    Username: Optional[String]
    WriteBufferSize: Optional[IntegerOptional]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    MapBooleanAsBoolean: Optional[BooleanOptional]


class NeptuneSettings(TypedDict, total=False):
    """Provides information that defines an Amazon Neptune endpoint."""

    ServiceAccessRoleArn: Optional[String]
    S3BucketName: String
    S3BucketFolder: String
    ErrorRetryDuration: Optional[IntegerOptional]
    MaxFileSize: Optional[IntegerOptional]
    MaxRetryCount: Optional[IntegerOptional]
    IamAuthEnabled: Optional[BooleanOptional]


class ElasticsearchSettings(TypedDict, total=False):
    """Provides information that defines an OpenSearch endpoint."""

    ServiceAccessRoleArn: String
    EndpointUri: String
    FullLoadErrorPercentage: Optional[IntegerOptional]
    ErrorRetryDuration: Optional[IntegerOptional]
    UseNewMappingType: Optional[BooleanOptional]


class KafkaSettings(TypedDict, total=False):
    """Provides information that describes an Apache Kafka endpoint. This
    information includes the output format of records applied to the
    endpoint and details of transaction and control table data information.
    """

    Broker: Optional[String]
    Topic: Optional[String]
    MessageFormat: Optional[MessageFormatValue]
    IncludeTransactionDetails: Optional[BooleanOptional]
    IncludePartitionValue: Optional[BooleanOptional]
    PartitionIncludeSchemaTable: Optional[BooleanOptional]
    IncludeTableAlterOperations: Optional[BooleanOptional]
    IncludeControlDetails: Optional[BooleanOptional]
    MessageMaxBytes: Optional[IntegerOptional]
    IncludeNullAndEmpty: Optional[BooleanOptional]
    SecurityProtocol: Optional[KafkaSecurityProtocol]
    SslClientCertificateArn: Optional[String]
    SslClientKeyArn: Optional[String]
    SslClientKeyPassword: Optional[SecretString]
    SslCaCertificateArn: Optional[String]
    SaslUsername: Optional[String]
    SaslPassword: Optional[SecretString]
    NoHexPrefix: Optional[BooleanOptional]
    SaslMechanism: Optional[KafkaSaslMechanism]
    SslEndpointIdentificationAlgorithm: Optional[KafkaSslEndpointIdentificationAlgorithm]
    UseLargeIntegerValue: Optional[BooleanOptional]


class KinesisSettings(TypedDict, total=False):
    """Provides information that describes an Amazon Kinesis Data Stream
    endpoint. This information includes the output format of records applied
    to the endpoint and details of transaction and control table data
    information.
    """

    StreamArn: Optional[String]
    MessageFormat: Optional[MessageFormatValue]
    ServiceAccessRoleArn: Optional[String]
    IncludeTransactionDetails: Optional[BooleanOptional]
    IncludePartitionValue: Optional[BooleanOptional]
    PartitionIncludeSchemaTable: Optional[BooleanOptional]
    IncludeTableAlterOperations: Optional[BooleanOptional]
    IncludeControlDetails: Optional[BooleanOptional]
    IncludeNullAndEmpty: Optional[BooleanOptional]
    NoHexPrefix: Optional[BooleanOptional]
    UseLargeIntegerValue: Optional[BooleanOptional]


class MongoDbSettings(TypedDict, total=False):
    """Provides information that defines a MongoDB endpoint."""

    Username: Optional[String]
    Password: Optional[SecretString]
    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    AuthType: Optional[AuthTypeValue]
    AuthMechanism: Optional[AuthMechanismValue]
    NestingLevel: Optional[NestingLevelValue]
    ExtractDocId: Optional[String]
    DocsToInvestigate: Optional[String]
    AuthSource: Optional[String]
    KmsKeyId: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    SecretsManagerSecretId: Optional[String]
    UseUpdateLookUp: Optional[BooleanOptional]
    ReplicateShardCollections: Optional[BooleanOptional]


class DmsTransferSettings(TypedDict, total=False):
    """The settings in JSON format for the DMS Transfer type source endpoint."""

    ServiceAccessRoleArn: Optional[String]
    BucketName: Optional[String]


class S3Settings(TypedDict, total=False):
    """Settings for exporting data to Amazon S3."""

    ServiceAccessRoleArn: Optional[String]
    ExternalTableDefinition: Optional[String]
    CsvRowDelimiter: Optional[String]
    CsvDelimiter: Optional[String]
    BucketFolder: Optional[String]
    BucketName: Optional[String]
    CompressionType: Optional[CompressionTypeValue]
    EncryptionMode: Optional[EncryptionModeValue]
    ServerSideEncryptionKmsKeyId: Optional[String]
    DataFormat: Optional[DataFormatValue]
    EncodingType: Optional[EncodingTypeValue]
    DictPageSizeLimit: Optional[IntegerOptional]
    RowGroupLength: Optional[IntegerOptional]
    DataPageSize: Optional[IntegerOptional]
    ParquetVersion: Optional[ParquetVersionValue]
    EnableStatistics: Optional[BooleanOptional]
    IncludeOpForFullLoad: Optional[BooleanOptional]
    CdcInsertsOnly: Optional[BooleanOptional]
    TimestampColumnName: Optional[String]
    ParquetTimestampInMillisecond: Optional[BooleanOptional]
    CdcInsertsAndUpdates: Optional[BooleanOptional]
    DatePartitionEnabled: Optional[BooleanOptional]
    DatePartitionSequence: Optional[DatePartitionSequenceValue]
    DatePartitionDelimiter: Optional[DatePartitionDelimiterValue]
    UseCsvNoSupValue: Optional[BooleanOptional]
    CsvNoSupValue: Optional[String]
    PreserveTransactions: Optional[BooleanOptional]
    CdcPath: Optional[String]
    UseTaskStartTimeForFullLoadTimestamp: Optional[BooleanOptional]
    CannedAclForObjects: Optional[CannedAclForObjectsValue]
    AddColumnName: Optional[BooleanOptional]
    CdcMaxBatchInterval: Optional[IntegerOptional]
    CdcMinFileSize: Optional[IntegerOptional]
    CsvNullValue: Optional[String]
    IgnoreHeaderRows: Optional[IntegerOptional]
    MaxFileSize: Optional[IntegerOptional]
    Rfc4180: Optional[BooleanOptional]
    DatePartitionTimezone: Optional[String]
    AddTrailingPaddingCharacter: Optional[BooleanOptional]
    ExpectedBucketOwner: Optional[String]
    GlueCatalogGeneration: Optional[BooleanOptional]


class DynamoDbSettings(TypedDict, total=False):
    """Provides the Amazon Resource Name (ARN) of the Identity and Access
    Management (IAM) role used to define an Amazon DynamoDB target endpoint.
    """

    ServiceAccessRoleArn: String


class CreateEndpointMessage(ServiceRequest):
    EndpointIdentifier: String
    EndpointType: ReplicationEndpointTypeValue
    EngineName: String
    Username: Optional[String]
    Password: Optional[SecretString]
    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    ExtraConnectionAttributes: Optional[String]
    KmsKeyId: Optional[String]
    Tags: Optional[TagList]
    CertificateArn: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    ServiceAccessRoleArn: Optional[String]
    ExternalTableDefinition: Optional[String]
    DynamoDbSettings: Optional[DynamoDbSettings]
    S3Settings: Optional[S3Settings]
    DmsTransferSettings: Optional[DmsTransferSettings]
    MongoDbSettings: Optional[MongoDbSettings]
    KinesisSettings: Optional[KinesisSettings]
    KafkaSettings: Optional[KafkaSettings]
    ElasticsearchSettings: Optional[ElasticsearchSettings]
    NeptuneSettings: Optional[NeptuneSettings]
    RedshiftSettings: Optional[RedshiftSettings]
    PostgreSQLSettings: Optional[PostgreSQLSettings]
    MySQLSettings: Optional[MySQLSettings]
    OracleSettings: Optional[OracleSettings]
    SybaseSettings: Optional[SybaseSettings]
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettings]
    IBMDb2Settings: Optional[IBMDb2Settings]
    ResourceIdentifier: Optional[String]
    DocDbSettings: Optional[DocDbSettings]
    RedisSettings: Optional[RedisSettings]
    GcpMySQLSettings: Optional[GcpMySQLSettings]
    TimestreamSettings: Optional[TimestreamSettings]


class Endpoint(TypedDict, total=False):
    """Describes an endpoint of a database instance in response to operations
    such as the following:

    -  ``CreateEndpoint``

    -  ``DescribeEndpoint``

    -  ``ModifyEndpoint``
    """

    EndpointIdentifier: Optional[String]
    EndpointType: Optional[ReplicationEndpointTypeValue]
    EngineName: Optional[String]
    EngineDisplayName: Optional[String]
    Username: Optional[String]
    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    ExtraConnectionAttributes: Optional[String]
    Status: Optional[String]
    KmsKeyId: Optional[String]
    EndpointArn: Optional[String]
    CertificateArn: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    ServiceAccessRoleArn: Optional[String]
    ExternalTableDefinition: Optional[String]
    ExternalId: Optional[String]
    DynamoDbSettings: Optional[DynamoDbSettings]
    S3Settings: Optional[S3Settings]
    DmsTransferSettings: Optional[DmsTransferSettings]
    MongoDbSettings: Optional[MongoDbSettings]
    KinesisSettings: Optional[KinesisSettings]
    KafkaSettings: Optional[KafkaSettings]
    ElasticsearchSettings: Optional[ElasticsearchSettings]
    NeptuneSettings: Optional[NeptuneSettings]
    RedshiftSettings: Optional[RedshiftSettings]
    PostgreSQLSettings: Optional[PostgreSQLSettings]
    MySQLSettings: Optional[MySQLSettings]
    OracleSettings: Optional[OracleSettings]
    SybaseSettings: Optional[SybaseSettings]
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettings]
    IBMDb2Settings: Optional[IBMDb2Settings]
    DocDbSettings: Optional[DocDbSettings]
    RedisSettings: Optional[RedisSettings]
    GcpMySQLSettings: Optional[GcpMySQLSettings]
    TimestreamSettings: Optional[TimestreamSettings]


class CreateEndpointResponse(TypedDict, total=False):
    Endpoint: Optional[Endpoint]


SourceIdsList = List[String]
EventCategoriesList = List[String]


class CreateEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SnsTopicArn: String
    SourceType: Optional[String]
    EventCategories: Optional[EventCategoriesList]
    SourceIds: Optional[SourceIdsList]
    Enabled: Optional[BooleanOptional]
    Tags: Optional[TagList]


class EventSubscription(TypedDict, total=False):
    """Describes an event notification subscription created by the
    ``CreateEventSubscription`` operation.
    """

    CustomerAwsId: Optional[String]
    CustSubscriptionId: Optional[String]
    SnsTopicArn: Optional[String]
    Status: Optional[String]
    SubscriptionCreationTime: Optional[String]
    SourceType: Optional[String]
    SourceIdsList: Optional[SourceIdsList]
    EventCategoriesList: Optional[EventCategoriesList]
    Enabled: Optional[Boolean]


class CreateEventSubscriptionResponse(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class CreateFleetAdvisorCollectorRequest(ServiceRequest):
    CollectorName: String
    Description: Optional[String]
    ServiceAccessRoleArn: String
    S3BucketName: String


class CreateFleetAdvisorCollectorResponse(TypedDict, total=False):
    CollectorReferencedId: Optional[String]
    CollectorName: Optional[String]
    Description: Optional[String]
    ServiceAccessRoleArn: Optional[String]
    S3BucketName: Optional[String]


class CreateInstanceProfileMessage(ServiceRequest):
    AvailabilityZone: Optional[String]
    KmsKeyArn: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    Tags: Optional[TagList]
    NetworkType: Optional[String]
    InstanceProfileName: Optional[String]
    Description: Optional[String]
    SubnetGroupIdentifier: Optional[String]
    VpcSecurityGroups: Optional[StringList]


class InstanceProfile(TypedDict, total=False):
    """Provides information that defines an instance profile."""

    InstanceProfileArn: Optional[String]
    AvailabilityZone: Optional[String]
    KmsKeyArn: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    NetworkType: Optional[String]
    InstanceProfileName: Optional[String]
    Description: Optional[String]
    InstanceProfileCreationTime: Optional[Iso8601DateTime]
    SubnetGroupIdentifier: Optional[String]
    VpcSecurityGroups: Optional[StringList]


class CreateInstanceProfileResponse(TypedDict, total=False):
    InstanceProfile: Optional[InstanceProfile]


class SCApplicationAttributes(TypedDict, total=False):
    """Provides information that defines a schema conversion application."""

    S3BucketPath: Optional[String]
    S3BucketRoleArn: Optional[String]


class DataProviderDescriptorDefinition(TypedDict, total=False):
    """Information about a data provider."""

    DataProviderIdentifier: String
    SecretsManagerSecretId: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]


DataProviderDescriptorDefinitionList = List[DataProviderDescriptorDefinition]


class CreateMigrationProjectMessage(ServiceRequest):
    MigrationProjectName: Optional[String]
    SourceDataProviderDescriptors: DataProviderDescriptorDefinitionList
    TargetDataProviderDescriptors: DataProviderDescriptorDefinitionList
    InstanceProfileIdentifier: String
    TransformationRules: Optional[String]
    Description: Optional[String]
    Tags: Optional[TagList]
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributes]


class DataProviderDescriptor(TypedDict, total=False):
    """Information about a data provider."""

    SecretsManagerSecretId: Optional[String]
    SecretsManagerAccessRoleArn: Optional[String]
    DataProviderName: Optional[String]
    DataProviderArn: Optional[String]


DataProviderDescriptorList = List[DataProviderDescriptor]


class MigrationProject(TypedDict, total=False):
    """Provides information that defines a migration project."""

    MigrationProjectName: Optional[String]
    MigrationProjectArn: Optional[String]
    MigrationProjectCreationTime: Optional[Iso8601DateTime]
    SourceDataProviderDescriptors: Optional[DataProviderDescriptorList]
    TargetDataProviderDescriptors: Optional[DataProviderDescriptorList]
    InstanceProfileArn: Optional[String]
    InstanceProfileName: Optional[String]
    TransformationRules: Optional[String]
    Description: Optional[String]
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributes]


class CreateMigrationProjectResponse(TypedDict, total=False):
    MigrationProject: Optional[MigrationProject]


class CreateReplicationConfigMessage(ServiceRequest):
    ReplicationConfigIdentifier: String
    SourceEndpointArn: String
    TargetEndpointArn: String
    ComputeConfig: ComputeConfig
    ReplicationType: MigrationTypeValue
    TableMappings: String
    ReplicationSettings: Optional[String]
    SupplementalSettings: Optional[String]
    ResourceIdentifier: Optional[String]
    Tags: Optional[TagList]


class ReplicationConfig(TypedDict, total=False):
    """This object provides configuration information about a serverless
    replication.
    """

    ReplicationConfigIdentifier: Optional[String]
    ReplicationConfigArn: Optional[String]
    SourceEndpointArn: Optional[String]
    TargetEndpointArn: Optional[String]
    ReplicationType: Optional[MigrationTypeValue]
    ComputeConfig: Optional[ComputeConfig]
    ReplicationSettings: Optional[String]
    SupplementalSettings: Optional[String]
    TableMappings: Optional[String]
    ReplicationConfigCreateTime: Optional[TStamp]
    ReplicationConfigUpdateTime: Optional[TStamp]


class CreateReplicationConfigResponse(TypedDict, total=False):
    ReplicationConfig: Optional[ReplicationConfig]


class KerberosAuthenticationSettings(TypedDict, total=False):
    """Specifies the settings required for kerberos authentication when
    creating the replication instance.
    """

    KeyCacheSecretId: Optional[String]
    KeyCacheSecretIamArn: Optional[String]
    Krb5FileContents: Optional[String]


VpcSecurityGroupIdList = List[String]


class CreateReplicationInstanceMessage(ServiceRequest):
    ReplicationInstanceIdentifier: String
    AllocatedStorage: Optional[IntegerOptional]
    ReplicationInstanceClass: ReplicationInstanceClass
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    AvailabilityZone: Optional[String]
    ReplicationSubnetGroupIdentifier: Optional[String]
    PreferredMaintenanceWindow: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    Tags: Optional[TagList]
    KmsKeyId: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    DnsNameServers: Optional[String]
    ResourceIdentifier: Optional[String]
    NetworkType: Optional[String]
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettings]


ReplicationInstanceIpv6AddressList = List[String]
ReplicationInstancePrivateIpAddressList = List[String]
ReplicationInstancePublicIpAddressList = List[String]


class ReplicationPendingModifiedValues(TypedDict, total=False):
    """Provides information about the values of pending modifications to a
    replication instance. This data type is an object of the
    ```ReplicationInstance`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationInstance.html>`__
    user-defined data type.
    """

    ReplicationInstanceClass: Optional[ReplicationInstanceClass]
    AllocatedStorage: Optional[IntegerOptional]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    NetworkType: Optional[String]


class Subnet(TypedDict, total=False):
    """In response to a request by the ``DescribeReplicationSubnetGroups``
    operation, this object identifies a subnet by its given Availability
    Zone, subnet identifier, and status.
    """

    SubnetIdentifier: Optional[String]
    SubnetAvailabilityZone: Optional[AvailabilityZone]
    SubnetStatus: Optional[String]


SubnetList = List[Subnet]


class ReplicationSubnetGroup(TypedDict, total=False):
    """Describes a subnet group in response to a request by the
    ``DescribeReplicationSubnetGroups`` operation.
    """

    ReplicationSubnetGroupIdentifier: Optional[String]
    ReplicationSubnetGroupDescription: Optional[String]
    VpcId: Optional[String]
    SubnetGroupStatus: Optional[String]
    Subnets: Optional[SubnetList]
    SupportedNetworkTypes: Optional[StringList]


class VpcSecurityGroupMembership(TypedDict, total=False):
    """Describes the status of a security group associated with the virtual
    private cloud (VPC) hosting your replication and DB instances.
    """

    VpcSecurityGroupId: Optional[String]
    Status: Optional[String]


VpcSecurityGroupMembershipList = List[VpcSecurityGroupMembership]


class ReplicationInstance(TypedDict, total=False):
    """Provides information that defines a replication instance."""

    ReplicationInstanceIdentifier: Optional[String]
    ReplicationInstanceClass: Optional[ReplicationInstanceClass]
    ReplicationInstanceStatus: Optional[String]
    AllocatedStorage: Optional[Integer]
    InstanceCreateTime: Optional[TStamp]
    VpcSecurityGroups: Optional[VpcSecurityGroupMembershipList]
    AvailabilityZone: Optional[String]
    ReplicationSubnetGroup: Optional[ReplicationSubnetGroup]
    PreferredMaintenanceWindow: Optional[String]
    PendingModifiedValues: Optional[ReplicationPendingModifiedValues]
    MultiAZ: Optional[Boolean]
    EngineVersion: Optional[String]
    AutoMinorVersionUpgrade: Optional[Boolean]
    KmsKeyId: Optional[String]
    ReplicationInstanceArn: Optional[String]
    ReplicationInstancePublicIpAddress: Optional[String]
    ReplicationInstancePrivateIpAddress: Optional[String]
    ReplicationInstancePublicIpAddresses: Optional[ReplicationInstancePublicIpAddressList]
    ReplicationInstancePrivateIpAddresses: Optional[ReplicationInstancePrivateIpAddressList]
    ReplicationInstanceIpv6Addresses: Optional[ReplicationInstanceIpv6AddressList]
    PubliclyAccessible: Optional[Boolean]
    SecondaryAvailabilityZone: Optional[String]
    FreeUntil: Optional[TStamp]
    DnsNameServers: Optional[String]
    NetworkType: Optional[String]
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettings]


class CreateReplicationInstanceResponse(TypedDict, total=False):
    ReplicationInstance: Optional[ReplicationInstance]


SubnetIdentifierList = List[String]


class CreateReplicationSubnetGroupMessage(ServiceRequest):
    ReplicationSubnetGroupIdentifier: String
    ReplicationSubnetGroupDescription: String
    SubnetIds: SubnetIdentifierList
    Tags: Optional[TagList]


class CreateReplicationSubnetGroupResponse(TypedDict, total=False):
    ReplicationSubnetGroup: Optional[ReplicationSubnetGroup]


class CreateReplicationTaskMessage(ServiceRequest):
    ReplicationTaskIdentifier: String
    SourceEndpointArn: String
    TargetEndpointArn: String
    ReplicationInstanceArn: String
    MigrationType: MigrationTypeValue
    TableMappings: String
    ReplicationTaskSettings: Optional[String]
    CdcStartTime: Optional[TStamp]
    CdcStartPosition: Optional[String]
    CdcStopPosition: Optional[String]
    Tags: Optional[TagList]
    TaskData: Optional[String]
    ResourceIdentifier: Optional[String]


class ReplicationTaskStats(TypedDict, total=False):
    """In response to a request by the ``DescribeReplicationTasks`` operation,
    this object provides a collection of statistics about a replication
    task.
    """

    FullLoadProgressPercent: Optional[Integer]
    ElapsedTimeMillis: Optional[Long]
    TablesLoaded: Optional[Integer]
    TablesLoading: Optional[Integer]
    TablesQueued: Optional[Integer]
    TablesErrored: Optional[Integer]
    FreshStartDate: Optional[TStamp]
    StartDate: Optional[TStamp]
    StopDate: Optional[TStamp]
    FullLoadStartDate: Optional[TStamp]
    FullLoadFinishDate: Optional[TStamp]


class ReplicationTask(TypedDict, total=False):
    """Provides information that describes a replication task created by the
    ``CreateReplicationTask`` operation.
    """

    ReplicationTaskIdentifier: Optional[String]
    SourceEndpointArn: Optional[String]
    TargetEndpointArn: Optional[String]
    ReplicationInstanceArn: Optional[String]
    MigrationType: Optional[MigrationTypeValue]
    TableMappings: Optional[String]
    ReplicationTaskSettings: Optional[String]
    Status: Optional[String]
    LastFailureMessage: Optional[String]
    StopReason: Optional[String]
    ReplicationTaskCreationDate: Optional[TStamp]
    ReplicationTaskStartDate: Optional[TStamp]
    CdcStartPosition: Optional[String]
    CdcStopPosition: Optional[String]
    RecoveryCheckpoint: Optional[String]
    ReplicationTaskArn: Optional[String]
    ReplicationTaskStats: Optional[ReplicationTaskStats]
    TaskData: Optional[String]
    TargetReplicationInstanceArn: Optional[String]


class CreateReplicationTaskResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


DataMigrations = List[DataMigration]
DataProviderList = List[DataProvider]


class DatabaseInstanceSoftwareDetailsResponse(TypedDict, total=False):
    """Describes an inventory database instance for a Fleet Advisor collector."""

    Engine: Optional[String]
    EngineVersion: Optional[String]
    EngineEdition: Optional[String]
    ServicePack: Optional[String]
    SupportLevel: Optional[String]
    OsArchitecture: Optional[IntegerOptional]
    Tooltip: Optional[String]


class ServerShortInfoResponse(TypedDict, total=False):
    """Describes a server in a Fleet Advisor collector inventory."""

    ServerId: Optional[String]
    IpAddress: Optional[String]
    ServerName: Optional[String]


LongOptional = int


class DatabaseResponse(TypedDict, total=False):
    """Describes a database in a Fleet Advisor collector inventory."""

    DatabaseId: Optional[String]
    DatabaseName: Optional[String]
    IpAddress: Optional[String]
    NumberOfSchemas: Optional[LongOptional]
    Server: Optional[ServerShortInfoResponse]
    SoftwareDetails: Optional[DatabaseInstanceSoftwareDetailsResponse]
    Collectors: Optional[CollectorsList]


DatabaseList = List[DatabaseResponse]


class DatabaseShortInfoResponse(TypedDict, total=False):
    """Describes a database in a Fleet Advisor collector inventory."""

    DatabaseId: Optional[String]
    DatabaseName: Optional[String]
    DatabaseIpAddress: Optional[String]
    DatabaseEngine: Optional[String]


class DefaultErrorDetails(TypedDict, total=False):
    """Provides error information about a schema conversion operation."""

    Message: Optional[String]


class DeleteCertificateMessage(ServiceRequest):
    CertificateArn: String


class DeleteCertificateResponse(TypedDict, total=False):
    Certificate: Optional[Certificate]


class DeleteCollectorRequest(ServiceRequest):
    CollectorReferencedId: String


class DeleteConnectionMessage(ServiceRequest):
    EndpointArn: String
    ReplicationInstanceArn: String


class DeleteConnectionResponse(TypedDict, total=False):
    Connection: Optional[Connection]


class DeleteDataMigrationMessage(ServiceRequest):
    DataMigrationIdentifier: String


class DeleteDataMigrationResponse(TypedDict, total=False):
    DataMigration: Optional[DataMigration]


class DeleteDataProviderMessage(ServiceRequest):
    DataProviderIdentifier: String


class DeleteDataProviderResponse(TypedDict, total=False):
    DataProvider: Optional[DataProvider]


class DeleteEndpointMessage(ServiceRequest):
    EndpointArn: String


class DeleteEndpointResponse(TypedDict, total=False):
    Endpoint: Optional[Endpoint]


class DeleteEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String


class DeleteEventSubscriptionResponse(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class DeleteFleetAdvisorDatabasesRequest(ServiceRequest):
    DatabaseIds: StringList


class DeleteFleetAdvisorDatabasesResponse(TypedDict, total=False):
    DatabaseIds: Optional[StringList]


class DeleteInstanceProfileMessage(ServiceRequest):
    InstanceProfileIdentifier: String


class DeleteInstanceProfileResponse(TypedDict, total=False):
    InstanceProfile: Optional[InstanceProfile]


class DeleteMigrationProjectMessage(ServiceRequest):
    MigrationProjectIdentifier: String


class DeleteMigrationProjectResponse(TypedDict, total=False):
    MigrationProject: Optional[MigrationProject]


class DeleteReplicationConfigMessage(ServiceRequest):
    ReplicationConfigArn: String


class DeleteReplicationConfigResponse(TypedDict, total=False):
    ReplicationConfig: Optional[ReplicationConfig]


class DeleteReplicationInstanceMessage(ServiceRequest):
    ReplicationInstanceArn: String


class DeleteReplicationInstanceResponse(TypedDict, total=False):
    ReplicationInstance: Optional[ReplicationInstance]


class DeleteReplicationSubnetGroupMessage(ServiceRequest):
    ReplicationSubnetGroupIdentifier: String


class DeleteReplicationSubnetGroupResponse(TypedDict, total=False):
    pass


class DeleteReplicationTaskAssessmentRunMessage(ServiceRequest):
    ReplicationTaskAssessmentRunArn: String


class DeleteReplicationTaskAssessmentRunResponse(TypedDict, total=False):
    ReplicationTaskAssessmentRun: Optional[ReplicationTaskAssessmentRun]


class DeleteReplicationTaskMessage(ServiceRequest):
    ReplicationTaskArn: String


class DeleteReplicationTaskResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


class DescribeAccountAttributesMessage(ServiceRequest):
    pass


class DescribeAccountAttributesResponse(TypedDict, total=False):
    AccountQuotas: Optional[AccountQuotaList]
    UniqueAccountIdentifier: Optional[String]


class DescribeApplicableIndividualAssessmentsMessage(ServiceRequest):
    ReplicationTaskArn: Optional[String]
    ReplicationInstanceArn: Optional[String]
    ReplicationConfigArn: Optional[String]
    SourceEngineName: Optional[String]
    TargetEngineName: Optional[String]
    MigrationType: Optional[MigrationTypeValue]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


IndividualAssessmentNameList = List[String]


class DescribeApplicableIndividualAssessmentsResponse(TypedDict, total=False):
    IndividualAssessmentNames: Optional[IndividualAssessmentNameList]
    Marker: Optional[String]


FilterValueList = List[String]


class Filter(TypedDict, total=False):
    """Identifies the name and value of a filter object. This filter is used to
    limit the number and type of DMS objects that are returned for a
    particular ``Describe*`` call or similar operation. Filters are used as
    an optional parameter for certain API operations.
    """

    Name: String
    Values: FilterValueList


FilterList = List[Filter]


class DescribeCertificatesMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeCertificatesResponse(TypedDict, total=False):
    Marker: Optional[String]
    Certificates: Optional[CertificateList]


class DescribeConnectionsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeConnectionsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Connections: Optional[ConnectionList]


class DescribeConversionConfigurationMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier


class DescribeConversionConfigurationResponse(TypedDict, total=False):
    MigrationProjectIdentifier: Optional[String]
    ConversionConfiguration: Optional[String]


class DescribeDataMigrationsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[Marker]
    WithoutSettings: Optional[BooleanOptional]
    WithoutStatistics: Optional[BooleanOptional]


class DescribeDataMigrationsResponse(TypedDict, total=False):
    DataMigrations: Optional[DataMigrations]
    Marker: Optional[Marker]


class DescribeDataProvidersMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class DescribeDataProvidersResponse(TypedDict, total=False):
    Marker: Optional[String]
    DataProviders: Optional[DataProviderList]


class DescribeEndpointSettingsMessage(ServiceRequest):
    EngineName: String
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


EndpointSettingEnumValues = List[String]


class EndpointSetting(TypedDict, total=False):
    """Endpoint settings."""

    Name: Optional[String]
    Type: Optional[EndpointSettingTypeValue]
    EnumValues: Optional[EndpointSettingEnumValues]
    Sensitive: Optional[BooleanOptional]
    Units: Optional[String]
    Applicability: Optional[String]
    IntValueMin: Optional[IntegerOptional]
    IntValueMax: Optional[IntegerOptional]
    DefaultValue: Optional[String]


EndpointSettingsList = List[EndpointSetting]


class DescribeEndpointSettingsResponse(TypedDict, total=False):
    Marker: Optional[String]
    EndpointSettings: Optional[EndpointSettingsList]


class DescribeEndpointTypesMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class SupportedEndpointType(TypedDict, total=False):
    """Provides information about types of supported endpoints in response to a
    request by the ``DescribeEndpointTypes`` operation. This information
    includes the type of endpoint, the database engine name, and whether
    change data capture (CDC) is supported.
    """

    EngineName: Optional[String]
    SupportsCDC: Optional[Boolean]
    EndpointType: Optional[ReplicationEndpointTypeValue]
    ReplicationInstanceEngineMinimumVersion: Optional[String]
    EngineDisplayName: Optional[String]


SupportedEndpointTypeList = List[SupportedEndpointType]


class DescribeEndpointTypesResponse(TypedDict, total=False):
    Marker: Optional[String]
    SupportedEndpointTypes: Optional[SupportedEndpointTypeList]


class DescribeEndpointsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


EndpointList = List[Endpoint]


class DescribeEndpointsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Endpoints: Optional[EndpointList]


class DescribeEngineVersionsMessage(ServiceRequest):
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class EngineVersion(TypedDict, total=False):
    """Provides information about a replication instance version."""

    Version: Optional[String]
    Lifecycle: Optional[String]
    ReleaseStatus: Optional[ReleaseStatusValues]
    LaunchDate: Optional[TStamp]
    AutoUpgradeDate: Optional[TStamp]
    DeprecationDate: Optional[TStamp]
    ForceUpgradeDate: Optional[TStamp]
    AvailableUpgrades: Optional[AvailableUpgradesList]


EngineVersionList = List[EngineVersion]


class DescribeEngineVersionsResponse(TypedDict, total=False):
    EngineVersions: Optional[EngineVersionList]
    Marker: Optional[String]


class DescribeEventCategoriesMessage(ServiceRequest):
    SourceType: Optional[String]
    Filters: Optional[FilterList]


class EventCategoryGroup(TypedDict, total=False):
    """Lists categories of events subscribed to, and generated by, the
    applicable DMS resource type. This data type appears in response to the
    ```DescribeEventCategories`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_EventCategoryGroup.html>`__
    action.
    """

    SourceType: Optional[String]
    EventCategories: Optional[EventCategoriesList]


EventCategoryGroupList = List[EventCategoryGroup]


class DescribeEventCategoriesResponse(TypedDict, total=False):
    EventCategoryGroupList: Optional[EventCategoryGroupList]


class DescribeEventSubscriptionsMessage(ServiceRequest):
    SubscriptionName: Optional[String]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


EventSubscriptionsList = List[EventSubscription]


class DescribeEventSubscriptionsResponse(TypedDict, total=False):
    Marker: Optional[String]
    EventSubscriptionsList: Optional[EventSubscriptionsList]


class DescribeEventsMessage(ServiceRequest):
    SourceIdentifier: Optional[String]
    SourceType: Optional[SourceType]
    StartTime: Optional[TStamp]
    EndTime: Optional[TStamp]
    Duration: Optional[IntegerOptional]
    EventCategories: Optional[EventCategoriesList]
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class Event(TypedDict, total=False):
    """Describes an identifiable significant activity that affects a
    replication instance or task. This object can provide the message, the
    available event categories, the date and source of the event, and the
    DMS resource type.
    """

    SourceIdentifier: Optional[String]
    SourceType: Optional[SourceType]
    Message: Optional[String]
    EventCategories: Optional[EventCategoriesList]
    Date: Optional[TStamp]


EventList = List[Event]


class DescribeEventsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Events: Optional[EventList]


class DescribeExtensionPackAssociationsMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class ExportSqlDetails(TypedDict, total=False):
    """Provides information about a metadata model assessment exported to SQL."""

    S3ObjectKey: Optional[String]
    ObjectURL: Optional[String]


class ErrorDetails(TypedDict, total=False):
    """Provides error information about a project."""

    defaultErrorDetails: Optional[DefaultErrorDetails]


class SchemaConversionRequest(TypedDict, total=False):
    """Provides information about a schema conversion action."""

    Status: Optional[String]
    RequestIdentifier: Optional[String]
    MigrationProjectArn: Optional[String]
    Error: Optional[ErrorDetails]
    ExportSqlDetails: Optional[ExportSqlDetails]


SchemaConversionRequestList = List[SchemaConversionRequest]


class DescribeExtensionPackAssociationsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Requests: Optional[SchemaConversionRequestList]


class DescribeFleetAdvisorCollectorsRequest(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class DescribeFleetAdvisorCollectorsResponse(TypedDict, total=False):
    Collectors: Optional[CollectorResponses]
    NextToken: Optional[String]


class DescribeFleetAdvisorDatabasesRequest(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class DescribeFleetAdvisorDatabasesResponse(TypedDict, total=False):
    Databases: Optional[DatabaseList]
    NextToken: Optional[String]


class DescribeFleetAdvisorLsaAnalysisRequest(ServiceRequest):
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class FleetAdvisorLsaAnalysisResponse(TypedDict, total=False):
    """Describes a large-scale assessment (LSA) analysis run by a Fleet Advisor
    collector.
    """

    LsaAnalysisId: Optional[String]
    Status: Optional[String]


FleetAdvisorLsaAnalysisResponseList = List[FleetAdvisorLsaAnalysisResponse]


class DescribeFleetAdvisorLsaAnalysisResponse(TypedDict, total=False):
    Analysis: Optional[FleetAdvisorLsaAnalysisResponseList]
    NextToken: Optional[String]


class DescribeFleetAdvisorSchemaObjectSummaryRequest(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class FleetAdvisorSchemaObjectResponse(TypedDict, total=False):
    """Describes a schema object in a Fleet Advisor collector inventory."""

    SchemaId: Optional[String]
    ObjectType: Optional[String]
    NumberOfObjects: Optional[LongOptional]
    CodeLineCount: Optional[LongOptional]
    CodeSize: Optional[LongOptional]


FleetAdvisorSchemaObjectList = List[FleetAdvisorSchemaObjectResponse]


class DescribeFleetAdvisorSchemaObjectSummaryResponse(TypedDict, total=False):
    FleetAdvisorSchemaObjects: Optional[FleetAdvisorSchemaObjectList]
    NextToken: Optional[String]


class DescribeFleetAdvisorSchemasRequest(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class SchemaShortInfoResponse(TypedDict, total=False):
    """Describes a schema in a Fleet Advisor collector inventory."""

    SchemaId: Optional[String]
    SchemaName: Optional[String]
    DatabaseId: Optional[String]
    DatabaseName: Optional[String]
    DatabaseIpAddress: Optional[String]


class SchemaResponse(TypedDict, total=False):
    """Describes a schema in a Fleet Advisor collector inventory."""

    CodeLineCount: Optional[LongOptional]
    CodeSize: Optional[LongOptional]
    Complexity: Optional[String]
    Server: Optional[ServerShortInfoResponse]
    DatabaseInstance: Optional[DatabaseShortInfoResponse]
    SchemaId: Optional[String]
    SchemaName: Optional[String]
    OriginalSchema: Optional[SchemaShortInfoResponse]
    Similarity: Optional[DoubleOptional]


FleetAdvisorSchemaList = List[SchemaResponse]


class DescribeFleetAdvisorSchemasResponse(TypedDict, total=False):
    FleetAdvisorSchemas: Optional[FleetAdvisorSchemaList]
    NextToken: Optional[String]


class DescribeInstanceProfilesMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


InstanceProfileList = List[InstanceProfile]


class DescribeInstanceProfilesResponse(TypedDict, total=False):
    Marker: Optional[String]
    InstanceProfiles: Optional[InstanceProfileList]


class DescribeMetadataModelAssessmentsMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeMetadataModelAssessmentsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Requests: Optional[SchemaConversionRequestList]


class DescribeMetadataModelConversionsMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeMetadataModelConversionsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Requests: Optional[SchemaConversionRequestList]


class DescribeMetadataModelExportsAsScriptMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeMetadataModelExportsAsScriptResponse(TypedDict, total=False):
    Marker: Optional[String]
    Requests: Optional[SchemaConversionRequestList]


class DescribeMetadataModelExportsToTargetMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeMetadataModelExportsToTargetResponse(TypedDict, total=False):
    Marker: Optional[String]
    Requests: Optional[SchemaConversionRequestList]


class DescribeMetadataModelImportsMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


class DescribeMetadataModelImportsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Requests: Optional[SchemaConversionRequestList]


class DescribeMigrationProjectsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


MigrationProjectList = List[MigrationProject]


class DescribeMigrationProjectsResponse(TypedDict, total=False):
    Marker: Optional[String]
    MigrationProjects: Optional[MigrationProjectList]


class DescribeOrderableReplicationInstancesMessage(ServiceRequest):
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class OrderableReplicationInstance(TypedDict, total=False):
    """In response to the ``DescribeOrderableReplicationInstances`` operation,
    this object describes an available replication instance. This
    description includes the replication instance's type, engine version,
    and allocated storage.
    """

    EngineVersion: Optional[String]
    ReplicationInstanceClass: Optional[ReplicationInstanceClass]
    StorageType: Optional[String]
    MinAllocatedStorage: Optional[Integer]
    MaxAllocatedStorage: Optional[Integer]
    DefaultAllocatedStorage: Optional[Integer]
    IncludedAllocatedStorage: Optional[Integer]
    AvailabilityZones: Optional[AvailabilityZonesList]
    ReleaseStatus: Optional[ReleaseStatusValues]


OrderableReplicationInstanceList = List[OrderableReplicationInstance]


class DescribeOrderableReplicationInstancesResponse(TypedDict, total=False):
    OrderableReplicationInstances: Optional[OrderableReplicationInstanceList]
    Marker: Optional[String]


class DescribePendingMaintenanceActionsMessage(ServiceRequest):
    ReplicationInstanceArn: Optional[String]
    Filters: Optional[FilterList]
    Marker: Optional[String]
    MaxRecords: Optional[IntegerOptional]


PendingMaintenanceActions = List[ResourcePendingMaintenanceActions]


class DescribePendingMaintenanceActionsResponse(TypedDict, total=False):
    PendingMaintenanceActions: Optional[PendingMaintenanceActions]
    Marker: Optional[String]


class DescribeRecommendationLimitationsRequest(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class Limitation(TypedDict, total=False):
    """Provides information about the limitations of target Amazon Web Services
    engines.

    Your source database might include features that the target Amazon Web
    Services engine doesn't support. Fleet Advisor lists these features as
    limitations. You should consider these limitations during database
    migration. For each limitation, Fleet Advisor recommends an action that
    you can take to address or avoid this limitation.
    """

    DatabaseId: Optional[String]
    EngineName: Optional[String]
    Name: Optional[String]
    Description: Optional[String]
    Impact: Optional[String]
    Type: Optional[String]


LimitationList = List[Limitation]


class DescribeRecommendationLimitationsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Limitations: Optional[LimitationList]


class DescribeRecommendationsRequest(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    NextToken: Optional[String]


class RdsConfiguration(TypedDict, total=False):
    """Provides information that describes the configuration of the recommended
    target engine on Amazon RDS.
    """

    EngineEdition: Optional[String]
    InstanceType: Optional[String]
    InstanceVcpu: Optional[DoubleOptional]
    InstanceMemory: Optional[DoubleOptional]
    StorageType: Optional[String]
    StorageSize: Optional[IntegerOptional]
    StorageIops: Optional[IntegerOptional]
    DeploymentOption: Optional[String]
    EngineVersion: Optional[String]


class RdsRequirements(TypedDict, total=False):
    """Provides information that describes the requirements to the target
    engine on Amazon RDS.
    """

    EngineEdition: Optional[String]
    InstanceVcpu: Optional[DoubleOptional]
    InstanceMemory: Optional[DoubleOptional]
    StorageSize: Optional[IntegerOptional]
    StorageIops: Optional[IntegerOptional]
    DeploymentOption: Optional[String]
    EngineVersion: Optional[String]


class RdsRecommendation(TypedDict, total=False):
    """Provides information that describes a recommendation of a target engine
    on Amazon RDS.
    """

    RequirementsToTarget: Optional[RdsRequirements]
    TargetConfiguration: Optional[RdsConfiguration]


class RecommendationData(TypedDict, total=False):
    """Provides information about the target engine for the specified source
    database.
    """

    RdsEngine: Optional[RdsRecommendation]


class Recommendation(TypedDict, total=False):
    """Provides information that describes a recommendation of a target engine.

    A *recommendation* is a set of possible Amazon Web Services target
    engines that you can choose to migrate your source on-premises database.
    In this set, Fleet Advisor suggests a single target engine as the right
    sized migration destination. To determine this rightsized migration
    destination, Fleet Advisor uses the inventory metadata and metrics from
    data collector. You can use recommendations before the start of
    migration to save costs and reduce risks.

    With recommendations, you can explore different target options and
    compare metrics, so you can make an informed decision when you choose
    the migration target.
    """

    DatabaseId: Optional[String]
    EngineName: Optional[String]
    CreatedDate: Optional[String]
    Status: Optional[String]
    Preferred: Optional[BooleanOptional]
    Settings: Optional[RecommendationSettings]
    Data: Optional[RecommendationData]


RecommendationList = List[Recommendation]


class DescribeRecommendationsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Recommendations: Optional[RecommendationList]


class DescribeRefreshSchemasStatusMessage(ServiceRequest):
    EndpointArn: String


class RefreshSchemasStatus(TypedDict, total=False):
    """Provides information that describes status of a schema at an endpoint
    specified by the ``DescribeRefreshSchemaStatus`` operation.
    """

    EndpointArn: Optional[String]
    ReplicationInstanceArn: Optional[String]
    Status: Optional[RefreshSchemasStatusTypeValue]
    LastRefreshDate: Optional[TStamp]
    LastFailureMessage: Optional[String]


class DescribeRefreshSchemasStatusResponse(TypedDict, total=False):
    RefreshSchemasStatus: Optional[RefreshSchemasStatus]


class DescribeReplicationConfigsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


ReplicationConfigList = List[ReplicationConfig]


class DescribeReplicationConfigsResponse(TypedDict, total=False):
    Marker: Optional[String]
    ReplicationConfigs: Optional[ReplicationConfigList]


class DescribeReplicationInstanceTaskLogsMessage(ServiceRequest):
    ReplicationInstanceArn: String
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class ReplicationInstanceTaskLog(TypedDict, total=False):
    """Contains metadata for a replication instance task log."""

    ReplicationTaskName: Optional[String]
    ReplicationTaskArn: Optional[String]
    ReplicationInstanceTaskLogSize: Optional[Long]


ReplicationInstanceTaskLogsList = List[ReplicationInstanceTaskLog]


class DescribeReplicationInstanceTaskLogsResponse(TypedDict, total=False):
    ReplicationInstanceArn: Optional[String]
    ReplicationInstanceTaskLogs: Optional[ReplicationInstanceTaskLogsList]
    Marker: Optional[String]


class DescribeReplicationInstancesMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


ReplicationInstanceList = List[ReplicationInstance]


class DescribeReplicationInstancesResponse(TypedDict, total=False):
    Marker: Optional[String]
    ReplicationInstances: Optional[ReplicationInstanceList]


class DescribeReplicationSubnetGroupsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


ReplicationSubnetGroups = List[ReplicationSubnetGroup]


class DescribeReplicationSubnetGroupsResponse(TypedDict, total=False):
    Marker: Optional[String]
    ReplicationSubnetGroups: Optional[ReplicationSubnetGroups]


class DescribeReplicationTableStatisticsMessage(ServiceRequest):
    ReplicationConfigArn: String
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    Filters: Optional[FilterList]


class TableStatistics(TypedDict, total=False):
    """Provides a collection of table statistics in response to a request by
    the ``DescribeTableStatistics`` operation.
    """

    SchemaName: Optional[String]
    TableName: Optional[String]
    Inserts: Optional[Long]
    Deletes: Optional[Long]
    Updates: Optional[Long]
    Ddls: Optional[Long]
    AppliedInserts: Optional[LongOptional]
    AppliedDeletes: Optional[LongOptional]
    AppliedUpdates: Optional[LongOptional]
    AppliedDdls: Optional[LongOptional]
    FullLoadRows: Optional[Long]
    FullLoadCondtnlChkFailedRows: Optional[Long]
    FullLoadErrorRows: Optional[Long]
    FullLoadStartTime: Optional[TStamp]
    FullLoadEndTime: Optional[TStamp]
    FullLoadReloaded: Optional[BooleanOptional]
    LastUpdateTime: Optional[TStamp]
    TableState: Optional[String]
    ValidationPendingRecords: Optional[Long]
    ValidationFailedRecords: Optional[Long]
    ValidationSuspendedRecords: Optional[Long]
    ValidationState: Optional[String]
    ValidationStateDetails: Optional[String]
    ResyncState: Optional[String]
    ResyncRowsAttempted: Optional[LongOptional]
    ResyncRowsSucceeded: Optional[LongOptional]
    ResyncRowsFailed: Optional[LongOptional]
    ResyncProgress: Optional[DoubleOptional]


ReplicationTableStatisticsList = List[TableStatistics]


class DescribeReplicationTableStatisticsResponse(TypedDict, total=False):
    ReplicationConfigArn: Optional[String]
    Marker: Optional[String]
    ReplicationTableStatistics: Optional[ReplicationTableStatisticsList]


class DescribeReplicationTaskAssessmentResultsMessage(ServiceRequest):
    ReplicationTaskArn: Optional[String]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class ReplicationTaskAssessmentResult(TypedDict, total=False):
    """The task assessment report in JSON format."""

    ReplicationTaskIdentifier: Optional[String]
    ReplicationTaskArn: Optional[String]
    ReplicationTaskLastAssessmentDate: Optional[TStamp]
    AssessmentStatus: Optional[String]
    AssessmentResultsFile: Optional[String]
    AssessmentResults: Optional[String]
    S3ObjectUrl: Optional[SecretString]


ReplicationTaskAssessmentResultList = List[ReplicationTaskAssessmentResult]


class DescribeReplicationTaskAssessmentResultsResponse(TypedDict, total=False):
    Marker: Optional[String]
    BucketName: Optional[String]
    ReplicationTaskAssessmentResults: Optional[ReplicationTaskAssessmentResultList]


class DescribeReplicationTaskAssessmentRunsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


ReplicationTaskAssessmentRunList = List[ReplicationTaskAssessmentRun]


class DescribeReplicationTaskAssessmentRunsResponse(TypedDict, total=False):
    Marker: Optional[String]
    ReplicationTaskAssessmentRuns: Optional[ReplicationTaskAssessmentRunList]


class DescribeReplicationTaskIndividualAssessmentsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class ReplicationTaskIndividualAssessment(TypedDict, total=False):
    """Provides information that describes an individual assessment from a
    premigration assessment run.
    """

    ReplicationTaskIndividualAssessmentArn: Optional[String]
    ReplicationTaskAssessmentRunArn: Optional[String]
    IndividualAssessmentName: Optional[String]
    Status: Optional[String]
    ReplicationTaskIndividualAssessmentStartDate: Optional[TStamp]


ReplicationTaskIndividualAssessmentList = List[ReplicationTaskIndividualAssessment]


class DescribeReplicationTaskIndividualAssessmentsResponse(TypedDict, total=False):
    Marker: Optional[String]
    ReplicationTaskIndividualAssessments: Optional[ReplicationTaskIndividualAssessmentList]


class DescribeReplicationTasksMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    WithoutSettings: Optional[BooleanOptional]


ReplicationTaskList = List[ReplicationTask]


class DescribeReplicationTasksResponse(TypedDict, total=False):
    Marker: Optional[String]
    ReplicationTasks: Optional[ReplicationTaskList]


class DescribeReplicationsMessage(ServiceRequest):
    Filters: Optional[FilterList]
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


class ReplicationStats(TypedDict, total=False):
    """This object provides a collection of statistics about a serverless
    replication.
    """

    FullLoadProgressPercent: Optional[Integer]
    ElapsedTimeMillis: Optional[Long]
    TablesLoaded: Optional[Integer]
    TablesLoading: Optional[Integer]
    TablesQueued: Optional[Integer]
    TablesErrored: Optional[Integer]
    FreshStartDate: Optional[TStamp]
    StartDate: Optional[TStamp]
    StopDate: Optional[TStamp]
    FullLoadStartDate: Optional[TStamp]
    FullLoadFinishDate: Optional[TStamp]


class PremigrationAssessmentStatus(TypedDict, total=False):
    """The results returned in ``describe-replications`` to display the results
    of the premigration assessment from the replication configuration.
    """

    PremigrationAssessmentRunArn: Optional[String]
    FailOnAssessmentFailure: Optional[Boolean]
    Status: Optional[String]
    PremigrationAssessmentRunCreationDate: Optional[TStamp]
    AssessmentProgress: Optional[ReplicationTaskAssessmentRunProgress]
    LastFailureMessage: Optional[String]
    ResultLocationBucket: Optional[String]
    ResultLocationFolder: Optional[String]
    ResultEncryptionMode: Optional[String]
    ResultKmsKeyArn: Optional[String]
    ResultStatistic: Optional[ReplicationTaskAssessmentRunResultStatistic]


PremigrationAssessmentStatusList = List[PremigrationAssessmentStatus]


class ProvisionData(TypedDict, total=False):
    """Information about provisioning resources for an DMS serverless
    replication.
    """

    ProvisionState: Optional[String]
    ProvisionedCapacityUnits: Optional[Integer]
    DateProvisioned: Optional[TStamp]
    IsNewProvisioningAvailable: Optional[Boolean]
    DateNewProvisioningDataAvailable: Optional[TStamp]
    ReasonForNewProvisioningData: Optional[String]


class Replication(TypedDict, total=False):
    """Provides information that describes a serverless replication created by
    the ``CreateReplication`` operation.
    """

    ReplicationConfigIdentifier: Optional[String]
    ReplicationConfigArn: Optional[String]
    SourceEndpointArn: Optional[String]
    TargetEndpointArn: Optional[String]
    ReplicationType: Optional[MigrationTypeValue]
    Status: Optional[String]
    ProvisionData: Optional[ProvisionData]
    PremigrationAssessmentStatuses: Optional[PremigrationAssessmentStatusList]
    StopReason: Optional[String]
    FailureMessages: Optional[StringList]
    ReplicationStats: Optional[ReplicationStats]
    StartReplicationType: Optional[String]
    CdcStartTime: Optional[TStamp]
    CdcStartPosition: Optional[String]
    CdcStopPosition: Optional[String]
    RecoveryCheckpoint: Optional[String]
    ReplicationCreateTime: Optional[TStamp]
    ReplicationUpdateTime: Optional[TStamp]
    ReplicationLastStopTime: Optional[TStamp]
    ReplicationDeprovisionTime: Optional[TStamp]


ReplicationList = List[Replication]


class DescribeReplicationsResponse(TypedDict, total=False):
    Marker: Optional[String]
    Replications: Optional[ReplicationList]


class DescribeSchemasMessage(ServiceRequest):
    EndpointArn: String
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]


SchemaList = List[String]


class DescribeSchemasResponse(TypedDict, total=False):
    Marker: Optional[String]
    Schemas: Optional[SchemaList]


class DescribeTableStatisticsMessage(ServiceRequest):
    ReplicationTaskArn: String
    MaxRecords: Optional[IntegerOptional]
    Marker: Optional[String]
    Filters: Optional[FilterList]


TableStatisticsList = List[TableStatistics]


class DescribeTableStatisticsResponse(TypedDict, total=False):
    ReplicationTaskArn: Optional[String]
    TableStatistics: Optional[TableStatisticsList]
    Marker: Optional[String]


ExcludeTestList = List[String]


class ExportMetadataModelAssessmentMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    SelectionRules: String
    FileName: Optional[String]
    AssessmentReportTypes: Optional[AssessmentReportTypesList]


class ExportMetadataModelAssessmentResultEntry(TypedDict, total=False):
    """Provides information about an exported metadata model assessment."""

    S3ObjectKey: Optional[String]
    ObjectURL: Optional[String]


class ExportMetadataModelAssessmentResponse(TypedDict, total=False):
    PdfReport: Optional[ExportMetadataModelAssessmentResultEntry]
    CsvReport: Optional[ExportMetadataModelAssessmentResultEntry]


class ImportCertificateMessage(ServiceRequest):
    CertificateIdentifier: String
    CertificatePem: Optional[SecretString]
    CertificateWallet: Optional[CertificateWallet]
    Tags: Optional[TagList]


class ImportCertificateResponse(TypedDict, total=False):
    Certificate: Optional[Certificate]


IncludeTestList = List[String]
KeyList = List[String]


class ListTagsForResourceMessage(ServiceRequest):
    ResourceArn: Optional[String]
    ResourceArnList: Optional[ArnList]


class ListTagsForResourceResponse(TypedDict, total=False):
    TagList: Optional[TagList]


class ModifyConversionConfigurationMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    ConversionConfiguration: String


class ModifyConversionConfigurationResponse(TypedDict, total=False):
    MigrationProjectIdentifier: Optional[String]


class ModifyDataMigrationMessage(ServiceRequest):
    DataMigrationIdentifier: String
    DataMigrationName: Optional[String]
    EnableCloudwatchLogs: Optional[BooleanOptional]
    ServiceAccessRoleArn: Optional[String]
    DataMigrationType: Optional[MigrationTypeValue]
    SourceDataSettings: Optional[SourceDataSettings]
    TargetDataSettings: Optional[TargetDataSettings]
    NumberOfJobs: Optional[IntegerOptional]
    SelectionRules: Optional[SecretString]


class ModifyDataMigrationResponse(TypedDict, total=False):
    DataMigration: Optional[DataMigration]


class ModifyDataProviderMessage(ServiceRequest):
    DataProviderIdentifier: String
    DataProviderName: Optional[String]
    Description: Optional[String]
    Engine: Optional[String]
    ExactSettings: Optional[BooleanOptional]
    Settings: Optional[DataProviderSettings]


class ModifyDataProviderResponse(TypedDict, total=False):
    DataProvider: Optional[DataProvider]


class ModifyEndpointMessage(ServiceRequest):
    EndpointArn: String
    EndpointIdentifier: Optional[String]
    EndpointType: Optional[ReplicationEndpointTypeValue]
    EngineName: Optional[String]
    Username: Optional[String]
    Password: Optional[SecretString]
    ServerName: Optional[String]
    Port: Optional[IntegerOptional]
    DatabaseName: Optional[String]
    ExtraConnectionAttributes: Optional[String]
    CertificateArn: Optional[String]
    SslMode: Optional[DmsSslModeValue]
    ServiceAccessRoleArn: Optional[String]
    ExternalTableDefinition: Optional[String]
    DynamoDbSettings: Optional[DynamoDbSettings]
    S3Settings: Optional[S3Settings]
    DmsTransferSettings: Optional[DmsTransferSettings]
    MongoDbSettings: Optional[MongoDbSettings]
    KinesisSettings: Optional[KinesisSettings]
    KafkaSettings: Optional[KafkaSettings]
    ElasticsearchSettings: Optional[ElasticsearchSettings]
    NeptuneSettings: Optional[NeptuneSettings]
    RedshiftSettings: Optional[RedshiftSettings]
    PostgreSQLSettings: Optional[PostgreSQLSettings]
    MySQLSettings: Optional[MySQLSettings]
    OracleSettings: Optional[OracleSettings]
    SybaseSettings: Optional[SybaseSettings]
    MicrosoftSQLServerSettings: Optional[MicrosoftSQLServerSettings]
    IBMDb2Settings: Optional[IBMDb2Settings]
    DocDbSettings: Optional[DocDbSettings]
    RedisSettings: Optional[RedisSettings]
    ExactSettings: Optional[BooleanOptional]
    GcpMySQLSettings: Optional[GcpMySQLSettings]
    TimestreamSettings: Optional[TimestreamSettings]


class ModifyEndpointResponse(TypedDict, total=False):
    Endpoint: Optional[Endpoint]


class ModifyEventSubscriptionMessage(ServiceRequest):
    SubscriptionName: String
    SnsTopicArn: Optional[String]
    SourceType: Optional[String]
    EventCategories: Optional[EventCategoriesList]
    Enabled: Optional[BooleanOptional]


class ModifyEventSubscriptionResponse(TypedDict, total=False):
    EventSubscription: Optional[EventSubscription]


class ModifyInstanceProfileMessage(ServiceRequest):
    InstanceProfileIdentifier: String
    AvailabilityZone: Optional[String]
    KmsKeyArn: Optional[String]
    PubliclyAccessible: Optional[BooleanOptional]
    NetworkType: Optional[String]
    InstanceProfileName: Optional[String]
    Description: Optional[String]
    SubnetGroupIdentifier: Optional[String]
    VpcSecurityGroups: Optional[StringList]


class ModifyInstanceProfileResponse(TypedDict, total=False):
    InstanceProfile: Optional[InstanceProfile]


class ModifyMigrationProjectMessage(ServiceRequest):
    MigrationProjectIdentifier: String
    MigrationProjectName: Optional[String]
    SourceDataProviderDescriptors: Optional[DataProviderDescriptorDefinitionList]
    TargetDataProviderDescriptors: Optional[DataProviderDescriptorDefinitionList]
    InstanceProfileIdentifier: Optional[String]
    TransformationRules: Optional[String]
    Description: Optional[String]
    SchemaConversionApplicationAttributes: Optional[SCApplicationAttributes]


class ModifyMigrationProjectResponse(TypedDict, total=False):
    MigrationProject: Optional[MigrationProject]


class ModifyReplicationConfigMessage(ServiceRequest):
    ReplicationConfigArn: String
    ReplicationConfigIdentifier: Optional[String]
    ReplicationType: Optional[MigrationTypeValue]
    TableMappings: Optional[String]
    ReplicationSettings: Optional[String]
    SupplementalSettings: Optional[String]
    ComputeConfig: Optional[ComputeConfig]
    SourceEndpointArn: Optional[String]
    TargetEndpointArn: Optional[String]


class ModifyReplicationConfigResponse(TypedDict, total=False):
    ReplicationConfig: Optional[ReplicationConfig]


class ModifyReplicationInstanceMessage(ServiceRequest):
    ReplicationInstanceArn: String
    AllocatedStorage: Optional[IntegerOptional]
    ApplyImmediately: Optional[Boolean]
    ReplicationInstanceClass: Optional[ReplicationInstanceClass]
    VpcSecurityGroupIds: Optional[VpcSecurityGroupIdList]
    PreferredMaintenanceWindow: Optional[String]
    MultiAZ: Optional[BooleanOptional]
    EngineVersion: Optional[String]
    AllowMajorVersionUpgrade: Optional[Boolean]
    AutoMinorVersionUpgrade: Optional[BooleanOptional]
    ReplicationInstanceIdentifier: Optional[String]
    NetworkType: Optional[String]
    KerberosAuthenticationSettings: Optional[KerberosAuthenticationSettings]


class ModifyReplicationInstanceResponse(TypedDict, total=False):
    ReplicationInstance: Optional[ReplicationInstance]


class ModifyReplicationSubnetGroupMessage(ServiceRequest):
    ReplicationSubnetGroupIdentifier: String
    ReplicationSubnetGroupDescription: Optional[String]
    SubnetIds: SubnetIdentifierList


class ModifyReplicationSubnetGroupResponse(TypedDict, total=False):
    ReplicationSubnetGroup: Optional[ReplicationSubnetGroup]


class ModifyReplicationTaskMessage(ServiceRequest):
    ReplicationTaskArn: String
    ReplicationTaskIdentifier: Optional[String]
    MigrationType: Optional[MigrationTypeValue]
    TableMappings: Optional[String]
    ReplicationTaskSettings: Optional[String]
    CdcStartTime: Optional[TStamp]
    CdcStartPosition: Optional[String]
    CdcStopPosition: Optional[String]
    TaskData: Optional[String]


class ModifyReplicationTaskResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


class MoveReplicationTaskMessage(ServiceRequest):
    ReplicationTaskArn: String
    TargetReplicationInstanceArn: String


class MoveReplicationTaskResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


class RebootReplicationInstanceMessage(ServiceRequest):
    ReplicationInstanceArn: String
    ForceFailover: Optional[BooleanOptional]
    ForcePlannedFailover: Optional[BooleanOptional]


class RebootReplicationInstanceResponse(TypedDict, total=False):
    ReplicationInstance: Optional[ReplicationInstance]


class RefreshSchemasMessage(ServiceRequest):
    EndpointArn: String
    ReplicationInstanceArn: String


class RefreshSchemasResponse(TypedDict, total=False):
    RefreshSchemasStatus: Optional[RefreshSchemasStatus]


class TableToReload(TypedDict, total=False):
    """Provides the name of the schema and table to be reloaded."""

    SchemaName: String
    TableName: String


TableListToReload = List[TableToReload]


class ReloadReplicationTablesMessage(ServiceRequest):
    ReplicationConfigArn: String
    TablesToReload: TableListToReload
    ReloadOption: Optional[ReloadOptionValue]


class ReloadReplicationTablesResponse(TypedDict, total=False):
    ReplicationConfigArn: Optional[String]


class ReloadTablesMessage(ServiceRequest):
    ReplicationTaskArn: String
    TablesToReload: TableListToReload
    ReloadOption: Optional[ReloadOptionValue]


class ReloadTablesResponse(TypedDict, total=False):
    ReplicationTaskArn: Optional[String]


class RemoveTagsFromResourceMessage(ServiceRequest):
    """Removes one or more tags from an DMS resource."""

    ResourceArn: String
    TagKeys: KeyList


class RemoveTagsFromResourceResponse(TypedDict, total=False):
    pass


class RunFleetAdvisorLsaAnalysisResponse(TypedDict, total=False):
    LsaAnalysisId: Optional[String]
    Status: Optional[String]


class StartDataMigrationMessage(ServiceRequest):
    DataMigrationIdentifier: String
    StartType: StartReplicationMigrationTypeValue


class StartDataMigrationResponse(TypedDict, total=False):
    DataMigration: Optional[DataMigration]


class StartExtensionPackAssociationMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier


class StartExtensionPackAssociationResponse(TypedDict, total=False):
    RequestIdentifier: Optional[String]


class StartMetadataModelAssessmentMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    SelectionRules: String


class StartMetadataModelAssessmentResponse(TypedDict, total=False):
    RequestIdentifier: Optional[String]


class StartMetadataModelConversionMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    SelectionRules: String


class StartMetadataModelConversionResponse(TypedDict, total=False):
    RequestIdentifier: Optional[String]


class StartMetadataModelExportAsScriptMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    SelectionRules: String
    Origin: OriginTypeValue
    FileName: Optional[String]


class StartMetadataModelExportAsScriptResponse(TypedDict, total=False):
    RequestIdentifier: Optional[String]


class StartMetadataModelExportToTargetMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    SelectionRules: String
    OverwriteExtensionPack: Optional[BooleanOptional]


class StartMetadataModelExportToTargetResponse(TypedDict, total=False):
    RequestIdentifier: Optional[String]


class StartMetadataModelImportMessage(ServiceRequest):
    MigrationProjectIdentifier: MigrationProjectIdentifier
    SelectionRules: String
    Origin: OriginTypeValue
    Refresh: Optional[Boolean]


class StartMetadataModelImportResponse(TypedDict, total=False):
    RequestIdentifier: Optional[String]


class StartRecommendationsRequest(ServiceRequest):
    DatabaseId: String
    Settings: RecommendationSettings


class StartReplicationMessage(ServiceRequest):
    ReplicationConfigArn: String
    StartReplicationType: String
    PremigrationAssessmentSettings: Optional[String]
    CdcStartTime: Optional[TStamp]
    CdcStartPosition: Optional[String]
    CdcStopPosition: Optional[String]


class StartReplicationResponse(TypedDict, total=False):
    Replication: Optional[Replication]


class StartReplicationTaskAssessmentMessage(ServiceRequest):
    ReplicationTaskArn: String


class StartReplicationTaskAssessmentResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


class StartReplicationTaskAssessmentRunMessage(ServiceRequest):
    ReplicationTaskArn: String
    ServiceAccessRoleArn: String
    ResultLocationBucket: String
    ResultLocationFolder: Optional[String]
    ResultEncryptionMode: Optional[String]
    ResultKmsKeyArn: Optional[String]
    AssessmentRunName: String
    IncludeOnly: Optional[IncludeTestList]
    Exclude: Optional[ExcludeTestList]
    Tags: Optional[TagList]


class StartReplicationTaskAssessmentRunResponse(TypedDict, total=False):
    ReplicationTaskAssessmentRun: Optional[ReplicationTaskAssessmentRun]


class StartReplicationTaskMessage(ServiceRequest):
    ReplicationTaskArn: String
    StartReplicationTaskType: StartReplicationTaskTypeValue
    CdcStartTime: Optional[TStamp]
    CdcStartPosition: Optional[String]
    CdcStopPosition: Optional[String]


class StartReplicationTaskResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


class StopDataMigrationMessage(ServiceRequest):
    DataMigrationIdentifier: String


class StopDataMigrationResponse(TypedDict, total=False):
    DataMigration: Optional[DataMigration]


class StopReplicationMessage(ServiceRequest):
    ReplicationConfigArn: String


class StopReplicationResponse(TypedDict, total=False):
    Replication: Optional[Replication]


class StopReplicationTaskMessage(ServiceRequest):
    ReplicationTaskArn: String


class StopReplicationTaskResponse(TypedDict, total=False):
    ReplicationTask: Optional[ReplicationTask]


class TestConnectionMessage(ServiceRequest):
    ReplicationInstanceArn: String
    EndpointArn: String


class TestConnectionResponse(TypedDict, total=False):
    Connection: Optional[Connection]


class UpdateSubscriptionsToEventBridgeMessage(ServiceRequest):
    ForceMove: Optional[BooleanOptional]


class UpdateSubscriptionsToEventBridgeResponse(TypedDict, total=False):
    Result: Optional[String]


class DmsApi:
    service = "dms"
    version = "2016-01-01"

    @handler("AddTagsToResource")
    def add_tags_to_resource(
        self, context: RequestContext, resource_arn: String, tags: TagList, **kwargs
    ) -> AddTagsToResourceResponse:
        """Adds metadata tags to an DMS resource, including replication instance,
        endpoint, subnet group, and migration task. These tags can also be used
        with cost allocation reporting to track cost associated with DMS
        resources, or used in a Condition statement in an IAM policy for DMS.
        For more information, see
        ```Tag`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html>`__
        data type description.

        :param resource_arn: Identifies the DMS resource to which tags should be added.
        :param tags: One or more tags to be assigned to the resource.
        :returns: AddTagsToResourceResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("ApplyPendingMaintenanceAction")
    def apply_pending_maintenance_action(
        self,
        context: RequestContext,
        replication_instance_arn: String,
        apply_action: String,
        opt_in_type: String,
        **kwargs,
    ) -> ApplyPendingMaintenanceActionResponse:
        """Applies a pending maintenance action to a resource (for example, to a
        replication instance).

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the DMS resource that the pending
        maintenance action applies to.
        :param apply_action: The pending maintenance action to apply to this resource.
        :param opt_in_type: A value that specifies the type of opt-in request, or undoes an opt-in
        request.
        :returns: ApplyPendingMaintenanceActionResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("BatchStartRecommendations")
    def batch_start_recommendations(
        self,
        context: RequestContext,
        data: StartRecommendationsRequestEntryList | None = None,
        **kwargs,
    ) -> BatchStartRecommendationsResponse:
        """Starts the analysis of up to 20 source databases to recommend target
        engines for each source database. This is a batch version of
        `StartRecommendations <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartRecommendations.html>`__.

        The result of analysis of each source database is reported individually
        in the response. Because the batch request can result in a combination
        of successful and unsuccessful actions, you should check for batch
        errors even when the call returns an HTTP status code of ``200``.

        :param data: Provides information about source databases to analyze.
        :returns: BatchStartRecommendationsResponse
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("CancelReplicationTaskAssessmentRun")
    def cancel_replication_task_assessment_run(
        self, context: RequestContext, replication_task_assessment_run_arn: String, **kwargs
    ) -> CancelReplicationTaskAssessmentRunResponse:
        """Cancels a single premigration assessment run.

        This operation prevents any individual assessments from running if they
        haven't started running. It also attempts to cancel any individual
        assessments that are currently running.

        :param replication_task_assessment_run_arn: Amazon Resource Name (ARN) of the premigration assessment run to be
        canceled.
        :returns: CancelReplicationTaskAssessmentRunResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("CreateDataMigration")
    def create_data_migration(
        self,
        context: RequestContext,
        migration_project_identifier: String,
        data_migration_type: MigrationTypeValue,
        service_access_role_arn: String,
        data_migration_name: String | None = None,
        enable_cloudwatch_logs: BooleanOptional | None = None,
        source_data_settings: SourceDataSettings | None = None,
        target_data_settings: TargetDataSettings | None = None,
        number_of_jobs: IntegerOptional | None = None,
        tags: TagList | None = None,
        selection_rules: SecretString | None = None,
        **kwargs,
    ) -> CreateDataMigrationResponse:
        """Creates a data migration using the provided settings.

        :param migration_project_identifier: An identifier for the migration project.
        :param data_migration_type: Specifies if the data migration is full-load only, change data capture
        (CDC) only, or full-load and CDC.
        :param service_access_role_arn: The Amazon Resource Name (ARN) for the service access role that you want
        to use to create the data migration.
        :param data_migration_name: A user-friendly name for the data migration.
        :param enable_cloudwatch_logs: Specifies whether to enable CloudWatch logs for the data migration.
        :param source_data_settings: Specifies information about the source data provider.
        :param target_data_settings: Specifies information about the target data provider.
        :param number_of_jobs: The number of parallel jobs that trigger parallel threads to unload the
        tables from the source, and then load them to the target.
        :param tags: One or more tags to be assigned to the data migration.
        :param selection_rules: An optional JSON string specifying what tables, views, and schemas to
        include or exclude from the migration.
        :returns: CreateDataMigrationResponse
        :raises ResourceQuotaExceededFault:
        :raises ResourceNotFoundFault:
        :raises ResourceAlreadyExistsFault:
        :raises InvalidOperationFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("CreateDataProvider")
    def create_data_provider(
        self,
        context: RequestContext,
        engine: String,
        settings: DataProviderSettings,
        data_provider_name: String | None = None,
        description: String | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDataProviderResponse:
        """Creates a data provider using the provided settings. A data provider
        stores a data store type and location information about your database.

        :param engine: The type of database engine for the data provider.
        :param settings: The settings in JSON format for a data provider.
        :param data_provider_name: A user-friendly name for the data provider.
        :param description: A user-friendly description of the data provider.
        :param tags: One or more tags to be assigned to the data provider.
        :returns: CreateDataProviderResponse
        :raises ResourceQuotaExceededFault:
        :raises AccessDeniedFault:
        :raises ResourceAlreadyExistsFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("CreateEndpoint")
    def create_endpoint(
        self,
        context: RequestContext,
        endpoint_identifier: String,
        endpoint_type: ReplicationEndpointTypeValue,
        engine_name: String,
        username: String | None = None,
        password: SecretString | None = None,
        server_name: String | None = None,
        port: IntegerOptional | None = None,
        database_name: String | None = None,
        extra_connection_attributes: String | None = None,
        kms_key_id: String | None = None,
        tags: TagList | None = None,
        certificate_arn: String | None = None,
        ssl_mode: DmsSslModeValue | None = None,
        service_access_role_arn: String | None = None,
        external_table_definition: String | None = None,
        dynamo_db_settings: DynamoDbSettings | None = None,
        s3_settings: S3Settings | None = None,
        dms_transfer_settings: DmsTransferSettings | None = None,
        mongo_db_settings: MongoDbSettings | None = None,
        kinesis_settings: KinesisSettings | None = None,
        kafka_settings: KafkaSettings | None = None,
        elasticsearch_settings: ElasticsearchSettings | None = None,
        neptune_settings: NeptuneSettings | None = None,
        redshift_settings: RedshiftSettings | None = None,
        postgre_sql_settings: PostgreSQLSettings | None = None,
        my_sql_settings: MySQLSettings | None = None,
        oracle_settings: OracleSettings | None = None,
        sybase_settings: SybaseSettings | None = None,
        microsoft_sql_server_settings: MicrosoftSQLServerSettings | None = None,
        ibm_db2_settings: IBMDb2Settings | None = None,
        resource_identifier: String | None = None,
        doc_db_settings: DocDbSettings | None = None,
        redis_settings: RedisSettings | None = None,
        gcp_my_sql_settings: GcpMySQLSettings | None = None,
        timestream_settings: TimestreamSettings | None = None,
        **kwargs,
    ) -> CreateEndpointResponse:
        """Creates an endpoint using the provided settings.

        For a MySQL source or target endpoint, don't explicitly specify the
        database using the ``DatabaseName`` request parameter on the
        ``CreateEndpoint`` API call. Specifying ``DatabaseName`` when you create
        a MySQL endpoint replicates all the task tables to this single database.
        For MySQL endpoints, you specify the database only when you specify the
        schema in the table-mapping rules of the DMS task.

        :param endpoint_identifier: The database endpoint identifier.
        :param endpoint_type: The type of endpoint.
        :param engine_name: The type of engine for the endpoint.
        :param username: The user name to be used to log in to the endpoint database.
        :param password: The password to be used to log in to the endpoint database.
        :param server_name: The name of the server where the endpoint database resides.
        :param port: The port used by the endpoint database.
        :param database_name: The name of the endpoint database.
        :param extra_connection_attributes: Additional attributes associated with the connection.
        :param kms_key_id: An KMS key identifier that is used to encrypt the connection parameters
        for the endpoint.
        :param tags: One or more tags to be assigned to the endpoint.
        :param certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param ssl_mode: The Secure Sockets Layer (SSL) mode to use for the SSL connection.
        :param service_access_role_arn: The Amazon Resource Name (ARN) for the service access role that you want
        to use to create the endpoint.
        :param external_table_definition: The external table definition.
        :param dynamo_db_settings: Settings in JSON format for the target Amazon DynamoDB endpoint.
        :param s3_settings: Settings in JSON format for the target Amazon S3 endpoint.
        :param dms_transfer_settings: The settings in JSON format for the DMS transfer type of source
        endpoint.
        :param mongo_db_settings: Settings in JSON format for the source MongoDB endpoint.
        :param kinesis_settings: Settings in JSON format for the target endpoint for Amazon Kinesis Data
        Streams.
        :param kafka_settings: Settings in JSON format for the target Apache Kafka endpoint.
        :param elasticsearch_settings: Settings in JSON format for the target OpenSearch endpoint.
        :param neptune_settings: Settings in JSON format for the target Amazon Neptune endpoint.
        :param redshift_settings: Provides information that defines an Amazon Redshift endpoint.
        :param postgre_sql_settings: Settings in JSON format for the source and target PostgreSQL endpoint.
        :param my_sql_settings: Settings in JSON format for the source and target MySQL endpoint.
        :param oracle_settings: Settings in JSON format for the source and target Oracle endpoint.
        :param sybase_settings: Settings in JSON format for the source and target SAP ASE endpoint.
        :param microsoft_sql_server_settings: Settings in JSON format for the source and target Microsoft SQL Server
        endpoint.
        :param ibm_db2_settings: Settings in JSON format for the source IBM Db2 LUW endpoint.
        :param resource_identifier: A friendly name for the resource identifier at the end of the
        ``EndpointArn`` response parameter that is returned in the created
        ``Endpoint`` object.
        :param doc_db_settings: Provides information that defines a DocumentDB endpoint.
        :param redis_settings: Settings in JSON format for the target Redis endpoint.
        :param gcp_my_sql_settings: Settings in JSON format for the source GCP MySQL endpoint.
        :param timestream_settings: Settings in JSON format for the target Amazon Timestream endpoint.
        :returns: CreateEndpointResponse
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceQuotaExceededFault:
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises AccessDeniedFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("CreateEventSubscription")
    def create_event_subscription(
        self,
        context: RequestContext,
        subscription_name: String,
        sns_topic_arn: String,
        source_type: String | None = None,
        event_categories: EventCategoriesList | None = None,
        source_ids: SourceIdsList | None = None,
        enabled: BooleanOptional | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateEventSubscriptionResponse:
        """Creates an DMS event notification subscription.

        You can specify the type of source (``SourceType``) you want to be
        notified of, provide a list of DMS source IDs (``SourceIds``) that
        triggers the events, and provide a list of event categories
        (``EventCategories``) for events you want to be notified of. If you
        specify both the ``SourceType`` and ``SourceIds``, such as
        ``SourceType = replication-instance`` and
        ``SourceIdentifier = my-replinstance``, you will be notified of all the
        replication instance events for the specified source. If you specify a
        ``SourceType`` but don't specify a ``SourceIdentifier``, you receive
        notice of the events for that source type for all your DMS sources. If
        you don't specify either ``SourceType`` nor ``SourceIdentifier``, you
        will be notified of events generated from all DMS sources belonging to
        your customer account.

        For more information about DMS events, see `Working with Events and
        Notifications <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__
        in the *Database Migration Service User Guide.*

        :param subscription_name: The name of the DMS event notification subscription.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event
        notification.
        :param source_type: The type of DMS resource that generates the events.
        :param event_categories: A list of event categories for a source type that you want to subscribe
        to.
        :param source_ids: A list of identifiers for which DMS provides notification events.
        :param enabled: A Boolean value; set to ``true`` to activate the subscription, or set to
        ``false`` to create the subscription but not activate it.
        :param tags: One or more tags to be assigned to the event subscription.
        :returns: CreateEventSubscriptionResponse
        :raises ResourceQuotaExceededFault:
        :raises ResourceNotFoundFault:
        :raises ResourceAlreadyExistsFault:
        :raises SNSInvalidTopicFault:
        :raises SNSNoAuthorizationFault:
        :raises KMSAccessDeniedFault:
        :raises KMSDisabledFault:
        :raises KMSInvalidStateFault:
        :raises KMSNotFoundFault:
        :raises KMSThrottlingFault:
        """
        raise NotImplementedError

    @handler("CreateFleetAdvisorCollector")
    def create_fleet_advisor_collector(
        self,
        context: RequestContext,
        collector_name: String,
        service_access_role_arn: String,
        s3_bucket_name: String,
        description: String | None = None,
        **kwargs,
    ) -> CreateFleetAdvisorCollectorResponse:
        """Creates a Fleet Advisor collector using the specified parameters.

        :param collector_name: The name of your Fleet Advisor collector (for example,
        ``sample-collector``).
        :param service_access_role_arn: The IAM role that grants permissions to access the specified Amazon S3
        bucket.
        :param s3_bucket_name: The Amazon S3 bucket that the Fleet Advisor collector uses to store
        inventory metadata.
        :param description: A summary description of your Fleet Advisor collector.
        :returns: CreateFleetAdvisorCollectorResponse
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        :raises S3AccessDeniedFault:
        :raises S3ResourceNotFoundFault:
        :raises ResourceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateInstanceProfile")
    def create_instance_profile(
        self,
        context: RequestContext,
        availability_zone: String | None = None,
        kms_key_arn: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        tags: TagList | None = None,
        network_type: String | None = None,
        instance_profile_name: String | None = None,
        description: String | None = None,
        subnet_group_identifier: String | None = None,
        vpc_security_groups: StringList | None = None,
        **kwargs,
    ) -> CreateInstanceProfileResponse:
        """Creates the instance profile using the specified parameters.

        :param availability_zone: The Availability Zone where the instance profile will be created.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key that is used to encrypt
        the connection parameters for the instance profile.
        :param publicly_accessible: Specifies the accessibility options for the instance profile.
        :param tags: One or more tags to be assigned to the instance profile.
        :param network_type: Specifies the network type for the instance profile.
        :param instance_profile_name: A user-friendly name for the instance profile.
        :param description: A user-friendly description of the instance profile.
        :param subnet_group_identifier: A subnet group to associate with the instance profile.
        :param vpc_security_groups: Specifies the VPC security group names to be used with the instance
        profile.
        :returns: CreateInstanceProfileResponse
        :raises AccessDeniedFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises ResourceQuotaExceededFault:
        :raises InvalidResourceStateFault:
        :raises KMSKeyNotAccessibleFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("CreateMigrationProject")
    def create_migration_project(
        self,
        context: RequestContext,
        source_data_provider_descriptors: DataProviderDescriptorDefinitionList,
        target_data_provider_descriptors: DataProviderDescriptorDefinitionList,
        instance_profile_identifier: String,
        migration_project_name: String | None = None,
        transformation_rules: String | None = None,
        description: String | None = None,
        tags: TagList | None = None,
        schema_conversion_application_attributes: SCApplicationAttributes | None = None,
        **kwargs,
    ) -> CreateMigrationProjectResponse:
        """Creates the migration project using the specified parameters.

        You can run this action only after you create an instance profile and
        data providers using
        `CreateInstanceProfile <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateInstanceProfile.html>`__
        and
        `CreateDataProvider <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateDataProvider.html>`__.

        :param source_data_provider_descriptors: Information about the source data provider, including the name, ARN, and
        Secrets Manager parameters.
        :param target_data_provider_descriptors: Information about the target data provider, including the name, ARN, and
        Amazon Web Services Secrets Manager parameters.
        :param instance_profile_identifier: The identifier of the associated instance profile.
        :param migration_project_name: A user-friendly name for the migration project.
        :param transformation_rules: The settings in JSON format for migration rules.
        :param description: A user-friendly description of the migration project.
        :param tags: One or more tags to be assigned to the migration project.
        :param schema_conversion_application_attributes: The schema conversion application attributes, including the Amazon S3
        bucket name and Amazon S3 role ARN.
        :returns: CreateMigrationProjectResponse
        :raises AccessDeniedFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceQuotaExceededFault:
        :raises ResourceNotFoundFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("CreateReplicationConfig")
    def create_replication_config(
        self,
        context: RequestContext,
        replication_config_identifier: String,
        source_endpoint_arn: String,
        target_endpoint_arn: String,
        compute_config: ComputeConfig,
        replication_type: MigrationTypeValue,
        table_mappings: String,
        replication_settings: String | None = None,
        supplemental_settings: String | None = None,
        resource_identifier: String | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateReplicationConfigResponse:
        """Creates a configuration that you can later provide to configure and
        start an DMS Serverless replication. You can also provide options to
        validate the configuration inputs before you start the replication.

        :param replication_config_identifier: A unique identifier that you want to use to create a
        ``ReplicationConfigArn`` that is returned as part of the output from
        this action.
        :param source_endpoint_arn: The Amazon Resource Name (ARN) of the source endpoint for this DMS
        Serverless replication configuration.
        :param target_endpoint_arn: The Amazon Resource Name (ARN) of the target endpoint for this DMS
        serverless replication configuration.
        :param compute_config: Configuration parameters for provisioning an DMS Serverless replication.
        :param replication_type: The type of DMS Serverless replication to provision using this
        replication configuration.
        :param table_mappings: JSON table mappings for DMS Serverless replications that are provisioned
        using this replication configuration.
        :param replication_settings: Optional JSON settings for DMS Serverless replications that are
        provisioned using this replication configuration.
        :param supplemental_settings: Optional JSON settings for specifying supplemental data.
        :param resource_identifier: Optional unique value or name that you set for a given resource that can
        be used to construct an Amazon Resource Name (ARN) for that resource.
        :param tags: One or more optional tags associated with resources used by the DMS
        Serverless replication.
        :returns: CreateReplicationConfigResponse
        :raises AccessDeniedFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises ReplicationSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("CreateReplicationInstance")
    def create_replication_instance(
        self,
        context: RequestContext,
        replication_instance_identifier: String,
        replication_instance_class: ReplicationInstanceClass,
        allocated_storage: IntegerOptional | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        availability_zone: String | None = None,
        replication_subnet_group_identifier: String | None = None,
        preferred_maintenance_window: String | None = None,
        multi_az: BooleanOptional | None = None,
        engine_version: String | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        tags: TagList | None = None,
        kms_key_id: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        dns_name_servers: String | None = None,
        resource_identifier: String | None = None,
        network_type: String | None = None,
        kerberos_authentication_settings: KerberosAuthenticationSettings | None = None,
        **kwargs,
    ) -> CreateReplicationInstanceResponse:
        """Creates the replication instance using the specified parameters.

        DMS requires that your account have certain roles with appropriate
        permissions before you can create a replication instance. For
        information on the required roles, see `Creating the IAM Roles to Use
        With the CLI and DMS
        API <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.APIRole>`__.
        For information on the required permissions, see `IAM Permissions Needed
        to Use
        DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions>`__.

        If you don't specify a version when creating a replication instance, DMS
        will create the instance using the default engine version. For
        information about the default engine version, see `Release
        Notes <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReleaseNotes.html>`__.

        :param replication_instance_identifier: The replication instance identifier.
        :param replication_instance_class: The compute and memory capacity of the replication instance as defined
        for the specified replication instance class.
        :param allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the
        replication instance.
        :param vpc_security_group_ids: Specifies the VPC security group to be used with the replication
        instance.
        :param availability_zone: The Availability Zone where the replication instance will be created.
        :param replication_subnet_group_identifier: A subnet group to associate with the replication instance.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in
        Universal Coordinated Time (UTC).
        :param multi_az: Specifies whether the replication instance is a Multi-AZ deployment.
        :param engine_version: The engine version number of the replication instance.
        :param auto_minor_version_upgrade: A value that indicates whether minor engine upgrades are applied
        automatically to the replication instance during the maintenance window.
        :param tags: One or more tags to be assigned to the replication instance.
        :param kms_key_id: An KMS key identifier that is used to encrypt the data on the
        replication instance.
        :param publicly_accessible: Specifies the accessibility options for the replication instance.
        :param dns_name_servers: A list of custom DNS name servers supported for the replication instance
        to access your on-premise source or target database.
        :param resource_identifier: A friendly name for the resource identifier at the end of the
        ``EndpointArn`` response parameter that is returned in the created
        ``Endpoint`` object.
        :param network_type: The type of IP address protocol used by a replication instance, such as
        IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing.
        :param kerberos_authentication_settings: Specifies the settings required for kerberos authentication when
        creating the replication instance.
        :returns: CreateReplicationInstanceResponse
        :raises AccessDeniedFault:
        :raises ResourceAlreadyExistsFault:
        :raises InsufficientResourceCapacityFault:
        :raises ResourceQuotaExceededFault:
        :raises StorageQuotaExceededFault:
        :raises ResourceNotFoundFault:
        :raises ReplicationSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidResourceStateFault:
        :raises InvalidSubnet:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("CreateReplicationSubnetGroup")
    def create_replication_subnet_group(
        self,
        context: RequestContext,
        replication_subnet_group_identifier: String,
        replication_subnet_group_description: String,
        subnet_ids: SubnetIdentifierList,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateReplicationSubnetGroupResponse:
        """Creates a replication subnet group given a list of the subnet IDs in a
        VPC.

        The VPC needs to have at least one subnet in at least two availability
        zones in the Amazon Web Services Region, otherwise the service will
        throw a ``ReplicationSubnetGroupDoesNotCoverEnoughAZs`` exception.

        If a replication subnet group exists in your Amazon Web Services
        account, the CreateReplicationSubnetGroup action returns the following
        error message: The Replication Subnet Group already exists. In this
        case, delete the existing replication subnet group. To do so, use the
        `DeleteReplicationSubnetGroup <https://docs.aws.amazon.com/en_us/dms/latest/APIReference/API_DeleteReplicationSubnetGroup.html>`__
        action. Optionally, choose Subnet groups in the DMS console, then choose
        your subnet group. Next, choose Delete from Actions.

        :param replication_subnet_group_identifier: The name for the replication subnet group.
        :param replication_subnet_group_description: The description for the subnet group.
        :param subnet_ids: Two or more subnet IDs to be assigned to the subnet group.
        :param tags: One or more tags to be assigned to the subnet group.
        :returns: CreateReplicationSubnetGroupResponse
        :raises AccessDeniedFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises ResourceQuotaExceededFault:
        :raises ReplicationSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        """
        raise NotImplementedError

    @handler("CreateReplicationTask")
    def create_replication_task(
        self,
        context: RequestContext,
        replication_task_identifier: String,
        source_endpoint_arn: String,
        target_endpoint_arn: String,
        replication_instance_arn: String,
        migration_type: MigrationTypeValue,
        table_mappings: String,
        replication_task_settings: String | None = None,
        cdc_start_time: TStamp | None = None,
        cdc_start_position: String | None = None,
        cdc_stop_position: String | None = None,
        tags: TagList | None = None,
        task_data: String | None = None,
        resource_identifier: String | None = None,
        **kwargs,
    ) -> CreateReplicationTaskResponse:
        """Creates a replication task using the specified parameters.

        :param replication_task_identifier: An identifier for the replication task.
        :param source_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the source
        endpoint.
        :param target_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the target
        endpoint.
        :param replication_instance_arn: The Amazon Resource Name (ARN) of a replication instance.
        :param migration_type: The migration type.
        :param table_mappings: The table mappings for the task, in JSON format.
        :param replication_task_settings: Overall settings for the task, in JSON format.
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop.
        :param tags: One or more tags to be assigned to the replication task.
        :param task_data: Supplemental information that the task requires to migrate the data for
        certain source and target endpoints.
        :param resource_identifier: A friendly name for the resource identifier at the end of the
        ``EndpointArn`` response parameter that is returned in the created
        ``Endpoint`` object.
        :returns: CreateReplicationTaskResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("DeleteCertificate")
    def delete_certificate(
        self, context: RequestContext, certificate_arn: String, **kwargs
    ) -> DeleteCertificateResponse:
        """Deletes the specified certificate.

        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate.
        :returns: DeleteCertificateResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DeleteConnection")
    def delete_connection(
        self,
        context: RequestContext,
        endpoint_arn: String,
        replication_instance_arn: String,
        **kwargs,
    ) -> DeleteConnectionResponse:
        """Deletes the connection between a replication instance and an endpoint.

        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :returns: DeleteConnectionResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DeleteDataMigration")
    def delete_data_migration(
        self, context: RequestContext, data_migration_identifier: String, **kwargs
    ) -> DeleteDataMigrationResponse:
        """Deletes the specified data migration.

        :param data_migration_identifier: The identifier (name or ARN) of the data migration to delete.
        :returns: DeleteDataMigrationResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DeleteDataProvider")
    def delete_data_provider(
        self, context: RequestContext, data_provider_identifier: String, **kwargs
    ) -> DeleteDataProviderResponse:
        """Deletes the specified data provider.

        All migration projects associated with the data provider must be deleted
        or modified before you can delete the data provider.

        :param data_provider_identifier: The identifier of the data provider to delete.
        :returns: DeleteDataProviderResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DeleteEndpoint")
    def delete_endpoint(
        self, context: RequestContext, endpoint_arn: String, **kwargs
    ) -> DeleteEndpointResponse:
        """Deletes the specified endpoint.

        All tasks associated with the endpoint must be deleted before you can
        delete the endpoint.

        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :returns: DeleteEndpointResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DeleteEventSubscription")
    def delete_event_subscription(
        self, context: RequestContext, subscription_name: String, **kwargs
    ) -> DeleteEventSubscriptionResponse:
        """Deletes an DMS event subscription.

        :param subscription_name: The name of the DMS event notification subscription to be deleted.
        :returns: DeleteEventSubscriptionResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("DeleteFleetAdvisorCollector")
    def delete_fleet_advisor_collector(
        self, context: RequestContext, collector_referenced_id: String, **kwargs
    ) -> None:
        """Deletes the specified Fleet Advisor collector.

        :param collector_referenced_id: The reference ID of the Fleet Advisor collector to delete.
        :raises InvalidResourceStateFault:
        :raises CollectorNotFoundFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("DeleteFleetAdvisorDatabases")
    def delete_fleet_advisor_databases(
        self, context: RequestContext, database_ids: StringList, **kwargs
    ) -> DeleteFleetAdvisorDatabasesResponse:
        """Deletes the specified Fleet Advisor collector databases.

        :param database_ids: The IDs of the Fleet Advisor collector databases to delete.
        :returns: DeleteFleetAdvisorDatabasesResponse
        :raises ResourceNotFoundFault:
        :raises InvalidOperationFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("DeleteInstanceProfile")
    def delete_instance_profile(
        self, context: RequestContext, instance_profile_identifier: String, **kwargs
    ) -> DeleteInstanceProfileResponse:
        """Deletes the specified instance profile.

        All migration projects associated with the instance profile must be
        deleted or modified before you can delete the instance profile.

        :param instance_profile_identifier: The identifier of the instance profile to delete.
        :returns: DeleteInstanceProfileResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DeleteMigrationProject")
    def delete_migration_project(
        self, context: RequestContext, migration_project_identifier: String, **kwargs
    ) -> DeleteMigrationProjectResponse:
        """Deletes the specified migration project.

        The migration project must be closed before you can delete it.

        :param migration_project_identifier: The name or Amazon Resource Name (ARN) of the migration project to
        delete.
        :returns: DeleteMigrationProjectResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DeleteReplicationConfig")
    def delete_replication_config(
        self, context: RequestContext, replication_config_arn: String, **kwargs
    ) -> DeleteReplicationConfigResponse:
        """Deletes an DMS Serverless replication configuration. This effectively
        deprovisions any and all replications that use this configuration. You
        can't delete the configuration for an DMS Serverless replication that is
        ongoing. You can delete the configuration when the replication is in a
        non-RUNNING and non-STARTING state.

        :param replication_config_arn: The replication config to delete.
        :returns: DeleteReplicationConfigResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DeleteReplicationInstance")
    def delete_replication_instance(
        self, context: RequestContext, replication_instance_arn: String, **kwargs
    ) -> DeleteReplicationInstanceResponse:
        """Deletes the specified replication instance.

        You must delete any migration tasks that are associated with the
        replication instance before you can delete it.

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance to be
        deleted.
        :returns: DeleteReplicationInstanceResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DeleteReplicationSubnetGroup")
    def delete_replication_subnet_group(
        self, context: RequestContext, replication_subnet_group_identifier: String, **kwargs
    ) -> DeleteReplicationSubnetGroupResponse:
        """Deletes a subnet group.

        :param replication_subnet_group_identifier: The subnet group name of the replication instance.
        :returns: DeleteReplicationSubnetGroupResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("DeleteReplicationTask")
    def delete_replication_task(
        self, context: RequestContext, replication_task_arn: String, **kwargs
    ) -> DeleteReplicationTaskResponse:
        """Deletes the specified replication task.

        :param replication_task_arn: The Amazon Resource Name (ARN) of the replication task to be deleted.
        :returns: DeleteReplicationTaskResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DeleteReplicationTaskAssessmentRun")
    def delete_replication_task_assessment_run(
        self, context: RequestContext, replication_task_assessment_run_arn: String, **kwargs
    ) -> DeleteReplicationTaskAssessmentRunResponse:
        """Deletes the record of a single premigration assessment run.

        This operation removes all metadata that DMS maintains about this
        assessment run. However, the operation leaves untouched all information
        about this assessment run that is stored in your Amazon S3 bucket.

        :param replication_task_assessment_run_arn: Amazon Resource Name (ARN) of the premigration assessment run to be
        deleted.
        :returns: DeleteReplicationTaskAssessmentRunResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeAccountAttributes")
    def describe_account_attributes(
        self, context: RequestContext, **kwargs
    ) -> DescribeAccountAttributesResponse:
        """Lists all of the DMS attributes for a customer account. These attributes
        include DMS quotas for the account and a unique account identifier in a
        particular DMS region. DMS quotas include a list of resource quotas
        supported by the account, such as the number of replication instances
        allowed. The description for each resource quota, includes the quota
        name, current usage toward that quota, and the quota's maximum value.
        DMS uses the unique account identifier to name each artifact used by DMS
        in the given region.

        This command does not take any parameters.

        :returns: DescribeAccountAttributesResponse
        """
        raise NotImplementedError

    @handler("DescribeApplicableIndividualAssessments")
    def describe_applicable_individual_assessments(
        self,
        context: RequestContext,
        replication_task_arn: String | None = None,
        replication_instance_arn: String | None = None,
        replication_config_arn: String | None = None,
        source_engine_name: String | None = None,
        target_engine_name: String | None = None,
        migration_type: MigrationTypeValue | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeApplicableIndividualAssessmentsResponse:
        """Provides a list of individual assessments that you can specify for a new
        premigration assessment run, given one or more parameters.

        If you specify an existing migration task, this operation provides the
        default individual assessments you can specify for that task. Otherwise,
        the specified parameters model elements of a possible migration task on
        which to base a premigration assessment run.

        To use these migration task modeling parameters, you must specify an
        existing replication instance, a source database engine, a target
        database engine, and a migration type. This combination of parameters
        potentially limits the default individual assessments available for an
        assessment run created for a corresponding migration task.

        If you specify no parameters, this operation provides a list of all
        possible individual assessments that you can specify for an assessment
        run. If you specify any one of the task modeling parameters, you must
        specify all of them or the operation cannot provide a list of individual
        assessments. The only parameter that you can specify alone is for an
        existing migration task. The specified task definition then determines
        the default list of individual assessments that you can specify in an
        assessment run for the task.

        :param replication_task_arn: Amazon Resource Name (ARN) of a migration task on which you want to base
        the default list of individual assessments.
        :param replication_instance_arn: ARN of a replication instance on which you want to base the default list
        of individual assessments.
        :param replication_config_arn: Amazon Resource Name (ARN) of a serverless replication on which you want
        to base the default list of individual assessments.
        :param source_engine_name: Name of a database engine that the specified replication instance
        supports as a source.
        :param target_engine_name: Name of a database engine that the specified replication instance
        supports as a target.
        :param migration_type: Name of the migration type that each provided individual assessment must
        support.
        :param max_records: Maximum number of records to include in the response.
        :param marker: Optional pagination token provided by a previous request.
        :returns: DescribeApplicableIndividualAssessmentsResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeCertificates")
    def describe_certificates(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeCertificatesResponse:
        """Provides a description of the certificate.

        :param filters: Filters applied to the certificates described in the form of key-value
        pairs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeCertificatesResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeConnections")
    def describe_connections(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeConnectionsResponse:
        """Describes the status of the connections that have been made between the
        replication instance and an endpoint. Connections are created when you
        test an endpoint.

        :param filters: The filters applied to the connection.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeConnectionsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeConversionConfiguration")
    def describe_conversion_configuration(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        **kwargs,
    ) -> DescribeConversionConfigurationResponse:
        """Returns configuration parameters for a schema conversion project.

        :param migration_project_identifier: The name or Amazon Resource Name (ARN) for the schema conversion project
        to describe.
        :returns: DescribeConversionConfigurationResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeDataMigrations")
    def describe_data_migrations(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: Marker | None = None,
        without_settings: BooleanOptional | None = None,
        without_statistics: BooleanOptional | None = None,
        **kwargs,
    ) -> DescribeDataMigrationsResponse:
        """Returns information about data migrations.

        :param filters: Filters applied to the data migrations.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :param without_settings: An option to set to avoid returning information about settings.
        :param without_statistics: An option to set to avoid returning information about statistics.
        :returns: DescribeDataMigrationsResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DescribeDataProviders")
    def describe_data_providers(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeDataProvidersResponse:
        """Returns a paginated list of data providers for your account in the
        current region.

        :param filters: Filters applied to the data providers described in the form of key-value
        pairs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :returns: DescribeDataProvidersResponse
        :raises ResourceNotFoundFault:
        :raises AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DescribeEndpointSettings")
    def describe_endpoint_settings(
        self,
        context: RequestContext,
        engine_name: String,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEndpointSettingsResponse:
        """Returns information about the possible endpoint settings available when
        you create an endpoint for a specific database engine.

        :param engine_name: The database engine used for your source or target endpoint.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeEndpointSettingsResponse
        """
        raise NotImplementedError

    @handler("DescribeEndpointTypes")
    def describe_endpoint_types(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEndpointTypesResponse:
        """Returns information about the type of endpoints available.

        :param filters: Filters applied to the endpoint types.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeEndpointTypesResponse
        """
        raise NotImplementedError

    @handler("DescribeEndpoints")
    def describe_endpoints(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEndpointsResponse:
        """Returns information about the endpoints for your account in the current
        region.

        :param filters: Filters applied to the endpoints.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeEndpointsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeEngineVersions")
    def describe_engine_versions(
        self,
        context: RequestContext,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEngineVersionsResponse:
        """Returns information about the replication instance versions used in the
        project.

        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeEngineVersionsResponse
        """
        raise NotImplementedError

    @handler("DescribeEventCategories")
    def describe_event_categories(
        self,
        context: RequestContext,
        source_type: String | None = None,
        filters: FilterList | None = None,
        **kwargs,
    ) -> DescribeEventCategoriesResponse:
        """Lists categories for all event source types, or, if specified, for a
        specified source type. You can see a list of the event categories and
        source types in `Working with Events and
        Notifications <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__
        in the *Database Migration Service User Guide.*

        :param source_type: The type of DMS resource that generates events.
        :param filters: Filters applied to the event categories.
        :returns: DescribeEventCategoriesResponse
        """
        raise NotImplementedError

    @handler("DescribeEventSubscriptions")
    def describe_event_subscriptions(
        self,
        context: RequestContext,
        subscription_name: String | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEventSubscriptionsResponse:
        """Lists all the event subscriptions for a customer account. The
        description of a subscription includes ``SubscriptionName``,
        ``SNSTopicARN``, ``CustomerID``, ``SourceType``, ``SourceID``,
        ``CreationTime``, and ``Status``.

        If you specify ``SubscriptionName``, this action lists the description
        for that subscription.

        :param subscription_name: The name of the DMS event subscription to be described.
        :param filters: Filters applied to event subscriptions.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeEventSubscriptionsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeEvents")
    def describe_events(
        self,
        context: RequestContext,
        source_identifier: String | None = None,
        source_type: SourceType | None = None,
        start_time: TStamp | None = None,
        end_time: TStamp | None = None,
        duration: IntegerOptional | None = None,
        event_categories: EventCategoriesList | None = None,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeEventsResponse:
        """Lists events for a given source identifier and source type. You can also
        specify a start and end time. For more information on DMS events, see
        `Working with Events and
        Notifications <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__
        in the *Database Migration Service User Guide.*

        :param source_identifier: The identifier of an event source.
        :param source_type: The type of DMS resource that generates events.
        :param start_time: The start time for the events to be listed.
        :param end_time: The end time for the events to be listed.
        :param duration: The duration of the events to be listed.
        :param event_categories: A list of event categories for the source type that you've chosen.
        :param filters: Filters applied to events.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeEventsResponse
        """
        raise NotImplementedError

    @handler("DescribeExtensionPackAssociations")
    def describe_extension_pack_associations(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribeExtensionPackAssociationsResponse:
        """Returns a paginated list of extension pack associations for the
        specified migration project. An extension pack is an add-on module that
        emulates functions present in a source database that are required when
        converting objects to the target database.

        :param migration_project_identifier: The name or Amazon Resource Name (ARN) for the migration project.
        :param filters: Filters applied to the extension pack associations described in the form
        of key-value pairs.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeExtensionPackAssociationsResponse
        """
        raise NotImplementedError

    @handler("DescribeFleetAdvisorCollectors")
    def describe_fleet_advisor_collectors(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeFleetAdvisorCollectorsResponse:
        """Returns a list of the Fleet Advisor collectors in your account.

        :param filters: If you specify any of the following filters, the output includes
        information for only those collectors that meet the filter criteria:

        -  ``collector-referenced-id`` – The ID of the collector agent, for
           example ``d4610ac5-e323-4ad9-bc50-eaf7249dfe9d``.
        :param max_records: Sets the maximum number of records returned in the response.
        :param next_token: If ``NextToken`` is returned by a previous response, there are more
        results available.
        :returns: DescribeFleetAdvisorCollectorsResponse
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeFleetAdvisorDatabases")
    def describe_fleet_advisor_databases(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeFleetAdvisorDatabasesResponse:
        """Returns a list of Fleet Advisor databases in your account.

        :param filters: If you specify any of the following filters, the output includes
        information for only those databases that meet the filter criteria:

        -  ``database-id`` – The ID of the database.
        :param max_records: Sets the maximum number of records returned in the response.
        :param next_token: If ``NextToken`` is returned by a previous response, there are more
        results available.
        :returns: DescribeFleetAdvisorDatabasesResponse
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeFleetAdvisorLsaAnalysis")
    def describe_fleet_advisor_lsa_analysis(
        self,
        context: RequestContext,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeFleetAdvisorLsaAnalysisResponse:
        """Provides descriptions of large-scale assessment (LSA) analyses produced
        by your Fleet Advisor collectors.

        :param max_records: Sets the maximum number of records returned in the response.
        :param next_token: If ``NextToken`` is returned by a previous response, there are more
        results available.
        :returns: DescribeFleetAdvisorLsaAnalysisResponse
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeFleetAdvisorSchemaObjectSummary")
    def describe_fleet_advisor_schema_object_summary(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeFleetAdvisorSchemaObjectSummaryResponse:
        """Provides descriptions of the schemas discovered by your Fleet Advisor
        collectors.

        :param filters: If you specify any of the following filters, the output includes
        information for only those schema objects that meet the filter criteria:

        -  ``schema-id`` – The ID of the schema, for example
           ``d4610ac5-e323-4ad9-bc50-eaf7249dfe9d``.
        :param max_records: Sets the maximum number of records returned in the response.
        :param next_token: If ``NextToken`` is returned by a previous response, there are more
        results available.
        :returns: DescribeFleetAdvisorSchemaObjectSummaryResponse
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeFleetAdvisorSchemas")
    def describe_fleet_advisor_schemas(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeFleetAdvisorSchemasResponse:
        """Returns a list of schemas detected by Fleet Advisor Collectors in your
        account.

        :param filters: If you specify any of the following filters, the output includes
        information for only those schemas that meet the filter criteria:

        -  ``complexity`` – The schema's complexity, for example ``Simple``.
        :param max_records: Sets the maximum number of records returned in the response.
        :param next_token: If ``NextToken`` is returned by a previous response, there are more
        results available.
        :returns: DescribeFleetAdvisorSchemasResponse
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeInstanceProfiles")
    def describe_instance_profiles(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeInstanceProfilesResponse:
        """Returns a paginated list of instance profiles for your account in the
        current region.

        :param filters: Filters applied to the instance profiles described in the form of
        key-value pairs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :returns: DescribeInstanceProfilesResponse
        :raises ResourceNotFoundFault:
        :raises AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DescribeMetadataModelAssessments")
    def describe_metadata_model_assessments(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribeMetadataModelAssessmentsResponse:
        """Returns a paginated list of metadata model assessments for your account
        in the current region.

        :param migration_project_identifier: The name or Amazon Resource Name (ARN) of the migration project.
        :param filters: Filters applied to the metadata model assessments described in the form
        of key-value pairs.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeMetadataModelAssessmentsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeMetadataModelConversions")
    def describe_metadata_model_conversions(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribeMetadataModelConversionsResponse:
        """Returns a paginated list of metadata model conversions for a migration
        project.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param filters: Filters applied to the metadata model conversions described in the form
        of key-value pairs.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeMetadataModelConversionsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeMetadataModelExportsAsScript")
    def describe_metadata_model_exports_as_script(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribeMetadataModelExportsAsScriptResponse:
        """Returns a paginated list of metadata model exports.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param filters: Filters applied to the metadata model exports described in the form of
        key-value pairs.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeMetadataModelExportsAsScriptResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeMetadataModelExportsToTarget")
    def describe_metadata_model_exports_to_target(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribeMetadataModelExportsToTargetResponse:
        """Returns a paginated list of metadata model exports.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param filters: Filters applied to the metadata model exports described in the form of
        key-value pairs.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribeMetadataModelExportsToTargetResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeMetadataModelImports")
    def describe_metadata_model_imports(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribeMetadataModelImportsResponse:
        """Returns a paginated list of metadata model imports.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param filters: Filters applied to the metadata model imports described in the form of
        key-value pairs.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :param max_records: A paginated list of metadata model imports.
        :returns: DescribeMetadataModelImportsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeMigrationProjects")
    def describe_migration_projects(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeMigrationProjectsResponse:
        """Returns a paginated list of migration projects for your account in the
        current region.

        :param filters: Filters applied to the migration projects described in the form of
        key-value pairs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :returns: DescribeMigrationProjectsResponse
        :raises ResourceNotFoundFault:
        :raises AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("DescribeOrderableReplicationInstances")
    def describe_orderable_replication_instances(
        self,
        context: RequestContext,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeOrderableReplicationInstancesResponse:
        """Returns information about the replication instance types that can be
        created in the specified region.

        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeOrderableReplicationInstancesResponse
        """
        raise NotImplementedError

    @handler("DescribePendingMaintenanceActions")
    def describe_pending_maintenance_actions(
        self,
        context: RequestContext,
        replication_instance_arn: String | None = None,
        filters: FilterList | None = None,
        marker: String | None = None,
        max_records: IntegerOptional | None = None,
        **kwargs,
    ) -> DescribePendingMaintenanceActionsResponse:
        """Returns a list of upcoming maintenance events for replication instances
        in your account in the current Region.

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param filters: .
        :param marker: An optional pagination token provided by a previous request.
        :param max_records: The maximum number of records to include in the response.
        :returns: DescribePendingMaintenanceActionsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeRecommendationLimitations")
    def describe_recommendation_limitations(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeRecommendationLimitationsResponse:
        """Returns a paginated list of limitations for recommendations of target
        Amazon Web Services engines.

        :param filters: Filters applied to the limitations described in the form of key-value
        pairs.
        :param max_records: The maximum number of records to include in the response.
        :param next_token: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :returns: DescribeRecommendationLimitationsResponse
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("DescribeRecommendations")
    def describe_recommendations(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeRecommendationsResponse:
        """Returns a paginated list of target engine recommendations for your
        source databases.

        :param filters: Filters applied to the target engine recommendations described in the
        form of key-value pairs.
        :param max_records: The maximum number of records to include in the response.
        :param next_token: Specifies the unique pagination token that makes it possible to display
        the next page of results.
        :returns: DescribeRecommendationsResponse
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("DescribeRefreshSchemasStatus")
    def describe_refresh_schemas_status(
        self, context: RequestContext, endpoint_arn: String, **kwargs
    ) -> DescribeRefreshSchemasStatusResponse:
        """Returns the status of the RefreshSchemas operation.

        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :returns: DescribeRefreshSchemasStatusResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationConfigs")
    def describe_replication_configs(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationConfigsResponse:
        """Returns one or more existing DMS Serverless replication configurations
        as a list of structures.

        :param filters: Filters applied to the replication configs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationConfigsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationInstanceTaskLogs")
    def describe_replication_instance_task_logs(
        self,
        context: RequestContext,
        replication_instance_arn: String,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationInstanceTaskLogsResponse:
        """Returns information about the task logs for the specified task.

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationInstanceTaskLogsResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationInstances")
    def describe_replication_instances(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationInstancesResponse:
        """Returns information about replication instances for your account in the
        current region.

        :param filters: Filters applied to replication instances.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationInstancesResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationSubnetGroups")
    def describe_replication_subnet_groups(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationSubnetGroupsResponse:
        """Returns information about the replication subnet groups.

        :param filters: Filters applied to replication subnet groups.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationSubnetGroupsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationTableStatistics")
    def describe_replication_table_statistics(
        self,
        context: RequestContext,
        replication_config_arn: String,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        filters: FilterList | None = None,
        **kwargs,
    ) -> DescribeReplicationTableStatisticsResponse:
        """Returns table and schema statistics for one or more provisioned
        replications that use a given DMS Serverless replication configuration.

        :param replication_config_arn: The replication config to describe.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :param filters: Filters applied to the replication table statistics.
        :returns: DescribeReplicationTableStatisticsResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationTaskAssessmentResults")
    def describe_replication_task_assessment_results(
        self,
        context: RequestContext,
        replication_task_arn: String | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationTaskAssessmentResultsResponse:
        """Returns the task assessment results from the Amazon S3 bucket that DMS
        creates in your Amazon Web Services account. This action always returns
        the latest results.

        For more information about DMS task assessments, see `Creating a task
        assessment
        report <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html>`__
        in the *Database Migration Service User Guide*.

        :param replication_task_arn: The Amazon Resource Name (ARN) string that uniquely identifies the task.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationTaskAssessmentResultsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationTaskAssessmentRuns")
    def describe_replication_task_assessment_runs(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationTaskAssessmentRunsResponse:
        """Returns a paginated list of premigration assessment runs based on filter
        settings.

        These filter settings can specify a combination of premigration
        assessment runs, migration tasks, replication instances, and assessment
        run status values.

        This operation doesn't return information about individual assessments.
        For this information, see the
        ``DescribeReplicationTaskIndividualAssessments`` operation.

        :param filters: Filters applied to the premigration assessment runs described in the
        form of key-value pairs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationTaskAssessmentRunsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationTaskIndividualAssessments")
    def describe_replication_task_individual_assessments(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationTaskIndividualAssessmentsResponse:
        """Returns a paginated list of individual assessments based on filter
        settings.

        These filter settings can specify a combination of premigration
        assessment runs, migration tasks, and assessment status values.

        :param filters: Filters applied to the individual assessments described in the form of
        key-value pairs.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationTaskIndividualAssessmentsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplicationTasks")
    def describe_replication_tasks(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        without_settings: BooleanOptional | None = None,
        **kwargs,
    ) -> DescribeReplicationTasksResponse:
        """Returns information about replication tasks for your account in the
        current region.

        :param filters: Filters applied to replication tasks.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :param without_settings: An option to set to avoid returning information about settings.
        :returns: DescribeReplicationTasksResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeReplications")
    def describe_replications(
        self,
        context: RequestContext,
        filters: FilterList | None = None,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeReplicationsResponse:
        """Provides details on replication progress by returning status information
        for one or more provisioned DMS Serverless replications.

        :param filters: Filters applied to the replications.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeReplicationsResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeSchemas")
    def describe_schemas(
        self,
        context: RequestContext,
        endpoint_arn: String,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        **kwargs,
    ) -> DescribeSchemasResponse:
        """Returns information about the schema for the specified endpoint.

        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :returns: DescribeSchemasResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("DescribeTableStatistics")
    def describe_table_statistics(
        self,
        context: RequestContext,
        replication_task_arn: String,
        max_records: IntegerOptional | None = None,
        marker: String | None = None,
        filters: FilterList | None = None,
        **kwargs,
    ) -> DescribeTableStatisticsResponse:
        """Returns table statistics on the database migration task, including table
        name, rows inserted, rows updated, and rows deleted.

        Note that the "last updated" column the DMS console only indicates the
        time that DMS last updated the table statistics record for a table. It
        does not indicate the time of the last update to the table.

        :param replication_task_arn: The Amazon Resource Name (ARN) of the replication task.
        :param max_records: The maximum number of records to include in the response.
        :param marker: An optional pagination token provided by a previous request.
        :param filters: Filters applied to table statistics.
        :returns: DescribeTableStatisticsResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("ExportMetadataModelAssessment")
    def export_metadata_model_assessment(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        selection_rules: String,
        file_name: String | None = None,
        assessment_report_types: AssessmentReportTypesList | None = None,
        **kwargs,
    ) -> ExportMetadataModelAssessmentResponse:
        """Saves a copy of a database migration assessment report to your Amazon S3
        bucket. DMS can save your assessment report as a comma-separated value
        (CSV) or a PDF file.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param selection_rules: A value that specifies the database objects to assess.
        :param file_name: The name of the assessment file to create in your Amazon S3 bucket.
        :param assessment_report_types: The file format of the assessment file.
        :returns: ExportMetadataModelAssessmentResponse
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("ImportCertificate")
    def import_certificate(
        self,
        context: RequestContext,
        certificate_identifier: String,
        certificate_pem: SecretString | None = None,
        certificate_wallet: CertificateWallet | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> ImportCertificateResponse:
        """Uploads the specified certificate.

        :param certificate_identifier: A customer-assigned name for the certificate.
        :param certificate_pem: The contents of a ``.
        :param certificate_wallet: The location of an imported Oracle Wallet certificate for use with SSL.
        :param tags: The tags associated with the certificate.
        :returns: ImportCertificateResponse
        :raises ResourceAlreadyExistsFault:
        :raises InvalidCertificateFault:
        :raises ResourceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self,
        context: RequestContext,
        resource_arn: String | None = None,
        resource_arn_list: ArnList | None = None,
        **kwargs,
    ) -> ListTagsForResourceResponse:
        """Lists all metadata tags attached to an DMS resource, including
        replication instance, endpoint, subnet group, and migration task. For
        more information, see
        ```Tag`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html>`__
        data type description.

        :param resource_arn: The Amazon Resource Name (ARN) string that uniquely identifies the DMS
        resource to list tags for.
        :param resource_arn_list: List of ARNs that identify multiple DMS resources that you want to list
        tags for.
        :returns: ListTagsForResourceResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("ModifyConversionConfiguration")
    def modify_conversion_configuration(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        conversion_configuration: String,
        **kwargs,
    ) -> ModifyConversionConfigurationResponse:
        """Modifies the specified schema conversion configuration using the
        provided parameters.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param conversion_configuration: The new conversion configuration.
        :returns: ModifyConversionConfigurationResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("ModifyDataMigration")
    def modify_data_migration(
        self,
        context: RequestContext,
        data_migration_identifier: String,
        data_migration_name: String | None = None,
        enable_cloudwatch_logs: BooleanOptional | None = None,
        service_access_role_arn: String | None = None,
        data_migration_type: MigrationTypeValue | None = None,
        source_data_settings: SourceDataSettings | None = None,
        target_data_settings: TargetDataSettings | None = None,
        number_of_jobs: IntegerOptional | None = None,
        selection_rules: SecretString | None = None,
        **kwargs,
    ) -> ModifyDataMigrationResponse:
        """Modifies an existing DMS data migration.

        :param data_migration_identifier: The identifier (name or ARN) of the data migration to modify.
        :param data_migration_name: The new name for the data migration.
        :param enable_cloudwatch_logs: Whether to enable Cloudwatch logs for the data migration.
        :param service_access_role_arn: The new service access role ARN for the data migration.
        :param data_migration_type: The new migration type for the data migration.
        :param source_data_settings: The new information about the source data provider for the data
        migration.
        :param target_data_settings: The new information about the target data provider for the data
        migration.
        :param number_of_jobs: The number of parallel jobs that trigger parallel threads to unload the
        tables from the source, and then load them to the target.
        :param selection_rules: A JSON-formatted string that defines what objects to include and exclude
        from the migration.
        :returns: ModifyDataMigrationResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("ModifyDataProvider")
    def modify_data_provider(
        self,
        context: RequestContext,
        data_provider_identifier: String,
        data_provider_name: String | None = None,
        description: String | None = None,
        engine: String | None = None,
        exact_settings: BooleanOptional | None = None,
        settings: DataProviderSettings | None = None,
        **kwargs,
    ) -> ModifyDataProviderResponse:
        """Modifies the specified data provider using the provided settings.

        You must remove the data provider from all migration projects before you
        can modify it.

        :param data_provider_identifier: The identifier of the data provider.
        :param data_provider_name: The name of the data provider.
        :param description: A user-friendly description of the data provider.
        :param engine: The type of database engine for the data provider.
        :param exact_settings: If this attribute is Y, the current call to ``ModifyDataProvider``
        replaces all existing data provider settings with the exact settings
        that you specify in this call.
        :param settings: The settings in JSON format for a data provider.
        :returns: ModifyDataProviderResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("ModifyEndpoint")
    def modify_endpoint(
        self,
        context: RequestContext,
        endpoint_arn: String,
        endpoint_identifier: String | None = None,
        endpoint_type: ReplicationEndpointTypeValue | None = None,
        engine_name: String | None = None,
        username: String | None = None,
        password: SecretString | None = None,
        server_name: String | None = None,
        port: IntegerOptional | None = None,
        database_name: String | None = None,
        extra_connection_attributes: String | None = None,
        certificate_arn: String | None = None,
        ssl_mode: DmsSslModeValue | None = None,
        service_access_role_arn: String | None = None,
        external_table_definition: String | None = None,
        dynamo_db_settings: DynamoDbSettings | None = None,
        s3_settings: S3Settings | None = None,
        dms_transfer_settings: DmsTransferSettings | None = None,
        mongo_db_settings: MongoDbSettings | None = None,
        kinesis_settings: KinesisSettings | None = None,
        kafka_settings: KafkaSettings | None = None,
        elasticsearch_settings: ElasticsearchSettings | None = None,
        neptune_settings: NeptuneSettings | None = None,
        redshift_settings: RedshiftSettings | None = None,
        postgre_sql_settings: PostgreSQLSettings | None = None,
        my_sql_settings: MySQLSettings | None = None,
        oracle_settings: OracleSettings | None = None,
        sybase_settings: SybaseSettings | None = None,
        microsoft_sql_server_settings: MicrosoftSQLServerSettings | None = None,
        ibm_db2_settings: IBMDb2Settings | None = None,
        doc_db_settings: DocDbSettings | None = None,
        redis_settings: RedisSettings | None = None,
        exact_settings: BooleanOptional | None = None,
        gcp_my_sql_settings: GcpMySQLSettings | None = None,
        timestream_settings: TimestreamSettings | None = None,
        **kwargs,
    ) -> ModifyEndpointResponse:
        """Modifies the specified endpoint.

        For a MySQL source or target endpoint, don't explicitly specify the
        database using the ``DatabaseName`` request parameter on the
        ``ModifyEndpoint`` API call. Specifying ``DatabaseName`` when you modify
        a MySQL endpoint replicates all the task tables to this single database.
        For MySQL endpoints, you specify the database only when you specify the
        schema in the table-mapping rules of the DMS task.

        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :param endpoint_identifier: The database endpoint identifier.
        :param endpoint_type: The type of endpoint.
        :param engine_name: The database engine name.
        :param username: The user name to be used to login to the endpoint database.
        :param password: The password to be used to login to the endpoint database.
        :param server_name: The name of the server where the endpoint database resides.
        :param port: The port used by the endpoint database.
        :param database_name: The name of the endpoint database.
        :param extra_connection_attributes: Additional attributes associated with the connection.
        :param certificate_arn: The Amazon Resource Name (ARN) of the certificate used for SSL
        connection.
        :param ssl_mode: The SSL mode used to connect to the endpoint.
        :param service_access_role_arn: The Amazon Resource Name (ARN) for the IAM role you want to use to
        modify the endpoint.
        :param external_table_definition: The external table definition.
        :param dynamo_db_settings: Settings in JSON format for the target Amazon DynamoDB endpoint.
        :param s3_settings: Settings in JSON format for the target Amazon S3 endpoint.
        :param dms_transfer_settings: The settings in JSON format for the DMS transfer type of source
        endpoint.
        :param mongo_db_settings: Settings in JSON format for the source MongoDB endpoint.
        :param kinesis_settings: Settings in JSON format for the target endpoint for Amazon Kinesis Data
        Streams.
        :param kafka_settings: Settings in JSON format for the target Apache Kafka endpoint.
        :param elasticsearch_settings: Settings in JSON format for the target OpenSearch endpoint.
        :param neptune_settings: Settings in JSON format for the target Amazon Neptune endpoint.
        :param redshift_settings: Provides information that defines an Amazon Redshift endpoint.
        :param postgre_sql_settings: Settings in JSON format for the source and target PostgreSQL endpoint.
        :param my_sql_settings: Settings in JSON format for the source and target MySQL endpoint.
        :param oracle_settings: Settings in JSON format for the source and target Oracle endpoint.
        :param sybase_settings: Settings in JSON format for the source and target SAP ASE endpoint.
        :param microsoft_sql_server_settings: Settings in JSON format for the source and target Microsoft SQL Server
        endpoint.
        :param ibm_db2_settings: Settings in JSON format for the source IBM Db2 LUW endpoint.
        :param doc_db_settings: Settings in JSON format for the source DocumentDB endpoint.
        :param redis_settings: Settings in JSON format for the Redis target endpoint.
        :param exact_settings: If this attribute is Y, the current call to ``ModifyEndpoint`` replaces
        all existing endpoint settings with the exact settings that you specify
        in this call.
        :param gcp_my_sql_settings: Settings in JSON format for the source GCP MySQL endpoint.
        :param timestream_settings: Settings in JSON format for the target Amazon Timestream endpoint.
        :returns: ModifyEndpointResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises ResourceAlreadyExistsFault:
        :raises KMSKeyNotAccessibleFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("ModifyEventSubscription")
    def modify_event_subscription(
        self,
        context: RequestContext,
        subscription_name: String,
        sns_topic_arn: String | None = None,
        source_type: String | None = None,
        event_categories: EventCategoriesList | None = None,
        enabled: BooleanOptional | None = None,
        **kwargs,
    ) -> ModifyEventSubscriptionResponse:
        """Modifies an existing DMS event notification subscription.

        :param subscription_name: The name of the DMS event notification subscription to be modified.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event
        notification.
        :param source_type: The type of DMS resource that generates the events you want to subscribe
        to.
        :param event_categories: A list of event categories for a source type that you want to subscribe
        to.
        :param enabled: A Boolean value; set to **true** to activate the subscription.
        :returns: ModifyEventSubscriptionResponse
        :raises ResourceQuotaExceededFault:
        :raises ResourceNotFoundFault:
        :raises SNSInvalidTopicFault:
        :raises SNSNoAuthorizationFault:
        :raises KMSAccessDeniedFault:
        :raises KMSDisabledFault:
        :raises KMSInvalidStateFault:
        :raises KMSNotFoundFault:
        :raises KMSThrottlingFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("ModifyInstanceProfile")
    def modify_instance_profile(
        self,
        context: RequestContext,
        instance_profile_identifier: String,
        availability_zone: String | None = None,
        kms_key_arn: String | None = None,
        publicly_accessible: BooleanOptional | None = None,
        network_type: String | None = None,
        instance_profile_name: String | None = None,
        description: String | None = None,
        subnet_group_identifier: String | None = None,
        vpc_security_groups: StringList | None = None,
        **kwargs,
    ) -> ModifyInstanceProfileResponse:
        """Modifies the specified instance profile using the provided parameters.

        All migration projects associated with the instance profile must be
        deleted or modified before you can modify the instance profile.

        :param instance_profile_identifier: The identifier of the instance profile.
        :param availability_zone: The Availability Zone where the instance profile runs.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key that is used to encrypt
        the connection parameters for the instance profile.
        :param publicly_accessible: Specifies the accessibility options for the instance profile.
        :param network_type: Specifies the network type for the instance profile.
        :param instance_profile_name: A user-friendly name for the instance profile.
        :param description: A user-friendly description for the instance profile.
        :param subnet_group_identifier: A subnet group to associate with the instance profile.
        :param vpc_security_groups: Specifies the VPC security groups to be used with the instance profile.
        :returns: ModifyInstanceProfileResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises KMSKeyNotAccessibleFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("ModifyMigrationProject")
    def modify_migration_project(
        self,
        context: RequestContext,
        migration_project_identifier: String,
        migration_project_name: String | None = None,
        source_data_provider_descriptors: DataProviderDescriptorDefinitionList | None = None,
        target_data_provider_descriptors: DataProviderDescriptorDefinitionList | None = None,
        instance_profile_identifier: String | None = None,
        transformation_rules: String | None = None,
        description: String | None = None,
        schema_conversion_application_attributes: SCApplicationAttributes | None = None,
        **kwargs,
    ) -> ModifyMigrationProjectResponse:
        """Modifies the specified migration project using the provided parameters.

        The migration project must be closed before you can modify it.

        :param migration_project_identifier: The identifier of the migration project.
        :param migration_project_name: A user-friendly name for the migration project.
        :param source_data_provider_descriptors: Information about the source data provider, including the name, ARN, and
        Amazon Web Services Secrets Manager parameters.
        :param target_data_provider_descriptors: Information about the target data provider, including the name, ARN, and
        Amazon Web Services Secrets Manager parameters.
        :param instance_profile_identifier: The name or Amazon Resource Name (ARN) for the instance profile.
        :param transformation_rules: The settings in JSON format for migration rules.
        :param description: A user-friendly description of the migration project.
        :param schema_conversion_application_attributes: The schema conversion application attributes, including the Amazon S3
        bucket name and Amazon S3 role ARN.
        :returns: ModifyMigrationProjectResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("ModifyReplicationConfig")
    def modify_replication_config(
        self,
        context: RequestContext,
        replication_config_arn: String,
        replication_config_identifier: String | None = None,
        replication_type: MigrationTypeValue | None = None,
        table_mappings: String | None = None,
        replication_settings: String | None = None,
        supplemental_settings: String | None = None,
        compute_config: ComputeConfig | None = None,
        source_endpoint_arn: String | None = None,
        target_endpoint_arn: String | None = None,
        **kwargs,
    ) -> ModifyReplicationConfigResponse:
        """Modifies an existing DMS Serverless replication configuration that you
        can use to start a replication. This command includes input validation
        and logic to check the state of any replication that uses this
        configuration. You can only modify a replication configuration before
        any replication that uses it has started. As soon as you have initially
        started a replication with a given configuiration, you can't modify that
        configuration, even if you stop it.

        Other run statuses that allow you to run this command include FAILED and
        CREATED. A provisioning state that allows you to run this command is
        FAILED_PROVISION.

        :param replication_config_arn: The Amazon Resource Name of the replication to modify.
        :param replication_config_identifier: The new replication config to apply to the replication.
        :param replication_type: The type of replication.
        :param table_mappings: Table mappings specified in the replication.
        :param replication_settings: The settings for the replication.
        :param supplemental_settings: Additional settings for the replication.
        :param compute_config: Configuration parameters for provisioning an DMS Serverless replication.
        :param source_endpoint_arn: The Amazon Resource Name (ARN) of the source endpoint for this DMS
        serverless replication configuration.
        :param target_endpoint_arn: The Amazon Resource Name (ARN) of the target endpoint for this DMS
        serverless replication configuration.
        :returns: ModifyReplicationConfigResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises ReplicationSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        :raises KMSKeyNotAccessibleFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("ModifyReplicationInstance")
    def modify_replication_instance(
        self,
        context: RequestContext,
        replication_instance_arn: String,
        allocated_storage: IntegerOptional | None = None,
        apply_immediately: Boolean | None = None,
        replication_instance_class: ReplicationInstanceClass | None = None,
        vpc_security_group_ids: VpcSecurityGroupIdList | None = None,
        preferred_maintenance_window: String | None = None,
        multi_az: BooleanOptional | None = None,
        engine_version: String | None = None,
        allow_major_version_upgrade: Boolean | None = None,
        auto_minor_version_upgrade: BooleanOptional | None = None,
        replication_instance_identifier: String | None = None,
        network_type: String | None = None,
        kerberos_authentication_settings: KerberosAuthenticationSettings | None = None,
        **kwargs,
    ) -> ModifyReplicationInstanceResponse:
        """Modifies the replication instance to apply new settings. You can change
        one or more parameters by specifying these parameters and the new values
        in the request.

        Some settings are applied during the maintenance window.

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param allocated_storage: The amount of storage (in gigabytes) to be allocated for the replication
        instance.
        :param apply_immediately: Indicates whether the changes should be applied immediately or during
        the next maintenance window.
        :param replication_instance_class: The compute and memory capacity of the replication instance as defined
        for the specified replication instance class.
        :param vpc_security_group_ids: Specifies the VPC security group to be used with the replication
        instance.
        :param preferred_maintenance_window: The weekly time range (in UTC) during which system maintenance can
        occur, which might result in an outage.
        :param multi_az: Specifies whether the replication instance is a Multi-AZ deployment.
        :param engine_version: The engine version number of the replication instance.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed.
        :param auto_minor_version_upgrade: A value that indicates that minor version upgrades are applied
        automatically to the replication instance during the maintenance window.
        :param replication_instance_identifier: The replication instance identifier.
        :param network_type: The type of IP address protocol used by a replication instance, such as
        IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing.
        :param kerberos_authentication_settings: Specifies the settings required for kerberos authentication when
        modifying a replication instance.
        :returns: ModifyReplicationInstanceResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises InsufficientResourceCapacityFault:
        :raises StorageQuotaExceededFault:
        :raises UpgradeDependencyFailureFault:
        """
        raise NotImplementedError

    @handler("ModifyReplicationSubnetGroup")
    def modify_replication_subnet_group(
        self,
        context: RequestContext,
        replication_subnet_group_identifier: String,
        subnet_ids: SubnetIdentifierList,
        replication_subnet_group_description: String | None = None,
        **kwargs,
    ) -> ModifyReplicationSubnetGroupResponse:
        """Modifies the settings for the specified replication subnet group.

        :param replication_subnet_group_identifier: The name of the replication instance subnet group.
        :param subnet_ids: A list of subnet IDs.
        :param replication_subnet_group_description: A description for the replication instance subnet group.
        :returns: ModifyReplicationSubnetGroupResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises ResourceQuotaExceededFault:
        :raises SubnetAlreadyInUse:
        :raises ReplicationSubnetGroupDoesNotCoverEnoughAZs:
        :raises InvalidSubnet:
        """
        raise NotImplementedError

    @handler("ModifyReplicationTask")
    def modify_replication_task(
        self,
        context: RequestContext,
        replication_task_arn: String,
        replication_task_identifier: String | None = None,
        migration_type: MigrationTypeValue | None = None,
        table_mappings: String | None = None,
        replication_task_settings: String | None = None,
        cdc_start_time: TStamp | None = None,
        cdc_start_position: String | None = None,
        cdc_stop_position: String | None = None,
        task_data: String | None = None,
        **kwargs,
    ) -> ModifyReplicationTaskResponse:
        """Modifies the specified replication task.

        You can't modify the task endpoints. The task must be stopped before you
        can modify it.

        For more information about DMS tasks, see `Working with Migration
        Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html>`__
        in the *Database Migration Service User Guide*.

        :param replication_task_arn: The Amazon Resource Name (ARN) of the replication task.
        :param replication_task_identifier: The replication task identifier.
        :param migration_type: The migration type.
        :param table_mappings: When using the CLI or boto3, provide the path of the JSON file that
        contains the table mappings.
        :param replication_task_settings: JSON file that contains settings for the task, such as task metadata
        settings.
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop.
        :param task_data: Supplemental information that the task requires to migrate the data for
        certain source and target endpoints.
        :returns: ModifyReplicationTaskResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises ResourceAlreadyExistsFault:
        :raises KMSKeyNotAccessibleFault:
        """
        raise NotImplementedError

    @handler("MoveReplicationTask")
    def move_replication_task(
        self,
        context: RequestContext,
        replication_task_arn: String,
        target_replication_instance_arn: String,
        **kwargs,
    ) -> MoveReplicationTaskResponse:
        """Moves a replication task from its current replication instance to a
        different target replication instance using the specified parameters.
        The target replication instance must be created with the same or later
        DMS version as the current replication instance.

        :param replication_task_arn: The Amazon Resource Name (ARN) of the task that you want to move.
        :param target_replication_instance_arn: The ARN of the replication instance where you want to move the task to.
        :returns: MoveReplicationTaskResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("RebootReplicationInstance")
    def reboot_replication_instance(
        self,
        context: RequestContext,
        replication_instance_arn: String,
        force_failover: BooleanOptional | None = None,
        force_planned_failover: BooleanOptional | None = None,
        **kwargs,
    ) -> RebootReplicationInstanceResponse:
        """Reboots a replication instance. Rebooting results in a momentary outage,
        until the replication instance becomes available again.

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param force_failover: If this parameter is ``true``, the reboot is conducted through a
        Multi-AZ failover.
        :param force_planned_failover: If this parameter is ``true``, the reboot is conducted through a planned
        Multi-AZ failover where resources are released and cleaned up prior to
        conducting the failover.
        :returns: RebootReplicationInstanceResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("RefreshSchemas")
    def refresh_schemas(
        self,
        context: RequestContext,
        endpoint_arn: String,
        replication_instance_arn: String,
        **kwargs,
    ) -> RefreshSchemasResponse:
        """Populates the schema for the specified endpoint. This is an asynchronous
        operation and can take several minutes. You can check the status of this
        operation by calling the DescribeRefreshSchemasStatus operation.

        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :returns: RefreshSchemasResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        """
        raise NotImplementedError

    @handler("ReloadReplicationTables")
    def reload_replication_tables(
        self,
        context: RequestContext,
        replication_config_arn: String,
        tables_to_reload: TableListToReload,
        reload_option: ReloadOptionValue | None = None,
        **kwargs,
    ) -> ReloadReplicationTablesResponse:
        """Reloads the target database table with the source data for a given DMS
        Serverless replication configuration.

        You can only use this operation with a task in the RUNNING state,
        otherwise the service will throw an ``InvalidResourceStateFault``
        exception.

        :param replication_config_arn: The Amazon Resource Name of the replication config for which to reload
        tables.
        :param tables_to_reload: The list of tables to reload.
        :param reload_option: Options for reload.
        :returns: ReloadReplicationTablesResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("ReloadTables")
    def reload_tables(
        self,
        context: RequestContext,
        replication_task_arn: String,
        tables_to_reload: TableListToReload,
        reload_option: ReloadOptionValue | None = None,
        **kwargs,
    ) -> ReloadTablesResponse:
        """Reloads the target database table with the source data.

        You can only use this operation with a task in the ``RUNNING`` state,
        otherwise the service will throw an ``InvalidResourceStateFault``
        exception.

        :param replication_task_arn: The Amazon Resource Name (ARN) of the replication task.
        :param tables_to_reload: The name and schema of the table to be reloaded.
        :param reload_option: Options for reload.
        :returns: ReloadTablesResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("RemoveTagsFromResource")
    def remove_tags_from_resource(
        self, context: RequestContext, resource_arn: String, tag_keys: KeyList, **kwargs
    ) -> RemoveTagsFromResourceResponse:
        """Removes metadata tags from an DMS resource, including replication
        instance, endpoint, subnet group, and migration task. For more
        information, see
        ```Tag`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html>`__
        data type description.

        :param resource_arn: An DMS resource from which you want to remove tag(s).
        :param tag_keys: The tag key (name) of the tag to be removed.
        :returns: RemoveTagsFromResourceResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("RunFleetAdvisorLsaAnalysis")
    def run_fleet_advisor_lsa_analysis(
        self, context: RequestContext, **kwargs
    ) -> RunFleetAdvisorLsaAnalysisResponse:
        """Runs large-scale assessment (LSA) analysis on every Fleet Advisor
        collector in your account.

        :returns: RunFleetAdvisorLsaAnalysisResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("StartDataMigration")
    def start_data_migration(
        self,
        context: RequestContext,
        data_migration_identifier: String,
        start_type: StartReplicationMigrationTypeValue,
        **kwargs,
    ) -> StartDataMigrationResponse:
        """Starts the specified data migration.

        :param data_migration_identifier: The identifier (name or ARN) of the data migration to start.
        :param start_type: Specifies the start type for the data migration.
        :returns: StartDataMigrationResponse
        :raises InvalidResourceStateFault:
        :raises InvalidOperationFault:
        :raises ResourceNotFoundFault:
        :raises ResourceQuotaExceededFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("StartExtensionPackAssociation")
    def start_extension_pack_association(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        **kwargs,
    ) -> StartExtensionPackAssociationResponse:
        """Applies the extension pack to your target database. An extension pack is
        an add-on module that emulates functions present in a source database
        that are required when converting objects to the target database.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :returns: StartExtensionPackAssociationResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartMetadataModelAssessment")
    def start_metadata_model_assessment(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        selection_rules: String,
        **kwargs,
    ) -> StartMetadataModelAssessmentResponse:
        """Creates a database migration assessment report by assessing the
        migration complexity for your source database. A database migration
        assessment report summarizes all of the schema conversion tasks. It also
        details the action items for database objects that can't be converted to
        the database engine of your target database instance.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param selection_rules: A value that specifies the database objects to assess.
        :returns: StartMetadataModelAssessmentResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartMetadataModelConversion")
    def start_metadata_model_conversion(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        selection_rules: String,
        **kwargs,
    ) -> StartMetadataModelConversionResponse:
        """Converts your source database objects to a format compatible with the
        target database.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param selection_rules: A value that specifies the database objects to convert.
        :returns: StartMetadataModelConversionResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartMetadataModelExportAsScript")
    def start_metadata_model_export_as_script(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        selection_rules: String,
        origin: OriginTypeValue,
        file_name: String | None = None,
        **kwargs,
    ) -> StartMetadataModelExportAsScriptResponse:
        """Saves your converted code to a file as a SQL script, and stores this
        file on your Amazon S3 bucket.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param selection_rules: A value that specifies the database objects to export.
        :param origin: Whether to export the metadata model from the source or the target.
        :param file_name: The name of the model file to create in the Amazon S3 bucket.
        :returns: StartMetadataModelExportAsScriptResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartMetadataModelExportToTarget")
    def start_metadata_model_export_to_target(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        selection_rules: String,
        overwrite_extension_pack: BooleanOptional | None = None,
        **kwargs,
    ) -> StartMetadataModelExportToTargetResponse:
        """Applies converted database objects to your target database.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param selection_rules: A value that specifies the database objects to export.
        :param overwrite_extension_pack: Whether to overwrite the migration project extension pack.
        :returns: StartMetadataModelExportToTargetResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartMetadataModelImport")
    def start_metadata_model_import(
        self,
        context: RequestContext,
        migration_project_identifier: MigrationProjectIdentifier,
        selection_rules: String,
        origin: OriginTypeValue,
        refresh: Boolean | None = None,
        **kwargs,
    ) -> StartMetadataModelImportResponse:
        """Loads the metadata for all the dependent database objects of the parent
        object.

        This operation uses your project's Amazon S3 bucket as a metadata cache
        to improve performance.

        :param migration_project_identifier: The migration project name or Amazon Resource Name (ARN).
        :param selection_rules: A value that specifies the database objects to import.
        :param origin: Whether to load metadata to the source or target database.
        :param refresh: If ``true``, DMS loads metadata for the specified objects from the
        source database.
        :returns: StartMetadataModelImportResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        :raises ResourceAlreadyExistsFault:
        :raises ResourceNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises S3ResourceNotFoundFault:
        :raises S3AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartRecommendations")
    def start_recommendations(
        self,
        context: RequestContext,
        database_id: String,
        settings: RecommendationSettings,
        **kwargs,
    ) -> None:
        """Starts the analysis of your source database to provide recommendations
        of target engines.

        You can create recommendations for multiple source databases using
        `BatchStartRecommendations <https://docs.aws.amazon.com/dms/latest/APIReference/API_BatchStartRecommendations.html>`__.

        :param database_id: The identifier of the source database to analyze and provide
        recommendations for.
        :param settings: The settings in JSON format that Fleet Advisor uses to determine target
        engine recommendations.
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("StartReplication")
    def start_replication(
        self,
        context: RequestContext,
        replication_config_arn: String,
        start_replication_type: String,
        premigration_assessment_settings: String | None = None,
        cdc_start_time: TStamp | None = None,
        cdc_start_position: String | None = None,
        cdc_stop_position: String | None = None,
        **kwargs,
    ) -> StartReplicationResponse:
        """For a given DMS Serverless replication configuration, DMS connects to
        the source endpoint and collects the metadata to analyze the replication
        workload. Using this metadata, DMS then computes and provisions the
        required capacity and starts replicating to the target endpoint using
        the server resources that DMS has provisioned for the DMS Serverless
        replication.

        :param replication_config_arn: The Amazon Resource Name of the replication for which to start
        replication.
        :param start_replication_type: The replication type.
        :param premigration_assessment_settings: User-defined settings for the premigration assessment.
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop.
        :returns: StartReplicationResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartReplicationTask")
    def start_replication_task(
        self,
        context: RequestContext,
        replication_task_arn: String,
        start_replication_task_type: StartReplicationTaskTypeValue,
        cdc_start_time: TStamp | None = None,
        cdc_start_position: String | None = None,
        cdc_stop_position: String | None = None,
        **kwargs,
    ) -> StartReplicationTaskResponse:
        """Starts the replication task.

        For more information about DMS tasks, see `Working with Migration
        Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html>`__
        in the *Database Migration Service User Guide.*

        :param replication_task_arn: The Amazon Resource Name (ARN) of the replication task to be started.
        :param start_replication_task_type: The type of replication task to start.
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop.
        :returns: StartReplicationTaskResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StartReplicationTaskAssessment")
    def start_replication_task_assessment(
        self, context: RequestContext, replication_task_arn: String, **kwargs
    ) -> StartReplicationTaskAssessmentResponse:
        """Starts the replication task assessment for unsupported data types in the
        source database.

        You can only use this operation for a task if the following conditions
        are true:

        -  The task must be in the ``stopped`` state.

        -  The task must have successful connections to the source and target.

        If either of these conditions are not met, an
        ``InvalidResourceStateFault`` error will result.

        For information about DMS task assessments, see `Creating a task
        assessment
        report <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html>`__
        in the *Database Migration Service User Guide*.

        :param replication_task_arn: The Amazon Resource Name (ARN) of the replication task.
        :returns: StartReplicationTaskAssessmentResponse
        :raises InvalidResourceStateFault:
        :raises ResourceNotFoundFault:
        """
        raise NotImplementedError

    @handler("StartReplicationTaskAssessmentRun")
    def start_replication_task_assessment_run(
        self,
        context: RequestContext,
        replication_task_arn: String,
        service_access_role_arn: String,
        result_location_bucket: String,
        assessment_run_name: String,
        result_location_folder: String | None = None,
        result_encryption_mode: String | None = None,
        result_kms_key_arn: String | None = None,
        include_only: IncludeTestList | None = None,
        exclude: ExcludeTestList | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> StartReplicationTaskAssessmentRunResponse:
        """Starts a new premigration assessment run for one or more individual
        assessments of a migration task.

        The assessments that you can specify depend on the source and target
        database engine and the migration type defined for the given task. To
        run this operation, your migration task must already be created. After
        you run this operation, you can review the status of each individual
        assessment. You can also run the migration task manually after the
        assessment run and its individual assessments complete.

        :param replication_task_arn: Amazon Resource Name (ARN) of the migration task associated with the
        premigration assessment run that you want to start.
        :param service_access_role_arn: ARN of the service role needed to start the assessment run.
        :param result_location_bucket: Amazon S3 bucket where you want DMS to store the results of this
        assessment run.
        :param assessment_run_name: Unique name to identify the assessment run.
        :param result_location_folder: Folder within an Amazon S3 bucket where you want DMS to store the
        results of this assessment run.
        :param result_encryption_mode: Encryption mode that you can specify to encrypt the results of this
        assessment run.
        :param result_kms_key_arn: ARN of a custom KMS encryption key that you specify when you set
        ``ResultEncryptionMode`` to ``"SSE_KMS``".
        :param include_only: Space-separated list of names for specific individual assessments that
        you want to include.
        :param exclude: Space-separated list of names for specific individual assessments that
        you want to exclude.
        :param tags: One or more tags to be assigned to the premigration assessment run that
        you want to start.
        :returns: StartReplicationTaskAssessmentRunResponse
        :raises AccessDeniedFault:
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises KMSAccessDeniedFault:
        :raises KMSDisabledFault:
        :raises KMSFault:
        :raises KMSInvalidStateFault:
        :raises KMSNotFoundFault:
        :raises KMSKeyNotAccessibleFault:
        :raises S3AccessDeniedFault:
        :raises S3ResourceNotFoundFault:
        :raises ResourceAlreadyExistsFault:
        """
        raise NotImplementedError

    @handler("StopDataMigration")
    def stop_data_migration(
        self, context: RequestContext, data_migration_identifier: String, **kwargs
    ) -> StopDataMigrationResponse:
        """Stops the specified data migration.

        :param data_migration_identifier: The identifier (name or ARN) of the data migration to stop.
        :returns: StopDataMigrationResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises FailedDependencyFault:
        """
        raise NotImplementedError

    @handler("StopReplication")
    def stop_replication(
        self, context: RequestContext, replication_config_arn: String, **kwargs
    ) -> StopReplicationResponse:
        """For a given DMS Serverless replication configuration, DMS stops any and
        all ongoing DMS Serverless replications. This command doesn't
        deprovision the stopped replications.

        :param replication_config_arn: The Amazon Resource Name of the replication to stop.
        :returns: StopReplicationResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("StopReplicationTask")
    def stop_replication_task(
        self, context: RequestContext, replication_task_arn: String, **kwargs
    ) -> StopReplicationTaskResponse:
        """Stops the replication task.

        :param replication_task_arn: The Amazon Resource Name(ARN) of the replication task to be stopped.
        :returns: StopReplicationTaskResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError

    @handler("TestConnection")
    def test_connection(
        self,
        context: RequestContext,
        replication_instance_arn: String,
        endpoint_arn: String,
        **kwargs,
    ) -> TestConnectionResponse:
        """Tests the connection between the replication instance and the endpoint.

        :param replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the
        endpoint.
        :returns: TestConnectionResponse
        :raises ResourceNotFoundFault:
        :raises InvalidResourceStateFault:
        :raises KMSKeyNotAccessibleFault:
        :raises ResourceQuotaExceededFault:
        :raises AccessDeniedFault:
        """
        raise NotImplementedError

    @handler("UpdateSubscriptionsToEventBridge")
    def update_subscriptions_to_event_bridge(
        self, context: RequestContext, force_move: BooleanOptional | None = None, **kwargs
    ) -> UpdateSubscriptionsToEventBridgeResponse:
        """Migrates 10 active and enabled Amazon SNS subscriptions at a time and
        converts them to corresponding Amazon EventBridge rules. By default,
        this operation migrates subscriptions only when all your replication
        instance versions are 3.4.5 or higher. If any replication instances are
        from versions earlier than 3.4.5, the operation raises an error and
        tells you to upgrade these instances to version 3.4.5 or higher. To
        enable migration regardless of version, set the ``Force`` option to
        true. However, if you don't upgrade instances earlier than version
        3.4.5, some types of events might not be available when you use Amazon
        EventBridge.

        To call this operation, make sure that you have certain permissions
        added to your user account. For more information, see `Migrating event
        subscriptions to Amazon
        EventBridge <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html#CHAP_Events-migrate-to-eventbridge>`__
        in the *Amazon Web Services Database Migration Service User Guide*.

        :param force_move: When set to true, this operation migrates DMS subscriptions for Amazon
        SNS notifications no matter what your replication instance version is.
        :returns: UpdateSubscriptionsToEventBridgeResponse
        :raises AccessDeniedFault:
        :raises InvalidResourceStateFault:
        """
        raise NotImplementedError
