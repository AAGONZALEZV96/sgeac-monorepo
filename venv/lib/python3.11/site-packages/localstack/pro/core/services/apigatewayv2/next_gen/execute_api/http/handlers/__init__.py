from localstack.pro.core.services.apigatewayv2.analytics import invocation_counter

from .analytics import HttpIntegrationUsageCounter
from .authorize import HttpAuthorizerHandler
from .cors import CorsResponseEnricher
from .exception import HttpApiExceptionHandler
from .integration import HttpIntegrationHandler
from .integration_request import HttpIntegrationRequestHandler
from .integration_response import HttpIntegrationResponseHandler
from .parse import HttpInvocationRequestParser
from .router import HttpInvocationRequestRouter

parse_request = HttpInvocationRequestParser()
route_request = HttpInvocationRequestRouter()
authorize = HttpAuthorizerHandler()
integration_request_handler = HttpIntegrationRequestHandler()
integration_handler = HttpIntegrationHandler()
integration_response_handler = HttpIntegrationResponseHandler()
exception_handler = HttpApiExceptionHandler()
cors_enricher = CorsResponseEnricher()
usage_counter = HttpIntegrationUsageCounter(counter=invocation_counter)
# TODO: add composite handlers for extensibility?
