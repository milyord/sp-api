from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.dimensions_unit import DimensionsUnit

T = TypeVar("T", bound="Dimensions")


@attr.s(auto_attribs=True)
class Dimensions:
    r"""A set of measurements for a three-dimensional object.

    Attributes:
        length (float): The length of the container.
        width (float): The width of the container.
        height (float): The height of the container.
        unit (DimensionsUnit): The unit of these measurements.
    """

    length: float
    width: float
    height: float
    unit: DimensionsUnit
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        length = self.length
        width = self.width
        height = self.height
        unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "length": length,
                "width": width,
                "height": height,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("length")

        width = d.pop("width")

        height = d.pop("height")

        unit = DimensionsUnit(d.pop("unit"))

        result = cls(
            length=length,
            width=width,
            height=height,
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
