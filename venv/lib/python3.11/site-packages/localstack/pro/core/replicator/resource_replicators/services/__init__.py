from .ec2 import Ec2SecurityGroupReplicator, Ec2SubnetReplicator, Ec2VPCReplicator
from .ecr import EcrRepositoryReplicator
from .iam import IamPolicyReplicator, IamRoleReplicator
from .kms import KmsKeyReplicator
from .lambda_ import LambdaLayerVersionReplicator
from .route53 import Route53HostedZoneReplicator
from .secrets_manager import SecretmanagerSecretReplicator
from .ssm import SsmParameterReplicator

RESOURCE_REPLICATORS = {
    resource_replicator.type: resource_replicator
    for resource_replicator in [
        Ec2SecurityGroupReplicator,
        Ec2SubnetReplicator,
        Ec2VPCReplicator,
        EcrRepositoryReplicator,
        IamPolicyReplicator,
        IamRoleReplicator,
        KmsKeyReplicator,
        LambdaLayerVersionReplicator,
        Route53HostedZoneReplicator,
        SecretmanagerSecretReplicator,
        SsmParameterReplicator,
    ]
}

__all__ = ["RESOURCE_REPLICATORS"]
