from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decimal_with_units import DecimalWithUnits


T = TypeVar("T", bound="Image")


@attr.s(auto_attribs=True)
class Image:
    r"""The image attribute of the item.

    Attributes:
        url (Union[Unset, str]): The image URL attribute of the item.
        height (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        width (Union[Unset, DecimalWithUnits]): The decimal value and unit.
    """

    url: Union[Unset, str] = UNSET
    height: Union[Unset, "DecimalWithUnits"] = UNSET
    width: Union[Unset, "DecimalWithUnits"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        height: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        width: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["URL"] = url
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.decimal_with_units import DecimalWithUnits

        d = src_dict.copy()
        url = d.pop("URL", UNSET)

        _height = d.pop("Height", UNSET)
        height: Union[Unset, DecimalWithUnits]
        if isinstance(_height, Unset):
            height = UNSET
        else:
            height = DecimalWithUnits.from_dict(_height)

        _width = d.pop("Width", UNSET)
        width: Union[Unset, DecimalWithUnits]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = DecimalWithUnits.from_dict(_width)

        result = cls(
            url=url,
            height=height,
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
