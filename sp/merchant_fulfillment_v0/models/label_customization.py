from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.standard_id_for_label import StandardIdForLabel
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelCustomization")


@attr.s(auto_attribs=True)
class LabelCustomization:
    r"""Custom text for shipping labels.

    Attributes:
        custom_text_for_label (Union[Unset, str]): Custom text to print on the label.

            Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support
            CustomTextForLabel.
        standard_id_for_label (Union[Unset, StandardIdForLabel]): The type of standard identifier to print on the label.
    """

    custom_text_for_label: Union[Unset, str] = UNSET
    standard_id_for_label: Union[Unset, StandardIdForLabel] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_text_for_label = self.custom_text_for_label
        standard_id_for_label: Union[Unset, str] = UNSET
        if not isinstance(self.standard_id_for_label, Unset):
            standard_id_for_label = self.standard_id_for_label.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_text_for_label is not UNSET:
            field_dict["CustomTextForLabel"] = custom_text_for_label
        if standard_id_for_label is not UNSET:
            field_dict["StandardIdForLabel"] = standard_id_for_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_text_for_label = d.pop("CustomTextForLabel", UNSET)

        _standard_id_for_label = d.pop("StandardIdForLabel", UNSET)
        standard_id_for_label: Union[Unset, StandardIdForLabel]
        if isinstance(_standard_id_for_label, Unset):
            standard_id_for_label = UNSET
        else:
            standard_id_for_label = StandardIdForLabel(_standard_id_for_label)

        result = cls(
            custom_text_for_label=custom_text_for_label,
            standard_id_for_label=standard_id_for_label,
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
