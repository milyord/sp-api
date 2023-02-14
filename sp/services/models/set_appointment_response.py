from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.warning import Warning_


T = TypeVar("T", bound="SetAppointmentResponse")


@attr.s(auto_attribs=True)
class SetAppointmentResponse:
    r"""Response schema for the `addAppointmentForServiceJobByServiceJobId` and
    `rescheduleAppointmentForServiceJobByServiceJobId` operations.

        Attributes:
            appointment_id (Union[Unset, str]): The appointment identifier.
            warnings (Union[Unset, List['Warning_']]): A list of warnings returned in the sucessful execution response of an
                API request.
            errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    appointment_id: Union[Unset, str] = UNSET
    warnings: Union[Unset, List["Warning_"]] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_id = self.appointment_id
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for componentsschemas_warning_list_item_data in self.warnings:
                componentsschemas_warning_list_item = componentsschemas_warning_list_item_data.to_dict()

                warnings.append(componentsschemas_warning_list_item)

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemas_error_list_item_data in self.errors:
                componentsschemas_error_list_item = componentsschemas_error_list_item_data.to_dict()

                errors.append(componentsschemas_error_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.warning import Warning_

        d = src_dict.copy()
        appointment_id = d.pop("appointmentId", UNSET)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for componentsschemas_warning_list_item_data in _warnings or []:
            componentsschemas_warning_list_item = Warning_.from_dict(componentsschemas_warning_list_item_data)

            warnings.append(componentsschemas_warning_list_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            appointment_id=appointment_id,
            warnings=warnings,
            errors=errors,
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
