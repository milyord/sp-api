from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderItemsItem")


@attr.s(auto_attribs=True)
class OrderItemsItem:
    r"""
    Attributes:
        order_item_id (Union[Unset, str]): The unique identifier of the order item.
        quantity (Union[Unset, int]): The quantity for which to update the shipment status.
    """

    order_item_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_item_id = self.order_item_id
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_item_id is not UNSET:
            field_dict["orderItemId"] = order_item_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_item_id = d.pop("orderItemId", UNSET)

        quantity = d.pop("quantity", UNSET)

        result = cls(
            order_item_id=order_item_id,
            quantity=quantity,
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
