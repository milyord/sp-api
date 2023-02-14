from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.label_format import LabelFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelFormatOption")


@attr.s(auto_attribs=True)
class LabelFormatOption:
    r"""The label format details and whether to include a packing slip.

    Attributes:
        include_packing_slip_with_label (Union[Unset, bool]): When true, include a packing slip with the label.
        label_format (Union[Unset, LabelFormat]): The label format.
    """

    include_packing_slip_with_label: Union[Unset, bool] = UNSET
    label_format: Union[Unset, LabelFormat] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        include_packing_slip_with_label = self.include_packing_slip_with_label
        label_format: Union[Unset, str] = UNSET
        if not isinstance(self.label_format, Unset):
            label_format = self.label_format.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_packing_slip_with_label is not UNSET:
            field_dict["IncludePackingSlipWithLabel"] = include_packing_slip_with_label
        if label_format is not UNSET:
            field_dict["LabelFormat"] = label_format

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        include_packing_slip_with_label = d.pop("IncludePackingSlipWithLabel", UNSET)

        _label_format = d.pop("LabelFormat", UNSET)
        label_format: Union[Unset, LabelFormat]
        if isinstance(_label_format, Unset):
            label_format = UNSET
        else:
            label_format = LabelFormat(_label_format)

        result = cls(
            include_packing_slip_with_label=include_packing_slip_with_label,
            label_format=label_format,
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
