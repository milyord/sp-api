from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="UpdateFulfillmentOrderItem")


@attr.s(auto_attribs=True)
class UpdateFulfillmentOrderItem:
    r"""Item information for updating a fulfillment order.

    Attributes:
        seller_fulfillment_order_item_id (str): Identifies the fulfillment order item to update. Created with a previous
            call to the createFulfillmentOrder operation.
        quantity (int): The item quantity.
        seller_sku (Union[Unset, str]): The seller SKU of the item.
        gift_message (Union[Unset, str]): A message to the gift recipient, if applicable.
        displayable_comment (Union[Unset, str]): Item-specific text that displays in recipient-facing materials such as
            the outbound shipment packing slip.
        fulfillment_network_sku (Union[Unset, str]): Amazon's fulfillment network SKU of the item.
        order_item_disposition (Union[Unset, str]): Indicates whether the item is sellable or unsellable.
        per_unit_declared_value (Union[Unset, Money]): An amount of money, including units in the form of currency.
        per_unit_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
        per_unit_tax (Union[Unset, Money]): An amount of money, including units in the form of currency.
    """

    seller_fulfillment_order_item_id: str
    quantity: int
    seller_sku: Union[Unset, str] = UNSET
    gift_message: Union[Unset, str] = UNSET
    displayable_comment: Union[Unset, str] = UNSET
    fulfillment_network_sku: Union[Unset, str] = UNSET
    order_item_disposition: Union[Unset, str] = UNSET
    per_unit_declared_value: Union[Unset, "Money"] = UNSET
    per_unit_price: Union[Unset, "Money"] = UNSET
    per_unit_tax: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        quantity = self.quantity
        seller_sku = self.seller_sku
        gift_message = self.gift_message
        displayable_comment = self.displayable_comment
        fulfillment_network_sku = self.fulfillment_network_sku
        order_item_disposition = self.order_item_disposition
        per_unit_declared_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_declared_value, Unset):
            per_unit_declared_value = self.per_unit_declared_value.to_dict()

        per_unit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_price, Unset):
            per_unit_price = self.per_unit_price.to_dict()

        per_unit_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_tax, Unset):
            per_unit_tax = self.per_unit_tax.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
                "quantity": quantity,
            }
        )
        if seller_sku is not UNSET:
            field_dict["sellerSku"] = seller_sku
        if gift_message is not UNSET:
            field_dict["giftMessage"] = gift_message
        if displayable_comment is not UNSET:
            field_dict["displayableComment"] = displayable_comment
        if fulfillment_network_sku is not UNSET:
            field_dict["fulfillmentNetworkSku"] = fulfillment_network_sku
        if order_item_disposition is not UNSET:
            field_dict["orderItemDisposition"] = order_item_disposition
        if per_unit_declared_value is not UNSET:
            field_dict["perUnitDeclaredValue"] = per_unit_declared_value
        if per_unit_price is not UNSET:
            field_dict["perUnitPrice"] = per_unit_price
        if per_unit_tax is not UNSET:
            field_dict["perUnitTax"] = per_unit_tax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        quantity = d.pop("quantity")

        seller_sku = d.pop("sellerSku", UNSET)

        gift_message = d.pop("giftMessage", UNSET)

        displayable_comment = d.pop("displayableComment", UNSET)

        fulfillment_network_sku = d.pop("fulfillmentNetworkSku", UNSET)

        order_item_disposition = d.pop("orderItemDisposition", UNSET)

        _per_unit_declared_value = d.pop("perUnitDeclaredValue", UNSET)
        per_unit_declared_value: Union[Unset, Money]
        if isinstance(_per_unit_declared_value, Unset):
            per_unit_declared_value = UNSET
        else:
            per_unit_declared_value = Money.from_dict(_per_unit_declared_value)

        _per_unit_price = d.pop("perUnitPrice", UNSET)
        per_unit_price: Union[Unset, Money]
        if isinstance(_per_unit_price, Unset):
            per_unit_price = UNSET
        else:
            per_unit_price = Money.from_dict(_per_unit_price)

        _per_unit_tax = d.pop("perUnitTax", UNSET)
        per_unit_tax: Union[Unset, Money]
        if isinstance(_per_unit_tax, Unset):
            per_unit_tax = UNSET
        else:
            per_unit_tax = Money.from_dict(_per_unit_tax)

        result = cls(
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            quantity=quantity,
            seller_sku=seller_sku,
            gift_message=gift_message,
            displayable_comment=displayable_comment,
            fulfillment_network_sku=fulfillment_network_sku,
            order_item_disposition=order_item_disposition,
            per_unit_declared_value=per_unit_declared_value,
            per_unit_price=per_unit_price,
            per_unit_tax=per_unit_tax,
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
