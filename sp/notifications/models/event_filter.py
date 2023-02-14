from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_settings import AggregationSettings


T = TypeVar("T", bound="EventFilter")


@attr.s(auto_attribs=True)
class EventFilter:
    r"""A notificationType specific filter. This object contains all of the currently available filters and properties that
    you can use to define a notificationType specific filter.

        Attributes:
            event_filter_type (str): An eventFilterType value that is supported by the specific notificationType. This is
                used by the subscription service to determine the type of event filter. Refer to the section of the
                [Notifications Use Case Guide](doc:notifications-api-v1-use-case-guide) that describes the specific
                notificationType to determine if an eventFilterType is supported.
            aggregation_settings (Union[Unset, AggregationSettings]): A container that holds all of the necessary properties
                to configure the aggregation of notifications.
            marketplace_ids (Union[Unset, List[str]]): A list of marketplace identifiers to subscribe to (e.g.
                ATVPDKIKX0DER). To receive notifications in every marketplace, do not provide this list.
    """

    event_filter_type: str
    aggregation_settings: Union[Unset, "AggregationSettings"] = UNSET
    marketplace_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_filter_type = self.event_filter_type
        aggregation_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregation_settings, Unset):
            aggregation_settings = self.aggregation_settings.to_dict()

        marketplace_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.marketplace_ids, Unset):
            marketplace_ids = self.marketplace_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventFilterType": event_filter_type,
            }
        )
        if aggregation_settings is not UNSET:
            field_dict["aggregationSettings"] = aggregation_settings
        if marketplace_ids is not UNSET:
            field_dict["marketplaceIds"] = marketplace_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_settings import AggregationSettings

        d = src_dict.copy()
        event_filter_type = d.pop("eventFilterType")

        _aggregation_settings = d.pop("aggregationSettings", UNSET)
        aggregation_settings: Union[Unset, AggregationSettings]
        if isinstance(_aggregation_settings, Unset):
            aggregation_settings = UNSET
        else:
            aggregation_settings = AggregationSettings.from_dict(_aggregation_settings)

        marketplace_ids = cast(List[str], d.pop("marketplaceIds", UNSET))

        result = cls(
            event_filter_type=event_filter_type,
            aggregation_settings=aggregation_settings,
            marketplace_ids=marketplace_ids,
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
