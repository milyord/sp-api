import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.create_report_schedule_specification_period import CreateReportScheduleSpecificationPeriod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_options import ReportOptions


T = TypeVar("T", bound="CreateReportScheduleSpecification")


@attr.s(auto_attribs=True)
class CreateReportScheduleSpecification:
    r"""
    Attributes:
        report_type (str): The report type.
        marketplace_ids (List[str]): A list of marketplace identifiers for the report schedule.
        period (CreateReportScheduleSpecificationPeriod): One of a set of predefined ISO 8601 periods that specifies how
            often a report should be created.
        report_options (Union[Unset, ReportOptions]): Additional information passed to reports. This varies by report
            type.
        next_report_creation_time (Union[Unset, datetime.datetime]): The date and time when the schedule will create its
            next report, in ISO 8601 date time format.
    """

    report_type: str
    marketplace_ids: List[str]
    period: CreateReportScheduleSpecificationPeriod
    report_options: Union[Unset, "ReportOptions"] = UNSET
    next_report_creation_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_type = self.report_type
        marketplace_ids = self.marketplace_ids

        period = self.period.value

        report_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_options, Unset):
            report_options = self.report_options.to_dict()

        next_report_creation_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_report_creation_time, Unset):
            next_report_creation_time = self.next_report_creation_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportType": report_type,
                "marketplaceIds": marketplace_ids,
                "period": period,
            }
        )
        if report_options is not UNSET:
            field_dict["reportOptions"] = report_options
        if next_report_creation_time is not UNSET:
            field_dict["nextReportCreationTime"] = next_report_creation_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_options import ReportOptions

        d = src_dict.copy()
        report_type = d.pop("reportType")

        marketplace_ids = cast(List[str], d.pop("marketplaceIds"))

        period = CreateReportScheduleSpecificationPeriod(d.pop("period"))

        _report_options = d.pop("reportOptions", UNSET)
        report_options: Union[Unset, ReportOptions]
        if isinstance(_report_options, Unset):
            report_options = UNSET
        else:
            report_options = ReportOptions.from_dict(_report_options)

        _next_report_creation_time = d.pop("nextReportCreationTime", UNSET)
        next_report_creation_time: Union[Unset, datetime.datetime]
        if isinstance(_next_report_creation_time, Unset):
            next_report_creation_time = UNSET
        else:
            next_report_creation_time = isoparse(_next_report_creation_time)

        result = cls(
            report_type=report_type,
            marketplace_ids=marketplace_ids,
            period=period,
            report_options=report_options,
            next_report_creation_time=next_report_creation_time,
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
