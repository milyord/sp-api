from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.appointment_time_input import AppointmentTimeInput


T = TypeVar("T", bound="AddAppointmentRequest")


@attr.s(auto_attribs=True)
class AddAppointmentRequest:
    r"""Input for add appointment operation.

    Attributes:
        appointment_time (AppointmentTimeInput): The input appointment time details.
    """

    appointment_time: "AppointmentTimeInput"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_time = self.appointment_time.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appointmentTime": appointment_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_time_input import AppointmentTimeInput

        d = src_dict.copy()
        appointment_time = AppointmentTimeInput.from_dict(d.pop("appointmentTime"))

        result = cls(
            appointment_time=appointment_time,
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
