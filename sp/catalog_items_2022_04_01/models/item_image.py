from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.item_image_variant import ItemImageVariant

T = TypeVar("T", bound="ItemImage")


@attr.s(auto_attribs=True)
class ItemImage:
    r"""Image for an item in the Amazon catalog.

    Attributes:
        variant (ItemImageVariant): Variant of the image, such as `MAIN` or `PT01`. Example: MAIN.
        link (str): Link, or URL, for the image.
        height (int): Height of the image in pixels.
        width (int): Width of the image in pixels.
    """

    variant: ItemImageVariant
    link: str
    height: int
    width: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variant = self.variant.value

        link = self.link
        height = self.height
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant": variant,
                "link": link,
                "height": height,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variant = ItemImageVariant(d.pop("variant"))

        link = d.pop("link")

        height = d.pop("height")

        width = d.pop("width")

        result = cls(
            variant=variant,
            link=link,
            height=height,
            width=width,
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
