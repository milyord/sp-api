from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.regulated_information_field import RegulatedInformationField


T = TypeVar("T", bound="RegulatedInformation")


@attr.s(auto_attribs=True)
class RegulatedInformation:
    r"""The regulated information collected during purchase and used to verify the order.

    Attributes:
        fields (List['RegulatedInformationField']): A list of regulated information fields as collected from the
            regulatory form.
    """

    fields: List["RegulatedInformationField"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.regulated_information_field import RegulatedInformationField

        d = src_dict.copy()
        fields = []
        _fields = d.pop("Fields")
        for fields_item_data in _fields:
            fields_item = RegulatedInformationField.from_dict(fields_item_data)

            fields.append(fields_item)

        result = cls(
            fields=fields,
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
