from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="ParagraphComponent")


@attr.s(auto_attribs=True)
class ParagraphComponent:
    r"""A list of rich text content, usually presented in a text box.

    Attributes:
        text_list (List['TextComponent']):
    """

    text_list: List["TextComponent"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text_list = []
        for text_list_item_data in self.text_list:
            text_list_item = text_list_item_data.to_dict()

            text_list.append(text_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "textList": text_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        text_list = []
        _text_list = d.pop("textList")
        for text_list_item_data in _text_list:
            text_list_item = TextComponent.from_dict(text_list_item_data)

            text_list.append(text_list_item)

        result = cls(
            text_list=text_list,
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
