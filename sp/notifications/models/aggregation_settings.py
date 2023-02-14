from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.aggregation_time_period import AggregationTimePeriod

T = TypeVar("T", bound="AggregationSettings")


@attr.s(auto_attribs=True)
class AggregationSettings:
    r"""A container that holds all of the necessary properties to configure the aggregation of notifications.

    Attributes:
        aggregation_time_period (AggregationTimePeriod): The supported aggregation time periods. For example, if
            FiveMinutes is the value chosen, and 50 price updates occur for an ASIN within 5 minutes, Amazon will send only
            two notifications; one for the first event, and then a subsequent notification 5 minutes later with the final
            end state of the data. The 48 interim events will be dropped.
    """

    aggregation_time_period: AggregationTimePeriod
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregation_time_period = self.aggregation_time_period.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationTimePeriod": aggregation_time_period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aggregation_time_period = AggregationTimePeriod(d.pop("aggregationTimePeriod"))

        result = cls(
            aggregation_time_period=aggregation_time_period,
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
