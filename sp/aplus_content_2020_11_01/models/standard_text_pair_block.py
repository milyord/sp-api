from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardTextPairBlock")


@attr.s(auto_attribs=True)
class StandardTextPairBlock:
    r"""The A+ Content standard label and description block, comprised of a pair of text components.

    Attributes:
        label (Union[Unset, TextComponent]): Rich text content.
        description (Union[Unset, TextComponent]): Rich text content.
    """

    label: Union[Unset, "TextComponent"] = UNSET
    description: Union[Unset, "TextComponent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _label = d.pop("label", UNSET)
        label: Union[Unset, TextComponent]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = TextComponent.from_dict(_label)

        _description = d.pop("description", UNSET)
        description: Union[Unset, TextComponent]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = TextComponent.from_dict(_description)

        result = cls(
            label=label,
            description=description,
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
