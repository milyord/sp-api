from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentAvailability")


@attr.s(auto_attribs=True)
class FulfillmentAvailability:
    r"""Fulfillment availability details for the listings item.

    Attributes:
        fulfillment_channel_code (str): Designates which fulfillment network will be used.
        quantity (Union[Unset, int]): The quantity of the item you are making available for sale.
    """

    fulfillment_channel_code: str
    quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillment_channel_code = self.fulfillment_channel_code
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fulfillmentChannelCode": fulfillment_channel_code,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fulfillment_channel_code = d.pop("fulfillmentChannelCode")

        quantity = d.pop("quantity", UNSET)

        result = cls(
            fulfillment_channel_code=fulfillment_channel_code,
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
