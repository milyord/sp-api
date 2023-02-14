from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureSku")


@attr.s(auto_attribs=True)
class FeatureSku:
    r"""Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the
    same inventory pool.

        Attributes:
            seller_sku (Union[Unset, str]): Used to identify an item in the given marketplace. SellerSKU is qualified by the
                seller's SellerId, which is included with every operation that you submit.
            fn_sku (Union[Unset, str]): The unique SKU used by Amazon's fulfillment network.
            asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
            sku_count (Union[Unset, float]): The number of SKUs available for this service.
            overlapping_skus (Union[Unset, List[str]]): Other seller SKUs that are shared across the same inventory.
    """

    seller_sku: Union[Unset, str] = UNSET
    fn_sku: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    sku_count: Union[Unset, float] = UNSET
    overlapping_skus: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        fn_sku = self.fn_sku
        asin = self.asin
        sku_count = self.sku_count
        overlapping_skus: Union[Unset, List[str]] = UNSET
        if not isinstance(self.overlapping_skus, Unset):
            overlapping_skus = self.overlapping_skus

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seller_sku is not UNSET:
            field_dict["sellerSku"] = seller_sku
        if fn_sku is not UNSET:
            field_dict["fnSku"] = fn_sku
        if asin is not UNSET:
            field_dict["asin"] = asin
        if sku_count is not UNSET:
            field_dict["skuCount"] = sku_count
        if overlapping_skus is not UNSET:
            field_dict["overlappingSkus"] = overlapping_skus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_sku = d.pop("sellerSku", UNSET)

        fn_sku = d.pop("fnSku", UNSET)

        asin = d.pop("asin", UNSET)

        sku_count = d.pop("skuCount", UNSET)

        overlapping_skus = cast(List[str], d.pop("overlappingSkus", UNSET))

        result = cls(
            seller_sku=seller_sku,
            fn_sku=fn_sku,
            asin=asin,
            sku_count=sku_count,
            overlapping_skus=overlapping_skus,
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
