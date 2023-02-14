from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_component import ImageComponent
    from ..models.paragraph_component import ParagraphComponent
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardImageTextBlock")


@attr.s(auto_attribs=True)
class StandardImageTextBlock:
    r"""The A+ Content standard image and text box block.

    Attributes:
        image (Union[Unset, ImageComponent]): A reference to an image, hosted in the A+ Content media library.
        headline (Union[Unset, TextComponent]): Rich text content.
        body (Union[Unset, ParagraphComponent]): A list of rich text content, usually presented in a text box.
    """

    image: Union[Unset, "ImageComponent"] = UNSET
    headline: Union[Unset, "TextComponent"] = UNSET
    body: Union[Unset, "ParagraphComponent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        body: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if headline is not UNSET:
            field_dict["headline"] = headline
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_component import ImageComponent
        from ..models.paragraph_component import ParagraphComponent
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _image = d.pop("image", UNSET)
        image: Union[Unset, ImageComponent]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ImageComponent.from_dict(_image)

        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        _body = d.pop("body", UNSET)
        body: Union[Unset, ParagraphComponent]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = ParagraphComponent.from_dict(_body)

        result = cls(
            image=image,
            headline=headline,
            body=body,
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
