from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.label_specification_label_format import LabelSpecificationLabelFormat
from ..models.label_specification_label_stock_size import LabelSpecificationLabelStockSize

T = TypeVar("T", bound="LabelSpecification")


@attr.s(auto_attribs=True)
class LabelSpecification:
    r"""The label specification info.

    Attributes:
        label_format (LabelSpecificationLabelFormat): The format of the label. Enum of PNG only for now.
        label_stock_size (LabelSpecificationLabelStockSize): The label stock size specification in length and height.
            Enum of 4x6 only for now.
    """

    label_format: LabelSpecificationLabelFormat
    label_stock_size: LabelSpecificationLabelStockSize
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label_format = self.label_format.value

        label_stock_size = self.label_stock_size.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labelFormat": label_format,
                "labelStockSize": label_stock_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label_format = LabelSpecificationLabelFormat(d.pop("labelFormat"))

        label_stock_size = LabelSpecificationLabelStockSize(d.pop("labelStockSize"))

        result = cls(
            label_format=label_format,
            label_stock_size=label_stock_size,
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
