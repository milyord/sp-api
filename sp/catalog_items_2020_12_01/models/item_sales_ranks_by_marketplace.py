from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item_sales_rank import ItemSalesRank


T = TypeVar("T", bound="ItemSalesRanksByMarketplace")


@attr.s(auto_attribs=True)
class ItemSalesRanksByMarketplace:
    r"""Sales ranks of an Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        ranks (List['ItemSalesRank']): Sales ranks of an Amazon catalog item for an Amazon marketplace.
    """

    marketplace_id: str
    ranks: List["ItemSalesRank"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        ranks = []
        for ranks_item_data in self.ranks:
            ranks_item = ranks_item_data.to_dict()

            ranks.append(ranks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "ranks": ranks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_sales_rank import ItemSalesRank

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        ranks = []
        _ranks = d.pop("ranks")
        for ranks_item_data in _ranks:
            ranks_item = ItemSalesRank.from_dict(ranks_item_data)

            ranks.append(ranks_item)

        result = cls(
            marketplace_id=marketplace_id,
            ranks=ranks,
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
