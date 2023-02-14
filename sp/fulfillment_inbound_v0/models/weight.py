from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.unit_of_weight import UnitOfWeight

T = TypeVar("T", bound="Weight")


@attr.s(auto_attribs=True)
class Weight:
    r"""The weight of the package.

    Attributes:
        value (float):
        unit (UnitOfWeight): Indicates the unit of weight.
    """

    value: float
    unit: UnitOfWeight
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Value": value,
                "Unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("Value")

        unit = UnitOfWeight(d.pop("Unit"))

        result = cls(
            value=value,
            unit=unit,
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
