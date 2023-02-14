from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SalesRankType")


@attr.s(auto_attribs=True)
class SalesRankType:
    r"""
    Attributes:
        product_category_id (str): Identifies the item category from which the sales rank is taken.
        rank (int): The sales rank of the item within the item category.
    """

    product_category_id: str
    rank: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_category_id = self.product_category_id
        rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ProductCategoryId": product_category_id,
                "Rank": rank,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_category_id = d.pop("ProductCategoryId")

        rank = d.pop("Rank")

        result = cls(
            product_category_id=product_category_id,
            rank=rank,
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
