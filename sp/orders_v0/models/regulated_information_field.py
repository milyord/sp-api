from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.regulated_information_field_field_type import RegulatedInformationFieldFieldType

T = TypeVar("T", bound="RegulatedInformationField")


@attr.s(auto_attribs=True)
class RegulatedInformationField:
    r"""A field collected from the regulatory form.

    Attributes:
        field_id (str): The unique identifier for the field.
        field_label (str): The name for the field.
        field_type (RegulatedInformationFieldFieldType): The type of field.
        field_value (str): The content of the field as collected in regulatory form. Note that FileAttachment type
            fields will contain a URL to download the attachment here.
    """

    field_id: str
    field_label: str
    field_type: RegulatedInformationFieldFieldType
    field_value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        field_label = self.field_label
        field_type = self.field_type.value

        field_value = self.field_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FieldId": field_id,
                "FieldLabel": field_label,
                "FieldType": field_type,
                "FieldValue": field_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("FieldId")

        field_label = d.pop("FieldLabel")

        field_type = RegulatedInformationFieldFieldType(d.pop("FieldType"))

        field_value = d.pop("FieldValue")

        result = cls(
            field_id=field_id,
            field_label=field_label,
            field_type=field_type,
            field_value=field_value,
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
