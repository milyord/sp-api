from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_component import ImageComponent
    from ..models.text_component import TextComponent


T = TypeVar("T", bound="StandardImageCaptionBlock")


@attr.s(auto_attribs=True)
class StandardImageCaptionBlock:
    r"""The A+ Content standard image and caption block.

    Attributes:
        image (Union[Unset, ImageComponent]): A reference to an image, hosted in the A+ Content media library.
        caption (Union[Unset, TextComponent]): Rich text content.
    """

    image: Union[Unset, "ImageComponent"] = UNSET
    caption: Union[Unset, "TextComponent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        caption: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.caption, Unset):
            caption = self.caption.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if caption is not UNSET:
            field_dict["caption"] = caption

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_component import ImageComponent
        from ..models.text_component import TextComponent

        d = src_dict.copy()
        _image = d.pop("image", UNSET)
        image: Union[Unset, ImageComponent]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ImageComponent.from_dict(_image)

        _caption = d.pop("caption", UNSET)
        caption: Union[Unset, TextComponent]
        if isinstance(_caption, Unset):
            caption = UNSET
        else:
            caption = TextComponent.from_dict(_caption)

        result = cls(
            image=image,
            caption=caption,
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
