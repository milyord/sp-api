from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.dimensions_unit_of_measure import DimensionsUnitOfMeasure

T = TypeVar("T", bound="Dimensions")


@attr.s(auto_attribs=True)
class Dimensions:
    r"""Physical dimensional measurements of a container.

    Attributes:
        length (str): A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with
            currencies. Follows RFC7159 for number representation. <br>**Pattern** :
            `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
        width (str): A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with
            currencies. Follows RFC7159 for number representation. <br>**Pattern** :
            `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
        height (str): A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with
            currencies. Follows RFC7159 for number representation. <br>**Pattern** :
            `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
        unit_of_measure (DimensionsUnitOfMeasure): The unit of measure for dimensions.
    """

    length: str
    width: str
    height: str
    unit_of_measure: DimensionsUnitOfMeasure
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        length = self.length
        width = self.width
        height = self.height
        unit_of_measure = self.unit_of_measure.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "length": length,
                "width": width,
                "height": height,
                "unitOfMeasure": unit_of_measure,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("length")

        width = d.pop("width")

        height = d.pop("height")

        unit_of_measure = DimensionsUnitOfMeasure(d.pop("unitOfMeasure"))

        result = cls(
            length=length,
            width=width,
            height=height,
            unit_of_measure=unit_of_measure,
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
