import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.acknowledgement_status import AcknowledgementStatus
    from ..models.order_item_acknowledgement import OrderItemAcknowledgement
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="OrderAcknowledgementItem")


@attr.s(auto_attribs=True)
class OrderAcknowledgementItem:
    r"""Details of an individual order being acknowledged.

    Attributes:
        purchase_order_number (str): The purchase order number for this order. Formatting Notes: alpha-numeric code.
        vendor_order_number (str): The vendor's order number for this order.
        acknowledgement_date (datetime.datetime): The date and time when the order is acknowledged, in ISO-8601
            date/time format. For example: 2018-07-16T23:00:00Z / 2018-07-16T23:00:00-05:00 / 2018-07-16T23:00:00-08:00.
        acknowledgement_status (AcknowledgementStatus): Status of acknowledgement.
        selling_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        item_acknowledgements (List['OrderItemAcknowledgement']): Item details including acknowledged quantity.
    """

    purchase_order_number: str
    vendor_order_number: str
    acknowledgement_date: datetime.datetime
    acknowledgement_status: "AcknowledgementStatus"
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    item_acknowledgements: List["OrderItemAcknowledgement"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        vendor_order_number = self.vendor_order_number
        acknowledgement_date = self.acknowledgement_date.isoformat()

        acknowledgement_status = self.acknowledgement_status.to_dict()

        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        item_acknowledgements = []
        for item_acknowledgements_item_data in self.item_acknowledgements:
            item_acknowledgements_item = item_acknowledgements_item_data.to_dict()

            item_acknowledgements.append(item_acknowledgements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "vendorOrderNumber": vendor_order_number,
                "acknowledgementDate": acknowledgement_date,
                "acknowledgementStatus": acknowledgement_status,
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
                "itemAcknowledgements": item_acknowledgements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acknowledgement_status import AcknowledgementStatus
        from ..models.order_item_acknowledgement import OrderItemAcknowledgement
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        vendor_order_number = d.pop("vendorOrderNumber")

        acknowledgement_date = isoparse(d.pop("acknowledgementDate"))

        acknowledgement_status = AcknowledgementStatus.from_dict(d.pop("acknowledgementStatus"))

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        item_acknowledgements = []
        _item_acknowledgements = d.pop("itemAcknowledgements")
        for item_acknowledgements_item_data in _item_acknowledgements:
            item_acknowledgements_item = OrderItemAcknowledgement.from_dict(item_acknowledgements_item_data)

            item_acknowledgements.append(item_acknowledgements_item)

        result = cls(
            purchase_order_number=purchase_order_number,
            vendor_order_number=vendor_order_number,
            acknowledgement_date=acknowledgement_date,
            acknowledgement_status=acknowledgement_status,
            selling_party=selling_party,
            ship_from_party=ship_from_party,
            item_acknowledgements=item_acknowledgements,
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
