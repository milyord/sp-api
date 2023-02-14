from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_details import GiftDetails
    from ..models.item_quantity import ItemQuantity
    from ..models.money import Money
    from ..models.scheduled_delivery_shipment import ScheduledDeliveryShipment
    from ..models.tax_item_details import TaxItemDetails


T = TypeVar("T", bound="OrderItem")


@attr.s(auto_attribs=True)
class OrderItem:
    r"""
    Attributes:
        item_sequence_number (str): Numbering of the item on the purchase order. The first item will be 1, the second 2,
            and so on.
        ordered_quantity (ItemQuantity): Details of quantity ordered.
        net_price (Money): An amount of money, including units in the form of currency.
        buyer_product_identifier (Union[Unset, str]): Buyer's standard identification number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item.
        title (Union[Unset, str]): Title for the item.
        scheduled_delivery_shipment (Union[Unset, ScheduledDeliveryShipment]): Dates for the scheduled delivery
            shipments.
        gift_details (Union[Unset, GiftDetails]): Gift details for the item.
        tax_details (Union[Unset, TaxItemDetails]): Total tax details for the line item.
        total_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
    """

    item_sequence_number: str
    ordered_quantity: "ItemQuantity"
    net_price: "Money"
    buyer_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    scheduled_delivery_shipment: Union[Unset, "ScheduledDeliveryShipment"] = UNSET
    gift_details: Union[Unset, "GiftDetails"] = UNSET
    tax_details: Union[Unset, "TaxItemDetails"] = UNSET
    total_price: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        ordered_quantity = self.ordered_quantity.to_dict()

        net_price = self.net_price.to_dict()

        buyer_product_identifier = self.buyer_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        title = self.title
        scheduled_delivery_shipment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scheduled_delivery_shipment, Unset):
            scheduled_delivery_shipment = self.scheduled_delivery_shipment.to_dict()

        gift_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gift_details, Unset):
            gift_details = self.gift_details.to_dict()

        tax_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_details, Unset):
            tax_details = self.tax_details.to_dict()

        total_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_price, Unset):
            total_price = self.total_price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
                "orderedQuantity": ordered_quantity,
                "netPrice": net_price,
            }
        )
        if buyer_product_identifier is not UNSET:
            field_dict["buyerProductIdentifier"] = buyer_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if title is not UNSET:
            field_dict["title"] = title
        if scheduled_delivery_shipment is not UNSET:
            field_dict["scheduledDeliveryShipment"] = scheduled_delivery_shipment
        if gift_details is not UNSET:
            field_dict["giftDetails"] = gift_details
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gift_details import GiftDetails
        from ..models.item_quantity import ItemQuantity
        from ..models.money import Money
        from ..models.scheduled_delivery_shipment import ScheduledDeliveryShipment
        from ..models.tax_item_details import TaxItemDetails

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        ordered_quantity = ItemQuantity.from_dict(d.pop("orderedQuantity"))

        net_price = Money.from_dict(d.pop("netPrice"))

        buyer_product_identifier = d.pop("buyerProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        title = d.pop("title", UNSET)

        _scheduled_delivery_shipment = d.pop("scheduledDeliveryShipment", UNSET)
        scheduled_delivery_shipment: Union[Unset, ScheduledDeliveryShipment]
        if isinstance(_scheduled_delivery_shipment, Unset):
            scheduled_delivery_shipment = UNSET
        else:
            scheduled_delivery_shipment = ScheduledDeliveryShipment.from_dict(_scheduled_delivery_shipment)

        _gift_details = d.pop("giftDetails", UNSET)
        gift_details: Union[Unset, GiftDetails]
        if isinstance(_gift_details, Unset):
            gift_details = UNSET
        else:
            gift_details = GiftDetails.from_dict(_gift_details)

        _tax_details = d.pop("taxDetails", UNSET)
        tax_details: Union[Unset, TaxItemDetails]
        if isinstance(_tax_details, Unset):
            tax_details = UNSET
        else:
            tax_details = TaxItemDetails.from_dict(_tax_details)

        _total_price = d.pop("totalPrice", UNSET)
        total_price: Union[Unset, Money]
        if isinstance(_total_price, Unset):
            total_price = UNSET
        else:
            total_price = Money.from_dict(_total_price)

        result = cls(
            item_sequence_number=item_sequence_number,
            ordered_quantity=ordered_quantity,
            net_price=net_price,
            buyer_product_identifier=buyer_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            title=title,
            scheduled_delivery_shipment=scheduled_delivery_shipment,
            gift_details=gift_details,
            tax_details=tax_details,
            total_price=total_price,
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
