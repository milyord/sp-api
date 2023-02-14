from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.offer_customer_type import OfferCustomerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money_type import MoneyType
    from ..models.price_type import PriceType
    from ..models.quantity_discount_price_type import QuantityDiscountPriceType


T = TypeVar("T", bound="OfferType")


@attr.s(auto_attribs=True)
class OfferType:
    r"""
    Attributes:
        buying_price (PriceType):
        regular_price (MoneyType):
        fulfillment_channel (str): The fulfillment channel for the offer listing. Possible values:

            * Amazon - Fulfilled by Amazon.
            * Merchant - Fulfilled by the seller.
        item_condition (str): The item condition for the offer listing. Possible values: New, Used, Collectible,
            Refurbished, or Club.
        item_sub_condition (str): The item subcondition for the offer listing. Possible values: New, Mint, Very Good,
            Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.
        seller_sku (str): The seller stock keeping unit (SKU) of the item.
        offer_type (Union[Unset, OfferCustomerType]):
        business_price (Union[Unset, MoneyType]):
        quantity_discount_prices (Union[Unset, List['QuantityDiscountPriceType']]):
    """

    buying_price: "PriceType"
    regular_price: "MoneyType"
    fulfillment_channel: str
    item_condition: str
    item_sub_condition: str
    seller_sku: str
    offer_type: Union[Unset, OfferCustomerType] = UNSET
    business_price: Union[Unset, "MoneyType"] = UNSET
    quantity_discount_prices: Union[Unset, List["QuantityDiscountPriceType"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buying_price = self.buying_price.to_dict()

        regular_price = self.regular_price.to_dict()

        fulfillment_channel = self.fulfillment_channel
        item_condition = self.item_condition
        item_sub_condition = self.item_sub_condition
        seller_sku = self.seller_sku
        offer_type: Union[Unset, str] = UNSET
        if not isinstance(self.offer_type, Unset):
            offer_type = self.offer_type.value

        business_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business_price, Unset):
            business_price = self.business_price.to_dict()

        quantity_discount_prices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantity_discount_prices, Unset):
            quantity_discount_prices = []
            for quantity_discount_prices_item_data in self.quantity_discount_prices:
                quantity_discount_prices_item = quantity_discount_prices_item_data.to_dict()

                quantity_discount_prices.append(quantity_discount_prices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "BuyingPrice": buying_price,
                "RegularPrice": regular_price,
                "FulfillmentChannel": fulfillment_channel,
                "ItemCondition": item_condition,
                "ItemSubCondition": item_sub_condition,
                "SellerSKU": seller_sku,
            }
        )
        if offer_type is not UNSET:
            field_dict["offerType"] = offer_type
        if business_price is not UNSET:
            field_dict["businessPrice"] = business_price
        if quantity_discount_prices is not UNSET:
            field_dict["quantityDiscountPrices"] = quantity_discount_prices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType
        from ..models.price_type import PriceType
        from ..models.quantity_discount_price_type import QuantityDiscountPriceType

        d = src_dict.copy()
        buying_price = PriceType.from_dict(d.pop("BuyingPrice"))

        regular_price = MoneyType.from_dict(d.pop("RegularPrice"))

        fulfillment_channel = d.pop("FulfillmentChannel")

        item_condition = d.pop("ItemCondition")

        item_sub_condition = d.pop("ItemSubCondition")

        seller_sku = d.pop("SellerSKU")

        _offer_type = d.pop("offerType", UNSET)
        offer_type: Union[Unset, OfferCustomerType]
        if isinstance(_offer_type, Unset):
            offer_type = UNSET
        else:
            offer_type = OfferCustomerType(_offer_type)

        _business_price = d.pop("businessPrice", UNSET)
        business_price: Union[Unset, MoneyType]
        if isinstance(_business_price, Unset):
            business_price = UNSET
        else:
            business_price = MoneyType.from_dict(_business_price)

        quantity_discount_prices = []
        _quantity_discount_prices = d.pop("quantityDiscountPrices", UNSET)
        for quantity_discount_prices_item_data in _quantity_discount_prices or []:
            quantity_discount_prices_item = QuantityDiscountPriceType.from_dict(quantity_discount_prices_item_data)

            quantity_discount_prices.append(quantity_discount_prices_item)

        result = cls(
            buying_price=buying_price,
            regular_price=regular_price,
            fulfillment_channel=fulfillment_channel,
            item_condition=item_condition,
            item_sub_condition=item_sub_condition,
            seller_sku=seller_sku,
            offer_type=offer_type,
            business_price=business_price,
            quantity_discount_prices=quantity_discount_prices,
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
