from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_identifier import ItemIdentifier


T = TypeVar("T", bound="ItemIdentifiersByMarketplace")


@attr.s(auto_attribs=True)
class ItemIdentifiersByMarketplace:
    r"""Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        identifiers (List['ItemIdentifier']): Identifiers associated with the item in the Amazon catalog for the
            indicated Amazon marketplace.
    """

    marketplace_id: str
    identifiers: List["ItemIdentifier"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        identifiers = []
        for identifiers_item_data in self.identifiers:
            identifiers_item = identifiers_item_data.to_dict()

            identifiers.append(identifiers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "identifiers": identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_identifier import ItemIdentifier

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        identifiers = []
        _identifiers = d.pop("identifiers")
        for identifiers_item_data in _identifiers:
            identifiers_item = ItemIdentifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        result = cls(
            marketplace_id=marketplace_id,
            identifiers=identifiers,
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
