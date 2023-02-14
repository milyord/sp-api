from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_text_list_block import StandardTextListBlock
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardHeaderTextListBlock")


@attr.s(auto_attribs=True)
class StandardHeaderTextListBlock:
    r"""The A+ standard fixed-length list of text, with a related headline.

    Attributes:
        headline (Union[Unset, TextComponent]): Rich text content.
        block (Union[Unset, StandardTextListBlock]): The A+ Content standard fixed length list of text, usually
            presented as bullet points.
    """

    headline: Union[Unset, "TextComponent"] = UNSET
    block: Union[Unset, "StandardTextListBlock"] = UNSET
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
        from ..models.standard_text_list_block import StandardTextListBlock
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _headline = d.pop("headline", UNSET)
        headline: Union[Unset, TextComponent]
        if isinstance(_headline, Unset):
            headline = UNSET
        else:
            headline = TextComponent.from_dict(_headline)

        _block = d.pop("block", UNSET)
        block: Union[Unset, StandardTextListBlock]
        if isinstance(_block, Unset):
            block = UNSET
        else:
            block = StandardTextListBlock.from_dict(_block)

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
