from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.shipment_type import ShipmentType

if TYPE_CHECKING:
    from ..models.transport_detail_input import TransportDetailInput


T = TypeVar("T", bound="PutTransportDetailsRequest")


@attr.s(auto_attribs=True)
class PutTransportDetailsRequest:
    r"""The request schema for a putTransportDetails operation.

    Attributes:
        is_partnered (bool): Indicates whether a putTransportDetails request is for an Amazon-partnered carrier.
        shipment_type (ShipmentType): Specifies the carrier shipment type in a putTransportDetails request.
        transport_details (TransportDetailInput): Information required to create an Amazon-partnered carrier shipping
            estimate, or to alert the Amazon fulfillment center to the arrival of an inbound shipment by a non-Amazon-
            partnered carrier.
    """

    is_partnered: bool
    shipment_type: ShipmentType
    transport_details: "TransportDetailInput"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_partnered = self.is_partnered
        shipment_type = self.shipment_type.value

        transport_details = self.transport_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IsPartnered": is_partnered,
                "ShipmentType": shipment_type,
                "TransportDetails": transport_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_detail_input import TransportDetailInput

        d = src_dict.copy()
        is_partnered = d.pop("IsPartnered")

        shipment_type = ShipmentType(d.pop("ShipmentType"))

        transport_details = TransportDetailInput.from_dict(d.pop("TransportDetails"))

        result = cls(
            is_partnered=is_partnered,
            shipment_type=shipment_type,
            transport_details=transport_details,
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
