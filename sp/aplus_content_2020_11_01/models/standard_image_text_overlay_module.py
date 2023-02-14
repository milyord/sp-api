from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.color_type import ColorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_image_text_block import StandardImageTextBlock


T = TypeVar("T", bound="StandardImageTextOverlayModule")


@attr.s(auto_attribs=True)
class StandardImageTextOverlayModule:
    r"""A standard background image with a floating text box.

    Attributes:
        overlay_color_type (ColorType): The relative color scheme of content.
        block (Union[Unset, StandardImageTextBlock]): The A+ Content standard image and text box block.
    """

    overlay_color_type: ColorType
    block: Union[Unset, "StandardImageTextBlock"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        overlay_color_type = self.overlay_color_type.value

        block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.block, Unset):
            block = self.block.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overlayColorType": overlay_color_type,
            }
        )
        if block is not UNSET:
            field_dict["block"] = block

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_image_text_block import StandardImageTextBlock

        d = src_dict.copy()
        overlay_color_type = ColorType(d.pop("overlayColorType"))

        _block = d.pop("block", UNSET)
        block: Union[Unset, StandardImageTextBlock]
        if isinstance(_block, Unset):
            block = UNSET
        else:
            block = StandardImageTextBlock.from_dict(_block)

        result = cls(
            overlay_color_type=overlay_color_type,
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
