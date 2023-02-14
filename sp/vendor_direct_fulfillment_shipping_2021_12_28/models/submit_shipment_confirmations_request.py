from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_confirmation import ShipmentConfirmation


T = TypeVar("T", bound="SubmitShipmentConfirmationsRequest")


@attr.s(auto_attribs=True)
class SubmitShipmentConfirmationsRequest:
    r"""
    Attributes:
        shipment_confirmations (Union[Unset, List['ShipmentConfirmation']]):
    """

    shipment_confirmations: Union[Unset, List["ShipmentConfirmation"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_confirmations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_confirmations, Unset):
            shipment_confirmations = []
            for shipment_confirmations_item_data in self.shipment_confirmations:
                shipment_confirmations_item = shipment_confirmations_item_data.to_dict()

                shipment_confirmations.append(shipment_confirmations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_confirmations is not UNSET:
            field_dict["shipmentConfirmations"] = shipment_confirmations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipment_confirmation import ShipmentConfirmation

        d = src_dict.copy()
        shipment_confirmations = []
        _shipment_confirmations = d.pop("shipmentConfirmations", UNSET)
        for shipment_confirmations_item_data in _shipment_confirmations or []:
            shipment_confirmations_item = ShipmentConfirmation.from_dict(shipment_confirmations_item_data)

            shipment_confirmations.append(shipment_confirmations_item)

        result = cls(
            shipment_confirmations=shipment_confirmations,
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
