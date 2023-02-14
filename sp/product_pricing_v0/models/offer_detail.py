from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.offer_customer_type import OfferCustomerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.detailed_shipping_time_type import DetailedShippingTimeType
    from ..models.money_type import MoneyType
    from ..models.points import Points
    from ..models.prime_information_type import PrimeInformationType
    from ..models.quantity_discount_price_type import QuantityDiscountPriceType
    from ..models.seller_feedback_type import SellerFeedbackType
    from ..models.ships_from_type import ShipsFromType


T = TypeVar("T", bound="OfferDetail")


@attr.s(auto_attribs=True)
class OfferDetail:
    r"""
    Attributes:
        sub_condition (str): The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable,
            Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
        shipping_time (DetailedShippingTimeType): The time range in which an item will likely be shipped once an order
            has been placed.
        listing_price (MoneyType):
        shipping (MoneyType):
        is_fulfilled_by_amazon (bool): When true, the offer is fulfilled by Amazon.
        my_offer (Union[Unset, bool]): When true, this is the seller's offer.
        offer_type (Union[Unset, OfferCustomerType]):
        seller_id (Union[Unset, str]): The seller identifier for the offer.
        condition_notes (Union[Unset, str]): Information about the condition of the item.
        seller_feedback_rating (Union[Unset, SellerFeedbackType]): Information about the seller's feedback, including
            the percentage of positive feedback, and the total number of ratings received.
        quantity_discount_prices (Union[Unset, List['QuantityDiscountPriceType']]):
        points (Union[Unset, Points]):
        ships_from (Union[Unset, ShipsFromType]): The state and country from where the item is shipped.
        prime_information (Union[Unset, PrimeInformationType]): Amazon Prime information.
        is_buy_box_winner (Union[Unset, bool]): When true, the offer is currently in the Buy Box. There can be up to two
            Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.
        is_featured_merchant (Union[Unset, bool]): When true, the seller of the item is eligible to win the Buy Box.
    """

    sub_condition: str
    shipping_time: "DetailedShippingTimeType"
    listing_price: "MoneyType"
    shipping: "MoneyType"
    is_fulfilled_by_amazon: bool
    my_offer: Union[Unset, bool] = UNSET
    offer_type: Union[Unset, OfferCustomerType] = UNSET
    seller_id: Union[Unset, str] = UNSET
    condition_notes: Union[Unset, str] = UNSET
    seller_feedback_rating: Union[Unset, "SellerFeedbackType"] = UNSET
    quantity_discount_prices: Union[Unset, List["QuantityDiscountPriceType"]] = UNSET
    points: Union[Unset, "Points"] = UNSET
    ships_from: Union[Unset, "ShipsFromType"] = UNSET
    prime_information: Union[Unset, "PrimeInformationType"] = UNSET
    is_buy_box_winner: Union[Unset, bool] = UNSET
    is_featured_merchant: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_condition = self.sub_condition
        shipping_time = self.shipping_time.to_dict()

        listing_price = self.listing_price.to_dict()

        shipping = self.shipping.to_dict()

        is_fulfilled_by_amazon = self.is_fulfilled_by_amazon
        my_offer = self.my_offer
        offer_type: Union[Unset, str] = UNSET
        if not isinstance(self.offer_type, Unset):
            offer_type = self.offer_type.value

        seller_id = self.seller_id
        condition_notes = self.condition_notes
        seller_feedback_rating: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_feedback_rating, Unset):
            seller_feedback_rating = self.seller_feedback_rating.to_dict()

        quantity_discount_prices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantity_discount_prices, Unset):
            quantity_discount_prices = []
            for quantity_discount_prices_item_data in self.quantity_discount_prices:
                quantity_discount_prices_item = quantity_discount_prices_item_data.to_dict()

                quantity_discount_prices.append(quantity_discount_prices_item)

        points: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        ships_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ships_from, Unset):
            ships_from = self.ships_from.to_dict()

        prime_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prime_information, Unset):
            prime_information = self.prime_information.to_dict()

        is_buy_box_winner = self.is_buy_box_winner
        is_featured_merchant = self.is_featured_merchant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SubCondition": sub_condition,
                "ShippingTime": shipping_time,
                "ListingPrice": listing_price,
                "Shipping": shipping,
                "IsFulfilledByAmazon": is_fulfilled_by_amazon,
            }
        )
        if my_offer is not UNSET:
            field_dict["MyOffer"] = my_offer
        if offer_type is not UNSET:
            field_dict["offerType"] = offer_type
        if seller_id is not UNSET:
            field_dict["SellerId"] = seller_id
        if condition_notes is not UNSET:
            field_dict["ConditionNotes"] = condition_notes
        if seller_feedback_rating is not UNSET:
            field_dict["SellerFeedbackRating"] = seller_feedback_rating
        if quantity_discount_prices is not UNSET:
            field_dict["quantityDiscountPrices"] = quantity_discount_prices
        if points is not UNSET:
            field_dict["Points"] = points
        if ships_from is not UNSET:
            field_dict["ShipsFrom"] = ships_from
        if prime_information is not UNSET:
            field_dict["PrimeInformation"] = prime_information
        if is_buy_box_winner is not UNSET:
            field_dict["IsBuyBoxWinner"] = is_buy_box_winner
        if is_featured_merchant is not UNSET:
            field_dict["IsFeaturedMerchant"] = is_featured_merchant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_shipping_time_type import DetailedShippingTimeType
        from ..models.money_type import MoneyType
        from ..models.points import Points
        from ..models.prime_information_type import PrimeInformationType
        from ..models.quantity_discount_price_type import QuantityDiscountPriceType
        from ..models.seller_feedback_type import SellerFeedbackType
        from ..models.ships_from_type import ShipsFromType

        d = src_dict.copy()
        sub_condition = d.pop("SubCondition")

        shipping_time = DetailedShippingTimeType.from_dict(d.pop("ShippingTime"))

        listing_price = MoneyType.from_dict(d.pop("ListingPrice"))

        shipping = MoneyType.from_dict(d.pop("Shipping"))

        is_fulfilled_by_amazon = d.pop("IsFulfilledByAmazon")

        my_offer = d.pop("MyOffer", UNSET)

        _offer_type = d.pop("offerType", UNSET)
        offer_type: Union[Unset, OfferCustomerType]
        if isinstance(_offer_type, Unset):
            offer_type = UNSET
        else:
            offer_type = OfferCustomerType(_offer_type)

        seller_id = d.pop("SellerId", UNSET)

        condition_notes = d.pop("ConditionNotes", UNSET)

        _seller_feedback_rating = d.pop("SellerFeedbackRating", UNSET)
        seller_feedback_rating: Union[Unset, SellerFeedbackType]
        if isinstance(_seller_feedback_rating, Unset):
            seller_feedback_rating = UNSET
        else:
            seller_feedback_rating = SellerFeedbackType.from_dict(_seller_feedback_rating)

        quantity_discount_prices = []
        _quantity_discount_prices = d.pop("quantityDiscountPrices", UNSET)
        for quantity_discount_prices_item_data in _quantity_discount_prices or []:
            quantity_discount_prices_item = QuantityDiscountPriceType.from_dict(quantity_discount_prices_item_data)

            quantity_discount_prices.append(quantity_discount_prices_item)

        _points = d.pop("Points", UNSET)
        points: Union[Unset, Points]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = Points.from_dict(_points)

        _ships_from = d.pop("ShipsFrom", UNSET)
        ships_from: Union[Unset, ShipsFromType]
        if isinstance(_ships_from, Unset):
            ships_from = UNSET
        else:
            ships_from = ShipsFromType.from_dict(_ships_from)

        _prime_information = d.pop("PrimeInformation", UNSET)
        prime_information: Union[Unset, PrimeInformationType]
        if isinstance(_prime_information, Unset):
            prime_information = UNSET
        else:
            prime_information = PrimeInformationType.from_dict(_prime_information)

        is_buy_box_winner = d.pop("IsBuyBoxWinner", UNSET)

        is_featured_merchant = d.pop("IsFeaturedMerchant", UNSET)

        result = cls(
            sub_condition=sub_condition,
            shipping_time=shipping_time,
            listing_price=listing_price,
            shipping=shipping,
            is_fulfilled_by_amazon=is_fulfilled_by_amazon,
            my_offer=my_offer,
            offer_type=offer_type,
            seller_id=seller_id,
            condition_notes=condition_notes,
            seller_feedback_rating=seller_feedback_rating,
            quantity_discount_prices=quantity_discount_prices,
            points=points,
            ships_from=ships_from,
            prime_information=prime_information,
            is_buy_box_winner=is_buy_box_winner,
            is_featured_merchant=is_featured_merchant,
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
