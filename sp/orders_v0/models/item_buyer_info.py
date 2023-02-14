from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buyer_customized_info_detail import BuyerCustomizedInfoDetail
    from ..models.money import Money


T = TypeVar("T", bound="ItemBuyerInfo")


@attr.s(auto_attribs=True)
class ItemBuyerInfo:
    r"""A single item's buyer information.

    Attributes:
        buyer_customized_info (Union[Unset, BuyerCustomizedInfoDetail]): Buyer information for custom orders from the
            Amazon Custom program.
        gift_wrap_price (Union[Unset, Money]): The monetary value of the order.
        gift_wrap_tax (Union[Unset, Money]): The monetary value of the order.
        gift_message_text (Union[Unset, str]): A gift message provided by the buyer.
        gift_wrap_level (Union[Unset, str]): The gift wrap level specified by the buyer.
    """

    buyer_customized_info: Union[Unset, "BuyerCustomizedInfoDetail"] = UNSET
    gift_wrap_price: Union[Unset, "Money"] = UNSET
    gift_wrap_tax: Union[Unset, "Money"] = UNSET
    gift_message_text: Union[Unset, str] = UNSET
    gift_wrap_level: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buyer_customized_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buyer_customized_info, Unset):
            buyer_customized_info = self.buyer_customized_info.to_dict()

        gift_wrap_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_wrap_price, Unset):
            gift_wrap_price = self.gift_wrap_price.to_dict()

        gift_wrap_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_wrap_tax, Unset):
            gift_wrap_tax = self.gift_wrap_tax.to_dict()

        gift_message_text = self.gift_message_text
        gift_wrap_level = self.gift_wrap_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buyer_customized_info is not UNSET:
            field_dict["BuyerCustomizedInfo"] = buyer_customized_info
        if gift_wrap_price is not UNSET:
            field_dict["GiftWrapPrice"] = gift_wrap_price
        if gift_wrap_tax is not UNSET:
            field_dict["GiftWrapTax"] = gift_wrap_tax
        if gift_message_text is not UNSET:
            field_dict["GiftMessageText"] = gift_message_text
        if gift_wrap_level is not UNSET:
            field_dict["GiftWrapLevel"] = gift_wrap_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buyer_customized_info_detail import BuyerCustomizedInfoDetail
        from ..models.money import Money

        d = src_dict.copy()
        _buyer_customized_info = d.pop("BuyerCustomizedInfo", UNSET)
        buyer_customized_info: Union[Unset, BuyerCustomizedInfoDetail]
        if isinstance(_buyer_customized_info, Unset):
            buyer_customized_info = UNSET
        else:
            buyer_customized_info = BuyerCustomizedInfoDetail.from_dict(_buyer_customized_info)

        _gift_wrap_price = d.pop("GiftWrapPrice", UNSET)
        gift_wrap_price: Union[Unset, Money]
        if isinstance(_gift_wrap_price, Unset):
            gift_wrap_price = UNSET
        else:
            gift_wrap_price = Money.from_dict(_gift_wrap_price)

        _gift_wrap_tax = d.pop("GiftWrapTax", UNSET)
        gift_wrap_tax: Union[Unset, Money]
        if isinstance(_gift_wrap_tax, Unset):
            gift_wrap_tax = UNSET
        else:
            gift_wrap_tax = Money.from_dict(_gift_wrap_tax)

        gift_message_text = d.pop("GiftMessageText", UNSET)

        gift_wrap_level = d.pop("GiftWrapLevel", UNSET)

        result = cls(
            buyer_customized_info=buyer_customized_info,
            gift_wrap_price=gift_wrap_price,
            gift_wrap_tax=gift_wrap_tax,
            gift_message_text=gift_message_text,
            gift_wrap_level=gift_wrap_level,
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
