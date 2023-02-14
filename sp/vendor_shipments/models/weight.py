from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.weight_unit_of_measure import WeightUnitOfMeasure

T = TypeVar("T", bound="Weight")


@attr.s(auto_attribs=True)
class Weight:
    r"""The weight.

    Attributes:
        unit_of_measure (WeightUnitOfMeasure): The unit of measurement.
        value (str): A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with
            currencies. Follows RFC7159 for number representation. <br>**Pattern** :
            `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """

    unit_of_measure: WeightUnitOfMeasure
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_of_measure = self.unit_of_measure.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unitOfMeasure": unit_of_measure,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_of_measure = WeightUnitOfMeasure(d.pop("unitOfMeasure"))

        value = d.pop("value")

        result = cls(
            unit_of_measure=unit_of_measure,
            value=value,
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
