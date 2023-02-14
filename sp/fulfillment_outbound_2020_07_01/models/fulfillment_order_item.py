import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="FulfillmentOrderItem")


@attr.s(auto_attribs=True)
class FulfillmentOrderItem:
    r"""Item information for a fulfillment order.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        seller_fulfillment_order_item_id (str): A fulfillment order item identifier submitted with a call to the
            createFulfillmentOrder operation.
        quantity (int): The item quantity.
        cancelled_quantity (int): The item quantity.
        unfulfillable_quantity (int): The item quantity.
        gift_message (Union[Unset, str]): A message to the gift recipient, if applicable.
        displayable_comment (Union[Unset, str]): Item-specific text that displays in recipient-facing materials such as
            the outbound shipment packing slip.
        fulfillment_network_sku (Union[Unset, str]): Amazon's fulfillment network SKU of the item.
        order_item_disposition (Union[Unset, str]): Indicates whether the item is sellable or unsellable.
        estimated_ship_date (Union[Unset, datetime.datetime]):
        estimated_arrival_date (Union[Unset, datetime.datetime]):
        per_unit_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
        per_unit_tax (Union[Unset, Money]): An amount of money, including units in the form of currency.
        per_unit_declared_value (Union[Unset, Money]): An amount of money, including units in the form of currency.
    """

    seller_sku: str
    seller_fulfillment_order_item_id: str
    quantity: int
    cancelled_quantity: int
    unfulfillable_quantity: int
    gift_message: Union[Unset, str] = UNSET
    displayable_comment: Union[Unset, str] = UNSET
    fulfillment_network_sku: Union[Unset, str] = UNSET
    order_item_disposition: Union[Unset, str] = UNSET
    estimated_ship_date: Union[Unset, datetime.datetime] = UNSET
    estimated_arrival_date: Union[Unset, datetime.datetime] = UNSET
    per_unit_price: Union[Unset, "Money"] = UNSET
    per_unit_tax: Union[Unset, "Money"] = UNSET
    per_unit_declared_value: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        quantity = self.quantity
        cancelled_quantity = self.cancelled_quantity
        unfulfillable_quantity = self.unfulfillable_quantity
        gift_message = self.gift_message
        displayable_comment = self.displayable_comment
        fulfillment_network_sku = self.fulfillment_network_sku
        order_item_disposition = self.order_item_disposition
        estimated_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_ship_date, Unset):
            estimated_ship_date = self.estimated_ship_date.isoformat()

        estimated_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival_date, Unset):
            estimated_arrival_date = self.estimated_arrival_date.isoformat()

        per_unit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_price, Unset):
            per_unit_price = self.per_unit_price.to_dict()

        per_unit_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_tax, Unset):
            per_unit_tax = self.per_unit_tax.to_dict()

        per_unit_declared_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_declared_value, Unset):
            per_unit_declared_value = self.per_unit_declared_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerSku": seller_sku,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
                "quantity": quantity,
                "cancelledQuantity": cancelled_quantity,
                "unfulfillableQuantity": unfulfillable_quantity,
            }
        )
        if gift_message is not UNSET:
            field_dict["giftMessage"] = gift_message
        if displayable_comment is not UNSET:
            field_dict["displayableComment"] = displayable_comment
        if fulfillment_network_sku is not UNSET:
            field_dict["fulfillmentNetworkSku"] = fulfillment_network_sku
        if order_item_disposition is not UNSET:
            field_dict["orderItemDisposition"] = order_item_disposition
        if estimated_ship_date is not UNSET:
            field_dict["estimatedShipDate"] = estimated_ship_date
        if estimated_arrival_date is not UNSET:
            field_dict["estimatedArrivalDate"] = estimated_arrival_date
        if per_unit_price is not UNSET:
            field_dict["perUnitPrice"] = per_unit_price
        if per_unit_tax is not UNSET:
            field_dict["perUnitTax"] = per_unit_tax
        if per_unit_declared_value is not UNSET:
            field_dict["perUnitDeclaredValue"] = per_unit_declared_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        seller_sku = d.pop("sellerSku")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        quantity = d.pop("quantity")

        cancelled_quantity = d.pop("cancelledQuantity")

        unfulfillable_quantity = d.pop("unfulfillableQuantity")

        gift_message = d.pop("giftMessage", UNSET)

        displayable_comment = d.pop("displayableComment", UNSET)

        fulfillment_network_sku = d.pop("fulfillmentNetworkSku", UNSET)

        order_item_disposition = d.pop("orderItemDisposition", UNSET)

        _estimated_ship_date = d.pop("estimatedShipDate", UNSET)
        estimated_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_ship_date, Unset):
            estimated_ship_date = UNSET
        else:
            estimated_ship_date = isoparse(_estimated_ship_date)

        _estimated_arrival_date = d.pop("estimatedArrivalDate", UNSET)
        estimated_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_arrival_date, Unset):
            estimated_arrival_date = UNSET
        else:
            estimated_arrival_date = isoparse(_estimated_arrival_date)

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

        _per_unit_declared_value = d.pop("perUnitDeclaredValue", UNSET)
        per_unit_declared_value: Union[Unset, Money]
        if isinstance(_per_unit_declared_value, Unset):
            per_unit_declared_value = UNSET
        else:
            per_unit_declared_value = Money.from_dict(_per_unit_declared_value)

        result = cls(
            seller_sku=seller_sku,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            quantity=quantity,
            cancelled_quantity=cancelled_quantity,
            unfulfillable_quantity=unfulfillable_quantity,
            gift_message=gift_message,
            displayable_comment=displayable_comment,
            fulfillment_network_sku=fulfillment_network_sku,
            order_item_disposition=order_item_disposition,
            estimated_ship_date=estimated_ship_date,
            estimated_arrival_date=estimated_arrival_date,
            per_unit_price=per_unit_price,
            per_unit_tax=per_unit_tax,
            per_unit_declared_value=per_unit_declared_value,
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
