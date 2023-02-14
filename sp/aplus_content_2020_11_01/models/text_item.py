from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="TextItem")


@attr.s(auto_attribs=True)
class TextItem:
    r"""Rich positional text, usually presented as a collection of bullet points.

    Attributes:
        position (int): The rank or index of this text item within the collection. Different items cannot occupy the
            same position within a single collection.
        text (TextComponent): Rich text content.
    """

    position: int
    text: "TextComponent"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        text = self.text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        position = d.pop("position")

        text = TextComponent.from_dict(d.pop("text"))

        result = cls(
            position=position,
            text=text,
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
