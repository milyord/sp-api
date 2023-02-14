from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.service_upload_document_content_type import ServiceUploadDocumentContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUploadDocument")


@attr.s(auto_attribs=True)
class ServiceUploadDocument:
    r"""Input for to be uploaded document.

    Attributes:
        content_type (ServiceUploadDocumentContentType): The content type of the to-be-uploaded file
        content_length (float): The content length of the to-be-uploaded file
        content_md5 (Union[Unset, str]): An MD5 hash of the content to be submitted to the upload destination. This
            value is used to determine if the data has been corrupted or tampered with during transit.
    """

    content_type: ServiceUploadDocumentContentType
    content_length: float
    content_md5: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type = self.content_type.value

        content_length = self.content_length
        content_md5 = self.content_md5

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentType": content_type,
                "contentLength": content_length,
            }
        )
        if content_md5 is not UNSET:
            field_dict["contentMD5"] = content_md5

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = ServiceUploadDocumentContentType(d.pop("contentType"))

        content_length = d.pop("contentLength")

        content_md5 = d.pop("contentMD5", UNSET)

        result = cls(
            content_type=content_type,
            content_length=content_length,
            content_md5=content_md5,
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
