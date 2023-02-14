from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension import Dimension


T = TypeVar("T", bound="Dimensions")


@attr.s(auto_attribs=True)
class Dimensions:
    r"""Dimensions of an Amazon catalog item or item in its packaging.

    Attributes:
        height (Union[Unset, Dimension]): Individual dimension value of an Amazon catalog item or item package.
        length (Union[Unset, Dimension]): Individual dimension value of an Amazon catalog item or item package.
        weight (Union[Unset, Dimension]): Individual dimension value of an Amazon catalog item or item package.
        width (Union[Unset, Dimension]): Individual dimension value of an Amazon catalog item or item package.
    """

    height: Union[Unset, "Dimension"] = UNSET
    length: Union[Unset, "Dimension"] = UNSET
    weight: Union[Unset, "Dimension"] = UNSET
    width: Union[Unset, "Dimension"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        height: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        length: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.length, Unset):
            length = self.length.to_dict()

        weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        width: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if weight is not UNSET:
            field_dict["weight"] = weight
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimension import Dimension

        d = src_dict.copy()
        _height = d.pop("height", UNSET)
        height: Union[Unset, Dimension]
        if isinstance(_height, Unset):
            height = UNSET
        else:
            height = Dimension.from_dict(_height)

        _length = d.pop("length", UNSET)
        length: Union[Unset, Dimension]
        if isinstance(_length, Unset):
            length = UNSET
        else:
            length = Dimension.from_dict(_length)

        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, Dimension]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Dimension.from_dict(_weight)

        _width = d.pop("width", UNSET)
        width: Union[Unset, Dimension]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = Dimension.from_dict(_width)

        result = cls(
            height=height,
            length=length,
            weight=weight,
            width=width,
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
