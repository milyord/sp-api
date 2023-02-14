from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.packing_slip_content_type import PackingSlipContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PackingSlip")


@attr.s(auto_attribs=True)
class PackingSlip:
    r"""Packing slip information.

    Attributes:
        purchase_order_number (str): Purchase order number of the shipment that the packing slip is for.
        content (str): A Base64encoded string of the packing slip PDF.
        content_type (Union[Unset, PackingSlipContentType]): The format of the file such as PDF, JPEG etc.
    """

    purchase_order_number: str
    content: str
    content_type: Union[Unset, PackingSlipContentType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        content = self.content
        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "content": content,
            }
        )
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        content = d.pop("content")

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, PackingSlipContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = PackingSlipContentType(_content_type)

        result = cls(
            purchase_order_number=purchase_order_number,
            content=content,
            content_type=content_type,
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
