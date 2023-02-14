from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanguageType")


@attr.s(auto_attribs=True)
class LanguageType:
    r"""The language type attribute of an item.

    Attributes:
        name (Union[Unset, str]): The name attribute of the item.
        type (Union[Unset, str]): The type attribute of the item.
        audio_format (Union[Unset, str]): The audio format attribute of the item.
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    audio_format: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        audio_format = self.audio_format

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if type is not UNSET:
            field_dict["Type"] = type
        if audio_format is not UNSET:
            field_dict["AudioFormat"] = audio_format

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        type = d.pop("Type", UNSET)

        audio_format = d.pop("AudioFormat", UNSET)

        result = cls(
            name=name,
            type=type,
            audio_format=audio_format,
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
