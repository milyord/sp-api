from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.unit_of_length import UnitOfLength
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dimensions")


@attr.s(auto_attribs=True)
class Dimensions:
    r"""The dimensions of the scheduled package.

    Attributes:
        length (Union[Unset, float]): The numerical value of the specified dimension.
        width (Union[Unset, float]): The numerical value of the specified dimension.
        height (Union[Unset, float]): The numerical value of the specified dimension.
        unit (Union[Unset, UnitOfLength]): The unit of measurement used to measure the length.
        identifier (Union[Unset, str]): A string of up to 255 characters.
    """

    length: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    unit: Union[Unset, UnitOfLength] = UNSET
    identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        length = self.length
        width = self.width
        height = self.height
        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        identifier = self.identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if unit is not UNSET:
            field_dict["unit"] = unit
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, UnitOfLength]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = UnitOfLength(_unit)

        identifier = d.pop("identifier", UNSET)

        result = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
            identifier=identifier,
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
