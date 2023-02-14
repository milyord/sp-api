from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fulfillment_channel_type import FulfillmentChannelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferCountType")


@attr.s(auto_attribs=True)
class OfferCountType:
    r"""The total number of offers for the specified condition and fulfillment channel.

    Attributes:
        condition (Union[Unset, str]): Indicates the condition of the item. For example: New, Used, Collectible,
            Refurbished, or Club.
        fulfillment_channel (Union[Unset, FulfillmentChannelType]): Indicates whether the item is fulfilled by Amazon or
            by the seller (merchant).
        offer_count (Union[Unset, int]): The number of offers in a fulfillment channel that meet a specific condition.
    """

    condition: Union[Unset, str] = UNSET
    fulfillment_channel: Union[Unset, FulfillmentChannelType] = UNSET
    offer_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition = self.condition
        fulfillment_channel: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_channel, Unset):
            fulfillment_channel = self.fulfillment_channel.value

        offer_count = self.offer_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition is not UNSET:
            field_dict["condition"] = condition
        if fulfillment_channel is not UNSET:
            field_dict["fulfillmentChannel"] = fulfillment_channel
        if offer_count is not UNSET:
            field_dict["OfferCount"] = offer_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        condition = d.pop("condition", UNSET)

        _fulfillment_channel = d.pop("fulfillmentChannel", UNSET)
        fulfillment_channel: Union[Unset, FulfillmentChannelType]
        if isinstance(_fulfillment_channel, Unset):
            fulfillment_channel = UNSET
        else:
            fulfillment_channel = FulfillmentChannelType(_fulfillment_channel)

        offer_count = d.pop("OfferCount", UNSET)

        result = cls(
            condition=condition,
            fulfillment_channel=fulfillment_channel,
            offer_count=offer_count,
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
