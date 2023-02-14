import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.handover_method import HandoverMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeSlot")


@attr.s(auto_attribs=True)
class TimeSlot:
    r"""A time window to hand over an Easy Ship package to Amazon Logistics.

    Attributes:
        slot_id (str): A string of up to 255 characters.
        start_time (Union[Unset, datetime.datetime]): A datetime value in ISO 8601 format.
        end_time (Union[Unset, datetime.datetime]): A datetime value in ISO 8601 format.
        handover_method (Union[Unset, HandoverMethod]): Identifies the method by which a seller will hand a package over
            to Amazon Logistics.
    """

    slot_id: str
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    handover_method: Union[Unset, HandoverMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slot_id = self.slot_id
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        handover_method: Union[Unset, str] = UNSET
        if not isinstance(self.handover_method, Unset):
            handover_method = self.handover_method.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slotId": slot_id,
            }
        )
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if handover_method is not UNSET:
            field_dict["handoverMethod"] = handover_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slot_id = d.pop("slotId")

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _handover_method = d.pop("handoverMethod", UNSET)
        handover_method: Union[Unset, HandoverMethod]
        if isinstance(_handover_method, Unset):
            handover_method = UNSET
        else:
            handover_method = HandoverMethod(_handover_method)

        result = cls(
            slot_id=slot_id,
            start_time=start_time,
            end_time=end_time,
            handover_method=handover_method,
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
