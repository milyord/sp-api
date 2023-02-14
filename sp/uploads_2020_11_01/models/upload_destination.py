from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_destination_headers import UploadDestinationHeaders


T = TypeVar("T", bound="UploadDestination")


@attr.s(auto_attribs=True)
class UploadDestination:
    r"""Information about an upload destination.

    Attributes:
        upload_destination_id (Union[Unset, str]): The unique identifier for the upload destination.
        url (Union[Unset, str]): The URL for the upload destination.
        headers (Union[Unset, UploadDestinationHeaders]): The headers to include in the upload request.
    """

    upload_destination_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    headers: Union[Unset, "UploadDestinationHeaders"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_destination_id = self.upload_destination_id
        url = self.url
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_destination_id is not UNSET:
            field_dict["uploadDestinationId"] = upload_destination_id
        if url is not UNSET:
            field_dict["url"] = url
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.upload_destination_headers import UploadDestinationHeaders

        d = src_dict.copy()
        upload_destination_id = d.pop("uploadDestinationId", UNSET)

        url = d.pop("url", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, UploadDestinationHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = UploadDestinationHeaders.from_dict(_headers)

        result = cls(
            upload_destination_id=upload_destination_id,
            url=url,
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
