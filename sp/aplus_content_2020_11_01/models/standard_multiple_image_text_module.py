from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_image_text_caption_block import StandardImageTextCaptionBlock


T = TypeVar("T", bound="StandardMultipleImageTextModule")


@attr.s(auto_attribs=True)
class StandardMultipleImageTextModule:
    r"""Standard images with text, presented one at a time. The user clicks on thumbnails to view each block.

    Attributes:
        blocks (Union[Unset, List['StandardImageTextCaptionBlock']]):
    """

    blocks: Union[Unset, List["StandardImageTextCaptionBlock"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        blocks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = []
            for blocks_item_data in self.blocks:
                blocks_item = blocks_item_data.to_dict()

                blocks.append(blocks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocks is not UNSET:
            field_dict["blocks"] = blocks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_image_text_caption_block import StandardImageTextCaptionBlock

        d = src_dict.copy()
        blocks = []
        _blocks = d.pop("blocks", UNSET)
        for blocks_item_data in _blocks or []:
            blocks_item = StandardImageTextCaptionBlock.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        result = cls(
            blocks=blocks,
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
