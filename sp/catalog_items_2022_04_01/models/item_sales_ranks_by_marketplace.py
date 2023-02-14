from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_classification_sales_rank import ItemClassificationSalesRank
    from ..models.item_display_group_sales_rank import ItemDisplayGroupSalesRank


T = TypeVar("T", bound="ItemSalesRanksByMarketplace")


@attr.s(auto_attribs=True)
class ItemSalesRanksByMarketplace:
    r"""Sales ranks of an Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        classification_ranks (Union[Unset, List['ItemClassificationSalesRank']]): Sales ranks of an Amazon catalog item
            for an Amazon marketplace by classification.
        display_group_ranks (Union[Unset, List['ItemDisplayGroupSalesRank']]): Sales ranks of an Amazon catalog item for
            an Amazon marketplace by website display group.
    """

    marketplace_id: str
    classification_ranks: Union[Unset, List["ItemClassificationSalesRank"]] = UNSET
    display_group_ranks: Union[Unset, List["ItemDisplayGroupSalesRank"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        classification_ranks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classification_ranks, Unset):
            classification_ranks = []
            for classification_ranks_item_data in self.classification_ranks:
                classification_ranks_item = classification_ranks_item_data.to_dict()

                classification_ranks.append(classification_ranks_item)

        display_group_ranks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.display_group_ranks, Unset):
            display_group_ranks = []
            for display_group_ranks_item_data in self.display_group_ranks:
                display_group_ranks_item = display_group_ranks_item_data.to_dict()

                display_group_ranks.append(display_group_ranks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if classification_ranks is not UNSET:
            field_dict["classificationRanks"] = classification_ranks
        if display_group_ranks is not UNSET:
            field_dict["displayGroupRanks"] = display_group_ranks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_classification_sales_rank import ItemClassificationSalesRank
        from ..models.item_display_group_sales_rank import ItemDisplayGroupSalesRank

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        classification_ranks = []
        _classification_ranks = d.pop("classificationRanks", UNSET)
        for classification_ranks_item_data in _classification_ranks or []:
            classification_ranks_item = ItemClassificationSalesRank.from_dict(classification_ranks_item_data)

            classification_ranks.append(classification_ranks_item)

        display_group_ranks = []
        _display_group_ranks = d.pop("displayGroupRanks", UNSET)
        for display_group_ranks_item_data in _display_group_ranks or []:
            display_group_ranks_item = ItemDisplayGroupSalesRank.from_dict(display_group_ranks_item_data)

            display_group_ranks.append(display_group_ranks_item)

        result = cls(
            marketplace_id=marketplace_id,
            classification_ranks=classification_ranks,
            display_group_ranks=display_group_ranks,
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
