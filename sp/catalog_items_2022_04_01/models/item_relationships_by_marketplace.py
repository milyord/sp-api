from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_relationship import ItemRelationship


T = TypeVar("T", bound="ItemRelationshipsByMarketplace")


@attr.s(auto_attribs=True)
class ItemRelationshipsByMarketplace:
    r"""Relationship details for the Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        relationships (List['ItemRelationship']): Relationships for the item.
    """

    marketplace_id: str
    relationships: List["ItemRelationship"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()

            relationships.append(relationships_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "relationships": relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_relationship import ItemRelationship

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = ItemRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        result = cls(
            marketplace_id=marketplace_id,
            relationships=relationships,
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
