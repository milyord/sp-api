from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.integer_with_units import IntegerWithUnits


T = TypeVar("T", bound="ImageDimensions")


@attr.s(auto_attribs=True)
class ImageDimensions:
    r"""The dimensions extending from the top left corner of the cropped image, or the top left corner of the original image
    if there is no cropping. Only `pixels` is allowed as the units value for ImageDimensions.

        Attributes:
            width (IntegerWithUnits): A whole number dimension and its unit of measurement. For example, this can represent
                100 pixels.
            height (IntegerWithUnits): A whole number dimension and its unit of measurement. For example, this can represent
                100 pixels.
    """

    width: "IntegerWithUnits"
    height: "IntegerWithUnits"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        width = self.width.to_dict()

        height = self.height.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.integer_with_units import IntegerWithUnits

        d = src_dict.copy()
        width = IntegerWithUnits.from_dict(d.pop("width"))

        height = IntegerWithUnits.from_dict(d.pop("height"))

        result = cls(
            width=width,
            height=height,
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
