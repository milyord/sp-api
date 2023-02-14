from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_of_length import UnitOfLength
from ..types import UNSET, Unset

T = TypeVar("T", bound="Length")


@attr.s(auto_attribs=True)
class Length:
    r"""The length.

    Attributes:
        value (Union[Unset, float]): The value in units.
        unit (Union[Unset, UnitOfLength]): The unit of length.
    """

    value: Union[Unset, float] = UNSET
    unit: Union[Unset, UnitOfLength] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, UnitOfLength]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = UnitOfLength(_unit)

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
