import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.order_acknowledgement_item import OrderAcknowledgementItem
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="OrderAcknowledgement")


@attr.s(auto_attribs=True)
class OrderAcknowledgement:
    r"""
    Attributes:
        purchase_order_number (str): The purchase order number. Formatting Notes: 8-character alpha-numeric code.
        selling_party (PartyIdentification):
        acknowledgement_date (datetime.datetime): The date and time when the purchase order is acknowledged, in ISO-8601
            date/time format.
        items (List['OrderAcknowledgementItem']): A list of the items being acknowledged with associated details.
    """

    purchase_order_number: str
    selling_party: "PartyIdentification"
    acknowledgement_date: datetime.datetime
    items: List["OrderAcknowledgementItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        selling_party = self.selling_party.to_dict()

        acknowledgement_date = self.acknowledgement_date.isoformat()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "sellingParty": selling_party,
                "acknowledgementDate": acknowledgement_date,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_acknowledgement_item import OrderAcknowledgementItem
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        acknowledgement_date = isoparse(d.pop("acknowledgementDate"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderAcknowledgementItem.from_dict(items_item_data)

            items.append(items_item)

        result = cls(
            purchase_order_number=purchase_order_number,
            selling_party=selling_party,
            acknowledgement_date=acknowledgement_date,
            items=items,
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
