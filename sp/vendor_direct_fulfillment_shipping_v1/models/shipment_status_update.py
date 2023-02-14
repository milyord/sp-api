from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.party_identification import PartyIdentification
    from ..models.status_update_details import StatusUpdateDetails


T = TypeVar("T", bound="ShipmentStatusUpdate")


@attr.s(auto_attribs=True)
class ShipmentStatusUpdate:
    r"""
    Attributes:
        purchase_order_number (str): Purchase order number of the shipment for which to update the shipment status.
        selling_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        status_update_details (StatusUpdateDetails): Details for the shipment status update given by the vendor for the
            specific package.
    """

    purchase_order_number: str
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    status_update_details: "StatusUpdateDetails"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        status_update_details = self.status_update_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
                "statusUpdateDetails": status_update_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.party_identification import PartyIdentification
        from ..models.status_update_details import StatusUpdateDetails

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        status_update_details = StatusUpdateDetails.from_dict(d.pop("statusUpdateDetails"))

        result = cls(
            purchase_order_number=purchase_order_number,
            selling_party=selling_party,
            ship_from_party=ship_from_party,
            status_update_details=status_update_details,
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
