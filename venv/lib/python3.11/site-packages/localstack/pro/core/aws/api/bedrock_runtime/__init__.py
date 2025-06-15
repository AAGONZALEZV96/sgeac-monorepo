from datetime import datetime
from enum import StrEnum
from typing import IO, Dict, Iterable, Iterator, List, Optional, TypedDict, Union

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccountId = str
AsyncInvokeArn = str
AsyncInvokeIdempotencyToken = str
AsyncInvokeIdentifier = str
AsyncInvokeMessage = str
Boolean = bool
ConversationalModelId = str
ConverseRequestAdditionalModelResponseFieldPathsListMemberString = str
ConverseStreamRequestAdditionalModelResponseFieldPathsListMemberString = str
DocumentBlockNameString = str
GuardrailContentPolicyImageUnitsProcessed = int
GuardrailContentPolicyUnitsProcessed = int
GuardrailContextualGroundingFilterScoreDouble = float
GuardrailContextualGroundingFilterThresholdDouble = float
GuardrailContextualGroundingPolicyUnitsProcessed = int
GuardrailIdentifier = str
GuardrailOutputText = str
GuardrailSensitiveInformationPolicyFreeUnitsProcessed = int
GuardrailSensitiveInformationPolicyUnitsProcessed = int
GuardrailTopicPolicyUnitsProcessed = int
GuardrailVersion = str
GuardrailWordPolicyUnitsProcessed = int
ImagesGuarded = int
ImagesTotal = int
InferenceConfigurationMaxTokensInteger = int
InferenceConfigurationTemperatureFloat = float
InferenceConfigurationTopPFloat = float
InvocationArn = str
InvokeModelIdentifier = str
InvokedModelId = str
KmsKeyId = str
MaxResults = int
MimeType = str
NonBlankString = str
NonEmptyString = str
NonNegativeInteger = int
PaginationToken = str
RequestMetadataKeyString = str
RequestMetadataValueString = str
S3Uri = str
StatusCode = int
String = str
TagKey = str
TagValue = str
TextCharactersGuarded = int
TextCharactersTotal = int
TokenUsageCacheReadInputTokensInteger = int
TokenUsageCacheWriteInputTokensInteger = int
TokenUsageInputTokensInteger = int
TokenUsageOutputTokensInteger = int
TokenUsageTotalTokensInteger = int
ToolName = str
ToolUseId = str


class AsyncInvokeStatus(StrEnum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"


class CachePointType(StrEnum):
    default = "default"


class ConversationRole(StrEnum):
    user = "user"
    assistant = "assistant"


class DocumentFormat(StrEnum):
    pdf = "pdf"
    csv = "csv"
    doc = "doc"
    docx = "docx"
    xls = "xls"
    xlsx = "xlsx"
    html = "html"
    txt = "txt"
    md = "md"


class GuardrailAction(StrEnum):
    NONE = "NONE"
    GUARDRAIL_INTERVENED = "GUARDRAIL_INTERVENED"


class GuardrailContentFilterConfidence(StrEnum):
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class GuardrailContentFilterStrength(StrEnum):
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class GuardrailContentFilterType(StrEnum):
    INSULTS = "INSULTS"
    HATE = "HATE"
    SEXUAL = "SEXUAL"
    VIOLENCE = "VIOLENCE"
    MISCONDUCT = "MISCONDUCT"
    PROMPT_ATTACK = "PROMPT_ATTACK"


class GuardrailContentPolicyAction(StrEnum):
    BLOCKED = "BLOCKED"
    NONE = "NONE"


class GuardrailContentQualifier(StrEnum):
    grounding_source = "grounding_source"
    query = "query"
    guard_content = "guard_content"


class GuardrailContentSource(StrEnum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


class GuardrailContextualGroundingFilterType(StrEnum):
    GROUNDING = "GROUNDING"
    RELEVANCE = "RELEVANCE"


class GuardrailContextualGroundingPolicyAction(StrEnum):
    BLOCKED = "BLOCKED"
    NONE = "NONE"


class GuardrailConverseContentQualifier(StrEnum):
    grounding_source = "grounding_source"
    query = "query"
    guard_content = "guard_content"


class GuardrailConverseImageFormat(StrEnum):
    png = "png"
    jpeg = "jpeg"


class GuardrailImageFormat(StrEnum):
    png = "png"
    jpeg = "jpeg"


class GuardrailManagedWordType(StrEnum):
    PROFANITY = "PROFANITY"


class GuardrailOutputScope(StrEnum):
    INTERVENTIONS = "INTERVENTIONS"
    FULL = "FULL"


class GuardrailPiiEntityType(StrEnum):
    ADDRESS = "ADDRESS"
    AGE = "AGE"
    AWS_ACCESS_KEY = "AWS_ACCESS_KEY"
    AWS_SECRET_KEY = "AWS_SECRET_KEY"
    CA_HEALTH_NUMBER = "CA_HEALTH_NUMBER"
    CA_SOCIAL_INSURANCE_NUMBER = "CA_SOCIAL_INSURANCE_NUMBER"
    CREDIT_DEBIT_CARD_CVV = "CREDIT_DEBIT_CARD_CVV"
    CREDIT_DEBIT_CARD_EXPIRY = "CREDIT_DEBIT_CARD_EXPIRY"
    CREDIT_DEBIT_CARD_NUMBER = "CREDIT_DEBIT_CARD_NUMBER"
    DRIVER_ID = "DRIVER_ID"
    EMAIL = "EMAIL"
    INTERNATIONAL_BANK_ACCOUNT_NUMBER = "INTERNATIONAL_BANK_ACCOUNT_NUMBER"
    IP_ADDRESS = "IP_ADDRESS"
    LICENSE_PLATE = "LICENSE_PLATE"
    MAC_ADDRESS = "MAC_ADDRESS"
    NAME = "NAME"
    PASSWORD = "PASSWORD"
    PHONE = "PHONE"
    PIN = "PIN"
    SWIFT_CODE = "SWIFT_CODE"
    UK_NATIONAL_HEALTH_SERVICE_NUMBER = "UK_NATIONAL_HEALTH_SERVICE_NUMBER"
    UK_NATIONAL_INSURANCE_NUMBER = "UK_NATIONAL_INSURANCE_NUMBER"
    UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER = "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER"
    URL = "URL"
    USERNAME = "USERNAME"
    US_BANK_ACCOUNT_NUMBER = "US_BANK_ACCOUNT_NUMBER"
    US_BANK_ROUTING_NUMBER = "US_BANK_ROUTING_NUMBER"
    US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER = "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER"
    US_PASSPORT_NUMBER = "US_PASSPORT_NUMBER"
    US_SOCIAL_SECURITY_NUMBER = "US_SOCIAL_SECURITY_NUMBER"
    VEHICLE_IDENTIFICATION_NUMBER = "VEHICLE_IDENTIFICATION_NUMBER"


class GuardrailSensitiveInformationPolicyAction(StrEnum):
    ANONYMIZED = "ANONYMIZED"
    BLOCKED = "BLOCKED"
    NONE = "NONE"


class GuardrailStreamProcessingMode(StrEnum):
    sync = "sync"
    async_ = "async"


class GuardrailTopicPolicyAction(StrEnum):
    BLOCKED = "BLOCKED"
    NONE = "NONE"


class GuardrailTopicType(StrEnum):
    DENY = "DENY"


class GuardrailTrace(StrEnum):
    enabled = "enabled"
    disabled = "disabled"
    enabled_full = "enabled_full"


class GuardrailWordPolicyAction(StrEnum):
    BLOCKED = "BLOCKED"
    NONE = "NONE"


class ImageFormat(StrEnum):
    png = "png"
    jpeg = "jpeg"
    gif = "gif"
    webp = "webp"


class PerformanceConfigLatency(StrEnum):
    standard = "standard"
    optimized = "optimized"


class SortAsyncInvocationBy(StrEnum):
    SubmissionTime = "SubmissionTime"


class SortOrder(StrEnum):
    Ascending = "Ascending"
    Descending = "Descending"


class StopReason(StrEnum):
    end_turn = "end_turn"
    tool_use = "tool_use"
    max_tokens = "max_tokens"
    stop_sequence = "stop_sequence"
    guardrail_intervened = "guardrail_intervened"
    content_filtered = "content_filtered"


class ToolResultStatus(StrEnum):
    success = "success"
    error = "error"


class Trace(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLED_FULL = "ENABLED_FULL"


class VideoFormat(StrEnum):
    mkv = "mkv"
    mov = "mov"
    mp4 = "mp4"
    webm = "webm"
    flv = "flv"
    mpeg = "mpeg"
    mpg = "mpg"
    wmv = "wmv"
    three_gp = "three_gp"


class AccessDeniedException(ServiceException):
    """The request is denied because you do not have sufficient permissions to
    perform the requested action. For troubleshooting this error, see
    `AccessDeniedException <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied>`__
    in the Amazon Bedrock User Guide
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = True
    status_code: int = 403


class ConflictException(ServiceException):
    """Error occurred because of a conflict while performing an operation."""

    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 400


class InternalServerException(ServiceException):
    """An internal server error occurred. For troubleshooting this error, see
    `InternalFailure <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure>`__
    in the Amazon Bedrock User Guide
    """

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500


class ModelErrorException(ServiceException):
    """The request failed due to an error while processing the model."""

    code: str = "ModelErrorException"
    sender_fault: bool = True
    status_code: int = 424
    originalStatusCode: Optional[StatusCode]
    resourceName: Optional[NonBlankString]


class ModelNotReadyException(ServiceException):
    """The model specified in the request is not ready to serve inference
    requests. The AWS SDK will automatically retry the operation up to 5
    times. For information about configuring automatic retries, see `Retry
    behavior <https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html>`__
    in the *AWS SDKs and Tools* reference guide.
    """

    code: str = "ModelNotReadyException"
    sender_fault: bool = True
    status_code: int = 429


class ModelStreamErrorException(ServiceException):
    """An error occurred while streaming the response. Retry your request."""

    code: str = "ModelStreamErrorException"
    sender_fault: bool = True
    status_code: int = 424
    originalStatusCode: Optional[StatusCode]
    originalMessage: Optional[NonBlankString]


class ModelTimeoutException(ServiceException):
    """The request took too long to process. Processing time exceeded the model
    timeout length.
    """

    code: str = "ModelTimeoutException"
    sender_fault: bool = True
    status_code: int = 408


class ResourceNotFoundException(ServiceException):
    """The specified resource ARN was not found. For troubleshooting this
    error, see
    `ResourceNotFound <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found>`__
    in the Amazon Bedrock User Guide
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class ServiceQuotaExceededException(ServiceException):
    """Your request exceeds the service quota for your account. You can view
    your quotas at `Viewing service
    quotas <https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html>`__.
    You can resubmit your request later.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = True
    status_code: int = 400


class ServiceUnavailableException(ServiceException):
    """The service isn't currently available. For troubleshooting this error,
    see
    `ServiceUnavailable <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable>`__
    in the Amazon Bedrock User Guide
    """

    code: str = "ServiceUnavailableException"
    sender_fault: bool = False
    status_code: int = 503


class ThrottlingException(ServiceException):
    """Your request was denied due to exceeding the account quotas for *Amazon
    Bedrock*. For troubleshooting this error, see
    `ThrottlingException <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception>`__
    in the Amazon Bedrock User Guide
    """

    code: str = "ThrottlingException"
    sender_fault: bool = True
    status_code: int = 429


class ValidationException(ServiceException):
    """The input fails to satisfy the constraints specified by *Amazon
    Bedrock*. For troubleshooting this error, see
    `ValidationError <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error>`__
    in the Amazon Bedrock User Guide
    """

    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400


class AnyToolChoice(TypedDict, total=False):
    """The model must request at least one tool (no text is generated). For
    example, ``{"any" : {}}``.
    """

    pass


GuardrailImageSourceBytesBlob = bytes


class GuardrailImageSource(TypedDict, total=False):
    """The image source (image bytes) of the guardrail image source. Object
    used in independent api.
    """

    bytes: Optional[GuardrailImageSourceBytesBlob]


class GuardrailImageBlock(TypedDict, total=False):
    """Contain an image which user wants guarded. This block is accepted by the
    guardrails independent API.
    """

    format: GuardrailImageFormat
    source: GuardrailImageSource


GuardrailContentQualifierList = List[GuardrailContentQualifier]


class GuardrailTextBlock(TypedDict, total=False):
    """The text block to be evaluated by the guardrail."""

    text: String
    qualifiers: Optional[GuardrailContentQualifierList]


class GuardrailContentBlock(TypedDict, total=False):
    """The content block to be evaluated by the guardrail."""

    text: Optional[GuardrailTextBlock]
    image: Optional[GuardrailImageBlock]


GuardrailContentBlockList = List[GuardrailContentBlock]


class ApplyGuardrailRequest(ServiceRequest):
    guardrailIdentifier: GuardrailIdentifier
    guardrailVersion: GuardrailVersion
    source: GuardrailContentSource
    content: GuardrailContentBlockList
    outputScope: Optional[GuardrailOutputScope]


class GuardrailImageCoverage(TypedDict, total=False):
    """The details of the guardrail image coverage."""

    guarded: Optional[ImagesGuarded]
    total: Optional[ImagesTotal]


class GuardrailTextCharactersCoverage(TypedDict, total=False):
    """The guardrail coverage for the text characters."""

    guarded: Optional[TextCharactersGuarded]
    total: Optional[TextCharactersTotal]


class GuardrailCoverage(TypedDict, total=False):
    """The action of the guardrail coverage details."""

    textCharacters: Optional[GuardrailTextCharactersCoverage]
    images: Optional[GuardrailImageCoverage]


class GuardrailUsage(TypedDict, total=False):
    """The details on the use of the guardrail."""

    topicPolicyUnits: GuardrailTopicPolicyUnitsProcessed
    contentPolicyUnits: GuardrailContentPolicyUnitsProcessed
    wordPolicyUnits: GuardrailWordPolicyUnitsProcessed
    sensitiveInformationPolicyUnits: GuardrailSensitiveInformationPolicyUnitsProcessed
    sensitiveInformationPolicyFreeUnits: GuardrailSensitiveInformationPolicyFreeUnitsProcessed
    contextualGroundingPolicyUnits: GuardrailContextualGroundingPolicyUnitsProcessed
    contentPolicyImageUnits: Optional[GuardrailContentPolicyImageUnitsProcessed]


GuardrailProcessingLatency = int


class GuardrailInvocationMetrics(TypedDict, total=False):
    """The invocation metrics for the guardrail."""

    guardrailProcessingLatency: Optional[GuardrailProcessingLatency]
    usage: Optional[GuardrailUsage]
    guardrailCoverage: Optional[GuardrailCoverage]


GuardrailContextualGroundingFilter = TypedDict(
    "GuardrailContextualGroundingFilter",
    {
        "type": GuardrailContextualGroundingFilterType,
        "threshold": GuardrailContextualGroundingFilterThresholdDouble,
        "score": GuardrailContextualGroundingFilterScoreDouble,
        "action": GuardrailContextualGroundingPolicyAction,
        "detected": Optional[Boolean],
    },
    total=False,
)
GuardrailContextualGroundingFilters = List[GuardrailContextualGroundingFilter]


class GuardrailContextualGroundingPolicyAssessment(TypedDict, total=False):
    """The policy assessment details for the guardrails contextual grounding
    filter.
    """

    filters: Optional[GuardrailContextualGroundingFilters]


class GuardrailRegexFilter(TypedDict, total=False):
    """A Regex filter configured in a guardrail."""

    name: Optional[String]
    match: Optional[String]
    regex: Optional[String]
    action: GuardrailSensitiveInformationPolicyAction
    detected: Optional[Boolean]


GuardrailRegexFilterList = List[GuardrailRegexFilter]
GuardrailPiiEntityFilter = TypedDict(
    "GuardrailPiiEntityFilter",
    {
        "match": String,
        "type": GuardrailPiiEntityType,
        "action": GuardrailSensitiveInformationPolicyAction,
        "detected": Optional[Boolean],
    },
    total=False,
)
GuardrailPiiEntityFilterList = List[GuardrailPiiEntityFilter]


class GuardrailSensitiveInformationPolicyAssessment(TypedDict, total=False):
    """The assessment for aPersonally Identifiable Information (PII) policy."""

    piiEntities: GuardrailPiiEntityFilterList
    regexes: GuardrailRegexFilterList


GuardrailManagedWord = TypedDict(
    "GuardrailManagedWord",
    {
        "match": String,
        "type": GuardrailManagedWordType,
        "action": GuardrailWordPolicyAction,
        "detected": Optional[Boolean],
    },
    total=False,
)
GuardrailManagedWordList = List[GuardrailManagedWord]


class GuardrailCustomWord(TypedDict, total=False):
    """A custom word configured in a guardrail."""

    match: String
    action: GuardrailWordPolicyAction
    detected: Optional[Boolean]


GuardrailCustomWordList = List[GuardrailCustomWord]


class GuardrailWordPolicyAssessment(TypedDict, total=False):
    """The word policy assessment."""

    customWords: GuardrailCustomWordList
    managedWordLists: GuardrailManagedWordList


GuardrailContentFilter = TypedDict(
    "GuardrailContentFilter",
    {
        "type": GuardrailContentFilterType,
        "confidence": GuardrailContentFilterConfidence,
        "filterStrength": Optional[GuardrailContentFilterStrength],
        "action": GuardrailContentPolicyAction,
        "detected": Optional[Boolean],
    },
    total=False,
)
GuardrailContentFilterList = List[GuardrailContentFilter]


class GuardrailContentPolicyAssessment(TypedDict, total=False):
    """An assessment of a content policy for a guardrail."""

    filters: GuardrailContentFilterList


GuardrailTopic = TypedDict(
    "GuardrailTopic",
    {
        "name": String,
        "type": GuardrailTopicType,
        "action": GuardrailTopicPolicyAction,
        "detected": Optional[Boolean],
    },
    total=False,
)
GuardrailTopicList = List[GuardrailTopic]


class GuardrailTopicPolicyAssessment(TypedDict, total=False):
    """A behavior assessment of a topic policy."""

    topics: GuardrailTopicList


class GuardrailAssessment(TypedDict, total=False):
    """A behavior assessment of the guardrail policies used in a call to the
    Converse API.
    """

    topicPolicy: Optional[GuardrailTopicPolicyAssessment]
    contentPolicy: Optional[GuardrailContentPolicyAssessment]
    wordPolicy: Optional[GuardrailWordPolicyAssessment]
    sensitiveInformationPolicy: Optional[GuardrailSensitiveInformationPolicyAssessment]
    contextualGroundingPolicy: Optional[GuardrailContextualGroundingPolicyAssessment]
    invocationMetrics: Optional[GuardrailInvocationMetrics]


GuardrailAssessmentList = List[GuardrailAssessment]


class GuardrailOutputContent(TypedDict, total=False):
    """The output content produced by the guardrail."""

    text: Optional[GuardrailOutputText]


GuardrailOutputContentList = List[GuardrailOutputContent]


class ApplyGuardrailResponse(TypedDict, total=False):
    usage: GuardrailUsage
    action: GuardrailAction
    actionReason: Optional[String]
    outputs: GuardrailOutputContentList
    assessments: GuardrailAssessmentList
    guardrailCoverage: Optional[GuardrailCoverage]


class AsyncInvokeS3OutputDataConfig(TypedDict, total=False):
    """Asynchronous invocation output data settings."""

    s3Uri: S3Uri
    kmsKeyId: Optional[KmsKeyId]
    bucketOwner: Optional[AccountId]


class AsyncInvokeOutputDataConfig(TypedDict, total=False):
    """Asynchronous invocation output data settings."""

    s3OutputDataConfig: Optional[AsyncInvokeS3OutputDataConfig]


Timestamp = datetime


class AsyncInvokeSummary(TypedDict, total=False):
    """A summary of an asynchronous invocation."""

    invocationArn: InvocationArn
    modelArn: AsyncInvokeArn
    clientRequestToken: Optional[AsyncInvokeIdempotencyToken]
    status: Optional[AsyncInvokeStatus]
    failureMessage: Optional[AsyncInvokeMessage]
    submitTime: Timestamp
    lastModifiedTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    outputDataConfig: AsyncInvokeOutputDataConfig


AsyncInvokeSummaries = List[AsyncInvokeSummary]


class AutoToolChoice(TypedDict, total=False):
    """The Model automatically decides if a tool should be called or whether to
    generate text instead. For example, ``{"auto" : {}}``.
    """

    pass


PartBody = bytes


class BidirectionalInputPayloadPart(TypedDict, total=False):
    """Payload content for the bidirectional input. The input is an audio
    stream.
    """

    bytes: Optional[PartBody]


class BidirectionalOutputPayloadPart(TypedDict, total=False):
    """Output from the bidirectional stream. The output is speech and a text
    transcription.
    """

    bytes: Optional[PartBody]


Blob = bytes
Body = bytes
CachePointBlock = TypedDict(
    "CachePointBlock",
    {
        "type": CachePointType,
    },
    total=False,
)


class ReasoningTextBlock(TypedDict, total=False):
    """Contains the reasoning that the model used to return the output."""

    text: String
    signature: Optional[String]


class ReasoningContentBlock(TypedDict, total=False):
    """Contains content regarding the reasoning that is carried out by the
    model with respect to the content in the content block. Reasoning refers
    to a Chain of Thought (CoT) that the model generates to enhance the
    accuracy of its final response.
    """

    reasoningText: Optional[ReasoningTextBlock]
    redactedContent: Optional[Blob]


GuardrailConverseImageSourceBytesBlob = bytes


class GuardrailConverseImageSource(TypedDict, total=False):
    """The image source (image bytes) of the guardrail converse image source."""

    bytes: Optional[GuardrailConverseImageSourceBytesBlob]


class GuardrailConverseImageBlock(TypedDict, total=False):
    """An image block that contains images that you want to assess with a
    guardrail.
    """

    format: GuardrailConverseImageFormat
    source: GuardrailConverseImageSource


GuardrailConverseContentQualifierList = List[GuardrailConverseContentQualifier]


class GuardrailConverseTextBlock(TypedDict, total=False):
    """A text block that contains text that you want to assess with a
    guardrail. For more information, see GuardrailConverseContentBlock.
    """

    text: String
    qualifiers: Optional[GuardrailConverseContentQualifierList]


class GuardrailConverseContentBlock(TypedDict, total=False):
    """A content block for selective guarding with the
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
    or
    `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__
    API operations.
    """

    text: Optional[GuardrailConverseTextBlock]
    image: Optional[GuardrailConverseImageBlock]


class S3Location(TypedDict, total=False):
    """A storage location in an Amazon S3 bucket."""

    uri: S3Uri
    bucketOwner: Optional[AccountId]


VideoSourceBytesBlob = bytes


class VideoSource(TypedDict, total=False):
    """A video source. You can upload a smaller video as a base64-encoded
    string as long as the encoded file is less than 25MB. You can also
    transfer videos up to 1GB in size from an S3 bucket.
    """

    bytes: Optional[VideoSourceBytesBlob]
    s3Location: Optional[S3Location]


class VideoBlock(TypedDict, total=False):
    """A video block."""

    format: VideoFormat
    source: VideoSource


DocumentSourceBytesBlob = bytes


class DocumentSource(TypedDict, total=False):
    """Contains the content of a document."""

    bytes: Optional[DocumentSourceBytesBlob]
    s3Location: Optional[S3Location]


class DocumentBlock(TypedDict, total=False):
    """A document to include in a message."""

    format: DocumentFormat
    name: DocumentBlockNameString
    source: DocumentSource


ImageSourceBytesBlob = bytes


class ImageSource(TypedDict, total=False):
    """The source for an image."""

    bytes: Optional[ImageSourceBytesBlob]
    s3Location: Optional[S3Location]


class ImageBlock(TypedDict, total=False):
    """Image content for a message."""

    format: ImageFormat
    source: ImageSource


class Document(TypedDict, total=False):
    pass


class ToolResultContentBlock(TypedDict, total=False):
    """The tool result content block."""

    json: Optional[Document]
    text: Optional[String]
    image: Optional[ImageBlock]
    document: Optional[DocumentBlock]
    video: Optional[VideoBlock]


ToolResultContentBlocks = List[ToolResultContentBlock]


class ToolResultBlock(TypedDict, total=False):
    """A tool result block that contains the results for a tool request that
    the model previously made.
    """

    toolUseId: ToolUseId
    content: ToolResultContentBlocks
    status: Optional[ToolResultStatus]


class ToolUseBlock(TypedDict, total=False):
    """A tool use content block. Contains information about a tool that the
    model is requesting be run., The model uses the result from the tool to
    generate a response.
    """

    toolUseId: ToolUseId
    name: ToolName
    input: Document


class ContentBlock(TypedDict, total=False):
    """A block of content for a message that you pass to, or receive from, a
    model with the
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
    or
    `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__
    API operations.
    """

    text: Optional[String]
    image: Optional[ImageBlock]
    document: Optional[DocumentBlock]
    video: Optional[VideoBlock]
    toolUse: Optional[ToolUseBlock]
    toolResult: Optional[ToolResultBlock]
    guardContent: Optional[GuardrailConverseContentBlock]
    cachePoint: Optional[CachePointBlock]
    reasoningContent: Optional[ReasoningContentBlock]


class ReasoningContentBlockDelta(TypedDict, total=False):
    """Contains content regarding the reasoning that is carried out by the
    model with respect to the content in the content block. Reasoning refers
    to a Chain of Thought (CoT) that the model generates to enhance the
    accuracy of its final response.
    """

    text: Optional[String]
    redactedContent: Optional[Blob]
    signature: Optional[String]


class ToolUseBlockDelta(TypedDict, total=False):
    """The delta for a tool use block."""

    input: String


class ContentBlockDelta(TypedDict, total=False):
    """A block of content in a streaming response."""

    text: Optional[String]
    toolUse: Optional[ToolUseBlockDelta]
    reasoningContent: Optional[ReasoningContentBlockDelta]


class ContentBlockDeltaEvent(TypedDict, total=False):
    """The content block delta event."""

    delta: ContentBlockDelta
    contentBlockIndex: NonNegativeInteger


class ToolUseBlockStart(TypedDict, total=False):
    """The start of a tool use block."""

    toolUseId: ToolUseId
    name: ToolName


class ContentBlockStart(TypedDict, total=False):
    """Content block start information."""

    toolUse: Optional[ToolUseBlockStart]


class ContentBlockStartEvent(TypedDict, total=False):
    """Content block start event."""

    start: ContentBlockStart
    contentBlockIndex: NonNegativeInteger


class ContentBlockStopEvent(TypedDict, total=False):
    """A content block stop event."""

    contentBlockIndex: NonNegativeInteger


ContentBlocks = List[ContentBlock]
Long = int


class ConverseMetrics(TypedDict, total=False):
    """Metrics for a call to
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__.
    """

    latencyMs: Long


class Message(TypedDict, total=False):
    """A message input, or returned from, a call to
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
    or
    `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__.
    """

    role: ConversationRole
    content: ContentBlocks


class ConverseOutput(TypedDict, total=False):
    """The output from a call to
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__.
    """

    message: Optional[Message]


class PerformanceConfiguration(TypedDict, total=False):
    """Performance settings for a model."""

    latency: Optional[PerformanceConfigLatency]


RequestMetadata = Dict[RequestMetadataKeyString, RequestMetadataValueString]
ConverseRequestAdditionalModelResponseFieldPathsList = List[
    ConverseRequestAdditionalModelResponseFieldPathsListMemberString
]


class PromptVariableValues(TypedDict, total=False):
    """Contains a map of variables in a prompt from Prompt management to an
    object containing the values to fill in for them when running model
    invocation. For more information, see `How Prompt management
    works <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-how.html>`__.
    """

    text: Optional[String]


PromptVariableMap = Dict[String, PromptVariableValues]


class GuardrailConfiguration(TypedDict, total=False):
    """Configuration information for a guardrail that you use with the
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
    operation.
    """

    guardrailIdentifier: GuardrailIdentifier
    guardrailVersion: GuardrailVersion
    trace: Optional[GuardrailTrace]


class SpecificToolChoice(TypedDict, total=False):
    """The model must request a specific tool. For example,
    ``{"tool" : {"name" : "Your tool name"}}``.

    This field is only supported by Anthropic Claude 3 models.
    """

    name: ToolName


class ToolChoice(TypedDict, total=False):
    """Determines which tools the model should request in a call to
    ``Converse`` or ``ConverseStream``. ``ToolChoice`` is only supported by
    Anthropic Claude 3 models and by Mistral AI Mistral Large.
    """

    auto: Optional[AutoToolChoice]
    any: Optional[AnyToolChoice]
    tool: Optional[SpecificToolChoice]


class ToolInputSchema(TypedDict, total=False):
    """The schema for the tool. The top level schema type must be ``object``."""

    json: Optional[Document]


class ToolSpecification(TypedDict, total=False):
    """The specification for the tool."""

    name: ToolName
    description: Optional[NonEmptyString]
    inputSchema: ToolInputSchema


class Tool(TypedDict, total=False):
    """Information about a tool that you can use with the Converse API. For
    more information, see `Tool use (function
    calling) <https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html>`__
    in the Amazon Bedrock User Guide.
    """

    toolSpec: Optional[ToolSpecification]
    cachePoint: Optional[CachePointBlock]


ToolConfigurationToolsList = List[Tool]


class ToolConfiguration(TypedDict, total=False):
    """Configuration information for the tools that you pass to a model. For
    more information, see `Tool use (function
    calling) <https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html>`__
    in the Amazon Bedrock User Guide.
    """

    tools: ToolConfigurationToolsList
    toolChoice: Optional[ToolChoice]


InferenceConfigurationStopSequencesList = List[NonEmptyString]


class InferenceConfiguration(TypedDict, total=False):
    """Base inference parameters to pass to a model in a call to
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
    or
    `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__.
    For more information, see `Inference parameters for foundation
    models <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html>`__.

    If you need to pass additional parameters that the model supports, use
    the ``additionalModelRequestFields`` request field in the call to
    ``Converse`` or ``ConverseStream``. For more information, see `Model
    parameters <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html>`__.
    """

    maxTokens: Optional[InferenceConfigurationMaxTokensInteger]
    temperature: Optional[InferenceConfigurationTemperatureFloat]
    topP: Optional[InferenceConfigurationTopPFloat]
    stopSequences: Optional[InferenceConfigurationStopSequencesList]


class SystemContentBlock(TypedDict, total=False):
    """A system content block."""

    text: Optional[NonEmptyString]
    guardContent: Optional[GuardrailConverseContentBlock]
    cachePoint: Optional[CachePointBlock]


SystemContentBlocks = List[SystemContentBlock]
Messages = List[Message]


class ConverseRequest(ServiceRequest):
    modelId: ConversationalModelId
    messages: Optional[Messages]
    system: Optional[SystemContentBlocks]
    inferenceConfig: Optional[InferenceConfiguration]
    toolConfig: Optional[ToolConfiguration]
    guardrailConfig: Optional[GuardrailConfiguration]
    additionalModelRequestFields: Optional[Document]
    promptVariables: Optional[PromptVariableMap]
    additionalModelResponseFieldPaths: Optional[
        ConverseRequestAdditionalModelResponseFieldPathsList
    ]
    requestMetadata: Optional[RequestMetadata]
    performanceConfig: Optional[PerformanceConfiguration]


class PromptRouterTrace(TypedDict, total=False):
    """A prompt router trace."""

    invokedModelId: Optional[InvokedModelId]


GuardrailAssessmentListMap = Dict[String, GuardrailAssessmentList]
GuardrailAssessmentMap = Dict[String, GuardrailAssessment]
ModelOutputs = List[GuardrailOutputText]


class GuardrailTraceAssessment(TypedDict, total=False):
    """A Top level guardrail trace object. For more information, see
    ConverseTrace.
    """

    modelOutput: Optional[ModelOutputs]
    inputAssessment: Optional[GuardrailAssessmentMap]
    outputAssessments: Optional[GuardrailAssessmentListMap]
    actionReason: Optional[String]


class ConverseTrace(TypedDict, total=False):
    """The trace object in a response from
    `Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__.
    Currently, you can only trace guardrails.
    """

    guardrail: Optional[GuardrailTraceAssessment]
    promptRouter: Optional[PromptRouterTrace]


class TokenUsage(TypedDict, total=False):
    """The tokens used in a message API inference call."""

    inputTokens: TokenUsageInputTokensInteger
    outputTokens: TokenUsageOutputTokensInteger
    totalTokens: TokenUsageTotalTokensInteger
    cacheReadInputTokens: Optional[TokenUsageCacheReadInputTokensInteger]
    cacheWriteInputTokens: Optional[TokenUsageCacheWriteInputTokensInteger]


class ConverseResponse(TypedDict, total=False):
    output: ConverseOutput
    stopReason: StopReason
    usage: TokenUsage
    metrics: ConverseMetrics
    additionalModelResponseFields: Optional[Document]
    trace: Optional[ConverseTrace]
    performanceConfig: Optional[PerformanceConfiguration]


class ConverseStreamTrace(TypedDict, total=False):
    """The trace object in a response from
    `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__.
    Currently, you can only trace guardrails.
    """

    guardrail: Optional[GuardrailTraceAssessment]
    promptRouter: Optional[PromptRouterTrace]


class ConverseStreamMetrics(TypedDict, total=False):
    """Metrics for the stream."""

    latencyMs: Long


class ConverseStreamMetadataEvent(TypedDict, total=False):
    """A conversation stream metadata event."""

    usage: TokenUsage
    metrics: ConverseStreamMetrics
    trace: Optional[ConverseStreamTrace]
    performanceConfig: Optional[PerformanceConfiguration]


class MessageStopEvent(TypedDict, total=False):
    """The stop event for a message."""

    stopReason: StopReason
    additionalModelResponseFields: Optional[Document]


class MessageStartEvent(TypedDict, total=False):
    """The start of a message."""

    role: ConversationRole


class ConverseStreamOutput(TypedDict, total=False):
    """The messages output stream"""

    messageStart: Optional[MessageStartEvent]
    contentBlockStart: Optional[ContentBlockStartEvent]
    contentBlockDelta: Optional[ContentBlockDeltaEvent]
    contentBlockStop: Optional[ContentBlockStopEvent]
    messageStop: Optional[MessageStopEvent]
    metadata: Optional[ConverseStreamMetadataEvent]
    internalServerException: Optional[InternalServerException]
    modelStreamErrorException: Optional[ModelStreamErrorException]
    validationException: Optional[ValidationException]
    throttlingException: Optional[ThrottlingException]
    serviceUnavailableException: Optional[ServiceUnavailableException]


ConverseStreamRequestAdditionalModelResponseFieldPathsList = List[
    ConverseStreamRequestAdditionalModelResponseFieldPathsListMemberString
]


class GuardrailStreamConfiguration(TypedDict, total=False):
    """Configuration information for a guardrail that you use with the
    ConverseStream action.
    """

    guardrailIdentifier: GuardrailIdentifier
    guardrailVersion: GuardrailVersion
    trace: Optional[GuardrailTrace]
    streamProcessingMode: Optional[GuardrailStreamProcessingMode]


class ConverseStreamRequest(ServiceRequest):
    modelId: ConversationalModelId
    messages: Optional[Messages]
    system: Optional[SystemContentBlocks]
    inferenceConfig: Optional[InferenceConfiguration]
    toolConfig: Optional[ToolConfiguration]
    guardrailConfig: Optional[GuardrailStreamConfiguration]
    additionalModelRequestFields: Optional[Document]
    promptVariables: Optional[PromptVariableMap]
    additionalModelResponseFieldPaths: Optional[
        ConverseStreamRequestAdditionalModelResponseFieldPathsList
    ]
    requestMetadata: Optional[RequestMetadata]
    performanceConfig: Optional[PerformanceConfiguration]


class ConverseStreamResponse(TypedDict, total=False):
    stream: Iterator[ConverseStreamOutput]


class GetAsyncInvokeRequest(ServiceRequest):
    invocationArn: InvocationArn


class GetAsyncInvokeResponse(TypedDict, total=False):
    invocationArn: InvocationArn
    modelArn: AsyncInvokeArn
    clientRequestToken: Optional[AsyncInvokeIdempotencyToken]
    status: AsyncInvokeStatus
    failureMessage: Optional[AsyncInvokeMessage]
    submitTime: Timestamp
    lastModifiedTime: Optional[Timestamp]
    endTime: Optional[Timestamp]
    outputDataConfig: AsyncInvokeOutputDataConfig


class InvokeModelRequest(ServiceRequest):
    body: Optional[IO[Body]]
    contentType: Optional[MimeType]
    accept: Optional[MimeType]
    modelId: InvokeModelIdentifier
    trace: Optional[Trace]
    guardrailIdentifier: Optional[GuardrailIdentifier]
    guardrailVersion: Optional[GuardrailVersion]
    performanceConfigLatency: Optional[PerformanceConfigLatency]


class InvokeModelResponse(TypedDict, total=False):
    body: Union[Body, IO[Body], Iterable[Body]]
    contentType: MimeType
    performanceConfigLatency: Optional[PerformanceConfigLatency]


class InvokeModelWithBidirectionalStreamInput(TypedDict, total=False):
    """Payload content, the speech chunk, for the bidirectional input of the
    invocation step.
    """

    chunk: Optional[BidirectionalInputPayloadPart]


class InvokeModelWithBidirectionalStreamOutput(TypedDict, total=False):
    """Output from the bidirectional stream that was used for model invocation."""

    chunk: Optional[BidirectionalOutputPayloadPart]
    internalServerException: Optional[InternalServerException]
    modelStreamErrorException: Optional[ModelStreamErrorException]
    validationException: Optional[ValidationException]
    throttlingException: Optional[ThrottlingException]
    modelTimeoutException: Optional[ModelTimeoutException]
    serviceUnavailableException: Optional[ServiceUnavailableException]


class InvokeModelWithBidirectionalStreamRequest(ServiceRequest):
    modelId: InvokeModelIdentifier
    body: Iterator[InvokeModelWithBidirectionalStreamInput]


class InvokeModelWithBidirectionalStreamResponse(TypedDict, total=False):
    body: Iterator[InvokeModelWithBidirectionalStreamOutput]


class InvokeModelWithResponseStreamRequest(ServiceRequest):
    body: Optional[IO[Body]]
    contentType: Optional[MimeType]
    accept: Optional[MimeType]
    modelId: InvokeModelIdentifier
    trace: Optional[Trace]
    guardrailIdentifier: Optional[GuardrailIdentifier]
    guardrailVersion: Optional[GuardrailVersion]
    performanceConfigLatency: Optional[PerformanceConfigLatency]


class PayloadPart(TypedDict, total=False):
    """Payload content included in the response."""

    bytes: Optional[PartBody]


class ResponseStream(TypedDict, total=False):
    """Definition of content in the response stream."""

    chunk: Optional[PayloadPart]
    internalServerException: Optional[InternalServerException]
    modelStreamErrorException: Optional[ModelStreamErrorException]
    validationException: Optional[ValidationException]
    throttlingException: Optional[ThrottlingException]
    modelTimeoutException: Optional[ModelTimeoutException]
    serviceUnavailableException: Optional[ServiceUnavailableException]


class InvokeModelWithResponseStreamResponse(TypedDict, total=False):
    body: Iterator[ResponseStream]
    contentType: MimeType
    performanceConfigLatency: Optional[PerformanceConfigLatency]


class ListAsyncInvokesRequest(ServiceRequest):
    submitTimeAfter: Optional[Timestamp]
    submitTimeBefore: Optional[Timestamp]
    statusEquals: Optional[AsyncInvokeStatus]
    maxResults: Optional[MaxResults]
    nextToken: Optional[PaginationToken]
    sortBy: Optional[SortAsyncInvocationBy]
    sortOrder: Optional[SortOrder]


class ListAsyncInvokesResponse(TypedDict, total=False):
    nextToken: Optional[PaginationToken]
    asyncInvokeSummaries: Optional[AsyncInvokeSummaries]


class ModelInputPayload(TypedDict, total=False):
    pass


class Tag(TypedDict, total=False):
    """A tag."""

    key: TagKey
    value: TagValue


TagList = List[Tag]


class StartAsyncInvokeRequest(ServiceRequest):
    clientRequestToken: Optional[AsyncInvokeIdempotencyToken]
    modelId: AsyncInvokeIdentifier
    modelInput: ModelInputPayload
    outputDataConfig: AsyncInvokeOutputDataConfig
    tags: Optional[TagList]


class StartAsyncInvokeResponse(TypedDict, total=False):
    invocationArn: InvocationArn


class BedrockRuntimeApi:
    service = "bedrock-runtime"
    version = "2023-09-30"

    @handler("ApplyGuardrail")
    def apply_guardrail(
        self,
        context: RequestContext,
        guardrail_identifier: GuardrailIdentifier,
        guardrail_version: GuardrailVersion,
        source: GuardrailContentSource,
        content: GuardrailContentBlockList,
        output_scope: GuardrailOutputScope | None = None,
        **kwargs,
    ) -> ApplyGuardrailResponse:
        """The action to apply a guardrail.

        For troubleshooting some of the common errors you might encounter when
        using the ``ApplyGuardrail`` API, see `Troubleshooting Amazon Bedrock
        API Error
        Codes <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html>`__
        in the Amazon Bedrock User Guide

        :param guardrail_identifier: The guardrail identifier used in the request to apply the guardrail.
        :param guardrail_version: The guardrail version used in the request to apply the guardrail.
        :param source: The source of data used in the request to apply the guardrail.
        :param content: The content details used in the request to apply the guardrail.
        :param output_scope: Specifies the scope of the output that you get in the response.
        :returns: ApplyGuardrailResponse
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        """
        raise NotImplementedError

    @handler("Converse")
    def converse(
        self,
        context: RequestContext,
        model_id: ConversationalModelId,
        messages: Messages | None = None,
        system: SystemContentBlocks | None = None,
        inference_config: InferenceConfiguration | None = None,
        tool_config: ToolConfiguration | None = None,
        guardrail_config: GuardrailConfiguration | None = None,
        additional_model_request_fields: Document | None = None,
        prompt_variables: PromptVariableMap | None = None,
        additional_model_response_field_paths: ConverseRequestAdditionalModelResponseFieldPathsList
        | None = None,
        request_metadata: RequestMetadata | None = None,
        performance_config: PerformanceConfiguration | None = None,
        **kwargs,
    ) -> ConverseResponse:
        """Sends messages to the specified Amazon Bedrock model. ``Converse``
        provides a consistent interface that works with all models that support
        messages. This allows you to write code once and use it with different
        models. If a model has unique inference parameters, you can also pass
        those unique parameters to the model.

        Amazon Bedrock doesn't store any text, images, or documents that you
        provide as content. The data is only used to generate the response.

        You can submit a prompt by including it in the ``messages`` field,
        specifying the ``modelId`` of a foundation model or inference profile to
        run inference on it, and including any other fields that are relevant to
        your use case.

        You can also submit a prompt from Prompt management by specifying the
        ARN of the prompt version and including a map of variables to values in
        the ``promptVariables`` field. You can append more messages to the
        prompt by using the ``messages`` field. If you use a prompt from Prompt
        management, you can't include the following fields in the request:
        ``additionalModelRequestFields``, ``inferenceConfig``, ``system``, or
        ``toolConfig``. Instead, these fields must be defined through Prompt
        management. For more information, see `Use a prompt from Prompt
        management <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html>`__.

        For information about the Converse API, see *Use the Converse API* in
        the *Amazon Bedrock User Guide*. To use a guardrail, see *Use a
        guardrail with the Converse API* in the *Amazon Bedrock User Guide*. To
        use a tool with a model, see *Tool use (Function calling)* in the
        *Amazon Bedrock User Guide*

        For example code, see *Converse API examples* in the *Amazon Bedrock
        User Guide*.

        This operation requires permission for the ``bedrock:InvokeModel``
        action.

        To deny all inference access to resources that you specify in the
        modelId field, you need to deny access to the ``bedrock:InvokeModel``
        and ``bedrock:InvokeModelWithResponseStream`` actions. Doing this also
        denies access to the resource through the base inference actions
        (`InvokeModel <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>`__
        and
        `InvokeModelWithResponseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html>`__).
        For more information see `Deny access for inference on specific
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference>`__.

        For troubleshooting some of the common errors you might encounter when
        using the ``Converse`` API, see `Troubleshooting Amazon Bedrock API
        Error
        Codes <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html>`__
        in the Amazon Bedrock User Guide

        :param model_id: Specifies the model or throughput with which to run inference, or the
        prompt resource to use in inference.
        :param messages: The messages that you want to send to the model.
        :param system: A prompt that provides instructions or context to the model about the
        task it should perform, or the persona it should adopt during the
        conversation.
        :param inference_config: Inference parameters to pass to the model.
        :param tool_config: Configuration information for the tools that the model can use when
        generating a response.
        :param guardrail_config: Configuration information for a guardrail that you want to use in the
        request.
        :param additional_model_request_fields: Additional inference parameters that the model supports, beyond the base
        set of inference parameters that ``Converse`` and ``ConverseStream``
        support in the ``inferenceConfig`` field.
        :param prompt_variables: Contains a map of variables in a prompt from Prompt management to
        objects containing the values to fill in for them when running model
        invocation.
        :param additional_model_response_field_paths: Additional model parameters field paths to return in the response.
        :param request_metadata: Key-value pairs that you can use to filter invocation logs.
        :param performance_config: Model performance settings for the request.
        :returns: ConverseResponse
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises ResourceNotFoundException:
        :raises ModelTimeoutException:
        :raises InternalServerException:
        :raises ServiceUnavailableException:
        :raises ValidationException:
        :raises ModelNotReadyException:
        :raises ModelErrorException:
        """
        raise NotImplementedError

    @handler("ConverseStream")
    def converse_stream(
        self,
        context: RequestContext,
        model_id: ConversationalModelId,
        messages: Messages | None = None,
        system: SystemContentBlocks | None = None,
        inference_config: InferenceConfiguration | None = None,
        tool_config: ToolConfiguration | None = None,
        guardrail_config: GuardrailStreamConfiguration | None = None,
        additional_model_request_fields: Document | None = None,
        prompt_variables: PromptVariableMap | None = None,
        additional_model_response_field_paths: ConverseStreamRequestAdditionalModelResponseFieldPathsList
        | None = None,
        request_metadata: RequestMetadata | None = None,
        performance_config: PerformanceConfiguration | None = None,
        **kwargs,
    ) -> ConverseStreamResponse:
        """Sends messages to the specified Amazon Bedrock model and returns the
        response in a stream. ``ConverseStream`` provides a consistent API that
        works with all Amazon Bedrock models that support messages. This allows
        you to write code once and use it with different models. Should a model
        have unique inference parameters, you can also pass those unique
        parameters to the model.

        To find out if a model supports streaming, call
        `GetFoundationModel <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html>`__
        and check the ``responseStreamingSupported`` field in the response.

        The CLI doesn't support streaming operations in Amazon Bedrock,
        including ``ConverseStream``.

        Amazon Bedrock doesn't store any text, images, or documents that you
        provide as content. The data is only used to generate the response.

        You can submit a prompt by including it in the ``messages`` field,
        specifying the ``modelId`` of a foundation model or inference profile to
        run inference on it, and including any other fields that are relevant to
        your use case.

        You can also submit a prompt from Prompt management by specifying the
        ARN of the prompt version and including a map of variables to values in
        the ``promptVariables`` field. You can append more messages to the
        prompt by using the ``messages`` field. If you use a prompt from Prompt
        management, you can't include the following fields in the request:
        ``additionalModelRequestFields``, ``inferenceConfig``, ``system``, or
        ``toolConfig``. Instead, these fields must be defined through Prompt
        management. For more information, see `Use a prompt from Prompt
        management <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html>`__.

        For information about the Converse API, see *Use the Converse API* in
        the *Amazon Bedrock User Guide*. To use a guardrail, see *Use a
        guardrail with the Converse API* in the *Amazon Bedrock User Guide*. To
        use a tool with a model, see *Tool use (Function calling)* in the
        *Amazon Bedrock User Guide*

        For example code, see *Conversation streaming example* in the *Amazon
        Bedrock User Guide*.

        This operation requires permission for the
        ``bedrock:InvokeModelWithResponseStream`` action.

        To deny all inference access to resources that you specify in the
        modelId field, you need to deny access to the ``bedrock:InvokeModel``
        and ``bedrock:InvokeModelWithResponseStream`` actions. Doing this also
        denies access to the resource through the base inference actions
        (`InvokeModel <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>`__
        and
        `InvokeModelWithResponseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html>`__).
        For more information see `Deny access for inference on specific
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference>`__.

        For troubleshooting some of the common errors you might encounter when
        using the ``ConverseStream`` API, see `Troubleshooting Amazon Bedrock
        API Error
        Codes <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html>`__
        in the Amazon Bedrock User Guide

        :param model_id: Specifies the model or throughput with which to run inference, or the
        prompt resource to use in inference.
        :param messages: The messages that you want to send to the model.
        :param system: A prompt that provides instructions or context to the model about the
        task it should perform, or the persona it should adopt during the
        conversation.
        :param inference_config: Inference parameters to pass to the model.
        :param tool_config: Configuration information for the tools that the model can use when
        generating a response.
        :param guardrail_config: Configuration information for a guardrail that you want to use in the
        request.
        :param additional_model_request_fields: Additional inference parameters that the model supports, beyond the base
        set of inference parameters that ``Converse`` and ``ConverseStream``
        support in the ``inferenceConfig`` field.
        :param prompt_variables: Contains a map of variables in a prompt from Prompt management to
        objects containing the values to fill in for them when running model
        invocation.
        :param additional_model_response_field_paths: Additional model parameters field paths to return in the response.
        :param request_metadata: Key-value pairs that you can use to filter invocation logs.
        :param performance_config: Model performance settings for the request.
        :returns: ConverseStreamResponse
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises ResourceNotFoundException:
        :raises ModelTimeoutException:
        :raises InternalServerException:
        :raises ServiceUnavailableException:
        :raises ValidationException:
        :raises ModelNotReadyException:
        :raises ModelErrorException:
        """
        raise NotImplementedError

    @handler("GetAsyncInvoke")
    def get_async_invoke(
        self, context: RequestContext, invocation_arn: InvocationArn, **kwargs
    ) -> GetAsyncInvokeResponse:
        """Retrieve information about an asynchronous invocation.

        :param invocation_arn: The invocation's ARN.
        :returns: GetAsyncInvokeResponse
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("InvokeModel")
    def invoke_model(
        self,
        context: RequestContext,
        model_id: InvokeModelIdentifier,
        body: IO[Body] | None = None,
        content_type: MimeType | None = None,
        accept: MimeType | None = None,
        trace: Trace | None = None,
        guardrail_identifier: GuardrailIdentifier | None = None,
        guardrail_version: GuardrailVersion | None = None,
        performance_config_latency: PerformanceConfigLatency | None = None,
        **kwargs,
    ) -> InvokeModelResponse:
        """Invokes the specified Amazon Bedrock model to run inference using the
        prompt and inference parameters provided in the request body. You use
        model inference to generate text, images, and embeddings.

        For example code, see *Invoke model code examples* in the *Amazon
        Bedrock User Guide*.

        This operation requires permission for the ``bedrock:InvokeModel``
        action.

        To deny all inference access to resources that you specify in the
        modelId field, you need to deny access to the ``bedrock:InvokeModel``
        and ``bedrock:InvokeModelWithResponseStream`` actions. Doing this also
        denies access to the resource through the Converse API actions
        (`Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
        and
        `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__).
        For more information see `Deny access for inference on specific
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference>`__.

        For troubleshooting some of the common errors you might encounter when
        using the ``InvokeModel`` API, see `Troubleshooting Amazon Bedrock API
        Error
        Codes <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html>`__
        in the Amazon Bedrock User Guide

        :param model_id: The unique identifier of the model to invoke to run inference.
        :param body: The prompt and inference parameters in the format specified in the
        ``contentType`` in the header.
        :param content_type: The MIME type of the input data in the request.
        :param accept: The desired MIME type of the inference body in the response.
        :param trace: Specifies whether to enable or disable the Bedrock trace.
        :param guardrail_identifier: The unique identifier of the guardrail that you want to use.
        :param guardrail_version: The version number for the guardrail.
        :param performance_config_latency: Model performance settings for the request.
        :returns: InvokeModelResponse
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ModelTimeoutException:
        :raises InternalServerException:
        :raises ServiceUnavailableException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ModelNotReadyException:
        :raises ModelErrorException:
        """
        raise NotImplementedError

    @handler("InvokeModelWithBidirectionalStream")
    def invoke_model_with_bidirectional_stream(
        self,
        context: RequestContext,
        model_id: InvokeModelIdentifier,
        body: InvokeModelWithBidirectionalStreamInput,
        **kwargs,
    ) -> InvokeModelWithBidirectionalStreamResponse:
        """Invoke the specified Amazon Bedrock model to run inference using the
        bidirectional stream. The response is returned in a stream that remains
        open for 8 minutes. A single session can contain multiple prompts and
        responses from the model. The prompts to the model are provided as audio
        files and the model's responses are spoken back to the user and
        transcribed.

        It is possible for users to interrupt the model's response with a new
        prompt, which will halt the response speech. The model will retain
        contextual awareness of the conversation while pivoting to respond to
        the new prompt.

        :param model_id: The model ID or ARN of the model ID to use.
        :param body: The prompt and inference parameters in the format specified in the
        ``BidirectionalInputPayloadPart`` in the header.
        :returns: InvokeModelWithBidirectionalStreamResponse
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ModelTimeoutException:
        :raises InternalServerException:
        :raises ServiceUnavailableException:
        :raises ModelStreamErrorException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ModelNotReadyException:
        :raises ModelErrorException:
        """
        raise NotImplementedError

    @handler("InvokeModelWithResponseStream")
    def invoke_model_with_response_stream(
        self,
        context: RequestContext,
        model_id: InvokeModelIdentifier,
        body: IO[Body] | None = None,
        content_type: MimeType | None = None,
        accept: MimeType | None = None,
        trace: Trace | None = None,
        guardrail_identifier: GuardrailIdentifier | None = None,
        guardrail_version: GuardrailVersion | None = None,
        performance_config_latency: PerformanceConfigLatency | None = None,
        **kwargs,
    ) -> InvokeModelWithResponseStreamResponse:
        """Invoke the specified Amazon Bedrock model to run inference using the
        prompt and inference parameters provided in the request body. The
        response is returned in a stream.

        To see if a model supports streaming, call
        `GetFoundationModel <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html>`__
        and check the ``responseStreamingSupported`` field in the response.

        The CLI doesn't support streaming operations in Amazon Bedrock,
        including ``InvokeModelWithResponseStream``.

        For example code, see *Invoke model with streaming code example* in the
        *Amazon Bedrock User Guide*.

        This operation requires permissions to perform the
        ``bedrock:InvokeModelWithResponseStream`` action.

        To deny all inference access to resources that you specify in the
        modelId field, you need to deny access to the ``bedrock:InvokeModel``
        and ``bedrock:InvokeModelWithResponseStream`` actions. Doing this also
        denies access to the resource through the Converse API actions
        (`Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
        and
        `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__).
        For more information see `Deny access for inference on specific
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference>`__.

        For troubleshooting some of the common errors you might encounter when
        using the ``InvokeModelWithResponseStream`` API, see `Troubleshooting
        Amazon Bedrock API Error
        Codes <https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html>`__
        in the Amazon Bedrock User Guide

        :param model_id: The unique identifier of the model to invoke to run inference.
        :param body: The prompt and inference parameters in the format specified in the
        ``contentType`` in the header.
        :param content_type: The MIME type of the input data in the request.
        :param accept: The desired MIME type of the inference body in the response.
        :param trace: Specifies whether to enable or disable the Bedrock trace.
        :param guardrail_identifier: The unique identifier of the guardrail that you want to use.
        :param guardrail_version: The version number for the guardrail.
        :param performance_config_latency: Model performance settings for the request.
        :returns: InvokeModelWithResponseStreamResponse
        :raises AccessDeniedException:
        :raises ResourceNotFoundException:
        :raises ThrottlingException:
        :raises ModelTimeoutException:
        :raises InternalServerException:
        :raises ServiceUnavailableException:
        :raises ModelStreamErrorException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ModelNotReadyException:
        :raises ModelErrorException:
        """
        raise NotImplementedError

    @handler("ListAsyncInvokes")
    def list_async_invokes(
        self,
        context: RequestContext,
        submit_time_after: Timestamp | None = None,
        submit_time_before: Timestamp | None = None,
        status_equals: AsyncInvokeStatus | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        sort_by: SortAsyncInvocationBy | None = None,
        sort_order: SortOrder | None = None,
        **kwargs,
    ) -> ListAsyncInvokesResponse:
        """Lists asynchronous invocations.

        :param submit_time_after: Include invocations submitted after this time.
        :param submit_time_before: Include invocations submitted before this time.
        :param status_equals: Filter invocations by status.
        :param max_results: The maximum number of invocations to return in one page of results.
        :param next_token: Specify the pagination token from a previous request to retrieve the
        next page of results.
        :param sort_by: How to sort the response.
        :param sort_order: The sorting order for the response.
        :returns: ListAsyncInvokesResponse
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises InternalServerException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("StartAsyncInvoke")
    def start_async_invoke(
        self,
        context: RequestContext,
        model_id: AsyncInvokeIdentifier,
        model_input: ModelInputPayload,
        output_data_config: AsyncInvokeOutputDataConfig,
        client_request_token: AsyncInvokeIdempotencyToken | None = None,
        tags: TagList | None = None,
        **kwargs,
    ) -> StartAsyncInvokeResponse:
        """Starts an asynchronous invocation.

        This operation requires permission for the ``bedrock:InvokeModel``
        action.

        To deny all inference access to resources that you specify in the
        modelId field, you need to deny access to the ``bedrock:InvokeModel``
        and ``bedrock:InvokeModelWithResponseStream`` actions. Doing this also
        denies access to the resource through the Converse API actions
        (`Converse <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>`__
        and
        `ConverseStream <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html>`__).
        For more information see `Deny access for inference on specific
        models <https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference>`__.

        :param model_id: The model to invoke.
        :param model_input: Input to send to the model.
        :param output_data_config: Where to store the output.
        :param client_request_token: Specify idempotency token to ensure that requests are not duplicated.
        :param tags: Tags to apply to the invocation.
        :returns: StartAsyncInvokeResponse
        :raises AccessDeniedException:
        :raises ThrottlingException:
        :raises ResourceNotFoundException:
        :raises InternalServerException:
        :raises ServiceUnavailableException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ConflictException:
        """
        raise NotImplementedError
