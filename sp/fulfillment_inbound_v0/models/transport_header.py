from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.shipment_type import ShipmentType

T = TypeVar("T", bound="TransportHeader")


@attr.s(auto_attribs=True)
class TransportHeader:
    r"""The shipping identifier, information about whether the shipment is by an Amazon-partnered carrier, and information
    about whether the shipment is Small Parcel or Less Than Truckload/Full Truckload (LTL/FTL).

        Attributes:
            seller_id (str): The Amazon seller identifier.
            shipment_id (str): A shipment identifier originally returned by the createInboundShipmentPlan operation.
            is_partnered (bool): Indicates whether a putTransportDetails request is for a partnered carrier.

                Possible values:

                * true – Request is for an Amazon-partnered carrier.

                * false – Request is for a non-Amazon-partnered carrier.
            shipment_type (ShipmentType): Specifies the carrier shipment type in a putTransportDetails request.
    """

    seller_id: str
    shipment_id: str
    is_partnered: bool
    shipment_type: ShipmentType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_id = self.seller_id
        shipment_id = self.shipment_id
        is_partnered = self.is_partnered
        shipment_type = self.shipment_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SellerId": seller_id,
                "ShipmentId": shipment_id,
                "IsPartnered": is_partnered,
                "ShipmentType": shipment_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_id = d.pop("SellerId")

        shipment_id = d.pop("ShipmentId")

        is_partnered = d.pop("IsPartnered")

        shipment_type = ShipmentType(d.pop("ShipmentType"))

        result = cls(
            seller_id=seller_id,
            shipment_id=shipment_id,
            is_partnered=is_partnered,
            shipment_type=shipment_type,
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
