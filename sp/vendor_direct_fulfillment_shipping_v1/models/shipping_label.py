from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.shipping_label_label_format import ShippingLabelLabelFormat

if TYPE_CHECKING:
    from ..models.label_data import LabelData
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="ShippingLabel")


@attr.s(auto_attribs=True)
class ShippingLabel:
    r"""
    Attributes:
        purchase_order_number (str): This field will contain the Purchase Order Number for this order.
        selling_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        label_format (ShippingLabelLabelFormat): Format of the label.
        label_data (List['LabelData']): Provides the details of the packages in this shipment.
    """

    purchase_order_number: str
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    label_format: ShippingLabelLabelFormat
    label_data: List["LabelData"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        label_format = self.label_format.value

        label_data = []
        for label_data_item_data in self.label_data:
            label_data_item = label_data_item_data.to_dict()

            label_data.append(label_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseOrderNumber": purchase_order_number,
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
                "labelFormat": label_format,
                "labelData": label_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_data import LabelData
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber")

        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        label_format = ShippingLabelLabelFormat(d.pop("labelFormat"))

        label_data = []
        _label_data = d.pop("labelData")
        for label_data_item_data in _label_data:
            label_data_item = LabelData.from_dict(label_data_item_data)

            label_data.append(label_data_item)

        result = cls(
            purchase_order_number=purchase_order_number,
            selling_party=selling_party,
            ship_from_party=ship_from_party,
            label_format=label_format,
            label_data=label_data,
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
