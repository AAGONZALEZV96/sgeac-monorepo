from datetime import datetime
from enum import StrEnum
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AdapterDescription = str
AdapterId = str
AdapterName = str
AdapterPage = str
AdapterVersion = str
AdapterVersionStatusMessage = str
AmazonResourceName = str
ClientRequestToken = str
ErrorCode = str
Float = float
FlowDefinitionArn = str
HumanLoopActivationConditionsEvaluationResults = str
HumanLoopActivationReason = str
HumanLoopArn = str
HumanLoopName = str
JobId = str
JobTag = str
KMSKeyId = str
MaxResults = int
NonEmptyString = str
PaginationToken = str
Percent = float
QueryInput = str
QueryPage = str
RoleArn = str
S3Bucket = str
S3ObjectName = str
S3ObjectVersion = str
SNSTopicArn = str
StatusMessage = str
String = str
TagKey = str
TagValue = str
UInteger = int


class AdapterVersionStatus(StrEnum):
    ACTIVE = "ACTIVE"
    AT_RISK = "AT_RISK"
    DEPRECATED = "DEPRECATED"
    CREATION_ERROR = "CREATION_ERROR"
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"


class AutoUpdate(StrEnum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BlockType(StrEnum):
    KEY_VALUE_SET = "KEY_VALUE_SET"
    PAGE = "PAGE"
    LINE = "LINE"
    WORD = "WORD"
    TABLE = "TABLE"
    CELL = "CELL"
    SELECTION_ELEMENT = "SELECTION_ELEMENT"
    MERGED_CELL = "MERGED_CELL"
    TITLE = "TITLE"
    QUERY = "QUERY"
    QUERY_RESULT = "QUERY_RESULT"
    SIGNATURE = "SIGNATURE"
    TABLE_TITLE = "TABLE_TITLE"
    TABLE_FOOTER = "TABLE_FOOTER"
    LAYOUT_TEXT = "LAYOUT_TEXT"
    LAYOUT_TITLE = "LAYOUT_TITLE"
    LAYOUT_HEADER = "LAYOUT_HEADER"
    LAYOUT_FOOTER = "LAYOUT_FOOTER"
    LAYOUT_SECTION_HEADER = "LAYOUT_SECTION_HEADER"
    LAYOUT_PAGE_NUMBER = "LAYOUT_PAGE_NUMBER"
    LAYOUT_LIST = "LAYOUT_LIST"
    LAYOUT_FIGURE = "LAYOUT_FIGURE"
    LAYOUT_TABLE = "LAYOUT_TABLE"
    LAYOUT_KEY_VALUE = "LAYOUT_KEY_VALUE"


class ContentClassifier(StrEnum):
    FreeOfPersonallyIdentifiableInformation = "FreeOfPersonallyIdentifiableInformation"
    FreeOfAdultContent = "FreeOfAdultContent"


class EntityType(StrEnum):
    KEY = "KEY"
    VALUE = "VALUE"
    COLUMN_HEADER = "COLUMN_HEADER"
    TABLE_TITLE = "TABLE_TITLE"
    TABLE_FOOTER = "TABLE_FOOTER"
    TABLE_SECTION_TITLE = "TABLE_SECTION_TITLE"
    TABLE_SUMMARY = "TABLE_SUMMARY"
    STRUCTURED_TABLE = "STRUCTURED_TABLE"
    SEMI_STRUCTURED_TABLE = "SEMI_STRUCTURED_TABLE"


class FeatureType(StrEnum):
    TABLES = "TABLES"
    FORMS = "FORMS"
    QUERIES = "QUERIES"
    SIGNATURES = "SIGNATURES"
    LAYOUT = "LAYOUT"


class JobStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"


class RelationshipType(StrEnum):
    VALUE = "VALUE"
    CHILD = "CHILD"
    COMPLEX_FEATURES = "COMPLEX_FEATURES"
    MERGED_CELL = "MERGED_CELL"
    TITLE = "TITLE"
    ANSWER = "ANSWER"
    TABLE = "TABLE"
    TABLE_TITLE = "TABLE_TITLE"
    TABLE_FOOTER = "TABLE_FOOTER"


class SelectionStatus(StrEnum):
    SELECTED = "SELECTED"
    NOT_SELECTED = "NOT_SELECTED"


class TextType(StrEnum):
    HANDWRITING = "HANDWRITING"
    PRINTED = "PRINTED"


class ValueType(StrEnum):
    DATE = "DATE"


class AccessDeniedException(ServiceException):
    """You aren't authorized to perform the action. Use the Amazon Resource
    Name (ARN) of an authorized user or IAM role to perform the operation.
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = False
    status_code: int = 400


class BadDocumentException(ServiceException):
    """Amazon Textract isn't able to read the document. For more information on
    the document limits in Amazon Textract, see limits.
    """

    code: str = "BadDocumentException"
    sender_fault: bool = False
    status_code: int = 400


class ConflictException(ServiceException):
    """Updating or deleting a resource can cause an inconsistent state."""

    code: str = "ConflictException"
    sender_fault: bool = False
    status_code: int = 400


class DocumentTooLargeException(ServiceException):
    """The document can't be processed because it's too large. The maximum
    document size for synchronous operations 10 MB. The maximum document
    size for asynchronous operations is 500 MB for PDF files.
    """

    code: str = "DocumentTooLargeException"
    sender_fault: bool = False
    status_code: int = 400


class HumanLoopQuotaExceededException(ServiceException):
    """Indicates you have exceeded the maximum number of active human in the
    loop workflows available
    """

    code: str = "HumanLoopQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 400
    ResourceType: Optional[String]
    QuotaCode: Optional[String]
    ServiceCode: Optional[String]


class IdempotentParameterMismatchException(ServiceException):
    """A ``ClientRequestToken`` input parameter was reused with an operation,
    but at least one of the other input parameters is different from the
    previous call to the operation.
    """

    code: str = "IdempotentParameterMismatchException"
    sender_fault: bool = False
    status_code: int = 400


class InternalServerError(ServiceException):
    """Amazon Textract experienced a service issue. Try your call again."""

    code: str = "InternalServerError"
    sender_fault: bool = False
    status_code: int = 400


class InvalidJobIdException(ServiceException):
    """An invalid job identifier was passed to an asynchronous analysis
    operation.
    """

    code: str = "InvalidJobIdException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidKMSKeyException(ServiceException):
    """Indicates you do not have decrypt permissions with the KMS key entered,
    or the KMS key was entered incorrectly.
    """

    code: str = "InvalidKMSKeyException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidParameterException(ServiceException):
    """An input parameter violated a constraint. For example, in synchronous
    operations, an ``InvalidParameterException`` exception occurs when
    neither of the ``S3Object`` or ``Bytes`` values are supplied in the
    ``Document`` request parameter. Validate your parameter before calling
    the API operation again.
    """

    code: str = "InvalidParameterException"
    sender_fault: bool = False
    status_code: int = 400


class InvalidS3ObjectException(ServiceException):
    """Amazon Textract is unable to access the S3 object that's specified in
    the request. for more information, `Configure Access to Amazon
    S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__
    For troubleshooting information, see `Troubleshooting Amazon
    S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html>`__
    """

    code: str = "InvalidS3ObjectException"
    sender_fault: bool = False
    status_code: int = 400


class LimitExceededException(ServiceException):
    """An Amazon Textract service limit was exceeded. For example, if you start
    too many asynchronous jobs concurrently, calls to start operations
    (``StartDocumentTextDetection``, for example) raise a
    LimitExceededException exception (HTTP status code: 400) until the
    number of concurrently running jobs is below the Amazon Textract service
    limit.
    """

    code: str = "LimitExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ProvisionedThroughputExceededException(ServiceException):
    """The number of requests exceeded your throughput limit. If you want to
    increase this limit, contact Amazon Textract.
    """

    code: str = "ProvisionedThroughputExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ResourceNotFoundException(ServiceException):
    """Returned when an operation tried to access a nonexistent resource."""

    code: str = "ResourceNotFoundException"
    sender_fault: bool = False
    status_code: int = 400


class ServiceQuotaExceededException(ServiceException):
    """Returned when a request cannot be completed as it would exceed a maximum
    service quota.
    """

    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = False
    status_code: int = 400


class ThrottlingException(ServiceException):
    """Amazon Textract is temporarily unable to process the request. Try your
    call again.
    """

    code: str = "ThrottlingException"
    sender_fault: bool = False
    status_code: int = 400


class UnsupportedDocumentException(ServiceException):
    """The format of the input document isn't supported. Documents for
    operations can be in PNG, JPEG, PDF, or TIFF format.
    """

    code: str = "UnsupportedDocumentException"
    sender_fault: bool = False
    status_code: int = 400


class ValidationException(ServiceException):
    """Indicates that a request was not valid. Check request for proper
    formatting.
    """

    code: str = "ValidationException"
    sender_fault: bool = False
    status_code: int = 400


AdapterPages = List[AdapterPage]


class Adapter(TypedDict, total=False):
    """An adapter selected for use when analyzing documents. Contains an
    adapter ID and a version number. Contains information on pages selected
    for analysis when analyzing documents asychronously.
    """

    AdapterId: AdapterId
    Pages: Optional[AdapterPages]
    Version: AdapterVersion


FeatureTypes = List[FeatureType]
DateTime = datetime


class AdapterOverview(TypedDict, total=False):
    """Contains information on the adapter, including the adapter ID, Name,
    Creation time, and feature types.
    """

    AdapterId: Optional[AdapterId]
    AdapterName: Optional[AdapterName]
    CreationTime: Optional[DateTime]
    FeatureTypes: Optional[FeatureTypes]


AdapterList = List[AdapterOverview]


class S3Object(TypedDict, total=False):
    """The S3 bucket name and file name that identifies the document.

    The AWS Region for the S3 bucket that contains the document must match
    the Region that you use for Amazon Textract operations.

    For Amazon Textract to process a file in an S3 bucket, the user must
    have permission to access the S3 bucket and file.
    """

    Bucket: Optional[S3Bucket]
    Name: Optional[S3ObjectName]
    Version: Optional[S3ObjectVersion]


class AdapterVersionDatasetConfig(TypedDict, total=False):
    """The dataset configuration options for a given version of an adapter. Can
    include an Amazon S3 bucket if specified.
    """

    ManifestS3Object: Optional[S3Object]


class EvaluationMetric(TypedDict, total=False):
    """The evaluation metrics (F1 score, Precision, and Recall) for an adapter
    version.
    """

    F1Score: Optional[Float]
    Precision: Optional[Float]
    Recall: Optional[Float]


class AdapterVersionEvaluationMetric(TypedDict, total=False):
    """Contains information on the metrics used to evalute the peformance of a
    given adapter version. Includes data for baseline model performance and
    individual adapter version perfromance.
    """

    Baseline: Optional[EvaluationMetric]
    AdapterVersion: Optional[EvaluationMetric]
    FeatureType: Optional[FeatureType]


AdapterVersionEvaluationMetrics = List[AdapterVersionEvaluationMetric]


class AdapterVersionOverview(TypedDict, total=False):
    """Summary info for an adapter version. Contains information on the
    AdapterId, AdapterVersion, CreationTime, FeatureTypes, and Status.
    """

    AdapterId: Optional[AdapterId]
    AdapterVersion: Optional[AdapterVersion]
    CreationTime: Optional[DateTime]
    FeatureTypes: Optional[FeatureTypes]
    Status: Optional[AdapterVersionStatus]
    StatusMessage: Optional[AdapterVersionStatusMessage]


AdapterVersionList = List[AdapterVersionOverview]
Adapters = List[Adapter]


class AdaptersConfig(TypedDict, total=False):
    """Contains information about adapters used when analyzing a document, with
    each adapter specified using an AdapterId and version
    """

    Adapters: Adapters


QueryPages = List[QueryPage]


class Query(TypedDict, total=False):
    """Each query contains the question you want to ask in the Text and the
    alias you want to associate.
    """

    Text: QueryInput
    Alias: Optional[QueryInput]
    Pages: Optional[QueryPages]


Queries = List[Query]


class QueriesConfig(TypedDict, total=False):
    Queries: Queries


ContentClassifiers = List[ContentClassifier]


class HumanLoopDataAttributes(TypedDict, total=False):
    """Allows you to set attributes of the image. Currently, you can declare an
    image as free of personally identifiable information and adult content.
    """

    ContentClassifiers: Optional[ContentClassifiers]


class HumanLoopConfig(TypedDict, total=False):
    """Sets up the human review workflow the document will be sent to if one of
    the conditions is met. You can also set certain attributes of the image
    before review.
    """

    HumanLoopName: HumanLoopName
    FlowDefinitionArn: FlowDefinitionArn
    DataAttributes: Optional[HumanLoopDataAttributes]


ImageBlob = bytes


class Document(TypedDict, total=False):
    """The input document, either as bytes or as an S3 object.

    You pass image bytes to an Amazon Textract API operation by using the
    ``Bytes`` property. For example, you would use the ``Bytes`` property to
    pass a document loaded from a local file system. Image bytes passed by
    using the ``Bytes`` property must be base64 encoded. Your code might not
    need to encode document file bytes if you're using an AWS SDK to call
    Amazon Textract API operations.

    You pass images stored in an S3 bucket to an Amazon Textract API
    operation by using the ``S3Object`` property. Documents stored in an S3
    bucket don't need to be base64 encoded.

    The AWS Region for the S3 bucket that contains the S3 object must match
    the AWS Region that you use for Amazon Textract operations.

    If you use the AWS CLI to call Amazon Textract operations, passing image
    bytes using the Bytes property isn't supported. You must first upload
    the document to an Amazon S3 bucket, and then call the operation using
    the S3Object property.

    For Amazon Textract to process an S3 object, the user must have
    permission to access the S3 object.
    """

    Bytes: Optional[ImageBlob]
    S3Object: Optional[S3Object]


class AnalyzeDocumentRequest(ServiceRequest):
    Document: Document
    FeatureTypes: FeatureTypes
    HumanLoopConfig: Optional[HumanLoopConfig]
    QueriesConfig: Optional[QueriesConfig]
    AdaptersConfig: Optional[AdaptersConfig]


HumanLoopActivationReasons = List[HumanLoopActivationReason]


class HumanLoopActivationOutput(TypedDict, total=False):
    """Shows the results of the human in the loop evaluation. If there is no
    HumanLoopArn, the input did not trigger human review.
    """

    HumanLoopArn: Optional[HumanLoopArn]
    HumanLoopActivationReasons: Optional[HumanLoopActivationReasons]
    HumanLoopActivationConditionsEvaluationResults: Optional[
        HumanLoopActivationConditionsEvaluationResults
    ]


EntityTypes = List[EntityType]
IdList = List[NonEmptyString]


class Relationship(TypedDict, total=False):
    """Information about how blocks are related to each other. A ``Block``
    object contains 0 or more ``Relation`` objects in a list,
    ``Relationships``. For more information, see Block.

    The ``Type`` element provides the type of the relationship for all
    blocks in the ``IDs`` array.
    """

    Type: Optional[RelationshipType]
    Ids: Optional[IdList]


RelationshipList = List[Relationship]


class Point(TypedDict, total=False):
    """The X and Y coordinates of a point on a document page. The X and Y
    values that are returned are ratios of the overall document page size.
    For example, if the input document is 700 x 200 and the operation
    returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel
    coordinate on the document page.

    An array of ``Point`` objects, ``Polygon``, is returned by
    DetectDocumentText. ``Polygon`` represents a fine-grained polygon around
    detected text. For more information, see Geometry in the Amazon Textract
    Developer Guide.
    """

    X: Optional[Float]
    Y: Optional[Float]


Polygon = List[Point]


class BoundingBox(TypedDict, total=False):
    """The bounding box around the detected page, text, key-value pair, table,
    table cell, or selection element on a document page. The ``left``
    (x-coordinate) and ``top`` (y-coordinate) are coordinates that represent
    the top and left sides of the bounding box. Note that the upper-left
    corner of the image is the origin (0,0).

    The ``top`` and ``left`` values returned are ratios of the overall
    document page size. For example, if the input image is 700 x 200 pixels,
    and the top-left coordinate of the bounding box is 350 x 50 pixels, the
    API returns a ``left`` value of 0.5 (350/700) and a ``top`` value of
    0.25 (50/200).

    The ``width`` and ``height`` values represent the dimensions of the
    bounding box as a ratio of the overall document page dimension. For
    example, if the document page size is 700 x 200 pixels, and the bounding
    box width is 70 pixels, the width returned is 0.1.
    """

    Width: Optional[Float]
    Height: Optional[Float]
    Left: Optional[Float]
    Top: Optional[Float]


class Geometry(TypedDict, total=False):
    """Information about where the following items are located on a document
    page: detected page, text, key-value pairs, tables, table cells, and
    selection elements.
    """

    BoundingBox: Optional[BoundingBox]
    Polygon: Optional[Polygon]


class Block(TypedDict, total=False):
    """A ``Block`` represents items that are recognized in a document within a
    group of pixels close to each other. The information returned in a
    ``Block`` object depends on the type of operation. In text detection for
    documents (for example DetectDocumentText), you get information about
    the detected words and lines of text. In text analysis (for example
    AnalyzeDocument), you can also get information about the fields, tables,
    and selection elements that are detected in the document.

    An array of ``Block`` objects is returned by both synchronous and
    asynchronous operations. In synchronous operations, such as
    DetectDocumentText, the array of ``Block`` objects is the entire set of
    results. In asynchronous operations, such as GetDocumentAnalysis, the
    array is returned over one or more responses.

    For more information, see `How Amazon Textract
    Works <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__.
    """

    BlockType: Optional[BlockType]
    Confidence: Optional[Percent]
    Text: Optional[String]
    TextType: Optional[TextType]
    RowIndex: Optional[UInteger]
    ColumnIndex: Optional[UInteger]
    RowSpan: Optional[UInteger]
    ColumnSpan: Optional[UInteger]
    Geometry: Optional[Geometry]
    Id: Optional[NonEmptyString]
    Relationships: Optional[RelationshipList]
    EntityTypes: Optional[EntityTypes]
    SelectionStatus: Optional[SelectionStatus]
    Page: Optional[UInteger]
    Query: Optional[Query]


BlockList = List[Block]


class DocumentMetadata(TypedDict, total=False):
    """Information about the input document."""

    Pages: Optional[UInteger]


class AnalyzeDocumentResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    Blocks: Optional[BlockList]
    HumanLoopActivationOutput: Optional[HumanLoopActivationOutput]
    AnalyzeDocumentModelVersion: Optional[String]


class AnalyzeExpenseRequest(ServiceRequest):
    Document: Document


StringList = List[String]


class ExpenseGroupProperty(TypedDict, total=False):
    """Shows the group that a certain key belongs to. This helps differentiate
    between names and addresses for different organizations, that can be
    hard to determine via JSON response.
    """

    Types: Optional[StringList]
    Id: Optional[String]


ExpenseGroupPropertyList = List[ExpenseGroupProperty]


class ExpenseCurrency(TypedDict, total=False):
    """Returns the kind of currency detected."""

    Code: Optional[String]
    Confidence: Optional[Percent]


class ExpenseDetection(TypedDict, total=False):
    """An object used to store information about the Value or Label detected by
    Amazon Textract.
    """

    Text: Optional[String]
    Geometry: Optional[Geometry]
    Confidence: Optional[Percent]


class ExpenseType(TypedDict, total=False):
    """An object used to store information about the Type detected by Amazon
    Textract.
    """

    Text: Optional[String]
    Confidence: Optional[Percent]


class ExpenseField(TypedDict, total=False):
    """Breakdown of detected information, seperated into the catagories Type,
    LabelDetection, and ValueDetection
    """

    Type: Optional[ExpenseType]
    LabelDetection: Optional[ExpenseDetection]
    ValueDetection: Optional[ExpenseDetection]
    PageNumber: Optional[UInteger]
    Currency: Optional[ExpenseCurrency]
    GroupProperties: Optional[ExpenseGroupPropertyList]


ExpenseFieldList = List[ExpenseField]


class LineItemFields(TypedDict, total=False):
    """A structure that holds information about the different lines found in a
    document's tables.
    """

    LineItemExpenseFields: Optional[ExpenseFieldList]


LineItemList = List[LineItemFields]


class LineItemGroup(TypedDict, total=False):
    """A grouping of tables which contain LineItems, with each table identified
    by the table's ``LineItemGroupIndex``.
    """

    LineItemGroupIndex: Optional[UInteger]
    LineItems: Optional[LineItemList]


LineItemGroupList = List[LineItemGroup]


class ExpenseDocument(TypedDict, total=False):
    """The structure holding all the information returned by AnalyzeExpense"""

    ExpenseIndex: Optional[UInteger]
    SummaryFields: Optional[ExpenseFieldList]
    LineItemGroups: Optional[LineItemGroupList]
    Blocks: Optional[BlockList]


ExpenseDocumentList = List[ExpenseDocument]


class AnalyzeExpenseResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    ExpenseDocuments: Optional[ExpenseDocumentList]


class NormalizedValue(TypedDict, total=False):
    """Contains information relating to dates in a document, including the type
    of value, and the value.
    """

    Value: Optional[String]
    ValueType: Optional[ValueType]


class AnalyzeIDDetections(TypedDict, total=False):
    """Used to contain the information detected by an AnalyzeID operation."""

    Text: String
    NormalizedValue: Optional[NormalizedValue]
    Confidence: Optional[Percent]


DocumentPages = List[Document]


class AnalyzeIDRequest(ServiceRequest):
    DocumentPages: DocumentPages


class IdentityDocumentField(TypedDict, total=False):
    """Structure containing both the normalized type of the extracted
    information and the text associated with it. These are extracted as Type
    and Value respectively.
    """

    Type: Optional[AnalyzeIDDetections]
    ValueDetection: Optional[AnalyzeIDDetections]


IdentityDocumentFieldList = List[IdentityDocumentField]


class IdentityDocument(TypedDict, total=False):
    """The structure that lists each document processed in an AnalyzeID
    operation.
    """

    DocumentIndex: Optional[UInteger]
    IdentityDocumentFields: Optional[IdentityDocumentFieldList]
    Blocks: Optional[BlockList]


IdentityDocumentList = List[IdentityDocument]


class AnalyzeIDResponse(TypedDict, total=False):
    IdentityDocuments: Optional[IdentityDocumentList]
    DocumentMetadata: Optional[DocumentMetadata]
    AnalyzeIDModelVersion: Optional[String]


TagMap = Dict[TagKey, TagValue]


class CreateAdapterRequest(ServiceRequest):
    AdapterName: AdapterName
    ClientRequestToken: Optional[ClientRequestToken]
    Description: Optional[AdapterDescription]
    FeatureTypes: FeatureTypes
    AutoUpdate: Optional[AutoUpdate]
    Tags: Optional[TagMap]


class CreateAdapterResponse(TypedDict, total=False):
    AdapterId: Optional[AdapterId]


class OutputConfig(TypedDict, total=False):
    """Sets whether or not your output will go to a user created bucket. Used
    to set the name of the bucket, and the prefix on the output file.

    ``OutputConfig`` is an optional parameter which lets you adjust where
    your output will be placed. By default, Amazon Textract will store the
    results internally and can only be accessed by the Get API operations.
    With ``OutputConfig`` enabled, you can set the name of the bucket the
    output will be sent to the file prefix of the results where you can
    download your results. Additionally, you can set the ``KMSKeyID``
    parameter to a customer master key (CMK) to encrypt your output. Without
    this parameter set Amazon Textract will encrypt server-side using the
    AWS managed CMK for Amazon S3.

    Decryption of Customer Content is necessary for processing of the
    documents by Amazon Textract. If your account is opted out under an AI
    services opt out policy then all unencrypted Customer Content is
    immediately and permanently deleted after the Customer Content has been
    processed by the service. No copy of of the output is retained by Amazon
    Textract. For information about how to opt out, see `Managing AI
    services opt-out
    policy. <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html>`__

    For more information on data privacy, see the `Data Privacy
    FAQ <https://aws.amazon.com/compliance/data-privacy-faq/>`__.
    """

    S3Bucket: S3Bucket
    S3Prefix: Optional[S3ObjectName]


class CreateAdapterVersionRequest(ServiceRequest):
    AdapterId: AdapterId
    ClientRequestToken: Optional[ClientRequestToken]
    DatasetConfig: AdapterVersionDatasetConfig
    KMSKeyId: Optional[KMSKeyId]
    OutputConfig: OutputConfig
    Tags: Optional[TagMap]


class CreateAdapterVersionResponse(TypedDict, total=False):
    AdapterId: Optional[AdapterId]
    AdapterVersion: Optional[AdapterVersion]


class DeleteAdapterRequest(ServiceRequest):
    AdapterId: AdapterId


class DeleteAdapterResponse(TypedDict, total=False):
    pass


class DeleteAdapterVersionRequest(ServiceRequest):
    AdapterId: AdapterId
    AdapterVersion: AdapterVersion


class DeleteAdapterVersionResponse(TypedDict, total=False):
    pass


class DetectDocumentTextRequest(ServiceRequest):
    Document: Document


class DetectDocumentTextResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    Blocks: Optional[BlockList]
    DetectDocumentTextModelVersion: Optional[String]


class DetectedSignature(TypedDict, total=False):
    """A structure that holds information regarding a detected signature on a
    page.
    """

    Page: Optional[UInteger]


DetectedSignatureList = List[DetectedSignature]


class UndetectedSignature(TypedDict, total=False):
    """A structure containing information about an undetected signature on a
    page where it was expected but not found.
    """

    Page: Optional[UInteger]


UndetectedSignatureList = List[UndetectedSignature]
PageList = List[UInteger]


class SplitDocument(TypedDict, total=False):
    """Contains information about the pages of a document, defined by logical
    boundary.
    """

    Index: Optional[UInteger]
    Pages: Optional[PageList]


SplitDocumentList = List[SplitDocument]


class DocumentGroup(TypedDict, total=False):
    """Summary information about documents grouped by the same document type."""

    Type: Optional[NonEmptyString]
    SplitDocuments: Optional[SplitDocumentList]
    DetectedSignatures: Optional[DetectedSignatureList]
    UndetectedSignatures: Optional[UndetectedSignatureList]


DocumentGroupList = List[DocumentGroup]


class DocumentLocation(TypedDict, total=False):
    """The Amazon S3 bucket that contains the document to be processed. It's
    used by asynchronous operations.

    The input document can be an image file in JPEG or PNG format. It can
    also be a file in PDF format.
    """

    S3Object: Optional[S3Object]


class SignatureDetection(TypedDict, total=False):
    """Information regarding a detected signature on a page."""

    Confidence: Optional[Percent]
    Geometry: Optional[Geometry]


SignatureDetectionList = List[SignatureDetection]


class LendingDetection(TypedDict, total=False):
    """The results extracted for a lending document."""

    Text: Optional[String]
    SelectionStatus: Optional[SelectionStatus]
    Geometry: Optional[Geometry]
    Confidence: Optional[Percent]


LendingDetectionList = List[LendingDetection]


class LendingField(TypedDict, total=False):
    """Holds the normalized key-value pairs returned by AnalyzeDocument,
    including the document type, detected text, and geometry.
    """

    Type: Optional[String]
    KeyDetection: Optional[LendingDetection]
    ValueDetections: Optional[LendingDetectionList]


LendingFieldList = List[LendingField]


class LendingDocument(TypedDict, total=False):
    """Holds the structured data returned by AnalyzeDocument for lending
    documents.
    """

    LendingFields: Optional[LendingFieldList]
    SignatureDetections: Optional[SignatureDetectionList]


class Extraction(TypedDict, total=False):
    """Contains information extracted by an analysis operation after using
    StartLendingAnalysis.
    """

    LendingDocument: Optional[LendingDocument]
    ExpenseDocument: Optional[ExpenseDocument]
    IdentityDocument: Optional[IdentityDocument]


ExtractionList = List[Extraction]


class GetAdapterRequest(ServiceRequest):
    AdapterId: AdapterId


class GetAdapterResponse(TypedDict, total=False):
    AdapterId: Optional[AdapterId]
    AdapterName: Optional[AdapterName]
    CreationTime: Optional[DateTime]
    Description: Optional[AdapterDescription]
    FeatureTypes: Optional[FeatureTypes]
    AutoUpdate: Optional[AutoUpdate]
    Tags: Optional[TagMap]


class GetAdapterVersionRequest(ServiceRequest):
    AdapterId: AdapterId
    AdapterVersion: AdapterVersion


class GetAdapterVersionResponse(TypedDict, total=False):
    AdapterId: Optional[AdapterId]
    AdapterVersion: Optional[AdapterVersion]
    CreationTime: Optional[DateTime]
    FeatureTypes: Optional[FeatureTypes]
    Status: Optional[AdapterVersionStatus]
    StatusMessage: Optional[AdapterVersionStatusMessage]
    DatasetConfig: Optional[AdapterVersionDatasetConfig]
    KMSKeyId: Optional[KMSKeyId]
    OutputConfig: Optional[OutputConfig]
    EvaluationMetrics: Optional[AdapterVersionEvaluationMetrics]
    Tags: Optional[TagMap]


class GetDocumentAnalysisRequest(ServiceRequest):
    JobId: JobId
    MaxResults: Optional[MaxResults]
    NextToken: Optional[PaginationToken]


Pages = List[UInteger]


class Warning(TypedDict, total=False):
    """A warning about an issue that occurred during asynchronous text analysis
    (StartDocumentAnalysis) or asynchronous document text detection
    (StartDocumentTextDetection).
    """

    ErrorCode: Optional[ErrorCode]
    Pages: Optional[Pages]


Warnings = List[Warning]


class GetDocumentAnalysisResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    JobStatus: Optional[JobStatus]
    NextToken: Optional[PaginationToken]
    Blocks: Optional[BlockList]
    Warnings: Optional[Warnings]
    StatusMessage: Optional[StatusMessage]
    AnalyzeDocumentModelVersion: Optional[String]


class GetDocumentTextDetectionRequest(ServiceRequest):
    JobId: JobId
    MaxResults: Optional[MaxResults]
    NextToken: Optional[PaginationToken]


class GetDocumentTextDetectionResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    JobStatus: Optional[JobStatus]
    NextToken: Optional[PaginationToken]
    Blocks: Optional[BlockList]
    Warnings: Optional[Warnings]
    StatusMessage: Optional[StatusMessage]
    DetectDocumentTextModelVersion: Optional[String]


class GetExpenseAnalysisRequest(ServiceRequest):
    JobId: JobId
    MaxResults: Optional[MaxResults]
    NextToken: Optional[PaginationToken]


class GetExpenseAnalysisResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    JobStatus: Optional[JobStatus]
    NextToken: Optional[PaginationToken]
    ExpenseDocuments: Optional[ExpenseDocumentList]
    Warnings: Optional[Warnings]
    StatusMessage: Optional[StatusMessage]
    AnalyzeExpenseModelVersion: Optional[String]


class GetLendingAnalysisRequest(ServiceRequest):
    JobId: JobId
    MaxResults: Optional[MaxResults]
    NextToken: Optional[PaginationToken]


class Prediction(TypedDict, total=False):
    """Contains information regarding predicted values returned by Amazon
    Textract operations, including the predicted value and the confidence in
    the predicted value.
    """

    Value: Optional[NonEmptyString]
    Confidence: Optional[Percent]


PredictionList = List[Prediction]


class PageClassification(TypedDict, total=False):
    """The class assigned to a Page object detected in an input document.
    Contains information regarding the predicted type/class of a document's
    page and the page number that the Page object was detected on.
    """

    PageType: PredictionList
    PageNumber: PredictionList


class LendingResult(TypedDict, total=False):
    """Contains the detections for each page analyzed through the Analyze
    Lending API.
    """

    Page: Optional[UInteger]
    PageClassification: Optional[PageClassification]
    Extractions: Optional[ExtractionList]


LendingResultList = List[LendingResult]


class GetLendingAnalysisResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    JobStatus: Optional[JobStatus]
    NextToken: Optional[PaginationToken]
    Results: Optional[LendingResultList]
    Warnings: Optional[Warnings]
    StatusMessage: Optional[StatusMessage]
    AnalyzeLendingModelVersion: Optional[String]


class GetLendingAnalysisSummaryRequest(ServiceRequest):
    JobId: JobId


UndetectedDocumentTypeList = List[NonEmptyString]


class LendingSummary(TypedDict, total=False):
    """Contains information regarding DocumentGroups and
    UndetectedDocumentTypes.
    """

    DocumentGroups: Optional[DocumentGroupList]
    UndetectedDocumentTypes: Optional[UndetectedDocumentTypeList]


class GetLendingAnalysisSummaryResponse(TypedDict, total=False):
    DocumentMetadata: Optional[DocumentMetadata]
    JobStatus: Optional[JobStatus]
    Summary: Optional[LendingSummary]
    Warnings: Optional[Warnings]
    StatusMessage: Optional[StatusMessage]
    AnalyzeLendingModelVersion: Optional[String]


class ListAdapterVersionsRequest(ServiceRequest):
    AdapterId: Optional[AdapterId]
    AfterCreationTime: Optional[DateTime]
    BeforeCreationTime: Optional[DateTime]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[PaginationToken]


class ListAdapterVersionsResponse(TypedDict, total=False):
    AdapterVersions: Optional[AdapterVersionList]
    NextToken: Optional[PaginationToken]


class ListAdaptersRequest(ServiceRequest):
    AfterCreationTime: Optional[DateTime]
    BeforeCreationTime: Optional[DateTime]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[PaginationToken]


class ListAdaptersResponse(TypedDict, total=False):
    Adapters: Optional[AdapterList]
    NextToken: Optional[PaginationToken]


class ListTagsForResourceRequest(ServiceRequest):
    ResourceARN: AmazonResourceName


class ListTagsForResourceResponse(TypedDict, total=False):
    Tags: Optional[TagMap]


class NotificationChannel(TypedDict, total=False):
    """The Amazon Simple Notification Service (Amazon SNS) topic to which
    Amazon Textract publishes the completion status of an asynchronous
    document operation.
    """

    SNSTopicArn: SNSTopicArn
    RoleArn: RoleArn


class StartDocumentAnalysisRequest(ServiceRequest):
    DocumentLocation: DocumentLocation
    FeatureTypes: FeatureTypes
    ClientRequestToken: Optional[ClientRequestToken]
    JobTag: Optional[JobTag]
    NotificationChannel: Optional[NotificationChannel]
    OutputConfig: Optional[OutputConfig]
    KMSKeyId: Optional[KMSKeyId]
    QueriesConfig: Optional[QueriesConfig]
    AdaptersConfig: Optional[AdaptersConfig]


class StartDocumentAnalysisResponse(TypedDict, total=False):
    JobId: Optional[JobId]


class StartDocumentTextDetectionRequest(ServiceRequest):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[ClientRequestToken]
    JobTag: Optional[JobTag]
    NotificationChannel: Optional[NotificationChannel]
    OutputConfig: Optional[OutputConfig]
    KMSKeyId: Optional[KMSKeyId]


class StartDocumentTextDetectionResponse(TypedDict, total=False):
    JobId: Optional[JobId]


class StartExpenseAnalysisRequest(ServiceRequest):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[ClientRequestToken]
    JobTag: Optional[JobTag]
    NotificationChannel: Optional[NotificationChannel]
    OutputConfig: Optional[OutputConfig]
    KMSKeyId: Optional[KMSKeyId]


class StartExpenseAnalysisResponse(TypedDict, total=False):
    JobId: Optional[JobId]


class StartLendingAnalysisRequest(ServiceRequest):
    DocumentLocation: DocumentLocation
    ClientRequestToken: Optional[ClientRequestToken]
    JobTag: Optional[JobTag]
    NotificationChannel: Optional[NotificationChannel]
    OutputConfig: Optional[OutputConfig]
    KMSKeyId: Optional[KMSKeyId]


class StartLendingAnalysisResponse(TypedDict, total=False):
    JobId: Optional[JobId]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    ResourceARN: AmazonResourceName
    Tags: TagMap


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    ResourceARN: AmazonResourceName
    TagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateAdapterRequest(ServiceRequest):
    AdapterId: AdapterId
    Description: Optional[AdapterDescription]
    AdapterName: Optional[AdapterName]
    AutoUpdate: Optional[AutoUpdate]


class UpdateAdapterResponse(TypedDict, total=False):
    AdapterId: Optional[AdapterId]
    AdapterName: Optional[AdapterName]
    CreationTime: Optional[DateTime]
    Description: Optional[AdapterDescription]
    FeatureTypes: Optional[FeatureTypes]
    AutoUpdate: Optional[AutoUpdate]


class TextractApi:
    service = "textract"
    version = "2018-06-27"

    @handler("AnalyzeDocument")
    def analyze_document(
        self,
        context: RequestContext,
        document: Document,
        feature_types: FeatureTypes,
        human_loop_config: HumanLoopConfig | None = None,
        queries_config: QueriesConfig | None = None,
        adapters_config: AdaptersConfig | None = None,
        **kwargs,
    ) -> AnalyzeDocumentResponse:
        """Analyzes an input document for relationships between detected items.

        The types of information returned are as follows:

        -  Form data (key-value pairs). The related information is returned in
           two Block objects, each of type ``KEY_VALUE_SET``: a KEY ``Block``
           object and a VALUE ``Block`` object. For example, *Name: Ana Silva
           Carolina* contains a key and value. *Name:* is the key. *Ana Silva
           Carolina* is the value.

        -  Table and table cell data. A TABLE ``Block`` object contains
           information about a detected table. A CELL ``Block`` object is
           returned for each cell in a table.

        -  Lines and words of text. A LINE ``Block`` object contains one or more
           WORD ``Block`` objects. All lines and words that are detected in the
           document are returned (including text that doesn't have a
           relationship with the value of ``FeatureTypes``).

        -  Signatures. A SIGNATURE ``Block`` object contains the location
           information of a signature in a document. If used in conjunction with
           forms or tables, a signature can be given a Key-Value pairing or be
           detected in the cell of a table.

        -  Query. A QUERY Block object contains the query text, alias and link
           to the associated Query results block object.

        -  Query Result. A QUERY_RESULT Block object contains the answer to the
           query and an ID that connects it to the query asked. This Block also
           contains a confidence score.

        Selection elements such as check boxes and option buttons (radio
        buttons) can be detected in form data and in tables. A SELECTION_ELEMENT
        ``Block`` object contains information about a selection element,
        including the selection status.

        You can choose which type of analysis to perform by specifying the
        ``FeatureTypes`` list.

        The output is returned in a list of ``Block`` objects.

        ``AnalyzeDocument`` is a synchronous operation. To analyze documents
        asynchronously, use StartDocumentAnalysis.

        For more information, see `Document Text
        Analysis <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html>`__.

        :param document: The input document as base64-encoded bytes or an Amazon S3 object.
        :param feature_types: A list of the types of analysis to perform.
        :param human_loop_config: Sets the configuration for the human in the loop workflow for analyzing
        documents.
        :param queries_config: Contains Queries and the alias for those Queries, as determined by the
        input.
        :param adapters_config: Specifies the adapter to be used when analyzing a document.
        :returns: AnalyzeDocumentResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises HumanLoopQuotaExceededException:
        """
        raise NotImplementedError

    @handler("AnalyzeExpense")
    def analyze_expense(
        self, context: RequestContext, document: Document, **kwargs
    ) -> AnalyzeExpenseResponse:
        """``AnalyzeExpense`` synchronously analyzes an input document for
        financially related relationships between text.

        Information is returned as ``ExpenseDocuments`` and seperated as
        follows:

        -  ``LineItemGroups``- A data set containing ``LineItems`` which store
           information about the lines of text, such as an item purchased and
           its price on a receipt.

        -  ``SummaryFields``- Contains all other information a receipt, such as
           header information or the vendors name.

        :param document: The input document, either as bytes or as an S3 object.
        :returns: AnalyzeExpenseResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("AnalyzeID")
    def analyze_id(
        self, context: RequestContext, document_pages: DocumentPages, **kwargs
    ) -> AnalyzeIDResponse:
        """Analyzes identity documents for relevant information. This information
        is extracted and returned as ``IdentityDocumentFields``, which records
        both the normalized field and value of the extracted text. Unlike other
        Amazon Textract operations, ``AnalyzeID`` doesn't return any Geometry
        data.

        :param document_pages: The document being passed to AnalyzeID.
        :returns: AnalyzeIDResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("CreateAdapter")
    def create_adapter(
        self,
        context: RequestContext,
        adapter_name: AdapterName,
        feature_types: FeatureTypes,
        client_request_token: ClientRequestToken | None = None,
        description: AdapterDescription | None = None,
        auto_update: AutoUpdate | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreateAdapterResponse:
        """Creates an adapter, which can be fine-tuned for enhanced performance on
        user provided documents. Takes an AdapterName and FeatureType. Currently
        the only supported feature type is ``QUERIES``. You can also provide a
        Description, Tags, and a ClientRequestToken. You can choose whether or
        not the adapter should be AutoUpdated with the AutoUpdate argument. By
        default, AutoUpdate is set to DISABLED.

        :param adapter_name: The name to be assigned to the adapter being created.
        :param feature_types: The type of feature that the adapter is being trained on.
        :param client_request_token: Idempotent token is used to recognize the request.
        :param description: The description to be assigned to the adapter being created.
        :param auto_update: Controls whether or not the adapter should automatically update.
        :param tags: A list of tags to be added to the adapter.
        :returns: CreateAdapterResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises IdempotentParameterMismatchException:
        :raises ThrottlingException:
        :raises LimitExceededException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        """
        raise NotImplementedError

    @handler("CreateAdapterVersion")
    def create_adapter_version(
        self,
        context: RequestContext,
        adapter_id: AdapterId,
        dataset_config: AdapterVersionDatasetConfig,
        output_config: OutputConfig,
        client_request_token: ClientRequestToken | None = None,
        kms_key_id: KMSKeyId | None = None,
        tags: TagMap | None = None,
        **kwargs,
    ) -> CreateAdapterVersionResponse:
        """Creates a new version of an adapter. Operates on a provided AdapterId
        and a specified dataset provided via the DatasetConfig argument.
        Requires that you specify an Amazon S3 bucket with the OutputConfig
        argument. You can provide an optional KMSKeyId, an optional
        ClientRequestToken, and optional tags.

        :param adapter_id: A string containing a unique ID for the adapter that will receive a new
        version.
        :param dataset_config: Specifies a dataset used to train a new adapter version.
        :param output_config: Sets whether or not your output will go to a user created bucket.
        :param client_request_token: Idempotent token is used to recognize the request.
        :param kms_key_id: The identifier for your AWS Key Management Service key (AWS KMS key).
        :param tags: A set of tags (key-value pairs) that you want to attach to the adapter
        version.
        :returns: CreateAdapterVersionResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises IdempotentParameterMismatchException:
        :raises ThrottlingException:
        :raises LimitExceededException:
        :raises ValidationException:
        :raises ServiceQuotaExceededException:
        :raises ResourceNotFoundException:
        :raises ConflictException:
        """
        raise NotImplementedError

    @handler("DeleteAdapter")
    def delete_adapter(
        self, context: RequestContext, adapter_id: AdapterId, **kwargs
    ) -> DeleteAdapterResponse:
        """Deletes an Amazon Textract adapter. Takes an AdapterId and deletes the
        adapter specified by the ID.

        :param adapter_id: A string containing a unique ID for the adapter to be deleted.
        :returns: DeleteAdapterResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteAdapterVersion")
    def delete_adapter_version(
        self,
        context: RequestContext,
        adapter_id: AdapterId,
        adapter_version: AdapterVersion,
        **kwargs,
    ) -> DeleteAdapterVersionResponse:
        """Deletes an Amazon Textract adapter version. Requires that you specify
        both an AdapterId and a AdapterVersion. Deletes the adapter version
        specified by the AdapterId and the AdapterVersion.

        :param adapter_id: A string containing a unique ID for the adapter version that will be
        deleted.
        :param adapter_version: Specifies the adapter version to be deleted.
        :returns: DeleteAdapterVersionResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("DetectDocumentText")
    def detect_document_text(
        self, context: RequestContext, document: Document, **kwargs
    ) -> DetectDocumentTextResponse:
        """Detects text in the input document. Amazon Textract can detect lines of
        text and the words that make up a line of text. The input document must
        be in one of the following image formats: JPEG, PNG, PDF, or TIFF.
        ``DetectDocumentText`` returns the detected text in an array of Block
        objects.

        Each document page has as an associated ``Block`` of type PAGE. Each
        PAGE ``Block`` object is the parent of LINE ``Block`` objects that
        represent the lines of detected text on a page. A LINE ``Block`` object
        is a parent for each word that makes up the line. Words are represented
        by ``Block`` objects of type WORD.

        ``DetectDocumentText`` is a synchronous operation. To analyze documents
        asynchronously, use StartDocumentTextDetection.

        For more information, see `Document Text
        Detection <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html>`__.

        :param document: The input document as base64-encoded bytes or an Amazon S3 object.
        :returns: DetectDocumentTextResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        """
        raise NotImplementedError

    @handler("GetAdapter")
    def get_adapter(
        self, context: RequestContext, adapter_id: AdapterId, **kwargs
    ) -> GetAdapterResponse:
        """Gets configuration information for an adapter specified by an AdapterId,
        returning information on AdapterName, Description, CreationTime,
        AutoUpdate status, and FeatureTypes.

        :param adapter_id: A string containing a unique ID for the adapter.
        :returns: GetAdapterResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetAdapterVersion")
    def get_adapter_version(
        self,
        context: RequestContext,
        adapter_id: AdapterId,
        adapter_version: AdapterVersion,
        **kwargs,
    ) -> GetAdapterVersionResponse:
        """Gets configuration information for the specified adapter version,
        including: AdapterId, AdapterVersion, FeatureTypes, Status,
        StatusMessage, DatasetConfig, KMSKeyId, OutputConfig, Tags and
        EvaluationMetrics.

        :param adapter_id: A string specifying a unique ID for the adapter version you want to
        retrieve information for.
        :param adapter_version: A string specifying the adapter version you want to retrieve information
        for.
        :returns: GetAdapterVersionResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("GetDocumentAnalysis")
    def get_document_analysis(
        self,
        context: RequestContext,
        job_id: JobId,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> GetDocumentAnalysisResponse:
        """Gets the results for an Amazon Textract asynchronous operation that
        analyzes text in a document.

        You start asynchronous text analysis by calling StartDocumentAnalysis,
        which returns a job identifier (``JobId``). When the text analysis
        operation finishes, Amazon Textract publishes a completion status to the
        Amazon Simple Notification Service (Amazon SNS) topic that's registered
        in the initial call to ``StartDocumentAnalysis``. To get the results of
        the text-detection operation, first check that the status value
        published to the Amazon SNS topic is ``SUCCEEDED``. If so, call
        ``GetDocumentAnalysis``, and pass the job identifier (``JobId``) from
        the initial call to ``StartDocumentAnalysis``.

        ``GetDocumentAnalysis`` returns an array of Block objects. The following
        types of information are returned:

        -  Form data (key-value pairs). The related information is returned in
           two Block objects, each of type ``KEY_VALUE_SET``: a KEY ``Block``
           object and a VALUE ``Block`` object. For example, *Name: Ana Silva
           Carolina* contains a key and value. *Name:* is the key. *Ana Silva
           Carolina* is the value.

        -  Table and table cell data. A TABLE ``Block`` object contains
           information about a detected table. A CELL ``Block`` object is
           returned for each cell in a table.

        -  Lines and words of text. A LINE ``Block`` object contains one or more
           WORD ``Block`` objects. All lines and words that are detected in the
           document are returned (including text that doesn't have a
           relationship with the value of the ``StartDocumentAnalysis``
           ``FeatureTypes`` input parameter).

        -  Query. A QUERY Block object contains the query text, alias and link
           to the associated Query results block object.

        -  Query Results. A QUERY_RESULT Block object contains the answer to the
           query and an ID that connects it to the query asked. This Block also
           contains a confidence score.

        While processing a document with queries, look out for
        ``INVALID_REQUEST_PARAMETERS`` output. This indicates that either the
        per page query limit has been exceeded or that the operation is trying
        to query a page in the document which doesn’t exist.

        Selection elements such as check boxes and option buttons (radio
        buttons) can be detected in form data and in tables. A SELECTION_ELEMENT
        ``Block`` object contains information about a selection element,
        including the selection status.

        Use the ``MaxResults`` parameter to limit the number of blocks that are
        returned. If there are more results than specified in ``MaxResults``,
        the value of ``NextToken`` in the operation response contains a
        pagination token for getting the next set of results. To get the next
        page of results, call ``GetDocumentAnalysis``, and populate the
        ``NextToken`` request parameter with the token value that's returned
        from the previous call to ``GetDocumentAnalysis``.

        For more information, see `Document Text
        Analysis <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html>`__.

        :param job_id: A unique identifier for the text-detection job.
        :param max_results: The maximum number of results to return per paginated call.
        :param next_token: If the previous response was incomplete (because there are more blocks
        to retrieve), Amazon Textract returns a pagination token in the
        response.
        :returns: GetDocumentAnalysisResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InvalidJobIdException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        """
        raise NotImplementedError

    @handler("GetDocumentTextDetection")
    def get_document_text_detection(
        self,
        context: RequestContext,
        job_id: JobId,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> GetDocumentTextDetectionResponse:
        """Gets the results for an Amazon Textract asynchronous operation that
        detects text in a document. Amazon Textract can detect lines of text and
        the words that make up a line of text.

        You start asynchronous text detection by calling
        StartDocumentTextDetection, which returns a job identifier (``JobId``).
        When the text detection operation finishes, Amazon Textract publishes a
        completion status to the Amazon Simple Notification Service (Amazon SNS)
        topic that's registered in the initial call to
        ``StartDocumentTextDetection``. To get the results of the text-detection
        operation, first check that the status value published to the Amazon SNS
        topic is ``SUCCEEDED``. If so, call ``GetDocumentTextDetection``, and
        pass the job identifier (``JobId``) from the initial call to
        ``StartDocumentTextDetection``.

        ``GetDocumentTextDetection`` returns an array of Block objects.

        Each document page has as an associated ``Block`` of type PAGE. Each
        PAGE ``Block`` object is the parent of LINE ``Block`` objects that
        represent the lines of detected text on a page. A LINE ``Block`` object
        is a parent for each word that makes up the line. Words are represented
        by ``Block`` objects of type WORD.

        Use the MaxResults parameter to limit the number of blocks that are
        returned. If there are more results than specified in ``MaxResults``,
        the value of ``NextToken`` in the operation response contains a
        pagination token for getting the next set of results. To get the next
        page of results, call ``GetDocumentTextDetection``, and populate the
        ``NextToken`` request parameter with the token value that's returned
        from the previous call to ``GetDocumentTextDetection``.

        For more information, see `Document Text
        Detection <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html>`__.

        :param job_id: A unique identifier for the text detection job.
        :param max_results: The maximum number of results to return per paginated call.
        :param next_token: If the previous response was incomplete (because there are more blocks
        to retrieve), Amazon Textract returns a pagination token in the
        response.
        :returns: GetDocumentTextDetectionResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InvalidJobIdException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        """
        raise NotImplementedError

    @handler("GetExpenseAnalysis")
    def get_expense_analysis(
        self,
        context: RequestContext,
        job_id: JobId,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> GetExpenseAnalysisResponse:
        """Gets the results for an Amazon Textract asynchronous operation that
        analyzes invoices and receipts. Amazon Textract finds contact
        information, items purchased, and vendor name, from input invoices and
        receipts.

        You start asynchronous invoice/receipt analysis by calling
        StartExpenseAnalysis, which returns a job identifier (``JobId``). Upon
        completion of the invoice/receipt analysis, Amazon Textract publishes
        the completion status to the Amazon Simple Notification Service (Amazon
        SNS) topic. This topic must be registered in the initial call to
        ``StartExpenseAnalysis``. To get the results of the invoice/receipt
        analysis operation, first ensure that the status value published to the
        Amazon SNS topic is ``SUCCEEDED``. If so, call ``GetExpenseAnalysis``,
        and pass the job identifier (``JobId``) from the initial call to
        ``StartExpenseAnalysis``.

        Use the MaxResults parameter to limit the number of blocks that are
        returned. If there are more results than specified in ``MaxResults``,
        the value of ``NextToken`` in the operation response contains a
        pagination token for getting the next set of results. To get the next
        page of results, call ``GetExpenseAnalysis``, and populate the
        ``NextToken`` request parameter with the token value that's returned
        from the previous call to ``GetExpenseAnalysis``.

        For more information, see `Analyzing Invoices and
        Receipts <https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html>`__.

        :param job_id: A unique identifier for the text detection job.
        :param max_results: The maximum number of results to return per paginated call.
        :param next_token: If the previous response was incomplete (because there are more blocks
        to retrieve), Amazon Textract returns a pagination token in the
        response.
        :returns: GetExpenseAnalysisResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InvalidJobIdException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        """
        raise NotImplementedError

    @handler("GetLendingAnalysis")
    def get_lending_analysis(
        self,
        context: RequestContext,
        job_id: JobId,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> GetLendingAnalysisResponse:
        """Gets the results for an Amazon Textract asynchronous operation that
        analyzes text in a lending document.

        You start asynchronous text analysis by calling
        ``StartLendingAnalysis``, which returns a job identifier (``JobId``).
        When the text analysis operation finishes, Amazon Textract publishes a
        completion status to the Amazon Simple Notification Service (Amazon SNS)
        topic that's registered in the initial call to ``StartLendingAnalysis``.

        To get the results of the text analysis operation, first check that the
        status value published to the Amazon SNS topic is SUCCEEDED. If so, call
        GetLendingAnalysis, and pass the job identifier (``JobId``) from the
        initial call to ``StartLendingAnalysis``.

        :param job_id: A unique identifier for the lending or text-detection job.
        :param max_results: The maximum number of results to return per paginated call.
        :param next_token: If the previous response was incomplete, Amazon Textract returns a
        pagination token in the response.
        :returns: GetLendingAnalysisResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InvalidJobIdException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        """
        raise NotImplementedError

    @handler("GetLendingAnalysisSummary")
    def get_lending_analysis_summary(
        self, context: RequestContext, job_id: JobId, **kwargs
    ) -> GetLendingAnalysisSummaryResponse:
        """Gets summarized results for the ``StartLendingAnalysis`` operation,
        which analyzes text in a lending document. The returned summary consists
        of information about documents grouped together by a common document
        type. Information like detected signatures, page numbers, and split
        documents is returned with respect to the type of grouped document.

        You start asynchronous text analysis by calling
        ``StartLendingAnalysis``, which returns a job identifier (``JobId``).
        When the text analysis operation finishes, Amazon Textract publishes a
        completion status to the Amazon Simple Notification Service (Amazon SNS)
        topic that's registered in the initial call to ``StartLendingAnalysis``.

        To get the results of the text analysis operation, first check that the
        status value published to the Amazon SNS topic is SUCCEEDED. If so, call
        ``GetLendingAnalysisSummary``, and pass the job identifier (``JobId``)
        from the initial call to ``StartLendingAnalysis``.

        :param job_id: A unique identifier for the lending or text-detection job.
        :returns: GetLendingAnalysisSummaryResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InvalidJobIdException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        """
        raise NotImplementedError

    @handler("ListAdapterVersions")
    def list_adapter_versions(
        self,
        context: RequestContext,
        adapter_id: AdapterId | None = None,
        after_creation_time: DateTime | None = None,
        before_creation_time: DateTime | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListAdapterVersionsResponse:
        """List all version of an adapter that meet the specified filtration
        criteria.

        :param adapter_id: A string containing a unique ID for the adapter to match for when
        listing adapter versions.
        :param after_creation_time: Specifies the lower bound for the ListAdapterVersions operation.
        :param before_creation_time: Specifies the upper bound for the ListAdapterVersions operation.
        :param max_results: The maximum number of results to return when listing adapter versions.
        :param next_token: Identifies the next page of results to return when listing adapter
        versions.
        :returns: ListAdapterVersionsResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError

    @handler("ListAdapters")
    def list_adapters(
        self,
        context: RequestContext,
        after_creation_time: DateTime | None = None,
        before_creation_time: DateTime | None = None,
        max_results: MaxResults | None = None,
        next_token: PaginationToken | None = None,
        **kwargs,
    ) -> ListAdaptersResponse:
        """Lists all adapters that match the specified filtration criteria.

        :param after_creation_time: Specifies the lower bound for the ListAdapters operation.
        :param before_creation_time: Specifies the upper bound for the ListAdapters operation.
        :param max_results: The maximum number of results to return when listing adapters.
        :param next_token: Identifies the next page of results to return when listing adapters.
        :returns: ListAdaptersResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, **kwargs
    ) -> ListTagsForResourceResponse:
        """Lists all tags for an Amazon Textract resource.

        :param resource_arn: The Amazon Resource Name (ARN) that specifies the resource to list tags
        for.
        :returns: ListTagsForResourceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("StartDocumentAnalysis")
    def start_document_analysis(
        self,
        context: RequestContext,
        document_location: DocumentLocation,
        feature_types: FeatureTypes,
        client_request_token: ClientRequestToken | None = None,
        job_tag: JobTag | None = None,
        notification_channel: NotificationChannel | None = None,
        output_config: OutputConfig | None = None,
        kms_key_id: KMSKeyId | None = None,
        queries_config: QueriesConfig | None = None,
        adapters_config: AdaptersConfig | None = None,
        **kwargs,
    ) -> StartDocumentAnalysisResponse:
        """Starts the asynchronous analysis of an input document for relationships
        between detected items such as key-value pairs, tables, and selection
        elements.

        ``StartDocumentAnalysis`` can analyze text in documents that are in
        JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon
        S3 bucket. Use DocumentLocation to specify the bucket name and file name
        of the document.

        ``StartDocumentAnalysis`` returns a job identifier (``JobId``) that you
        use to get the results of the operation. When text analysis is finished,
        Amazon Textract publishes a completion status to the Amazon Simple
        Notification Service (Amazon SNS) topic that you specify in
        ``NotificationChannel``. To get the results of the text analysis
        operation, first check that the status value published to the Amazon SNS
        topic is ``SUCCEEDED``. If so, call GetDocumentAnalysis, and pass the
        job identifier (``JobId``) from the initial call to
        ``StartDocumentAnalysis``.

        For more information, see `Document Text
        Analysis <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html>`__.

        :param document_location: The location of the document to be processed.
        :param feature_types: A list of the types of analysis to perform.
        :param client_request_token: The idempotent token that you use to identify the start request.
        :param job_tag: An identifier that you specify that's included in the completion
        notification published to the Amazon SNS topic.
        :param notification_channel: The Amazon SNS topic ARN that you want Amazon Textract to publish the
        completion status of the operation to.
        :param output_config: Sets if the output will go to a customer defined bucket.
        :param kms_key_id: The KMS key used to encrypt the inference results.
        :param queries_config: .
        :param adapters_config: Specifies the adapter to be used when analyzing a document.
        :returns: StartDocumentAnalysisResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises IdempotentParameterMismatchException:
        :raises ThrottlingException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("StartDocumentTextDetection")
    def start_document_text_detection(
        self,
        context: RequestContext,
        document_location: DocumentLocation,
        client_request_token: ClientRequestToken | None = None,
        job_tag: JobTag | None = None,
        notification_channel: NotificationChannel | None = None,
        output_config: OutputConfig | None = None,
        kms_key_id: KMSKeyId | None = None,
        **kwargs,
    ) -> StartDocumentTextDetectionResponse:
        """Starts the asynchronous detection of text in a document. Amazon Textract
        can detect lines of text and the words that make up a line of text.

        ``StartDocumentTextDetection`` can analyze text in documents that are in
        JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon
        S3 bucket. Use DocumentLocation to specify the bucket name and file name
        of the document.

        ``StartTextDetection`` returns a job identifier (``JobId``) that you use
        to get the results of the operation. When text detection is finished,
        Amazon Textract publishes a completion status to the Amazon Simple
        Notification Service (Amazon SNS) topic that you specify in
        ``NotificationChannel``. To get the results of the text detection
        operation, first check that the status value published to the Amazon SNS
        topic is ``SUCCEEDED``. If so, call GetDocumentTextDetection, and pass
        the job identifier (``JobId``) from the initial call to
        ``StartDocumentTextDetection``.

        For more information, see `Document Text
        Detection <https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html>`__.

        :param document_location: The location of the document to be processed.
        :param client_request_token: The idempotent token that's used to identify the start request.
        :param job_tag: An identifier that you specify that's included in the completion
        notification published to the Amazon SNS topic.
        :param notification_channel: The Amazon SNS topic ARN that you want Amazon Textract to publish the
        completion status of the operation to.
        :param output_config: Sets if the output will go to a customer defined bucket.
        :param kms_key_id: The KMS key used to encrypt the inference results.
        :returns: StartDocumentTextDetectionResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises IdempotentParameterMismatchException:
        :raises ThrottlingException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("StartExpenseAnalysis")
    def start_expense_analysis(
        self,
        context: RequestContext,
        document_location: DocumentLocation,
        client_request_token: ClientRequestToken | None = None,
        job_tag: JobTag | None = None,
        notification_channel: NotificationChannel | None = None,
        output_config: OutputConfig | None = None,
        kms_key_id: KMSKeyId | None = None,
        **kwargs,
    ) -> StartExpenseAnalysisResponse:
        """Starts the asynchronous analysis of invoices or receipts for data like
        contact information, items purchased, and vendor names.

        ``StartExpenseAnalysis`` can analyze text in documents that are in JPEG,
        PNG, and PDF format. The documents must be stored in an Amazon S3
        bucket. Use the DocumentLocation parameter to specify the name of your
        S3 bucket and the name of the document in that bucket.

        ``StartExpenseAnalysis`` returns a job identifier (``JobId``) that you
        will provide to ``GetExpenseAnalysis`` to retrieve the results of the
        operation. When the analysis of the input invoices/receipts is finished,
        Amazon Textract publishes a completion status to the Amazon Simple
        Notification Service (Amazon SNS) topic that you provide to the
        ``NotificationChannel``. To obtain the results of the invoice and
        receipt analysis operation, ensure that the status value published to
        the Amazon SNS topic is ``SUCCEEDED``. If so, call GetExpenseAnalysis,
        and pass the job identifier (``JobId``) that was returned by your call
        to ``StartExpenseAnalysis``.

        For more information, see `Analyzing Invoices and
        Receipts <https://docs.aws.amazon.com/textract/latest/dg/invoice-receipts.html>`__.

        :param document_location: The location of the document to be processed.
        :param client_request_token: The idempotent token that's used to identify the start request.
        :param job_tag: An identifier you specify that's included in the completion notification
        published to the Amazon SNS topic.
        :param notification_channel: The Amazon SNS topic ARN that you want Amazon Textract to publish the
        completion status of the operation to.
        :param output_config: Sets if the output will go to a customer defined bucket.
        :param kms_key_id: The KMS key used to encrypt the inference results.
        :returns: StartExpenseAnalysisResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises IdempotentParameterMismatchException:
        :raises ThrottlingException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("StartLendingAnalysis")
    def start_lending_analysis(
        self,
        context: RequestContext,
        document_location: DocumentLocation,
        client_request_token: ClientRequestToken | None = None,
        job_tag: JobTag | None = None,
        notification_channel: NotificationChannel | None = None,
        output_config: OutputConfig | None = None,
        kms_key_id: KMSKeyId | None = None,
        **kwargs,
    ) -> StartLendingAnalysisResponse:
        """Starts the classification and analysis of an input document.
        ``StartLendingAnalysis`` initiates the classification and analysis of a
        packet of lending documents. ``StartLendingAnalysis`` operates on a
        document file located in an Amazon S3 bucket.

        ``StartLendingAnalysis`` can analyze text in documents that are in one
        of the following formats: JPEG, PNG, TIFF, PDF. Use ``DocumentLocation``
        to specify the bucket name and the file name of the document.

        ``StartLendingAnalysis`` returns a job identifier (``JobId``) that you
        use to get the results of the operation. When the text analysis is
        finished, Amazon Textract publishes a completion status to the Amazon
        Simple Notification Service (Amazon SNS) topic that you specify in
        ``NotificationChannel``. To get the results of the text analysis
        operation, first check that the status value published to the Amazon SNS
        topic is SUCCEEDED. If the status is SUCCEEDED you can call either
        ``GetLendingAnalysis`` or ``GetLendingAnalysisSummary`` and provide the
        ``JobId`` to obtain the results of the analysis.

        If using ``OutputConfig`` to specify an Amazon S3 bucket, the output
        will be contained within the specified prefix in a directory labeled
        with the job-id. In the directory there are 3 sub-directories:

        -  detailedResponse (contains the GetLendingAnalysis response)

        -  summaryResponse (for the GetLendingAnalysisSummary response)

        -  splitDocuments (documents split across logical boundaries)

        :param document_location: The Amazon S3 bucket that contains the document to be processed.
        :param client_request_token: The idempotent token that you use to identify the start request.
        :param job_tag: An identifier that you specify to be included in the completion
        notification published to the Amazon SNS topic.
        :param notification_channel: The Amazon Simple Notification Service (Amazon SNS) topic to which
        Amazon Textract publishes the completion status of an asynchronous
        document operation.
        :param output_config: Sets whether or not your output will go to a user created bucket.
        :param kms_key_id: The KMS key used to encrypt the inference results.
        :returns: StartLendingAnalysisResponse
        :raises InvalidParameterException:
        :raises InvalidS3ObjectException:
        :raises InvalidKMSKeyException:
        :raises UnsupportedDocumentException:
        :raises DocumentTooLargeException:
        :raises BadDocumentException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises IdempotentParameterMismatchException:
        :raises ThrottlingException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, tags: TagMap, **kwargs
    ) -> TagResourceResponse:
        """Adds one or more tags to the specified resource.

        :param resource_arn: The Amazon Resource Name (ARN) that specifies the resource to be tagged.
        :param tags: A set of tags (key-value pairs) that you want to assign to the resource.
        :returns: TagResourceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises ServiceQuotaExceededException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: AmazonResourceName,
        tag_keys: TagKeyList,
        **kwargs,
    ) -> UntagResourceResponse:
        """Removes any tags with the specified keys from the specified resource.

        :param resource_arn: The Amazon Resource Name (ARN) that specifies the resource to be
        untagged.
        :param tag_keys: Specifies the tags to be removed from the resource specified by the
        ResourceARN.
        :returns: UntagResourceResponse
        :raises ResourceNotFoundException:
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        """
        raise NotImplementedError

    @handler("UpdateAdapter")
    def update_adapter(
        self,
        context: RequestContext,
        adapter_id: AdapterId,
        description: AdapterDescription | None = None,
        adapter_name: AdapterName | None = None,
        auto_update: AutoUpdate | None = None,
        **kwargs,
    ) -> UpdateAdapterResponse:
        """Update the configuration for an adapter. FeatureTypes configurations
        cannot be updated. At least one new parameter must be specified as an
        argument.

        :param adapter_id: A string containing a unique ID for the adapter that will be updated.
        :param description: The new description to be applied to the adapter.
        :param adapter_name: The new name to be applied to the adapter.
        :param auto_update: The new auto-update status to be applied to the adapter.
        :returns: UpdateAdapterResponse
        :raises InvalidParameterException:
        :raises AccessDeniedException:
        :raises ConflictException:
        :raises ProvisionedThroughputExceededException:
        :raises InternalServerError:
        :raises ThrottlingException:
        :raises ValidationException:
        :raises ResourceNotFoundException:
        """
        raise NotImplementedError
