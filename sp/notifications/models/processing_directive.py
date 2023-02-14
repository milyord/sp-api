from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_filter import EventFilter


T = TypeVar("T", bound="ProcessingDirective")


@attr.s(auto_attribs=True)
class ProcessingDirective:
    r"""Additional information passed to the subscription to control the processing of notifications. For example, you can
    use an eventFilter to customize your subscription to send notifications for only the specified marketplaceId's, or
    select the aggregation time period at which to send notifications (e.g. limit to one notification every five minutes
    for high frequency notifications). The specific features available vary depending on the notificationType.

    This feature is limited to specific notificationTypes and is currently only supported by the ANY_OFFER_CHANGED
    notificationType.

        Attributes:
            event_filter (Union[Unset, EventFilter]): A notificationType specific filter. This object contains all of the
                currently available filters and properties that you can use to define a notificationType specific filter.
    """

    event_filter: Union[Unset, "EventFilter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_filter, Unset):
            event_filter = self.event_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_filter is not UNSET:
            field_dict["eventFilter"] = event_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_filter import EventFilter

        d = src_dict.copy()
        _event_filter = d.pop("eventFilter", UNSET)
        event_filter: Union[Unset, EventFilter]
        if isinstance(_event_filter, Unset):
            event_filter = UNSET
        else:
            event_filter = EventFilter.from_dict(_event_filter)

        result = cls(
            event_filter=event_filter,
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
