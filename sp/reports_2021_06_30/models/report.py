import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.report_processing_status import ReportProcessingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Report")


@attr.s(auto_attribs=True)
class Report:
    r"""Detailed information about the report.

    Attributes:
        report_id (str): The identifier for the report. This identifier is unique only in combination with a seller ID.
        report_type (str): The report type.
        created_time (datetime.datetime): The date and time when the report was created.
        processing_status (ReportProcessingStatus): The processing status of the report.
        marketplace_ids (Union[Unset, List[str]]): A list of marketplace identifiers for the report.
        data_start_time (Union[Unset, datetime.datetime]): The start of a date and time range used for selecting the
            data to report.
        data_end_time (Union[Unset, datetime.datetime]): The end of a date and time range used for selecting the data to
            report.
        report_schedule_id (Union[Unset, str]): The identifier of the report schedule that created this report (if any).
            This identifier is unique only in combination with a seller ID.
        processing_start_time (Union[Unset, datetime.datetime]): The date and time when the report processing started,
            in ISO 8601 date time format.
        processing_end_time (Union[Unset, datetime.datetime]): The date and time when the report processing completed,
            in ISO 8601 date time format.
        report_document_id (Union[Unset, str]): The identifier for the report document. Pass this into the
            getReportDocument operation to get the information you will need to retrieve the report document's contents.
    """

    report_id: str
    report_type: str
    created_time: datetime.datetime
    processing_status: ReportProcessingStatus
    marketplace_ids: Union[Unset, List[str]] = UNSET
    data_start_time: Union[Unset, datetime.datetime] = UNSET
    data_end_time: Union[Unset, datetime.datetime] = UNSET
    report_schedule_id: Union[Unset, str] = UNSET
    processing_start_time: Union[Unset, datetime.datetime] = UNSET
    processing_end_time: Union[Unset, datetime.datetime] = UNSET
    report_document_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_id = self.report_id
        report_type = self.report_type
        created_time = self.created_time.isoformat()

        processing_status = self.processing_status.value

        marketplace_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.marketplace_ids, Unset):
            marketplace_ids = self.marketplace_ids

        data_start_time: Union[Unset, str] = UNSET
        if not isinstance(self.data_start_time, Unset):
            data_start_time = self.data_start_time.isoformat()

        data_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.data_end_time, Unset):
            data_end_time = self.data_end_time.isoformat()

        report_schedule_id = self.report_schedule_id
        processing_start_time: Union[Unset, str] = UNSET
        if not isinstance(self.processing_start_time, Unset):
            processing_start_time = self.processing_start_time.isoformat()

        processing_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.processing_end_time, Unset):
            processing_end_time = self.processing_end_time.isoformat()

        report_document_id = self.report_document_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "reportType": report_type,
                "createdTime": created_time,
                "processingStatus": processing_status,
            }
        )
        if marketplace_ids is not UNSET:
            field_dict["marketplaceIds"] = marketplace_ids
        if data_start_time is not UNSET:
            field_dict["dataStartTime"] = data_start_time
        if data_end_time is not UNSET:
            field_dict["dataEndTime"] = data_end_time
        if report_schedule_id is not UNSET:
            field_dict["reportScheduleId"] = report_schedule_id
        if processing_start_time is not UNSET:
            field_dict["processingStartTime"] = processing_start_time
        if processing_end_time is not UNSET:
            field_dict["processingEndTime"] = processing_end_time
        if report_document_id is not UNSET:
            field_dict["reportDocumentId"] = report_document_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        report_id = d.pop("reportId")

        report_type = d.pop("reportType")

        created_time = isoparse(d.pop("createdTime"))

        processing_status = ReportProcessingStatus(d.pop("processingStatus"))

        marketplace_ids = cast(List[str], d.pop("marketplaceIds", UNSET))

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

        report_schedule_id = d.pop("reportScheduleId", UNSET)

        _processing_start_time = d.pop("processingStartTime", UNSET)
        processing_start_time: Union[Unset, datetime.datetime]
        if isinstance(_processing_start_time, Unset):
            processing_start_time = UNSET
        else:
            processing_start_time = isoparse(_processing_start_time)

        _processing_end_time = d.pop("processingEndTime", UNSET)
        processing_end_time: Union[Unset, datetime.datetime]
        if isinstance(_processing_end_time, Unset):
            processing_end_time = UNSET
        else:
            processing_end_time = isoparse(_processing_end_time)

        report_document_id = d.pop("reportDocumentId", UNSET)

        result = cls(
            report_id=report_id,
            report_type=report_type,
            created_time=created_time,
            processing_status=processing_status,
            marketplace_ids=marketplace_ids,
            data_start_time=data_start_time,
            data_end_time=data_end_time,
            report_schedule_id=report_schedule_id,
            processing_start_time=processing_start_time,
            processing_end_time=processing_end_time,
            report_document_id=report_document_id,
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
