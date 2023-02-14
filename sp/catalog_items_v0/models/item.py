from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_set_list_type import AttributeSetListType
    from ..models.identifier_type import IdentifierType
    from ..models.relationship_type import RelationshipType
    from ..models.sales_rank_type import SalesRankType


T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""An item in the Amazon catalog.

    Attributes:
        identifiers (IdentifierType):
        attribute_sets (Union[Unset, List['AttributeSetListType']]): A list of attributes for the item.
        relationships (Union[Unset, List['RelationshipType']]): A list of variation relationship information, if
            applicable for the item.
        sales_rankings (Union[Unset, List['SalesRankType']]): A list of sales rank information for the item by category.
    """

    identifiers: "IdentifierType"
    attribute_sets: Union[Unset, List["AttributeSetListType"]] = UNSET
    relationships: Union[Unset, List["RelationshipType"]] = UNSET
    sales_rankings: Union[Unset, List["SalesRankType"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifiers = self.identifiers.to_dict()

        attribute_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_sets, Unset):
            attribute_sets = []
            for componentsschemas_attribute_set_list_item_data in self.attribute_sets:
                componentsschemas_attribute_set_list_item = componentsschemas_attribute_set_list_item_data.to_dict()

                attribute_sets.append(componentsschemas_attribute_set_list_item)

        relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for componentsschemas_relationship_list_item_data in self.relationships:
                componentsschemas_relationship_list_item = componentsschemas_relationship_list_item_data.to_dict()

                relationships.append(componentsschemas_relationship_list_item)

        sales_rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_rankings, Unset):
            sales_rankings = []
            for componentsschemas_sales_rank_list_item_data in self.sales_rankings:
                componentsschemas_sales_rank_list_item = componentsschemas_sales_rank_list_item_data.to_dict()

                sales_rankings.append(componentsschemas_sales_rank_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Identifiers": identifiers,
            }
        )
        if attribute_sets is not UNSET:
            field_dict["AttributeSets"] = attribute_sets
        if relationships is not UNSET:
            field_dict["Relationships"] = relationships
        if sales_rankings is not UNSET:
            field_dict["SalesRankings"] = sales_rankings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_set_list_type import AttributeSetListType
        from ..models.identifier_type import IdentifierType
        from ..models.relationship_type import RelationshipType
        from ..models.sales_rank_type import SalesRankType

        d = src_dict.copy()
        identifiers = IdentifierType.from_dict(d.pop("Identifiers"))

        attribute_sets = []
        _attribute_sets = d.pop("AttributeSets", UNSET)
        for componentsschemas_attribute_set_list_item_data in _attribute_sets or []:
            componentsschemas_attribute_set_list_item = AttributeSetListType.from_dict(
                componentsschemas_attribute_set_list_item_data
            )

            attribute_sets.append(componentsschemas_attribute_set_list_item)

        relationships = []
        _relationships = d.pop("Relationships", UNSET)
        for componentsschemas_relationship_list_item_data in _relationships or []:
            componentsschemas_relationship_list_item = RelationshipType.from_dict(
                componentsschemas_relationship_list_item_data
            )

            relationships.append(componentsschemas_relationship_list_item)

        sales_rankings = []
        _sales_rankings = d.pop("SalesRankings", UNSET)
        for componentsschemas_sales_rank_list_item_data in _sales_rankings or []:
            componentsschemas_sales_rank_list_item = SalesRankType.from_dict(
                componentsschemas_sales_rank_list_item_data
            )

            sales_rankings.append(componentsschemas_sales_rank_list_item)

        result = cls(
            identifiers=identifiers,
            attribute_sets=attribute_sets,
            relationships=relationships,
            sales_rankings=sales_rankings,
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
