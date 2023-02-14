from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CustomerInvoice")


@attr.s(auto_attribs=True)
class CustomerInvoice:
    r"""
    Attributes:
        purchase_order_number (str): The purchase order number for this order.
        content (str): The Base64encoded customer invoice.
    """

    purchase_order_number: str
    content: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        content = d.pop("content")

        result = cls(
            purchase_order_number=purchase_order_number,
            content=content,
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
