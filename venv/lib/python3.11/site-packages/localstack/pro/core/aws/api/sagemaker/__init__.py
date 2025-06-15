from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Accept = str
AcceptEula = bool
AccountId = str
ActionArn = str
AdditionalModelChannelName = str
AlarmName = str
AlgorithmArn = str
AlgorithmImage = str
AppArn = str
AppImageConfigArn = str
AppImageConfigName = str
AppManaged = bool
AppName = str
ApprovalDescription = str
ArnOrName = str
ArtifactArn = str
ArtifactDigest = str
ArtifactPropertyValue = str
AssociationEntityArn = str
AthenaCatalog = str
AthenaDatabase = str
AthenaQueryString = str
AthenaWorkGroup = str
AttributeName = str
AuthenticationRequestExtraParamsKey = str
AuthenticationRequestExtraParamsValue = str
AutoGenerateEndpointName = bool
AutoMLFailureReason = str
AutoMLJobArn = str
AutoMLJobName = str
AutoMLMaxResults = int
AutoMLMaxResultsForTrials = int
AutoMLNameContains = str
AvailabilityZone = str
AvailableInstanceCount = int
BacktestResultsLocation = str
BaseModelName = str
BillableTimeInSeconds = int
BlockedReason = str
Boolean = bool
BorrowLimit = int
Branch = str
BucketName = str
CallbackToken = str
CandidateDefinitionNotebookLocation = str
CandidateName = str
CandidateStepArn = str
CandidateStepName = str
CapacitySizeValue = int
CapacityUnit = int
Catalog = str
Cents = int
CertifyForMarketplace = bool
ChannelName = str
Cidr = str
ClarifyContentTemplate = str
ClarifyEnableExplanations = str
ClarifyFeaturesAttribute = str
ClarifyHeader = str
ClarifyLabelAttribute = str
ClarifyLabelIndex = int
ClarifyMaxPayloadInMB = int
ClarifyMaxRecordCount = int
ClarifyMimeType = str
ClarifyProbabilityAttribute = str
ClarifyProbabilityIndex = int
ClarifyShapBaseline = str
ClarifyShapNumberOfSamples = int
ClarifyShapSeed = int
ClarifyShapUseLogit = bool
ClientId = str
ClientSecret = str
ClientToken = str
ClusterArn = str
ClusterAvailabilityZone = str
ClusterAvailabilityZoneId = str
ClusterEbsVolumeSizeInGB = int
ClusterInstanceCount = int
ClusterInstanceGroupName = str
ClusterLifeCycleConfigFileName = str
ClusterName = str
ClusterNameOrArn = str
ClusterNodeId = str
ClusterNonNegativeInstanceCount = int
ClusterPrivateDnsHostname = str
ClusterPrivatePrimaryIp = str
ClusterPrivatePrimaryIpv6 = str
ClusterSchedulerConfigArn = str
ClusterSchedulerConfigId = str
ClusterSchedulerPriorityClassName = str
ClusterThreadsPerCore = int
CodeRepositoryArn = str
CodeRepositoryContains = str
CodeRepositoryNameContains = str
CodeRepositoryNameOrUrl = str
CognitoUserGroup = str
CognitoUserPool = str
CollectionName = str
CompilationJobArn = str
CompilerOptions = str
ComputeQuotaArn = str
ComputeQuotaId = str
ComputeQuotaTargetTeamName = str
ConfigKey = str
ConfigValue = str
ContainerArgument = str
ContainerEntrypointString = str
ContainerHostname = str
ContainerImage = str
ContentColumn = str
ContentDigest = str
ContentType = str
ContextArn = str
ContextName = str
ContextNameOrArn = str
CountryCode = str
CronScheduleExpression = str
CsvContentType = str
CurrencyCode = str
CustomerMetadataKey = str
CustomerMetadataValue = str
DataExplorationNotebookLocation = str
DataInputConfig = str
Database = str
DefaultGid = int
DefaultUid = int
DependencyCopyPath = str
DependencyOriginPath = str
DeploymentStageMaxResults = int
Description = str
DestinationS3Uri = str
DeviceArn = str
DeviceDescription = str
DeviceFleetArn = str
DeviceFleetDescription = str
DeviceName = str
Dimension = int
DirectoryPath = str
DisableProfiler = bool
DisassociateAdditionalCodeRepositories = bool
DisassociateDefaultCodeRepository = bool
DisassociateNotebookInstanceAcceleratorTypes = bool
DisassociateNotebookInstanceLifecycleConfig = bool
DocumentSchemaVersion = str
Dollars = int
DomainArn = str
DomainId = str
DomainName = str
Double = float
DoubleParameterValue = float
Ec2CapacityReservationId = str
EdgeDeploymentPlanArn = str
EdgePackagingJobArn = str
EdgePresetDeploymentArtifact = str
EdgeVersion = str
EfsUid = str
EksClusterArn = str
EnableCapture = bool
EnableInfraCheck = bool
EnableIotRoleAlias = bool
EnableRemoteDebug = bool
EnableSessionTagChaining = bool
EndpointArn = str
EndpointConfigArn = str
EndpointConfigName = str
EndpointConfigNameContains = str
EndpointName = str
EndpointNameContains = str
EntityDescription = str
EntityName = str
EnvironmentKey = str
EnvironmentValue = str
ExcludeFeaturesAttribute = str
ExitMessage = str
ExperimentArn = str
ExperimentDescription = str
ExperimentEntityName = str
ExperimentEntityNameOrArn = str
ExperimentSourceArn = str
ExpiresInSeconds = int
ExplainabilityLocation = str
FailureReason = str
FairShareWeight = int
FeatureDescription = str
FeatureGroupArn = str
FeatureGroupMaxResults = int
FeatureGroupName = str
FeatureGroupNameContains = str
FeatureGroupNameOrArn = str
FeatureName = str
FeatureParameterKey = str
FeatureParameterValue = str
FileSystemId = str
FileSystemPath = str
FillingTransformationValue = str
FilterValue = str
Float = float
FlowDefinitionArn = str
FlowDefinitionName = str
FlowDefinitionTaskAvailabilityLifetimeInSeconds = int
FlowDefinitionTaskCount = int
FlowDefinitionTaskDescription = str
FlowDefinitionTaskKeyword = str
FlowDefinitionTaskTimeLimitInSeconds = int
FlowDefinitionTaskTitle = str
ForecastFrequency = str
ForecastHorizon = int
ForecastQuantile = str
FrameworkVersion = str
GenerateCandidateDefinitionsOnly = bool
GitConfigUrl = str
Group = str
GroupingAttributeName = str
Horovod = bool
HubArn = str
HubContentArn = str
HubContentDescription = str
HubContentDisplayName = str
HubContentDocument = str
HubContentMarkdown = str
HubContentName = str
HubContentVersion = str
HubDescription = str
HubDisplayName = str
HubName = str
HubNameOrArn = str
HubSearchKeyword = str
HumanLoopActivationConditions = str
HumanTaskUiArn = str
HumanTaskUiName = str
HyperParameterKey = str
HyperParameterTrainingJobDefinitionName = str
HyperParameterTrainingJobEnvironmentKey = str
HyperParameterTrainingJobEnvironmentValue = str
HyperParameterTuningJobArn = str
HyperParameterTuningJobName = str
HyperParameterTuningMaxRuntimeInSeconds = int
HyperParameterValue = str
HyperbandStrategyMaxResource = int
HyperbandStrategyMinResource = int
IdempotencyToken = str
IdleTimeoutInMinutes = int
ImageArn = str
ImageBaseImage = str
ImageContainerImage = str
ImageDeleteProperty = str
ImageDescription = str
ImageDigest = str
ImageDisplayName = str
ImageName = str
ImageNameContains = str
ImageUri = str
ImageVersionAlias = str
ImageVersionAliasPattern = str
ImageVersionArn = str
ImageVersionNumber = int
InUseInstanceCount = int
InferenceComponentArn = str
InferenceComponentCopyCount = int
InferenceComponentName = str
InferenceComponentNameContains = str
InferenceExperimentArn = str
InferenceExperimentDescription = str
InferenceExperimentName = str
InferenceExperimentStatusReason = str
InferenceImage = str
InferenceSpecificationName = str
InitialInstanceCount = int
InitialNumberOfUsers = int
InitialTaskCount = int
InstanceCount = int
InstanceGroupName = str
InstanceGroupTrainingPlanStatus = str
Integer = int
InvocationsMaxRetries = int
InvocationsTimeoutInSeconds = int
IotRoleAlias = str
ItemIdentifierAttributeName = str
JobDurationInSeconds = int
JobReferenceCode = str
JobReferenceCodeContains = str
JsonContentType = str
JsonPath = str
KeepAlivePeriodInSeconds = int
KernelDisplayName = str
KernelName = str
Key = str
KmsKeyId = str
LabelAttributeName = str
LabelCounter = int
LabelingJobAlgorithmSpecificationArn = str
LabelingJobArn = str
LabelingJobName = str
LambdaFunctionArn = str
LandingUri = str
LineageGroupArn = str
LineageGroupNameOrArn = str
ListMaxResults = int
ListTagsMaxResults = int
MLFramework = str
ManagedInstanceScalingMaxInstanceCount = int
ManagedInstanceScalingMinInstanceCount = int
MaxAutoMLJobRuntimeInSeconds = int
MaxCandidates = int
MaxConcurrentInvocationsPerInstance = int
MaxConcurrentTaskCount = int
MaxConcurrentTransforms = int
MaxHumanLabeledObjectCount = int
MaxNumberOfTests = int
MaxNumberOfTrainingJobs = int
MaxNumberOfTrainingJobsNotImproving = int
MaxParallelExecutionSteps = int
MaxParallelOfTests = int
MaxParallelTrainingJobs = int
MaxPayloadInMB = int
MaxPendingTimeInSeconds = int
MaxPercentageOfInputDatasetLabeled = int
MaxResults = int
MaxRuntimeInSeconds = int
MaxRuntimePerTrainingJobInSeconds = int
MaxWaitTimeInSeconds = int
MaximumExecutionTimeoutInSeconds = int
MaximumRetryAttempts = int
MediaType = str
MemoryInMb = int
MetadataPropertyValue = str
MetricName = str
MetricRegex = str
MetricValue = float
MinimumInstanceMetadataServiceVersion = str
MlReservationArn = str
MlflowVersion = str
ModelArn = str
ModelCardArn = str
ModelCardContent = str
ModelCardExportJobArn = str
ModelCardNameOrArn = str
ModelInsightsLocation = str
ModelName = str
ModelNameContains = str
ModelPackageArn = str
ModelPackageFrameworkVersion = str
ModelPackageGroupArn = str
ModelPackageSourceUri = str
ModelPackageVersion = int
ModelSetupTime = int
ModelVariantName = str
MonitoringAlertName = str
MonitoringDatapointsToAlert = int
MonitoringEvaluationPeriod = int
MonitoringJobDefinitionArn = str
MonitoringJobDefinitionName = str
MonitoringMaxRuntimeInSeconds = int
MonitoringS3Uri = str
MonitoringScheduleArn = str
MonitoringScheduleName = str
MonitoringTimeOffsetString = str
MountPath = str
NameContains = str
NeoVpcSecurityGroupId = str
NeoVpcSubnetId = str
NetworkInterfaceId = str
NextToken = str
NodeUnavailabilityValue = int
NonEmptyString256 = str
NonEmptyString64 = str
NotebookInstanceArn = str
NotebookInstanceLifecycleConfigArn = str
NotebookInstanceLifecycleConfigContent = str
NotebookInstanceLifecycleConfigName = str
NotebookInstanceLifecycleConfigNameContains = str
NotebookInstanceName = str
NotebookInstanceNameContains = str
NotebookInstanceUrl = str
NotebookInstanceVolumeSizeInGB = int
NotificationTopicArn = str
NumberOfAcceleratorDevices = float
NumberOfCpuCores = float
NumberOfHumanWorkersPerDataObject = int
NumberOfSteps = int
ObjectiveStatusCounter = int
OidcEndpoint = str
OptimizationContainerImage = str
OptimizationJobArn = str
OptimizationModelAcceptEula = bool
OptimizationType = str
OptimizationVpcSecurityGroupId = str
OptimizationVpcSubnetId = str
OptionalDouble = float
OptionalInteger = int
OptionalVolumeSizeInGB = int
PaginationToken = str
ParameterKey = str
ParameterName = str
ParameterValue = str
PartnerAppArn = str
PartnerAppName = str
Percentage = int
PipelineArn = str
PipelineDefinition = str
PipelineDescription = str
PipelineExecutionArn = str
PipelineExecutionDescription = str
PipelineExecutionFailureReason = str
PipelineExecutionName = str
PipelineName = str
PipelineNameOrArn = str
PipelineParameterName = str
PlatformIdentifier = str
PolicyString = str
PresignedDomainUrl = str
PriorityWeight = int
ProbabilityThresholdAttribute = float
ProcessingEnvironmentKey = str
ProcessingEnvironmentValue = str
ProcessingInstanceCount = int
ProcessingJobArn = str
ProcessingJobName = str
ProcessingLocalPath = str
ProcessingMaxRuntimeInSeconds = int
ProcessingVolumeSizeInGB = int
ProductId = str
ProductionVariantContainerStartupHealthCheckTimeoutInSeconds = int
ProductionVariantModelDataDownloadTimeoutInSeconds = int
ProductionVariantSSMAccess = bool
ProductionVariantVolumeSizeInGB = int
ProgrammingLang = str
ProjectArn = str
ProjectEntityName = str
ProjectId = str
PropertyNameHint = str
ProvisionedProductStatusMessage = str
ProvisioningParameterKey = str
ProvisioningParameterValue = str
QProfileArn = str
QueryLineageMaxDepth = int
QueryLineageMaxResults = int
RandomSeed = int
RecommendationFailureReason = str
RecommendationJobArn = str
RecommendationJobCompilationJobName = str
RecommendationJobDataInputConfig = str
RecommendationJobDescription = str
RecommendationJobFrameworkVersion = str
RecommendationJobName = str
RecommendationJobSupportedContentType = str
RecommendationJobSupportedResponseMIMEType = str
RecommendationJobVpcSecurityGroupId = str
RecommendationJobVpcSubnetId = str
RedshiftClusterId = str
RedshiftDatabase = str
RedshiftQueryString = str
RedshiftUserName = str
ReferenceMinVersion = str
RegionName = str
ReleaseNotes = str
RepositoryCredentialsProviderArn = str
RepositoryUrl = str
ReservedCapacityArn = str
ReservedCapacityInstanceCount = int
ResourceArn = str
ResourceCatalogArn = str
ResourceCatalogDescription = str
ResourceCatalogName = str
ResourceId = str
ResourcePolicyString = str
ResourcePropertyName = str
ResourceRetainedBillableTimeInSeconds = int
ResponseMIMEType = str
RoleArn = str
RuleConfigurationName = str
S3ModelUri = str
S3OutputPath = str
S3Uri = str
SageMakerImageVersionAlias = str
SageMakerPublicHubContentArn = str
SampleWeightAttributeName = str
SamplingPercentage = int
ScheduleExpression = str
Scope = str
SecretArn = str
SecurityGroupId = str
ServerlessMaxConcurrency = int
ServerlessMemorySizeInMB = int
ServerlessProvisionedConcurrency = int
ServiceCatalogEntityId = str
SessionExpirationDurationInSeconds = int
SingleSignOnApplicationArn = str
SingleSignOnUserIdentifier = str
SnsTopicArn = str
SourceType = str
SourceUri = str
SpaceArn = str
SpaceEbsVolumeSizeInGb = int
SpaceName = str
SpawnRate = int
StageDescription = str
StatusDetails = str
StatusMessage = str
StepDescription = str
StepDisplayName = str
StepName = str
String = str
String1024 = str
String128 = str
String200 = str
String2048 = str
String256 = str
String3072 = str
String40 = str
String64 = str
String8192 = str
StringParameterValue = str
StudioLifecycleConfigArn = str
StudioLifecycleConfigContent = str
StudioLifecycleConfigName = str
SubnetId = str
Success = bool
TableName = str
TagKey = str
TagValue = str
TargetAttributeName = str
TargetLabelColumn = str
TargetObjectiveMetricValue = float
TaskAvailabilityLifetimeInSeconds = int
TaskCount = int
TaskDescription = str
TaskInput = str
TaskKeyword = str
TaskTimeLimitInSeconds = int
TaskTitle = str
TemplateContent = str
TemplateContentSha256 = str
TemplateUrl = str
TenthFractionsOfACent = int
TerminationWaitInSeconds = int
TextGenerationHyperParameterKey = str
TextGenerationHyperParameterValue = str
ThingName = str
TimestampAttributeName = str
TotalInstanceCount = int
TrackingServerArn = str
TrackingServerName = str
TrackingServerUrl = str
TrafficDurationInSeconds = int
TrainingContainerArgument = str
TrainingContainerEntrypointString = str
TrainingEnvironmentKey = str
TrainingEnvironmentValue = str
TrainingInstanceCount = int
TrainingJobArn = str
TrainingJobName = str
TrainingJobStatusCounter = int
TrainingPlanArn = str
TrainingPlanName = str
TrainingPlanOfferingId = str
TrainingPlanStatusMessage = str
TrainingRepositoryCredentialsProviderArn = str
TrainingTimeInSeconds = int
TransformAmiVersion = str
TransformEnvironmentKey = str
TransformEnvironmentValue = str
TransformInstanceCount = int
TransformJobArn = str
TransformJobName = str
TransformationAttributeName = str
TrialArn = str
TrialComponentArn = str
TrialComponentArtifactValue = str
TrialComponentKey128 = str
TrialComponentKey256 = str
TrialComponentKey320 = str
TrialComponentSourceArn = str
TrialComponentStatusMessage = str
TrialSourceArn = str
TtlDurationValue = int
UnifiedStudioDomainId = str
UnifiedStudioEnvironmentId = str
UnifiedStudioProjectId = str
Url = str
UserProfileArn = str
UserProfileName = str
UsersPerStep = int
UtilizationMetric = float
UtilizationPercentagePerCore = int
ValidationFraction = float
VariantName = str
VariantStatusMessage = str
VariantWeight = float
VersionId = str
VersionedArnOrName = str
VisibilityConditionsKey = str
VisibilityConditionsValue = str
VolumeSizeInGB = int
VpcId = str
WaitIntervalInSeconds = int
WaitTimeIntervalInSeconds = int
WeeklyMaintenanceWindowStart = str
WeeklyScheduleTimeFormat = str
WorkforceArn = str
WorkforceFailureReason = str
WorkforceName = str
WorkforceSecurityGroupId = str
WorkforceSubnetId = str
WorkforceVpcEndpointId = str
WorkforceVpcId = str
WorkteamArn = str
WorkteamName = str


class ActionStatus(StrEnum):
    Unknown = "Unknown"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class ActivationState(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class AdditionalS3DataSourceDataType(StrEnum):
    S3Object = "S3Object"
    S3Prefix = "S3Prefix"


class AggregationTransformationValue(StrEnum):
    sum = "sum"
    avg = "avg"
    first = "first"
    min = "min"
    max = "max"


class AlgorithmSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class AlgorithmStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Deleting = "Deleting"


class AppImageConfigSortKey(StrEnum):
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"
    Name = "Name"


class AppInstanceType(StrEnum):
    system = "system"
    ml_t3_micro = "ml.t3.micro"
    ml_t3_small = "ml.t3.small"
    ml_t3_medium = "ml.t3.medium"
    ml_t3_large = "ml.t3.large"
    ml_t3_xlarge = "ml.t3.xlarge"
    ml_t3_2xlarge = "ml.t3.2xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_8xlarge = "ml.m5.8xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_16xlarge = "ml.m5.16xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_m5d_large = "ml.m5d.large"
    ml_m5d_xlarge = "ml.m5d.xlarge"
    ml_m5d_2xlarge = "ml.m5d.2xlarge"
    ml_m5d_4xlarge = "ml.m5d.4xlarge"
    ml_m5d_8xlarge = "ml.m5d.8xlarge"
    ml_m5d_12xlarge = "ml.m5d.12xlarge"
    ml_m5d_16xlarge = "ml.m5d.16xlarge"
    ml_m5d_24xlarge = "ml.m5d.24xlarge"
    ml_c5_large = "ml.c5.large"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_12xlarge = "ml.c5.12xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_c5_24xlarge = "ml.c5.24xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_p3dn_24xlarge = "ml.p3dn.24xlarge"
    ml_g4dn_xlarge = "ml.g4dn.xlarge"
    ml_g4dn_2xlarge = "ml.g4dn.2xlarge"
    ml_g4dn_4xlarge = "ml.g4dn.4xlarge"
    ml_g4dn_8xlarge = "ml.g4dn.8xlarge"
    ml_g4dn_12xlarge = "ml.g4dn.12xlarge"
    ml_g4dn_16xlarge = "ml.g4dn.16xlarge"
    ml_r5_large = "ml.r5.large"
    ml_r5_xlarge = "ml.r5.xlarge"
    ml_r5_2xlarge = "ml.r5.2xlarge"
    ml_r5_4xlarge = "ml.r5.4xlarge"
    ml_r5_8xlarge = "ml.r5.8xlarge"
    ml_r5_12xlarge = "ml.r5.12xlarge"
    ml_r5_16xlarge = "ml.r5.16xlarge"
    ml_r5_24xlarge = "ml.r5.24xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"
    ml_g6e_xlarge = "ml.g6e.xlarge"
    ml_g6e_2xlarge = "ml.g6e.2xlarge"
    ml_g6e_4xlarge = "ml.g6e.4xlarge"
    ml_g6e_8xlarge = "ml.g6e.8xlarge"
    ml_g6e_12xlarge = "ml.g6e.12xlarge"
    ml_g6e_16xlarge = "ml.g6e.16xlarge"
    ml_g6e_24xlarge = "ml.g6e.24xlarge"
    ml_g6e_48xlarge = "ml.g6e.48xlarge"
    ml_geospatial_interactive = "ml.geospatial.interactive"
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_p4de_24xlarge = "ml.p4de.24xlarge"
    ml_trn1_2xlarge = "ml.trn1.2xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn1n_32xlarge = "ml.trn1n.32xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_p5en_48xlarge = "ml.p5en.48xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_m7i_large = "ml.m7i.large"
    ml_m7i_xlarge = "ml.m7i.xlarge"
    ml_m7i_2xlarge = "ml.m7i.2xlarge"
    ml_m7i_4xlarge = "ml.m7i.4xlarge"
    ml_m7i_8xlarge = "ml.m7i.8xlarge"
    ml_m7i_12xlarge = "ml.m7i.12xlarge"
    ml_m7i_16xlarge = "ml.m7i.16xlarge"
    ml_m7i_24xlarge = "ml.m7i.24xlarge"
    ml_m7i_48xlarge = "ml.m7i.48xlarge"
    ml_c6i_large = "ml.c6i.large"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"
    ml_c7i_large = "ml.c7i.large"
    ml_c7i_xlarge = "ml.c7i.xlarge"
    ml_c7i_2xlarge = "ml.c7i.2xlarge"
    ml_c7i_4xlarge = "ml.c7i.4xlarge"
    ml_c7i_8xlarge = "ml.c7i.8xlarge"
    ml_c7i_12xlarge = "ml.c7i.12xlarge"
    ml_c7i_16xlarge = "ml.c7i.16xlarge"
    ml_c7i_24xlarge = "ml.c7i.24xlarge"
    ml_c7i_48xlarge = "ml.c7i.48xlarge"
    ml_r6i_large = "ml.r6i.large"
    ml_r6i_xlarge = "ml.r6i.xlarge"
    ml_r6i_2xlarge = "ml.r6i.2xlarge"
    ml_r6i_4xlarge = "ml.r6i.4xlarge"
    ml_r6i_8xlarge = "ml.r6i.8xlarge"
    ml_r6i_12xlarge = "ml.r6i.12xlarge"
    ml_r6i_16xlarge = "ml.r6i.16xlarge"
    ml_r6i_24xlarge = "ml.r6i.24xlarge"
    ml_r6i_32xlarge = "ml.r6i.32xlarge"
    ml_r7i_large = "ml.r7i.large"
    ml_r7i_xlarge = "ml.r7i.xlarge"
    ml_r7i_2xlarge = "ml.r7i.2xlarge"
    ml_r7i_4xlarge = "ml.r7i.4xlarge"
    ml_r7i_8xlarge = "ml.r7i.8xlarge"
    ml_r7i_12xlarge = "ml.r7i.12xlarge"
    ml_r7i_16xlarge = "ml.r7i.16xlarge"
    ml_r7i_24xlarge = "ml.r7i.24xlarge"
    ml_r7i_48xlarge = "ml.r7i.48xlarge"
    ml_m6id_large = "ml.m6id.large"
    ml_m6id_xlarge = "ml.m6id.xlarge"
    ml_m6id_2xlarge = "ml.m6id.2xlarge"
    ml_m6id_4xlarge = "ml.m6id.4xlarge"
    ml_m6id_8xlarge = "ml.m6id.8xlarge"
    ml_m6id_12xlarge = "ml.m6id.12xlarge"
    ml_m6id_16xlarge = "ml.m6id.16xlarge"
    ml_m6id_24xlarge = "ml.m6id.24xlarge"
    ml_m6id_32xlarge = "ml.m6id.32xlarge"
    ml_c6id_large = "ml.c6id.large"
    ml_c6id_xlarge = "ml.c6id.xlarge"
    ml_c6id_2xlarge = "ml.c6id.2xlarge"
    ml_c6id_4xlarge = "ml.c6id.4xlarge"
    ml_c6id_8xlarge = "ml.c6id.8xlarge"
    ml_c6id_12xlarge = "ml.c6id.12xlarge"
    ml_c6id_16xlarge = "ml.c6id.16xlarge"
    ml_c6id_24xlarge = "ml.c6id.24xlarge"
    ml_c6id_32xlarge = "ml.c6id.32xlarge"
    ml_r6id_large = "ml.r6id.large"
    ml_r6id_xlarge = "ml.r6id.xlarge"
    ml_r6id_2xlarge = "ml.r6id.2xlarge"
    ml_r6id_4xlarge = "ml.r6id.4xlarge"
    ml_r6id_8xlarge = "ml.r6id.8xlarge"
    ml_r6id_12xlarge = "ml.r6id.12xlarge"
    ml_r6id_16xlarge = "ml.r6id.16xlarge"
    ml_r6id_24xlarge = "ml.r6id.24xlarge"
    ml_r6id_32xlarge = "ml.r6id.32xlarge"


class AppNetworkAccessType(StrEnum):
    PublicInternetOnly = "PublicInternetOnly"
    VpcOnly = "VpcOnly"


class AppSecurityGroupManagement(StrEnum):
    Service = "Service"
    Customer = "Customer"


class AppSortKey(StrEnum):
    CreationTime = "CreationTime"


class AppStatus(StrEnum):
    Deleted = "Deleted"
    Deleting = "Deleting"
    Failed = "Failed"
    InService = "InService"
    Pending = "Pending"


class AppType(StrEnum):
    JupyterServer = "JupyterServer"
    KernelGateway = "KernelGateway"
    DetailedProfiler = "DetailedProfiler"
    TensorBoard = "TensorBoard"
    CodeEditor = "CodeEditor"
    JupyterLab = "JupyterLab"
    RStudioServerPro = "RStudioServerPro"
    RSessionGateway = "RSessionGateway"
    Canvas = "Canvas"


class ArtifactSourceIdType(StrEnum):
    MD5Hash = "MD5Hash"
    S3ETag = "S3ETag"
    S3Version = "S3Version"
    Custom = "Custom"


class AssemblyType(StrEnum):
    None_ = "None"
    Line = "Line"


class AssociationEdgeType(StrEnum):
    ContributedTo = "ContributedTo"
    AssociatedWith = "AssociatedWith"
    DerivedFrom = "DerivedFrom"
    Produced = "Produced"
    SameAs = "SameAs"


class AsyncNotificationTopicTypes(StrEnum):
    SUCCESS_NOTIFICATION_TOPIC = "SUCCESS_NOTIFICATION_TOPIC"
    ERROR_NOTIFICATION_TOPIC = "ERROR_NOTIFICATION_TOPIC"


class AthenaResultCompressionType(StrEnum):
    GZIP = "GZIP"
    SNAPPY = "SNAPPY"
    ZLIB = "ZLIB"


class AthenaResultFormat(StrEnum):
    PARQUET = "PARQUET"
    ORC = "ORC"
    AVRO = "AVRO"
    JSON = "JSON"
    TEXTFILE = "TEXTFILE"


class AuthMode(StrEnum):
    SSO = "SSO"
    IAM = "IAM"


class AutoMLAlgorithm(StrEnum):
    xgboost = "xgboost"
    linear_learner = "linear-learner"
    mlp = "mlp"
    lightgbm = "lightgbm"
    catboost = "catboost"
    randomforest = "randomforest"
    extra_trees = "extra-trees"
    nn_torch = "nn-torch"
    fastai = "fastai"
    cnn_qr = "cnn-qr"
    deepar = "deepar"
    prophet = "prophet"
    npts = "npts"
    arima = "arima"
    ets = "ets"


class AutoMLChannelType(StrEnum):
    training = "training"
    validation = "validation"


class AutoMLJobObjectiveType(StrEnum):
    Maximize = "Maximize"
    Minimize = "Minimize"


class AutoMLJobSecondaryStatus(StrEnum):
    Starting = "Starting"
    MaxCandidatesReached = "MaxCandidatesReached"
    Failed = "Failed"
    Stopped = "Stopped"
    MaxAutoMLJobRuntimeReached = "MaxAutoMLJobRuntimeReached"
    Stopping = "Stopping"
    CandidateDefinitionsGenerated = "CandidateDefinitionsGenerated"
    Completed = "Completed"
    ExplainabilityError = "ExplainabilityError"
    DeployingModel = "DeployingModel"
    ModelDeploymentError = "ModelDeploymentError"
    GeneratingModelInsightsReport = "GeneratingModelInsightsReport"
    ModelInsightsError = "ModelInsightsError"
    AnalyzingData = "AnalyzingData"
    FeatureEngineering = "FeatureEngineering"
    ModelTuning = "ModelTuning"
    GeneratingExplainabilityReport = "GeneratingExplainabilityReport"
    TrainingModels = "TrainingModels"
    PreTraining = "PreTraining"


class AutoMLJobStatus(StrEnum):
    Completed = "Completed"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"


class AutoMLMetricEnum(StrEnum):
    Accuracy = "Accuracy"
    MSE = "MSE"
    F1 = "F1"
    F1macro = "F1macro"
    AUC = "AUC"
    RMSE = "RMSE"
    BalancedAccuracy = "BalancedAccuracy"
    R2 = "R2"
    Recall = "Recall"
    RecallMacro = "RecallMacro"
    Precision = "Precision"
    PrecisionMacro = "PrecisionMacro"
    MAE = "MAE"
    MAPE = "MAPE"
    MASE = "MASE"
    WAPE = "WAPE"
    AverageWeightedQuantileLoss = "AverageWeightedQuantileLoss"


class AutoMLMetricExtendedEnum(StrEnum):
    Accuracy = "Accuracy"
    MSE = "MSE"
    F1 = "F1"
    F1macro = "F1macro"
    AUC = "AUC"
    RMSE = "RMSE"
    MAE = "MAE"
    R2 = "R2"
    BalancedAccuracy = "BalancedAccuracy"
    Precision = "Precision"
    PrecisionMacro = "PrecisionMacro"
    Recall = "Recall"
    RecallMacro = "RecallMacro"
    LogLoss = "LogLoss"
    InferenceLatency = "InferenceLatency"
    MAPE = "MAPE"
    MASE = "MASE"
    WAPE = "WAPE"
    AverageWeightedQuantileLoss = "AverageWeightedQuantileLoss"
    Rouge1 = "Rouge1"
    Rouge2 = "Rouge2"
    RougeL = "RougeL"
    RougeLSum = "RougeLSum"
    Perplexity = "Perplexity"
    ValidationLoss = "ValidationLoss"
    TrainingLoss = "TrainingLoss"


class AutoMLMode(StrEnum):
    AUTO = "AUTO"
    ENSEMBLING = "ENSEMBLING"
    HYPERPARAMETER_TUNING = "HYPERPARAMETER_TUNING"


class AutoMLProblemTypeConfigName(StrEnum):
    ImageClassification = "ImageClassification"
    TextClassification = "TextClassification"
    TimeSeriesForecasting = "TimeSeriesForecasting"
    Tabular = "Tabular"
    TextGeneration = "TextGeneration"


class AutoMLProcessingUnit(StrEnum):
    CPU = "CPU"
    GPU = "GPU"


class AutoMLS3DataType(StrEnum):
    ManifestFile = "ManifestFile"
    S3Prefix = "S3Prefix"
    AugmentedManifestFile = "AugmentedManifestFile"


class AutoMLSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class AutoMLSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class AutoMountHomeEFS(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"
    DefaultAsDomain = "DefaultAsDomain"


class AutotuneMode(StrEnum):
    Enabled = "Enabled"


class AwsManagedHumanLoopRequestSource(StrEnum):
    AWS_Rekognition_DetectModerationLabels_Image_V3 = (
        "AWS/Rekognition/DetectModerationLabels/Image/V3"
    )
    AWS_Textract_AnalyzeDocument_Forms_V1 = "AWS/Textract/AnalyzeDocument/Forms/V1"


class BatchDeleteClusterNodesErrorCode(StrEnum):
    NodeIdNotFound = "NodeIdNotFound"
    InvalidNodeStatus = "InvalidNodeStatus"
    NodeIdInUse = "NodeIdInUse"


class BatchStrategy(StrEnum):
    MultiRecord = "MultiRecord"
    SingleRecord = "SingleRecord"


class BooleanOperator(StrEnum):
    And = "And"
    Or = "Or"


class CandidateSortBy(StrEnum):
    CreationTime = "CreationTime"
    Status = "Status"
    FinalObjectiveMetricValue = "FinalObjectiveMetricValue"


class CandidateStatus(StrEnum):
    Completed = "Completed"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"


class CandidateStepType(StrEnum):
    AWS_SageMaker_TrainingJob = "AWS::SageMaker::TrainingJob"
    AWS_SageMaker_TransformJob = "AWS::SageMaker::TransformJob"
    AWS_SageMaker_ProcessingJob = "AWS::SageMaker::ProcessingJob"


class CapacityReservationPreference(StrEnum):
    capacity_reservations_only = "capacity-reservations-only"


class CapacitySizeType(StrEnum):
    INSTANCE_COUNT = "INSTANCE_COUNT"
    CAPACITY_PERCENT = "CAPACITY_PERCENT"


class CaptureMode(StrEnum):
    Input = "Input"
    Output = "Output"
    InputAndOutput = "InputAndOutput"


class CaptureStatus(StrEnum):
    Started = "Started"
    Stopped = "Stopped"


class ClarifyFeatureType(StrEnum):
    numerical = "numerical"
    categorical = "categorical"
    text = "text"


class ClarifyTextGranularity(StrEnum):
    token = "token"
    sentence = "sentence"
    paragraph = "paragraph"


class ClarifyTextLanguage(StrEnum):
    af = "af"
    sq = "sq"
    ar = "ar"
    hy = "hy"
    eu = "eu"
    bn = "bn"
    bg = "bg"
    ca = "ca"
    zh = "zh"
    hr = "hr"
    cs = "cs"
    da = "da"
    nl = "nl"
    en = "en"
    et = "et"
    fi = "fi"
    fr = "fr"
    de = "de"
    el = "el"
    gu = "gu"
    he = "he"
    hi = "hi"
    hu = "hu"
    is_ = "is"
    id = "id"
    ga = "ga"
    it = "it"
    kn = "kn"
    ky = "ky"
    lv = "lv"
    lt = "lt"
    lb = "lb"
    mk = "mk"
    ml = "ml"
    mr = "mr"
    ne = "ne"
    nb = "nb"
    fa = "fa"
    pl = "pl"
    pt = "pt"
    ro = "ro"
    ru = "ru"
    sa = "sa"
    sr = "sr"
    tn = "tn"
    si = "si"
    sk = "sk"
    sl = "sl"
    es = "es"
    sv = "sv"
    tl = "tl"
    ta = "ta"
    tt = "tt"
    te = "te"
    tr = "tr"
    uk = "uk"
    ur = "ur"
    yo = "yo"
    lij = "lij"
    xx = "xx"


class ClusterInstanceStatus(StrEnum):
    Running = "Running"
    Failure = "Failure"
    Pending = "Pending"
    ShuttingDown = "ShuttingDown"
    SystemUpdating = "SystemUpdating"
    DeepHealthCheckInProgress = "DeepHealthCheckInProgress"


class ClusterInstanceType(StrEnum):
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_p4de_24xlarge = "ml.p4de.24xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn1n_32xlarge = "ml.trn1n.32xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_c5_large = "ml.c5.large"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_12xlarge = "ml.c5.12xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_c5_24xlarge = "ml.c5.24xlarge"
    ml_c5n_large = "ml.c5n.large"
    ml_c5n_2xlarge = "ml.c5n.2xlarge"
    ml_c5n_4xlarge = "ml.c5n.4xlarge"
    ml_c5n_9xlarge = "ml.c5n.9xlarge"
    ml_c5n_18xlarge = "ml.c5n.18xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_8xlarge = "ml.m5.8xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_16xlarge = "ml.m5.16xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_t3_medium = "ml.t3.medium"
    ml_t3_large = "ml.t3.large"
    ml_t3_xlarge = "ml.t3.xlarge"
    ml_t3_2xlarge = "ml.t3.2xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"
    ml_gr6_4xlarge = "ml.gr6.4xlarge"
    ml_gr6_8xlarge = "ml.gr6.8xlarge"
    ml_g6e_xlarge = "ml.g6e.xlarge"
    ml_g6e_2xlarge = "ml.g6e.2xlarge"
    ml_g6e_4xlarge = "ml.g6e.4xlarge"
    ml_g6e_8xlarge = "ml.g6e.8xlarge"
    ml_g6e_16xlarge = "ml.g6e.16xlarge"
    ml_g6e_12xlarge = "ml.g6e.12xlarge"
    ml_g6e_24xlarge = "ml.g6e.24xlarge"
    ml_g6e_48xlarge = "ml.g6e.48xlarge"
    ml_p5e_48xlarge = "ml.p5e.48xlarge"
    ml_p5en_48xlarge = "ml.p5en.48xlarge"
    ml_trn2_48xlarge = "ml.trn2.48xlarge"
    ml_c6i_large = "ml.c6i.large"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_r6i_large = "ml.r6i.large"
    ml_r6i_xlarge = "ml.r6i.xlarge"
    ml_r6i_2xlarge = "ml.r6i.2xlarge"
    ml_r6i_4xlarge = "ml.r6i.4xlarge"
    ml_r6i_8xlarge = "ml.r6i.8xlarge"
    ml_r6i_12xlarge = "ml.r6i.12xlarge"
    ml_r6i_16xlarge = "ml.r6i.16xlarge"
    ml_r6i_24xlarge = "ml.r6i.24xlarge"
    ml_r6i_32xlarge = "ml.r6i.32xlarge"
    ml_i3en_large = "ml.i3en.large"
    ml_i3en_xlarge = "ml.i3en.xlarge"
    ml_i3en_2xlarge = "ml.i3en.2xlarge"
    ml_i3en_3xlarge = "ml.i3en.3xlarge"
    ml_i3en_6xlarge = "ml.i3en.6xlarge"
    ml_i3en_12xlarge = "ml.i3en.12xlarge"
    ml_i3en_24xlarge = "ml.i3en.24xlarge"
    ml_m7i_large = "ml.m7i.large"
    ml_m7i_xlarge = "ml.m7i.xlarge"
    ml_m7i_2xlarge = "ml.m7i.2xlarge"
    ml_m7i_4xlarge = "ml.m7i.4xlarge"
    ml_m7i_8xlarge = "ml.m7i.8xlarge"
    ml_m7i_12xlarge = "ml.m7i.12xlarge"
    ml_m7i_16xlarge = "ml.m7i.16xlarge"
    ml_m7i_24xlarge = "ml.m7i.24xlarge"
    ml_m7i_48xlarge = "ml.m7i.48xlarge"
    ml_r7i_large = "ml.r7i.large"
    ml_r7i_xlarge = "ml.r7i.xlarge"
    ml_r7i_2xlarge = "ml.r7i.2xlarge"
    ml_r7i_4xlarge = "ml.r7i.4xlarge"
    ml_r7i_8xlarge = "ml.r7i.8xlarge"
    ml_r7i_12xlarge = "ml.r7i.12xlarge"
    ml_r7i_16xlarge = "ml.r7i.16xlarge"
    ml_r7i_24xlarge = "ml.r7i.24xlarge"
    ml_r7i_48xlarge = "ml.r7i.48xlarge"


class ClusterNodeRecovery(StrEnum):
    Automatic = "Automatic"
    None_ = "None"


class ClusterSortBy(StrEnum):
    CREATION_TIME = "CREATION_TIME"
    NAME = "NAME"


class ClusterStatus(StrEnum):
    Creating = "Creating"
    Deleting = "Deleting"
    Failed = "Failed"
    InService = "InService"
    RollingBack = "RollingBack"
    SystemUpdating = "SystemUpdating"
    Updating = "Updating"


class CodeRepositorySortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"


class CodeRepositorySortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class CollectionType(StrEnum):
    List = "List"
    Set = "Set"
    Vector = "Vector"


class CompilationJobStatus(StrEnum):
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class CompleteOnConvergence(StrEnum):
    Disabled = "Disabled"
    Enabled = "Enabled"


class CompressionType(StrEnum):
    None_ = "None"
    Gzip = "Gzip"


class ConditionOutcome(StrEnum):
    True_ = "True"
    False_ = "False"


class ContainerMode(StrEnum):
    SingleModel = "SingleModel"
    MultiModel = "MultiModel"


class ContentClassifier(StrEnum):
    FreeOfPersonallyIdentifiableInformation = "FreeOfPersonallyIdentifiableInformation"
    FreeOfAdultContent = "FreeOfAdultContent"


class CrossAccountFilterOption(StrEnum):
    SameAccount = "SameAccount"
    CrossAccount = "CrossAccount"


class DataDistributionType(StrEnum):
    FullyReplicated = "FullyReplicated"
    ShardedByS3Key = "ShardedByS3Key"


class DataSourceName(StrEnum):
    SalesforceGenie = "SalesforceGenie"
    Snowflake = "Snowflake"


class DeepHealthCheckType(StrEnum):
    InstanceStress = "InstanceStress"
    InstanceConnectivity = "InstanceConnectivity"


class DetailedAlgorithmStatus(StrEnum):
    NotStarted = "NotStarted"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"


class DetailedModelPackageStatus(StrEnum):
    NotStarted = "NotStarted"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"


class DeviceDeploymentStatus(StrEnum):
    READYTODEPLOY = "READYTODEPLOY"
    INPROGRESS = "INPROGRESS"
    DEPLOYED = "DEPLOYED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class DeviceSubsetType(StrEnum):
    PERCENTAGE = "PERCENTAGE"
    SELECTION = "SELECTION"
    NAMECONTAINS = "NAMECONTAINS"


class DirectInternetAccess(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class Direction(StrEnum):
    Both = "Both"
    Ascendants = "Ascendants"
    Descendants = "Descendants"


class DomainStatus(StrEnum):
    Deleting = "Deleting"
    Failed = "Failed"
    InService = "InService"
    Pending = "Pending"
    Updating = "Updating"
    Update_Failed = "Update_Failed"
    Delete_Failed = "Delete_Failed"


class EdgePackagingJobStatus(StrEnum):
    STARTING = "STARTING"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class EdgePresetDeploymentStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class EdgePresetDeploymentType(StrEnum):
    GreengrassV2Component = "GreengrassV2Component"


class EnabledOrDisabled(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class EndpointConfigSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class EndpointSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class EndpointStatus(StrEnum):
    OutOfService = "OutOfService"
    Creating = "Creating"
    Updating = "Updating"
    SystemUpdating = "SystemUpdating"
    RollingBack = "RollingBack"
    InService = "InService"
    Deleting = "Deleting"
    Failed = "Failed"
    UpdateRollbackFailed = "UpdateRollbackFailed"


class ExecutionRoleIdentityConfig(StrEnum):
    USER_PROFILE_NAME = "USER_PROFILE_NAME"
    DISABLED = "DISABLED"


class ExecutionStatus(StrEnum):
    Pending = "Pending"
    Completed = "Completed"
    CompletedWithViolations = "CompletedWithViolations"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class FailureHandlingPolicy(StrEnum):
    ROLLBACK_ON_FAILURE = "ROLLBACK_ON_FAILURE"
    DO_NOTHING = "DO_NOTHING"


class FairShare(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class FeatureGroupSortBy(StrEnum):
    Name = "Name"
    FeatureGroupStatus = "FeatureGroupStatus"
    OfflineStoreStatus = "OfflineStoreStatus"
    CreationTime = "CreationTime"


class FeatureGroupSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class FeatureGroupStatus(StrEnum):
    Creating = "Creating"
    Created = "Created"
    CreateFailed = "CreateFailed"
    Deleting = "Deleting"
    DeleteFailed = "DeleteFailed"


class FeatureStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FeatureType(StrEnum):
    Integral = "Integral"
    Fractional = "Fractional"
    String = "String"


class FileSystemAccessMode(StrEnum):
    rw = "rw"
    ro = "ro"


class FileSystemType(StrEnum):
    EFS = "EFS"
    FSxLustre = "FSxLustre"


class FillingType(StrEnum):
    frontfill = "frontfill"
    middlefill = "middlefill"
    backfill = "backfill"
    futurefill = "futurefill"
    frontfill_value = "frontfill_value"
    middlefill_value = "middlefill_value"
    backfill_value = "backfill_value"
    futurefill_value = "futurefill_value"


class FlatInvocations(StrEnum):
    Continue = "Continue"
    Stop = "Stop"


class FlowDefinitionStatus(StrEnum):
    Initializing = "Initializing"
    Active = "Active"
    Failed = "Failed"
    Deleting = "Deleting"


class Framework(StrEnum):
    TENSORFLOW = "TENSORFLOW"
    KERAS = "KERAS"
    MXNET = "MXNET"
    ONNX = "ONNX"
    PYTORCH = "PYTORCH"
    XGBOOST = "XGBOOST"
    TFLITE = "TFLITE"
    DARKNET = "DARKNET"
    SKLEARN = "SKLEARN"


class HubContentSortBy(StrEnum):
    HubContentName = "HubContentName"
    CreationTime = "CreationTime"
    HubContentStatus = "HubContentStatus"


class HubContentStatus(StrEnum):
    Available = "Available"
    Importing = "Importing"
    Deleting = "Deleting"
    ImportFailed = "ImportFailed"
    DeleteFailed = "DeleteFailed"


class HubContentSupportStatus(StrEnum):
    Supported = "Supported"
    Deprecated = "Deprecated"
    Restricted = "Restricted"


class HubContentType(StrEnum):
    Model = "Model"
    Notebook = "Notebook"
    ModelReference = "ModelReference"


class HubSortBy(StrEnum):
    HubName = "HubName"
    CreationTime = "CreationTime"
    HubStatus = "HubStatus"
    AccountIdOwner = "AccountIdOwner"


class HubStatus(StrEnum):
    InService = "InService"
    Creating = "Creating"
    Updating = "Updating"
    Deleting = "Deleting"
    CreateFailed = "CreateFailed"
    UpdateFailed = "UpdateFailed"
    DeleteFailed = "DeleteFailed"


class HumanTaskUiStatus(StrEnum):
    Active = "Active"
    Deleting = "Deleting"


class HyperParameterScalingType(StrEnum):
    Auto = "Auto"
    Linear = "Linear"
    Logarithmic = "Logarithmic"
    ReverseLogarithmic = "ReverseLogarithmic"


class HyperParameterTuningAllocationStrategy(StrEnum):
    Prioritized = "Prioritized"


class HyperParameterTuningJobObjectiveType(StrEnum):
    Maximize = "Maximize"
    Minimize = "Minimize"


class HyperParameterTuningJobSortByOptions(StrEnum):
    Name = "Name"
    Status = "Status"
    CreationTime = "CreationTime"


class HyperParameterTuningJobStatus(StrEnum):
    Completed = "Completed"
    InProgress = "InProgress"
    Failed = "Failed"
    Stopped = "Stopped"
    Stopping = "Stopping"
    Deleting = "Deleting"
    DeleteFailed = "DeleteFailed"


class HyperParameterTuningJobStrategyType(StrEnum):
    Bayesian = "Bayesian"
    Random = "Random"
    Hyperband = "Hyperband"
    Grid = "Grid"


class HyperParameterTuningJobWarmStartType(StrEnum):
    IdenticalDataAndAlgorithm = "IdenticalDataAndAlgorithm"
    TransferLearning = "TransferLearning"


class ImageSortBy(StrEnum):
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"
    IMAGE_NAME = "IMAGE_NAME"


class ImageSortOrder(StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ImageStatus(StrEnum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class ImageVersionSortBy(StrEnum):
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"
    VERSION = "VERSION"


class ImageVersionSortOrder(StrEnum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ImageVersionStatus(StrEnum):
    CREATING = "CREATING"
    CREATED = "CREATED"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class InferenceComponentCapacitySizeType(StrEnum):
    COPY_COUNT = "COPY_COUNT"
    CAPACITY_PERCENT = "CAPACITY_PERCENT"


class InferenceComponentSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class InferenceComponentStatus(StrEnum):
    InService = "InService"
    Creating = "Creating"
    Updating = "Updating"
    Failed = "Failed"
    Deleting = "Deleting"


class InferenceExecutionMode(StrEnum):
    Serial = "Serial"
    Direct = "Direct"


class InferenceExperimentStatus(StrEnum):
    Creating = "Creating"
    Created = "Created"
    Updating = "Updating"
    Running = "Running"
    Starting = "Starting"
    Stopping = "Stopping"
    Completed = "Completed"
    Cancelled = "Cancelled"


class InferenceExperimentStopDesiredState(StrEnum):
    Completed = "Completed"
    Cancelled = "Cancelled"


class InferenceExperimentType(StrEnum):
    ShadowMode = "ShadowMode"


class InputMode(StrEnum):
    Pipe = "Pipe"
    File = "File"


class InstanceGroupStatus(StrEnum):
    InService = "InService"
    Creating = "Creating"
    Updating = "Updating"
    Failed = "Failed"
    Degraded = "Degraded"
    SystemUpdating = "SystemUpdating"
    Deleting = "Deleting"


class InstanceType(StrEnum):
    ml_t2_medium = "ml.t2.medium"
    ml_t2_large = "ml.t2.large"
    ml_t2_xlarge = "ml.t2.xlarge"
    ml_t2_2xlarge = "ml.t2.2xlarge"
    ml_t3_medium = "ml.t3.medium"
    ml_t3_large = "ml.t3.large"
    ml_t3_xlarge = "ml.t3.xlarge"
    ml_t3_2xlarge = "ml.t3.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_m5d_large = "ml.m5d.large"
    ml_m5d_xlarge = "ml.m5d.xlarge"
    ml_m5d_2xlarge = "ml.m5d.2xlarge"
    ml_m5d_4xlarge = "ml.m5d.4xlarge"
    ml_m5d_8xlarge = "ml.m5d.8xlarge"
    ml_m5d_12xlarge = "ml.m5d.12xlarge"
    ml_m5d_16xlarge = "ml.m5d.16xlarge"
    ml_m5d_24xlarge = "ml.m5d.24xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_c5d_xlarge = "ml.c5d.xlarge"
    ml_c5d_2xlarge = "ml.c5d.2xlarge"
    ml_c5d_4xlarge = "ml.c5d.4xlarge"
    ml_c5d_9xlarge = "ml.c5d.9xlarge"
    ml_c5d_18xlarge = "ml.c5d.18xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_p3dn_24xlarge = "ml.p3dn.24xlarge"
    ml_g4dn_xlarge = "ml.g4dn.xlarge"
    ml_g4dn_2xlarge = "ml.g4dn.2xlarge"
    ml_g4dn_4xlarge = "ml.g4dn.4xlarge"
    ml_g4dn_8xlarge = "ml.g4dn.8xlarge"
    ml_g4dn_12xlarge = "ml.g4dn.12xlarge"
    ml_g4dn_16xlarge = "ml.g4dn.16xlarge"
    ml_r5_large = "ml.r5.large"
    ml_r5_xlarge = "ml.r5.xlarge"
    ml_r5_2xlarge = "ml.r5.2xlarge"
    ml_r5_4xlarge = "ml.r5.4xlarge"
    ml_r5_8xlarge = "ml.r5.8xlarge"
    ml_r5_12xlarge = "ml.r5.12xlarge"
    ml_r5_16xlarge = "ml.r5.16xlarge"
    ml_r5_24xlarge = "ml.r5.24xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_inf1_xlarge = "ml.inf1.xlarge"
    ml_inf1_2xlarge = "ml.inf1.2xlarge"
    ml_inf1_6xlarge = "ml.inf1.6xlarge"
    ml_inf1_24xlarge = "ml.inf1.24xlarge"
    ml_trn1_2xlarge = "ml.trn1.2xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn1n_32xlarge = "ml.trn1n.32xlarge"
    ml_inf2_xlarge = "ml.inf2.xlarge"
    ml_inf2_8xlarge = "ml.inf2.8xlarge"
    ml_inf2_24xlarge = "ml.inf2.24xlarge"
    ml_inf2_48xlarge = "ml.inf2.48xlarge"
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_p4de_24xlarge = "ml.p4de.24xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_m7i_large = "ml.m7i.large"
    ml_m7i_xlarge = "ml.m7i.xlarge"
    ml_m7i_2xlarge = "ml.m7i.2xlarge"
    ml_m7i_4xlarge = "ml.m7i.4xlarge"
    ml_m7i_8xlarge = "ml.m7i.8xlarge"
    ml_m7i_12xlarge = "ml.m7i.12xlarge"
    ml_m7i_16xlarge = "ml.m7i.16xlarge"
    ml_m7i_24xlarge = "ml.m7i.24xlarge"
    ml_m7i_48xlarge = "ml.m7i.48xlarge"
    ml_c6i_large = "ml.c6i.large"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"
    ml_c7i_large = "ml.c7i.large"
    ml_c7i_xlarge = "ml.c7i.xlarge"
    ml_c7i_2xlarge = "ml.c7i.2xlarge"
    ml_c7i_4xlarge = "ml.c7i.4xlarge"
    ml_c7i_8xlarge = "ml.c7i.8xlarge"
    ml_c7i_12xlarge = "ml.c7i.12xlarge"
    ml_c7i_16xlarge = "ml.c7i.16xlarge"
    ml_c7i_24xlarge = "ml.c7i.24xlarge"
    ml_c7i_48xlarge = "ml.c7i.48xlarge"
    ml_r6i_large = "ml.r6i.large"
    ml_r6i_xlarge = "ml.r6i.xlarge"
    ml_r6i_2xlarge = "ml.r6i.2xlarge"
    ml_r6i_4xlarge = "ml.r6i.4xlarge"
    ml_r6i_8xlarge = "ml.r6i.8xlarge"
    ml_r6i_12xlarge = "ml.r6i.12xlarge"
    ml_r6i_16xlarge = "ml.r6i.16xlarge"
    ml_r6i_24xlarge = "ml.r6i.24xlarge"
    ml_r6i_32xlarge = "ml.r6i.32xlarge"
    ml_r7i_large = "ml.r7i.large"
    ml_r7i_xlarge = "ml.r7i.xlarge"
    ml_r7i_2xlarge = "ml.r7i.2xlarge"
    ml_r7i_4xlarge = "ml.r7i.4xlarge"
    ml_r7i_8xlarge = "ml.r7i.8xlarge"
    ml_r7i_12xlarge = "ml.r7i.12xlarge"
    ml_r7i_16xlarge = "ml.r7i.16xlarge"
    ml_r7i_24xlarge = "ml.r7i.24xlarge"
    ml_r7i_48xlarge = "ml.r7i.48xlarge"
    ml_m6id_large = "ml.m6id.large"
    ml_m6id_xlarge = "ml.m6id.xlarge"
    ml_m6id_2xlarge = "ml.m6id.2xlarge"
    ml_m6id_4xlarge = "ml.m6id.4xlarge"
    ml_m6id_8xlarge = "ml.m6id.8xlarge"
    ml_m6id_12xlarge = "ml.m6id.12xlarge"
    ml_m6id_16xlarge = "ml.m6id.16xlarge"
    ml_m6id_24xlarge = "ml.m6id.24xlarge"
    ml_m6id_32xlarge = "ml.m6id.32xlarge"
    ml_c6id_large = "ml.c6id.large"
    ml_c6id_xlarge = "ml.c6id.xlarge"
    ml_c6id_2xlarge = "ml.c6id.2xlarge"
    ml_c6id_4xlarge = "ml.c6id.4xlarge"
    ml_c6id_8xlarge = "ml.c6id.8xlarge"
    ml_c6id_12xlarge = "ml.c6id.12xlarge"
    ml_c6id_16xlarge = "ml.c6id.16xlarge"
    ml_c6id_24xlarge = "ml.c6id.24xlarge"
    ml_c6id_32xlarge = "ml.c6id.32xlarge"
    ml_r6id_large = "ml.r6id.large"
    ml_r6id_xlarge = "ml.r6id.xlarge"
    ml_r6id_2xlarge = "ml.r6id.2xlarge"
    ml_r6id_4xlarge = "ml.r6id.4xlarge"
    ml_r6id_8xlarge = "ml.r6id.8xlarge"
    ml_r6id_12xlarge = "ml.r6id.12xlarge"
    ml_r6id_16xlarge = "ml.r6id.16xlarge"
    ml_r6id_24xlarge = "ml.r6id.24xlarge"
    ml_r6id_32xlarge = "ml.r6id.32xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"


class IsTrackingServerActive(StrEnum):
    Active = "Active"
    Inactive = "Inactive"


class JobType(StrEnum):
    TRAINING = "TRAINING"
    INFERENCE = "INFERENCE"
    NOTEBOOK_KERNEL = "NOTEBOOK_KERNEL"


class JoinSource(StrEnum):
    Input = "Input"
    None_ = "None"


class LabelingJobStatus(StrEnum):
    Initializing = "Initializing"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class LastUpdateStatusValue(StrEnum):
    Successful = "Successful"
    Failed = "Failed"
    InProgress = "InProgress"


class LifecycleManagement(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class LineageType(StrEnum):
    TrialComponent = "TrialComponent"
    Artifact = "Artifact"
    Context = "Context"
    Action = "Action"


class ListCompilationJobsSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class ListDeviceFleetsSortBy(StrEnum):
    NAME = "NAME"
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ListEdgeDeploymentPlansSortBy(StrEnum):
    NAME = "NAME"
    DEVICE_FLEET_NAME = "DEVICE_FLEET_NAME"
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ListEdgePackagingJobsSortBy(StrEnum):
    NAME = "NAME"
    MODEL_NAME = "MODEL_NAME"
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"
    STATUS = "STATUS"


class ListInferenceRecommendationsJobsSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class ListLabelingJobsForWorkteamSortByOptions(StrEnum):
    CreationTime = "CreationTime"


class ListOptimizationJobsSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class ListWorkforcesSortByOptions(StrEnum):
    Name = "Name"
    CreateDate = "CreateDate"


class ListWorkteamsSortByOptions(StrEnum):
    Name = "Name"
    CreateDate = "CreateDate"


class ManagedInstanceScalingStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MetricSetSource(StrEnum):
    Train = "Train"
    Validation = "Validation"
    Test = "Test"


class MlTools(StrEnum):
    DataWrangler = "DataWrangler"
    FeatureStore = "FeatureStore"
    EmrClusters = "EmrClusters"
    AutoMl = "AutoMl"
    Experiments = "Experiments"
    Training = "Training"
    ModelEvaluation = "ModelEvaluation"
    Pipelines = "Pipelines"
    Models = "Models"
    JumpStart = "JumpStart"
    InferenceRecommender = "InferenceRecommender"
    Endpoints = "Endpoints"
    Projects = "Projects"
    InferenceOptimization = "InferenceOptimization"
    PerformanceEvaluation = "PerformanceEvaluation"
    LakeraGuard = "LakeraGuard"
    Comet = "Comet"
    DeepchecksLLMEvaluation = "DeepchecksLLMEvaluation"
    Fiddler = "Fiddler"
    HyperPodClusters = "HyperPodClusters"


class ModelApprovalStatus(StrEnum):
    Approved = "Approved"
    Rejected = "Rejected"
    PendingManualApproval = "PendingManualApproval"


class ModelCacheSetting(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ModelCardExportJobSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class ModelCardExportJobSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class ModelCardExportJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"


class ModelCardProcessingStatus(StrEnum):
    DeleteInProgress = "DeleteInProgress"
    DeletePending = "DeletePending"
    ContentDeleted = "ContentDeleted"
    ExportJobsDeleted = "ExportJobsDeleted"
    DeleteCompleted = "DeleteCompleted"
    DeleteFailed = "DeleteFailed"


class ModelCardSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class ModelCardSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class ModelCardStatus(StrEnum):
    Draft = "Draft"
    PendingReview = "PendingReview"
    Approved = "Approved"
    Archived = "Archived"


class ModelCardVersionSortBy(StrEnum):
    Version = "Version"


class ModelCompressionType(StrEnum):
    None_ = "None"
    Gzip = "Gzip"


class ModelInfrastructureType(StrEnum):
    RealTimeInference = "RealTimeInference"


class ModelMetadataFilterType(StrEnum):
    Domain = "Domain"
    Framework = "Framework"
    Task = "Task"
    FrameworkVersion = "FrameworkVersion"


class ModelPackageGroupSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class ModelPackageGroupStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Deleting = "Deleting"
    DeleteFailed = "DeleteFailed"


class ModelPackageSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class ModelPackageStatus(StrEnum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Deleting = "Deleting"


class ModelPackageType(StrEnum):
    Versioned = "Versioned"
    Unversioned = "Unversioned"
    Both = "Both"


class ModelSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class ModelVariantAction(StrEnum):
    Retain = "Retain"
    Remove = "Remove"
    Promote = "Promote"


class ModelVariantStatus(StrEnum):
    Creating = "Creating"
    Updating = "Updating"
    InService = "InService"
    Deleting = "Deleting"
    Deleted = "Deleted"


class MonitoringAlertHistorySortKey(StrEnum):
    CreationTime = "CreationTime"
    Status = "Status"


class MonitoringAlertStatus(StrEnum):
    InAlert = "InAlert"
    OK = "OK"


class MonitoringExecutionSortKey(StrEnum):
    CreationTime = "CreationTime"
    ScheduledTime = "ScheduledTime"
    Status = "Status"


class MonitoringJobDefinitionSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class MonitoringProblemType(StrEnum):
    BinaryClassification = "BinaryClassification"
    MulticlassClassification = "MulticlassClassification"
    Regression = "Regression"


class MonitoringScheduleSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class MonitoringType(StrEnum):
    DataQuality = "DataQuality"
    ModelQuality = "ModelQuality"
    ModelBias = "ModelBias"
    ModelExplainability = "ModelExplainability"


class NodeUnavailabilityType(StrEnum):
    INSTANCE_COUNT = "INSTANCE_COUNT"
    CAPACITY_PERCENTAGE = "CAPACITY_PERCENTAGE"


class NotebookInstanceAcceleratorType(StrEnum):
    ml_eia1_medium = "ml.eia1.medium"
    ml_eia1_large = "ml.eia1.large"
    ml_eia1_xlarge = "ml.eia1.xlarge"
    ml_eia2_medium = "ml.eia2.medium"
    ml_eia2_large = "ml.eia2.large"
    ml_eia2_xlarge = "ml.eia2.xlarge"


class NotebookInstanceLifecycleConfigSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"


class NotebookInstanceLifecycleConfigSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class NotebookInstanceSortKey(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class NotebookInstanceSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class NotebookInstanceStatus(StrEnum):
    Pending = "Pending"
    InService = "InService"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Failed = "Failed"
    Deleting = "Deleting"
    Updating = "Updating"


class NotebookOutputOption(StrEnum):
    Allowed = "Allowed"
    Disabled = "Disabled"


class ObjectiveStatus(StrEnum):
    Succeeded = "Succeeded"
    Pending = "Pending"
    Failed = "Failed"


class OfflineStoreStatusValue(StrEnum):
    Active = "Active"
    Blocked = "Blocked"
    Disabled = "Disabled"


class Operator(StrEnum):
    Equals = "Equals"
    NotEquals = "NotEquals"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"
    LessThan = "LessThan"
    LessThanOrEqualTo = "LessThanOrEqualTo"
    Contains = "Contains"
    Exists = "Exists"
    NotExists = "NotExists"
    In = "In"


class OptimizationJobDeploymentInstanceType(StrEnum):
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_p4de_24xlarge = "ml.p4de.24xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"
    ml_g6e_xlarge = "ml.g6e.xlarge"
    ml_g6e_2xlarge = "ml.g6e.2xlarge"
    ml_g6e_4xlarge = "ml.g6e.4xlarge"
    ml_g6e_8xlarge = "ml.g6e.8xlarge"
    ml_g6e_12xlarge = "ml.g6e.12xlarge"
    ml_g6e_16xlarge = "ml.g6e.16xlarge"
    ml_g6e_24xlarge = "ml.g6e.24xlarge"
    ml_g6e_48xlarge = "ml.g6e.48xlarge"
    ml_inf2_xlarge = "ml.inf2.xlarge"
    ml_inf2_8xlarge = "ml.inf2.8xlarge"
    ml_inf2_24xlarge = "ml.inf2.24xlarge"
    ml_inf2_48xlarge = "ml.inf2.48xlarge"
    ml_trn1_2xlarge = "ml.trn1.2xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn1n_32xlarge = "ml.trn1n.32xlarge"


class OptimizationJobStatus(StrEnum):
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class OrderKey(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class OutputCompressionType(StrEnum):
    GZIP = "GZIP"
    NONE = "NONE"


class ParameterType(StrEnum):
    Integer = "Integer"
    Continuous = "Continuous"
    Categorical = "Categorical"
    FreeText = "FreeText"


class PartnerAppAuthType(StrEnum):
    IAM = "IAM"


class PartnerAppStatus(StrEnum):
    Creating = "Creating"
    Updating = "Updating"
    Deleting = "Deleting"
    Available = "Available"
    Failed = "Failed"
    UpdateFailed = "UpdateFailed"
    Deleted = "Deleted"


class PartnerAppType(StrEnum):
    lakera_guard = "lakera-guard"
    comet = "comet"
    deepchecks_llm_evaluation = "deepchecks-llm-evaluation"
    fiddler = "fiddler"


class PipelineExecutionStatus(StrEnum):
    Executing = "Executing"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Failed = "Failed"
    Succeeded = "Succeeded"


class PipelineStatus(StrEnum):
    Active = "Active"
    Deleting = "Deleting"


class PreemptTeamTasks(StrEnum):
    Never = "Never"
    LowerPriority = "LowerPriority"


class ProblemType(StrEnum):
    BinaryClassification = "BinaryClassification"
    MulticlassClassification = "MulticlassClassification"
    Regression = "Regression"


class ProcessingInstanceType(StrEnum):
    ml_t3_medium = "ml.t3.medium"
    ml_t3_large = "ml.t3.large"
    ml_t3_xlarge = "ml.t3.xlarge"
    ml_t3_2xlarge = "ml.t3.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_r5_large = "ml.r5.large"
    ml_r5_xlarge = "ml.r5.xlarge"
    ml_r5_2xlarge = "ml.r5.2xlarge"
    ml_r5_4xlarge = "ml.r5.4xlarge"
    ml_r5_8xlarge = "ml.r5.8xlarge"
    ml_r5_12xlarge = "ml.r5.12xlarge"
    ml_r5_16xlarge = "ml.r5.16xlarge"
    ml_r5_24xlarge = "ml.r5.24xlarge"
    ml_g4dn_xlarge = "ml.g4dn.xlarge"
    ml_g4dn_2xlarge = "ml.g4dn.2xlarge"
    ml_g4dn_4xlarge = "ml.g4dn.4xlarge"
    ml_g4dn_8xlarge = "ml.g4dn.8xlarge"
    ml_g4dn_12xlarge = "ml.g4dn.12xlarge"
    ml_g4dn_16xlarge = "ml.g4dn.16xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_r5d_large = "ml.r5d.large"
    ml_r5d_xlarge = "ml.r5d.xlarge"
    ml_r5d_2xlarge = "ml.r5d.2xlarge"
    ml_r5d_4xlarge = "ml.r5d.4xlarge"
    ml_r5d_8xlarge = "ml.r5d.8xlarge"
    ml_r5d_12xlarge = "ml.r5d.12xlarge"
    ml_r5d_16xlarge = "ml.r5d.16xlarge"
    ml_r5d_24xlarge = "ml.r5d.24xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"
    ml_g6e_xlarge = "ml.g6e.xlarge"
    ml_g6e_2xlarge = "ml.g6e.2xlarge"
    ml_g6e_4xlarge = "ml.g6e.4xlarge"
    ml_g6e_8xlarge = "ml.g6e.8xlarge"
    ml_g6e_12xlarge = "ml.g6e.12xlarge"
    ml_g6e_16xlarge = "ml.g6e.16xlarge"
    ml_g6e_24xlarge = "ml.g6e.24xlarge"
    ml_g6e_48xlarge = "ml.g6e.48xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"


class ProcessingJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class ProcessingS3CompressionType(StrEnum):
    None_ = "None"
    Gzip = "Gzip"


class ProcessingS3DataDistributionType(StrEnum):
    FullyReplicated = "FullyReplicated"
    ShardedByS3Key = "ShardedByS3Key"


class ProcessingS3DataType(StrEnum):
    ManifestFile = "ManifestFile"
    S3Prefix = "S3Prefix"


class ProcessingS3InputMode(StrEnum):
    Pipe = "Pipe"
    File = "File"


class ProcessingS3UploadMode(StrEnum):
    Continuous = "Continuous"
    EndOfJob = "EndOfJob"


class Processor(StrEnum):
    CPU = "CPU"
    GPU = "GPU"


class ProductionVariantAcceleratorType(StrEnum):
    ml_eia1_medium = "ml.eia1.medium"
    ml_eia1_large = "ml.eia1.large"
    ml_eia1_xlarge = "ml.eia1.xlarge"
    ml_eia2_medium = "ml.eia2.medium"
    ml_eia2_large = "ml.eia2.large"
    ml_eia2_xlarge = "ml.eia2.xlarge"


class ProductionVariantInferenceAmiVersion(StrEnum):
    al2_ami_sagemaker_inference_gpu_2 = "al2-ami-sagemaker-inference-gpu-2"
    al2_ami_sagemaker_inference_gpu_2_1 = "al2-ami-sagemaker-inference-gpu-2-1"
    al2_ami_sagemaker_inference_gpu_3_1 = "al2-ami-sagemaker-inference-gpu-3-1"
    al2_ami_sagemaker_inference_neuron_2 = "al2-ami-sagemaker-inference-neuron-2"


class ProductionVariantInstanceType(StrEnum):
    ml_t2_medium = "ml.t2.medium"
    ml_t2_large = "ml.t2.large"
    ml_t2_xlarge = "ml.t2.xlarge"
    ml_t2_2xlarge = "ml.t2.2xlarge"
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_m5d_large = "ml.m5d.large"
    ml_m5d_xlarge = "ml.m5d.xlarge"
    ml_m5d_2xlarge = "ml.m5d.2xlarge"
    ml_m5d_4xlarge = "ml.m5d.4xlarge"
    ml_m5d_12xlarge = "ml.m5d.12xlarge"
    ml_m5d_24xlarge = "ml.m5d.24xlarge"
    ml_c4_large = "ml.c4.large"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_large = "ml.c5.large"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_c5d_large = "ml.c5d.large"
    ml_c5d_xlarge = "ml.c5d.xlarge"
    ml_c5d_2xlarge = "ml.c5d.2xlarge"
    ml_c5d_4xlarge = "ml.c5d.4xlarge"
    ml_c5d_9xlarge = "ml.c5d.9xlarge"
    ml_c5d_18xlarge = "ml.c5d.18xlarge"
    ml_g4dn_xlarge = "ml.g4dn.xlarge"
    ml_g4dn_2xlarge = "ml.g4dn.2xlarge"
    ml_g4dn_4xlarge = "ml.g4dn.4xlarge"
    ml_g4dn_8xlarge = "ml.g4dn.8xlarge"
    ml_g4dn_12xlarge = "ml.g4dn.12xlarge"
    ml_g4dn_16xlarge = "ml.g4dn.16xlarge"
    ml_r5_large = "ml.r5.large"
    ml_r5_xlarge = "ml.r5.xlarge"
    ml_r5_2xlarge = "ml.r5.2xlarge"
    ml_r5_4xlarge = "ml.r5.4xlarge"
    ml_r5_12xlarge = "ml.r5.12xlarge"
    ml_r5_24xlarge = "ml.r5.24xlarge"
    ml_r5d_large = "ml.r5d.large"
    ml_r5d_xlarge = "ml.r5d.xlarge"
    ml_r5d_2xlarge = "ml.r5d.2xlarge"
    ml_r5d_4xlarge = "ml.r5d.4xlarge"
    ml_r5d_12xlarge = "ml.r5d.12xlarge"
    ml_r5d_24xlarge = "ml.r5d.24xlarge"
    ml_inf1_xlarge = "ml.inf1.xlarge"
    ml_inf1_2xlarge = "ml.inf1.2xlarge"
    ml_inf1_6xlarge = "ml.inf1.6xlarge"
    ml_inf1_24xlarge = "ml.inf1.24xlarge"
    ml_dl1_24xlarge = "ml.dl1.24xlarge"
    ml_c6i_large = "ml.c6i.large"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_r6i_large = "ml.r6i.large"
    ml_r6i_xlarge = "ml.r6i.xlarge"
    ml_r6i_2xlarge = "ml.r6i.2xlarge"
    ml_r6i_4xlarge = "ml.r6i.4xlarge"
    ml_r6i_8xlarge = "ml.r6i.8xlarge"
    ml_r6i_12xlarge = "ml.r6i.12xlarge"
    ml_r6i_16xlarge = "ml.r6i.16xlarge"
    ml_r6i_24xlarge = "ml.r6i.24xlarge"
    ml_r6i_32xlarge = "ml.r6i.32xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"
    ml_r8g_medium = "ml.r8g.medium"
    ml_r8g_large = "ml.r8g.large"
    ml_r8g_xlarge = "ml.r8g.xlarge"
    ml_r8g_2xlarge = "ml.r8g.2xlarge"
    ml_r8g_4xlarge = "ml.r8g.4xlarge"
    ml_r8g_8xlarge = "ml.r8g.8xlarge"
    ml_r8g_12xlarge = "ml.r8g.12xlarge"
    ml_r8g_16xlarge = "ml.r8g.16xlarge"
    ml_r8g_24xlarge = "ml.r8g.24xlarge"
    ml_r8g_48xlarge = "ml.r8g.48xlarge"
    ml_g6e_xlarge = "ml.g6e.xlarge"
    ml_g6e_2xlarge = "ml.g6e.2xlarge"
    ml_g6e_4xlarge = "ml.g6e.4xlarge"
    ml_g6e_8xlarge = "ml.g6e.8xlarge"
    ml_g6e_12xlarge = "ml.g6e.12xlarge"
    ml_g6e_16xlarge = "ml.g6e.16xlarge"
    ml_g6e_24xlarge = "ml.g6e.24xlarge"
    ml_g6e_48xlarge = "ml.g6e.48xlarge"
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_c7g_large = "ml.c7g.large"
    ml_c7g_xlarge = "ml.c7g.xlarge"
    ml_c7g_2xlarge = "ml.c7g.2xlarge"
    ml_c7g_4xlarge = "ml.c7g.4xlarge"
    ml_c7g_8xlarge = "ml.c7g.8xlarge"
    ml_c7g_12xlarge = "ml.c7g.12xlarge"
    ml_c7g_16xlarge = "ml.c7g.16xlarge"
    ml_m6g_large = "ml.m6g.large"
    ml_m6g_xlarge = "ml.m6g.xlarge"
    ml_m6g_2xlarge = "ml.m6g.2xlarge"
    ml_m6g_4xlarge = "ml.m6g.4xlarge"
    ml_m6g_8xlarge = "ml.m6g.8xlarge"
    ml_m6g_12xlarge = "ml.m6g.12xlarge"
    ml_m6g_16xlarge = "ml.m6g.16xlarge"
    ml_m6gd_large = "ml.m6gd.large"
    ml_m6gd_xlarge = "ml.m6gd.xlarge"
    ml_m6gd_2xlarge = "ml.m6gd.2xlarge"
    ml_m6gd_4xlarge = "ml.m6gd.4xlarge"
    ml_m6gd_8xlarge = "ml.m6gd.8xlarge"
    ml_m6gd_12xlarge = "ml.m6gd.12xlarge"
    ml_m6gd_16xlarge = "ml.m6gd.16xlarge"
    ml_c6g_large = "ml.c6g.large"
    ml_c6g_xlarge = "ml.c6g.xlarge"
    ml_c6g_2xlarge = "ml.c6g.2xlarge"
    ml_c6g_4xlarge = "ml.c6g.4xlarge"
    ml_c6g_8xlarge = "ml.c6g.8xlarge"
    ml_c6g_12xlarge = "ml.c6g.12xlarge"
    ml_c6g_16xlarge = "ml.c6g.16xlarge"
    ml_c6gd_large = "ml.c6gd.large"
    ml_c6gd_xlarge = "ml.c6gd.xlarge"
    ml_c6gd_2xlarge = "ml.c6gd.2xlarge"
    ml_c6gd_4xlarge = "ml.c6gd.4xlarge"
    ml_c6gd_8xlarge = "ml.c6gd.8xlarge"
    ml_c6gd_12xlarge = "ml.c6gd.12xlarge"
    ml_c6gd_16xlarge = "ml.c6gd.16xlarge"
    ml_c6gn_large = "ml.c6gn.large"
    ml_c6gn_xlarge = "ml.c6gn.xlarge"
    ml_c6gn_2xlarge = "ml.c6gn.2xlarge"
    ml_c6gn_4xlarge = "ml.c6gn.4xlarge"
    ml_c6gn_8xlarge = "ml.c6gn.8xlarge"
    ml_c6gn_12xlarge = "ml.c6gn.12xlarge"
    ml_c6gn_16xlarge = "ml.c6gn.16xlarge"
    ml_r6g_large = "ml.r6g.large"
    ml_r6g_xlarge = "ml.r6g.xlarge"
    ml_r6g_2xlarge = "ml.r6g.2xlarge"
    ml_r6g_4xlarge = "ml.r6g.4xlarge"
    ml_r6g_8xlarge = "ml.r6g.8xlarge"
    ml_r6g_12xlarge = "ml.r6g.12xlarge"
    ml_r6g_16xlarge = "ml.r6g.16xlarge"
    ml_r6gd_large = "ml.r6gd.large"
    ml_r6gd_xlarge = "ml.r6gd.xlarge"
    ml_r6gd_2xlarge = "ml.r6gd.2xlarge"
    ml_r6gd_4xlarge = "ml.r6gd.4xlarge"
    ml_r6gd_8xlarge = "ml.r6gd.8xlarge"
    ml_r6gd_12xlarge = "ml.r6gd.12xlarge"
    ml_r6gd_16xlarge = "ml.r6gd.16xlarge"
    ml_p4de_24xlarge = "ml.p4de.24xlarge"
    ml_trn1_2xlarge = "ml.trn1.2xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn1n_32xlarge = "ml.trn1n.32xlarge"
    ml_trn2_48xlarge = "ml.trn2.48xlarge"
    ml_inf2_xlarge = "ml.inf2.xlarge"
    ml_inf2_8xlarge = "ml.inf2.8xlarge"
    ml_inf2_24xlarge = "ml.inf2.24xlarge"
    ml_inf2_48xlarge = "ml.inf2.48xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_p5e_48xlarge = "ml.p5e.48xlarge"
    ml_p5en_48xlarge = "ml.p5en.48xlarge"
    ml_m7i_large = "ml.m7i.large"
    ml_m7i_xlarge = "ml.m7i.xlarge"
    ml_m7i_2xlarge = "ml.m7i.2xlarge"
    ml_m7i_4xlarge = "ml.m7i.4xlarge"
    ml_m7i_8xlarge = "ml.m7i.8xlarge"
    ml_m7i_12xlarge = "ml.m7i.12xlarge"
    ml_m7i_16xlarge = "ml.m7i.16xlarge"
    ml_m7i_24xlarge = "ml.m7i.24xlarge"
    ml_m7i_48xlarge = "ml.m7i.48xlarge"
    ml_c7i_large = "ml.c7i.large"
    ml_c7i_xlarge = "ml.c7i.xlarge"
    ml_c7i_2xlarge = "ml.c7i.2xlarge"
    ml_c7i_4xlarge = "ml.c7i.4xlarge"
    ml_c7i_8xlarge = "ml.c7i.8xlarge"
    ml_c7i_12xlarge = "ml.c7i.12xlarge"
    ml_c7i_16xlarge = "ml.c7i.16xlarge"
    ml_c7i_24xlarge = "ml.c7i.24xlarge"
    ml_c7i_48xlarge = "ml.c7i.48xlarge"
    ml_r7i_large = "ml.r7i.large"
    ml_r7i_xlarge = "ml.r7i.xlarge"
    ml_r7i_2xlarge = "ml.r7i.2xlarge"
    ml_r7i_4xlarge = "ml.r7i.4xlarge"
    ml_r7i_8xlarge = "ml.r7i.8xlarge"
    ml_r7i_12xlarge = "ml.r7i.12xlarge"
    ml_r7i_16xlarge = "ml.r7i.16xlarge"
    ml_r7i_24xlarge = "ml.r7i.24xlarge"
    ml_r7i_48xlarge = "ml.r7i.48xlarge"


class ProfilingStatus(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ProjectSortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class ProjectSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class ProjectStatus(StrEnum):
    Pending = "Pending"
    CreateInProgress = "CreateInProgress"
    CreateCompleted = "CreateCompleted"
    CreateFailed = "CreateFailed"
    DeleteInProgress = "DeleteInProgress"
    DeleteFailed = "DeleteFailed"
    DeleteCompleted = "DeleteCompleted"
    UpdateInProgress = "UpdateInProgress"
    UpdateCompleted = "UpdateCompleted"
    UpdateFailed = "UpdateFailed"


class RStudioServerProAccessStatus(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RStudioServerProUserGroup(StrEnum):
    R_STUDIO_ADMIN = "R_STUDIO_ADMIN"
    R_STUDIO_USER = "R_STUDIO_USER"


class RecommendationJobStatus(StrEnum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class RecommendationJobSupportedEndpointType(StrEnum):
    RealTime = "RealTime"
    Serverless = "Serverless"


class RecommendationJobType(StrEnum):
    Default = "Default"
    Advanced = "Advanced"


class RecommendationStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class RecommendationStepType(StrEnum):
    BENCHMARK = "BENCHMARK"


class RecordWrapper(StrEnum):
    None_ = "None"
    RecordIO = "RecordIO"


class RedshiftResultCompressionType(StrEnum):
    None_ = "None"
    GZIP = "GZIP"
    BZIP2 = "BZIP2"
    ZSTD = "ZSTD"
    SNAPPY = "SNAPPY"


class RedshiftResultFormat(StrEnum):
    PARQUET = "PARQUET"
    CSV = "CSV"


class Relation(StrEnum):
    EqualTo = "EqualTo"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"


class RepositoryAccessMode(StrEnum):
    Platform = "Platform"
    Vpc = "Vpc"


class ReservedCapacityInstanceType(StrEnum):
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_p5e_48xlarge = "ml.p5e.48xlarge"
    ml_p5en_48xlarge = "ml.p5en.48xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn2_48xlarge = "ml.trn2.48xlarge"


class ReservedCapacityStatus(StrEnum):
    Pending = "Pending"
    Active = "Active"
    Scheduled = "Scheduled"
    Expired = "Expired"
    Failed = "Failed"


class ResourceCatalogSortBy(StrEnum):
    CreationTime = "CreationTime"


class ResourceCatalogSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class ResourceSharingStrategy(StrEnum):
    Lend = "Lend"
    DontLend = "DontLend"
    LendAndBorrow = "LendAndBorrow"


class ResourceType(StrEnum):
    TrainingJob = "TrainingJob"
    Experiment = "Experiment"
    ExperimentTrial = "ExperimentTrial"
    ExperimentTrialComponent = "ExperimentTrialComponent"
    Endpoint = "Endpoint"
    Model = "Model"
    ModelPackage = "ModelPackage"
    ModelPackageGroup = "ModelPackageGroup"
    Pipeline = "Pipeline"
    PipelineExecution = "PipelineExecution"
    FeatureGroup = "FeatureGroup"
    FeatureMetadata = "FeatureMetadata"
    Image = "Image"
    ImageVersion = "ImageVersion"
    Project = "Project"
    HyperParameterTuningJob = "HyperParameterTuningJob"
    ModelCard = "ModelCard"


class RetentionType(StrEnum):
    Retain = "Retain"
    Delete = "Delete"


class RootAccess(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class RoutingStrategy(StrEnum):
    LEAST_OUTSTANDING_REQUESTS = "LEAST_OUTSTANDING_REQUESTS"
    RANDOM = "RANDOM"


class RuleEvaluationStatus(StrEnum):
    InProgress = "InProgress"
    NoIssuesFound = "NoIssuesFound"
    IssuesFound = "IssuesFound"
    Error = "Error"
    Stopping = "Stopping"
    Stopped = "Stopped"


class S3DataDistribution(StrEnum):
    FullyReplicated = "FullyReplicated"
    ShardedByS3Key = "ShardedByS3Key"


class S3DataType(StrEnum):
    ManifestFile = "ManifestFile"
    S3Prefix = "S3Prefix"
    AugmentedManifestFile = "AugmentedManifestFile"


class S3ModelDataType(StrEnum):
    S3Prefix = "S3Prefix"
    S3Object = "S3Object"


class SageMakerImageName(StrEnum):
    sagemaker_distribution = "sagemaker_distribution"


class SageMakerResourceName(StrEnum):
    training_job = "training-job"
    hyperpod_cluster = "hyperpod-cluster"


class SagemakerServicecatalogStatus(StrEnum):
    Enabled = "Enabled"
    Disabled = "Disabled"


class ScheduleStatus(StrEnum):
    Pending = "Pending"
    Failed = "Failed"
    Scheduled = "Scheduled"
    Stopped = "Stopped"


class SchedulerResourceStatus(StrEnum):
    Creating = "Creating"
    CreateFailed = "CreateFailed"
    CreateRollbackFailed = "CreateRollbackFailed"
    Created = "Created"
    Updating = "Updating"
    UpdateFailed = "UpdateFailed"
    UpdateRollbackFailed = "UpdateRollbackFailed"
    Updated = "Updated"
    Deleting = "Deleting"
    DeleteFailed = "DeleteFailed"
    DeleteRollbackFailed = "DeleteRollbackFailed"
    Deleted = "Deleted"


class SearchSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class SecondaryStatus(StrEnum):
    Starting = "Starting"
    LaunchingMLInstances = "LaunchingMLInstances"
    PreparingTrainingStack = "PreparingTrainingStack"
    Downloading = "Downloading"
    DownloadingTrainingImage = "DownloadingTrainingImage"
    Training = "Training"
    Uploading = "Uploading"
    Stopping = "Stopping"
    Stopped = "Stopped"
    MaxRuntimeExceeded = "MaxRuntimeExceeded"
    Completed = "Completed"
    Failed = "Failed"
    Interrupted = "Interrupted"
    MaxWaitTimeExceeded = "MaxWaitTimeExceeded"
    Updating = "Updating"
    Restarting = "Restarting"
    Pending = "Pending"


class SharingType(StrEnum):
    Private = "Private"
    Shared = "Shared"


class SkipModelValidation(StrEnum):
    All = "All"
    None_ = "None"


class SortActionsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SortArtifactsBy(StrEnum):
    CreationTime = "CreationTime"


class SortAssociationsBy(StrEnum):
    SourceArn = "SourceArn"
    DestinationArn = "DestinationArn"
    SourceType = "SourceType"
    DestinationType = "DestinationType"
    CreationTime = "CreationTime"


class SortBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class SortClusterSchedulerConfigBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class SortContextsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SortExperimentsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SortInferenceExperimentsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class SortLineageGroupsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class SortPipelineExecutionsBy(StrEnum):
    CreationTime = "CreationTime"
    PipelineExecutionArn = "PipelineExecutionArn"


class SortPipelinesBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SortQuotaBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"
    ClusterArn = "ClusterArn"


class SortTrackingServerBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"


class SortTrialComponentsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SortTrialsBy(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"


class SpaceSortKey(StrEnum):
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"


class SpaceStatus(StrEnum):
    Deleting = "Deleting"
    Failed = "Failed"
    InService = "InService"
    Pending = "Pending"
    Updating = "Updating"
    Update_Failed = "Update_Failed"
    Delete_Failed = "Delete_Failed"


class SplitType(StrEnum):
    None_ = "None"
    Line = "Line"
    RecordIO = "RecordIO"
    TFRecord = "TFRecord"


class StageStatus(StrEnum):
    CREATING = "CREATING"
    READYTODEPLOY = "READYTODEPLOY"
    STARTING = "STARTING"
    INPROGRESS = "INPROGRESS"
    DEPLOYED = "DEPLOYED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class Statistic(StrEnum):
    Average = "Average"
    Minimum = "Minimum"
    Maximum = "Maximum"
    SampleCount = "SampleCount"
    Sum = "Sum"


class StepStatus(StrEnum):
    Starting = "Starting"
    Executing = "Executing"
    Stopping = "Stopping"
    Stopped = "Stopped"
    Failed = "Failed"
    Succeeded = "Succeeded"


class StorageType(StrEnum):
    Standard = "Standard"
    InMemory = "InMemory"


class StudioLifecycleConfigAppType(StrEnum):
    JupyterServer = "JupyterServer"
    KernelGateway = "KernelGateway"
    CodeEditor = "CodeEditor"
    JupyterLab = "JupyterLab"


class StudioLifecycleConfigSortKey(StrEnum):
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"
    Name = "Name"


class StudioWebPortal(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TableFormat(StrEnum):
    Default = "Default"
    Glue = "Glue"
    Iceberg = "Iceberg"


class TagPropagation(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TargetDevice(StrEnum):
    lambda_ = "lambda"
    ml_m4 = "ml_m4"
    ml_m5 = "ml_m5"
    ml_m6g = "ml_m6g"
    ml_c4 = "ml_c4"
    ml_c5 = "ml_c5"
    ml_c6g = "ml_c6g"
    ml_p2 = "ml_p2"
    ml_p3 = "ml_p3"
    ml_g4dn = "ml_g4dn"
    ml_inf1 = "ml_inf1"
    ml_inf2 = "ml_inf2"
    ml_trn1 = "ml_trn1"
    ml_eia2 = "ml_eia2"
    jetson_tx1 = "jetson_tx1"
    jetson_tx2 = "jetson_tx2"
    jetson_nano = "jetson_nano"
    jetson_xavier = "jetson_xavier"
    rasp3b = "rasp3b"
    rasp4b = "rasp4b"
    imx8qm = "imx8qm"
    deeplens = "deeplens"
    rk3399 = "rk3399"
    rk3288 = "rk3288"
    aisage = "aisage"
    sbe_c = "sbe_c"
    qcs605 = "qcs605"
    qcs603 = "qcs603"
    sitara_am57x = "sitara_am57x"
    amba_cv2 = "amba_cv2"
    amba_cv22 = "amba_cv22"
    amba_cv25 = "amba_cv25"
    x86_win32 = "x86_win32"
    x86_win64 = "x86_win64"
    coreml = "coreml"
    jacinto_tda4vm = "jacinto_tda4vm"
    imx8mplus = "imx8mplus"


class TargetPlatformAccelerator(StrEnum):
    INTEL_GRAPHICS = "INTEL_GRAPHICS"
    MALI = "MALI"
    NVIDIA = "NVIDIA"
    NNA = "NNA"


class TargetPlatformArch(StrEnum):
    X86_64 = "X86_64"
    X86 = "X86"
    ARM64 = "ARM64"
    ARM_EABI = "ARM_EABI"
    ARM_EABIHF = "ARM_EABIHF"


class TargetPlatformOs(StrEnum):
    ANDROID = "ANDROID"
    LINUX = "LINUX"


class ThroughputMode(StrEnum):
    OnDemand = "OnDemand"
    Provisioned = "Provisioned"


class TrackingServerMaintenanceStatus(StrEnum):
    MaintenanceInProgress = "MaintenanceInProgress"
    MaintenanceComplete = "MaintenanceComplete"
    MaintenanceFailed = "MaintenanceFailed"


class TrackingServerSize(StrEnum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"


class TrackingServerStatus(StrEnum):
    Creating = "Creating"
    Created = "Created"
    CreateFailed = "CreateFailed"
    Updating = "Updating"
    Updated = "Updated"
    UpdateFailed = "UpdateFailed"
    Deleting = "Deleting"
    DeleteFailed = "DeleteFailed"
    Stopping = "Stopping"
    Stopped = "Stopped"
    StopFailed = "StopFailed"
    Starting = "Starting"
    Started = "Started"
    StartFailed = "StartFailed"
    MaintenanceInProgress = "MaintenanceInProgress"
    MaintenanceComplete = "MaintenanceComplete"
    MaintenanceFailed = "MaintenanceFailed"


class TrafficRoutingConfigType(StrEnum):
    ALL_AT_ONCE = "ALL_AT_ONCE"
    CANARY = "CANARY"
    LINEAR = "LINEAR"


class TrafficType(StrEnum):
    PHASES = "PHASES"
    STAIRS = "STAIRS"


class TrainingInputMode(StrEnum):
    Pipe = "Pipe"
    File = "File"
    FastFile = "FastFile"


class TrainingInstanceType(StrEnum):
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_g4dn_xlarge = "ml.g4dn.xlarge"
    ml_g4dn_2xlarge = "ml.g4dn.2xlarge"
    ml_g4dn_4xlarge = "ml.g4dn.4xlarge"
    ml_g4dn_8xlarge = "ml.g4dn.8xlarge"
    ml_g4dn_12xlarge = "ml.g4dn.12xlarge"
    ml_g4dn_16xlarge = "ml.g4dn.16xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_p3dn_24xlarge = "ml.p3dn.24xlarge"
    ml_p4d_24xlarge = "ml.p4d.24xlarge"
    ml_p4de_24xlarge = "ml.p4de.24xlarge"
    ml_p5_48xlarge = "ml.p5.48xlarge"
    ml_p5e_48xlarge = "ml.p5e.48xlarge"
    ml_p5en_48xlarge = "ml.p5en.48xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_c5n_xlarge = "ml.c5n.xlarge"
    ml_c5n_2xlarge = "ml.c5n.2xlarge"
    ml_c5n_4xlarge = "ml.c5n.4xlarge"
    ml_c5n_9xlarge = "ml.c5n.9xlarge"
    ml_c5n_18xlarge = "ml.c5n.18xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_g6_xlarge = "ml.g6.xlarge"
    ml_g6_2xlarge = "ml.g6.2xlarge"
    ml_g6_4xlarge = "ml.g6.4xlarge"
    ml_g6_8xlarge = "ml.g6.8xlarge"
    ml_g6_16xlarge = "ml.g6.16xlarge"
    ml_g6_12xlarge = "ml.g6.12xlarge"
    ml_g6_24xlarge = "ml.g6.24xlarge"
    ml_g6_48xlarge = "ml.g6.48xlarge"
    ml_g6e_xlarge = "ml.g6e.xlarge"
    ml_g6e_2xlarge = "ml.g6e.2xlarge"
    ml_g6e_4xlarge = "ml.g6e.4xlarge"
    ml_g6e_8xlarge = "ml.g6e.8xlarge"
    ml_g6e_16xlarge = "ml.g6e.16xlarge"
    ml_g6e_12xlarge = "ml.g6e.12xlarge"
    ml_g6e_24xlarge = "ml.g6e.24xlarge"
    ml_g6e_48xlarge = "ml.g6e.48xlarge"
    ml_trn1_2xlarge = "ml.trn1.2xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_trn1n_32xlarge = "ml.trn1n.32xlarge"
    ml_trn2_48xlarge = "ml.trn2.48xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"
    ml_r5d_large = "ml.r5d.large"
    ml_r5d_xlarge = "ml.r5d.xlarge"
    ml_r5d_2xlarge = "ml.r5d.2xlarge"
    ml_r5d_4xlarge = "ml.r5d.4xlarge"
    ml_r5d_8xlarge = "ml.r5d.8xlarge"
    ml_r5d_12xlarge = "ml.r5d.12xlarge"
    ml_r5d_16xlarge = "ml.r5d.16xlarge"
    ml_r5d_24xlarge = "ml.r5d.24xlarge"
    ml_t3_medium = "ml.t3.medium"
    ml_t3_large = "ml.t3.large"
    ml_t3_xlarge = "ml.t3.xlarge"
    ml_t3_2xlarge = "ml.t3.2xlarge"
    ml_r5_large = "ml.r5.large"
    ml_r5_xlarge = "ml.r5.xlarge"
    ml_r5_2xlarge = "ml.r5.2xlarge"
    ml_r5_4xlarge = "ml.r5.4xlarge"
    ml_r5_8xlarge = "ml.r5.8xlarge"
    ml_r5_12xlarge = "ml.r5.12xlarge"
    ml_r5_16xlarge = "ml.r5.16xlarge"
    ml_r5_24xlarge = "ml.r5.24xlarge"


class TrainingJobEarlyStoppingType(StrEnum):
    Off = "Off"
    Auto = "Auto"


class TrainingJobSortByOptions(StrEnum):
    Name = "Name"
    CreationTime = "CreationTime"
    Status = "Status"
    FinalObjectiveMetricValue = "FinalObjectiveMetricValue"


class TrainingJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class TrainingPlanFilterName(StrEnum):
    Status = "Status"


class TrainingPlanSortBy(StrEnum):
    TrainingPlanName = "TrainingPlanName"
    StartTime = "StartTime"
    Status = "Status"


class TrainingPlanSortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class TrainingPlanStatus(StrEnum):
    Pending = "Pending"
    Active = "Active"
    Scheduled = "Scheduled"
    Expired = "Expired"
    Failed = "Failed"


class TrainingRepositoryAccessMode(StrEnum):
    Platform = "Platform"
    Vpc = "Vpc"


class TransformInstanceType(StrEnum):
    ml_m4_xlarge = "ml.m4.xlarge"
    ml_m4_2xlarge = "ml.m4.2xlarge"
    ml_m4_4xlarge = "ml.m4.4xlarge"
    ml_m4_10xlarge = "ml.m4.10xlarge"
    ml_m4_16xlarge = "ml.m4.16xlarge"
    ml_c4_xlarge = "ml.c4.xlarge"
    ml_c4_2xlarge = "ml.c4.2xlarge"
    ml_c4_4xlarge = "ml.c4.4xlarge"
    ml_c4_8xlarge = "ml.c4.8xlarge"
    ml_p2_xlarge = "ml.p2.xlarge"
    ml_p2_8xlarge = "ml.p2.8xlarge"
    ml_p2_16xlarge = "ml.p2.16xlarge"
    ml_p3_2xlarge = "ml.p3.2xlarge"
    ml_p3_8xlarge = "ml.p3.8xlarge"
    ml_p3_16xlarge = "ml.p3.16xlarge"
    ml_c5_xlarge = "ml.c5.xlarge"
    ml_c5_2xlarge = "ml.c5.2xlarge"
    ml_c5_4xlarge = "ml.c5.4xlarge"
    ml_c5_9xlarge = "ml.c5.9xlarge"
    ml_c5_18xlarge = "ml.c5.18xlarge"
    ml_m5_large = "ml.m5.large"
    ml_m5_xlarge = "ml.m5.xlarge"
    ml_m5_2xlarge = "ml.m5.2xlarge"
    ml_m5_4xlarge = "ml.m5.4xlarge"
    ml_m5_12xlarge = "ml.m5.12xlarge"
    ml_m5_24xlarge = "ml.m5.24xlarge"
    ml_m6i_large = "ml.m6i.large"
    ml_m6i_xlarge = "ml.m6i.xlarge"
    ml_m6i_2xlarge = "ml.m6i.2xlarge"
    ml_m6i_4xlarge = "ml.m6i.4xlarge"
    ml_m6i_8xlarge = "ml.m6i.8xlarge"
    ml_m6i_12xlarge = "ml.m6i.12xlarge"
    ml_m6i_16xlarge = "ml.m6i.16xlarge"
    ml_m6i_24xlarge = "ml.m6i.24xlarge"
    ml_m6i_32xlarge = "ml.m6i.32xlarge"
    ml_c6i_large = "ml.c6i.large"
    ml_c6i_xlarge = "ml.c6i.xlarge"
    ml_c6i_2xlarge = "ml.c6i.2xlarge"
    ml_c6i_4xlarge = "ml.c6i.4xlarge"
    ml_c6i_8xlarge = "ml.c6i.8xlarge"
    ml_c6i_12xlarge = "ml.c6i.12xlarge"
    ml_c6i_16xlarge = "ml.c6i.16xlarge"
    ml_c6i_24xlarge = "ml.c6i.24xlarge"
    ml_c6i_32xlarge = "ml.c6i.32xlarge"
    ml_r6i_large = "ml.r6i.large"
    ml_r6i_xlarge = "ml.r6i.xlarge"
    ml_r6i_2xlarge = "ml.r6i.2xlarge"
    ml_r6i_4xlarge = "ml.r6i.4xlarge"
    ml_r6i_8xlarge = "ml.r6i.8xlarge"
    ml_r6i_12xlarge = "ml.r6i.12xlarge"
    ml_r6i_16xlarge = "ml.r6i.16xlarge"
    ml_r6i_24xlarge = "ml.r6i.24xlarge"
    ml_r6i_32xlarge = "ml.r6i.32xlarge"
    ml_m7i_large = "ml.m7i.large"
    ml_m7i_xlarge = "ml.m7i.xlarge"
    ml_m7i_2xlarge = "ml.m7i.2xlarge"
    ml_m7i_4xlarge = "ml.m7i.4xlarge"
    ml_m7i_8xlarge = "ml.m7i.8xlarge"
    ml_m7i_12xlarge = "ml.m7i.12xlarge"
    ml_m7i_16xlarge = "ml.m7i.16xlarge"
    ml_m7i_24xlarge = "ml.m7i.24xlarge"
    ml_m7i_48xlarge = "ml.m7i.48xlarge"
    ml_c7i_large = "ml.c7i.large"
    ml_c7i_xlarge = "ml.c7i.xlarge"
    ml_c7i_2xlarge = "ml.c7i.2xlarge"
    ml_c7i_4xlarge = "ml.c7i.4xlarge"
    ml_c7i_8xlarge = "ml.c7i.8xlarge"
    ml_c7i_12xlarge = "ml.c7i.12xlarge"
    ml_c7i_16xlarge = "ml.c7i.16xlarge"
    ml_c7i_24xlarge = "ml.c7i.24xlarge"
    ml_c7i_48xlarge = "ml.c7i.48xlarge"
    ml_r7i_large = "ml.r7i.large"
    ml_r7i_xlarge = "ml.r7i.xlarge"
    ml_r7i_2xlarge = "ml.r7i.2xlarge"
    ml_r7i_4xlarge = "ml.r7i.4xlarge"
    ml_r7i_8xlarge = "ml.r7i.8xlarge"
    ml_r7i_12xlarge = "ml.r7i.12xlarge"
    ml_r7i_16xlarge = "ml.r7i.16xlarge"
    ml_r7i_24xlarge = "ml.r7i.24xlarge"
    ml_r7i_48xlarge = "ml.r7i.48xlarge"
    ml_g4dn_xlarge = "ml.g4dn.xlarge"
    ml_g4dn_2xlarge = "ml.g4dn.2xlarge"
    ml_g4dn_4xlarge = "ml.g4dn.4xlarge"
    ml_g4dn_8xlarge = "ml.g4dn.8xlarge"
    ml_g4dn_12xlarge = "ml.g4dn.12xlarge"
    ml_g4dn_16xlarge = "ml.g4dn.16xlarge"
    ml_g5_xlarge = "ml.g5.xlarge"
    ml_g5_2xlarge = "ml.g5.2xlarge"
    ml_g5_4xlarge = "ml.g5.4xlarge"
    ml_g5_8xlarge = "ml.g5.8xlarge"
    ml_g5_12xlarge = "ml.g5.12xlarge"
    ml_g5_16xlarge = "ml.g5.16xlarge"
    ml_g5_24xlarge = "ml.g5.24xlarge"
    ml_g5_48xlarge = "ml.g5.48xlarge"
    ml_trn1_2xlarge = "ml.trn1.2xlarge"
    ml_trn1_32xlarge = "ml.trn1.32xlarge"
    ml_inf2_xlarge = "ml.inf2.xlarge"
    ml_inf2_8xlarge = "ml.inf2.8xlarge"
    ml_inf2_24xlarge = "ml.inf2.24xlarge"
    ml_inf2_48xlarge = "ml.inf2.48xlarge"


class TransformJobStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class TrialComponentPrimaryStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
    Stopping = "Stopping"
    Stopped = "Stopped"


class TtlDurationUnit(StrEnum):
    Seconds = "Seconds"
    Minutes = "Minutes"
    Hours = "Hours"
    Days = "Days"
    Weeks = "Weeks"


class UserProfileSortKey(StrEnum):
    CreationTime = "CreationTime"
    LastModifiedTime = "LastModifiedTime"


class UserProfileStatus(StrEnum):
    Deleting = "Deleting"
    Failed = "Failed"
    InService = "InService"
    Pending = "Pending"
    Updating = "Updating"
    Update_Failed = "Update_Failed"
    Delete_Failed = "Delete_Failed"


class VariantPropertyType(StrEnum):
    DesiredInstanceCount = "DesiredInstanceCount"
    DesiredWeight = "DesiredWeight"
    DataCaptureConfig = "DataCaptureConfig"


class VariantStatus(StrEnum):
    Creating = "Creating"
    Updating = "Updating"
    Deleting = "Deleting"
    ActivatingTraffic = "ActivatingTraffic"
    Baking = "Baking"


class VendorGuidance(StrEnum):
    NOT_PROVIDED = "NOT_PROVIDED"
    STABLE = "STABLE"
    TO_BE_ARCHIVED = "TO_BE_ARCHIVED"
    ARCHIVED = "ARCHIVED"


class WarmPoolResourceStatus(StrEnum):
    Available = "Available"
    Terminated = "Terminated"
    Reused = "Reused"
    InUse = "InUse"


class WorkforceStatus(StrEnum):
    Initializing = "Initializing"
    Updating = "Updating"
    Deleting = "Deleting"
    Failed = "Failed"
    Active = "Active"


class ConflictException(ServiceException):
    """There was a conflict when you attempted to modify a SageMaker entity
    such as an ``Experiment`` or ``Artifact``.
    """

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceInUse(ServiceException):
    """Resource being accessed is in use."""

    code: str = "ResourceInUse"
    sender_fault: bool = False
    status_code: int = 400


class ResourceLimitExceeded(ServiceException):
    """You have exceeded an SageMaker resource limit. For example, you might
    have too many training jobs created.
    """

    code: str = "ResourceLimitExceeded"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFound(ServiceException):
    """Resource being access is not found."""

    code: str = "ResourceNotFound"
    sender_fault: bool = False
    status_code: int = 400


class ActionSource(TypedDict, total=False):
    """A structure describing the source of an action."""

    SourceUri: SourceUri
    SourceType: Optional[String256]
    SourceId: Optional[String256]


Timestamp = datetime


class ActionSummary(TypedDict, total=False):
    """Lists the properties of an *action*. An action represents an action or
    activity. Some examples are a workflow step and a model deployment.
    Generally, an action involves at least one input artifact or output
    artifact.
    """

    ActionArn: Optional[ActionArn]
    ActionName: Optional[ExperimentEntityName]
    Source: Optional[ActionSource]
    ActionType: Optional[String64]
    Status: Optional[ActionStatus]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


ActionSummaries = List[ActionSummary]


class AddAssociationRequest(ServiceRequest):
    SourceArn: AssociationEntityArn
    DestinationArn: AssociationEntityArn
    AssociationType: Optional[AssociationEdgeType]


class AddAssociationResponse(TypedDict, total=False):
    SourceArn: Optional[AssociationEntityArn]
    DestinationArn: Optional[AssociationEntityArn]


class Tag(TypedDict, total=False):
    """A tag object that consists of a key and an optional value, used to
    manage metadata for SageMaker Amazon Web Services resources.

    You can add tags to notebook instances, training jobs, hyperparameter
    tuning jobs, batch transform jobs, models, labeling jobs, work teams,
    endpoint configurations, and endpoints. For more information on adding
    tags to SageMaker resources, see
    `AddTags <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html>`__.

    For more information on adding metadata to your Amazon Web Services
    resources with tagging, see `Tagging Amazon Web Services
    resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`__.
    For advice on best practices for managing Amazon Web Services resources
    with tagging, see `Tagging Best Practices: Implement an Effective Amazon
    Web Services Resource Tagging
    Strategy <https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf>`__.
    """

    Key: TagKey
    Value: TagValue


TagList = List[Tag]


class AddTagsInput(ServiceRequest):
    ResourceArn: ResourceArn
    Tags: TagList


class AddTagsOutput(TypedDict, total=False):
    Tags: Optional[TagList]


AdditionalCodeRepositoryNamesOrUrls = List[CodeRepositoryNameOrUrl]
ResponseMIMETypes = List[ResponseMIMEType]
ContentTypes = List[ContentType]
RealtimeInferenceInstanceTypes = List[ProductionVariantInstanceType]
TransformInstanceTypes = List[TransformInstanceType]


class AdditionalS3DataSource(TypedDict, total=False):
    """A data source used for training or inference that is in addition to the
    input dataset or model data.
    """

    S3DataType: AdditionalS3DataSourceDataType
    S3Uri: S3Uri
    CompressionType: Optional[CompressionType]
    ETag: Optional[String]


class ModelInput(TypedDict, total=False):
    """Input object for the model."""

    DataInputConfig: DataInputConfig


EnvironmentMap = Dict[EnvironmentKey, EnvironmentValue]


class InferenceHubAccessConfig(TypedDict, total=False):
    """Configuration information specifying which hub contents have accessible
    deployment options.
    """

    HubContentArn: HubContentArn


class ModelAccessConfig(TypedDict, total=False):
    """The access configuration file to control access to the ML model. You can
    explicitly accept the model end-user license agreement (EULA) within the
    ``ModelAccessConfig``.

    -  If you are a Jumpstart user, see the `End-user license
       agreements <https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula>`__
       section for more details on accepting the EULA.

    -  If you are an AutoML user, see the *Optional Parameters* section of
       *Create an AutoML job to fine-tune text generation models using the
       API* for details on `How to set the EULA acceptance when fine-tuning
       a model using the AutoML
       API <https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params>`__.
    """

    AcceptEula: AcceptEula


class S3ModelDataSource(TypedDict, total=False):
    """Specifies the S3 location of ML model data to deploy."""

    S3Uri: S3ModelUri
    S3DataType: S3ModelDataType
    CompressionType: ModelCompressionType
    ModelAccessConfig: Optional[ModelAccessConfig]
    HubAccessConfig: Optional[InferenceHubAccessConfig]
    ManifestS3Uri: Optional[S3ModelUri]
    ETag: Optional[String]
    ManifestEtag: Optional[String]


class ModelDataSource(TypedDict, total=False):
    """Specifies the location of ML model data to deploy. If specified, you
    must specify one and only one of the available data sources.
    """

    S3DataSource: Optional[S3ModelDataSource]


class ModelPackageContainerDefinition(TypedDict, total=False):
    """Describes the Docker container for the model package."""

    ContainerHostname: Optional[ContainerHostname]
    Image: ContainerImage
    ImageDigest: Optional[ImageDigest]
    ModelDataUrl: Optional[Url]
    ModelDataSource: Optional[ModelDataSource]
    ProductId: Optional[ProductId]
    Environment: Optional[EnvironmentMap]
    ModelInput: Optional[ModelInput]
    Framework: Optional[String]
    FrameworkVersion: Optional[ModelPackageFrameworkVersion]
    NearestModelName: Optional[String]
    AdditionalS3DataSource: Optional[AdditionalS3DataSource]
    ModelDataETag: Optional[String]


ModelPackageContainerDefinitionList = List[ModelPackageContainerDefinition]


class AdditionalInferenceSpecificationDefinition(TypedDict, total=False):
    """A structure of additional Inference Specification. Additional Inference
    Specification specifies details about inference jobs that can be run
    with models based on this model package
    """

    Name: EntityName
    Description: Optional[EntityDescription]
    Containers: ModelPackageContainerDefinitionList
    SupportedTransformInstanceTypes: Optional[TransformInstanceTypes]
    SupportedRealtimeInferenceInstanceTypes: Optional[RealtimeInferenceInstanceTypes]
    SupportedContentTypes: Optional[ContentTypes]
    SupportedResponseMIMETypes: Optional[ResponseMIMETypes]


AdditionalInferenceSpecifications = List[AdditionalInferenceSpecificationDefinition]


class AdditionalModelDataSource(TypedDict, total=False):
    """Data sources that are available to your model in addition to the one
    that you specify for ``ModelDataSource`` when you use the
    ``CreateModel`` action.
    """

    ChannelName: AdditionalModelChannelName
    S3DataSource: S3ModelDataSource


AdditionalModelDataSources = List[AdditionalModelDataSource]
Long = int


class AgentVersion(TypedDict, total=False):
    """Edge Manager agent version."""

    Version: EdgeVersion
    AgentCount: Long


AgentVersions = List[AgentVersion]
AggregationTransformations = Dict[TransformationAttributeName, AggregationTransformationValue]


class Alarm(TypedDict, total=False):
    """An Amazon CloudWatch alarm configured to monitor metrics on an endpoint."""

    AlarmName: Optional[AlarmName]


class AlarmDetails(TypedDict, total=False):
    """The details of the alarm to monitor during the AMI update."""

    AlarmName: AlarmName


AlarmList = List[Alarm]


class TrainingRepositoryAuthConfig(TypedDict, total=False):
    """An object containing authentication information for a private Docker
    registry.
    """

    TrainingRepositoryCredentialsProviderArn: TrainingRepositoryCredentialsProviderArn


class TrainingImageConfig(TypedDict, total=False):
    """The configuration to use an image from a private Docker registry for a
    training job.
    """

    TrainingRepositoryAccessMode: TrainingRepositoryAccessMode
    TrainingRepositoryAuthConfig: Optional[TrainingRepositoryAuthConfig]


TrainingContainerArguments = List[TrainingContainerArgument]
TrainingContainerEntrypoint = List[TrainingContainerEntrypointString]


class MetricDefinition(TypedDict, total=False):
    """Specifies a metric that the training algorithm writes to ``stderr`` or
    ``stdout``. You can view these logs to understand how your training job
    performs and check for any errors encountered during training. SageMaker
    hyperparameter tuning captures all defined metrics. Specify one of the
    defined metrics to use as an objective metric using the
    `TuningObjective <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective>`__
    parameter in the ``HyperParameterTrainingJobDefinition`` API to evaluate
    job performance during hyperparameter tuning.
    """

    Name: MetricName
    Regex: MetricRegex


MetricDefinitionList = List[MetricDefinition]


class AlgorithmSpecification(TypedDict, total=False):
    """Specifies the training algorithm to use in a
    `CreateTrainingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html>`__
    request.

    SageMaker uses its own SageMaker account credentials to pull and access
    built-in algorithms so built-in algorithms are universally accessible
    across all Amazon Web Services accounts. As a result, built-in
    algorithms have standard, unrestricted access. You cannot restrict
    built-in algorithms using IAM roles. Use custom algorithms if you
    require specific access controls.

    For more information about algorithms provided by SageMaker, see
    `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__.
    For information about using your own algorithms, see `Using Your Own
    Algorithms with Amazon
    SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__.
    """

    TrainingImage: Optional[AlgorithmImage]
    AlgorithmName: Optional[ArnOrName]
    TrainingInputMode: TrainingInputMode
    MetricDefinitions: Optional[MetricDefinitionList]
    EnableSageMakerMetricsTimeSeries: Optional[Boolean]
    ContainerEntrypoint: Optional[TrainingContainerEntrypoint]
    ContainerArguments: Optional[TrainingContainerArguments]
    TrainingImageConfig: Optional[TrainingImageConfig]


class AlgorithmStatusItem(TypedDict, total=False):
    """Represents the overall status of an algorithm."""

    Name: EntityName
    Status: DetailedAlgorithmStatus
    FailureReason: Optional[String]


AlgorithmStatusItemList = List[AlgorithmStatusItem]


class AlgorithmStatusDetails(TypedDict, total=False):
    """Specifies the validation and image scan statuses of the algorithm."""

    ValidationStatuses: Optional[AlgorithmStatusItemList]
    ImageScanStatuses: Optional[AlgorithmStatusItemList]


CreationTime = datetime


class AlgorithmSummary(TypedDict, total=False):
    """Provides summary information about an algorithm."""

    AlgorithmName: EntityName
    AlgorithmArn: AlgorithmArn
    AlgorithmDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    AlgorithmStatus: AlgorithmStatus


AlgorithmSummaryList = List[AlgorithmSummary]


class TransformResources(TypedDict, total=False):
    """Describes the resources, including ML instance types and ML instance
    count, to use for transform job.
    """

    InstanceType: TransformInstanceType
    InstanceCount: TransformInstanceCount
    VolumeKmsKeyId: Optional[KmsKeyId]
    TransformAmiVersion: Optional[TransformAmiVersion]


class TransformOutput(TypedDict, total=False):
    """Describes the results of a transform job."""

    S3OutputPath: S3Uri
    Accept: Optional[Accept]
    AssembleWith: Optional[AssemblyType]
    KmsKeyId: Optional[KmsKeyId]


class TransformS3DataSource(TypedDict, total=False):
    """Describes the S3 data source."""

    S3DataType: S3DataType
    S3Uri: S3Uri


class TransformDataSource(TypedDict, total=False):
    """Describes the location of the channel data."""

    S3DataSource: TransformS3DataSource


class TransformInput(TypedDict, total=False):
    """Describes the input source of a transform job and the way the transform
    job consumes it.
    """

    DataSource: TransformDataSource
    ContentType: Optional[ContentType]
    CompressionType: Optional[CompressionType]
    SplitType: Optional[SplitType]


TransformEnvironmentMap = Dict[TransformEnvironmentKey, TransformEnvironmentValue]


class TransformJobDefinition(TypedDict, total=False):
    """Defines the input needed to run a transform job using the inference
    specification specified in the algorithm.
    """

    MaxConcurrentTransforms: Optional[MaxConcurrentTransforms]
    MaxPayloadInMB: Optional[MaxPayloadInMB]
    BatchStrategy: Optional[BatchStrategy]
    Environment: Optional[TransformEnvironmentMap]
    TransformInput: TransformInput
    TransformOutput: TransformOutput
    TransformResources: TransformResources


class StoppingCondition(TypedDict, total=False):
    """Specifies a limit to how long a job can run. When the job reaches the
    time limit, SageMaker ends the job. Use this API to cap costs.

    To stop a training job, SageMaker sends the algorithm the ``SIGTERM``
    signal, which delays job termination for 120 seconds. Algorithms can use
    this 120-second window to save the model artifacts, so the results of
    training are not lost.

    The training algorithms provided by SageMaker automatically save the
    intermediate results of a model training job when possible. This attempt
    to save artifacts is only a best effort case as model might not be in a
    state from which it can be saved. For example, if training has just
    started, the model might not be ready to save. When saved, this
    intermediate data is a valid model artifact. You can use it to create a
    model with ``CreateModel``.

    The Neural Topic Model (NTM) currently does not support saving
    intermediate model artifacts. When training NTMs, make sure that the
    maximum runtime is sufficient for the training job to complete.
    """

    MaxRuntimeInSeconds: Optional[MaxRuntimeInSeconds]
    MaxWaitTimeInSeconds: Optional[MaxWaitTimeInSeconds]
    MaxPendingTimeInSeconds: Optional[MaxPendingTimeInSeconds]


class InstanceGroup(TypedDict, total=False):
    """Defines an instance group for heterogeneous cluster training. When
    requesting a training job using the
    `CreateTrainingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html>`__
    API, you can configure multiple instance groups .
    """

    InstanceType: TrainingInstanceType
    InstanceCount: TrainingInstanceCount
    InstanceGroupName: InstanceGroupName


InstanceGroups = List[InstanceGroup]


class ResourceConfig(TypedDict, total=False):
    """Describes the resources, including machine learning (ML) compute
    instances and ML storage volumes, to use for model training.
    """

    InstanceType: Optional[TrainingInstanceType]
    InstanceCount: Optional[TrainingInstanceCount]
    VolumeSizeInGB: VolumeSizeInGB
    VolumeKmsKeyId: Optional[KmsKeyId]
    KeepAlivePeriodInSeconds: Optional[KeepAlivePeriodInSeconds]
    InstanceGroups: Optional[InstanceGroups]
    TrainingPlanArn: Optional[TrainingPlanArn]


class OutputDataConfig(TypedDict, total=False):
    """Provides information about how to store model training results (model
    artifacts).
    """

    KmsKeyId: Optional[KmsKeyId]
    S3OutputPath: S3Uri
    CompressionType: Optional[OutputCompressionType]


Seed = int


class ShuffleConfig(TypedDict, total=False):
    """A configuration for a shuffle option for input data in a channel. If you
    use ``S3Prefix`` for ``S3DataType``, the results of the S3 key prefix
    matches are shuffled. If you use ``ManifestFile``, the order of the S3
    object references in the ``ManifestFile`` is shuffled. If you use
    ``AugmentedManifestFile``, the order of the JSON lines in the
    ``AugmentedManifestFile`` is shuffled. The shuffling order is determined
    using the ``Seed`` value.

    For Pipe input mode, when ``ShuffleConfig`` is specified shuffling is
    done at the start of every epoch. With large datasets, this ensures that
    the order of the training data is different for each epoch, and it helps
    reduce bias and possible overfitting. In a multi-node training job when
    ``ShuffleConfig`` is combined with ``S3DataDistributionType`` of
    ``ShardedByS3Key``, the data is shuffled across nodes so that the
    content sent to a particular node on the first epoch might be sent to a
    different node on the second epoch.
    """

    Seed: Seed


class FileSystemDataSource(TypedDict, total=False):
    """Specifies a file system data source for a channel."""

    FileSystemId: FileSystemId
    FileSystemAccessMode: FileSystemAccessMode
    FileSystemType: FileSystemType
    DirectoryPath: DirectoryPath


class HubAccessConfig(TypedDict, total=False):
    """The configuration for a private hub model reference that points to a
    public SageMaker JumpStart model.

    For more information about private hubs, see `Private curated hubs for
    foundation model access control in
    JumpStart <https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html>`__.
    """

    HubContentArn: HubContentArn


InstanceGroupNames = List[InstanceGroupName]
AttributeNames = List[AttributeName]


class S3DataSource(TypedDict, total=False):
    """Describes the S3 data source.

    Your input bucket must be in the same Amazon Web Services region as your
    training job.
    """

    S3DataType: S3DataType
    S3Uri: S3Uri
    S3DataDistributionType: Optional[S3DataDistribution]
    AttributeNames: Optional[AttributeNames]
    InstanceGroupNames: Optional[InstanceGroupNames]
    ModelAccessConfig: Optional[ModelAccessConfig]
    HubAccessConfig: Optional[HubAccessConfig]


class DataSource(TypedDict, total=False):
    """Describes the location of the channel data."""

    S3DataSource: Optional[S3DataSource]
    FileSystemDataSource: Optional[FileSystemDataSource]


class Channel(TypedDict, total=False):
    """A channel is a named input source that training algorithms can consume."""

    ChannelName: ChannelName
    DataSource: DataSource
    ContentType: Optional[ContentType]
    CompressionType: Optional[CompressionType]
    RecordWrapperType: Optional[RecordWrapper]
    InputMode: Optional[TrainingInputMode]
    ShuffleConfig: Optional[ShuffleConfig]


InputDataConfig = List[Channel]
HyperParameters = Dict[HyperParameterKey, HyperParameterValue]


class TrainingJobDefinition(TypedDict, total=False):
    """Defines the input needed to run a training job using the algorithm."""

    TrainingInputMode: TrainingInputMode
    HyperParameters: Optional[HyperParameters]
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfig
    StoppingCondition: StoppingCondition


class AlgorithmValidationProfile(TypedDict, total=False):
    """Defines a training job and a batch transform job that SageMaker runs to
    validate your algorithm.

    The data provided in the validation profile is made available to your
    buyers on Amazon Web Services Marketplace.
    """

    ProfileName: EntityName
    TrainingJobDefinition: TrainingJobDefinition
    TransformJobDefinition: Optional[TransformJobDefinition]


AlgorithmValidationProfiles = List[AlgorithmValidationProfile]


class AlgorithmValidationSpecification(TypedDict, total=False):
    """Specifies configurations for one or more training jobs that SageMaker
    runs to test the algorithm.
    """

    ValidationRole: RoleArn
    ValidationProfiles: AlgorithmValidationProfiles


class AmazonQSettings(TypedDict, total=False):
    """A collection of settings that configure the Amazon Q experience within
    the domain.
    """

    Status: Optional[FeatureStatus]
    QProfileArn: Optional[QProfileArn]


class AnnotationConsolidationConfig(TypedDict, total=False):
    """Configures how labels are consolidated across human workers and
    processes output data.
    """

    AnnotationConsolidationLambdaArn: LambdaFunctionArn


class ResourceSpec(TypedDict, total=False):
    """Specifies the ARN's of a SageMaker AI image and SageMaker AI image
    version, and the instance type that the version runs on.

    When both ``SageMakerImageVersionArn`` and ``SageMakerImageArn`` are
    passed, ``SageMakerImageVersionArn`` is used. Any updates to
    ``SageMakerImageArn`` will not take effect if
    ``SageMakerImageVersionArn`` already exists in the ``ResourceSpec``
    because ``SageMakerImageVersionArn`` always takes precedence. To clear
    the value set for ``SageMakerImageVersionArn``, pass ``None`` as the
    value.
    """

    SageMakerImageArn: Optional[ImageArn]
    SageMakerImageVersionArn: Optional[ImageVersionArn]
    SageMakerImageVersionAlias: Optional[ImageVersionAlias]
    InstanceType: Optional[AppInstanceType]
    LifecycleConfigArn: Optional[StudioLifecycleConfigArn]


class AppDetails(TypedDict, total=False):
    """Details about an Amazon SageMaker AI app."""

    DomainId: Optional[DomainId]
    UserProfileName: Optional[UserProfileName]
    SpaceName: Optional[SpaceName]
    AppType: Optional[AppType]
    AppName: Optional[AppName]
    Status: Optional[AppStatus]
    CreationTime: Optional[CreationTime]
    ResourceSpec: Optional[ResourceSpec]


CustomImageContainerEnvironmentVariables = Dict[NonEmptyString256, String256]
CustomImageContainerEntrypoint = List[NonEmptyString256]
CustomImageContainerArguments = List[NonEmptyString64]


class ContainerConfig(TypedDict, total=False):
    """The configuration used to run the application image container."""

    ContainerArguments: Optional[CustomImageContainerArguments]
    ContainerEntrypoint: Optional[CustomImageContainerEntrypoint]
    ContainerEnvironmentVariables: Optional[CustomImageContainerEnvironmentVariables]


class FileSystemConfig(TypedDict, total=False):
    """The Amazon Elastic File System storage configuration for a SageMaker AI
    image.
    """

    MountPath: Optional[MountPath]
    DefaultUid: Optional[DefaultUid]
    DefaultGid: Optional[DefaultGid]


class CodeEditorAppImageConfig(TypedDict, total=False):
    """The configuration for the file system and kernels in a SageMaker image
    running as a Code Editor app. The ``FileSystemConfig`` object is not
    supported.
    """

    FileSystemConfig: Optional[FileSystemConfig]
    ContainerConfig: Optional[ContainerConfig]


class JupyterLabAppImageConfig(TypedDict, total=False):
    """The configuration for the file system and kernels in a SageMaker AI
    image running as a JupyterLab app. The ``FileSystemConfig`` object is
    not supported.
    """

    FileSystemConfig: Optional[FileSystemConfig]
    ContainerConfig: Optional[ContainerConfig]


class KernelSpec(TypedDict, total=False):
    """The specification of a Jupyter kernel."""

    Name: KernelName
    DisplayName: Optional[KernelDisplayName]


KernelSpecs = List[KernelSpec]


class KernelGatewayImageConfig(TypedDict, total=False):
    """The configuration for the file system and kernels in a SageMaker AI
    image running as a KernelGateway app.
    """

    KernelSpecs: KernelSpecs
    FileSystemConfig: Optional[FileSystemConfig]


class AppImageConfigDetails(TypedDict, total=False):
    """The configuration for running a SageMaker AI image as a KernelGateway
    app.
    """

    AppImageConfigArn: Optional[AppImageConfigArn]
    AppImageConfigName: Optional[AppImageConfigName]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfig]
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfig]
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfig]


AppImageConfigList = List[AppImageConfigDetails]


class IdleSettings(TypedDict, total=False):
    """Settings related to idle shutdown of Studio applications."""

    LifecycleManagement: Optional[LifecycleManagement]
    IdleTimeoutInMinutes: Optional[IdleTimeoutInMinutes]
    MinIdleTimeoutInMinutes: Optional[IdleTimeoutInMinutes]
    MaxIdleTimeoutInMinutes: Optional[IdleTimeoutInMinutes]


class AppLifecycleManagement(TypedDict, total=False):
    """Settings that are used to configure and manage the lifecycle of Amazon
    SageMaker Studio applications.
    """

    IdleSettings: Optional[IdleSettings]


AppList = List[AppDetails]
ContainerArguments = List[ContainerArgument]
ContainerEntrypoint = List[ContainerEntrypointString]


class AppSpecification(TypedDict, total=False):
    """Configuration to run a processing job in a specified container image."""

    ImageUri: ImageUri
    ContainerEntrypoint: Optional[ContainerEntrypoint]
    ContainerArguments: Optional[ContainerArguments]


ArtifactProperties = Dict[StringParameterValue, ArtifactPropertyValue]


class ArtifactSourceType(TypedDict, total=False):
    """The ID and ID type of an artifact source."""

    SourceIdType: ArtifactSourceIdType
    Value: String256


ArtifactSourceTypes = List[ArtifactSourceType]


class ArtifactSource(TypedDict, total=False):
    """A structure describing the source of an artifact."""

    SourceUri: SourceUri
    SourceTypes: Optional[ArtifactSourceTypes]


class ArtifactSummary(TypedDict, total=False):
    """Lists a summary of the properties of an artifact. An artifact represents
    a URI addressable object or data. Some examples are a dataset and a
    model.
    """

    ArtifactArn: Optional[ArtifactArn]
    ArtifactName: Optional[ExperimentEntityName]
    Source: Optional[ArtifactSource]
    ArtifactType: Optional[String256]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


ArtifactSummaries = List[ArtifactSummary]


class AssociateTrialComponentRequest(ServiceRequest):
    TrialComponentName: ExperimentEntityName
    TrialName: ExperimentEntityName


class AssociateTrialComponentResponse(TypedDict, total=False):
    TrialComponentArn: Optional[TrialComponentArn]
    TrialArn: Optional[TrialArn]


class IamIdentity(TypedDict, total=False):
    """The IAM Identity details associated with the user. These details are
    associated with model package groups, model packages and project
    entities only.
    """

    Arn: Optional[String]
    PrincipalId: Optional[String]
    SourceIdentity: Optional[String]


class UserContext(TypedDict, total=False):
    """Information about the user who created or modified an experiment, trial,
    trial component, lineage group, project, or model card.
    """

    UserProfileArn: Optional[String]
    UserProfileName: Optional[String]
    DomainId: Optional[String]
    IamIdentity: Optional[IamIdentity]


class AssociationSummary(TypedDict, total=False):
    """Lists a summary of the properties of an association. An association is
    an entity that links other lineage or experiment entities. An example
    would be an association between a training job and a model.
    """

    SourceArn: Optional[AssociationEntityArn]
    DestinationArn: Optional[AssociationEntityArn]
    SourceType: Optional[String256]
    DestinationType: Optional[String256]
    AssociationType: Optional[AssociationEdgeType]
    SourceName: Optional[ExperimentEntityName]
    DestinationName: Optional[ExperimentEntityName]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]


AssociationSummaries = List[AssociationSummary]
AssumableRoleArns = List[RoleArn]


class AsyncInferenceClientConfig(TypedDict, total=False):
    """Configures the behavior of the client used by SageMaker to interact with
    the model container during asynchronous inference.
    """

    MaxConcurrentInvocationsPerInstance: Optional[MaxConcurrentInvocationsPerInstance]


AsyncNotificationTopicTypeList = List[AsyncNotificationTopicTypes]


class AsyncInferenceNotificationConfig(TypedDict, total=False):
    """Specifies the configuration for notifications of inference results for
    asynchronous inference.
    """

    SuccessTopic: Optional[SnsTopicArn]
    ErrorTopic: Optional[SnsTopicArn]
    IncludeInferenceResponseIn: Optional[AsyncNotificationTopicTypeList]


class AsyncInferenceOutputConfig(TypedDict, total=False):
    """Specifies the configuration for asynchronous inference invocation
    outputs.
    """

    KmsKeyId: Optional[KmsKeyId]
    S3OutputPath: Optional[DestinationS3Uri]
    NotificationConfig: Optional[AsyncInferenceNotificationConfig]
    S3FailurePath: Optional[DestinationS3Uri]


class AsyncInferenceConfig(TypedDict, total=False):
    """Specifies configuration for how an endpoint performs asynchronous
    inference.
    """

    ClientConfig: Optional[AsyncInferenceClientConfig]
    OutputConfig: AsyncInferenceOutputConfig


class AthenaDatasetDefinition(TypedDict, total=False):
    """Configuration for Athena Dataset Definition input."""

    Catalog: AthenaCatalog
    Database: AthenaDatabase
    QueryString: AthenaQueryString
    WorkGroup: Optional[AthenaWorkGroup]
    OutputS3Uri: S3Uri
    KmsKeyId: Optional[KmsKeyId]
    OutputFormat: AthenaResultFormat
    OutputCompression: Optional[AthenaResultCompressionType]


AuthenticationRequestExtraParams = Dict[
    AuthenticationRequestExtraParamsKey, AuthenticationRequestExtraParamsValue
]
AutoMLAlgorithms = List[AutoMLAlgorithm]


class AutoMLAlgorithmConfig(TypedDict, total=False):
    """The selection of algorithms trained on your dataset to generate the
    model candidates for an Autopilot job.
    """

    AutoMLAlgorithms: AutoMLAlgorithms


AutoMLAlgorithmsConfig = List[AutoMLAlgorithmConfig]


class AutoMLContainerDefinition(TypedDict, total=False):
    """A list of container definitions that describe the different containers
    that make up an AutoML candidate. For more information, see
    `ContainerDefinition <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html>`__.
    """

    Image: ContainerImage
    ModelDataUrl: Url
    Environment: Optional[EnvironmentMap]


AutoMLContainerDefinitions = List[AutoMLContainerDefinition]
AutoMLInferenceContainerDefinitions = Dict[AutoMLProcessingUnit, AutoMLContainerDefinitions]


class MetricDatum(TypedDict, total=False):
    """Information about the metric for a candidate produced by an AutoML job."""

    MetricName: Optional[AutoMLMetricEnum]
    StandardMetricName: Optional[AutoMLMetricExtendedEnum]
    Value: Optional[Float]
    Set: Optional[MetricSetSource]


MetricDataList = List[MetricDatum]


class CandidateArtifactLocations(TypedDict, total=False):
    """The location of artifacts for an AutoML candidate job."""

    Explainability: ExplainabilityLocation
    ModelInsights: Optional[ModelInsightsLocation]
    BacktestResults: Optional[BacktestResultsLocation]


class CandidateProperties(TypedDict, total=False):
    """The properties of an AutoML candidate job."""

    CandidateArtifactLocations: Optional[CandidateArtifactLocations]
    CandidateMetrics: Optional[MetricDataList]


class AutoMLCandidateStep(TypedDict, total=False):
    """Information about the steps for a candidate and what step it is working
    on.
    """

    CandidateStepType: CandidateStepType
    CandidateStepArn: CandidateStepArn
    CandidateStepName: CandidateStepName


CandidateSteps = List[AutoMLCandidateStep]


class FinalAutoMLJobObjectiveMetric(TypedDict, total=False):
    """The best candidate result from an AutoML training job."""

    Type: Optional[AutoMLJobObjectiveType]
    MetricName: AutoMLMetricEnum
    Value: MetricValue
    StandardMetricName: Optional[AutoMLMetricEnum]


class AutoMLCandidate(TypedDict, total=False):
    """Information about a candidate produced by an AutoML training job,
    including its status, steps, and other properties.
    """

    CandidateName: CandidateName
    FinalAutoMLJobObjectiveMetric: Optional[FinalAutoMLJobObjectiveMetric]
    ObjectiveStatus: ObjectiveStatus
    CandidateSteps: CandidateSteps
    CandidateStatus: CandidateStatus
    InferenceContainers: Optional[AutoMLContainerDefinitions]
    CreationTime: Timestamp
    EndTime: Optional[Timestamp]
    LastModifiedTime: Timestamp
    FailureReason: Optional[AutoMLFailureReason]
    CandidateProperties: Optional[CandidateProperties]
    InferenceContainerDefinitions: Optional[AutoMLInferenceContainerDefinitions]


class AutoMLCandidateGenerationConfig(TypedDict, total=False):
    """Stores the configuration information for how a candidate is generated
    (optional).
    """

    FeatureSpecificationS3Uri: Optional[S3Uri]
    AlgorithmsConfig: Optional[AutoMLAlgorithmsConfig]


AutoMLCandidates = List[AutoMLCandidate]


class AutoMLS3DataSource(TypedDict, total=False):
    """Describes the Amazon S3 data source."""

    S3DataType: AutoMLS3DataType
    S3Uri: S3Uri


class AutoMLDataSource(TypedDict, total=False):
    """The data source for the Autopilot job."""

    S3DataSource: AutoMLS3DataSource


class AutoMLChannel(TypedDict, total=False):
    """A channel is a named input source that training algorithms can consume.
    The validation dataset size is limited to less than 2 GB. The training
    dataset size must be less than 100 GB. For more information, see
    `Channel <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html>`__.

    A validation dataset must contain the same headers as the training
    dataset.
    """

    DataSource: Optional[AutoMLDataSource]
    CompressionType: Optional[CompressionType]
    TargetAttributeName: TargetAttributeName
    ContentType: Optional[ContentType]
    ChannelType: Optional[AutoMLChannelType]
    SampleWeightAttributeName: Optional[SampleWeightAttributeName]


class EmrServerlessComputeConfig(TypedDict, total=False):
    """This data type is intended for use exclusively by SageMaker Canvas and
    cannot be used in other contexts at the moment.

    Specifies the compute configuration for the EMR Serverless job.
    """

    ExecutionRoleARN: RoleArn


class AutoMLComputeConfig(TypedDict, total=False):
    """This data type is intended for use exclusively by SageMaker Canvas and
    cannot be used in other contexts at the moment.

    Specifies the compute configuration for an AutoML job V2.
    """

    EmrServerlessComputeConfig: Optional[EmrServerlessComputeConfig]


class AutoMLDataSplitConfig(TypedDict, total=False):
    """This structure specifies how to split the data into train and validation
    datasets.

    The validation and training datasets must contain the same headers. For
    jobs created by calling ``CreateAutoMLJob``, the validation dataset must
    be less than 2 GB in size.
    """

    ValidationFraction: Optional[ValidationFraction]


AutoMLInputDataConfig = List[AutoMLChannel]


class AutoMLJobArtifacts(TypedDict, total=False):
    """The artifacts that are generated during an AutoML job."""

    CandidateDefinitionNotebookLocation: Optional[CandidateDefinitionNotebookLocation]
    DataExplorationNotebookLocation: Optional[DataExplorationNotebookLocation]


class AutoMLJobChannel(TypedDict, total=False):
    """A channel is a named input source that training algorithms can consume.
    This channel is used for AutoML jobs V2 (jobs created by calling
    `CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html>`__).
    """

    ChannelType: Optional[AutoMLChannelType]
    ContentType: Optional[ContentType]
    CompressionType: Optional[CompressionType]
    DataSource: Optional[AutoMLDataSource]


class AutoMLJobCompletionCriteria(TypedDict, total=False):
    """How long a job is allowed to run, or how many candidates a job is
    allowed to generate.
    """

    MaxCandidates: Optional[MaxCandidates]
    MaxRuntimePerTrainingJobInSeconds: Optional[MaxRuntimePerTrainingJobInSeconds]
    MaxAutoMLJobRuntimeInSeconds: Optional[MaxAutoMLJobRuntimeInSeconds]


Subnets = List[SubnetId]
VpcSecurityGroupIds = List[SecurityGroupId]


class VpcConfig(TypedDict, total=False):
    """Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker
    jobs, hosted models, and compute resources have access to. You can
    control access to and from your resources by configuring a VPC. For more
    information, see `Give SageMaker Access to Resources in your Amazon
    VPC <https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html>`__.
    """

    SecurityGroupIds: VpcSecurityGroupIds
    Subnets: Subnets


class AutoMLSecurityConfig(TypedDict, total=False):
    """Security options."""

    VolumeKmsKeyId: Optional[KmsKeyId]
    EnableInterContainerTrafficEncryption: Optional[Boolean]
    VpcConfig: Optional[VpcConfig]


class AutoMLJobConfig(TypedDict, total=False):
    """A collection of settings used for an AutoML job."""

    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]
    SecurityConfig: Optional[AutoMLSecurityConfig]
    CandidateGenerationConfig: Optional[AutoMLCandidateGenerationConfig]
    DataSplitConfig: Optional[AutoMLDataSplitConfig]
    Mode: Optional[AutoMLMode]


AutoMLJobInputDataConfig = List[AutoMLJobChannel]


class AutoMLJobObjective(TypedDict, total=False):
    """Specifies a metric to minimize or maximize as the objective of an AutoML
    job.
    """

    MetricName: AutoMLMetricEnum


class AutoMLJobStepMetadata(TypedDict, total=False):
    """Metadata for an AutoML job step."""

    Arn: Optional[AutoMLJobArn]


class AutoMLPartialFailureReason(TypedDict, total=False):
    """The reason for a partial failure of an AutoML job."""

    PartialFailureMessage: Optional[AutoMLFailureReason]


AutoMLPartialFailureReasons = List[AutoMLPartialFailureReason]


class AutoMLJobSummary(TypedDict, total=False):
    """Provides a summary about an AutoML job."""

    AutoMLJobName: AutoMLJobName
    AutoMLJobArn: AutoMLJobArn
    AutoMLJobStatus: AutoMLJobStatus
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatus
    CreationTime: Timestamp
    EndTime: Optional[Timestamp]
    LastModifiedTime: Timestamp
    FailureReason: Optional[AutoMLFailureReason]
    PartialFailureReasons: Optional[AutoMLPartialFailureReasons]


AutoMLJobSummaries = List[AutoMLJobSummary]


class AutoMLOutputDataConfig(TypedDict, total=False):
    """The output data configuration."""

    KmsKeyId: Optional[KmsKeyId]
    S3OutputPath: S3Uri


TextGenerationHyperParameters = Dict[
    TextGenerationHyperParameterKey, TextGenerationHyperParameterValue
]


class TextGenerationJobConfig(TypedDict, total=False):
    """The collection of settings used by an AutoML job V2 for the text
    generation problem type.

    The text generation models that support fine-tuning in Autopilot are
    currently accessible exclusively in regions supported by Canvas. Refer
    to the documentation of Canvas for the `full list of its supported
    Regions <https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html>`__.
    """

    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]
    BaseModelName: Optional[BaseModelName]
    TextGenerationHyperParameters: Optional[TextGenerationHyperParameters]
    ModelAccessConfig: Optional[ModelAccessConfig]


class CandidateGenerationConfig(TypedDict, total=False):
    """Stores the configuration information for how model candidates are
    generated using an AutoML job V2.
    """

    AlgorithmsConfig: Optional[AutoMLAlgorithmsConfig]


class TabularJobConfig(TypedDict, total=False):
    """The collection of settings used by an AutoML job V2 for the tabular
    problem type.
    """

    CandidateGenerationConfig: Optional[CandidateGenerationConfig]
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]
    FeatureSpecificationS3Uri: Optional[S3Uri]
    Mode: Optional[AutoMLMode]
    GenerateCandidateDefinitionsOnly: Optional[GenerateCandidateDefinitionsOnly]
    ProblemType: Optional[ProblemType]
    TargetAttributeName: TargetAttributeName
    SampleWeightAttributeName: Optional[SampleWeightAttributeName]


class HolidayConfigAttributes(TypedDict, total=False):
    """Stores the holiday featurization attributes applicable to each item of
    time-series datasets during the training of a forecasting model. This
    allows the model to identify patterns associated with specific holidays.
    """

    CountryCode: Optional[CountryCode]


HolidayConfig = List[HolidayConfigAttributes]
GroupingAttributeNames = List[GroupingAttributeName]


class TimeSeriesConfig(TypedDict, total=False):
    """The collection of components that defines the time-series."""

    TargetAttributeName: TargetAttributeName
    TimestampAttributeName: TimestampAttributeName
    ItemIdentifierAttributeName: ItemIdentifierAttributeName
    GroupingAttributeNames: Optional[GroupingAttributeNames]


FillingTransformationMap = Dict[FillingType, FillingTransformationValue]
FillingTransformations = Dict[TransformationAttributeName, FillingTransformationMap]


class TimeSeriesTransformations(TypedDict, total=False):
    """Transformations allowed on the dataset. Supported transformations are
    ``Filling`` and ``Aggregation``. ``Filling`` specifies how to add values
    to missing values in the dataset. ``Aggregation`` defines how to
    aggregate data that does not align with forecast frequency.
    """

    Filling: Optional[FillingTransformations]
    Aggregation: Optional[AggregationTransformations]


ForecastQuantiles = List[ForecastQuantile]


class TimeSeriesForecastingJobConfig(TypedDict, total=False):
    """The collection of settings used by an AutoML job V2 for the time-series
    forecasting problem type.
    """

    FeatureSpecificationS3Uri: Optional[S3Uri]
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]
    ForecastFrequency: ForecastFrequency
    ForecastHorizon: ForecastHorizon
    ForecastQuantiles: Optional[ForecastQuantiles]
    Transformations: Optional[TimeSeriesTransformations]
    TimeSeriesConfig: TimeSeriesConfig
    HolidayConfig: Optional[HolidayConfig]
    CandidateGenerationConfig: Optional[CandidateGenerationConfig]


class TextClassificationJobConfig(TypedDict, total=False):
    """The collection of settings used by an AutoML job V2 for the text
    classification problem type.
    """

    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]
    ContentColumn: ContentColumn
    TargetLabelColumn: TargetLabelColumn


class ImageClassificationJobConfig(TypedDict, total=False):
    """The collection of settings used by an AutoML job V2 for the image
    classification problem type.
    """

    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]


class AutoMLProblemTypeConfig(TypedDict, total=False):
    """A collection of settings specific to the problem type used to configure
    an AutoML job V2. There must be one and only one config of the following
    type.
    """

    ImageClassificationJobConfig: Optional[ImageClassificationJobConfig]
    TextClassificationJobConfig: Optional[TextClassificationJobConfig]
    TimeSeriesForecastingJobConfig: Optional[TimeSeriesForecastingJobConfig]
    TabularJobConfig: Optional[TabularJobConfig]
    TextGenerationJobConfig: Optional[TextGenerationJobConfig]


class TextGenerationResolvedAttributes(TypedDict, total=False):
    """The resolved attributes specific to the text generation problem type."""

    BaseModelName: Optional[BaseModelName]


class TabularResolvedAttributes(TypedDict, total=False):
    """The resolved attributes specific to the tabular problem type."""

    ProblemType: Optional[ProblemType]


class AutoMLProblemTypeResolvedAttributes(TypedDict, total=False):
    """Stores resolved attributes specific to the problem type of an AutoML job
    V2.
    """

    TabularResolvedAttributes: Optional[TabularResolvedAttributes]
    TextGenerationResolvedAttributes: Optional[TextGenerationResolvedAttributes]


class AutoMLResolvedAttributes(TypedDict, total=False):
    """The resolved attributes used to configure an AutoML job V2."""

    AutoMLJobObjective: Optional[AutoMLJobObjective]
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]
    AutoMLProblemTypeResolvedAttributes: Optional[AutoMLProblemTypeResolvedAttributes]


class AutoParameter(TypedDict, total=False):
    """The name and an example value of the hyperparameter that you want to use
    in Autotune. If Automatic model tuning (AMT) determines that your
    hyperparameter is eligible for Autotune, an optimal hyperparameter range
    is selected for you.
    """

    Name: ParameterKey
    ValueHint: ParameterValue


AutoParameters = List[AutoParameter]
AutoRollbackAlarms = List[AlarmDetails]


class AutoRollbackConfig(TypedDict, total=False):
    """Automatic rollback configuration for handling endpoint deployment
    failures and recovery.
    """

    Alarms: Optional[AlarmList]


class Autotune(TypedDict, total=False):
    """A flag to indicate if you want to use Autotune to automatically find
    optimal values for the following fields:

    -  `ParameterRanges <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges>`__:
       The names and ranges of parameters that a hyperparameter tuning job
       can optimize.

    -  `ResourceLimits <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html>`__:
       The maximum resources that can be used for a training job. These
       resources include the maximum number of training jobs, the maximum
       runtime of a tuning job, and the maximum number of training jobs to
       run at the same time.

    -  `TrainingJobEarlyStoppingType <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType>`__:
       A flag that specifies whether or not to use early stopping for
       training jobs launched by a hyperparameter tuning job.

    -  `RetryStrategy <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy>`__:
       The number of times to retry a training job.

    -  `Strategy <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html>`__:
       Specifies how hyperparameter tuning chooses the combinations of
       hyperparameter values to use for the training jobs that it launches.

    -  `ConvergenceDetected <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html>`__:
       A flag to indicate that Automatic model tuning (AMT) has detected
       model convergence.
    """

    Mode: AutotuneMode


class BatchDataCaptureConfig(TypedDict, total=False):
    """Configuration to control how SageMaker captures inference data for batch
    transform jobs.
    """

    DestinationS3Uri: S3Uri
    KmsKeyId: Optional[KmsKeyId]
    GenerateInferenceId: Optional[Boolean]


class BatchDeleteClusterNodesError(TypedDict, total=False):
    """Represents an error encountered when deleting a node from a SageMaker
    HyperPod cluster.
    """

    Code: BatchDeleteClusterNodesErrorCode
    Message: String
    NodeId: ClusterNodeId


BatchDeleteClusterNodesErrorList = List[BatchDeleteClusterNodesError]
ClusterNodeIds = List[ClusterNodeId]


class BatchDeleteClusterNodesRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn
    NodeIds: ClusterNodeIds


class BatchDeleteClusterNodesResponse(TypedDict, total=False):
    Failed: Optional[BatchDeleteClusterNodesErrorList]
    Successful: Optional[ClusterNodeIds]


class BatchDescribeModelPackageError(TypedDict, total=False):
    """The error code and error description associated with the resource."""

    ErrorCode: String
    ErrorResponse: String


BatchDescribeModelPackageErrorMap = Dict[ModelPackageArn, BatchDescribeModelPackageError]
ModelPackageArnList = List[ModelPackageArn]


class BatchDescribeModelPackageInput(ServiceRequest):
    ModelPackageArnList: ModelPackageArnList


class InferenceSpecification(TypedDict, total=False):
    """Defines how to perform inference generation after a training job is run."""

    Containers: ModelPackageContainerDefinitionList
    SupportedTransformInstanceTypes: Optional[TransformInstanceTypes]
    SupportedRealtimeInferenceInstanceTypes: Optional[RealtimeInferenceInstanceTypes]
    SupportedContentTypes: Optional[ContentTypes]
    SupportedResponseMIMETypes: Optional[ResponseMIMETypes]


class BatchDescribeModelPackageSummary(TypedDict, total=False):
    """Provides summary information about the model package."""

    ModelPackageGroupName: EntityName
    ModelPackageVersion: Optional[ModelPackageVersion]
    ModelPackageArn: ModelPackageArn
    ModelPackageDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    InferenceSpecification: InferenceSpecification
    ModelPackageStatus: ModelPackageStatus
    ModelApprovalStatus: Optional[ModelApprovalStatus]


ModelPackageSummaries = Dict[ModelPackageArn, BatchDescribeModelPackageSummary]


class BatchDescribeModelPackageOutput(TypedDict, total=False):
    ModelPackageSummaries: Optional[ModelPackageSummaries]
    BatchDescribeModelPackageErrorMap: Optional[BatchDescribeModelPackageErrorMap]


class MonitoringParquetDatasetFormat(TypedDict, total=False):
    """Represents the Parquet dataset format used when running a monitoring
    job.
    """

    pass


class MonitoringJsonDatasetFormat(TypedDict, total=False):
    """Represents the JSON dataset format used when running a monitoring job."""

    Line: Optional[Boolean]


class MonitoringCsvDatasetFormat(TypedDict, total=False):
    """Represents the CSV dataset format used when running a monitoring job."""

    Header: Optional[Boolean]


class MonitoringDatasetFormat(TypedDict, total=False):
    """Represents the dataset format used when running a monitoring job."""

    Csv: Optional[MonitoringCsvDatasetFormat]
    Json: Optional[MonitoringJsonDatasetFormat]
    Parquet: Optional[MonitoringParquetDatasetFormat]


class BatchTransformInput(TypedDict, total=False):
    """Input object for the batch transform job."""

    DataCapturedDestinationS3Uri: DestinationS3Uri
    DatasetFormat: MonitoringDatasetFormat
    LocalPath: ProcessingLocalPath
    S3InputMode: Optional[ProcessingS3InputMode]
    S3DataDistributionType: Optional[ProcessingS3DataDistributionType]
    FeaturesAttribute: Optional[String]
    InferenceAttribute: Optional[String]
    ProbabilityAttribute: Optional[String]
    ProbabilityThresholdAttribute: Optional[ProbabilityThresholdAttribute]
    StartTimeOffset: Optional[MonitoringTimeOffsetString]
    EndTimeOffset: Optional[MonitoringTimeOffsetString]
    ExcludeFeaturesAttribute: Optional[ExcludeFeaturesAttribute]


class BestObjectiveNotImproving(TypedDict, total=False):
    """A structure that keeps track of which training jobs launched by your
    hyperparameter tuning job are not improving model performance as
    evaluated against an objective function.
    """

    MaxNumberOfTrainingJobsNotImproving: Optional[MaxNumberOfTrainingJobsNotImproving]


class MetricsSource(TypedDict, total=False):
    """Details about the metrics source."""

    ContentType: ContentType
    ContentDigest: Optional[ContentDigest]
    S3Uri: S3Uri


class Bias(TypedDict, total=False):
    """Contains bias metrics for a model."""

    Report: Optional[MetricsSource]
    PreTrainingReport: Optional[MetricsSource]
    PostTrainingReport: Optional[MetricsSource]


class CapacitySize(TypedDict, total=False):
    """Specifies the type and size of the endpoint capacity to activate for a
    blue/green deployment, a rolling deployment, or a rollback strategy. You
    can specify your batches as either instance count or the overall
    percentage or your fleet.

    For a rollback strategy, if you don't specify the fields in this object,
    or if you set the ``Value`` to 100%, then SageMaker uses a blue/green
    rollback strategy and rolls all traffic back to the blue fleet.
    """

    Type: CapacitySizeType
    Value: CapacitySizeValue


class TrafficRoutingConfig(TypedDict, total=False):
    """Defines the traffic routing strategy during an endpoint deployment to
    shift traffic from the old fleet to the new fleet.
    """

    Type: TrafficRoutingConfigType
    WaitIntervalInSeconds: WaitIntervalInSeconds
    CanarySize: Optional[CapacitySize]
    LinearStepSize: Optional[CapacitySize]


class BlueGreenUpdatePolicy(TypedDict, total=False):
    """Update policy for a blue/green deployment. If this update policy is
    specified, SageMaker creates a new fleet during the deployment while
    maintaining the old fleet. SageMaker flips traffic to the new fleet
    according to the specified traffic routing configuration. Only one
    update policy should be used in the deployment configuration. If no
    update policy is specified, SageMaker uses a blue/green deployment
    strategy with all at once traffic shifting by default.
    """

    TrafficRoutingConfiguration: TrafficRoutingConfig
    TerminationWaitInSeconds: Optional[TerminationWaitInSeconds]
    MaximumExecutionTimeoutInSeconds: Optional[MaximumExecutionTimeoutInSeconds]


class CacheHitResult(TypedDict, total=False):
    """Details on the cache hit of a pipeline execution step."""

    SourcePipelineExecutionArn: Optional[PipelineExecutionArn]


class OutputParameter(TypedDict, total=False):
    """An output parameter of a pipeline step."""

    Name: String256
    Value: String1024


OutputParameterList = List[OutputParameter]


class CallbackStepMetadata(TypedDict, total=False):
    """Metadata about a callback step."""

    CallbackToken: Optional[CallbackToken]
    SqsQueueUrl: Optional[String256]
    OutputParameters: Optional[OutputParameterList]


class EmrServerlessSettings(TypedDict, total=False):
    """The settings for running Amazon EMR Serverless jobs in SageMaker Canvas."""

    ExecutionRoleArn: Optional[RoleArn]
    Status: Optional[FeatureStatus]


class GenerativeAiSettings(TypedDict, total=False):
    """The generative AI settings for the SageMaker Canvas application.

    Configure these settings for Canvas users starting chats with generative
    AI foundation models. For more information, see `Use generative AI with
    foundation
    models <https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat.html>`__.
    """

    AmazonBedrockRoleArn: Optional[RoleArn]


class KendraSettings(TypedDict, total=False):
    """The Amazon SageMaker Canvas application setting where you configure
    document querying.
    """

    Status: Optional[FeatureStatus]


class DirectDeploySettings(TypedDict, total=False):
    """The model deployment settings for the SageMaker Canvas application.

    In order to enable model deployment for Canvas, the SageMaker Domain's
    or user profile's Amazon Web Services IAM execution role must have the
    ``AmazonSageMakerCanvasDirectDeployAccess`` policy attached. You can
    also turn on model deployment permissions through the SageMaker Domain's
    or user profile's settings in the SageMaker console.
    """

    Status: Optional[FeatureStatus]


class IdentityProviderOAuthSetting(TypedDict, total=False):
    """The Amazon SageMaker Canvas application setting where you configure
    OAuth for connecting to an external data source, such as Snowflake.
    """

    DataSourceName: Optional[DataSourceName]
    Status: Optional[FeatureStatus]
    SecretArn: Optional[SecretArn]


IdentityProviderOAuthSettings = List[IdentityProviderOAuthSetting]


class WorkspaceSettings(TypedDict, total=False):
    """The workspace settings for the SageMaker Canvas application."""

    S3ArtifactPath: Optional[S3Uri]
    S3KmsKeyId: Optional[KmsKeyId]


class ModelRegisterSettings(TypedDict, total=False):
    """The model registry settings for the SageMaker Canvas application."""

    Status: Optional[FeatureStatus]
    CrossAccountModelRegisterRoleArn: Optional[RoleArn]


class TimeSeriesForecastingSettings(TypedDict, total=False):
    """Time series forecast settings for the SageMaker Canvas application."""

    Status: Optional[FeatureStatus]
    AmazonForecastRoleArn: Optional[RoleArn]


class CanvasAppSettings(TypedDict, total=False):
    """The SageMaker Canvas application settings."""

    TimeSeriesForecastingSettings: Optional[TimeSeriesForecastingSettings]
    ModelRegisterSettings: Optional[ModelRegisterSettings]
    WorkspaceSettings: Optional[WorkspaceSettings]
    IdentityProviderOAuthSettings: Optional[IdentityProviderOAuthSettings]
    DirectDeploySettings: Optional[DirectDeploySettings]
    KendraSettings: Optional[KendraSettings]
    GenerativeAiSettings: Optional[GenerativeAiSettings]
    EmrServerlessSettings: Optional[EmrServerlessSettings]


class CapacitySizeConfig(TypedDict, total=False):
    """The configuration of the size measurements of the AMI update. Using this
    configuration, you can specify whether SageMaker should update your
    instance group by an amount or percentage of instances.
    """

    Type: NodeUnavailabilityType
    Value: NodeUnavailabilityValue


JsonContentTypes = List[JsonContentType]
CsvContentTypes = List[CsvContentType]


class CaptureContentTypeHeader(TypedDict, total=False):
    """Configuration specifying how to treat different headers. If no headers
    are specified Amazon SageMaker AI will by default base64 encode when
    capturing the data.
    """

    CsvContentTypes: Optional[CsvContentTypes]
    JsonContentTypes: Optional[JsonContentTypes]


class CaptureOption(TypedDict, total=False):
    """Specifies data Model Monitor will capture."""

    CaptureMode: CaptureMode


CaptureOptionList = List[CaptureOption]
CategoricalParameterRangeValues = List[String128]


class CategoricalParameter(TypedDict, total=False):
    """Environment parameters you want to benchmark your load test against."""

    Name: String64
    Value: CategoricalParameterRangeValues


ParameterValues = List[ParameterValue]


class CategoricalParameterRange(TypedDict, total=False):
    """A list of categorical hyperparameters to tune."""

    Name: ParameterKey
    Values: ParameterValues


class CategoricalParameterRangeSpecification(TypedDict, total=False):
    """Defines the possible values for a categorical hyperparameter."""

    Values: ParameterValues


CategoricalParameterRanges = List[CategoricalParameterRange]
CategoricalParameters = List[CategoricalParameter]
InputModes = List[TrainingInputMode]
CompressionTypes = List[CompressionType]


class ChannelSpecification(TypedDict, total=False):
    """Defines a named input source, called a channel, to be used by an
    algorithm.
    """

    Name: ChannelName
    Description: Optional[EntityDescription]
    IsRequired: Optional[Boolean]
    SupportedContentTypes: ContentTypes
    SupportedCompressionTypes: Optional[CompressionTypes]
    SupportedInputModes: InputModes


ChannelSpecifications = List[ChannelSpecification]


class CheckpointConfig(TypedDict, total=False):
    """Contains information about the output location for managed spot training
    checkpoint data.
    """

    S3Uri: S3Uri
    LocalPath: Optional[DirectoryPath]


Cidrs = List[Cidr]


class ClarifyCheckStepMetadata(TypedDict, total=False):
    """The container for the metadata for the ClarifyCheck step. For more
    information, see the topic on `ClarifyCheck
    step <https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-clarify-check>`__
    in the *Amazon SageMaker Developer Guide*.
    """

    CheckType: Optional[String256]
    BaselineUsedForDriftCheckConstraints: Optional[String1024]
    CalculatedBaselineConstraints: Optional[String1024]
    ModelPackageGroupName: Optional[String256]
    ViolationReport: Optional[String1024]
    CheckJobArn: Optional[String256]
    SkipCheck: Optional[Boolean]
    RegisterNewBaseline: Optional[Boolean]


class ClarifyTextConfig(TypedDict, total=False):
    """A parameter used to configure the SageMaker Clarify explainer to treat
    text features as text so that explanations are provided for individual
    units of text. Required only for natural language processing (NLP)
    explainability.
    """

    Language: ClarifyTextLanguage
    Granularity: ClarifyTextGranularity


class ClarifyShapBaselineConfig(TypedDict, total=False):
    """The configuration for the `SHAP
    baseline <https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.html>`__
    (also called the background or reference dataset) of the Kernal SHAP
    algorithm.

    -  The number of records in the baseline data determines the size of the
       synthetic dataset, which has an impact on latency of explainability
       requests. For more information, see the **Synthetic data** of
       `Configure and create an
       endpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html>`__.

    -  ``ShapBaseline`` and ``ShapBaselineUri`` are mutually exclusive
       parameters. One or the either is required to configure a SHAP
       baseline.
    """

    MimeType: Optional[ClarifyMimeType]
    ShapBaseline: Optional[ClarifyShapBaseline]
    ShapBaselineUri: Optional[Url]


class ClarifyShapConfig(TypedDict, total=False):
    """The configuration for SHAP analysis using SageMaker Clarify Explainer."""

    ShapBaselineConfig: ClarifyShapBaselineConfig
    NumberOfSamples: Optional[ClarifyShapNumberOfSamples]
    UseLogit: Optional[ClarifyShapUseLogit]
    Seed: Optional[ClarifyShapSeed]
    TextConfig: Optional[ClarifyTextConfig]


ClarifyFeatureTypes = List[ClarifyFeatureType]
ClarifyFeatureHeaders = List[ClarifyHeader]
ClarifyLabelHeaders = List[ClarifyHeader]


class ClarifyInferenceConfig(TypedDict, total=False):
    """The inference configuration parameter for the model container."""

    FeaturesAttribute: Optional[ClarifyFeaturesAttribute]
    ContentTemplate: Optional[ClarifyContentTemplate]
    MaxRecordCount: Optional[ClarifyMaxRecordCount]
    MaxPayloadInMB: Optional[ClarifyMaxPayloadInMB]
    ProbabilityIndex: Optional[ClarifyProbabilityIndex]
    LabelIndex: Optional[ClarifyLabelIndex]
    ProbabilityAttribute: Optional[ClarifyProbabilityAttribute]
    LabelAttribute: Optional[ClarifyLabelAttribute]
    LabelHeaders: Optional[ClarifyLabelHeaders]
    FeatureHeaders: Optional[ClarifyFeatureHeaders]
    FeatureTypes: Optional[ClarifyFeatureTypes]


class ClarifyExplainerConfig(TypedDict, total=False):
    """The configuration parameters for the SageMaker Clarify explainer."""

    EnableExplanations: Optional[ClarifyEnableExplanations]
    InferenceConfig: Optional[ClarifyInferenceConfig]
    ShapConfig: ClarifyShapConfig


class ClusterEbsVolumeConfig(TypedDict, total=False):
    """Defines the configuration for attaching an additional Amazon Elastic
    Block Store (EBS) volume to each instance of the SageMaker HyperPod
    cluster instance group. To learn more, see `SageMaker HyperPod release
    notes: June 20,
    2024 <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620>`__.
    """

    VolumeSizeInGB: ClusterEbsVolumeSizeInGB


class RollingDeploymentPolicy(TypedDict, total=False):
    """The configurations that SageMaker uses when updating the AMI versions."""

    MaximumBatchSize: CapacitySizeConfig
    RollbackMaximumBatchSize: Optional[CapacitySizeConfig]


class DeploymentConfiguration(TypedDict, total=False):
    """The configuration to use when updating the AMI versions."""

    RollingUpdatePolicy: Optional[RollingDeploymentPolicy]
    WaitIntervalInSeconds: Optional[WaitTimeIntervalInSeconds]
    AutoRollbackConfiguration: Optional[AutoRollbackAlarms]


class ScheduledUpdateConfig(TypedDict, total=False):
    """The configuration object of the schedule that SageMaker follows when
    updating the AMI.
    """

    ScheduleExpression: CronScheduleExpression
    DeploymentConfig: Optional[DeploymentConfiguration]


OnStartDeepHealthChecks = List[DeepHealthCheckType]


class ClusterInstanceStorageConfig(TypedDict, total=False):
    """Defines the configuration for attaching additional storage to the
    instances in the SageMaker HyperPod cluster instance group. To learn
    more, see `SageMaker HyperPod release notes: June 20,
    2024 <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620>`__.
    """

    EbsVolumeConfig: Optional[ClusterEbsVolumeConfig]


ClusterInstanceStorageConfigs = List[ClusterInstanceStorageConfig]


class ClusterLifeCycleConfig(TypedDict, total=False):
    """The lifecycle configuration for a SageMaker HyperPod cluster."""

    SourceS3Uri: S3Uri
    OnCreate: ClusterLifeCycleConfigFileName


class ClusterInstanceGroupDetails(TypedDict, total=False):
    """Details of an instance group in a SageMaker HyperPod cluster."""

    CurrentCount: Optional[ClusterNonNegativeInstanceCount]
    TargetCount: Optional[ClusterInstanceCount]
    InstanceGroupName: Optional[ClusterInstanceGroupName]
    InstanceType: Optional[ClusterInstanceType]
    LifeCycleConfig: Optional[ClusterLifeCycleConfig]
    ExecutionRole: Optional[RoleArn]
    ThreadsPerCore: Optional[ClusterThreadsPerCore]
    InstanceStorageConfigs: Optional[ClusterInstanceStorageConfigs]
    OnStartDeepHealthChecks: Optional[OnStartDeepHealthChecks]
    Status: Optional[InstanceGroupStatus]
    TrainingPlanArn: Optional[TrainingPlanArn]
    TrainingPlanStatus: Optional[InstanceGroupTrainingPlanStatus]
    OverrideVpcConfig: Optional[VpcConfig]
    ScheduledUpdateConfig: Optional[ScheduledUpdateConfig]


ClusterInstanceGroupDetailsList = List[ClusterInstanceGroupDetails]


class ClusterInstanceGroupSpecification(TypedDict, total=False):
    """The specifications of an instance group that you need to define."""

    InstanceCount: ClusterInstanceCount
    InstanceGroupName: ClusterInstanceGroupName
    InstanceType: ClusterInstanceType
    LifeCycleConfig: ClusterLifeCycleConfig
    ExecutionRole: RoleArn
    ThreadsPerCore: Optional[ClusterThreadsPerCore]
    InstanceStorageConfigs: Optional[ClusterInstanceStorageConfigs]
    OnStartDeepHealthChecks: Optional[OnStartDeepHealthChecks]
    TrainingPlanArn: Optional[TrainingPlanArn]
    OverrideVpcConfig: Optional[VpcConfig]
    ScheduledUpdateConfig: Optional[ScheduledUpdateConfig]


ClusterInstanceGroupSpecifications = List[ClusterInstanceGroupSpecification]
ClusterInstanceGroupsToDelete = List[ClusterInstanceGroupName]


class ClusterInstancePlacement(TypedDict, total=False):
    """Specifies the placement details for the node in the SageMaker HyperPod
    cluster, including the Availability Zone and the unique identifier (ID)
    of the Availability Zone.
    """

    AvailabilityZone: Optional[ClusterAvailabilityZone]
    AvailabilityZoneId: Optional[ClusterAvailabilityZoneId]


class ClusterInstanceStatusDetails(TypedDict, total=False):
    """Details of an instance in a SageMaker HyperPod cluster."""

    Status: ClusterInstanceStatus
    Message: Optional[String]


class ClusterNodeDetails(TypedDict, total=False):
    """Details of an instance (also called a *node* interchangeably) in a
    SageMaker HyperPod cluster.
    """

    InstanceGroupName: Optional[ClusterInstanceGroupName]
    InstanceId: Optional[String]
    InstanceStatus: Optional[ClusterInstanceStatusDetails]
    InstanceType: Optional[ClusterInstanceType]
    LaunchTime: Optional[Timestamp]
    LastSoftwareUpdateTime: Optional[Timestamp]
    LifeCycleConfig: Optional[ClusterLifeCycleConfig]
    OverrideVpcConfig: Optional[VpcConfig]
    ThreadsPerCore: Optional[ClusterThreadsPerCore]
    InstanceStorageConfigs: Optional[ClusterInstanceStorageConfigs]
    PrivatePrimaryIp: Optional[ClusterPrivatePrimaryIp]
    PrivatePrimaryIpv6: Optional[ClusterPrivatePrimaryIpv6]
    PrivateDnsHostname: Optional[ClusterPrivateDnsHostname]
    Placement: Optional[ClusterInstancePlacement]


class ClusterNodeSummary(TypedDict, total=False):
    """Lists a summary of the properties of an instance (also called a *node*
    interchangeably) of a SageMaker HyperPod cluster.
    """

    InstanceGroupName: ClusterInstanceGroupName
    InstanceId: String
    InstanceType: ClusterInstanceType
    LaunchTime: Timestamp
    LastSoftwareUpdateTime: Optional[Timestamp]
    InstanceStatus: ClusterInstanceStatusDetails


ClusterNodeSummaries = List[ClusterNodeSummary]


class ClusterOrchestratorEksConfig(TypedDict, total=False):
    """The configuration settings for the Amazon EKS cluster used as the
    orchestrator for the SageMaker HyperPod cluster.
    """

    ClusterArn: EksClusterArn


class ClusterOrchestrator(TypedDict, total=False):
    """The type of orchestrator used for the SageMaker HyperPod cluster."""

    Eks: ClusterOrchestratorEksConfig


class ClusterSchedulerConfigSummary(TypedDict, total=False):
    """Summary of the cluster policy."""

    ClusterSchedulerConfigArn: ClusterSchedulerConfigArn
    ClusterSchedulerConfigId: ClusterSchedulerConfigId
    ClusterSchedulerConfigVersion: Optional[Integer]
    Name: EntityName
    CreationTime: Timestamp
    LastModifiedTime: Optional[Timestamp]
    Status: SchedulerResourceStatus
    ClusterArn: Optional[ClusterArn]


ClusterSchedulerConfigSummaryList = List[ClusterSchedulerConfigSummary]
TrainingPlanArns = List[TrainingPlanArn]


class ClusterSummary(TypedDict, total=False):
    """Lists a summary of the properties of a SageMaker HyperPod cluster."""

    ClusterArn: ClusterArn
    ClusterName: ClusterName
    CreationTime: Timestamp
    ClusterStatus: ClusterStatus
    TrainingPlanArns: Optional[TrainingPlanArns]


ClusterSummaries = List[ClusterSummary]
LifecycleConfigArns = List[StudioLifecycleConfigArn]


class CustomImage(TypedDict, total=False):
    """A custom SageMaker AI image. For more information, see `Bring your own
    SageMaker AI
    image <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html>`__.
    """

    ImageName: ImageName
    ImageVersionNumber: Optional[ImageVersionNumber]
    AppImageConfigName: AppImageConfigName


CustomImages = List[CustomImage]


class CodeEditorAppSettings(TypedDict, total=False):
    """The Code Editor application settings.

    For more information about Code Editor, see `Get started with Code
    Editor in Amazon
    SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html>`__.
    """

    DefaultResourceSpec: Optional[ResourceSpec]
    CustomImages: Optional[CustomImages]
    LifecycleConfigArns: Optional[LifecycleConfigArns]
    AppLifecycleManagement: Optional[AppLifecycleManagement]
    BuiltInLifecycleConfigArn: Optional[StudioLifecycleConfigArn]


class CodeRepository(TypedDict, total=False):
    """A Git repository that SageMaker AI automatically displays to users for
    cloning in the JupyterServer application.
    """

    RepositoryUrl: RepositoryUrl


CodeRepositories = List[CodeRepository]


class GitConfig(TypedDict, total=False):
    """Specifies configuration details for a Git repository in your Amazon Web
    Services account.
    """

    RepositoryUrl: GitConfigUrl
    Branch: Optional[Branch]
    SecretArn: Optional[SecretArn]


LastModifiedTime = datetime


class CodeRepositorySummary(TypedDict, total=False):
    """Specifies summary information about a Git repository."""

    CodeRepositoryName: EntityName
    CodeRepositoryArn: CodeRepositoryArn
    CreationTime: CreationTime
    LastModifiedTime: LastModifiedTime
    GitConfig: Optional[GitConfig]


CodeRepositorySummaryList = List[CodeRepositorySummary]


class CognitoConfig(TypedDict, total=False):
    """Use this parameter to configure your Amazon Cognito workforce. A single
    Cognito workforce is created using and corresponds to a single `Amazon
    Cognito user
    pool <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html>`__.
    """

    UserPool: CognitoUserPool
    ClientId: ClientId


class CognitoMemberDefinition(TypedDict, total=False):
    """Identifies a Amazon Cognito user group. A user group can be used in on
    or more work teams.
    """

    UserPool: CognitoUserPool
    UserGroup: CognitoUserGroup
    ClientId: ClientId


class VectorConfig(TypedDict, total=False):
    """Configuration for your vector collection type."""

    Dimension: Dimension


class CollectionConfig(TypedDict, total=False):
    """Configuration for your collection."""

    VectorConfig: Optional[VectorConfig]


CollectionParameters = Dict[ConfigKey, ConfigValue]


class CollectionConfiguration(TypedDict, total=False):
    """Configuration information for the Amazon SageMaker Debugger output
    tensor collections.
    """

    CollectionName: Optional[CollectionName]
    CollectionParameters: Optional[CollectionParameters]


CollectionConfigurations = List[CollectionConfiguration]


class CompilationJobSummary(TypedDict, total=False):
    """A summary of a model compilation job."""

    CompilationJobName: EntityName
    CompilationJobArn: CompilationJobArn
    CreationTime: CreationTime
    CompilationStartTime: Optional[Timestamp]
    CompilationEndTime: Optional[Timestamp]
    CompilationTargetDevice: Optional[TargetDevice]
    CompilationTargetPlatformOs: Optional[TargetPlatformOs]
    CompilationTargetPlatformArch: Optional[TargetPlatformArch]
    CompilationTargetPlatformAccelerator: Optional[TargetPlatformAccelerator]
    LastModifiedTime: Optional[LastModifiedTime]
    CompilationJobStatus: CompilationJobStatus


CompilationJobSummaries = List[CompilationJobSummary]


class ResourceSharingConfig(TypedDict, total=False):
    """Resource sharing configuration."""

    Strategy: ResourceSharingStrategy
    BorrowLimit: Optional[BorrowLimit]


class ComputeQuotaResourceConfig(TypedDict, total=False):
    """Configuration of the resources used for the compute allocation
    definition.
    """

    InstanceType: ClusterInstanceType
    Count: InstanceCount


ComputeQuotaResourceConfigList = List[ComputeQuotaResourceConfig]


class ComputeQuotaConfig(TypedDict, total=False):
    """Configuration of the compute allocation definition for an entity. This
    includes the resource sharing option and the setting to preempt low
    priority tasks.
    """

    ComputeQuotaResources: Optional[ComputeQuotaResourceConfigList]
    ResourceSharingConfig: Optional[ResourceSharingConfig]
    PreemptTeamTasks: Optional[PreemptTeamTasks]


class ComputeQuotaTarget(TypedDict, total=False):
    """The target entity to allocate compute resources to."""

    TeamName: ComputeQuotaTargetTeamName
    FairShareWeight: Optional[FairShareWeight]


class ComputeQuotaSummary(TypedDict, total=False):
    """Summary of the compute allocation definition."""

    ComputeQuotaArn: ComputeQuotaArn
    ComputeQuotaId: ComputeQuotaId
    Name: EntityName
    ComputeQuotaVersion: Optional[Integer]
    Status: SchedulerResourceStatus
    ClusterArn: Optional[ClusterArn]
    ComputeQuotaConfig: Optional[ComputeQuotaConfig]
    ComputeQuotaTarget: ComputeQuotaTarget
    ActivationState: Optional[ActivationState]
    CreationTime: Timestamp
    LastModifiedTime: Optional[Timestamp]


ComputeQuotaSummaryList = List[ComputeQuotaSummary]


class ConditionStepMetadata(TypedDict, total=False):
    """Metadata for a Condition step."""

    Outcome: Optional[ConditionOutcome]


class MultiModelConfig(TypedDict, total=False):
    """Specifies additional configuration for hosting multi-model endpoints."""

    ModelCacheSetting: Optional[ModelCacheSetting]


class RepositoryAuthConfig(TypedDict, total=False):
    """Specifies an authentication configuration for the private docker
    registry where your model image is hosted. Specify a value for this
    property only if you specified ``Vpc`` as the value for the
    ``RepositoryAccessMode`` field of the ``ImageConfig`` object that you
    passed to a call to ``CreateModel`` and the private Docker registry
    where the model image is hosted requires authentication.
    """

    RepositoryCredentialsProviderArn: RepositoryCredentialsProviderArn


class ImageConfig(TypedDict, total=False):
    """Specifies whether the model container is in Amazon ECR or a private
    Docker registry accessible from your Amazon Virtual Private Cloud (VPC).
    """

    RepositoryAccessMode: RepositoryAccessMode
    RepositoryAuthConfig: Optional[RepositoryAuthConfig]


class ContainerDefinition(TypedDict, total=False):
    """Describes the container, as part of model definition."""

    ContainerHostname: Optional[ContainerHostname]
    Image: Optional[ContainerImage]
    ImageConfig: Optional[ImageConfig]
    Mode: Optional[ContainerMode]
    ModelDataUrl: Optional[Url]
    ModelDataSource: Optional[ModelDataSource]
    AdditionalModelDataSources: Optional[AdditionalModelDataSources]
    Environment: Optional[EnvironmentMap]
    ModelPackageName: Optional[VersionedArnOrName]
    InferenceSpecificationName: Optional[InferenceSpecificationName]
    MultiModelConfig: Optional[MultiModelConfig]


ContainerDefinitionList = List[ContainerDefinition]
ContentClassifiers = List[ContentClassifier]


class ContextSource(TypedDict, total=False):
    """A structure describing the source of a context."""

    SourceUri: SourceUri
    SourceType: Optional[String256]
    SourceId: Optional[String256]


class ContextSummary(TypedDict, total=False):
    """Lists a summary of the properties of a context. A context provides a
    logical grouping of other entities.
    """

    ContextArn: Optional[ContextArn]
    ContextName: Optional[ContextName]
    Source: Optional[ContextSource]
    ContextType: Optional[String256]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


ContextSummaries = List[ContextSummary]


class ContinuousParameterRange(TypedDict, total=False):
    """A list of continuous hyperparameters to tune."""

    Name: ParameterKey
    MinValue: ParameterValue
    MaxValue: ParameterValue
    ScalingType: Optional[HyperParameterScalingType]


class ContinuousParameterRangeSpecification(TypedDict, total=False):
    """Defines the possible values for a continuous hyperparameter."""

    MinValue: ParameterValue
    MaxValue: ParameterValue


ContinuousParameterRanges = List[ContinuousParameterRange]


class ConvergenceDetected(TypedDict, total=False):
    """A flag to indicating that automatic model tuning (AMT) has detected
    model convergence, defined as a lack of significant improvement (1% or
    less) against an objective metric.
    """

    CompleteOnConvergence: Optional[CompleteOnConvergence]


class MetadataProperties(TypedDict, total=False):
    """Metadata properties of the tracking entity, trial, or trial component."""

    CommitId: Optional[MetadataPropertyValue]
    Repository: Optional[MetadataPropertyValue]
    GeneratedBy: Optional[MetadataPropertyValue]
    ProjectId: Optional[MetadataPropertyValue]


LineageEntityParameters = Dict[StringParameterValue, StringParameterValue]


class CreateActionRequest(ServiceRequest):
    ActionName: ExperimentEntityName
    Source: ActionSource
    ActionType: String256
    Description: Optional[ExperimentDescription]
    Status: Optional[ActionStatus]
    Properties: Optional[LineageEntityParameters]
    MetadataProperties: Optional[MetadataProperties]
    Tags: Optional[TagList]


class CreateActionResponse(TypedDict, total=False):
    ActionArn: Optional[ActionArn]


class HyperParameterTuningJobObjective(TypedDict, total=False):
    """Defines the objective metric for a hyperparameter tuning job.
    Hyperparameter tuning uses the value of this metric to evaluate the
    training jobs it launches, and returns the training job that results in
    either the highest or lowest value for this metric, depending on the
    value you specify for the ``Type`` parameter. If you want to define a
    custom objective metric, see `Define metrics and environment
    variables <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html>`__.
    """

    Type: HyperParameterTuningJobObjectiveType
    MetricName: MetricName


HyperParameterTuningJobObjectives = List[HyperParameterTuningJobObjective]
TrainingInstanceTypes = List[TrainingInstanceType]


class IntegerParameterRangeSpecification(TypedDict, total=False):
    """Defines the possible values for an integer hyperparameter."""

    MinValue: ParameterValue
    MaxValue: ParameterValue


class ParameterRange(TypedDict, total=False):
    """Defines the possible values for categorical, continuous, and integer
    hyperparameters to be used by an algorithm.
    """

    IntegerParameterRangeSpecification: Optional[IntegerParameterRangeSpecification]
    ContinuousParameterRangeSpecification: Optional[ContinuousParameterRangeSpecification]
    CategoricalParameterRangeSpecification: Optional[CategoricalParameterRangeSpecification]


class HyperParameterSpecification(TypedDict, total=False):
    """Defines a hyperparameter to be used by an algorithm."""

    Name: ParameterName
    Description: Optional[EntityDescription]
    Type: ParameterType
    Range: Optional[ParameterRange]
    IsTunable: Optional[Boolean]
    IsRequired: Optional[Boolean]
    DefaultValue: Optional[HyperParameterValue]


HyperParameterSpecifications = List[HyperParameterSpecification]


class TrainingSpecification(TypedDict, total=False):
    """Defines how the algorithm is used for a training job."""

    TrainingImage: ContainerImage
    TrainingImageDigest: Optional[ImageDigest]
    SupportedHyperParameters: Optional[HyperParameterSpecifications]
    SupportedTrainingInstanceTypes: TrainingInstanceTypes
    SupportsDistributedTraining: Optional[Boolean]
    MetricDefinitions: Optional[MetricDefinitionList]
    TrainingChannels: ChannelSpecifications
    SupportedTuningJobObjectiveMetrics: Optional[HyperParameterTuningJobObjectives]
    AdditionalS3DataSource: Optional[AdditionalS3DataSource]


class CreateAlgorithmInput(ServiceRequest):
    AlgorithmName: EntityName
    AlgorithmDescription: Optional[EntityDescription]
    TrainingSpecification: TrainingSpecification
    InferenceSpecification: Optional[InferenceSpecification]
    ValidationSpecification: Optional[AlgorithmValidationSpecification]
    CertifyForMarketplace: Optional[CertifyForMarketplace]
    Tags: Optional[TagList]


class CreateAlgorithmOutput(TypedDict, total=False):
    AlgorithmArn: AlgorithmArn


class CreateAppImageConfigRequest(ServiceRequest):
    AppImageConfigName: AppImageConfigName
    Tags: Optional[TagList]
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfig]
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfig]
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfig]


class CreateAppImageConfigResponse(TypedDict, total=False):
    AppImageConfigArn: Optional[AppImageConfigArn]


class CreateAppRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: Optional[UserProfileName]
    SpaceName: Optional[SpaceName]
    AppType: AppType
    AppName: AppName
    Tags: Optional[TagList]
    ResourceSpec: Optional[ResourceSpec]
    RecoveryMode: Optional[Boolean]


class CreateAppResponse(TypedDict, total=False):
    AppArn: Optional[AppArn]


class CreateArtifactRequest(ServiceRequest):
    ArtifactName: Optional[ExperimentEntityName]
    Source: ArtifactSource
    ArtifactType: String256
    Properties: Optional[ArtifactProperties]
    MetadataProperties: Optional[MetadataProperties]
    Tags: Optional[TagList]


class CreateArtifactResponse(TypedDict, total=False):
    ArtifactArn: Optional[ArtifactArn]


class ModelDeployConfig(TypedDict, total=False):
    """Specifies how to generate the endpoint name for an automatic one-click
    Autopilot model deployment.
    """

    AutoGenerateEndpointName: Optional[AutoGenerateEndpointName]
    EndpointName: Optional[EndpointName]


class CreateAutoMLJobRequest(ServiceRequest):
    AutoMLJobName: AutoMLJobName
    InputDataConfig: AutoMLInputDataConfig
    OutputDataConfig: AutoMLOutputDataConfig
    ProblemType: Optional[ProblemType]
    AutoMLJobObjective: Optional[AutoMLJobObjective]
    AutoMLJobConfig: Optional[AutoMLJobConfig]
    RoleArn: RoleArn
    GenerateCandidateDefinitionsOnly: Optional[GenerateCandidateDefinitionsOnly]
    Tags: Optional[TagList]
    ModelDeployConfig: Optional[ModelDeployConfig]


class CreateAutoMLJobResponse(TypedDict, total=False):
    AutoMLJobArn: AutoMLJobArn


class CreateAutoMLJobV2Request(ServiceRequest):
    AutoMLJobName: AutoMLJobName
    AutoMLJobInputDataConfig: AutoMLJobInputDataConfig
    OutputDataConfig: AutoMLOutputDataConfig
    AutoMLProblemTypeConfig: AutoMLProblemTypeConfig
    RoleArn: RoleArn
    Tags: Optional[TagList]
    SecurityConfig: Optional[AutoMLSecurityConfig]
    AutoMLJobObjective: Optional[AutoMLJobObjective]
    ModelDeployConfig: Optional[ModelDeployConfig]
    DataSplitConfig: Optional[AutoMLDataSplitConfig]
    AutoMLComputeConfig: Optional[AutoMLComputeConfig]


class CreateAutoMLJobV2Response(TypedDict, total=False):
    AutoMLJobArn: AutoMLJobArn


class CreateClusterRequest(ServiceRequest):
    ClusterName: ClusterName
    InstanceGroups: ClusterInstanceGroupSpecifications
    VpcConfig: Optional[VpcConfig]
    Tags: Optional[TagList]
    Orchestrator: Optional[ClusterOrchestrator]
    NodeRecovery: Optional[ClusterNodeRecovery]


class CreateClusterResponse(TypedDict, total=False):
    ClusterArn: ClusterArn


class PriorityClass(TypedDict, total=False):
    """Priority class configuration. When included in ``PriorityClasses``,
    these class configurations define how tasks are queued.
    """

    Name: ClusterSchedulerPriorityClassName
    Weight: PriorityWeight


PriorityClassList = List[PriorityClass]


class SchedulerConfig(TypedDict, total=False):
    """Cluster policy configuration. This policy is used for task
    prioritization and fair-share allocation. This helps prioritize critical
    workloads and distributes idle compute across entities.
    """

    PriorityClasses: Optional[PriorityClassList]
    FairShare: Optional[FairShare]


class CreateClusterSchedulerConfigRequest(ServiceRequest):
    Name: EntityName
    ClusterArn: ClusterArn
    SchedulerConfig: SchedulerConfig
    Description: Optional[EntityDescription]
    Tags: Optional[TagList]


class CreateClusterSchedulerConfigResponse(TypedDict, total=False):
    ClusterSchedulerConfigArn: ClusterSchedulerConfigArn
    ClusterSchedulerConfigId: ClusterSchedulerConfigId


class CreateCodeRepositoryInput(ServiceRequest):
    CodeRepositoryName: EntityName
    GitConfig: GitConfig
    Tags: Optional[TagList]


class CreateCodeRepositoryOutput(TypedDict, total=False):
    CodeRepositoryArn: CodeRepositoryArn


NeoVpcSubnets = List[NeoVpcSubnetId]
NeoVpcSecurityGroupIds = List[NeoVpcSecurityGroupId]


class NeoVpcConfig(TypedDict, total=False):
    """The
    `VpcConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html>`__
    configuration object that specifies the VPC that you want the
    compilation jobs to connect to. For more information on controlling
    access to your Amazon S3 buckets used for compilation job, see `Give
    Amazon SageMaker AI Compilation Jobs Access to Resources in Your Amazon
    VPC <https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html>`__.
    """

    SecurityGroupIds: NeoVpcSecurityGroupIds
    Subnets: NeoVpcSubnets


class TargetPlatform(TypedDict, total=False):
    """Contains information about a target platform that you want your model to
    run on, such as OS, architecture, and accelerators. It is an alternative
    of ``TargetDevice``.
    """

    Os: TargetPlatformOs
    Arch: TargetPlatformArch
    Accelerator: Optional[TargetPlatformAccelerator]


class OutputConfig(TypedDict, total=False):
    """Contains information about the output location for the compiled model
    and the target device that the model runs on. ``TargetDevice`` and
    ``TargetPlatform`` are mutually exclusive, so you need to choose one
    between the two to specify your target device or platform. If you cannot
    find your device you want to use from the ``TargetDevice`` list, use
    ``TargetPlatform`` to describe the platform of your edge device and
    ``CompilerOptions`` if there are specific settings that are required or
    recommended to use for particular TargetPlatform.
    """

    S3OutputLocation: S3Uri
    TargetDevice: Optional[TargetDevice]
    TargetPlatform: Optional[TargetPlatform]
    CompilerOptions: Optional[CompilerOptions]
    KmsKeyId: Optional[KmsKeyId]


class InputConfig(TypedDict, total=False):
    """Contains information about the location of input model artifacts, the
    name and shape of the expected data inputs, and the framework in which
    the model was trained.
    """

    S3Uri: S3Uri
    DataInputConfig: Optional[DataInputConfig]
    Framework: Framework
    FrameworkVersion: Optional[FrameworkVersion]


class CreateCompilationJobRequest(ServiceRequest):
    CompilationJobName: EntityName
    RoleArn: RoleArn
    ModelPackageVersionArn: Optional[ModelPackageArn]
    InputConfig: Optional[InputConfig]
    OutputConfig: OutputConfig
    VpcConfig: Optional[NeoVpcConfig]
    StoppingCondition: StoppingCondition
    Tags: Optional[TagList]


class CreateCompilationJobResponse(TypedDict, total=False):
    CompilationJobArn: CompilationJobArn


class CreateComputeQuotaRequest(ServiceRequest):
    Name: EntityName
    Description: Optional[EntityDescription]
    ClusterArn: ClusterArn
    ComputeQuotaConfig: ComputeQuotaConfig
    ComputeQuotaTarget: ComputeQuotaTarget
    ActivationState: Optional[ActivationState]
    Tags: Optional[TagList]


class CreateComputeQuotaResponse(TypedDict, total=False):
    ComputeQuotaArn: ComputeQuotaArn
    ComputeQuotaId: ComputeQuotaId


class CreateContextRequest(ServiceRequest):
    ContextName: ContextName
    Source: ContextSource
    ContextType: String256
    Description: Optional[ExperimentDescription]
    Properties: Optional[LineageEntityParameters]
    Tags: Optional[TagList]


class CreateContextResponse(TypedDict, total=False):
    ContextArn: Optional[ContextArn]


class MonitoringStoppingCondition(TypedDict, total=False):
    """A time limit for how long the monitoring job is allowed to run before
    stopping.
    """

    MaxRuntimeInSeconds: MonitoringMaxRuntimeInSeconds


class MonitoringNetworkConfig(TypedDict, total=False):
    """The networking configuration for the monitoring job."""

    EnableInterContainerTrafficEncryption: Optional[Boolean]
    EnableNetworkIsolation: Optional[Boolean]
    VpcConfig: Optional[VpcConfig]


class MonitoringClusterConfig(TypedDict, total=False):
    """Configuration for the cluster used to run model monitoring jobs."""

    InstanceCount: ProcessingInstanceCount
    InstanceType: ProcessingInstanceType
    VolumeSizeInGB: ProcessingVolumeSizeInGB
    VolumeKmsKeyId: Optional[KmsKeyId]


class MonitoringResources(TypedDict, total=False):
    """Identifies the resources to deploy for a monitoring job."""

    ClusterConfig: MonitoringClusterConfig


class MonitoringS3Output(TypedDict, total=False):
    """Information about where and how you want to store the results of a
    monitoring job.
    """

    S3Uri: MonitoringS3Uri
    LocalPath: ProcessingLocalPath
    S3UploadMode: Optional[ProcessingS3UploadMode]


class MonitoringOutput(TypedDict, total=False):
    """The output object for a monitoring job."""

    S3Output: MonitoringS3Output


MonitoringOutputs = List[MonitoringOutput]


class MonitoringOutputConfig(TypedDict, total=False):
    """The output configuration for monitoring jobs."""

    MonitoringOutputs: MonitoringOutputs
    KmsKeyId: Optional[KmsKeyId]


class EndpointInput(TypedDict, total=False):
    """Input object for the endpoint"""

    EndpointName: EndpointName
    LocalPath: ProcessingLocalPath
    S3InputMode: Optional[ProcessingS3InputMode]
    S3DataDistributionType: Optional[ProcessingS3DataDistributionType]
    FeaturesAttribute: Optional[String]
    InferenceAttribute: Optional[String]
    ProbabilityAttribute: Optional[String]
    ProbabilityThresholdAttribute: Optional[ProbabilityThresholdAttribute]
    StartTimeOffset: Optional[MonitoringTimeOffsetString]
    EndTimeOffset: Optional[MonitoringTimeOffsetString]
    ExcludeFeaturesAttribute: Optional[ExcludeFeaturesAttribute]


class DataQualityJobInput(TypedDict, total=False):
    """The input for the data quality monitoring job. Currently endpoints are
    supported for input.
    """

    EndpointInput: Optional[EndpointInput]
    BatchTransformInput: Optional[BatchTransformInput]


MonitoringEnvironmentMap = Dict[ProcessingEnvironmentKey, ProcessingEnvironmentValue]
MonitoringContainerArguments = List[ContainerArgument]


class DataQualityAppSpecification(TypedDict, total=False):
    """Information about the container that a data quality monitoring job runs."""

    ImageUri: ImageUri
    ContainerEntrypoint: Optional[ContainerEntrypoint]
    ContainerArguments: Optional[MonitoringContainerArguments]
    RecordPreprocessorSourceUri: Optional[S3Uri]
    PostAnalyticsProcessorSourceUri: Optional[S3Uri]
    Environment: Optional[MonitoringEnvironmentMap]


class MonitoringStatisticsResource(TypedDict, total=False):
    """The statistics resource for a monitoring job."""

    S3Uri: Optional[S3Uri]


class MonitoringConstraintsResource(TypedDict, total=False):
    """The constraints resource for a monitoring job."""

    S3Uri: Optional[S3Uri]


class DataQualityBaselineConfig(TypedDict, total=False):
    """Configuration for monitoring constraints and monitoring statistics.
    These baseline resources are compared against the results of the current
    job from the series of jobs scheduled to collect data periodically.
    """

    BaseliningJobName: Optional[ProcessingJobName]
    ConstraintsResource: Optional[MonitoringConstraintsResource]
    StatisticsResource: Optional[MonitoringStatisticsResource]


class CreateDataQualityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName
    DataQualityBaselineConfig: Optional[DataQualityBaselineConfig]
    DataQualityAppSpecification: DataQualityAppSpecification
    DataQualityJobInput: DataQualityJobInput
    DataQualityJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]
    Tags: Optional[TagList]


class CreateDataQualityJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn


class EdgeOutputConfig(TypedDict, total=False):
    """The output configuration."""

    S3OutputLocation: S3Uri
    KmsKeyId: Optional[KmsKeyId]
    PresetDeploymentType: Optional[EdgePresetDeploymentType]
    PresetDeploymentConfig: Optional[String]


class CreateDeviceFleetRequest(ServiceRequest):
    DeviceFleetName: EntityName
    RoleArn: Optional[RoleArn]
    Description: Optional[DeviceFleetDescription]
    OutputConfig: EdgeOutputConfig
    Tags: Optional[TagList]
    EnableIotRoleAlias: Optional[EnableIotRoleAlias]


class FSxLustreFileSystemConfig(TypedDict, total=False):
    """The settings for assigning a custom Amazon FSx for Lustre file system to
    a user profile or space for an Amazon SageMaker Domain.
    """

    FileSystemId: FileSystemId
    FileSystemPath: Optional[FileSystemPath]


class EFSFileSystemConfig(TypedDict, total=False):
    """The settings for assigning a custom Amazon EFS file system to a user
    profile or space for an Amazon SageMaker AI Domain.
    """

    FileSystemId: FileSystemId
    FileSystemPath: Optional[FileSystemPath]


class CustomFileSystemConfig(TypedDict, total=False):
    """The settings for assigning a custom file system to a user profile or
    space for an Amazon SageMaker AI Domain. Permitted users can access this
    file system in Amazon SageMaker AI Studio.
    """

    EFSFileSystemConfig: Optional[EFSFileSystemConfig]
    FSxLustreFileSystemConfig: Optional[FSxLustreFileSystemConfig]


CustomFileSystemConfigs = List[CustomFileSystemConfig]
Gid = int
Uid = int


class CustomPosixUserConfig(TypedDict, total=False):
    """Details about the POSIX identity that is used for file system
    operations.
    """

    Uid: Uid
    Gid: Gid


class DefaultEbsStorageSettings(TypedDict, total=False):
    """A collection of default EBS storage settings that apply to spaces
    created within a domain or user profile.
    """

    DefaultEbsVolumeSizeInGb: SpaceEbsVolumeSizeInGb
    MaximumEbsVolumeSizeInGb: SpaceEbsVolumeSizeInGb


class DefaultSpaceStorageSettings(TypedDict, total=False):
    """The default storage settings for a space."""

    DefaultEbsStorageSettings: Optional[DefaultEbsStorageSettings]


ExecutionRoleArns = List[RoleArn]


class EmrSettings(TypedDict, total=False):
    """The configuration parameters that specify the IAM roles assumed by the
    execution role of SageMaker (assumable roles) and the cluster instances
    or job execution environments (execution roles or runtime roles) to
    manage and access resources required for running Amazon EMR clusters or
    Amazon EMR Serverless applications.
    """

    AssumableRoleArns: Optional[AssumableRoleArns]
    ExecutionRoleArns: Optional[ExecutionRoleArns]


class JupyterLabAppSettings(TypedDict, total=False):
    """The settings for the JupyterLab application."""

    DefaultResourceSpec: Optional[ResourceSpec]
    CustomImages: Optional[CustomImages]
    LifecycleConfigArns: Optional[LifecycleConfigArns]
    CodeRepositories: Optional[CodeRepositories]
    AppLifecycleManagement: Optional[AppLifecycleManagement]
    EmrSettings: Optional[EmrSettings]
    BuiltInLifecycleConfigArn: Optional[StudioLifecycleConfigArn]


class KernelGatewayAppSettings(TypedDict, total=False):
    """The KernelGateway app settings."""

    DefaultResourceSpec: Optional[ResourceSpec]
    CustomImages: Optional[CustomImages]
    LifecycleConfigArns: Optional[LifecycleConfigArns]


class JupyterServerAppSettings(TypedDict, total=False):
    """The JupyterServer app settings."""

    DefaultResourceSpec: Optional[ResourceSpec]
    LifecycleConfigArns: Optional[LifecycleConfigArns]
    CodeRepositories: Optional[CodeRepositories]


SecurityGroupIds = List[SecurityGroupId]


class DefaultSpaceSettings(TypedDict, total=False):
    """The default settings for shared spaces that users create in the domain.

    SageMaker applies these settings only to shared spaces. It doesn't apply
    them to private spaces.
    """

    ExecutionRole: Optional[RoleArn]
    SecurityGroups: Optional[SecurityGroupIds]
    JupyterServerAppSettings: Optional[JupyterServerAppSettings]
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettings]
    JupyterLabAppSettings: Optional[JupyterLabAppSettings]
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettings]
    CustomPosixUserConfig: Optional[CustomPosixUserConfig]
    CustomFileSystemConfigs: Optional[CustomFileSystemConfigs]


class UnifiedStudioSettings(TypedDict, total=False):
    """The settings that apply to an Amazon SageMaker AI domain when you use it
    in Amazon SageMaker Unified Studio.
    """

    StudioWebPortalAccess: Optional[FeatureStatus]
    DomainAccountId: Optional[AccountId]
    DomainRegion: Optional[RegionName]
    DomainId: Optional[UnifiedStudioDomainId]
    ProjectId: Optional[UnifiedStudioProjectId]
    EnvironmentId: Optional[UnifiedStudioEnvironmentId]
    ProjectS3Path: Optional[S3Uri]
    SingleSignOnApplicationArn: Optional[SingleSignOnApplicationArn]


VpcOnlyTrustedAccounts = List[AccountId]


class DockerSettings(TypedDict, total=False):
    """A collection of settings that configure the domain's Docker interaction."""

    EnableDockerAccess: Optional[FeatureStatus]
    VpcOnlyTrustedAccounts: Optional[VpcOnlyTrustedAccounts]


class RStudioServerProDomainSettings(TypedDict, total=False):
    """A collection of settings that configure the ``RStudioServerPro``
    Domain-level app.
    """

    DomainExecutionRoleArn: RoleArn
    RStudioConnectUrl: Optional[String]
    RStudioPackageManagerUrl: Optional[String]
    DefaultResourceSpec: Optional[ResourceSpec]


DomainSecurityGroupIds = List[SecurityGroupId]


class DomainSettings(TypedDict, total=False):
    """A collection of settings that apply to the ``SageMaker Domain``. These
    settings are specified through the ``CreateDomain`` API call.
    """

    SecurityGroupIds: Optional[DomainSecurityGroupIds]
    RStudioServerProDomainSettings: Optional[RStudioServerProDomainSettings]
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfig]
    DockerSettings: Optional[DockerSettings]
    AmazonQSettings: Optional[AmazonQSettings]
    UnifiedStudioSettings: Optional[UnifiedStudioSettings]


VersionAliasesList = List[ImageVersionAliasPattern]


class HiddenSageMakerImage(TypedDict, total=False):
    """The SageMaker images that are hidden from the Studio user interface. You
    must specify the SageMaker image name and version aliases.
    """

    SageMakerImageName: Optional[SageMakerImageName]
    VersionAliases: Optional[VersionAliasesList]


HiddenSageMakerImageVersionAliasesList = List[HiddenSageMakerImage]
HiddenInstanceTypesList = List[AppInstanceType]
HiddenAppTypesList = List[AppType]
HiddenMlToolsList = List[MlTools]


class StudioWebPortalSettings(TypedDict, total=False):
    """Studio settings. If these settings are applied on a user level, they
    take priority over the settings applied on a domain level.
    """

    HiddenMlTools: Optional[HiddenMlToolsList]
    HiddenAppTypes: Optional[HiddenAppTypesList]
    HiddenInstanceTypes: Optional[HiddenInstanceTypesList]
    HiddenSageMakerImageVersionAliases: Optional[HiddenSageMakerImageVersionAliasesList]


class RSessionAppSettings(TypedDict, total=False):
    """A collection of settings that apply to an ``RSessionGateway`` app."""

    DefaultResourceSpec: Optional[ResourceSpec]
    CustomImages: Optional[CustomImages]


class RStudioServerProAppSettings(TypedDict, total=False):
    """A collection of settings that configure user interaction with the
    ``RStudioServerPro`` app.
    """

    AccessStatus: Optional[RStudioServerProAccessStatus]
    UserGroup: Optional[RStudioServerProUserGroup]


class TensorBoardAppSettings(TypedDict, total=False):
    """The TensorBoard app settings."""

    DefaultResourceSpec: Optional[ResourceSpec]


class SharingSettings(TypedDict, total=False):
    """Specifies options for sharing Amazon SageMaker AI Studio notebooks.
    These settings are specified as part of ``DefaultUserSettings`` when the
    ``CreateDomain`` API is called, and as part of ``UserSettings`` when the
    ``CreateUserProfile`` API is called. When ``SharingSettings`` is not
    specified, notebook sharing isn't allowed.
    """

    NotebookOutputOption: Optional[NotebookOutputOption]
    S3OutputPath: Optional[S3Uri]
    S3KmsKeyId: Optional[KmsKeyId]


class UserSettings(TypedDict, total=False):
    """A collection of settings that apply to users in a domain. These settings
    are specified when the ``CreateUserProfile`` API is called, and as
    ``DefaultUserSettings`` when the ``CreateDomain`` API is called.

    ``SecurityGroups`` is aggregated when specified in both calls. For all
    other settings in ``UserSettings``, the values specified in
    ``CreateUserProfile`` take precedence over those specified in
    ``CreateDomain``.
    """

    ExecutionRole: Optional[RoleArn]
    SecurityGroups: Optional[SecurityGroupIds]
    SharingSettings: Optional[SharingSettings]
    JupyterServerAppSettings: Optional[JupyterServerAppSettings]
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettings]
    TensorBoardAppSettings: Optional[TensorBoardAppSettings]
    RStudioServerProAppSettings: Optional[RStudioServerProAppSettings]
    RSessionAppSettings: Optional[RSessionAppSettings]
    CanvasAppSettings: Optional[CanvasAppSettings]
    CodeEditorAppSettings: Optional[CodeEditorAppSettings]
    JupyterLabAppSettings: Optional[JupyterLabAppSettings]
    SpaceStorageSettings: Optional[DefaultSpaceStorageSettings]
    DefaultLandingUri: Optional[LandingUri]
    StudioWebPortal: Optional[StudioWebPortal]
    CustomPosixUserConfig: Optional[CustomPosixUserConfig]
    CustomFileSystemConfigs: Optional[CustomFileSystemConfigs]
    StudioWebPortalSettings: Optional[StudioWebPortalSettings]
    AutoMountHomeEFS: Optional[AutoMountHomeEFS]


class CreateDomainRequest(ServiceRequest):
    DomainName: DomainName
    AuthMode: AuthMode
    DefaultUserSettings: UserSettings
    DomainSettings: Optional[DomainSettings]
    SubnetIds: Subnets
    VpcId: VpcId
    Tags: Optional[TagList]
    AppNetworkAccessType: Optional[AppNetworkAccessType]
    HomeEfsFileSystemKmsKeyId: Optional[KmsKeyId]
    KmsKeyId: Optional[KmsKeyId]
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagement]
    TagPropagation: Optional[TagPropagation]
    DefaultSpaceSettings: Optional[DefaultSpaceSettings]


class CreateDomainResponse(TypedDict, total=False):
    DomainArn: Optional[DomainArn]
    DomainId: Optional[DomainId]
    Url: Optional[String1024]


class EdgeDeploymentConfig(TypedDict, total=False):
    """Contains information about the configuration of a deployment."""

    FailureHandlingPolicy: FailureHandlingPolicy


DeviceNames = List[DeviceName]


class DeviceSelectionConfig(TypedDict, total=False):
    """Contains information about the configurations of selected devices."""

    DeviceSubsetType: DeviceSubsetType
    Percentage: Optional[Percentage]
    DeviceNames: Optional[DeviceNames]
    DeviceNameContains: Optional[DeviceName]


class DeploymentStage(TypedDict, total=False):
    """Contains information about a stage in an edge deployment plan."""

    StageName: EntityName
    DeviceSelectionConfig: DeviceSelectionConfig
    DeploymentConfig: Optional[EdgeDeploymentConfig]


DeploymentStages = List[DeploymentStage]


class EdgeDeploymentModelConfig(TypedDict, total=False):
    """Contains information about the configuration of a model in a deployment."""

    ModelHandle: EntityName
    EdgePackagingJobName: EntityName


EdgeDeploymentModelConfigs = List[EdgeDeploymentModelConfig]


class CreateEdgeDeploymentPlanRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName
    ModelConfigs: EdgeDeploymentModelConfigs
    DeviceFleetName: EntityName
    Stages: Optional[DeploymentStages]
    Tags: Optional[TagList]


class CreateEdgeDeploymentPlanResponse(TypedDict, total=False):
    EdgeDeploymentPlanArn: EdgeDeploymentPlanArn


class CreateEdgeDeploymentStageRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName
    Stages: DeploymentStages


class CreateEdgePackagingJobRequest(ServiceRequest):
    EdgePackagingJobName: EntityName
    CompilationJobName: EntityName
    ModelName: EntityName
    ModelVersion: EdgeVersion
    RoleArn: RoleArn
    OutputConfig: EdgeOutputConfig
    ResourceKey: Optional[KmsKeyId]
    Tags: Optional[TagList]


class ProductionVariantCapacityReservationConfig(TypedDict, total=False):
    """Settings for the capacity reservation for the compute instances that
    SageMaker AI reserves for an endpoint.
    """

    CapacityReservationPreference: Optional[CapacityReservationPreference]
    MlReservationArn: Optional[MlReservationArn]


class ProductionVariantRoutingConfig(TypedDict, total=False):
    """Settings that control how the endpoint routes incoming traffic to the
    instances that the endpoint hosts.
    """

    RoutingStrategy: RoutingStrategy


class ProductionVariantManagedInstanceScaling(TypedDict, total=False):
    """Settings that control the range in the number of instances that the
    endpoint provisions as it scales up or down to accommodate traffic.
    """

    Status: Optional[ManagedInstanceScalingStatus]
    MinInstanceCount: Optional[ManagedInstanceScalingMinInstanceCount]
    MaxInstanceCount: Optional[ManagedInstanceScalingMaxInstanceCount]


class ProductionVariantServerlessConfig(TypedDict, total=False):
    """Specifies the serverless configuration for an endpoint variant."""

    MemorySizeInMB: ServerlessMemorySizeInMB
    MaxConcurrency: ServerlessMaxConcurrency
    ProvisionedConcurrency: Optional[ServerlessProvisionedConcurrency]


class ProductionVariantCoreDumpConfig(TypedDict, total=False):
    """Specifies configuration for a core dump from the model container when
    the process crashes.
    """

    DestinationS3Uri: DestinationS3Uri
    KmsKeyId: Optional[KmsKeyId]


class ProductionVariant(TypedDict, total=False):
    """Identifies a model that you want to host and the resources chosen to
    deploy for hosting it. If you are deploying multiple models, tell
    SageMaker how to distribute traffic among the models by specifying
    variant weights. For more information on production variants, check
    `Production
    variants <https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html>`__.
    """

    VariantName: VariantName
    ModelName: Optional[ModelName]
    InitialInstanceCount: Optional[InitialTaskCount]
    InstanceType: Optional[ProductionVariantInstanceType]
    InitialVariantWeight: Optional[VariantWeight]
    AcceleratorType: Optional[ProductionVariantAcceleratorType]
    CoreDumpConfig: Optional[ProductionVariantCoreDumpConfig]
    ServerlessConfig: Optional[ProductionVariantServerlessConfig]
    VolumeSizeInGB: Optional[ProductionVariantVolumeSizeInGB]
    ModelDataDownloadTimeoutInSeconds: Optional[ProductionVariantModelDataDownloadTimeoutInSeconds]
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[
        ProductionVariantContainerStartupHealthCheckTimeoutInSeconds
    ]
    EnableSSMAccess: Optional[ProductionVariantSSMAccess]
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScaling]
    RoutingConfig: Optional[ProductionVariantRoutingConfig]
    InferenceAmiVersion: Optional[ProductionVariantInferenceAmiVersion]
    CapacityReservationConfig: Optional[ProductionVariantCapacityReservationConfig]


ProductionVariantList = List[ProductionVariant]


class ExplainerConfig(TypedDict, total=False):
    """A parameter to activate explainers."""

    ClarifyExplainerConfig: Optional[ClarifyExplainerConfig]


class DataCaptureConfig(TypedDict, total=False):
    """Configuration to control how SageMaker AI captures inference data."""

    EnableCapture: Optional[EnableCapture]
    InitialSamplingPercentage: SamplingPercentage
    DestinationS3Uri: DestinationS3Uri
    KmsKeyId: Optional[KmsKeyId]
    CaptureOptions: CaptureOptionList
    CaptureContentTypeHeader: Optional[CaptureContentTypeHeader]


class CreateEndpointConfigInput(ServiceRequest):
    EndpointConfigName: EndpointConfigName
    ProductionVariants: ProductionVariantList
    DataCaptureConfig: Optional[DataCaptureConfig]
    Tags: Optional[TagList]
    KmsKeyId: Optional[KmsKeyId]
    AsyncInferenceConfig: Optional[AsyncInferenceConfig]
    ExplainerConfig: Optional[ExplainerConfig]
    ShadowProductionVariants: Optional[ProductionVariantList]
    ExecutionRoleArn: Optional[RoleArn]
    VpcConfig: Optional[VpcConfig]
    EnableNetworkIsolation: Optional[Boolean]


class CreateEndpointConfigOutput(TypedDict, total=False):
    EndpointConfigArn: EndpointConfigArn


class RollingUpdatePolicy(TypedDict, total=False):
    """Specifies a rolling deployment strategy for updating a SageMaker
    endpoint.
    """

    MaximumBatchSize: CapacitySize
    WaitIntervalInSeconds: WaitIntervalInSeconds
    MaximumExecutionTimeoutInSeconds: Optional[MaximumExecutionTimeoutInSeconds]
    RollbackMaximumBatchSize: Optional[CapacitySize]


class DeploymentConfig(TypedDict, total=False):
    """The deployment configuration for an endpoint, which contains the desired
    deployment strategy and rollback configurations.
    """

    BlueGreenUpdatePolicy: Optional[BlueGreenUpdatePolicy]
    RollingUpdatePolicy: Optional[RollingUpdatePolicy]
    AutoRollbackConfiguration: Optional[AutoRollbackConfig]


class CreateEndpointInput(ServiceRequest):
    EndpointName: EndpointName
    EndpointConfigName: EndpointConfigName
    DeploymentConfig: Optional[DeploymentConfig]
    Tags: Optional[TagList]


class CreateEndpointOutput(TypedDict, total=False):
    EndpointArn: EndpointArn


class CreateExperimentRequest(ServiceRequest):
    ExperimentName: ExperimentEntityName
    DisplayName: Optional[ExperimentEntityName]
    Description: Optional[ExperimentDescription]
    Tags: Optional[TagList]


class CreateExperimentResponse(TypedDict, total=False):
    ExperimentArn: Optional[ExperimentArn]


class ThroughputConfig(TypedDict, total=False):
    """Used to set feature group throughput configuration. There are two modes:
    ``ON_DEMAND`` and ``PROVISIONED``. With on-demand mode, you are charged
    for data reads and writes that your application performs on your feature
    group. You do not need to specify read and write throughput because
    Feature Store accommodates your workloads as they ramp up and down. You
    can switch a feature group to on-demand only once in a 24 hour period.
    With provisioned throughput mode, you specify the read and write
    capacity per second that you expect your application to require, and you
    are billed based on those limits. Exceeding provisioned throughput will
    result in your requests being throttled.

    Note: ``PROVISIONED`` throughput mode is supported only for feature
    groups that are offline-only, or use the
    ```Standard`` <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType>`__
    tier online store.
    """

    ThroughputMode: ThroughputMode
    ProvisionedReadCapacityUnits: Optional[CapacityUnit]
    ProvisionedWriteCapacityUnits: Optional[CapacityUnit]


class DataCatalogConfig(TypedDict, total=False):
    """The meta data of the Glue table which serves as data catalog for the
    ``OfflineStore``.
    """

    TableName: TableName
    Catalog: Catalog
    Database: Database


class S3StorageConfig(TypedDict, total=False):
    """The Amazon Simple Storage (Amazon S3) location and security
    configuration for ``OfflineStore``.
    """

    S3Uri: S3Uri
    KmsKeyId: Optional[KmsKeyId]
    ResolvedOutputS3Uri: Optional[S3Uri]


class OfflineStoreConfig(TypedDict, total=False):
    """The configuration of an ``OfflineStore``.

    Provide an ``OfflineStoreConfig`` in a request to ``CreateFeatureGroup``
    to create an ``OfflineStore``.

    To encrypt an ``OfflineStore`` using at rest data encryption, specify
    Amazon Web Services Key Management Service (KMS) key ID, or
    ``KMSKeyId``, in ``S3StorageConfig``.
    """

    S3StorageConfig: S3StorageConfig
    DisableGlueTableCreation: Optional[Boolean]
    DataCatalogConfig: Optional[DataCatalogConfig]
    TableFormat: Optional[TableFormat]


class TtlDuration(TypedDict, total=False):
    """Time to live duration, where the record is hard deleted after the
    expiration time is reached; ``ExpiresAt`` = ``EventTime`` +
    ``TtlDuration``. For information on HardDelete, see the
    `DeleteRecord <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html>`__
    API in the Amazon SageMaker API Reference guide.
    """

    Unit: Optional[TtlDurationUnit]
    Value: Optional[TtlDurationValue]


class OnlineStoreSecurityConfig(TypedDict, total=False):
    """The security configuration for ``OnlineStore``."""

    KmsKeyId: Optional[KmsKeyId]


class OnlineStoreConfig(TypedDict, total=False):
    """Use this to specify the Amazon Web Services Key Management Service (KMS)
    Key ID, or ``KMSKeyId``, for at rest data encryption. You can turn
    ``OnlineStore`` on or off by specifying the ``EnableOnlineStore`` flag
    at General Assembly.

    The default value is ``False``.
    """

    SecurityConfig: Optional[OnlineStoreSecurityConfig]
    EnableOnlineStore: Optional[Boolean]
    TtlDuration: Optional[TtlDuration]
    StorageType: Optional[StorageType]


class FeatureDefinition(TypedDict, total=False):
    """A list of features. You must include ``FeatureName`` and
    ``FeatureType``. Valid feature ``FeatureType`` s are ``Integral``,
    ``Fractional`` and ``String``.
    """

    FeatureName: FeatureName
    FeatureType: FeatureType
    CollectionType: Optional[CollectionType]
    CollectionConfig: Optional[CollectionConfig]


FeatureDefinitions = List[FeatureDefinition]


class CreateFeatureGroupRequest(ServiceRequest):
    FeatureGroupName: FeatureGroupName
    RecordIdentifierFeatureName: FeatureName
    EventTimeFeatureName: FeatureName
    FeatureDefinitions: FeatureDefinitions
    OnlineStoreConfig: Optional[OnlineStoreConfig]
    OfflineStoreConfig: Optional[OfflineStoreConfig]
    ThroughputConfig: Optional[ThroughputConfig]
    RoleArn: Optional[RoleArn]
    Description: Optional[Description]
    Tags: Optional[TagList]


class CreateFeatureGroupResponse(TypedDict, total=False):
    FeatureGroupArn: FeatureGroupArn


class FlowDefinitionOutputConfig(TypedDict, total=False):
    """Contains information about where human output will be stored."""

    S3OutputPath: S3Uri
    KmsKeyId: Optional[KmsKeyId]


class USD(TypedDict, total=False):
    """Represents an amount of money in United States dollars."""

    Dollars: Optional[Dollars]
    Cents: Optional[Cents]
    TenthFractionsOfACent: Optional[TenthFractionsOfACent]


class PublicWorkforceTaskPrice(TypedDict, total=False):
    """Defines the amount of money paid to an Amazon Mechanical Turk worker for
    each task performed.

    Use one of the following prices for bounding box tasks. Prices are in US
    dollars and should be based on the complexity of the task; the longer it
    takes in your initial testing, the more you should offer.

    -  0.036

    -  0.048

    -  0.060

    -  0.072

    -  0.120

    -  0.240

    -  0.360

    -  0.480

    -  0.600

    -  0.720

    -  0.840

    -  0.960

    -  1.080

    -  1.200

    Use one of the following prices for image classification, text
    classification, and custom tasks. Prices are in US dollars.

    -  0.012

    -  0.024

    -  0.036

    -  0.048

    -  0.060

    -  0.072

    -  0.120

    -  0.240

    -  0.360

    -  0.480

    -  0.600

    -  0.720

    -  0.840

    -  0.960

    -  1.080

    -  1.200

    Use one of the following prices for semantic segmentation tasks. Prices
    are in US dollars.

    -  0.840

    -  0.960

    -  1.080

    -  1.200

    Use one of the following prices for Textract AnalyzeDocument Important
    Form Key Amazon Augmented AI review tasks. Prices are in US dollars.

    -  2.400

    -  2.280

    -  2.160

    -  2.040

    -  1.920

    -  1.800

    -  1.680

    -  1.560

    -  1.440

    -  1.320

    -  1.200

    -  1.080

    -  0.960

    -  0.840

    -  0.720

    -  0.600

    -  0.480

    -  0.360

    -  0.240

    -  0.120

    -  0.072

    -  0.060

    -  0.048

    -  0.036

    -  0.024

    -  0.012

    Use one of the following prices for Rekognition DetectModerationLabels
    Amazon Augmented AI review tasks. Prices are in US dollars.

    -  1.200

    -  1.080

    -  0.960

    -  0.840

    -  0.720

    -  0.600

    -  0.480

    -  0.360

    -  0.240

    -  0.120

    -  0.072

    -  0.060

    -  0.048

    -  0.036

    -  0.024

    -  0.012

    Use one of the following prices for Amazon Augmented AI custom human
    review tasks. Prices are in US dollars.

    -  1.200

    -  1.080

    -  0.960

    -  0.840

    -  0.720

    -  0.600

    -  0.480

    -  0.360

    -  0.240

    -  0.120

    -  0.072

    -  0.060

    -  0.048

    -  0.036

    -  0.024

    -  0.012
    """

    AmountInUsd: Optional[USD]


FlowDefinitionTaskKeywords = List[FlowDefinitionTaskKeyword]


class HumanLoopConfig(TypedDict, total=False):
    """Describes the work to be performed by human workers."""

    WorkteamArn: WorkteamArn
    HumanTaskUiArn: HumanTaskUiArn
    TaskTitle: FlowDefinitionTaskTitle
    TaskDescription: FlowDefinitionTaskDescription
    TaskCount: FlowDefinitionTaskCount
    TaskAvailabilityLifetimeInSeconds: Optional[FlowDefinitionTaskAvailabilityLifetimeInSeconds]
    TaskTimeLimitInSeconds: Optional[FlowDefinitionTaskTimeLimitInSeconds]
    TaskKeywords: Optional[FlowDefinitionTaskKeywords]
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPrice]


class HumanLoopActivationConditionsConfig(TypedDict, total=False):
    """Defines under what conditions SageMaker creates a human loop. Used
    within
    `CreateFlowDefinition <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFlowDefinition.html>`__.
    See
    `HumanLoopActivationConditionsConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanLoopActivationConditionsConfig.html>`__
    for the required format of activation conditions.
    """

    HumanLoopActivationConditions: HumanLoopActivationConditions


class HumanLoopActivationConfig(TypedDict, total=False):
    """Provides information about how and under what conditions SageMaker
    creates a human loop. If ``HumanLoopActivationConfig`` is not given,
    then all requests go to humans.
    """

    HumanLoopActivationConditionsConfig: HumanLoopActivationConditionsConfig


class HumanLoopRequestSource(TypedDict, total=False):
    """Container for configuring the source of human task requests."""

    AwsManagedHumanLoopRequestSource: AwsManagedHumanLoopRequestSource


class CreateFlowDefinitionRequest(ServiceRequest):
    FlowDefinitionName: FlowDefinitionName
    HumanLoopRequestSource: Optional[HumanLoopRequestSource]
    HumanLoopActivationConfig: Optional[HumanLoopActivationConfig]
    HumanLoopConfig: Optional[HumanLoopConfig]
    OutputConfig: FlowDefinitionOutputConfig
    RoleArn: RoleArn
    Tags: Optional[TagList]


class CreateFlowDefinitionResponse(TypedDict, total=False):
    FlowDefinitionArn: FlowDefinitionArn


class CreateHubContentReferenceRequest(ServiceRequest):
    HubName: HubNameOrArn
    SageMakerPublicHubContentArn: SageMakerPublicHubContentArn
    HubContentName: Optional[HubContentName]
    MinVersion: Optional[HubContentVersion]
    Tags: Optional[TagList]


class CreateHubContentReferenceResponse(TypedDict, total=False):
    HubArn: HubArn
    HubContentArn: HubContentArn


class HubS3StorageConfig(TypedDict, total=False):
    """The Amazon S3 storage configuration of a hub."""

    S3OutputPath: Optional[S3OutputPath]


HubSearchKeywordList = List[HubSearchKeyword]


class CreateHubRequest(ServiceRequest):
    HubName: HubName
    HubDescription: HubDescription
    HubDisplayName: Optional[HubDisplayName]
    HubSearchKeywords: Optional[HubSearchKeywordList]
    S3StorageConfig: Optional[HubS3StorageConfig]
    Tags: Optional[TagList]


class CreateHubResponse(TypedDict, total=False):
    HubArn: HubArn


class UiTemplate(TypedDict, total=False):
    """The Liquid template for the worker user interface."""

    Content: TemplateContent


class CreateHumanTaskUiRequest(ServiceRequest):
    HumanTaskUiName: HumanTaskUiName
    UiTemplate: UiTemplate
    Tags: Optional[TagList]


class CreateHumanTaskUiResponse(TypedDict, total=False):
    HumanTaskUiArn: HumanTaskUiArn


class ParentHyperParameterTuningJob(TypedDict, total=False):
    """A previously completed or stopped hyperparameter tuning job to be used
    as a starting point for a new hyperparameter tuning job.
    """

    HyperParameterTuningJobName: Optional[HyperParameterTuningJobName]


ParentHyperParameterTuningJobs = List[ParentHyperParameterTuningJob]


class HyperParameterTuningJobWarmStartConfig(TypedDict, total=False):
    """Specifies the configuration for a hyperparameter tuning job that uses
    one or more previous hyperparameter tuning jobs as a starting point. The
    results of previous tuning jobs are used to inform which combinations of
    hyperparameters to search over in the new tuning job.

    All training jobs launched by the new hyperparameter tuning job are
    evaluated by using the objective metric, and the training job that
    performs the best is compared to the best training jobs from the parent
    tuning jobs. From these, the training job that performs the best as
    measured by the objective metric is returned as the overall best
    training job.

    All training jobs launched by parent hyperparameter tuning jobs and the
    new hyperparameter tuning jobs count against the limit of training jobs
    for the tuning job.
    """

    ParentHyperParameterTuningJobs: ParentHyperParameterTuningJobs
    WarmStartType: HyperParameterTuningJobWarmStartType


HyperParameterTrainingJobEnvironmentMap = Dict[
    HyperParameterTrainingJobEnvironmentKey, HyperParameterTrainingJobEnvironmentValue
]


class RetryStrategy(TypedDict, total=False):
    """The retry strategy to use when a training job fails due to an
    ``InternalServerError``. ``RetryStrategy`` is specified as part of the
    ``CreateTrainingJob`` and ``CreateHyperParameterTuningJob`` requests.
    You can add the ``StoppingCondition`` parameter to the request to limit
    the training time for the complete job.
    """

    MaximumRetryAttempts: MaximumRetryAttempts


class HyperParameterTuningInstanceConfig(TypedDict, total=False):
    """The configuration for hyperparameter tuning resources for use in
    training jobs launched by the tuning job. These resources include
    compute instances and storage volumes. Specify one or more compute
    instance configurations and allocation strategies to select resources
    (optional).
    """

    InstanceType: TrainingInstanceType
    InstanceCount: TrainingInstanceCount
    VolumeSizeInGB: VolumeSizeInGB


HyperParameterTuningInstanceConfigs = List[HyperParameterTuningInstanceConfig]


class HyperParameterTuningResourceConfig(TypedDict, total=False):
    """The configuration of resources, including compute instances and storage
    volumes for use in training jobs launched by hyperparameter tuning jobs.
    ``HyperParameterTuningResourceConfig`` is similar to ``ResourceConfig``,
    but has the additional ``InstanceConfigs`` and ``AllocationStrategy``
    fields to allow for flexible instance management. Specify one or more
    instance types, count, and the allocation strategy for instance
    selection.

    ``HyperParameterTuningResourceConfig`` supports the capabilities of
    ``ResourceConfig`` with the exception of ``KeepAlivePeriodInSeconds``.
    Hyperparameter tuning jobs use warm pools by default, which reuse
    clusters between training jobs.
    """

    InstanceType: Optional[TrainingInstanceType]
    InstanceCount: Optional[TrainingInstanceCount]
    VolumeSizeInGB: Optional[OptionalVolumeSizeInGB]
    VolumeKmsKeyId: Optional[KmsKeyId]
    AllocationStrategy: Optional[HyperParameterTuningAllocationStrategy]
    InstanceConfigs: Optional[HyperParameterTuningInstanceConfigs]


class HyperParameterAlgorithmSpecification(TypedDict, total=False):
    """Specifies which training algorithm to use for training jobs that a
    hyperparameter tuning job launches and the metrics to monitor.
    """

    TrainingImage: Optional[AlgorithmImage]
    TrainingInputMode: TrainingInputMode
    AlgorithmName: Optional[ArnOrName]
    MetricDefinitions: Optional[MetricDefinitionList]


class IntegerParameterRange(TypedDict, total=False):
    """For a hyperparameter of the integer type, specifies the range that a
    hyperparameter tuning job searches.
    """

    Name: ParameterKey
    MinValue: ParameterValue
    MaxValue: ParameterValue
    ScalingType: Optional[HyperParameterScalingType]


IntegerParameterRanges = List[IntegerParameterRange]


class ParameterRanges(TypedDict, total=False):
    """Specifies ranges of integer, continuous, and categorical hyperparameters
    that a hyperparameter tuning job searches. The hyperparameter tuning job
    launches training jobs with hyperparameter values within these ranges to
    find the combination of values that result in the training job with the
    best performance as measured by the objective metric of the
    hyperparameter tuning job.

    The maximum number of items specified for ``Array Members`` refers to
    the maximum number of hyperparameters for each range and also the
    maximum for the hyperparameter tuning job itself. That is, the sum of
    the number of hyperparameters for all the ranges can't exceed the
    maximum number specified.
    """

    IntegerParameterRanges: Optional[IntegerParameterRanges]
    ContinuousParameterRanges: Optional[ContinuousParameterRanges]
    CategoricalParameterRanges: Optional[CategoricalParameterRanges]
    AutoParameters: Optional[AutoParameters]


class HyperParameterTrainingJobDefinition(TypedDict, total=False):
    """Defines the training jobs launched by a hyperparameter tuning job."""

    DefinitionName: Optional[HyperParameterTrainingJobDefinitionName]
    TuningObjective: Optional[HyperParameterTuningJobObjective]
    HyperParameterRanges: Optional[ParameterRanges]
    StaticHyperParameters: Optional[HyperParameters]
    AlgorithmSpecification: HyperParameterAlgorithmSpecification
    RoleArn: RoleArn
    InputDataConfig: Optional[InputDataConfig]
    VpcConfig: Optional[VpcConfig]
    OutputDataConfig: OutputDataConfig
    ResourceConfig: Optional[ResourceConfig]
    HyperParameterTuningResourceConfig: Optional[HyperParameterTuningResourceConfig]
    StoppingCondition: StoppingCondition
    EnableNetworkIsolation: Optional[Boolean]
    EnableInterContainerTrafficEncryption: Optional[Boolean]
    EnableManagedSpotTraining: Optional[Boolean]
    CheckpointConfig: Optional[CheckpointConfig]
    RetryStrategy: Optional[RetryStrategy]
    Environment: Optional[HyperParameterTrainingJobEnvironmentMap]


HyperParameterTrainingJobDefinitions = List[HyperParameterTrainingJobDefinition]


class TuningJobCompletionCriteria(TypedDict, total=False):
    """The job completion criteria."""

    TargetObjectiveMetricValue: Optional[TargetObjectiveMetricValue]
    BestObjectiveNotImproving: Optional[BestObjectiveNotImproving]
    ConvergenceDetected: Optional[ConvergenceDetected]


class ResourceLimits(TypedDict, total=False):
    """Specifies the maximum number of training jobs and parallel training jobs
    that a hyperparameter tuning job can launch.
    """

    MaxNumberOfTrainingJobs: Optional[MaxNumberOfTrainingJobs]
    MaxParallelTrainingJobs: MaxParallelTrainingJobs
    MaxRuntimeInSeconds: Optional[HyperParameterTuningMaxRuntimeInSeconds]


class HyperbandStrategyConfig(TypedDict, total=False):
    """The configuration for ``Hyperband``, a multi-fidelity based
    hyperparameter tuning strategy. ``Hyperband`` uses the final and
    intermediate results of a training job to dynamically allocate resources
    to utilized hyperparameter configurations while automatically stopping
    under-performing configurations. This parameter should be provided only
    if ``Hyperband`` is selected as the ``StrategyConfig`` under the
    ``HyperParameterTuningJobConfig`` API.
    """

    MinResource: Optional[HyperbandStrategyMinResource]
    MaxResource: Optional[HyperbandStrategyMaxResource]


class HyperParameterTuningJobStrategyConfig(TypedDict, total=False):
    """The configuration for a training job launched by a hyperparameter tuning
    job. Choose ``Bayesian`` for Bayesian optimization, and ``Random`` for
    random search optimization. For more advanced use cases, use
    ``Hyperband``, which evaluates objective metrics for training jobs after
    every epoch. For more information about strategies, see `How
    Hyperparameter Tuning
    Works <https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html>`__.
    """

    HyperbandStrategyConfig: Optional[HyperbandStrategyConfig]


class HyperParameterTuningJobConfig(TypedDict, total=False):
    """Configures a hyperparameter tuning job."""

    Strategy: HyperParameterTuningJobStrategyType
    StrategyConfig: Optional[HyperParameterTuningJobStrategyConfig]
    HyperParameterTuningJobObjective: Optional[HyperParameterTuningJobObjective]
    ResourceLimits: ResourceLimits
    ParameterRanges: Optional[ParameterRanges]
    TrainingJobEarlyStoppingType: Optional[TrainingJobEarlyStoppingType]
    TuningJobCompletionCriteria: Optional[TuningJobCompletionCriteria]
    RandomSeed: Optional[RandomSeed]


class CreateHyperParameterTuningJobRequest(ServiceRequest):
    HyperParameterTuningJobName: HyperParameterTuningJobName
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfig
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinition]
    TrainingJobDefinitions: Optional[HyperParameterTrainingJobDefinitions]
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfig]
    Tags: Optional[TagList]
    Autotune: Optional[Autotune]


class CreateHyperParameterTuningJobResponse(TypedDict, total=False):
    HyperParameterTuningJobArn: HyperParameterTuningJobArn


class CreateImageRequest(ServiceRequest):
    Description: Optional[ImageDescription]
    DisplayName: Optional[ImageDisplayName]
    ImageName: ImageName
    RoleArn: RoleArn
    Tags: Optional[TagList]


class CreateImageResponse(TypedDict, total=False):
    ImageArn: Optional[ImageArn]


SageMakerImageVersionAliases = List[SageMakerImageVersionAlias]


class CreateImageVersionRequest(ServiceRequest):
    BaseImage: ImageBaseImage
    ClientToken: ClientToken
    ImageName: ImageName
    Aliases: Optional[SageMakerImageVersionAliases]
    VendorGuidance: Optional[VendorGuidance]
    JobType: Optional[JobType]
    MLFramework: Optional[MLFramework]
    ProgrammingLang: Optional[ProgrammingLang]
    Processor: Optional[Processor]
    Horovod: Optional[Horovod]
    ReleaseNotes: Optional[ReleaseNotes]


class CreateImageVersionResponse(TypedDict, total=False):
    ImageVersionArn: Optional[ImageVersionArn]


class InferenceComponentRuntimeConfig(TypedDict, total=False):
    """Runtime settings for a model that is deployed with an inference
    component.
    """

    CopyCount: InferenceComponentCopyCount


class InferenceComponentComputeResourceRequirements(TypedDict, total=False):
    """Defines the compute resources to allocate to run a model, plus any
    adapter models, that you assign to an inference component. These
    resources include CPU cores, accelerators, and memory.
    """

    NumberOfCpuCoresRequired: Optional[NumberOfCpuCores]
    NumberOfAcceleratorDevicesRequired: Optional[NumberOfAcceleratorDevices]
    MinMemoryRequiredInMb: MemoryInMb
    MaxMemoryRequiredInMb: Optional[MemoryInMb]


class InferenceComponentStartupParameters(TypedDict, total=False):
    """Settings that take effect while the model container starts up."""

    ModelDataDownloadTimeoutInSeconds: Optional[ProductionVariantModelDataDownloadTimeoutInSeconds]
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[
        ProductionVariantContainerStartupHealthCheckTimeoutInSeconds
    ]


class InferenceComponentContainerSpecification(TypedDict, total=False):
    """Defines a container that provides the runtime environment for a model
    that you deploy with an inference component.
    """

    Image: Optional[ContainerImage]
    ArtifactUrl: Optional[Url]
    Environment: Optional[EnvironmentMap]


class InferenceComponentSpecification(TypedDict, total=False):
    """Details about the resources to deploy with this inference component,
    including the model, container, and compute resources.
    """

    ModelName: Optional[ModelName]
    Container: Optional[InferenceComponentContainerSpecification]
    StartupParameters: Optional[InferenceComponentStartupParameters]
    ComputeResourceRequirements: Optional[InferenceComponentComputeResourceRequirements]
    BaseInferenceComponentName: Optional[InferenceComponentName]


class CreateInferenceComponentInput(ServiceRequest):
    InferenceComponentName: InferenceComponentName
    EndpointName: EndpointName
    VariantName: Optional[VariantName]
    Specification: InferenceComponentSpecification
    RuntimeConfig: Optional[InferenceComponentRuntimeConfig]
    Tags: Optional[TagList]


class CreateInferenceComponentOutput(TypedDict, total=False):
    InferenceComponentArn: InferenceComponentArn


class ShadowModelVariantConfig(TypedDict, total=False):
    """The name and sampling percentage of a shadow variant."""

    ShadowModelVariantName: ModelVariantName
    SamplingPercentage: Percentage


ShadowModelVariantConfigList = List[ShadowModelVariantConfig]


class ShadowModeConfig(TypedDict, total=False):
    """The configuration of ``ShadowMode`` inference experiment type, which
    specifies a production variant to take all the inference requests, and a
    shadow variant to which Amazon SageMaker replicates a percentage of the
    inference requests. For the shadow variant it also specifies the
    percentage of requests that Amazon SageMaker replicates.
    """

    SourceModelVariantName: ModelVariantName
    ShadowModelVariants: ShadowModelVariantConfigList


class InferenceExperimentDataStorageConfig(TypedDict, total=False):
    """The Amazon S3 location and configuration for storing inference request
    and response data.
    """

    Destination: DestinationS3Uri
    KmsKey: Optional[KmsKeyId]
    ContentType: Optional[CaptureContentTypeHeader]


class RealTimeInferenceConfig(TypedDict, total=False):
    """The infrastructure configuration for deploying the model to a real-time
    inference endpoint.
    """

    InstanceType: InstanceType
    InstanceCount: TaskCount


class ModelInfrastructureConfig(TypedDict, total=False):
    """The configuration for the infrastructure that the model will be deployed
    to.
    """

    InfrastructureType: ModelInfrastructureType
    RealTimeInferenceConfig: RealTimeInferenceConfig


class ModelVariantConfig(TypedDict, total=False):
    """Contains information about the deployment options of a model."""

    ModelName: ModelName
    VariantName: ModelVariantName
    InfrastructureConfig: ModelInfrastructureConfig


ModelVariantConfigList = List[ModelVariantConfig]


class InferenceExperimentSchedule(TypedDict, total=False):
    """The start and end times of an inference experiment.

    The maximum duration that you can set for an inference experiment is 30
    days.
    """

    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]


class CreateInferenceExperimentRequest(ServiceRequest):
    Name: InferenceExperimentName
    Type: InferenceExperimentType
    Schedule: Optional[InferenceExperimentSchedule]
    Description: Optional[InferenceExperimentDescription]
    RoleArn: RoleArn
    EndpointName: EndpointName
    ModelVariants: ModelVariantConfigList
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfig]
    ShadowModeConfig: ShadowModeConfig
    KmsKey: Optional[KmsKeyId]
    Tags: Optional[TagList]


class CreateInferenceExperimentResponse(TypedDict, total=False):
    InferenceExperimentArn: InferenceExperimentArn


class RecommendationJobCompiledOutputConfig(TypedDict, total=False):
    """Provides information about the output configuration for the compiled
    model.
    """

    S3OutputUri: Optional[S3Uri]


class RecommendationJobOutputConfig(TypedDict, total=False):
    """Provides information about the output configuration for the compiled
    model.
    """

    KmsKeyId: Optional[KmsKeyId]
    CompiledOutputConfig: Optional[RecommendationJobCompiledOutputConfig]


class ModelLatencyThreshold(TypedDict, total=False):
    """The model latency threshold."""

    Percentile: Optional[String64]
    ValueInMilliseconds: Optional[Integer]


ModelLatencyThresholds = List[ModelLatencyThreshold]


class RecommendationJobStoppingConditions(TypedDict, total=False):
    """Specifies conditions for stopping a job. When a job reaches a stopping
    condition limit, SageMaker ends the job.
    """

    MaxInvocations: Optional[Integer]
    ModelLatencyThresholds: Optional[ModelLatencyThresholds]
    FlatInvocations: Optional[FlatInvocations]


RecommendationJobVpcSubnets = List[RecommendationJobVpcSubnetId]
RecommendationJobVpcSecurityGroupIds = List[RecommendationJobVpcSecurityGroupId]


class RecommendationJobVpcConfig(TypedDict, total=False):
    """Inference Recommender provisions SageMaker endpoints with access to VPC
    in the inference recommendation job.
    """

    SecurityGroupIds: RecommendationJobVpcSecurityGroupIds
    Subnets: RecommendationJobVpcSubnets


class EndpointInfo(TypedDict, total=False):
    """Details about a customer endpoint that was compared in an Inference
    Recommender job.
    """

    EndpointName: Optional[EndpointName]


Endpoints = List[EndpointInfo]
RecommendationJobSupportedResponseMIMETypes = List[RecommendationJobSupportedResponseMIMEType]
RecommendationJobSupportedInstanceTypes = List[String]
RecommendationJobSupportedContentTypes = List[RecommendationJobSupportedContentType]


class RecommendationJobPayloadConfig(TypedDict, total=False):
    """The configuration for the payload for a recommendation job."""

    SamplePayloadUrl: Optional[S3Uri]
    SupportedContentTypes: Optional[RecommendationJobSupportedContentTypes]


class RecommendationJobContainerConfig(TypedDict, total=False):
    """Specifies mandatory fields for running an Inference Recommender job
    directly in the
    `CreateInferenceRecommendationsJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html>`__
    API. The fields specified in ``ContainerConfig`` override the
    corresponding fields in the model package. Use ``ContainerConfig`` if
    you want to specify these fields for the recommendation job but don't
    want to edit them in your model package.
    """

    Domain: Optional[String]
    Task: Optional[String]
    Framework: Optional[String]
    FrameworkVersion: Optional[RecommendationJobFrameworkVersion]
    PayloadConfig: Optional[RecommendationJobPayloadConfig]
    NearestModelName: Optional[String]
    SupportedInstanceTypes: Optional[RecommendationJobSupportedInstanceTypes]
    SupportedEndpointType: Optional[RecommendationJobSupportedEndpointType]
    DataInputConfig: Optional[RecommendationJobDataInputConfig]
    SupportedResponseMIMETypes: Optional[RecommendationJobSupportedResponseMIMETypes]


class EnvironmentParameterRanges(TypedDict, total=False):
    """Specifies the range of environment parameters"""

    CategoricalParameterRanges: Optional[CategoricalParameters]


class EndpointInputConfiguration(TypedDict, total=False):
    """The endpoint configuration for the load test."""

    InstanceType: Optional[ProductionVariantInstanceType]
    ServerlessConfig: Optional[ProductionVariantServerlessConfig]
    InferenceSpecificationName: Optional[InferenceSpecificationName]
    EnvironmentParameterRanges: Optional[EnvironmentParameterRanges]


EndpointInputConfigurations = List[EndpointInputConfiguration]


class RecommendationJobResourceLimit(TypedDict, total=False):
    """Specifies the maximum number of jobs that can run in parallel and the
    maximum number of jobs that can run.
    """

    MaxNumberOfTests: Optional[MaxNumberOfTests]
    MaxParallelOfTests: Optional[MaxParallelOfTests]


class Stairs(TypedDict, total=False):
    """Defines the stairs traffic pattern for an Inference Recommender load
    test. This pattern type consists of multiple steps where the number of
    users increases at each step.

    Specify either the stairs or phases traffic pattern.
    """

    DurationInSeconds: Optional[TrafficDurationInSeconds]
    NumberOfSteps: Optional[NumberOfSteps]
    UsersPerStep: Optional[UsersPerStep]


class Phase(TypedDict, total=False):
    """Defines the traffic pattern."""

    InitialNumberOfUsers: Optional[InitialNumberOfUsers]
    SpawnRate: Optional[SpawnRate]
    DurationInSeconds: Optional[TrafficDurationInSeconds]


Phases = List[Phase]


class TrafficPattern(TypedDict, total=False):
    """Defines the traffic pattern of the load test."""

    TrafficType: Optional[TrafficType]
    Phases: Optional[Phases]
    Stairs: Optional[Stairs]


class RecommendationJobInputConfig(TypedDict, total=False):
    """The input configuration of the recommendation job."""

    ModelPackageVersionArn: Optional[ModelPackageArn]
    ModelName: Optional[ModelName]
    JobDurationInSeconds: Optional[JobDurationInSeconds]
    TrafficPattern: Optional[TrafficPattern]
    ResourceLimit: Optional[RecommendationJobResourceLimit]
    EndpointConfigurations: Optional[EndpointInputConfigurations]
    VolumeKmsKeyId: Optional[KmsKeyId]
    ContainerConfig: Optional[RecommendationJobContainerConfig]
    Endpoints: Optional[Endpoints]
    VpcConfig: Optional[RecommendationJobVpcConfig]


class CreateInferenceRecommendationsJobRequest(ServiceRequest):
    JobName: RecommendationJobName
    JobType: RecommendationJobType
    RoleArn: RoleArn
    InputConfig: RecommendationJobInputConfig
    JobDescription: Optional[RecommendationJobDescription]
    StoppingConditions: Optional[RecommendationJobStoppingConditions]
    OutputConfig: Optional[RecommendationJobOutputConfig]
    Tags: Optional[TagList]


class CreateInferenceRecommendationsJobResponse(TypedDict, total=False):
    JobArn: RecommendationJobArn


TaskKeywords = List[TaskKeyword]


class UiConfig(TypedDict, total=False):
    """Provided configuration information for the worker UI for a labeling job.
    Provide either ``HumanTaskUiArn`` or ``UiTemplateS3Uri``.

    For named entity recognition, 3D point cloud and video frame labeling
    jobs, use ``HumanTaskUiArn``.

    For all other Ground Truth built-in task types and custom task types,
    use ``UiTemplateS3Uri`` to specify the location of a worker task
    template in Amazon S3.
    """

    UiTemplateS3Uri: Optional[S3Uri]
    HumanTaskUiArn: Optional[HumanTaskUiArn]


class HumanTaskConfig(TypedDict, total=False):
    """Information required for human workers to complete a labeling task."""

    WorkteamArn: WorkteamArn
    UiConfig: UiConfig
    PreHumanTaskLambdaArn: Optional[LambdaFunctionArn]
    TaskKeywords: Optional[TaskKeywords]
    TaskTitle: TaskTitle
    TaskDescription: TaskDescription
    NumberOfHumanWorkersPerDataObject: NumberOfHumanWorkersPerDataObject
    TaskTimeLimitInSeconds: TaskTimeLimitInSeconds
    TaskAvailabilityLifetimeInSeconds: Optional[TaskAvailabilityLifetimeInSeconds]
    MaxConcurrentTaskCount: Optional[MaxConcurrentTaskCount]
    AnnotationConsolidationConfig: Optional[AnnotationConsolidationConfig]
    PublicWorkforceTaskPrice: Optional[PublicWorkforceTaskPrice]


class LabelingJobResourceConfig(TypedDict, total=False):
    """Configure encryption on the storage volume attached to the ML compute
    instance used to run automated data labeling model training and
    inference.
    """

    VolumeKmsKeyId: Optional[KmsKeyId]
    VpcConfig: Optional[VpcConfig]


class LabelingJobAlgorithmsConfig(TypedDict, total=False):
    """Provides configuration information for auto-labeling of your data
    objects. A ``LabelingJobAlgorithmsConfig`` object must be supplied in
    order to use auto-labeling.
    """

    LabelingJobAlgorithmSpecificationArn: LabelingJobAlgorithmSpecificationArn
    InitialActiveLearningModelArn: Optional[ModelArn]
    LabelingJobResourceConfig: Optional[LabelingJobResourceConfig]


class LabelingJobStoppingConditions(TypedDict, total=False):
    """A set of conditions for stopping a labeling job. If any of the
    conditions are met, the job is automatically stopped. You can use these
    conditions to control the cost of data labeling.

    Labeling jobs fail after 30 days with an appropriate client error
    message.
    """

    MaxHumanLabeledObjectCount: Optional[MaxHumanLabeledObjectCount]
    MaxPercentageOfInputDatasetLabeled: Optional[MaxPercentageOfInputDatasetLabeled]


class LabelingJobOutputConfig(TypedDict, total=False):
    """Output configuration information for a labeling job."""

    S3OutputPath: S3Uri
    KmsKeyId: Optional[KmsKeyId]
    SnsTopicArn: Optional[SnsTopicArn]


class LabelingJobDataAttributes(TypedDict, total=False):
    """Attributes of the data specified by the customer. Use these to describe
    the data to be labeled.
    """

    ContentClassifiers: Optional[ContentClassifiers]


class LabelingJobSnsDataSource(TypedDict, total=False):
    """An Amazon SNS data source used for streaming labeling jobs."""

    SnsTopicArn: SnsTopicArn


class LabelingJobS3DataSource(TypedDict, total=False):
    """The Amazon S3 location of the input data objects."""

    ManifestS3Uri: S3Uri


class LabelingJobDataSource(TypedDict, total=False):
    """Provides information about the location of input data.

    You must specify at least one of the following: ``S3DataSource`` or
    ``SnsDataSource``.

    Use ``SnsDataSource`` to specify an SNS input topic for a streaming
    labeling job. If you do not specify and SNS input topic ARN, Ground
    Truth will create a one-time labeling job.

    Use ``S3DataSource`` to specify an input manifest file for both
    streaming and one-time labeling jobs. Adding an ``S3DataSource`` is
    optional if you use ``SnsDataSource`` to create a streaming labeling
    job.
    """

    S3DataSource: Optional[LabelingJobS3DataSource]
    SnsDataSource: Optional[LabelingJobSnsDataSource]


class LabelingJobInputConfig(TypedDict, total=False):
    """Input configuration information for a labeling job."""

    DataSource: LabelingJobDataSource
    DataAttributes: Optional[LabelingJobDataAttributes]


class CreateLabelingJobRequest(ServiceRequest):
    LabelingJobName: LabelingJobName
    LabelAttributeName: LabelAttributeName
    InputConfig: LabelingJobInputConfig
    OutputConfig: LabelingJobOutputConfig
    RoleArn: RoleArn
    LabelCategoryConfigS3Uri: Optional[S3Uri]
    StoppingConditions: Optional[LabelingJobStoppingConditions]
    LabelingJobAlgorithmsConfig: Optional[LabelingJobAlgorithmsConfig]
    HumanTaskConfig: HumanTaskConfig
    Tags: Optional[TagList]


class CreateLabelingJobResponse(TypedDict, total=False):
    LabelingJobArn: LabelingJobArn


class CreateMlflowTrackingServerRequest(ServiceRequest):
    TrackingServerName: TrackingServerName
    ArtifactStoreUri: S3Uri
    TrackingServerSize: Optional[TrackingServerSize]
    MlflowVersion: Optional[MlflowVersion]
    RoleArn: RoleArn
    AutomaticModelRegistration: Optional[Boolean]
    WeeklyMaintenanceWindowStart: Optional[WeeklyMaintenanceWindowStart]
    Tags: Optional[TagList]


class CreateMlflowTrackingServerResponse(TypedDict, total=False):
    TrackingServerArn: Optional[TrackingServerArn]


class MonitoringGroundTruthS3Input(TypedDict, total=False):
    """The ground truth labels for the dataset used for the monitoring job."""

    S3Uri: Optional[MonitoringS3Uri]


class ModelBiasJobInput(TypedDict, total=False):
    """Inputs for the model bias job."""

    EndpointInput: Optional[EndpointInput]
    BatchTransformInput: Optional[BatchTransformInput]
    GroundTruthS3Input: MonitoringGroundTruthS3Input


class ModelBiasAppSpecification(TypedDict, total=False):
    """Docker container image configuration object for the model bias job."""

    ImageUri: ImageUri
    ConfigUri: S3Uri
    Environment: Optional[MonitoringEnvironmentMap]


class ModelBiasBaselineConfig(TypedDict, total=False):
    """The configuration for a baseline model bias job."""

    BaseliningJobName: Optional[ProcessingJobName]
    ConstraintsResource: Optional[MonitoringConstraintsResource]


class CreateModelBiasJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName
    ModelBiasBaselineConfig: Optional[ModelBiasBaselineConfig]
    ModelBiasAppSpecification: ModelBiasAppSpecification
    ModelBiasJobInput: ModelBiasJobInput
    ModelBiasJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]
    Tags: Optional[TagList]


class CreateModelBiasJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn


class ModelCardExportOutputConfig(TypedDict, total=False):
    """Configure the export output details for an Amazon SageMaker Model Card."""

    S3OutputPath: S3Uri


class CreateModelCardExportJobRequest(ServiceRequest):
    ModelCardName: ModelCardNameOrArn
    ModelCardVersion: Optional[Integer]
    ModelCardExportJobName: EntityName
    OutputConfig: ModelCardExportOutputConfig


class CreateModelCardExportJobResponse(TypedDict, total=False):
    ModelCardExportJobArn: ModelCardExportJobArn


class ModelCardSecurityConfig(TypedDict, total=False):
    """Configure the security settings to protect model card data."""

    KmsKeyId: Optional[KmsKeyId]


class CreateModelCardRequest(ServiceRequest):
    ModelCardName: EntityName
    SecurityConfig: Optional[ModelCardSecurityConfig]
    Content: ModelCardContent
    ModelCardStatus: ModelCardStatus
    Tags: Optional[TagList]


class CreateModelCardResponse(TypedDict, total=False):
    ModelCardArn: ModelCardArn


class ModelExplainabilityJobInput(TypedDict, total=False):
    """Inputs for the model explainability job."""

    EndpointInput: Optional[EndpointInput]
    BatchTransformInput: Optional[BatchTransformInput]


class ModelExplainabilityAppSpecification(TypedDict, total=False):
    """Docker container image configuration object for the model explainability
    job.
    """

    ImageUri: ImageUri
    ConfigUri: S3Uri
    Environment: Optional[MonitoringEnvironmentMap]


class ModelExplainabilityBaselineConfig(TypedDict, total=False):
    """The configuration for a baseline model explainability job."""

    BaseliningJobName: Optional[ProcessingJobName]
    ConstraintsResource: Optional[MonitoringConstraintsResource]


class CreateModelExplainabilityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName
    ModelExplainabilityBaselineConfig: Optional[ModelExplainabilityBaselineConfig]
    ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecification
    ModelExplainabilityJobInput: ModelExplainabilityJobInput
    ModelExplainabilityJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]
    Tags: Optional[TagList]


class CreateModelExplainabilityJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn


class InferenceExecutionConfig(TypedDict, total=False):
    """Specifies details about how containers in a multi-container endpoint are
    run.
    """

    Mode: InferenceExecutionMode


class CreateModelInput(ServiceRequest):
    ModelName: ModelName
    PrimaryContainer: Optional[ContainerDefinition]
    Containers: Optional[ContainerDefinitionList]
    InferenceExecutionConfig: Optional[InferenceExecutionConfig]
    ExecutionRoleArn: Optional[RoleArn]
    Tags: Optional[TagList]
    VpcConfig: Optional[VpcConfig]
    EnableNetworkIsolation: Optional[Boolean]


class CreateModelOutput(TypedDict, total=False):
    ModelArn: ModelArn


class CreateModelPackageGroupInput(ServiceRequest):
    ModelPackageGroupName: EntityName
    ModelPackageGroupDescription: Optional[EntityDescription]
    Tags: Optional[TagList]


class CreateModelPackageGroupOutput(TypedDict, total=False):
    ModelPackageGroupArn: ModelPackageGroupArn


class ModelLifeCycle(TypedDict, total=False):
    """A structure describing the current state of the model in its life cycle."""

    Stage: EntityName
    StageStatus: EntityName
    StageDescription: Optional[StageDescription]


class ModelPackageModelCard(TypedDict, total=False):
    """The model card associated with the model package. Since
    ``ModelPackageModelCard`` is tied to a model package, it is a specific
    usage of a model card and its schema is simplified compared to the
    schema of ``ModelCard``. The ``ModelPackageModelCard`` schema does not
    include ``model_package_details``, and ``model_overview`` is composed of
    the ``model_creator`` and ``model_artifact`` properties. For more
    information about the model package model card schema, see `Model
    package model card
    schema <https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema>`__.
    For more information about the model card associated with the model
    package, see `View the Details of a Model
    Version <https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html>`__.
    """

    ModelCardContent: Optional[ModelCardContent]
    ModelCardStatus: Optional[ModelCardStatus]


class ModelPackageSecurityConfig(TypedDict, total=False):
    """An optional Key Management Service key to encrypt, decrypt, and
    re-encrypt model package information for regulated workloads with highly
    sensitive data.
    """

    KmsKeyId: KmsKeyId


class DriftCheckModelDataQuality(TypedDict, total=False):
    """Represents the drift check data quality baselines that can be used when
    the model monitor is set using the model package.
    """

    Statistics: Optional[MetricsSource]
    Constraints: Optional[MetricsSource]


class DriftCheckModelQuality(TypedDict, total=False):
    """Represents the drift check model quality baselines that can be used when
    the model monitor is set using the model package.
    """

    Statistics: Optional[MetricsSource]
    Constraints: Optional[MetricsSource]


class FileSource(TypedDict, total=False):
    """Contains details regarding the file source."""

    ContentType: Optional[ContentType]
    ContentDigest: Optional[ContentDigest]
    S3Uri: S3Uri


class DriftCheckExplainability(TypedDict, total=False):
    """Represents the drift check explainability baselines that can be used
    when the model monitor is set using the model package.
    """

    Constraints: Optional[MetricsSource]
    ConfigFile: Optional[FileSource]


class DriftCheckBias(TypedDict, total=False):
    """Represents the drift check bias baselines that can be used when the
    model monitor is set using the model package.
    """

    ConfigFile: Optional[FileSource]
    PreTrainingConstraints: Optional[MetricsSource]
    PostTrainingConstraints: Optional[MetricsSource]


class DriftCheckBaselines(TypedDict, total=False):
    """Represents the drift check baselines that can be used when the model
    monitor is set using the model package.
    """

    Bias: Optional[DriftCheckBias]
    Explainability: Optional[DriftCheckExplainability]
    ModelQuality: Optional[DriftCheckModelQuality]
    ModelDataQuality: Optional[DriftCheckModelDataQuality]


CustomerMetadataMap = Dict[CustomerMetadataKey, CustomerMetadataValue]


class Explainability(TypedDict, total=False):
    """Contains explainability metrics for a model."""

    Report: Optional[MetricsSource]


class ModelDataQuality(TypedDict, total=False):
    """Data quality constraints and statistics for a model."""

    Statistics: Optional[MetricsSource]
    Constraints: Optional[MetricsSource]


class ModelQuality(TypedDict, total=False):
    """Model quality statistics and constraints."""

    Statistics: Optional[MetricsSource]
    Constraints: Optional[MetricsSource]


class ModelMetrics(TypedDict, total=False):
    """Contains metrics captured from a model."""

    ModelQuality: Optional[ModelQuality]
    ModelDataQuality: Optional[ModelDataQuality]
    Bias: Optional[Bias]
    Explainability: Optional[Explainability]


class SourceAlgorithm(TypedDict, total=False):
    """Specifies an algorithm that was used to create the model package. The
    algorithm must be either an algorithm resource in your SageMaker account
    or an algorithm in Amazon Web Services Marketplace that you are
    subscribed to.
    """

    ModelDataUrl: Optional[Url]
    ModelDataSource: Optional[ModelDataSource]
    ModelDataETag: Optional[String]
    AlgorithmName: ArnOrName


SourceAlgorithmList = List[SourceAlgorithm]


class SourceAlgorithmSpecification(TypedDict, total=False):
    """A list of algorithms that were used to create a model package."""

    SourceAlgorithms: SourceAlgorithmList


class ModelPackageValidationProfile(TypedDict, total=False):
    """Contains data, such as the inputs and targeted instance types that are
    used in the process of validating the model package.

    The data provided in the validation profile is made available to your
    buyers on Amazon Web Services Marketplace.
    """

    ProfileName: EntityName
    TransformJobDefinition: TransformJobDefinition


ModelPackageValidationProfiles = List[ModelPackageValidationProfile]


class ModelPackageValidationSpecification(TypedDict, total=False):
    """Specifies batch transform jobs that SageMaker runs to validate your
    model package.
    """

    ValidationRole: RoleArn
    ValidationProfiles: ModelPackageValidationProfiles


class CreateModelPackageInput(ServiceRequest):
    ModelPackageName: Optional[EntityName]
    ModelPackageGroupName: Optional[ArnOrName]
    ModelPackageDescription: Optional[EntityDescription]
    InferenceSpecification: Optional[InferenceSpecification]
    ValidationSpecification: Optional[ModelPackageValidationSpecification]
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecification]
    CertifyForMarketplace: Optional[CertifyForMarketplace]
    Tags: Optional[TagList]
    ModelApprovalStatus: Optional[ModelApprovalStatus]
    MetadataProperties: Optional[MetadataProperties]
    ModelMetrics: Optional[ModelMetrics]
    ClientToken: Optional[ClientToken]
    Domain: Optional[String]
    Task: Optional[String]
    SamplePayloadUrl: Optional[S3Uri]
    CustomerMetadataProperties: Optional[CustomerMetadataMap]
    DriftCheckBaselines: Optional[DriftCheckBaselines]
    AdditionalInferenceSpecifications: Optional[AdditionalInferenceSpecifications]
    SkipModelValidation: Optional[SkipModelValidation]
    SourceUri: Optional[ModelPackageSourceUri]
    SecurityConfig: Optional[ModelPackageSecurityConfig]
    ModelCard: Optional[ModelPackageModelCard]
    ModelLifeCycle: Optional[ModelLifeCycle]


class CreateModelPackageOutput(TypedDict, total=False):
    ModelPackageArn: ModelPackageArn


class ModelQualityJobInput(TypedDict, total=False):
    """The input for the model quality monitoring job. Currently endpoints are
    supported for input for model quality monitoring jobs.
    """

    EndpointInput: Optional[EndpointInput]
    BatchTransformInput: Optional[BatchTransformInput]
    GroundTruthS3Input: MonitoringGroundTruthS3Input


class ModelQualityAppSpecification(TypedDict, total=False):
    """Container image configuration object for the monitoring job."""

    ImageUri: ImageUri
    ContainerEntrypoint: Optional[ContainerEntrypoint]
    ContainerArguments: Optional[MonitoringContainerArguments]
    RecordPreprocessorSourceUri: Optional[S3Uri]
    PostAnalyticsProcessorSourceUri: Optional[S3Uri]
    ProblemType: Optional[MonitoringProblemType]
    Environment: Optional[MonitoringEnvironmentMap]


class ModelQualityBaselineConfig(TypedDict, total=False):
    """Configuration for monitoring constraints and monitoring statistics.
    These baseline resources are compared against the results of the current
    job from the series of jobs scheduled to collect data periodically.
    """

    BaseliningJobName: Optional[ProcessingJobName]
    ConstraintsResource: Optional[MonitoringConstraintsResource]


class CreateModelQualityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName
    ModelQualityBaselineConfig: Optional[ModelQualityBaselineConfig]
    ModelQualityAppSpecification: ModelQualityAppSpecification
    ModelQualityJobInput: ModelQualityJobInput
    ModelQualityJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]
    Tags: Optional[TagList]


class CreateModelQualityJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn


class NetworkConfig(TypedDict, total=False):
    """Networking options for a job, such as network traffic encryption between
    containers, whether to allow inbound and outbound network calls to and
    from containers, and the VPC subnets and security groups to use for
    VPC-enabled jobs.
    """

    EnableInterContainerTrafficEncryption: Optional[Boolean]
    EnableNetworkIsolation: Optional[Boolean]
    VpcConfig: Optional[VpcConfig]


class MonitoringAppSpecification(TypedDict, total=False):
    """Container image configuration object for the monitoring job."""

    ImageUri: ImageUri
    ContainerEntrypoint: Optional[ContainerEntrypoint]
    ContainerArguments: Optional[MonitoringContainerArguments]
    RecordPreprocessorSourceUri: Optional[S3Uri]
    PostAnalyticsProcessorSourceUri: Optional[S3Uri]


class MonitoringInput(TypedDict, total=False):
    """The inputs for a monitoring job."""

    EndpointInput: Optional[EndpointInput]
    BatchTransformInput: Optional[BatchTransformInput]


MonitoringInputs = List[MonitoringInput]


class MonitoringBaselineConfig(TypedDict, total=False):
    """Configuration for monitoring constraints and monitoring statistics.
    These baseline resources are compared against the results of the current
    job from the series of jobs scheduled to collect data periodically.
    """

    BaseliningJobName: Optional[ProcessingJobName]
    ConstraintsResource: Optional[MonitoringConstraintsResource]
    StatisticsResource: Optional[MonitoringStatisticsResource]


class MonitoringJobDefinition(TypedDict, total=False):
    """Defines the monitoring job."""

    BaselineConfig: Optional[MonitoringBaselineConfig]
    MonitoringInputs: MonitoringInputs
    MonitoringOutputConfig: MonitoringOutputConfig
    MonitoringResources: MonitoringResources
    MonitoringAppSpecification: MonitoringAppSpecification
    StoppingCondition: Optional[MonitoringStoppingCondition]
    Environment: Optional[MonitoringEnvironmentMap]
    NetworkConfig: Optional[NetworkConfig]
    RoleArn: RoleArn


class ScheduleConfig(TypedDict, total=False):
    """Configuration details about the monitoring schedule."""

    ScheduleExpression: ScheduleExpression
    DataAnalysisStartTime: Optional[String]
    DataAnalysisEndTime: Optional[String]


class MonitoringScheduleConfig(TypedDict, total=False):
    """Configures the monitoring schedule and defines the monitoring job."""

    ScheduleConfig: Optional[ScheduleConfig]
    MonitoringJobDefinition: Optional[MonitoringJobDefinition]
    MonitoringJobDefinitionName: Optional[MonitoringJobDefinitionName]
    MonitoringType: Optional[MonitoringType]


class CreateMonitoringScheduleRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName
    MonitoringScheduleConfig: MonitoringScheduleConfig
    Tags: Optional[TagList]


class CreateMonitoringScheduleResponse(TypedDict, total=False):
    MonitoringScheduleArn: MonitoringScheduleArn


class InstanceMetadataServiceConfiguration(TypedDict, total=False):
    """Information on the IMDS configuration of the notebook instance"""

    MinimumInstanceMetadataServiceVersion: MinimumInstanceMetadataServiceVersion


NotebookInstanceAcceleratorTypes = List[NotebookInstanceAcceleratorType]


class CreateNotebookInstanceInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName
    InstanceType: InstanceType
    SubnetId: Optional[SubnetId]
    SecurityGroupIds: Optional[SecurityGroupIds]
    RoleArn: RoleArn
    KmsKeyId: Optional[KmsKeyId]
    Tags: Optional[TagList]
    LifecycleConfigName: Optional[NotebookInstanceLifecycleConfigName]
    DirectInternetAccess: Optional[DirectInternetAccess]
    VolumeSizeInGB: Optional[NotebookInstanceVolumeSizeInGB]
    AcceleratorTypes: Optional[NotebookInstanceAcceleratorTypes]
    DefaultCodeRepository: Optional[CodeRepositoryNameOrUrl]
    AdditionalCodeRepositories: Optional[AdditionalCodeRepositoryNamesOrUrls]
    RootAccess: Optional[RootAccess]
    PlatformIdentifier: Optional[PlatformIdentifier]
    InstanceMetadataServiceConfiguration: Optional[InstanceMetadataServiceConfiguration]


class NotebookInstanceLifecycleHook(TypedDict, total=False):
    """Contains the notebook instance lifecycle configuration script.

    Each lifecycle configuration script has a limit of 16384 characters.

    The value of the ``$PATH`` environment variable that is available to
    both scripts is ``/sbin:bin:/usr/sbin:/usr/bin``.

    View Amazon CloudWatch Logs for notebook instance lifecycle
    configurations in log group ``/aws/sagemaker/NotebookInstances`` in log
    stream ``[notebook-instance-name]/[LifecycleConfigHook]``.

    Lifecycle configuration scripts cannot run for longer than 5 minutes. If
    a script runs for longer than 5 minutes, it fails and the notebook
    instance is not created or started.

    For information about notebook instance lifestyle configurations, see
    `Step 2.1: (Optional) Customize a Notebook
    Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__.
    """

    Content: Optional[NotebookInstanceLifecycleConfigContent]


NotebookInstanceLifecycleConfigList = List[NotebookInstanceLifecycleHook]


class CreateNotebookInstanceLifecycleConfigInput(ServiceRequest):
    NotebookInstanceLifecycleConfigName: NotebookInstanceLifecycleConfigName
    OnCreate: Optional[NotebookInstanceLifecycleConfigList]
    OnStart: Optional[NotebookInstanceLifecycleConfigList]
    Tags: Optional[TagList]


class CreateNotebookInstanceLifecycleConfigOutput(TypedDict, total=False):
    NotebookInstanceLifecycleConfigArn: Optional[NotebookInstanceLifecycleConfigArn]


class CreateNotebookInstanceOutput(TypedDict, total=False):
    NotebookInstanceArn: Optional[NotebookInstanceArn]


OptimizationVpcSubnets = List[OptimizationVpcSubnetId]
OptimizationVpcSecurityGroupIds = List[OptimizationVpcSecurityGroupId]


class OptimizationVpcConfig(TypedDict, total=False):
    """A VPC in Amazon VPC that's accessible to an optimized that you create
    with an optimization job. You can control access to and from your
    resources by configuring a VPC. For more information, see `Give
    SageMaker Access to Resources in your Amazon
    VPC <https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html>`__.
    """

    SecurityGroupIds: OptimizationVpcSecurityGroupIds
    Subnets: OptimizationVpcSubnets


class OptimizationJobOutputConfig(TypedDict, total=False):
    """Details for where to store the optimized model that you create with the
    optimization job.
    """

    KmsKeyId: Optional[KmsKeyId]
    S3OutputLocation: S3Uri


OptimizationJobEnvironmentVariables = Dict[NonEmptyString256, String256]


class ModelShardingConfig(TypedDict, total=False):
    """Settings for the model sharding technique that's applied by a model
    optimization job.
    """

    Image: Optional[OptimizationContainerImage]
    OverrideEnvironment: Optional[OptimizationJobEnvironmentVariables]


class ModelCompilationConfig(TypedDict, total=False):
    """Settings for the model compilation technique that's applied by a model
    optimization job.
    """

    Image: Optional[OptimizationContainerImage]
    OverrideEnvironment: Optional[OptimizationJobEnvironmentVariables]


class ModelQuantizationConfig(TypedDict, total=False):
    """Settings for the model quantization technique that's applied by a model
    optimization job.
    """

    Image: Optional[OptimizationContainerImage]
    OverrideEnvironment: Optional[OptimizationJobEnvironmentVariables]


class OptimizationConfig(TypedDict, total=False):
    """Settings for an optimization technique that you apply with a model
    optimization job.
    """

    ModelQuantizationConfig: Optional[ModelQuantizationConfig]
    ModelCompilationConfig: Optional[ModelCompilationConfig]
    ModelShardingConfig: Optional[ModelShardingConfig]


OptimizationConfigs = List[OptimizationConfig]


class OptimizationModelAccessConfig(TypedDict, total=False):
    """The access configuration settings for the source ML model for an
    optimization job, where you can accept the model end-user license
    agreement (EULA).
    """

    AcceptEula: OptimizationModelAcceptEula


class OptimizationJobModelSourceS3(TypedDict, total=False):
    """The Amazon S3 location of a source model to optimize with an
    optimization job.
    """

    S3Uri: Optional[S3Uri]
    ModelAccessConfig: Optional[OptimizationModelAccessConfig]


class OptimizationJobModelSource(TypedDict, total=False):
    """The location of the source model to optimize with an optimization job."""

    S3: Optional[OptimizationJobModelSourceS3]


class CreateOptimizationJobRequest(ServiceRequest):
    OptimizationJobName: EntityName
    RoleArn: RoleArn
    ModelSource: OptimizationJobModelSource
    DeploymentInstanceType: OptimizationJobDeploymentInstanceType
    OptimizationEnvironment: Optional[OptimizationJobEnvironmentVariables]
    OptimizationConfigs: OptimizationConfigs
    OutputConfig: OptimizationJobOutputConfig
    StoppingCondition: StoppingCondition
    Tags: Optional[TagList]
    VpcConfig: Optional[OptimizationVpcConfig]


class CreateOptimizationJobResponse(TypedDict, total=False):
    OptimizationJobArn: OptimizationJobArn


class CreatePartnerAppPresignedUrlRequest(ServiceRequest):
    Arn: PartnerAppArn
    ExpiresInSeconds: Optional[ExpiresInSeconds]
    SessionExpirationDurationInSeconds: Optional[SessionExpirationDurationInSeconds]


class CreatePartnerAppPresignedUrlResponse(TypedDict, total=False):
    Url: Optional[String2048]


PartnerAppArguments = Dict[NonEmptyString256, String1024]
PartnerAppAdminUserList = List[NonEmptyString256]


class PartnerAppConfig(TypedDict, total=False):
    """Configuration settings for the SageMaker Partner AI App."""

    AdminUsers: Optional[PartnerAppAdminUserList]
    Arguments: Optional[PartnerAppArguments]


class PartnerAppMaintenanceConfig(TypedDict, total=False):
    """Maintenance configuration settings for the SageMaker Partner AI App."""

    MaintenanceWindowStart: Optional[WeeklyScheduleTimeFormat]


class CreatePartnerAppRequest(ServiceRequest):
    Name: PartnerAppName
    Type: PartnerAppType
    ExecutionRoleArn: RoleArn
    KmsKeyId: Optional[KmsKeyId]
    MaintenanceConfig: Optional[PartnerAppMaintenanceConfig]
    Tier: NonEmptyString64
    ApplicationConfig: Optional[PartnerAppConfig]
    AuthType: PartnerAppAuthType
    EnableIamSessionBasedIdentity: Optional[Boolean]
    ClientToken: Optional[ClientToken]
    Tags: Optional[TagList]


class CreatePartnerAppResponse(TypedDict, total=False):
    Arn: Optional[PartnerAppArn]


class ParallelismConfiguration(TypedDict, total=False):
    """Configuration that controls the parallelism of the pipeline. By default,
    the parallelism configuration specified applies to all executions of the
    pipeline unless overridden.
    """

    MaxParallelExecutionSteps: MaxParallelExecutionSteps


class PipelineDefinitionS3Location(TypedDict, total=False):
    """The location of the pipeline definition stored in Amazon S3."""

    Bucket: BucketName
    ObjectKey: Key
    VersionId: Optional[VersionId]


class CreatePipelineRequest(ServiceRequest):
    PipelineName: PipelineName
    PipelineDisplayName: Optional[PipelineName]
    PipelineDefinition: Optional[PipelineDefinition]
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3Location]
    PipelineDescription: Optional[PipelineDescription]
    ClientRequestToken: IdempotencyToken
    RoleArn: RoleArn
    Tags: Optional[TagList]
    ParallelismConfiguration: Optional[ParallelismConfiguration]


class CreatePipelineResponse(TypedDict, total=False):
    PipelineArn: Optional[PipelineArn]


class CreatePresignedDomainUrlRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: UserProfileName
    SessionExpirationDurationInSeconds: Optional[SessionExpirationDurationInSeconds]
    ExpiresInSeconds: Optional[ExpiresInSeconds]
    SpaceName: Optional[SpaceName]
    LandingUri: Optional[LandingUri]


class CreatePresignedDomainUrlResponse(TypedDict, total=False):
    AuthorizedUrl: Optional[PresignedDomainUrl]


class CreatePresignedMlflowTrackingServerUrlRequest(ServiceRequest):
    TrackingServerName: TrackingServerName
    ExpiresInSeconds: Optional[ExpiresInSeconds]
    SessionExpirationDurationInSeconds: Optional[SessionExpirationDurationInSeconds]


class CreatePresignedMlflowTrackingServerUrlResponse(TypedDict, total=False):
    AuthorizedUrl: Optional[TrackingServerUrl]


class CreatePresignedNotebookInstanceUrlInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName
    SessionExpirationDurationInSeconds: Optional[SessionExpirationDurationInSeconds]


class CreatePresignedNotebookInstanceUrlOutput(TypedDict, total=False):
    AuthorizedUrl: Optional[NotebookInstanceUrl]


class ExperimentConfig(TypedDict, total=False):
    """Associates a SageMaker job as a trial component with an experiment and
    trial. Specified when you call the following APIs:

    -  `CreateProcessingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html>`__

    -  `CreateTrainingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html>`__

    -  `CreateTransformJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html>`__
    """

    ExperimentName: Optional[ExperimentEntityName]
    TrialName: Optional[ExperimentEntityName]
    TrialComponentDisplayName: Optional[ExperimentEntityName]
    RunName: Optional[ExperimentEntityName]


ProcessingEnvironmentMap = Dict[ProcessingEnvironmentKey, ProcessingEnvironmentValue]


class ProcessingStoppingCondition(TypedDict, total=False):
    """Configures conditions under which the processing job should be stopped,
    such as how long the processing job has been running. After the
    condition is met, the processing job is stopped.
    """

    MaxRuntimeInSeconds: ProcessingMaxRuntimeInSeconds


class ProcessingClusterConfig(TypedDict, total=False):
    """Configuration for the cluster used to run a processing job."""

    InstanceCount: ProcessingInstanceCount
    InstanceType: ProcessingInstanceType
    VolumeSizeInGB: ProcessingVolumeSizeInGB
    VolumeKmsKeyId: Optional[KmsKeyId]


class ProcessingResources(TypedDict, total=False):
    """Identifies the resources, ML compute instances, and ML storage volumes
    to deploy for a processing job. In distributed training, you specify
    more than one instance.
    """

    ClusterConfig: ProcessingClusterConfig


class ProcessingFeatureStoreOutput(TypedDict, total=False):
    """Configuration for processing job outputs in Amazon SageMaker Feature
    Store.
    """

    FeatureGroupName: FeatureGroupName


class ProcessingS3Output(TypedDict, total=False):
    """Configuration for uploading output data to Amazon S3 from the processing
    container.
    """

    S3Uri: S3Uri
    LocalPath: Optional[ProcessingLocalPath]
    S3UploadMode: ProcessingS3UploadMode


class ProcessingOutput(TypedDict, total=False):
    """Describes the results of a processing job. The processing output must
    specify exactly one of either ``S3Output`` or ``FeatureStoreOutput``
    types.
    """

    OutputName: String
    S3Output: Optional[ProcessingS3Output]
    FeatureStoreOutput: Optional[ProcessingFeatureStoreOutput]
    AppManaged: Optional[AppManaged]


ProcessingOutputs = List[ProcessingOutput]


class ProcessingOutputConfig(TypedDict, total=False):
    """Configuration for uploading output from the processing container."""

    Outputs: ProcessingOutputs
    KmsKeyId: Optional[KmsKeyId]


class RedshiftDatasetDefinition(TypedDict, total=False):
    """Configuration for Redshift Dataset Definition input."""

    ClusterId: RedshiftClusterId
    Database: RedshiftDatabase
    DbUser: RedshiftUserName
    QueryString: RedshiftQueryString
    ClusterRoleArn: RoleArn
    OutputS3Uri: S3Uri
    KmsKeyId: Optional[KmsKeyId]
    OutputFormat: RedshiftResultFormat
    OutputCompression: Optional[RedshiftResultCompressionType]


class DatasetDefinition(TypedDict, total=False):
    """Configuration for Dataset Definition inputs. The Dataset Definition
    input must specify exactly one of either ``AthenaDatasetDefinition`` or
    ``RedshiftDatasetDefinition`` types.
    """

    AthenaDatasetDefinition: Optional[AthenaDatasetDefinition]
    RedshiftDatasetDefinition: Optional[RedshiftDatasetDefinition]
    LocalPath: Optional[ProcessingLocalPath]
    DataDistributionType: Optional[DataDistributionType]
    InputMode: Optional[InputMode]


class ProcessingS3Input(TypedDict, total=False):
    """Configuration for downloading input data from Amazon S3 into the
    processing container.
    """

    S3Uri: S3Uri
    LocalPath: Optional[ProcessingLocalPath]
    S3DataType: ProcessingS3DataType
    S3InputMode: Optional[ProcessingS3InputMode]
    S3DataDistributionType: Optional[ProcessingS3DataDistributionType]
    S3CompressionType: Optional[ProcessingS3CompressionType]


class ProcessingInput(TypedDict, total=False):
    """The inputs for a processing job. The processing input must specify
    exactly one of either ``S3Input`` or ``DatasetDefinition`` types.
    """

    InputName: String
    AppManaged: Optional[AppManaged]
    S3Input: Optional[ProcessingS3Input]
    DatasetDefinition: Optional[DatasetDefinition]


ProcessingInputs = List[ProcessingInput]


class CreateProcessingJobRequest(ServiceRequest):
    ProcessingInputs: Optional[ProcessingInputs]
    ProcessingOutputConfig: Optional[ProcessingOutputConfig]
    ProcessingJobName: ProcessingJobName
    ProcessingResources: ProcessingResources
    StoppingCondition: Optional[ProcessingStoppingCondition]
    AppSpecification: AppSpecification
    Environment: Optional[ProcessingEnvironmentMap]
    NetworkConfig: Optional[NetworkConfig]
    RoleArn: RoleArn
    Tags: Optional[TagList]
    ExperimentConfig: Optional[ExperimentConfig]


class CreateProcessingJobResponse(TypedDict, total=False):
    ProcessingJobArn: ProcessingJobArn


class ProvisioningParameter(TypedDict, total=False):
    """A key value pair used when you provision a project as a service catalog
    product. For information, see `What is Amazon Web Services Service
    Catalog <https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html>`__.
    """

    Key: Optional[ProvisioningParameterKey]
    Value: Optional[ProvisioningParameterValue]


ProvisioningParameters = List[ProvisioningParameter]


class ServiceCatalogProvisioningDetails(TypedDict, total=False):
    """Details that you specify to provision a service catalog product. For
    information about service catalog, see `What is Amazon Web Services
    Service
    Catalog <https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html>`__.
    """

    ProductId: ServiceCatalogEntityId
    ProvisioningArtifactId: Optional[ServiceCatalogEntityId]
    PathId: Optional[ServiceCatalogEntityId]
    ProvisioningParameters: Optional[ProvisioningParameters]


class CreateProjectInput(ServiceRequest):
    ProjectName: ProjectEntityName
    ProjectDescription: Optional[EntityDescription]
    ServiceCatalogProvisioningDetails: Optional[ServiceCatalogProvisioningDetails]
    Tags: Optional[TagList]


class CreateProjectOutput(TypedDict, total=False):
    ProjectArn: ProjectArn
    ProjectId: ProjectId


class SpaceSharingSettings(TypedDict, total=False):
    """A collection of space sharing settings."""

    SharingType: SharingType


class OwnershipSettings(TypedDict, total=False):
    """The collection of ownership settings for a space."""

    OwnerUserProfileName: UserProfileName


class FSxLustreFileSystem(TypedDict, total=False):
    """A custom file system in Amazon FSx for Lustre."""

    FileSystemId: FileSystemId


class EFSFileSystem(TypedDict, total=False):
    """A file system, created by you in Amazon EFS, that you assign to a user
    profile or space for an Amazon SageMaker AI Domain. Permitted users can
    access this file system in Amazon SageMaker AI Studio.
    """

    FileSystemId: FileSystemId


class CustomFileSystem(TypedDict, total=False):
    """A file system, created by you, that you assign to a user profile or
    space for an Amazon SageMaker AI Domain. Permitted users can access this
    file system in Amazon SageMaker AI Studio.
    """

    EFSFileSystem: Optional[EFSFileSystem]
    FSxLustreFileSystem: Optional[FSxLustreFileSystem]


CustomFileSystems = List[CustomFileSystem]


class EbsStorageSettings(TypedDict, total=False):
    """A collection of EBS storage settings that apply to both private and
    shared spaces.
    """

    EbsVolumeSizeInGb: SpaceEbsVolumeSizeInGb


class SpaceStorageSettings(TypedDict, total=False):
    """The storage settings for a space."""

    EbsStorageSettings: Optional[EbsStorageSettings]


class SpaceIdleSettings(TypedDict, total=False):
    """Settings related to idle shutdown of Studio applications in a space."""

    IdleTimeoutInMinutes: Optional[IdleTimeoutInMinutes]


class SpaceAppLifecycleManagement(TypedDict, total=False):
    """Settings that are used to configure and manage the lifecycle of Amazon
    SageMaker Studio applications in a space.
    """

    IdleSettings: Optional[SpaceIdleSettings]


class SpaceJupyterLabAppSettings(TypedDict, total=False):
    """The settings for the JupyterLab application within a space."""

    DefaultResourceSpec: Optional[ResourceSpec]
    CodeRepositories: Optional[CodeRepositories]
    AppLifecycleManagement: Optional[SpaceAppLifecycleManagement]


class SpaceCodeEditorAppSettings(TypedDict, total=False):
    """The application settings for a Code Editor space."""

    DefaultResourceSpec: Optional[ResourceSpec]
    AppLifecycleManagement: Optional[SpaceAppLifecycleManagement]


class SpaceSettings(TypedDict, total=False):
    """A collection of space settings."""

    JupyterServerAppSettings: Optional[JupyterServerAppSettings]
    KernelGatewayAppSettings: Optional[KernelGatewayAppSettings]
    CodeEditorAppSettings: Optional[SpaceCodeEditorAppSettings]
    JupyterLabAppSettings: Optional[SpaceJupyterLabAppSettings]
    AppType: Optional[AppType]
    SpaceStorageSettings: Optional[SpaceStorageSettings]
    SpaceManagedResources: Optional[FeatureStatus]
    CustomFileSystems: Optional[CustomFileSystems]


class CreateSpaceRequest(ServiceRequest):
    DomainId: DomainId
    SpaceName: SpaceName
    Tags: Optional[TagList]
    SpaceSettings: Optional[SpaceSettings]
    OwnershipSettings: Optional[OwnershipSettings]
    SpaceSharingSettings: Optional[SpaceSharingSettings]
    SpaceDisplayName: Optional[NonEmptyString64]


class CreateSpaceResponse(TypedDict, total=False):
    SpaceArn: Optional[SpaceArn]


class CreateStudioLifecycleConfigRequest(ServiceRequest):
    StudioLifecycleConfigName: StudioLifecycleConfigName
    StudioLifecycleConfigContent: StudioLifecycleConfigContent
    StudioLifecycleConfigAppType: StudioLifecycleConfigAppType
    Tags: Optional[TagList]


class CreateStudioLifecycleConfigResponse(TypedDict, total=False):
    StudioLifecycleConfigArn: Optional[StudioLifecycleConfigArn]


class SessionChainingConfig(TypedDict, total=False):
    """Contains information about attribute-based access control (ABAC) for a
    training job. The session chaining configuration uses Amazon Security
    Token Service (STS) for your training job to request temporary,
    limited-privilege credentials to tenants. For more information, see
    `Attribute-based access control (ABAC) for multi-tenancy
    training <https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data.html#model-access-training-data-abac>`__.
    """

    EnableSessionTagChaining: Optional[EnableSessionTagChaining]


class InfraCheckConfig(TypedDict, total=False):
    """Configuration information for the infrastructure health check of a
    training job. A SageMaker-provided health check tests the health of
    instance hardware and cluster network connectivity.
    """

    EnableInfraCheck: Optional[EnableInfraCheck]


class RemoteDebugConfig(TypedDict, total=False):
    """Configuration for remote debugging for the
    `CreateTrainingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html>`__
    API. To learn more about the remote debugging functionality of
    SageMaker, see `Access a training container through Amazon Web Services
    Systems Manager (SSM) for remote
    debugging <https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html>`__.
    """

    EnableRemoteDebug: Optional[EnableRemoteDebug]


TrainingEnvironmentMap = Dict[TrainingEnvironmentKey, TrainingEnvironmentValue]
RuleParameters = Dict[ConfigKey, ConfigValue]


class ProfilerRuleConfiguration(TypedDict, total=False):
    """Configuration information for profiling rules."""

    RuleConfigurationName: RuleConfigurationName
    LocalPath: Optional[DirectoryPath]
    S3OutputPath: Optional[S3Uri]
    RuleEvaluatorImage: AlgorithmImage
    InstanceType: Optional[ProcessingInstanceType]
    VolumeSizeInGB: Optional[OptionalVolumeSizeInGB]
    RuleParameters: Optional[RuleParameters]


ProfilerRuleConfigurations = List[ProfilerRuleConfiguration]
ProfilingParameters = Dict[ConfigKey, ConfigValue]
ProfilingIntervalInMilliseconds = int


class ProfilerConfig(TypedDict, total=False):
    """Configuration information for Amazon SageMaker Debugger system
    monitoring, framework profiling, and storage paths.
    """

    S3OutputPath: Optional[S3Uri]
    ProfilingIntervalInMilliseconds: Optional[ProfilingIntervalInMilliseconds]
    ProfilingParameters: Optional[ProfilingParameters]
    DisableProfiler: Optional[DisableProfiler]


class TensorBoardOutputConfig(TypedDict, total=False):
    """Configuration of storage locations for the Amazon SageMaker Debugger
    TensorBoard output data.
    """

    LocalPath: Optional[DirectoryPath]
    S3OutputPath: S3Uri


class DebugRuleConfiguration(TypedDict, total=False):
    """Configuration information for SageMaker Debugger rules for debugging. To
    learn more about how to configure the ``DebugRuleConfiguration``
    parameter, see `Use the SageMaker and Debugger Configuration API
    Operations to Create, Update, and Debug Your Training
    Job <https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html>`__.
    """

    RuleConfigurationName: RuleConfigurationName
    LocalPath: Optional[DirectoryPath]
    S3OutputPath: Optional[S3Uri]
    RuleEvaluatorImage: AlgorithmImage
    InstanceType: Optional[ProcessingInstanceType]
    VolumeSizeInGB: Optional[OptionalVolumeSizeInGB]
    RuleParameters: Optional[RuleParameters]


DebugRuleConfigurations = List[DebugRuleConfiguration]
HookParameters = Dict[ConfigKey, ConfigValue]


class DebugHookConfig(TypedDict, total=False):
    """Configuration information for the Amazon SageMaker Debugger hook
    parameters, metric and tensor collections, and storage paths. To learn
    more about how to configure the ``DebugHookConfig`` parameter, see `Use
    the SageMaker and Debugger Configuration API Operations to Create,
    Update, and Debug Your Training
    Job <https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html>`__.
    """

    LocalPath: Optional[DirectoryPath]
    S3OutputPath: S3Uri
    HookParameters: Optional[HookParameters]
    CollectionConfigurations: Optional[CollectionConfigurations]


class CreateTrainingJobRequest(ServiceRequest):
    TrainingJobName: TrainingJobName
    HyperParameters: Optional[HyperParameters]
    AlgorithmSpecification: AlgorithmSpecification
    RoleArn: RoleArn
    InputDataConfig: Optional[InputDataConfig]
    OutputDataConfig: OutputDataConfig
    ResourceConfig: ResourceConfig
    VpcConfig: Optional[VpcConfig]
    StoppingCondition: StoppingCondition
    Tags: Optional[TagList]
    EnableNetworkIsolation: Optional[Boolean]
    EnableInterContainerTrafficEncryption: Optional[Boolean]
    EnableManagedSpotTraining: Optional[Boolean]
    CheckpointConfig: Optional[CheckpointConfig]
    DebugHookConfig: Optional[DebugHookConfig]
    DebugRuleConfigurations: Optional[DebugRuleConfigurations]
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfig]
    ExperimentConfig: Optional[ExperimentConfig]
    ProfilerConfig: Optional[ProfilerConfig]
    ProfilerRuleConfigurations: Optional[ProfilerRuleConfigurations]
    Environment: Optional[TrainingEnvironmentMap]
    RetryStrategy: Optional[RetryStrategy]
    RemoteDebugConfig: Optional[RemoteDebugConfig]
    InfraCheckConfig: Optional[InfraCheckConfig]
    SessionChainingConfig: Optional[SessionChainingConfig]


class CreateTrainingJobResponse(TypedDict, total=False):
    TrainingJobArn: TrainingJobArn


class CreateTrainingPlanRequest(ServiceRequest):
    TrainingPlanName: TrainingPlanName
    TrainingPlanOfferingId: TrainingPlanOfferingId
    Tags: Optional[TagList]


class CreateTrainingPlanResponse(TypedDict, total=False):
    TrainingPlanArn: TrainingPlanArn


class DataProcessing(TypedDict, total=False):
    """The data structure used to specify the data to be used for inference in
    a batch transform job and to associate the data that is relevant to the
    prediction results in the output. The input filter provided allows you
    to exclude input data that is not needed for inference in a batch
    transform job. The output filter provided allows you to include input
    data relevant to interpreting the predictions in the output from the
    job. For more information, see `Associate Prediction Results with their
    Corresponding Input
    Records <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html>`__.
    """

    InputFilter: Optional[JsonPath]
    OutputFilter: Optional[JsonPath]
    JoinSource: Optional[JoinSource]


class ModelClientConfig(TypedDict, total=False):
    """Configures the timeout and maximum number of retries for processing a
    transform job invocation.
    """

    InvocationsTimeoutInSeconds: Optional[InvocationsTimeoutInSeconds]
    InvocationsMaxRetries: Optional[InvocationsMaxRetries]


class CreateTransformJobRequest(ServiceRequest):
    TransformJobName: TransformJobName
    ModelName: ModelName
    MaxConcurrentTransforms: Optional[MaxConcurrentTransforms]
    ModelClientConfig: Optional[ModelClientConfig]
    MaxPayloadInMB: Optional[MaxPayloadInMB]
    BatchStrategy: Optional[BatchStrategy]
    Environment: Optional[TransformEnvironmentMap]
    TransformInput: TransformInput
    TransformOutput: TransformOutput
    DataCaptureConfig: Optional[BatchDataCaptureConfig]
    TransformResources: TransformResources
    DataProcessing: Optional[DataProcessing]
    Tags: Optional[TagList]
    ExperimentConfig: Optional[ExperimentConfig]


class CreateTransformJobResponse(TypedDict, total=False):
    TransformJobArn: TransformJobArn


class TrialComponentArtifact(TypedDict, total=False):
    """Represents an input or output artifact of a trial component. You specify
    ``TrialComponentArtifact`` as part of the ``InputArtifacts`` and
    ``OutputArtifacts`` parameters in the
    `CreateTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html>`__
    request.

    Examples of input artifacts are datasets, algorithms, hyperparameters,
    source code, and instance types. Examples of output artifacts are
    metrics, snapshots, logs, and images.
    """

    MediaType: Optional[MediaType]
    Value: TrialComponentArtifactValue


TrialComponentArtifacts = Dict[TrialComponentKey128, TrialComponentArtifact]


class TrialComponentParameterValue(TypedDict, total=False):
    """The value of a hyperparameter. Only one of ``NumberValue`` or
    ``StringValue`` can be specified.

    This object is specified in the
    `CreateTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html>`__
    request.
    """

    StringValue: Optional[StringParameterValue]
    NumberValue: Optional[DoubleParameterValue]


TrialComponentParameters = Dict[TrialComponentKey320, TrialComponentParameterValue]


class TrialComponentStatus(TypedDict, total=False):
    """The status of the trial component."""

    PrimaryStatus: Optional[TrialComponentPrimaryStatus]
    Message: Optional[TrialComponentStatusMessage]


class CreateTrialComponentRequest(ServiceRequest):
    TrialComponentName: ExperimentEntityName
    DisplayName: Optional[ExperimentEntityName]
    Status: Optional[TrialComponentStatus]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    Parameters: Optional[TrialComponentParameters]
    InputArtifacts: Optional[TrialComponentArtifacts]
    OutputArtifacts: Optional[TrialComponentArtifacts]
    MetadataProperties: Optional[MetadataProperties]
    Tags: Optional[TagList]


class CreateTrialComponentResponse(TypedDict, total=False):
    TrialComponentArn: Optional[TrialComponentArn]


class CreateTrialRequest(ServiceRequest):
    TrialName: ExperimentEntityName
    DisplayName: Optional[ExperimentEntityName]
    ExperimentName: ExperimentEntityName
    MetadataProperties: Optional[MetadataProperties]
    Tags: Optional[TagList]


class CreateTrialResponse(TypedDict, total=False):
    TrialArn: Optional[TrialArn]


class CreateUserProfileRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: UserProfileName
    SingleSignOnUserIdentifier: Optional[SingleSignOnUserIdentifier]
    SingleSignOnUserValue: Optional[String256]
    Tags: Optional[TagList]
    UserSettings: Optional[UserSettings]


class CreateUserProfileResponse(TypedDict, total=False):
    UserProfileArn: Optional[UserProfileArn]


WorkforceSubnets = List[WorkforceSubnetId]
WorkforceSecurityGroupIds = List[WorkforceSecurityGroupId]


class WorkforceVpcConfigRequest(TypedDict, total=False):
    """The VPC object you use to create or update a workforce."""

    VpcId: Optional[WorkforceVpcId]
    SecurityGroupIds: Optional[WorkforceSecurityGroupIds]
    Subnets: Optional[WorkforceSubnets]


class SourceIpConfig(TypedDict, total=False):
    """A list of IP address ranges
    (`CIDRs <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__).
    Used to create an allow list of IP addresses for a private workforce.
    Workers will only be able to log in to their worker portal from an IP
    address within this range. By default, a workforce isn't restricted to
    specific IP addresses.
    """

    Cidrs: Cidrs


class OidcConfig(TypedDict, total=False):
    """Use this parameter to configure your OIDC Identity Provider (IdP)."""

    ClientId: ClientId
    ClientSecret: ClientSecret
    Issuer: OidcEndpoint
    AuthorizationEndpoint: OidcEndpoint
    TokenEndpoint: OidcEndpoint
    UserInfoEndpoint: OidcEndpoint
    LogoutEndpoint: OidcEndpoint
    JwksUri: OidcEndpoint
    Scope: Optional[Scope]
    AuthenticationRequestExtraParams: Optional[AuthenticationRequestExtraParams]


class CreateWorkforceRequest(ServiceRequest):
    CognitoConfig: Optional[CognitoConfig]
    OidcConfig: Optional[OidcConfig]
    SourceIpConfig: Optional[SourceIpConfig]
    WorkforceName: WorkforceName
    Tags: Optional[TagList]
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequest]


class CreateWorkforceResponse(TypedDict, total=False):
    WorkforceArn: WorkforceArn


class IamPolicyConstraints(TypedDict, total=False):
    """Use this parameter to specify a supported global condition key that is
    added to the IAM policy.
    """

    SourceIp: Optional[EnabledOrDisabled]
    VpcSourceIp: Optional[EnabledOrDisabled]


class S3Presign(TypedDict, total=False):
    """This object defines the access restrictions to Amazon S3 resources that
    are included in custom worker task templates using the Liquid filter,
    ``grant_read_access``.

    To learn more about how custom templates are created, see `Create custom
    worker task
    templates <https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html>`__.
    """

    IamPolicyConstraints: Optional[IamPolicyConstraints]


class WorkerAccessConfiguration(TypedDict, total=False):
    """Use this optional parameter to constrain access to an Amazon S3 resource
    based on the IP address using supported IAM global condition keys. The
    Amazon S3 resource is accessed in the worker portal using a Amazon S3
    presigned URL.
    """

    S3Presign: Optional[S3Presign]


class NotificationConfiguration(TypedDict, total=False):
    """Configures Amazon SNS notifications of available or expiring work items
    for work teams.
    """

    NotificationTopicArn: Optional[NotificationTopicArn]


Groups = List[Group]


class OidcMemberDefinition(TypedDict, total=False):
    """A list of user groups that exist in your OIDC Identity Provider (IdP).
    One to ten groups can be used to create a single private work team. When
    you add a user group to the list of ``Groups``, you can add that user
    group to one or more private work teams. If you add a user group to a
    private work team, all workers in that user group are added to the work
    team.
    """

    Groups: Optional[Groups]


class MemberDefinition(TypedDict, total=False):
    """Defines an Amazon Cognito or your own OIDC IdP user group that is part
    of a work team.
    """

    CognitoMemberDefinition: Optional[CognitoMemberDefinition]
    OidcMemberDefinition: Optional[OidcMemberDefinition]


MemberDefinitions = List[MemberDefinition]


class CreateWorkteamRequest(ServiceRequest):
    WorkteamName: WorkteamName
    WorkforceName: Optional[WorkforceName]
    MemberDefinitions: MemberDefinitions
    Description: String200
    NotificationConfiguration: Optional[NotificationConfiguration]
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration]
    Tags: Optional[TagList]


class CreateWorkteamResponse(TypedDict, total=False):
    WorkteamArn: Optional[WorkteamArn]


CustomerMetadataKeyList = List[CustomerMetadataKey]


class CustomizedMetricSpecification(TypedDict, total=False):
    """A customized metric."""

    MetricName: Optional[String]
    Namespace: Optional[String]
    Statistic: Optional[Statistic]


class DataCaptureConfigSummary(TypedDict, total=False):
    """The currently active data capture configuration used by your Endpoint."""

    EnableCapture: EnableCapture
    CaptureStatus: CaptureStatus
    CurrentSamplingPercentage: SamplingPercentage
    DestinationS3Uri: DestinationS3Uri
    KmsKeyId: KmsKeyId


class DebugRuleEvaluationStatus(TypedDict, total=False):
    """Information about the status of the rule evaluation."""

    RuleConfigurationName: Optional[RuleConfigurationName]
    RuleEvaluationJobArn: Optional[ProcessingJobArn]
    RuleEvaluationStatus: Optional[RuleEvaluationStatus]
    StatusDetails: Optional[StatusDetails]
    LastModifiedTime: Optional[Timestamp]


DebugRuleEvaluationStatuses = List[DebugRuleEvaluationStatus]


class DeleteActionRequest(ServiceRequest):
    ActionName: ExperimentEntityName


class DeleteActionResponse(TypedDict, total=False):
    ActionArn: Optional[ActionArn]


class DeleteAlgorithmInput(ServiceRequest):
    AlgorithmName: EntityName


class DeleteAppImageConfigRequest(ServiceRequest):
    AppImageConfigName: AppImageConfigName


class DeleteAppRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: Optional[UserProfileName]
    SpaceName: Optional[SpaceName]
    AppType: AppType
    AppName: AppName


class DeleteArtifactRequest(ServiceRequest):
    ArtifactArn: Optional[ArtifactArn]
    Source: Optional[ArtifactSource]


class DeleteArtifactResponse(TypedDict, total=False):
    ArtifactArn: Optional[ArtifactArn]


class DeleteAssociationRequest(ServiceRequest):
    SourceArn: AssociationEntityArn
    DestinationArn: AssociationEntityArn


class DeleteAssociationResponse(TypedDict, total=False):
    SourceArn: Optional[AssociationEntityArn]
    DestinationArn: Optional[AssociationEntityArn]


class DeleteClusterRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn


class DeleteClusterResponse(TypedDict, total=False):
    ClusterArn: ClusterArn


class DeleteClusterSchedulerConfigRequest(ServiceRequest):
    ClusterSchedulerConfigId: ClusterSchedulerConfigId


class DeleteCodeRepositoryInput(ServiceRequest):
    CodeRepositoryName: EntityName


class DeleteCompilationJobRequest(ServiceRequest):
    CompilationJobName: EntityName


class DeleteComputeQuotaRequest(ServiceRequest):
    ComputeQuotaId: ComputeQuotaId


class DeleteContextRequest(ServiceRequest):
    ContextName: ContextName


class DeleteContextResponse(TypedDict, total=False):
    ContextArn: Optional[ContextArn]


class DeleteDataQualityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DeleteDeviceFleetRequest(ServiceRequest):
    DeviceFleetName: EntityName


class RetentionPolicy(TypedDict, total=False):
    """The retention policy for data stored on an Amazon Elastic File System
    volume.
    """

    HomeEfsFileSystem: Optional[RetentionType]


class DeleteDomainRequest(ServiceRequest):
    DomainId: DomainId
    RetentionPolicy: Optional[RetentionPolicy]


class DeleteEdgeDeploymentPlanRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName


class DeleteEdgeDeploymentStageRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName
    StageName: EntityName


class DeleteEndpointConfigInput(ServiceRequest):
    EndpointConfigName: EndpointConfigName


class DeleteEndpointInput(ServiceRequest):
    EndpointName: EndpointName


class DeleteExperimentRequest(ServiceRequest):
    ExperimentName: ExperimentEntityName


class DeleteExperimentResponse(TypedDict, total=False):
    ExperimentArn: Optional[ExperimentArn]


class DeleteFeatureGroupRequest(ServiceRequest):
    FeatureGroupName: FeatureGroupName


class DeleteFlowDefinitionRequest(ServiceRequest):
    FlowDefinitionName: FlowDefinitionName


class DeleteFlowDefinitionResponse(TypedDict, total=False):
    pass


class DeleteHubContentReferenceRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentType: HubContentType
    HubContentName: HubContentName


class DeleteHubContentRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentType: HubContentType
    HubContentName: HubContentName
    HubContentVersion: HubContentVersion


class DeleteHubRequest(ServiceRequest):
    HubName: HubNameOrArn


class DeleteHumanTaskUiRequest(ServiceRequest):
    HumanTaskUiName: HumanTaskUiName


class DeleteHumanTaskUiResponse(TypedDict, total=False):
    pass


class DeleteHyperParameterTuningJobRequest(ServiceRequest):
    HyperParameterTuningJobName: HyperParameterTuningJobName


class DeleteImageRequest(ServiceRequest):
    ImageName: ImageName


class DeleteImageResponse(TypedDict, total=False):
    pass


class DeleteImageVersionRequest(ServiceRequest):
    ImageName: ImageName
    Version: Optional[ImageVersionNumber]
    Alias: Optional[SageMakerImageVersionAlias]


class DeleteImageVersionResponse(TypedDict, total=False):
    pass


class DeleteInferenceComponentInput(ServiceRequest):
    InferenceComponentName: InferenceComponentName


class DeleteInferenceExperimentRequest(ServiceRequest):
    Name: InferenceExperimentName


class DeleteInferenceExperimentResponse(TypedDict, total=False):
    InferenceExperimentArn: InferenceExperimentArn


class DeleteMlflowTrackingServerRequest(ServiceRequest):
    TrackingServerName: TrackingServerName


class DeleteMlflowTrackingServerResponse(TypedDict, total=False):
    TrackingServerArn: Optional[TrackingServerArn]


class DeleteModelBiasJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DeleteModelCardRequest(ServiceRequest):
    ModelCardName: EntityName


class DeleteModelExplainabilityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DeleteModelInput(ServiceRequest):
    ModelName: ModelName


class DeleteModelPackageGroupInput(ServiceRequest):
    ModelPackageGroupName: ArnOrName


class DeleteModelPackageGroupPolicyInput(ServiceRequest):
    ModelPackageGroupName: EntityName


class DeleteModelPackageInput(ServiceRequest):
    ModelPackageName: VersionedArnOrName


class DeleteModelQualityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DeleteMonitoringScheduleRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName


class DeleteNotebookInstanceInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName


class DeleteNotebookInstanceLifecycleConfigInput(ServiceRequest):
    NotebookInstanceLifecycleConfigName: NotebookInstanceLifecycleConfigName


class DeleteOptimizationJobRequest(ServiceRequest):
    OptimizationJobName: EntityName


class DeletePartnerAppRequest(ServiceRequest):
    Arn: PartnerAppArn
    ClientToken: Optional[ClientToken]


class DeletePartnerAppResponse(TypedDict, total=False):
    Arn: Optional[PartnerAppArn]


class DeletePipelineRequest(ServiceRequest):
    PipelineName: PipelineName
    ClientRequestToken: IdempotencyToken


class DeletePipelineResponse(TypedDict, total=False):
    PipelineArn: Optional[PipelineArn]


class DeleteProjectInput(ServiceRequest):
    ProjectName: ProjectEntityName


class DeleteSpaceRequest(ServiceRequest):
    DomainId: DomainId
    SpaceName: SpaceName


class DeleteStudioLifecycleConfigRequest(ServiceRequest):
    StudioLifecycleConfigName: StudioLifecycleConfigName


TagKeyList = List[TagKey]


class DeleteTagsInput(ServiceRequest):
    ResourceArn: ResourceArn
    TagKeys: TagKeyList


class DeleteTagsOutput(TypedDict, total=False):
    pass


class DeleteTrialComponentRequest(ServiceRequest):
    TrialComponentName: ExperimentEntityName


class DeleteTrialComponentResponse(TypedDict, total=False):
    TrialComponentArn: Optional[TrialComponentArn]


class DeleteTrialRequest(ServiceRequest):
    TrialName: ExperimentEntityName


class DeleteTrialResponse(TypedDict, total=False):
    TrialArn: Optional[TrialArn]


class DeleteUserProfileRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: UserProfileName


class DeleteWorkforceRequest(ServiceRequest):
    WorkforceName: WorkforceName


class DeleteWorkforceResponse(TypedDict, total=False):
    pass


class DeleteWorkteamRequest(ServiceRequest):
    WorkteamName: WorkteamName


class DeleteWorkteamResponse(TypedDict, total=False):
    Success: Success


class DeployedImage(TypedDict, total=False):
    """Gets the Amazon EC2 Container Registry path of the docker image of the
    model that is hosted in this
    `ProductionVariant <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html>`__.

    If you used the ``registry/repository[:tag]`` form to specify the image
    path of the primary container when you created the model hosted in this
    ``ProductionVariant``, the path resolves to a path of the form
    ``registry/repository[@digest]``. A digest is a hash value that
    identifies a specific version of an image. For information about Amazon
    ECR paths, see `Pulling an
    Image <https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html>`__
    in the *Amazon ECR User Guide*.
    """

    SpecifiedImage: Optional[ContainerImage]
    ResolvedImage: Optional[ContainerImage]
    ResolutionTime: Optional[Timestamp]


DeployedImages = List[DeployedImage]


class RealTimeInferenceRecommendation(TypedDict, total=False):
    """The recommended configuration to use for Real-Time Inference."""

    RecommendationId: String
    InstanceType: ProductionVariantInstanceType
    Environment: Optional[EnvironmentMap]


RealTimeInferenceRecommendations = List[RealTimeInferenceRecommendation]


class DeploymentRecommendation(TypedDict, total=False):
    """A set of recommended deployment configurations for the model. To get
    more advanced recommendations, see
    `CreateInferenceRecommendationsJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html>`__
    to create an inference recommendation job.
    """

    RecommendationStatus: RecommendationStatus
    RealTimeInferenceRecommendations: Optional[RealTimeInferenceRecommendations]


class EdgeDeploymentStatus(TypedDict, total=False):
    """Contains information summarizing the deployment stage results."""

    StageStatus: StageStatus
    EdgeDeploymentSuccessInStage: Integer
    EdgeDeploymentPendingInStage: Integer
    EdgeDeploymentFailedInStage: Integer
    EdgeDeploymentStatusMessage: Optional[String]
    EdgeDeploymentStageStartTime: Optional[Timestamp]


class DeploymentStageStatusSummary(TypedDict, total=False):
    """Contains information summarizing the deployment stage results."""

    StageName: EntityName
    DeviceSelectionConfig: DeviceSelectionConfig
    DeploymentConfig: EdgeDeploymentConfig
    DeploymentStatus: EdgeDeploymentStatus


DeploymentStageStatusSummaries = List[DeploymentStageStatusSummary]


class DeregisterDevicesRequest(ServiceRequest):
    DeviceFleetName: EntityName
    DeviceNames: DeviceNames


class DerivedInformation(TypedDict, total=False):
    """Information that SageMaker Neo automatically derived about the model."""

    DerivedDataInputConfig: Optional[DataInputConfig]


class DescribeActionRequest(ServiceRequest):
    ActionName: ExperimentEntityNameOrArn


class DescribeActionResponse(TypedDict, total=False):
    ActionName: Optional[ExperimentEntityNameOrArn]
    ActionArn: Optional[ActionArn]
    Source: Optional[ActionSource]
    ActionType: Optional[String256]
    Description: Optional[ExperimentDescription]
    Status: Optional[ActionStatus]
    Properties: Optional[LineageEntityParameters]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    MetadataProperties: Optional[MetadataProperties]
    LineageGroupArn: Optional[LineageGroupArn]


class DescribeAlgorithmInput(ServiceRequest):
    AlgorithmName: ArnOrName


class DescribeAlgorithmOutput(TypedDict, total=False):
    AlgorithmName: EntityName
    AlgorithmArn: AlgorithmArn
    AlgorithmDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    TrainingSpecification: TrainingSpecification
    InferenceSpecification: Optional[InferenceSpecification]
    ValidationSpecification: Optional[AlgorithmValidationSpecification]
    AlgorithmStatus: AlgorithmStatus
    AlgorithmStatusDetails: AlgorithmStatusDetails
    ProductId: Optional[ProductId]
    CertifyForMarketplace: Optional[CertifyForMarketplace]


class DescribeAppImageConfigRequest(ServiceRequest):
    AppImageConfigName: AppImageConfigName


class DescribeAppImageConfigResponse(TypedDict, total=False):
    AppImageConfigArn: Optional[AppImageConfigArn]
    AppImageConfigName: Optional[AppImageConfigName]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfig]
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfig]
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfig]


class DescribeAppRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: Optional[UserProfileName]
    SpaceName: Optional[SpaceName]
    AppType: AppType
    AppName: AppName


class DescribeAppResponse(TypedDict, total=False):
    AppArn: Optional[AppArn]
    AppType: Optional[AppType]
    AppName: Optional[AppName]
    DomainId: Optional[DomainId]
    UserProfileName: Optional[UserProfileName]
    SpaceName: Optional[SpaceName]
    Status: Optional[AppStatus]
    RecoveryMode: Optional[Boolean]
    LastHealthCheckTimestamp: Optional[Timestamp]
    LastUserActivityTimestamp: Optional[Timestamp]
    CreationTime: Optional[Timestamp]
    FailureReason: Optional[FailureReason]
    ResourceSpec: Optional[ResourceSpec]
    BuiltInLifecycleConfigArn: Optional[StudioLifecycleConfigArn]


class DescribeArtifactRequest(ServiceRequest):
    ArtifactArn: ArtifactArn


class DescribeArtifactResponse(TypedDict, total=False):
    ArtifactName: Optional[ExperimentEntityNameOrArn]
    ArtifactArn: Optional[ArtifactArn]
    Source: Optional[ArtifactSource]
    ArtifactType: Optional[String256]
    Properties: Optional[LineageEntityParameters]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    MetadataProperties: Optional[MetadataProperties]
    LineageGroupArn: Optional[LineageGroupArn]


class DescribeAutoMLJobRequest(ServiceRequest):
    AutoMLJobName: AutoMLJobName


class ModelDeployResult(TypedDict, total=False):
    """Provides information about the endpoint of the model deployment."""

    EndpointName: Optional[EndpointName]


class ResolvedAttributes(TypedDict, total=False):
    """The resolved attributes."""

    AutoMLJobObjective: Optional[AutoMLJobObjective]
    ProblemType: Optional[ProblemType]
    CompletionCriteria: Optional[AutoMLJobCompletionCriteria]


class DescribeAutoMLJobResponse(TypedDict, total=False):
    AutoMLJobName: AutoMLJobName
    AutoMLJobArn: AutoMLJobArn
    InputDataConfig: AutoMLInputDataConfig
    OutputDataConfig: AutoMLOutputDataConfig
    RoleArn: RoleArn
    AutoMLJobObjective: Optional[AutoMLJobObjective]
    ProblemType: Optional[ProblemType]
    AutoMLJobConfig: Optional[AutoMLJobConfig]
    CreationTime: Timestamp
    EndTime: Optional[Timestamp]
    LastModifiedTime: Timestamp
    FailureReason: Optional[AutoMLFailureReason]
    PartialFailureReasons: Optional[AutoMLPartialFailureReasons]
    BestCandidate: Optional[AutoMLCandidate]
    AutoMLJobStatus: AutoMLJobStatus
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatus
    GenerateCandidateDefinitionsOnly: Optional[GenerateCandidateDefinitionsOnly]
    AutoMLJobArtifacts: Optional[AutoMLJobArtifacts]
    ResolvedAttributes: Optional[ResolvedAttributes]
    ModelDeployConfig: Optional[ModelDeployConfig]
    ModelDeployResult: Optional[ModelDeployResult]


class DescribeAutoMLJobV2Request(ServiceRequest):
    AutoMLJobName: AutoMLJobName


class DescribeAutoMLJobV2Response(TypedDict, total=False):
    AutoMLJobName: AutoMLJobName
    AutoMLJobArn: AutoMLJobArn
    AutoMLJobInputDataConfig: AutoMLJobInputDataConfig
    OutputDataConfig: AutoMLOutputDataConfig
    RoleArn: RoleArn
    AutoMLJobObjective: Optional[AutoMLJobObjective]
    AutoMLProblemTypeConfig: Optional[AutoMLProblemTypeConfig]
    AutoMLProblemTypeConfigName: Optional[AutoMLProblemTypeConfigName]
    CreationTime: Timestamp
    EndTime: Optional[Timestamp]
    LastModifiedTime: Timestamp
    FailureReason: Optional[AutoMLFailureReason]
    PartialFailureReasons: Optional[AutoMLPartialFailureReasons]
    BestCandidate: Optional[AutoMLCandidate]
    AutoMLJobStatus: AutoMLJobStatus
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatus
    AutoMLJobArtifacts: Optional[AutoMLJobArtifacts]
    ResolvedAttributes: Optional[AutoMLResolvedAttributes]
    ModelDeployConfig: Optional[ModelDeployConfig]
    ModelDeployResult: Optional[ModelDeployResult]
    DataSplitConfig: Optional[AutoMLDataSplitConfig]
    SecurityConfig: Optional[AutoMLSecurityConfig]
    AutoMLComputeConfig: Optional[AutoMLComputeConfig]


class DescribeClusterNodeRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn
    NodeId: ClusterNodeId


class DescribeClusterNodeResponse(TypedDict, total=False):
    NodeDetails: ClusterNodeDetails


class DescribeClusterRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn


class DescribeClusterResponse(TypedDict, total=False):
    ClusterArn: ClusterArn
    ClusterName: Optional[ClusterName]
    ClusterStatus: ClusterStatus
    CreationTime: Optional[Timestamp]
    FailureMessage: Optional[String]
    InstanceGroups: ClusterInstanceGroupDetailsList
    VpcConfig: Optional[VpcConfig]
    Orchestrator: Optional[ClusterOrchestrator]
    NodeRecovery: Optional[ClusterNodeRecovery]


class DescribeClusterSchedulerConfigRequest(ServiceRequest):
    ClusterSchedulerConfigId: ClusterSchedulerConfigId
    ClusterSchedulerConfigVersion: Optional[Integer]


class DescribeClusterSchedulerConfigResponse(TypedDict, total=False):
    ClusterSchedulerConfigArn: ClusterSchedulerConfigArn
    ClusterSchedulerConfigId: ClusterSchedulerConfigId
    Name: EntityName
    ClusterSchedulerConfigVersion: Integer
    Status: SchedulerResourceStatus
    FailureReason: Optional[FailureReason]
    ClusterArn: Optional[ClusterArn]
    SchedulerConfig: Optional[SchedulerConfig]
    Description: Optional[EntityDescription]
    CreationTime: Timestamp
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class DescribeCodeRepositoryInput(ServiceRequest):
    CodeRepositoryName: EntityName


class DescribeCodeRepositoryOutput(TypedDict, total=False):
    CodeRepositoryName: EntityName
    CodeRepositoryArn: CodeRepositoryArn
    CreationTime: CreationTime
    LastModifiedTime: LastModifiedTime
    GitConfig: Optional[GitConfig]


class DescribeCompilationJobRequest(ServiceRequest):
    CompilationJobName: EntityName


class ModelDigests(TypedDict, total=False):
    """Provides information to verify the integrity of stored model artifacts."""

    ArtifactDigest: Optional[ArtifactDigest]


class ModelArtifacts(TypedDict, total=False):
    """Provides information about the location that is configured for storing
    model artifacts.

    Model artifacts are outputs that result from training a model. They
    typically consist of trained parameters, a model definition that
    describes how to compute inferences, and other metadata. A SageMaker
    container stores your trained model artifacts in the ``/opt/ml/model``
    directory. After training has completed, by default, these artifacts are
    uploaded to your Amazon S3 bucket as compressed files.
    """

    S3ModelArtifacts: S3Uri


class DescribeCompilationJobResponse(TypedDict, total=False):
    CompilationJobName: EntityName
    CompilationJobArn: CompilationJobArn
    CompilationJobStatus: CompilationJobStatus
    CompilationStartTime: Optional[Timestamp]
    CompilationEndTime: Optional[Timestamp]
    StoppingCondition: StoppingCondition
    InferenceImage: Optional[InferenceImage]
    ModelPackageVersionArn: Optional[ModelPackageArn]
    CreationTime: CreationTime
    LastModifiedTime: LastModifiedTime
    FailureReason: FailureReason
    ModelArtifacts: ModelArtifacts
    ModelDigests: Optional[ModelDigests]
    RoleArn: RoleArn
    InputConfig: InputConfig
    OutputConfig: OutputConfig
    VpcConfig: Optional[NeoVpcConfig]
    DerivedInformation: Optional[DerivedInformation]


class DescribeComputeQuotaRequest(ServiceRequest):
    ComputeQuotaId: ComputeQuotaId
    ComputeQuotaVersion: Optional[Integer]


class DescribeComputeQuotaResponse(TypedDict, total=False):
    ComputeQuotaArn: ComputeQuotaArn
    ComputeQuotaId: ComputeQuotaId
    Name: EntityName
    Description: Optional[EntityDescription]
    ComputeQuotaVersion: Integer
    Status: SchedulerResourceStatus
    FailureReason: Optional[FailureReason]
    ClusterArn: Optional[ClusterArn]
    ComputeQuotaConfig: Optional[ComputeQuotaConfig]
    ComputeQuotaTarget: ComputeQuotaTarget
    ActivationState: Optional[ActivationState]
    CreationTime: Timestamp
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class DescribeContextRequest(ServiceRequest):
    ContextName: ContextNameOrArn


class DescribeContextResponse(TypedDict, total=False):
    ContextName: Optional[ContextName]
    ContextArn: Optional[ContextArn]
    Source: Optional[ContextSource]
    ContextType: Optional[String256]
    Description: Optional[ExperimentDescription]
    Properties: Optional[LineageEntityParameters]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    LineageGroupArn: Optional[LineageGroupArn]


class DescribeDataQualityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DescribeDataQualityJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn
    JobDefinitionName: MonitoringJobDefinitionName
    CreationTime: Timestamp
    DataQualityBaselineConfig: Optional[DataQualityBaselineConfig]
    DataQualityAppSpecification: DataQualityAppSpecification
    DataQualityJobInput: DataQualityJobInput
    DataQualityJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]


class DescribeDeviceFleetRequest(ServiceRequest):
    DeviceFleetName: EntityName


class DescribeDeviceFleetResponse(TypedDict, total=False):
    DeviceFleetName: EntityName
    DeviceFleetArn: DeviceFleetArn
    OutputConfig: EdgeOutputConfig
    Description: Optional[DeviceFleetDescription]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    RoleArn: Optional[RoleArn]
    IotRoleAlias: Optional[IotRoleAlias]


class DescribeDeviceRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    DeviceName: EntityName
    DeviceFleetName: EntityName


class EdgeModel(TypedDict, total=False):
    """The model on the edge device."""

    ModelName: EntityName
    ModelVersion: EdgeVersion
    LatestSampleTime: Optional[Timestamp]
    LatestInference: Optional[Timestamp]


EdgeModels = List[EdgeModel]


class DescribeDeviceResponse(TypedDict, total=False):
    DeviceArn: Optional[DeviceArn]
    DeviceName: EntityName
    Description: Optional[DeviceDescription]
    DeviceFleetName: EntityName
    IotThingName: Optional[ThingName]
    RegistrationTime: Timestamp
    LatestHeartbeat: Optional[Timestamp]
    Models: Optional[EdgeModels]
    MaxModels: Optional[Integer]
    NextToken: Optional[NextToken]
    AgentVersion: Optional[EdgeVersion]


class DescribeDomainRequest(ServiceRequest):
    DomainId: DomainId


class DescribeDomainResponse(TypedDict, total=False):
    DomainArn: Optional[DomainArn]
    DomainId: Optional[DomainId]
    DomainName: Optional[DomainName]
    HomeEfsFileSystemId: Optional[ResourceId]
    SingleSignOnManagedApplicationInstanceId: Optional[String256]
    SingleSignOnApplicationArn: Optional[SingleSignOnApplicationArn]
    Status: Optional[DomainStatus]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]
    FailureReason: Optional[FailureReason]
    SecurityGroupIdForDomainBoundary: Optional[SecurityGroupId]
    AuthMode: Optional[AuthMode]
    DefaultUserSettings: Optional[UserSettings]
    DomainSettings: Optional[DomainSettings]
    AppNetworkAccessType: Optional[AppNetworkAccessType]
    HomeEfsFileSystemKmsKeyId: Optional[KmsKeyId]
    SubnetIds: Optional[Subnets]
    Url: Optional[String1024]
    VpcId: Optional[VpcId]
    KmsKeyId: Optional[KmsKeyId]
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagement]
    TagPropagation: Optional[TagPropagation]
    DefaultSpaceSettings: Optional[DefaultSpaceSettings]


class DescribeEdgeDeploymentPlanRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName
    NextToken: Optional[NextToken]
    MaxResults: Optional[DeploymentStageMaxResults]


class DescribeEdgeDeploymentPlanResponse(TypedDict, total=False):
    EdgeDeploymentPlanArn: EdgeDeploymentPlanArn
    EdgeDeploymentPlanName: EntityName
    ModelConfigs: EdgeDeploymentModelConfigs
    DeviceFleetName: EntityName
    EdgeDeploymentSuccess: Optional[Integer]
    EdgeDeploymentPending: Optional[Integer]
    EdgeDeploymentFailed: Optional[Integer]
    Stages: DeploymentStageStatusSummaries
    NextToken: Optional[NextToken]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


class DescribeEdgePackagingJobRequest(ServiceRequest):
    EdgePackagingJobName: EntityName


class EdgePresetDeploymentOutput(TypedDict, total=False):
    """The output of a SageMaker Edge Manager deployable resource."""

    Type: EdgePresetDeploymentType
    Artifact: Optional[EdgePresetDeploymentArtifact]
    Status: Optional[EdgePresetDeploymentStatus]
    StatusMessage: Optional[String]


class DescribeEdgePackagingJobResponse(TypedDict, total=False):
    EdgePackagingJobArn: EdgePackagingJobArn
    EdgePackagingJobName: EntityName
    CompilationJobName: Optional[EntityName]
    ModelName: Optional[EntityName]
    ModelVersion: Optional[EdgeVersion]
    RoleArn: Optional[RoleArn]
    OutputConfig: Optional[EdgeOutputConfig]
    ResourceKey: Optional[KmsKeyId]
    EdgePackagingJobStatus: EdgePackagingJobStatus
    EdgePackagingJobStatusMessage: Optional[String]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    ModelArtifact: Optional[S3Uri]
    ModelSignature: Optional[String]
    PresetDeploymentOutput: Optional[EdgePresetDeploymentOutput]


class DescribeEndpointConfigInput(ServiceRequest):
    EndpointConfigName: EndpointConfigName


class DescribeEndpointConfigOutput(TypedDict, total=False):
    EndpointConfigName: EndpointConfigName
    EndpointConfigArn: EndpointConfigArn
    ProductionVariants: ProductionVariantList
    DataCaptureConfig: Optional[DataCaptureConfig]
    KmsKeyId: Optional[KmsKeyId]
    CreationTime: Timestamp
    AsyncInferenceConfig: Optional[AsyncInferenceConfig]
    ExplainerConfig: Optional[ExplainerConfig]
    ShadowProductionVariants: Optional[ProductionVariantList]
    ExecutionRoleArn: Optional[RoleArn]
    VpcConfig: Optional[VpcConfig]
    EnableNetworkIsolation: Optional[Boolean]


class DescribeEndpointInput(ServiceRequest):
    EndpointName: EndpointName


class Ec2CapacityReservation(TypedDict, total=False):
    """The EC2 capacity reservations that are shared to an ML capacity
    reservation.
    """

    Ec2CapacityReservationId: Optional[Ec2CapacityReservationId]
    TotalInstanceCount: Optional[TaskCount]
    AvailableInstanceCount: Optional[TaskCount]
    UsedByCurrentEndpoint: Optional[TaskCount]


Ec2CapacityReservationsList = List[Ec2CapacityReservation]


class ProductionVariantCapacityReservationSummary(TypedDict, total=False):
    """Details about an ML capacity reservation."""

    MlReservationArn: Optional[MlReservationArn]
    CapacityReservationPreference: Optional[CapacityReservationPreference]
    TotalInstanceCount: Optional[TaskCount]
    AvailableInstanceCount: Optional[TaskCount]
    UsedByCurrentEndpoint: Optional[TaskCount]
    Ec2CapacityReservations: Optional[Ec2CapacityReservationsList]


class ProductionVariantStatus(TypedDict, total=False):
    """Describes the status of the production variant."""

    Status: VariantStatus
    StatusMessage: Optional[VariantStatusMessage]
    StartTime: Optional[Timestamp]


ProductionVariantStatusList = List[ProductionVariantStatus]


class ProductionVariantSummary(TypedDict, total=False):
    """Describes weight and capacities for a production variant associated with
    an endpoint. If you sent a request to the
    ``UpdateEndpointWeightsAndCapacities`` API and the endpoint status is
    ``Updating``, you get different desired and current values.
    """

    VariantName: VariantName
    DeployedImages: Optional[DeployedImages]
    CurrentWeight: Optional[VariantWeight]
    DesiredWeight: Optional[VariantWeight]
    CurrentInstanceCount: Optional[TaskCount]
    DesiredInstanceCount: Optional[TaskCount]
    VariantStatus: Optional[ProductionVariantStatusList]
    CurrentServerlessConfig: Optional[ProductionVariantServerlessConfig]
    DesiredServerlessConfig: Optional[ProductionVariantServerlessConfig]
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScaling]
    RoutingConfig: Optional[ProductionVariantRoutingConfig]
    CapacityReservationConfig: Optional[ProductionVariantCapacityReservationSummary]


ProductionVariantSummaryList = List[ProductionVariantSummary]


class PendingProductionVariantSummary(TypedDict, total=False):
    """The production variant summary for a deployment when an endpoint is
    creating or updating with the
    `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__
    or
    `UpdateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html>`__
    operations. Describes the ``VariantStatus``, weight and capacity for a
    production variant associated with an endpoint.
    """

    VariantName: VariantName
    DeployedImages: Optional[DeployedImages]
    CurrentWeight: Optional[VariantWeight]
    DesiredWeight: Optional[VariantWeight]
    CurrentInstanceCount: Optional[TaskCount]
    DesiredInstanceCount: Optional[TaskCount]
    InstanceType: Optional[ProductionVariantInstanceType]
    AcceleratorType: Optional[ProductionVariantAcceleratorType]
    VariantStatus: Optional[ProductionVariantStatusList]
    CurrentServerlessConfig: Optional[ProductionVariantServerlessConfig]
    DesiredServerlessConfig: Optional[ProductionVariantServerlessConfig]
    ManagedInstanceScaling: Optional[ProductionVariantManagedInstanceScaling]
    RoutingConfig: Optional[ProductionVariantRoutingConfig]


PendingProductionVariantSummaryList = List[PendingProductionVariantSummary]


class PendingDeploymentSummary(TypedDict, total=False):
    """The summary of an in-progress deployment when an endpoint is creating or
    updating with a new endpoint configuration.
    """

    EndpointConfigName: EndpointConfigName
    ProductionVariants: Optional[PendingProductionVariantSummaryList]
    StartTime: Optional[Timestamp]
    ShadowProductionVariants: Optional[PendingProductionVariantSummaryList]


class DescribeEndpointOutput(TypedDict, total=False):
    EndpointName: EndpointName
    EndpointArn: EndpointArn
    EndpointConfigName: Optional[EndpointConfigName]
    ProductionVariants: Optional[ProductionVariantSummaryList]
    DataCaptureConfig: Optional[DataCaptureConfigSummary]
    EndpointStatus: EndpointStatus
    FailureReason: Optional[FailureReason]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    LastDeploymentConfig: Optional[DeploymentConfig]
    AsyncInferenceConfig: Optional[AsyncInferenceConfig]
    PendingDeploymentSummary: Optional[PendingDeploymentSummary]
    ExplainerConfig: Optional[ExplainerConfig]
    ShadowProductionVariants: Optional[ProductionVariantSummaryList]


class DescribeExperimentRequest(ServiceRequest):
    ExperimentName: ExperimentEntityName


class ExperimentSource(TypedDict, total=False):
    """The source of the experiment."""

    SourceArn: ExperimentSourceArn
    SourceType: Optional[SourceType]


class DescribeExperimentResponse(TypedDict, total=False):
    ExperimentName: Optional[ExperimentEntityName]
    ExperimentArn: Optional[ExperimentArn]
    DisplayName: Optional[ExperimentEntityName]
    Source: Optional[ExperimentSource]
    Description: Optional[ExperimentDescription]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class DescribeFeatureGroupRequest(ServiceRequest):
    FeatureGroupName: FeatureGroupNameOrArn
    NextToken: Optional[NextToken]


OnlineStoreTotalSizeBytes = int


class LastUpdateStatus(TypedDict, total=False):
    """A value that indicates whether the update was successful."""

    Status: LastUpdateStatusValue
    FailureReason: Optional[FailureReason]


class OfflineStoreStatus(TypedDict, total=False):
    """The status of ``OfflineStore``."""

    Status: OfflineStoreStatusValue
    BlockedReason: Optional[BlockedReason]


class ThroughputConfigDescription(TypedDict, total=False):
    """Active throughput configuration of the feature group. There are two
    modes: ``ON_DEMAND`` and ``PROVISIONED``. With on-demand mode, you are
    charged for data reads and writes that your application performs on your
    feature group. You do not need to specify read and write throughput
    because Feature Store accommodates your workloads as they ramp up and
    down. You can switch a feature group to on-demand only once in a 24 hour
    period. With provisioned throughput mode, you specify the read and write
    capacity per second that you expect your application to require, and you
    are billed based on those limits. Exceeding provisioned throughput will
    result in your requests being throttled.

    Note: ``PROVISIONED`` throughput mode is supported only for feature
    groups that are offline-only, or use the
    ```Standard`` <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType>`__
    tier online store.
    """

    ThroughputMode: ThroughputMode
    ProvisionedReadCapacityUnits: Optional[CapacityUnit]
    ProvisionedWriteCapacityUnits: Optional[CapacityUnit]


class DescribeFeatureGroupResponse(TypedDict, total=False):
    FeatureGroupArn: FeatureGroupArn
    FeatureGroupName: FeatureGroupName
    RecordIdentifierFeatureName: FeatureName
    EventTimeFeatureName: FeatureName
    FeatureDefinitions: FeatureDefinitions
    CreationTime: CreationTime
    LastModifiedTime: Optional[LastModifiedTime]
    OnlineStoreConfig: Optional[OnlineStoreConfig]
    OfflineStoreConfig: Optional[OfflineStoreConfig]
    ThroughputConfig: Optional[ThroughputConfigDescription]
    RoleArn: Optional[RoleArn]
    FeatureGroupStatus: Optional[FeatureGroupStatus]
    OfflineStoreStatus: Optional[OfflineStoreStatus]
    LastUpdateStatus: Optional[LastUpdateStatus]
    FailureReason: Optional[FailureReason]
    Description: Optional[Description]
    NextToken: NextToken
    OnlineStoreTotalSizeBytes: Optional[OnlineStoreTotalSizeBytes]


class DescribeFeatureMetadataRequest(ServiceRequest):
    FeatureGroupName: FeatureGroupNameOrArn
    FeatureName: FeatureName


class FeatureParameter(TypedDict, total=False):
    """A key-value pair that you specify to describe the feature."""

    Key: Optional[FeatureParameterKey]
    Value: Optional[FeatureParameterValue]


FeatureParameters = List[FeatureParameter]


class DescribeFeatureMetadataResponse(TypedDict, total=False):
    FeatureGroupArn: FeatureGroupArn
    FeatureGroupName: FeatureGroupName
    FeatureName: FeatureName
    FeatureType: FeatureType
    CreationTime: CreationTime
    LastModifiedTime: LastModifiedTime
    Description: Optional[FeatureDescription]
    Parameters: Optional[FeatureParameters]


class DescribeFlowDefinitionRequest(ServiceRequest):
    FlowDefinitionName: FlowDefinitionName


class DescribeFlowDefinitionResponse(TypedDict, total=False):
    FlowDefinitionArn: FlowDefinitionArn
    FlowDefinitionName: FlowDefinitionName
    FlowDefinitionStatus: FlowDefinitionStatus
    CreationTime: Timestamp
    HumanLoopRequestSource: Optional[HumanLoopRequestSource]
    HumanLoopActivationConfig: Optional[HumanLoopActivationConfig]
    HumanLoopConfig: Optional[HumanLoopConfig]
    OutputConfig: FlowDefinitionOutputConfig
    RoleArn: RoleArn
    FailureReason: Optional[FailureReason]


class DescribeHubContentRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentType: HubContentType
    HubContentName: HubContentName
    HubContentVersion: Optional[HubContentVersion]


class HubContentDependency(TypedDict, total=False):
    """Any dependencies related to hub content, such as scripts, model
    artifacts, datasets, or notebooks.
    """

    DependencyOriginPath: Optional[DependencyOriginPath]
    DependencyCopyPath: Optional[DependencyCopyPath]


HubContentDependencyList = List[HubContentDependency]
HubContentSearchKeywordList = List[HubSearchKeyword]


class DescribeHubContentResponse(TypedDict, total=False):
    HubContentName: HubContentName
    HubContentArn: HubContentArn
    HubContentVersion: HubContentVersion
    HubContentType: HubContentType
    DocumentSchemaVersion: DocumentSchemaVersion
    HubName: HubName
    HubArn: HubArn
    HubContentDisplayName: Optional[HubContentDisplayName]
    HubContentDescription: Optional[HubContentDescription]
    HubContentMarkdown: Optional[HubContentMarkdown]
    HubContentDocument: HubContentDocument
    SageMakerPublicHubContentArn: Optional[SageMakerPublicHubContentArn]
    ReferenceMinVersion: Optional[ReferenceMinVersion]
    SupportStatus: Optional[HubContentSupportStatus]
    HubContentSearchKeywords: Optional[HubContentSearchKeywordList]
    HubContentDependencies: Optional[HubContentDependencyList]
    HubContentStatus: HubContentStatus
    FailureReason: Optional[FailureReason]
    CreationTime: Timestamp
    LastModifiedTime: Optional[Timestamp]


class DescribeHubRequest(ServiceRequest):
    HubName: HubNameOrArn


class DescribeHubResponse(TypedDict, total=False):
    HubName: HubName
    HubArn: HubArn
    HubDisplayName: Optional[HubDisplayName]
    HubDescription: Optional[HubDescription]
    HubSearchKeywords: Optional[HubSearchKeywordList]
    S3StorageConfig: Optional[HubS3StorageConfig]
    HubStatus: HubStatus
    FailureReason: Optional[FailureReason]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp


class DescribeHumanTaskUiRequest(ServiceRequest):
    HumanTaskUiName: HumanTaskUiName


class UiTemplateInfo(TypedDict, total=False):
    """Container for user interface template information."""

    Url: Optional[TemplateUrl]
    ContentSha256: Optional[TemplateContentSha256]


class DescribeHumanTaskUiResponse(TypedDict, total=False):
    HumanTaskUiArn: HumanTaskUiArn
    HumanTaskUiName: HumanTaskUiName
    HumanTaskUiStatus: Optional[HumanTaskUiStatus]
    CreationTime: Timestamp
    UiTemplate: UiTemplateInfo


class DescribeHyperParameterTuningJobRequest(ServiceRequest):
    HyperParameterTuningJobName: HyperParameterTuningJobName


class HyperParameterTuningJobConsumedResources(TypedDict, total=False):
    """The total resources consumed by your hyperparameter tuning job."""

    RuntimeInSeconds: Optional[Integer]


class HyperParameterTuningJobCompletionDetails(TypedDict, total=False):
    """A structure that contains runtime information about both current and
    completed hyperparameter tuning jobs.
    """

    NumberOfTrainingJobsObjectiveNotImproving: Optional[Integer]
    ConvergenceDetectedTime: Optional[Timestamp]


class FinalHyperParameterTuningJobObjectiveMetric(TypedDict, total=False):
    """Shows the latest objective metric emitted by a training job that was
    launched by a hyperparameter tuning job. You define the objective metric
    in the ``HyperParameterTuningJobObjective`` parameter of
    `HyperParameterTuningJobConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html>`__.
    """

    Type: Optional[HyperParameterTuningJobObjectiveType]
    MetricName: MetricName
    Value: MetricValue


class HyperParameterTrainingJobSummary(TypedDict, total=False):
    """The container for the summary information about a training job."""

    TrainingJobDefinitionName: Optional[HyperParameterTrainingJobDefinitionName]
    TrainingJobName: TrainingJobName
    TrainingJobArn: TrainingJobArn
    TuningJobName: Optional[HyperParameterTuningJobName]
    CreationTime: Timestamp
    TrainingStartTime: Optional[Timestamp]
    TrainingEndTime: Optional[Timestamp]
    TrainingJobStatus: TrainingJobStatus
    TunedHyperParameters: HyperParameters
    FailureReason: Optional[FailureReason]
    FinalHyperParameterTuningJobObjectiveMetric: Optional[
        FinalHyperParameterTuningJobObjectiveMetric
    ]
    ObjectiveStatus: Optional[ObjectiveStatus]


class ObjectiveStatusCounters(TypedDict, total=False):
    """Specifies the number of training jobs that this hyperparameter tuning
    job launched, categorized by the status of their objective metric. The
    objective metric status shows whether the final objective metric for the
    training job has been evaluated by the tuning job and used in the
    hyperparameter tuning process.
    """

    Succeeded: Optional[ObjectiveStatusCounter]
    Pending: Optional[ObjectiveStatusCounter]
    Failed: Optional[ObjectiveStatusCounter]


class TrainingJobStatusCounters(TypedDict, total=False):
    """The numbers of training jobs launched by a hyperparameter tuning job,
    categorized by status.
    """

    Completed: Optional[TrainingJobStatusCounter]
    InProgress: Optional[TrainingJobStatusCounter]
    RetryableError: Optional[TrainingJobStatusCounter]
    NonRetryableError: Optional[TrainingJobStatusCounter]
    Stopped: Optional[TrainingJobStatusCounter]


class DescribeHyperParameterTuningJobResponse(TypedDict, total=False):
    HyperParameterTuningJobName: HyperParameterTuningJobName
    HyperParameterTuningJobArn: HyperParameterTuningJobArn
    HyperParameterTuningJobConfig: HyperParameterTuningJobConfig
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinition]
    TrainingJobDefinitions: Optional[HyperParameterTrainingJobDefinitions]
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatus
    CreationTime: Timestamp
    HyperParameterTuningEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    TrainingJobStatusCounters: TrainingJobStatusCounters
    ObjectiveStatusCounters: ObjectiveStatusCounters
    BestTrainingJob: Optional[HyperParameterTrainingJobSummary]
    OverallBestTrainingJob: Optional[HyperParameterTrainingJobSummary]
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfig]
    Autotune: Optional[Autotune]
    FailureReason: Optional[FailureReason]
    TuningJobCompletionDetails: Optional[HyperParameterTuningJobCompletionDetails]
    ConsumedResources: Optional[HyperParameterTuningJobConsumedResources]


class DescribeImageRequest(ServiceRequest):
    ImageName: ImageName


class DescribeImageResponse(TypedDict, total=False):
    CreationTime: Optional[Timestamp]
    Description: Optional[ImageDescription]
    DisplayName: Optional[ImageDisplayName]
    FailureReason: Optional[FailureReason]
    ImageArn: Optional[ImageArn]
    ImageName: Optional[ImageName]
    ImageStatus: Optional[ImageStatus]
    LastModifiedTime: Optional[Timestamp]
    RoleArn: Optional[RoleArn]


class DescribeImageVersionRequest(ServiceRequest):
    ImageName: ImageName
    Version: Optional[ImageVersionNumber]
    Alias: Optional[SageMakerImageVersionAlias]


class DescribeImageVersionResponse(TypedDict, total=False):
    BaseImage: Optional[ImageBaseImage]
    ContainerImage: Optional[ImageContainerImage]
    CreationTime: Optional[Timestamp]
    FailureReason: Optional[FailureReason]
    ImageArn: Optional[ImageArn]
    ImageVersionArn: Optional[ImageVersionArn]
    ImageVersionStatus: Optional[ImageVersionStatus]
    LastModifiedTime: Optional[Timestamp]
    Version: Optional[ImageVersionNumber]
    VendorGuidance: Optional[VendorGuidance]
    JobType: Optional[JobType]
    MLFramework: Optional[MLFramework]
    ProgrammingLang: Optional[ProgrammingLang]
    Processor: Optional[Processor]
    Horovod: Optional[Horovod]
    ReleaseNotes: Optional[ReleaseNotes]


class DescribeInferenceComponentInput(ServiceRequest):
    InferenceComponentName: InferenceComponentName


class InferenceComponentCapacitySize(TypedDict, total=False):
    """Specifies the type and size of the endpoint capacity to activate for a
    rolling deployment or a rollback strategy. You can specify your batches
    as either of the following:

    -  A count of inference component copies

    -  The overall percentage or your fleet

    For a rollback strategy, if you don't specify the fields in this object,
    or if you set the ``Value`` parameter to 100%, then SageMaker AI uses a
    blue/green rollback strategy and rolls all traffic back to the blue
    fleet.
    """

    Type: InferenceComponentCapacitySizeType
    Value: CapacitySizeValue


class InferenceComponentRollingUpdatePolicy(TypedDict, total=False):
    """Specifies a rolling deployment strategy for updating a SageMaker AI
    inference component.
    """

    MaximumBatchSize: InferenceComponentCapacitySize
    WaitIntervalInSeconds: WaitIntervalInSeconds
    MaximumExecutionTimeoutInSeconds: Optional[MaximumExecutionTimeoutInSeconds]
    RollbackMaximumBatchSize: Optional[InferenceComponentCapacitySize]


class InferenceComponentDeploymentConfig(TypedDict, total=False):
    """The deployment configuration for an endpoint that hosts inference
    components. The configuration includes the desired deployment strategy
    and rollback settings.
    """

    RollingUpdatePolicy: InferenceComponentRollingUpdatePolicy
    AutoRollbackConfiguration: Optional[AutoRollbackConfig]


class InferenceComponentRuntimeConfigSummary(TypedDict, total=False):
    """Details about the runtime settings for the model that is deployed with
    the inference component.
    """

    DesiredCopyCount: Optional[InferenceComponentCopyCount]
    CurrentCopyCount: Optional[InferenceComponentCopyCount]


class InferenceComponentContainerSpecificationSummary(TypedDict, total=False):
    """Details about the resources that are deployed with this inference
    component.
    """

    DeployedImage: Optional[DeployedImage]
    ArtifactUrl: Optional[Url]
    Environment: Optional[EnvironmentMap]


class InferenceComponentSpecificationSummary(TypedDict, total=False):
    """Details about the resources that are deployed with this inference
    component.
    """

    ModelName: Optional[ModelName]
    Container: Optional[InferenceComponentContainerSpecificationSummary]
    StartupParameters: Optional[InferenceComponentStartupParameters]
    ComputeResourceRequirements: Optional[InferenceComponentComputeResourceRequirements]
    BaseInferenceComponentName: Optional[InferenceComponentName]


class DescribeInferenceComponentOutput(TypedDict, total=False):
    InferenceComponentName: InferenceComponentName
    InferenceComponentArn: InferenceComponentArn
    EndpointName: EndpointName
    EndpointArn: EndpointArn
    VariantName: Optional[VariantName]
    FailureReason: Optional[FailureReason]
    Specification: Optional[InferenceComponentSpecificationSummary]
    RuntimeConfig: Optional[InferenceComponentRuntimeConfigSummary]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    InferenceComponentStatus: Optional[InferenceComponentStatus]
    LastDeploymentConfig: Optional[InferenceComponentDeploymentConfig]


class DescribeInferenceExperimentRequest(ServiceRequest):
    Name: InferenceExperimentName


class ModelVariantConfigSummary(TypedDict, total=False):
    """Summary of the deployment configuration of a model."""

    ModelName: ModelName
    VariantName: ModelVariantName
    InfrastructureConfig: ModelInfrastructureConfig
    Status: ModelVariantStatus


ModelVariantConfigSummaryList = List[ModelVariantConfigSummary]


class EndpointMetadata(TypedDict, total=False):
    """The metadata of the endpoint."""

    EndpointName: EndpointName
    EndpointConfigName: Optional[EndpointConfigName]
    EndpointStatus: Optional[EndpointStatus]
    FailureReason: Optional[FailureReason]


class DescribeInferenceExperimentResponse(TypedDict, total=False):
    Arn: InferenceExperimentArn
    Name: InferenceExperimentName
    Type: InferenceExperimentType
    Schedule: Optional[InferenceExperimentSchedule]
    Status: InferenceExperimentStatus
    StatusReason: Optional[InferenceExperimentStatusReason]
    Description: Optional[InferenceExperimentDescription]
    CreationTime: Optional[Timestamp]
    CompletionTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    RoleArn: Optional[RoleArn]
    EndpointMetadata: EndpointMetadata
    ModelVariants: ModelVariantConfigSummaryList
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfig]
    ShadowModeConfig: Optional[ShadowModeConfig]
    KmsKey: Optional[KmsKeyId]


class DescribeInferenceRecommendationsJobRequest(ServiceRequest):
    JobName: RecommendationJobName


class InferenceMetrics(TypedDict, total=False):
    """The metrics for an existing endpoint compared in an Inference
    Recommender job.
    """

    MaxInvocations: Integer
    ModelLatency: Integer


class EndpointPerformance(TypedDict, total=False):
    """The performance results from running an Inference Recommender job on an
    existing endpoint.
    """

    Metrics: InferenceMetrics
    EndpointInfo: EndpointInfo


EndpointPerformances = List[EndpointPerformance]
InvocationStartTime = datetime
InvocationEndTime = datetime


class EnvironmentParameter(TypedDict, total=False):
    """A list of environment parameters suggested by the Amazon SageMaker
    Inference Recommender.
    """

    Key: String
    ValueType: String
    Value: String


EnvironmentParameters = List[EnvironmentParameter]


class ModelConfiguration(TypedDict, total=False):
    """Defines the model configuration. Includes the specification name and
    environment parameters.
    """

    InferenceSpecificationName: Optional[InferenceSpecificationName]
    EnvironmentParameters: Optional[EnvironmentParameters]
    CompilationJobName: Optional[RecommendationJobCompilationJobName]


class EndpointOutputConfiguration(TypedDict, total=False):
    """The endpoint configuration made by Inference Recommender during a
    recommendation job.
    """

    EndpointName: String
    VariantName: String
    InstanceType: Optional[ProductionVariantInstanceType]
    InitialInstanceCount: Optional[InitialInstanceCount]
    ServerlessConfig: Optional[ProductionVariantServerlessConfig]


class RecommendationMetrics(TypedDict, total=False):
    """The metrics of recommendations."""

    CostPerHour: Optional[Float]
    CostPerInference: Optional[Float]
    MaxInvocations: Optional[Integer]
    ModelLatency: Optional[Integer]
    CpuUtilization: Optional[UtilizationMetric]
    MemoryUtilization: Optional[UtilizationMetric]
    ModelSetupTime: Optional[ModelSetupTime]


class InferenceRecommendation(TypedDict, total=False):
    """A list of recommendations made by Amazon SageMaker Inference
    Recommender.
    """

    RecommendationId: Optional[String]
    Metrics: Optional[RecommendationMetrics]
    EndpointConfiguration: EndpointOutputConfiguration
    ModelConfiguration: ModelConfiguration
    InvocationEndTime: Optional[InvocationEndTime]
    InvocationStartTime: Optional[InvocationStartTime]


InferenceRecommendations = List[InferenceRecommendation]


class DescribeInferenceRecommendationsJobResponse(TypedDict, total=False):
    JobName: RecommendationJobName
    JobDescription: Optional[RecommendationJobDescription]
    JobType: RecommendationJobType
    JobArn: RecommendationJobArn
    RoleArn: RoleArn
    Status: RecommendationJobStatus
    CreationTime: CreationTime
    CompletionTime: Optional[Timestamp]
    LastModifiedTime: LastModifiedTime
    FailureReason: Optional[FailureReason]
    InputConfig: RecommendationJobInputConfig
    StoppingConditions: Optional[RecommendationJobStoppingConditions]
    InferenceRecommendations: Optional[InferenceRecommendations]
    EndpointPerformances: Optional[EndpointPerformances]


class DescribeLabelingJobRequest(ServiceRequest):
    LabelingJobName: LabelingJobName


class LabelingJobOutput(TypedDict, total=False):
    """Specifies the location of the output produced by the labeling job."""

    OutputDatasetS3Uri: S3Uri
    FinalActiveLearningModelArn: Optional[ModelArn]


class LabelCounters(TypedDict, total=False):
    """Provides a breakdown of the number of objects labeled."""

    TotalLabeled: Optional[LabelCounter]
    HumanLabeled: Optional[LabelCounter]
    MachineLabeled: Optional[LabelCounter]
    FailedNonRetryableError: Optional[LabelCounter]
    Unlabeled: Optional[LabelCounter]


class DescribeLabelingJobResponse(TypedDict, total=False):
    LabelingJobStatus: LabelingJobStatus
    LabelCounters: LabelCounters
    FailureReason: Optional[FailureReason]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    JobReferenceCode: JobReferenceCode
    LabelingJobName: LabelingJobName
    LabelingJobArn: LabelingJobArn
    LabelAttributeName: Optional[LabelAttributeName]
    InputConfig: LabelingJobInputConfig
    OutputConfig: LabelingJobOutputConfig
    RoleArn: RoleArn
    LabelCategoryConfigS3Uri: Optional[S3Uri]
    StoppingConditions: Optional[LabelingJobStoppingConditions]
    LabelingJobAlgorithmsConfig: Optional[LabelingJobAlgorithmsConfig]
    HumanTaskConfig: HumanTaskConfig
    Tags: Optional[TagList]
    LabelingJobOutput: Optional[LabelingJobOutput]


class DescribeLineageGroupRequest(ServiceRequest):
    LineageGroupName: ExperimentEntityName


class DescribeLineageGroupResponse(TypedDict, total=False):
    LineageGroupName: Optional[ExperimentEntityName]
    LineageGroupArn: Optional[LineageGroupArn]
    DisplayName: Optional[ExperimentEntityName]
    Description: Optional[ExperimentDescription]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class DescribeMlflowTrackingServerRequest(ServiceRequest):
    TrackingServerName: TrackingServerName


class DescribeMlflowTrackingServerResponse(TypedDict, total=False):
    TrackingServerArn: Optional[TrackingServerArn]
    TrackingServerName: Optional[TrackingServerName]
    ArtifactStoreUri: Optional[S3Uri]
    TrackingServerSize: Optional[TrackingServerSize]
    MlflowVersion: Optional[MlflowVersion]
    RoleArn: Optional[RoleArn]
    TrackingServerStatus: Optional[TrackingServerStatus]
    TrackingServerMaintenanceStatus: Optional[TrackingServerMaintenanceStatus]
    IsActive: Optional[IsTrackingServerActive]
    TrackingServerUrl: Optional[TrackingServerUrl]
    WeeklyMaintenanceWindowStart: Optional[WeeklyMaintenanceWindowStart]
    AutomaticModelRegistration: Optional[Boolean]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class DescribeModelBiasJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DescribeModelBiasJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn
    JobDefinitionName: MonitoringJobDefinitionName
    CreationTime: Timestamp
    ModelBiasBaselineConfig: Optional[ModelBiasBaselineConfig]
    ModelBiasAppSpecification: ModelBiasAppSpecification
    ModelBiasJobInput: ModelBiasJobInput
    ModelBiasJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]


class DescribeModelCardExportJobRequest(ServiceRequest):
    ModelCardExportJobArn: ModelCardExportJobArn


class ModelCardExportArtifacts(TypedDict, total=False):
    """The artifacts of the model card export job."""

    S3ExportArtifacts: S3Uri


class DescribeModelCardExportJobResponse(TypedDict, total=False):
    ModelCardExportJobName: EntityName
    ModelCardExportJobArn: ModelCardExportJobArn
    Status: ModelCardExportJobStatus
    ModelCardName: EntityName
    ModelCardVersion: Integer
    OutputConfig: ModelCardExportOutputConfig
    CreatedAt: Timestamp
    LastModifiedAt: Timestamp
    FailureReason: Optional[FailureReason]
    ExportArtifacts: Optional[ModelCardExportArtifacts]


class DescribeModelCardRequest(ServiceRequest):
    ModelCardName: ModelCardNameOrArn
    ModelCardVersion: Optional[Integer]


class DescribeModelCardResponse(TypedDict, total=False):
    ModelCardArn: ModelCardArn
    ModelCardName: EntityName
    ModelCardVersion: Integer
    Content: ModelCardContent
    ModelCardStatus: ModelCardStatus
    SecurityConfig: Optional[ModelCardSecurityConfig]
    CreationTime: Timestamp
    CreatedBy: UserContext
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    ModelCardProcessingStatus: Optional[ModelCardProcessingStatus]


class DescribeModelExplainabilityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DescribeModelExplainabilityJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn
    JobDefinitionName: MonitoringJobDefinitionName
    CreationTime: Timestamp
    ModelExplainabilityBaselineConfig: Optional[ModelExplainabilityBaselineConfig]
    ModelExplainabilityAppSpecification: ModelExplainabilityAppSpecification
    ModelExplainabilityJobInput: ModelExplainabilityJobInput
    ModelExplainabilityJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]


class DescribeModelInput(ServiceRequest):
    ModelName: ModelName


class DescribeModelOutput(TypedDict, total=False):
    ModelName: ModelName
    PrimaryContainer: Optional[ContainerDefinition]
    Containers: Optional[ContainerDefinitionList]
    InferenceExecutionConfig: Optional[InferenceExecutionConfig]
    ExecutionRoleArn: Optional[RoleArn]
    VpcConfig: Optional[VpcConfig]
    CreationTime: Timestamp
    ModelArn: ModelArn
    EnableNetworkIsolation: Optional[Boolean]
    DeploymentRecommendation: Optional[DeploymentRecommendation]


class DescribeModelPackageGroupInput(ServiceRequest):
    ModelPackageGroupName: ArnOrName


class DescribeModelPackageGroupOutput(TypedDict, total=False):
    ModelPackageGroupName: EntityName
    ModelPackageGroupArn: ModelPackageGroupArn
    ModelPackageGroupDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    CreatedBy: UserContext
    ModelPackageGroupStatus: ModelPackageGroupStatus


class DescribeModelPackageInput(ServiceRequest):
    ModelPackageName: VersionedArnOrName


class ModelPackageStatusItem(TypedDict, total=False):
    """Represents the overall status of a model package."""

    Name: EntityName
    Status: DetailedModelPackageStatus
    FailureReason: Optional[String]


ModelPackageStatusItemList = List[ModelPackageStatusItem]


class ModelPackageStatusDetails(TypedDict, total=False):
    """Specifies the validation and image scan statuses of the model package."""

    ValidationStatuses: ModelPackageStatusItemList
    ImageScanStatuses: Optional[ModelPackageStatusItemList]


class DescribeModelPackageOutput(TypedDict, total=False):
    ModelPackageName: EntityName
    ModelPackageGroupName: Optional[EntityName]
    ModelPackageVersion: Optional[ModelPackageVersion]
    ModelPackageArn: ModelPackageArn
    ModelPackageDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    InferenceSpecification: Optional[InferenceSpecification]
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecification]
    ValidationSpecification: Optional[ModelPackageValidationSpecification]
    ModelPackageStatus: ModelPackageStatus
    ModelPackageStatusDetails: ModelPackageStatusDetails
    CertifyForMarketplace: Optional[CertifyForMarketplace]
    ModelApprovalStatus: Optional[ModelApprovalStatus]
    CreatedBy: Optional[UserContext]
    MetadataProperties: Optional[MetadataProperties]
    ModelMetrics: Optional[ModelMetrics]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    ApprovalDescription: Optional[ApprovalDescription]
    Domain: Optional[String]
    Task: Optional[String]
    SamplePayloadUrl: Optional[String]
    CustomerMetadataProperties: Optional[CustomerMetadataMap]
    DriftCheckBaselines: Optional[DriftCheckBaselines]
    AdditionalInferenceSpecifications: Optional[AdditionalInferenceSpecifications]
    SkipModelValidation: Optional[SkipModelValidation]
    SourceUri: Optional[ModelPackageSourceUri]
    SecurityConfig: Optional[ModelPackageSecurityConfig]
    ModelCard: Optional[ModelPackageModelCard]
    ModelLifeCycle: Optional[ModelLifeCycle]


class DescribeModelQualityJobDefinitionRequest(ServiceRequest):
    JobDefinitionName: MonitoringJobDefinitionName


class DescribeModelQualityJobDefinitionResponse(TypedDict, total=False):
    JobDefinitionArn: MonitoringJobDefinitionArn
    JobDefinitionName: MonitoringJobDefinitionName
    CreationTime: Timestamp
    ModelQualityBaselineConfig: Optional[ModelQualityBaselineConfig]
    ModelQualityAppSpecification: ModelQualityAppSpecification
    ModelQualityJobInput: ModelQualityJobInput
    ModelQualityJobOutputConfig: MonitoringOutputConfig
    JobResources: MonitoringResources
    NetworkConfig: Optional[MonitoringNetworkConfig]
    RoleArn: RoleArn
    StoppingCondition: Optional[MonitoringStoppingCondition]


class DescribeMonitoringScheduleRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName


class MonitoringExecutionSummary(TypedDict, total=False):
    """Summary of information about the last monitoring job to run."""

    MonitoringScheduleName: MonitoringScheduleName
    ScheduledTime: Timestamp
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    MonitoringExecutionStatus: ExecutionStatus
    ProcessingJobArn: Optional[ProcessingJobArn]
    EndpointName: Optional[EndpointName]
    FailureReason: Optional[FailureReason]
    MonitoringJobDefinitionName: Optional[MonitoringJobDefinitionName]
    MonitoringType: Optional[MonitoringType]


class DescribeMonitoringScheduleResponse(TypedDict, total=False):
    MonitoringScheduleArn: MonitoringScheduleArn
    MonitoringScheduleName: MonitoringScheduleName
    MonitoringScheduleStatus: ScheduleStatus
    MonitoringType: Optional[MonitoringType]
    FailureReason: Optional[FailureReason]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    MonitoringScheduleConfig: MonitoringScheduleConfig
    EndpointName: Optional[EndpointName]
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummary]


class DescribeNotebookInstanceInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName


class DescribeNotebookInstanceLifecycleConfigInput(ServiceRequest):
    NotebookInstanceLifecycleConfigName: NotebookInstanceLifecycleConfigName


class DescribeNotebookInstanceLifecycleConfigOutput(TypedDict, total=False):
    NotebookInstanceLifecycleConfigArn: Optional[NotebookInstanceLifecycleConfigArn]
    NotebookInstanceLifecycleConfigName: Optional[NotebookInstanceLifecycleConfigName]
    OnCreate: Optional[NotebookInstanceLifecycleConfigList]
    OnStart: Optional[NotebookInstanceLifecycleConfigList]
    LastModifiedTime: Optional[LastModifiedTime]
    CreationTime: Optional[CreationTime]


class DescribeNotebookInstanceOutput(TypedDict, total=False):
    NotebookInstanceArn: Optional[NotebookInstanceArn]
    NotebookInstanceName: Optional[NotebookInstanceName]
    NotebookInstanceStatus: Optional[NotebookInstanceStatus]
    FailureReason: Optional[FailureReason]
    Url: Optional[NotebookInstanceUrl]
    InstanceType: Optional[InstanceType]
    SubnetId: Optional[SubnetId]
    SecurityGroups: Optional[SecurityGroupIds]
    RoleArn: Optional[RoleArn]
    KmsKeyId: Optional[KmsKeyId]
    NetworkInterfaceId: Optional[NetworkInterfaceId]
    LastModifiedTime: Optional[LastModifiedTime]
    CreationTime: Optional[CreationTime]
    NotebookInstanceLifecycleConfigName: Optional[NotebookInstanceLifecycleConfigName]
    DirectInternetAccess: Optional[DirectInternetAccess]
    VolumeSizeInGB: Optional[NotebookInstanceVolumeSizeInGB]
    AcceleratorTypes: Optional[NotebookInstanceAcceleratorTypes]
    DefaultCodeRepository: Optional[CodeRepositoryNameOrUrl]
    AdditionalCodeRepositories: Optional[AdditionalCodeRepositoryNamesOrUrls]
    RootAccess: Optional[RootAccess]
    PlatformIdentifier: Optional[PlatformIdentifier]
    InstanceMetadataServiceConfiguration: Optional[InstanceMetadataServiceConfiguration]


class DescribeOptimizationJobRequest(ServiceRequest):
    OptimizationJobName: EntityName


class OptimizationOutput(TypedDict, total=False):
    """Output values produced by an optimization job."""

    RecommendedInferenceImage: Optional[OptimizationContainerImage]


class DescribeOptimizationJobResponse(TypedDict, total=False):
    OptimizationJobArn: OptimizationJobArn
    OptimizationJobStatus: OptimizationJobStatus
    OptimizationStartTime: Optional[Timestamp]
    OptimizationEndTime: Optional[Timestamp]
    CreationTime: CreationTime
    LastModifiedTime: LastModifiedTime
    FailureReason: Optional[FailureReason]
    OptimizationJobName: EntityName
    ModelSource: OptimizationJobModelSource
    OptimizationEnvironment: Optional[OptimizationJobEnvironmentVariables]
    DeploymentInstanceType: OptimizationJobDeploymentInstanceType
    OptimizationConfigs: OptimizationConfigs
    OutputConfig: OptimizationJobOutputConfig
    OptimizationOutput: Optional[OptimizationOutput]
    RoleArn: RoleArn
    StoppingCondition: StoppingCondition
    VpcConfig: Optional[OptimizationVpcConfig]


class DescribePartnerAppRequest(ServiceRequest):
    Arn: PartnerAppArn


class ErrorInfo(TypedDict, total=False):
    """This is an error field object that contains the error code and the
    reason for an operation failure.
    """

    Code: Optional[NonEmptyString64]
    Reason: Optional[NonEmptyString256]


class DescribePartnerAppResponse(TypedDict, total=False):
    Arn: Optional[PartnerAppArn]
    Name: Optional[PartnerAppName]
    Type: Optional[PartnerAppType]
    Status: Optional[PartnerAppStatus]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    ExecutionRoleArn: Optional[RoleArn]
    KmsKeyId: Optional[KmsKeyId]
    BaseUrl: Optional[String2048]
    MaintenanceConfig: Optional[PartnerAppMaintenanceConfig]
    Tier: Optional[NonEmptyString64]
    Version: Optional[NonEmptyString64]
    ApplicationConfig: Optional[PartnerAppConfig]
    AuthType: Optional[PartnerAppAuthType]
    EnableIamSessionBasedIdentity: Optional[Boolean]
    Error: Optional[ErrorInfo]


class DescribePipelineDefinitionForExecutionRequest(ServiceRequest):
    PipelineExecutionArn: PipelineExecutionArn


class DescribePipelineDefinitionForExecutionResponse(TypedDict, total=False):
    PipelineDefinition: Optional[PipelineDefinition]
    CreationTime: Optional[Timestamp]


class DescribePipelineExecutionRequest(ServiceRequest):
    PipelineExecutionArn: PipelineExecutionArn


class SelectedStep(TypedDict, total=False):
    """A step selected to run in selective execution mode."""

    StepName: String256


SelectedStepList = List[SelectedStep]


class SelectiveExecutionConfig(TypedDict, total=False):
    """The selective execution configuration applied to the pipeline run."""

    SourcePipelineExecutionArn: Optional[PipelineExecutionArn]
    SelectedSteps: SelectedStepList


class PipelineExperimentConfig(TypedDict, total=False):
    """Specifies the names of the experiment and trial created by a pipeline."""

    ExperimentName: Optional[ExperimentEntityName]
    TrialName: Optional[ExperimentEntityName]


class DescribePipelineExecutionResponse(TypedDict, total=False):
    PipelineArn: Optional[PipelineArn]
    PipelineExecutionArn: Optional[PipelineExecutionArn]
    PipelineExecutionDisplayName: Optional[PipelineExecutionName]
    PipelineExecutionStatus: Optional[PipelineExecutionStatus]
    PipelineExecutionDescription: Optional[PipelineExecutionDescription]
    PipelineExperimentConfig: Optional[PipelineExperimentConfig]
    FailureReason: Optional[PipelineExecutionFailureReason]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedBy: Optional[UserContext]
    ParallelismConfiguration: Optional[ParallelismConfiguration]
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfig]


class DescribePipelineRequest(ServiceRequest):
    PipelineName: PipelineNameOrArn


class DescribePipelineResponse(TypedDict, total=False):
    PipelineArn: Optional[PipelineArn]
    PipelineName: Optional[PipelineName]
    PipelineDisplayName: Optional[PipelineName]
    PipelineDefinition: Optional[PipelineDefinition]
    PipelineDescription: Optional[PipelineDescription]
    RoleArn: Optional[RoleArn]
    PipelineStatus: Optional[PipelineStatus]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    LastRunTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedBy: Optional[UserContext]
    ParallelismConfiguration: Optional[ParallelismConfiguration]


class DescribeProcessingJobRequest(ServiceRequest):
    ProcessingJobName: ProcessingJobName


class DescribeProcessingJobResponse(TypedDict, total=False):
    ProcessingInputs: Optional[ProcessingInputs]
    ProcessingOutputConfig: Optional[ProcessingOutputConfig]
    ProcessingJobName: ProcessingJobName
    ProcessingResources: ProcessingResources
    StoppingCondition: Optional[ProcessingStoppingCondition]
    AppSpecification: AppSpecification
    Environment: Optional[ProcessingEnvironmentMap]
    NetworkConfig: Optional[NetworkConfig]
    RoleArn: Optional[RoleArn]
    ExperimentConfig: Optional[ExperimentConfig]
    ProcessingJobArn: ProcessingJobArn
    ProcessingJobStatus: ProcessingJobStatus
    ExitMessage: Optional[ExitMessage]
    FailureReason: Optional[FailureReason]
    ProcessingEndTime: Optional[Timestamp]
    ProcessingStartTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    CreationTime: Timestamp
    MonitoringScheduleArn: Optional[MonitoringScheduleArn]
    AutoMLJobArn: Optional[AutoMLJobArn]
    TrainingJobArn: Optional[TrainingJobArn]


class DescribeProjectInput(ServiceRequest):
    ProjectName: ProjectEntityName


class ServiceCatalogProvisionedProductDetails(TypedDict, total=False):
    """Details of a provisioned service catalog product. For information about
    service catalog, see `What is Amazon Web Services Service
    Catalog <https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html>`__.
    """

    ProvisionedProductId: Optional[ServiceCatalogEntityId]
    ProvisionedProductStatusMessage: Optional[ProvisionedProductStatusMessage]


class DescribeProjectOutput(TypedDict, total=False):
    ProjectArn: ProjectArn
    ProjectName: ProjectEntityName
    ProjectId: ProjectId
    ProjectDescription: Optional[EntityDescription]
    ServiceCatalogProvisioningDetails: Optional[ServiceCatalogProvisioningDetails]
    ServiceCatalogProvisionedProductDetails: Optional[ServiceCatalogProvisionedProductDetails]
    ProjectStatus: ProjectStatus
    CreatedBy: Optional[UserContext]
    CreationTime: Timestamp
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class DescribeSpaceRequest(ServiceRequest):
    DomainId: DomainId
    SpaceName: SpaceName


class DescribeSpaceResponse(TypedDict, total=False):
    DomainId: Optional[DomainId]
    SpaceArn: Optional[SpaceArn]
    SpaceName: Optional[SpaceName]
    HomeEfsFileSystemUid: Optional[EfsUid]
    Status: Optional[SpaceStatus]
    LastModifiedTime: Optional[LastModifiedTime]
    CreationTime: Optional[CreationTime]
    FailureReason: Optional[FailureReason]
    SpaceSettings: Optional[SpaceSettings]
    OwnershipSettings: Optional[OwnershipSettings]
    SpaceSharingSettings: Optional[SpaceSharingSettings]
    SpaceDisplayName: Optional[NonEmptyString64]
    Url: Optional[String1024]


class DescribeStudioLifecycleConfigRequest(ServiceRequest):
    StudioLifecycleConfigName: StudioLifecycleConfigName


class DescribeStudioLifecycleConfigResponse(TypedDict, total=False):
    StudioLifecycleConfigArn: Optional[StudioLifecycleConfigArn]
    StudioLifecycleConfigName: Optional[StudioLifecycleConfigName]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    StudioLifecycleConfigContent: Optional[StudioLifecycleConfigContent]
    StudioLifecycleConfigAppType: Optional[StudioLifecycleConfigAppType]


class DescribeSubscribedWorkteamRequest(ServiceRequest):
    WorkteamArn: WorkteamArn


class SubscribedWorkteam(TypedDict, total=False):
    """Describes a work team of a vendor that does the labelling job."""

    WorkteamArn: WorkteamArn
    MarketplaceTitle: Optional[String200]
    SellerName: Optional[String]
    MarketplaceDescription: Optional[String200]
    ListingId: Optional[String]


class DescribeSubscribedWorkteamResponse(TypedDict, total=False):
    SubscribedWorkteam: SubscribedWorkteam


class DescribeTrainingJobRequest(ServiceRequest):
    TrainingJobName: TrainingJobName


class ProfilerRuleEvaluationStatus(TypedDict, total=False):
    """Information about the status of the rule evaluation."""

    RuleConfigurationName: Optional[RuleConfigurationName]
    RuleEvaluationJobArn: Optional[ProcessingJobArn]
    RuleEvaluationStatus: Optional[RuleEvaluationStatus]
    StatusDetails: Optional[StatusDetails]
    LastModifiedTime: Optional[Timestamp]


ProfilerRuleEvaluationStatuses = List[ProfilerRuleEvaluationStatus]


class MetricData(TypedDict, total=False):
    """The name, value, and date and time of a metric that was emitted to
    Amazon CloudWatch.
    """

    MetricName: Optional[MetricName]
    Value: Optional[Float]
    Timestamp: Optional[Timestamp]


FinalMetricDataList = List[MetricData]


class SecondaryStatusTransition(TypedDict, total=False):
    """An array element of ``SecondaryStatusTransitions`` for
    `DescribeTrainingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html>`__.
    It provides additional details about a status that the training job has
    transitioned through. A training job can be in one of several states,
    for example, starting, downloading, training, or uploading. Within each
    state, there are a number of intermediate states. For example, within
    the starting state, SageMaker could be starting the training job or
    launching the ML instances. These transitional states are referred to as
    the job's secondary status.
    """

    Status: SecondaryStatus
    StartTime: Timestamp
    EndTime: Optional[Timestamp]
    StatusMessage: Optional[StatusMessage]


SecondaryStatusTransitions = List[SecondaryStatusTransition]


class WarmPoolStatus(TypedDict, total=False):
    """Status and billing information about the warm pool."""

    Status: WarmPoolResourceStatus
    ResourceRetainedBillableTimeInSeconds: Optional[ResourceRetainedBillableTimeInSeconds]
    ReusedByJob: Optional[TrainingJobName]


class DescribeTrainingJobResponse(TypedDict, total=False):
    TrainingJobName: TrainingJobName
    TrainingJobArn: TrainingJobArn
    TuningJobArn: Optional[HyperParameterTuningJobArn]
    LabelingJobArn: Optional[LabelingJobArn]
    AutoMLJobArn: Optional[AutoMLJobArn]
    ModelArtifacts: ModelArtifacts
    TrainingJobStatus: TrainingJobStatus
    SecondaryStatus: SecondaryStatus
    FailureReason: Optional[FailureReason]
    HyperParameters: Optional[HyperParameters]
    AlgorithmSpecification: AlgorithmSpecification
    RoleArn: Optional[RoleArn]
    InputDataConfig: Optional[InputDataConfig]
    OutputDataConfig: Optional[OutputDataConfig]
    ResourceConfig: ResourceConfig
    WarmPoolStatus: Optional[WarmPoolStatus]
    VpcConfig: Optional[VpcConfig]
    StoppingCondition: StoppingCondition
    CreationTime: Timestamp
    TrainingStartTime: Optional[Timestamp]
    TrainingEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    SecondaryStatusTransitions: Optional[SecondaryStatusTransitions]
    FinalMetricDataList: Optional[FinalMetricDataList]
    EnableNetworkIsolation: Optional[Boolean]
    EnableInterContainerTrafficEncryption: Optional[Boolean]
    EnableManagedSpotTraining: Optional[Boolean]
    CheckpointConfig: Optional[CheckpointConfig]
    TrainingTimeInSeconds: Optional[TrainingTimeInSeconds]
    BillableTimeInSeconds: Optional[BillableTimeInSeconds]
    DebugHookConfig: Optional[DebugHookConfig]
    ExperimentConfig: Optional[ExperimentConfig]
    DebugRuleConfigurations: Optional[DebugRuleConfigurations]
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfig]
    DebugRuleEvaluationStatuses: Optional[DebugRuleEvaluationStatuses]
    ProfilerConfig: Optional[ProfilerConfig]
    ProfilerRuleConfigurations: Optional[ProfilerRuleConfigurations]
    ProfilerRuleEvaluationStatuses: Optional[ProfilerRuleEvaluationStatuses]
    ProfilingStatus: Optional[ProfilingStatus]
    Environment: Optional[TrainingEnvironmentMap]
    RetryStrategy: Optional[RetryStrategy]
    RemoteDebugConfig: Optional[RemoteDebugConfig]
    InfraCheckConfig: Optional[InfraCheckConfig]


class DescribeTrainingPlanRequest(ServiceRequest):
    TrainingPlanName: TrainingPlanName


ReservedCapacityDurationMinutes = int
ReservedCapacityDurationHours = int


class ReservedCapacitySummary(TypedDict, total=False):
    """Details of a reserved capacity for the training plan.

    For more information about how to reserve GPU capacity for your
    SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see
    ``CreateTrainingPlan``.
    """

    ReservedCapacityArn: ReservedCapacityArn
    InstanceType: ReservedCapacityInstanceType
    TotalInstanceCount: TotalInstanceCount
    Status: ReservedCapacityStatus
    AvailabilityZone: Optional[AvailabilityZone]
    DurationHours: Optional[ReservedCapacityDurationHours]
    DurationMinutes: Optional[ReservedCapacityDurationMinutes]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]


ReservedCapacitySummaries = List[ReservedCapacitySummary]
SageMakerResourceNames = List[SageMakerResourceName]
TrainingPlanDurationMinutes = int
TrainingPlanDurationHours = int


class DescribeTrainingPlanResponse(TypedDict, total=False):
    TrainingPlanArn: TrainingPlanArn
    TrainingPlanName: TrainingPlanName
    Status: TrainingPlanStatus
    StatusMessage: Optional[TrainingPlanStatusMessage]
    DurationHours: Optional[TrainingPlanDurationHours]
    DurationMinutes: Optional[TrainingPlanDurationMinutes]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    UpfrontFee: Optional[String256]
    CurrencyCode: Optional[CurrencyCode]
    TotalInstanceCount: Optional[TotalInstanceCount]
    AvailableInstanceCount: Optional[AvailableInstanceCount]
    InUseInstanceCount: Optional[InUseInstanceCount]
    TargetResources: Optional[SageMakerResourceNames]
    ReservedCapacitySummaries: Optional[ReservedCapacitySummaries]


class DescribeTransformJobRequest(ServiceRequest):
    TransformJobName: TransformJobName


class DescribeTransformJobResponse(TypedDict, total=False):
    TransformJobName: TransformJobName
    TransformJobArn: TransformJobArn
    TransformJobStatus: TransformJobStatus
    FailureReason: Optional[FailureReason]
    ModelName: ModelName
    MaxConcurrentTransforms: Optional[MaxConcurrentTransforms]
    ModelClientConfig: Optional[ModelClientConfig]
    MaxPayloadInMB: Optional[MaxPayloadInMB]
    BatchStrategy: Optional[BatchStrategy]
    Environment: Optional[TransformEnvironmentMap]
    TransformInput: TransformInput
    TransformOutput: Optional[TransformOutput]
    DataCaptureConfig: Optional[BatchDataCaptureConfig]
    TransformResources: TransformResources
    CreationTime: Timestamp
    TransformStartTime: Optional[Timestamp]
    TransformEndTime: Optional[Timestamp]
    LabelingJobArn: Optional[LabelingJobArn]
    AutoMLJobArn: Optional[AutoMLJobArn]
    DataProcessing: Optional[DataProcessing]
    ExperimentConfig: Optional[ExperimentConfig]


class DescribeTrialComponentRequest(ServiceRequest):
    TrialComponentName: ExperimentEntityNameOrArn


class TrialComponentSource(TypedDict, total=False):
    """The Amazon Resource Name (ARN) and job type of the source of a trial
    component.
    """

    SourceArn: TrialComponentSourceArn
    SourceType: Optional[SourceType]


TrialComponentSources = List[TrialComponentSource]


class TrialComponentMetricSummary(TypedDict, total=False):
    """A summary of the metrics of a trial component."""

    MetricName: Optional[MetricName]
    SourceArn: Optional[TrialComponentSourceArn]
    TimeStamp: Optional[Timestamp]
    Max: Optional[OptionalDouble]
    Min: Optional[OptionalDouble]
    Last: Optional[OptionalDouble]
    Count: Optional[OptionalInteger]
    Avg: Optional[OptionalDouble]
    StdDev: Optional[OptionalDouble]


TrialComponentMetricSummaries = List[TrialComponentMetricSummary]


class DescribeTrialComponentResponse(TypedDict, total=False):
    TrialComponentName: Optional[ExperimentEntityName]
    TrialComponentArn: Optional[TrialComponentArn]
    DisplayName: Optional[ExperimentEntityName]
    Source: Optional[TrialComponentSource]
    Status: Optional[TrialComponentStatus]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    Parameters: Optional[TrialComponentParameters]
    InputArtifacts: Optional[TrialComponentArtifacts]
    OutputArtifacts: Optional[TrialComponentArtifacts]
    MetadataProperties: Optional[MetadataProperties]
    Metrics: Optional[TrialComponentMetricSummaries]
    LineageGroupArn: Optional[LineageGroupArn]
    Sources: Optional[TrialComponentSources]


class DescribeTrialRequest(ServiceRequest):
    TrialName: ExperimentEntityName


class TrialSource(TypedDict, total=False):
    """The source of the trial."""

    SourceArn: TrialSourceArn
    SourceType: Optional[SourceType]


class DescribeTrialResponse(TypedDict, total=False):
    TrialName: Optional[ExperimentEntityName]
    TrialArn: Optional[TrialArn]
    DisplayName: Optional[ExperimentEntityName]
    ExperimentName: Optional[ExperimentEntityName]
    Source: Optional[TrialSource]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    MetadataProperties: Optional[MetadataProperties]


class DescribeUserProfileRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: UserProfileName


class DescribeUserProfileResponse(TypedDict, total=False):
    DomainId: Optional[DomainId]
    UserProfileArn: Optional[UserProfileArn]
    UserProfileName: Optional[UserProfileName]
    HomeEfsFileSystemUid: Optional[EfsUid]
    Status: Optional[UserProfileStatus]
    LastModifiedTime: Optional[LastModifiedTime]
    CreationTime: Optional[CreationTime]
    FailureReason: Optional[FailureReason]
    SingleSignOnUserIdentifier: Optional[SingleSignOnUserIdentifier]
    SingleSignOnUserValue: Optional[String256]
    UserSettings: Optional[UserSettings]


class DescribeWorkforceRequest(ServiceRequest):
    WorkforceName: WorkforceName


class WorkforceVpcConfigResponse(TypedDict, total=False):
    """A VpcConfig object that specifies the VPC that you want your workforce
    to connect to.
    """

    VpcId: WorkforceVpcId
    SecurityGroupIds: WorkforceSecurityGroupIds
    Subnets: WorkforceSubnets
    VpcEndpointId: Optional[WorkforceVpcEndpointId]


class OidcConfigForResponse(TypedDict, total=False):
    """Your OIDC IdP workforce configuration."""

    ClientId: Optional[ClientId]
    Issuer: Optional[OidcEndpoint]
    AuthorizationEndpoint: Optional[OidcEndpoint]
    TokenEndpoint: Optional[OidcEndpoint]
    UserInfoEndpoint: Optional[OidcEndpoint]
    LogoutEndpoint: Optional[OidcEndpoint]
    JwksUri: Optional[OidcEndpoint]
    Scope: Optional[Scope]
    AuthenticationRequestExtraParams: Optional[AuthenticationRequestExtraParams]


class Workforce(TypedDict, total=False):
    """A single private workforce, which is automatically created when you
    create your first private work team. You can create one private work
    force in each Amazon Web Services Region. By default, any
    workforce-related API operation used in a specific region will apply to
    the workforce created in that region. To learn how to create a private
    workforce, see `Create a Private
    Workforce <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html>`__.
    """

    WorkforceName: WorkforceName
    WorkforceArn: WorkforceArn
    LastUpdatedDate: Optional[Timestamp]
    SourceIpConfig: Optional[SourceIpConfig]
    SubDomain: Optional[String]
    CognitoConfig: Optional[CognitoConfig]
    OidcConfig: Optional[OidcConfigForResponse]
    CreateDate: Optional[Timestamp]
    WorkforceVpcConfig: Optional[WorkforceVpcConfigResponse]
    Status: Optional[WorkforceStatus]
    FailureReason: Optional[WorkforceFailureReason]


class DescribeWorkforceResponse(TypedDict, total=False):
    Workforce: Workforce


class DescribeWorkteamRequest(ServiceRequest):
    WorkteamName: WorkteamName


ProductListings = List[String]


class Workteam(TypedDict, total=False):
    """Provides details about a labeling work team."""

    WorkteamName: WorkteamName
    MemberDefinitions: MemberDefinitions
    WorkteamArn: WorkteamArn
    WorkforceArn: Optional[WorkforceArn]
    ProductListingIds: Optional[ProductListings]
    Description: String200
    SubDomain: Optional[String]
    CreateDate: Optional[Timestamp]
    LastUpdatedDate: Optional[Timestamp]
    NotificationConfiguration: Optional[NotificationConfiguration]
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration]


class DescribeWorkteamResponse(TypedDict, total=False):
    Workteam: Workteam


class ProductionVariantServerlessUpdateConfig(TypedDict, total=False):
    """Specifies the serverless update concurrency configuration for an
    endpoint variant.
    """

    MaxConcurrency: Optional[ServerlessMaxConcurrency]
    ProvisionedConcurrency: Optional[ServerlessProvisionedConcurrency]


class DesiredWeightAndCapacity(TypedDict, total=False):
    """Specifies weight and capacity values for a production variant."""

    VariantName: VariantName
    DesiredWeight: Optional[VariantWeight]
    DesiredInstanceCount: Optional[TaskCount]
    ServerlessUpdateConfig: Optional[ProductionVariantServerlessUpdateConfig]


DesiredWeightAndCapacityList = List[DesiredWeightAndCapacity]


class Device(TypedDict, total=False):
    """Information of a particular device."""

    DeviceName: DeviceName
    Description: Optional[DeviceDescription]
    IotThingName: Optional[ThingName]


class DeviceDeploymentSummary(TypedDict, total=False):
    """Contains information summarizing device details and deployment status."""

    EdgeDeploymentPlanArn: EdgeDeploymentPlanArn
    EdgeDeploymentPlanName: EntityName
    StageName: EntityName
    DeployedStageName: Optional[EntityName]
    DeviceFleetName: Optional[EntityName]
    DeviceName: DeviceName
    DeviceArn: DeviceArn
    DeviceDeploymentStatus: Optional[DeviceDeploymentStatus]
    DeviceDeploymentStatusMessage: Optional[String]
    Description: Optional[DeviceDescription]
    DeploymentStartTime: Optional[Timestamp]


DeviceDeploymentSummaries = List[DeviceDeploymentSummary]


class DeviceFleetSummary(TypedDict, total=False):
    """Summary of the device fleet."""

    DeviceFleetArn: DeviceFleetArn
    DeviceFleetName: EntityName
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


DeviceFleetSummaries = List[DeviceFleetSummary]


class DeviceStats(TypedDict, total=False):
    """Status of devices."""

    ConnectedDeviceCount: Long
    RegisteredDeviceCount: Long


class EdgeModelSummary(TypedDict, total=False):
    """Summary of model on edge device."""

    ModelName: EntityName
    ModelVersion: EdgeVersion


EdgeModelSummaries = List[EdgeModelSummary]


class DeviceSummary(TypedDict, total=False):
    """Summary of the device."""

    DeviceName: EntityName
    DeviceArn: DeviceArn
    Description: Optional[DeviceDescription]
    DeviceFleetName: Optional[EntityName]
    IotThingName: Optional[ThingName]
    RegistrationTime: Optional[Timestamp]
    LatestHeartbeat: Optional[Timestamp]
    Models: Optional[EdgeModelSummaries]
    AgentVersion: Optional[EdgeVersion]


DeviceSummaries = List[DeviceSummary]
Devices = List[Device]


class DisableSagemakerServicecatalogPortfolioInput(ServiceRequest):
    pass


class DisableSagemakerServicecatalogPortfolioOutput(TypedDict, total=False):
    pass


class DisassociateTrialComponentRequest(ServiceRequest):
    TrialComponentName: ExperimentEntityName
    TrialName: ExperimentEntityName


class DisassociateTrialComponentResponse(TypedDict, total=False):
    TrialComponentArn: Optional[TrialComponentArn]
    TrialArn: Optional[TrialArn]


class DomainDetails(TypedDict, total=False):
    """The domain's details."""

    DomainArn: Optional[DomainArn]
    DomainId: Optional[DomainId]
    DomainName: Optional[DomainName]
    Status: Optional[DomainStatus]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]
    Url: Optional[String1024]


DomainList = List[DomainDetails]


class RStudioServerProDomainSettingsForUpdate(TypedDict, total=False):
    """A collection of settings that update the current configuration for the
    ``RStudioServerPro`` Domain-level app.
    """

    DomainExecutionRoleArn: RoleArn
    DefaultResourceSpec: Optional[ResourceSpec]
    RStudioConnectUrl: Optional[String]
    RStudioPackageManagerUrl: Optional[String]


class DomainSettingsForUpdate(TypedDict, total=False):
    """A collection of ``Domain`` configuration settings to update."""

    RStudioServerProDomainSettingsForUpdate: Optional[RStudioServerProDomainSettingsForUpdate]
    ExecutionRoleIdentityConfig: Optional[ExecutionRoleIdentityConfig]
    SecurityGroupIds: Optional[DomainSecurityGroupIds]
    DockerSettings: Optional[DockerSettings]
    AmazonQSettings: Optional[AmazonQSettings]
    UnifiedStudioSettings: Optional[UnifiedStudioSettings]


class PredefinedMetricSpecification(TypedDict, total=False):
    """A specification for a predefined metric."""

    PredefinedMetricType: Optional[String]


class MetricSpecification(TypedDict, total=False):
    """An object containing information about a metric."""

    Predefined: Optional[PredefinedMetricSpecification]
    Customized: Optional[CustomizedMetricSpecification]


class TargetTrackingScalingPolicyConfiguration(TypedDict, total=False):
    """A target tracking scaling policy. Includes support for predefined or
    customized metrics.

    When using the
    `PutScalingPolicy <https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html>`__
    API, this parameter is required when you are creating a policy with the
    policy type ``TargetTrackingScaling``.
    """

    MetricSpecification: Optional[MetricSpecification]
    TargetValue: Optional[Double]


class ScalingPolicy(TypedDict, total=False):
    """An object containing a recommended scaling policy."""

    TargetTracking: Optional[TargetTrackingScalingPolicyConfiguration]


ScalingPolicies = List[ScalingPolicy]


class DynamicScalingConfiguration(TypedDict, total=False):
    """An object with the recommended values for you to specify when creating
    an autoscaling policy.
    """

    MinCapacity: Optional[Integer]
    MaxCapacity: Optional[Integer]
    ScaleInCooldown: Optional[Integer]
    ScaleOutCooldown: Optional[Integer]
    ScalingPolicies: Optional[ScalingPolicies]


class EMRStepMetadata(TypedDict, total=False):
    """The configurations and outcomes of an Amazon EMR step execution."""

    ClusterId: Optional[String256]
    StepId: Optional[String256]
    StepName: Optional[String256]
    LogFilePath: Optional[String1024]


class Edge(TypedDict, total=False):
    """A directed edge connecting two lineage entities."""

    SourceArn: Optional[AssociationEntityArn]
    DestinationArn: Optional[AssociationEntityArn]
    AssociationType: Optional[AssociationEdgeType]


class EdgeDeploymentPlanSummary(TypedDict, total=False):
    """Contains information summarizing an edge deployment plan."""

    EdgeDeploymentPlanArn: EdgeDeploymentPlanArn
    EdgeDeploymentPlanName: EntityName
    DeviceFleetName: EntityName
    EdgeDeploymentSuccess: Integer
    EdgeDeploymentPending: Integer
    EdgeDeploymentFailed: Integer
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


EdgeDeploymentPlanSummaries = List[EdgeDeploymentPlanSummary]


class EdgeModelStat(TypedDict, total=False):
    """Status of edge devices with this model."""

    ModelName: EntityName
    ModelVersion: EdgeVersion
    OfflineDeviceCount: Long
    ConnectedDeviceCount: Long
    ActiveDeviceCount: Long
    SamplingDeviceCount: Long


EdgeModelStats = List[EdgeModelStat]


class EdgePackagingJobSummary(TypedDict, total=False):
    """Summary of edge packaging job."""

    EdgePackagingJobArn: EdgePackagingJobArn
    EdgePackagingJobName: EntityName
    EdgePackagingJobStatus: EdgePackagingJobStatus
    CompilationJobName: Optional[EntityName]
    ModelName: Optional[EntityName]
    ModelVersion: Optional[EdgeVersion]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


EdgePackagingJobSummaries = List[EdgePackagingJobSummary]
Edges = List[Edge]


class EnableSagemakerServicecatalogPortfolioInput(ServiceRequest):
    pass


class EnableSagemakerServicecatalogPortfolioOutput(TypedDict, total=False):
    pass


class MonitoringSchedule(TypedDict, total=False):
    """A schedule for a model monitoring job. For information about model
    monitor, see `Amazon SageMaker Model
    Monitor <https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html>`__.
    """

    MonitoringScheduleArn: Optional[MonitoringScheduleArn]
    MonitoringScheduleName: Optional[MonitoringScheduleName]
    MonitoringScheduleStatus: Optional[ScheduleStatus]
    MonitoringType: Optional[MonitoringType]
    FailureReason: Optional[FailureReason]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    MonitoringScheduleConfig: Optional[MonitoringScheduleConfig]
    EndpointName: Optional[EndpointName]
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummary]
    Tags: Optional[TagList]


MonitoringScheduleList = List[MonitoringSchedule]


class Endpoint(TypedDict, total=False):
    """A hosted endpoint for real-time inference."""

    EndpointName: EndpointName
    EndpointArn: EndpointArn
    EndpointConfigName: EndpointConfigName
    ProductionVariants: Optional[ProductionVariantSummaryList]
    DataCaptureConfig: Optional[DataCaptureConfigSummary]
    EndpointStatus: EndpointStatus
    FailureReason: Optional[FailureReason]
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    MonitoringSchedules: Optional[MonitoringScheduleList]
    Tags: Optional[TagList]
    ShadowProductionVariants: Optional[ProductionVariantSummaryList]


class EndpointConfigStepMetadata(TypedDict, total=False):
    """Metadata for an endpoint configuration step."""

    Arn: Optional[EndpointConfigArn]


class EndpointConfigSummary(TypedDict, total=False):
    """Provides summary information for an endpoint configuration."""

    EndpointConfigName: EndpointConfigName
    EndpointConfigArn: EndpointConfigArn
    CreationTime: Timestamp


EndpointConfigSummaryList = List[EndpointConfigSummary]


class EndpointStepMetadata(TypedDict, total=False):
    """Metadata for an endpoint step."""

    Arn: Optional[EndpointArn]


class EndpointSummary(TypedDict, total=False):
    """Provides summary information for an endpoint."""

    EndpointName: EndpointName
    EndpointArn: EndpointArn
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    EndpointStatus: EndpointStatus


EndpointSummaryList = List[EndpointSummary]


class Experiment(TypedDict, total=False):
    """The properties of an experiment as returned by the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API. For information about experiments, see the
    `CreateExperiment <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateExperiment.html>`__
    API.
    """

    ExperimentName: Optional[ExperimentEntityName]
    ExperimentArn: Optional[ExperimentArn]
    DisplayName: Optional[ExperimentEntityName]
    Source: Optional[ExperimentSource]
    Description: Optional[ExperimentDescription]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    Tags: Optional[TagList]


class ExperimentSummary(TypedDict, total=False):
    """A summary of the properties of an experiment. To get the complete set of
    properties, call the
    `DescribeExperiment <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeExperiment.html>`__
    API and provide the ``ExperimentName``.
    """

    ExperimentArn: Optional[ExperimentArn]
    ExperimentName: Optional[ExperimentEntityName]
    DisplayName: Optional[ExperimentEntityName]
    ExperimentSource: Optional[ExperimentSource]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


ExperimentSummaries = List[ExperimentSummary]


class FailStepMetadata(TypedDict, total=False):
    """The container for the metadata for Fail step."""

    ErrorMessage: Optional[String3072]


FeatureAdditions = List[FeatureDefinition]


class FeatureGroup(TypedDict, total=False):
    """Amazon SageMaker Feature Store stores features in a collection called
    Feature Group. A Feature Group can be visualized as a table which has
    rows, with a unique identifier for each row where each column in the
    table is a feature. In principle, a Feature Group is composed of
    features and values per features.
    """

    FeatureGroupArn: Optional[FeatureGroupArn]
    FeatureGroupName: Optional[FeatureGroupName]
    RecordIdentifierFeatureName: Optional[FeatureName]
    EventTimeFeatureName: Optional[FeatureName]
    FeatureDefinitions: Optional[FeatureDefinitions]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]
    OnlineStoreConfig: Optional[OnlineStoreConfig]
    OfflineStoreConfig: Optional[OfflineStoreConfig]
    RoleArn: Optional[RoleArn]
    FeatureGroupStatus: Optional[FeatureGroupStatus]
    OfflineStoreStatus: Optional[OfflineStoreStatus]
    LastUpdateStatus: Optional[LastUpdateStatus]
    FailureReason: Optional[FailureReason]
    Description: Optional[Description]
    Tags: Optional[TagList]


class FeatureGroupSummary(TypedDict, total=False):
    """The name, ARN, ``CreationTime``, ``FeatureGroup`` values,
    ``LastUpdatedTime`` and ``EnableOnlineStorage`` status of a
    ``FeatureGroup``.
    """

    FeatureGroupName: FeatureGroupName
    FeatureGroupArn: FeatureGroupArn
    CreationTime: Timestamp
    FeatureGroupStatus: Optional[FeatureGroupStatus]
    OfflineStoreStatus: Optional[OfflineStoreStatus]


FeatureGroupSummaries = List[FeatureGroupSummary]


class FeatureMetadata(TypedDict, total=False):
    """The metadata for a feature. It can either be metadata that you specify,
    or metadata that is updated automatically.
    """

    FeatureGroupArn: Optional[FeatureGroupArn]
    FeatureGroupName: Optional[FeatureGroupName]
    FeatureName: Optional[FeatureName]
    FeatureType: Optional[FeatureType]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]
    Description: Optional[FeatureDescription]
    Parameters: Optional[FeatureParameters]


FeatureParameterAdditions = List[FeatureParameter]
FeatureParameterRemovals = List[FeatureParameterKey]


class Filter(TypedDict, total=False):
    """A conditional statement for a search expression that includes a resource
    property, a Boolean operator, and a value. Resources that match the
    statement are returned in the results from the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API.

    If you specify a ``Value``, but not an ``Operator``, SageMaker uses the
    equals operator.

    In search, there are several property types:

    Metrics
       To define a metric filter, enter a value using the form
       ``"Metrics.<name>"``, where ``<name>`` is a metric name. For example,
       the following filter searches for training jobs with an
       ``"accuracy"`` metric greater than ``"0.9"``:

       ``{``

       ``"Name": "Metrics.accuracy",``

       ``"Operator": "GreaterThan",``

       ``"Value": "0.9"``

       ``}``

    HyperParameters
       To define a hyperparameter filter, enter a value with the form
       ``"HyperParameters.<name>"``. Decimal hyperparameter values are
       treated as a decimal in a comparison if the specified ``Value`` is
       also a decimal value. If the specified ``Value`` is an integer, the
       decimal hyperparameter values are treated as integers. For example,
       the following filter is satisfied by training jobs with a
       ``"learning_rate"`` hyperparameter that is less than ``"0.5"``:

       ``{``

       ``"Name": "HyperParameters.learning_rate",``

       ``"Operator": "LessThan",``

       ``"Value": "0.5"``

       ``}``

    Tags
       To define a tag filter, enter a value with the form ``Tags.<key>``.
    """

    Name: ResourcePropertyName
    Operator: Optional[Operator]
    Value: Optional[FilterValue]


FilterList = List[Filter]


class FlowDefinitionSummary(TypedDict, total=False):
    """Contains summary information about the flow definition."""

    FlowDefinitionName: FlowDefinitionName
    FlowDefinitionArn: FlowDefinitionArn
    FlowDefinitionStatus: FlowDefinitionStatus
    CreationTime: Timestamp
    FailureReason: Optional[FailureReason]


FlowDefinitionSummaries = List[FlowDefinitionSummary]


class GetDeviceFleetReportRequest(ServiceRequest):
    DeviceFleetName: EntityName


class GetDeviceFleetReportResponse(TypedDict, total=False):
    DeviceFleetArn: DeviceFleetArn
    DeviceFleetName: EntityName
    OutputConfig: Optional[EdgeOutputConfig]
    Description: Optional[DeviceFleetDescription]
    ReportGenerated: Optional[Timestamp]
    DeviceStats: Optional[DeviceStats]
    AgentVersions: Optional[AgentVersions]
    ModelStats: Optional[EdgeModelStats]


class GetLineageGroupPolicyRequest(ServiceRequest):
    LineageGroupName: LineageGroupNameOrArn


class GetLineageGroupPolicyResponse(TypedDict, total=False):
    LineageGroupArn: Optional[LineageGroupArn]
    ResourcePolicy: Optional[ResourcePolicyString]


class GetModelPackageGroupPolicyInput(ServiceRequest):
    ModelPackageGroupName: EntityName


class GetModelPackageGroupPolicyOutput(TypedDict, total=False):
    ResourcePolicy: PolicyString


class GetSagemakerServicecatalogPortfolioStatusInput(ServiceRequest):
    pass


class GetSagemakerServicecatalogPortfolioStatusOutput(TypedDict, total=False):
    Status: Optional[SagemakerServicecatalogStatus]


class ScalingPolicyObjective(TypedDict, total=False):
    """An object where you specify the anticipated traffic pattern for an
    endpoint.
    """

    MinInvocationsPerMinute: Optional[Integer]
    MaxInvocationsPerMinute: Optional[Integer]


class GetScalingConfigurationRecommendationRequest(ServiceRequest):
    InferenceRecommendationsJobName: RecommendationJobName
    RecommendationId: Optional[String]
    EndpointName: Optional[EndpointName]
    TargetCpuUtilizationPerCore: Optional[UtilizationPercentagePerCore]
    ScalingPolicyObjective: Optional[ScalingPolicyObjective]


class ScalingPolicyMetric(TypedDict, total=False):
    """The metric for a scaling policy."""

    InvocationsPerInstance: Optional[Integer]
    ModelLatency: Optional[Integer]


class GetScalingConfigurationRecommendationResponse(TypedDict, total=False):
    InferenceRecommendationsJobName: Optional[RecommendationJobName]
    RecommendationId: Optional[String]
    EndpointName: Optional[EndpointName]
    TargetCpuUtilizationPerCore: Optional[UtilizationPercentagePerCore]
    ScalingPolicyObjective: Optional[ScalingPolicyObjective]
    Metric: Optional[ScalingPolicyMetric]
    DynamicScalingConfiguration: Optional[DynamicScalingConfiguration]


class PropertyNameQuery(TypedDict, total=False):
    """Part of the ``SuggestionQuery`` type. Specifies a hint for retrieving
    property names that begin with the specified text.
    """

    PropertyNameHint: PropertyNameHint


class SuggestionQuery(TypedDict, total=False):
    """Specified in the
    `GetSearchSuggestions <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetSearchSuggestions.html>`__
    request. Limits the property names that are included in the response.
    """

    PropertyNameQuery: Optional[PropertyNameQuery]


class GetSearchSuggestionsRequest(ServiceRequest):
    Resource: ResourceType
    SuggestionQuery: Optional[SuggestionQuery]


class PropertyNameSuggestion(TypedDict, total=False):
    """A property name returned from a ``GetSearchSuggestions`` call that
    specifies a value in the ``PropertyNameQuery`` field.
    """

    PropertyName: Optional[ResourcePropertyName]


PropertyNameSuggestionList = List[PropertyNameSuggestion]


class GetSearchSuggestionsResponse(TypedDict, total=False):
    PropertyNameSuggestions: Optional[PropertyNameSuggestionList]


class GitConfigForUpdate(TypedDict, total=False):
    """Specifies configuration details for a Git repository when the repository
    is updated.
    """

    SecretArn: Optional[SecretArn]


class HubContentInfo(TypedDict, total=False):
    """Information about hub content."""

    HubContentName: HubContentName
    HubContentArn: HubContentArn
    SageMakerPublicHubContentArn: Optional[SageMakerPublicHubContentArn]
    HubContentVersion: HubContentVersion
    HubContentType: HubContentType
    DocumentSchemaVersion: DocumentSchemaVersion
    HubContentDisplayName: Optional[HubContentDisplayName]
    HubContentDescription: Optional[HubContentDescription]
    SupportStatus: Optional[HubContentSupportStatus]
    HubContentSearchKeywords: Optional[HubContentSearchKeywordList]
    HubContentStatus: HubContentStatus
    CreationTime: Timestamp
    OriginalCreationTime: Optional[Timestamp]


HubContentInfoList = List[HubContentInfo]


class HubInfo(TypedDict, total=False):
    """Information about a hub."""

    HubName: HubName
    HubArn: HubArn
    HubDisplayName: Optional[HubDisplayName]
    HubDescription: Optional[HubDescription]
    HubSearchKeywords: Optional[HubSearchKeywordList]
    HubStatus: HubStatus
    CreationTime: Timestamp
    LastModifiedTime: Timestamp


HubInfoList = List[HubInfo]


class HumanTaskUiSummary(TypedDict, total=False):
    """Container for human task user interface information."""

    HumanTaskUiName: HumanTaskUiName
    HumanTaskUiArn: HumanTaskUiArn
    CreationTime: Timestamp


HumanTaskUiSummaries = List[HumanTaskUiSummary]
HyperParameterTrainingJobSummaries = List[HyperParameterTrainingJobSummary]


class HyperParameterTuningJobSearchEntity(TypedDict, total=False):
    """An entity returned by the
    `SearchRecord <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html>`__
    API containing the properties of a hyperparameter tuning job.
    """

    HyperParameterTuningJobName: Optional[HyperParameterTuningJobName]
    HyperParameterTuningJobArn: Optional[HyperParameterTuningJobArn]
    HyperParameterTuningJobConfig: Optional[HyperParameterTuningJobConfig]
    TrainingJobDefinition: Optional[HyperParameterTrainingJobDefinition]
    TrainingJobDefinitions: Optional[HyperParameterTrainingJobDefinitions]
    HyperParameterTuningJobStatus: Optional[HyperParameterTuningJobStatus]
    CreationTime: Optional[Timestamp]
    HyperParameterTuningEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    TrainingJobStatusCounters: Optional[TrainingJobStatusCounters]
    ObjectiveStatusCounters: Optional[ObjectiveStatusCounters]
    BestTrainingJob: Optional[HyperParameterTrainingJobSummary]
    OverallBestTrainingJob: Optional[HyperParameterTrainingJobSummary]
    WarmStartConfig: Optional[HyperParameterTuningJobWarmStartConfig]
    FailureReason: Optional[FailureReason]
    TuningJobCompletionDetails: Optional[HyperParameterTuningJobCompletionDetails]
    ConsumedResources: Optional[HyperParameterTuningJobConsumedResources]
    Tags: Optional[TagList]


class HyperParameterTuningJobSummary(TypedDict, total=False):
    """Provides summary information about a hyperparameter tuning job."""

    HyperParameterTuningJobName: HyperParameterTuningJobName
    HyperParameterTuningJobArn: HyperParameterTuningJobArn
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatus
    Strategy: HyperParameterTuningJobStrategyType
    CreationTime: Timestamp
    HyperParameterTuningEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    TrainingJobStatusCounters: TrainingJobStatusCounters
    ObjectiveStatusCounters: ObjectiveStatusCounters
    ResourceLimits: Optional[ResourceLimits]


HyperParameterTuningJobSummaries = List[HyperParameterTuningJobSummary]


class Image(TypedDict, total=False):
    """A SageMaker AI image. A SageMaker AI image represents a set of container
    images that are derived from a common base container image. Each of
    these container images is represented by a SageMaker AI
    ``ImageVersion``.
    """

    CreationTime: Timestamp
    Description: Optional[ImageDescription]
    DisplayName: Optional[ImageDisplayName]
    FailureReason: Optional[FailureReason]
    ImageArn: ImageArn
    ImageName: ImageName
    ImageStatus: ImageStatus
    LastModifiedTime: Timestamp


ImageDeletePropertyList = List[ImageDeleteProperty]


class ImageVersion(TypedDict, total=False):
    """A version of a SageMaker AI ``Image``. A version represents an existing
    container image.
    """

    CreationTime: Timestamp
    FailureReason: Optional[FailureReason]
    ImageArn: ImageArn
    ImageVersionArn: ImageVersionArn
    ImageVersionStatus: ImageVersionStatus
    LastModifiedTime: Timestamp
    Version: ImageVersionNumber


ImageVersions = List[ImageVersion]
Images = List[Image]


class ImportHubContentRequest(ServiceRequest):
    HubContentName: HubContentName
    HubContentVersion: Optional[HubContentVersion]
    HubContentType: HubContentType
    DocumentSchemaVersion: DocumentSchemaVersion
    HubName: HubNameOrArn
    HubContentDisplayName: Optional[HubContentDisplayName]
    HubContentDescription: Optional[HubContentDescription]
    HubContentMarkdown: Optional[HubContentMarkdown]
    HubContentDocument: HubContentDocument
    SupportStatus: Optional[HubContentSupportStatus]
    HubContentSearchKeywords: Optional[HubContentSearchKeywordList]
    Tags: Optional[TagList]


class ImportHubContentResponse(TypedDict, total=False):
    HubArn: HubArn
    HubContentArn: HubContentArn


class InferenceComponentSummary(TypedDict, total=False):
    """A summary of the properties of an inference component."""

    CreationTime: Timestamp
    InferenceComponentArn: InferenceComponentArn
    InferenceComponentName: InferenceComponentName
    EndpointArn: EndpointArn
    EndpointName: EndpointName
    VariantName: VariantName
    InferenceComponentStatus: Optional[InferenceComponentStatus]
    LastModifiedTime: Timestamp


InferenceComponentSummaryList = List[InferenceComponentSummary]


class InferenceExperimentSummary(TypedDict, total=False):
    """Lists a summary of properties of an inference experiment."""

    Name: InferenceExperimentName
    Type: InferenceExperimentType
    Schedule: Optional[InferenceExperimentSchedule]
    Status: InferenceExperimentStatus
    StatusReason: Optional[InferenceExperimentStatusReason]
    Description: Optional[InferenceExperimentDescription]
    CreationTime: Timestamp
    CompletionTime: Optional[Timestamp]
    LastModifiedTime: Timestamp
    RoleArn: Optional[RoleArn]


InferenceExperimentList = List[InferenceExperimentSummary]


class InferenceRecommendationsJob(TypedDict, total=False):
    """A structure that contains a list of recommendation jobs."""

    JobName: RecommendationJobName
    JobDescription: RecommendationJobDescription
    JobType: RecommendationJobType
    JobArn: RecommendationJobArn
    Status: RecommendationJobStatus
    CreationTime: CreationTime
    CompletionTime: Optional[Timestamp]
    RoleArn: RoleArn
    LastModifiedTime: LastModifiedTime
    FailureReason: Optional[FailureReason]
    ModelName: Optional[ModelName]
    SamplePayloadUrl: Optional[S3Uri]
    ModelPackageVersionArn: Optional[ModelPackageArn]


class RecommendationJobInferenceBenchmark(TypedDict, total=False):
    """The details for a specific benchmark from an Inference Recommender job."""

    Metrics: Optional[RecommendationMetrics]
    EndpointMetrics: Optional[InferenceMetrics]
    EndpointConfiguration: Optional[EndpointOutputConfiguration]
    ModelConfiguration: ModelConfiguration
    FailureReason: Optional[RecommendationFailureReason]
    InvocationEndTime: Optional[InvocationEndTime]
    InvocationStartTime: Optional[InvocationStartTime]


class InferenceRecommendationsJobStep(TypedDict, total=False):
    """A returned array object for the ``Steps`` response field in the
    `ListInferenceRecommendationsJobSteps <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobSteps.html>`__
    API command.
    """

    StepType: RecommendationStepType
    JobName: RecommendationJobName
    Status: RecommendationJobStatus
    InferenceBenchmark: Optional[RecommendationJobInferenceBenchmark]


InferenceRecommendationsJobSteps = List[InferenceRecommendationsJobStep]
InferenceRecommendationsJobs = List[InferenceRecommendationsJob]


class LabelCountersForWorkteam(TypedDict, total=False):
    """Provides counts for human-labeled tasks in the labeling job."""

    HumanLabeled: Optional[LabelCounter]
    PendingHuman: Optional[LabelCounter]
    Total: Optional[LabelCounter]


class LabelingJobForWorkteamSummary(TypedDict, total=False):
    """Provides summary information for a work team."""

    LabelingJobName: Optional[LabelingJobName]
    JobReferenceCode: JobReferenceCode
    WorkRequesterAccountId: AccountId
    CreationTime: Timestamp
    LabelCounters: Optional[LabelCountersForWorkteam]
    NumberOfHumanWorkersPerDataObject: Optional[NumberOfHumanWorkersPerDataObject]


LabelingJobForWorkteamSummaryList = List[LabelingJobForWorkteamSummary]


class LabelingJobSummary(TypedDict, total=False):
    """Provides summary information about a labeling job."""

    LabelingJobName: LabelingJobName
    LabelingJobArn: LabelingJobArn
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    LabelingJobStatus: LabelingJobStatus
    LabelCounters: LabelCounters
    WorkteamArn: WorkteamArn
    PreHumanTaskLambdaArn: Optional[LambdaFunctionArn]
    AnnotationConsolidationLambdaArn: Optional[LambdaFunctionArn]
    FailureReason: Optional[FailureReason]
    LabelingJobOutput: Optional[LabelingJobOutput]
    InputConfig: Optional[LabelingJobInputConfig]


LabelingJobSummaryList = List[LabelingJobSummary]


class LambdaStepMetadata(TypedDict, total=False):
    """Metadata for a Lambda step."""

    Arn: Optional[String256]
    OutputParameters: Optional[OutputParameterList]


class LineageGroupSummary(TypedDict, total=False):
    """Lists a summary of the properties of a lineage group. A lineage group
    provides a group of shareable lineage entity resources.
    """

    LineageGroupArn: Optional[LineageGroupArn]
    LineageGroupName: Optional[ExperimentEntityName]
    DisplayName: Optional[ExperimentEntityName]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


LineageGroupSummaries = List[LineageGroupSummary]


class ListActionsRequest(ServiceRequest):
    SourceUri: Optional[SourceUri]
    ActionType: Optional[String256]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortActionsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListActionsResponse(TypedDict, total=False):
    ActionSummaries: Optional[ActionSummaries]
    NextToken: Optional[NextToken]


class ListAlgorithmsInput(ServiceRequest):
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    NextToken: Optional[NextToken]
    SortBy: Optional[AlgorithmSortBy]
    SortOrder: Optional[SortOrder]


class ListAlgorithmsOutput(TypedDict, total=False):
    AlgorithmSummaryList: AlgorithmSummaryList
    NextToken: Optional[NextToken]


class ListAliasesRequest(ServiceRequest):
    ImageName: ImageName
    Alias: Optional[SageMakerImageVersionAlias]
    Version: Optional[ImageVersionNumber]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListAliasesResponse(TypedDict, total=False):
    SageMakerImageVersionAliases: Optional[SageMakerImageVersionAliases]
    NextToken: Optional[NextToken]


class ListAppImageConfigsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    NameContains: Optional[AppImageConfigName]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    ModifiedTimeBefore: Optional[Timestamp]
    ModifiedTimeAfter: Optional[Timestamp]
    SortBy: Optional[AppImageConfigSortKey]
    SortOrder: Optional[SortOrder]


class ListAppImageConfigsResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    AppImageConfigs: Optional[AppImageConfigList]


class ListAppsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortOrder: Optional[SortOrder]
    SortBy: Optional[AppSortKey]
    DomainIdEquals: Optional[DomainId]
    UserProfileNameEquals: Optional[UserProfileName]
    SpaceNameEquals: Optional[SpaceName]


class ListAppsResponse(TypedDict, total=False):
    Apps: Optional[AppList]
    NextToken: Optional[NextToken]


class ListArtifactsRequest(ServiceRequest):
    SourceUri: Optional[SourceUri]
    ArtifactType: Optional[String256]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortArtifactsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListArtifactsResponse(TypedDict, total=False):
    ArtifactSummaries: Optional[ArtifactSummaries]
    NextToken: Optional[NextToken]


class ListAssociationsRequest(ServiceRequest):
    SourceArn: Optional[AssociationEntityArn]
    DestinationArn: Optional[AssociationEntityArn]
    SourceType: Optional[String256]
    DestinationType: Optional[String256]
    AssociationType: Optional[AssociationEdgeType]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortAssociationsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListAssociationsResponse(TypedDict, total=False):
    AssociationSummaries: Optional[AssociationSummaries]
    NextToken: Optional[NextToken]


class ListAutoMLJobsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[AutoMLNameContains]
    StatusEquals: Optional[AutoMLJobStatus]
    SortOrder: Optional[AutoMLSortOrder]
    SortBy: Optional[AutoMLSortBy]
    MaxResults: Optional[AutoMLMaxResults]
    NextToken: Optional[NextToken]


class ListAutoMLJobsResponse(TypedDict, total=False):
    AutoMLJobSummaries: AutoMLJobSummaries
    NextToken: Optional[NextToken]


class ListCandidatesForAutoMLJobRequest(ServiceRequest):
    AutoMLJobName: AutoMLJobName
    StatusEquals: Optional[CandidateStatus]
    CandidateNameEquals: Optional[CandidateName]
    SortOrder: Optional[AutoMLSortOrder]
    SortBy: Optional[CandidateSortBy]
    MaxResults: Optional[AutoMLMaxResultsForTrials]
    NextToken: Optional[NextToken]


class ListCandidatesForAutoMLJobResponse(TypedDict, total=False):
    Candidates: AutoMLCandidates
    NextToken: Optional[NextToken]


class ListClusterNodesRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    InstanceGroupNameContains: Optional[ClusterInstanceGroupName]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    SortBy: Optional[ClusterSortBy]
    SortOrder: Optional[SortOrder]


class ListClusterNodesResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    ClusterNodeSummaries: ClusterNodeSummaries


class ListClusterSchedulerConfigsRequest(ServiceRequest):
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    NameContains: Optional[EntityName]
    ClusterArn: Optional[ClusterArn]
    Status: Optional[SchedulerResourceStatus]
    SortBy: Optional[SortClusterSchedulerConfigBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListClusterSchedulerConfigsResponse(TypedDict, total=False):
    ClusterSchedulerConfigSummaries: Optional[ClusterSchedulerConfigSummaryList]
    NextToken: Optional[NextToken]


class ListClustersRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    NextToken: Optional[NextToken]
    SortBy: Optional[ClusterSortBy]
    SortOrder: Optional[SortOrder]
    TrainingPlanArn: Optional[TrainingPlanArn]


class ListClustersResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    ClusterSummaries: ClusterSummaries


class ListCodeRepositoriesInput(ServiceRequest):
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[CodeRepositoryNameContains]
    NextToken: Optional[NextToken]
    SortBy: Optional[CodeRepositorySortBy]
    SortOrder: Optional[CodeRepositorySortOrder]


class ListCodeRepositoriesOutput(TypedDict, total=False):
    CodeRepositorySummaryList: CodeRepositorySummaryList
    NextToken: Optional[NextToken]


class ListCompilationJobsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    LastModifiedTimeAfter: Optional[LastModifiedTime]
    LastModifiedTimeBefore: Optional[LastModifiedTime]
    NameContains: Optional[NameContains]
    StatusEquals: Optional[CompilationJobStatus]
    SortBy: Optional[ListCompilationJobsSortBy]
    SortOrder: Optional[SortOrder]


class ListCompilationJobsResponse(TypedDict, total=False):
    CompilationJobSummaries: CompilationJobSummaries
    NextToken: Optional[NextToken]


class ListComputeQuotasRequest(ServiceRequest):
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    NameContains: Optional[EntityName]
    Status: Optional[SchedulerResourceStatus]
    ClusterArn: Optional[ClusterArn]
    SortBy: Optional[SortQuotaBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListComputeQuotasResponse(TypedDict, total=False):
    ComputeQuotaSummaries: Optional[ComputeQuotaSummaryList]
    NextToken: Optional[NextToken]


class ListContextsRequest(ServiceRequest):
    SourceUri: Optional[SourceUri]
    ContextType: Optional[String256]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortContextsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListContextsResponse(TypedDict, total=False):
    ContextSummaries: Optional[ContextSummaries]
    NextToken: Optional[NextToken]


class ListDataQualityJobDefinitionsRequest(ServiceRequest):
    EndpointName: Optional[EndpointName]
    SortBy: Optional[MonitoringJobDefinitionSortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]


class MonitoringJobDefinitionSummary(TypedDict, total=False):
    """Summary information about a monitoring job."""

    MonitoringJobDefinitionName: MonitoringJobDefinitionName
    MonitoringJobDefinitionArn: MonitoringJobDefinitionArn
    CreationTime: Timestamp
    EndpointName: EndpointName


MonitoringJobDefinitionSummaryList = List[MonitoringJobDefinitionSummary]


class ListDataQualityJobDefinitionsResponse(TypedDict, total=False):
    JobDefinitionSummaries: MonitoringJobDefinitionSummaryList
    NextToken: Optional[NextToken]


class ListDeviceFleetsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListMaxResults]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[NameContains]
    SortBy: Optional[ListDeviceFleetsSortBy]
    SortOrder: Optional[SortOrder]


class ListDeviceFleetsResponse(TypedDict, total=False):
    DeviceFleetSummaries: DeviceFleetSummaries
    NextToken: Optional[NextToken]


class ListDevicesRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListMaxResults]
    LatestHeartbeatAfter: Optional[Timestamp]
    ModelName: Optional[EntityName]
    DeviceFleetName: Optional[EntityName]


class ListDevicesResponse(TypedDict, total=False):
    DeviceSummaries: DeviceSummaries
    NextToken: Optional[NextToken]


class ListDomainsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListDomainsResponse(TypedDict, total=False):
    Domains: Optional[DomainList]
    NextToken: Optional[NextToken]


class ListEdgeDeploymentPlansRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListMaxResults]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[NameContains]
    DeviceFleetNameContains: Optional[NameContains]
    SortBy: Optional[ListEdgeDeploymentPlansSortBy]
    SortOrder: Optional[SortOrder]


class ListEdgeDeploymentPlansResponse(TypedDict, total=False):
    EdgeDeploymentPlanSummaries: EdgeDeploymentPlanSummaries
    NextToken: Optional[NextToken]


class ListEdgePackagingJobsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListMaxResults]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[NameContains]
    ModelNameContains: Optional[NameContains]
    StatusEquals: Optional[EdgePackagingJobStatus]
    SortBy: Optional[ListEdgePackagingJobsSortBy]
    SortOrder: Optional[SortOrder]


class ListEdgePackagingJobsResponse(TypedDict, total=False):
    EdgePackagingJobSummaries: EdgePackagingJobSummaries
    NextToken: Optional[NextToken]


class ListEndpointConfigsInput(ServiceRequest):
    SortBy: Optional[EndpointConfigSortKey]
    SortOrder: Optional[OrderKey]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[EndpointConfigNameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]


class ListEndpointConfigsOutput(TypedDict, total=False):
    EndpointConfigs: EndpointConfigSummaryList
    NextToken: Optional[PaginationToken]


class ListEndpointsInput(ServiceRequest):
    SortBy: Optional[EndpointSortKey]
    SortOrder: Optional[OrderKey]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[EndpointNameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    StatusEquals: Optional[EndpointStatus]


class ListEndpointsOutput(TypedDict, total=False):
    Endpoints: EndpointSummaryList
    NextToken: Optional[PaginationToken]


class ListExperimentsRequest(ServiceRequest):
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortExperimentsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListExperimentsResponse(TypedDict, total=False):
    ExperimentSummaries: Optional[ExperimentSummaries]
    NextToken: Optional[NextToken]


class ListFeatureGroupsRequest(ServiceRequest):
    NameContains: Optional[FeatureGroupNameContains]
    FeatureGroupStatusEquals: Optional[FeatureGroupStatus]
    OfflineStoreStatusEquals: Optional[OfflineStoreStatusValue]
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    SortOrder: Optional[FeatureGroupSortOrder]
    SortBy: Optional[FeatureGroupSortBy]
    MaxResults: Optional[FeatureGroupMaxResults]
    NextToken: Optional[NextToken]


class ListFeatureGroupsResponse(TypedDict, total=False):
    FeatureGroupSummaries: FeatureGroupSummaries
    NextToken: Optional[NextToken]


class ListFlowDefinitionsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListFlowDefinitionsResponse(TypedDict, total=False):
    FlowDefinitionSummaries: FlowDefinitionSummaries
    NextToken: Optional[NextToken]


class ListHubContentVersionsRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentType: HubContentType
    HubContentName: HubContentName
    MinVersion: Optional[HubContentVersion]
    MaxSchemaVersion: Optional[DocumentSchemaVersion]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    SortBy: Optional[HubContentSortBy]
    SortOrder: Optional[SortOrder]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListHubContentVersionsResponse(TypedDict, total=False):
    HubContentSummaries: HubContentInfoList
    NextToken: Optional[NextToken]


class ListHubContentsRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentType: HubContentType
    NameContains: Optional[NameContains]
    MaxSchemaVersion: Optional[DocumentSchemaVersion]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    SortBy: Optional[HubContentSortBy]
    SortOrder: Optional[SortOrder]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListHubContentsResponse(TypedDict, total=False):
    HubContentSummaries: HubContentInfoList
    NextToken: Optional[NextToken]


class ListHubsRequest(ServiceRequest):
    NameContains: Optional[NameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    SortBy: Optional[HubSortBy]
    SortOrder: Optional[SortOrder]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListHubsResponse(TypedDict, total=False):
    HubSummaries: HubInfoList
    NextToken: Optional[NextToken]


class ListHumanTaskUisRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListHumanTaskUisResponse(TypedDict, total=False):
    HumanTaskUiSummaries: HumanTaskUiSummaries
    NextToken: Optional[NextToken]


class ListHyperParameterTuningJobsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortBy: Optional[HyperParameterTuningJobSortByOptions]
    SortOrder: Optional[SortOrder]
    NameContains: Optional[NameContains]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    StatusEquals: Optional[HyperParameterTuningJobStatus]


class ListHyperParameterTuningJobsResponse(TypedDict, total=False):
    HyperParameterTuningJobSummaries: HyperParameterTuningJobSummaries
    NextToken: Optional[NextToken]


class ListImageVersionsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    ImageName: ImageName
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    SortBy: Optional[ImageVersionSortBy]
    SortOrder: Optional[ImageVersionSortOrder]


class ListImageVersionsResponse(TypedDict, total=False):
    ImageVersions: Optional[ImageVersions]
    NextToken: Optional[NextToken]


class ListImagesRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[ImageNameContains]
    NextToken: Optional[NextToken]
    SortBy: Optional[ImageSortBy]
    SortOrder: Optional[ImageSortOrder]


class ListImagesResponse(TypedDict, total=False):
    Images: Optional[Images]
    NextToken: Optional[NextToken]


class ListInferenceComponentsInput(ServiceRequest):
    SortBy: Optional[InferenceComponentSortKey]
    SortOrder: Optional[OrderKey]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[InferenceComponentNameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    StatusEquals: Optional[InferenceComponentStatus]
    EndpointNameEquals: Optional[EndpointName]
    VariantNameEquals: Optional[VariantName]


class ListInferenceComponentsOutput(TypedDict, total=False):
    InferenceComponents: InferenceComponentSummaryList
    NextToken: Optional[PaginationToken]


class ListInferenceExperimentsRequest(ServiceRequest):
    NameContains: Optional[NameContains]
    Type: Optional[InferenceExperimentType]
    StatusEquals: Optional[InferenceExperimentStatus]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    SortBy: Optional[SortInferenceExperimentsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListInferenceExperimentsResponse(TypedDict, total=False):
    InferenceExperiments: Optional[InferenceExperimentList]
    NextToken: Optional[NextToken]


class ListInferenceRecommendationsJobStepsRequest(ServiceRequest):
    JobName: RecommendationJobName
    Status: Optional[RecommendationJobStatus]
    StepType: Optional[RecommendationStepType]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ListInferenceRecommendationsJobStepsResponse(TypedDict, total=False):
    Steps: Optional[InferenceRecommendationsJobSteps]
    NextToken: Optional[NextToken]


class ListInferenceRecommendationsJobsRequest(ServiceRequest):
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    LastModifiedTimeAfter: Optional[LastModifiedTime]
    LastModifiedTimeBefore: Optional[LastModifiedTime]
    NameContains: Optional[NameContains]
    StatusEquals: Optional[RecommendationJobStatus]
    SortBy: Optional[ListInferenceRecommendationsJobsSortBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    ModelNameEquals: Optional[ModelName]
    ModelPackageVersionArnEquals: Optional[ModelPackageArn]


class ListInferenceRecommendationsJobsResponse(TypedDict, total=False):
    InferenceRecommendationsJobs: InferenceRecommendationsJobs
    NextToken: Optional[NextToken]


class ListLabelingJobsForWorkteamRequest(ServiceRequest):
    WorkteamArn: WorkteamArn
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    JobReferenceCodeContains: Optional[JobReferenceCodeContains]
    SortBy: Optional[ListLabelingJobsForWorkteamSortByOptions]
    SortOrder: Optional[SortOrder]


class ListLabelingJobsForWorkteamResponse(TypedDict, total=False):
    LabelingJobSummaryList: LabelingJobForWorkteamSummaryList
    NextToken: Optional[NextToken]


class ListLabelingJobsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    NameContains: Optional[NameContains]
    SortBy: Optional[SortBy]
    SortOrder: Optional[SortOrder]
    StatusEquals: Optional[LabelingJobStatus]


class ListLabelingJobsResponse(TypedDict, total=False):
    LabelingJobSummaryList: Optional[LabelingJobSummaryList]
    NextToken: Optional[NextToken]


ListLineageEntityParameterKey = List[StringParameterValue]


class ListLineageGroupsRequest(ServiceRequest):
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortLineageGroupsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListLineageGroupsResponse(TypedDict, total=False):
    LineageGroupSummaries: Optional[LineageGroupSummaries]
    NextToken: Optional[NextToken]


class ListMlflowTrackingServersRequest(ServiceRequest):
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    TrackingServerStatus: Optional[TrackingServerStatus]
    MlflowVersion: Optional[MlflowVersion]
    SortBy: Optional[SortTrackingServerBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class TrackingServerSummary(TypedDict, total=False):
    """The summary of the tracking server to list."""

    TrackingServerArn: Optional[TrackingServerArn]
    TrackingServerName: Optional[TrackingServerName]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    TrackingServerStatus: Optional[TrackingServerStatus]
    IsActive: Optional[IsTrackingServerActive]
    MlflowVersion: Optional[MlflowVersion]


TrackingServerSummaryList = List[TrackingServerSummary]


class ListMlflowTrackingServersResponse(TypedDict, total=False):
    TrackingServerSummaries: Optional[TrackingServerSummaryList]
    NextToken: Optional[NextToken]


class ListModelBiasJobDefinitionsRequest(ServiceRequest):
    EndpointName: Optional[EndpointName]
    SortBy: Optional[MonitoringJobDefinitionSortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]


class ListModelBiasJobDefinitionsResponse(TypedDict, total=False):
    JobDefinitionSummaries: MonitoringJobDefinitionSummaryList
    NextToken: Optional[NextToken]


class ListModelCardExportJobsRequest(ServiceRequest):
    ModelCardName: EntityName
    ModelCardVersion: Optional[Integer]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    ModelCardExportJobNameContains: Optional[EntityName]
    StatusEquals: Optional[ModelCardExportJobStatus]
    SortBy: Optional[ModelCardExportJobSortBy]
    SortOrder: Optional[ModelCardExportJobSortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ModelCardExportJobSummary(TypedDict, total=False):
    """The summary of the Amazon SageMaker Model Card export job."""

    ModelCardExportJobName: EntityName
    ModelCardExportJobArn: ModelCardExportJobArn
    Status: ModelCardExportJobStatus
    ModelCardName: EntityName
    ModelCardVersion: Integer
    CreatedAt: Timestamp
    LastModifiedAt: Timestamp


ModelCardExportJobSummaryList = List[ModelCardExportJobSummary]


class ListModelCardExportJobsResponse(TypedDict, total=False):
    ModelCardExportJobSummaries: ModelCardExportJobSummaryList
    NextToken: Optional[NextToken]


class ListModelCardVersionsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    ModelCardName: ModelCardNameOrArn
    ModelCardStatus: Optional[ModelCardStatus]
    NextToken: Optional[NextToken]
    SortBy: Optional[ModelCardVersionSortBy]
    SortOrder: Optional[ModelCardSortOrder]


class ModelCardVersionSummary(TypedDict, total=False):
    """A summary of a specific version of the model card."""

    ModelCardName: EntityName
    ModelCardArn: ModelCardArn
    ModelCardStatus: ModelCardStatus
    ModelCardVersion: Integer
    CreationTime: Timestamp
    LastModifiedTime: Optional[Timestamp]


ModelCardVersionSummaryList = List[ModelCardVersionSummary]


class ListModelCardVersionsResponse(TypedDict, total=False):
    ModelCardVersionSummaryList: ModelCardVersionSummaryList
    NextToken: Optional[NextToken]


class ListModelCardsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[EntityName]
    ModelCardStatus: Optional[ModelCardStatus]
    NextToken: Optional[NextToken]
    SortBy: Optional[ModelCardSortBy]
    SortOrder: Optional[ModelCardSortOrder]


class ModelCardSummary(TypedDict, total=False):
    """A summary of the model card."""

    ModelCardName: EntityName
    ModelCardArn: ModelCardArn
    ModelCardStatus: ModelCardStatus
    CreationTime: Timestamp
    LastModifiedTime: Optional[Timestamp]


ModelCardSummaryList = List[ModelCardSummary]


class ListModelCardsResponse(TypedDict, total=False):
    ModelCardSummaries: ModelCardSummaryList
    NextToken: Optional[NextToken]


class ListModelExplainabilityJobDefinitionsRequest(ServiceRequest):
    EndpointName: Optional[EndpointName]
    SortBy: Optional[MonitoringJobDefinitionSortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]


class ListModelExplainabilityJobDefinitionsResponse(TypedDict, total=False):
    JobDefinitionSummaries: MonitoringJobDefinitionSummaryList
    NextToken: Optional[NextToken]


class ModelMetadataFilter(TypedDict, total=False):
    """Part of the search expression. You can specify the name and value
    (domain, task, framework, framework version, task, and model).
    """

    Name: ModelMetadataFilterType
    Value: String256


ModelMetadataFilters = List[ModelMetadataFilter]


class ModelMetadataSearchExpression(TypedDict, total=False):
    """One or more filters that searches for the specified resource or
    resources in a search. All resource objects that satisfy the
    expression's condition are included in the search results
    """

    Filters: Optional[ModelMetadataFilters]


class ListModelMetadataRequest(ServiceRequest):
    SearchExpression: Optional[ModelMetadataSearchExpression]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ModelMetadataSummary(TypedDict, total=False):
    """A summary of the model metadata."""

    Domain: String
    Framework: String
    Task: String
    Model: String
    FrameworkVersion: String


ModelMetadataSummaries = List[ModelMetadataSummary]


class ListModelMetadataResponse(TypedDict, total=False):
    ModelMetadataSummaries: ModelMetadataSummaries
    NextToken: Optional[NextToken]


class ListModelPackageGroupsInput(ServiceRequest):
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    NextToken: Optional[NextToken]
    SortBy: Optional[ModelPackageGroupSortBy]
    SortOrder: Optional[SortOrder]
    CrossAccountFilterOption: Optional[CrossAccountFilterOption]


class ModelPackageGroupSummary(TypedDict, total=False):
    """Summary information about a model group."""

    ModelPackageGroupName: EntityName
    ModelPackageGroupArn: ModelPackageGroupArn
    ModelPackageGroupDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    ModelPackageGroupStatus: ModelPackageGroupStatus


ModelPackageGroupSummaryList = List[ModelPackageGroupSummary]


class ListModelPackageGroupsOutput(TypedDict, total=False):
    ModelPackageGroupSummaryList: ModelPackageGroupSummaryList
    NextToken: Optional[NextToken]


class ListModelPackagesInput(ServiceRequest):
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    ModelApprovalStatus: Optional[ModelApprovalStatus]
    ModelPackageGroupName: Optional[ArnOrName]
    ModelPackageType: Optional[ModelPackageType]
    NextToken: Optional[NextToken]
    SortBy: Optional[ModelPackageSortBy]
    SortOrder: Optional[SortOrder]


class ModelPackageSummary(TypedDict, total=False):
    """Provides summary information about a model package."""

    ModelPackageName: Optional[EntityName]
    ModelPackageGroupName: Optional[EntityName]
    ModelPackageVersion: Optional[ModelPackageVersion]
    ModelPackageArn: ModelPackageArn
    ModelPackageDescription: Optional[EntityDescription]
    CreationTime: CreationTime
    ModelPackageStatus: ModelPackageStatus
    ModelApprovalStatus: Optional[ModelApprovalStatus]
    ModelLifeCycle: Optional[ModelLifeCycle]


ModelPackageSummaryList = List[ModelPackageSummary]


class ListModelPackagesOutput(TypedDict, total=False):
    ModelPackageSummaryList: ModelPackageSummaryList
    NextToken: Optional[NextToken]


class ListModelQualityJobDefinitionsRequest(ServiceRequest):
    EndpointName: Optional[EndpointName]
    SortBy: Optional[MonitoringJobDefinitionSortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]


class ListModelQualityJobDefinitionsResponse(TypedDict, total=False):
    JobDefinitionSummaries: MonitoringJobDefinitionSummaryList
    NextToken: Optional[NextToken]


class ListModelsInput(ServiceRequest):
    SortBy: Optional[ModelSortKey]
    SortOrder: Optional[OrderKey]
    NextToken: Optional[PaginationToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[ModelNameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]


class ModelSummary(TypedDict, total=False):
    """Provides summary information about a model."""

    ModelName: ModelName
    ModelArn: ModelArn
    CreationTime: Timestamp


ModelSummaryList = List[ModelSummary]


class ListModelsOutput(TypedDict, total=False):
    Models: ModelSummaryList
    NextToken: Optional[PaginationToken]


class ListMonitoringAlertHistoryRequest(ServiceRequest):
    MonitoringScheduleName: Optional[MonitoringScheduleName]
    MonitoringAlertName: Optional[MonitoringAlertName]
    SortBy: Optional[MonitoringAlertHistorySortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    StatusEquals: Optional[MonitoringAlertStatus]


class MonitoringAlertHistorySummary(TypedDict, total=False):
    """Provides summary information of an alert's history."""

    MonitoringScheduleName: MonitoringScheduleName
    MonitoringAlertName: MonitoringAlertName
    CreationTime: Timestamp
    AlertStatus: MonitoringAlertStatus


MonitoringAlertHistoryList = List[MonitoringAlertHistorySummary]


class ListMonitoringAlertHistoryResponse(TypedDict, total=False):
    MonitoringAlertHistory: Optional[MonitoringAlertHistoryList]
    NextToken: Optional[NextToken]


class ListMonitoringAlertsRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ModelDashboardIndicatorAction(TypedDict, total=False):
    """An alert action taken to light up an icon on the Amazon SageMaker Model
    Dashboard when an alert goes into ``InAlert`` status.
    """

    Enabled: Optional[Boolean]


class MonitoringAlertActions(TypedDict, total=False):
    """A list of alert actions taken in response to an alert going into
    ``InAlert`` status.
    """

    ModelDashboardIndicator: Optional[ModelDashboardIndicatorAction]


class MonitoringAlertSummary(TypedDict, total=False):
    """Provides summary information about a monitor alert."""

    MonitoringAlertName: MonitoringAlertName
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    AlertStatus: MonitoringAlertStatus
    DatapointsToAlert: MonitoringDatapointsToAlert
    EvaluationPeriod: MonitoringEvaluationPeriod
    Actions: MonitoringAlertActions


MonitoringAlertSummaryList = List[MonitoringAlertSummary]


class ListMonitoringAlertsResponse(TypedDict, total=False):
    MonitoringAlertSummaries: Optional[MonitoringAlertSummaryList]
    NextToken: Optional[NextToken]


class ListMonitoringExecutionsRequest(ServiceRequest):
    MonitoringScheduleName: Optional[MonitoringScheduleName]
    EndpointName: Optional[EndpointName]
    SortBy: Optional[MonitoringExecutionSortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    ScheduledTimeBefore: Optional[Timestamp]
    ScheduledTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    StatusEquals: Optional[ExecutionStatus]
    MonitoringJobDefinitionName: Optional[MonitoringJobDefinitionName]
    MonitoringTypeEquals: Optional[MonitoringType]


MonitoringExecutionSummaryList = List[MonitoringExecutionSummary]


class ListMonitoringExecutionsResponse(TypedDict, total=False):
    MonitoringExecutionSummaries: MonitoringExecutionSummaryList
    NextToken: Optional[NextToken]


class ListMonitoringSchedulesRequest(ServiceRequest):
    EndpointName: Optional[EndpointName]
    SortBy: Optional[MonitoringScheduleSortKey]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[NameContains]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    StatusEquals: Optional[ScheduleStatus]
    MonitoringJobDefinitionName: Optional[MonitoringJobDefinitionName]
    MonitoringTypeEquals: Optional[MonitoringType]


class MonitoringScheduleSummary(TypedDict, total=False):
    """Summarizes the monitoring schedule."""

    MonitoringScheduleName: MonitoringScheduleName
    MonitoringScheduleArn: MonitoringScheduleArn
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    MonitoringScheduleStatus: ScheduleStatus
    EndpointName: Optional[EndpointName]
    MonitoringJobDefinitionName: Optional[MonitoringJobDefinitionName]
    MonitoringType: Optional[MonitoringType]


MonitoringScheduleSummaryList = List[MonitoringScheduleSummary]


class ListMonitoringSchedulesResponse(TypedDict, total=False):
    MonitoringScheduleSummaries: MonitoringScheduleSummaryList
    NextToken: Optional[NextToken]


class ListNotebookInstanceLifecycleConfigsInput(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortBy: Optional[NotebookInstanceLifecycleConfigSortKey]
    SortOrder: Optional[NotebookInstanceLifecycleConfigSortOrder]
    NameContains: Optional[NotebookInstanceLifecycleConfigNameContains]
    CreationTimeBefore: Optional[CreationTime]
    CreationTimeAfter: Optional[CreationTime]
    LastModifiedTimeBefore: Optional[LastModifiedTime]
    LastModifiedTimeAfter: Optional[LastModifiedTime]


class NotebookInstanceLifecycleConfigSummary(TypedDict, total=False):
    """Provides a summary of a notebook instance lifecycle configuration."""

    NotebookInstanceLifecycleConfigName: NotebookInstanceLifecycleConfigName
    NotebookInstanceLifecycleConfigArn: NotebookInstanceLifecycleConfigArn
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]


NotebookInstanceLifecycleConfigSummaryList = List[NotebookInstanceLifecycleConfigSummary]


class ListNotebookInstanceLifecycleConfigsOutput(TypedDict, total=False):
    NextToken: Optional[NextToken]
    NotebookInstanceLifecycleConfigs: Optional[NotebookInstanceLifecycleConfigSummaryList]


class ListNotebookInstancesInput(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortBy: Optional[NotebookInstanceSortKey]
    SortOrder: Optional[NotebookInstanceSortOrder]
    NameContains: Optional[NotebookInstanceNameContains]
    CreationTimeBefore: Optional[CreationTime]
    CreationTimeAfter: Optional[CreationTime]
    LastModifiedTimeBefore: Optional[LastModifiedTime]
    LastModifiedTimeAfter: Optional[LastModifiedTime]
    StatusEquals: Optional[NotebookInstanceStatus]
    NotebookInstanceLifecycleConfigNameContains: Optional[NotebookInstanceLifecycleConfigName]
    DefaultCodeRepositoryContains: Optional[CodeRepositoryContains]
    AdditionalCodeRepositoryEquals: Optional[CodeRepositoryNameOrUrl]


class NotebookInstanceSummary(TypedDict, total=False):
    """Provides summary information for an SageMaker AI notebook instance."""

    NotebookInstanceName: NotebookInstanceName
    NotebookInstanceArn: NotebookInstanceArn
    NotebookInstanceStatus: Optional[NotebookInstanceStatus]
    Url: Optional[NotebookInstanceUrl]
    InstanceType: Optional[InstanceType]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]
    NotebookInstanceLifecycleConfigName: Optional[NotebookInstanceLifecycleConfigName]
    DefaultCodeRepository: Optional[CodeRepositoryNameOrUrl]
    AdditionalCodeRepositories: Optional[AdditionalCodeRepositoryNamesOrUrls]


NotebookInstanceSummaryList = List[NotebookInstanceSummary]


class ListNotebookInstancesOutput(TypedDict, total=False):
    NextToken: Optional[NextToken]
    NotebookInstances: Optional[NotebookInstanceSummaryList]


class ListOptimizationJobsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CreationTimeAfter: Optional[CreationTime]
    CreationTimeBefore: Optional[CreationTime]
    LastModifiedTimeAfter: Optional[LastModifiedTime]
    LastModifiedTimeBefore: Optional[LastModifiedTime]
    OptimizationContains: Optional[NameContains]
    NameContains: Optional[NameContains]
    StatusEquals: Optional[OptimizationJobStatus]
    SortBy: Optional[ListOptimizationJobsSortBy]
    SortOrder: Optional[SortOrder]


OptimizationTypes = List[OptimizationType]


class OptimizationJobSummary(TypedDict, total=False):
    """Summarizes an optimization job by providing some of its key properties."""

    OptimizationJobName: EntityName
    OptimizationJobArn: OptimizationJobArn
    CreationTime: CreationTime
    OptimizationJobStatus: OptimizationJobStatus
    OptimizationStartTime: Optional[Timestamp]
    OptimizationEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[LastModifiedTime]
    DeploymentInstanceType: OptimizationJobDeploymentInstanceType
    OptimizationTypes: OptimizationTypes


OptimizationJobSummaries = List[OptimizationJobSummary]


class ListOptimizationJobsResponse(TypedDict, total=False):
    OptimizationJobSummaries: OptimizationJobSummaries
    NextToken: Optional[NextToken]


class ListPartnerAppsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class PartnerAppSummary(TypedDict, total=False):
    """A subset of information related to a SageMaker Partner AI App. This
    information is used as part of the ``ListPartnerApps`` API response.
    """

    Arn: Optional[PartnerAppArn]
    Name: Optional[PartnerAppName]
    Type: Optional[PartnerAppType]
    Status: Optional[PartnerAppStatus]
    CreationTime: Optional[Timestamp]


PartnerAppSummaries = List[PartnerAppSummary]


class ListPartnerAppsResponse(TypedDict, total=False):
    Summaries: Optional[PartnerAppSummaries]
    NextToken: Optional[NextToken]


class ListPipelineExecutionStepsRequest(ServiceRequest):
    PipelineExecutionArn: Optional[PipelineExecutionArn]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortOrder: Optional[SortOrder]


class SelectiveExecutionResult(TypedDict, total=False):
    """The ARN from an execution of the current pipeline."""

    SourcePipelineExecutionArn: Optional[PipelineExecutionArn]


class QualityCheckStepMetadata(TypedDict, total=False):
    """Container for the metadata for a Quality check step. For more
    information, see the topic on `QualityCheck
    step <https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-quality-check>`__
    in the *Amazon SageMaker Developer Guide*.
    """

    CheckType: Optional[String256]
    BaselineUsedForDriftCheckStatistics: Optional[String1024]
    BaselineUsedForDriftCheckConstraints: Optional[String1024]
    CalculatedBaselineStatistics: Optional[String1024]
    CalculatedBaselineConstraints: Optional[String1024]
    ModelPackageGroupName: Optional[String256]
    ViolationReport: Optional[String1024]
    CheckJobArn: Optional[String256]
    SkipCheck: Optional[Boolean]
    RegisterNewBaseline: Optional[Boolean]


class RegisterModelStepMetadata(TypedDict, total=False):
    """Metadata for a register model job step."""

    Arn: Optional[String256]


class ModelStepMetadata(TypedDict, total=False):
    """Metadata for Model steps."""

    Arn: Optional[String256]


class TuningJobStepMetaData(TypedDict, total=False):
    """Metadata for a tuning step."""

    Arn: Optional[HyperParameterTuningJobArn]


class TransformJobStepMetadata(TypedDict, total=False):
    """Metadata for a transform job step."""

    Arn: Optional[TransformJobArn]


class ProcessingJobStepMetadata(TypedDict, total=False):
    """Metadata for a processing job step."""

    Arn: Optional[ProcessingJobArn]


class TrainingJobStepMetadata(TypedDict, total=False):
    """Metadata for a training job step."""

    Arn: Optional[TrainingJobArn]


class PipelineExecutionStepMetadata(TypedDict, total=False):
    """Metadata for a step execution."""

    TrainingJob: Optional[TrainingJobStepMetadata]
    ProcessingJob: Optional[ProcessingJobStepMetadata]
    TransformJob: Optional[TransformJobStepMetadata]
    TuningJob: Optional[TuningJobStepMetaData]
    Model: Optional[ModelStepMetadata]
    RegisterModel: Optional[RegisterModelStepMetadata]
    Condition: Optional[ConditionStepMetadata]
    Callback: Optional[CallbackStepMetadata]
    Lambda: Optional[LambdaStepMetadata]
    EMR: Optional[EMRStepMetadata]
    QualityCheck: Optional[QualityCheckStepMetadata]
    ClarifyCheck: Optional[ClarifyCheckStepMetadata]
    Fail: Optional[FailStepMetadata]
    AutoMLJob: Optional[AutoMLJobStepMetadata]
    Endpoint: Optional[EndpointStepMetadata]
    EndpointConfig: Optional[EndpointConfigStepMetadata]


class PipelineExecutionStep(TypedDict, total=False):
    """An execution of a step in a pipeline."""

    StepName: Optional[StepName]
    StepDisplayName: Optional[StepDisplayName]
    StepDescription: Optional[StepDescription]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    StepStatus: Optional[StepStatus]
    CacheHitResult: Optional[CacheHitResult]
    FailureReason: Optional[FailureReason]
    Metadata: Optional[PipelineExecutionStepMetadata]
    AttemptCount: Optional[Integer]
    SelectiveExecutionResult: Optional[SelectiveExecutionResult]


PipelineExecutionStepList = List[PipelineExecutionStep]


class ListPipelineExecutionStepsResponse(TypedDict, total=False):
    PipelineExecutionSteps: Optional[PipelineExecutionStepList]
    NextToken: Optional[NextToken]


class ListPipelineExecutionsRequest(ServiceRequest):
    PipelineName: PipelineNameOrArn
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortPipelineExecutionsBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class PipelineExecutionSummary(TypedDict, total=False):
    """A pipeline execution summary."""

    PipelineExecutionArn: Optional[PipelineExecutionArn]
    StartTime: Optional[Timestamp]
    PipelineExecutionStatus: Optional[PipelineExecutionStatus]
    PipelineExecutionDescription: Optional[PipelineExecutionDescription]
    PipelineExecutionDisplayName: Optional[PipelineExecutionName]
    PipelineExecutionFailureReason: Optional[String3072]


PipelineExecutionSummaryList = List[PipelineExecutionSummary]


class ListPipelineExecutionsResponse(TypedDict, total=False):
    PipelineExecutionSummaries: Optional[PipelineExecutionSummaryList]
    NextToken: Optional[NextToken]


class ListPipelineParametersForExecutionRequest(ServiceRequest):
    PipelineExecutionArn: PipelineExecutionArn
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class Parameter(TypedDict, total=False):
    """Assigns a value to a named Pipeline parameter."""

    Name: PipelineParameterName
    Value: String1024


ParameterList = List[Parameter]


class ListPipelineParametersForExecutionResponse(TypedDict, total=False):
    PipelineParameters: Optional[ParameterList]
    NextToken: Optional[NextToken]


class ListPipelinesRequest(ServiceRequest):
    PipelineNamePrefix: Optional[PipelineName]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortPipelinesBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class PipelineSummary(TypedDict, total=False):
    """A summary of a pipeline."""

    PipelineArn: Optional[PipelineArn]
    PipelineName: Optional[PipelineName]
    PipelineDisplayName: Optional[PipelineName]
    PipelineDescription: Optional[PipelineDescription]
    RoleArn: Optional[RoleArn]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    LastExecutionTime: Optional[Timestamp]


PipelineSummaryList = List[PipelineSummary]


class ListPipelinesResponse(TypedDict, total=False):
    PipelineSummaries: Optional[PipelineSummaryList]
    NextToken: Optional[NextToken]


class ListProcessingJobsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[String]
    StatusEquals: Optional[ProcessingJobStatus]
    SortBy: Optional[SortBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ProcessingJobSummary(TypedDict, total=False):
    """Summary of information about a processing job."""

    ProcessingJobName: ProcessingJobName
    ProcessingJobArn: ProcessingJobArn
    CreationTime: Timestamp
    ProcessingEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    ProcessingJobStatus: ProcessingJobStatus
    FailureReason: Optional[FailureReason]
    ExitMessage: Optional[ExitMessage]


ProcessingJobSummaries = List[ProcessingJobSummary]


class ListProcessingJobsResponse(TypedDict, total=False):
    ProcessingJobSummaries: ProcessingJobSummaries
    NextToken: Optional[NextToken]


class ListProjectsInput(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    MaxResults: Optional[MaxResults]
    NameContains: Optional[ProjectEntityName]
    NextToken: Optional[NextToken]
    SortBy: Optional[ProjectSortBy]
    SortOrder: Optional[ProjectSortOrder]


class ProjectSummary(TypedDict, total=False):
    """Information about a project."""

    ProjectName: ProjectEntityName
    ProjectDescription: Optional[EntityDescription]
    ProjectArn: ProjectArn
    ProjectId: ProjectId
    CreationTime: Timestamp
    ProjectStatus: ProjectStatus


ProjectSummaryList = List[ProjectSummary]


class ListProjectsOutput(TypedDict, total=False):
    ProjectSummaryList: ProjectSummaryList
    NextToken: Optional[NextToken]


class ListResourceCatalogsRequest(ServiceRequest):
    NameContains: Optional[ResourceCatalogName]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    SortOrder: Optional[ResourceCatalogSortOrder]
    SortBy: Optional[ResourceCatalogSortBy]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class ResourceCatalog(TypedDict, total=False):
    """A resource catalog containing all of the resources of a specific
    resource type within a resource owner account. For an example on sharing
    the Amazon SageMaker Feature Store ``DefaultFeatureGroupCatalog``, see
    `Share Amazon SageMaker Catalog resource
    type <https://docs.aws.amazon.com/sagemaker/latest/APIReference/feature-store-cross-account-discoverability-share-sagemaker-catalog.html>`__
    in the Amazon SageMaker Developer Guide.
    """

    ResourceCatalogArn: ResourceCatalogArn
    ResourceCatalogName: ResourceCatalogName
    Description: ResourceCatalogDescription
    CreationTime: Timestamp


ResourceCatalogList = List[ResourceCatalog]


class ListResourceCatalogsResponse(TypedDict, total=False):
    ResourceCatalogs: Optional[ResourceCatalogList]
    NextToken: Optional[NextToken]


class ListSpacesRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortOrder: Optional[SortOrder]
    SortBy: Optional[SpaceSortKey]
    DomainIdEquals: Optional[DomainId]
    SpaceNameContains: Optional[SpaceName]


class OwnershipSettingsSummary(TypedDict, total=False):
    """Specifies summary information about the ownership settings."""

    OwnerUserProfileName: Optional[UserProfileName]


class SpaceSharingSettingsSummary(TypedDict, total=False):
    """Specifies summary information about the space sharing settings."""

    SharingType: Optional[SharingType]


class SpaceSettingsSummary(TypedDict, total=False):
    """Specifies summary information about the space settings."""

    AppType: Optional[AppType]
    SpaceStorageSettings: Optional[SpaceStorageSettings]


class SpaceDetails(TypedDict, total=False):
    """The space's details."""

    DomainId: Optional[DomainId]
    SpaceName: Optional[SpaceName]
    Status: Optional[SpaceStatus]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]
    SpaceSettingsSummary: Optional[SpaceSettingsSummary]
    SpaceSharingSettingsSummary: Optional[SpaceSharingSettingsSummary]
    OwnershipSettingsSummary: Optional[OwnershipSettingsSummary]
    SpaceDisplayName: Optional[NonEmptyString64]


SpaceList = List[SpaceDetails]


class ListSpacesResponse(TypedDict, total=False):
    Spaces: Optional[SpaceList]
    NextToken: Optional[NextToken]


class ListStageDevicesRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListMaxResults]
    EdgeDeploymentPlanName: EntityName
    ExcludeDevicesDeployedInOtherStage: Optional[Boolean]
    StageName: EntityName


class ListStageDevicesResponse(TypedDict, total=False):
    DeviceDeploymentSummaries: DeviceDeploymentSummaries
    NextToken: Optional[NextToken]


class ListStudioLifecycleConfigsRequest(ServiceRequest):
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    NameContains: Optional[StudioLifecycleConfigName]
    AppTypeEquals: Optional[StudioLifecycleConfigAppType]
    CreationTimeBefore: Optional[Timestamp]
    CreationTimeAfter: Optional[Timestamp]
    ModifiedTimeBefore: Optional[Timestamp]
    ModifiedTimeAfter: Optional[Timestamp]
    SortBy: Optional[StudioLifecycleConfigSortKey]
    SortOrder: Optional[SortOrder]


class StudioLifecycleConfigDetails(TypedDict, total=False):
    """Details of the Amazon SageMaker AI Studio Lifecycle Configuration."""

    StudioLifecycleConfigArn: Optional[StudioLifecycleConfigArn]
    StudioLifecycleConfigName: Optional[StudioLifecycleConfigName]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    StudioLifecycleConfigAppType: Optional[StudioLifecycleConfigAppType]


StudioLifecycleConfigsList = List[StudioLifecycleConfigDetails]


class ListStudioLifecycleConfigsResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    StudioLifecycleConfigs: Optional[StudioLifecycleConfigsList]


class ListSubscribedWorkteamsRequest(ServiceRequest):
    NameContains: Optional[WorkteamName]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


SubscribedWorkteams = List[SubscribedWorkteam]


class ListSubscribedWorkteamsResponse(TypedDict, total=False):
    SubscribedWorkteams: SubscribedWorkteams
    NextToken: Optional[NextToken]


class ListTagsInput(ServiceRequest):
    ResourceArn: ResourceArn
    NextToken: Optional[NextToken]
    MaxResults: Optional[ListTagsMaxResults]


class ListTagsOutput(TypedDict, total=False):
    Tags: Optional[TagList]
    NextToken: Optional[NextToken]


class ListTrainingJobsForHyperParameterTuningJobRequest(ServiceRequest):
    HyperParameterTuningJobName: HyperParameterTuningJobName
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    StatusEquals: Optional[TrainingJobStatus]
    SortBy: Optional[TrainingJobSortByOptions]
    SortOrder: Optional[SortOrder]


class ListTrainingJobsForHyperParameterTuningJobResponse(TypedDict, total=False):
    TrainingJobSummaries: HyperParameterTrainingJobSummaries
    NextToken: Optional[NextToken]


class ListTrainingJobsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[NameContains]
    StatusEquals: Optional[TrainingJobStatus]
    SortBy: Optional[SortBy]
    SortOrder: Optional[SortOrder]
    WarmPoolStatusEquals: Optional[WarmPoolResourceStatus]
    TrainingPlanArnEquals: Optional[TrainingPlanArn]


class TrainingJobSummary(TypedDict, total=False):
    """Provides summary information about a training job."""

    TrainingJobName: TrainingJobName
    TrainingJobArn: TrainingJobArn
    CreationTime: Timestamp
    TrainingEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    TrainingJobStatus: TrainingJobStatus
    SecondaryStatus: Optional[SecondaryStatus]
    WarmPoolStatus: Optional[WarmPoolStatus]
    TrainingPlanArn: Optional[TrainingPlanArn]


TrainingJobSummaries = List[TrainingJobSummary]


class ListTrainingJobsResponse(TypedDict, total=False):
    TrainingJobSummaries: TrainingJobSummaries
    NextToken: Optional[NextToken]


class TrainingPlanFilter(TypedDict, total=False):
    """A filter to apply when listing or searching for training plans.

    For more information about how to reserve GPU capacity for your
    SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see
    ``CreateTrainingPlan``.
    """

    Name: TrainingPlanFilterName
    Value: String64


TrainingPlanFilters = List[TrainingPlanFilter]


class ListTrainingPlansRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    StartTimeAfter: Optional[Timestamp]
    StartTimeBefore: Optional[Timestamp]
    SortBy: Optional[TrainingPlanSortBy]
    SortOrder: Optional[TrainingPlanSortOrder]
    Filters: Optional[TrainingPlanFilters]


class TrainingPlanSummary(TypedDict, total=False):
    """Details of the training plan.

    For more information about how to reserve GPU capacity for your
    SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see
    ``CreateTrainingPlan``.
    """

    TrainingPlanArn: TrainingPlanArn
    TrainingPlanName: TrainingPlanName
    Status: TrainingPlanStatus
    StatusMessage: Optional[TrainingPlanStatusMessage]
    DurationHours: Optional[TrainingPlanDurationHours]
    DurationMinutes: Optional[TrainingPlanDurationMinutes]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    UpfrontFee: Optional[String256]
    CurrencyCode: Optional[CurrencyCode]
    TotalInstanceCount: Optional[TotalInstanceCount]
    AvailableInstanceCount: Optional[AvailableInstanceCount]
    InUseInstanceCount: Optional[InUseInstanceCount]
    TargetResources: Optional[SageMakerResourceNames]
    ReservedCapacitySummaries: Optional[ReservedCapacitySummaries]


TrainingPlanSummaries = List[TrainingPlanSummary]


class ListTrainingPlansResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    TrainingPlanSummaries: TrainingPlanSummaries


class ListTransformJobsRequest(ServiceRequest):
    CreationTimeAfter: Optional[Timestamp]
    CreationTimeBefore: Optional[Timestamp]
    LastModifiedTimeAfter: Optional[Timestamp]
    LastModifiedTimeBefore: Optional[Timestamp]
    NameContains: Optional[NameContains]
    StatusEquals: Optional[TransformJobStatus]
    SortBy: Optional[SortBy]
    SortOrder: Optional[SortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class TransformJobSummary(TypedDict, total=False):
    """Provides a summary of a transform job. Multiple ``TransformJobSummary``
    objects are returned as a list after in response to a
    `ListTransformJobs <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTransformJobs.html>`__
    call.
    """

    TransformJobName: TransformJobName
    TransformJobArn: TransformJobArn
    CreationTime: Timestamp
    TransformEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    TransformJobStatus: TransformJobStatus
    FailureReason: Optional[FailureReason]


TransformJobSummaries = List[TransformJobSummary]


class ListTransformJobsResponse(TypedDict, total=False):
    TransformJobSummaries: TransformJobSummaries
    NextToken: Optional[NextToken]


ListTrialComponentKey256 = List[TrialComponentKey256]


class ListTrialComponentsRequest(ServiceRequest):
    ExperimentName: Optional[ExperimentEntityName]
    TrialName: Optional[ExperimentEntityName]
    SourceArn: Optional[String256]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortTrialComponentsBy]
    SortOrder: Optional[SortOrder]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class TrialComponentSummary(TypedDict, total=False):
    """A summary of the properties of a trial component. To get all the
    properties, call the
    `DescribeTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html>`__
    API and provide the ``TrialComponentName``.
    """

    TrialComponentName: Optional[ExperimentEntityName]
    TrialComponentArn: Optional[TrialComponentArn]
    DisplayName: Optional[ExperimentEntityName]
    TrialComponentSource: Optional[TrialComponentSource]
    Status: Optional[TrialComponentStatus]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


TrialComponentSummaries = List[TrialComponentSummary]


class ListTrialComponentsResponse(TypedDict, total=False):
    TrialComponentSummaries: Optional[TrialComponentSummaries]
    NextToken: Optional[NextToken]


class ListTrialsRequest(ServiceRequest):
    ExperimentName: Optional[ExperimentEntityName]
    TrialComponentName: Optional[ExperimentEntityName]
    CreatedAfter: Optional[Timestamp]
    CreatedBefore: Optional[Timestamp]
    SortBy: Optional[SortTrialsBy]
    SortOrder: Optional[SortOrder]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class TrialSummary(TypedDict, total=False):
    """A summary of the properties of a trial. To get the complete set of
    properties, call the
    `DescribeTrial <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrial.html>`__
    API and provide the ``TrialName``.
    """

    TrialArn: Optional[TrialArn]
    TrialName: Optional[ExperimentEntityName]
    DisplayName: Optional[ExperimentEntityName]
    TrialSource: Optional[TrialSource]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]


TrialSummaries = List[TrialSummary]


class ListTrialsResponse(TypedDict, total=False):
    TrialSummaries: Optional[TrialSummaries]
    NextToken: Optional[NextToken]


class ListUserProfilesRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    SortOrder: Optional[SortOrder]
    SortBy: Optional[UserProfileSortKey]
    DomainIdEquals: Optional[DomainId]
    UserProfileNameContains: Optional[UserProfileName]


class UserProfileDetails(TypedDict, total=False):
    """The user profile details."""

    DomainId: Optional[DomainId]
    UserProfileName: Optional[UserProfileName]
    Status: Optional[UserProfileStatus]
    CreationTime: Optional[CreationTime]
    LastModifiedTime: Optional[LastModifiedTime]


UserProfileList = List[UserProfileDetails]


class ListUserProfilesResponse(TypedDict, total=False):
    UserProfiles: Optional[UserProfileList]
    NextToken: Optional[NextToken]


class ListWorkforcesRequest(ServiceRequest):
    SortBy: Optional[ListWorkforcesSortByOptions]
    SortOrder: Optional[SortOrder]
    NameContains: Optional[WorkforceName]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


Workforces = List[Workforce]


class ListWorkforcesResponse(TypedDict, total=False):
    Workforces: Workforces
    NextToken: Optional[NextToken]


class ListWorkteamsRequest(ServiceRequest):
    SortBy: Optional[ListWorkteamsSortByOptions]
    SortOrder: Optional[SortOrder]
    NameContains: Optional[WorkteamName]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


Workteams = List[Workteam]


class ListWorkteamsResponse(TypedDict, total=False):
    Workteams: Workteams
    NextToken: Optional[NextToken]


class Model(TypedDict, total=False):
    """The properties of a model as returned by the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API.
    """

    ModelName: Optional[ModelName]
    PrimaryContainer: Optional[ContainerDefinition]
    Containers: Optional[ContainerDefinitionList]
    InferenceExecutionConfig: Optional[InferenceExecutionConfig]
    ExecutionRoleArn: Optional[RoleArn]
    VpcConfig: Optional[VpcConfig]
    CreationTime: Optional[Timestamp]
    ModelArn: Optional[ModelArn]
    EnableNetworkIsolation: Optional[Boolean]
    Tags: Optional[TagList]
    DeploymentRecommendation: Optional[DeploymentRecommendation]


class ModelCard(TypedDict, total=False):
    """An Amazon SageMaker Model Card."""

    ModelCardArn: Optional[ModelCardArn]
    ModelCardName: Optional[EntityName]
    ModelCardVersion: Optional[Integer]
    Content: Optional[ModelCardContent]
    ModelCardStatus: Optional[ModelCardStatus]
    SecurityConfig: Optional[ModelCardSecurityConfig]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    Tags: Optional[TagList]
    ModelId: Optional[String]
    RiskRating: Optional[String]
    ModelPackageGroupName: Optional[String]


class ModelDashboardEndpoint(TypedDict, total=False):
    """An endpoint that hosts a model displayed in the Amazon SageMaker Model
    Dashboard.
    """

    EndpointName: EndpointName
    EndpointArn: EndpointArn
    CreationTime: Timestamp
    LastModifiedTime: Timestamp
    EndpointStatus: EndpointStatus


ModelDashboardEndpoints = List[ModelDashboardEndpoint]


class ModelDashboardModelCard(TypedDict, total=False):
    """The model card for a model displayed in the Amazon SageMaker Model
    Dashboard.
    """

    ModelCardArn: Optional[ModelCardArn]
    ModelCardName: Optional[EntityName]
    ModelCardVersion: Optional[Integer]
    ModelCardStatus: Optional[ModelCardStatus]
    SecurityConfig: Optional[ModelCardSecurityConfig]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    Tags: Optional[TagList]
    ModelId: Optional[String]
    RiskRating: Optional[String]


class ModelDashboardMonitoringSchedule(TypedDict, total=False):
    """A monitoring schedule for a model displayed in the Amazon SageMaker
    Model Dashboard.
    """

    MonitoringScheduleArn: Optional[MonitoringScheduleArn]
    MonitoringScheduleName: Optional[MonitoringScheduleName]
    MonitoringScheduleStatus: Optional[ScheduleStatus]
    MonitoringType: Optional[MonitoringType]
    FailureReason: Optional[FailureReason]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    MonitoringScheduleConfig: Optional[MonitoringScheduleConfig]
    EndpointName: Optional[EndpointName]
    MonitoringAlertSummaries: Optional[MonitoringAlertSummaryList]
    LastMonitoringExecutionSummary: Optional[MonitoringExecutionSummary]
    BatchTransformInput: Optional[BatchTransformInput]


ModelDashboardMonitoringSchedules = List[ModelDashboardMonitoringSchedule]


class TransformJob(TypedDict, total=False):
    """A batch transform job. For information about SageMaker batch transform,
    see `Use Batch
    Transform <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html>`__.
    """

    TransformJobName: Optional[TransformJobName]
    TransformJobArn: Optional[TransformJobArn]
    TransformJobStatus: Optional[TransformJobStatus]
    FailureReason: Optional[FailureReason]
    ModelName: Optional[ModelName]
    MaxConcurrentTransforms: Optional[MaxConcurrentTransforms]
    ModelClientConfig: Optional[ModelClientConfig]
    MaxPayloadInMB: Optional[MaxPayloadInMB]
    BatchStrategy: Optional[BatchStrategy]
    Environment: Optional[TransformEnvironmentMap]
    TransformInput: Optional[TransformInput]
    TransformOutput: Optional[TransformOutput]
    DataCaptureConfig: Optional[BatchDataCaptureConfig]
    TransformResources: Optional[TransformResources]
    CreationTime: Optional[Timestamp]
    TransformStartTime: Optional[Timestamp]
    TransformEndTime: Optional[Timestamp]
    LabelingJobArn: Optional[LabelingJobArn]
    AutoMLJobArn: Optional[AutoMLJobArn]
    DataProcessing: Optional[DataProcessing]
    ExperimentConfig: Optional[ExperimentConfig]
    Tags: Optional[TagList]


class ModelDashboardModel(TypedDict, total=False):
    """A model displayed in the Amazon SageMaker Model Dashboard."""

    Model: Optional[Model]
    Endpoints: Optional[ModelDashboardEndpoints]
    LastBatchTransformJob: Optional[TransformJob]
    MonitoringSchedules: Optional[ModelDashboardMonitoringSchedules]
    ModelCard: Optional[ModelDashboardModelCard]


class ModelPackage(TypedDict, total=False):
    """A container for your trained model that can be deployed for SageMaker
    inference. This can include inference code, artifacts, and metadata. The
    model package type can be one of the following.

    -  Versioned model: A part of a model package group in Model Registry.

    -  Unversioned model: Not part of a model package group and used in
       Amazon Web Services Marketplace.

    For more information, see
    ```CreateModelPackage`` <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html>`__
    .
    """

    ModelPackageName: Optional[EntityName]
    ModelPackageGroupName: Optional[EntityName]
    ModelPackageVersion: Optional[ModelPackageVersion]
    ModelPackageArn: Optional[ModelPackageArn]
    ModelPackageDescription: Optional[EntityDescription]
    CreationTime: Optional[CreationTime]
    InferenceSpecification: Optional[InferenceSpecification]
    SourceAlgorithmSpecification: Optional[SourceAlgorithmSpecification]
    ValidationSpecification: Optional[ModelPackageValidationSpecification]
    ModelPackageStatus: Optional[ModelPackageStatus]
    ModelPackageStatusDetails: Optional[ModelPackageStatusDetails]
    CertifyForMarketplace: Optional[CertifyForMarketplace]
    ModelApprovalStatus: Optional[ModelApprovalStatus]
    CreatedBy: Optional[UserContext]
    MetadataProperties: Optional[MetadataProperties]
    ModelMetrics: Optional[ModelMetrics]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    ApprovalDescription: Optional[ApprovalDescription]
    Domain: Optional[String]
    Task: Optional[String]
    SamplePayloadUrl: Optional[String]
    AdditionalInferenceSpecifications: Optional[AdditionalInferenceSpecifications]
    SourceUri: Optional[ModelPackageSourceUri]
    SecurityConfig: Optional[ModelPackageSecurityConfig]
    ModelCard: Optional[ModelPackageModelCard]
    ModelLifeCycle: Optional[ModelLifeCycle]
    Tags: Optional[TagList]
    CustomerMetadataProperties: Optional[CustomerMetadataMap]
    DriftCheckBaselines: Optional[DriftCheckBaselines]
    SkipModelValidation: Optional[SkipModelValidation]


class ModelPackageGroup(TypedDict, total=False):
    """A group of versioned models in the Model Registry."""

    ModelPackageGroupName: Optional[EntityName]
    ModelPackageGroupArn: Optional[ModelPackageGroupArn]
    ModelPackageGroupDescription: Optional[EntityDescription]
    CreationTime: Optional[CreationTime]
    CreatedBy: Optional[UserContext]
    ModelPackageGroupStatus: Optional[ModelPackageGroupStatus]
    Tags: Optional[TagList]


ModelVariantActionMap = Dict[ModelVariantName, ModelVariantAction]


class NestedFilters(TypedDict, total=False):
    """A list of nested
    `Filter <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Filter.html>`__
    objects. A resource must satisfy the conditions of all filters to be
    included in the results returned from the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API.

    For example, to filter on a training job's ``InputDataConfig`` property
    with a specific channel name and ``S3Uri`` prefix, define the following
    filters:

    -  ``'{Name:"InputDataConfig.ChannelName", "Operator":"Equals", "Value":"train"}',``

    -  ``'{Name:"InputDataConfig.DataSource.S3DataSource.S3Uri", "Operator":"Contains", "Value":"mybucket/catdata"}'``
    """

    NestedPropertyName: ResourcePropertyName
    Filters: FilterList


NestedFiltersList = List[NestedFilters]


class OnlineStoreConfigUpdate(TypedDict, total=False):
    """Updates the feature group online store configuration."""

    TtlDuration: Optional[TtlDuration]


class Parent(TypedDict, total=False):
    """The trial that a trial component is associated with and the experiment
    the trial is part of. A component might not be associated with a trial.
    A component can be associated with multiple trials.
    """

    TrialName: Optional[ExperimentEntityName]
    ExperimentName: Optional[ExperimentEntityName]


Parents = List[Parent]


class Pipeline(TypedDict, total=False):
    """A SageMaker Model Building Pipeline instance."""

    PipelineArn: Optional[PipelineArn]
    PipelineName: Optional[PipelineName]
    PipelineDisplayName: Optional[PipelineName]
    PipelineDescription: Optional[PipelineDescription]
    RoleArn: Optional[RoleArn]
    PipelineStatus: Optional[PipelineStatus]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    LastRunTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedBy: Optional[UserContext]
    ParallelismConfiguration: Optional[ParallelismConfiguration]
    Tags: Optional[TagList]


class PipelineExecution(TypedDict, total=False):
    """An execution of a pipeline."""

    PipelineArn: Optional[PipelineArn]
    PipelineExecutionArn: Optional[PipelineExecutionArn]
    PipelineExecutionDisplayName: Optional[PipelineExecutionName]
    PipelineExecutionStatus: Optional[PipelineExecutionStatus]
    PipelineExecutionDescription: Optional[PipelineExecutionDescription]
    PipelineExperimentConfig: Optional[PipelineExperimentConfig]
    FailureReason: Optional[PipelineExecutionFailureReason]
    CreationTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedBy: Optional[UserContext]
    ParallelismConfiguration: Optional[ParallelismConfiguration]
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfig]
    PipelineParameters: Optional[ParameterList]


class ProcessingJob(TypedDict, total=False):
    """An Amazon SageMaker processing job that is used to analyze data and
    evaluate models. For more information, see `Process Data and Evaluate
    Models <https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html>`__.
    """

    ProcessingInputs: Optional[ProcessingInputs]
    ProcessingOutputConfig: Optional[ProcessingOutputConfig]
    ProcessingJobName: Optional[ProcessingJobName]
    ProcessingResources: Optional[ProcessingResources]
    StoppingCondition: Optional[ProcessingStoppingCondition]
    AppSpecification: Optional[AppSpecification]
    Environment: Optional[ProcessingEnvironmentMap]
    NetworkConfig: Optional[NetworkConfig]
    RoleArn: Optional[RoleArn]
    ExperimentConfig: Optional[ExperimentConfig]
    ProcessingJobArn: Optional[ProcessingJobArn]
    ProcessingJobStatus: Optional[ProcessingJobStatus]
    ExitMessage: Optional[ExitMessage]
    FailureReason: Optional[FailureReason]
    ProcessingEndTime: Optional[Timestamp]
    ProcessingStartTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    CreationTime: Optional[Timestamp]
    MonitoringScheduleArn: Optional[MonitoringScheduleArn]
    AutoMLJobArn: Optional[AutoMLJobArn]
    TrainingJobArn: Optional[TrainingJobArn]
    Tags: Optional[TagList]


class ProfilerConfigForUpdate(TypedDict, total=False):
    """Configuration information for updating the Amazon SageMaker Debugger
    profile parameters, system and framework metrics configurations, and
    storage paths.
    """

    S3OutputPath: Optional[S3Uri]
    ProfilingIntervalInMilliseconds: Optional[ProfilingIntervalInMilliseconds]
    ProfilingParameters: Optional[ProfilingParameters]
    DisableProfiler: Optional[DisableProfiler]


class Project(TypedDict, total=False):
    """The properties of a project as returned by the Search API."""

    ProjectArn: Optional[ProjectArn]
    ProjectName: Optional[ProjectEntityName]
    ProjectId: Optional[ProjectId]
    ProjectDescription: Optional[EntityDescription]
    ServiceCatalogProvisioningDetails: Optional[ServiceCatalogProvisioningDetails]
    ServiceCatalogProvisionedProductDetails: Optional[ServiceCatalogProvisionedProductDetails]
    ProjectStatus: Optional[ProjectStatus]
    CreatedBy: Optional[UserContext]
    CreationTime: Optional[Timestamp]
    Tags: Optional[TagList]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]


class PutModelPackageGroupPolicyInput(ServiceRequest):
    ModelPackageGroupName: EntityName
    ResourcePolicy: PolicyString


class PutModelPackageGroupPolicyOutput(TypedDict, total=False):
    ModelPackageGroupArn: ModelPackageGroupArn


QueryProperties = Dict[String256, String256]
QueryLineageTypes = List[LineageType]
QueryTypes = List[String40]


class QueryFilters(TypedDict, total=False):
    """A set of filters to narrow the set of lineage entities connected to the
    ``StartArn`` (s) returned by the ``QueryLineage`` API action.
    """

    Types: Optional[QueryTypes]
    LineageTypes: Optional[QueryLineageTypes]
    CreatedBefore: Optional[Timestamp]
    CreatedAfter: Optional[Timestamp]
    ModifiedBefore: Optional[Timestamp]
    ModifiedAfter: Optional[Timestamp]
    Properties: Optional[QueryProperties]


QueryLineageStartArns = List[AssociationEntityArn]


class QueryLineageRequest(ServiceRequest):
    StartArns: Optional[QueryLineageStartArns]
    Direction: Optional[Direction]
    IncludeEdges: Optional[Boolean]
    Filters: Optional[QueryFilters]
    MaxDepth: Optional[QueryLineageMaxDepth]
    MaxResults: Optional[QueryLineageMaxResults]
    NextToken: Optional[String8192]


class Vertex(TypedDict, total=False):
    """A lineage entity connected to the starting entity(ies)."""

    Arn: Optional[AssociationEntityArn]
    Type: Optional[String40]
    LineageType: Optional[LineageType]


Vertices = List[Vertex]


class QueryLineageResponse(TypedDict, total=False):
    Vertices: Optional[Vertices]
    Edges: Optional[Edges]
    NextToken: Optional[String8192]


class RegisterDevicesRequest(ServiceRequest):
    DeviceFleetName: EntityName
    Devices: Devices
    Tags: Optional[TagList]


class RemoteDebugConfigForUpdate(TypedDict, total=False):
    """Configuration for remote debugging for the
    `UpdateTrainingJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateTrainingJob.html>`__
    API. To learn more about the remote debugging functionality of
    SageMaker, see `Access a training container through Amazon Web Services
    Systems Manager (SSM) for remote
    debugging <https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html>`__.
    """

    EnableRemoteDebug: Optional[EnableRemoteDebug]


class RenderableTask(TypedDict, total=False):
    """Contains input values for a task."""

    Input: TaskInput


class RenderUiTemplateRequest(ServiceRequest):
    UiTemplate: Optional[UiTemplate]
    Task: RenderableTask
    RoleArn: RoleArn
    HumanTaskUiArn: Optional[HumanTaskUiArn]


class RenderingError(TypedDict, total=False):
    """A description of an error that occurred while rendering the template."""

    Code: String
    Message: String


RenderingErrorList = List[RenderingError]


class RenderUiTemplateResponse(TypedDict, total=False):
    RenderedContent: String
    Errors: RenderingErrorList


class ReservedCapacityOffering(TypedDict, total=False):
    """Details about a reserved capacity offering for a training plan offering.

    For more information about how to reserve GPU capacity for your
    SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see
    ``CreateTrainingPlan``.
    """

    InstanceType: ReservedCapacityInstanceType
    InstanceCount: ReservedCapacityInstanceCount
    AvailabilityZone: Optional[AvailabilityZone]
    DurationHours: Optional[ReservedCapacityDurationHours]
    DurationMinutes: Optional[ReservedCapacityDurationMinutes]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]


ReservedCapacityOfferings = List[ReservedCapacityOffering]


class ResourceConfigForUpdate(TypedDict, total=False):
    """The ``ResourceConfig`` to update ``KeepAlivePeriodInSeconds``. Other
    fields in the ``ResourceConfig`` cannot be updated.
    """

    KeepAlivePeriodInSeconds: KeepAlivePeriodInSeconds


class RetryPipelineExecutionRequest(ServiceRequest):
    PipelineExecutionArn: PipelineExecutionArn
    ClientRequestToken: IdempotencyToken
    ParallelismConfiguration: Optional[ParallelismConfiguration]


class RetryPipelineExecutionResponse(TypedDict, total=False):
    PipelineExecutionArn: Optional[PipelineExecutionArn]


class SearchExpression(TypedDict, total=False):
    """A multi-expression that searches for the specified resource or resources
    in a search. All resource objects that satisfy the expression's
    condition are included in the search results. You must specify at least
    one subexpression, filter, or nested filter. A ``SearchExpression`` can
    contain up to twenty elements.

    A ``SearchExpression`` contains the following components:

    -  A list of ``Filter`` objects. Each filter defines a simple Boolean
       expression comprised of a resource property name, Boolean operator,
       and value.

    -  A list of ``NestedFilter`` objects. Each nested filter defines a list
       of Boolean expressions using a list of resource properties. A nested
       filter is satisfied if a single object in the list satisfies all
       Boolean expressions.

    -  A list of ``SearchExpression`` objects. A search expression object
       can be nested in a list of search expression objects.

    -  A Boolean operator: ``And`` or ``Or``.
    """

    Filters: Optional["FilterList"]
    NestedFilters: Optional["NestedFiltersList"]
    SubExpressions: Optional["SearchExpressionList"]
    Operator: Optional["BooleanOperator"]


SearchExpressionList = List[SearchExpression]


class TrainingJob(TypedDict, total=False):
    """Contains information about a training job."""

    TrainingJobName: Optional[TrainingJobName]
    TrainingJobArn: Optional[TrainingJobArn]
    TuningJobArn: Optional[HyperParameterTuningJobArn]
    LabelingJobArn: Optional[LabelingJobArn]
    AutoMLJobArn: Optional[AutoMLJobArn]
    ModelArtifacts: Optional[ModelArtifacts]
    TrainingJobStatus: Optional[TrainingJobStatus]
    SecondaryStatus: Optional[SecondaryStatus]
    FailureReason: Optional[FailureReason]
    HyperParameters: Optional[HyperParameters]
    AlgorithmSpecification: Optional[AlgorithmSpecification]
    RoleArn: Optional[RoleArn]
    InputDataConfig: Optional[InputDataConfig]
    OutputDataConfig: Optional[OutputDataConfig]
    ResourceConfig: Optional[ResourceConfig]
    VpcConfig: Optional[VpcConfig]
    StoppingCondition: Optional[StoppingCondition]
    CreationTime: Optional[Timestamp]
    TrainingStartTime: Optional[Timestamp]
    TrainingEndTime: Optional[Timestamp]
    LastModifiedTime: Optional[Timestamp]
    SecondaryStatusTransitions: Optional[SecondaryStatusTransitions]
    FinalMetricDataList: Optional[FinalMetricDataList]
    EnableNetworkIsolation: Optional[Boolean]
    EnableInterContainerTrafficEncryption: Optional[Boolean]
    EnableManagedSpotTraining: Optional[Boolean]
    CheckpointConfig: Optional[CheckpointConfig]
    TrainingTimeInSeconds: Optional[TrainingTimeInSeconds]
    BillableTimeInSeconds: Optional[BillableTimeInSeconds]
    DebugHookConfig: Optional[DebugHookConfig]
    ExperimentConfig: Optional[ExperimentConfig]
    DebugRuleConfigurations: Optional[DebugRuleConfigurations]
    TensorBoardOutputConfig: Optional[TensorBoardOutputConfig]
    DebugRuleEvaluationStatuses: Optional[DebugRuleEvaluationStatuses]
    ProfilerConfig: Optional[ProfilerConfig]
    Environment: Optional[TrainingEnvironmentMap]
    RetryStrategy: Optional[RetryStrategy]
    Tags: Optional[TagList]


class TrialComponentSourceDetail(TypedDict, total=False):
    """Detailed information about the source of a trial component. Either
    ``ProcessingJob`` or ``TrainingJob`` is returned.
    """

    SourceArn: Optional[TrialComponentSourceArn]
    TrainingJob: Optional[TrainingJob]
    ProcessingJob: Optional[ProcessingJob]
    TransformJob: Optional[TransformJob]


class TrialComponent(TypedDict, total=False):
    """The properties of a trial component as returned by the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API.
    """

    TrialComponentName: Optional[ExperimentEntityName]
    DisplayName: Optional[ExperimentEntityName]
    TrialComponentArn: Optional[TrialComponentArn]
    Source: Optional[TrialComponentSource]
    Status: Optional[TrialComponentStatus]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    Parameters: Optional[TrialComponentParameters]
    InputArtifacts: Optional[TrialComponentArtifacts]
    OutputArtifacts: Optional[TrialComponentArtifacts]
    Metrics: Optional[TrialComponentMetricSummaries]
    MetadataProperties: Optional[MetadataProperties]
    SourceDetail: Optional[TrialComponentSourceDetail]
    LineageGroupArn: Optional[LineageGroupArn]
    Tags: Optional[TagList]
    Parents: Optional[Parents]
    RunName: Optional[ExperimentEntityName]


class TrialComponentSimpleSummary(TypedDict, total=False):
    """A short summary of a trial component."""

    TrialComponentName: Optional[ExperimentEntityName]
    TrialComponentArn: Optional[TrialComponentArn]
    TrialComponentSource: Optional[TrialComponentSource]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]


TrialComponentSimpleSummaries = List[TrialComponentSimpleSummary]


class Trial(TypedDict, total=False):
    """The properties of a trial as returned by the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API.
    """

    TrialName: Optional[ExperimentEntityName]
    TrialArn: Optional[TrialArn]
    DisplayName: Optional[ExperimentEntityName]
    ExperimentName: Optional[ExperimentEntityName]
    Source: Optional[TrialSource]
    CreationTime: Optional[Timestamp]
    CreatedBy: Optional[UserContext]
    LastModifiedTime: Optional[Timestamp]
    LastModifiedBy: Optional[UserContext]
    MetadataProperties: Optional[MetadataProperties]
    Tags: Optional[TagList]
    TrialComponentSummaries: Optional[TrialComponentSimpleSummaries]


class SearchRecord(TypedDict, total=False):
    """A single resource returned as part of the
    `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
    API response.
    """

    TrainingJob: Optional[TrainingJob]
    Experiment: Optional[Experiment]
    Trial: Optional[Trial]
    TrialComponent: Optional[TrialComponent]
    Endpoint: Optional[Endpoint]
    ModelPackage: Optional[ModelPackage]
    ModelPackageGroup: Optional[ModelPackageGroup]
    Pipeline: Optional[Pipeline]
    PipelineExecution: Optional[PipelineExecution]
    FeatureGroup: Optional[FeatureGroup]
    FeatureMetadata: Optional[FeatureMetadata]
    Project: Optional[Project]
    HyperParameterTuningJob: Optional[HyperParameterTuningJobSearchEntity]
    ModelCard: Optional[ModelCard]
    Model: Optional[ModelDashboardModel]


class VisibilityConditions(TypedDict, total=False):
    """The list of key-value pairs used to filter your search results. If a
    search result contains a key from your list, it is included in the final
    search response if the value associated with the key in the result
    matches the value you specified. If the value doesn't match, the result
    is excluded from the search response. Any resources that don't have a
    key from the list that you've provided will also be included in the
    search response.
    """

    Key: Optional[VisibilityConditionsKey]
    Value: Optional[VisibilityConditionsValue]


VisibilityConditionsList = List[VisibilityConditions]


class SearchRequest(ServiceRequest):
    Resource: ResourceType
    SearchExpression: Optional[SearchExpression]
    SortBy: Optional[ResourcePropertyName]
    SortOrder: Optional[SearchSortOrder]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CrossAccountFilterOption: Optional[CrossAccountFilterOption]
    VisibilityConditions: Optional[VisibilityConditionsList]


class TotalHits(TypedDict, total=False):
    """Represents the total number of matching results and indicates how
    accurate that count is.

    The ``Value`` field provides the count, which may be exact or estimated.
    The ``Relation`` field indicates whether it's an exact figure or a lower
    bound. This helps understand the full scope of search results,
    especially when dealing with large result sets.
    """

    Value: Optional[Long]
    Relation: Optional[Relation]


SearchResultsList = List[SearchRecord]


class SearchResponse(TypedDict, total=False):
    Results: Optional[SearchResultsList]
    NextToken: Optional[NextToken]
    TotalHits: Optional[TotalHits]


TrainingPlanDurationHoursInput = int


class SearchTrainingPlanOfferingsRequest(ServiceRequest):
    InstanceType: Optional[ReservedCapacityInstanceType]
    InstanceCount: Optional[ReservedCapacityInstanceCount]
    StartTimeAfter: Optional[Timestamp]
    EndTimeBefore: Optional[Timestamp]
    DurationHours: TrainingPlanDurationHoursInput
    TargetResources: SageMakerResourceNames


class TrainingPlanOffering(TypedDict, total=False):
    """Details about a training plan offering.

    For more information about how to reserve GPU capacity for your
    SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see
    ``CreateTrainingPlan``.
    """

    TrainingPlanOfferingId: TrainingPlanOfferingId
    TargetResources: SageMakerResourceNames
    RequestedStartTimeAfter: Optional[Timestamp]
    RequestedEndTimeBefore: Optional[Timestamp]
    DurationHours: Optional[TrainingPlanDurationHours]
    DurationMinutes: Optional[TrainingPlanDurationMinutes]
    UpfrontFee: Optional[String256]
    CurrencyCode: Optional[CurrencyCode]
    ReservedCapacityOfferings: Optional[ReservedCapacityOfferings]


TrainingPlanOfferings = List[TrainingPlanOffering]


class SearchTrainingPlanOfferingsResponse(TypedDict, total=False):
    TrainingPlanOfferings: TrainingPlanOfferings


class SendPipelineExecutionStepFailureRequest(ServiceRequest):
    CallbackToken: CallbackToken
    FailureReason: Optional[String256]
    ClientRequestToken: Optional[IdempotencyToken]


class SendPipelineExecutionStepFailureResponse(TypedDict, total=False):
    PipelineExecutionArn: Optional[PipelineExecutionArn]


class SendPipelineExecutionStepSuccessRequest(ServiceRequest):
    CallbackToken: CallbackToken
    OutputParameters: Optional[OutputParameterList]
    ClientRequestToken: Optional[IdempotencyToken]


class SendPipelineExecutionStepSuccessResponse(TypedDict, total=False):
    PipelineExecutionArn: Optional[PipelineExecutionArn]


class ServiceCatalogProvisioningUpdateDetails(TypedDict, total=False):
    """Details that you specify to provision a service catalog product. For
    information about service catalog, see `What is Amazon Web Services
    Service
    Catalog <https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html>`__.
    """

    ProvisioningArtifactId: Optional[ServiceCatalogEntityId]
    ProvisioningParameters: Optional[ProvisioningParameters]


class StartEdgeDeploymentStageRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName
    StageName: EntityName


class StartInferenceExperimentRequest(ServiceRequest):
    Name: InferenceExperimentName


class StartInferenceExperimentResponse(TypedDict, total=False):
    InferenceExperimentArn: InferenceExperimentArn


class StartMlflowTrackingServerRequest(ServiceRequest):
    TrackingServerName: TrackingServerName


class StartMlflowTrackingServerResponse(TypedDict, total=False):
    TrackingServerArn: Optional[TrackingServerArn]


class StartMonitoringScheduleRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName


class StartNotebookInstanceInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName


class StartPipelineExecutionRequest(ServiceRequest):
    PipelineName: PipelineNameOrArn
    PipelineExecutionDisplayName: Optional[PipelineExecutionName]
    PipelineParameters: Optional[ParameterList]
    PipelineExecutionDescription: Optional[PipelineExecutionDescription]
    ClientRequestToken: IdempotencyToken
    ParallelismConfiguration: Optional[ParallelismConfiguration]
    SelectiveExecutionConfig: Optional[SelectiveExecutionConfig]


class StartPipelineExecutionResponse(TypedDict, total=False):
    PipelineExecutionArn: Optional[PipelineExecutionArn]


class StopAutoMLJobRequest(ServiceRequest):
    AutoMLJobName: AutoMLJobName


class StopCompilationJobRequest(ServiceRequest):
    CompilationJobName: EntityName


class StopEdgeDeploymentStageRequest(ServiceRequest):
    EdgeDeploymentPlanName: EntityName
    StageName: EntityName


class StopEdgePackagingJobRequest(ServiceRequest):
    EdgePackagingJobName: EntityName


class StopHyperParameterTuningJobRequest(ServiceRequest):
    HyperParameterTuningJobName: HyperParameterTuningJobName


class StopInferenceExperimentRequest(ServiceRequest):
    Name: InferenceExperimentName
    ModelVariantActions: ModelVariantActionMap
    DesiredModelVariants: Optional[ModelVariantConfigList]
    DesiredState: Optional[InferenceExperimentStopDesiredState]
    Reason: Optional[InferenceExperimentStatusReason]


class StopInferenceExperimentResponse(TypedDict, total=False):
    InferenceExperimentArn: InferenceExperimentArn


class StopInferenceRecommendationsJobRequest(ServiceRequest):
    JobName: RecommendationJobName


class StopLabelingJobRequest(ServiceRequest):
    LabelingJobName: LabelingJobName


class StopMlflowTrackingServerRequest(ServiceRequest):
    TrackingServerName: TrackingServerName


class StopMlflowTrackingServerResponse(TypedDict, total=False):
    TrackingServerArn: Optional[TrackingServerArn]


class StopMonitoringScheduleRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName


class StopNotebookInstanceInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName


class StopOptimizationJobRequest(ServiceRequest):
    OptimizationJobName: EntityName


class StopPipelineExecutionRequest(ServiceRequest):
    PipelineExecutionArn: PipelineExecutionArn
    ClientRequestToken: IdempotencyToken


class StopPipelineExecutionResponse(TypedDict, total=False):
    PipelineExecutionArn: Optional[PipelineExecutionArn]


class StopProcessingJobRequest(ServiceRequest):
    ProcessingJobName: ProcessingJobName


class StopTrainingJobRequest(ServiceRequest):
    TrainingJobName: TrainingJobName


class StopTransformJobRequest(ServiceRequest):
    TransformJobName: TransformJobName


class ThroughputConfigUpdate(TypedDict, total=False):
    """The new throughput configuration for the feature group. You can switch
    between on-demand and provisioned modes or update the read / write
    capacity of provisioned feature groups. You can switch a feature group
    to on-demand only once in a 24 hour period.
    """

    ThroughputMode: Optional[ThroughputMode]
    ProvisionedReadCapacityUnits: Optional[CapacityUnit]
    ProvisionedWriteCapacityUnits: Optional[CapacityUnit]


class UpdateActionRequest(ServiceRequest):
    ActionName: ExperimentEntityName
    Description: Optional[ExperimentDescription]
    Status: Optional[ActionStatus]
    Properties: Optional[LineageEntityParameters]
    PropertiesToRemove: Optional[ListLineageEntityParameterKey]


class UpdateActionResponse(TypedDict, total=False):
    ActionArn: Optional[ActionArn]


class UpdateAppImageConfigRequest(ServiceRequest):
    AppImageConfigName: AppImageConfigName
    KernelGatewayImageConfig: Optional[KernelGatewayImageConfig]
    JupyterLabAppImageConfig: Optional[JupyterLabAppImageConfig]
    CodeEditorAppImageConfig: Optional[CodeEditorAppImageConfig]


class UpdateAppImageConfigResponse(TypedDict, total=False):
    AppImageConfigArn: Optional[AppImageConfigArn]


class UpdateArtifactRequest(ServiceRequest):
    ArtifactArn: ArtifactArn
    ArtifactName: Optional[ExperimentEntityName]
    Properties: Optional[ArtifactProperties]
    PropertiesToRemove: Optional[ListLineageEntityParameterKey]


class UpdateArtifactResponse(TypedDict, total=False):
    ArtifactArn: Optional[ArtifactArn]


class UpdateClusterRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn
    InstanceGroups: ClusterInstanceGroupSpecifications
    NodeRecovery: Optional[ClusterNodeRecovery]
    InstanceGroupsToDelete: Optional[ClusterInstanceGroupsToDelete]


class UpdateClusterResponse(TypedDict, total=False):
    ClusterArn: ClusterArn


class UpdateClusterSchedulerConfigRequest(ServiceRequest):
    ClusterSchedulerConfigId: ClusterSchedulerConfigId
    TargetVersion: Integer
    SchedulerConfig: Optional[SchedulerConfig]
    Description: Optional[EntityDescription]


class UpdateClusterSchedulerConfigResponse(TypedDict, total=False):
    ClusterSchedulerConfigArn: ClusterSchedulerConfigArn
    ClusterSchedulerConfigVersion: Integer


class UpdateClusterSoftwareInstanceGroupSpecification(TypedDict, total=False):
    """The configuration that describes specifications of the instance groups
    to update.
    """

    InstanceGroupName: ClusterInstanceGroupName


UpdateClusterSoftwareInstanceGroups = List[UpdateClusterSoftwareInstanceGroupSpecification]


class UpdateClusterSoftwareRequest(ServiceRequest):
    ClusterName: ClusterNameOrArn
    InstanceGroups: Optional[UpdateClusterSoftwareInstanceGroups]
    DeploymentConfig: Optional[DeploymentConfiguration]


class UpdateClusterSoftwareResponse(TypedDict, total=False):
    ClusterArn: ClusterArn


class UpdateCodeRepositoryInput(ServiceRequest):
    CodeRepositoryName: EntityName
    GitConfig: Optional[GitConfigForUpdate]


class UpdateCodeRepositoryOutput(TypedDict, total=False):
    CodeRepositoryArn: CodeRepositoryArn


class UpdateComputeQuotaRequest(ServiceRequest):
    ComputeQuotaId: ComputeQuotaId
    TargetVersion: Integer
    ComputeQuotaConfig: Optional[ComputeQuotaConfig]
    ComputeQuotaTarget: Optional[ComputeQuotaTarget]
    ActivationState: Optional[ActivationState]
    Description: Optional[EntityDescription]


class UpdateComputeQuotaResponse(TypedDict, total=False):
    ComputeQuotaArn: ComputeQuotaArn
    ComputeQuotaVersion: Integer


class UpdateContextRequest(ServiceRequest):
    ContextName: ContextName
    Description: Optional[ExperimentDescription]
    Properties: Optional[LineageEntityParameters]
    PropertiesToRemove: Optional[ListLineageEntityParameterKey]


class UpdateContextResponse(TypedDict, total=False):
    ContextArn: Optional[ContextArn]


class UpdateDeviceFleetRequest(ServiceRequest):
    DeviceFleetName: EntityName
    RoleArn: Optional[RoleArn]
    Description: Optional[DeviceFleetDescription]
    OutputConfig: EdgeOutputConfig
    EnableIotRoleAlias: Optional[EnableIotRoleAlias]


class UpdateDevicesRequest(ServiceRequest):
    DeviceFleetName: EntityName
    Devices: Devices


class UpdateDomainRequest(ServiceRequest):
    DomainId: DomainId
    DefaultUserSettings: Optional[UserSettings]
    DomainSettingsForUpdate: Optional[DomainSettingsForUpdate]
    AppSecurityGroupManagement: Optional[AppSecurityGroupManagement]
    DefaultSpaceSettings: Optional[DefaultSpaceSettings]
    SubnetIds: Optional[Subnets]
    AppNetworkAccessType: Optional[AppNetworkAccessType]
    TagPropagation: Optional[TagPropagation]


class UpdateDomainResponse(TypedDict, total=False):
    DomainArn: Optional[DomainArn]


class VariantProperty(TypedDict, total=False):
    """Specifies a production variant property type for an Endpoint.

    If you are updating an endpoint with the ``RetainAllVariantProperties``
    option of
    `UpdateEndpointInput <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html>`__
    set to ``true``, the ``VariantProperty`` objects listed in the
    ``ExcludeRetainedVariantProperties`` parameter of
    `UpdateEndpointInput <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html>`__
    override the existing variant properties of the endpoint.
    """

    VariantPropertyType: VariantPropertyType


VariantPropertyList = List[VariantProperty]


class UpdateEndpointInput(ServiceRequest):
    EndpointName: EndpointName
    EndpointConfigName: EndpointConfigName
    RetainAllVariantProperties: Optional[Boolean]
    ExcludeRetainedVariantProperties: Optional[VariantPropertyList]
    DeploymentConfig: Optional[DeploymentConfig]
    RetainDeploymentConfig: Optional[Boolean]


class UpdateEndpointOutput(TypedDict, total=False):
    EndpointArn: EndpointArn


class UpdateEndpointWeightsAndCapacitiesInput(ServiceRequest):
    EndpointName: EndpointName
    DesiredWeightsAndCapacities: DesiredWeightAndCapacityList


class UpdateEndpointWeightsAndCapacitiesOutput(TypedDict, total=False):
    EndpointArn: EndpointArn


class UpdateExperimentRequest(ServiceRequest):
    ExperimentName: ExperimentEntityName
    DisplayName: Optional[ExperimentEntityName]
    Description: Optional[ExperimentDescription]


class UpdateExperimentResponse(TypedDict, total=False):
    ExperimentArn: Optional[ExperimentArn]


class UpdateFeatureGroupRequest(ServiceRequest):
    FeatureGroupName: FeatureGroupNameOrArn
    FeatureAdditions: Optional[FeatureAdditions]
    OnlineStoreConfig: Optional[OnlineStoreConfigUpdate]
    ThroughputConfig: Optional[ThroughputConfigUpdate]


class UpdateFeatureGroupResponse(TypedDict, total=False):
    FeatureGroupArn: FeatureGroupArn


class UpdateFeatureMetadataRequest(ServiceRequest):
    FeatureGroupName: FeatureGroupNameOrArn
    FeatureName: FeatureName
    Description: Optional[FeatureDescription]
    ParameterAdditions: Optional[FeatureParameterAdditions]
    ParameterRemovals: Optional[FeatureParameterRemovals]


class UpdateHubContentReferenceRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentName: HubContentName
    HubContentType: HubContentType
    MinVersion: Optional[HubContentVersion]


class UpdateHubContentReferenceResponse(TypedDict, total=False):
    HubArn: HubArn
    HubContentArn: HubContentArn


class UpdateHubContentRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubContentName: HubContentName
    HubContentType: HubContentType
    HubContentVersion: HubContentVersion
    HubContentDisplayName: Optional[HubContentDisplayName]
    HubContentDescription: Optional[HubContentDescription]
    HubContentMarkdown: Optional[HubContentMarkdown]
    HubContentSearchKeywords: Optional[HubContentSearchKeywordList]
    SupportStatus: Optional[HubContentSupportStatus]


class UpdateHubContentResponse(TypedDict, total=False):
    HubArn: HubArn
    HubContentArn: HubContentArn


class UpdateHubRequest(ServiceRequest):
    HubName: HubNameOrArn
    HubDescription: Optional[HubDescription]
    HubDisplayName: Optional[HubDisplayName]
    HubSearchKeywords: Optional[HubSearchKeywordList]


class UpdateHubResponse(TypedDict, total=False):
    HubArn: HubArn


class UpdateImageRequest(ServiceRequest):
    DeleteProperties: Optional[ImageDeletePropertyList]
    Description: Optional[ImageDescription]
    DisplayName: Optional[ImageDisplayName]
    ImageName: ImageName
    RoleArn: Optional[RoleArn]


class UpdateImageResponse(TypedDict, total=False):
    ImageArn: Optional[ImageArn]


class UpdateImageVersionRequest(ServiceRequest):
    ImageName: ImageName
    Alias: Optional[SageMakerImageVersionAlias]
    Version: Optional[ImageVersionNumber]
    AliasesToAdd: Optional[SageMakerImageVersionAliases]
    AliasesToDelete: Optional[SageMakerImageVersionAliases]
    VendorGuidance: Optional[VendorGuidance]
    JobType: Optional[JobType]
    MLFramework: Optional[MLFramework]
    ProgrammingLang: Optional[ProgrammingLang]
    Processor: Optional[Processor]
    Horovod: Optional[Horovod]
    ReleaseNotes: Optional[ReleaseNotes]


class UpdateImageVersionResponse(TypedDict, total=False):
    ImageVersionArn: Optional[ImageVersionArn]


class UpdateInferenceComponentInput(ServiceRequest):
    InferenceComponentName: InferenceComponentName
    Specification: Optional[InferenceComponentSpecification]
    RuntimeConfig: Optional[InferenceComponentRuntimeConfig]
    DeploymentConfig: Optional[InferenceComponentDeploymentConfig]


class UpdateInferenceComponentOutput(TypedDict, total=False):
    InferenceComponentArn: InferenceComponentArn


class UpdateInferenceComponentRuntimeConfigInput(ServiceRequest):
    InferenceComponentName: InferenceComponentName
    DesiredRuntimeConfig: InferenceComponentRuntimeConfig


class UpdateInferenceComponentRuntimeConfigOutput(TypedDict, total=False):
    InferenceComponentArn: InferenceComponentArn


class UpdateInferenceExperimentRequest(ServiceRequest):
    Name: InferenceExperimentName
    Schedule: Optional[InferenceExperimentSchedule]
    Description: Optional[InferenceExperimentDescription]
    ModelVariants: Optional[ModelVariantConfigList]
    DataStorageConfig: Optional[InferenceExperimentDataStorageConfig]
    ShadowModeConfig: Optional[ShadowModeConfig]


class UpdateInferenceExperimentResponse(TypedDict, total=False):
    InferenceExperimentArn: InferenceExperimentArn


class UpdateMlflowTrackingServerRequest(ServiceRequest):
    TrackingServerName: TrackingServerName
    ArtifactStoreUri: Optional[S3Uri]
    TrackingServerSize: Optional[TrackingServerSize]
    AutomaticModelRegistration: Optional[Boolean]
    WeeklyMaintenanceWindowStart: Optional[WeeklyMaintenanceWindowStart]


class UpdateMlflowTrackingServerResponse(TypedDict, total=False):
    TrackingServerArn: Optional[TrackingServerArn]


class UpdateModelCardRequest(ServiceRequest):
    ModelCardName: ModelCardNameOrArn
    Content: Optional[ModelCardContent]
    ModelCardStatus: Optional[ModelCardStatus]


class UpdateModelCardResponse(TypedDict, total=False):
    ModelCardArn: ModelCardArn


class UpdateModelPackageInput(ServiceRequest):
    ModelPackageArn: ModelPackageArn
    ModelApprovalStatus: Optional[ModelApprovalStatus]
    ApprovalDescription: Optional[ApprovalDescription]
    CustomerMetadataProperties: Optional[CustomerMetadataMap]
    CustomerMetadataPropertiesToRemove: Optional[CustomerMetadataKeyList]
    AdditionalInferenceSpecificationsToAdd: Optional[AdditionalInferenceSpecifications]
    InferenceSpecification: Optional[InferenceSpecification]
    SourceUri: Optional[ModelPackageSourceUri]
    ModelCard: Optional[ModelPackageModelCard]
    ModelLifeCycle: Optional[ModelLifeCycle]
    ClientToken: Optional[ClientToken]


class UpdateModelPackageOutput(TypedDict, total=False):
    ModelPackageArn: ModelPackageArn


class UpdateMonitoringAlertRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName
    MonitoringAlertName: MonitoringAlertName
    DatapointsToAlert: MonitoringDatapointsToAlert
    EvaluationPeriod: MonitoringEvaluationPeriod


class UpdateMonitoringAlertResponse(TypedDict, total=False):
    MonitoringScheduleArn: MonitoringScheduleArn
    MonitoringAlertName: Optional[MonitoringAlertName]


class UpdateMonitoringScheduleRequest(ServiceRequest):
    MonitoringScheduleName: MonitoringScheduleName
    MonitoringScheduleConfig: MonitoringScheduleConfig


class UpdateMonitoringScheduleResponse(TypedDict, total=False):
    MonitoringScheduleArn: MonitoringScheduleArn


class UpdateNotebookInstanceInput(ServiceRequest):
    NotebookInstanceName: NotebookInstanceName
    InstanceType: Optional[InstanceType]
    RoleArn: Optional[RoleArn]
    LifecycleConfigName: Optional[NotebookInstanceLifecycleConfigName]
    DisassociateLifecycleConfig: Optional[DisassociateNotebookInstanceLifecycleConfig]
    VolumeSizeInGB: Optional[NotebookInstanceVolumeSizeInGB]
    DefaultCodeRepository: Optional[CodeRepositoryNameOrUrl]
    AdditionalCodeRepositories: Optional[AdditionalCodeRepositoryNamesOrUrls]
    AcceleratorTypes: Optional[NotebookInstanceAcceleratorTypes]
    DisassociateAcceleratorTypes: Optional[DisassociateNotebookInstanceAcceleratorTypes]
    DisassociateDefaultCodeRepository: Optional[DisassociateDefaultCodeRepository]
    DisassociateAdditionalCodeRepositories: Optional[DisassociateAdditionalCodeRepositories]
    RootAccess: Optional[RootAccess]
    InstanceMetadataServiceConfiguration: Optional[InstanceMetadataServiceConfiguration]


class UpdateNotebookInstanceLifecycleConfigInput(ServiceRequest):
    NotebookInstanceLifecycleConfigName: NotebookInstanceLifecycleConfigName
    OnCreate: Optional[NotebookInstanceLifecycleConfigList]
    OnStart: Optional[NotebookInstanceLifecycleConfigList]


class UpdateNotebookInstanceLifecycleConfigOutput(TypedDict, total=False):
    pass


class UpdateNotebookInstanceOutput(TypedDict, total=False):
    pass


class UpdatePartnerAppRequest(ServiceRequest):
    Arn: PartnerAppArn
    MaintenanceConfig: Optional[PartnerAppMaintenanceConfig]
    Tier: Optional[NonEmptyString64]
    ApplicationConfig: Optional[PartnerAppConfig]
    EnableIamSessionBasedIdentity: Optional[Boolean]
    ClientToken: Optional[ClientToken]
    Tags: Optional[TagList]


class UpdatePartnerAppResponse(TypedDict, total=False):
    Arn: Optional[PartnerAppArn]


class UpdatePipelineExecutionRequest(ServiceRequest):
    PipelineExecutionArn: PipelineExecutionArn
    PipelineExecutionDescription: Optional[PipelineExecutionDescription]
    PipelineExecutionDisplayName: Optional[PipelineExecutionName]
    ParallelismConfiguration: Optional[ParallelismConfiguration]


class UpdatePipelineExecutionResponse(TypedDict, total=False):
    PipelineExecutionArn: Optional[PipelineExecutionArn]


class UpdatePipelineRequest(ServiceRequest):
    PipelineName: PipelineName
    PipelineDisplayName: Optional[PipelineName]
    PipelineDefinition: Optional[PipelineDefinition]
    PipelineDefinitionS3Location: Optional[PipelineDefinitionS3Location]
    PipelineDescription: Optional[PipelineDescription]
    RoleArn: Optional[RoleArn]
    ParallelismConfiguration: Optional[ParallelismConfiguration]


class UpdatePipelineResponse(TypedDict, total=False):
    PipelineArn: Optional[PipelineArn]


class UpdateProjectInput(ServiceRequest):
    ProjectName: ProjectEntityName
    ProjectDescription: Optional[EntityDescription]
    ServiceCatalogProvisioningUpdateDetails: Optional[ServiceCatalogProvisioningUpdateDetails]
    Tags: Optional[TagList]


class UpdateProjectOutput(TypedDict, total=False):
    ProjectArn: ProjectArn


class UpdateSpaceRequest(ServiceRequest):
    DomainId: DomainId
    SpaceName: SpaceName
    SpaceSettings: Optional[SpaceSettings]
    SpaceDisplayName: Optional[NonEmptyString64]


class UpdateSpaceResponse(TypedDict, total=False):
    SpaceArn: Optional[SpaceArn]


class UpdateTrainingJobRequest(ServiceRequest):
    TrainingJobName: TrainingJobName
    ProfilerConfig: Optional[ProfilerConfigForUpdate]
    ProfilerRuleConfigurations: Optional[ProfilerRuleConfigurations]
    ResourceConfig: Optional[ResourceConfigForUpdate]
    RemoteDebugConfig: Optional[RemoteDebugConfigForUpdate]


class UpdateTrainingJobResponse(TypedDict, total=False):
    TrainingJobArn: TrainingJobArn


class UpdateTrialComponentRequest(ServiceRequest):
    TrialComponentName: ExperimentEntityName
    DisplayName: Optional[ExperimentEntityName]
    Status: Optional[TrialComponentStatus]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]
    Parameters: Optional[TrialComponentParameters]
    ParametersToRemove: Optional[ListTrialComponentKey256]
    InputArtifacts: Optional[TrialComponentArtifacts]
    InputArtifactsToRemove: Optional[ListTrialComponentKey256]
    OutputArtifacts: Optional[TrialComponentArtifacts]
    OutputArtifactsToRemove: Optional[ListTrialComponentKey256]


class UpdateTrialComponentResponse(TypedDict, total=False):
    TrialComponentArn: Optional[TrialComponentArn]


class UpdateTrialRequest(ServiceRequest):
    TrialName: ExperimentEntityName
    DisplayName: Optional[ExperimentEntityName]


class UpdateTrialResponse(TypedDict, total=False):
    TrialArn: Optional[TrialArn]


class UpdateUserProfileRequest(ServiceRequest):
    DomainId: DomainId
    UserProfileName: UserProfileName
    UserSettings: Optional[UserSettings]


class UpdateUserProfileResponse(TypedDict, total=False):
    UserProfileArn: Optional[UserProfileArn]


class UpdateWorkforceRequest(ServiceRequest):
    WorkforceName: WorkforceName
    SourceIpConfig: Optional[SourceIpConfig]
    OidcConfig: Optional[OidcConfig]
    WorkforceVpcConfig: Optional[WorkforceVpcConfigRequest]


class UpdateWorkforceResponse(TypedDict, total=False):
    Workforce: Workforce


class UpdateWorkteamRequest(ServiceRequest):
    WorkteamName: WorkteamName
    MemberDefinitions: Optional[MemberDefinitions]
    Description: Optional[String200]
    NotificationConfiguration: Optional[NotificationConfiguration]
    WorkerAccessConfiguration: Optional[WorkerAccessConfiguration]


class UpdateWorkteamResponse(TypedDict, total=False):
    Workteam: Workteam


class SagemakerApi:
    service = "sagemaker"
    version = "2017-07-24"

    @handler("AddAssociation")
    def add_association(
        self,
        context: RequestContext,
        source_arn: AssociationEntityArn,
        destination_arn: AssociationEntityArn,
        association_type: AssociationEdgeType | None = None,
        **kwargs,
    ) -> AddAssociationResponse:
        """Creates an *association* between the source and the destination. A
        source can be associated with multiple destinations, and a destination
        can be associated with multiple sources. An association is a lineage
        tracking entity. For more information, see `Amazon SageMaker ML Lineage
        Tracking <https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html>`__.

        :param source_arn: The ARN of the source.
        :param destination_arn: The Amazon Resource Name (ARN) of the destination.
        :param association_type: The type of association.
        :returns: AddAssociationResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("AddTags")
    def add_tags(
        self, context: RequestContext, resource_arn: ResourceArn, tags: TagList, **kwargs
    ) -> AddTagsOutput:
        """Adds or overwrites one or more tags for the specified SageMaker
        resource. You can add tags to notebook instances, training jobs,
        hyperparameter tuning jobs, batch transform jobs, models, labeling jobs,
        work teams, endpoint configurations, and endpoints.

        Each tag consists of a key and an optional value. Tag keys must be
        unique per resource. For more information about tags, see For more
        information, see `Amazon Web Services Tagging
        Strategies <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__.

        Tags that you add to a hyperparameter tuning job by calling this API are
        also added to any training jobs that the hyperparameter tuning job
        launches after you call this API, but not to training jobs that the
        hyperparameter tuning job launched before you called this API. To make
        sure that the tags associated with a hyperparameter tuning job are also
        added to all training jobs that the hyperparameter tuning job launches,
        add the tags when you first create the tuning job by specifying them in
        the ``Tags`` parameter of
        `CreateHyperParameterTuningJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html>`__

        Tags that you add to a SageMaker Domain or User Profile by calling this
        API are also added to any Apps that the Domain or User Profile launches
        after you call this API, but not to Apps that the Domain or User Profile
        launched before you called this API. To make sure that the tags
        associated with a Domain or User Profile are also added to all Apps that
        the Domain or User Profile launches, add the tags when you first create
        the Domain or User Profile by specifying them in the ``Tags`` parameter
        of
        `CreateDomain <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDomain.html>`__
        or
        `CreateUserProfile <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateUserProfile.html>`__.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to tag.
        :param tags: An array of key-value pairs.
        :returns: AddTagsOutput
        """
        raise NotImplementedError

    @handler("AssociateTrialComponent")
    def associate_trial_component(
        self,
        context: RequestContext,
        trial_component_name: ExperimentEntityName,
        trial_name: ExperimentEntityName,
        **kwargs,
    ) -> AssociateTrialComponentResponse:
        """Associates a trial component with a trial. A trial component can be
        associated with multiple trials. To disassociate a trial component from
        a trial, call the
        `DisassociateTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DisassociateTrialComponent.html>`__
        API.

        :param trial_component_name: The name of the component to associated with the trial.
        :param trial_name: The name of the trial to associate with.
        :returns: AssociateTrialComponentResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("BatchDeleteClusterNodes")
    def batch_delete_cluster_nodes(
        self,
        context: RequestContext,
        cluster_name: ClusterNameOrArn,
        node_ids: ClusterNodeIds,
        **kwargs,
    ) -> BatchDeleteClusterNodesResponse:
        """Deletes specific nodes within a SageMaker HyperPod cluster.
        ``BatchDeleteClusterNodes`` accepts a cluster name and a list of node
        IDs.

        -  To safeguard your work, back up your data to Amazon S3 or an FSx for
           Lustre file system before invoking the API on a worker node group.
           This will help prevent any potential data loss from the instance root
           volume. For more information about backup, see `Use the backup script
           provided by SageMaker
           HyperPod <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-cli-command.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software-backup>`__.

        -  If you want to invoke this API on an existing cluster, you'll first
           need to patch the cluster by running the `UpdateClusterSoftware
           API <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html>`__.
           For more information about patching a cluster, see `Update the
           SageMaker HyperPod platform software of a
           cluster <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-cli-command.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software>`__.

        :param cluster_name: The name of the SageMaker HyperPod cluster from which to delete the
        specified nodes.
        :param node_ids: A list of node IDs to be deleted from the specified cluster.
        :returns: BatchDeleteClusterNodesResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("BatchDescribeModelPackage")
    def batch_describe_model_package(
        self, context: RequestContext, model_package_arn_list: ModelPackageArnList, **kwargs
    ) -> BatchDescribeModelPackageOutput:
        """This action batch describes a list of versioned model packages

        :param model_package_arn_list: The list of Amazon Resource Name (ARN) of the model package groups.
        :returns: BatchDescribeModelPackageOutput
        """
        raise NotImplementedError

    @handler("CreateAction")
    def create_action(
        self,
        context: RequestContext,
        action_name: ExperimentEntityName,
        source: ActionSource,
        action_type: String256,
        description: ExperimentDescription | None = None,
        status: ActionStatus | None = None,
        properties: LineageEntityParameters | None = None,
        metadata_properties: MetadataProperties | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateActionResponse:
        """Creates an *action*. An action is a lineage tracking entity that
        represents an action or activity. For example, a model deployment or an
        HPO job. Generally, an action involves at least one input or output
        artifact. For more information, see `Amazon SageMaker ML Lineage
        Tracking <https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html>`__.

        :param action_name: The name of the action.
        :param source: The source type, ID, and URI.
        :param action_type: The action type.
        :param description: The description of the action.
        :param status: The status of the action.
        :param properties: A list of properties to add to the action.
        :param metadata_properties: Metadata properties of the tracking entity, trial, or trial component.
        :param tags: A list of tags to apply to the action.
        :returns: CreateActionResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateAlgorithm")
    def create_algorithm(
        self,
        context: RequestContext,
        algorithm_name: EntityName,
        training_specification: TrainingSpecification,
        algorithm_description: EntityDescription | None = None,
        inference_specification: InferenceSpecification | None = None,
        validation_specification: AlgorithmValidationSpecification | None = None,
        certify_for_marketplace: CertifyForMarketplace | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateAlgorithmOutput:
        """Create a machine learning algorithm that you can use in SageMaker and
        list in the Amazon Web Services Marketplace.

        :param algorithm_name: The name of the algorithm.
        :param training_specification: Specifies details about training jobs run by this algorithm, including
        the following:

        -  The Amazon ECR path of the container and the version digest of the
           algorithm.
        :param algorithm_description: A description of the algorithm.
        :param inference_specification: Specifies details about inference jobs that the algorithm runs,
        including the following:

        -  The Amazon ECR paths of containers that contain the inference code
           and model artifacts.
        :param validation_specification: Specifies configurations for one or more training jobs and that
        SageMaker runs to test the algorithm's training code and, optionally,
        one or more batch transform jobs that SageMaker runs to test the
        algorithm's inference code.
        :param certify_for_marketplace: Whether to certify the algorithm so that it can be listed in Amazon Web
        Services Marketplace.
        :param tags: An array of key-value pairs.
        :returns: CreateAlgorithmOutput
        """
        raise NotImplementedError

    @handler("CreateApp")
    def create_app(
        self,
        context: RequestContext,
        domain_id: DomainId,
        app_type: AppType,
        app_name: AppName,
        user_profile_name: UserProfileName | None = None,
        space_name: SpaceName | None = None,
        tags: TagList | None = None,
        resource_spec: ResourceSpec | None = None,
        recovery_mode: Boolean | None = None,
        **kwargs,
    ) -> CreateAppResponse:
        """Creates a running app for the specified UserProfile. This operation is
        automatically invoked by Amazon SageMaker AI upon access to the
        associated Domain, and when new kernel configurations are selected by
        the user. A user may have multiple Apps active simultaneously.

        :param domain_id: The domain ID.
        :param app_type: The type of app.
        :param app_name: The name of the app.
        :param user_profile_name: The user profile name.
        :param space_name: The name of the space.
        :param tags: Each tag consists of a key and an optional value.
        :param resource_spec: The instance type and the Amazon Resource Name (ARN) of the SageMaker AI
        image created on the instance.
        :param recovery_mode: Indicates whether the application is launched in recovery mode.
        :returns: CreateAppResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateAppImageConfig")
    def create_app_image_config(
        self,
        context: RequestContext,
        app_image_config_name: AppImageConfigName,
        tags: TagList | None = None,
        kernel_gateway_image_config: KernelGatewayImageConfig | None = None,
        jupyter_lab_app_image_config: JupyterLabAppImageConfig | None = None,
        code_editor_app_image_config: CodeEditorAppImageConfig | None = None,
        **kwargs,
    ) -> CreateAppImageConfigResponse:
        """Creates a configuration for running a SageMaker AI image as a
        KernelGateway app. The configuration specifies the Amazon Elastic File
        System storage volume on the image, and a list of the kernels in the
        image.

        :param app_image_config_name: The name of the AppImageConfig.
        :param tags: A list of tags to apply to the AppImageConfig.
        :param kernel_gateway_image_config: The KernelGatewayImageConfig.
        :param jupyter_lab_app_image_config: The ``JupyterLabAppImageConfig``.
        :param code_editor_app_image_config: The ``CodeEditorAppImageConfig``.
        :returns: CreateAppImageConfigResponse
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("CreateArtifact")
    def create_artifact(
        self,
        context: RequestContext,
        source: ArtifactSource,
        artifact_type: String256,
        artifact_name: ExperimentEntityName | None = None,
        properties: ArtifactProperties | None = None,
        metadata_properties: MetadataProperties | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateArtifactResponse:
        """Creates an *artifact*. An artifact is a lineage tracking entity that
        represents a URI addressable object or data. Some examples are the S3
        URI of a dataset and the ECR registry path of an image. For more
        information, see `Amazon SageMaker ML Lineage
        Tracking <https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html>`__.

        :param source: The ID, ID type, and URI of the source.
        :param artifact_type: The artifact type.
        :param artifact_name: The name of the artifact.
        :param properties: A list of properties to add to the artifact.
        :param metadata_properties: Metadata properties of the tracking entity, trial, or trial component.
        :param tags: A list of tags to apply to the artifact.
        :returns: CreateArtifactResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateAutoMLJob")
    def create_auto_ml_job(
        self,
        context: RequestContext,
        auto_ml_job_name: AutoMLJobName,
        input_data_config: AutoMLInputDataConfig,
        output_data_config: AutoMLOutputDataConfig,
        role_arn: RoleArn,
        problem_type: ProblemType | None = None,
        auto_ml_job_objective: AutoMLJobObjective | None = None,
        auto_ml_job_config: AutoMLJobConfig | None = None,
        generate_candidate_definitions_only: GenerateCandidateDefinitionsOnly | None = None,
        tags: TagList | None = None,
        model_deploy_config: ModelDeployConfig | None = None,
        **kwargs,
    ) -> CreateAutoMLJobResponse:
        """Creates an Autopilot job also referred to as Autopilot experiment or
        AutoML job.

        An AutoML job in SageMaker AI is a fully automated process that allows
        you to build machine learning models with minimal effort and machine
        learning expertise. When initiating an AutoML job, you provide your data
        and optionally specify parameters tailored to your use case. SageMaker
        AI then automates the entire model development lifecycle, including data
        preprocessing, model training, tuning, and evaluation. AutoML jobs are
        designed to simplify and accelerate the model building process by
        automating various tasks and exploring different combinations of machine
        learning algorithms, data preprocessing techniques, and hyperparameter
        values. The output of an AutoML job comprises one or more trained models
        ready for deployment and inference. Additionally, SageMaker AI AutoML
        jobs generate a candidate model leaderboard, allowing you to select the
        best-performing model for deployment.

        For more information about AutoML jobs, see
        https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html
        in the SageMaker AI developer guide.

        We recommend using the new versions
        `CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html>`__
        and
        `DescribeAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html>`__,
        which offer backward compatibility.

        ``CreateAutoMLJobV2`` can manage tabular problem types identical to
        those of its previous version ``CreateAutoMLJob``, as well as
        time-series forecasting, non-tabular problem types such as image or text
        classification, and text generation (LLMs fine-tuning).

        Find guidelines about how to migrate a ``CreateAutoMLJob`` to
        ``CreateAutoMLJobV2`` in `Migrate a CreateAutoMLJob to
        CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2>`__.

        You can find the best-performing model after you run an AutoML job by
        calling
        `DescribeAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html>`__
        (recommended) or
        `DescribeAutoMLJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html>`__.

        :param auto_ml_job_name: Identifies an Autopilot job.
        :param input_data_config: An array of channel objects that describes the input data and its
        location.
        :param output_data_config: Provides information about encryption and the Amazon S3 output path
        needed to store artifacts from an AutoML job.
        :param role_arn: The ARN of the role that is used to access the data.
        :param problem_type: Defines the type of supervised learning problem available for the
        candidates.
        :param auto_ml_job_objective: Specifies a metric to minimize or maximize as the objective of a job.
        :param auto_ml_job_config: A collection of settings used to configure an AutoML job.
        :param generate_candidate_definitions_only: Generates possible candidates without training the models.
        :param tags: An array of key-value pairs.
        :param model_deploy_config: Specifies how to generate the endpoint name for an automatic one-click
        Autopilot model deployment.
        :returns: CreateAutoMLJobResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateAutoMLJobV2")
    def create_auto_ml_job_v2(
        self,
        context: RequestContext,
        auto_ml_job_name: AutoMLJobName,
        auto_ml_job_input_data_config: AutoMLJobInputDataConfig,
        output_data_config: AutoMLOutputDataConfig,
        auto_ml_problem_type_config: AutoMLProblemTypeConfig,
        role_arn: RoleArn,
        tags: TagList | None = None,
        security_config: AutoMLSecurityConfig | None = None,
        auto_ml_job_objective: AutoMLJobObjective | None = None,
        model_deploy_config: ModelDeployConfig | None = None,
        data_split_config: AutoMLDataSplitConfig | None = None,
        auto_ml_compute_config: AutoMLComputeConfig | None = None,
        **kwargs,
    ) -> CreateAutoMLJobV2Response:
        """Creates an Autopilot job also referred to as Autopilot experiment or
        AutoML job V2.

        An AutoML job in SageMaker AI is a fully automated process that allows
        you to build machine learning models with minimal effort and machine
        learning expertise. When initiating an AutoML job, you provide your data
        and optionally specify parameters tailored to your use case. SageMaker
        AI then automates the entire model development lifecycle, including data
        preprocessing, model training, tuning, and evaluation. AutoML jobs are
        designed to simplify and accelerate the model building process by
        automating various tasks and exploring different combinations of machine
        learning algorithms, data preprocessing techniques, and hyperparameter
        values. The output of an AutoML job comprises one or more trained models
        ready for deployment and inference. Additionally, SageMaker AI AutoML
        jobs generate a candidate model leaderboard, allowing you to select the
        best-performing model for deployment.

        For more information about AutoML jobs, see
        https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html
        in the SageMaker AI developer guide.

        AutoML jobs V2 support various problem types such as regression, binary,
        and multiclass classification with tabular data, text and image
        classification, time-series forecasting, and fine-tuning of large
        language models (LLMs) for text generation.

        `CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html>`__
        and
        `DescribeAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html>`__
        are new versions of
        `CreateAutoMLJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html>`__
        and
        `DescribeAutoMLJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html>`__
        which offer backward compatibility.

        ``CreateAutoMLJobV2`` can manage tabular problem types identical to
        those of its previous version ``CreateAutoMLJob``, as well as
        time-series forecasting, non-tabular problem types such as image or text
        classification, and text generation (LLMs fine-tuning).

        Find guidelines about how to migrate a ``CreateAutoMLJob`` to
        ``CreateAutoMLJobV2`` in `Migrate a CreateAutoMLJob to
        CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2>`__.

        For the list of available problem types supported by
        ``CreateAutoMLJobV2``, see
        `AutoMLProblemTypeConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html>`__.

        You can find the best-performing model after you run an AutoML job V2 by
        calling
        `DescribeAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html>`__.

        :param auto_ml_job_name: Identifies an Autopilot job.
        :param auto_ml_job_input_data_config: An array of channel objects describing the input data and their
        location.
        :param output_data_config: Provides information about encryption and the Amazon S3 output path
        needed to store artifacts from an AutoML job.
        :param auto_ml_problem_type_config: Defines the configuration settings of one of the supported problem
        types.
        :param role_arn: The ARN of the role that is used to access the data.
        :param tags: An array of key-value pairs.
        :param security_config: The security configuration for traffic encryption or Amazon VPC
        settings.
        :param auto_ml_job_objective: Specifies a metric to minimize or maximize as the objective of a job.
        :param model_deploy_config: Specifies how to generate the endpoint name for an automatic one-click
        Autopilot model deployment.
        :param data_split_config: This structure specifies how to split the data into train and validation
        datasets.
        :param auto_ml_compute_config: Specifies the compute configuration for the AutoML job V2.
        :returns: CreateAutoMLJobV2Response
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateCluster")
    def create_cluster(
        self,
        context: RequestContext,
        cluster_name: ClusterName,
        instance_groups: ClusterInstanceGroupSpecifications,
        vpc_config: VpcConfig | None = None,
        tags: TagList | None = None,
        orchestrator: ClusterOrchestrator | None = None,
        node_recovery: ClusterNodeRecovery | None = None,
        **kwargs,
    ) -> CreateClusterResponse:
        """Creates a SageMaker HyperPod cluster. SageMaker HyperPod is a capability
        of SageMaker for creating and managing persistent clusters for
        developing large machine learning models, such as large language models
        (LLMs) and diffusion models. To learn more, see `Amazon SageMaker
        HyperPod <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html>`__
        in the *Amazon SageMaker Developer Guide*.

        :param cluster_name: The name for the new SageMaker HyperPod cluster.
        :param instance_groups: The instance groups to be created in the SageMaker HyperPod cluster.
        :param vpc_config: Specifies the Amazon Virtual Private Cloud (VPC) that is associated with
        the Amazon SageMaker HyperPod cluster.
        :param tags: Custom tags for managing the SageMaker HyperPod cluster as an Amazon Web
        Services resource.
        :param orchestrator: The type of orchestrator to use for the SageMaker HyperPod cluster.
        :param node_recovery: The node recovery mode for the SageMaker HyperPod cluster.
        :returns: CreateClusterResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateClusterSchedulerConfig")
    def create_cluster_scheduler_config(
        self,
        context: RequestContext,
        name: EntityName,
        cluster_arn: ClusterArn,
        scheduler_config: SchedulerConfig,
        description: EntityDescription | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateClusterSchedulerConfigResponse:
        """Create cluster policy configuration. This policy is used for task
        prioritization and fair-share allocation of idle compute. This helps
        prioritize critical workloads and distributes idle compute across
        entities.

        :param name: Name for the cluster policy.
        :param cluster_arn: ARN of the cluster.
        :param scheduler_config: Configuration about the monitoring schedule.
        :param description: Description of the cluster policy.
        :param tags: Tags of the cluster policy.
        :returns: CreateClusterSchedulerConfigResponse
        :raises ConflictException:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateCodeRepository")
    def create_code_repository(
        self,
        context: RequestContext,
        code_repository_name: EntityName,
        git_config: GitConfig,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateCodeRepositoryOutput:
        """Creates a Git repository as a resource in your SageMaker AI account. You
        can associate the repository with notebook instances so that you can use
        Git source control for the notebooks you create. The Git repository is a
        resource in your SageMaker AI account, so it can be associated with more
        than one notebook instance, and it persists independently from the
        lifecycle of any notebook instances it is associated with.

        The repository can be hosted either in `Amazon Web Services
        CodeCommit <https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html>`__
        or in any other Git repository.

        :param code_repository_name: The name of the Git repository.
        :param git_config: Specifies details about the repository, including the URL where the
        repository is located, the default branch, and credentials to use to
        access the repository.
        :param tags: An array of key-value pairs.
        :returns: CreateCodeRepositoryOutput
        """
        raise NotImplementedError

    @handler("CreateCompilationJob")
    def create_compilation_job(
        self,
        context: RequestContext,
        compilation_job_name: EntityName,
        role_arn: RoleArn,
        output_config: OutputConfig,
        stopping_condition: StoppingCondition,
        model_package_version_arn: ModelPackageArn | None = None,
        input_config: InputConfig | None = None,
        vpc_config: NeoVpcConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateCompilationJobResponse:
        """Starts a model compilation job. After the model has been compiled,
        Amazon SageMaker AI saves the resulting model artifacts to an Amazon
        Simple Storage Service (Amazon S3) bucket that you specify.

        If you choose to host your model using Amazon SageMaker AI hosting
        services, you can use the resulting model artifacts as part of the
        model. You can also use the artifacts with Amazon Web Services IoT
        Greengrass. In that case, deploy them as an ML resource.

        In the request body, you provide the following:

        -  A name for the compilation job

        -  Information about the input model artifacts

        -  The output location for the compiled model and the device (target)
           that the model runs on

        -  The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker
           AI assumes to perform the model compilation job.

        You can also provide a ``Tag`` to track the model compilation job's
        resource use and costs. The response body contains the
        ``CompilationJobArn`` for the compiled job.

        To stop a model compilation job, use
        `StopCompilationJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopCompilationJob.html>`__.
        To get information about a particular model compilation job, use
        `DescribeCompilationJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html>`__.
        To get information about multiple model compilation jobs, use
        `ListCompilationJobs <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html>`__.

        :param compilation_job_name: A name for the model compilation job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that enables Amazon
        SageMaker AI to perform tasks on your behalf.
        :param output_config: Provides information about the output location for the compiled model
        and the target device the model runs on.
        :param stopping_condition: Specifies a limit to how long a model compilation job can run.
        :param model_package_version_arn: The Amazon Resource Name (ARN) of a versioned model package.
        :param input_config: Provides information about the location of input model artifacts, the
        name and shape of the expected data inputs, and the framework in which
        the model was trained.
        :param vpc_config: A
        `VpcConfig <https://docs.
        :param tags: An array of key-value pairs.
        :returns: CreateCompilationJobResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateComputeQuota")
    def create_compute_quota(
        self,
        context: RequestContext,
        name: EntityName,
        cluster_arn: ClusterArn,
        compute_quota_config: ComputeQuotaConfig,
        compute_quota_target: ComputeQuotaTarget,
        description: EntityDescription | None = None,
        activation_state: ActivationState | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateComputeQuotaResponse:
        """Create compute allocation definition. This defines how compute is
        allocated, shared, and borrowed for specified entities. Specifically,
        how to lend and borrow idle compute and assign a fair-share weight to
        the specified entities.

        :param name: Name to the compute allocation definition.
        :param cluster_arn: ARN of the cluster.
        :param compute_quota_config: Configuration of the compute allocation definition.
        :param compute_quota_target: The target entity to allocate compute resources to.
        :param description: Description of the compute allocation definition.
        :param activation_state: The state of the compute allocation being described.
        :param tags: Tags of the compute allocation definition.
        :returns: CreateComputeQuotaResponse
        :raises ConflictException:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateContext")
    def create_context(
        self,
        context: RequestContext,
        context_name: ContextName,
        source: ContextSource,
        context_type: String256,
        description: ExperimentDescription | None = None,
        properties: LineageEntityParameters | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateContextResponse:
        """Creates a *context*. A context is a lineage tracking entity that
        represents a logical grouping of other tracking or experiment entities.
        Some examples are an endpoint and a model package. For more information,
        see `Amazon SageMaker ML Lineage
        Tracking <https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html>`__.

        :param context_name: The name of the context.
        :param source: The source type, ID, and URI.
        :param context_type: The context type.
        :param description: The description of the context.
        :param properties: A list of properties to add to the context.
        :param tags: A list of tags to apply to the context.
        :returns: CreateContextResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateDataQualityJobDefinition")
    def create_data_quality_job_definition(
        self,
        context: RequestContext,
        job_definition_name: MonitoringJobDefinitionName,
        data_quality_app_specification: DataQualityAppSpecification,
        data_quality_job_input: DataQualityJobInput,
        data_quality_job_output_config: MonitoringOutputConfig,
        job_resources: MonitoringResources,
        role_arn: RoleArn,
        data_quality_baseline_config: DataQualityBaselineConfig | None = None,
        network_config: MonitoringNetworkConfig | None = None,
        stopping_condition: MonitoringStoppingCondition | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateDataQualityJobDefinitionResponse:
        """Creates a definition for a job that monitors data quality and drift. For
        information about model monitor, see `Amazon SageMaker AI Model
        Monitor <https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html>`__.

        :param job_definition_name: The name for the monitoring job definition.
        :param data_quality_app_specification: Specifies the container that runs the monitoring job.
        :param data_quality_job_input: A list of inputs for the monitoring job.
        :param data_quality_job_output_config: The output configuration for monitoring jobs.
        :param job_resources: Identifies the resources to deploy for a monitoring job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI
        can assume to perform tasks on your behalf.
        :param data_quality_baseline_config: Configures the constraints and baselines for the monitoring job.
        :param network_config: Specifies networking configuration for the monitoring job.
        :param stopping_condition: A time limit for how long the monitoring job is allowed to run before
        stopping.
        :param tags: (Optional) An array of key-value pairs.
        :returns: CreateDataQualityJobDefinitionResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateDeviceFleet")
    def create_device_fleet(
        self,
        context: RequestContext,
        device_fleet_name: EntityName,
        output_config: EdgeOutputConfig,
        role_arn: RoleArn | None = None,
        description: DeviceFleetDescription | None = None,
        tags: TagList | None = None,
        enable_iot_role_alias: EnableIotRoleAlias | None = None,
        **kwargs,
    ) -> None:
        """Creates a device fleet.

        :param device_fleet_name: The name of the fleet that the device belongs to.
        :param output_config: The output configuration for storing sample data collected by the fleet.
        :param role_arn: The Amazon Resource Name (ARN) that has access to Amazon Web Services
        Internet of Things (IoT).
        :param description: A description of the fleet.
        :param tags: Creates tags for the specified fleet.
        :param enable_iot_role_alias: Whether to create an Amazon Web Services IoT Role Alias during device
        fleet creation.
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateDomain")
    def create_domain(
        self,
        context: RequestContext,
        domain_name: DomainName,
        auth_mode: AuthMode,
        default_user_settings: UserSettings,
        subnet_ids: Subnets,
        vpc_id: VpcId,
        domain_settings: DomainSettings | None = None,
        tags: TagList | None = None,
        app_network_access_type: AppNetworkAccessType | None = None,
        home_efs_file_system_kms_key_id: KmsKeyId | None = None,
        kms_key_id: KmsKeyId | None = None,
        app_security_group_management: AppSecurityGroupManagement | None = None,
        tag_propagation: TagPropagation | None = None,
        default_space_settings: DefaultSpaceSettings | None = None,
        **kwargs,
    ) -> CreateDomainResponse:
        """Creates a ``Domain``. A domain consists of an associated Amazon Elastic
        File System volume, a list of authorized users, and a variety of
        security, application, policy, and Amazon Virtual Private Cloud (VPC)
        configurations. Users within a domain can share notebook files and other
        artifacts with each other.

        **EFS storage**

        When a domain is created, an EFS volume is created for use by all of the
        users within the domain. Each user receives a private home directory
        within the EFS volume for notebooks, Git repositories, and data files.

        SageMaker AI uses the Amazon Web Services Key Management Service (Amazon
        Web Services KMS) to encrypt the EFS volume attached to the domain with
        an Amazon Web Services managed key by default. For more control, you can
        specify a customer managed key. For more information, see `Protect Data
        at Rest Using
        Encryption <https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html>`__.

        **VPC configuration**

        All traffic between the domain and the Amazon EFS volume is through the
        specified VPC and subnets. For other traffic, you can specify the
        ``AppNetworkAccessType`` parameter. ``AppNetworkAccessType`` corresponds
        to the network access type that you choose when you onboard to the
        domain. The following options are available:

        -  ``PublicInternetOnly`` - Non-EFS traffic goes through a VPC managed
           by Amazon SageMaker AI, which allows internet access. This is the
           default value.

        -  ``VpcOnly`` - All traffic is through the specified VPC and subnets.
           Internet access is disabled by default. To allow internet access, you
           must specify a NAT gateway.

           When internet access is disabled, you won't be able to run a Amazon
           SageMaker AI Studio notebook or to train or host models unless your
           VPC has an interface endpoint to the SageMaker AI API and runtime or
           a NAT gateway and your security groups allow outbound connections.

        NFS traffic over TCP on port 2049 needs to be allowed in both inbound
        and outbound rules in order to launch a Amazon SageMaker AI Studio app
        successfully.

        For more information, see `Connect Amazon SageMaker AI Studio Notebooks
        to Resources in a
        VPC <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html>`__.

        :param domain_name: A name for the domain.
        :param auth_mode: The mode of authentication that members use to access the domain.
        :param default_user_settings: The default settings to use to create a user profile when
        ``UserSettings`` isn't specified in the call to the
        ``CreateUserProfile`` API.
        :param subnet_ids: The VPC subnets that the domain uses for communication.
        :param vpc_id: The ID of the Amazon Virtual Private Cloud (VPC) that the domain uses
        for communication.
        :param domain_settings: A collection of ``Domain`` settings.
        :param tags: Tags to associated with the Domain.
        :param app_network_access_type: Specifies the VPC used for non-EFS traffic.
        :param home_efs_file_system_kms_key_id: Use ``KmsKeyId``.
        :param kms_key_id: SageMaker AI uses Amazon Web Services KMS to encrypt EFS and EBS volumes
        attached to the domain with an Amazon Web Services managed key by
        default.
        :param app_security_group_management: The entity that creates and manages the required security groups for
        inter-app communication in ``VPCOnly`` mode.
        :param tag_propagation: Indicates whether custom tag propagation is supported for the domain.
        :param default_space_settings: The default settings for shared spaces that users create in the domain.
        :returns: CreateDomainResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateEdgeDeploymentPlan")
    def create_edge_deployment_plan(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        model_configs: EdgeDeploymentModelConfigs,
        device_fleet_name: EntityName,
        stages: DeploymentStages | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateEdgeDeploymentPlanResponse:
        """Creates an edge deployment plan, consisting of multiple stages. Each
        stage may have a different deployment configuration and devices.

        :param edge_deployment_plan_name: The name of the edge deployment plan.
        :param model_configs: List of models associated with the edge deployment plan.
        :param device_fleet_name: The device fleet used for this edge deployment plan.
        :param stages: List of stages of the edge deployment plan.
        :param tags: List of tags with which to tag the edge deployment plan.
        :returns: CreateEdgeDeploymentPlanResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateEdgeDeploymentStage")
    def create_edge_deployment_stage(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        stages: DeploymentStages,
        **kwargs,
    ) -> None:
        """Creates a new stage in an existing edge deployment plan.

        :param edge_deployment_plan_name: The name of the edge deployment plan.
        :param stages: List of stages to be added to the edge deployment plan.
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateEdgePackagingJob")
    def create_edge_packaging_job(
        self,
        context: RequestContext,
        edge_packaging_job_name: EntityName,
        compilation_job_name: EntityName,
        model_name: EntityName,
        model_version: EdgeVersion,
        role_arn: RoleArn,
        output_config: EdgeOutputConfig,
        resource_key: KmsKeyId | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> None:
        """Starts a SageMaker Edge Manager model packaging job. Edge Manager will
        use the model artifacts from the Amazon Simple Storage Service bucket
        that you specify. After the model has been packaged, Amazon SageMaker
        saves the resulting artifacts to an S3 bucket that you specify.

        :param edge_packaging_job_name: The name of the edge packaging job.
        :param compilation_job_name: The name of the SageMaker Neo compilation job that will be used to
        locate model artifacts for packaging.
        :param model_name: The name of the model.
        :param model_version: The version of the model.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that enables Amazon
        SageMaker to download and upload the model, and to contact SageMaker
        Neo.
        :param output_config: Provides information about the output location for the packaged model.
        :param resource_key: The Amazon Web Services KMS key to use when encrypting the EBS volume
        the edge packaging job runs on.
        :param tags: Creates tags for the packaging job.
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateEndpoint")
    def create_endpoint(
        self,
        context: RequestContext,
        endpoint_name: EndpointName,
        endpoint_config_name: EndpointConfigName,
        deployment_config: DeploymentConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateEndpointOutput:
        """Creates an endpoint using the endpoint configuration specified in the
        request. SageMaker uses the endpoint to provision resources and deploy
        models. You create the endpoint configuration with the
        `CreateEndpointConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html>`__
        API.

        Use this API to deploy models using SageMaker hosting services.

        You must not delete an ``EndpointConfig`` that is in use by an endpoint
        that is live or while the ``UpdateEndpoint`` or ``CreateEndpoint``
        operations are being performed on the endpoint. To update an endpoint,
        you must create a new ``EndpointConfig``.

        The endpoint name must be unique within an Amazon Web Services Region in
        your Amazon Web Services account.

        When it receives the request, SageMaker creates the endpoint, launches
        the resources (ML compute instances), and deploys the model(s) on them.

        When you call
        `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__,
        a load call is made to DynamoDB to verify that your endpoint
        configuration exists. When you read data from a DynamoDB table
        supporting
        ```Eventually Consistent Reads`` <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html>`__
        , the response might not reflect the results of a recently completed
        write operation. The response might include some stale data. If the
        dependent entities are not yet in DynamoDB, this causes a validation
        error. If you repeat your read request after a short time, the response
        should return the latest data. So retry logic is recommended to handle
        these possible issues. We also recommend that customers call
        `DescribeEndpointConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html>`__
        before calling
        `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__
        to minimize the potential impact of a DynamoDB eventually consistent
        read.

        When SageMaker receives the request, it sets the endpoint status to
        ``Creating``. After it creates the endpoint, it sets the status to
        ``InService``. SageMaker can then process incoming requests for
        inferences. To check the status of an endpoint, use the
        `DescribeEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html>`__
        API.

        If any of the models hosted at this endpoint get model data from an
        Amazon S3 location, SageMaker uses Amazon Web Services Security Token
        Service to download model artifacts from the S3 path you provided.
        Amazon Web Services STS is activated in your Amazon Web Services account
        by default. If you previously deactivated Amazon Web Services STS for a
        region, you need to reactivate Amazon Web Services STS for that region.
        For more information, see `Activating and Deactivating Amazon Web
        Services STS in an Amazon Web Services
        Region <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__
        in the *Amazon Web Services Identity and Access Management User Guide*.

        To add the IAM role policies for using this API operation, go to the
        `IAM console <https://console.aws.amazon.com/iam/>`__, and choose Roles
        in the left navigation pane. Search the IAM role that you want to grant
        access to use the
        `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__
        and
        `CreateEndpointConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html>`__
        API operations, add the following policies to the role.

        -  Option 1: For a full SageMaker access, search and attach the
           ``AmazonSageMakerFullAccess`` policy.

        -  Option 2: For granting a limited access to an IAM role, paste the
           following Action elements manually into the JSON file of the IAM
           role:

           ``"Action": ["sagemaker:CreateEndpoint", "sagemaker:CreateEndpointConfig"]``

           ``"Resource": [``

           ``"arn:aws:sagemaker:region:account-id:endpoint/endpointName"``

           ``"arn:aws:sagemaker:region:account-id:endpoint-config/endpointConfigName"``

           ``]``

           For more information, see `SageMaker API Permissions: Actions,
           Permissions, and Resources
           Reference <https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html>`__.

        :param endpoint_name: The name of the endpoint.
        :param endpoint_config_name: The name of an endpoint configuration.
        :param deployment_config: The deployment configuration for an endpoint, which contains the desired
        deployment strategy and rollback configurations.
        :param tags: An array of key-value pairs.
        :returns: CreateEndpointOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateEndpointConfig")
    def create_endpoint_config(
        self,
        context: RequestContext,
        endpoint_config_name: EndpointConfigName,
        production_variants: ProductionVariantList,
        data_capture_config: DataCaptureConfig | None = None,
        tags: TagList | None = None,
        kms_key_id: KmsKeyId | None = None,
        async_inference_config: AsyncInferenceConfig | None = None,
        explainer_config: ExplainerConfig | None = None,
        shadow_production_variants: ProductionVariantList | None = None,
        execution_role_arn: RoleArn | None = None,
        vpc_config: VpcConfig | None = None,
        enable_network_isolation: Boolean | None = None,
        **kwargs,
    ) -> CreateEndpointConfigOutput:
        """Creates an endpoint configuration that SageMaker hosting services uses
        to deploy models. In the configuration, you identify one or more models,
        created using the ``CreateModel`` API, to deploy and the resources that
        you want SageMaker to provision. Then you call the
        `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__
        API.

        Use this API if you want to use SageMaker hosting services to deploy
        models into production.

        In the request, you define a ``ProductionVariant``, for each model that
        you want to deploy. Each ``ProductionVariant`` parameter also describes
        the resources that you want SageMaker to provision. This includes the
        number and type of ML compute instances to deploy.

        If you are hosting multiple models, you also assign a ``VariantWeight``
        to specify how much traffic you want to allocate to each model. For
        example, suppose that you want to host two models, A and B, and you
        assign traffic weight 2 for model A and 1 for model B. SageMaker
        distributes two-thirds of the traffic to Model A, and one-third to model
        B.

        When you call
        `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__,
        a load call is made to DynamoDB to verify that your endpoint
        configuration exists. When you read data from a DynamoDB table
        supporting
        ```Eventually Consistent Reads`` <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html>`__
        , the response might not reflect the results of a recently completed
        write operation. The response might include some stale data. If the
        dependent entities are not yet in DynamoDB, this causes a validation
        error. If you repeat your read request after a short time, the response
        should return the latest data. So retry logic is recommended to handle
        these possible issues. We also recommend that customers call
        `DescribeEndpointConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html>`__
        before calling
        `CreateEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html>`__
        to minimize the potential impact of a DynamoDB eventually consistent
        read.

        :param endpoint_config_name: The name of the endpoint configuration.
        :param production_variants: An array of ``ProductionVariant`` objects, one for each model that you
        want to host at this endpoint.
        :param data_capture_config: Configuration to control how SageMaker AI captures inference data.
        :param tags: An array of key-value pairs.
        :param kms_key_id: The Amazon Resource Name (ARN) of a Amazon Web Services Key Management
        Service key that SageMaker uses to encrypt data on the storage volume
        attached to the ML compute instance that hosts the endpoint.
        :param async_inference_config: Specifies configuration for how an endpoint performs asynchronous
        inference.
        :param explainer_config: A member of ``CreateEndpointConfig`` that enables explainers.
        :param shadow_production_variants: An array of ``ProductionVariant`` objects, one for each model that you
        want to host at this endpoint in shadow mode with production traffic
        replicated from the model specified on ``ProductionVariants``.
        :param execution_role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI
        can assume to perform actions on your behalf.
        :param vpc_config: Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker
        jobs, hosted models, and compute resources have access to.
        :param enable_network_isolation: Sets whether all model containers deployed to the endpoint are isolated.
        :returns: CreateEndpointConfigOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateExperiment")
    def create_experiment(
        self,
        context: RequestContext,
        experiment_name: ExperimentEntityName,
        display_name: ExperimentEntityName | None = None,
        description: ExperimentDescription | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateExperimentResponse:
        """Creates a SageMaker *experiment*. An experiment is a collection of
        *trials* that are observed, compared and evaluated as a group. A trial
        is a set of steps, called *trial components*, that produce a machine
        learning model.

        In the Studio UI, trials are referred to as *run groups* and trial
        components are referred to as *runs*.

        The goal of an experiment is to determine the components that produce
        the best model. Multiple trials are performed, each one isolating and
        measuring the impact of a change to one or more inputs, while keeping
        the remaining inputs constant.

        When you use SageMaker Studio or the SageMaker Python SDK, all
        experiments, trials, and trial components are automatically tracked,
        logged, and indexed. When you use the Amazon Web Services SDK for Python
        (Boto), you must use the logging APIs provided by the SDK.

        You can add tags to experiments, trials, trial components and then use
        the
        `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
        API to search for the tags.

        To add a description to an experiment, specify the optional
        ``Description`` parameter. To add a description later, or to change the
        description, call the
        `UpdateExperiment <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateExperiment.html>`__
        API.

        To get a list of all your experiments, call the
        `ListExperiments <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListExperiments.html>`__
        API. To view an experiment's properties, call the
        `DescribeExperiment <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeExperiment.html>`__
        API. To get a list of all the trials associated with an experiment, call
        the
        `ListTrials <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html>`__
        API. To create a trial call the
        `CreateTrial <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrial.html>`__
        API.

        :param experiment_name: The name of the experiment.
        :param display_name: The name of the experiment as displayed.
        :param description: The description of the experiment.
        :param tags: A list of tags to associate with the experiment.
        :returns: CreateExperimentResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateFeatureGroup")
    def create_feature_group(
        self,
        context: RequestContext,
        feature_group_name: FeatureGroupName,
        record_identifier_feature_name: FeatureName,
        event_time_feature_name: FeatureName,
        feature_definitions: FeatureDefinitions,
        online_store_config: OnlineStoreConfig | None = None,
        offline_store_config: OfflineStoreConfig | None = None,
        throughput_config: ThroughputConfig | None = None,
        role_arn: RoleArn | None = None,
        description: Description | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateFeatureGroupResponse:
        """Create a new ``FeatureGroup``. A ``FeatureGroup`` is a group of
        ``Features`` defined in the ``FeatureStore`` to describe a ``Record``.

        The ``FeatureGroup`` defines the schema and features contained in the
        ``FeatureGroup``. A ``FeatureGroup`` definition is composed of a list of
        ``Features``, a ``RecordIdentifierFeatureName``, an
        ``EventTimeFeatureName`` and configurations for its ``OnlineStore`` and
        ``OfflineStore``. Check `Amazon Web Services service
        quotas <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html>`__
        to see the ``FeatureGroup`` s quota for your Amazon Web Services
        account.

        Note that it can take approximately 10-15 minutes to provision an
        ``OnlineStore`` ``FeatureGroup`` with the ``InMemory`` ``StorageType``.

        You must include at least one of ``OnlineStoreConfig`` and
        ``OfflineStoreConfig`` to create a ``FeatureGroup``.

        :param feature_group_name: The name of the ``FeatureGroup``.
        :param record_identifier_feature_name: The name of the ``Feature`` whose value uniquely identifies a ``Record``
        defined in the ``FeatureStore``.
        :param event_time_feature_name: The name of the feature that stores the ``EventTime`` of a ``Record`` in
        a ``FeatureGroup``.
        :param feature_definitions: A list of ``Feature`` names and types.
        :param online_store_config: You can turn the ``OnlineStore`` on or off by specifying ``True`` for
        the ``EnableOnlineStore`` flag in ``OnlineStoreConfig``.
        :param offline_store_config: Use this to configure an ``OfflineFeatureStore``.
        :param throughput_config: Used to set feature group throughput configuration.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM execution role used to persist
        data into the ``OfflineStore`` if an ``OfflineStoreConfig`` is provided.
        :param description: A free-form description of a ``FeatureGroup``.
        :param tags: Tags used to identify ``Features`` in each ``FeatureGroup``.
        :returns: CreateFeatureGroupResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateFlowDefinition")
    def create_flow_definition(
        self,
        context: RequestContext,
        flow_definition_name: FlowDefinitionName,
        output_config: FlowDefinitionOutputConfig,
        role_arn: RoleArn,
        human_loop_request_source: HumanLoopRequestSource | None = None,
        human_loop_activation_config: HumanLoopActivationConfig | None = None,
        human_loop_config: HumanLoopConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateFlowDefinitionResponse:
        """Creates a flow definition.

        :param flow_definition_name: The name of your flow definition.
        :param output_config: An object containing information about where the human review results
        will be uploaded.
        :param role_arn: The Amazon Resource Name (ARN) of the role needed to call other services
        on your behalf.
        :param human_loop_request_source: Container for configuring the source of human task requests.
        :param human_loop_activation_config: An object containing information about the events that trigger a human
        workflow.
        :param human_loop_config: An object containing information about the tasks the human reviewers
        will perform.
        :param tags: An array of key-value pairs that contain metadata to help you categorize
        and organize a flow definition.
        :returns: CreateFlowDefinitionResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateHub")
    def create_hub(
        self,
        context: RequestContext,
        hub_name: HubName,
        hub_description: HubDescription,
        hub_display_name: HubDisplayName | None = None,
        hub_search_keywords: HubSearchKeywordList | None = None,
        s3_storage_config: HubS3StorageConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateHubResponse:
        """Create a hub.

        :param hub_name: The name of the hub to create.
        :param hub_description: A description of the hub.
        :param hub_display_name: The display name of the hub.
        :param hub_search_keywords: The searchable keywords for the hub.
        :param s3_storage_config: The Amazon S3 storage configuration for the hub.
        :param tags: Any tags to associate with the hub.
        :returns: CreateHubResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateHubContentReference")
    def create_hub_content_reference(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        sage_maker_public_hub_content_arn: SageMakerPublicHubContentArn,
        hub_content_name: HubContentName | None = None,
        min_version: HubContentVersion | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateHubContentReferenceResponse:
        """Create a hub content reference in order to add a model in the JumpStart
        public hub to a private hub.

        :param hub_name: The name of the hub to add the hub content reference to.
        :param sage_maker_public_hub_content_arn: The ARN of the public hub content to reference.
        :param hub_content_name: The name of the hub content to reference.
        :param min_version: The minimum version of the hub content to reference.
        :param tags: Any tags associated with the hub content to reference.
        :returns: CreateHubContentReferenceResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateHumanTaskUi")
    def create_human_task_ui(
        self,
        context: RequestContext,
        human_task_ui_name: HumanTaskUiName,
        ui_template: UiTemplate,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateHumanTaskUiResponse:
        """Defines the settings you will use for the human review workflow user
        interface. Reviewers will see a three-panel interface with an
        instruction area, the item to review, and an input area.

        :param human_task_ui_name: The name of the user interface you are creating.
        :param ui_template: The Liquid template for the worker user interface.
        :param tags: An array of key-value pairs that contain metadata to help you categorize
        and organize a human review workflow user interface.
        :returns: CreateHumanTaskUiResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateHyperParameterTuningJob")
    def create_hyper_parameter_tuning_job(
        self,
        context: RequestContext,
        hyper_parameter_tuning_job_name: HyperParameterTuningJobName,
        hyper_parameter_tuning_job_config: HyperParameterTuningJobConfig,
        training_job_definition: HyperParameterTrainingJobDefinition | None = None,
        training_job_definitions: HyperParameterTrainingJobDefinitions | None = None,
        warm_start_config: HyperParameterTuningJobWarmStartConfig | None = None,
        tags: TagList | None = None,
        autotune: Autotune | None = None,
        **kwargs,
    ) -> CreateHyperParameterTuningJobResponse:
        """Starts a hyperparameter tuning job. A hyperparameter tuning job finds
        the best version of a model by running many training jobs on your
        dataset using the algorithm you choose and values for hyperparameters
        within ranges that you specify. It then chooses the hyperparameter
        values that result in a model that performs the best, as measured by an
        objective metric that you choose.

        A hyperparameter tuning job automatically creates Amazon SageMaker
        experiments, trials, and trial components for each training job that it
        runs. You can view these entities in Amazon SageMaker Studio. For more
        information, see `View Experiments, Trials, and Trial
        Components <https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-view-compare.html#experiments-view>`__.

        Do not include any security-sensitive information including account
        access IDs, secrets, or tokens in any hyperparameter fields. As part of
        the shared responsibility model, you are responsible for any potential
        exposure, unauthorized access, or compromise of your sensitive data if
        caused by any security-sensitive information included in the request
        hyperparameter variable or plain text fields..

        :param hyper_parameter_tuning_job_name: The name of the tuning job.
        :param hyper_parameter_tuning_job_config: The
        `HyperParameterTuningJobConfig <https://docs.
        :param training_job_definition: The
        `HyperParameterTrainingJobDefinition <https://docs.
        :param training_job_definitions: A list of the
        `HyperParameterTrainingJobDefinition <https://docs.
        :param warm_start_config: Specifies the configuration for starting the hyperparameter tuning job
        using one or more previous tuning jobs as a starting point.
        :param tags: An array of key-value pairs.
        :param autotune: Configures SageMaker Automatic model tuning (AMT) to automatically find
        optimal parameters for the following fields:

        -  `ParameterRanges <https://docs.
        :returns: CreateHyperParameterTuningJobResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateImage")
    def create_image(
        self,
        context: RequestContext,
        image_name: ImageName,
        role_arn: RoleArn,
        description: ImageDescription | None = None,
        display_name: ImageDisplayName | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateImageResponse:
        """Creates a custom SageMaker AI image. A SageMaker AI image is a set of
        image versions. Each image version represents a container image stored
        in Amazon ECR. For more information, see `Bring your own SageMaker AI
        image <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html>`__.

        :param image_name: The name of the image.
        :param role_arn: The ARN of an IAM role that enables Amazon SageMaker AI to perform tasks
        on your behalf.
        :param description: The description of the image.
        :param display_name: The display name of the image.
        :param tags: A list of tags to apply to the image.
        :returns: CreateImageResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateImageVersion")
    def create_image_version(
        self,
        context: RequestContext,
        base_image: ImageBaseImage,
        client_token: ClientToken,
        image_name: ImageName,
        aliases: SageMakerImageVersionAliases | None = None,
        vendor_guidance: VendorGuidance | None = None,
        job_type: JobType | None = None,
        ml_framework: MLFramework | None = None,
        programming_lang: ProgrammingLang | None = None,
        processor: Processor | None = None,
        horovod: Horovod | None = None,
        release_notes: ReleaseNotes | None = None,
        **kwargs,
    ) -> CreateImageVersionResponse:
        """Creates a version of the SageMaker AI image specified by ``ImageName``.
        The version represents the Amazon ECR container image specified by
        ``BaseImage``.

        :param base_image: The registry path of the container image to use as the starting point
        for this version.
        :param client_token: A unique ID.
        :param image_name: The ``ImageName`` of the ``Image`` to create a version of.
        :param aliases: A list of aliases created with the image version.
        :param vendor_guidance: The stability of the image version, specified by the maintainer.
        :param job_type: Indicates SageMaker AI job type compatibility.
        :param ml_framework: The machine learning framework vended in the image version.
        :param programming_lang: The supported programming language and its version.
        :param processor: Indicates CPU or GPU compatibility.
        :param horovod: Indicates Horovod compatibility.
        :param release_notes: The maintainer description of the image version.
        :returns: CreateImageVersionResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateInferenceComponent")
    def create_inference_component(
        self,
        context: RequestContext,
        inference_component_name: InferenceComponentName,
        endpoint_name: EndpointName,
        specification: InferenceComponentSpecification,
        variant_name: VariantName | None = None,
        runtime_config: InferenceComponentRuntimeConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateInferenceComponentOutput:
        """Creates an inference component, which is a SageMaker AI hosting object
        that you can use to deploy a model to an endpoint. In the inference
        component settings, you specify the model, the endpoint, and how the
        model utilizes the resources that the endpoint hosts. You can optimize
        resource utilization by tailoring how the required CPU cores,
        accelerators, and memory are allocated. You can deploy multiple
        inference components to an endpoint, where each inference component
        contains one model and the resource utilization needs for that
        individual model. After you deploy an inference component, you can
        directly invoke the associated model when you use the InvokeEndpoint API
        action.

        :param inference_component_name: A unique name to assign to the inference component.
        :param endpoint_name: The name of an existing endpoint where you host the inference component.
        :param specification: Details about the resources to deploy with this inference component,
        including the model, container, and compute resources.
        :param variant_name: The name of an existing production variant where you host the inference
        component.
        :param runtime_config: Runtime settings for a model that is deployed with an inference
        component.
        :param tags: A list of key-value pairs associated with the model.
        :returns: CreateInferenceComponentOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateInferenceExperiment", expand=False)
    def create_inference_experiment(
        self, context: RequestContext, request: CreateInferenceExperimentRequest, **kwargs
    ) -> CreateInferenceExperimentResponse:
        """Creates an inference experiment using the configurations specified in
        the request.

        Use this API to setup and schedule an experiment to compare model
        variants on a Amazon SageMaker inference endpoint. For more information
        about inference experiments, see `Shadow
        tests <https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html>`__.

        Amazon SageMaker begins your experiment at the scheduled time and routes
        traffic to your endpoint's model variants based on your specified
        configuration.

        While the experiment is in progress or after it has concluded, you can
        view metrics that compare your model variants. For more information, see
        `View, monitor, and edit shadow
        tests <https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-view-monitor-edit.html>`__.

        :param name: The name for the inference experiment.
        :param type: The type of the inference experiment that you want to run.
        :param role_arn: The ARN of the IAM role that Amazon SageMaker can assume to access model
        artifacts and container images, and manage Amazon SageMaker Inference
        endpoints for model deployment.
        :param endpoint_name: The name of the Amazon SageMaker endpoint on which you want to run the
        inference experiment.
        :param model_variants: An array of ``ModelVariantConfig`` objects.
        :param shadow_mode_config: The configuration of ``ShadowMode`` inference experiment type.
        :param schedule: The duration for which you want the inference experiment to run.
        :param description: A description for the inference experiment.
        :param data_storage_config: The Amazon S3 location and configuration for storing inference request
        and response data.
        :param kms_key: The Amazon Web Services Key Management Service (Amazon Web Services KMS)
        key that Amazon SageMaker uses to encrypt data on the storage volume
        attached to the ML compute instance that hosts the endpoint.
        :param tags: Array of key-value pairs.
        :returns: CreateInferenceExperimentResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateInferenceRecommendationsJob")
    def create_inference_recommendations_job(
        self,
        context: RequestContext,
        job_name: RecommendationJobName,
        job_type: RecommendationJobType,
        role_arn: RoleArn,
        input_config: RecommendationJobInputConfig,
        job_description: RecommendationJobDescription | None = None,
        stopping_conditions: RecommendationJobStoppingConditions | None = None,
        output_config: RecommendationJobOutputConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateInferenceRecommendationsJobResponse:
        """Starts a recommendation job. You can create either an instance
        recommendation or load test job.

        :param job_name: A name for the recommendation job.
        :param job_type: Defines the type of recommendation job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that enables Amazon
        SageMaker to perform tasks on your behalf.
        :param input_config: Provides information about the versioned model package Amazon Resource
        Name (ARN), the traffic pattern, and endpoint configurations.
        :param job_description: Description of the recommendation job.
        :param stopping_conditions: A set of conditions for stopping a recommendation job.
        :param output_config: Provides information about the output artifacts and the KMS key to use
        for Amazon S3 server-side encryption.
        :param tags: The metadata that you apply to Amazon Web Services resources to help you
        categorize and organize them.
        :returns: CreateInferenceRecommendationsJobResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateLabelingJob")
    def create_labeling_job(
        self,
        context: RequestContext,
        labeling_job_name: LabelingJobName,
        label_attribute_name: LabelAttributeName,
        input_config: LabelingJobInputConfig,
        output_config: LabelingJobOutputConfig,
        role_arn: RoleArn,
        human_task_config: HumanTaskConfig,
        label_category_config_s3_uri: S3Uri | None = None,
        stopping_conditions: LabelingJobStoppingConditions | None = None,
        labeling_job_algorithms_config: LabelingJobAlgorithmsConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateLabelingJobResponse:
        """Creates a job that uses workers to label the data objects in your input
        dataset. You can use the labeled data to train machine learning models.

        You can select your workforce from one of three providers:

        -  A private workforce that you create. It can include employees,
           contractors, and outside experts. Use a private workforce when want
           the data to stay within your organization or when a specific set of
           skills is required.

        -  One or more vendors that you select from the Amazon Web Services
           Marketplace. Vendors provide expertise in specific areas.

        -  The Amazon Mechanical Turk workforce. This is the largest workforce,
           but it should only be used for public data or data that has been
           stripped of any personally identifiable information.

        You can also use *automated data labeling* to reduce the number of data
        objects that need to be labeled by a human. Automated data labeling uses
        *active learning* to determine if a data object can be labeled by
        machine or if it needs to be sent to a human worker. For more
        information, see `Using Automated Data
        Labeling <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html>`__.

        The data objects to be labeled are contained in an Amazon S3 bucket. You
        create a *manifest file* that describes the location of each object. For
        more information, see `Using Input and Output
        Data <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data.html>`__.

        The output can be used as the manifest file for another labeling job or
        as training data for your machine learning models.

        You can use this operation to create a static labeling job or a
        streaming labeling job. A static labeling job stops if all data objects
        in the input manifest file identified in ``ManifestS3Uri`` have been
        labeled. A streaming labeling job runs perpetually until it is manually
        stopped, or remains idle for 10 days. You can send new data objects to
        an active (``InProgress``) streaming labeling job in real time. To learn
        how to create a static labeling job, see `Create a Labeling Job
        (API) <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-labeling-job-api.html>`__
        in the Amazon SageMaker Developer Guide. To learn how to create a
        streaming labeling job, see `Create a Streaming Labeling
        Job <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-create-job.html>`__.

        :param labeling_job_name: The name of the labeling job.
        :param label_attribute_name: The attribute name to use for the label in the output manifest file.
        :param input_config: Input data for the labeling job, such as the Amazon S3 location of the
        data objects and the location of the manifest file that describes the
        data objects.
        :param output_config: The location of the output data and the Amazon Web Services Key
        Management Service key ID for the key used to encrypt the output data,
        if any.
        :param role_arn: The Amazon Resource Number (ARN) that Amazon SageMaker assumes to
        perform tasks on your behalf during data labeling.
        :param human_task_config: Configures the labeling task and how it is presented to workers;
        including, but not limited to price, keywords, and batch size (task
        count).
        :param label_category_config_s3_uri: The S3 URI of the file, referred to as a *label category configuration
        file*, that defines the categories used to label the data objects.
        :param stopping_conditions: A set of conditions for stopping the labeling job.
        :param labeling_job_algorithms_config: Configures the information required to perform automated data labeling.
        :param tags: An array of key/value pairs.
        :returns: CreateLabelingJobResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateMlflowTrackingServer")
    def create_mlflow_tracking_server(
        self,
        context: RequestContext,
        tracking_server_name: TrackingServerName,
        artifact_store_uri: S3Uri,
        role_arn: RoleArn,
        tracking_server_size: TrackingServerSize | None = None,
        mlflow_version: MlflowVersion | None = None,
        automatic_model_registration: Boolean | None = None,
        weekly_maintenance_window_start: WeeklyMaintenanceWindowStart | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateMlflowTrackingServerResponse:
        """Creates an MLflow Tracking Server using a general purpose Amazon S3
        bucket as the artifact store. For more information, see `Create an
        MLflow Tracking
        Server <https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html>`__.

        :param tracking_server_name: A unique string identifying the tracking server name.
        :param artifact_store_uri: The S3 URI for a general purpose bucket to use as the MLflow Tracking
        Server artifact store.
        :param role_arn: The Amazon Resource Name (ARN) for an IAM role in your account that the
        MLflow Tracking Server uses to access the artifact store in Amazon S3.
        :param tracking_server_size: The size of the tracking server you want to create.
        :param mlflow_version: The version of MLflow that the tracking server uses.
        :param automatic_model_registration: Whether to enable or disable automatic registration of new MLflow models
        to the SageMaker Model Registry.
        :param weekly_maintenance_window_start: The day and time of the week in Coordinated Universal Time (UTC) 24-hour
        standard time that weekly maintenance updates are scheduled.
        :param tags: Tags consisting of key-value pairs used to manage metadata for the
        tracking server.
        :returns: CreateMlflowTrackingServerResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModel")
    def create_model(
        self,
        context: RequestContext,
        model_name: ModelName,
        primary_container: ContainerDefinition | None = None,
        containers: ContainerDefinitionList | None = None,
        inference_execution_config: InferenceExecutionConfig | None = None,
        execution_role_arn: RoleArn | None = None,
        tags: TagList | None = None,
        vpc_config: VpcConfig | None = None,
        enable_network_isolation: Boolean | None = None,
        **kwargs,
    ) -> CreateModelOutput:
        """Creates a model in SageMaker. In the request, you name the model and
        describe a primary container. For the primary container, you specify the
        Docker image that contains inference code, artifacts (from prior
        training), and a custom environment map that the inference code uses
        when you deploy the model for predictions.

        Use this API to create a model if you want to use SageMaker hosting
        services or run a batch transform job.

        To host your model, you create an endpoint configuration with the
        ``CreateEndpointConfig`` API, and then create an endpoint with the
        ``CreateEndpoint`` API. SageMaker then deploys all of the containers
        that you defined for the model in the hosting environment.

        To run a batch transform using your model, you start a job with the
        ``CreateTransformJob`` API. SageMaker uses your model and your dataset
        to get inferences which are then saved to a specified S3 location.

        In the request, you also provide an IAM role that SageMaker can assume
        to access model artifacts and docker image for deployment on ML compute
        hosting instances or for batch transform jobs. In addition, you also use
        the IAM role to manage permissions the inference code needs. For
        example, if the inference code access any other Amazon Web Services
        resources, you grant necessary permissions via this role.

        :param model_name: The name of the new model.
        :param primary_container: The location of the primary docker image containing inference code,
        associated artifacts, and custom environment map that the inference code
        uses when the model is deployed for predictions.
        :param containers: Specifies the containers in the inference pipeline.
        :param inference_execution_config: Specifies details of how containers in a multi-container endpoint are
        called.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role that SageMaker can assume
        to access model artifacts and docker image for deployment on ML compute
        instances or for batch transform jobs.
        :param tags: An array of key-value pairs.
        :param vpc_config: A
        `VpcConfig <https://docs.
        :param enable_network_isolation: Isolates the model container.
        :returns: CreateModelOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelBiasJobDefinition")
    def create_model_bias_job_definition(
        self,
        context: RequestContext,
        job_definition_name: MonitoringJobDefinitionName,
        model_bias_app_specification: ModelBiasAppSpecification,
        model_bias_job_input: ModelBiasJobInput,
        model_bias_job_output_config: MonitoringOutputConfig,
        job_resources: MonitoringResources,
        role_arn: RoleArn,
        model_bias_baseline_config: ModelBiasBaselineConfig | None = None,
        network_config: MonitoringNetworkConfig | None = None,
        stopping_condition: MonitoringStoppingCondition | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateModelBiasJobDefinitionResponse:
        """Creates the definition for a model bias job.

        :param job_definition_name: The name of the bias job definition.
        :param model_bias_app_specification: Configures the model bias job to run a specified Docker container image.
        :param model_bias_job_input: Inputs for the model bias job.
        :param model_bias_job_output_config: The output configuration for monitoring jobs.
        :param job_resources: Identifies the resources to deploy for a monitoring job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI
        can assume to perform tasks on your behalf.
        :param model_bias_baseline_config: The baseline configuration for a model bias job.
        :param network_config: Networking options for a model bias job.
        :param stopping_condition: A time limit for how long the monitoring job is allowed to run before
        stopping.
        :param tags: (Optional) An array of key-value pairs.
        :returns: CreateModelBiasJobDefinitionResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelCard")
    def create_model_card(
        self,
        context: RequestContext,
        model_card_name: EntityName,
        content: ModelCardContent,
        model_card_status: ModelCardStatus,
        security_config: ModelCardSecurityConfig | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateModelCardResponse:
        """Creates an Amazon SageMaker Model Card.

        For information about how to use model cards, see `Amazon SageMaker
        Model
        Card <https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html>`__.

        :param model_card_name: The unique name of the model card.
        :param content: The content of the model card.
        :param model_card_status: The approval status of the model card within your organization.
        :param security_config: An optional Key Management Service key to encrypt, decrypt, and
        re-encrypt model card content for regulated workloads with highly
        sensitive data.
        :param tags: Key-value pairs used to manage metadata for model cards.
        :returns: CreateModelCardResponse
        :raises ConflictException:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelCardExportJob")
    def create_model_card_export_job(
        self,
        context: RequestContext,
        model_card_name: ModelCardNameOrArn,
        model_card_export_job_name: EntityName,
        output_config: ModelCardExportOutputConfig,
        model_card_version: Integer | None = None,
        **kwargs,
    ) -> CreateModelCardExportJobResponse:
        """Creates an Amazon SageMaker Model Card export job.

        :param model_card_name: The name or Amazon Resource Name (ARN) of the model card to export.
        :param model_card_export_job_name: The name of the model card export job.
        :param output_config: The model card output configuration that specifies the Amazon S3 path
        for exporting.
        :param model_card_version: The version of the model card to export.
        :returns: CreateModelCardExportJobResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelExplainabilityJobDefinition")
    def create_model_explainability_job_definition(
        self,
        context: RequestContext,
        job_definition_name: MonitoringJobDefinitionName,
        model_explainability_app_specification: ModelExplainabilityAppSpecification,
        model_explainability_job_input: ModelExplainabilityJobInput,
        model_explainability_job_output_config: MonitoringOutputConfig,
        job_resources: MonitoringResources,
        role_arn: RoleArn,
        model_explainability_baseline_config: ModelExplainabilityBaselineConfig | None = None,
        network_config: MonitoringNetworkConfig | None = None,
        stopping_condition: MonitoringStoppingCondition | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateModelExplainabilityJobDefinitionResponse:
        """Creates the definition for a model explainability job.

        :param job_definition_name: The name of the model explainability job definition.
        :param model_explainability_app_specification: Configures the model explainability job to run a specified Docker
        container image.
        :param model_explainability_job_input: Inputs for the model explainability job.
        :param model_explainability_job_output_config: The output configuration for monitoring jobs.
        :param job_resources: Identifies the resources to deploy for a monitoring job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI
        can assume to perform tasks on your behalf.
        :param model_explainability_baseline_config: The baseline configuration for a model explainability job.
        :param network_config: Networking options for a model explainability job.
        :param stopping_condition: A time limit for how long the monitoring job is allowed to run before
        stopping.
        :param tags: (Optional) An array of key-value pairs.
        :returns: CreateModelExplainabilityJobDefinitionResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelPackage")
    def create_model_package(
        self,
        context: RequestContext,
        model_package_name: EntityName | None = None,
        model_package_group_name: ArnOrName | None = None,
        model_package_description: EntityDescription | None = None,
        inference_specification: InferenceSpecification | None = None,
        validation_specification: ModelPackageValidationSpecification | None = None,
        source_algorithm_specification: SourceAlgorithmSpecification | None = None,
        certify_for_marketplace: CertifyForMarketplace | None = None,
        tags: TagList | None = None,
        model_approval_status: ModelApprovalStatus | None = None,
        metadata_properties: MetadataProperties | None = None,
        model_metrics: ModelMetrics | None = None,
        client_token: ClientToken | None = None,
        domain: String | None = None,
        task: String | None = None,
        sample_payload_url: S3Uri | None = None,
        customer_metadata_properties: CustomerMetadataMap | None = None,
        drift_check_baselines: DriftCheckBaselines | None = None,
        additional_inference_specifications: AdditionalInferenceSpecifications | None = None,
        skip_model_validation: SkipModelValidation | None = None,
        source_uri: ModelPackageSourceUri | None = None,
        security_config: ModelPackageSecurityConfig | None = None,
        model_card: ModelPackageModelCard | None = None,
        model_life_cycle: ModelLifeCycle | None = None,
        **kwargs,
    ) -> CreateModelPackageOutput:
        """Creates a model package that you can use to create SageMaker models or
        list on Amazon Web Services Marketplace, or a versioned model that is
        part of a model group. Buyers can subscribe to model packages listed on
        Amazon Web Services Marketplace to create models in SageMaker.

        To create a model package by specifying a Docker container that contains
        your inference code and the Amazon S3 location of your model artifacts,
        provide values for ``InferenceSpecification``. To create a model from an
        algorithm resource that you created or subscribed to in Amazon Web
        Services Marketplace, provide a value for
        ``SourceAlgorithmSpecification``.

        There are two types of model packages:

        -  Versioned - a model that is part of a model group in the model
           registry.

        -  Unversioned - a model package that is not part of a model group.

        :param model_package_name: The name of the model package.
        :param model_package_group_name: The name or Amazon Resource Name (ARN) of the model package group that
        this model version belongs to.
        :param model_package_description: A description of the model package.
        :param inference_specification: Specifies details about inference jobs that you can run with models
        based on this model package, including the following information:

        -  The Amazon ECR paths of containers that contain the inference code
           and model artifacts.
        :param validation_specification: Specifies configurations for one or more transform jobs that SageMaker
        runs to test the model package.
        :param source_algorithm_specification: Details about the algorithm that was used to create the model package.
        :param certify_for_marketplace: Whether to certify the model package for listing on Amazon Web Services
        Marketplace.
        :param tags: A list of key value pairs associated with the model.
        :param model_approval_status: Whether the model is approved for deployment.
        :param metadata_properties: Metadata properties of the tracking entity, trial, or trial component.
        :param model_metrics: A structure that contains model metrics reports.
        :param client_token: A unique token that guarantees that the call to this API is idempotent.
        :param domain: The machine learning domain of your model package and its components.
        :param task: The machine learning task your model package accomplishes.
        :param sample_payload_url: The Amazon Simple Storage Service (Amazon S3) path where the sample
        payload is stored.
        :param customer_metadata_properties: The metadata properties associated with the model package versions.
        :param drift_check_baselines: Represents the drift check baselines that can be used when the model
        monitor is set using the model package.
        :param additional_inference_specifications: An array of additional Inference Specification objects.
        :param skip_model_validation: Indicates if you want to skip model validation.
        :param source_uri: The URI of the source for the model package.
        :param security_config: The KMS Key ID (``KMSKeyId``) used for encryption of model package
        information.
        :param model_card: The model card associated with the model package.
        :param model_life_cycle: A structure describing the current state of the model in its life cycle.
        :returns: CreateModelPackageOutput
        :raises ConflictException:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelPackageGroup")
    def create_model_package_group(
        self,
        context: RequestContext,
        model_package_group_name: EntityName,
        model_package_group_description: EntityDescription | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateModelPackageGroupOutput:
        """Creates a model group. A model group contains a group of model versions.

        :param model_package_group_name: The name of the model group.
        :param model_package_group_description: A description for the model group.
        :param tags: A list of key value pairs associated with the model group.
        :returns: CreateModelPackageGroupOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateModelQualityJobDefinition")
    def create_model_quality_job_definition(
        self,
        context: RequestContext,
        job_definition_name: MonitoringJobDefinitionName,
        model_quality_app_specification: ModelQualityAppSpecification,
        model_quality_job_input: ModelQualityJobInput,
        model_quality_job_output_config: MonitoringOutputConfig,
        job_resources: MonitoringResources,
        role_arn: RoleArn,
        model_quality_baseline_config: ModelQualityBaselineConfig | None = None,
        network_config: MonitoringNetworkConfig | None = None,
        stopping_condition: MonitoringStoppingCondition | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateModelQualityJobDefinitionResponse:
        """Creates a definition for a job that monitors model quality and drift.
        For information about model monitor, see `Amazon SageMaker AI Model
        Monitor <https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html>`__.

        :param job_definition_name: The name of the monitoring job definition.
        :param model_quality_app_specification: The container that runs the monitoring job.
        :param model_quality_job_input: A list of the inputs that are monitored.
        :param model_quality_job_output_config: The output configuration for monitoring jobs.
        :param job_resources: Identifies the resources to deploy for a monitoring job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI
        can assume to perform tasks on your behalf.
        :param model_quality_baseline_config: Specifies the constraints and baselines for the monitoring job.
        :param network_config: Specifies the network configuration for the monitoring job.
        :param stopping_condition: A time limit for how long the monitoring job is allowed to run before
        stopping.
        :param tags: (Optional) An array of key-value pairs.
        :returns: CreateModelQualityJobDefinitionResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateMonitoringSchedule")
    def create_monitoring_schedule(
        self,
        context: RequestContext,
        monitoring_schedule_name: MonitoringScheduleName,
        monitoring_schedule_config: MonitoringScheduleConfig,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateMonitoringScheduleResponse:
        """Creates a schedule that regularly starts Amazon SageMaker AI Processing
        Jobs to monitor the data captured for an Amazon SageMaker AI Endpoint.

        :param monitoring_schedule_name: The name of the monitoring schedule.
        :param monitoring_schedule_config: The configuration object that specifies the monitoring schedule and
        defines the monitoring job.
        :param tags: (Optional) An array of key-value pairs.
        :returns: CreateMonitoringScheduleResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateNotebookInstance")
    def create_notebook_instance(
        self,
        context: RequestContext,
        notebook_instance_name: NotebookInstanceName,
        instance_type: InstanceType,
        role_arn: RoleArn,
        subnet_id: SubnetId | None = None,
        security_group_ids: SecurityGroupIds | None = None,
        kms_key_id: KmsKeyId | None = None,
        tags: TagList | None = None,
        lifecycle_config_name: NotebookInstanceLifecycleConfigName | None = None,
        direct_internet_access: DirectInternetAccess | None = None,
        volume_size_in_gb: NotebookInstanceVolumeSizeInGB | None = None,
        accelerator_types: NotebookInstanceAcceleratorTypes | None = None,
        default_code_repository: CodeRepositoryNameOrUrl | None = None,
        additional_code_repositories: AdditionalCodeRepositoryNamesOrUrls | None = None,
        root_access: RootAccess | None = None,
        platform_identifier: PlatformIdentifier | None = None,
        instance_metadata_service_configuration: InstanceMetadataServiceConfiguration | None = None,
        **kwargs,
    ) -> CreateNotebookInstanceOutput:
        """Creates an SageMaker AI notebook instance. A notebook instance is a
        machine learning (ML) compute instance running on a Jupyter notebook.

        In a ``CreateNotebookInstance`` request, specify the type of ML compute
        instance that you want to run. SageMaker AI launches the instance,
        installs common libraries that you can use to explore datasets for model
        training, and attaches an ML storage volume to the notebook instance.

        SageMaker AI also provides a set of example notebooks. Each notebook
        demonstrates how to use SageMaker AI with a specific algorithm or with a
        machine learning framework.

        After receiving the request, SageMaker AI does the following:

        #. Creates a network interface in the SageMaker AI VPC.

        #. (Option) If you specified ``SubnetId``, SageMaker AI creates a
           network interface in your own VPC, which is inferred from the subnet
           ID that you provide in the input. When creating this network
           interface, SageMaker AI attaches the security group that you
           specified in the request to the network interface that it creates in
           your VPC.

        #. Launches an EC2 instance of the type specified in the request in the
           SageMaker AI VPC. If you specified ``SubnetId`` of your VPC,
           SageMaker AI specifies both network interfaces when launching this
           instance. This enables inbound traffic from your own VPC to the
           notebook instance, assuming that the security groups allow it.

        After creating the notebook instance, SageMaker AI returns its Amazon
        Resource Name (ARN). You can't change the name of a notebook instance
        after you create it.

        After SageMaker AI creates the notebook instance, you can connect to the
        Jupyter server and work in Jupyter notebooks. For example, you can write
        code to explore a dataset that you can use for model training, train a
        model, host models by creating SageMaker AI endpoints, and validate
        hosted models.

        For more information, see `How It
        Works <https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__.

        :param notebook_instance_name: The name of the new notebook instance.
        :param instance_type: The type of ML compute instance to launch for the notebook instance.
        :param role_arn: When you send any requests to Amazon Web Services resources from the
        notebook instance, SageMaker AI assumes this role to perform tasks on
        your behalf.
        :param subnet_id: The ID of the subnet in a VPC to which you would like to have a
        connectivity from your ML compute instance.
        :param security_group_ids: The VPC security group IDs, in the form sg-xxxxxxxx.
        :param kms_key_id: The Amazon Resource Name (ARN) of a Amazon Web Services Key Management
        Service key that SageMaker AI uses to encrypt data on the storage volume
        attached to your notebook instance.
        :param tags: An array of key-value pairs.
        :param lifecycle_config_name: The name of a lifecycle configuration to associate with the notebook
        instance.
        :param direct_internet_access: Sets whether SageMaker AI provides internet access to the notebook
        instance.
        :param volume_size_in_gb: The size, in GB, of the ML storage volume to attach to the notebook
        instance.
        :param accelerator_types: This parameter is no longer supported.
        :param default_code_repository: A Git repository to associate with the notebook instance as its default
        code repository.
        :param additional_code_repositories: An array of up to three Git repositories to associate with the notebook
        instance.
        :param root_access: Whether root access is enabled or disabled for users of the notebook
        instance.
        :param platform_identifier: The platform identifier of the notebook instance runtime environment.
        :param instance_metadata_service_configuration: Information on the IMDS configuration of the notebook instance.
        :returns: CreateNotebookInstanceOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateNotebookInstanceLifecycleConfig")
    def create_notebook_instance_lifecycle_config(
        self,
        context: RequestContext,
        notebook_instance_lifecycle_config_name: NotebookInstanceLifecycleConfigName,
        on_create: NotebookInstanceLifecycleConfigList | None = None,
        on_start: NotebookInstanceLifecycleConfigList | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateNotebookInstanceLifecycleConfigOutput:
        """Creates a lifecycle configuration that you can associate with a notebook
        instance. A *lifecycle configuration* is a collection of shell scripts
        that run when you create or start a notebook instance.

        Each lifecycle configuration script has a limit of 16384 characters.

        The value of the ``$PATH`` environment variable that is available to
        both scripts is ``/sbin:bin:/usr/sbin:/usr/bin``.

        View Amazon CloudWatch Logs for notebook instance lifecycle
        configurations in log group ``/aws/sagemaker/NotebookInstances`` in log
        stream ``[notebook-instance-name]/[LifecycleConfigHook]``.

        Lifecycle configuration scripts cannot run for longer than 5 minutes. If
        a script runs for longer than 5 minutes, it fails and the notebook
        instance is not created or started.

        For information about notebook instance lifestyle configurations, see
        `Step 2.1: (Optional) Customize a Notebook
        Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__.

        :param notebook_instance_lifecycle_config_name: The name of the lifecycle configuration.
        :param on_create: A shell script that runs only once, when you create a notebook instance.
        :param on_start: A shell script that runs every time you start a notebook instance,
        including when you create the notebook instance.
        :param tags: An array of key-value pairs.
        :returns: CreateNotebookInstanceLifecycleConfigOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateOptimizationJob")
    def create_optimization_job(
        self,
        context: RequestContext,
        optimization_job_name: EntityName,
        role_arn: RoleArn,
        model_source: OptimizationJobModelSource,
        deployment_instance_type: OptimizationJobDeploymentInstanceType,
        optimization_configs: OptimizationConfigs,
        output_config: OptimizationJobOutputConfig,
        stopping_condition: StoppingCondition,
        optimization_environment: OptimizationJobEnvironmentVariables | None = None,
        tags: TagList | None = None,
        vpc_config: OptimizationVpcConfig | None = None,
        **kwargs,
    ) -> CreateOptimizationJobResponse:
        """Creates a job that optimizes a model for inference performance. To
        create the job, you provide the location of a source model, and you
        provide the settings for the optimization techniques that you want the
        job to apply. When the job completes successfully, SageMaker uploads the
        new optimized model to the output destination that you specify.

        For more information about how to use this action, and about the
        supported optimization techniques, see `Optimize model inference with
        Amazon
        SageMaker <https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html>`__.

        :param optimization_job_name: A custom name for the new optimization job.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that enables Amazon
        SageMaker AI to perform tasks on your behalf.
        :param model_source: The location of the source model to optimize with an optimization job.
        :param deployment_instance_type: The type of instance that hosts the optimized model that you create with
        the optimization job.
        :param optimization_configs: Settings for each of the optimization techniques that the job applies.
        :param output_config: Details for where to store the optimized model that you create with the
        optimization job.
        :param stopping_condition: Specifies a limit to how long a job can run.
        :param optimization_environment: The environment variables to set in the model container.
        :param tags: A list of key-value pairs associated with the optimization job.
        :param vpc_config: A VPC in Amazon VPC that your optimized model has access to.
        :returns: CreateOptimizationJobResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreatePartnerApp", expand=False)
    def create_partner_app(
        self, context: RequestContext, request: CreatePartnerAppRequest, **kwargs
    ) -> CreatePartnerAppResponse:
        """Creates an Amazon SageMaker Partner AI App.

        :param name: The name to give the SageMaker Partner AI App.
        :param type: The type of SageMaker Partner AI App to create.
        :param execution_role_arn: The ARN of the IAM role that the partner application uses.
        :param tier: Indicates the instance type and size of the cluster attached to the
        SageMaker Partner AI App.
        :param auth_type: The authorization type that users use to access the SageMaker Partner AI
        App.
        :param kms_key_id: SageMaker Partner AI Apps uses Amazon Web Services KMS to encrypt data
        at rest using an Amazon Web Services managed key by default.
        :param maintenance_config: Maintenance configuration settings for the SageMaker Partner AI App.
        :param application_config: Configuration settings for the SageMaker Partner AI App.
        :param enable_iam_session_based_identity: When set to ``TRUE``, the SageMaker Partner AI App sets the Amazon Web
        Services IAM session name or the authenticated IAM user as the identity
        of the SageMaker Partner AI App user.
        :param client_token: A unique token that guarantees that the call to this API is idempotent.
        :param tags: Each tag consists of a key and an optional value.
        :returns: CreatePartnerAppResponse
        :raises ConflictException:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreatePartnerAppPresignedUrl")
    def create_partner_app_presigned_url(
        self,
        context: RequestContext,
        arn: PartnerAppArn,
        expires_in_seconds: ExpiresInSeconds | None = None,
        session_expiration_duration_in_seconds: SessionExpirationDurationInSeconds | None = None,
        **kwargs,
    ) -> CreatePartnerAppPresignedUrlResponse:
        """Creates a presigned URL to access an Amazon SageMaker Partner AI App.

        :param arn: The ARN of the SageMaker Partner AI App to create the presigned URL for.
        :param expires_in_seconds: The time that will pass before the presigned URL expires.
        :param session_expiration_duration_in_seconds: Indicates how long the Amazon SageMaker Partner AI App session can be
        accessed for after logging in.
        :returns: CreatePartnerAppPresignedUrlResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("CreatePipeline")
    def create_pipeline(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        client_request_token: IdempotencyToken,
        role_arn: RoleArn,
        pipeline_display_name: PipelineName | None = None,
        pipeline_definition: PipelineDefinition | None = None,
        pipeline_definition_s3_location: PipelineDefinitionS3Location | None = None,
        pipeline_description: PipelineDescription | None = None,
        tags: TagList | None = None,
        parallelism_configuration: ParallelismConfiguration | None = None,
        **kwargs,
    ) -> CreatePipelineResponse:
        """Creates a pipeline using a JSON pipeline definition.

        :param pipeline_name: The name of the pipeline.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :param role_arn: The Amazon Resource Name (ARN) of the role used by the pipeline to
        access and create resources.
        :param pipeline_display_name: The display name of the pipeline.
        :param pipeline_definition: The `JSON pipeline
        definition <https://aws-sagemaker-mlops.
        :param pipeline_definition_s3_location: The location of the pipeline definition stored in Amazon S3.
        :param pipeline_description: A description of the pipeline.
        :param tags: A list of tags to apply to the created pipeline.
        :param parallelism_configuration: This is the configuration that controls the parallelism of the pipeline.
        :returns: CreatePipelineResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreatePresignedDomainUrl")
    def create_presigned_domain_url(
        self,
        context: RequestContext,
        domain_id: DomainId,
        user_profile_name: UserProfileName,
        session_expiration_duration_in_seconds: SessionExpirationDurationInSeconds | None = None,
        expires_in_seconds: ExpiresInSeconds | None = None,
        space_name: SpaceName | None = None,
        landing_uri: LandingUri | None = None,
        **kwargs,
    ) -> CreatePresignedDomainUrlResponse:
        """Creates a URL for a specified UserProfile in a Domain. When accessed in
        a web browser, the user will be automatically signed in to the domain,
        and granted access to all of the Apps and files associated with the
        Domain's Amazon Elastic File System volume. This operation can only be
        called when the authentication mode equals IAM.

        The IAM role or user passed to this API defines the permissions to
        access the app. Once the presigned URL is created, no additional
        permission is required to access this URL. IAM authorization policies
        for this API are also enforced for every HTTP request and WebSocket
        frame that attempts to connect to the app.

        You can restrict access to this API and to the URL that it returns to a
        list of IP addresses, Amazon VPCs or Amazon VPC Endpoints that you
        specify. For more information, see `Connect to Amazon SageMaker AI
        Studio Through an Interface VPC
        Endpoint <https://docs.aws.amazon.com/sagemaker/latest/dg/studio-interface-endpoint.html>`__
        .

        -  The URL that you get from a call to ``CreatePresignedDomainUrl`` has
           a default timeout of 5 minutes. You can configure this value using
           ``ExpiresInSeconds``. If you try to use the URL after the timeout
           limit expires, you are directed to the Amazon Web Services console
           sign-in page.

        -  The JupyterLab session default expiration time is 12 hours. You can
           configure this value using SessionExpirationDurationInSeconds.

        :param domain_id: The domain ID.
        :param user_profile_name: The name of the UserProfile to sign-in as.
        :param session_expiration_duration_in_seconds: The session expiration duration in seconds.
        :param expires_in_seconds: The number of seconds until the pre-signed URL expires.
        :param space_name: The name of the space.
        :param landing_uri: The landing page that the user is directed to when accessing the
        presigned URL.
        :returns: CreatePresignedDomainUrlResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("CreatePresignedMlflowTrackingServerUrl")
    def create_presigned_mlflow_tracking_server_url(
        self,
        context: RequestContext,
        tracking_server_name: TrackingServerName,
        expires_in_seconds: ExpiresInSeconds | None = None,
        session_expiration_duration_in_seconds: SessionExpirationDurationInSeconds | None = None,
        **kwargs,
    ) -> CreatePresignedMlflowTrackingServerUrlResponse:
        """Returns a presigned URL that you can use to connect to the MLflow UI
        attached to your tracking server. For more information, see `Launch the
        MLflow UI using a presigned
        URL <https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-launch-ui.html>`__.

        :param tracking_server_name: The name of the tracking server to connect to your MLflow UI.
        :param expires_in_seconds: The duration in seconds that your presigned URL is valid.
        :param session_expiration_duration_in_seconds: The duration in seconds that your MLflow UI session is valid.
        :returns: CreatePresignedMlflowTrackingServerUrlResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("CreatePresignedNotebookInstanceUrl")
    def create_presigned_notebook_instance_url(
        self,
        context: RequestContext,
        notebook_instance_name: NotebookInstanceName,
        session_expiration_duration_in_seconds: SessionExpirationDurationInSeconds | None = None,
        **kwargs,
    ) -> CreatePresignedNotebookInstanceUrlOutput:
        """Returns a URL that you can use to connect to the Jupyter server from a
        notebook instance. In the SageMaker AI console, when you choose ``Open``
        next to a notebook instance, SageMaker AI opens a new tab showing the
        Jupyter server home page from the notebook instance. The console uses
        this API to get the URL and show the page.

        The IAM role or user used to call this API defines the permissions to
        access the notebook instance. Once the presigned URL is created, no
        additional permission is required to access this URL. IAM authorization
        policies for this API are also enforced for every HTTP request and
        WebSocket frame that attempts to connect to the notebook instance.

        You can restrict access to this API and to the URL that it returns to a
        list of IP addresses that you specify. Use the ``NotIpAddress``
        condition operator and the ``aws:SourceIP`` condition context key to
        specify the list of IP addresses that you want to have access to the
        notebook instance. For more information, see `Limit Access to a Notebook
        Instance by IP
        Address <https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html#nbi-ip-filter>`__.

        The URL that you get from a call to
        `CreatePresignedNotebookInstanceUrl <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedNotebookInstanceUrl.html>`__
        is valid only for 5 minutes. If you try to use the URL after the
        5-minute limit expires, you are directed to the Amazon Web Services
        console sign-in page.

        :param notebook_instance_name: The name of the notebook instance.
        :param session_expiration_duration_in_seconds: The duration of the session, in seconds.
        :returns: CreatePresignedNotebookInstanceUrlOutput
        """
        raise NotImplementedError

    @handler("CreateProcessingJob")
    def create_processing_job(
        self,
        context: RequestContext,
        processing_job_name: ProcessingJobName,
        processing_resources: ProcessingResources,
        app_specification: AppSpecification,
        role_arn: RoleArn,
        processing_inputs: ProcessingInputs | None = None,
        processing_output_config: ProcessingOutputConfig | None = None,
        stopping_condition: ProcessingStoppingCondition | None = None,
        environment: ProcessingEnvironmentMap | None = None,
        network_config: NetworkConfig | None = None,
        tags: TagList | None = None,
        experiment_config: ExperimentConfig | None = None,
        **kwargs,
    ) -> CreateProcessingJobResponse:
        """Creates a processing job.

        :param processing_job_name: The name of the processing job.
        :param processing_resources: Identifies the resources, ML compute instances, and ML storage volumes
        to deploy for a processing job.
        :param app_specification: Configures the processing job to run a specified Docker container image.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can
        assume to perform tasks on your behalf.
        :param processing_inputs: An array of inputs configuring the data to download into the processing
        container.
        :param processing_output_config: Output configuration for the processing job.
        :param stopping_condition: The time limit for how long the processing job is allowed to run.
        :param environment: The environment variables to set in the Docker container.
        :param network_config: Networking options for a processing job, such as whether to allow
        inbound and outbound network calls to and from processing containers,
        and the VPC subnets and security groups to use for VPC-enabled
        processing jobs.
        :param tags: (Optional) An array of key-value pairs.
        :param experiment_config: Associates a SageMaker job as a trial component with an experiment and
        trial.
        :returns: CreateProcessingJobResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateProject")
    def create_project(
        self,
        context: RequestContext,
        project_name: ProjectEntityName,
        project_description: EntityDescription | None = None,
        service_catalog_provisioning_details: ServiceCatalogProvisioningDetails | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateProjectOutput:
        """Creates a machine learning (ML) project that can contain one or more
        templates that set up an ML pipeline from training to deploying an
        approved model.

        :param project_name: The name of the project.
        :param project_description: A description for the project.
        :param service_catalog_provisioning_details: The product ID and provisioning artifact ID to provision a service
        catalog.
        :param tags: An array of key-value pairs that you want to use to organize and track
        your Amazon Web Services resource costs.
        :returns: CreateProjectOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateSpace")
    def create_space(
        self,
        context: RequestContext,
        domain_id: DomainId,
        space_name: SpaceName,
        tags: TagList | None = None,
        space_settings: SpaceSettings | None = None,
        ownership_settings: OwnershipSettings | None = None,
        space_sharing_settings: SpaceSharingSettings | None = None,
        space_display_name: NonEmptyString64 | None = None,
        **kwargs,
    ) -> CreateSpaceResponse:
        """Creates a private space or a space used for real time collaboration in a
        domain.

        :param domain_id: The ID of the associated domain.
        :param space_name: The name of the space.
        :param tags: Tags to associated with the space.
        :param space_settings: A collection of space settings.
        :param ownership_settings: A collection of ownership settings.
        :param space_sharing_settings: A collection of space sharing settings.
        :param space_display_name: The name of the space that appears in the SageMaker Studio UI.
        :returns: CreateSpaceResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateStudioLifecycleConfig")
    def create_studio_lifecycle_config(
        self,
        context: RequestContext,
        studio_lifecycle_config_name: StudioLifecycleConfigName,
        studio_lifecycle_config_content: StudioLifecycleConfigContent,
        studio_lifecycle_config_app_type: StudioLifecycleConfigAppType,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateStudioLifecycleConfigResponse:
        """Creates a new Amazon SageMaker AI Studio Lifecycle Configuration.

        :param studio_lifecycle_config_name: The name of the Amazon SageMaker AI Studio Lifecycle Configuration to
        create.
        :param studio_lifecycle_config_content: The content of your Amazon SageMaker AI Studio Lifecycle Configuration
        script.
        :param studio_lifecycle_config_app_type: The App type that the Lifecycle Configuration is attached to.
        :param tags: Tags to be associated with the Lifecycle Configuration.
        :returns: CreateStudioLifecycleConfigResponse
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("CreateTrainingJob")
    def create_training_job(
        self,
        context: RequestContext,
        training_job_name: TrainingJobName,
        algorithm_specification: AlgorithmSpecification,
        role_arn: RoleArn,
        output_data_config: OutputDataConfig,
        resource_config: ResourceConfig,
        stopping_condition: StoppingCondition,
        hyper_parameters: HyperParameters | None = None,
        input_data_config: InputDataConfig | None = None,
        vpc_config: VpcConfig | None = None,
        tags: TagList | None = None,
        enable_network_isolation: Boolean | None = None,
        enable_inter_container_traffic_encryption: Boolean | None = None,
        enable_managed_spot_training: Boolean | None = None,
        checkpoint_config: CheckpointConfig | None = None,
        debug_hook_config: DebugHookConfig | None = None,
        debug_rule_configurations: DebugRuleConfigurations | None = None,
        tensor_board_output_config: TensorBoardOutputConfig | None = None,
        experiment_config: ExperimentConfig | None = None,
        profiler_config: ProfilerConfig | None = None,
        profiler_rule_configurations: ProfilerRuleConfigurations | None = None,
        environment: TrainingEnvironmentMap | None = None,
        retry_strategy: RetryStrategy | None = None,
        remote_debug_config: RemoteDebugConfig | None = None,
        infra_check_config: InfraCheckConfig | None = None,
        session_chaining_config: SessionChainingConfig | None = None,
        **kwargs,
    ) -> CreateTrainingJobResponse:
        """Starts a model training job. After training completes, SageMaker saves
        the resulting model artifacts to an Amazon S3 location that you specify.

        If you choose to host your model using SageMaker hosting services, you
        can use the resulting model artifacts as part of the model. You can also
        use the artifacts in a machine learning service other than SageMaker,
        provided that you know how to use them for inference.

        In the request body, you provide the following:

        -  ``AlgorithmSpecification`` - Identifies the training algorithm to
           use.

        -  ``HyperParameters`` - Specify these algorithm-specific parameters to
           enable the estimation of model parameters during training.
           Hyperparameters can be tuned to optimize this learning process. For a
           list of hyperparameters for each training algorithm provided by
           SageMaker, see
           `Algorithms <https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__.

           Do not include any security-sensitive information including account
           access IDs, secrets, or tokens in any hyperparameter fields. As part
           of the shared responsibility model, you are responsible for any
           potential exposure, unauthorized access, or compromise of your
           sensitive data if caused by security-sensitive information included
           in the request hyperparameter variable or plain text fields.

        -  ``InputDataConfig`` - Describes the input required by the training
           job and the Amazon S3, EFS, or FSx location where it is stored.

        -  ``OutputDataConfig`` - Identifies the Amazon S3 bucket where you want
           SageMaker to save the results of model training.

        -  ``ResourceConfig`` - Identifies the resources, ML compute instances,
           and ML storage volumes to deploy for model training. In distributed
           training, you specify more than one instance.

        -  ``EnableManagedSpotTraining`` - Optimize the cost of training machine
           learning models by up to 80% by using Amazon EC2 Spot instances. For
           more information, see `Managed Spot
           Training <https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html>`__.

        -  ``RoleArn`` - The Amazon Resource Name (ARN) that SageMaker assumes
           to perform tasks on your behalf during model training. You must grant
           this role the necessary permissions so that SageMaker can
           successfully complete model training.

        -  ``StoppingCondition`` - To help cap training costs, use
           ``MaxRuntimeInSeconds`` to set a time limit for training. Use
           ``MaxWaitTimeInSeconds`` to specify how long a managed spot training
           job has to complete.

        -  ``Environment`` - The environment variables to set in the Docker
           container.

           Do not include any security-sensitive information including account
           access IDs, secrets, or tokens in any environment fields. As part of
           the shared responsibility model, you are responsible for any
           potential exposure, unauthorized access, or compromise of your
           sensitive data if caused by security-sensitive information included
           in the request environment variable or plain text fields.

        -  ``RetryStrategy`` - The number of times to retry the job when the job
           fails due to an ``InternalServerError``.

        For more information about SageMaker, see `How It
        Works <https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__.

        :param training_job_name: The name of the training job.
        :param algorithm_specification: The registry path of the Docker image that contains the training
        algorithm and algorithm-specific metadata, including the input mode.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role that SageMaker can assume
        to perform tasks on your behalf.
        :param output_data_config: Specifies the path to the S3 location where you want to store model
        artifacts.
        :param resource_config: The resources, including the ML compute instances and ML storage
        volumes, to use for model training.
        :param stopping_condition: Specifies a limit to how long a model training job can run.
        :param hyper_parameters: Algorithm-specific parameters that influence the quality of the model.
        :param input_data_config: An array of ``Channel`` objects.
        :param vpc_config: A
        `VpcConfig <https://docs.
        :param tags: An array of key-value pairs.
        :param enable_network_isolation: Isolates the training container.
        :param enable_inter_container_traffic_encryption: To encrypt all communications between ML compute instances in
        distributed training, choose ``True``.
        :param enable_managed_spot_training: To train models using managed spot training, choose ``True``.
        :param checkpoint_config: Contains information about the output location for managed spot training
        checkpoint data.
        :param debug_hook_config: Configuration information for the Amazon SageMaker Debugger hook
        parameters, metric and tensor collections, and storage paths.
        :param debug_rule_configurations: Configuration information for Amazon SageMaker Debugger rules for
        debugging output tensors.
        :param tensor_board_output_config: Configuration of storage locations for the Amazon SageMaker Debugger
        TensorBoard output data.
        :param experiment_config: Associates a SageMaker job as a trial component with an experiment and
        trial.
        :param profiler_config: Configuration information for Amazon SageMaker Debugger system
        monitoring, framework profiling, and storage paths.
        :param profiler_rule_configurations: Configuration information for Amazon SageMaker Debugger rules for
        profiling system and framework metrics.
        :param environment: The environment variables to set in the Docker container.
        :param retry_strategy: The number of times to retry the job when the job fails due to an
        ``InternalServerError``.
        :param remote_debug_config: Configuration for remote debugging.
        :param infra_check_config: Contains information about the infrastructure health check configuration
        for the training job.
        :param session_chaining_config: Contains information about attribute-based access control (ABAC) for the
        training job.
        :returns: CreateTrainingJobResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateTrainingPlan")
    def create_training_plan(
        self,
        context: RequestContext,
        training_plan_name: TrainingPlanName,
        training_plan_offering_id: TrainingPlanOfferingId,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateTrainingPlanResponse:
        """Creates a new training plan in SageMaker to reserve compute capacity.

        Amazon SageMaker Training Plan is a capability within SageMaker that
        allows customers to reserve and manage GPU capacity for large-scale AI
        model training. It provides a way to secure predictable access to
        computational resources within specific timelines and budgets, without
        the need to manage underlying infrastructure.

        **How it works**

        Plans can be created for specific resources such as SageMaker Training
        Jobs or SageMaker HyperPod clusters, automatically provisioning
        resources, setting up infrastructure, executing workloads, and handling
        infrastructure failures.

        **Plan creation workflow**

        -  Users search for available plan offerings based on their requirements
           (e.g., instance type, count, start time, duration) using the
           ``SearchTrainingPlanOfferings`` API operation.

        -  They create a plan that best matches their needs using the ID of the
           plan offering they want to use.

        -  After successful upfront payment, the plan's status becomes
           ``Scheduled``.

        -  The plan can be used to:

           -  Queue training jobs.

           -  Allocate to an instance group of a SageMaker HyperPod cluster.

        -  When the plan start date arrives, it becomes ``Active``. Based on
           available reserved capacity:

           -  Training jobs are launched.

           -  Instance groups are provisioned.

        **Plan composition**

        A plan can consist of one or more Reserved Capacities, each defined by a
        specific instance type, quantity, Availability Zone, duration, and start
        and end times. For more information about Reserved Capacity, see
        ``ReservedCapacitySummary``.

        :param training_plan_name: The name of the training plan to create.
        :param training_plan_offering_id: The unique identifier of the training plan offering to use for creating
        this plan.
        :param tags: An array of key-value pairs to apply to this training plan.
        :returns: CreateTrainingPlanResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateTransformJob")
    def create_transform_job(
        self,
        context: RequestContext,
        transform_job_name: TransformJobName,
        model_name: ModelName,
        transform_input: TransformInput,
        transform_output: TransformOutput,
        transform_resources: TransformResources,
        max_concurrent_transforms: MaxConcurrentTransforms | None = None,
        model_client_config: ModelClientConfig | None = None,
        max_payload_in_mb: MaxPayloadInMB | None = None,
        batch_strategy: BatchStrategy | None = None,
        environment: TransformEnvironmentMap | None = None,
        data_capture_config: BatchDataCaptureConfig | None = None,
        data_processing: DataProcessing | None = None,
        tags: TagList | None = None,
        experiment_config: ExperimentConfig | None = None,
        **kwargs,
    ) -> CreateTransformJobResponse:
        """Starts a transform job. A transform job uses a trained model to get
        inferences on a dataset and saves these results to an Amazon S3 location
        that you specify.

        To perform batch transformations, you create a transform job and use the
        data that you have readily available.

        In the request body, you provide the following:

        -  ``TransformJobName`` - Identifies the transform job. The name must be
           unique within an Amazon Web Services Region in an Amazon Web Services
           account.

        -  ``ModelName`` - Identifies the model to use. ``ModelName`` must be
           the name of an existing Amazon SageMaker model in the same Amazon Web
           Services Region and Amazon Web Services account. For information on
           creating a model, see
           `CreateModel <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html>`__.

        -  ``TransformInput`` - Describes the dataset to be transformed and the
           Amazon S3 location where it is stored.

        -  ``TransformOutput`` - Identifies the Amazon S3 location where you
           want Amazon SageMaker to save the results from the transform job.

        -  ``TransformResources`` - Identifies the ML compute instances and AMI
           image versions for the transform job.

        For more information about how batch transformation works, see `Batch
        Transform <https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html>`__.

        :param transform_job_name: The name of the transform job.
        :param model_name: The name of the model that you want to use for the transform job.
        :param transform_input: Describes the input source and the way the transform job consumes it.
        :param transform_output: Describes the results of the transform job.
        :param transform_resources: Describes the resources, including ML instance types and ML instance
        count, to use for the transform job.
        :param max_concurrent_transforms: The maximum number of parallel requests that can be sent to each
        instance in a transform job.
        :param model_client_config: Configures the timeout and maximum number of retries for processing a
        transform job invocation.
        :param max_payload_in_mb: The maximum allowed size of the payload, in MB.
        :param batch_strategy: Specifies the number of records to include in a mini-batch for an HTTP
        inference request.
        :param environment: The environment variables to set in the Docker container.
        :param data_capture_config: Configuration to control how SageMaker captures inference data.
        :param data_processing: The data structure used to specify the data to be used for inference in
        a batch transform job and to associate the data that is relevant to the
        prediction results in the output.
        :param tags: (Optional) An array of key-value pairs.
        :param experiment_config: Associates a SageMaker job as a trial component with an experiment and
        trial.
        :returns: CreateTransformJobResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateTrial")
    def create_trial(
        self,
        context: RequestContext,
        trial_name: ExperimentEntityName,
        experiment_name: ExperimentEntityName,
        display_name: ExperimentEntityName | None = None,
        metadata_properties: MetadataProperties | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateTrialResponse:
        """Creates an SageMaker *trial*. A trial is a set of steps called *trial
        components* that produce a machine learning model. A trial is part of a
        single SageMaker *experiment*.

        When you use SageMaker Studio or the SageMaker Python SDK, all
        experiments, trials, and trial components are automatically tracked,
        logged, and indexed. When you use the Amazon Web Services SDK for Python
        (Boto), you must use the logging APIs provided by the SDK.

        You can add tags to a trial and then use the
        `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
        API to search for the tags.

        To get a list of all your trials, call the
        `ListTrials <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html>`__
        API. To view a trial's properties, call the
        `DescribeTrial <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrial.html>`__
        API. To create a trial component, call the
        `CreateTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html>`__
        API.

        :param trial_name: The name of the trial.
        :param experiment_name: The name of the experiment to associate the trial with.
        :param display_name: The name of the trial as displayed.
        :param metadata_properties: Metadata properties of the tracking entity, trial, or trial component.
        :param tags: A list of tags to associate with the trial.
        :returns: CreateTrialResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateTrialComponent")
    def create_trial_component(
        self,
        context: RequestContext,
        trial_component_name: ExperimentEntityName,
        display_name: ExperimentEntityName | None = None,
        status: TrialComponentStatus | None = None,
        start_time: Timestamp | None = None,
        end_time: Timestamp | None = None,
        parameters: TrialComponentParameters | None = None,
        input_artifacts: TrialComponentArtifacts | None = None,
        output_artifacts: TrialComponentArtifacts | None = None,
        metadata_properties: MetadataProperties | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateTrialComponentResponse:
        """Creates a *trial component*, which is a stage of a machine learning
        *trial*. A trial is composed of one or more trial components. A trial
        component can be used in multiple trials.

        Trial components include pre-processing jobs, training jobs, and batch
        transform jobs.

        When you use SageMaker Studio or the SageMaker Python SDK, all
        experiments, trials, and trial components are automatically tracked,
        logged, and indexed. When you use the Amazon Web Services SDK for Python
        (Boto), you must use the logging APIs provided by the SDK.

        You can add tags to a trial component and then use the
        `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
        API to search for the tags.

        :param trial_component_name: The name of the component.
        :param display_name: The name of the component as displayed.
        :param status: The status of the component.
        :param start_time: When the component started.
        :param end_time: When the component ended.
        :param parameters: The hyperparameters for the component.
        :param input_artifacts: The input artifacts for the component.
        :param output_artifacts: The output artifacts for the component.
        :param metadata_properties: Metadata properties of the tracking entity, trial, or trial component.
        :param tags: A list of tags to associate with the component.
        :returns: CreateTrialComponentResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateUserProfile")
    def create_user_profile(
        self,
        context: RequestContext,
        domain_id: DomainId,
        user_profile_name: UserProfileName,
        single_sign_on_user_identifier: SingleSignOnUserIdentifier | None = None,
        single_sign_on_user_value: String256 | None = None,
        tags: TagList | None = None,
        user_settings: UserSettings | None = None,
        **kwargs,
    ) -> CreateUserProfileResponse:
        """Creates a user profile. A user profile represents a single user within a
        domain, and is the main way to reference a "person" for the purposes of
        sharing, reporting, and other user-oriented features. This entity is
        created when a user onboards to a domain. If an administrator invites a
        person by email or imports them from IAM Identity Center, a user profile
        is automatically created. A user profile is the primary holder of
        settings for an individual user and has a reference to the user's
        private Amazon Elastic File System home directory.

        :param domain_id: The ID of the associated Domain.
        :param user_profile_name: A name for the UserProfile.
        :param single_sign_on_user_identifier: A specifier for the type of value specified in SingleSignOnUserValue.
        :param single_sign_on_user_value: The username of the associated Amazon Web Services Single Sign-On User
        for this UserProfile.
        :param tags: Each tag consists of a key and an optional value.
        :param user_settings: A collection of settings.
        :returns: CreateUserProfileResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("CreateWorkforce")
    def create_workforce(
        self,
        context: RequestContext,
        workforce_name: WorkforceName,
        cognito_config: CognitoConfig | None = None,
        oidc_config: OidcConfig | None = None,
        source_ip_config: SourceIpConfig | None = None,
        tags: TagList | None = None,
        workforce_vpc_config: WorkforceVpcConfigRequest | None = None,
        **kwargs,
    ) -> CreateWorkforceResponse:
        """Use this operation to create a workforce. This operation will return an
        error if a workforce already exists in the Amazon Web Services Region
        that you specify. You can only create one workforce in each Amazon Web
        Services Region per Amazon Web Services account.

        If you want to create a new workforce in an Amazon Web Services Region
        where a workforce already exists, use the
        `DeleteWorkforce <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkforce.html>`__
        API operation to delete the existing workforce and then use
        ``CreateWorkforce`` to create a new workforce.

        To create a private workforce using Amazon Cognito, you must specify a
        Cognito user pool in ``CognitoConfig``. You can also create an Amazon
        Cognito workforce using the Amazon SageMaker console. For more
        information, see `Create a Private Workforce (Amazon
        Cognito) <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html>`__.

        To create a private workforce using your own OIDC Identity Provider
        (IdP), specify your IdP configuration in ``OidcConfig``. Your OIDC IdP
        must support *groups* because groups are used by Ground Truth and Amazon
        A2I to create work teams. For more information, see `Create a Private
        Workforce (OIDC
        IdP) <https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private-oidc.html>`__.

        :param workforce_name: The name of the private workforce.
        :param cognito_config: Use this parameter to configure an Amazon Cognito private workforce.
        :param oidc_config: Use this parameter to configure a private workforce using your own OIDC
        Identity Provider.
        :param source_ip_config: A list of IP address ranges
        (`CIDRs <https://docs.
        :param tags: An array of key-value pairs that contain metadata to help you categorize
        and organize our workforce.
        :param workforce_vpc_config: Use this parameter to configure a workforce using VPC.
        :returns: CreateWorkforceResponse
        """
        raise NotImplementedError

    @handler("CreateWorkteam")
    def create_workteam(
        self,
        context: RequestContext,
        workteam_name: WorkteamName,
        member_definitions: MemberDefinitions,
        description: String200,
        workforce_name: WorkforceName | None = None,
        notification_configuration: NotificationConfiguration | None = None,
        worker_access_configuration: WorkerAccessConfiguration | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> CreateWorkteamResponse:
        """Creates a new work team for labeling your data. A work team is defined
        by one or more Amazon Cognito user pools. You must first create the user
        pools before you can create a work team.

        You cannot create more than 25 work teams in an account and region.

        :param workteam_name: The name of the work team.
        :param member_definitions: A list of ``MemberDefinition`` objects that contains objects that
        identify the workers that make up the work team.
        :param description: A description of the work team.
        :param workforce_name: The name of the workforce.
        :param notification_configuration: Configures notification of workers regarding available or expiring work
        items.
        :param worker_access_configuration: Use this optional parameter to constrain access to an Amazon S3 resource
        based on the IP address using supported IAM global condition keys.
        :param tags: An array of key-value pairs.
        :returns: CreateWorkteamResponse
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("DeleteAction")
    def delete_action(
        self, context: RequestContext, action_name: ExperimentEntityName, **kwargs
    ) -> DeleteActionResponse:
        """Deletes an action.

        :param action_name: The name of the action to delete.
        :returns: DeleteActionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteAlgorithm")
    def delete_algorithm(
        self, context: RequestContext, algorithm_name: EntityName, **kwargs
    ) -> None:
        """Removes the specified algorithm from your account.

        :param algorithm_name: The name of the algorithm to delete.
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteApp")
    def delete_app(
        self,
        context: RequestContext,
        domain_id: DomainId,
        app_type: AppType,
        app_name: AppName,
        user_profile_name: UserProfileName | None = None,
        space_name: SpaceName | None = None,
        **kwargs,
    ) -> None:
        """Used to stop and delete an app.

        :param domain_id: The domain ID.
        :param app_type: The type of app.
        :param app_name: The name of the app.
        :param user_profile_name: The user profile name.
        :param space_name: The name of the space.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteAppImageConfig")
    def delete_app_image_config(
        self, context: RequestContext, app_image_config_name: AppImageConfigName, **kwargs
    ) -> None:
        """Deletes an AppImageConfig.

        :param app_image_config_name: The name of the AppImageConfig to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteArtifact")
    def delete_artifact(
        self,
        context: RequestContext,
        artifact_arn: ArtifactArn | None = None,
        source: ArtifactSource | None = None,
        **kwargs,
    ) -> DeleteArtifactResponse:
        """Deletes an artifact. Either ``ArtifactArn`` or ``Source`` must be
        specified.

        :param artifact_arn: The Amazon Resource Name (ARN) of the artifact to delete.
        :param source: The URI of the source.
        :returns: DeleteArtifactResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteAssociation")
    def delete_association(
        self,
        context: RequestContext,
        source_arn: AssociationEntityArn,
        destination_arn: AssociationEntityArn,
        **kwargs,
    ) -> DeleteAssociationResponse:
        """Deletes an association.

        :param source_arn: The ARN of the source.
        :param destination_arn: The Amazon Resource Name (ARN) of the destination.
        :returns: DeleteAssociationResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteCluster")
    def delete_cluster(
        self, context: RequestContext, cluster_name: ClusterNameOrArn, **kwargs
    ) -> DeleteClusterResponse:
        """Delete a SageMaker HyperPod cluster.

        :param cluster_name: The string name or the Amazon Resource Name (ARN) of the SageMaker
        HyperPod cluster to delete.
        :returns: DeleteClusterResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteClusterSchedulerConfig")
    def delete_cluster_scheduler_config(
        self,
        context: RequestContext,
        cluster_scheduler_config_id: ClusterSchedulerConfigId,
        **kwargs,
    ) -> None:
        """Deletes the cluster policy of the cluster.

        :param cluster_scheduler_config_id: ID of the cluster policy.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteCodeRepository")
    def delete_code_repository(
        self, context: RequestContext, code_repository_name: EntityName, **kwargs
    ) -> None:
        """Deletes the specified Git repository from your account.

        :param code_repository_name: The name of the Git repository to delete.
        """
        raise NotImplementedError

    @handler("DeleteCompilationJob")
    def delete_compilation_job(
        self, context: RequestContext, compilation_job_name: EntityName, **kwargs
    ) -> None:
        """Deletes the specified compilation job. This action deletes only the
        compilation job resource in Amazon SageMaker AI. It doesn't delete other
        resources that are related to that job, such as the model artifacts that
        the job creates, the compilation logs in CloudWatch, the compiled model,
        or the IAM role.

        You can delete a compilation job only if its current status is
        ``COMPLETED``, ``FAILED``, or ``STOPPED``. If the job status is
        ``STARTING`` or ``INPROGRESS``, stop the job, and then delete it after
        its status becomes ``STOPPED``.

        :param compilation_job_name: The name of the compilation job to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteComputeQuota")
    def delete_compute_quota(
        self, context: RequestContext, compute_quota_id: ComputeQuotaId, **kwargs
    ) -> None:
        """Deletes the compute allocation from the cluster.

        :param compute_quota_id: ID of the compute allocation definition.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteContext")
    def delete_context(
        self, context: RequestContext, context_name: ContextName, **kwargs
    ) -> DeleteContextResponse:
        """Deletes an context.

        :param context_name: The name of the context to delete.
        :returns: DeleteContextResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteDataQualityJobDefinition")
    def delete_data_quality_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> None:
        """Deletes a data quality monitoring job definition.

        :param job_definition_name: The name of the data quality monitoring job definition to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteDeviceFleet")
    def delete_device_fleet(
        self, context: RequestContext, device_fleet_name: EntityName, **kwargs
    ) -> None:
        """Deletes a fleet.

        :param device_fleet_name: The name of the fleet to delete.
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteDomain")
    def delete_domain(
        self,
        context: RequestContext,
        domain_id: DomainId,
        retention_policy: RetentionPolicy | None = None,
        **kwargs,
    ) -> None:
        """Used to delete a domain. If you onboarded with IAM mode, you will need
        to delete your domain to onboard again using IAM Identity Center. Use
        with caution. All of the members of the domain will lose access to their
        EFS volume, including data, notebooks, and other artifacts.

        :param domain_id: The domain ID.
        :param retention_policy: The retention policy for this domain, which specifies whether resources
        will be retained after the Domain is deleted.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteEdgeDeploymentPlan")
    def delete_edge_deployment_plan(
        self, context: RequestContext, edge_deployment_plan_name: EntityName, **kwargs
    ) -> None:
        """Deletes an edge deployment plan if (and only if) all the stages in the
        plan are inactive or there are no stages in the plan.

        :param edge_deployment_plan_name: The name of the edge deployment plan to delete.
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteEdgeDeploymentStage")
    def delete_edge_deployment_stage(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        stage_name: EntityName,
        **kwargs,
    ) -> None:
        """Delete a stage in an edge deployment plan if (and only if) the stage is
        inactive.

        :param edge_deployment_plan_name: The name of the edge deployment plan from which the stage will be
        deleted.
        :param stage_name: The name of the stage.
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteEndpoint")
    def delete_endpoint(
        self, context: RequestContext, endpoint_name: EndpointName, **kwargs
    ) -> None:
        """Deletes an endpoint. SageMaker frees up all of the resources that were
        deployed when the endpoint was created.

        SageMaker retires any custom KMS key grants associated with the
        endpoint, meaning you don't need to use the
        `RevokeGrant <http://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html>`__
        API call.

        When you delete your endpoint, SageMaker asynchronously deletes
        associated endpoint resources such as KMS key grants. You might still
        see these resources in your account for a few minutes after deleting
        your endpoint. Do not delete or revoke the permissions for your
        ``ExecutionRoleArn``, otherwise SageMaker cannot delete these resources.

        :param endpoint_name: The name of the endpoint that you want to delete.
        """
        raise NotImplementedError

    @handler("DeleteEndpointConfig")
    def delete_endpoint_config(
        self, context: RequestContext, endpoint_config_name: EndpointConfigName, **kwargs
    ) -> None:
        """Deletes an endpoint configuration. The ``DeleteEndpointConfig`` API
        deletes only the specified configuration. It does not delete endpoints
        created using the configuration.

        You must not delete an ``EndpointConfig`` in use by an endpoint that is
        live or while the ``UpdateEndpoint`` or ``CreateEndpoint`` operations
        are being performed on the endpoint. If you delete the
        ``EndpointConfig`` of an endpoint that is active or being created or
        updated you may lose visibility into the instance type the endpoint is
        using. The endpoint must be deleted in order to stop incurring charges.

        :param endpoint_config_name: The name of the endpoint configuration that you want to delete.
        """
        raise NotImplementedError

    @handler("DeleteExperiment")
    def delete_experiment(
        self, context: RequestContext, experiment_name: ExperimentEntityName, **kwargs
    ) -> DeleteExperimentResponse:
        """Deletes an SageMaker experiment. All trials associated with the
        experiment must be deleted first. Use the
        `ListTrials <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html>`__
        API to get a list of the trials associated with the experiment.

        :param experiment_name: The name of the experiment to delete.
        :returns: DeleteExperimentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteFeatureGroup")
    def delete_feature_group(
        self, context: RequestContext, feature_group_name: FeatureGroupName, **kwargs
    ) -> None:
        """Delete the ``FeatureGroup`` and any data that was written to the
        ``OnlineStore`` of the ``FeatureGroup``. Data cannot be accessed from
        the ``OnlineStore`` immediately after ``DeleteFeatureGroup`` is called.

        Data written into the ``OfflineStore`` will not be deleted. The Amazon
        Web Services Glue database and tables that are automatically created for
        your ``OfflineStore`` are not deleted.

        Note that it can take approximately 10-15 minutes to delete an
        ``OnlineStore`` ``FeatureGroup`` with the ``InMemory`` ``StorageType``.

        :param feature_group_name: The name of the ``FeatureGroup`` you want to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteFlowDefinition")
    def delete_flow_definition(
        self, context: RequestContext, flow_definition_name: FlowDefinitionName, **kwargs
    ) -> DeleteFlowDefinitionResponse:
        """Deletes the specified flow definition.

        :param flow_definition_name: The name of the flow definition you are deleting.
        :returns: DeleteFlowDefinitionResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteHub")
    def delete_hub(self, context: RequestContext, hub_name: HubNameOrArn, **kwargs) -> None:
        """Delete a hub.

        :param hub_name: The name of the hub to delete.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteHubContent")
    def delete_hub_content(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_type: HubContentType,
        hub_content_name: HubContentName,
        hub_content_version: HubContentVersion,
        **kwargs,
    ) -> None:
        """Delete the contents of a hub.

        :param hub_name: The name of the hub that you want to delete content in.
        :param hub_content_type: The type of content that you want to delete from a hub.
        :param hub_content_name: The name of the content that you want to delete from a hub.
        :param hub_content_version: The version of the content that you want to delete from a hub.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteHubContentReference")
    def delete_hub_content_reference(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_type: HubContentType,
        hub_content_name: HubContentName,
        **kwargs,
    ) -> None:
        """Delete a hub content reference in order to remove a model from a private
        hub.

        :param hub_name: The name of the hub to delete the hub content reference from.
        :param hub_content_type: The type of hub content reference to delete.
        :param hub_content_name: The name of the hub content to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteHumanTaskUi")
    def delete_human_task_ui(
        self, context: RequestContext, human_task_ui_name: HumanTaskUiName, **kwargs
    ) -> DeleteHumanTaskUiResponse:
        """Use this operation to delete a human task user interface (worker task
        template).

        To see a list of human task user interfaces (work task templates) in
        your account, use
        `ListHumanTaskUis <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHumanTaskUis.html>`__.
        When you delete a worker task template, it no longer appears when you
        call ``ListHumanTaskUis``.

        :param human_task_ui_name: The name of the human task user interface (work task template) you want
        to delete.
        :returns: DeleteHumanTaskUiResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteHyperParameterTuningJob")
    def delete_hyper_parameter_tuning_job(
        self,
        context: RequestContext,
        hyper_parameter_tuning_job_name: HyperParameterTuningJobName,
        **kwargs,
    ) -> None:
        """Deletes a hyperparameter tuning job. The
        ``DeleteHyperParameterTuningJob`` API deletes only the tuning job entry
        that was created in SageMaker when you called the
        ``CreateHyperParameterTuningJob`` API. It does not delete training jobs,
        artifacts, or the IAM role that you specified when creating the model.

        :param hyper_parameter_tuning_job_name: The name of the hyperparameter tuning job that you want to delete.
        """
        raise NotImplementedError

    @handler("DeleteImage")
    def delete_image(
        self, context: RequestContext, image_name: ImageName, **kwargs
    ) -> DeleteImageResponse:
        """Deletes a SageMaker AI image and all versions of the image. The
        container images aren't deleted.

        :param image_name: The name of the image to delete.
        :returns: DeleteImageResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteImageVersion")
    def delete_image_version(
        self,
        context: RequestContext,
        image_name: ImageName,
        version: ImageVersionNumber | None = None,
        alias: SageMakerImageVersionAlias | None = None,
        **kwargs,
    ) -> DeleteImageVersionResponse:
        """Deletes a version of a SageMaker AI image. The container image the
        version represents isn't deleted.

        :param image_name: The name of the image to delete.
        :param version: The version to delete.
        :param alias: The alias of the image to delete.
        :returns: DeleteImageVersionResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteInferenceComponent")
    def delete_inference_component(
        self, context: RequestContext, inference_component_name: InferenceComponentName, **kwargs
    ) -> None:
        """Deletes an inference component.

        :param inference_component_name: The name of the inference component to delete.
        """
        raise NotImplementedError

    @handler("DeleteInferenceExperiment")
    def delete_inference_experiment(
        self, context: RequestContext, name: InferenceExperimentName, **kwargs
    ) -> DeleteInferenceExperimentResponse:
        """Deletes an inference experiment.

        This operation does not delete your endpoint, variants, or any
        underlying resources. This operation only deletes the metadata of your
        experiment.

        :param name: The name of the inference experiment you want to delete.
        :returns: DeleteInferenceExperimentResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteMlflowTrackingServer")
    def delete_mlflow_tracking_server(
        self, context: RequestContext, tracking_server_name: TrackingServerName, **kwargs
    ) -> DeleteMlflowTrackingServerResponse:
        """Deletes an MLflow Tracking Server. For more information, see `Clean up
        MLflow
        resources <https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-cleanup.html.html>`__.

        :param tracking_server_name: The name of the the tracking server to delete.
        :returns: DeleteMlflowTrackingServerResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteModel")
    def delete_model(self, context: RequestContext, model_name: ModelName, **kwargs) -> None:
        """Deletes a model. The ``DeleteModel`` API deletes only the model entry
        that was created in SageMaker when you called the ``CreateModel`` API.
        It does not delete model artifacts, inference code, or the IAM role that
        you specified when creating the model.

        :param model_name: The name of the model to delete.
        """
        raise NotImplementedError

    @handler("DeleteModelBiasJobDefinition")
    def delete_model_bias_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> None:
        """Deletes an Amazon SageMaker AI model bias job definition.

        :param job_definition_name: The name of the model bias job definition to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteModelCard")
    def delete_model_card(
        self, context: RequestContext, model_card_name: EntityName, **kwargs
    ) -> None:
        """Deletes an Amazon SageMaker Model Card.

        :param model_card_name: The name of the model card to delete.
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteModelExplainabilityJobDefinition")
    def delete_model_explainability_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> None:
        """Deletes an Amazon SageMaker AI model explainability job definition.

        :param job_definition_name: The name of the model explainability job definition to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteModelPackage")
    def delete_model_package(
        self, context: RequestContext, model_package_name: VersionedArnOrName, **kwargs
    ) -> None:
        """Deletes a model package.

        A model package is used to create SageMaker models or list on Amazon Web
        Services Marketplace. Buyers can subscribe to model packages listed on
        Amazon Web Services Marketplace to create models in SageMaker.

        :param model_package_name: The name or Amazon Resource Name (ARN) of the model package to delete.
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteModelPackageGroup")
    def delete_model_package_group(
        self, context: RequestContext, model_package_group_name: ArnOrName, **kwargs
    ) -> None:
        """Deletes the specified model group.

        :param model_package_group_name: The name of the model group to delete.
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteModelPackageGroupPolicy")
    def delete_model_package_group_policy(
        self, context: RequestContext, model_package_group_name: EntityName, **kwargs
    ) -> None:
        """Deletes a model group resource policy.

        :param model_package_group_name: The name of the model group for which to delete the policy.
        """
        raise NotImplementedError

    @handler("DeleteModelQualityJobDefinition")
    def delete_model_quality_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> None:
        """Deletes the secified model quality monitoring job definition.

        :param job_definition_name: The name of the model quality monitoring job definition to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteMonitoringSchedule")
    def delete_monitoring_schedule(
        self, context: RequestContext, monitoring_schedule_name: MonitoringScheduleName, **kwargs
    ) -> None:
        """Deletes a monitoring schedule. Also stops the schedule had not already
        been stopped. This does not delete the job execution history of the
        monitoring schedule.

        :param monitoring_schedule_name: The name of the monitoring schedule to delete.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteNotebookInstance")
    def delete_notebook_instance(
        self, context: RequestContext, notebook_instance_name: NotebookInstanceName, **kwargs
    ) -> None:
        """Deletes an SageMaker AI notebook instance. Before you can delete a
        notebook instance, you must call the ``StopNotebookInstance`` API.

        When you delete a notebook instance, you lose all of your data.
        SageMaker AI removes the ML compute instance, and deletes the ML storage
        volume and the network interface associated with the notebook instance.

        :param notebook_instance_name: The name of the SageMaker AI notebook instance to delete.
        """
        raise NotImplementedError

    @handler("DeleteNotebookInstanceLifecycleConfig")
    def delete_notebook_instance_lifecycle_config(
        self,
        context: RequestContext,
        notebook_instance_lifecycle_config_name: NotebookInstanceLifecycleConfigName,
        **kwargs,
    ) -> None:
        """Deletes a notebook instance lifecycle configuration.

        :param notebook_instance_lifecycle_config_name: The name of the lifecycle configuration to delete.
        """
        raise NotImplementedError

    @handler("DeleteOptimizationJob")
    def delete_optimization_job(
        self, context: RequestContext, optimization_job_name: EntityName, **kwargs
    ) -> None:
        """Deletes an optimization job.

        :param optimization_job_name: The name that you assigned to the optimization job.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeletePartnerApp")
    def delete_partner_app(
        self,
        context: RequestContext,
        arn: PartnerAppArn,
        client_token: ClientToken | None = None,
        **kwargs,
    ) -> DeletePartnerAppResponse:
        """Deletes a SageMaker Partner AI App.

        :param arn: The ARN of the SageMaker Partner AI App to delete.
        :param client_token: A unique token that guarantees that the call to this API is idempotent.
        :returns: DeletePartnerAppResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeletePipeline")
    def delete_pipeline(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        client_request_token: IdempotencyToken,
        **kwargs,
    ) -> DeletePipelineResponse:
        """Deletes a pipeline if there are no running instances of the pipeline. To
        delete a pipeline, you must stop all running instances of the pipeline
        using the ``StopPipelineExecution`` API. When you delete a pipeline, all
        instances of the pipeline are deleted.

        :param pipeline_name: The name of the pipeline to delete.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :returns: DeletePipelineResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteProject")
    def delete_project(
        self, context: RequestContext, project_name: ProjectEntityName, **kwargs
    ) -> None:
        """Delete the specified project.

        :param project_name: The name of the project to delete.
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteSpace")
    def delete_space(
        self, context: RequestContext, domain_id: DomainId, space_name: SpaceName, **kwargs
    ) -> None:
        """Used to delete a space.

        :param domain_id: The ID of the associated domain.
        :param space_name: The name of the space.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteStudioLifecycleConfig")
    def delete_studio_lifecycle_config(
        self,
        context: RequestContext,
        studio_lifecycle_config_name: StudioLifecycleConfigName,
        **kwargs,
    ) -> None:
        """Deletes the Amazon SageMaker AI Studio Lifecycle Configuration. In order
        to delete the Lifecycle Configuration, there must be no running apps
        using the Lifecycle Configuration. You must also remove the Lifecycle
        Configuration from UserSettings in all Domains and UserProfiles.

        :param studio_lifecycle_config_name: The name of the Amazon SageMaker AI Studio Lifecycle Configuration to
        delete.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteTags")
    def delete_tags(
        self, context: RequestContext, resource_arn: ResourceArn, tag_keys: TagKeyList, **kwargs
    ) -> DeleteTagsOutput:
        """Deletes the specified tags from an SageMaker resource.

        To list a resource's tags, use the ``ListTags`` API.

        When you call this API to delete tags from a hyperparameter tuning job,
        the deleted tags are not removed from training jobs that the
        hyperparameter tuning job launched before you called this API.

        When you call this API to delete tags from a SageMaker Domain or User
        Profile, the deleted tags are not removed from Apps that the SageMaker
        Domain or User Profile launched before you called this API.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource whose tags you want to
        delete.
        :param tag_keys: An array or one or more tag keys to delete.
        :returns: DeleteTagsOutput
        """
        raise NotImplementedError

    @handler("DeleteTrial")
    def delete_trial(
        self, context: RequestContext, trial_name: ExperimentEntityName, **kwargs
    ) -> DeleteTrialResponse:
        """Deletes the specified trial. All trial components that make up the trial
        must be deleted first. Use the
        `DescribeTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html>`__
        API to get the list of trial components.

        :param trial_name: The name of the trial to delete.
        :returns: DeleteTrialResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteTrialComponent")
    def delete_trial_component(
        self, context: RequestContext, trial_component_name: ExperimentEntityName, **kwargs
    ) -> DeleteTrialComponentResponse:
        """Deletes the specified trial component. A trial component must be
        disassociated from all trials before the trial component can be deleted.
        To disassociate a trial component from a trial, call the
        `DisassociateTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DisassociateTrialComponent.html>`__
        API.

        :param trial_component_name: The name of the component to delete.
        :returns: DeleteTrialComponentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DeleteUserProfile")
    def delete_user_profile(
        self,
        context: RequestContext,
        domain_id: DomainId,
        user_profile_name: UserProfileName,
        **kwargs,
    ) -> None:
        """Deletes a user profile. When a user profile is deleted, the user loses
        access to their EFS volume, including data, notebooks, and other
        artifacts.

        :param domain_id: The domain ID.
        :param user_profile_name: The user profile name.
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("DeleteWorkforce")
    def delete_workforce(
        self, context: RequestContext, workforce_name: WorkforceName, **kwargs
    ) -> DeleteWorkforceResponse:
        """Use this operation to delete a workforce.

        If you want to create a new workforce in an Amazon Web Services Region
        where a workforce already exists, use this operation to delete the
        existing workforce and then use
        `CreateWorkforce <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateWorkforce.html>`__
        to create a new workforce.

        If a private workforce contains one or more work teams, you must use the
        `DeleteWorkteam <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html>`__
        operation to delete all work teams before you delete the workforce. If
        you try to delete a workforce that contains one or more work teams, you
        will receive a ``ResourceInUse`` error.

        :param workforce_name: The name of the workforce.
        :returns: DeleteWorkforceResponse
        """
        raise NotImplementedError

    @handler("DeleteWorkteam")
    def delete_workteam(
        self, context: RequestContext, workteam_name: WorkteamName, **kwargs
    ) -> DeleteWorkteamResponse:
        """Deletes an existing work team. This operation can't be undone.

        :param workteam_name: The name of the work team to delete.
        :returns: DeleteWorkteamResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("DeregisterDevices")
    def deregister_devices(
        self,
        context: RequestContext,
        device_fleet_name: EntityName,
        device_names: DeviceNames,
        **kwargs,
    ) -> None:
        """Deregisters the specified devices. After you deregister a device, you
        will need to re-register the devices.

        :param device_fleet_name: The name of the fleet the devices belong to.
        :param device_names: The unique IDs of the devices.
        """
        raise NotImplementedError

    @handler("DescribeAction")
    def describe_action(
        self, context: RequestContext, action_name: ExperimentEntityNameOrArn, **kwargs
    ) -> DescribeActionResponse:
        """Describes an action.

        :param action_name: The name of the action to describe.
        :returns: DescribeActionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeAlgorithm")
    def describe_algorithm(
        self, context: RequestContext, algorithm_name: ArnOrName, **kwargs
    ) -> DescribeAlgorithmOutput:
        """Returns a description of the specified algorithm that is in your
        account.

        :param algorithm_name: The name of the algorithm to describe.
        :returns: DescribeAlgorithmOutput
        """
        raise NotImplementedError

    @handler("DescribeApp")
    def describe_app(
        self,
        context: RequestContext,
        domain_id: DomainId,
        app_type: AppType,
        app_name: AppName,
        user_profile_name: UserProfileName | None = None,
        space_name: SpaceName | None = None,
        **kwargs,
    ) -> DescribeAppResponse:
        """Describes the app.

        :param domain_id: The domain ID.
        :param app_type: The type of app.
        :param app_name: The name of the app.
        :param user_profile_name: The user profile name.
        :param space_name: The name of the space.
        :returns: DescribeAppResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeAppImageConfig")
    def describe_app_image_config(
        self, context: RequestContext, app_image_config_name: AppImageConfigName, **kwargs
    ) -> DescribeAppImageConfigResponse:
        """Describes an AppImageConfig.

        :param app_image_config_name: The name of the AppImageConfig to describe.
        :returns: DescribeAppImageConfigResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeArtifact")
    def describe_artifact(
        self, context: RequestContext, artifact_arn: ArtifactArn, **kwargs
    ) -> DescribeArtifactResponse:
        """Describes an artifact.

        :param artifact_arn: The Amazon Resource Name (ARN) of the artifact to describe.
        :returns: DescribeArtifactResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeAutoMLJob")
    def describe_auto_ml_job(
        self, context: RequestContext, auto_ml_job_name: AutoMLJobName, **kwargs
    ) -> DescribeAutoMLJobResponse:
        """Returns information about an AutoML job created by calling
        `CreateAutoMLJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html>`__.

        AutoML jobs created by calling
        `CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html>`__
        cannot be described by ``DescribeAutoMLJob``.

        :param auto_ml_job_name: Requests information about an AutoML job using its unique name.
        :returns: DescribeAutoMLJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeAutoMLJobV2")
    def describe_auto_ml_job_v2(
        self, context: RequestContext, auto_ml_job_name: AutoMLJobName, **kwargs
    ) -> DescribeAutoMLJobV2Response:
        """Returns information about an AutoML job created by calling
        `CreateAutoMLJobV2 <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html>`__
        or
        `CreateAutoMLJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html>`__.

        :param auto_ml_job_name: Requests information about an AutoML job V2 using its unique name.
        :returns: DescribeAutoMLJobV2Response
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeCluster")
    def describe_cluster(
        self, context: RequestContext, cluster_name: ClusterNameOrArn, **kwargs
    ) -> DescribeClusterResponse:
        """Retrieves information of a SageMaker HyperPod cluster.

        :param cluster_name: The string name or the Amazon Resource Name (ARN) of the SageMaker
        HyperPod cluster.
        :returns: DescribeClusterResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeClusterNode")
    def describe_cluster_node(
        self,
        context: RequestContext,
        cluster_name: ClusterNameOrArn,
        node_id: ClusterNodeId,
        **kwargs,
    ) -> DescribeClusterNodeResponse:
        """Retrieves information of a node (also called a *instance*
        interchangeably) of a SageMaker HyperPod cluster.

        :param cluster_name: The string name or the Amazon Resource Name (ARN) of the SageMaker
        HyperPod cluster in which the node is.
        :param node_id: The ID of the SageMaker HyperPod cluster node.
        :returns: DescribeClusterNodeResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeClusterSchedulerConfig")
    def describe_cluster_scheduler_config(
        self,
        context: RequestContext,
        cluster_scheduler_config_id: ClusterSchedulerConfigId,
        cluster_scheduler_config_version: Integer | None = None,
        **kwargs,
    ) -> DescribeClusterSchedulerConfigResponse:
        """Description of the cluster policy. This policy is used for task
        prioritization and fair-share allocation. This helps prioritize critical
        workloads and distributes idle compute across entities.

        :param cluster_scheduler_config_id: ID of the cluster policy.
        :param cluster_scheduler_config_version: Version of the cluster policy.
        :returns: DescribeClusterSchedulerConfigResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeCodeRepository")
    def describe_code_repository(
        self, context: RequestContext, code_repository_name: EntityName, **kwargs
    ) -> DescribeCodeRepositoryOutput:
        """Gets details about the specified Git repository.

        :param code_repository_name: The name of the Git repository to describe.
        :returns: DescribeCodeRepositoryOutput
        """
        raise NotImplementedError

    @handler("DescribeCompilationJob")
    def describe_compilation_job(
        self, context: RequestContext, compilation_job_name: EntityName, **kwargs
    ) -> DescribeCompilationJobResponse:
        """Returns information about a model compilation job.

        To create a model compilation job, use
        `CreateCompilationJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html>`__.
        To get information about multiple model compilation jobs, use
        `ListCompilationJobs <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html>`__.

        :param compilation_job_name: The name of the model compilation job that you want information about.
        :returns: DescribeCompilationJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeComputeQuota")
    def describe_compute_quota(
        self,
        context: RequestContext,
        compute_quota_id: ComputeQuotaId,
        compute_quota_version: Integer | None = None,
        **kwargs,
    ) -> DescribeComputeQuotaResponse:
        """Description of the compute allocation definition.

        :param compute_quota_id: ID of the compute allocation definition.
        :param compute_quota_version: Version of the compute allocation definition.
        :returns: DescribeComputeQuotaResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeContext")
    def describe_context(
        self, context: RequestContext, context_name: ContextNameOrArn, **kwargs
    ) -> DescribeContextResponse:
        """Describes a context.

        :param context_name: The name of the context to describe.
        :returns: DescribeContextResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeDataQualityJobDefinition")
    def describe_data_quality_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> DescribeDataQualityJobDefinitionResponse:
        """Gets the details of a data quality monitoring job definition.

        :param job_definition_name: The name of the data quality monitoring job definition to describe.
        :returns: DescribeDataQualityJobDefinitionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeDevice")
    def describe_device(
        self,
        context: RequestContext,
        device_name: EntityName,
        device_fleet_name: EntityName,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> DescribeDeviceResponse:
        """Describes the device.

        :param device_name: The unique ID of the device.
        :param device_fleet_name: The name of the fleet the devices belong to.
        :param next_token: Next token of device description.
        :returns: DescribeDeviceResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeDeviceFleet")
    def describe_device_fleet(
        self, context: RequestContext, device_fleet_name: EntityName, **kwargs
    ) -> DescribeDeviceFleetResponse:
        """A description of the fleet the device belongs to.

        :param device_fleet_name: The name of the fleet.
        :returns: DescribeDeviceFleetResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeDomain")
    def describe_domain(
        self, context: RequestContext, domain_id: DomainId, **kwargs
    ) -> DescribeDomainResponse:
        """The description of the domain.

        :param domain_id: The domain ID.
        :returns: DescribeDomainResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeEdgeDeploymentPlan")
    def describe_edge_deployment_plan(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        next_token: NextToken | None = None,
        max_results: DeploymentStageMaxResults | None = None,
        **kwargs,
    ) -> DescribeEdgeDeploymentPlanResponse:
        """Describes an edge deployment plan with deployment status per stage.

        :param edge_deployment_plan_name: The name of the deployment plan to describe.
        :param next_token: If the edge deployment plan has enough stages to require tokening, then
        this is the response from the last list of stages returned.
        :param max_results: The maximum number of results to select (50 by default).
        :returns: DescribeEdgeDeploymentPlanResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeEdgePackagingJob")
    def describe_edge_packaging_job(
        self, context: RequestContext, edge_packaging_job_name: EntityName, **kwargs
    ) -> DescribeEdgePackagingJobResponse:
        """A description of edge packaging jobs.

        :param edge_packaging_job_name: The name of the edge packaging job.
        :returns: DescribeEdgePackagingJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeEndpoint")
    def describe_endpoint(
        self, context: RequestContext, endpoint_name: EndpointName, **kwargs
    ) -> DescribeEndpointOutput:
        """Returns the description of an endpoint.

        :param endpoint_name: The name of the endpoint.
        :returns: DescribeEndpointOutput
        """
        raise NotImplementedError

    @handler("DescribeEndpointConfig")
    def describe_endpoint_config(
        self, context: RequestContext, endpoint_config_name: EndpointConfigName, **kwargs
    ) -> DescribeEndpointConfigOutput:
        """Returns the description of an endpoint configuration created using the
        ``CreateEndpointConfig`` API.

        :param endpoint_config_name: The name of the endpoint configuration.
        :returns: DescribeEndpointConfigOutput
        """
        raise NotImplementedError

    @handler("DescribeExperiment")
    def describe_experiment(
        self, context: RequestContext, experiment_name: ExperimentEntityName, **kwargs
    ) -> DescribeExperimentResponse:
        """Provides a list of an experiment's properties.

        :param experiment_name: The name of the experiment to describe.
        :returns: DescribeExperimentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeFeatureGroup")
    def describe_feature_group(
        self,
        context: RequestContext,
        feature_group_name: FeatureGroupNameOrArn,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> DescribeFeatureGroupResponse:
        """Use this operation to describe a ``FeatureGroup``. The response includes
        information on the creation time, ``FeatureGroup`` name, the unique
        identifier for each ``FeatureGroup``, and more.

        :param feature_group_name: The name or Amazon Resource Name (ARN) of the ``FeatureGroup`` you want
        described.
        :param next_token: A token to resume pagination of the list of ``Features``
        (``FeatureDefinitions``).
        :returns: DescribeFeatureGroupResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeFeatureMetadata")
    def describe_feature_metadata(
        self,
        context: RequestContext,
        feature_group_name: FeatureGroupNameOrArn,
        feature_name: FeatureName,
        **kwargs,
    ) -> DescribeFeatureMetadataResponse:
        """Shows the metadata for a feature within a feature group.

        :param feature_group_name: The name or Amazon Resource Name (ARN) of the feature group containing
        the feature.
        :param feature_name: The name of the feature.
        :returns: DescribeFeatureMetadataResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeFlowDefinition")
    def describe_flow_definition(
        self, context: RequestContext, flow_definition_name: FlowDefinitionName, **kwargs
    ) -> DescribeFlowDefinitionResponse:
        """Returns information about the specified flow definition.

        :param flow_definition_name: The name of the flow definition.
        :returns: DescribeFlowDefinitionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeHub")
    def describe_hub(
        self, context: RequestContext, hub_name: HubNameOrArn, **kwargs
    ) -> DescribeHubResponse:
        """Describes a hub.

        :param hub_name: The name of the hub to describe.
        :returns: DescribeHubResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeHubContent")
    def describe_hub_content(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_type: HubContentType,
        hub_content_name: HubContentName,
        hub_content_version: HubContentVersion | None = None,
        **kwargs,
    ) -> DescribeHubContentResponse:
        """Describe the content of a hub.

        :param hub_name: The name of the hub that contains the content to describe.
        :param hub_content_type: The type of content in the hub.
        :param hub_content_name: The name of the content to describe.
        :param hub_content_version: The version of the content to describe.
        :returns: DescribeHubContentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeHumanTaskUi")
    def describe_human_task_ui(
        self, context: RequestContext, human_task_ui_name: HumanTaskUiName, **kwargs
    ) -> DescribeHumanTaskUiResponse:
        """Returns information about the requested human task user interface
        (worker task template).

        :param human_task_ui_name: The name of the human task user interface (worker task template) you
        want information about.
        :returns: DescribeHumanTaskUiResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeHyperParameterTuningJob")
    def describe_hyper_parameter_tuning_job(
        self,
        context: RequestContext,
        hyper_parameter_tuning_job_name: HyperParameterTuningJobName,
        **kwargs,
    ) -> DescribeHyperParameterTuningJobResponse:
        """Returns a description of a hyperparameter tuning job, depending on the
        fields selected. These fields can include the name, Amazon Resource Name
        (ARN), job status of your tuning job and more.

        :param hyper_parameter_tuning_job_name: The name of the tuning job.
        :returns: DescribeHyperParameterTuningJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeImage")
    def describe_image(
        self, context: RequestContext, image_name: ImageName, **kwargs
    ) -> DescribeImageResponse:
        """Describes a SageMaker AI image.

        :param image_name: The name of the image to describe.
        :returns: DescribeImageResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeImageVersion")
    def describe_image_version(
        self,
        context: RequestContext,
        image_name: ImageName,
        version: ImageVersionNumber | None = None,
        alias: SageMakerImageVersionAlias | None = None,
        **kwargs,
    ) -> DescribeImageVersionResponse:
        """Describes a version of a SageMaker AI image.

        :param image_name: The name of the image.
        :param version: The version of the image.
        :param alias: The alias of the image version.
        :returns: DescribeImageVersionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeInferenceComponent")
    def describe_inference_component(
        self, context: RequestContext, inference_component_name: InferenceComponentName, **kwargs
    ) -> DescribeInferenceComponentOutput:
        """Returns information about an inference component.

        :param inference_component_name: The name of the inference component.
        :returns: DescribeInferenceComponentOutput
        """
        raise NotImplementedError

    @handler("DescribeInferenceExperiment")
    def describe_inference_experiment(
        self, context: RequestContext, name: InferenceExperimentName, **kwargs
    ) -> DescribeInferenceExperimentResponse:
        """Returns details about an inference experiment.

        :param name: The name of the inference experiment to describe.
        :returns: DescribeInferenceExperimentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeInferenceRecommendationsJob")
    def describe_inference_recommendations_job(
        self, context: RequestContext, job_name: RecommendationJobName, **kwargs
    ) -> DescribeInferenceRecommendationsJobResponse:
        """Provides the results of the Inference Recommender job. One or more
        recommendation jobs are returned.

        :param job_name: The name of the job.
        :returns: DescribeInferenceRecommendationsJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeLabelingJob")
    def describe_labeling_job(
        self, context: RequestContext, labeling_job_name: LabelingJobName, **kwargs
    ) -> DescribeLabelingJobResponse:
        """Gets information about a labeling job.

        :param labeling_job_name: The name of the labeling job to return information for.
        :returns: DescribeLabelingJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeLineageGroup")
    def describe_lineage_group(
        self, context: RequestContext, lineage_group_name: ExperimentEntityName, **kwargs
    ) -> DescribeLineageGroupResponse:
        """Provides a list of properties for the requested lineage group. For more
        information, see `Cross-Account Lineage
        Tracking <https://docs.aws.amazon.com/sagemaker/latest/dg/xaccount-lineage-tracking.html>`__
        in the *Amazon SageMaker Developer Guide*.

        :param lineage_group_name: The name of the lineage group.
        :returns: DescribeLineageGroupResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeMlflowTrackingServer")
    def describe_mlflow_tracking_server(
        self, context: RequestContext, tracking_server_name: TrackingServerName, **kwargs
    ) -> DescribeMlflowTrackingServerResponse:
        """Returns information about an MLflow Tracking Server.

        :param tracking_server_name: The name of the MLflow Tracking Server to describe.
        :returns: DescribeMlflowTrackingServerResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeModel")
    def describe_model(
        self, context: RequestContext, model_name: ModelName, **kwargs
    ) -> DescribeModelOutput:
        """Describes a model that you created using the ``CreateModel`` API.

        :param model_name: The name of the model.
        :returns: DescribeModelOutput
        """
        raise NotImplementedError

    @handler("DescribeModelBiasJobDefinition")
    def describe_model_bias_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> DescribeModelBiasJobDefinitionResponse:
        """Returns a description of a model bias job definition.

        :param job_definition_name: The name of the model bias job definition.
        :returns: DescribeModelBiasJobDefinitionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeModelCard")
    def describe_model_card(
        self,
        context: RequestContext,
        model_card_name: ModelCardNameOrArn,
        model_card_version: Integer | None = None,
        **kwargs,
    ) -> DescribeModelCardResponse:
        """Describes the content, creation time, and security configuration of an
        Amazon SageMaker Model Card.

        :param model_card_name: The name or Amazon Resource Name (ARN) of the model card to describe.
        :param model_card_version: The version of the model card to describe.
        :returns: DescribeModelCardResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeModelCardExportJob")
    def describe_model_card_export_job(
        self, context: RequestContext, model_card_export_job_arn: ModelCardExportJobArn, **kwargs
    ) -> DescribeModelCardExportJobResponse:
        """Describes an Amazon SageMaker Model Card export job.

        :param model_card_export_job_arn: The Amazon Resource Name (ARN) of the model card export job to describe.
        :returns: DescribeModelCardExportJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeModelExplainabilityJobDefinition")
    def describe_model_explainability_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> DescribeModelExplainabilityJobDefinitionResponse:
        """Returns a description of a model explainability job definition.

        :param job_definition_name: The name of the model explainability job definition.
        :returns: DescribeModelExplainabilityJobDefinitionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeModelPackage")
    def describe_model_package(
        self, context: RequestContext, model_package_name: VersionedArnOrName, **kwargs
    ) -> DescribeModelPackageOutput:
        """Returns a description of the specified model package, which is used to
        create SageMaker models or list them on Amazon Web Services Marketplace.

        If you provided a KMS Key ID when you created your model package, you
        will see the `KMS
        Decrypt <https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html>`__
        API call in your CloudTrail logs when you use this API.

        To create models in SageMaker, buyers can subscribe to model packages
        listed on Amazon Web Services Marketplace.

        :param model_package_name: The name or Amazon Resource Name (ARN) of the model package to describe.
        :returns: DescribeModelPackageOutput
        """
        raise NotImplementedError

    @handler("DescribeModelPackageGroup")
    def describe_model_package_group(
        self, context: RequestContext, model_package_group_name: ArnOrName, **kwargs
    ) -> DescribeModelPackageGroupOutput:
        """Gets a description for the specified model group.

        :param model_package_group_name: The name of the model group to describe.
        :returns: DescribeModelPackageGroupOutput
        """
        raise NotImplementedError

    @handler("DescribeModelQualityJobDefinition")
    def describe_model_quality_job_definition(
        self, context: RequestContext, job_definition_name: MonitoringJobDefinitionName, **kwargs
    ) -> DescribeModelQualityJobDefinitionResponse:
        """Returns a description of a model quality job definition.

        :param job_definition_name: The name of the model quality job.
        :returns: DescribeModelQualityJobDefinitionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeMonitoringSchedule")
    def describe_monitoring_schedule(
        self, context: RequestContext, monitoring_schedule_name: MonitoringScheduleName, **kwargs
    ) -> DescribeMonitoringScheduleResponse:
        """Describes the schedule for a monitoring job.

        :param monitoring_schedule_name: Name of a previously created monitoring schedule.
        :returns: DescribeMonitoringScheduleResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeNotebookInstance")
    def describe_notebook_instance(
        self, context: RequestContext, notebook_instance_name: NotebookInstanceName, **kwargs
    ) -> DescribeNotebookInstanceOutput:
        """Returns information about a notebook instance.

        :param notebook_instance_name: The name of the notebook instance that you want information about.
        :returns: DescribeNotebookInstanceOutput
        """
        raise NotImplementedError

    @handler("DescribeNotebookInstanceLifecycleConfig")
    def describe_notebook_instance_lifecycle_config(
        self,
        context: RequestContext,
        notebook_instance_lifecycle_config_name: NotebookInstanceLifecycleConfigName,
        **kwargs,
    ) -> DescribeNotebookInstanceLifecycleConfigOutput:
        """Returns a description of a notebook instance lifecycle configuration.

        For information about notebook instance lifestyle configurations, see
        `Step 2.1: (Optional) Customize a Notebook
        Instance <https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html>`__.

        :param notebook_instance_lifecycle_config_name: The name of the lifecycle configuration to describe.
        :returns: DescribeNotebookInstanceLifecycleConfigOutput
        """
        raise NotImplementedError

    @handler("DescribeOptimizationJob")
    def describe_optimization_job(
        self, context: RequestContext, optimization_job_name: EntityName, **kwargs
    ) -> DescribeOptimizationJobResponse:
        """Provides the properties of the specified optimization job.

        :param optimization_job_name: The name that you assigned to the optimization job.
        :returns: DescribeOptimizationJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribePartnerApp")
    def describe_partner_app(
        self, context: RequestContext, arn: PartnerAppArn, **kwargs
    ) -> DescribePartnerAppResponse:
        """Gets information about a SageMaker Partner AI App.

        :param arn: The ARN of the SageMaker Partner AI App to describe.
        :returns: DescribePartnerAppResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribePipeline")
    def describe_pipeline(
        self, context: RequestContext, pipeline_name: PipelineNameOrArn, **kwargs
    ) -> DescribePipelineResponse:
        """Describes the details of a pipeline.

        :param pipeline_name: The name or Amazon Resource Name (ARN) of the pipeline to describe.
        :returns: DescribePipelineResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribePipelineDefinitionForExecution")
    def describe_pipeline_definition_for_execution(
        self, context: RequestContext, pipeline_execution_arn: PipelineExecutionArn, **kwargs
    ) -> DescribePipelineDefinitionForExecutionResponse:
        """Describes the details of an execution's pipeline definition.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :returns: DescribePipelineDefinitionForExecutionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribePipelineExecution")
    def describe_pipeline_execution(
        self, context: RequestContext, pipeline_execution_arn: PipelineExecutionArn, **kwargs
    ) -> DescribePipelineExecutionResponse:
        """Describes the details of a pipeline execution.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :returns: DescribePipelineExecutionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeProcessingJob")
    def describe_processing_job(
        self, context: RequestContext, processing_job_name: ProcessingJobName, **kwargs
    ) -> DescribeProcessingJobResponse:
        """Returns a description of a processing job.

        :param processing_job_name: The name of the processing job.
        :returns: DescribeProcessingJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeProject")
    def describe_project(
        self, context: RequestContext, project_name: ProjectEntityName, **kwargs
    ) -> DescribeProjectOutput:
        """Describes the details of a project.

        :param project_name: The name of the project to describe.
        :returns: DescribeProjectOutput
        """
        raise NotImplementedError

    @handler("DescribeSpace")
    def describe_space(
        self, context: RequestContext, domain_id: DomainId, space_name: SpaceName, **kwargs
    ) -> DescribeSpaceResponse:
        """Describes the space.

        :param domain_id: The ID of the associated domain.
        :param space_name: The name of the space.
        :returns: DescribeSpaceResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeStudioLifecycleConfig")
    def describe_studio_lifecycle_config(
        self,
        context: RequestContext,
        studio_lifecycle_config_name: StudioLifecycleConfigName,
        **kwargs,
    ) -> DescribeStudioLifecycleConfigResponse:
        """Describes the Amazon SageMaker AI Studio Lifecycle Configuration.

        :param studio_lifecycle_config_name: The name of the Amazon SageMaker AI Studio Lifecycle Configuration to
        describe.
        :returns: DescribeStudioLifecycleConfigResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeSubscribedWorkteam")
    def describe_subscribed_workteam(
        self, context: RequestContext, workteam_arn: WorkteamArn, **kwargs
    ) -> DescribeSubscribedWorkteamResponse:
        """Gets information about a work team provided by a vendor. It returns
        details about the subscription with a vendor in the Amazon Web Services
        Marketplace.

        :param workteam_arn: The Amazon Resource Name (ARN) of the subscribed work team to describe.
        :returns: DescribeSubscribedWorkteamResponse
        """
        raise NotImplementedError

    @handler("DescribeTrainingJob")
    def describe_training_job(
        self, context: RequestContext, training_job_name: TrainingJobName, **kwargs
    ) -> DescribeTrainingJobResponse:
        """Returns information about a training job.

        Some of the attributes below only appear if the training job
        successfully starts. If the training job fails, ``TrainingJobStatus`` is
        ``Failed`` and, depending on the ``FailureReason``, attributes like
        ``TrainingStartTime``, ``TrainingTimeInSeconds``, ``TrainingEndTime``,
        and ``BillableTimeInSeconds`` may not be present in the response.

        :param training_job_name: The name of the training job.
        :returns: DescribeTrainingJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeTrainingPlan")
    def describe_training_plan(
        self, context: RequestContext, training_plan_name: TrainingPlanName, **kwargs
    ) -> DescribeTrainingPlanResponse:
        """Retrieves detailed information about a specific training plan.

        :param training_plan_name: The name of the training plan to describe.
        :returns: DescribeTrainingPlanResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeTransformJob")
    def describe_transform_job(
        self, context: RequestContext, transform_job_name: TransformJobName, **kwargs
    ) -> DescribeTransformJobResponse:
        """Returns information about a transform job.

        :param transform_job_name: The name of the transform job that you want to view details of.
        :returns: DescribeTransformJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeTrial")
    def describe_trial(
        self, context: RequestContext, trial_name: ExperimentEntityName, **kwargs
    ) -> DescribeTrialResponse:
        """Provides a list of a trial's properties.

        :param trial_name: The name of the trial to describe.
        :returns: DescribeTrialResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeTrialComponent")
    def describe_trial_component(
        self, context: RequestContext, trial_component_name: ExperimentEntityNameOrArn, **kwargs
    ) -> DescribeTrialComponentResponse:
        """Provides a list of a trials component's properties.

        :param trial_component_name: The name of the trial component to describe.
        :returns: DescribeTrialComponentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("DescribeUserProfile")
    def describe_user_profile(
        self,
        context: RequestContext,
        domain_id: DomainId,
        user_profile_name: UserProfileName,
        **kwargs,
    ) -> DescribeUserProfileResponse:
        """Describes a user profile. For more information, see
        ``CreateUserProfile``.

        :param domain_id: The domain ID.
        :param user_profile_name: The user profile name.
        :returns: DescribeUserProfileResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("DescribeWorkforce")
    def describe_workforce(
        self, context: RequestContext, workforce_name: WorkforceName, **kwargs
    ) -> DescribeWorkforceResponse:
        """Lists private workforce information, including workforce name, Amazon
        Resource Name (ARN), and, if applicable, allowed IP address ranges
        (`CIDRs <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__).
        Allowable IP address ranges are the IP addresses that workers can use to
        access tasks.

        This operation applies only to private workforces.

        :param workforce_name: The name of the private workforce whose access you want to restrict.
        :returns: DescribeWorkforceResponse
        """
        raise NotImplementedError

    @handler("DescribeWorkteam")
    def describe_workteam(
        self, context: RequestContext, workteam_name: WorkteamName, **kwargs
    ) -> DescribeWorkteamResponse:
        """Gets information about a specific work team. You can see information
        such as the creation date, the last updated date, membership
        information, and the work team's Amazon Resource Name (ARN).

        :param workteam_name: The name of the work team to return a description of.
        :returns: DescribeWorkteamResponse
        """
        raise NotImplementedError

    @handler("DisableSagemakerServicecatalogPortfolio")
    def disable_sagemaker_servicecatalog_portfolio(
        self, context: RequestContext, **kwargs
    ) -> DisableSagemakerServicecatalogPortfolioOutput:
        """Disables using Service Catalog in SageMaker. Service Catalog is used to
        create SageMaker projects.

        :returns: DisableSagemakerServicecatalogPortfolioOutput
        """
        raise NotImplementedError

    @handler("DisassociateTrialComponent")
    def disassociate_trial_component(
        self,
        context: RequestContext,
        trial_component_name: ExperimentEntityName,
        trial_name: ExperimentEntityName,
        **kwargs,
    ) -> DisassociateTrialComponentResponse:
        """Disassociates a trial component from a trial. This doesn't effect other
        trials the component is associated with. Before you can delete a
        component, you must disassociate the component from all trials it is
        associated with. To associate a trial component with a trial, call the
        `AssociateTrialComponent <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AssociateTrialComponent.html>`__
        API.

        To get a list of the trials a component is associated with, use the
        `Search <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html>`__
        API. Specify ``ExperimentTrialComponent`` for the ``Resource``
        parameter. The list appears in the response under
        ``Results.TrialComponent.Parents``.

        :param trial_component_name: The name of the component to disassociate from the trial.
        :param trial_name: The name of the trial to disassociate from.
        :returns: DisassociateTrialComponentResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("EnableSagemakerServicecatalogPortfolio")
    def enable_sagemaker_servicecatalog_portfolio(
        self, context: RequestContext, **kwargs
    ) -> EnableSagemakerServicecatalogPortfolioOutput:
        """Enables using Service Catalog in SageMaker. Service Catalog is used to
        create SageMaker projects.

        :returns: EnableSagemakerServicecatalogPortfolioOutput
        """
        raise NotImplementedError

    @handler("GetDeviceFleetReport")
    def get_device_fleet_report(
        self, context: RequestContext, device_fleet_name: EntityName, **kwargs
    ) -> GetDeviceFleetReportResponse:
        """Describes a fleet.

        :param device_fleet_name: The name of the fleet.
        :returns: GetDeviceFleetReportResponse
        """
        raise NotImplementedError

    @handler("GetLineageGroupPolicy")
    def get_lineage_group_policy(
        self, context: RequestContext, lineage_group_name: LineageGroupNameOrArn, **kwargs
    ) -> GetLineageGroupPolicyResponse:
        """The resource policy for the lineage group.

        :param lineage_group_name: The name or Amazon Resource Name (ARN) of the lineage group.
        :returns: GetLineageGroupPolicyResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("GetModelPackageGroupPolicy")
    def get_model_package_group_policy(
        self, context: RequestContext, model_package_group_name: EntityName, **kwargs
    ) -> GetModelPackageGroupPolicyOutput:
        """Gets a resource policy that manages access for a model group. For
        information about resource policies, see `Identity-based policies and
        resource-based
        policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html>`__
        in the *Amazon Web Services Identity and Access Management User Guide.*.

        :param model_package_group_name: The name of the model group for which to get the resource policy.
        :returns: GetModelPackageGroupPolicyOutput
        """
        raise NotImplementedError

    @handler("GetSagemakerServicecatalogPortfolioStatus")
    def get_sagemaker_servicecatalog_portfolio_status(
        self, context: RequestContext, **kwargs
    ) -> GetSagemakerServicecatalogPortfolioStatusOutput:
        """Gets the status of Service Catalog in SageMaker. Service Catalog is used
        to create SageMaker projects.

        :returns: GetSagemakerServicecatalogPortfolioStatusOutput
        """
        raise NotImplementedError

    @handler("GetScalingConfigurationRecommendation")
    def get_scaling_configuration_recommendation(
        self,
        context: RequestContext,
        inference_recommendations_job_name: RecommendationJobName,
        recommendation_id: String | None = None,
        endpoint_name: EndpointName | None = None,
        target_cpu_utilization_per_core: UtilizationPercentagePerCore | None = None,
        scaling_policy_objective: ScalingPolicyObjective | None = None,
        **kwargs,
    ) -> GetScalingConfigurationRecommendationResponse:
        """Starts an Amazon SageMaker Inference Recommender autoscaling
        recommendation job. Returns recommendations for autoscaling policies
        that you can apply to your SageMaker endpoint.

        :param inference_recommendations_job_name: The name of a previously completed Inference Recommender job.
        :param recommendation_id: The recommendation ID of a previously completed inference
        recommendation.
        :param endpoint_name: The name of an endpoint benchmarked during a previously completed
        inference recommendation job.
        :param target_cpu_utilization_per_core: The percentage of how much utilization you want an instance to use
        before autoscaling.
        :param scaling_policy_objective: An object where you specify the anticipated traffic pattern for an
        endpoint.
        :returns: GetScalingConfigurationRecommendationResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("GetSearchSuggestions")
    def get_search_suggestions(
        self,
        context: RequestContext,
        resource: ResourceType,
        suggestion_query: SuggestionQuery | None = None,
        **kwargs,
    ) -> GetSearchSuggestionsResponse:
        """An auto-complete API for the search functionality in the SageMaker
        console. It returns suggestions of possible matches for the property
        name to use in ``Search`` queries. Provides suggestions for
        ``HyperParameters``, ``Tags``, and ``Metrics``.

        :param resource: The name of the SageMaker resource to search for.
        :param suggestion_query: Limits the property names that are included in the response.
        :returns: GetSearchSuggestionsResponse
        """
        raise NotImplementedError

    @handler("ImportHubContent")
    def import_hub_content(
        self,
        context: RequestContext,
        hub_content_name: HubContentName,
        hub_content_type: HubContentType,
        document_schema_version: DocumentSchemaVersion,
        hub_name: HubNameOrArn,
        hub_content_document: HubContentDocument,
        hub_content_version: HubContentVersion | None = None,
        hub_content_display_name: HubContentDisplayName | None = None,
        hub_content_description: HubContentDescription | None = None,
        hub_content_markdown: HubContentMarkdown | None = None,
        support_status: HubContentSupportStatus | None = None,
        hub_content_search_keywords: HubContentSearchKeywordList | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> ImportHubContentResponse:
        """Import hub content.

        :param hub_content_name: The name of the hub content to import.
        :param hub_content_type: The type of hub content to import.
        :param document_schema_version: The version of the hub content schema to import.
        :param hub_name: The name of the hub to import content into.
        :param hub_content_document: The hub content document that describes information about the hub
        content such as type, associated containers, scripts, and more.
        :param hub_content_version: The version of the hub content to import.
        :param hub_content_display_name: The display name of the hub content to import.
        :param hub_content_description: A description of the hub content to import.
        :param hub_content_markdown: A string that provides a description of the hub content.
        :param support_status: The status of the hub content resource.
        :param hub_content_search_keywords: The searchable keywords of the hub content.
        :param tags: Any tags associated with the hub content.
        :returns: ImportHubContentResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("ListActions")
    def list_actions(
        self,
        context: RequestContext,
        source_uri: SourceUri | None = None,
        action_type: String256 | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortActionsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListActionsResponse:
        """Lists the actions in your account and their properties.

        :param source_uri: A filter that returns only actions with the specified source URI.
        :param action_type: A filter that returns only actions of the specified type.
        :param created_after: A filter that returns only actions created on or after the specified
        time.
        :param created_before: A filter that returns only actions created on or before the specified
        time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param next_token: If the previous call to ``ListActions`` didn't return the full set of
        actions, the call returns a token for getting the next set of actions.
        :param max_results: The maximum number of actions to return in the response.
        :returns: ListActionsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListAlgorithms")
    def list_algorithms(
        self,
        context: RequestContext,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        next_token: NextToken | None = None,
        sort_by: AlgorithmSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListAlgorithmsOutput:
        """Lists the machine learning algorithms that have been created.

        :param creation_time_after: A filter that returns only algorithms created after the specified time
        (timestamp).
        :param creation_time_before: A filter that returns only algorithms created before the specified time
        (timestamp).
        :param max_results: The maximum number of algorithms to return in the response.
        :param name_contains: A string in the algorithm name.
        :param next_token: If the response to a previous ``ListAlgorithms`` request was truncated,
        the response includes a ``NextToken``.
        :param sort_by: The parameter by which to sort the results.
        :param sort_order: The sort order for the results.
        :returns: ListAlgorithmsOutput
        """
        raise NotImplementedError

    @handler("ListAliases")
    def list_aliases(
        self,
        context: RequestContext,
        image_name: ImageName,
        alias: SageMakerImageVersionAlias | None = None,
        version: ImageVersionNumber | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListAliasesResponse:
        """Lists the aliases of a specified image or image version.

        :param image_name: The name of the image.
        :param alias: The alias of the image version.
        :param version: The version of the image.
        :param max_results: The maximum number of aliases to return.
        :param next_token: If the previous call to ``ListAliases`` didn't return the full set of
        aliases, the call returns a token for retrieving the next set of
        aliases.
        :returns: ListAliasesResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListAppImageConfigs")
    def list_app_image_configs(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        name_contains: AppImageConfigName | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        modified_time_before: Timestamp | None = None,
        modified_time_after: Timestamp | None = None,
        sort_by: AppImageConfigSortKey | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListAppImageConfigsResponse:
        """Lists the AppImageConfigs in your account and their properties. The list
        can be filtered by creation time or modified time, and whether the
        AppImageConfig name contains a specified string.

        :param max_results: The total number of items to return in the response.
        :param next_token: If the previous call to ``ListImages`` didn't return the full set of
        AppImageConfigs, the call returns a token for getting the next set of
        AppImageConfigs.
        :param name_contains: A filter that returns only AppImageConfigs whose name contains the
        specified string.
        :param creation_time_before: A filter that returns only AppImageConfigs created on or before the
        specified time.
        :param creation_time_after: A filter that returns only AppImageConfigs created on or after the
        specified time.
        :param modified_time_before: A filter that returns only AppImageConfigs modified on or before the
        specified time.
        :param modified_time_after: A filter that returns only AppImageConfigs modified on or after the
        specified time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :returns: ListAppImageConfigsResponse
        """
        raise NotImplementedError

    @handler("ListApps")
    def list_apps(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_order: SortOrder | None = None,
        sort_by: AppSortKey | None = None,
        domain_id_equals: DomainId | None = None,
        user_profile_name_equals: UserProfileName | None = None,
        space_name_equals: SpaceName | None = None,
        **kwargs,
    ) -> ListAppsResponse:
        """Lists apps.

        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: This parameter defines the maximum number of results that can be return
        in a single response.
        :param sort_order: The sort order for the results.
        :param sort_by: The parameter by which to sort the results.
        :param domain_id_equals: A parameter to search for the domain ID.
        :param user_profile_name_equals: A parameter to search by user profile name.
        :param space_name_equals: A parameter to search by space name.
        :returns: ListAppsResponse
        """
        raise NotImplementedError

    @handler("ListArtifacts")
    def list_artifacts(
        self,
        context: RequestContext,
        source_uri: SourceUri | None = None,
        artifact_type: String256 | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortArtifactsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListArtifactsResponse:
        """Lists the artifacts in your account and their properties.

        :param source_uri: A filter that returns only artifacts with the specified source URI.
        :param artifact_type: A filter that returns only artifacts of the specified type.
        :param created_after: A filter that returns only artifacts created on or after the specified
        time.
        :param created_before: A filter that returns only artifacts created on or before the specified
        time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param next_token: If the previous call to ``ListArtifacts`` didn't return the full set of
        artifacts, the call returns a token for getting the next set of
        artifacts.
        :param max_results: The maximum number of artifacts to return in the response.
        :returns: ListArtifactsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListAssociations")
    def list_associations(
        self,
        context: RequestContext,
        source_arn: AssociationEntityArn | None = None,
        destination_arn: AssociationEntityArn | None = None,
        source_type: String256 | None = None,
        destination_type: String256 | None = None,
        association_type: AssociationEdgeType | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortAssociationsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListAssociationsResponse:
        """Lists the associations in your account and their properties.

        :param source_arn: A filter that returns only associations with the specified source ARN.
        :param destination_arn: A filter that returns only associations with the specified destination
        Amazon Resource Name (ARN).
        :param source_type: A filter that returns only associations with the specified source type.
        :param destination_type: A filter that returns only associations with the specified destination
        type.
        :param association_type: A filter that returns only associations of the specified type.
        :param created_after: A filter that returns only associations created on or after the
        specified time.
        :param created_before: A filter that returns only associations created on or before the
        specified time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param next_token: If the previous call to ``ListAssociations`` didn't return the full set
        of associations, the call returns a token for getting the next set of
        associations.
        :param max_results: The maximum number of associations to return in the response.
        :returns: ListAssociationsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListAutoMLJobs")
    def list_auto_ml_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: AutoMLNameContains | None = None,
        status_equals: AutoMLJobStatus | None = None,
        sort_order: AutoMLSortOrder | None = None,
        sort_by: AutoMLSortBy | None = None,
        max_results: AutoMLMaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListAutoMLJobsResponse:
        """Request a list of jobs.

        :param creation_time_after: Request a list of jobs, using a filter for time.
        :param creation_time_before: Request a list of jobs, using a filter for time.
        :param last_modified_time_after: Request a list of jobs, using a filter for time.
        :param last_modified_time_before: Request a list of jobs, using a filter for time.
        :param name_contains: Request a list of jobs, using a search filter for name.
        :param status_equals: Request a list of jobs, using a filter for status.
        :param sort_order: The sort order for the results.
        :param sort_by: The parameter by which to sort the results.
        :param max_results: Request a list of jobs up to a specified limit.
        :param next_token: If the previous response was truncated, you receive this token.
        :returns: ListAutoMLJobsResponse
        """
        raise NotImplementedError

    @handler("ListCandidatesForAutoMLJob")
    def list_candidates_for_auto_ml_job(
        self,
        context: RequestContext,
        auto_ml_job_name: AutoMLJobName,
        status_equals: CandidateStatus | None = None,
        candidate_name_equals: CandidateName | None = None,
        sort_order: AutoMLSortOrder | None = None,
        sort_by: CandidateSortBy | None = None,
        max_results: AutoMLMaxResultsForTrials | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListCandidatesForAutoMLJobResponse:
        """List the candidates created for the job.

        :param auto_ml_job_name: List the candidates created for the job by providing the job's name.
        :param status_equals: List the candidates for the job and filter by status.
        :param candidate_name_equals: List the candidates for the job and filter by candidate name.
        :param sort_order: The sort order for the results.
        :param sort_by: The parameter by which to sort the results.
        :param max_results: List the job's candidates up to a specified limit.
        :param next_token: If the previous response was truncated, you receive this token.
        :returns: ListCandidatesForAutoMLJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListClusterNodes")
    def list_cluster_nodes(
        self,
        context: RequestContext,
        cluster_name: ClusterNameOrArn,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        instance_group_name_contains: ClusterInstanceGroupName | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        sort_by: ClusterSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListClusterNodesResponse:
        """Retrieves the list of instances (also called *nodes* interchangeably) in
        a SageMaker HyperPod cluster.

        :param cluster_name: The string name or the Amazon Resource Name (ARN) of the SageMaker
        HyperPod cluster in which you want to retrieve the list of nodes.
        :param creation_time_after: A filter that returns nodes in a SageMaker HyperPod cluster created
        after the specified time.
        :param creation_time_before: A filter that returns nodes in a SageMaker HyperPod cluster created
        before the specified time.
        :param instance_group_name_contains: A filter that returns the instance groups whose name contain a specified
        string.
        :param max_results: The maximum number of nodes to return in the response.
        :param next_token: If the result of the previous ``ListClusterNodes`` request was
        truncated, the response includes a ``NextToken``.
        :param sort_by: The field by which to sort results.
        :param sort_order: The sort order for results.
        :returns: ListClusterNodesResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListClusterSchedulerConfigs")
    def list_cluster_scheduler_configs(
        self,
        context: RequestContext,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        name_contains: EntityName | None = None,
        cluster_arn: ClusterArn | None = None,
        status: SchedulerResourceStatus | None = None,
        sort_by: SortClusterSchedulerConfigBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListClusterSchedulerConfigsResponse:
        """List the cluster policy configurations.

        :param created_after: Filter for after this creation time.
        :param created_before: Filter for before this creation time.
        :param name_contains: Filter for name containing this string.
        :param cluster_arn: Filter for ARN of the cluster.
        :param status: Filter for status.
        :param sort_by: Filter for sorting the list by a given value.
        :param sort_order: The order of the list.
        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: The maximum number of cluster policies to list.
        :returns: ListClusterSchedulerConfigsResponse
        """
        raise NotImplementedError

    @handler("ListClusters")
    def list_clusters(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        next_token: NextToken | None = None,
        sort_by: ClusterSortBy | None = None,
        sort_order: SortOrder | None = None,
        training_plan_arn: TrainingPlanArn | None = None,
        **kwargs,
    ) -> ListClustersResponse:
        """Retrieves the list of SageMaker HyperPod clusters.

        :param creation_time_after: Set a start time for the time range during which you want to list
        SageMaker HyperPod clusters.
        :param creation_time_before: Set an end time for the time range during which you want to list
        SageMaker HyperPod clusters.
        :param max_results: Set the maximum number of SageMaker HyperPod clusters to list.
        :param name_contains: Set the maximum number of instances to print in the list.
        :param next_token: Set the next token to retrieve the list of SageMaker HyperPod clusters.
        :param sort_by: The field by which to sort results.
        :param sort_order: The sort order for results.
        :param training_plan_arn: The Amazon Resource Name (ARN); of the training plan to filter clusters
        by.
        :returns: ListClustersResponse
        """
        raise NotImplementedError

    @handler("ListCodeRepositories")
    def list_code_repositories(
        self,
        context: RequestContext,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        name_contains: CodeRepositoryNameContains | None = None,
        next_token: NextToken | None = None,
        sort_by: CodeRepositorySortBy | None = None,
        sort_order: CodeRepositorySortOrder | None = None,
        **kwargs,
    ) -> ListCodeRepositoriesOutput:
        """Gets a list of the Git repositories in your account.

        :param creation_time_after: A filter that returns only Git repositories that were created after the
        specified time.
        :param creation_time_before: A filter that returns only Git repositories that were created before the
        specified time.
        :param last_modified_time_after: A filter that returns only Git repositories that were last modified
        after the specified time.
        :param last_modified_time_before: A filter that returns only Git repositories that were last modified
        before the specified time.
        :param max_results: The maximum number of Git repositories to return in the response.
        :param name_contains: A string in the Git repositories name.
        :param next_token: If the result of a ``ListCodeRepositoriesOutput`` request was truncated,
        the response includes a ``NextToken``.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :returns: ListCodeRepositoriesOutput
        """
        raise NotImplementedError

    @handler("ListCompilationJobs")
    def list_compilation_jobs(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        last_modified_time_after: LastModifiedTime | None = None,
        last_modified_time_before: LastModifiedTime | None = None,
        name_contains: NameContains | None = None,
        status_equals: CompilationJobStatus | None = None,
        sort_by: ListCompilationJobsSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListCompilationJobsResponse:
        """Lists model compilation jobs that satisfy various filters.

        To create a model compilation job, use
        `CreateCompilationJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html>`__.
        To get information about a particular model compilation job you have
        created, use
        `DescribeCompilationJob <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html>`__.

        :param next_token: If the result of the previous ``ListCompilationJobs`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of model compilation jobs to return in the response.
        :param creation_time_after: A filter that returns the model compilation jobs that were created after
        a specified time.
        :param creation_time_before: A filter that returns the model compilation jobs that were created
        before a specified time.
        :param last_modified_time_after: A filter that returns the model compilation jobs that were modified
        after a specified time.
        :param last_modified_time_before: A filter that returns the model compilation jobs that were modified
        before a specified time.
        :param name_contains: A filter that returns the model compilation jobs whose name contains a
        specified string.
        :param status_equals: A filter that retrieves model compilation jobs with a specific
        ``CompilationJobStatus`` status.
        :param sort_by: The field by which to sort results.
        :param sort_order: The sort order for results.
        :returns: ListCompilationJobsResponse
        """
        raise NotImplementedError

    @handler("ListComputeQuotas")
    def list_compute_quotas(
        self,
        context: RequestContext,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        name_contains: EntityName | None = None,
        status: SchedulerResourceStatus | None = None,
        cluster_arn: ClusterArn | None = None,
        sort_by: SortQuotaBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListComputeQuotasResponse:
        """List the resource allocation definitions.

        :param created_after: Filter for after this creation time.
        :param created_before: Filter for before this creation time.
        :param name_contains: Filter for name containing this string.
        :param status: Filter for status.
        :param cluster_arn: Filter for ARN of the cluster.
        :param sort_by: Filter for sorting the list by a given value.
        :param sort_order: The order of the list.
        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: The maximum number of compute allocation definitions to list.
        :returns: ListComputeQuotasResponse
        """
        raise NotImplementedError

    @handler("ListContexts")
    def list_contexts(
        self,
        context: RequestContext,
        source_uri: SourceUri | None = None,
        context_type: String256 | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortContextsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListContextsResponse:
        """Lists the contexts in your account and their properties.

        :param source_uri: A filter that returns only contexts with the specified source URI.
        :param context_type: A filter that returns only contexts of the specified type.
        :param created_after: A filter that returns only contexts created on or after the specified
        time.
        :param created_before: A filter that returns only contexts created on or before the specified
        time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param next_token: If the previous call to ``ListContexts`` didn't return the full set of
        contexts, the call returns a token for getting the next set of contexts.
        :param max_results: The maximum number of contexts to return in the response.
        :returns: ListContextsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListDataQualityJobDefinitions")
    def list_data_quality_job_definitions(
        self,
        context: RequestContext,
        endpoint_name: EndpointName | None = None,
        sort_by: MonitoringJobDefinitionSortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        **kwargs,
    ) -> ListDataQualityJobDefinitionsResponse:
        """Lists the data quality job definitions in your account.

        :param endpoint_name: A filter that lists the data quality job definitions associated with the
        specified endpoint.
        :param sort_by: The field to sort results by.
        :param sort_order: Whether to sort the results in ``Ascending`` or ``Descending`` order.
        :param next_token: If the result of the previous ``ListDataQualityJobDefinitions`` request
        was truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of data quality monitoring job definitions to return
        in the response.
        :param name_contains: A string in the data quality monitoring job definition name.
        :param creation_time_before: A filter that returns only data quality monitoring job definitions
        created before the specified time.
        :param creation_time_after: A filter that returns only data quality monitoring job definitions
        created after the specified time.
        :returns: ListDataQualityJobDefinitionsResponse
        """
        raise NotImplementedError

    @handler("ListDeviceFleets")
    def list_device_fleets(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: ListMaxResults | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: NameContains | None = None,
        sort_by: ListDeviceFleetsSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListDeviceFleetsResponse:
        """Returns a list of devices in the fleet.

        :param next_token: The response from the last list when returning a list large enough to
        need tokening.
        :param max_results: The maximum number of results to select.
        :param creation_time_after: Filter fleets where packaging job was created after specified time.
        :param creation_time_before: Filter fleets where the edge packaging job was created before specified
        time.
        :param last_modified_time_after: Select fleets where the job was updated after X.
        :param last_modified_time_before: Select fleets where the job was updated before X.
        :param name_contains: Filter for fleets containing this name in their fleet device name.
        :param sort_by: The column to sort by.
        :param sort_order: What direction to sort in.
        :returns: ListDeviceFleetsResponse
        """
        raise NotImplementedError

    @handler("ListDevices")
    def list_devices(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: ListMaxResults | None = None,
        latest_heartbeat_after: Timestamp | None = None,
        model_name: EntityName | None = None,
        device_fleet_name: EntityName | None = None,
        **kwargs,
    ) -> ListDevicesResponse:
        """A list of devices.

        :param next_token: The response from the last list when returning a list large enough to
        need tokening.
        :param max_results: Maximum number of results to select.
        :param latest_heartbeat_after: Select fleets where the job was updated after X.
        :param model_name: A filter that searches devices that contains this name in any of their
        models.
        :param device_fleet_name: Filter for fleets containing this name in their device fleet name.
        :returns: ListDevicesResponse
        """
        raise NotImplementedError

    @handler("ListDomains")
    def list_domains(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListDomainsResponse:
        """Lists the domains.

        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: This parameter defines the maximum number of results that can be return
        in a single response.
        :returns: ListDomainsResponse
        """
        raise NotImplementedError

    @handler("ListEdgeDeploymentPlans")
    def list_edge_deployment_plans(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: ListMaxResults | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: NameContains | None = None,
        device_fleet_name_contains: NameContains | None = None,
        sort_by: ListEdgeDeploymentPlansSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListEdgeDeploymentPlansResponse:
        """Lists all edge deployment plans.

        :param next_token: The response from the last list when returning a list large enough to
        need tokening.
        :param max_results: The maximum number of results to select (50 by default).
        :param creation_time_after: Selects edge deployment plans created after this time.
        :param creation_time_before: Selects edge deployment plans created before this time.
        :param last_modified_time_after: Selects edge deployment plans that were last updated after this time.
        :param last_modified_time_before: Selects edge deployment plans that were last updated before this time.
        :param name_contains: Selects edge deployment plans with names containing this name.
        :param device_fleet_name_contains: Selects edge deployment plans with a device fleet name containing this
        name.
        :param sort_by: The column by which to sort the edge deployment plans.
        :param sort_order: The direction of the sorting (ascending or descending).
        :returns: ListEdgeDeploymentPlansResponse
        """
        raise NotImplementedError

    @handler("ListEdgePackagingJobs")
    def list_edge_packaging_jobs(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: ListMaxResults | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: NameContains | None = None,
        model_name_contains: NameContains | None = None,
        status_equals: EdgePackagingJobStatus | None = None,
        sort_by: ListEdgePackagingJobsSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListEdgePackagingJobsResponse:
        """Returns a list of edge packaging jobs.

        :param next_token: The response from the last list when returning a list large enough to
        need tokening.
        :param max_results: Maximum number of results to select.
        :param creation_time_after: Select jobs where the job was created after specified time.
        :param creation_time_before: Select jobs where the job was created before specified time.
        :param last_modified_time_after: Select jobs where the job was updated after specified time.
        :param last_modified_time_before: Select jobs where the job was updated before specified time.
        :param name_contains: Filter for jobs containing this name in their packaging job name.
        :param model_name_contains: Filter for jobs where the model name contains this string.
        :param status_equals: The job status to filter for.
        :param sort_by: Use to specify what column to sort by.
        :param sort_order: What direction to sort by.
        :returns: ListEdgePackagingJobsResponse
        """
        raise NotImplementedError

    @handler("ListEndpointConfigs")
    def list_endpoint_configs(
        self,
        context: RequestContext,
        sort_by: EndpointConfigSortKey | None = None,
        sort_order: OrderKey | None = None,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: EndpointConfigNameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        **kwargs,
    ) -> ListEndpointConfigsOutput:
        """Lists endpoint configurations.

        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param next_token: If the result of the previous ``ListEndpointConfig`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of training jobs to return in the response.
        :param name_contains: A string in the endpoint configuration name.
        :param creation_time_before: A filter that returns only endpoint configurations created before the
        specified time (timestamp).
        :param creation_time_after: A filter that returns only endpoint configurations with a creation time
        greater than or equal to the specified time (timestamp).
        :returns: ListEndpointConfigsOutput
        """
        raise NotImplementedError

    @handler("ListEndpoints")
    def list_endpoints(
        self,
        context: RequestContext,
        sort_by: EndpointSortKey | None = None,
        sort_order: OrderKey | None = None,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: EndpointNameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        status_equals: EndpointStatus | None = None,
        **kwargs,
    ) -> ListEndpointsOutput:
        """Lists endpoints.

        :param sort_by: Sorts the list of results.
        :param sort_order: The sort order for results.
        :param next_token: If the result of a ``ListEndpoints`` request was truncated, the response
        includes a ``NextToken``.
        :param max_results: The maximum number of endpoints to return in the response.
        :param name_contains: A string in endpoint names.
        :param creation_time_before: A filter that returns only endpoints that were created before the
        specified time (timestamp).
        :param creation_time_after: A filter that returns only endpoints with a creation time greater than
        or equal to the specified time (timestamp).
        :param last_modified_time_before: A filter that returns only endpoints that were modified before the
        specified timestamp.
        :param last_modified_time_after: A filter that returns only endpoints that were modified after the
        specified timestamp.
        :param status_equals: A filter that returns only endpoints with the specified status.
        :returns: ListEndpointsOutput
        """
        raise NotImplementedError

    @handler("ListExperiments")
    def list_experiments(
        self,
        context: RequestContext,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortExperimentsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListExperimentsResponse:
        """Lists all the experiments in your account. The list can be filtered to
        show only experiments that were created in a specific time range. The
        list can be sorted by experiment name or creation time.

        :param created_after: A filter that returns only experiments created after the specified time.
        :param created_before: A filter that returns only experiments created before the specified
        time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param next_token: If the previous call to ``ListExperiments`` didn't return the full set
        of experiments, the call returns a token for getting the next set of
        experiments.
        :param max_results: The maximum number of experiments to return in the response.
        :returns: ListExperimentsResponse
        """
        raise NotImplementedError

    @handler("ListFeatureGroups")
    def list_feature_groups(
        self,
        context: RequestContext,
        name_contains: FeatureGroupNameContains | None = None,
        feature_group_status_equals: FeatureGroupStatus | None = None,
        offline_store_status_equals: OfflineStoreStatusValue | None = None,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        sort_order: FeatureGroupSortOrder | None = None,
        sort_by: FeatureGroupSortBy | None = None,
        max_results: FeatureGroupMaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListFeatureGroupsResponse:
        """List ``FeatureGroup`` s based on given filter and order.

        :param name_contains: A string that partially matches one or more ``FeatureGroup`` s names.
        :param feature_group_status_equals: A ``FeatureGroup`` status.
        :param offline_store_status_equals: An ``OfflineStore`` status.
        :param creation_time_after: Use this parameter to search for ``FeatureGroups`` s created after a
        specific date and time.
        :param creation_time_before: Use this parameter to search for ``FeatureGroups`` s created before a
        specific date and time.
        :param sort_order: The order in which feature groups are listed.
        :param sort_by: The value on which the feature group list is sorted.
        :param max_results: The maximum number of results returned by ``ListFeatureGroups``.
        :param next_token: A token to resume pagination of ``ListFeatureGroups`` results.
        :returns: ListFeatureGroupsResponse
        """
        raise NotImplementedError

    @handler("ListFlowDefinitions")
    def list_flow_definitions(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListFlowDefinitionsResponse:
        """Returns information about the flow definitions in your account.

        :param creation_time_after: A filter that returns only flow definitions with a creation time greater
        than or equal to the specified timestamp.
        :param creation_time_before: A filter that returns only flow definitions that were created before the
        specified timestamp.
        :param sort_order: An optional value that specifies whether you want the results sorted in
        ``Ascending`` or ``Descending`` order.
        :param next_token: A token to resume pagination.
        :param max_results: The total number of items to return.
        :returns: ListFlowDefinitionsResponse
        """
        raise NotImplementedError

    @handler("ListHubContentVersions")
    def list_hub_content_versions(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_type: HubContentType,
        hub_content_name: HubContentName,
        min_version: HubContentVersion | None = None,
        max_schema_version: DocumentSchemaVersion | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        sort_by: HubContentSortBy | None = None,
        sort_order: SortOrder | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListHubContentVersionsResponse:
        """List hub content versions.

        :param hub_name: The name of the hub to list the content versions of.
        :param hub_content_type: The type of hub content to list versions of.
        :param hub_content_name: The name of the hub content.
        :param min_version: The lower bound of the hub content versions to list.
        :param max_schema_version: The upper bound of the hub content schema version.
        :param creation_time_before: Only list hub content versions that were created before the time
        specified.
        :param creation_time_after: Only list hub content versions that were created after the time
        specified.
        :param sort_by: Sort hub content versions by either name or creation time.
        :param sort_order: Sort hub content versions by ascending or descending order.
        :param max_results: The maximum number of hub content versions to list.
        :param next_token: If the response to a previous ``ListHubContentVersions`` request was
        truncated, the response includes a ``NextToken``.
        :returns: ListHubContentVersionsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListHubContents")
    def list_hub_contents(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_type: HubContentType,
        name_contains: NameContains | None = None,
        max_schema_version: DocumentSchemaVersion | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        sort_by: HubContentSortBy | None = None,
        sort_order: SortOrder | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListHubContentsResponse:
        """List the contents of a hub.

        :param hub_name: The name of the hub to list the contents of.
        :param hub_content_type: The type of hub content to list.
        :param name_contains: Only list hub content if the name contains the specified string.
        :param max_schema_version: The upper bound of the hub content schema verion.
        :param creation_time_before: Only list hub content that was created before the time specified.
        :param creation_time_after: Only list hub content that was created after the time specified.
        :param sort_by: Sort hub content versions by either name or creation time.
        :param sort_order: Sort hubs by ascending or descending order.
        :param max_results: The maximum amount of hub content to list.
        :param next_token: If the response to a previous ``ListHubContents`` request was truncated,
        the response includes a ``NextToken``.
        :returns: ListHubContentsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListHubs")
    def list_hubs(
        self,
        context: RequestContext,
        name_contains: NameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        sort_by: HubSortBy | None = None,
        sort_order: SortOrder | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListHubsResponse:
        """List all existing hubs.

        :param name_contains: Only list hubs with names that contain the specified string.
        :param creation_time_before: Only list hubs that were created before the time specified.
        :param creation_time_after: Only list hubs that were created after the time specified.
        :param last_modified_time_before: Only list hubs that were last modified before the time specified.
        :param last_modified_time_after: Only list hubs that were last modified after the time specified.
        :param sort_by: Sort hubs by either name or creation time.
        :param sort_order: Sort hubs by ascending or descending order.
        :param max_results: The maximum number of hubs to list.
        :param next_token: If the response to a previous ``ListHubs`` request was truncated, the
        response includes a ``NextToken``.
        :returns: ListHubsResponse
        """
        raise NotImplementedError

    @handler("ListHumanTaskUis")
    def list_human_task_uis(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListHumanTaskUisResponse:
        """Returns information about the human task user interfaces in your
        account.

        :param creation_time_after: A filter that returns only human task user interfaces with a creation
        time greater than or equal to the specified timestamp.
        :param creation_time_before: A filter that returns only human task user interfaces that were created
        before the specified timestamp.
        :param sort_order: An optional value that specifies whether you want the results sorted in
        ``Ascending`` or ``Descending`` order.
        :param next_token: A token to resume pagination.
        :param max_results: The total number of items to return.
        :returns: ListHumanTaskUisResponse
        """
        raise NotImplementedError

    @handler("ListHyperParameterTuningJobs")
    def list_hyper_parameter_tuning_jobs(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_by: HyperParameterTuningJobSortByOptions | None = None,
        sort_order: SortOrder | None = None,
        name_contains: NameContains | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        status_equals: HyperParameterTuningJobStatus | None = None,
        **kwargs,
    ) -> ListHyperParameterTuningJobsResponse:
        """Gets a list of
        `HyperParameterTuningJobSummary <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html>`__
        objects that describe the hyperparameter tuning jobs launched in your
        account.

        :param next_token: If the result of the previous ``ListHyperParameterTuningJobs`` request
        was truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of tuning jobs to return.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param name_contains: A string in the tuning job name.
        :param creation_time_after: A filter that returns only tuning jobs that were created after the
        specified time.
        :param creation_time_before: A filter that returns only tuning jobs that were created before the
        specified time.
        :param last_modified_time_after: A filter that returns only tuning jobs that were modified after the
        specified time.
        :param last_modified_time_before: A filter that returns only tuning jobs that were modified before the
        specified time.
        :param status_equals: A filter that returns only tuning jobs with the specified status.
        :returns: ListHyperParameterTuningJobsResponse
        """
        raise NotImplementedError

    @handler("ListImageVersions")
    def list_image_versions(
        self,
        context: RequestContext,
        image_name: ImageName,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        sort_by: ImageVersionSortBy | None = None,
        sort_order: ImageVersionSortOrder | None = None,
        **kwargs,
    ) -> ListImageVersionsResponse:
        """Lists the versions of a specified image and their properties. The list
        can be filtered by creation time or modified time.

        :param image_name: The name of the image to list the versions of.
        :param creation_time_after: A filter that returns only versions created on or after the specified
        time.
        :param creation_time_before: A filter that returns only versions created on or before the specified
        time.
        :param last_modified_time_after: A filter that returns only versions modified on or after the specified
        time.
        :param last_modified_time_before: A filter that returns only versions modified on or before the specified
        time.
        :param max_results: The maximum number of versions to return in the response.
        :param next_token: If the previous call to ``ListImageVersions`` didn't return the full set
        of versions, the call returns a token for getting the next set of
        versions.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :returns: ListImageVersionsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListImages")
    def list_images(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        name_contains: ImageNameContains | None = None,
        next_token: NextToken | None = None,
        sort_by: ImageSortBy | None = None,
        sort_order: ImageSortOrder | None = None,
        **kwargs,
    ) -> ListImagesResponse:
        """Lists the images in your account and their properties. The list can be
        filtered by creation time or modified time, and whether the image name
        contains a specified string.

        :param creation_time_after: A filter that returns only images created on or after the specified
        time.
        :param creation_time_before: A filter that returns only images created on or before the specified
        time.
        :param last_modified_time_after: A filter that returns only images modified on or after the specified
        time.
        :param last_modified_time_before: A filter that returns only images modified on or before the specified
        time.
        :param max_results: The maximum number of images to return in the response.
        :param name_contains: A filter that returns only images whose name contains the specified
        string.
        :param next_token: If the previous call to ``ListImages`` didn't return the full set of
        images, the call returns a token for getting the next set of images.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :returns: ListImagesResponse
        """
        raise NotImplementedError

    @handler("ListInferenceComponents")
    def list_inference_components(
        self,
        context: RequestContext,
        sort_by: InferenceComponentSortKey | None = None,
        sort_order: OrderKey | None = None,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: InferenceComponentNameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        status_equals: InferenceComponentStatus | None = None,
        endpoint_name_equals: EndpointName | None = None,
        variant_name_equals: VariantName | None = None,
        **kwargs,
    ) -> ListInferenceComponentsOutput:
        """Lists the inference components in your account and their properties.

        :param sort_by: The field by which to sort the inference components in the response.
        :param sort_order: The sort order for results.
        :param next_token: A token that you use to get the next set of results following a
        truncated response.
        :param max_results: The maximum number of inference components to return in the response.
        :param name_contains: Filters the results to only those inference components with a name that
        contains the specified string.
        :param creation_time_before: Filters the results to only those inference components that were created
        before the specified time.
        :param creation_time_after: Filters the results to only those inference components that were created
        after the specified time.
        :param last_modified_time_before: Filters the results to only those inference components that were updated
        before the specified time.
        :param last_modified_time_after: Filters the results to only those inference components that were updated
        after the specified time.
        :param status_equals: Filters the results to only those inference components with the
        specified status.
        :param endpoint_name_equals: An endpoint name to filter the listed inference components.
        :param variant_name_equals: A production variant name to filter the listed inference components.
        :returns: ListInferenceComponentsOutput
        """
        raise NotImplementedError

    @handler("ListInferenceExperiments", expand=False)
    def list_inference_experiments(
        self, context: RequestContext, request: ListInferenceExperimentsRequest, **kwargs
    ) -> ListInferenceExperimentsResponse:
        """Returns the list of all inference experiments.

        :param name_contains: Selects inference experiments whose names contain this name.
        :param type: Selects inference experiments of this type.
        :param status_equals: Selects inference experiments which are in this status.
        :param creation_time_after: Selects inference experiments which were created after this timestamp.
        :param creation_time_before: Selects inference experiments which were created before this timestamp.
        :param last_modified_time_after: Selects inference experiments which were last modified after this
        timestamp.
        :param last_modified_time_before: Selects inference experiments which were last modified before this
        timestamp.
        :param sort_by: The column by which to sort the listed inference experiments.
        :param sort_order: The direction of sorting (ascending or descending).
        :param next_token: The response from the last list when returning a list large enough to
        need tokening.
        :param max_results: The maximum number of results to select.
        :returns: ListInferenceExperimentsResponse
        """
        raise NotImplementedError

    @handler("ListInferenceRecommendationsJobSteps")
    def list_inference_recommendations_job_steps(
        self,
        context: RequestContext,
        job_name: RecommendationJobName,
        status: RecommendationJobStatus | None = None,
        step_type: RecommendationStepType | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListInferenceRecommendationsJobStepsResponse:
        """Returns a list of the subtasks for an Inference Recommender job.

        The supported subtasks are benchmarks, which evaluate the performance of
        your model on different instance types.

        :param job_name: The name for the Inference Recommender job.
        :param status: A filter to return benchmarks of a specified status.
        :param step_type: A filter to return details about the specified type of subtask.
        :param max_results: The maximum number of results to return.
        :param next_token: A token that you can specify to return more results from the list.
        :returns: ListInferenceRecommendationsJobStepsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListInferenceRecommendationsJobs")
    def list_inference_recommendations_jobs(
        self,
        context: RequestContext,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        last_modified_time_after: LastModifiedTime | None = None,
        last_modified_time_before: LastModifiedTime | None = None,
        name_contains: NameContains | None = None,
        status_equals: RecommendationJobStatus | None = None,
        sort_by: ListInferenceRecommendationsJobsSortBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        model_name_equals: ModelName | None = None,
        model_package_version_arn_equals: ModelPackageArn | None = None,
        **kwargs,
    ) -> ListInferenceRecommendationsJobsResponse:
        """Lists recommendation jobs that satisfy various filters.

        :param creation_time_after: A filter that returns only jobs created after the specified time
        (timestamp).
        :param creation_time_before: A filter that returns only jobs created before the specified time
        (timestamp).
        :param last_modified_time_after: A filter that returns only jobs that were last modified after the
        specified time (timestamp).
        :param last_modified_time_before: A filter that returns only jobs that were last modified before the
        specified time (timestamp).
        :param name_contains: A string in the job name.
        :param status_equals: A filter that retrieves only inference recommendations jobs with a
        specific status.
        :param sort_by: The parameter by which to sort the results.
        :param sort_order: The sort order for the results.
        :param next_token: If the response to a previous
        ``ListInferenceRecommendationsJobsRequest`` request was truncated, the
        response includes a ``NextToken``.
        :param max_results: The maximum number of recommendations to return in the response.
        :param model_name_equals: A filter that returns only jobs that were created for this model.
        :param model_package_version_arn_equals: A filter that returns only jobs that were created for this versioned
        model package.
        :returns: ListInferenceRecommendationsJobsResponse
        """
        raise NotImplementedError

    @handler("ListLabelingJobs")
    def list_labeling_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        name_contains: NameContains | None = None,
        sort_by: SortBy | None = None,
        sort_order: SortOrder | None = None,
        status_equals: LabelingJobStatus | None = None,
        **kwargs,
    ) -> ListLabelingJobsResponse:
        """Gets a list of labeling jobs.

        :param creation_time_after: A filter that returns only labeling jobs created after the specified
        time (timestamp).
        :param creation_time_before: A filter that returns only labeling jobs created before the specified
        time (timestamp).
        :param last_modified_time_after: A filter that returns only labeling jobs modified after the specified
        time (timestamp).
        :param last_modified_time_before: A filter that returns only labeling jobs modified before the specified
        time (timestamp).
        :param max_results: The maximum number of labeling jobs to return in each page of the
        response.
        :param next_token: If the result of the previous ``ListLabelingJobs`` request was
        truncated, the response includes a ``NextToken``.
        :param name_contains: A string in the labeling job name.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param status_equals: A filter that retrieves only labeling jobs with a specific status.
        :returns: ListLabelingJobsResponse
        """
        raise NotImplementedError

    @handler("ListLabelingJobsForWorkteam")
    def list_labeling_jobs_for_workteam(
        self,
        context: RequestContext,
        workteam_arn: WorkteamArn,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        job_reference_code_contains: JobReferenceCodeContains | None = None,
        sort_by: ListLabelingJobsForWorkteamSortByOptions | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListLabelingJobsForWorkteamResponse:
        """Gets a list of labeling jobs assigned to a specified work team.

        :param workteam_arn: The Amazon Resource Name (ARN) of the work team for which you want to
        see labeling jobs for.
        :param max_results: The maximum number of labeling jobs to return in each page of the
        response.
        :param next_token: If the result of the previous ``ListLabelingJobsForWorkteam`` request
        was truncated, the response includes a ``NextToken``.
        :param creation_time_after: A filter that returns only labeling jobs created after the specified
        time (timestamp).
        :param creation_time_before: A filter that returns only labeling jobs created before the specified
        time (timestamp).
        :param job_reference_code_contains: A filter the limits jobs to only the ones whose job reference code
        contains the specified string.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :returns: ListLabelingJobsForWorkteamResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListLineageGroups")
    def list_lineage_groups(
        self,
        context: RequestContext,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortLineageGroupsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListLineageGroupsResponse:
        """A list of lineage groups shared with your Amazon Web Services account.
        For more information, see `Cross-Account Lineage
        Tracking <https://docs.aws.amazon.com/sagemaker/latest/dg/xaccount-lineage-tracking.html>`__
        in the *Amazon SageMaker Developer Guide*.

        :param created_after: A timestamp to filter against lineage groups created after a certain
        point in time.
        :param created_before: A timestamp to filter against lineage groups created before a certain
        point in time.
        :param sort_by: The parameter by which to sort the results.
        :param sort_order: The sort order for the results.
        :param next_token: If the response is truncated, SageMaker returns this token.
        :param max_results: The maximum number of endpoints to return in the response.
        :returns: ListLineageGroupsResponse
        """
        raise NotImplementedError

    @handler("ListMlflowTrackingServers")
    def list_mlflow_tracking_servers(
        self,
        context: RequestContext,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        tracking_server_status: TrackingServerStatus | None = None,
        mlflow_version: MlflowVersion | None = None,
        sort_by: SortTrackingServerBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListMlflowTrackingServersResponse:
        """Lists all MLflow Tracking Servers.

        :param created_after: Use the ``CreatedAfter`` filter to only list tracking servers created
        after a specific date and time.
        :param created_before: Use the ``CreatedBefore`` filter to only list tracking servers created
        before a specific date and time.
        :param tracking_server_status: Filter for tracking servers with a specified creation status.
        :param mlflow_version: Filter for tracking servers using the specified MLflow version.
        :param sort_by: Filter for trackings servers sorting by name, creation time, or creation
        status.
        :param sort_order: Change the order of the listed tracking servers.
        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: The maximum number of tracking servers to list.
        :returns: ListMlflowTrackingServersResponse
        """
        raise NotImplementedError

    @handler("ListModelBiasJobDefinitions")
    def list_model_bias_job_definitions(
        self,
        context: RequestContext,
        endpoint_name: EndpointName | None = None,
        sort_by: MonitoringJobDefinitionSortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        **kwargs,
    ) -> ListModelBiasJobDefinitionsResponse:
        """Lists model bias jobs definitions that satisfy various filters.

        :param endpoint_name: Name of the endpoint to monitor for model bias.
        :param sort_by: Whether to sort results by the ``Name`` or ``CreationTime`` field.
        :param sort_order: Whether to sort the results in ``Ascending`` or ``Descending`` order.
        :param next_token: The token returned if the response is truncated.
        :param max_results: The maximum number of model bias jobs to return in the response.
        :param name_contains: Filter for model bias jobs whose name contains a specified string.
        :param creation_time_before: A filter that returns only model bias jobs created before a specified
        time.
        :param creation_time_after: A filter that returns only model bias jobs created after a specified
        time.
        :returns: ListModelBiasJobDefinitionsResponse
        """
        raise NotImplementedError

    @handler("ListModelCardExportJobs")
    def list_model_card_export_jobs(
        self,
        context: RequestContext,
        model_card_name: EntityName,
        model_card_version: Integer | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        model_card_export_job_name_contains: EntityName | None = None,
        status_equals: ModelCardExportJobStatus | None = None,
        sort_by: ModelCardExportJobSortBy | None = None,
        sort_order: ModelCardExportJobSortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListModelCardExportJobsResponse:
        """List the export jobs for the Amazon SageMaker Model Card.

        :param model_card_name: List export jobs for the model card with the specified name.
        :param model_card_version: List export jobs for the model card with the specified version.
        :param creation_time_after: Only list model card export jobs that were created after the time
        specified.
        :param creation_time_before: Only list model card export jobs that were created before the time
        specified.
        :param model_card_export_job_name_contains: Only list model card export jobs with names that contain the specified
        string.
        :param status_equals: Only list model card export jobs with the specified status.
        :param sort_by: Sort model card export jobs by either name or creation time.
        :param sort_order: Sort model card export jobs by ascending or descending order.
        :param next_token: If the response to a previous ``ListModelCardExportJobs`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of model card export jobs to list.
        :returns: ListModelCardExportJobsResponse
        """
        raise NotImplementedError

    @handler("ListModelCardVersions")
    def list_model_card_versions(
        self,
        context: RequestContext,
        model_card_name: ModelCardNameOrArn,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        model_card_status: ModelCardStatus | None = None,
        next_token: NextToken | None = None,
        sort_by: ModelCardVersionSortBy | None = None,
        sort_order: ModelCardSortOrder | None = None,
        **kwargs,
    ) -> ListModelCardVersionsResponse:
        """List existing versions of an Amazon SageMaker Model Card.

        :param model_card_name: List model card versions for the model card with the specified name or
        Amazon Resource Name (ARN).
        :param creation_time_after: Only list model card versions that were created after the time
        specified.
        :param creation_time_before: Only list model card versions that were created before the time
        specified.
        :param max_results: The maximum number of model card versions to list.
        :param model_card_status: Only list model card versions with the specified approval status.
        :param next_token: If the response to a previous ``ListModelCardVersions`` request was
        truncated, the response includes a ``NextToken``.
        :param sort_by: Sort listed model card versions by version.
        :param sort_order: Sort model card versions by ascending or descending order.
        :returns: ListModelCardVersionsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListModelCards")
    def list_model_cards(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        name_contains: EntityName | None = None,
        model_card_status: ModelCardStatus | None = None,
        next_token: NextToken | None = None,
        sort_by: ModelCardSortBy | None = None,
        sort_order: ModelCardSortOrder | None = None,
        **kwargs,
    ) -> ListModelCardsResponse:
        """List existing model cards.

        :param creation_time_after: Only list model cards that were created after the time specified.
        :param creation_time_before: Only list model cards that were created before the time specified.
        :param max_results: The maximum number of model cards to list.
        :param name_contains: Only list model cards with names that contain the specified string.
        :param model_card_status: Only list model cards with the specified approval status.
        :param next_token: If the response to a previous ``ListModelCards`` request was truncated,
        the response includes a ``NextToken``.
        :param sort_by: Sort model cards by either name or creation time.
        :param sort_order: Sort model cards by ascending or descending order.
        :returns: ListModelCardsResponse
        """
        raise NotImplementedError

    @handler("ListModelExplainabilityJobDefinitions")
    def list_model_explainability_job_definitions(
        self,
        context: RequestContext,
        endpoint_name: EndpointName | None = None,
        sort_by: MonitoringJobDefinitionSortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        **kwargs,
    ) -> ListModelExplainabilityJobDefinitionsResponse:
        """Lists model explainability job definitions that satisfy various filters.

        :param endpoint_name: Name of the endpoint to monitor for model explainability.
        :param sort_by: Whether to sort results by the ``Name`` or ``CreationTime`` field.
        :param sort_order: Whether to sort the results in ``Ascending`` or ``Descending`` order.
        :param next_token: The token returned if the response is truncated.
        :param max_results: The maximum number of jobs to return in the response.
        :param name_contains: Filter for model explainability jobs whose name contains a specified
        string.
        :param creation_time_before: A filter that returns only model explainability jobs created before a
        specified time.
        :param creation_time_after: A filter that returns only model explainability jobs created after a
        specified time.
        :returns: ListModelExplainabilityJobDefinitionsResponse
        """
        raise NotImplementedError

    @handler("ListModelMetadata")
    def list_model_metadata(
        self,
        context: RequestContext,
        search_expression: ModelMetadataSearchExpression | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListModelMetadataResponse:
        """Lists the domain, framework, task, and model name of standard machine
        learning models found in common model zoos.

        :param search_expression: One or more filters that searches for the specified resource or
        resources in a search.
        :param next_token: If the response to a previous ``ListModelMetadataResponse`` request was
        truncated, the response includes a NextToken.
        :param max_results: The maximum number of models to return in the response.
        :returns: ListModelMetadataResponse
        """
        raise NotImplementedError

    @handler("ListModelPackageGroups")
    def list_model_package_groups(
        self,
        context: RequestContext,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        next_token: NextToken | None = None,
        sort_by: ModelPackageGroupSortBy | None = None,
        sort_order: SortOrder | None = None,
        cross_account_filter_option: CrossAccountFilterOption | None = None,
        **kwargs,
    ) -> ListModelPackageGroupsOutput:
        """Gets a list of the model groups in your Amazon Web Services account.

        :param creation_time_after: A filter that returns only model groups created after the specified
        time.
        :param creation_time_before: A filter that returns only model groups created before the specified
        time.
        :param max_results: The maximum number of results to return in the response.
        :param name_contains: A string in the model group name.
        :param next_token: If the result of the previous ``ListModelPackageGroups`` request was
        truncated, the response includes a ``NextToken``.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param cross_account_filter_option: A filter that returns either model groups shared with you or model
        groups in your own account.
        :returns: ListModelPackageGroupsOutput
        """
        raise NotImplementedError

    @handler("ListModelPackages")
    def list_model_packages(
        self,
        context: RequestContext,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        model_approval_status: ModelApprovalStatus | None = None,
        model_package_group_name: ArnOrName | None = None,
        model_package_type: ModelPackageType | None = None,
        next_token: NextToken | None = None,
        sort_by: ModelPackageSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListModelPackagesOutput:
        """Lists the model packages that have been created.

        :param creation_time_after: A filter that returns only model packages created after the specified
        time (timestamp).
        :param creation_time_before: A filter that returns only model packages created before the specified
        time (timestamp).
        :param max_results: The maximum number of model packages to return in the response.
        :param name_contains: A string in the model package name.
        :param model_approval_status: A filter that returns only the model packages with the specified
        approval status.
        :param model_package_group_name: A filter that returns only model versions that belong to the specified
        model group.
        :param model_package_type: A filter that returns only the model packages of the specified type.
        :param next_token: If the response to a previous ``ListModelPackages`` request was
        truncated, the response includes a ``NextToken``.
        :param sort_by: The parameter by which to sort the results.
        :param sort_order: The sort order for the results.
        :returns: ListModelPackagesOutput
        """
        raise NotImplementedError

    @handler("ListModelQualityJobDefinitions")
    def list_model_quality_job_definitions(
        self,
        context: RequestContext,
        endpoint_name: EndpointName | None = None,
        sort_by: MonitoringJobDefinitionSortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        **kwargs,
    ) -> ListModelQualityJobDefinitionsResponse:
        """Gets a list of model quality monitoring job definitions in your account.

        :param endpoint_name: A filter that returns only model quality monitoring job definitions that
        are associated with the specified endpoint.
        :param sort_by: The field to sort results by.
        :param sort_order: Whether to sort the results in ``Ascending`` or ``Descending`` order.
        :param next_token: If the result of the previous ``ListModelQualityJobDefinitions`` request
        was truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of results to return in a call to
        ``ListModelQualityJobDefinitions``.
        :param name_contains: A string in the transform job name.
        :param creation_time_before: A filter that returns only model quality monitoring job definitions
        created before the specified time.
        :param creation_time_after: A filter that returns only model quality monitoring job definitions
        created after the specified time.
        :returns: ListModelQualityJobDefinitionsResponse
        """
        raise NotImplementedError

    @handler("ListModels")
    def list_models(
        self,
        context: RequestContext,
        sort_by: ModelSortKey | None = None,
        sort_order: OrderKey | None = None,
        next_token: PaginationToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: ModelNameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        **kwargs,
    ) -> ListModelsOutput:
        """Lists models created with the ``CreateModel`` API.

        :param sort_by: Sorts the list of results.
        :param sort_order: The sort order for results.
        :param next_token: If the response to a previous ``ListModels`` request was truncated, the
        response includes a ``NextToken``.
        :param max_results: The maximum number of models to return in the response.
        :param name_contains: A string in the model name.
        :param creation_time_before: A filter that returns only models created before the specified time
        (timestamp).
        :param creation_time_after: A filter that returns only models with a creation time greater than or
        equal to the specified time (timestamp).
        :returns: ListModelsOutput
        """
        raise NotImplementedError

    @handler("ListMonitoringAlertHistory")
    def list_monitoring_alert_history(
        self,
        context: RequestContext,
        monitoring_schedule_name: MonitoringScheduleName | None = None,
        monitoring_alert_name: MonitoringAlertName | None = None,
        sort_by: MonitoringAlertHistorySortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        status_equals: MonitoringAlertStatus | None = None,
        **kwargs,
    ) -> ListMonitoringAlertHistoryResponse:
        """Gets a list of past alerts in a model monitoring schedule.

        :param monitoring_schedule_name: The name of a monitoring schedule.
        :param monitoring_alert_name: The name of a monitoring alert.
        :param sort_by: The field used to sort results.
        :param sort_order: The sort order, whether ``Ascending`` or ``Descending``, of the alert
        history.
        :param next_token: If the result of the previous ``ListMonitoringAlertHistory`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of results to display.
        :param creation_time_before: A filter that returns only alerts created on or before the specified
        time.
        :param creation_time_after: A filter that returns only alerts created on or after the specified
        time.
        :param status_equals: A filter that retrieves only alerts with a specific status.
        :returns: ListMonitoringAlertHistoryResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListMonitoringAlerts")
    def list_monitoring_alerts(
        self,
        context: RequestContext,
        monitoring_schedule_name: MonitoringScheduleName,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListMonitoringAlertsResponse:
        """Gets the alerts for a single monitoring schedule.

        :param monitoring_schedule_name: The name of a monitoring schedule.
        :param next_token: If the result of the previous ``ListMonitoringAlerts`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of results to display.
        :returns: ListMonitoringAlertsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListMonitoringExecutions")
    def list_monitoring_executions(
        self,
        context: RequestContext,
        monitoring_schedule_name: MonitoringScheduleName | None = None,
        endpoint_name: EndpointName | None = None,
        sort_by: MonitoringExecutionSortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        scheduled_time_before: Timestamp | None = None,
        scheduled_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        status_equals: ExecutionStatus | None = None,
        monitoring_job_definition_name: MonitoringJobDefinitionName | None = None,
        monitoring_type_equals: MonitoringType | None = None,
        **kwargs,
    ) -> ListMonitoringExecutionsResponse:
        """Returns list of all monitoring job executions.

        :param monitoring_schedule_name: Name of a specific schedule to fetch jobs for.
        :param endpoint_name: Name of a specific endpoint to fetch jobs for.
        :param sort_by: Whether to sort the results by the ``Status``, ``CreationTime``, or
        ``ScheduledTime`` field.
        :param sort_order: Whether to sort the results in ``Ascending`` or ``Descending`` order.
        :param next_token: The token returned if the response is truncated.
        :param max_results: The maximum number of jobs to return in the response.
        :param scheduled_time_before: Filter for jobs scheduled before a specified time.
        :param scheduled_time_after: Filter for jobs scheduled after a specified time.
        :param creation_time_before: A filter that returns only jobs created before a specified time.
        :param creation_time_after: A filter that returns only jobs created after a specified time.
        :param last_modified_time_before: A filter that returns only jobs modified after a specified time.
        :param last_modified_time_after: A filter that returns only jobs modified before a specified time.
        :param status_equals: A filter that retrieves only jobs with a specific status.
        :param monitoring_job_definition_name: Gets a list of the monitoring job runs of the specified monitoring job
        definitions.
        :param monitoring_type_equals: A filter that returns only the monitoring job runs of the specified
        monitoring type.
        :returns: ListMonitoringExecutionsResponse
        """
        raise NotImplementedError

    @handler("ListMonitoringSchedules")
    def list_monitoring_schedules(
        self,
        context: RequestContext,
        endpoint_name: EndpointName | None = None,
        sort_by: MonitoringScheduleSortKey | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        name_contains: NameContains | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        status_equals: ScheduleStatus | None = None,
        monitoring_job_definition_name: MonitoringJobDefinitionName | None = None,
        monitoring_type_equals: MonitoringType | None = None,
        **kwargs,
    ) -> ListMonitoringSchedulesResponse:
        """Returns list of all monitoring schedules.

        :param endpoint_name: Name of a specific endpoint to fetch schedules for.
        :param sort_by: Whether to sort the results by the ``Status``, ``CreationTime``, or
        ``ScheduledTime`` field.
        :param sort_order: Whether to sort the results in ``Ascending`` or ``Descending`` order.
        :param next_token: The token returned if the response is truncated.
        :param max_results: The maximum number of jobs to return in the response.
        :param name_contains: Filter for monitoring schedules whose name contains a specified string.
        :param creation_time_before: A filter that returns only monitoring schedules created before a
        specified time.
        :param creation_time_after: A filter that returns only monitoring schedules created after a
        specified time.
        :param last_modified_time_before: A filter that returns only monitoring schedules modified before a
        specified time.
        :param last_modified_time_after: A filter that returns only monitoring schedules modified after a
        specified time.
        :param status_equals: A filter that returns only monitoring schedules modified before a
        specified time.
        :param monitoring_job_definition_name: Gets a list of the monitoring schedules for the specified monitoring job
        definition.
        :param monitoring_type_equals: A filter that returns only the monitoring schedules for the specified
        monitoring type.
        :returns: ListMonitoringSchedulesResponse
        """
        raise NotImplementedError

    @handler("ListNotebookInstanceLifecycleConfigs")
    def list_notebook_instance_lifecycle_configs(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_by: NotebookInstanceLifecycleConfigSortKey | None = None,
        sort_order: NotebookInstanceLifecycleConfigSortOrder | None = None,
        name_contains: NotebookInstanceLifecycleConfigNameContains | None = None,
        creation_time_before: CreationTime | None = None,
        creation_time_after: CreationTime | None = None,
        last_modified_time_before: LastModifiedTime | None = None,
        last_modified_time_after: LastModifiedTime | None = None,
        **kwargs,
    ) -> ListNotebookInstanceLifecycleConfigsOutput:
        """Lists notebook instance lifestyle configurations created with the
        `CreateNotebookInstanceLifecycleConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html>`__
        API.

        :param next_token: If the result of a ``ListNotebookInstanceLifecycleConfigs`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of lifecycle configurations to return in the
        response.
        :param sort_by: Sorts the list of results.
        :param sort_order: The sort order for results.
        :param name_contains: A string in the lifecycle configuration name.
        :param creation_time_before: A filter that returns only lifecycle configurations that were created
        before the specified time (timestamp).
        :param creation_time_after: A filter that returns only lifecycle configurations that were created
        after the specified time (timestamp).
        :param last_modified_time_before: A filter that returns only lifecycle configurations that were modified
        before the specified time (timestamp).
        :param last_modified_time_after: A filter that returns only lifecycle configurations that were modified
        after the specified time (timestamp).
        :returns: ListNotebookInstanceLifecycleConfigsOutput
        """
        raise NotImplementedError

    @handler("ListNotebookInstances")
    def list_notebook_instances(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_by: NotebookInstanceSortKey | None = None,
        sort_order: NotebookInstanceSortOrder | None = None,
        name_contains: NotebookInstanceNameContains | None = None,
        creation_time_before: CreationTime | None = None,
        creation_time_after: CreationTime | None = None,
        last_modified_time_before: LastModifiedTime | None = None,
        last_modified_time_after: LastModifiedTime | None = None,
        status_equals: NotebookInstanceStatus | None = None,
        notebook_instance_lifecycle_config_name_contains: NotebookInstanceLifecycleConfigName
        | None = None,
        default_code_repository_contains: CodeRepositoryContains | None = None,
        additional_code_repository_equals: CodeRepositoryNameOrUrl | None = None,
        **kwargs,
    ) -> ListNotebookInstancesOutput:
        """Returns a list of the SageMaker AI notebook instances in the requester's
        account in an Amazon Web Services Region.

        :param next_token: If the previous call to the ``ListNotebookInstances`` is truncated, the
        response includes a ``NextToken``.
        :param max_results: The maximum number of notebook instances to return.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param name_contains: A string in the notebook instances' name.
        :param creation_time_before: A filter that returns only notebook instances that were created before
        the specified time (timestamp).
        :param creation_time_after: A filter that returns only notebook instances that were created after
        the specified time (timestamp).
        :param last_modified_time_before: A filter that returns only notebook instances that were modified before
        the specified time (timestamp).
        :param last_modified_time_after: A filter that returns only notebook instances that were modified after
        the specified time (timestamp).
        :param status_equals: A filter that returns only notebook instances with the specified status.
        :param notebook_instance_lifecycle_config_name_contains: A string in the name of a notebook instances lifecycle configuration
        associated with this notebook instance.
        :param default_code_repository_contains: A string in the name or URL of a Git repository associated with this
        notebook instance.
        :param additional_code_repository_equals: A filter that returns only notebook instances with associated with the
        specified git repository.
        :returns: ListNotebookInstancesOutput
        """
        raise NotImplementedError

    @handler("ListOptimizationJobs")
    def list_optimization_jobs(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        creation_time_after: CreationTime | None = None,
        creation_time_before: CreationTime | None = None,
        last_modified_time_after: LastModifiedTime | None = None,
        last_modified_time_before: LastModifiedTime | None = None,
        optimization_contains: NameContains | None = None,
        name_contains: NameContains | None = None,
        status_equals: OptimizationJobStatus | None = None,
        sort_by: ListOptimizationJobsSortBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListOptimizationJobsResponse:
        """Lists the optimization jobs in your account and their properties.

        :param next_token: A token that you use to get the next set of results following a
        truncated response.
        :param max_results: The maximum number of optimization jobs to return in the response.
        :param creation_time_after: Filters the results to only those optimization jobs that were created
        after the specified time.
        :param creation_time_before: Filters the results to only those optimization jobs that were created
        before the specified time.
        :param last_modified_time_after: Filters the results to only those optimization jobs that were updated
        after the specified time.
        :param last_modified_time_before: Filters the results to only those optimization jobs that were updated
        before the specified time.
        :param optimization_contains: Filters the results to only those optimization jobs that apply the
        specified optimization techniques.
        :param name_contains: Filters the results to only those optimization jobs with a name that
        contains the specified string.
        :param status_equals: Filters the results to only those optimization jobs with the specified
        status.
        :param sort_by: The field by which to sort the optimization jobs in the response.
        :param sort_order: The sort order for results.
        :returns: ListOptimizationJobsResponse
        """
        raise NotImplementedError

    @handler("ListPartnerApps")
    def list_partner_apps(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListPartnerAppsResponse:
        """Lists all of the SageMaker Partner AI Apps in an account.

        :param max_results: This parameter defines the maximum number of results that can be
        returned in a single response.
        :param next_token: If the previous response was truncated, you will receive this token.
        :returns: ListPartnerAppsResponse
        """
        raise NotImplementedError

    @handler("ListPipelineExecutionSteps")
    def list_pipeline_execution_steps(
        self,
        context: RequestContext,
        pipeline_execution_arn: PipelineExecutionArn | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListPipelineExecutionStepsResponse:
        """Gets a list of ``PipeLineExecutionStep`` objects.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :param next_token: If the result of the previous ``ListPipelineExecutionSteps`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of pipeline execution steps to return in the
        response.
        :param sort_order: The field by which to sort results.
        :returns: ListPipelineExecutionStepsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListPipelineExecutions")
    def list_pipeline_executions(
        self,
        context: RequestContext,
        pipeline_name: PipelineNameOrArn,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortPipelineExecutionsBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListPipelineExecutionsResponse:
        """Gets a list of the pipeline executions.

        :param pipeline_name: The name or Amazon Resource Name (ARN) of the pipeline.
        :param created_after: A filter that returns the pipeline executions that were created after a
        specified time.
        :param created_before: A filter that returns the pipeline executions that were created before a
        specified time.
        :param sort_by: The field by which to sort results.
        :param sort_order: The sort order for results.
        :param next_token: If the result of the previous ``ListPipelineExecutions`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of pipeline executions to return in the response.
        :returns: ListPipelineExecutionsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListPipelineParametersForExecution")
    def list_pipeline_parameters_for_execution(
        self,
        context: RequestContext,
        pipeline_execution_arn: PipelineExecutionArn,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListPipelineParametersForExecutionResponse:
        """Gets a list of parameters for a pipeline execution.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :param next_token: If the result of the previous ``ListPipelineParametersForExecution``
        request was truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of parameters to return in the response.
        :returns: ListPipelineParametersForExecutionResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListPipelines")
    def list_pipelines(
        self,
        context: RequestContext,
        pipeline_name_prefix: PipelineName | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortPipelinesBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListPipelinesResponse:
        """Gets a list of pipelines.

        :param pipeline_name_prefix: The prefix of the pipeline name.
        :param created_after: A filter that returns the pipelines that were created after a specified
        time.
        :param created_before: A filter that returns the pipelines that were created before a specified
        time.
        :param sort_by: The field by which to sort results.
        :param sort_order: The sort order for results.
        :param next_token: If the result of the previous ``ListPipelines`` request was truncated,
        the response includes a ``NextToken``.
        :param max_results: The maximum number of pipelines to return in the response.
        :returns: ListPipelinesResponse
        """
        raise NotImplementedError

    @handler("ListProcessingJobs")
    def list_processing_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: String | None = None,
        status_equals: ProcessingJobStatus | None = None,
        sort_by: SortBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListProcessingJobsResponse:
        """Lists processing jobs that satisfy various filters.

        :param creation_time_after: A filter that returns only processing jobs created after the specified
        time.
        :param creation_time_before: A filter that returns only processing jobs created after the specified
        time.
        :param last_modified_time_after: A filter that returns only processing jobs modified after the specified
        time.
        :param last_modified_time_before: A filter that returns only processing jobs modified before the specified
        time.
        :param name_contains: A string in the processing job name.
        :param status_equals: A filter that retrieves only processing jobs with a specific status.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param next_token: If the result of the previous ``ListProcessingJobs`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of processing jobs to return in the response.
        :returns: ListProcessingJobsResponse
        """
        raise NotImplementedError

    @handler("ListProjects")
    def list_projects(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        max_results: MaxResults | None = None,
        name_contains: ProjectEntityName | None = None,
        next_token: NextToken | None = None,
        sort_by: ProjectSortBy | None = None,
        sort_order: ProjectSortOrder | None = None,
        **kwargs,
    ) -> ListProjectsOutput:
        """Gets a list of the projects in an Amazon Web Services account.

        :param creation_time_after: A filter that returns the projects that were created after a specified
        time.
        :param creation_time_before: A filter that returns the projects that were created before a specified
        time.
        :param max_results: The maximum number of projects to return in the response.
        :param name_contains: A filter that returns the projects whose name contains a specified
        string.
        :param next_token: If the result of the previous ``ListProjects`` request was truncated,
        the response includes a ``NextToken``.
        :param sort_by: The field by which to sort results.
        :param sort_order: The sort order for results.
        :returns: ListProjectsOutput
        """
        raise NotImplementedError

    @handler("ListResourceCatalogs")
    def list_resource_catalogs(
        self,
        context: RequestContext,
        name_contains: ResourceCatalogName | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        sort_order: ResourceCatalogSortOrder | None = None,
        sort_by: ResourceCatalogSortBy | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListResourceCatalogsResponse:
        """Lists Amazon SageMaker Catalogs based on given filters and orders. The
        maximum number of ``ResourceCatalog`` s viewable is 1000.

        :param name_contains: A string that partially matches one or more ``ResourceCatalog`` s
        names.
        :param creation_time_after: Use this parameter to search for ``ResourceCatalog`` s created after a
        specific date and time.
        :param creation_time_before: Use this parameter to search for ``ResourceCatalog`` s created before a
        specific date and time.
        :param sort_order: The order in which the resource catalogs are listed.
        :param sort_by: The value on which the resource catalog list is sorted.
        :param max_results: The maximum number of results returned by ``ListResourceCatalogs``.
        :param next_token: A token to resume pagination of ``ListResourceCatalogs`` results.
        :returns: ListResourceCatalogsResponse
        """
        raise NotImplementedError

    @handler("ListSpaces")
    def list_spaces(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_order: SortOrder | None = None,
        sort_by: SpaceSortKey | None = None,
        domain_id_equals: DomainId | None = None,
        space_name_contains: SpaceName | None = None,
        **kwargs,
    ) -> ListSpacesResponse:
        """Lists spaces.

        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: This parameter defines the maximum number of results that can be return
        in a single response.
        :param sort_order: The sort order for the results.
        :param sort_by: The parameter by which to sort the results.
        :param domain_id_equals: A parameter to search for the domain ID.
        :param space_name_contains: A parameter by which to filter the results.
        :returns: ListSpacesResponse
        """
        raise NotImplementedError

    @handler("ListStageDevices")
    def list_stage_devices(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        stage_name: EntityName,
        next_token: NextToken | None = None,
        max_results: ListMaxResults | None = None,
        exclude_devices_deployed_in_other_stage: Boolean | None = None,
        **kwargs,
    ) -> ListStageDevicesResponse:
        """Lists devices allocated to the stage, containing detailed device
        information and deployment status.

        :param edge_deployment_plan_name: The name of the edge deployment plan.
        :param stage_name: The name of the stage in the deployment.
        :param next_token: The response from the last list when returning a list large enough to
        neeed tokening.
        :param max_results: The maximum number of requests to select.
        :param exclude_devices_deployed_in_other_stage: Toggle for excluding devices deployed in other stages.
        :returns: ListStageDevicesResponse
        """
        raise NotImplementedError

    @handler("ListStudioLifecycleConfigs")
    def list_studio_lifecycle_configs(
        self,
        context: RequestContext,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        name_contains: StudioLifecycleConfigName | None = None,
        app_type_equals: StudioLifecycleConfigAppType | None = None,
        creation_time_before: Timestamp | None = None,
        creation_time_after: Timestamp | None = None,
        modified_time_before: Timestamp | None = None,
        modified_time_after: Timestamp | None = None,
        sort_by: StudioLifecycleConfigSortKey | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListStudioLifecycleConfigsResponse:
        """Lists the Amazon SageMaker AI Studio Lifecycle Configurations in your
        Amazon Web Services Account.

        :param max_results: The total number of items to return in the response.
        :param next_token: If the previous call to ListStudioLifecycleConfigs didn't return the
        full set of Lifecycle Configurations, the call returns a token for
        getting the next set of Lifecycle Configurations.
        :param name_contains: A string in the Lifecycle Configuration name.
        :param app_type_equals: A parameter to search for the App Type to which the Lifecycle
        Configuration is attached.
        :param creation_time_before: A filter that returns only Lifecycle Configurations created on or before
        the specified time.
        :param creation_time_after: A filter that returns only Lifecycle Configurations created on or after
        the specified time.
        :param modified_time_before: A filter that returns only Lifecycle Configurations modified before the
        specified time.
        :param modified_time_after: A filter that returns only Lifecycle Configurations modified after the
        specified time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :returns: ListStudioLifecycleConfigsResponse
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("ListSubscribedWorkteams")
    def list_subscribed_workteams(
        self,
        context: RequestContext,
        name_contains: WorkteamName | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListSubscribedWorkteamsResponse:
        """Gets a list of the work teams that you are subscribed to in the Amazon
        Web Services Marketplace. The list may be empty if no work team
        satisfies the filter specified in the ``NameContains`` parameter.

        :param name_contains: A string in the work team name.
        :param next_token: If the result of the previous ``ListSubscribedWorkteams`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of work teams to return in each page of the response.
        :returns: ListSubscribedWorkteamsResponse
        """
        raise NotImplementedError

    @handler("ListTags")
    def list_tags(
        self,
        context: RequestContext,
        resource_arn: ResourceArn,
        next_token: NextToken | None = None,
        max_results: ListTagsMaxResults | None = None,
        **kwargs,
    ) -> ListTagsOutput:
        """Returns the tags for the specified SageMaker resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource whose tags you want to
        retrieve.
        :param next_token: If the response to the previous ``ListTags`` request is truncated,
        SageMaker returns this token.
        :param max_results: Maximum number of tags to return.
        :returns: ListTagsOutput
        """
        raise NotImplementedError

    @handler("ListTrainingJobs")
    def list_training_jobs(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: NameContains | None = None,
        status_equals: TrainingJobStatus | None = None,
        sort_by: SortBy | None = None,
        sort_order: SortOrder | None = None,
        warm_pool_status_equals: WarmPoolResourceStatus | None = None,
        training_plan_arn_equals: TrainingPlanArn | None = None,
        **kwargs,
    ) -> ListTrainingJobsResponse:
        """Lists training jobs.

        When ``StatusEquals`` and ``MaxResults`` are set at the same time, the
        ``MaxResults`` number of training jobs are first retrieved ignoring the
        ``StatusEquals`` parameter and then they are filtered by the
        ``StatusEquals`` parameter, which is returned as a response.

        For example, if ``ListTrainingJobs`` is invoked with the following
        parameters:

        ``{ ... MaxResults: 100, StatusEquals: InProgress ... }``

        First, 100 trainings jobs with any status, including those other than
        ``InProgress``, are selected (sorted according to the creation time,
        from the most current to the oldest). Next, those with a status of
        ``InProgress`` are returned.

        You can quickly test the API using the following Amazon Web Services CLI
        code.

        ``aws sagemaker list-training-jobs --max-results 100 --status-equals InProgress``

        :param next_token: If the result of the previous ``ListTrainingJobs`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of training jobs to return in the response.
        :param creation_time_after: A filter that returns only training jobs created after the specified
        time (timestamp).
        :param creation_time_before: A filter that returns only training jobs created before the specified
        time (timestamp).
        :param last_modified_time_after: A filter that returns only training jobs modified after the specified
        time (timestamp).
        :param last_modified_time_before: A filter that returns only training jobs modified before the specified
        time (timestamp).
        :param name_contains: A string in the training job name.
        :param status_equals: A filter that retrieves only training jobs with a specific status.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param warm_pool_status_equals: A filter that retrieves only training jobs with a specific warm pool
        status.
        :param training_plan_arn_equals: The Amazon Resource Name (ARN); of the training plan to filter training
        jobs by.
        :returns: ListTrainingJobsResponse
        """
        raise NotImplementedError

    @handler("ListTrainingJobsForHyperParameterTuningJob")
    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        context: RequestContext,
        hyper_parameter_tuning_job_name: HyperParameterTuningJobName,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        status_equals: TrainingJobStatus | None = None,
        sort_by: TrainingJobSortByOptions | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListTrainingJobsForHyperParameterTuningJobResponse:
        """Gets a list of
        `TrainingJobSummary <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html>`__
        objects that describe the training jobs that a hyperparameter tuning job
        launched.

        :param hyper_parameter_tuning_job_name: The name of the tuning job whose training jobs you want to list.
        :param next_token: If the result of the previous
        ``ListTrainingJobsForHyperParameterTuningJob`` request was truncated,
        the response includes a ``NextToken``.
        :param max_results: The maximum number of training jobs to return.
        :param status_equals: A filter that returns only training jobs with the specified status.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :returns: ListTrainingJobsForHyperParameterTuningJobResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListTrainingPlans")
    def list_training_plans(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        start_time_after: Timestamp | None = None,
        start_time_before: Timestamp | None = None,
        sort_by: TrainingPlanSortBy | None = None,
        sort_order: TrainingPlanSortOrder | None = None,
        filters: TrainingPlanFilters | None = None,
        **kwargs,
    ) -> ListTrainingPlansResponse:
        """Retrieves a list of training plans for the current account.

        :param next_token: A token to continue pagination if more results are available.
        :param max_results: The maximum number of results to return in the response.
        :param start_time_after: Filter to list only training plans with an actual start time after this
        date.
        :param start_time_before: Filter to list only training plans with an actual start time before this
        date.
        :param sort_by: The training plan field to sort the results by (e.
        :param sort_order: The order to sort the results (Ascending or Descending).
        :param filters: Additional filters to apply to the list of training plans.
        :returns: ListTrainingPlansResponse
        """
        raise NotImplementedError

    @handler("ListTransformJobs")
    def list_transform_jobs(
        self,
        context: RequestContext,
        creation_time_after: Timestamp | None = None,
        creation_time_before: Timestamp | None = None,
        last_modified_time_after: Timestamp | None = None,
        last_modified_time_before: Timestamp | None = None,
        name_contains: NameContains | None = None,
        status_equals: TransformJobStatus | None = None,
        sort_by: SortBy | None = None,
        sort_order: SortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListTransformJobsResponse:
        """Lists transform jobs.

        :param creation_time_after: A filter that returns only transform jobs created after the specified
        time.
        :param creation_time_before: A filter that returns only transform jobs created before the specified
        time.
        :param last_modified_time_after: A filter that returns only transform jobs modified after the specified
        time.
        :param last_modified_time_before: A filter that returns only transform jobs modified before the specified
        time.
        :param name_contains: A string in the transform job name.
        :param status_equals: A filter that retrieves only transform jobs with a specific status.
        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param next_token: If the result of the previous ``ListTransformJobs`` request was
        truncated, the response includes a ``NextToken``.
        :param max_results: The maximum number of transform jobs to return in the response.
        :returns: ListTransformJobsResponse
        """
        raise NotImplementedError

    @handler("ListTrialComponents")
    def list_trial_components(
        self,
        context: RequestContext,
        experiment_name: ExperimentEntityName | None = None,
        trial_name: ExperimentEntityName | None = None,
        source_arn: String256 | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortTrialComponentsBy | None = None,
        sort_order: SortOrder | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListTrialComponentsResponse:
        """Lists the trial components in your account. You can sort the list by
        trial component name or creation time. You can filter the list to show
        only components that were created in a specific time range. You can also
        filter on one of the following:

        -  ``ExperimentName``

        -  ``SourceArn``

        -  ``TrialName``

        :param experiment_name: A filter that returns only components that are part of the specified
        experiment.
        :param trial_name: A filter that returns only components that are part of the specified
        trial.
        :param source_arn: A filter that returns only components that have the specified source
        Amazon Resource Name (ARN).
        :param created_after: A filter that returns only components created after the specified time.
        :param created_before: A filter that returns only components created before the specified time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param max_results: The maximum number of components to return in the response.
        :param next_token: If the previous call to ``ListTrialComponents`` didn't return the full
        set of components, the call returns a token for getting the next set of
        components.
        :returns: ListTrialComponentsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListTrials")
    def list_trials(
        self,
        context: RequestContext,
        experiment_name: ExperimentEntityName | None = None,
        trial_component_name: ExperimentEntityName | None = None,
        created_after: Timestamp | None = None,
        created_before: Timestamp | None = None,
        sort_by: SortTrialsBy | None = None,
        sort_order: SortOrder | None = None,
        max_results: MaxResults | None = None,
        next_token: NextToken | None = None,
        **kwargs,
    ) -> ListTrialsResponse:
        """Lists the trials in your account. Specify an experiment name to limit
        the list to the trials that are part of that experiment. Specify a trial
        component name to limit the list to the trials that associated with that
        trial component. The list can be filtered to show only trials that were
        created in a specific time range. The list can be sorted by trial name
        or creation time.

        :param experiment_name: A filter that returns only trials that are part of the specified
        experiment.
        :param trial_component_name: A filter that returns only trials that are associated with the specified
        trial component.
        :param created_after: A filter that returns only trials created after the specified time.
        :param created_before: A filter that returns only trials created before the specified time.
        :param sort_by: The property used to sort results.
        :param sort_order: The sort order.
        :param max_results: The maximum number of trials to return in the response.
        :param next_token: If the previous call to ``ListTrials`` didn't return the full set of
        trials, the call returns a token for getting the next set of trials.
        :returns: ListTrialsResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("ListUserProfiles")
    def list_user_profiles(
        self,
        context: RequestContext,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        sort_order: SortOrder | None = None,
        sort_by: UserProfileSortKey | None = None,
        domain_id_equals: DomainId | None = None,
        user_profile_name_contains: UserProfileName | None = None,
        **kwargs,
    ) -> ListUserProfilesResponse:
        """Lists user profiles.

        :param next_token: If the previous response was truncated, you will receive this token.
        :param max_results: This parameter defines the maximum number of results that can be return
        in a single response.
        :param sort_order: The sort order for the results.
        :param sort_by: The parameter by which to sort the results.
        :param domain_id_equals: A parameter by which to filter the results.
        :param user_profile_name_contains: A parameter by which to filter the results.
        :returns: ListUserProfilesResponse
        """
        raise NotImplementedError

    @handler("ListWorkforces")
    def list_workforces(
        self,
        context: RequestContext,
        sort_by: ListWorkforcesSortByOptions | None = None,
        sort_order: SortOrder | None = None,
        name_contains: WorkforceName | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListWorkforcesResponse:
        """Use this operation to list all private and vendor workforces in an
        Amazon Web Services Region. Note that you can only have one private
        workforce per Amazon Web Services Region.

        :param sort_by: Sort workforces using the workforce name or creation date.
        :param sort_order: Sort workforces in ascending or descending order.
        :param name_contains: A filter you can use to search for workforces using part of the
        workforce name.
        :param next_token: A token to resume pagination.
        :param max_results: The maximum number of workforces returned in the response.
        :returns: ListWorkforcesResponse
        """
        raise NotImplementedError

    @handler("ListWorkteams")
    def list_workteams(
        self,
        context: RequestContext,
        sort_by: ListWorkteamsSortByOptions | None = None,
        sort_order: SortOrder | None = None,
        name_contains: WorkteamName | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        **kwargs,
    ) -> ListWorkteamsResponse:
        """Gets a list of private work teams that you have defined in a region. The
        list may be empty if no work team satisfies the filter specified in the
        ``NameContains`` parameter.

        :param sort_by: The field to sort results by.
        :param sort_order: The sort order for results.
        :param name_contains: A string in the work team's name.
        :param next_token: If the result of the previous ``ListWorkteams`` request was truncated,
        the response includes a ``NextToken``.
        :param max_results: The maximum number of work teams to return in each page of the response.
        :returns: ListWorkteamsResponse
        """
        raise NotImplementedError

    @handler("PutModelPackageGroupPolicy")
    def put_model_package_group_policy(
        self,
        context: RequestContext,
        model_package_group_name: EntityName,
        resource_policy: PolicyString,
        **kwargs,
    ) -> PutModelPackageGroupPolicyOutput:
        """Adds a resouce policy to control access to a model group. For
        information about resoure policies, see `Identity-based policies and
        resource-based
        policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html>`__
        in the *Amazon Web Services Identity and Access Management User Guide.*.

        :param model_package_group_name: The name of the model group to add a resource policy to.
        :param resource_policy: The resource policy for the model group.
        :returns: PutModelPackageGroupPolicyOutput
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("QueryLineage")
    def query_lineage(
        self,
        context: RequestContext,
        start_arns: QueryLineageStartArns | None = None,
        direction: Direction | None = None,
        include_edges: Boolean | None = None,
        filters: QueryFilters | None = None,
        max_depth: QueryLineageMaxDepth | None = None,
        max_results: QueryLineageMaxResults | None = None,
        next_token: String8192 | None = None,
        **kwargs,
    ) -> QueryLineageResponse:
        """Use this action to inspect your lineage and discover relationships
        between entities. For more information, see `Querying Lineage
        Entities <https://docs.aws.amazon.com/sagemaker/latest/dg/querying-lineage-entities.html>`__
        in the *Amazon SageMaker Developer Guide*.

        :param start_arns: A list of resource Amazon Resource Name (ARN) that represent the
        starting point for your lineage query.
        :param direction: Associations between lineage entities have a direction.
        :param include_edges: Setting this value to ``True`` retrieves not only the entities of
        interest but also the
        `Associations <https://docs.
        :param filters: A set of filtering parameters that allow you to specify which entities
        should be returned.
        :param max_depth: The maximum depth in lineage relationships from the ``StartArns`` that
        are traversed.
        :param max_results: Limits the number of vertices in the results.
        :param next_token: Limits the number of vertices in the request.
        :returns: QueryLineageResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("RegisterDevices")
    def register_devices(
        self,
        context: RequestContext,
        device_fleet_name: EntityName,
        devices: Devices,
        tags: TagList | None = None,
        **kwargs,
    ) -> None:
        """Register devices.

        :param device_fleet_name: The name of the fleet.
        :param devices: A list of devices to register with SageMaker Edge Manager.
        :param tags: The tags associated with devices.
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("RenderUiTemplate")
    def render_ui_template(
        self,
        context: RequestContext,
        task: RenderableTask,
        role_arn: RoleArn,
        ui_template: UiTemplate | None = None,
        human_task_ui_arn: HumanTaskUiArn | None = None,
        **kwargs,
    ) -> RenderUiTemplateResponse:
        """Renders the UI template so that you can preview the worker's experience.

        :param task: A ``RenderableTask`` object containing a representative task to render.
        :param role_arn: The Amazon Resource Name (ARN) that has access to the S3 objects that
        are used by the template.
        :param ui_template: A ``Template`` object containing the worker UI template to render.
        :param human_task_ui_arn: The ``HumanTaskUiArn`` of the worker UI that you want to render.
        :returns: RenderUiTemplateResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("RetryPipelineExecution")
    def retry_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_execution_arn: PipelineExecutionArn,
        client_request_token: IdempotencyToken,
        parallelism_configuration: ParallelismConfiguration | None = None,
        **kwargs,
    ) -> RetryPipelineExecutionResponse:
        """Retry the execution of the pipeline.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :param parallelism_configuration: This configuration, if specified, overrides the parallelism
        configuration of the parent pipeline.
        :returns: RetryPipelineExecutionResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("Search")
    def search(
        self,
        context: RequestContext,
        resource: ResourceType,
        search_expression: SearchExpression | None = None,
        sort_by: ResourcePropertyName | None = None,
        sort_order: SearchSortOrder | None = None,
        next_token: NextToken | None = None,
        max_results: MaxResults | None = None,
        cross_account_filter_option: CrossAccountFilterOption | None = None,
        visibility_conditions: VisibilityConditionsList | None = None,
        **kwargs,
    ) -> SearchResponse:
        """Finds SageMaker resources that match a search query. Matching resources
        are returned as a list of ``SearchRecord`` objects in the response. You
        can sort the search results by any resource property in a ascending or
        descending order.

        You can query against the following value types: numeric, text, Boolean,
        and timestamp.

        The Search API may provide access to otherwise restricted data. See
        `Amazon SageMaker API Permissions: Actions, Permissions, and Resources
        Reference <https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html>`__
        for more information.

        :param resource: The name of the SageMaker resource to search for.
        :param search_expression: A Boolean conditional statement.
        :param sort_by: The name of the resource property used to sort the ``SearchResults``.
        :param sort_order: How ``SearchResults`` are ordered.
        :param next_token: If more than ``MaxResults`` resources match the specified
        ``SearchExpression``, the response includes a ``NextToken``.
        :param max_results: The maximum number of results to return.
        :param cross_account_filter_option: A cross account filter option.
        :param visibility_conditions: Limits the results of your search request to the resources that you can
        access.
        :returns: SearchResponse
        """
        raise NotImplementedError

    @handler("SearchTrainingPlanOfferings")
    def search_training_plan_offerings(
        self,
        context: RequestContext,
        duration_hours: TrainingPlanDurationHoursInput,
        target_resources: SageMakerResourceNames,
        instance_type: ReservedCapacityInstanceType | None = None,
        instance_count: ReservedCapacityInstanceCount | None = None,
        start_time_after: Timestamp | None = None,
        end_time_before: Timestamp | None = None,
        **kwargs,
    ) -> SearchTrainingPlanOfferingsResponse:
        """Searches for available training plan offerings based on specified
        criteria.

        -  Users search for available plan offerings based on their requirements
           (e.g., instance type, count, start time, duration).

        -  And then, they create a plan that best matches their needs using the
           ID of the plan offering they want to use.

        For more information about how to reserve GPU capacity for your
        SageMaker training jobs or SageMaker HyperPod clusters using Amazon
        SageMaker Training Plan , see ``CreateTrainingPlan``.

        :param duration_hours: The desired duration in hours for the training plan offerings.
        :param target_resources: The target resources (e.
        :param instance_type: The type of instance you want to search for in the available training
        plan offerings.
        :param instance_count: The number of instances you want to reserve in the training plan
        offerings.
        :param start_time_after: A filter to search for training plan offerings with a start time after a
        specified date.
        :param end_time_before: A filter to search for reserved capacity offerings with an end time
        before a specified date.
        :returns: SearchTrainingPlanOfferingsResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("SendPipelineExecutionStepFailure")
    def send_pipeline_execution_step_failure(
        self,
        context: RequestContext,
        callback_token: CallbackToken,
        failure_reason: String256 | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> SendPipelineExecutionStepFailureResponse:
        """Notifies the pipeline that the execution of a callback step failed,
        along with a message describing why. When a callback step is run, the
        pipeline generates a callback token and includes the token in a message
        sent to Amazon Simple Queue Service (Amazon SQS).

        :param callback_token: The pipeline generated token from the Amazon SQS queue.
        :param failure_reason: A message describing why the step failed.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :returns: SendPipelineExecutionStepFailureResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("SendPipelineExecutionStepSuccess")
    def send_pipeline_execution_step_success(
        self,
        context: RequestContext,
        callback_token: CallbackToken,
        output_parameters: OutputParameterList | None = None,
        client_request_token: IdempotencyToken | None = None,
        **kwargs,
    ) -> SendPipelineExecutionStepSuccessResponse:
        """Notifies the pipeline that the execution of a callback step succeeded
        and provides a list of the step's output parameters. When a callback
        step is run, the pipeline generates a callback token and includes the
        token in a message sent to Amazon Simple Queue Service (Amazon SQS).

        :param callback_token: The pipeline generated token from the Amazon SQS queue.
        :param output_parameters: A list of the output parameters of the callback step.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :returns: SendPipelineExecutionStepSuccessResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("StartEdgeDeploymentStage")
    def start_edge_deployment_stage(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        stage_name: EntityName,
        **kwargs,
    ) -> None:
        """Starts a stage in an edge deployment plan.

        :param edge_deployment_plan_name: The name of the edge deployment plan to start.
        :param stage_name: The name of the stage to start.
        """
        raise NotImplementedError

    @handler("StartInferenceExperiment")
    def start_inference_experiment(
        self, context: RequestContext, name: InferenceExperimentName, **kwargs
    ) -> StartInferenceExperimentResponse:
        """Starts an inference experiment.

        :param name: The name of the inference experiment to start.
        :returns: StartInferenceExperimentResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StartMlflowTrackingServer")
    def start_mlflow_tracking_server(
        self, context: RequestContext, tracking_server_name: TrackingServerName, **kwargs
    ) -> StartMlflowTrackingServerResponse:
        """Programmatically start an MLflow Tracking Server.

        :param tracking_server_name: The name of the tracking server to start.
        :returns: StartMlflowTrackingServerResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StartMonitoringSchedule")
    def start_monitoring_schedule(
        self, context: RequestContext, monitoring_schedule_name: MonitoringScheduleName, **kwargs
    ) -> None:
        """Starts a previously stopped monitoring schedule.

        By default, when you successfully create a new schedule, the status of a
        monitoring schedule is ``scheduled``.

        :param monitoring_schedule_name: The name of the schedule to start.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StartNotebookInstance")
    def start_notebook_instance(
        self, context: RequestContext, notebook_instance_name: NotebookInstanceName, **kwargs
    ) -> None:
        """Launches an ML compute instance with the latest version of the libraries
        and attaches your ML storage volume. After configuring the notebook
        instance, SageMaker AI sets the notebook instance status to
        ``InService``. A notebook instance's status must be ``InService`` before
        you can connect to your Jupyter notebook.

        :param notebook_instance_name: The name of the notebook instance to start.
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("StartPipelineExecution")
    def start_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_name: PipelineNameOrArn,
        client_request_token: IdempotencyToken,
        pipeline_execution_display_name: PipelineExecutionName | None = None,
        pipeline_parameters: ParameterList | None = None,
        pipeline_execution_description: PipelineExecutionDescription | None = None,
        parallelism_configuration: ParallelismConfiguration | None = None,
        selective_execution_config: SelectiveExecutionConfig | None = None,
        **kwargs,
    ) -> StartPipelineExecutionResponse:
        """Starts a pipeline execution.

        :param pipeline_name: The name or Amazon Resource Name (ARN) of the pipeline.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :param pipeline_execution_display_name: The display name of the pipeline execution.
        :param pipeline_parameters: Contains a list of pipeline parameters.
        :param pipeline_execution_description: The description of the pipeline execution.
        :param parallelism_configuration: This configuration, if specified, overrides the parallelism
        configuration of the parent pipeline for this specific run.
        :param selective_execution_config: The selective execution configuration applied to the pipeline run.
        :returns: StartPipelineExecutionResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("StopAutoMLJob")
    def stop_auto_ml_job(
        self, context: RequestContext, auto_ml_job_name: AutoMLJobName, **kwargs
    ) -> None:
        """A method for forcing a running job to shut down.

        :param auto_ml_job_name: The name of the object you are requesting.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopCompilationJob")
    def stop_compilation_job(
        self, context: RequestContext, compilation_job_name: EntityName, **kwargs
    ) -> None:
        """Stops a model compilation job.

        To stop a job, Amazon SageMaker AI sends the algorithm the SIGTERM
        signal. This gracefully shuts the job down. If the job hasn't stopped,
        it sends the SIGKILL signal.

        When it receives a ``StopCompilationJob`` request, Amazon SageMaker AI
        changes the ``CompilationJobStatus`` of the job to ``Stopping``. After
        Amazon SageMaker stops the job, it sets the ``CompilationJobStatus`` to
        ``Stopped``.

        :param compilation_job_name: The name of the model compilation job to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopEdgeDeploymentStage")
    def stop_edge_deployment_stage(
        self,
        context: RequestContext,
        edge_deployment_plan_name: EntityName,
        stage_name: EntityName,
        **kwargs,
    ) -> None:
        """Stops a stage in an edge deployment plan.

        :param edge_deployment_plan_name: The name of the edge deployment plan to stop.
        :param stage_name: The name of the stage to stop.
        """
        raise NotImplementedError

    @handler("StopEdgePackagingJob")
    def stop_edge_packaging_job(
        self, context: RequestContext, edge_packaging_job_name: EntityName, **kwargs
    ) -> None:
        """Request to stop an edge packaging job.

        :param edge_packaging_job_name: The name of the edge packaging job.
        """
        raise NotImplementedError

    @handler("StopHyperParameterTuningJob")
    def stop_hyper_parameter_tuning_job(
        self,
        context: RequestContext,
        hyper_parameter_tuning_job_name: HyperParameterTuningJobName,
        **kwargs,
    ) -> None:
        """Stops a running hyperparameter tuning job and all running training jobs
        that the tuning job launched.

        All model artifacts output from the training jobs are stored in Amazon
        Simple Storage Service (Amazon S3). All data that the training jobs
        write to Amazon CloudWatch Logs are still available in CloudWatch. After
        the tuning job moves to the ``Stopped`` state, it releases all reserved
        resources for the tuning job.

        :param hyper_parameter_tuning_job_name: The name of the tuning job to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopInferenceExperiment")
    def stop_inference_experiment(
        self,
        context: RequestContext,
        name: InferenceExperimentName,
        model_variant_actions: ModelVariantActionMap,
        desired_model_variants: ModelVariantConfigList | None = None,
        desired_state: InferenceExperimentStopDesiredState | None = None,
        reason: InferenceExperimentStatusReason | None = None,
        **kwargs,
    ) -> StopInferenceExperimentResponse:
        """Stops an inference experiment.

        :param name: The name of the inference experiment to stop.
        :param model_variant_actions: Array of key-value pairs, with names of variants mapped to actions.
        :param desired_model_variants: An array of ``ModelVariantConfig`` objects.
        :param desired_state: The desired state of the experiment after stopping.
        :param reason: The reason for stopping the experiment.
        :returns: StopInferenceExperimentResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopInferenceRecommendationsJob")
    def stop_inference_recommendations_job(
        self, context: RequestContext, job_name: RecommendationJobName, **kwargs
    ) -> None:
        """Stops an Inference Recommender job.

        :param job_name: The name of the job you want to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopLabelingJob")
    def stop_labeling_job(
        self, context: RequestContext, labeling_job_name: LabelingJobName, **kwargs
    ) -> None:
        """Stops a running labeling job. A job that is stopped cannot be restarted.
        Any results obtained before the job is stopped are placed in the Amazon
        S3 output bucket.

        :param labeling_job_name: The name of the labeling job to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopMlflowTrackingServer")
    def stop_mlflow_tracking_server(
        self, context: RequestContext, tracking_server_name: TrackingServerName, **kwargs
    ) -> StopMlflowTrackingServerResponse:
        """Programmatically stop an MLflow Tracking Server.

        :param tracking_server_name: The name of the tracking server to stop.
        :returns: StopMlflowTrackingServerResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopMonitoringSchedule")
    def stop_monitoring_schedule(
        self, context: RequestContext, monitoring_schedule_name: MonitoringScheduleName, **kwargs
    ) -> None:
        """Stops a previously started monitoring schedule.

        :param monitoring_schedule_name: The name of the schedule to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopNotebookInstance")
    def stop_notebook_instance(
        self, context: RequestContext, notebook_instance_name: NotebookInstanceName, **kwargs
    ) -> None:
        """Terminates the ML compute instance. Before terminating the instance,
        SageMaker AI disconnects the ML storage volume from it. SageMaker AI
        preserves the ML storage volume. SageMaker AI stops charging you for the
        ML compute instance when you call ``StopNotebookInstance``.

        To access data on the ML storage volume for a notebook instance that has
        been terminated, call the ``StartNotebookInstance`` API.
        ``StartNotebookInstance`` launches another ML compute instance,
        configures it, and attaches the preserved ML storage volume so you can
        continue your work.

        :param notebook_instance_name: The name of the notebook instance to terminate.
        """
        raise NotImplementedError

    @handler("StopOptimizationJob")
    def stop_optimization_job(
        self, context: RequestContext, optimization_job_name: EntityName, **kwargs
    ) -> None:
        """Ends a running inference optimization job.

        :param optimization_job_name: The name that you assigned to the optimization job.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopPipelineExecution")
    def stop_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_execution_arn: PipelineExecutionArn,
        client_request_token: IdempotencyToken,
        **kwargs,
    ) -> StopPipelineExecutionResponse:
        """Stops a pipeline execution.

        **Callback Step**

        A pipeline execution won't stop while a callback step is running. When
        you call ``StopPipelineExecution`` on a pipeline execution with a
        running callback step, SageMaker Pipelines sends an additional Amazon
        SQS message to the specified SQS queue. The body of the SQS message
        contains a "Status" field which is set to "Stopping".

        You should add logic to your Amazon SQS message consumer to take any
        needed action (for example, resource cleanup) upon receipt of the
        message followed by a call to ``SendPipelineExecutionStepSuccess`` or
        ``SendPipelineExecutionStepFailure``.

        Only when SageMaker Pipelines receives one of these calls will it stop
        the pipeline execution.

        **Lambda Step**

        A pipeline execution can't be stopped while a lambda step is running
        because the Lambda function invoked by the lambda step can't be stopped.
        If you attempt to stop the execution while the Lambda function is
        running, the pipeline waits for the Lambda function to finish or until
        the timeout is hit, whichever occurs first, and then stops. If the
        Lambda function finishes, the pipeline execution status is ``Stopped``.
        If the timeout is hit the pipeline execution status is ``Failed``.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :param client_request_token: A unique, case-sensitive identifier that you provide to ensure the
        idempotency of the operation.
        :returns: StopPipelineExecutionResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopProcessingJob")
    def stop_processing_job(
        self, context: RequestContext, processing_job_name: ProcessingJobName, **kwargs
    ) -> None:
        """Stops a processing job.

        :param processing_job_name: The name of the processing job to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopTrainingJob")
    def stop_training_job(
        self, context: RequestContext, training_job_name: TrainingJobName, **kwargs
    ) -> None:
        """Stops a training job. To stop a job, SageMaker sends the algorithm the
        ``SIGTERM`` signal, which delays job termination for 120 seconds.
        Algorithms might use this 120-second window to save the model artifacts,
        so the results of the training is not lost.

        When it receives a ``StopTrainingJob`` request, SageMaker changes the
        status of the job to ``Stopping``. After SageMaker stops the job, it
        sets the status to ``Stopped``.

        :param training_job_name: The name of the training job to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("StopTransformJob")
    def stop_transform_job(
        self, context: RequestContext, transform_job_name: TransformJobName, **kwargs
    ) -> None:
        """Stops a batch transform job.

        When Amazon SageMaker receives a ``StopTransformJob`` request, the
        status of the job changes to ``Stopping``. After Amazon SageMaker stops
        the job, the status is set to ``Stopped``. When you stop a batch
        transform job before it is completed, Amazon SageMaker doesn't store the
        job's output in Amazon S3.

        :param transform_job_name: The name of the batch transform job to stop.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateAction")
    def update_action(
        self,
        context: RequestContext,
        action_name: ExperimentEntityName,
        description: ExperimentDescription | None = None,
        status: ActionStatus | None = None,
        properties: LineageEntityParameters | None = None,
        properties_to_remove: ListLineageEntityParameterKey | None = None,
        **kwargs,
    ) -> UpdateActionResponse:
        """Updates an action.

        :param action_name: The name of the action to update.
        :param description: The new description for the action.
        :param status: The new status for the action.
        :param properties: The new list of properties.
        :param properties_to_remove: A list of properties to remove.
        :returns: UpdateActionResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateAppImageConfig")
    def update_app_image_config(
        self,
        context: RequestContext,
        app_image_config_name: AppImageConfigName,
        kernel_gateway_image_config: KernelGatewayImageConfig | None = None,
        jupyter_lab_app_image_config: JupyterLabAppImageConfig | None = None,
        code_editor_app_image_config: CodeEditorAppImageConfig | None = None,
        **kwargs,
    ) -> UpdateAppImageConfigResponse:
        """Updates the properties of an AppImageConfig.

        :param app_image_config_name: The name of the AppImageConfig to update.
        :param kernel_gateway_image_config: The new KernelGateway app to run on the image.
        :param jupyter_lab_app_image_config: The JupyterLab app running on the image.
        :param code_editor_app_image_config: The Code Editor app running on the image.
        :returns: UpdateAppImageConfigResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateArtifact")
    def update_artifact(
        self,
        context: RequestContext,
        artifact_arn: ArtifactArn,
        artifact_name: ExperimentEntityName | None = None,
        properties: ArtifactProperties | None = None,
        properties_to_remove: ListLineageEntityParameterKey | None = None,
        **kwargs,
    ) -> UpdateArtifactResponse:
        """Updates an artifact.

        :param artifact_arn: The Amazon Resource Name (ARN) of the artifact to update.
        :param artifact_name: The new name for the artifact.
        :param properties: The new list of properties.
        :param properties_to_remove: A list of properties to remove.
        :returns: UpdateArtifactResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateCluster")
    def update_cluster(
        self,
        context: RequestContext,
        cluster_name: ClusterNameOrArn,
        instance_groups: ClusterInstanceGroupSpecifications,
        node_recovery: ClusterNodeRecovery | None = None,
        instance_groups_to_delete: ClusterInstanceGroupsToDelete | None = None,
        **kwargs,
    ) -> UpdateClusterResponse:
        """Updates a SageMaker HyperPod cluster.

        :param cluster_name: Specify the name of the SageMaker HyperPod cluster you want to update.
        :param instance_groups: Specify the instance groups to update.
        :param node_recovery: The node recovery mode to be applied to the SageMaker HyperPod cluster.
        :param instance_groups_to_delete: Specify the names of the instance groups to delete.
        :returns: UpdateClusterResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateClusterSchedulerConfig")
    def update_cluster_scheduler_config(
        self,
        context: RequestContext,
        cluster_scheduler_config_id: ClusterSchedulerConfigId,
        target_version: Integer,
        scheduler_config: SchedulerConfig | None = None,
        description: EntityDescription | None = None,
        **kwargs,
    ) -> UpdateClusterSchedulerConfigResponse:
        """Update the cluster policy configuration.

        :param cluster_scheduler_config_id: ID of the cluster policy.
        :param target_version: Target version.
        :param scheduler_config: Cluster policy configuration.
        :param description: Description of the cluster policy.
        :returns: UpdateClusterSchedulerConfigResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateClusterSoftware")
    def update_cluster_software(
        self,
        context: RequestContext,
        cluster_name: ClusterNameOrArn,
        instance_groups: UpdateClusterSoftwareInstanceGroups | None = None,
        deployment_config: DeploymentConfiguration | None = None,
        **kwargs,
    ) -> UpdateClusterSoftwareResponse:
        """Updates the platform software of a SageMaker HyperPod cluster for
        security patching. To learn how to use this API, see `Update the
        SageMaker HyperPod platform software of a
        cluster <https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software>`__.

        The ``UpgradeClusterSoftware`` API call may impact your SageMaker
        HyperPod cluster uptime and availability. Plan accordingly to mitigate
        potential disruptions to your workloads.

        :param cluster_name: Specify the name or the Amazon Resource Name (ARN) of the SageMaker
        HyperPod cluster you want to update for security patching.
        :param instance_groups: The array of instance groups for which to update AMI versions.
        :param deployment_config: The configuration to use when updating the AMI versions.
        :returns: UpdateClusterSoftwareResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateCodeRepository")
    def update_code_repository(
        self,
        context: RequestContext,
        code_repository_name: EntityName,
        git_config: GitConfigForUpdate | None = None,
        **kwargs,
    ) -> UpdateCodeRepositoryOutput:
        """Updates the specified Git repository with the specified values.

        :param code_repository_name: The name of the Git repository to update.
        :param git_config: The configuration of the git repository, including the URL and the
        Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager
        secret that contains the credentials used to access the repository.
        :returns: UpdateCodeRepositoryOutput
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateComputeQuota")
    def update_compute_quota(
        self,
        context: RequestContext,
        compute_quota_id: ComputeQuotaId,
        target_version: Integer,
        compute_quota_config: ComputeQuotaConfig | None = None,
        compute_quota_target: ComputeQuotaTarget | None = None,
        activation_state: ActivationState | None = None,
        description: EntityDescription | None = None,
        **kwargs,
    ) -> UpdateComputeQuotaResponse:
        """Update the compute allocation definition.

        :param compute_quota_id: ID of the compute allocation definition.
        :param target_version: Target version.
        :param compute_quota_config: Configuration of the compute allocation definition.
        :param compute_quota_target: The target entity to allocate compute resources to.
        :param activation_state: The state of the compute allocation being described.
        :param description: Description of the compute allocation definition.
        :returns: UpdateComputeQuotaResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateContext")
    def update_context(
        self,
        context: RequestContext,
        context_name: ContextName,
        description: ExperimentDescription | None = None,
        properties: LineageEntityParameters | None = None,
        properties_to_remove: ListLineageEntityParameterKey | None = None,
        **kwargs,
    ) -> UpdateContextResponse:
        """Updates a context.

        :param context_name: The name of the context to update.
        :param description: The new description for the context.
        :param properties: The new list of properties.
        :param properties_to_remove: A list of properties to remove.
        :returns: UpdateContextResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateDeviceFleet")
    def update_device_fleet(
        self,
        context: RequestContext,
        device_fleet_name: EntityName,
        output_config: EdgeOutputConfig,
        role_arn: RoleArn | None = None,
        description: DeviceFleetDescription | None = None,
        enable_iot_role_alias: EnableIotRoleAlias | None = None,
        **kwargs,
    ) -> None:
        """Updates a fleet of devices.

        :param device_fleet_name: The name of the fleet.
        :param output_config: Output configuration for storing sample data collected by the fleet.
        :param role_arn: The Amazon Resource Name (ARN) of the device.
        :param description: Description of the fleet.
        :param enable_iot_role_alias: Whether to create an Amazon Web Services IoT Role Alias during device
        fleet creation.
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("UpdateDevices")
    def update_devices(
        self, context: RequestContext, device_fleet_name: EntityName, devices: Devices, **kwargs
    ) -> None:
        """Updates one or more devices in a fleet.

        :param device_fleet_name: The name of the fleet the devices belong to.
        :param devices: List of devices to register with Edge Manager agent.
        """
        raise NotImplementedError

    @handler("UpdateDomain")
    def update_domain(
        self,
        context: RequestContext,
        domain_id: DomainId,
        default_user_settings: UserSettings | None = None,
        domain_settings_for_update: DomainSettingsForUpdate | None = None,
        app_security_group_management: AppSecurityGroupManagement | None = None,
        default_space_settings: DefaultSpaceSettings | None = None,
        subnet_ids: Subnets | None = None,
        app_network_access_type: AppNetworkAccessType | None = None,
        tag_propagation: TagPropagation | None = None,
        **kwargs,
    ) -> UpdateDomainResponse:
        """Updates the default settings for new user profiles in the domain.

        :param domain_id: The ID of the domain to be updated.
        :param default_user_settings: A collection of settings.
        :param domain_settings_for_update: A collection of ``DomainSettings`` configuration values to update.
        :param app_security_group_management: The entity that creates and manages the required security groups for
        inter-app communication in ``VPCOnly`` mode.
        :param default_space_settings: The default settings for shared spaces that users create in the domain.
        :param subnet_ids: The VPC subnets that Studio uses for communication.
        :param app_network_access_type: Specifies the VPC used for non-EFS traffic.
        :param tag_propagation: Indicates whether custom tag propagation is supported for the domain.
        :returns: UpdateDomainResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateEndpoint")
    def update_endpoint(
        self,
        context: RequestContext,
        endpoint_name: EndpointName,
        endpoint_config_name: EndpointConfigName,
        retain_all_variant_properties: Boolean | None = None,
        exclude_retained_variant_properties: VariantPropertyList | None = None,
        deployment_config: DeploymentConfig | None = None,
        retain_deployment_config: Boolean | None = None,
        **kwargs,
    ) -> UpdateEndpointOutput:
        """Deploys the ``EndpointConfig`` specified in the request to a new fleet
        of instances. SageMaker shifts endpoint traffic to the new instances
        with the updated endpoint configuration and then deletes the old
        instances using the previous ``EndpointConfig`` (there is no
        availability loss). For more information about how to control the update
        and traffic shifting process, see `Update models in
        production <https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html>`__.

        When SageMaker receives the request, it sets the endpoint status to
        ``Updating``. After updating the endpoint, it sets the status to
        ``InService``. To check the status of an endpoint, use the
        `DescribeEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html>`__
        API.

        You must not delete an ``EndpointConfig`` in use by an endpoint that is
        live or while the ``UpdateEndpoint`` or ``CreateEndpoint`` operations
        are being performed on the endpoint. To update an endpoint, you must
        create a new ``EndpointConfig``.

        If you delete the ``EndpointConfig`` of an endpoint that is active or
        being created or updated you may lose visibility into the instance type
        the endpoint is using. The endpoint must be deleted in order to stop
        incurring charges.

        :param endpoint_name: The name of the endpoint whose configuration you want to update.
        :param endpoint_config_name: The name of the new endpoint configuration.
        :param retain_all_variant_properties: When updating endpoint resources, enables or disables the retention of
        `variant
        properties <https://docs.
        :param exclude_retained_variant_properties: When you are updating endpoint resources with
        ``RetainAllVariantProperties``, whose value is set to ``true``,
        ``ExcludeRetainedVariantProperties`` specifies the list of type
        `VariantProperty <https://docs.
        :param deployment_config: The deployment configuration for an endpoint, which contains the desired
        deployment strategy and rollback configurations.
        :param retain_deployment_config: Specifies whether to reuse the last deployment configuration.
        :returns: UpdateEndpointOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateEndpointWeightsAndCapacities")
    def update_endpoint_weights_and_capacities(
        self,
        context: RequestContext,
        endpoint_name: EndpointName,
        desired_weights_and_capacities: DesiredWeightAndCapacityList,
        **kwargs,
    ) -> UpdateEndpointWeightsAndCapacitiesOutput:
        """Updates variant weight of one or more variants associated with an
        existing endpoint, or capacity of one variant associated with an
        existing endpoint. When it receives the request, SageMaker sets the
        endpoint status to ``Updating``. After updating the endpoint, it sets
        the status to ``InService``. To check the status of an endpoint, use the
        `DescribeEndpoint <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html>`__
        API.

        :param endpoint_name: The name of an existing SageMaker endpoint.
        :param desired_weights_and_capacities: An object that provides new capacity and weight values for a variant.
        :returns: UpdateEndpointWeightsAndCapacitiesOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateExperiment")
    def update_experiment(
        self,
        context: RequestContext,
        experiment_name: ExperimentEntityName,
        display_name: ExperimentEntityName | None = None,
        description: ExperimentDescription | None = None,
        **kwargs,
    ) -> UpdateExperimentResponse:
        """Adds, updates, or removes the description of an experiment. Updates the
        display name of an experiment.

        :param experiment_name: The name of the experiment to update.
        :param display_name: The name of the experiment as displayed.
        :param description: The description of the experiment.
        :returns: UpdateExperimentResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateFeatureGroup")
    def update_feature_group(
        self,
        context: RequestContext,
        feature_group_name: FeatureGroupNameOrArn,
        feature_additions: FeatureAdditions | None = None,
        online_store_config: OnlineStoreConfigUpdate | None = None,
        throughput_config: ThroughputConfigUpdate | None = None,
        **kwargs,
    ) -> UpdateFeatureGroupResponse:
        """Updates the feature group by either adding features or updating the
        online store configuration. Use one of the following request parameters
        at a time while using the ``UpdateFeatureGroup`` API.

        You can add features for your feature group using the
        ``FeatureAdditions`` request parameter. Features cannot be removed from
        a feature group.

        You can update the online store configuration by using the
        ``OnlineStoreConfig`` request parameter. If a ``TtlDuration`` is
        specified, the default ``TtlDuration`` applies for all records added to
        the feature group *after the feature group is updated*. If a record
        level ``TtlDuration`` exists from using the ``PutRecord`` API, the
        record level ``TtlDuration`` applies to that record instead of the
        default ``TtlDuration``. To remove the default ``TtlDuration`` from an
        existing feature group, use the ``UpdateFeatureGroup`` API and set the
        ``TtlDuration`` ``Unit`` and ``Value`` to ``null``.

        :param feature_group_name: The name or Amazon Resource Name (ARN) of the feature group that you're
        updating.
        :param feature_additions: Updates the feature group.
        :param online_store_config: Updates the feature group online store configuration.
        :param throughput_config: The new throughput configuration for the feature group.
        :returns: UpdateFeatureGroupResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateFeatureMetadata")
    def update_feature_metadata(
        self,
        context: RequestContext,
        feature_group_name: FeatureGroupNameOrArn,
        feature_name: FeatureName,
        description: FeatureDescription | None = None,
        parameter_additions: FeatureParameterAdditions | None = None,
        parameter_removals: FeatureParameterRemovals | None = None,
        **kwargs,
    ) -> None:
        """Updates the description and parameters of the feature group.

        :param feature_group_name: The name or Amazon Resource Name (ARN) of the feature group containing
        the feature that you're updating.
        :param feature_name: The name of the feature that you're updating.
        :param description: A description that you can write to better describe the feature.
        :param parameter_additions: A list of key-value pairs that you can add to better describe the
        feature.
        :param parameter_removals: A list of parameter keys that you can specify to remove parameters that
        describe your feature.
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateHub")
    def update_hub(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_description: HubDescription | None = None,
        hub_display_name: HubDisplayName | None = None,
        hub_search_keywords: HubSearchKeywordList | None = None,
        **kwargs,
    ) -> UpdateHubResponse:
        """Update a hub.

        :param hub_name: The name of the hub to update.
        :param hub_description: A description of the updated hub.
        :param hub_display_name: The display name of the hub.
        :param hub_search_keywords: The searchable keywords for the hub.
        :returns: UpdateHubResponse
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateHubContent")
    def update_hub_content(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_name: HubContentName,
        hub_content_type: HubContentType,
        hub_content_version: HubContentVersion,
        hub_content_display_name: HubContentDisplayName | None = None,
        hub_content_description: HubContentDescription | None = None,
        hub_content_markdown: HubContentMarkdown | None = None,
        hub_content_search_keywords: HubContentSearchKeywordList | None = None,
        support_status: HubContentSupportStatus | None = None,
        **kwargs,
    ) -> UpdateHubContentResponse:
        """Updates SageMaker hub content (either a ``Model`` or ``Notebook``
        resource).

        You can update the metadata that describes the resource. In addition to
        the required request fields, specify at least one of the following
        fields to update:

        -  ``HubContentDescription``

        -  ``HubContentDisplayName``

        -  ``HubContentMarkdown``

        -  ``HubContentSearchKeywords``

        -  ``SupportStatus``

        For more information about hubs, see `Private curated hubs for
        foundation model access control in
        JumpStart <https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html>`__.

        If you want to update a ``ModelReference`` resource in your hub, use the
        ``UpdateHubContentResource`` API instead.

        :param hub_name: The name of the SageMaker hub that contains the hub content you want to
        update.
        :param hub_content_name: The name of the hub content resource that you want to update.
        :param hub_content_type: The content type of the resource that you want to update.
        :param hub_content_version: The hub content version that you want to update.
        :param hub_content_display_name: The display name of the hub content.
        :param hub_content_description: The description of the hub content.
        :param hub_content_markdown: A string that provides a description of the hub content.
        :param hub_content_search_keywords: The searchable keywords of the hub content.
        :param support_status: Indicates the current status of the hub content resource.
        :returns: UpdateHubContentResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("UpdateHubContentReference")
    def update_hub_content_reference(
        self,
        context: RequestContext,
        hub_name: HubNameOrArn,
        hub_content_name: HubContentName,
        hub_content_type: HubContentType,
        min_version: HubContentVersion | None = None,
        **kwargs,
    ) -> UpdateHubContentReferenceResponse:
        """Updates the contents of a SageMaker hub for a ``ModelReference``
        resource. A ``ModelReference`` allows you to access public SageMaker
        JumpStart models from within your private hub.

        When using this API, you can update the ``MinVersion`` field for
        additional flexibility in the model version. You shouldn't update any
        additional fields when using this API, because the metadata in your
        private hub should match the public JumpStart model's metadata.

        If you want to update a ``Model`` or ``Notebook`` resource in your hub,
        use the ``UpdateHubContent`` API instead.

        For more information about adding model references to your hub, see `Add
        models to a private
        hub <https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-add-models.html>`__.

        :param hub_name: The name of the SageMaker hub that contains the hub content you want to
        update.
        :param hub_content_name: The name of the hub content resource that you want to update.
        :param hub_content_type: The content type of the resource that you want to update.
        :param min_version: The minimum hub content version of the referenced model that you want to
        use.
        :returns: UpdateHubContentReferenceResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("UpdateImage")
    def update_image(
        self,
        context: RequestContext,
        image_name: ImageName,
        delete_properties: ImageDeletePropertyList | None = None,
        description: ImageDescription | None = None,
        display_name: ImageDisplayName | None = None,
        role_arn: RoleArn | None = None,
        **kwargs,
    ) -> UpdateImageResponse:
        """Updates the properties of a SageMaker AI image. To change the image's
        tags, use the
        `AddTags <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html>`__
        and
        `DeleteTags <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTags.html>`__
        APIs.

        :param image_name: The name of the image to update.
        :param delete_properties: A list of properties to delete.
        :param description: The new description for the image.
        :param display_name: The new display name for the image.
        :param role_arn: The new ARN for the IAM role that enables Amazon SageMaker AI to perform
        tasks on your behalf.
        :returns: UpdateImageResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("UpdateImageVersion")
    def update_image_version(
        self,
        context: RequestContext,
        image_name: ImageName,
        alias: SageMakerImageVersionAlias | None = None,
        version: ImageVersionNumber | None = None,
        aliases_to_add: SageMakerImageVersionAliases | None = None,
        aliases_to_delete: SageMakerImageVersionAliases | None = None,
        vendor_guidance: VendorGuidance | None = None,
        job_type: JobType | None = None,
        ml_framework: MLFramework | None = None,
        programming_lang: ProgrammingLang | None = None,
        processor: Processor | None = None,
        horovod: Horovod | None = None,
        release_notes: ReleaseNotes | None = None,
        **kwargs,
    ) -> UpdateImageVersionResponse:
        """Updates the properties of a SageMaker AI image version.

        :param image_name: The name of the image.
        :param alias: The alias of the image version.
        :param version: The version of the image.
        :param aliases_to_add: A list of aliases to add.
        :param aliases_to_delete: A list of aliases to delete.
        :param vendor_guidance: The availability of the image version specified by the maintainer.
        :param job_type: Indicates SageMaker AI job type compatibility.
        :param ml_framework: The machine learning framework vended in the image version.
        :param programming_lang: The supported programming language and its version.
        :param processor: Indicates CPU or GPU compatibility.
        :param horovod: Indicates Horovod compatibility.
        :param release_notes: The maintainer description of the image version.
        :returns: UpdateImageVersionResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        """
        raise NotImplementedError

    @handler("UpdateInferenceComponent")
    def update_inference_component(
        self,
        context: RequestContext,
        inference_component_name: InferenceComponentName,
        specification: InferenceComponentSpecification | None = None,
        runtime_config: InferenceComponentRuntimeConfig | None = None,
        deployment_config: InferenceComponentDeploymentConfig | None = None,
        **kwargs,
    ) -> UpdateInferenceComponentOutput:
        """Updates an inference component.

        :param inference_component_name: The name of the inference component.
        :param specification: Details about the resources to deploy with this inference component,
        including the model, container, and compute resources.
        :param runtime_config: Runtime settings for a model that is deployed with an inference
        component.
        :param deployment_config: The deployment configuration for the inference component.
        :returns: UpdateInferenceComponentOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateInferenceComponentRuntimeConfig")
    def update_inference_component_runtime_config(
        self,
        context: RequestContext,
        inference_component_name: InferenceComponentName,
        desired_runtime_config: InferenceComponentRuntimeConfig,
        **kwargs,
    ) -> UpdateInferenceComponentRuntimeConfigOutput:
        """Runtime settings for a model that is deployed with an inference
        component.

        :param inference_component_name: The name of the inference component to update.
        :param desired_runtime_config: Runtime settings for a model that is deployed with an inference
        component.
        :returns: UpdateInferenceComponentRuntimeConfigOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateInferenceExperiment")
    def update_inference_experiment(
        self,
        context: RequestContext,
        name: InferenceExperimentName,
        schedule: InferenceExperimentSchedule | None = None,
        description: InferenceExperimentDescription | None = None,
        model_variants: ModelVariantConfigList | None = None,
        data_storage_config: InferenceExperimentDataStorageConfig | None = None,
        shadow_mode_config: ShadowModeConfig | None = None,
        **kwargs,
    ) -> UpdateInferenceExperimentResponse:
        """Updates an inference experiment that you created. The status of the
        inference experiment has to be either ``Created``, ``Running``. For more
        information on the status of an inference experiment, see
        `DescribeInferenceExperiment <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html>`__.

        :param name: The name of the inference experiment to be updated.
        :param schedule: The duration for which the inference experiment will run.
        :param description: The description of the inference experiment.
        :param model_variants: An array of ``ModelVariantConfig`` objects.
        :param data_storage_config: The Amazon S3 location and configuration for storing inference request
        and response data.
        :param shadow_mode_config: The configuration of ``ShadowMode`` inference experiment type.
        :returns: UpdateInferenceExperimentResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateMlflowTrackingServer")
    def update_mlflow_tracking_server(
        self,
        context: RequestContext,
        tracking_server_name: TrackingServerName,
        artifact_store_uri: S3Uri | None = None,
        tracking_server_size: TrackingServerSize | None = None,
        automatic_model_registration: Boolean | None = None,
        weekly_maintenance_window_start: WeeklyMaintenanceWindowStart | None = None,
        **kwargs,
    ) -> UpdateMlflowTrackingServerResponse:
        """Updates properties of an existing MLflow Tracking Server.

        :param tracking_server_name: The name of the MLflow Tracking Server to update.
        :param artifact_store_uri: The new S3 URI for the general purpose bucket to use as the artifact
        store for the MLflow Tracking Server.
        :param tracking_server_size: The new size for the MLflow Tracking Server.
        :param automatic_model_registration: Whether to enable or disable automatic registration of new MLflow models
        to the SageMaker Model Registry.
        :param weekly_maintenance_window_start: The new weekly maintenance window start day and time to update.
        :returns: UpdateMlflowTrackingServerResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateModelCard")
    def update_model_card(
        self,
        context: RequestContext,
        model_card_name: ModelCardNameOrArn,
        content: ModelCardContent | None = None,
        model_card_status: ModelCardStatus | None = None,
        **kwargs,
    ) -> UpdateModelCardResponse:
        """Update an Amazon SageMaker Model Card.

        You cannot update both model card content and model card status in a
        single call.

        :param model_card_name: The name or Amazon Resource Name (ARN) of the model card to update.
        :param content: The updated model card content.
        :param model_card_status: The approval status of the model card within your organization.
        :returns: UpdateModelCardResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateModelPackage")
    def update_model_package(
        self,
        context: RequestContext,
        model_package_arn: ModelPackageArn,
        model_approval_status: ModelApprovalStatus | None = None,
        approval_description: ApprovalDescription | None = None,
        customer_metadata_properties: CustomerMetadataMap | None = None,
        customer_metadata_properties_to_remove: CustomerMetadataKeyList | None = None,
        additional_inference_specifications_to_add: AdditionalInferenceSpecifications | None = None,
        inference_specification: InferenceSpecification | None = None,
        source_uri: ModelPackageSourceUri | None = None,
        model_card: ModelPackageModelCard | None = None,
        model_life_cycle: ModelLifeCycle | None = None,
        client_token: ClientToken | None = None,
        **kwargs,
    ) -> UpdateModelPackageOutput:
        """Updates a versioned model.

        :param model_package_arn: The Amazon Resource Name (ARN) of the model package.
        :param model_approval_status: The approval status of the model.
        :param approval_description: A description for the approval status of the model.
        :param customer_metadata_properties: The metadata properties associated with the model package versions.
        :param customer_metadata_properties_to_remove: The metadata properties associated with the model package versions to
        remove.
        :param additional_inference_specifications_to_add: An array of additional Inference Specification objects to be added to
        the existing array additional Inference Specification.
        :param inference_specification: Specifies details about inference jobs that you can run with models
        based on this model package, including the following information:

        -  The Amazon ECR paths of containers that contain the inference code
           and model artifacts.
        :param source_uri: The URI of the source for the model package.
        :param model_card: The model card associated with the model package.
        :param model_life_cycle: A structure describing the current state of the model in its life cycle.
        :param client_token: A unique token that guarantees that the call to this API is idempotent.
        :returns: UpdateModelPackageOutput
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateMonitoringAlert")
    def update_monitoring_alert(
        self,
        context: RequestContext,
        monitoring_schedule_name: MonitoringScheduleName,
        monitoring_alert_name: MonitoringAlertName,
        datapoints_to_alert: MonitoringDatapointsToAlert,
        evaluation_period: MonitoringEvaluationPeriod,
        **kwargs,
    ) -> UpdateMonitoringAlertResponse:
        """Update the parameters of a model monitor alert.

        :param monitoring_schedule_name: The name of a monitoring schedule.
        :param monitoring_alert_name: The name of a monitoring alert.
        :param datapoints_to_alert: Within ``EvaluationPeriod``, how many execution failures will raise an
        alert.
        :param evaluation_period: The number of most recent monitoring executions to consider when
        evaluating alert status.
        :returns: UpdateMonitoringAlertResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateMonitoringSchedule")
    def update_monitoring_schedule(
        self,
        context: RequestContext,
        monitoring_schedule_name: MonitoringScheduleName,
        monitoring_schedule_config: MonitoringScheduleConfig,
        **kwargs,
    ) -> UpdateMonitoringScheduleResponse:
        """Updates a previously created schedule.

        :param monitoring_schedule_name: The name of the monitoring schedule.
        :param monitoring_schedule_config: The configuration object that specifies the monitoring schedule and
        defines the monitoring job.
        :returns: UpdateMonitoringScheduleResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateNotebookInstance")
    def update_notebook_instance(
        self,
        context: RequestContext,
        notebook_instance_name: NotebookInstanceName,
        instance_type: InstanceType | None = None,
        role_arn: RoleArn | None = None,
        lifecycle_config_name: NotebookInstanceLifecycleConfigName | None = None,
        disassociate_lifecycle_config: DisassociateNotebookInstanceLifecycleConfig | None = None,
        volume_size_in_gb: NotebookInstanceVolumeSizeInGB | None = None,
        default_code_repository: CodeRepositoryNameOrUrl | None = None,
        additional_code_repositories: AdditionalCodeRepositoryNamesOrUrls | None = None,
        accelerator_types: NotebookInstanceAcceleratorTypes | None = None,
        disassociate_accelerator_types: DisassociateNotebookInstanceAcceleratorTypes | None = None,
        disassociate_default_code_repository: DisassociateDefaultCodeRepository | None = None,
        disassociate_additional_code_repositories: DisassociateAdditionalCodeRepositories
        | None = None,
        root_access: RootAccess | None = None,
        instance_metadata_service_configuration: InstanceMetadataServiceConfiguration | None = None,
        **kwargs,
    ) -> UpdateNotebookInstanceOutput:
        """Updates a notebook instance. NotebookInstance updates include upgrading
        or downgrading the ML compute instance used for your notebook instance
        to accommodate changes in your workload requirements.

        :param notebook_instance_name: The name of the notebook instance to update.
        :param instance_type: The Amazon ML compute instance type.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that SageMaker AI can
        assume to access the notebook instance.
        :param lifecycle_config_name: The name of a lifecycle configuration to associate with the notebook
        instance.
        :param disassociate_lifecycle_config: Set to ``true`` to remove the notebook instance lifecycle configuration
        currently associated with the notebook instance.
        :param volume_size_in_gb: The size, in GB, of the ML storage volume to attach to the notebook
        instance.
        :param default_code_repository: The Git repository to associate with the notebook instance as its
        default code repository.
        :param additional_code_repositories: An array of up to three Git repositories to associate with the notebook
        instance.
        :param accelerator_types: This parameter is no longer supported.
        :param disassociate_accelerator_types: This parameter is no longer supported.
        :param disassociate_default_code_repository: The name or URL of the default Git repository to remove from this
        notebook instance.
        :param disassociate_additional_code_repositories: A list of names or URLs of the default Git repositories to remove from
        this notebook instance.
        :param root_access: Whether root access is enabled or disabled for users of the notebook
        instance.
        :param instance_metadata_service_configuration: Information on the IMDS configuration of the notebook instance.
        :returns: UpdateNotebookInstanceOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateNotebookInstanceLifecycleConfig")
    def update_notebook_instance_lifecycle_config(
        self,
        context: RequestContext,
        notebook_instance_lifecycle_config_name: NotebookInstanceLifecycleConfigName,
        on_create: NotebookInstanceLifecycleConfigList | None = None,
        on_start: NotebookInstanceLifecycleConfigList | None = None,
        **kwargs,
    ) -> UpdateNotebookInstanceLifecycleConfigOutput:
        """Updates a notebook instance lifecycle configuration created with the
        `CreateNotebookInstanceLifecycleConfig <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html>`__
        API.

        :param notebook_instance_lifecycle_config_name: The name of the lifecycle configuration.
        :param on_create: The shell script that runs only once, when you create a notebook
        instance.
        :param on_start: The shell script that runs every time you start a notebook instance,
        including when you create the notebook instance.
        :returns: UpdateNotebookInstanceLifecycleConfigOutput
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdatePartnerApp")
    def update_partner_app(
        self,
        context: RequestContext,
        arn: PartnerAppArn,
        maintenance_config: PartnerAppMaintenanceConfig | None = None,
        tier: NonEmptyString64 | None = None,
        application_config: PartnerAppConfig | None = None,
        enable_iam_session_based_identity: Boolean | None = None,
        client_token: ClientToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> UpdatePartnerAppResponse:
        """Updates all of the SageMaker Partner AI Apps in an account.

        :param arn: The ARN of the SageMaker Partner AI App to update.
        :param maintenance_config: Maintenance configuration settings for the SageMaker Partner AI App.
        :param tier: Indicates the instance type and size of the cluster attached to the
        SageMaker Partner AI App.
        :param application_config: Configuration settings for the SageMaker Partner AI App.
        :param enable_iam_session_based_identity: When set to ``TRUE``, the SageMaker Partner AI App sets the Amazon Web
        Services IAM session name or the authenticated IAM user as the identity
        of the SageMaker Partner AI App user.
        :param client_token: A unique token that guarantees that the call to this API is idempotent.
        :param tags: Each tag consists of a key and an optional value.
        :returns: UpdatePartnerAppResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdatePipeline")
    def update_pipeline(
        self,
        context: RequestContext,
        pipeline_name: PipelineName,
        pipeline_display_name: PipelineName | None = None,
        pipeline_definition: PipelineDefinition | None = None,
        pipeline_definition_s3_location: PipelineDefinitionS3Location | None = None,
        pipeline_description: PipelineDescription | None = None,
        role_arn: RoleArn | None = None,
        parallelism_configuration: ParallelismConfiguration | None = None,
        **kwargs,
    ) -> UpdatePipelineResponse:
        """Updates a pipeline.

        :param pipeline_name: The name of the pipeline to update.
        :param pipeline_display_name: The display name of the pipeline.
        :param pipeline_definition: The JSON pipeline definition.
        :param pipeline_definition_s3_location: The location of the pipeline definition stored in Amazon S3.
        :param pipeline_description: The description of the pipeline.
        :param role_arn: The Amazon Resource Name (ARN) that the pipeline uses to execute.
        :param parallelism_configuration: If specified, it applies to all executions of this pipeline by default.
        :returns: UpdatePipelineResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdatePipelineExecution")
    def update_pipeline_execution(
        self,
        context: RequestContext,
        pipeline_execution_arn: PipelineExecutionArn,
        pipeline_execution_description: PipelineExecutionDescription | None = None,
        pipeline_execution_display_name: PipelineExecutionName | None = None,
        parallelism_configuration: ParallelismConfiguration | None = None,
        **kwargs,
    ) -> UpdatePipelineExecutionResponse:
        """Updates a pipeline execution.

        :param pipeline_execution_arn: The Amazon Resource Name (ARN) of the pipeline execution.
        :param pipeline_execution_description: The description of the pipeline execution.
        :param pipeline_execution_display_name: The display name of the pipeline execution.
        :param parallelism_configuration: This configuration, if specified, overrides the parallelism
        configuration of the parent pipeline for this specific run.
        :returns: UpdatePipelineExecutionResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateProject")
    def update_project(
        self,
        context: RequestContext,
        project_name: ProjectEntityName,
        project_description: EntityDescription | None = None,
        service_catalog_provisioning_update_details: ServiceCatalogProvisioningUpdateDetails
        | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> UpdateProjectOutput:
        """Updates a machine learning (ML) project that is created from a template
        that sets up an ML pipeline from training to deploying an approved
        model.

        You must not update a project that is in use. If you update the
        ``ServiceCatalogProvisioningUpdateDetails`` of a project that is active
        or being created, or updated, you may lose resources already created by
        the project.

        :param project_name: The name of the project.
        :param project_description: The description for the project.
        :param service_catalog_provisioning_update_details: The product ID and provisioning artifact ID to provision a service
        catalog.
        :param tags: An array of key-value pairs.
        :returns: UpdateProjectOutput
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateSpace")
    def update_space(
        self,
        context: RequestContext,
        domain_id: DomainId,
        space_name: SpaceName,
        space_settings: SpaceSettings | None = None,
        space_display_name: NonEmptyString64 | None = None,
        **kwargs,
    ) -> UpdateSpaceResponse:
        """Updates the settings of a space.

        You can't edit the app type of a space in the ``SpaceSettings``.

        :param domain_id: The ID of the associated domain.
        :param space_name: The name of the space.
        :param space_settings: A collection of space settings.
        :param space_display_name: The name of the space that appears in the Amazon SageMaker Studio UI.
        :returns: UpdateSpaceResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateTrainingJob")
    def update_training_job(
        self,
        context: RequestContext,
        training_job_name: TrainingJobName,
        profiler_config: ProfilerConfigForUpdate | None = None,
        profiler_rule_configurations: ProfilerRuleConfigurations | None = None,
        resource_config: ResourceConfigForUpdate | None = None,
        remote_debug_config: RemoteDebugConfigForUpdate | None = None,
        **kwargs,
    ) -> UpdateTrainingJobResponse:
        """Update a model training job to request a new Debugger profiling
        configuration or to change warm pool retention length.

        :param training_job_name: The name of a training job to update the Debugger profiling
        configuration.
        :param profiler_config: Configuration information for Amazon SageMaker Debugger system
        monitoring, framework profiling, and storage paths.
        :param profiler_rule_configurations: Configuration information for Amazon SageMaker Debugger rules for
        profiling system and framework metrics.
        :param resource_config: The training job ``ResourceConfig`` to update warm pool retention
        length.
        :param remote_debug_config: Configuration for remote debugging while the training job is running.
        :returns: UpdateTrainingJobResponse
        :raises ResourceNotFound:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateTrial")
    def update_trial(
        self,
        context: RequestContext,
        trial_name: ExperimentEntityName,
        display_name: ExperimentEntityName | None = None,
        **kwargs,
    ) -> UpdateTrialResponse:
        """Updates the display name of a trial.

        :param trial_name: The name of the trial to update.
        :param display_name: The name of the trial as displayed.
        :returns: UpdateTrialResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateTrialComponent")
    def update_trial_component(
        self,
        context: RequestContext,
        trial_component_name: ExperimentEntityName,
        display_name: ExperimentEntityName | None = None,
        status: TrialComponentStatus | None = None,
        start_time: Timestamp | None = None,
        end_time: Timestamp | None = None,
        parameters: TrialComponentParameters | None = None,
        parameters_to_remove: ListTrialComponentKey256 | None = None,
        input_artifacts: TrialComponentArtifacts | None = None,
        input_artifacts_to_remove: ListTrialComponentKey256 | None = None,
        output_artifacts: TrialComponentArtifacts | None = None,
        output_artifacts_to_remove: ListTrialComponentKey256 | None = None,
        **kwargs,
    ) -> UpdateTrialComponentResponse:
        """Updates one or more properties of a trial component.

        :param trial_component_name: The name of the component to update.
        :param display_name: The name of the component as displayed.
        :param status: The new status of the component.
        :param start_time: When the component started.
        :param end_time: When the component ended.
        :param parameters: Replaces all of the component's hyperparameters with the specified
        hyperparameters or add new hyperparameters.
        :param parameters_to_remove: The hyperparameters to remove from the component.
        :param input_artifacts: Replaces all of the component's input artifacts with the specified
        artifacts or adds new input artifacts.
        :param input_artifacts_to_remove: The input artifacts to remove from the component.
        :param output_artifacts: Replaces all of the component's output artifacts with the specified
        artifacts or adds new output artifacts.
        :param output_artifacts_to_remove: The output artifacts to remove from the component.
        :returns: UpdateTrialComponentResponse
        :raises ConflictException:
        :raises ResourceNotFound:
        """
        raise NotImplementedError

    @handler("UpdateUserProfile")
    def update_user_profile(
        self,
        context: RequestContext,
        domain_id: DomainId,
        user_profile_name: UserProfileName,
        user_settings: UserSettings | None = None,
        **kwargs,
    ) -> UpdateUserProfileResponse:
        """Updates a user profile.

        :param domain_id: The domain ID.
        :param user_profile_name: The user profile name.
        :param user_settings: A collection of settings.
        :returns: UpdateUserProfileResponse
        :raises ResourceNotFound:
        :raises ResourceInUse:
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError

    @handler("UpdateWorkforce")
    def update_workforce(
        self,
        context: RequestContext,
        workforce_name: WorkforceName,
        source_ip_config: SourceIpConfig | None = None,
        oidc_config: OidcConfig | None = None,
        workforce_vpc_config: WorkforceVpcConfigRequest | None = None,
        **kwargs,
    ) -> UpdateWorkforceResponse:
        """Use this operation to update your workforce. You can use this operation
        to require that workers use specific IP addresses to work on tasks and
        to update your OpenID Connect (OIDC) Identity Provider (IdP) workforce
        configuration.

        The worker portal is now supported in VPC and public internet.

        Use ``SourceIpConfig`` to restrict worker access to tasks to a specific
        range of IP addresses. You specify allowed IP addresses by creating a
        list of up to ten
        `CIDRs <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__.
        By default, a workforce isn't restricted to specific IP addresses. If
        you specify a range of IP addresses, workers who attempt to access tasks
        using any IP address outside the specified range are denied and get a
        ``Not Found`` error message on the worker portal.

        To restrict access to all the workers in public internet, add the
        ``SourceIpConfig`` CIDR value as "10.0.0.0/16".

        Amazon SageMaker does not support Source Ip restriction for worker
        portals in VPC.

        Use ``OidcConfig`` to update the configuration of a workforce created
        using your own OIDC IdP.

        You can only update your OIDC IdP configuration when there are no work
        teams associated with your workforce. You can delete work teams using
        the
        `DeleteWorkteam <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html>`__
        operation.

        After restricting access to a range of IP addresses or updating your
        OIDC IdP configuration with this operation, you can view details about
        your update workforce using the
        `DescribeWorkforce <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkforce.html>`__
        operation.

        This operation only applies to private workforces.

        :param workforce_name: The name of the private workforce that you want to update.
        :param source_ip_config: A list of one to ten worker IP address ranges
        (`CIDRs <https://docs.
        :param oidc_config: Use this parameter to update your OIDC Identity Provider (IdP)
        configuration for a workforce made using your own IdP.
        :param workforce_vpc_config: Use this parameter to update your VPC configuration for a workforce.
        :returns: UpdateWorkforceResponse
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("UpdateWorkteam")
    def update_workteam(
        self,
        context: RequestContext,
        workteam_name: WorkteamName,
        member_definitions: MemberDefinitions | None = None,
        description: String200 | None = None,
        notification_configuration: NotificationConfiguration | None = None,
        worker_access_configuration: WorkerAccessConfiguration | None = None,
        **kwargs,
    ) -> UpdateWorkteamResponse:
        """Updates an existing work team with new member definitions or
        description.

        :param workteam_name: The name of the work team to update.
        :param member_definitions: A list of ``MemberDefinition`` objects that contains objects that
        identify the workers that make up the work team.
        :param description: An updated description for the work team.
        :param notification_configuration: Configures SNS topic notifications for available or expiring work items.
        :param worker_access_configuration: Use this optional parameter to constrain access to an Amazon S3 resource
        based on the IP address using supported IAM global condition keys.
        :returns: UpdateWorkteamResponse
        :raises ResourceLimitExceeded:
        """
        raise NotImplementedError
