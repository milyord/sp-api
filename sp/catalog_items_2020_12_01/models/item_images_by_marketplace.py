from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_image import ItemImage


T = TypeVar("T", bound="ItemImagesByMarketplace")


@attr.s(auto_attribs=True)
class ItemImagesByMarketplace:
    r"""Images for an item in the Amazon catalog for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        images (List['ItemImage']): Images for an item in the Amazon catalog for the indicated Amazon marketplace.
    """

    marketplace_id: str
    images: List["ItemImage"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()

            images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "images": images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_image import ItemImage

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = ItemImage.from_dict(images_item_data)

            images.append(images_item)

        result = cls(
            marketplace_id=marketplace_id,
            images=images,
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
