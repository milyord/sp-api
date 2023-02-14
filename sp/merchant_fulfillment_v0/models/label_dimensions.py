from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.unit_of_length import UnitOfLength

T = TypeVar("T", bound="LabelDimensions")


@attr.s(auto_attribs=True)
class LabelDimensions:
    r"""Dimensions for printing a shipping label.

    Attributes:
        length (float): A label dimension.
        width (float): A label dimension.
        unit (UnitOfLength): The unit of length.
    """

    length: float
    width: float
    unit: UnitOfLength
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        length = self.length
        width = self.width
        unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Length": length,
                "Width": width,
                "Unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("Length")

        width = d.pop("Width")

        unit = UnitOfLength(d.pop("Unit"))

        result = cls(
            length=length,
            width=width,
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
