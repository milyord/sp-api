from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.package_status import PackageStatus

T = TypeVar("T", bound="NonPartneredSmallParcelPackageOutput")


@attr.s(auto_attribs=True)
class NonPartneredSmallParcelPackageOutput:
    r"""Carrier, tracking number, and status information for the package.

    Attributes:
        carrier_name (str): The carrier that you are using for the inbound shipment.
        tracking_id (str): The tracking number of the package, provided by the carrier.
        package_status (PackageStatus): The shipment status of the package.
    """

    carrier_name: str
    tracking_id: str
    package_status: PackageStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_name = self.carrier_name
        tracking_id = self.tracking_id
        package_status = self.package_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CarrierName": carrier_name,
                "TrackingId": tracking_id,
                "PackageStatus": package_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier_name = d.pop("CarrierName")

        tracking_id = d.pop("TrackingId")

        package_status = PackageStatus(d.pop("PackageStatus"))

        result = cls(
            carrier_name=carrier_name,
            tracking_id=tracking_id,
            package_status=package_status,
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
