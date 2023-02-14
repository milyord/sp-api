from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.weight_unit import WeightUnit

T = TypeVar("T", bound="Weight")


@attr.s(auto_attribs=True)
class Weight:
    r"""The weight.

    Attributes:
        unit (WeightUnit): The unit of weight.
        value (str): The weight value.
    """

    unit: WeightUnit
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = WeightUnit(d.pop("unit"))

        value = d.pop("value")

        result = cls(
            unit=unit,
            value=value,
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
