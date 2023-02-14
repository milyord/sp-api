from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_settings import AggregationSettings


T = TypeVar("T", bound="AggregationFilter")


@attr.s(auto_attribs=True)
class AggregationFilter:
    r"""Use this filter to select the aggregation time period at which to send notifications (e.g. limit to one notification
    every five minutes for high frequency notifications).

        Attributes:
            aggregation_settings (Union[Unset, AggregationSettings]): A container that holds all of the necessary properties
                to configure the aggregation of notifications.
    """

    aggregation_settings: Union[Unset, "AggregationSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregation_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregation_settings, Unset):
            aggregation_settings = self.aggregation_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_settings is not UNSET:
            field_dict["aggregationSettings"] = aggregation_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aggregation_settings import AggregationSettings

        d = src_dict.copy()
        _aggregation_settings = d.pop("aggregationSettings", UNSET)
        aggregation_settings: Union[Unset, AggregationSettings]
        if isinstance(_aggregation_settings, Unset):
            aggregation_settings = UNSET
        else:
            aggregation_settings = AggregationSettings.from_dict(_aggregation_settings)

        result = cls(
            aggregation_settings=aggregation_settings,
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
