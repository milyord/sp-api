from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.appointment_time_input import AppointmentTimeInput


T = TypeVar("T", bound="RescheduleAppointmentRequest")


@attr.s(auto_attribs=True)
class RescheduleAppointmentRequest:
    r"""Input for rescheduled appointment operation.

    Attributes:
        appointment_time (AppointmentTimeInput): The input appointment time details.
        reschedule_reason_code (str): The appointment reschedule reason code.
    """

    appointment_time: "AppointmentTimeInput"
    reschedule_reason_code: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_time = self.appointment_time.to_dict()

        reschedule_reason_code = self.reschedule_reason_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appointmentTime": appointment_time,
                "rescheduleReasonCode": reschedule_reason_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_time_input import AppointmentTimeInput

        d = src_dict.copy()
        appointment_time = AppointmentTimeInput.from_dict(d.pop("appointmentTime"))

        reschedule_reason_code = d.pop("rescheduleReasonCode")

        result = cls(
            appointment_time=appointment_time,
            reschedule_reason_code=reschedule_reason_code,
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
