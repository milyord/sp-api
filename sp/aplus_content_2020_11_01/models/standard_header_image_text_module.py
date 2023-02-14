from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_image_text_block import StandardImageTextBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardHeaderImageTextModule")


@attr.s(auto_attribs=True)
class StandardHeaderImageTextModule:
    r"""Standard headline text, an image, and body text.

    Attributes:
        headline (Union[Unset, TextComponent]): Rich text content.
        block (Union[Unset, StandardImageTextBlock]): The A+ Content standard image and text box block.
    """

    headline: Union[Unset, "TextComponent"] = UNSET
    block: Union[Unset, "StandardImageTextBlock"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.block, Unset):
            block = self.block.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if block is not UNSET:
            field_dict["block"] = block

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_image_text_block import StandardImageTextBlock
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        _block = d.pop("block", UNSET)
        block: Union[Unset, StandardImageTextBlock]
        if isinstance(_block, Unset):
            block = UNSET
        else:
            block = StandardImageTextBlock.from_dict(_block)

        result = cls(
            headline=headline,
            block=block,
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
