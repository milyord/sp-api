import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_details_payment_method import OrderDetailsPaymentMethod
from ..models.order_details_purchase_order_type import OrderDetailsPurchaseOrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_details import ImportDetails
    from ..models.order_item import OrderItem
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="OrderDetails")


@attr.s(auto_attribs=True)
class OrderDetails:
    r"""Details of an order.

    Attributes:
        purchase_order_date (datetime.datetime): The date the purchase order was placed. Must be in ISO-8601 date/time
            format.
        purchase_order_state_changed_date (datetime.datetime): The date when current purchase order state was changed.
            Current purchase order state is available in the field 'purchaseOrderState'. Must be in ISO-8601 date/time
            format.
        items (List['OrderItem']): A list of items in this purchase order.
        purchase_order_changed_date (Union[Unset, datetime.datetime]): The date when purchase order was last changed by
            Amazon after the order was placed. This date will be greater than 'purchaseOrderDate'. This means the PO data
            was changed on that date and vendors are required to fulfill the  updated PO. The PO changes can be related to
            Item Quantity, Ship to Location, Ship Window etc. This field will not be present in orders that have not changed
            after creation. Must be in ISO-8601 date/time format.
        purchase_order_type (Union[Unset, OrderDetailsPurchaseOrderType]): Type of purchase order.
        import_details (Union[Unset, ImportDetails]): Import details for an import order.
        deal_code (Union[Unset, str]): If requested by the recipient, this field will contain a promotional/deal number.
            The discount code line is optional. It is used to obtain a price discount on items on the order.
        payment_method (Union[Unset, OrderDetailsPaymentMethod]): Payment method used.
        buying_party (Union[Unset, PartyIdentification]):
        selling_party (Union[Unset, PartyIdentification]):
        ship_to_party (Union[Unset, PartyIdentification]):
        bill_to_party (Union[Unset, PartyIdentification]):
        ship_window (Union[Unset, str]): Defines a date time interval according to ISO8601. Interval is separated by
            double hyphen (--).
        delivery_window (Union[Unset, str]): Defines a date time interval according to ISO8601. Interval is separated by
            double hyphen (--).
    """

    purchase_order_date: datetime.datetime
    purchase_order_state_changed_date: datetime.datetime
    items: List["OrderItem"]
    purchase_order_changed_date: Union[Unset, datetime.datetime] = UNSET
    purchase_order_type: Union[Unset, OrderDetailsPurchaseOrderType] = UNSET
    import_details: Union[Unset, "ImportDetails"] = UNSET
    deal_code: Union[Unset, str] = UNSET
    payment_method: Union[Unset, OrderDetailsPaymentMethod] = UNSET
    buying_party: Union[Unset, "PartyIdentification"] = UNSET
    selling_party: Union[Unset, "PartyIdentification"] = UNSET
    ship_to_party: Union[Unset, "PartyIdentification"] = UNSET
    bill_to_party: Union[Unset, "PartyIdentification"] = UNSET
    ship_window: Union[Unset, str] = UNSET
    delivery_window: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_date = self.purchase_order_date.isoformat()

        purchase_order_state_changed_date = self.purchase_order_state_changed_date.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        purchase_order_changed_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_order_changed_date, Unset):
            purchase_order_changed_date = self.purchase_order_changed_date.isoformat()

        purchase_order_type: Union[Unset, str] = UNSET
        if not isinstance(self.purchase_order_type, Unset):
            purchase_order_type = self.purchase_order_type.value

        import_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_details, Unset):
            import_details = self.import_details.to_dict()

        deal_code = self.deal_code
        payment_method: Union[Unset, str] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        buying_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.buying_party, Unset):
            buying_party = self.buying_party.to_dict()

        selling_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.selling_party, Unset):
            selling_party = self.selling_party.to_dict()

        ship_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_party, Unset):
            ship_to_party = self.ship_to_party.to_dict()

        bill_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_to_party, Unset):
            bill_to_party = self.bill_to_party.to_dict()

        ship_window = self.ship_window
        delivery_window = self.delivery_window

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderDate": purchase_order_date,
                "purchaseOrderStateChangedDate": purchase_order_state_changed_date,
                "items": items,
            }
        )
        if purchase_order_changed_date is not UNSET:
            field_dict["purchaseOrderChangedDate"] = purchase_order_changed_date
        if purchase_order_type is not UNSET:
            field_dict["purchaseOrderType"] = purchase_order_type
        if import_details is not UNSET:
            field_dict["importDetails"] = import_details
        if deal_code is not UNSET:
            field_dict["dealCode"] = deal_code
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if buying_party is not UNSET:
            field_dict["buyingParty"] = buying_party
        if selling_party is not UNSET:
            field_dict["sellingParty"] = selling_party
        if ship_to_party is not UNSET:
            field_dict["shipToParty"] = ship_to_party
        if bill_to_party is not UNSET:
            field_dict["billToParty"] = bill_to_party
        if ship_window is not UNSET:
            field_dict["shipWindow"] = ship_window
        if delivery_window is not UNSET:
            field_dict["deliveryWindow"] = delivery_window

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.import_details import ImportDetails
        from ..models.order_item import OrderItem
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        purchase_order_date = isoparse(d.pop("purchaseOrderDate"))

        purchase_order_state_changed_date = isoparse(d.pop("purchaseOrderStateChangedDate"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        _purchase_order_changed_date = d.pop("purchaseOrderChangedDate", UNSET)
        purchase_order_changed_date: Union[Unset, datetime.datetime]
        if isinstance(_purchase_order_changed_date, Unset):
            purchase_order_changed_date = UNSET
        else:
            purchase_order_changed_date = isoparse(_purchase_order_changed_date)

        _purchase_order_type = d.pop("purchaseOrderType", UNSET)
        purchase_order_type: Union[Unset, OrderDetailsPurchaseOrderType]
        if isinstance(_purchase_order_type, Unset):
            purchase_order_type = UNSET
        else:
            purchase_order_type = OrderDetailsPurchaseOrderType(_purchase_order_type)

        _import_details = d.pop("importDetails", UNSET)
        import_details: Union[Unset, ImportDetails]
        if isinstance(_import_details, Unset):
            import_details = UNSET
        else:
            import_details = ImportDetails.from_dict(_import_details)

        deal_code = d.pop("dealCode", UNSET)

        _payment_method = d.pop("paymentMethod", UNSET)
        payment_method: Union[Unset, OrderDetailsPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = OrderDetailsPaymentMethod(_payment_method)

        _buying_party = d.pop("buyingParty", UNSET)
        buying_party: Union[Unset, PartyIdentification]
        if isinstance(_buying_party, Unset):
            buying_party = UNSET
        else:
            buying_party = PartyIdentification.from_dict(_buying_party)

        _selling_party = d.pop("sellingParty", UNSET)
        selling_party: Union[Unset, PartyIdentification]
        if isinstance(_selling_party, Unset):
            selling_party = UNSET
        else:
            selling_party = PartyIdentification.from_dict(_selling_party)

        _ship_to_party = d.pop("shipToParty", UNSET)
        ship_to_party: Union[Unset, PartyIdentification]
        if isinstance(_ship_to_party, Unset):
            ship_to_party = UNSET
        else:
            ship_to_party = PartyIdentification.from_dict(_ship_to_party)

        _bill_to_party = d.pop("billToParty", UNSET)
        bill_to_party: Union[Unset, PartyIdentification]
        if isinstance(_bill_to_party, Unset):
            bill_to_party = UNSET
        else:
            bill_to_party = PartyIdentification.from_dict(_bill_to_party)

        ship_window = d.pop("shipWindow", UNSET)

        delivery_window = d.pop("deliveryWindow", UNSET)

        result = cls(
            purchase_order_date=purchase_order_date,
            purchase_order_state_changed_date=purchase_order_state_changed_date,
            items=items,
            purchase_order_changed_date=purchase_order_changed_date,
            purchase_order_type=purchase_order_type,
            import_details=import_details,
            deal_code=deal_code,
            payment_method=payment_method,
            buying_party=buying_party,
            selling_party=selling_party,
            ship_to_party=ship_to_party,
            bill_to_party=bill_to_party,
            ship_window=ship_window,
            delivery_window=delivery_window,
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
