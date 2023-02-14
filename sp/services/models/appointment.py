from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.appointment_appointment_status import AppointmentAppointmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_time import AppointmentTime
    from ..models.poa import Poa
    from ..models.technician import Technician


T = TypeVar("T", bound="Appointment")


@attr.s(auto_attribs=True)
class Appointment:
    r"""The details of an appointment.

    Attributes:
        appointment_id (Union[Unset, str]): The appointment identifier.
        appointment_status (Union[Unset, AppointmentAppointmentStatus]): The status of the appointment.
        appointment_time (Union[Unset, AppointmentTime]): The time of the appointment window.
        assigned_technicians (Union[Unset, List['Technician']]): A list of technicians assigned to the service job.
        rescheduled_appointment_id (Union[Unset, str]): The appointment identifier.
        poa (Union[Unset, Poa]): Proof of Appointment (POA) details.
    """

    appointment_id: Union[Unset, str] = UNSET
    appointment_status: Union[Unset, AppointmentAppointmentStatus] = UNSET
    appointment_time: Union[Unset, "AppointmentTime"] = UNSET
    assigned_technicians: Union[Unset, List["Technician"]] = UNSET
    rescheduled_appointment_id: Union[Unset, str] = UNSET
    poa: Union[Unset, "Poa"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_id = self.appointment_id
        appointment_status: Union[Unset, str] = UNSET
        if not isinstance(self.appointment_status, Unset):
            appointment_status = self.appointment_status.value

        appointment_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_time, Unset):
            appointment_time = self.appointment_time.to_dict()

        assigned_technicians: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assigned_technicians, Unset):
            assigned_technicians = []
            for assigned_technicians_item_data in self.assigned_technicians:
                assigned_technicians_item = assigned_technicians_item_data.to_dict()

                assigned_technicians.append(assigned_technicians_item)

        rescheduled_appointment_id = self.rescheduled_appointment_id
        poa: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.poa, Unset):
            poa = self.poa.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if appointment_status is not UNSET:
            field_dict["appointmentStatus"] = appointment_status
        if appointment_time is not UNSET:
            field_dict["appointmentTime"] = appointment_time
        if assigned_technicians is not UNSET:
            field_dict["assignedTechnicians"] = assigned_technicians
        if rescheduled_appointment_id is not UNSET:
            field_dict["rescheduledAppointmentId"] = rescheduled_appointment_id
        if poa is not UNSET:
            field_dict["poa"] = poa

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_time import AppointmentTime
        from ..models.poa import Poa
        from ..models.technician import Technician

        d = src_dict.copy()
        appointment_id = d.pop("appointmentId", UNSET)

        _appointment_status = d.pop("appointmentStatus", UNSET)
        appointment_status: Union[Unset, AppointmentAppointmentStatus]
        if isinstance(_appointment_status, Unset):
            appointment_status = UNSET
        else:
            appointment_status = AppointmentAppointmentStatus(_appointment_status)

        _appointment_time = d.pop("appointmentTime", UNSET)
        appointment_time: Union[Unset, AppointmentTime]
        if isinstance(_appointment_time, Unset):
            appointment_time = UNSET
        else:
            appointment_time = AppointmentTime.from_dict(_appointment_time)

        assigned_technicians = []
        _assigned_technicians = d.pop("assignedTechnicians", UNSET)
        for assigned_technicians_item_data in _assigned_technicians or []:
            assigned_technicians_item = Technician.from_dict(assigned_technicians_item_data)

            assigned_technicians.append(assigned_technicians_item)

        rescheduled_appointment_id = d.pop("rescheduledAppointmentId", UNSET)

        _poa = d.pop("poa", UNSET)
        poa: Union[Unset, Poa]
        if isinstance(_poa, Unset):
            poa = UNSET
        else:
            poa = Poa.from_dict(_poa)

        result = cls(
            appointment_id=appointment_id,
            appointment_status=appointment_status,
            appointment_time=appointment_time,
            assigned_technicians=assigned_technicians,
            rescheduled_appointment_id=rescheduled_appointment_id,
            poa=poa,
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
