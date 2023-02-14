from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelFormatOptionRequest")


@attr.s(auto_attribs=True)
class LabelFormatOptionRequest:
    r"""Whether to include a packing slip.

    Attributes:
        include_packing_slip_with_label (Union[Unset, bool]): When true, include a packing slip with the label.
    """

    include_packing_slip_with_label: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        include_packing_slip_with_label = self.include_packing_slip_with_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_packing_slip_with_label is not UNSET:
            field_dict["IncludePackingSlipWithLabel"] = include_packing_slip_with_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        include_packing_slip_with_label = d.pop("IncludePackingSlipWithLabel", UNSET)

        result = cls(
            include_packing_slip_with_label=include_packing_slip_with_label,
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
