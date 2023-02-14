import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="Event")


@attr.s(auto_attribs=True)
class Event:
    r"""An event of a shipment

    Attributes:
        event_code (str): The event code of a shipment, such as Departed, Received, and ReadyForReceive.
        event_time (datetime.datetime): The date and time of an event for a shipment.
        location (Union[Unset, Location]): The location where the person, business or institution is located.
    """

    event_code: str
    event_time: datetime.datetime
    location: Union[Unset, "Location"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_code = self.event_code
        event_time = self.event_time.isoformat()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventCode": event_code,
                "eventTime": event_time,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location import Location

        d = src_dict.copy()
        event_code = d.pop("eventCode")

        event_time = isoparse(d.pop("eventTime"))

        _location = d.pop("location", UNSET)
        location: Union[Unset, Location]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Location.from_dict(_location)

        result = cls(
            event_code=event_code,
            event_time=event_time,
            location=location,
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
