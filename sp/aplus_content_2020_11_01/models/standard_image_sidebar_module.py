from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_image_caption_block import StandardImageCaptionBlock
    from ..models.standard_image_text_block import StandardImageTextBlock
    from ..models.standard_text_block import StandardTextBlock
    from ..models.standard_text_list_block import StandardTextListBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardImageSidebarModule")


@attr.s(auto_attribs=True)
class StandardImageSidebarModule:
    r"""Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar.

    Attributes:
        headline (Union[Unset, TextComponent]): Rich text content.
        image_caption_block (Union[Unset, StandardImageCaptionBlock]): The A+ Content standard image and caption block.
        description_text_block (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of a
            paragraph with a headline.
        description_list_block (Union[Unset, StandardTextListBlock]): The A+ Content standard fixed length list of text,
            usually presented as bullet points.
        sidebar_image_text_block (Union[Unset, StandardImageTextBlock]): The A+ Content standard image and text box
            block.
        sidebar_list_block (Union[Unset, StandardTextListBlock]): The A+ Content standard fixed length list of text,
            usually presented as bullet points.
    """

    headline: Union[Unset, "TextComponent"] = UNSET
    image_caption_block: Union[Unset, "StandardImageCaptionBlock"] = UNSET
    description_text_block: Union[Unset, "StandardTextBlock"] = UNSET
    description_list_block: Union[Unset, "StandardTextListBlock"] = UNSET
    sidebar_image_text_block: Union[Unset, "StandardImageTextBlock"] = UNSET
    sidebar_list_block: Union[Unset, "StandardTextListBlock"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        image_caption_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_caption_block, Unset):
            image_caption_block = self.image_caption_block.to_dict()

        description_text_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_text_block, Unset):
            description_text_block = self.description_text_block.to_dict()

        description_list_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_list_block, Unset):
            description_list_block = self.description_list_block.to_dict()

        sidebar_image_text_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sidebar_image_text_block, Unset):
            sidebar_image_text_block = self.sidebar_image_text_block.to_dict()

        sidebar_list_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sidebar_list_block, Unset):
            sidebar_list_block = self.sidebar_list_block.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if image_caption_block is not UNSET:
            field_dict["imageCaptionBlock"] = image_caption_block
        if description_text_block is not UNSET:
            field_dict["descriptionTextBlock"] = description_text_block
        if description_list_block is not UNSET:
            field_dict["descriptionListBlock"] = description_list_block
        if sidebar_image_text_block is not UNSET:
            field_dict["sidebarImageTextBlock"] = sidebar_image_text_block
        if sidebar_list_block is not UNSET:
            field_dict["sidebarListBlock"] = sidebar_list_block

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_image_caption_block import StandardImageCaptionBlock
        from ..models.standard_image_text_block import StandardImageTextBlock
        from ..models.standard_text_block import StandardTextBlock
        from ..models.standard_text_list_block import StandardTextListBlock
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        _image_caption_block = d.pop("imageCaptionBlock", UNSET)
        image_caption_block: Union[Unset, StandardImageCaptionBlock]
        if isinstance(_image_caption_block, Unset):
            image_caption_block = UNSET
        else:
            image_caption_block = StandardImageCaptionBlock.from_dict(_image_caption_block)

        _description_text_block = d.pop("descriptionTextBlock", UNSET)
        description_text_block: Union[Unset, StandardTextBlock]
        if isinstance(_description_text_block, Unset):
            description_text_block = UNSET
        else:
            description_text_block = StandardTextBlock.from_dict(_description_text_block)

        _description_list_block = d.pop("descriptionListBlock", UNSET)
        description_list_block: Union[Unset, StandardTextListBlock]
        if isinstance(_description_list_block, Unset):
            description_list_block = UNSET
        else:
            description_list_block = StandardTextListBlock.from_dict(_description_list_block)

        _sidebar_image_text_block = d.pop("sidebarImageTextBlock", UNSET)
        sidebar_image_text_block: Union[Unset, StandardImageTextBlock]
        if isinstance(_sidebar_image_text_block, Unset):
            sidebar_image_text_block = UNSET
        else:
            sidebar_image_text_block = StandardImageTextBlock.from_dict(_sidebar_image_text_block)

        _sidebar_list_block = d.pop("sidebarListBlock", UNSET)
        sidebar_list_block: Union[Unset, StandardTextListBlock]
        if isinstance(_sidebar_list_block, Unset):
            sidebar_list_block = UNSET
        else:
            sidebar_list_block = StandardTextListBlock.from_dict(_sidebar_list_block)

        result = cls(
            headline=headline,
            image_caption_block=image_caption_block,
            description_text_block=description_text_block,
            description_list_block=description_list_block,
            sidebar_image_text_block=sidebar_image_text_block,
            sidebar_list_block=sidebar_list_block,
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
