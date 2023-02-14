import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.status_update_details_shipment_schedule import StatusUpdateDetailsShipmentSchedule


T = TypeVar("T", bound="StatusUpdateDetails")


@attr.s(auto_attribs=True)
class StatusUpdateDetails:
    r"""Details for the shipment status update given by the vendor for the specific package.

    Attributes:
        tracking_number (str): This is required to be provided for every package and should match with the
            trackingNumber sent for the shipment confirmation.
        status_code (str): Indicates the shipment status code of the package that provides transportation information
            for Amazon tracking systems and ultimately for the final customer.
        reason_code (str): Provides a reason code for the status of the package that will provide additional information
            about the transportation status.
        status_date_time (datetime.datetime): The date and time when the shipment status was updated. This field is
            expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z
            or 2020-07-16T23:00:00+01:00.
        status_location_address (Address): Address of the party.
        shipment_schedule (Union[Unset, StatusUpdateDetailsShipmentSchedule]):
    """

    tracking_number: str
    status_code: str
    reason_code: str
    status_date_time: datetime.datetime
    status_location_address: "Address"
    shipment_schedule: Union[Unset, "StatusUpdateDetailsShipmentSchedule"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracking_number = self.tracking_number
        status_code = self.status_code
        reason_code = self.reason_code
        status_date_time = self.status_date_time.isoformat()

        status_location_address = self.status_location_address.to_dict()

        shipment_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipment_schedule, Unset):
            shipment_schedule = self.shipment_schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trackingNumber": tracking_number,
                "statusCode": status_code,
                "reasonCode": reason_code,
                "statusDateTime": status_date_time,
                "statusLocationAddress": status_location_address,
            }
        )
        if shipment_schedule is not UNSET:
            field_dict["shipmentSchedule"] = shipment_schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.status_update_details_shipment_schedule import StatusUpdateDetailsShipmentSchedule

        d = src_dict.copy()
        tracking_number = d.pop("trackingNumber")

        status_code = d.pop("statusCode")

        reason_code = d.pop("reasonCode")

        status_date_time = isoparse(d.pop("statusDateTime"))

        status_location_address = Address.from_dict(d.pop("statusLocationAddress"))

        _shipment_schedule = d.pop("shipmentSchedule", UNSET)
        shipment_schedule: Union[Unset, StatusUpdateDetailsShipmentSchedule]
        if isinstance(_shipment_schedule, Unset):
            shipment_schedule = UNSET
        else:
            shipment_schedule = StatusUpdateDetailsShipmentSchedule.from_dict(_shipment_schedule)

        result = cls(
            tracking_number=tracking_number,
            status_code=status_code,
            reason_code=reason_code,
            status_date_time=status_date_time,
            status_location_address=status_location_address,
            shipment_schedule=shipment_schedule,
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
