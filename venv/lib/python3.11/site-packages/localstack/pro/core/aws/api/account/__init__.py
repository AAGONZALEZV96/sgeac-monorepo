from datetime import datetime
from enum import StrEnum
from typing import List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccountId = str
AccountName = str
AddressLine = str
City = str
CompanyName = str
ContactInformationPhoneNumber = str
CountryCode = str
DistrictOrCounty = str
EmailAddress = str
FullName = str
ListRegionsRequestMaxResultsInteger = int
ListRegionsRequestNextTokenString = str
Name = str
Otp = str
PhoneNumber = str
PostalCode = str
PrimaryEmailAddress = str
RegionName = str
SensitiveString = str
StateOrRegion = str
String = str
Title = str
WebsiteUrl = str


class AlternateContactType(StrEnum):
    BILLING = "BILLING"
    OPERATIONS = "OPERATIONS"
    SECURITY = "SECURITY"


class PrimaryEmailUpdateStatus(StrEnum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"


class RegionOptStatus(StrEnum):
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    ENABLED_BY_DEFAULT = "ENABLED_BY_DEFAULT"


class ValidationExceptionReason(StrEnum):
    invalidRegionOptTarget = "invalidRegionOptTarget"
    fieldValidationFailed = "fieldValidationFailed"


class AccessDeniedException(ServiceException):
    """The operation failed because the calling identity doesn't have the
    minimum required permissions.
    """

    code: str = "AccessDeniedException"
    sender_fault: bool = True
    status_code: int = 403
    errorType: Optional[String]


class ConflictException(ServiceException):
    """The request could not be processed because of a conflict in the current
    status of the resource. For example, this happens if you try to enable a
    Region that is currently being disabled (in a status of DISABLING) or if
    you try to change an account’s root user email to an email address which
    is already in use.
    """

    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 409
    errorType: Optional[String]


class InternalServerException(ServiceException):
    """The operation failed because of an error internal to Amazon Web
    Services. Try your operation again later.
    """

    code: str = "InternalServerException"
    sender_fault: bool = False
    status_code: int = 500
    errorType: Optional[String]


class ResourceNotFoundException(ServiceException):
    """The operation failed because it specified a resource that can't be
    found.
    """

    code: str = "ResourceNotFoundException"
    sender_fault: bool = True
    status_code: int = 404
    errorType: Optional[String]


class TooManyRequestsException(ServiceException):
    """The operation failed because it was called too frequently and exceeded a
    throttle limit.
    """

    code: str = "TooManyRequestsException"
    sender_fault: bool = True
    status_code: int = 429
    errorType: Optional[String]


class ValidationExceptionField(TypedDict, total=False):
    """The input failed to meet the constraints specified by the Amazon Web
    Services service in a specified field.
    """

    message: SensitiveString
    name: String


ValidationExceptionFieldList = List[ValidationExceptionField]


class ValidationException(ServiceException):
    """The operation failed because one of the input parameters was invalid."""

    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400
    fieldList: Optional[ValidationExceptionFieldList]
    reason: Optional[ValidationExceptionReason]


class AcceptPrimaryEmailUpdateRequest(ServiceRequest):
    AccountId: AccountId
    Otp: Otp
    PrimaryEmail: PrimaryEmailAddress


class AcceptPrimaryEmailUpdateResponse(TypedDict, total=False):
    Status: Optional[PrimaryEmailUpdateStatus]


AccountCreatedDate = datetime


class AlternateContact(TypedDict, total=False):
    """A structure that contains the details of an alternate contact associated
    with an Amazon Web Services account
    """

    AlternateContactType: Optional[AlternateContactType]
    EmailAddress: Optional[EmailAddress]
    Name: Optional[Name]
    PhoneNumber: Optional[PhoneNumber]
    Title: Optional[Title]


class ContactInformation(TypedDict, total=False):
    """Contains the details of the primary contact information associated with
    an Amazon Web Services account.
    """

    AddressLine1: AddressLine
    AddressLine2: Optional[AddressLine]
    AddressLine3: Optional[AddressLine]
    City: City
    CompanyName: Optional[CompanyName]
    CountryCode: CountryCode
    DistrictOrCounty: Optional[DistrictOrCounty]
    FullName: FullName
    PhoneNumber: ContactInformationPhoneNumber
    PostalCode: PostalCode
    StateOrRegion: Optional[StateOrRegion]
    WebsiteUrl: Optional[WebsiteUrl]


class DeleteAlternateContactRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    AlternateContactType: AlternateContactType


class DisableRegionRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    RegionName: RegionName


class EnableRegionRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    RegionName: RegionName


class GetAccountInformationRequest(ServiceRequest):
    AccountId: Optional[AccountId]


class GetAccountInformationResponse(TypedDict, total=False):
    AccountCreatedDate: Optional[AccountCreatedDate]
    AccountId: Optional[AccountId]
    AccountName: Optional[AccountName]


class GetAlternateContactRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    AlternateContactType: AlternateContactType


class GetAlternateContactResponse(TypedDict, total=False):
    AlternateContact: Optional[AlternateContact]


class GetContactInformationRequest(ServiceRequest):
    AccountId: Optional[AccountId]


class GetContactInformationResponse(TypedDict, total=False):
    ContactInformation: Optional[ContactInformation]


class GetPrimaryEmailRequest(ServiceRequest):
    AccountId: AccountId


class GetPrimaryEmailResponse(TypedDict, total=False):
    PrimaryEmail: Optional[PrimaryEmailAddress]


class GetRegionOptStatusRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    RegionName: RegionName


class GetRegionOptStatusResponse(TypedDict, total=False):
    RegionName: Optional[RegionName]
    RegionOptStatus: Optional[RegionOptStatus]


RegionOptStatusList = List[RegionOptStatus]


class ListRegionsRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    MaxResults: Optional[ListRegionsRequestMaxResultsInteger]
    NextToken: Optional[ListRegionsRequestNextTokenString]
    RegionOptStatusContains: Optional[RegionOptStatusList]


class Region(TypedDict, total=False):
    """This is a structure that expresses the Region for a given account,
    consisting of a name and opt-in status.
    """

    RegionName: Optional[RegionName]
    RegionOptStatus: Optional[RegionOptStatus]


RegionOptList = List[Region]


class ListRegionsResponse(TypedDict, total=False):
    NextToken: Optional[String]
    Regions: Optional[RegionOptList]


class PutAccountNameRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    AccountName: AccountName


class PutAlternateContactRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    AlternateContactType: AlternateContactType
    EmailAddress: EmailAddress
    Name: Name
    PhoneNumber: PhoneNumber
    Title: Title


class PutContactInformationRequest(ServiceRequest):
    AccountId: Optional[AccountId]
    ContactInformation: ContactInformation


class StartPrimaryEmailUpdateRequest(ServiceRequest):
    AccountId: AccountId
    PrimaryEmail: PrimaryEmailAddress


class StartPrimaryEmailUpdateResponse(TypedDict, total=False):
    Status: Optional[PrimaryEmailUpdateStatus]


class AccountApi:
    service = "account"
    version = "2021-02-01"

    @handler("AcceptPrimaryEmailUpdate")
    def accept_primary_email_update(
        self,
        context: RequestContext,
        account_id: AccountId,
        otp: Otp,
        primary_email: PrimaryEmailAddress,
        **kwargs,
    ) -> AcceptPrimaryEmailUpdateResponse:
        """Accepts the request that originated from StartPrimaryEmailUpdate to
        update the primary email address (also known as the root user email
        address) for the specified account.

        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :param otp: The OTP code sent to the ``PrimaryEmail`` specified on the
        ``StartPrimaryEmailUpdate`` API call.
        :param primary_email: The new primary email address for use with the specified account.
        :returns: AcceptPrimaryEmailUpdateResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DeleteAlternateContact")
    def delete_alternate_contact(
        self,
        context: RequestContext,
        alternate_contact_type: AlternateContactType,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> None:
        """Deletes the specified alternate contact from an Amazon Web Services
        account.

        For complete details about how to use the alternate contact operations,
        see `Access or updating the alternate
        contacts <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html>`__.

        Before you can update the alternate contact information for an Amazon
        Web Services account that is managed by Organizations, you must first
        enable integration between Amazon Web Services Account Management and
        Organizations. For more information, see `Enabling trusted access for
        Amazon Web Services Account
        Management <https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html>`__.

        :param alternate_contact_type: Specifies which of the alternate contacts to delete.
        :param account_id: Specifies the 12 digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("DisableRegion")
    def disable_region(
        self,
        context: RequestContext,
        region_name: RegionName,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> None:
        """Disables (opts-out) a particular Region for an account.

        The act of disabling a Region will remove all IAM access to any
        resources that reside in that Region.

        :param region_name: Specifies the Region-code for a given Region name (for example,
        ``af-south-1``).
        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("EnableRegion")
    def enable_region(
        self,
        context: RequestContext,
        region_name: RegionName,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> None:
        """Enables (opts-in) a particular Region for an account.

        :param region_name: Specifies the Region-code for a given Region name (for example,
        ``af-south-1``).
        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetAccountInformation")
    def get_account_information(
        self, context: RequestContext, account_id: AccountId | None = None, **kwargs
    ) -> GetAccountInformationResponse:
        """Retrieves information about the specified account including its account
        name, account ID, and account creation date and time. To use this API,
        an IAM user or role must have the ``account:GetAccountInformation`` IAM
        permission.

        :param account_id: Specifies the 12 digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :returns: GetAccountInformationResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetAlternateContact")
    def get_alternate_contact(
        self,
        context: RequestContext,
        alternate_contact_type: AlternateContactType,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> GetAlternateContactResponse:
        """Retrieves the specified alternate contact attached to an Amazon Web
        Services account.

        For complete details about how to use the alternate contact operations,
        see `Access or updating the alternate
        contacts <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html>`__.

        Before you can update the alternate contact information for an Amazon
        Web Services account that is managed by Organizations, you must first
        enable integration between Amazon Web Services Account Management and
        Organizations. For more information, see `Enabling trusted access for
        Amazon Web Services Account
        Management <https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html>`__.

        :param alternate_contact_type: Specifies which alternate contact you want to retrieve.
        :param account_id: Specifies the 12 digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :returns: GetAlternateContactResponse
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetContactInformation")
    def get_contact_information(
        self, context: RequestContext, account_id: AccountId | None = None, **kwargs
    ) -> GetContactInformationResponse:
        """Retrieves the primary contact information of an Amazon Web Services
        account.

        For complete details about how to use the primary contact operations,
        see `Update the primary and alternate contact
        information <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html>`__.

        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :returns: GetContactInformationResponse
        :raises ResourceNotFoundException:
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetPrimaryEmail")
    def get_primary_email(
        self, context: RequestContext, account_id: AccountId, **kwargs
    ) -> GetPrimaryEmailResponse:
        """Retrieves the primary email address for the specified account.

        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :returns: GetPrimaryEmailResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("GetRegionOptStatus")
    def get_region_opt_status(
        self,
        context: RequestContext,
        region_name: RegionName,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> GetRegionOptStatusResponse:
        """Retrieves the opt-in status of a particular Region.

        :param region_name: Specifies the Region-code for a given Region name (for example,
        ``af-south-1``).
        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :returns: GetRegionOptStatusResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("ListRegions")
    def list_regions(
        self,
        context: RequestContext,
        account_id: AccountId | None = None,
        max_results: ListRegionsRequestMaxResultsInteger | None = None,
        next_token: ListRegionsRequestNextTokenString | None = None,
        region_opt_status_contains: RegionOptStatusList | None = None,
        **kwargs,
    ) -> ListRegionsResponse:
        """Lists all the Regions for a given account and their respective opt-in
        statuses. Optionally, this list can be filtered by the
        ``region-opt-status-contains`` parameter.

        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :param max_results: The total number of items to return in the command’s output.
        :param next_token: A token used to specify where to start paginating.
        :param region_opt_status_contains: A list of Region statuses (Enabling, Enabled, Disabling, Disabled,
        Enabled_by_default) to use to filter the list of Regions for a given
        account.
        :returns: ListRegionsResponse
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("PutAccountName")
    def put_account_name(
        self,
        context: RequestContext,
        account_name: AccountName,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> None:
        """Updates the account name of the specified account. To use this API, IAM
        principals must have the ``account:PutAccountName`` IAM permission.

        :param account_name: The name of the account.
        :param account_id: Specifies the 12 digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("PutAlternateContact")
    def put_alternate_contact(
        self,
        context: RequestContext,
        alternate_contact_type: AlternateContactType,
        email_address: EmailAddress,
        name: Name,
        phone_number: PhoneNumber,
        title: Title,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> None:
        """Modifies the specified alternate contact attached to an Amazon Web
        Services account.

        For complete details about how to use the alternate contact operations,
        see `Access or updating the alternate
        contacts <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html>`__.

        Before you can update the alternate contact information for an Amazon
        Web Services account that is managed by Organizations, you must first
        enable integration between Amazon Web Services Account Management and
        Organizations. For more information, see `Enabling trusted access for
        Amazon Web Services Account
        Management <https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html>`__.

        :param alternate_contact_type: Specifies which alternate contact you want to create or update.
        :param email_address: Specifies an email address for the alternate contact.
        :param name: Specifies a name for the alternate contact.
        :param phone_number: Specifies a phone number for the alternate contact.
        :param title: Specifies a title for the alternate contact.
        :param account_id: Specifies the 12 digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("PutContactInformation")
    def put_contact_information(
        self,
        context: RequestContext,
        contact_information: ContactInformation,
        account_id: AccountId | None = None,
        **kwargs,
    ) -> None:
        """Updates the primary contact information of an Amazon Web Services
        account.

        For complete details about how to use the primary contact operations,
        see `Update the primary and alternate contact
        information <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html>`__.

        :param contact_information: Contains the details of the primary contact information associated with
        an Amazon Web Services account.
        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :raises ValidationException:
        :raises AccessDeniedException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError

    @handler("StartPrimaryEmailUpdate")
    def start_primary_email_update(
        self,
        context: RequestContext,
        account_id: AccountId,
        primary_email: PrimaryEmailAddress,
        **kwargs,
    ) -> StartPrimaryEmailUpdateResponse:
        """Starts the process to update the primary email address for the specified
        account.

        :param account_id: Specifies the 12-digit account ID number of the Amazon Web Services
        account that you want to access or modify with this operation.
        :param primary_email: The new primary email address (also known as the root user email
        address) to use in the specified account.
        :returns: StartPrimaryEmailUpdateResponse
        :raises ResourceNotFoundException:
        :raises AccessDeniedException:
        :raises ValidationException:
        :raises ConflictException:
        :raises TooManyRequestsException:
        :raises InternalServerException:
        """
        raise NotImplementedError
