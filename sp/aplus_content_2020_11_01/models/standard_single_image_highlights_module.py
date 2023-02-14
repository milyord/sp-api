from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_component import ImageComponent
    from ..models.standard_header_text_list_block import StandardHeaderTextListBlock
    from ..models.standard_text_block import StandardTextBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardSingleImageHighlightsModule")


@attr.s(auto_attribs=True)
class StandardSingleImageHighlightsModule:
    r"""A standard image with several paragraphs and a bulleted list.

    Attributes:
        image (Union[Unset, ImageComponent]): A reference to an image, hosted in the A+ Content media library.
        headline (Union[Unset, TextComponent]): Rich text content.
        text_block_1 (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of a paragraph
            with a headline.
        text_block_2 (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of a paragraph
            with a headline.
        text_block_3 (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of a paragraph
            with a headline.
        bulleted_list_block (Union[Unset, StandardHeaderTextListBlock]): The A+ standard fixed-length list of text, with
            a related headline.
    """

    image: Union[Unset, "ImageComponent"] = UNSET
    headline: Union[Unset, "TextComponent"] = UNSET
    text_block_1: Union[Unset, "StandardTextBlock"] = UNSET
    text_block_2: Union[Unset, "StandardTextBlock"] = UNSET
    text_block_3: Union[Unset, "StandardTextBlock"] = UNSET
    bulleted_list_block: Union[Unset, "StandardHeaderTextListBlock"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        text_block_1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text_block_1, Unset):
            text_block_1 = self.text_block_1.to_dict()

        text_block_2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text_block_2, Unset):
            text_block_2 = self.text_block_2.to_dict()

        text_block_3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text_block_3, Unset):
            text_block_3 = self.text_block_3.to_dict()

        bulleted_list_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bulleted_list_block, Unset):
            bulleted_list_block = self.bulleted_list_block.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if headline is not UNSET:
            field_dict["headline"] = headline
        if text_block_1 is not UNSET:
            field_dict["textBlock1"] = text_block_1
        if text_block_2 is not UNSET:
            field_dict["textBlock2"] = text_block_2
        if text_block_3 is not UNSET:
            field_dict["textBlock3"] = text_block_3
        if bulleted_list_block is not UNSET:
            field_dict["bulletedListBlock"] = bulleted_list_block

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_component import ImageComponent
        from ..models.standard_header_text_list_block import StandardHeaderTextListBlock
        from ..models.standard_text_block import StandardTextBlock
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

        _text_block_1 = d.pop("textBlock1", UNSET)
        text_block_1: Union[Unset, StandardTextBlock]
        if isinstance(_text_block_1, Unset):
            text_block_1 = UNSET
        else:
            text_block_1 = StandardTextBlock.from_dict(_text_block_1)

        _text_block_2 = d.pop("textBlock2", UNSET)
        text_block_2: Union[Unset, StandardTextBlock]
        if isinstance(_text_block_2, Unset):
            text_block_2 = UNSET
        else:
            text_block_2 = StandardTextBlock.from_dict(_text_block_2)

        _text_block_3 = d.pop("textBlock3", UNSET)
        text_block_3: Union[Unset, StandardTextBlock]
        if isinstance(_text_block_3, Unset):
            text_block_3 = UNSET
        else:
            text_block_3 = StandardTextBlock.from_dict(_text_block_3)

        _bulleted_list_block = d.pop("bulletedListBlock", UNSET)
        bulleted_list_block: Union[Unset, StandardHeaderTextListBlock]
        if isinstance(_bulleted_list_block, Unset):
            bulleted_list_block = UNSET
        else:
            bulleted_list_block = StandardHeaderTextListBlock.from_dict(_bulleted_list_block)

        result = cls(
            image=image,
            headline=headline,
            text_block_1=text_block_1,
            text_block_2=text_block_2,
            text_block_3=text_block_3,
            bulleted_list_block=bulleted_list_block,
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
