from .iam import HttpIAMAuthorizer
from .jwt import JwtAuthorizer
from .request import RequestAuthorizer

HTTP_API_AUTHORIZERS = {
    JwtAuthorizer.type: JwtAuthorizer(),
    HttpIAMAuthorizer.type: HttpIAMAuthorizer(),
    RequestAuthorizer.type: RequestAuthorizer(),
}

__all__ = [
    "HTTP_API_AUTHORIZERS",
]
