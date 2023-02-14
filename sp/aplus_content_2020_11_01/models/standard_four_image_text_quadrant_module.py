from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.standard_image_text_block import StandardImageTextBlock


T = TypeVar("T", bound="StandardFourImageTextQuadrantModule")


@attr.s(auto_attribs=True)
class StandardFourImageTextQuadrantModule:
    r"""Four standard images with text, presented on a grid of four quadrants.

    Attributes:
        block1 (StandardImageTextBlock): The A+ Content standard image and text box block.
        block2 (StandardImageTextBlock): The A+ Content standard image and text box block.
        block3 (StandardImageTextBlock): The A+ Content standard image and text box block.
        block4 (StandardImageTextBlock): The A+ Content standard image and text box block.
    """

    block1: "StandardImageTextBlock"
    block2: "StandardImageTextBlock"
    block3: "StandardImageTextBlock"
    block4: "StandardImageTextBlock"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block1 = self.block1.to_dict()

        block2 = self.block2.to_dict()

        block3 = self.block3.to_dict()

        block4 = self.block4.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "block1": block1,
                "block2": block2,
                "block3": block3,
                "block4": block4,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_image_text_block import StandardImageTextBlock

        d = src_dict.copy()
        block1 = StandardImageTextBlock.from_dict(d.pop("block1"))

        block2 = StandardImageTextBlock.from_dict(d.pop("block2"))

        block3 = StandardImageTextBlock.from_dict(d.pop("block3"))

        block4 = StandardImageTextBlock.from_dict(d.pop("block4"))

        result = cls(
            block1=block1,
            block2=block2,
            block3=block3,
            block4=block4,
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
