from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateReportScheduleResult")


@attr.s(auto_attribs=True)
class CreateReportScheduleResult:
    r"""
    Attributes:
        report_schedule_id (str): The identifier for the report schedule. This identifier is unique only in combination
            with a seller ID.
    """

    report_schedule_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_schedule_id = self.report_schedule_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportScheduleId": report_schedule_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        report_schedule_id = d.pop("reportScheduleId")

        result = cls(
            report_schedule_id=report_schedule_id,
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
