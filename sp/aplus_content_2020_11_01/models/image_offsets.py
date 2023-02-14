from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.integer_with_units import IntegerWithUnits


T = TypeVar("T", bound="ImageOffsets")


@attr.s(auto_attribs=True)
class ImageOffsets:
    r"""The top left corner of the cropped image, specified in the original image's coordinate space.

    Attributes:
        x (IntegerWithUnits): A whole number dimension and its unit of measurement. For example, this can represent 100
            pixels.
        y (IntegerWithUnits): A whole number dimension and its unit of measurement. For example, this can represent 100
            pixels.
    """

    x: "IntegerWithUnits"
    y: "IntegerWithUnits"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x = self.x.to_dict()

        y = self.y.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.integer_with_units import IntegerWithUnits

        d = src_dict.copy()
        x = IntegerWithUnits.from_dict(d.pop("x"))

        y = IntegerWithUnits.from_dict(d.pop("y"))

        result = cls(
            x=x,
            y=y,
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
