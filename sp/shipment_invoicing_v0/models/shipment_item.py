from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="ShipmentItem")


@attr.s(auto_attribs=True)
class ShipmentItem:
    r"""The shipment item information required by a seller to issue a shipment invoice.

    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        seller_sku (Union[Unset, str]): The seller SKU of the item.
        order_item_id (Union[Unset, str]): The Amazon-defined identifier for the order item.
        title (Union[Unset, str]): The name of the item.
        quantity_ordered (Union[Unset, float]): The number of items ordered.
        item_price (Union[Unset, Money]): The currency type and amount.
        shipping_price (Union[Unset, Money]): The currency type and amount.
        gift_wrap_price (Union[Unset, Money]): The currency type and amount.
        shipping_discount (Union[Unset, Money]): The currency type and amount.
        promotion_discount (Union[Unset, Money]): The currency type and amount.
        serial_numbers (Union[Unset, List[str]]): The list of serial numbers.
    """

    asin: Union[Unset, str] = UNSET
    seller_sku: Union[Unset, str] = UNSET
    order_item_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    quantity_ordered: Union[Unset, float] = UNSET
    item_price: Union[Unset, "Money"] = UNSET
    shipping_price: Union[Unset, "Money"] = UNSET
    gift_wrap_price: Union[Unset, "Money"] = UNSET
    shipping_discount: Union[Unset, "Money"] = UNSET
    promotion_discount: Union[Unset, "Money"] = UNSET
    serial_numbers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        seller_sku = self.seller_sku
        order_item_id = self.order_item_id
        title = self.title
        quantity_ordered = self.quantity_ordered
        item_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_price, Unset):
            item_price = self.item_price.to_dict()

        shipping_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_price, Unset):
            shipping_price = self.shipping_price.to_dict()

        gift_wrap_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_wrap_price, Unset):
            gift_wrap_price = self.gift_wrap_price.to_dict()

        shipping_discount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_discount, Unset):
            shipping_discount = self.shipping_discount.to_dict()

        promotion_discount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.promotion_discount, Unset):
            promotion_discount = self.promotion_discount.to_dict()

        serial_numbers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.serial_numbers, Unset):
            serial_numbers = self.serial_numbers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if order_item_id is not UNSET:
            field_dict["OrderItemId"] = order_item_id
        if title is not UNSET:
            field_dict["Title"] = title
        if quantity_ordered is not UNSET:
            field_dict["QuantityOrdered"] = quantity_ordered
        if item_price is not UNSET:
            field_dict["ItemPrice"] = item_price
        if shipping_price is not UNSET:
            field_dict["ShippingPrice"] = shipping_price
        if gift_wrap_price is not UNSET:
            field_dict["GiftWrapPrice"] = gift_wrap_price
        if shipping_discount is not UNSET:
            field_dict["ShippingDiscount"] = shipping_discount
        if promotion_discount is not UNSET:
            field_dict["PromotionDiscount"] = promotion_discount
        if serial_numbers is not UNSET:
            field_dict["SerialNumbers"] = serial_numbers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        asin = d.pop("ASIN", UNSET)

        seller_sku = d.pop("SellerSKU", UNSET)

        order_item_id = d.pop("OrderItemId", UNSET)

        title = d.pop("Title", UNSET)

        quantity_ordered = d.pop("QuantityOrdered", UNSET)

        _item_price = d.pop("ItemPrice", UNSET)
        item_price: Union[Unset, Money]
        if isinstance(_item_price, Unset):
            item_price = UNSET
        else:
            item_price = Money.from_dict(_item_price)

        _shipping_price = d.pop("ShippingPrice", UNSET)
        shipping_price: Union[Unset, Money]
        if isinstance(_shipping_price, Unset):
            shipping_price = UNSET
        else:
            shipping_price = Money.from_dict(_shipping_price)

        _gift_wrap_price = d.pop("GiftWrapPrice", UNSET)
        gift_wrap_price: Union[Unset, Money]
        if isinstance(_gift_wrap_price, Unset):
            gift_wrap_price = UNSET
        else:
            gift_wrap_price = Money.from_dict(_gift_wrap_price)

        _shipping_discount = d.pop("ShippingDiscount", UNSET)
        shipping_discount: Union[Unset, Money]
        if isinstance(_shipping_discount, Unset):
            shipping_discount = UNSET
        else:
            shipping_discount = Money.from_dict(_shipping_discount)

        _promotion_discount = d.pop("PromotionDiscount", UNSET)
        promotion_discount: Union[Unset, Money]
        if isinstance(_promotion_discount, Unset):
            promotion_discount = UNSET
        else:
            promotion_discount = Money.from_dict(_promotion_discount)

        serial_numbers = cast(List[str], d.pop("SerialNumbers", UNSET))

        result = cls(
            asin=asin,
            seller_sku=seller_sku,
            order_item_id=order_item_id,
            title=title,
            quantity_ordered=quantity_ordered,
            item_price=item_price,
            shipping_price=shipping_price,
            gift_wrap_price=gift_wrap_price,
            shipping_discount=shipping_discount,
            promotion_discount=promotion_discount,
            serial_numbers=serial_numbers,
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
