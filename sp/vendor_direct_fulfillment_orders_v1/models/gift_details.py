from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftDetails")


@attr.s(auto_attribs=True)
class GiftDetails:
    r"""Gift details for the item.

    Attributes:
        gift_message (Union[Unset, str]): Gift message to be printed in shipment.
        gift_wrap_id (Union[Unset, str]): Gift wrap identifier for the gift wrapping, if any.
    """

    gift_message: Union[Unset, str] = UNSET
    gift_wrap_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gift_message = self.gift_message
        gift_wrap_id = self.gift_wrap_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gift_message is not UNSET:
            field_dict["giftMessage"] = gift_message
        if gift_wrap_id is not UNSET:
            field_dict["giftWrapId"] = gift_wrap_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gift_message = d.pop("giftMessage", UNSET)

        gift_wrap_id = d.pop("giftWrapId", UNSET)

        result = cls(
            gift_message=gift_message,
            gift_wrap_id=gift_wrap_id,
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
