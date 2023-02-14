from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customer_type import CustomerType
from ..models.item_condition import ItemCondition
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchOffersRequestParams")


@attr.s(auto_attribs=True)
class BatchOffersRequestParams:
    r"""
    Attributes:
        marketplace_id (str): A marketplace identifier. Specifies the marketplace for which prices are returned.
        item_condition (ItemCondition): Filters the offer listings to be considered based on item condition. Possible
            values: New, Used, Collectible, Refurbished, Club.
        customer_type (Union[Unset, CustomerType]): Indicates whether to request Consumer or Business offers. Default is
            Consumer.
    """

    marketplace_id: str
    item_condition: ItemCondition
    customer_type: Union[Unset, CustomerType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        item_condition = self.item_condition.value

        customer_type: Union[Unset, str] = UNSET
        if not isinstance(self.customer_type, Unset):
            customer_type = self.customer_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MarketplaceId": marketplace_id,
                "ItemCondition": item_condition,
            }
        )
        if customer_type is not UNSET:
            field_dict["CustomerType"] = customer_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("MarketplaceId")

        item_condition = ItemCondition(d.pop("ItemCondition"))

        _customer_type = d.pop("CustomerType", UNSET)
        customer_type: Union[Unset, CustomerType]
        if isinstance(_customer_type, Unset):
            customer_type = UNSET
        else:
            customer_type = CustomerType(_customer_type)

        result = cls(
            marketplace_id=marketplace_id,
            item_condition=item_condition,
            customer_type=customer_type,
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
