from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_component import ImageComponent
    from ..models.standard_header_text_list_block import StandardHeaderTextListBlock
    from ..models.standard_text_block import StandardTextBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardSingleImageSpecsDetailModule")


@attr.s(auto_attribs=True)
class StandardSingleImageSpecsDetailModule:
    r"""A standard image with paragraphs and a bulleted list, and extra space for technical details.

    Attributes:
        headline (Union[Unset, TextComponent]): Rich text content.
        image (Union[Unset, ImageComponent]): A reference to an image, hosted in the A+ Content media library.
        description_headline (Union[Unset, TextComponent]): Rich text content.
        description_block_1 (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of a
            paragraph with a headline.
        description_block_2 (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of a
            paragraph with a headline.
        specification_headline (Union[Unset, TextComponent]): Rich text content.
        specification_list_block (Union[Unset, StandardHeaderTextListBlock]): The A+ standard fixed-length list of text,
            with a related headline.
        specification_text_block (Union[Unset, StandardTextBlock]): The A+ Content standard text box block, comprised of
            a paragraph with a headline.
    """

    headline: Union[Unset, "TextComponent"] = UNSET
    image: Union[Unset, "ImageComponent"] = UNSET
    description_headline: Union[Unset, "TextComponent"] = UNSET
    description_block_1: Union[Unset, "StandardTextBlock"] = UNSET
    description_block_2: Union[Unset, "StandardTextBlock"] = UNSET
    specification_headline: Union[Unset, "TextComponent"] = UNSET
    specification_list_block: Union[Unset, "StandardHeaderTextListBlock"] = UNSET
    specification_text_block: Union[Unset, "StandardTextBlock"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        description_headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_headline, Unset):
            description_headline = self.description_headline.to_dict()

        description_block_1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_block_1, Unset):
            description_block_1 = self.description_block_1.to_dict()

        description_block_2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_block_2, Unset):
            description_block_2 = self.description_block_2.to_dict()

        specification_headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.specification_headline, Unset):
            specification_headline = self.specification_headline.to_dict()

        specification_list_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.specification_list_block, Unset):
            specification_list_block = self.specification_list_block.to_dict()

        specification_text_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.specification_text_block, Unset):
            specification_text_block = self.specification_text_block.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if image is not UNSET:
            field_dict["image"] = image
        if description_headline is not UNSET:
            field_dict["descriptionHeadline"] = description_headline
        if description_block_1 is not UNSET:
            field_dict["descriptionBlock1"] = description_block_1
        if description_block_2 is not UNSET:
            field_dict["descriptionBlock2"] = description_block_2
        if specification_headline is not UNSET:
            field_dict["specificationHeadline"] = specification_headline
        if specification_list_block is not UNSET:
            field_dict["specificationListBlock"] = specification_list_block
        if specification_text_block is not UNSET:
            field_dict["specificationTextBlock"] = specification_text_block

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_component import ImageComponent
        from ..models.standard_header_text_list_block import StandardHeaderTextListBlock
        from ..models.standard_text_block import StandardTextBlock
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        _image = d.pop("image", UNSET)
        image: Union[Unset, ImageComponent]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ImageComponent.from_dict(_image)

        _description_headline = d.pop("descriptionHeadline", UNSET)
        description_headline: Union[Unset, TextComponent]
        if isinstance(_description_headline, Unset):
            description_headline = UNSET
        else:
            description_headline = TextComponent.from_dict(_description_headline)

        _description_block_1 = d.pop("descriptionBlock1", UNSET)
        description_block_1: Union[Unset, StandardTextBlock]
        if isinstance(_description_block_1, Unset):
            description_block_1 = UNSET
        else:
            description_block_1 = StandardTextBlock.from_dict(_description_block_1)

        _description_block_2 = d.pop("descriptionBlock2", UNSET)
        description_block_2: Union[Unset, StandardTextBlock]
        if isinstance(_description_block_2, Unset):
            description_block_2 = UNSET
        else:
            description_block_2 = StandardTextBlock.from_dict(_description_block_2)

        _specification_headline = d.pop("specificationHeadline", UNSET)
        specification_headline: Union[Unset, TextComponent]
        if isinstance(_specification_headline, Unset):
            specification_headline = UNSET
        else:
            specification_headline = TextComponent.from_dict(_specification_headline)

        _specification_list_block = d.pop("specificationListBlock", UNSET)
        specification_list_block: Union[Unset, StandardHeaderTextListBlock]
        if isinstance(_specification_list_block, Unset):
            specification_list_block = UNSET
        else:
            specification_list_block = StandardHeaderTextListBlock.from_dict(_specification_list_block)

        _specification_text_block = d.pop("specificationTextBlock", UNSET)
        specification_text_block: Union[Unset, StandardTextBlock]
        if isinstance(_specification_text_block, Unset):
            specification_text_block = UNSET
        else:
            specification_text_block = StandardTextBlock.from_dict(_specification_text_block)

        result = cls(
            headline=headline,
            image=image,
            description_headline=description_headline,
            description_block_1=description_block_1,
            description_block_2=description_block_2,
            specification_headline=specification_headline,
            specification_list_block=specification_list_block,
            specification_text_block=specification_text_block,
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
