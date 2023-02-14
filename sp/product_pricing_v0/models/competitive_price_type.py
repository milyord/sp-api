from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.offer_customer_type import OfferCustomerType
from ..models.quantity_discount_type import QuantityDiscountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_type import PriceType


T = TypeVar("T", bound="CompetitivePriceType")


@attr.s(auto_attribs=True)
class CompetitivePriceType:
    r"""
    Attributes:
        competitive_price_id (str): The pricing model for each price that is returned.

            Possible values:

            * 1 - New Buy Box Price.
            * 2 - Used Buy Box Price.
        price (PriceType):
        condition (Union[Unset, str]): Indicates the condition of the item whose pricing information is returned.
            Possible values are: New, Used, Collectible, Refurbished, or Club.
        subcondition (Union[Unset, str]): Indicates the subcondition of the item whose pricing information is returned.
            Possible values are: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty,
            Refurbished, Open Box, or Other.
        offer_type (Union[Unset, OfferCustomerType]):
        quantity_tier (Union[Unset, int]): Indicates at what quantity this price becomes active.
        quantity_discount_type (Union[Unset, QuantityDiscountType]):
        seller_id (Union[Unset, str]): The seller identifier for the offer.
        belongs_to_requester (Union[Unset, bool]):  Indicates whether or not the pricing information is for an offer
            listing that belongs to the requester. The requester is the seller associated with the SellerId that was
            submitted with the request. Possible values are: true and false.
    """

    competitive_price_id: str
    price: "PriceType"
    condition: Union[Unset, str] = UNSET
    subcondition: Union[Unset, str] = UNSET
    offer_type: Union[Unset, OfferCustomerType] = UNSET
    quantity_tier: Union[Unset, int] = UNSET
    quantity_discount_type: Union[Unset, QuantityDiscountType] = UNSET
    seller_id: Union[Unset, str] = UNSET
    belongs_to_requester: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        competitive_price_id = self.competitive_price_id
        price = self.price.to_dict()

        condition = self.condition
        subcondition = self.subcondition
        offer_type: Union[Unset, str] = UNSET
        if not isinstance(self.offer_type, Unset):
            offer_type = self.offer_type.value

        quantity_tier = self.quantity_tier
        quantity_discount_type: Union[Unset, str] = UNSET
        if not isinstance(self.quantity_discount_type, Unset):
            quantity_discount_type = self.quantity_discount_type.value

        seller_id = self.seller_id
        belongs_to_requester = self.belongs_to_requester

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CompetitivePriceId": competitive_price_id,
                "Price": price,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition
        if subcondition is not UNSET:
            field_dict["subcondition"] = subcondition
        if offer_type is not UNSET:
            field_dict["offerType"] = offer_type
        if quantity_tier is not UNSET:
            field_dict["quantityTier"] = quantity_tier
        if quantity_discount_type is not UNSET:
            field_dict["quantityDiscountType"] = quantity_discount_type
        if seller_id is not UNSET:
            field_dict["sellerId"] = seller_id
        if belongs_to_requester is not UNSET:
            field_dict["belongsToRequester"] = belongs_to_requester

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_type import PriceType

        d = src_dict.copy()
        competitive_price_id = d.pop("CompetitivePriceId")

        price = PriceType.from_dict(d.pop("Price"))

        condition = d.pop("condition", UNSET)

        subcondition = d.pop("subcondition", UNSET)

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

        seller_id = d.pop("sellerId", UNSET)

        belongs_to_requester = d.pop("belongsToRequester", UNSET)

        result = cls(
            competitive_price_id=competitive_price_id,
            price=price,
            condition=condition,
            subcondition=subcondition,
            offer_type=offer_type,
            quantity_tier=quantity_tier,
            quantity_discount_type=quantity_discount_type,
            seller_id=seller_id,
            belongs_to_requester=belongs_to_requester,
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
