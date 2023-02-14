from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encryption_details import EncryptionDetails
    from ..models.service_document_upload_destination_headers import ServiceDocumentUploadDestinationHeaders


T = TypeVar("T", bound="ServiceDocumentUploadDestination")


@attr.s(auto_attribs=True)
class ServiceDocumentUploadDestination:
    r"""Information about an upload destination.

    Attributes:
        upload_destination_id (str): The unique identifier to be used by APIs that reference the upload destination.
        url (str): The URL to which to upload the file.
        encryption_details (EncryptionDetails): Encryption details for required client-side encryption and decryption of
            document contents.
        headers (Union[Unset, ServiceDocumentUploadDestinationHeaders]): The headers to include in the upload request.
    """

    upload_destination_id: str
    url: str
    encryption_details: "EncryptionDetails"
    headers: Union[Unset, "ServiceDocumentUploadDestinationHeaders"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_destination_id = self.upload_destination_id
        url = self.url
        encryption_details = self.encryption_details.to_dict()

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadDestinationId": upload_destination_id,
                "url": url,
                "encryptionDetails": encryption_details,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.encryption_details import EncryptionDetails
        from ..models.service_document_upload_destination_headers import ServiceDocumentUploadDestinationHeaders

        d = src_dict.copy()
        upload_destination_id = d.pop("uploadDestinationId")

        url = d.pop("url")

        encryption_details = EncryptionDetails.from_dict(d.pop("encryptionDetails"))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, ServiceDocumentUploadDestinationHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ServiceDocumentUploadDestinationHeaders.from_dict(_headers)

        result = cls(
            upload_destination_id=upload_destination_id,
            url=url,
            encryption_details=encryption_details,
            headers=headers,
        )

        result.additional_properties = d
        return result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
