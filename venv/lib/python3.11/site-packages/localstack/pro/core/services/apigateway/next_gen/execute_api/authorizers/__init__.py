from .cognito import CognitoAuthorizer
from .iam import IAMAuthorizer
from .lambda_ import LambdaRequestAuthorizer, LambdaTokenAuthorizer

REST_API_AUTHORIZERS = {
    (CognitoAuthorizer.type, CognitoAuthorizer.name): CognitoAuthorizer(),
    (IAMAuthorizer.type, IAMAuthorizer.name): IAMAuthorizer(),
    (LambdaRequestAuthorizer.type, LambdaRequestAuthorizer.name): LambdaRequestAuthorizer(),
    (LambdaTokenAuthorizer.type, LambdaTokenAuthorizer.name): LambdaTokenAuthorizer(),
}

__all__ = [
    "REST_API_AUTHORIZERS",
]
