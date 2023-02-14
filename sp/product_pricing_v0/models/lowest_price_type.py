from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.offer_customer_type import OfferCustomerType
from ..models.quantity_discount_type import QuantityDiscountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money_type import MoneyType
    from ..models.points import Points


T = TypeVar("T", bound="LowestPriceType")


@attr.s(auto_attribs=True)
class LowestPriceType:
    r"""
    Attributes:
        condition (str): Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.
        fulfillment_channel (str): Indicates whether the item is fulfilled by Amazon or by the seller.
        landed_price (MoneyType):
        listing_price (MoneyType):
        shipping (MoneyType):
        offer_type (Union[Unset, OfferCustomerType]):
        quantity_tier (Union[Unset, int]): Indicates at what quantity this price becomes active.
        quantity_discount_type (Union[Unset, QuantityDiscountType]):
        points (Union[Unset, Points]):
    """

    condition: str
    fulfillment_channel: str
    landed_price: "MoneyType"
    listing_price: "MoneyType"
    shipping: "MoneyType"
    offer_type: Union[Unset, OfferCustomerType] = UNSET
    quantity_tier: Union[Unset, int] = UNSET
    quantity_discount_type: Union[Unset, QuantityDiscountType] = UNSET
    points: Union[Unset, "Points"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition = self.condition
        fulfillment_channel = self.fulfillment_channel
        landed_price = self.landed_price.to_dict()

        listing_price = self.listing_price.to_dict()

        shipping = self.shipping.to_dict()

        offer_type: Union[Unset, str] = UNSET
        if not isinstance(self.offer_type, Unset):
            offer_type = self.offer_type.value

        quantity_tier = self.quantity_tier
        quantity_discount_type: Union[Unset, str] = UNSET
        if not isinstance(self.quantity_discount_type, Unset):
            quantity_discount_type = self.quantity_discount_type.value

        points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition": condition,
                "fulfillmentChannel": fulfillment_channel,
                "LandedPrice": landed_price,
                "ListingPrice": listing_price,
                "Shipping": shipping,
            }
        )
        if offer_type is not UNSET:
            field_dict["offerType"] = offer_type
        if quantity_tier is not UNSET:
            field_dict["quantityTier"] = quantity_tier
        if quantity_discount_type is not UNSET:
            field_dict["quantityDiscountType"] = quantity_discount_type
        if points is not UNSET:
            field_dict["Points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType
        from ..models.points import Points

        d = src_dict.copy()
        condition = d.pop("condition")

        fulfillment_channel = d.pop("fulfillmentChannel")

        landed_price = MoneyType.from_dict(d.pop("LandedPrice"))

        listing_price = MoneyType.from_dict(d.pop("ListingPrice"))

        shipping = MoneyType.from_dict(d.pop("Shipping"))

        _offer_type = d.pop("offerType", UNSET)
        offer_type: Union[Unset, OfferCustomerType]
        if isinstance(_offer_type, Unset):
            offer_type = UNSET
        else:
            offer_type = OfferCustomerType(_offer_type)

        quantity_tier = d.pop("quantityTier", UNSET)

        _quantity_discount_type = d.pop("quantityDiscountType", UNSET)
        quantity_discount_type: Union[Unset, QuantityDiscountType]
        if isinstance(_quantity_discount_type, Unset):
            quantity_discount_type = UNSET
        else:
            quantity_discount_type = QuantityDiscountType(_quantity_discount_type)

        _points = d.pop("Points", UNSET)
        points: Union[Unset, Points]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = Points.from_dict(_points)

        result = cls(
            condition=condition,
            fulfillment_channel=fulfillment_channel,
            landed_price=landed_price,
            listing_price=listing_price,
            shipping=shipping,
            offer_type=offer_type,
            quantity_tier=quantity_tier,
            quantity_discount_type=quantity_discount_type,
            points=points,
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
