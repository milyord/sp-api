import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_options import ReportOptions


T = TypeVar("T", bound="CreateReportSpecification")


@attr.s(auto_attribs=True)
class CreateReportSpecification:
    r"""Information required to create the report.

    Attributes:
        report_type (str): The report type.
        marketplace_ids (List[str]): A list of marketplace identifiers. The report document's contents will contain data
            for all of the specified marketplaces, unless the report type indicates otherwise.
        report_options (Union[Unset, ReportOptions]): Additional information passed to reports. This varies by report
            type.
        data_start_time (Union[Unset, datetime.datetime]): The start of a date and time range, in ISO 8601 date time
            format, used for selecting the data to report. The default is now. The value must be prior to or equal to the
            current date and time. Not all report types make use of this.
        data_end_time (Union[Unset, datetime.datetime]): The end of a date and time range, in ISO 8601 date time format,
            used for selecting the data to report. The default is now. The value must be prior to or equal to the current
            date and time. Not all report types make use of this.
    """

    report_type: str
    marketplace_ids: List[str]
    report_options: Union[Unset, "ReportOptions"] = UNSET
    data_start_time: Union[Unset, datetime.datetime] = UNSET
    data_end_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_type = self.report_type
        marketplace_ids = self.marketplace_ids

        report_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_options, Unset):
            report_options = self.report_options.to_dict()

        data_start_time: Union[Unset, str] = UNSET
        if not isinstance(self.data_start_time, Unset):
            data_start_time = self.data_start_time.isoformat()

        data_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.data_end_time, Unset):
            data_end_time = self.data_end_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportType": report_type,
                "marketplaceIds": marketplace_ids,
            }
        )
        if report_options is not UNSET:
            field_dict["reportOptions"] = report_options
        if data_start_time is not UNSET:
            field_dict["dataStartTime"] = data_start_time
        if data_end_time is not UNSET:
            field_dict["dataEndTime"] = data_end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_options import ReportOptions

        d = src_dict.copy()
        report_type = d.pop("reportType")

        marketplace_ids = cast(List[str], d.pop("marketplaceIds"))

        _report_options = d.pop("reportOptions", UNSET)
        report_options: Union[Unset, ReportOptions]
        if isinstance(_report_options, Unset):
            report_options = UNSET
        else:
            report_options = ReportOptions.from_dict(_report_options)

        _data_start_time = d.pop("dataStartTime", UNSET)
        data_start_time: Union[Unset, datetime.datetime]
        if isinstance(_data_start_time, Unset):
            data_start_time = UNSET
        else:
            data_start_time = isoparse(_data_start_time)

        _data_end_time = d.pop("dataEndTime", UNSET)
        data_end_time: Union[Unset, datetime.datetime]
        if isinstance(_data_end_time, Unset):
            data_end_time = UNSET
        else:
            data_end_time = isoparse(_data_end_time)

        result = cls(
            report_type=report_type,
            marketplace_ids=marketplace_ids,
            report_options=report_options,
            data_start_time=data_start_time,
            data_end_time=data_end_time,
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
