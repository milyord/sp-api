from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_image_text_block import StandardImageTextBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardThreeImageTextModule")


@attr.s(auto_attribs=True)
class StandardThreeImageTextModule:
    r"""Three standard images with text, presented across a single row.

    Attributes:
        headline (Union[Unset, TextComponent]): Rich text content.
        block1 (Union[Unset, StandardImageTextBlock]): The A+ Content standard image and text box block.
        block2 (Union[Unset, StandardImageTextBlock]): The A+ Content standard image and text box block.
        block3 (Union[Unset, StandardImageTextBlock]): The A+ Content standard image and text box block.
    """

    headline: Union[Unset, "TextComponent"] = UNSET
    block1: Union[Unset, "StandardImageTextBlock"] = UNSET
    block2: Union[Unset, "StandardImageTextBlock"] = UNSET
    block3: Union[Unset, "StandardImageTextBlock"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headline, Unset):
            headline = self.headline.to_dict()

        block1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.block1, Unset):
            block1 = self.block1.to_dict()

        block2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.block2, Unset):
            block2 = self.block2.to_dict()

        block3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.block3, Unset):
            block3 = self.block3.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headline is not UNSET:
            field_dict["headline"] = headline
        if block1 is not UNSET:
            field_dict["block1"] = block1
        if block2 is not UNSET:
            field_dict["block2"] = block2
        if block3 is not UNSET:
            field_dict["block3"] = block3

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

        _block1 = d.pop("block1", UNSET)
        block1: Union[Unset, StandardImageTextBlock]
        if isinstance(_block1, Unset):
            block1 = UNSET
        else:
            block1 = StandardImageTextBlock.from_dict(_block1)

        _block2 = d.pop("block2", UNSET)
        block2: Union[Unset, StandardImageTextBlock]
        if isinstance(_block2, Unset):
            block2 = UNSET
        else:
            block2 = StandardImageTextBlock.from_dict(_block2)

        _block3 = d.pop("block3", UNSET)
        block3: Union[Unset, StandardImageTextBlock]
        if isinstance(_block3, Unset):
            block3 = UNSET
        else:
            block3 = StandardImageTextBlock.from_dict(_block3)

        result = cls(
            headline=headline,
            block1=block1,
            block2=block2,
            block3=block3,
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
