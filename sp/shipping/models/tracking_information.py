import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.tracking_summary import TrackingSummary


T = TypeVar("T", bound="TrackingInformation")


@attr.s(auto_attribs=True)
class TrackingInformation:
    r"""The payload schema for the getTrackingInformation operation.

    Attributes:
        tracking_id (str): The tracking id generated to each shipment. It contains a series of letters or digits or
            both.
        summary (TrackingSummary): The tracking summary.
        promised_delivery_date (datetime.datetime): The promised delivery date and time of a shipment.
        event_history (List['Event']): A list of events of a shipment.
    """

    tracking_id: str
    summary: "TrackingSummary"
    promised_delivery_date: datetime.datetime
    event_history: List["Event"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracking_id = self.tracking_id
        summary = self.summary.to_dict()

        promised_delivery_date = self.promised_delivery_date.isoformat()

        event_history = []
        for componentsschemas_event_list_item_data in self.event_history:
            componentsschemas_event_list_item = componentsschemas_event_list_item_data.to_dict()

            event_history.append(componentsschemas_event_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trackingId": tracking_id,
                "summary": summary,
                "promisedDeliveryDate": promised_delivery_date,
                "eventHistory": event_history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event
        from ..models.tracking_summary import TrackingSummary

        d = src_dict.copy()
        tracking_id = d.pop("trackingId")

        summary = TrackingSummary.from_dict(d.pop("summary"))

        promised_delivery_date = isoparse(d.pop("promisedDeliveryDate"))

        event_history = []
        _event_history = d.pop("eventHistory")
        for componentsschemas_event_list_item_data in _event_history:
            componentsschemas_event_list_item = Event.from_dict(componentsschemas_event_list_item_data)

            event_history.append(componentsschemas_event_list_item)

        result = cls(
            tracking_id=tracking_id,
            summary=summary,
            promised_delivery_date=promised_delivery_date,
            event_history=event_history,
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
