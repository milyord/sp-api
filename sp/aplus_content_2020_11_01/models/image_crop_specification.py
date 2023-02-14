from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_dimensions import ImageDimensions
    from ..models.image_offsets import ImageOffsets


T = TypeVar("T", bound="ImageCropSpecification")


@attr.s(auto_attribs=True)
class ImageCropSpecification:
    r"""The instructions for optionally cropping an image. If no cropping is desired, set the dimensions to the original
    image size. If the image is cropped and no offset values are provided, then the coordinates of the top left corner
    of the cropped image, relative to the original image, are defaulted to (0,0).

        Attributes:
            size (ImageDimensions): The dimensions extending from the top left corner of the cropped image, or the top left
                corner of the original image if there is no cropping. Only `pixels` is allowed as the units value for
                ImageDimensions.
            offset (Union[Unset, ImageOffsets]): The top left corner of the cropped image, specified in the original image's
                coordinate space.
    """

    size: "ImageDimensions"
    offset: Union[Unset, "ImageOffsets"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size.to_dict()

        offset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
            }
        )
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_dimensions import ImageDimensions
        from ..models.image_offsets import ImageOffsets

        d = src_dict.copy()
        size = ImageDimensions.from_dict(d.pop("size"))

        _offset = d.pop("offset", UNSET)
        offset: Union[Unset, ImageOffsets]
        if isinstance(_offset, Unset):
            offset = UNSET
        else:
            offset = ImageOffsets.from_dict(_offset)

        result = cls(
            size=size,
            offset=offset,
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
