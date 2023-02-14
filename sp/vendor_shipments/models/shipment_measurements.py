from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume import Volume
    from ..models.weight import Weight


T = TypeVar("T", bound="ShipmentMeasurements")


@attr.s(auto_attribs=True)
class ShipmentMeasurements:
    r"""Shipment measurement details.

    Attributes:
        gross_shipment_weight (Union[Unset, Weight]): The weight.
        shipment_volume (Union[Unset, Volume]): The volume of the container.
        carton_count (Union[Unset, int]): Number of cartons present in the shipment. Provide the cartonCount only for
            unpalletized shipments.
        pallet_count (Union[Unset, int]): Number of pallets present in the shipment. Provide the palletCount only for
            palletized shipments.
    """

    gross_shipment_weight: Union[Unset, "Weight"] = UNSET
    shipment_volume: Union[Unset, "Volume"] = UNSET
    carton_count: Union[Unset, int] = UNSET
    pallet_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gross_shipment_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gross_shipment_weight, Unset):
            gross_shipment_weight = self.gross_shipment_weight.to_dict()

        shipment_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_volume, Unset):
            shipment_volume = self.shipment_volume.to_dict()

        carton_count = self.carton_count
        pallet_count = self.pallet_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gross_shipment_weight is not UNSET:
            field_dict["grossShipmentWeight"] = gross_shipment_weight
        if shipment_volume is not UNSET:
            field_dict["shipmentVolume"] = shipment_volume
        if carton_count is not UNSET:
            field_dict["cartonCount"] = carton_count
        if pallet_count is not UNSET:
            field_dict["palletCount"] = pallet_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.volume import Volume
        from ..models.weight import Weight

        d = src_dict.copy()
        _gross_shipment_weight = d.pop("grossShipmentWeight", UNSET)
        gross_shipment_weight: Union[Unset, Weight]
        if isinstance(_gross_shipment_weight, Unset):
            gross_shipment_weight = UNSET
        else:
            gross_shipment_weight = Weight.from_dict(_gross_shipment_weight)

        _shipment_volume = d.pop("shipmentVolume", UNSET)
        shipment_volume: Union[Unset, Volume]
        if isinstance(_shipment_volume, Unset):
            shipment_volume = UNSET
        else:
            shipment_volume = Volume.from_dict(_shipment_volume)

        carton_count = d.pop("cartonCount", UNSET)

        pallet_count = d.pop("palletCount", UNSET)

        result = cls(
            gross_shipment_weight=gross_shipment_weight,
            shipment_volume=shipment_volume,
            carton_count=carton_count,
            pallet_count=pallet_count,
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
