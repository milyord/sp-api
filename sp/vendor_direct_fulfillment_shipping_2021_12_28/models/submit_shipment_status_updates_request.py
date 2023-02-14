from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_status_update import ShipmentStatusUpdate


T = TypeVar("T", bound="SubmitShipmentStatusUpdatesRequest")


@attr.s(auto_attribs=True)
class SubmitShipmentStatusUpdatesRequest:
    r"""
    Attributes:
        shipment_status_updates (Union[Unset, List['ShipmentStatusUpdate']]):
    """

    shipment_status_updates: Union[Unset, List["ShipmentStatusUpdate"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_status_updates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_status_updates, Unset):
            shipment_status_updates = []
            for shipment_status_updates_item_data in self.shipment_status_updates:
                shipment_status_updates_item = shipment_status_updates_item_data.to_dict()

                shipment_status_updates.append(shipment_status_updates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_status_updates is not UNSET:
            field_dict["shipmentStatusUpdates"] = shipment_status_updates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipment_status_update import ShipmentStatusUpdate

        d = src_dict.copy()
        shipment_status_updates = []
        _shipment_status_updates = d.pop("shipmentStatusUpdates", UNSET)
        for shipment_status_updates_item_data in _shipment_status_updates or []:
            shipment_status_updates_item = ShipmentStatusUpdate.from_dict(shipment_status_updates_item_data)

            shipment_status_updates.append(shipment_status_updates_item)

        result = cls(
            shipment_status_updates=shipment_status_updates,
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
