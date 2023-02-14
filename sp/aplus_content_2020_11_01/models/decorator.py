from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.decorator_type import DecoratorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Decorator")


@attr.s(auto_attribs=True)
class Decorator:
    r"""A decorator applied to a content string value in order to create rich text.

    Attributes:
        type (Union[Unset, DecoratorType]): The type of rich text decorator.
        offset (Union[Unset, int]): The starting character of this decorator within the content string. Use zero for the
            first character.
        length (Union[Unset, int]): The number of content characters to alter with this decorator. Decorators such as
            line breaks can have zero length and fit between characters.
        depth (Union[Unset, int]): The relative intensity or variation of this decorator. Decorators such as bullet-
            points, for example, can have multiple indentation depths.
    """

    type: Union[Unset, DecoratorType] = UNSET
    offset: Union[Unset, int] = UNSET
    length: Union[Unset, int] = UNSET
    depth: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        offset = self.offset
        length = self.length
        depth = self.depth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if offset is not UNSET:
            field_dict["offset"] = offset
        if length is not UNSET:
            field_dict["length"] = length
        if depth is not UNSET:
            field_dict["depth"] = depth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DecoratorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DecoratorType(_type)

        offset = d.pop("offset", UNSET)

        length = d.pop("length", UNSET)

        depth = d.pop("depth", UNSET)

        result = cls(
            type=type,
            offset=offset,
            length=length,
            depth=depth,
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
