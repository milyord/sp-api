from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.condition import Condition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_identifier import OfferIdentifier
    from ..models.price import Price


T = TypeVar("T", bound="FeaturedOffer")


@attr.s(auto_attribs=True)
class FeaturedOffer:
    r"""
    Attributes:
        offer_identifier (OfferIdentifier): Identifies an offer from a particular seller on an ASIN.
        condition (Union[Unset, Condition]): The condition of the item.
        price (Union[Unset, Price]):
    """

    offer_identifier: "OfferIdentifier"
    condition: Union[Unset, Condition] = UNSET
    price: Union[Unset, "Price"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offer_identifier = self.offer_identifier.to_dict()

        condition: Union[Unset, str] = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.value

        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offerIdentifier": offer_identifier,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offer_identifier import OfferIdentifier
        from ..models.price import Price

        d = src_dict.copy()
        offer_identifier = OfferIdentifier.from_dict(d.pop("offerIdentifier"))

        _condition = d.pop("condition", UNSET)
        condition: Union[Unset, Condition]
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = Condition(_condition)

        _price = d.pop("price", UNSET)
        price: Union[Unset, Price]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        result = cls(
            offer_identifier=offer_identifier,
            condition=condition,
            price=price,
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
