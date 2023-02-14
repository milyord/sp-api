from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.quantity_discount_type import QuantityDiscountType

if TYPE_CHECKING:
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="QuantityDiscountPriceType")


@attr.s(auto_attribs=True)
class QuantityDiscountPriceType:
    r"""Contains pricing information that includes special pricing when buying in bulk.

    Attributes:
        quantity_tier (int): Indicates at what quantity this price becomes active.
        quantity_discount_type (QuantityDiscountType):
        listing_price (MoneyType):
    """

    quantity_tier: int
    quantity_discount_type: QuantityDiscountType
    listing_price: "MoneyType"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity_tier = self.quantity_tier
        quantity_discount_type = self.quantity_discount_type.value

        listing_price = self.listing_price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantityTier": quantity_tier,
                "quantityDiscountType": quantity_discount_type,
                "listingPrice": listing_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        quantity_tier = d.pop("quantityTier")

        quantity_discount_type = QuantityDiscountType(d.pop("quantityDiscountType"))

        listing_price = MoneyType.from_dict(d.pop("listingPrice"))

        result = cls(
            quantity_tier=quantity_tier,
            quantity_discount_type=quantity_discount_type,
            listing_price=listing_price,
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
