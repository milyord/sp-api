from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.report_schedule import ReportSchedule


T = TypeVar("T", bound="ReportScheduleList")


@attr.s(auto_attribs=True)
class ReportScheduleList:
    r"""A list of report schedules.

    Attributes:
        report_schedules (List['ReportSchedule']):
    """

    report_schedules: List["ReportSchedule"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_schedules = []
        for report_schedules_item_data in self.report_schedules:
            report_schedules_item = report_schedules_item_data.to_dict()

            report_schedules.append(report_schedules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportSchedules": report_schedules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_schedule import ReportSchedule

        d = src_dict.copy()
        report_schedules = []
        _report_schedules = d.pop("reportSchedules")
        for report_schedules_item_data in _report_schedules:
            report_schedules_item = ReportSchedule.from_dict(report_schedules_item_data)

            report_schedules.append(report_schedules_item)

        result = cls(
            report_schedules=report_schedules,
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
