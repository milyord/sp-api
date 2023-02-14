from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.image_crop_specification import ImageCropSpecification


T = TypeVar("T", bound="ImageComponent")


@attr.s(auto_attribs=True)
class ImageComponent:
    r"""A reference to an image, hosted in the A+ Content media library.

    Attributes:
        upload_destination_id (str): This identifier is provided by the Selling Partner API for Uploads.
        image_crop_specification (ImageCropSpecification): The instructions for optionally cropping an image. If no
            cropping is desired, set the dimensions to the original image size. If the image is cropped and no offset values
            are provided, then the coordinates of the top left corner of the cropped image, relative to the original image,
            are defaulted to (0,0).
        alt_text (str): The alternative text for the image.
    """

    upload_destination_id: str
    image_crop_specification: "ImageCropSpecification"
    alt_text: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_destination_id = self.upload_destination_id
        image_crop_specification = self.image_crop_specification.to_dict()

        alt_text = self.alt_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadDestinationId": upload_destination_id,
                "imageCropSpecification": image_crop_specification,
                "altText": alt_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_crop_specification import ImageCropSpecification

        d = src_dict.copy()
        upload_destination_id = d.pop("uploadDestinationId")

        image_crop_specification = ImageCropSpecification.from_dict(d.pop("imageCropSpecification"))

        alt_text = d.pop("altText")

        result = cls(
            upload_destination_id=upload_destination_id,
            image_crop_specification=image_crop_specification,
            alt_text=alt_text,
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
