import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentShipmentPackage")


@attr.s(auto_attribs=True)
class FulfillmentShipmentPackage:
    r"""Package information for a shipment in a fulfillment order.

    Attributes:
        package_number (int): Identifies a package in a shipment.
        carrier_code (str): Identifies the carrier who will deliver the shipment to the recipient.
        tracking_number (Union[Unset, str]): The tracking number, if provided, can be used to obtain tracking and
            delivery information.
        estimated_arrival_date (Union[Unset, datetime.datetime]):
    """

    package_number: int
    carrier_code: str
    tracking_number: Union[Unset, str] = UNSET
    estimated_arrival_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_number = self.package_number
        carrier_code = self.carrier_code
        tracking_number = self.tracking_number
        estimated_arrival_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival_date, Unset):
            estimated_arrival_date = self.estimated_arrival_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageNumber": package_number,
                "carrierCode": carrier_code,
            }
        )
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if estimated_arrival_date is not UNSET:
            field_dict["estimatedArrivalDate"] = estimated_arrival_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package_number = d.pop("packageNumber")

        carrier_code = d.pop("carrierCode")

        tracking_number = d.pop("trackingNumber", UNSET)

        _estimated_arrival_date = d.pop("estimatedArrivalDate", UNSET)
        estimated_arrival_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_arrival_date, Unset):
            estimated_arrival_date = UNSET
        else:
            estimated_arrival_date = isoparse(_estimated_arrival_date)

        result = cls(
            package_number=package_number,
            carrier_code=carrier_code,
            tracking_number=tracking_number,
            estimated_arrival_date=estimated_arrival_date,
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
