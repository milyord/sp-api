from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.item_relationship_type import ItemRelationshipType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_variation_theme import ItemVariationTheme


T = TypeVar("T", bound="ItemRelationship")


@attr.s(auto_attribs=True)
class ItemRelationship:
    r"""Relationship details for an Amazon catalog item.

    Attributes:
        type (ItemRelationshipType): Type of relationship. Example: VARIATION.
        child_asins (Union[Unset, List[str]]): Identifiers (ASINs) of the related items that are children of this item.
        parent_asins (Union[Unset, List[str]]): Identifiers (ASINs) of the related items that are parents of this item.
        variation_theme (Union[Unset, ItemVariationTheme]): Variation theme indicating the combination of Amazon item
            catalog attributes that define the variation family.
    """

    type: ItemRelationshipType
    child_asins: Union[Unset, List[str]] = UNSET
    parent_asins: Union[Unset, List[str]] = UNSET
    variation_theme: Union[Unset, "ItemVariationTheme"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        child_asins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.child_asins, Unset):
            child_asins = self.child_asins

        parent_asins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_asins, Unset):
            parent_asins = self.parent_asins

        variation_theme: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.variation_theme, Unset):
            variation_theme = self.variation_theme.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if child_asins is not UNSET:
            field_dict["childAsins"] = child_asins
        if parent_asins is not UNSET:
            field_dict["parentAsins"] = parent_asins
        if variation_theme is not UNSET:
            field_dict["variationTheme"] = variation_theme

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_variation_theme import ItemVariationTheme

        d = src_dict.copy()
        type = ItemRelationshipType(d.pop("type"))

        child_asins = cast(List[str], d.pop("childAsins", UNSET))

        parent_asins = cast(List[str], d.pop("parentAsins", UNSET))

        _variation_theme = d.pop("variationTheme", UNSET)
        variation_theme: Union[Unset, ItemVariationTheme]
        if isinstance(_variation_theme, Unset):
            variation_theme = UNSET
        else:
            variation_theme = ItemVariationTheme.from_dict(_variation_theme)

        result = cls(
            type=type,
            child_asins=child_asins,
            parent_asins=parent_asins,
            variation_theme=variation_theme,
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
