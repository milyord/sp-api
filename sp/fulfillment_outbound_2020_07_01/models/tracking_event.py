import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.event_code import EventCode

if TYPE_CHECKING:
    from ..models.tracking_address import TrackingAddress


T = TypeVar("T", bound="TrackingEvent")


@attr.s(auto_attribs=True)
class TrackingEvent:
    r"""Information for tracking package deliveries.

    Attributes:
        event_date (datetime.datetime):
        event_address (TrackingAddress): Address information for tracking the package.
        event_code (EventCode): The event code for the delivery event.
        event_description (str): A description for the corresponding event code.
    """

    event_date: datetime.datetime
    event_address: "TrackingAddress"
    event_code: EventCode
    event_description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_date = self.event_date.isoformat()

        event_address = self.event_address.to_dict()

        event_code = self.event_code.value

        event_description = self.event_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventDate": event_date,
                "eventAddress": event_address,
                "eventCode": event_code,
                "eventDescription": event_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tracking_address import TrackingAddress

        d = src_dict.copy()
        event_date = isoparse(d.pop("eventDate"))

        event_address = TrackingAddress.from_dict(d.pop("eventAddress"))

        event_code = EventCode(d.pop("eventCode"))

        event_description = d.pop("eventDescription")

        result = cls(
            event_date=event_date,
            event_address=event_address,
            event_code=event_code,
            event_description=event_description,
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
