from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.duration_duration_unit import DurationDurationUnit

T = TypeVar("T", bound="Duration")


@attr.s(auto_attribs=True)
class Duration:
    r"""
    Attributes:
        duration_unit (DurationDurationUnit): Unit for duration.
        duration_value (int): Value for the duration in terms of the durationUnit.
    """

    duration_unit: DurationDurationUnit
    duration_value: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration_unit = self.duration_unit.value

        duration_value = self.duration_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "durationUnit": duration_unit,
                "durationValue": duration_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duration_unit = DurationDurationUnit(d.pop("durationUnit"))

        duration_value = d.pop("durationValue")

        result = cls(
            duration_unit=duration_unit,
            duration_value=duration_value,
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
