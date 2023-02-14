from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemVariationTheme")


@attr.s(auto_attribs=True)
class ItemVariationTheme:
    r"""Variation theme indicating the combination of Amazon item catalog attributes that define the variation family.

    Attributes:
        attributes (Union[Unset, List[str]]): Names of the Amazon catalog item attributes associated with the variation
            theme.
        theme (Union[Unset, str]): Variation theme indicating the combination of Amazon item catalog attributes that
            define the variation family. Example: COLOR_NAME/STYLE_NAME.
    """

    attributes: Union[Unset, List[str]] = UNSET
    theme: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        theme = self.theme

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if theme is not UNSET:
            field_dict["theme"] = theme

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = cast(List[str], d.pop("attributes", UNSET))

        theme = d.pop("theme", UNSET)

        result = cls(
            attributes=attributes,
            theme=theme,
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
