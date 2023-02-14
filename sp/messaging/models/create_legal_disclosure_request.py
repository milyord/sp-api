from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="CreateLegalDisclosureRequest")


@attr.s(auto_attribs=True)
class CreateLegalDisclosureRequest:
    r"""The request schema for the createLegalDisclosure operation.

    Attributes:
        attachments (Union[Unset, List['Attachment']]): Attachments to include in the message to the buyer. If any text
            is included in the attachment, the text must be written in the buyer's language of preference, which can be
            retrieved from the GetAttributes operation.
    """

    attachments: Union[Unset, List["Attachment"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment import Attachment

        d = src_dict.copy()
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        result = cls(
            attachments=attachments,
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
