from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.label_format import LabelFormat
from ..models.standard_id_for_label import StandardIdForLabel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_contents import FileContents
    from ..models.label_dimensions import LabelDimensions


T = TypeVar("T", bound="Label")


@attr.s(auto_attribs=True)
class Label:
    r"""Data for creating a shipping label and dimensions for printing the label.

    Attributes:
        dimensions (LabelDimensions): Dimensions for printing a shipping label.
        file_contents (FileContents): The document data and checksum.
        custom_text_for_label (Union[Unset, str]): Custom text to print on the label.

            Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support
            CustomTextForLabel.
        label_format (Union[Unset, LabelFormat]): The label format.
        standard_id_for_label (Union[Unset, StandardIdForLabel]): The type of standard identifier to print on the label.
    """

    dimensions: "LabelDimensions"
    file_contents: "FileContents"
    custom_text_for_label: Union[Unset, str] = UNSET
    label_format: Union[Unset, LabelFormat] = UNSET
    standard_id_for_label: Union[Unset, StandardIdForLabel] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dimensions = self.dimensions.to_dict()

        file_contents = self.file_contents.to_dict()

        custom_text_for_label = self.custom_text_for_label
        label_format: Union[Unset, str] = UNSET
        if not isinstance(self.label_format, Unset):
            label_format = self.label_format.value

        standard_id_for_label: Union[Unset, str] = UNSET
        if not isinstance(self.standard_id_for_label, Unset):
            standard_id_for_label = self.standard_id_for_label.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Dimensions": dimensions,
                "FileContents": file_contents,
            }
        )
        if custom_text_for_label is not UNSET:
            field_dict["CustomTextForLabel"] = custom_text_for_label
        if label_format is not UNSET:
            field_dict["LabelFormat"] = label_format
        if standard_id_for_label is not UNSET:
            field_dict["StandardIdForLabel"] = standard_id_for_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_contents import FileContents
        from ..models.label_dimensions import LabelDimensions

        d = src_dict.copy()
        dimensions = LabelDimensions.from_dict(d.pop("Dimensions"))

        file_contents = FileContents.from_dict(d.pop("FileContents"))

        custom_text_for_label = d.pop("CustomTextForLabel", UNSET)

        _label_format = d.pop("LabelFormat", UNSET)
        label_format: Union[Unset, LabelFormat]
        if isinstance(_label_format, Unset):
            label_format = UNSET
        else:
            label_format = LabelFormat(_label_format)

        _standard_id_for_label = d.pop("StandardIdForLabel", UNSET)
        standard_id_for_label: Union[Unset, StandardIdForLabel]
        if isinstance(_standard_id_for_label, Unset):
            standard_id_for_label = UNSET
        else:
            standard_id_for_label = StandardIdForLabel(_standard_id_for_label)

        result = cls(
            dimensions=dimensions,
            file_contents=file_contents,
            custom_text_for_label=custom_text_for_label,
            label_format=label_format,
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
