import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_details_order_status import OrderDetailsOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.order_details_tax_total import OrderDetailsTaxTotal
    from ..models.order_item import OrderItem
    from ..models.party_identification import PartyIdentification
    from ..models.shipment_details import ShipmentDetails


T = TypeVar("T", bound="OrderDetails")


@attr.s(auto_attribs=True)
class OrderDetails:
    r"""Details of an order.

    Attributes:
        customer_order_number (str): The customer order number.
        order_date (datetime.datetime): The date the order was placed. This field is expected to be in ISO-8601
            date/time format, for example:2018-07-16T23:00:00Z/ 2018-07-16T23:00:00-05:00 /2018-07-16T23:00:00-08:00. If no
            time zone is specified, UTC should be assumed.
        shipment_details (ShipmentDetails): Shipment details required for the shipment.
        selling_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        ship_to_party (Address): Address of the party.
        bill_to_party (PartyIdentification):
        items (List['OrderItem']): A list of items in this purchase order.
        order_status (Union[Unset, OrderDetailsOrderStatus]): Current status of the order.
        tax_total (Union[Unset, OrderDetailsTaxTotal]):
    """

    customer_order_number: str
    order_date: datetime.datetime
    shipment_details: "ShipmentDetails"
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    ship_to_party: "Address"
    bill_to_party: "PartyIdentification"
    items: List["OrderItem"]
    order_status: Union[Unset, OrderDetailsOrderStatus] = UNSET
    tax_total: Union[Unset, "OrderDetailsTaxTotal"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_order_number = self.customer_order_number
        order_date = self.order_date.isoformat()

        shipment_details = self.shipment_details.to_dict()

        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        ship_to_party = self.ship_to_party.to_dict()

        bill_to_party = self.bill_to_party.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        order_status: Union[Unset, str] = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        tax_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_total, Unset):
            tax_total = self.tax_total.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerOrderNumber": customer_order_number,
                "orderDate": order_date,
                "shipmentDetails": shipment_details,
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
                "shipToParty": ship_to_party,
                "billToParty": bill_to_party,
                "items": items,
            }
        )
        if order_status is not UNSET:
            field_dict["orderStatus"] = order_status
        if tax_total is not UNSET:
            field_dict["taxTotal"] = tax_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.order_details_tax_total import OrderDetailsTaxTotal
        from ..models.order_item import OrderItem
        from ..models.party_identification import PartyIdentification
        from ..models.shipment_details import ShipmentDetails

        d = src_dict.copy()
        customer_order_number = d.pop("customerOrderNumber")

        order_date = isoparse(d.pop("orderDate"))

        shipment_details = ShipmentDetails.from_dict(d.pop("shipmentDetails"))

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        ship_to_party = Address.from_dict(d.pop("shipToParty"))

        bill_to_party = PartyIdentification.from_dict(d.pop("billToParty"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        _order_status = d.pop("orderStatus", UNSET)
        order_status: Union[Unset, OrderDetailsOrderStatus]
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = OrderDetailsOrderStatus(_order_status)

        _tax_total = d.pop("taxTotal", UNSET)
        tax_total: Union[Unset, OrderDetailsTaxTotal]
        if isinstance(_tax_total, Unset):
            tax_total = UNSET
        else:
            tax_total = OrderDetailsTaxTotal.from_dict(_tax_total)

        result = cls(
            customer_order_number=customer_order_number,
            order_date=order_date,
            shipment_details=shipment_details,
            selling_party=selling_party,
            ship_from_party=ship_from_party,
            ship_to_party=ship_to_party,
            bill_to_party=bill_to_party,
            items=items,
            order_status=order_status,
            tax_total=tax_total,
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
