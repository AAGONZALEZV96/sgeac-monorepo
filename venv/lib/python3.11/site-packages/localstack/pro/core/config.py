import os
from typing import List, Literal

from localstack import config as localstack_config
from localstack import constants as localstack_constants
from localstack.config import is_env_true
from localstack.utils.urls import localstack_host

FALSE_STRINGS = localstack_constants.FALSE_STRINGS

ROOT_FOLDER = os.path.realpath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "..")
)

# list of folders (within the localstack.pro.core or localstack.pro.azure module) which are *not* protected
# i.e., published unencrypted
UNPROTECTED_FOLDERS = ["aws", "bootstrap", "cli", "packages", "testing"]
# list of filenames (within the localstack.pro.core module) which are *not* protected (i.e., published unencrypted)
UNPROTECTED_FILES = [
    "__init__.py",
    "plugins.py",
    "packages.py",
    "localstack-pro-core/localstack/pro/core/runtime/plugin/api.py",
]

# api server config
API_URL = localstack_constants.API_ENDPOINT

# localhost IP address and hostname
LOCALHOST_IP = "127.0.0.1"

# base domain name used for endpoints of created resources (e.g., CloudFront distributions)
RESOURCES_BASE_DOMAIN_NAME = (
    os.environ.get("RESOURCES_BASE_DOMAIN_NAME", "").strip() or localstack_host().host
)

# SMTP settings (required, e.g., for Cognito)
SMTP_HOST = os.environ.get("SMTP_HOST", "")
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
SMTP_EMAIL = os.environ.get("SMTP_EMAIL", "")

# whether to transparently set the target endpoint (by passing $AWS_ENDPOINT_URL) in
#  AWS SDK clients used in user code (e.g., Lambdas). default: true
TRANSPARENT_LOCAL_ENDPOINTS = localstack_config.is_env_not_false("TRANSPARENT_LOCAL_ENDPOINTS")

# whether to disable transparent endpoint injection or not
DISABLE_TRANSPARENT_ENDPOINT_INJECTION = localstack_config.is_env_true(
    "DISABLE_TRANSPARENT_ENDPOINT_INJECTION"
)

# whether to enforce IAM policies when processing requests
ENFORCE_IAM = localstack_config.is_env_true("ENFORCE_IAM")
IAM_SOFT_MODE = localstack_config.is_env_true("IAM_SOFT_MODE")

# endpoint URL for kube cluster (defaults to https://<docker_bridge_ip>:6443)
KUBE_ENDPOINT = os.environ.get("KUBE_ENDPOINT", "")

# toggle developer mode for extensions
EXTENSION_DEV_MODE = localstack_config.is_env_true("EXTENSION_DEV_MODE")

# List of extensions that should be installed when localstack starts
EXTENSION_AUTO_INSTALL: List[str] = [
    e.strip() for e in (os.environ.get("EXTENSION_AUTO_INSTALL") or "").split(",") if e.strip()
]

# ---
# service-specific configurations
# ---

# the endpoint strategy for AppSync GraphQL endpoints
GRAPHQL_ENDPOINT_STRATEGY: Literal["legacy", "domain", "path"] = (
    os.environ.get("GRAPHQL_ENDPOINT_STRATEGY", "") or "legacy"
)

# PUBLIC: 1 (default, pro) Only applies to new lambda provider.
# Whether to download public Lambda layers from AWS through a LocalStack proxy when creating or updating functions.
LAMBDA_DOWNLOAD_AWS_LAYERS = localstack_config.is_env_not_false("LAMBDA_DOWNLOAD_AWS_LAYERS")

# PUBLIC: 0 (default, pro) Only applies to new lambda provider
# Whether to use java sdk v2 certificate validation disabling java agent
LAMBDA_DISABLE_JAVA_SDK_V2_CERTIFICATE_VALIDATION = localstack_config.is_env_not_false(
    "LAMBDA_DISABLE_JAVA_SDK_V2_CERTIFICATE_VALIDATION"
)

# PUBLIC: amazon/aws-lambda- (default, pro)
# Prefix for images that will be used to execute Lambda functions in Kubernetes.
LAMBDA_K8S_IMAGE_PREFIX = os.environ.get("LAMBDA_K8S_IMAGE_PREFIX") or "amazon/aws-lambda-"

# PUBLIC: localstack (default, pro)
# Prefix for the Flink image that will be used to run kinesisanalyticsv2
KINESISANALYTICSV2_IMAGE = os.environ.get("KINESISANALYTICSV2_IMAGE") or "localstack/flink"

# Kubernetes pod labels. Will be added to all spawned pods
LOCALSTACK_K8S_LABELS = os.environ.get("LOCALSTACK_K8S_LABELS") or os.environ.get(
    "LAMBDA_K8S_LABELS"
)

# Kubernetes pod annotations. Will be added to all spawned pods
LOCALSTACK_K8S_ANNOTATIONS = os.environ.get("LOCALSTACK_K8S_ANNOTATIONS")

# Kubernetes pod security context. Will be set on all spawned pods
LOCALSTACK_K8S_SECURITY_CONTEXT = os.environ.get(
    "LOCALSTACK_K8S_SECURITY_CONTEXT"
) or os.environ.get("LAMBDA_K8S_SECURITY_CONTEXT")

# Kubernetes init image used for downloading the init binary into the pod when using container lambdas
LAMBDA_K8S_INIT_IMAGE = os.environ.get("LAMBDA_K8S_INIT_IMAGE")

# Kubernetes namespace for Localstack resources
LOCALSTACK_K8S_NAMESPACE = os.environ.get("LOCALSTACK_K8S_NAMESPACE", "default")

# Comma-separated hosts for which pip won't verify SSL while installing packages within MWAA container.
# Useful for LocalStack sessions inside proxied networks which inject custom SSL certificates.
# eg. 'pypi.org,pythonhosted.org,files.pythonhosted.org'
MWAA_PIP_TRUSTED_HOSTS = os.environ.get("MWAA_PIP_TRUSTED_HOSTS")

# Frequency with which MWAA polls S3 bucket for DAGs, plugins, requirements file, etc.
MWAA_S3_POLL_INTERVAL = int(os.environ.get("MWAA_S3_POLL_INTERVAL", 30))

# Extra flags to pass in to the MWAA container when creating it
MWAA_DOCKER_FLAGS = os.environ.get("MWAA_DOCKER_FLAGS")

# Experimental feature flag for CloudFront Lambda@Edge
CLOUDFRONT_LAMBDA_EDGE = is_env_true("CLOUDFRONT_LAMBDA_EDGE")

# whether to use static ports and IDs (e.g., cf-<port>) for CloudFormation distributions
CLOUDFRONT_STATIC_PORTS = localstack_config.is_env_true("CLOUDFRONT_STATIC_PORTS")

# support preventing injecting AWS_ENDPOINT_URL into containers
ECS_DISABLE_AWS_ENDPOINT_URL = localstack_config.is_env_true("ECS_DISABLE_AWS_ENDPOINT_URL")

# additional flags passed to Docker engine when creating ECS task containers
ECS_DOCKER_FLAGS = os.environ.get("ECS_DOCKER_FLAGS", "").strip()

# fluentbit image repository used in the public SSM parameters in the path /aws/service/aws-for-fluent-bit
ECS_FLUENT_BIT_IMAGE_REPOSITORY = os.environ.get(
    "ECS_FLUENT_BIT_IMAGE_REPOSITORY", "amazon/aws-for-fluent-bit"
).strip()

# whether to remove task containers after execution
ECS_REMOVE_CONTAINERS = localstack_config.is_env_not_false("ECS_REMOVE_CONTAINERS")

# which task executor runtime to use
ECS_TASK_EXECUTOR = os.environ.get("ECS_TASK_EXECUTOR", localstack_config.CONTAINER_RUNTIME).strip()

# additional flags passed to Docker engine when creating Dockerised EC2 instances
EC2_DOCKER_FLAGS = os.environ.get("EC2_DOCKER_FLAGS", "")

# whether default Docker images are downloaded at provider startup which can be used as AMIs (default: True)
EC2_DOWNLOAD_DEFAULT_IMAGES = localstack_config.is_env_not_false("EC2_DOWNLOAD_DEFAULT_IMAGES")

# EC2 VM manager which is a supported hypervisor or container engine
EC2_VM_MANAGER = (
    os.environ.get("EC2_VM_MANAGER", localstack_config.CONTAINER_RUNTIME).strip() or "docker"
)

# whether containers should be removed when EC2 instances are terminated or when LS shuts down (default: True)
EC2_REMOVE_CONTAINERS = localstack_config.is_env_not_false("EC2_REMOVE_CONTAINERS")

# start EC2 container instances with an init process by passing the `--init` to `docker run` (default: True)
EC2_DOCKER_INIT = localstack_config.is_env_not_false("EC2_DOCKER_INIT")

# Libvirt connection URI to use when hypervisor is remote
EC2_HYPERVISOR_URI = os.environ.get("EC2_HYPERVISOR_URI", "").strip() or "qemu:///system"

# Flag to enable loading of DMS provider
ENABLE_DMS = localstack_config.is_env_true("ENABLE_DMS")

# simulated delay (in seconds) before the serverless replication config is deprovisioned (will reset the table stats)
DMS_SERVERLESS_DEPROVISIONING_DELAY = int(
    os.environ.get("DMS_SERVERLESS_DEPROVISIONING_DELAY", "60").strip()
)

# simulated delay (in seconds) for status changes for serverless when calling `start-replication`
DMS_SERVERLESS_STATUS_CHANGE_WAITING_TIME = int(
    os.environ.get("DMS_SERVERLESS_STATUS_CHANGE_WAITING_TIME", "0").strip()
)

# whether to return repositoryUris in the format `<account>.dkr.ecr.<region>.localhost.localstack.cloud`
# (if "domain", default) or just `localhost.localstack.cloud` (if "off")
ECR_ENDPOINT_STRATEGY = os.environ.get("ECR_ENDPOINT_STRATEGY", "") or "domain"

# Repository override for starting an K3S EKS cluster. Overrides the repository part of the used k3s image.
# The tag will either be dependent on the specified K8S version when creating the cluster, or on `EKS_K3S_IMAGE_TAG`
EKS_K3S_IMAGE_REPOSITORY = os.environ.get("EKS_K3S_IMAGE_REPOSITORY", "rancher/k3s")

# Tag override for starting an K3S EKS cluster. Overrides the tag part of the used k3s image.
EKS_K3S_IMAGE_TAG = os.environ.get("EKS_K3S_IMAGE_TAG", "").strip()

# Chosen EKS provider for the k8s implementation. Either "k3s" or "local".
EKS_K8S_PROVIDER = os.environ.get("EKS_K8S_PROVIDER", "") or "k3s"

# simulated delay (in seconds) for creating clusters in EKS mocked mode
EKS_MOCK_CREATE_CLUSTER_DELAY = int(os.environ.get("EKS_MOCK_CREATE_CLUSTER_DELAY", "0").strip())

# startup timeout for an EKS cluster
EKS_STARTUP_TIMEOUT = int(os.environ.get("EKS_STARTUP_TIMEOUT", "180").strip())

# Allow customsiation of the k3s cluster
EKS_K3S_FLAGS = os.environ.get("EKS_K3S_FLAGS")

# Port where Hive/metastore/Spark are available for EMR/Athena
PORT_HIVE_METASTORE = int(os.getenv("PORT_HIVE_METASTORE") or 9083)
PORT_HIVE_SERVER = int(os.getenv("PORT_HIVE_SERVER") or 10000)
PORT_TRINO_SERVER = int(os.getenv("PORT_TRINO_SERVER") or 41983)
PORT_SPARK_MASTER = int(os.getenv("PORT_SPARK_MASTER") or 7077)
PORT_SPARK_UI = int(os.getenv("PORT_SPARK_UI") or 4040)

# option to force a hard-coded Spark version to be used for EMR jobs
EMR_SPARK_VERSION = str(os.getenv("EMR_SPARK_VERSION") or "").strip()

# whether to lazily install and spin up custom Postgres versions
RDS_PG_CUSTOM_VERSIONS = localstack_config.is_env_not_false("RDS_PG_CUSTOM_VERSIONS")

# override the default postgres max connections
RDS_PG_MAX_CONNECTIONS = int(os.getenv("RDS_PG_MAX_CONNECTIONS") or 0)

# whether official MySQL is supported, spins up a MySQL docker container
RDS_MYSQL_DOCKER = localstack_config.is_env_not_false("RDS_MYSQL_DOCKER")

# whether Cluster Endpoints should return the hostname only
RDS_CLUSTER_ENDPOINT_HOST_ONLY = localstack_config.is_env_not_false(
    "RDS_CLUSTER_ENDPOINT_HOST_ONLY"
)

# whether to start redis instances (ElastiCache/MemoryDB) in separate containers
REDIS_CONTAINER_MODE = localstack_config.is_env_true("REDIS_CONTAINER_MODE")

# whether DocDB should use a proxied docker container for mongodb
DOCDB_PROXY_CONTAINER = localstack_config.is_env_true("DOCDB_PROXY_CONTAINER")

# whether we serve WebSockets through the Gateway with Rolo
# Beware! This cannot be used in conjunction of `PROVIDER_OVERRIDE_APIGATEWAY=legacy`, otherwise it does not do
# anything
APIGW_ENABLE_NEXT_GEN_WEBSOCKETS = localstack_config.is_env_true("APIGW_ENABLE_NEXT_GEN_WEBSOCKETS")

# whether to enable the NextGen invocation logic of WebSockets (full rework of the invocation logic)
# this is internal to enable testing of the ongoing work.
# needs to be used in conjunction with `APIGW_ENABLE_NEXT_GEN_WEBSOCKETS=1`
APIGW_ENABLE_NEXT_GEN_WEBSOCKETS_INVOCATION = localstack_config.is_env_true(
    "APIGW_ENABLE_NEXT_GEN_WEBSOCKETS_INVOCATION"
)

# CLI file path to the auth cache populated by `localstack auth`
AUTH_CACHE_PATH = os.path.join(localstack_config.CONFIG_DIR, "auth.json")

# Whether to automatically instrument SSL sockets with authomatically generated certificates
AUTO_SSL_CERTS = localstack_config.is_env_true("AUTO_SSL_CERTS")

# Flag to enable pre-warming the Bedrock engine when Bedrock is enabled
BEDROCK_PREWARM = localstack_config.is_env_true("BEDROCK_PREWARM")

# Default model to use in Ollama
DEFAULT_BEDROCK_MODEL = os.environ.get("DEFAULT_BEDROCK_MODEL", "smollm2:360m").strip()

# Models that get downloaded and cached by the Ollama service
BEDROCK_PULL_MODELS = {
    model.strip() for model in os.environ.get("BEDROCK_PULL_MODELS", "").split(",") if model.strip()
} | {DEFAULT_BEDROCK_MODEL}

# Glue job executor to use
GLUE_JOB_EXECUTOR = os.environ.get("GLUE_JOB_EXECUTOR", "local").strip()
GLUE_JOB_EXECUTOR_PROVIDER = os.environ.get("GLUE_JOB_EXECUTOR_PROVIDER", "v1").strip()


def is_auth_token_set_in_cache() -> bool:
    """Whether the LOCALSTACK_AUTH_TOKEN was set via the `localstack auth` method. CLI-specific method."""
    # FIXME: it would probably be better to have some basic abstractions for auth token and credentials that
    #  are defined in bootstrap.auth and bootstrap.licensingv2 already in the config, then we could
    #  consolidate some of the code. until then, we need to do this "lightweight" parsing of the auth cache
    #  file.

    if not os.path.isfile(AUTH_CACHE_PATH):
        return False

    try:
        import json

        with open(AUTH_CACHE_PATH, "rb") as fd:
            if json.load(fd).get("LOCALSTACK_AUTH_TOKEN"):
                return True
    except Exception:
        pass

    return False


def is_auth_token_configured() -> bool:
    """Whether an API key is set in the environment."""
    # TODO: this method is too general for it's name. needs to be cleaned up with a clean concept for
    #  authentication that reconciles API_KEY, AUTH_TOKEN, `localstack auth`, and `localstack login`.
    if os.environ.get("LOCALSTACK_AUTH_TOKEN", "").strip():
        return True

    if is_env_true("LOCALSTACK_CLI") and is_auth_token_set_in_cache():
        return True

    if os.environ.get("LOCALSTACK_API_KEY", "").strip():
        return True

    return False


# whether pro should be activated or not. this is set to true by default if using the pro image. if set to
# true, localstack will fail to start if the key activation did not work. if set to false, then we will make
# an attempt to start localstack community.
ACTIVATE_PRO = localstack_config.is_env_not_false("ACTIVATE_PRO")

# a comma-separated list of cloud pods to be automatically loaded at startup
AUTO_LOAD_POD = os.environ.get("AUTO_LOAD_POD", "")

# if true, we encrypt the pod before sending it to the remote. It requires a secret
POD_ENCRYPTION = is_env_true("POD_ENCRYPTION")

# If enabled, we store a JSONified string of resources at pod creation time using the cloud control provider.
#   We released this feature flag with v4.0.
ENABLE_POD_RESOURCES = is_env_true("ENABLE_POD_RESOURCES")

# CLI specific.
# If set, the CLI will inject the header to authenticate to the platform.
# The header is built with the auth token in the CLI environment.
# If not set, the authentication header is built in the runtime with the token used to start the container.
# If the toke in the CLI environment and the one in the runtime differ, users might have visibility of a different
#   set of Cloud Pods.
CLI_INJECT_POD_IDENTITY = localstack_config.is_env_not_false("CLI_INJECT_POD_IDENTITY")

if is_env_true("LOCALSTACK_CLI"):
    # when we're in the CLI, we only want to activate pro code if an API key is set. this is because we are
    # always loading localstack/pro/core/config.py in the CLI, and we would otherwise always have ACTIVATE_PRO=1
    # when running `localstack start`.
    ACTIVATE_PRO = ACTIVATE_PRO and is_auth_token_configured()
    # we also need to update the environment so `ACTIVATE_PRO` is disabled in the container
    os.environ["LOCALSTACK_ACTIVATE_PRO"] = "1" if ACTIVATE_PRO else "0"

# backend service ports
DEFAULT_PORT_LOCAL_DAEMON = 4600
DEFAULT_PORT_LOCAL_DAEMON_ROOT = 4601
DISABLE_LOCAL_DAEMON_CONNECTION = localstack_config.is_env_true("DISABLE_LOCAL_DAEMON_CONNECTION")

# name of CI project to sync usage events and state with (TODO: deprecate `CI_PROJECT`)
CI_PROJECT = os.environ.get("LS_CI_PROJECT") or os.environ.get("CI_PROJECT") or ""

# PAT GitHub Token needed by CodePipeline to retrieve the source code from a private repository
CODEPIPELINE_GH_TOKEN = os.environ.get("CODEPIPELINE_GH_TOKEN")

# Flag to remove a codebuild container after a build is completed. True by default
CODEBUILD_REMOVE_CONTAINERS = localstack_config.is_env_not_false("CODEBUILD_REMOVE_CONTAINERS")

# Controls the snapshot granularity of the run. The lower the interval, the more snapshot metamodels are created
COMMIT_INTERVAL_SECS = os.environ.get("COMMIT_INTERVAL_SECS", 10)

# Controls the synchronization rate of the run. The lower the rate, the more remote synchronization requests are performed.
#  Note: If the container shuts down gracefully a synchronization request is done at the very end of the run, otherwise
#   all results up until the last synchronization request are lost.
SYNCHRONIZATION_RATE = os.environ.get("SYNCHRONIZATION_RATE", 1)

# Additional flags provided to the batch container
# only flags for volumes, ports, environment variables and add-hosts are allowed
BATCH_DOCKER_FLAGS = os.environ.get("BATCH_DOCKER_FLAGS", "")

# timeout (in seconds) to wait before returning from load operations on the CLI; 60 by default
POD_LOAD_CLI_TIMEOUT = int(os.getenv("POD_LOAD_CLI_TIMEOUT", "60"))

# whether to enforce explicit provider loading (if not set, by default providers "<x>" will be overridden by "<x>_pro")
PROVIDER_FORCE_EXPLICIT_LOADING = is_env_true("PROVIDER_FORCE_EXPLICIT_LOADING")

# whether to ignore the existing appsync js libs path
APPSYNC_JS_LIBS_VERSION = os.getenv("APPSYNC_JS_LIBS_VERSION", "latest")

# whether neptune engine should start with SSL configuration enabled
NEPTUNE_USE_SSL = localstack_config.is_env_true("NEPTUNE_USE_SSL")

# Neptune graph graph DB type, valid values: "tinkerpop", "neo4j"
NEPTUNE_DB_TYPE = (os.environ.get("NEPTUNE_DB_TYPE", "") or "tinkerpop").strip()

# whether to enable transaction for all created neptune database.
NEPTUNE_ENABLE_TRANSACTION = is_env_true("NEPTUNE_ENABLE_TRANSACTION")

# user flag to enable Gremlin logs for debugging
NEPTUNE_GREMLIN_DEBUG = is_env_true("NEPTUNE_GREMLIN_DEBUG")

# Instant job completion for MediaConvert
MEDIACONVERT_DISABLE_JOB_DURATION = is_env_true("MEDIACONVERT_DISABLE_JOB_DURATION")

# Batch provider override
BATCH_V2_PROVIDER_OVERRIDE = os.getenv("PROVIDER_OVERRIDE_BATCH") == "v2"

# update variable names that need to be passed as arguments to Docker
localstack_config.CONFIG_ENV_VARS += [
    "ACTIVATE_PRO",
    "APPSYNC_JS_LIBS_VERSION",
    "APIGW_ENABLE_NEXT_GEN_WEBSOCKETS",
    "APIGW_ENABLE_NEXT_GEN_WEBSOCKETS_INVOCATION",
    "AUTO_LOAD_POD",
    "AUTO_SSL_CERTS",
    "AUTOSTART_UTIL_CONTAINERS",
    "CI_PROJECT",
    "CODEBUILD_REMOVE_CONTAINERS",
    "CODEPIPELINE_GH_TOKEN",
    "CLOUDFRONT_STATIC_PORTS",
    "CLOUDFRONT_LAMBDA_EDGE",
    "DISABLE_LOCAL_DAEMON_CONNECTION",
    "DOCDB_PROXY_CONTAINER",
    "ECS_DISABLE_AWS_ENDPOINT_URL",
    "ECS_DOCKER_FLAGS",
    "ECS_FLUENT_BIT_IMAGE_REPOSITORY",
    "ECS_REMOVE_CONTAINERS",
    "ECS_TASK_EXECUTOR",
    "EC2_DOCKER_FLAGS",
    "EC2_DOCKER_INIT",
    "EC2_DOWNLOAD_DEFAULT_IMAGES",
    "EC2_HYPERVISOR_URI",
    "EC2_REMOVE_CONTAINERS",
    "EC2_VM_MANAGER",
    "EKS_K3S_IMAGE_REPOSITORY",
    "EKS_K3S_IMAGE_TAG",
    "EKS_K8S_PROVIDER",
    "EKS_MOCK_CREATE_CLUSTER_DELAY",
    "EKS_STARTUP_TIMEOUT",
    "EKS_K3S_FLAGS",
    "ENABLE_DMS",
    "ENABLE_POD_RESOURCES",
    "DMS_SERVERLESS_DEPROVISIONING_DELAY",
    "DMS_SERVERLESS_STATUS_CHANGE_WAITING_TIME",
    "POD_ENCRYPTION",
    "ENFORCE_IAM",
    "EXTENSION_DEV_MODE",
    "EXTENSION_AUTO_INSTALL",
    "GRAPHQL_ENDPOINT_STRATEGY",
    "IAM_SOFT_MODE",
    "KUBE_ENDPOINT",
    "LAMBDA_DOWNLOAD_AWS_LAYERS",
    "LOCALSTACK_K8S_NAMESPACE",
    "LOCALSTACK_K8S_LABELS",
    "LOCALSTACK_K8S_ANNOTATIONS",
    "KINESISANALYTICSV2_IMAGE",
    "LOG_LICENSE_ISSUES",
    "LS_CI_PROJECT",
    "LS_CI_LOGS",
    "MEDIACONVERT_DISABLE_JOB_DURATION",
    "MSSQL_ACCEPT_EULA",
    "MWAA_PIP_TRUSTED_HOSTS",
    "MWAA_S3_POLL_INTERVAL",
    "MWAA_DOCKER_FLAGS",
    "PERSIST_ALL",
    "SMTP_EMAIL",
    "SMTP_HOST",
    "SMTP_PASS",
    "SMTP_USER",
    "SSL_NO_VERIFY",
    "SYNC_POD_NAME",
    "TRANSPARENT_LOCAL_ENDPOINTS",
    "DISABLE_TRANSPARENT_ENDPOINT_INJECTION",
    "PERSIST_FLUSH_STRATEGY",
    "PROVIDER_FORCE_EXPLICIT_LOADING",
    "RDS_MYSQL_DOCKER",
    "RDS_CLUSTER_ENDPOINT_HOST_ONLY",
    "REDIS_CONTAINER_MODE",
    "POD_LOAD_CLI_TIMEOUT",
    "NEPTUNE_DB_TYPE",
    "NEPTUNE_ENABLE_TRANSACTION",
    "NEPTUNE_GREMLIN_DEBUG",
    "NEPTUNE_USE_SSL",
    # Removed in 3.0.0
    "LAMBDA_XRAY_INIT",  # deprecated since 2.0.0
    "GLUE_JOB_EXECUTOR",
    "GLUE_JOB_EXECUTOR_PROVIDER",
]

# re-initialize configs in localstack
localstack_config.populate_config_env_var_names()
