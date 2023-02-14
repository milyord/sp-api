from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.report_schedule import ReportSchedule


T = TypeVar("T", bound="GetReportSchedulesResponse")


@attr.s(auto_attribs=True)
class GetReportSchedulesResponse:
    r"""The response for the getReportSchedules operation.

    Attributes:
        payload (Union[Unset, List['ReportSchedule']]):
        errors (Union[Unset, List['Error']]): A list of error responses returned when a request is unsuccessful.
    """

    payload: Union[Unset, List["ReportSchedule"]] = UNSET
    errors: Union[Unset, List["Error"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = []
            for componentsschemas_report_schedule_list_item_data in self.payload:
                componentsschemas_report_schedule_list_item = componentsschemas_report_schedule_list_item_data.to_dict()

                payload.append(componentsschemas_report_schedule_list_item)

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemas_error_list_item_data in self.errors:
                componentsschemas_error_list_item = componentsschemas_error_list_item_data.to_dict()

                errors.append(componentsschemas_error_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error
        from ..models.report_schedule import ReportSchedule

        d = src_dict.copy()
        payload = []
        _payload = d.pop("payload", UNSET)
        for componentsschemas_report_schedule_list_item_data in _payload or []:
            componentsschemas_report_schedule_list_item = ReportSchedule.from_dict(
                componentsschemas_report_schedule_list_item_data
            )

            payload.append(componentsschemas_report_schedule_list_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_error_list_item_data in _errors or []:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            errors.append(componentsschemas_error_list_item)

        result = cls(
            payload=payload,
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
