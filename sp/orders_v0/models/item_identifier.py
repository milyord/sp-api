from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.item_identifier_identifier_type import ItemIdentifierIdentifierType

T = TypeVar("T", bound="ItemIdentifier")


@attr.s(auto_attribs=True)
class ItemIdentifier:
    r"""Item identifiers used in the context of approvals operations.

    Attributes:
        identifier_type (ItemIdentifierIdentifierType): Defines the type of identifiers allowed to specify a
            substitution.
        identifier (str):
    """

    identifier_type: ItemIdentifierIdentifierType
    identifier: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier_type = self.identifier_type.value

        identifier = self.identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IdentifierType": identifier_type,
                "Identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier_type = ItemIdentifierIdentifierType(d.pop("IdentifierType"))

        identifier = d.pop("Identifier")

        result = cls(
            identifier_type=identifier_type,
            identifier=identifier,
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
