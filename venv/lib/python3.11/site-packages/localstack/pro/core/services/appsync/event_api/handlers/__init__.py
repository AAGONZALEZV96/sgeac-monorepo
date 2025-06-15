from localstack.pro.core.services.appsync.event_api.handlers.authorize import AuthorizerHandler
from localstack.pro.core.services.appsync.event_api.handlers.exception import (
    EventApiExceptionHandler,
)
from localstack.pro.core.services.appsync.event_api.handlers.parse import RequestParserHandler
from localstack.pro.core.services.appsync.event_api.handlers.process_message import (
    ProcessMessageHandler,
)
from localstack.pro.core.services.appsync.event_api.handlers.publish import PublishHandler

authorize_handler = AuthorizerHandler()
process_message_handler = ProcessMessageHandler()
request_parser_handler = RequestParserHandler()
publish_handler = PublishHandler()

exception_handler = EventApiExceptionHandler()
