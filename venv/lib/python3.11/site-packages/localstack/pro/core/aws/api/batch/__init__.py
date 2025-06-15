from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Boolean = bool
ClientRequestToken = str
Float = float
ImageIdOverride = str
ImageType = str
Integer = int
KubernetesVersion = str
Quantity = str
String = str
TagKey = str
TagValue = str


class ArrayJobDependency(StrEnum):
    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


class AssignPublicIp(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEState(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CEStatus(StrEnum):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class CEType(StrEnum):
    MANAGED = "MANAGED"
    UNMANAGED = "UNMANAGED"


class CRAllocationStrategy(StrEnum):
    BEST_FIT = "BEST_FIT"
    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"


class CRType(StrEnum):
    EC2 = "EC2"
    SPOT = "SPOT"
    FARGATE = "FARGATE"
    FARGATE_SPOT = "FARGATE_SPOT"


class CRUpdateAllocationStrategy(StrEnum):
    BEST_FIT_PROGRESSIVE = "BEST_FIT_PROGRESSIVE"
    SPOT_CAPACITY_OPTIMIZED = "SPOT_CAPACITY_OPTIMIZED"
    SPOT_PRICE_CAPACITY_OPTIMIZED = "SPOT_PRICE_CAPACITY_OPTIMIZED"


class DeviceCgroupPermission(StrEnum):
    READ = "READ"
    WRITE = "WRITE"
    MKNOD = "MKNOD"


class EFSAuthorizationConfigIAM(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EFSTransitEncryption(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FirelensConfigurationType(StrEnum):
    fluentd = "fluentd"
    fluentbit = "fluentbit"


class JQState(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class JQStatus(StrEnum):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    VALID = "VALID"
    INVALID = "INVALID"


class JobDefinitionType(StrEnum):
    container = "container"
    multinode = "multinode"


class JobStateTimeLimitActionsAction(StrEnum):
    CANCEL = "CANCEL"


class JobStateTimeLimitActionsState(StrEnum):
    RUNNABLE = "RUNNABLE"


class JobStatus(StrEnum):
    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    RUNNABLE = "RUNNABLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class LogDriver(StrEnum):
    json_file = "json-file"
    syslog = "syslog"
    journald = "journald"
    gelf = "gelf"
    fluentd = "fluentd"
    awslogs = "awslogs"
    splunk = "splunk"
    awsfirelens = "awsfirelens"


class OrchestrationType(StrEnum):
    ECS = "ECS"
    EKS = "EKS"


class PlatformCapability(StrEnum):
    EC2 = "EC2"
    FARGATE = "FARGATE"


class ResourceType(StrEnum):
    GPU = "GPU"
    VCPU = "VCPU"
    MEMORY = "MEMORY"


class RetryAction(StrEnum):
    RETRY = "RETRY"
    EXIT = "EXIT"


class ClientException(ServiceException):
    """These errors are usually caused by a client action. One example cause is
    using an action or resource on behalf of a user that doesn't have
    permissions to use the action or resource. Another cause is specifying
    an identifier that's not valid.
    """

    code: str = "ClientException"
    sender_fault: bool = False
    status_code: int = 400


class ServerException(ServiceException):
    """These errors are usually caused by a server issue."""

    code: str = "ServerException"
    sender_fault: bool = False
    status_code: int = 500


ArrayJobStatusSummary = Dict[String, Integer]


class ArrayProperties(TypedDict, total=False):
    """An object that represents an Batch array job."""

    size: Optional[Integer]


class ArrayPropertiesDetail(TypedDict, total=False):
    """An object that represents the array properties of a job."""

    statusSummary: Optional[ArrayJobStatusSummary]
    size: Optional[Integer]
    index: Optional[Integer]


class ArrayPropertiesSummary(TypedDict, total=False):
    """An object that represents the array properties of a job."""

    size: Optional[Integer]
    index: Optional[Integer]


class NetworkInterface(TypedDict, total=False):
    """An object that represents the elastic network interface for a multi-node
    parallel job node.
    """

    attachmentId: Optional[String]
    ipv6Address: Optional[String]
    privateIpv4Address: Optional[String]


NetworkInterfaceList = List[NetworkInterface]


class AttemptContainerDetail(TypedDict, total=False):
    """An object that represents the details of a container that's part of a
    job attempt.
    """

    containerInstanceArn: Optional[String]
    taskArn: Optional[String]
    exitCode: Optional[Integer]
    reason: Optional[String]
    logStreamName: Optional[String]
    networkInterfaces: Optional[NetworkInterfaceList]


class AttemptTaskContainerDetails(TypedDict, total=False):
    """An object that represents the details of a container that's part of a
    job attempt.
    """

    exitCode: Optional[Integer]
    name: Optional[String]
    reason: Optional[String]
    logStreamName: Optional[String]
    networkInterfaces: Optional[NetworkInterfaceList]


ListAttemptTaskContainerDetails = List[AttemptTaskContainerDetails]


class AttemptEcsTaskDetails(TypedDict, total=False):
    """An object that represents the details of a task."""

    containerInstanceArn: Optional[String]
    taskArn: Optional[String]
    containers: Optional[ListAttemptTaskContainerDetails]


ListAttemptEcsTaskDetails = List[AttemptEcsTaskDetails]
Long = int


class AttemptDetail(TypedDict, total=False):
    """An object that represents a job attempt."""

    container: Optional[AttemptContainerDetail]
    startedAt: Optional[Long]
    stoppedAt: Optional[Long]
    statusReason: Optional[String]
    taskProperties: Optional[ListAttemptEcsTaskDetails]


AttemptDetails = List[AttemptDetail]


class CancelJobRequest(ServiceRequest):
    """Contains the parameters for ``CancelJob``."""

    jobId: String
    reason: String


class CancelJobResponse(TypedDict, total=False):
    pass


class EksConfiguration(TypedDict, total=False):
    """Configuration for the Amazon EKS cluster that supports the Batch compute
    environment. The cluster must exist before the compute environment can
    be created.
    """

    eksClusterArn: String
    kubernetesNamespace: String


JobExecutionTimeoutMinutes = int


class UpdatePolicy(TypedDict, total=False):
    """Specifies the infrastructure update policy for the Amazon EC2 compute
    environment. For more information about infrastructure updates, see
    `Updating compute
    environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`__
    in the *Batch User Guide*.
    """

    terminateJobsOnUpdate: Optional[Boolean]
    jobExecutionTimeoutMinutes: Optional[JobExecutionTimeoutMinutes]


class Ec2Configuration(TypedDict, total=False):
    """Provides information used to select Amazon Machine Images (AMIs) for
    instances in the compute environment. If ``Ec2Configuration`` isn't
    specified, the default is ``ECS_AL2`` (`Amazon Linux
    2 <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#al2ami>`__).

    This object isn't applicable to jobs that are running on Fargate
    resources.
    """

    imageType: ImageType
    imageIdOverride: Optional[ImageIdOverride]
    imageKubernetesVersion: Optional[KubernetesVersion]


Ec2ConfigurationList = List[Ec2Configuration]
StringList = List[String]


class LaunchTemplateSpecificationOverride(TypedDict, total=False):
    """An object that represents a launch template to use in place of the
    default launch template. You must specify either the launch template ID
    or launch template name in the request, but not both.

    If security groups are specified using both the ``securityGroupIds``
    parameter of ``CreateComputeEnvironment`` and the launch template, the
    values in the ``securityGroupIds`` parameter of
    ``CreateComputeEnvironment`` will be used.

    You can define up to ten (10) overrides for each compute environment.

    This object isn't applicable to jobs that are running on Fargate
    resources.

    To unset all override templates for a compute environment, you can pass
    an empty array to the
    `UpdateComputeEnvironment.overrides <https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html>`__
    parameter, or not include the ``overrides`` parameter when submitting
    the ``UpdateComputeEnvironment`` API operation.
    """

    launchTemplateId: Optional[String]
    launchTemplateName: Optional[String]
    version: Optional[String]
    targetInstanceTypes: Optional[StringList]


LaunchTemplateSpecificationOverrideList = List[LaunchTemplateSpecificationOverride]


class LaunchTemplateSpecification(TypedDict, total=False):
    """An object that represents a launch template that's associated with a
    compute resource. You must specify either the launch template ID or
    launch template name in the request, but not both.

    If security groups are specified using both the ``securityGroupIds``
    parameter of ``CreateComputeEnvironment`` and the launch template, the
    values in the ``securityGroupIds`` parameter of
    ``CreateComputeEnvironment`` will be used.

    This object isn't applicable to jobs that are running on Fargate
    resources.
    """

    launchTemplateId: Optional[String]
    launchTemplateName: Optional[String]
    version: Optional[String]
    overrides: Optional[LaunchTemplateSpecificationOverrideList]


TagsMap = Dict[String, String]
ComputeResource = TypedDict(
    "ComputeResource",
    {
        "type": CRType,
        "allocationStrategy": Optional[CRAllocationStrategy],
        "minvCpus": Optional[Integer],
        "maxvCpus": Integer,
        "desiredvCpus": Optional[Integer],
        "instanceTypes": Optional[StringList],
        "imageId": Optional[String],
        "subnets": StringList,
        "securityGroupIds": Optional[StringList],
        "ec2KeyPair": Optional[String],
        "instanceRole": Optional[String],
        "tags": Optional[TagsMap],
        "placementGroup": Optional[String],
        "bidPercentage": Optional[Integer],
        "spotIamFleetRole": Optional[String],
        "launchTemplate": Optional[LaunchTemplateSpecification],
        "ec2Configuration": Optional[Ec2ConfigurationList],
    },
    total=False,
)
TagrisTagsMap = Dict[TagKey, TagValue]
ComputeEnvironmentDetail = TypedDict(
    "ComputeEnvironmentDetail",
    {
        "computeEnvironmentName": String,
        "computeEnvironmentArn": String,
        "unmanagedvCpus": Optional[Integer],
        "ecsClusterArn": Optional[String],
        "tags": Optional[TagrisTagsMap],
        "type": Optional[CEType],
        "state": Optional[CEState],
        "status": Optional[CEStatus],
        "statusReason": Optional[String],
        "computeResources": Optional[ComputeResource],
        "serviceRole": Optional[String],
        "updatePolicy": Optional[UpdatePolicy],
        "eksConfiguration": Optional[EksConfiguration],
        "containerOrchestrationType": Optional[OrchestrationType],
        "uuid": Optional[String],
        "context": Optional[String],
    },
    total=False,
)
ComputeEnvironmentDetailList = List[ComputeEnvironmentDetail]


class ComputeEnvironmentOrder(TypedDict, total=False):
    """The order that compute environments are tried in for job placement
    within a queue. Compute environments are tried in ascending order. For
    example, if two compute environments are associated with a job queue,
    the compute environment with a lower order integer value is tried for
    job placement first. Compute environments must be in the ``VALID`` state
    before you can associate them with a job queue. All of the compute
    environments must be either EC2 (``EC2`` or ``SPOT``) or Fargate
    (``FARGATE`` or ``FARGATE_SPOT``); Amazon EC2 and Fargate compute
    environments can't be mixed.

    All compute environments that are associated with a job queue must share
    the same architecture. Batch doesn't support mixing compute environment
    architecture types in a single job queue.
    """

    order: Integer
    computeEnvironment: String


ComputeEnvironmentOrders = List[ComputeEnvironmentOrder]
ComputeResourceUpdate = TypedDict(
    "ComputeResourceUpdate",
    {
        "minvCpus": Optional[Integer],
        "maxvCpus": Optional[Integer],
        "desiredvCpus": Optional[Integer],
        "subnets": Optional[StringList],
        "securityGroupIds": Optional[StringList],
        "allocationStrategy": Optional[CRUpdateAllocationStrategy],
        "instanceTypes": Optional[StringList],
        "ec2KeyPair": Optional[String],
        "instanceRole": Optional[String],
        "tags": Optional[TagsMap],
        "placementGroup": Optional[String],
        "bidPercentage": Optional[Integer],
        "launchTemplate": Optional[LaunchTemplateSpecification],
        "ec2Configuration": Optional[Ec2ConfigurationList],
        "updateToLatestImageVersion": Optional[Boolean],
        "type": Optional[CRType],
        "imageId": Optional[String],
    },
    total=False,
)


class ConsumableResourceRequirement(TypedDict, total=False):
    """Information about a consumable resource required to run a job."""

    consumableResource: Optional[String]
    quantity: Optional[Long]


ConsumableResourceList = List[ConsumableResourceRequirement]


class ConsumableResourceProperties(TypedDict, total=False):
    """Contains a list of consumable resources required by a job."""

    consumableResourceList: Optional[ConsumableResourceList]


class ConsumableResourceSummary(TypedDict, total=False):
    """Current information about a consumable resource."""

    consumableResourceArn: String
    consumableResourceName: String
    totalQuantity: Optional[Long]
    inUseQuantity: Optional[Long]
    resourceType: Optional[String]


ConsumableResourceSummaryList = List[ConsumableResourceSummary]


class RepositoryCredentials(TypedDict, total=False):
    """The repository credentials for private registry authentication."""

    credentialsParameter: String


class RuntimePlatform(TypedDict, total=False):
    """An object that represents the compute environment architecture for Batch
    jobs on Fargate.
    """

    operatingSystemFamily: Optional[String]
    cpuArchitecture: Optional[String]


class EphemeralStorage(TypedDict, total=False):
    """The amount of ephemeral storage to allocate for the task. This parameter
    is used to expand the total amount of ephemeral storage available,
    beyond the default amount, for tasks hosted on Fargate.
    """

    sizeInGiB: Integer


class FargatePlatformConfiguration(TypedDict, total=False):
    """The platform configuration for jobs that are running on Fargate
    resources. Jobs that run on Amazon EC2 resources must not specify this
    parameter.
    """

    platformVersion: Optional[String]


class NetworkConfiguration(TypedDict, total=False):
    """The network configuration for jobs that are running on Fargate
    resources. Jobs that are running on Amazon EC2 resources must not
    specify this parameter.
    """

    assignPublicIp: Optional[AssignPublicIp]


class Secret(TypedDict, total=False):
    """An object that represents the secret to expose to your container.
    Secrets can be exposed to a container in the following ways:

    -  To inject sensitive data into your containers as environment
       variables, use the ``secrets`` container definition parameter.

    -  To reference sensitive information in the log configuration of a
       container, use the ``secretOptions`` container definition parameter.

    For more information, see `Specifying sensitive
    data <https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html>`__
    in the *Batch User Guide*.
    """

    name: String
    valueFrom: String


SecretList = List[Secret]
LogConfigurationOptionsMap = Dict[String, String]


class LogConfiguration(TypedDict, total=False):
    """Log configuration options to send to a custom log driver for the
    container.
    """

    logDriver: LogDriver
    options: Optional[LogConfigurationOptionsMap]
    secretOptions: Optional[SecretList]


class Tmpfs(TypedDict, total=False):
    """The container path, mount options, and size of the ``tmpfs`` mount.

    This object isn't applicable to jobs that are running on Fargate
    resources.
    """

    containerPath: String
    size: Integer
    mountOptions: Optional[StringList]


TmpfsList = List[Tmpfs]
DeviceCgroupPermissions = List[DeviceCgroupPermission]


class Device(TypedDict, total=False):
    """An object that represents a container instance host device.

    This object isn't applicable to jobs that are running on Fargate
    resources and shouldn't be provided.
    """

    hostPath: String
    containerPath: Optional[String]
    permissions: Optional[DeviceCgroupPermissions]


DevicesList = List[Device]


class LinuxParameters(TypedDict, total=False):
    """Linux-specific modifications that are applied to the container, such as
    details for device mappings.
    """

    devices: Optional[DevicesList]
    initProcessEnabled: Optional[Boolean]
    sharedMemorySize: Optional[Integer]
    tmpfs: Optional[TmpfsList]
    maxSwap: Optional[Integer]
    swappiness: Optional[Integer]


ResourceRequirement = TypedDict(
    "ResourceRequirement",
    {
        "value": String,
        "type": ResourceType,
    },
    total=False,
)
ResourceRequirements = List[ResourceRequirement]


class Ulimit(TypedDict, total=False):
    """The ``ulimit`` settings to pass to the container. For more information,
    see
    `Ulimit <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html>`__.

    This object isn't applicable to jobs that are running on Fargate
    resources.
    """

    hardLimit: Integer
    name: String
    softLimit: Integer


Ulimits = List[Ulimit]


class MountPoint(TypedDict, total=False):
    """Details for a Docker volume mount point that's used in a job's container
    properties. This parameter maps to ``Volumes`` in the `Create a
    container <https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerCreate>`__
    section of the *Docker Remote API* and the ``--volume`` option to docker
    run.
    """

    containerPath: Optional[String]
    readOnly: Optional[Boolean]
    sourceVolume: Optional[String]


MountPoints = List[MountPoint]


class KeyValuePair(TypedDict, total=False):
    """A key-value pair object."""

    name: Optional[String]
    value: Optional[String]


EnvironmentVariables = List[KeyValuePair]


class EFSAuthorizationConfig(TypedDict, total=False):
    """The authorization configuration details for the Amazon EFS file system."""

    accessPointId: Optional[String]
    iam: Optional[EFSAuthorizationConfigIAM]


class EFSVolumeConfiguration(TypedDict, total=False):
    """This is used when you're using an Amazon Elastic File System file system
    for job storage. For more information, see `Amazon EFS
    Volumes <https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html>`__
    in the *Batch User Guide*.
    """

    fileSystemId: String
    rootDirectory: Optional[String]
    transitEncryption: Optional[EFSTransitEncryption]
    transitEncryptionPort: Optional[Integer]
    authorizationConfig: Optional[EFSAuthorizationConfig]


class Host(TypedDict, total=False):
    """Determine whether your data volume persists on the host container
    instance and where it's stored. If this parameter is empty, then the
    Docker daemon assigns a host path for your data volume. However, the
    data isn't guaranteed to persist after the containers that are
    associated with it stop running.
    """

    sourcePath: Optional[String]


class Volume(TypedDict, total=False):
    """A data volume that's used in a job's container properties."""

    host: Optional[Host]
    name: Optional[String]
    efsVolumeConfiguration: Optional[EFSVolumeConfiguration]


Volumes = List[Volume]


class ContainerDetail(TypedDict, total=False):
    """An object that represents the details of a container that's part of a
    job.
    """

    image: Optional[String]
    vcpus: Optional[Integer]
    memory: Optional[Integer]
    command: Optional[StringList]
    jobRoleArn: Optional[String]
    executionRoleArn: Optional[String]
    volumes: Optional[Volumes]
    environment: Optional[EnvironmentVariables]
    mountPoints: Optional[MountPoints]
    readonlyRootFilesystem: Optional[Boolean]
    ulimits: Optional[Ulimits]
    privileged: Optional[Boolean]
    user: Optional[String]
    exitCode: Optional[Integer]
    reason: Optional[String]
    containerInstanceArn: Optional[String]
    taskArn: Optional[String]
    logStreamName: Optional[String]
    instanceType: Optional[String]
    networkInterfaces: Optional[NetworkInterfaceList]
    resourceRequirements: Optional[ResourceRequirements]
    linuxParameters: Optional[LinuxParameters]
    logConfiguration: Optional[LogConfiguration]
    secrets: Optional[SecretList]
    networkConfiguration: Optional[NetworkConfiguration]
    fargatePlatformConfiguration: Optional[FargatePlatformConfiguration]
    ephemeralStorage: Optional[EphemeralStorage]
    runtimePlatform: Optional[RuntimePlatform]
    repositoryCredentials: Optional[RepositoryCredentials]
    enableExecuteCommand: Optional[Boolean]


class ContainerOverrides(TypedDict, total=False):
    """The overrides that should be sent to a container.

    For information about using Batch overrides when you connect event
    sources to targets, see
    `BatchContainerOverrides <https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html>`__.
    """

    vcpus: Optional[Integer]
    memory: Optional[Integer]
    command: Optional[StringList]
    instanceType: Optional[String]
    environment: Optional[EnvironmentVariables]
    resourceRequirements: Optional[ResourceRequirements]


class ContainerProperties(TypedDict, total=False):
    """Container properties are used for Amazon ECS based job definitions.
    These properties to describe the container that's launched as part of a
    job.
    """

    image: Optional[String]
    vcpus: Optional[Integer]
    memory: Optional[Integer]
    command: Optional[StringList]
    jobRoleArn: Optional[String]
    executionRoleArn: Optional[String]
    volumes: Optional[Volumes]
    environment: Optional[EnvironmentVariables]
    mountPoints: Optional[MountPoints]
    readonlyRootFilesystem: Optional[Boolean]
    privileged: Optional[Boolean]
    ulimits: Optional[Ulimits]
    user: Optional[String]
    instanceType: Optional[String]
    resourceRequirements: Optional[ResourceRequirements]
    linuxParameters: Optional[LinuxParameters]
    logConfiguration: Optional[LogConfiguration]
    secrets: Optional[SecretList]
    networkConfiguration: Optional[NetworkConfiguration]
    fargatePlatformConfiguration: Optional[FargatePlatformConfiguration]
    enableExecuteCommand: Optional[Boolean]
    ephemeralStorage: Optional[EphemeralStorage]
    runtimePlatform: Optional[RuntimePlatform]
    repositoryCredentials: Optional[RepositoryCredentials]


class ContainerSummary(TypedDict, total=False):
    """An object that represents summary details of a container within a job."""

    exitCode: Optional[Integer]
    reason: Optional[String]


CreateComputeEnvironmentRequest = TypedDict(
    "CreateComputeEnvironmentRequest",
    {
        "computeEnvironmentName": String,
        "type": CEType,
        "state": Optional[CEState],
        "unmanagedvCpus": Optional[Integer],
        "computeResources": Optional[ComputeResource],
        "serviceRole": Optional[String],
        "tags": Optional[TagrisTagsMap],
        "eksConfiguration": Optional[EksConfiguration],
        "context": Optional[String],
    },
    total=False,
)


class CreateComputeEnvironmentResponse(TypedDict, total=False):
    computeEnvironmentName: Optional[String]
    computeEnvironmentArn: Optional[String]


class CreateConsumableResourceRequest(ServiceRequest):
    consumableResourceName: String
    totalQuantity: Optional[Long]
    resourceType: Optional[String]
    tags: Optional[TagrisTagsMap]


class CreateConsumableResourceResponse(TypedDict, total=False):
    consumableResourceName: String
    consumableResourceArn: String


class JobStateTimeLimitAction(TypedDict, total=False):
    """Specifies an action that Batch will take after the job has remained at
    the head of the queue in the specified state for longer than the
    specified time.
    """

    reason: String
    state: JobStateTimeLimitActionsState
    maxTimeSeconds: Integer
    action: JobStateTimeLimitActionsAction


JobStateTimeLimitActions = List[JobStateTimeLimitAction]


class CreateJobQueueRequest(ServiceRequest):
    """Contains the parameters for ``CreateJobQueue``."""

    jobQueueName: String
    state: Optional[JQState]
    schedulingPolicyArn: Optional[String]
    priority: Integer
    computeEnvironmentOrder: ComputeEnvironmentOrders
    tags: Optional[TagrisTagsMap]
    jobStateTimeLimitActions: Optional[JobStateTimeLimitActions]


class CreateJobQueueResponse(TypedDict, total=False):
    jobQueueName: String
    jobQueueArn: String


class ShareAttributes(TypedDict, total=False):
    """Specifies the weights for the share identifiers for the fair-share
    policy. Share identifiers that aren't included have a default weight of
    ``1.0``.
    """

    shareIdentifier: String
    weightFactor: Optional[Float]


ShareAttributesList = List[ShareAttributes]


class FairsharePolicy(TypedDict, total=False):
    """The fair-share scheduling policy details."""

    shareDecaySeconds: Optional[Integer]
    computeReservation: Optional[Integer]
    shareDistribution: Optional[ShareAttributesList]


class CreateSchedulingPolicyRequest(ServiceRequest):
    """Contains the parameters for ``CreateSchedulingPolicy``."""

    name: String
    fairsharePolicy: Optional[FairsharePolicy]
    tags: Optional[TagrisTagsMap]


class CreateSchedulingPolicyResponse(TypedDict, total=False):
    name: String
    arn: String


class DeleteComputeEnvironmentRequest(ServiceRequest):
    """Contains the parameters for ``DeleteComputeEnvironment``."""

    computeEnvironment: String


class DeleteComputeEnvironmentResponse(TypedDict, total=False):
    pass


class DeleteConsumableResourceRequest(ServiceRequest):
    consumableResource: String


class DeleteConsumableResourceResponse(TypedDict, total=False):
    pass


class DeleteJobQueueRequest(ServiceRequest):
    """Contains the parameters for ``DeleteJobQueue``."""

    jobQueue: String


class DeleteJobQueueResponse(TypedDict, total=False):
    pass


class DeleteSchedulingPolicyRequest(ServiceRequest):
    """Contains the parameters for ``DeleteSchedulingPolicy``."""

    arn: String


class DeleteSchedulingPolicyResponse(TypedDict, total=False):
    pass


class DeregisterJobDefinitionRequest(ServiceRequest):
    jobDefinition: String


class DeregisterJobDefinitionResponse(TypedDict, total=False):
    pass


class DescribeComputeEnvironmentsRequest(ServiceRequest):
    """Contains the parameters for ``DescribeComputeEnvironments``."""

    computeEnvironments: Optional[StringList]
    maxResults: Optional[Integer]
    nextToken: Optional[String]


class DescribeComputeEnvironmentsResponse(TypedDict, total=False):
    computeEnvironments: Optional[ComputeEnvironmentDetailList]
    nextToken: Optional[String]


class DescribeConsumableResourceRequest(ServiceRequest):
    consumableResource: String


class DescribeConsumableResourceResponse(TypedDict, total=False):
    consumableResourceName: String
    consumableResourceArn: String
    totalQuantity: Optional[Long]
    inUseQuantity: Optional[Long]
    availableQuantity: Optional[Long]
    resourceType: Optional[String]
    createdAt: Optional[Long]
    tags: Optional[TagrisTagsMap]


class DescribeJobDefinitionsRequest(ServiceRequest):
    """Contains the parameters for ``DescribeJobDefinitions``."""

    jobDefinitions: Optional[StringList]
    maxResults: Optional[Integer]
    jobDefinitionName: Optional[String]
    status: Optional[String]
    nextToken: Optional[String]


EksAnnotationsMap = Dict[String, String]
EksLabelsMap = Dict[String, String]


class EksMetadata(TypedDict, total=False):
    """Describes and uniquely identifies Kubernetes resources. For example, the
    compute environment that a pod runs in or the ``jobID`` for a job
    running in the pod. For more information, see `Understanding Kubernetes
    Objects <https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/>`__
    in the *Kubernetes documentation*.
    """

    labels: Optional[EksLabelsMap]
    annotations: Optional[EksAnnotationsMap]
    namespace: Optional[String]


class EksPersistentVolumeClaim(TypedDict, total=False):
    """A ``persistentVolumeClaim`` volume is used to mount a
    `PersistentVolume <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>`__
    into a Pod. PersistentVolumeClaims are a way for users to "claim"
    durable storage without knowing the details of the particular cloud
    environment. See the information about
    `PersistentVolumes <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>`__
    in the *Kubernetes documentation*.
    """

    claimName: String
    readOnly: Optional[Boolean]


class EksSecret(TypedDict, total=False):
    """Specifies the configuration of a Kubernetes ``secret`` volume. For more
    information, see
    `secret <https://kubernetes.io/docs/concepts/storage/volumes/#secret>`__
    in the *Kubernetes documentation*.
    """

    secretName: String
    optional: Optional[Boolean]


class EksEmptyDir(TypedDict, total=False):
    """Specifies the configuration of a Kubernetes ``emptyDir`` volume. An
    ``emptyDir`` volume is first created when a pod is assigned to a node.
    It exists as long as that pod is running on that node. The ``emptyDir``
    volume is initially empty. All containers in the pod can read and write
    the files in the ``emptyDir`` volume. However, the ``emptyDir`` volume
    can be mounted at the same or different paths in each container. When a
    pod is removed from a node for any reason, the data in the ``emptyDir``
    is deleted permanently. For more information, see
    `emptyDir <https://kubernetes.io/docs/concepts/storage/volumes/#emptydir>`__
    in the *Kubernetes documentation*.
    """

    medium: Optional[String]
    sizeLimit: Optional[Quantity]


class EksHostPath(TypedDict, total=False):
    """Specifies the configuration of a Kubernetes ``hostPath`` volume. A
    ``hostPath`` volume mounts an existing file or directory from the host
    node's filesystem into your pod. For more information, see
    `hostPath <https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`__
    in the *Kubernetes documentation*.
    """

    path: Optional[String]


class EksVolume(TypedDict, total=False):
    """Specifies an Amazon EKS volume for a job definition."""

    name: String
    hostPath: Optional[EksHostPath]
    emptyDir: Optional[EksEmptyDir]
    secret: Optional[EksSecret]
    persistentVolumeClaim: Optional[EksPersistentVolumeClaim]


EksVolumes = List[EksVolume]


class EksContainerSecurityContext(TypedDict, total=False):
    """The security context for a job. For more information, see `Configure a
    security context for a pod or
    container <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>`__
    in the *Kubernetes documentation*.
    """

    runAsUser: Optional[Long]
    runAsGroup: Optional[Long]
    privileged: Optional[Boolean]
    allowPrivilegeEscalation: Optional[Boolean]
    readOnlyRootFilesystem: Optional[Boolean]
    runAsNonRoot: Optional[Boolean]


class EksContainerVolumeMount(TypedDict, total=False):
    """The volume mounts for a container for an Amazon EKS job. For more
    information about volumes and volume mounts in Kubernetes, see
    `Volumes <https://kubernetes.io/docs/concepts/storage/volumes/>`__ in
    the *Kubernetes documentation*.
    """

    name: Optional[String]
    mountPath: Optional[String]
    subPath: Optional[String]
    readOnly: Optional[Boolean]


EksContainerVolumeMounts = List[EksContainerVolumeMount]
EksRequests = Dict[String, Quantity]
EksLimits = Dict[String, Quantity]


class EksContainerResourceRequirements(TypedDict, total=False):
    """The type and amount of resources to assign to a container. The supported
    resources include ``memory``, ``cpu``, and ``nvidia.com/gpu``. For more
    information, see `Resource management for pods and
    containers <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>`__
    in the *Kubernetes documentation*.
    """

    limits: Optional[EksLimits]
    requests: Optional[EksRequests]


class EksContainerEnvironmentVariable(TypedDict, total=False):
    """An environment variable."""

    name: String
    value: Optional[String]


EksContainerEnvironmentVariables = List[EksContainerEnvironmentVariable]


class EksContainer(TypedDict, total=False):
    """EKS container properties are used in job definitions for Amazon EKS
    based job definitions to describe the properties for a container node in
    the pod that's launched as part of a job. This can't be specified for
    Amazon ECS based job definitions.
    """

    name: Optional[String]
    image: String
    imagePullPolicy: Optional[String]
    command: Optional[StringList]
    args: Optional[StringList]
    env: Optional[EksContainerEnvironmentVariables]
    resources: Optional[EksContainerResourceRequirements]
    volumeMounts: Optional[EksContainerVolumeMounts]
    securityContext: Optional[EksContainerSecurityContext]


EksContainers = List[EksContainer]


class ImagePullSecret(TypedDict, total=False):
    """References a Kubernetes secret resource. This name of the secret must
    start and end with an alphanumeric character, is required to be
    lowercase, can include periods (.) and hyphens (-), and can't contain
    more than 253 characters.
    """

    name: String


ImagePullSecrets = List[ImagePullSecret]


class EksPodProperties(TypedDict, total=False):
    """The properties for the pod."""

    serviceAccountName: Optional[String]
    hostNetwork: Optional[Boolean]
    dnsPolicy: Optional[String]
    imagePullSecrets: Optional[ImagePullSecrets]
    containers: Optional[EksContainers]
    initContainers: Optional[EksContainers]
    volumes: Optional[EksVolumes]
    metadata: Optional[EksMetadata]
    shareProcessNamespace: Optional[Boolean]


class EksProperties(TypedDict, total=False):
    """An object that contains the properties for the Kubernetes resources of a
    job.
    """

    podProperties: Optional[EksPodProperties]


FirelensConfigurationOptionsMap = Dict[String, String]
FirelensConfiguration = TypedDict(
    "FirelensConfiguration",
    {
        "type": FirelensConfigurationType,
        "options": Optional[FirelensConfigurationOptionsMap],
    },
    total=False,
)


class TaskContainerDependency(TypedDict, total=False):
    """A list of containers that this task depends on."""

    containerName: Optional[String]
    condition: Optional[String]


TaskContainerDependencyList = List[TaskContainerDependency]


class TaskContainerProperties(TypedDict, total=False):
    """Container properties are used for Amazon ECS-based job definitions.
    These properties to describe the container that's launched as part of a
    job.
    """

    command: Optional[StringList]
    dependsOn: Optional[TaskContainerDependencyList]
    environment: Optional[EnvironmentVariables]
    essential: Optional[Boolean]
    firelensConfiguration: Optional[FirelensConfiguration]
    image: String
    linuxParameters: Optional[LinuxParameters]
    logConfiguration: Optional[LogConfiguration]
    mountPoints: Optional[MountPoints]
    name: Optional[String]
    privileged: Optional[Boolean]
    readonlyRootFilesystem: Optional[Boolean]
    repositoryCredentials: Optional[RepositoryCredentials]
    resourceRequirements: Optional[ResourceRequirements]
    secrets: Optional[SecretList]
    ulimits: Optional[Ulimits]
    user: Optional[String]


ListTaskContainerProperties = List[TaskContainerProperties]


class EcsTaskProperties(TypedDict, total=False):
    """The properties for a task definition that describes the container and
    volume definitions of an Amazon ECS task. You can specify which Docker
    images to use, the required resources, and other configurations related
    to launching the task definition through an Amazon ECS service or task.
    """

    containers: ListTaskContainerProperties
    ephemeralStorage: Optional[EphemeralStorage]
    executionRoleArn: Optional[String]
    platformVersion: Optional[String]
    ipcMode: Optional[String]
    taskRoleArn: Optional[String]
    pidMode: Optional[String]
    networkConfiguration: Optional[NetworkConfiguration]
    runtimePlatform: Optional[RuntimePlatform]
    volumes: Optional[Volumes]
    enableExecuteCommand: Optional[Boolean]


ListEcsTaskProperties = List[EcsTaskProperties]


class EcsProperties(TypedDict, total=False):
    """An object that contains the properties for the Amazon ECS resources of a
    job.
    """

    taskProperties: ListEcsTaskProperties


PlatformCapabilityList = List[PlatformCapability]


class NodeRangeProperty(TypedDict, total=False):
    """This is an object that represents the properties of the node range for a
    multi-node parallel job.
    """

    targetNodes: String
    container: Optional[ContainerProperties]
    instanceTypes: Optional[StringList]
    ecsProperties: Optional[EcsProperties]
    eksProperties: Optional[EksProperties]
    consumableResourceProperties: Optional[ConsumableResourceProperties]


NodeRangeProperties = List[NodeRangeProperty]


class NodeProperties(TypedDict, total=False):
    """An object that represents the node properties of a multi-node parallel
    job.

    Node properties can't be specified for Amazon EKS based job definitions.
    """

    numNodes: Integer
    mainNode: Integer
    nodeRangeProperties: NodeRangeProperties


class JobTimeout(TypedDict, total=False):
    """An object that represents a job timeout configuration."""

    attemptDurationSeconds: Optional[Integer]


class EvaluateOnExit(TypedDict, total=False):
    """Specifies an array of up to 5 conditions to be met, and an action to
    take (``RETRY`` or ``EXIT``) if all conditions are met. If none of the
    ``EvaluateOnExit`` conditions in a ``RetryStrategy`` match, then the job
    is retried.
    """

    onStatusReason: Optional[String]
    onReason: Optional[String]
    onExitCode: Optional[String]
    action: RetryAction


EvaluateOnExitList = List[EvaluateOnExit]


class RetryStrategy(TypedDict, total=False):
    """The retry strategy that's associated with a job. For more information,
    see `Automated job
    retries <https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html>`__
    in the *Batch User Guide*.
    """

    attempts: Optional[Integer]
    evaluateOnExit: Optional[EvaluateOnExitList]


ParametersMap = Dict[String, String]
JobDefinition = TypedDict(
    "JobDefinition",
    {
        "jobDefinitionName": String,
        "jobDefinitionArn": String,
        "revision": Integer,
        "status": Optional[String],
        "type": String,
        "schedulingPriority": Optional[Integer],
        "parameters": Optional[ParametersMap],
        "retryStrategy": Optional[RetryStrategy],
        "containerProperties": Optional[ContainerProperties],
        "timeout": Optional[JobTimeout],
        "nodeProperties": Optional[NodeProperties],
        "tags": Optional[TagrisTagsMap],
        "propagateTags": Optional[Boolean],
        "platformCapabilities": Optional[PlatformCapabilityList],
        "ecsProperties": Optional[EcsProperties],
        "eksProperties": Optional[EksProperties],
        "containerOrchestrationType": Optional[OrchestrationType],
        "consumableResourceProperties": Optional[ConsumableResourceProperties],
    },
    total=False,
)
JobDefinitionList = List[JobDefinition]


class DescribeJobDefinitionsResponse(TypedDict, total=False):
    jobDefinitions: Optional[JobDefinitionList]
    nextToken: Optional[String]


class DescribeJobQueuesRequest(ServiceRequest):
    """Contains the parameters for ``DescribeJobQueues``."""

    jobQueues: Optional[StringList]
    maxResults: Optional[Integer]
    nextToken: Optional[String]


class JobQueueDetail(TypedDict, total=False):
    """An object that represents the details for an Batch job queue."""

    jobQueueName: String
    jobQueueArn: String
    state: JQState
    schedulingPolicyArn: Optional[String]
    status: Optional[JQStatus]
    statusReason: Optional[String]
    priority: Integer
    computeEnvironmentOrder: ComputeEnvironmentOrders
    tags: Optional[TagrisTagsMap]
    jobStateTimeLimitActions: Optional[JobStateTimeLimitActions]


JobQueueDetailList = List[JobQueueDetail]


class DescribeJobQueuesResponse(TypedDict, total=False):
    jobQueues: Optional[JobQueueDetailList]
    nextToken: Optional[String]


class DescribeJobsRequest(ServiceRequest):
    """Contains the parameters for ``DescribeJobs``."""

    jobs: StringList


class TaskContainerDetails(TypedDict, total=False):
    """The details for the container in this task attempt."""

    command: Optional[StringList]
    dependsOn: Optional[TaskContainerDependencyList]
    environment: Optional[EnvironmentVariables]
    essential: Optional[Boolean]
    firelensConfiguration: Optional[FirelensConfiguration]
    image: Optional[String]
    linuxParameters: Optional[LinuxParameters]
    logConfiguration: Optional[LogConfiguration]
    mountPoints: Optional[MountPoints]
    name: Optional[String]
    privileged: Optional[Boolean]
    readonlyRootFilesystem: Optional[Boolean]
    repositoryCredentials: Optional[RepositoryCredentials]
    resourceRequirements: Optional[ResourceRequirements]
    secrets: Optional[SecretList]
    ulimits: Optional[Ulimits]
    user: Optional[String]
    exitCode: Optional[Integer]
    reason: Optional[String]
    logStreamName: Optional[String]
    networkInterfaces: Optional[NetworkInterfaceList]


ListTaskContainerDetails = List[TaskContainerDetails]


class EcsTaskDetails(TypedDict, total=False):
    """The details of a task definition that describes the container and volume
    definitions of an Amazon ECS task.
    """

    containers: Optional[ListTaskContainerDetails]
    containerInstanceArn: Optional[String]
    taskArn: Optional[String]
    ephemeralStorage: Optional[EphemeralStorage]
    executionRoleArn: Optional[String]
    platformVersion: Optional[String]
    ipcMode: Optional[String]
    taskRoleArn: Optional[String]
    pidMode: Optional[String]
    networkConfiguration: Optional[NetworkConfiguration]
    runtimePlatform: Optional[RuntimePlatform]
    volumes: Optional[Volumes]
    enableExecuteCommand: Optional[Boolean]


ListEcsTaskDetails = List[EcsTaskDetails]


class EcsPropertiesDetail(TypedDict, total=False):
    """An object that contains the details for the Amazon ECS resources of a
    job.
    """

    taskProperties: Optional[ListEcsTaskDetails]


class EksAttemptContainerDetail(TypedDict, total=False):
    """An object that represents the details for an attempt for a job attempt
    that an Amazon EKS container runs.
    """

    name: Optional[String]
    containerID: Optional[String]
    exitCode: Optional[Integer]
    reason: Optional[String]


EksAttemptContainerDetails = List[EksAttemptContainerDetail]


class EksAttemptDetail(TypedDict, total=False):
    """An object that represents the details of a job attempt for a job attempt
    by an Amazon EKS container.
    """

    containers: Optional[EksAttemptContainerDetails]
    initContainers: Optional[EksAttemptContainerDetails]
    eksClusterArn: Optional[String]
    podName: Optional[String]
    podNamespace: Optional[String]
    nodeName: Optional[String]
    startedAt: Optional[Long]
    stoppedAt: Optional[Long]
    statusReason: Optional[String]


EksAttemptDetails = List[EksAttemptDetail]


class EksContainerDetail(TypedDict, total=False):
    """The details for container properties that are returned by
    ``DescribeJobs`` for jobs that use Amazon EKS.
    """

    name: Optional[String]
    image: Optional[String]
    imagePullPolicy: Optional[String]
    command: Optional[StringList]
    args: Optional[StringList]
    env: Optional[EksContainerEnvironmentVariables]
    resources: Optional[EksContainerResourceRequirements]
    exitCode: Optional[Integer]
    reason: Optional[String]
    volumeMounts: Optional[EksContainerVolumeMounts]
    securityContext: Optional[EksContainerSecurityContext]


EksContainerDetails = List[EksContainerDetail]


class EksPodPropertiesDetail(TypedDict, total=False):
    """The details for the pod."""

    serviceAccountName: Optional[String]
    hostNetwork: Optional[Boolean]
    dnsPolicy: Optional[String]
    imagePullSecrets: Optional[ImagePullSecrets]
    containers: Optional[EksContainerDetails]
    initContainers: Optional[EksContainerDetails]
    volumes: Optional[EksVolumes]
    podName: Optional[String]
    nodeName: Optional[String]
    metadata: Optional[EksMetadata]
    shareProcessNamespace: Optional[Boolean]


class EksPropertiesDetail(TypedDict, total=False):
    """An object that contains the details for the Kubernetes resources of a
    job.
    """

    podProperties: Optional[EksPodPropertiesDetail]


class NodeDetails(TypedDict, total=False):
    """An object that represents the details of a multi-node parallel job node."""

    nodeIndex: Optional[Integer]
    isMainNode: Optional[Boolean]


JobDependency = TypedDict(
    "JobDependency",
    {
        "jobId": Optional[String],
        "type": Optional[ArrayJobDependency],
    },
    total=False,
)
JobDependencyList = List[JobDependency]


class JobDetail(TypedDict, total=False):
    """An object that represents an Batch job."""

    jobArn: Optional[String]
    jobName: String
    jobId: String
    jobQueue: String
    status: JobStatus
    shareIdentifier: Optional[String]
    schedulingPriority: Optional[Integer]
    attempts: Optional[AttemptDetails]
    statusReason: Optional[String]
    createdAt: Optional[Long]
    retryStrategy: Optional[RetryStrategy]
    startedAt: Long
    stoppedAt: Optional[Long]
    dependsOn: Optional[JobDependencyList]
    jobDefinition: String
    parameters: Optional[ParametersMap]
    container: Optional[ContainerDetail]
    nodeDetails: Optional[NodeDetails]
    nodeProperties: Optional[NodeProperties]
    arrayProperties: Optional[ArrayPropertiesDetail]
    timeout: Optional[JobTimeout]
    tags: Optional[TagrisTagsMap]
    propagateTags: Optional[Boolean]
    platformCapabilities: Optional[PlatformCapabilityList]
    eksProperties: Optional[EksPropertiesDetail]
    eksAttempts: Optional[EksAttemptDetails]
    ecsProperties: Optional[EcsPropertiesDetail]
    isCancelled: Optional[Boolean]
    isTerminated: Optional[Boolean]
    consumableResourceProperties: Optional[ConsumableResourceProperties]


JobDetailList = List[JobDetail]


class DescribeJobsResponse(TypedDict, total=False):
    jobs: Optional[JobDetailList]


class DescribeSchedulingPoliciesRequest(ServiceRequest):
    """Contains the parameters for ``DescribeSchedulingPolicies``."""

    arns: StringList


class SchedulingPolicyDetail(TypedDict, total=False):
    """An object that represents a scheduling policy."""

    name: String
    arn: String
    fairsharePolicy: Optional[FairsharePolicy]
    tags: Optional[TagrisTagsMap]


SchedulingPolicyDetailList = List[SchedulingPolicyDetail]


class DescribeSchedulingPoliciesResponse(TypedDict, total=False):
    schedulingPolicies: Optional[SchedulingPolicyDetailList]


class TaskContainerOverrides(TypedDict, total=False):
    """The overrides that should be sent to a container.

    For information about using Batch overrides when you connect event
    sources to targets, see
    `BatchContainerOverrides <https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_BatchContainerOverrides.html>`__.
    """

    command: Optional[StringList]
    environment: Optional[EnvironmentVariables]
    name: Optional[String]
    resourceRequirements: Optional[ResourceRequirements]


ListTaskContainerOverrides = List[TaskContainerOverrides]


class TaskPropertiesOverride(TypedDict, total=False):
    """An object that contains overrides for the task definition of a job."""

    containers: Optional[ListTaskContainerOverrides]


ListTaskPropertiesOverride = List[TaskPropertiesOverride]


class EcsPropertiesOverride(TypedDict, total=False):
    """An object that contains overrides for the Amazon ECS task definition of
    a job.
    """

    taskProperties: Optional[ListTaskPropertiesOverride]


class EksContainerOverride(TypedDict, total=False):
    """Object representing any Kubernetes overrides to a job definition that's
    used in a
    `SubmitJob <https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html>`__
    API operation.
    """

    name: Optional[String]
    image: Optional[String]
    command: Optional[StringList]
    args: Optional[StringList]
    env: Optional[EksContainerEnvironmentVariables]
    resources: Optional[EksContainerResourceRequirements]


EksContainerOverrideList = List[EksContainerOverride]


class EksPodPropertiesOverride(TypedDict, total=False):
    """An object that contains overrides for the Kubernetes pod properties of a
    job.
    """

    containers: Optional[EksContainerOverrideList]
    initContainers: Optional[EksContainerOverrideList]
    metadata: Optional[EksMetadata]


class EksPropertiesOverride(TypedDict, total=False):
    """An object that contains overrides for the Kubernetes resources of a job."""

    podProperties: Optional[EksPodPropertiesOverride]


class FrontOfQueueJobSummary(TypedDict, total=False):
    """An object that represents summary details for the first 100 ``RUNNABLE``
    jobs in a job queue.
    """

    jobArn: Optional[String]
    earliestTimeAtPosition: Optional[Long]


FrontOfQueueJobSummaryList = List[FrontOfQueueJobSummary]


class FrontOfQueueDetail(TypedDict, total=False):
    """Contains a list of the first 100 ``RUNNABLE`` jobs associated to a
    single job queue.
    """

    jobs: Optional[FrontOfQueueJobSummaryList]
    lastUpdatedAt: Optional[Long]


class GetJobQueueSnapshotRequest(ServiceRequest):
    jobQueue: String


class GetJobQueueSnapshotResponse(TypedDict, total=False):
    frontOfQueue: Optional[FrontOfQueueDetail]


class NodePropertiesSummary(TypedDict, total=False):
    """An object that represents the properties of a node that's associated
    with a multi-node parallel job.
    """

    isMainNode: Optional[Boolean]
    numNodes: Optional[Integer]
    nodeIndex: Optional[Integer]


class JobSummary(TypedDict, total=False):
    """An object that represents summary details of a job."""

    jobArn: Optional[String]
    jobId: String
    jobName: String
    createdAt: Optional[Long]
    status: Optional[JobStatus]
    statusReason: Optional[String]
    startedAt: Optional[Long]
    stoppedAt: Optional[Long]
    container: Optional[ContainerSummary]
    arrayProperties: Optional[ArrayPropertiesSummary]
    nodeProperties: Optional[NodePropertiesSummary]
    jobDefinition: Optional[String]


JobSummaryList = List[JobSummary]


class KeyValuesPair(TypedDict, total=False):
    """A filter name and value pair that's used to return a more specific list
    of results from a ``ListJobs`` or ``ListJobsByConsumableResource`` API
    operation.
    """

    name: Optional[String]
    values: Optional[StringList]


ListConsumableResourcesFilterList = List[KeyValuesPair]


class ListConsumableResourcesRequest(ServiceRequest):
    filters: Optional[ListConsumableResourcesFilterList]
    maxResults: Optional[Integer]
    nextToken: Optional[String]


class ListConsumableResourcesResponse(TypedDict, total=False):
    consumableResources: ConsumableResourceSummaryList
    nextToken: Optional[String]


ListJobsByConsumableResourceFilterList = List[KeyValuesPair]


class ListJobsByConsumableResourceRequest(ServiceRequest):
    consumableResource: String
    filters: Optional[ListJobsByConsumableResourceFilterList]
    maxResults: Optional[Integer]
    nextToken: Optional[String]


class ListJobsByConsumableResourceSummary(TypedDict, total=False):
    """Current information about a consumable resource required by a job."""

    jobArn: String
    jobQueueArn: String
    jobName: String
    jobDefinitionArn: Optional[String]
    shareIdentifier: Optional[String]
    jobStatus: String
    quantity: Long
    statusReason: Optional[String]
    startedAt: Optional[Long]
    createdAt: Long
    consumableResourceProperties: ConsumableResourceProperties


ListJobsByConsumableResourceSummaryList = List[ListJobsByConsumableResourceSummary]


class ListJobsByConsumableResourceResponse(TypedDict, total=False):
    jobs: ListJobsByConsumableResourceSummaryList
    nextToken: Optional[String]


ListJobsFilterList = List[KeyValuesPair]


class ListJobsRequest(ServiceRequest):
    """Contains the parameters for ``ListJobs``."""

    jobQueue: Optional[String]
    arrayJobId: Optional[String]
    multiNodeJobId: Optional[String]
    jobStatus: Optional[JobStatus]
    maxResults: Optional[Integer]
    nextToken: Optional[String]
    filters: Optional[ListJobsFilterList]


class ListJobsResponse(TypedDict, total=False):
    jobSummaryList: JobSummaryList
    nextToken: Optional[String]


class ListSchedulingPoliciesRequest(ServiceRequest):
    """Contains the parameters for ``ListSchedulingPolicies``."""

    maxResults: Optional[Integer]
    nextToken: Optional[String]


class SchedulingPolicyListingDetail(TypedDict, total=False):
    """An object that contains the details of a scheduling policy that's
    returned in a ``ListSchedulingPolicy`` action.
    """

    arn: String


SchedulingPolicyListingDetailList = List[SchedulingPolicyListingDetail]


class ListSchedulingPoliciesResponse(TypedDict, total=False):
    schedulingPolicies: Optional[SchedulingPolicyListingDetailList]
    nextToken: Optional[String]


class ListTagsForResourceRequest(ServiceRequest):
    """Contains the parameters for ``ListTagsForResource``."""

    resourceArn: String


class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Optional[TagrisTagsMap]


class NodePropertyOverride(TypedDict, total=False):
    """The object that represents any node overrides to a job definition that's
    used in a
    `SubmitJob <https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html>`__
    API operation.
    """

    targetNodes: String
    containerOverrides: Optional[ContainerOverrides]
    ecsPropertiesOverride: Optional[EcsPropertiesOverride]
    instanceTypes: Optional[StringList]
    eksPropertiesOverride: Optional[EksPropertiesOverride]
    consumableResourcePropertiesOverride: Optional[ConsumableResourceProperties]


NodePropertyOverrides = List[NodePropertyOverride]


class NodeOverrides(TypedDict, total=False):
    """An object that represents any node overrides to a job definition that's
    used in a
    `SubmitJob <https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html>`__
    API operation.

    This parameter isn't applicable to jobs that are running on Fargate
    resources. Don't provide it for these jobs. Rather, use
    ``containerOverrides`` instead.
    """

    numNodes: Optional[Integer]
    nodePropertyOverrides: Optional[NodePropertyOverrides]


RegisterJobDefinitionRequest = TypedDict(
    "RegisterJobDefinitionRequest",
    {
        "jobDefinitionName": String,
        "type": JobDefinitionType,
        "parameters": Optional[ParametersMap],
        "schedulingPriority": Optional[Integer],
        "containerProperties": Optional[ContainerProperties],
        "nodeProperties": Optional[NodeProperties],
        "retryStrategy": Optional[RetryStrategy],
        "propagateTags": Optional[Boolean],
        "timeout": Optional[JobTimeout],
        "tags": Optional[TagrisTagsMap],
        "platformCapabilities": Optional[PlatformCapabilityList],
        "eksProperties": Optional[EksProperties],
        "ecsProperties": Optional[EcsProperties],
        "consumableResourceProperties": Optional[ConsumableResourceProperties],
    },
    total=False,
)


class RegisterJobDefinitionResponse(TypedDict, total=False):
    jobDefinitionName: String
    jobDefinitionArn: String
    revision: Integer


class SubmitJobRequest(ServiceRequest):
    """Contains the parameters for ``SubmitJob``."""

    jobName: String
    jobQueue: String
    shareIdentifier: Optional[String]
    schedulingPriorityOverride: Optional[Integer]
    arrayProperties: Optional[ArrayProperties]
    dependsOn: Optional[JobDependencyList]
    jobDefinition: String
    parameters: Optional[ParametersMap]
    containerOverrides: Optional[ContainerOverrides]
    nodeOverrides: Optional[NodeOverrides]
    retryStrategy: Optional[RetryStrategy]
    propagateTags: Optional[Boolean]
    timeout: Optional[JobTimeout]
    tags: Optional[TagrisTagsMap]
    eksPropertiesOverride: Optional[EksPropertiesOverride]
    ecsPropertiesOverride: Optional[EcsPropertiesOverride]
    consumableResourcePropertiesOverride: Optional[ConsumableResourceProperties]


class SubmitJobResponse(TypedDict, total=False):
    jobArn: Optional[String]
    jobName: String
    jobId: String


TagKeysList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    """Contains the parameters for ``TagResource``."""

    resourceArn: String
    tags: TagrisTagsMap


class TagResourceResponse(TypedDict, total=False):
    pass


class TerminateJobRequest(ServiceRequest):
    """Contains the parameters for ``TerminateJob``."""

    jobId: String
    reason: String


class TerminateJobResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    """Contains the parameters for ``UntagResource``."""

    resourceArn: String
    tagKeys: TagKeysList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateComputeEnvironmentRequest(ServiceRequest):
    """Contains the parameters for ``UpdateComputeEnvironment``."""

    computeEnvironment: String
    state: Optional[CEState]
    unmanagedvCpus: Optional[Integer]
    computeResources: Optional[ComputeResourceUpdate]
    serviceRole: Optional[String]
    updatePolicy: Optional[UpdatePolicy]
    context: Optional[String]


class UpdateComputeEnvironmentResponse(TypedDict, total=False):
    computeEnvironmentName: Optional[String]
    computeEnvironmentArn: Optional[String]


class UpdateConsumableResourceRequest(ServiceRequest):
    consumableResource: String
    operation: Optional[String]
    quantity: Optional[Long]
    clientToken: Optional[ClientRequestToken]


class UpdateConsumableResourceResponse(TypedDict, total=False):
    consumableResourceName: String
    consumableResourceArn: String
    totalQuantity: Optional[Long]


class UpdateJobQueueRequest(ServiceRequest):
    """Contains the parameters for ``UpdateJobQueue``."""

    jobQueue: String
    state: Optional[JQState]
    schedulingPolicyArn: Optional[String]
    priority: Optional[Integer]
    computeEnvironmentOrder: Optional[ComputeEnvironmentOrders]
    jobStateTimeLimitActions: Optional[JobStateTimeLimitActions]


class UpdateJobQueueResponse(TypedDict, total=False):
    jobQueueName: Optional[String]
    jobQueueArn: Optional[String]


class UpdateSchedulingPolicyRequest(ServiceRequest):
    """Contains the parameters for ``UpdateSchedulingPolicy``."""

    arn: String
    fairsharePolicy: Optional[FairsharePolicy]


class UpdateSchedulingPolicyResponse(TypedDict, total=False):
    pass


class BatchApi:
    service = "batch"
    version = "2016-08-10"

    @handler("CancelJob")
    def cancel_job(
        self, context: RequestContext, job_id: String, reason: String, **kwargs
    ) -> CancelJobResponse:
        """Cancels a job in an Batch job queue. Jobs that are in a ``SUBMITTED``,
        ``PENDING``, or ``RUNNABLE`` state are cancelled and the job status is
        updated to ``FAILED``.

        A ``PENDING`` job is canceled after all dependency jobs are completed.
        Therefore, it may take longer than expected to cancel a job in
        ``PENDING`` status.

        When you try to cancel an array parent job in ``PENDING``, Batch
        attempts to cancel all child jobs. The array parent job is canceled when
        all child jobs are completed.

        Jobs that progressed to the ``STARTING`` or ``RUNNING`` state aren't
        canceled. However, the API operation still succeeds, even if no job is
        canceled. These jobs must be terminated with the TerminateJob operation.

        :param job_id: The Batch job ID of the job to cancel.
        :param reason: A message to attach to the job that explains the reason for canceling
        it.
        :returns: CancelJobResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("CreateComputeEnvironment", expand=False)
    def create_compute_environment(
        self, context: RequestContext, request: CreateComputeEnvironmentRequest, **kwargs
    ) -> CreateComputeEnvironmentResponse:
        """Creates an Batch compute environment. You can create ``MANAGED`` or
        ``UNMANAGED`` compute environments. ``MANAGED`` compute environments can
        use Amazon EC2 or Fargate resources. ``UNMANAGED`` compute environments
        can only use EC2 resources.

        In a managed compute environment, Batch manages the capacity and
        instance types of the compute resources within the environment. This is
        based on the compute resource specification that you define or the
        `launch
        template <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`__
        that you specify when you create the compute environment. Either, you
        can choose to use EC2 On-Demand Instances and EC2 Spot Instances. Or,
        you can use Fargate and Fargate Spot capacity in your managed compute
        environment. You can optionally set a maximum price so that Spot
        Instances only launch when the Spot Instance price is less than a
        specified percentage of the On-Demand price.

        Multi-node parallel jobs aren't supported on Spot Instances.

        In an unmanaged compute environment, you can manage your own EC2 compute
        resources and have flexibility with how you configure your compute
        resources. For example, you can use custom AMIs. However, you must
        verify that each of your AMIs meet the Amazon ECS container instance AMI
        specification. For more information, see `container instance
        AMIs <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html>`__
        in the *Amazon Elastic Container Service Developer Guide*. After you
        created your unmanaged compute environment, you can use the
        DescribeComputeEnvironments operation to find the Amazon ECS cluster
        that's associated with it. Then, launch your container instances into
        that Amazon ECS cluster. For more information, see `Launching an Amazon
        ECS container
        instance <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html>`__
        in the *Amazon Elastic Container Service Developer Guide*.

        To create a compute environment that uses EKS resources, the caller must
        have permissions to call ``eks:DescribeCluster``.

        Batch doesn't automatically upgrade the AMIs in a compute environment
        after it's created. For example, it also doesn't update the AMIs in your
        compute environment when a newer version of the Amazon ECS optimized AMI
        is available. You're responsible for the management of the guest
        operating system. This includes any updates and security patches. You're
        also responsible for any additional application software or utilities
        that you install on the compute resources. There are two ways to use a
        new AMI for your Batch jobs. The original method is to complete these
        steps:

        #. Create a new compute environment with the new AMI.

        #. Add the compute environment to an existing job queue.

        #. Remove the earlier compute environment from your job queue.

        #. Delete the earlier compute environment.

        In April 2022, Batch added enhanced support for updating compute
        environments. For more information, see `Updating compute
        environments <https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html>`__.
        To use the enhanced updating of compute environments to update AMIs,
        follow these rules:

        -  Either don't set the service role (``serviceRole``) parameter or set
           it to the **AWSBatchServiceRole** service-linked role.

        -  Set the allocation strategy (``allocationStrategy``) parameter to
           ``BEST_FIT_PROGRESSIVE``, ``SPOT_CAPACITY_OPTIMIZED``, or
           ``SPOT_PRICE_CAPACITY_OPTIMIZED``.

        -  Set the update to latest image version
           (``updateToLatestImageVersion``) parameter to ``true``. The
           ``updateToLatestImageVersion`` parameter is used when you update a
           compute environment. This parameter is ignored when you create a
           compute environment.

        -  Don't specify an AMI ID in ``imageId``, ``imageIdOverride`` (in
           ```ec2Configuration`` <https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html>`__
           ), or in the launch template (``launchTemplate``). In that case,
           Batch selects the latest Amazon ECS optimized AMI that's supported by
           Batch at the time the infrastructure update is initiated.
           Alternatively, you can specify the AMI ID in the ``imageId`` or
           ``imageIdOverride`` parameters, or the launch template identified by
           the ``LaunchTemplate`` properties. Changing any of these properties
           starts an infrastructure update. If the AMI ID is specified in the
           launch template, it can't be replaced by specifying an AMI ID in
           either the ``imageId`` or ``imageIdOverride`` parameters. It can only
           be replaced by specifying a different launch template, or if the
           launch template version is set to ``$Default`` or ``$Latest``, by
           setting either a new default version for the launch template (if
           ``$Default``) or by adding a new version to the launch template (if
           ``$Latest``).

        If these rules are followed, any update that starts an infrastructure
        update causes the AMI ID to be re-selected. If the ``version`` setting
        in the launch template (``launchTemplate``) is set to ``$Latest`` or
        ``$Default``, the latest or default version of the launch template is
        evaluated up at the time of the infrastructure update, even if the
        ``launchTemplate`` wasn't updated.

        :param compute_environment_name: The name for your compute environment.
        :param type: The type of the compute environment: ``MANAGED`` or ``UNMANAGED``.
        :param state: The state of the compute environment.
        :param unmanagedv_cpus: The maximum number of vCPUs for an unmanaged compute environment.
        :param compute_resources: Details about the compute resources managed by the compute environment.
        :param service_role: The full Amazon Resource Name (ARN) of the IAM role that allows Batch to
        make calls to other Amazon Web Services services on your behalf.
        :param tags: The tags that you apply to the compute environment to help you
        categorize and organize your resources.
        :param eks_configuration: The details for the Amazon EKS cluster that supports the compute
        environment.
        :param context: Reserved.
        :returns: CreateComputeEnvironmentResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("CreateConsumableResource")
    def create_consumable_resource(
        self,
        context: RequestContext,
        consumable_resource_name: String,
        total_quantity: Long | None = None,
        resource_type: String | None = None,
        tags: TagrisTagsMap | None = None,
        **kwargs,
    ) -> CreateConsumableResourceResponse:
        """Creates an Batch consumable resource.

        :param consumable_resource_name: The name of the consumable resource.
        :param total_quantity: The total amount of the consumable resource that is available.
        :param resource_type: Indicates whether the resource is available to be re-used after a job
        completes.
        :param tags: The tags that you apply to the consumable resource to help you
        categorize and organize your resources.
        :returns: CreateConsumableResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("CreateJobQueue")
    def create_job_queue(
        self,
        context: RequestContext,
        job_queue_name: String,
        priority: Integer,
        compute_environment_order: ComputeEnvironmentOrders,
        state: JQState | None = None,
        scheduling_policy_arn: String | None = None,
        tags: TagrisTagsMap | None = None,
        job_state_time_limit_actions: JobStateTimeLimitActions | None = None,
        **kwargs,
    ) -> CreateJobQueueResponse:
        """Creates an Batch job queue. When you create a job queue, you associate
        one or more compute environments to the queue and assign an order of
        preference for the compute environments.

        You also set a priority to the job queue that determines the order that
        the Batch scheduler places jobs onto its associated compute
        environments. For example, if a compute environment is associated with
        more than one job queue, the job queue with a higher priority is given
        preference for scheduling jobs to that compute environment.

        :param job_queue_name: The name of the job queue.
        :param priority: The priority of the job queue.
        :param compute_environment_order: The set of compute environments mapped to a job queue and their order
        relative to each other.
        :param state: The state of the job queue.
        :param scheduling_policy_arn: The Amazon Resource Name (ARN) of the fair-share scheduling policy.
        :param tags: The tags that you apply to the job queue to help you categorize and
        organize your resources.
        :param job_state_time_limit_actions: The set of actions that Batch performs on jobs that remain at the head
        of the job queue in the specified state longer than specified times.
        :returns: CreateJobQueueResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("CreateSchedulingPolicy")
    def create_scheduling_policy(
        self,
        context: RequestContext,
        name: String,
        fairshare_policy: FairsharePolicy | None = None,
        tags: TagrisTagsMap | None = None,
        **kwargs,
    ) -> CreateSchedulingPolicyResponse:
        """Creates an Batch scheduling policy.

        :param name: The name of the fair-share scheduling policy.
        :param fairshare_policy: The fair-share scheduling policy details.
        :param tags: The tags that you apply to the scheduling policy to help you categorize
        and organize your resources.
        :returns: CreateSchedulingPolicyResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeleteComputeEnvironment")
    def delete_compute_environment(
        self, context: RequestContext, compute_environment: String, **kwargs
    ) -> DeleteComputeEnvironmentResponse:
        """Deletes an Batch compute environment.

        Before you can delete a compute environment, you must set its state to
        ``DISABLED`` with the UpdateComputeEnvironment API operation and
        disassociate it from any job queues with the UpdateJobQueue API
        operation. Compute environments that use Fargate resources must
        terminate all active jobs on that compute environment before deleting
        the compute environment. If this isn't done, the compute environment
        enters an invalid state.

        :param compute_environment: The name or Amazon Resource Name (ARN) of the compute environment to
        delete.
        :returns: DeleteComputeEnvironmentResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeleteConsumableResource")
    def delete_consumable_resource(
        self, context: RequestContext, consumable_resource: String, **kwargs
    ) -> DeleteConsumableResourceResponse:
        """Deletes the specified consumable resource.

        :param consumable_resource: The name or ARN of the consumable resource that will be deleted.
        :returns: DeleteConsumableResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeleteJobQueue")
    def delete_job_queue(
        self, context: RequestContext, job_queue: String, **kwargs
    ) -> DeleteJobQueueResponse:
        """Deletes the specified job queue. You must first disable submissions for
        a queue with the UpdateJobQueue operation. All jobs in the queue are
        eventually terminated when you delete a job queue. The jobs are
        terminated at a rate of about 16 jobs each second.

        It's not necessary to disassociate compute environments from a queue
        before submitting a ``DeleteJobQueue`` request.

        :param job_queue: The short name or full Amazon Resource Name (ARN) of the queue to
        delete.
        :returns: DeleteJobQueueResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeleteSchedulingPolicy")
    def delete_scheduling_policy(
        self, context: RequestContext, arn: String, **kwargs
    ) -> DeleteSchedulingPolicyResponse:
        """Deletes the specified scheduling policy.

        You can't delete a scheduling policy that's used in any job queues.

        :param arn: The Amazon Resource Name (ARN) of the scheduling policy to delete.
        :returns: DeleteSchedulingPolicyResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DeregisterJobDefinition")
    def deregister_job_definition(
        self, context: RequestContext, job_definition: String, **kwargs
    ) -> DeregisterJobDefinitionResponse:
        """Deregisters an Batch job definition. Job definitions are permanently
        deleted after 180 days.

        :param job_definition: The name and revision (``name:revision``) or full Amazon Resource Name
        (ARN) of the job definition to deregister.
        :returns: DeregisterJobDefinitionResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeComputeEnvironments")
    def describe_compute_environments(
        self,
        context: RequestContext,
        compute_environments: StringList | None = None,
        max_results: Integer | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeComputeEnvironmentsResponse:
        """Describes one or more of your compute environments.

        If you're using an unmanaged compute environment, you can use the
        ``DescribeComputeEnvironment`` operation to determine the
        ``ecsClusterArn`` that you launch your Amazon ECS container instances
        into.

        :param compute_environments: A list of up to 100 compute environment names or full Amazon Resource
        Name (ARN) entries.
        :param max_results: The maximum number of cluster results returned by
        ``DescribeComputeEnvironments`` in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``DescribeComputeEnvironments`` request where ``maxResults`` was used
        and the results exceeded the value of that parameter.
        :returns: DescribeComputeEnvironmentsResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeConsumableResource")
    def describe_consumable_resource(
        self, context: RequestContext, consumable_resource: String, **kwargs
    ) -> DescribeConsumableResourceResponse:
        """Returns a description of the specified consumable resource.

        :param consumable_resource: The name or ARN of the consumable resource whose description will be
        returned.
        :returns: DescribeConsumableResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeJobDefinitions")
    def describe_job_definitions(
        self,
        context: RequestContext,
        job_definitions: StringList | None = None,
        max_results: Integer | None = None,
        job_definition_name: String | None = None,
        status: String | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeJobDefinitionsResponse:
        """Describes a list of job definitions. You can specify a ``status`` (such
        as ``ACTIVE``) to only return job definitions that match that status.

        :param job_definitions: A list of up to 100 job definitions.
        :param max_results: The maximum number of results returned by ``DescribeJobDefinitions`` in
        paginated output.
        :param job_definition_name: The name of the job definition to describe.
        :param status: The status used to filter job definitions.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``DescribeJobDefinitions`` request where ``maxResults`` was used and the
        results exceeded the value of that parameter.
        :returns: DescribeJobDefinitionsResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeJobQueues")
    def describe_job_queues(
        self,
        context: RequestContext,
        job_queues: StringList | None = None,
        max_results: Integer | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> DescribeJobQueuesResponse:
        """Describes one or more of your job queues.

        :param job_queues: A list of up to 100 queue names or full queue Amazon Resource Name (ARN)
        entries.
        :param max_results: The maximum number of results returned by ``DescribeJobQueues`` in
        paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``DescribeJobQueues`` request where ``maxResults`` was used and the
        results exceeded the value of that parameter.
        :returns: DescribeJobQueuesResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeJobs")
    def describe_jobs(
        self, context: RequestContext, jobs: StringList, **kwargs
    ) -> DescribeJobsResponse:
        """Describes a list of Batch jobs.

        :param jobs: A list of up to 100 job IDs.
        :returns: DescribeJobsResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("DescribeSchedulingPolicies")
    def describe_scheduling_policies(
        self, context: RequestContext, arns: StringList, **kwargs
    ) -> DescribeSchedulingPoliciesResponse:
        """Describes one or more of your scheduling policies.

        :param arns: A list of up to 100 scheduling policy Amazon Resource Name (ARN)
        entries.
        :returns: DescribeSchedulingPoliciesResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("GetJobQueueSnapshot")
    def get_job_queue_snapshot(
        self, context: RequestContext, job_queue: String, **kwargs
    ) -> GetJobQueueSnapshotResponse:
        """Provides a list of the first 100 ``RUNNABLE`` jobs associated to a
        single job queue.

        :param job_queue: The job queue’s name or full queue Amazon Resource Name (ARN).
        :returns: GetJobQueueSnapshotResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListConsumableResources")
    def list_consumable_resources(
        self,
        context: RequestContext,
        filters: ListConsumableResourcesFilterList | None = None,
        max_results: Integer | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListConsumableResourcesResponse:
        """Returns a list of Batch consumable resources.

        :param filters: The filters to apply to the consumable resource list query.
        :param max_results: The maximum number of results returned by ``ListConsumableResources`` in
        paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``ListConsumableResources`` request where ``maxResults`` was used and
        the results exceeded the value of that parameter.
        :returns: ListConsumableResourcesResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListJobs")
    def list_jobs(
        self,
        context: RequestContext,
        job_queue: String | None = None,
        array_job_id: String | None = None,
        multi_node_job_id: String | None = None,
        job_status: JobStatus | None = None,
        max_results: Integer | None = None,
        next_token: String | None = None,
        filters: ListJobsFilterList | None = None,
        **kwargs,
    ) -> ListJobsResponse:
        """Returns a list of Batch jobs.

        You must specify only one of the following items:

        -  A job queue ID to return a list of jobs in that job queue

        -  A multi-node parallel job ID to return a list of nodes for that job

        -  An array job ID to return a list of the children for that job

        You can filter the results by job status with the ``jobStatus``
        parameter. If you don't specify a status, only ``RUNNING`` jobs are
        returned.

        :param job_queue: The name or full Amazon Resource Name (ARN) of the job queue used to
        list jobs.
        :param array_job_id: The job ID for an array job.
        :param multi_node_job_id: The job ID for a multi-node parallel job.
        :param job_status: The job status used to filter jobs in the specified queue.
        :param max_results: The maximum number of results returned by ``ListJobs`` in a paginated
        output.
        :param next_token: The ``nextToken`` value returned from a previous paginated ``ListJobs``
        request where ``maxResults`` was used and the results exceeded the value
        of that parameter.
        :param filters: The filter to apply to the query.
        :returns: ListJobsResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListJobsByConsumableResource")
    def list_jobs_by_consumable_resource(
        self,
        context: RequestContext,
        consumable_resource: String,
        filters: ListJobsByConsumableResourceFilterList | None = None,
        max_results: Integer | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListJobsByConsumableResourceResponse:
        """Returns a list of Batch jobs that require a specific consumable
        resource.

        :param consumable_resource: The name or ARN of the consumable resource.
        :param filters: The filters to apply to the job list query.
        :param max_results: The maximum number of results returned by
        ``ListJobsByConsumableResource`` in paginated output.
        :param next_token: The ``nextToken`` value returned from a previous paginated
        ``ListJobsByConsumableResource`` request where ``maxResults`` was used
        and the results exceeded the value of that parameter.
        :returns: ListJobsByConsumableResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListSchedulingPolicies")
    def list_scheduling_policies(
        self,
        context: RequestContext,
        max_results: Integer | None = None,
        next_token: String | None = None,
        **kwargs,
    ) -> ListSchedulingPoliciesResponse:
        """Returns a list of Batch scheduling policies.

        :param max_results: The maximum number of results that's returned by
        ``ListSchedulingPolicies`` in paginated output.
        :param next_token: The ``nextToken`` value that's returned from a previous paginated
        ``ListSchedulingPolicies`` request where ``maxResults`` was used and the
        results exceeded the value of that parameter.
        :returns: ListSchedulingPoliciesResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: String, **kwargs
    ) -> ListTagsForResourceResponse:
        """Lists the tags for an Batch resource. Batch resources that support tags
        are compute environments, jobs, job definitions, job queues, and
        scheduling policies. ARNs for child jobs of array and multi-node
        parallel (MNP) jobs aren't supported.

        :param resource_arn: The Amazon Resource Name (ARN) that identifies the resource that tags
        are listed for.
        :returns: ListTagsForResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("RegisterJobDefinition", expand=False)
    def register_job_definition(
        self, context: RequestContext, request: RegisterJobDefinitionRequest, **kwargs
    ) -> RegisterJobDefinitionResponse:
        """Registers an Batch job definition.

        :param job_definition_name: The name of the job definition to register.
        :param type: The type of job definition.
        :param parameters: Default parameter substitution placeholders to set in the job
        definition.
        :param scheduling_priority: The scheduling priority for jobs that are submitted with this job
        definition.
        :param container_properties: An object with properties specific to Amazon ECS-based single-node
        container-based jobs.
        :param node_properties: An object with properties specific to multi-node parallel jobs.
        :param retry_strategy: The retry strategy to use for failed jobs that are submitted with this
        job definition.
        :param propagate_tags: Specifies whether to propagate the tags from the job or job definition
        to the corresponding Amazon ECS task.
        :param timeout: The timeout configuration for jobs that are submitted with this job
        definition, after which Batch terminates your jobs if they have not
        finished.
        :param tags: The tags that you apply to the job definition to help you categorize and
        organize your resources.
        :param platform_capabilities: The platform capabilities required by the job definition.
        :param eks_properties: An object with properties that are specific to Amazon EKS-based jobs.
        :param ecs_properties: An object with properties that are specific to Amazon ECS-based jobs.
        :param consumable_resource_properties: Contains a list of consumable resources required by the job.
        :returns: RegisterJobDefinitionResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("SubmitJob")
    def submit_job(
        self,
        context: RequestContext,
        job_name: String,
        job_queue: String,
        job_definition: String,
        share_identifier: String | None = None,
        scheduling_priority_override: Integer | None = None,
        array_properties: ArrayProperties | None = None,
        depends_on: JobDependencyList | None = None,
        parameters: ParametersMap | None = None,
        container_overrides: ContainerOverrides | None = None,
        node_overrides: NodeOverrides | None = None,
        retry_strategy: RetryStrategy | None = None,
        propagate_tags: Boolean | None = None,
        timeout: JobTimeout | None = None,
        tags: TagrisTagsMap | None = None,
        eks_properties_override: EksPropertiesOverride | None = None,
        ecs_properties_override: EcsPropertiesOverride | None = None,
        consumable_resource_properties_override: ConsumableResourceProperties | None = None,
        **kwargs,
    ) -> SubmitJobResponse:
        """Submits an Batch job from a job definition. Parameters that are
        specified during SubmitJob override parameters defined in the job
        definition. vCPU and memory requirements that are specified in the
        ``resourceRequirements`` objects in the job definition are the
        exception. They can't be overridden this way using the ``memory`` and
        ``vcpus`` parameters. Rather, you must specify updates to job definition
        parameters in a ``resourceRequirements`` object that's included in the
        ``containerOverrides`` parameter.

        Job queues with a scheduling policy are limited to 500 active share
        identifiers at a time.

        Jobs that run on Fargate resources can't be guaranteed to run for more
        than 14 days. This is because, after 14 days, Fargate resources might
        become unavailable and job might be terminated.

        :param job_name: The name of the job.
        :param job_queue: The job queue where the job is submitted.
        :param job_definition: The job definition used by this job.
        :param share_identifier: The share identifier for the job.
        :param scheduling_priority_override: The scheduling priority for the job.
        :param array_properties: The array properties for the submitted job, such as the size of the
        array.
        :param depends_on: A list of dependencies for the job.
        :param parameters: Additional parameters passed to the job that replace parameter
        substitution placeholders that are set in the job definition.
        :param container_overrides: An object with properties that override the defaults for the job
        definition that specify the name of a container in the specified job
        definition and the overrides it should receive.
        :param node_overrides: A list of node overrides in JSON format that specify the node range to
        target and the container overrides for that node range.
        :param retry_strategy: The retry strategy to use for failed jobs from this SubmitJob operation.
        :param propagate_tags: Specifies whether to propagate the tags from the job or job definition
        to the corresponding Amazon ECS task.
        :param timeout: The timeout configuration for this SubmitJob operation.
        :param tags: The tags that you apply to the job request to help you categorize and
        organize your resources.
        :param eks_properties_override: An object, with properties that override defaults for the job
        definition, can only be specified for jobs that are run on Amazon EKS
        resources.
        :param ecs_properties_override: An object, with properties that override defaults for the job
        definition, can only be specified for jobs that are run on Amazon ECS
        resources.
        :param consumable_resource_properties_override: An object that contains overrides for the consumable resources of a job.
        :returns: SubmitJobResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: String, tags: TagrisTagsMap, **kwargs
    ) -> TagResourceResponse:
        """Associates the specified tags to a resource with the specified
        ``resourceArn``. If existing tags on a resource aren't specified in the
        request parameters, they aren't changed. When a resource is deleted, the
        tags that are associated with that resource are deleted as well. Batch
        resources that support tags are compute environments, jobs, job
        definitions, job queues, and scheduling policies. ARNs for child jobs of
        array and multi-node parallel (MNP) jobs aren't supported.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource that tags are added to.
        :param tags: The tags that you apply to the resource to help you categorize and
        organize your resources.
        :returns: TagResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("TerminateJob")
    def terminate_job(
        self, context: RequestContext, job_id: String, reason: String, **kwargs
    ) -> TerminateJobResponse:
        """Terminates a job in a job queue. Jobs that are in the ``STARTING`` or
        ``RUNNING`` state are terminated, which causes them to transition to
        ``FAILED``. Jobs that have not progressed to the ``STARTING`` state are
        cancelled.

        :param job_id: The Batch job ID of the job to terminate.
        :param reason: A message to attach to the job that explains the reason for canceling
        it.
        :returns: TerminateJobResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: String, tag_keys: TagKeysList, **kwargs
    ) -> UntagResourceResponse:
        """Deletes specified tags from an Batch resource.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource from which to delete
        tags.
        :param tag_keys: The keys of the tags to be removed.
        :returns: UntagResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("UpdateComputeEnvironment", expand=False)
    def update_compute_environment(
        self, context: RequestContext, request: UpdateComputeEnvironmentRequest, **kwargs
    ) -> UpdateComputeEnvironmentResponse:
        """Updates an Batch compute environment.

        :param compute_environment: The name or full Amazon Resource Name (ARN) of the compute environment
        to update.
        :param state: The state of the compute environment.
        :param unmanagedv_cpus: The maximum number of vCPUs expected to be used for an unmanaged compute
        environment.
        :param compute_resources: Details of the compute resources managed by the compute environment.
        :param service_role: The full Amazon Resource Name (ARN) of the IAM role that allows Batch to
        make calls to other Amazon Web Services services on your behalf.
        :param update_policy: Specifies the updated infrastructure update policy for the compute
        environment.
        :param context: Reserved.
        :returns: UpdateComputeEnvironmentResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("UpdateConsumableResource")
    def update_consumable_resource(
        self,
        context: RequestContext,
        consumable_resource: String,
        operation: String | None = None,
        quantity: Long | None = None,
        client_token: ClientRequestToken | None = None,
        **kwargs,
    ) -> UpdateConsumableResourceResponse:
        """Updates a consumable resource.

        :param consumable_resource: The name or ARN of the consumable resource to be updated.
        :param operation: Indicates how the quantity of the consumable resource will be updated.
        :param quantity: The change in the total quantity of the consumable resource.
        :param client_token: If this parameter is specified and two update requests with identical
        payloads and ``clientToken`` s are received, these requests are
        considered the same request and the second request is rejected.
        :returns: UpdateConsumableResourceResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("UpdateJobQueue")
    def update_job_queue(
        self,
        context: RequestContext,
        job_queue: String,
        state: JQState | None = None,
        scheduling_policy_arn: String | None = None,
        priority: Integer | None = None,
        compute_environment_order: ComputeEnvironmentOrders | None = None,
        job_state_time_limit_actions: JobStateTimeLimitActions | None = None,
        **kwargs,
    ) -> UpdateJobQueueResponse:
        """Updates a job queue.

        :param job_queue: The name or the Amazon Resource Name (ARN) of the job queue.
        :param state: Describes the queue's ability to accept new jobs.
        :param scheduling_policy_arn: Amazon Resource Name (ARN) of the fair-share scheduling policy.
        :param priority: The priority of the job queue.
        :param compute_environment_order: Details the set of compute environments mapped to a job queue and their
        order relative to each other.
        :param job_state_time_limit_actions: The set of actions that Batch perform on jobs that remain at the head of
        the job queue in the specified state longer than specified times.
        :returns: UpdateJobQueueResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError

    @handler("UpdateSchedulingPolicy")
    def update_scheduling_policy(
        self,
        context: RequestContext,
        arn: String,
        fairshare_policy: FairsharePolicy | None = None,
        **kwargs,
    ) -> UpdateSchedulingPolicyResponse:
        """Updates a scheduling policy.

        :param arn: The Amazon Resource Name (ARN) of the scheduling policy to update.
        :param fairshare_policy: The fair-share policy scheduling details.
        :returns: UpdateSchedulingPolicyResponse
        :raises ClientException:
        :raises ServerException:
        """
        raise NotImplementedError
