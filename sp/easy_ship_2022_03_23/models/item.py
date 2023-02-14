from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""Item identifier and serial number information.

    Attributes:
        order_item_id (Union[Unset, str]): The Amazon-defined order item identifier.
        order_item_serial_numbers (Union[Unset, List[str]]): A list of serial numbers for the items associated with the
            `OrderItemId` value.
    """

    order_item_id: Union[Unset, str] = UNSET
    order_item_serial_numbers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_item_id = self.order_item_id
        order_item_serial_numbers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.order_item_serial_numbers, Unset):
            order_item_serial_numbers = self.order_item_serial_numbers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_item_id is not UNSET:
            field_dict["orderItemId"] = order_item_id
        if order_item_serial_numbers is not UNSET:
            field_dict["orderItemSerialNumbers"] = order_item_serial_numbers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_item_id = d.pop("orderItemId", UNSET)

        order_item_serial_numbers = cast(List[str], d.pop("orderItemSerialNumbers", UNSET))

        result = cls(
            order_item_id=order_item_id,
            order_item_serial_numbers=order_item_serial_numbers,
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
