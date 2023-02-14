import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_options import ReportOptions


T = TypeVar("T", bound="ReportSchedule")


@attr.s(auto_attribs=True)
class ReportSchedule:
    r"""Detailed information about a report schedule.

    Attributes:
        report_schedule_id (str): The identifier for the report schedule. This identifier is unique only in combination
            with a seller ID.
        report_type (str): The report type.
        period (str): An ISO 8601 period value that indicates how often a report should be created.
        marketplace_ids (Union[Unset, List[str]]): A list of marketplace identifiers. The report document's contents
            will contain data for all of the specified marketplaces, unless the report type indicates otherwise.
        report_options (Union[Unset, ReportOptions]): Additional information passed to reports. This varies by report
            type.
        next_report_creation_time (Union[Unset, datetime.datetime]): The date and time when the schedule will create its
            next report, in ISO 8601 date time format.
    """

    report_schedule_id: str
    report_type: str
    period: str
    marketplace_ids: Union[Unset, List[str]] = UNSET
    report_options: Union[Unset, "ReportOptions"] = UNSET
    next_report_creation_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_schedule_id = self.report_schedule_id
        report_type = self.report_type
        period = self.period
        marketplace_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.marketplace_ids, Unset):
            marketplace_ids = self.marketplace_ids

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
                "reportScheduleId": report_schedule_id,
                "reportType": report_type,
                "period": period,
            }
        )
        if marketplace_ids is not UNSET:
            field_dict["marketplaceIds"] = marketplace_ids
        if report_options is not UNSET:
            field_dict["reportOptions"] = report_options
        if next_report_creation_time is not UNSET:
            field_dict["nextReportCreationTime"] = next_report_creation_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_options import ReportOptions

        d = src_dict.copy()
        report_schedule_id = d.pop("reportScheduleId")

        report_type = d.pop("reportType")

        period = d.pop("period")

        marketplace_ids = cast(List[str], d.pop("marketplaceIds", UNSET))

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
            report_schedule_id=report_schedule_id,
            report_type=report_type,
            period=period,
            marketplace_ids=marketplace_ids,
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
