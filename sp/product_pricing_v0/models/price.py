from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product import Product


T = TypeVar("T", bound="Price")


@attr.s(auto_attribs=True)
class Price:
    r"""
    Attributes:
        status (str): The status of the operation.
        seller_sku (Union[Unset, str]): The seller stock keeping unit (SKU) of the item.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        product (Union[Unset, Product]): An item.
    """

    status: str
    seller_sku: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    product: Union[Unset, "Product"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        seller_sku = self.seller_sku
        asin = self.asin
        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if product is not UNSET:
            field_dict["Product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product import Product

        d = src_dict.copy()
        status = d.pop("status")

        seller_sku = d.pop("SellerSKU", UNSET)

        asin = d.pop("ASIN", UNSET)

        _product = d.pop("Product", UNSET)
        product: Union[Unset, Product]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = Product.from_dict(_product)

        result = cls(
            status=status,
            seller_sku=seller_sku,
            asin=asin,
            product=product,
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
