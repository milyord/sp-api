from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemProductTypeByMarketplace")


@attr.s(auto_attribs=True)
class ItemProductTypeByMarketplace:
    r"""Product type associated with the Amazon catalog item for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (Union[Unset, str]): Amazon marketplace identifier.
        product_type (Union[Unset, str]): Name of the product type associated with the Amazon catalog item. Example:
            LUGGAGE.
    """

    marketplace_id: Union[Unset, str] = UNSET
    product_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        product_type = self.product_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if product_type is not UNSET:
            field_dict["productType"] = product_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId", UNSET)

        product_type = d.pop("productType", UNSET)

        result = cls(
            marketplace_id=marketplace_id,
            product_type=product_type,
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
