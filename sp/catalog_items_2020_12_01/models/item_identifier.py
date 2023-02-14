from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ItemIdentifier")


@attr.s(auto_attribs=True)
class ItemIdentifier:
    r"""Identifier associated with the item in the Amazon catalog, such as a UPC or EAN identifier.

    Attributes:
        identifier_type (str): Type of identifier, such as UPC, EAN, or ISBN.
        identifier (str): Identifier.
    """

    identifier_type: str
    identifier: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier_type = self.identifier_type
        identifier = self.identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifierType": identifier_type,
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier_type = d.pop("identifierType")

        identifier = d.pop("identifier")

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
