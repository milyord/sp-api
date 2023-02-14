import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.appointment_slot_report_scheduling_type import AppointmentSlotReportSchedulingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_slot import AppointmentSlot


T = TypeVar("T", bound="AppointmentSlotReport")


@attr.s(auto_attribs=True)
class AppointmentSlotReport:
    r"""Availability information as per the service context queried.

    Attributes:
        scheduling_type (Union[Unset, AppointmentSlotReportSchedulingType]): Defines the type of slots.
        start_time (Union[Unset, datetime.datetime]): Start Time from which the appointment slots are generated in ISO
            8601 format.
        end_time (Union[Unset, datetime.datetime]): End Time up to which the appointment slots are generated in ISO 8601
            format.
        appointment_slots (Union[Unset, List['AppointmentSlot']]): A list of time windows along with associated capacity
            in which the service can be performed.
    """

    scheduling_type: Union[Unset, AppointmentSlotReportSchedulingType] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    appointment_slots: Union[Unset, List["AppointmentSlot"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduling_type: Union[Unset, str] = UNSET
        if not isinstance(self.scheduling_type, Unset):
            scheduling_type = self.scheduling_type.value

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        appointment_slots: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.appointment_slots, Unset):
            appointment_slots = []
            for appointment_slots_item_data in self.appointment_slots:
                appointment_slots_item = appointment_slots_item_data.to_dict()

                appointment_slots.append(appointment_slots_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheduling_type is not UNSET:
            field_dict["schedulingType"] = scheduling_type
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if appointment_slots is not UNSET:
            field_dict["appointmentSlots"] = appointment_slots

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_slot import AppointmentSlot

        d = src_dict.copy()
        _scheduling_type = d.pop("schedulingType", UNSET)
        scheduling_type: Union[Unset, AppointmentSlotReportSchedulingType]
        if isinstance(_scheduling_type, Unset):
            scheduling_type = UNSET
        else:
            scheduling_type = AppointmentSlotReportSchedulingType(_scheduling_type)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        appointment_slots = []
        _appointment_slots = d.pop("appointmentSlots", UNSET)
        for appointment_slots_item_data in _appointment_slots or []:
            appointment_slots_item = AppointmentSlot.from_dict(appointment_slots_item_data)

            appointment_slots.append(appointment_slots_item)

        result = cls(
            scheduling_type=scheduling_type,
            start_time=start_time,
            end_time=end_time,
            appointment_slots=appointment_slots,
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
