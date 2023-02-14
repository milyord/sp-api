from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentDocument")


@attr.s(auto_attribs=True)
class FulfillmentDocument:
    r"""Document that captured during service appointment fulfillment that portrays proof of completion

    Attributes:
        upload_destination_id (Union[Unset, str]): The identifier of the upload destination. Get this value by calling
            the `createServiceDocumentUploadDestination` operation of the Services API.
        content_sha_256 (Union[Unset, str]): Sha256 hash of the file content. This value is used to determine if the
            file has been corrupted or tampered with during transit.
    """

    upload_destination_id: Union[Unset, str] = UNSET
    content_sha_256: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_destination_id = self.upload_destination_id
        content_sha_256 = self.content_sha_256

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_destination_id is not UNSET:
            field_dict["uploadDestinationId"] = upload_destination_id
        if content_sha_256 is not UNSET:
            field_dict["contentSha256"] = content_sha_256

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upload_destination_id = d.pop("uploadDestinationId", UNSET)

        content_sha_256 = d.pop("contentSha256", UNSET)

        result = cls(
            upload_destination_id=upload_destination_id,
            content_sha_256=content_sha_256,
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
