import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.feed_processing_status import FeedProcessingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Feed")


@attr.s(auto_attribs=True)
class Feed:
    r"""Detailed information about the feed.

    Attributes:
        feed_id (str): The identifier for the feed. This identifier is unique only in combination with a seller ID.
        feed_type (str): The feed type.
        created_time (datetime.datetime): The date and time when the feed was created, in ISO 8601 date time format.
        processing_status (FeedProcessingStatus): The processing status of the feed.
        marketplace_ids (Union[Unset, List[str]]): A list of identifiers for the marketplaces that the feed is applied
            to.
        processing_start_time (Union[Unset, datetime.datetime]): The date and time when feed processing started, in ISO
            8601 date time format.
        processing_end_time (Union[Unset, datetime.datetime]): The date and time when feed processing completed, in ISO
            8601 date time format.
        result_feed_document_id (Union[Unset, str]): The identifier for the feed document. This identifier is unique
            only in combination with a seller ID.
    """

    feed_id: str
    feed_type: str
    created_time: datetime.datetime
    processing_status: FeedProcessingStatus
    marketplace_ids: Union[Unset, List[str]] = UNSET
    processing_start_time: Union[Unset, datetime.datetime] = UNSET
    processing_end_time: Union[Unset, datetime.datetime] = UNSET
    result_feed_document_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_id = self.feed_id
        feed_type = self.feed_type
        created_time = self.created_time.isoformat()

        processing_status = self.processing_status.value

        marketplace_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.marketplace_ids, Unset):
            marketplace_ids = self.marketplace_ids

        processing_start_time: Union[Unset, str] = UNSET
        if not isinstance(self.processing_start_time, Unset):
            processing_start_time = self.processing_start_time.isoformat()

        processing_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.processing_end_time, Unset):
            processing_end_time = self.processing_end_time.isoformat()

        result_feed_document_id = self.result_feed_document_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feedId": feed_id,
                "feedType": feed_type,
                "createdTime": created_time,
                "processingStatus": processing_status,
            }
        )
        if marketplace_ids is not UNSET:
            field_dict["marketplaceIds"] = marketplace_ids
        if processing_start_time is not UNSET:
            field_dict["processingStartTime"] = processing_start_time
        if processing_end_time is not UNSET:
            field_dict["processingEndTime"] = processing_end_time
        if result_feed_document_id is not UNSET:
            field_dict["resultFeedDocumentId"] = result_feed_document_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feed_id = d.pop("feedId")

        feed_type = d.pop("feedType")

        created_time = isoparse(d.pop("createdTime"))

        processing_status = FeedProcessingStatus(d.pop("processingStatus"))

        marketplace_ids = cast(List[str], d.pop("marketplaceIds", UNSET))

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

        result_feed_document_id = d.pop("resultFeedDocumentId", UNSET)

        result = cls(
            feed_id=feed_id,
            feed_type=feed_type,
            created_time=created_time,
            processing_status=processing_status,
            marketplace_ids=marketplace_ids,
            processing_start_time=processing_start_time,
            processing_end_time=processing_end_time,
            result_feed_document_id=result_feed_document_id,
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
