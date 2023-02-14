import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusUpdateDetailsShipmentSchedule")


@attr.s(auto_attribs=True)
class StatusUpdateDetailsShipmentSchedule:
    r"""
    Attributes:
        estimated_delivery_date_time (Union[Unset, datetime.datetime]): Date on which the shipment is expected to reach
            the customer delivery location. This field is expected to be in ISO-8601 date/time format, with UTC time zone or
            UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.
        appt_window_start_date_time (Union[Unset, datetime.datetime]): This field indicates the date and time at the
            start of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601
            date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or
            2020-07-16T23:00:00+01:00.
        appt_window_end_date_time (Union[Unset, datetime.datetime]): This field indicates the date and time at the end
            of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time
            format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.
    """

    estimated_delivery_date_time: Union[Unset, datetime.datetime] = UNSET
    appt_window_start_date_time: Union[Unset, datetime.datetime] = UNSET
    appt_window_end_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        estimated_delivery_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_delivery_date_time, Unset):
            estimated_delivery_date_time = self.estimated_delivery_date_time.isoformat()

        appt_window_start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.appt_window_start_date_time, Unset):
            appt_window_start_date_time = self.appt_window_start_date_time.isoformat()

        appt_window_end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.appt_window_end_date_time, Unset):
            appt_window_end_date_time = self.appt_window_end_date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_delivery_date_time is not UNSET:
            field_dict["estimatedDeliveryDateTime"] = estimated_delivery_date_time
        if appt_window_start_date_time is not UNSET:
            field_dict["apptWindowStartDateTime"] = appt_window_start_date_time
        if appt_window_end_date_time is not UNSET:
            field_dict["apptWindowEndDateTime"] = appt_window_end_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _estimated_delivery_date_time = d.pop("estimatedDeliveryDateTime", UNSET)
        estimated_delivery_date_time: Union[Unset, datetime.datetime]
        if isinstance(_estimated_delivery_date_time, Unset):
            estimated_delivery_date_time = UNSET
        else:
            estimated_delivery_date_time = isoparse(_estimated_delivery_date_time)

        _appt_window_start_date_time = d.pop("apptWindowStartDateTime", UNSET)
        appt_window_start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_appt_window_start_date_time, Unset):
            appt_window_start_date_time = UNSET
        else:
            appt_window_start_date_time = isoparse(_appt_window_start_date_time)

        _appt_window_end_date_time = d.pop("apptWindowEndDateTime", UNSET)
        appt_window_end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_appt_window_end_date_time, Unset):
            appt_window_end_date_time = UNSET
        else:
            appt_window_end_date_time = isoparse(_appt_window_end_date_time)

        result = cls(
            estimated_delivery_date_time=estimated_delivery_date_time,
            appt_window_start_date_time=appt_window_start_date_time,
            appt_window_end_date_time=appt_window_end_date_time,
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
