from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paragraph_component import ParagraphComponent
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardTextModule")


@attr.s(auto_attribs=True)
class StandardTextModule:
    r"""A standard headline and body text.

    Attributes:
        body (ParagraphComponent): A list of rich text content, usually presented in a text box.
        headline (Union[Unset, TextComponent]): Rich text content.
    """

    body: "ParagraphComponent"
    headline: Union[Unset, "TextComponent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body.to_dict()

        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if headline is not UNSET:
            field_dict["headline"] = headline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.paragraph_component import ParagraphComponent
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        body = ParagraphComponent.from_dict(d.pop("body"))

        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        result = cls(
            body=body,
            headline=headline,
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
