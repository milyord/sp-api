import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_status_purchase_order_status import OrderStatusPurchaseOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_item_status import OrderItemStatus
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="OrderStatus")


@attr.s(auto_attribs=True)
class OrderStatus:
    r"""Current status of a purchase order.

    Attributes:
        purchase_order_number (str): The buyer's purchase order number for this order. Formatting Notes: 8-character
            alpha-numeric code.
        purchase_order_status (OrderStatusPurchaseOrderStatus): The status of the buyer's purchase order for this order.
        purchase_order_date (datetime.datetime): The date the purchase order was placed. Must be in ISO-8601 date/time
            format.
        selling_party (PartyIdentification):
        ship_to_party (PartyIdentification):
        item_status (List['OrderItemStatus']): Detailed description of items order status.
        last_updated_date (Union[Unset, datetime.datetime]): The date when the purchase order was last updated. Must be
            in ISO-8601 date/time format.
    """

    purchase_order_number: str
    purchase_order_status: OrderStatusPurchaseOrderStatus
    purchase_order_date: datetime.datetime
    selling_party: "PartyIdentification"
    ship_to_party: "PartyIdentification"
    item_status: List["OrderItemStatus"]
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        purchase_order_status = self.purchase_order_status.value

        purchase_order_date = self.purchase_order_date.isoformat()

        selling_party = self.selling_party.to_dict()

        ship_to_party = self.ship_to_party.to_dict()

        item_status = []
        for componentsschemas_item_status_item_data in self.item_status:
            componentsschemas_item_status_item = componentsschemas_item_status_item_data.to_dict()

            item_status.append(componentsschemas_item_status_item)

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "purchaseOrderStatus": purchase_order_status,
                "purchaseOrderDate": purchase_order_date,
                "sellingParty": selling_party,
                "shipToParty": ship_to_party,
                "itemStatus": item_status,
            }
        )
        if last_updated_date is not UNSET:
            field_dict["lastUpdatedDate"] = last_updated_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_item_status import OrderItemStatus
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        purchase_order_status = OrderStatusPurchaseOrderStatus(d.pop("purchaseOrderStatus"))

        purchase_order_date = isoparse(d.pop("purchaseOrderDate"))

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_to_party = PartyIdentification.from_dict(d.pop("shipToParty"))

        item_status = []
        _item_status = d.pop("itemStatus")
        for componentsschemas_item_status_item_data in _item_status:
            componentsschemas_item_status_item = OrderItemStatus.from_dict(componentsschemas_item_status_item_data)

            item_status.append(componentsschemas_item_status_item)

        _last_updated_date = d.pop("lastUpdatedDate", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        result = cls(
            purchase_order_number=purchase_order_number,
            purchase_order_status=purchase_order_status,
            purchase_order_date=purchase_order_date,
            selling_party=selling_party,
            ship_to_party=ship_to_party,
            item_status=item_status,
            last_updated_date=last_updated_date,
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
