from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.unit_of_measurement import UnitOfMeasurement

T = TypeVar("T", bound="Dimensions")


@attr.s(auto_attribs=True)
class Dimensions:
    r"""The dimension values and unit of measurement.

    Attributes:
        length (float):
        width (float):
        height (float):
        unit (UnitOfMeasurement): Indicates the unit of measurement.
    """

    length: float
    width: float
    height: float
    unit: UnitOfMeasurement
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
                "Length": length,
                "Width": width,
                "Height": height,
                "Unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("Length")

        width = d.pop("Width")

        height = d.pop("Height")

        unit = UnitOfMeasurement(d.pop("Unit"))

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
