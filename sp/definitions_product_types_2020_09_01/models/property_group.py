from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyGroup")


@attr.s(auto_attribs=True)
class PropertyGroup:
    r"""A property group represents a logical grouping of schema properties that can be used for display or informational
    purposes.

        Attributes:
            title (Union[Unset, str]): The display label of the property group.
            description (Union[Unset, str]): The description of the property group.
            property_names (Union[Unset, List[str]]): The names of the schema properties for the property group.
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    property_names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        property_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_names, Unset):
            property_names = self.property_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if property_names is not UNSET:
            field_dict["propertyNames"] = property_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        property_names = cast(List[str], d.pop("propertyNames", UNSET))

        result = cls(
            title=title,
            description=description,
            property_names=property_names,
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
