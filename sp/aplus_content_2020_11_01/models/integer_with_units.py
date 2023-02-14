from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="IntegerWithUnits")


@attr.s(auto_attribs=True)
class IntegerWithUnits:
    r"""A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.

    Attributes:
        value (int): The dimension value.
        units (str): The unit of measurement.
    """

    value: int
    units: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "units": units,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        units = d.pop("units")

        result = cls(
            value=value,
            units=units,
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
