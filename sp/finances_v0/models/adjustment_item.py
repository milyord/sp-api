from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="AdjustmentItem")


@attr.s(auto_attribs=True)
class AdjustmentItem:
    r"""An item in an adjustment to the seller's account.

    Attributes:
        quantity (Union[Unset, str]): Represents the number of units in the seller's inventory when the AdustmentType is
            FBAInventoryReimbursement.
        per_unit_amount (Union[Unset, Currency]): A currency type and amount.
        total_amount (Union[Unset, Currency]): A currency type and amount.
        seller_sku (Union[Unset, str]): The seller SKU of the item. The seller SKU is qualified by the seller's seller
            ID, which is included with every call to the Selling Partner API.
        fn_sku (Union[Unset, str]): A unique identifier assigned to products stored in and fulfilled from a fulfillment
            center.
        product_description (Union[Unset, str]): A short description of the item.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
    """

    quantity: Union[Unset, str] = UNSET
    per_unit_amount: Union[Unset, "Currency"] = UNSET
    total_amount: Union[Unset, "Currency"] = UNSET
    seller_sku: Union[Unset, str] = UNSET
    fn_sku: Union[Unset, str] = UNSET
    product_description: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        per_unit_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_amount, Unset):
            per_unit_amount = self.per_unit_amount.to_dict()

        total_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_amount, Unset):
            total_amount = self.total_amount.to_dict()

        seller_sku = self.seller_sku
        fn_sku = self.fn_sku
        product_description = self.product_description
        asin = self.asin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["Quantity"] = quantity
        if per_unit_amount is not UNSET:
            field_dict["PerUnitAmount"] = per_unit_amount
        if total_amount is not UNSET:
            field_dict["TotalAmount"] = total_amount
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if fn_sku is not UNSET:
            field_dict["FnSKU"] = fn_sku
        if product_description is not UNSET:
            field_dict["ProductDescription"] = product_description
        if asin is not UNSET:
            field_dict["ASIN"] = asin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        quantity = d.pop("Quantity", UNSET)

        _per_unit_amount = d.pop("PerUnitAmount", UNSET)
        per_unit_amount: Union[Unset, Currency]
        if isinstance(_per_unit_amount, Unset):
            per_unit_amount = UNSET
        else:
            per_unit_amount = Currency.from_dict(_per_unit_amount)

        _total_amount = d.pop("TotalAmount", UNSET)
        total_amount: Union[Unset, Currency]
        if isinstance(_total_amount, Unset):
            total_amount = UNSET
        else:
            total_amount = Currency.from_dict(_total_amount)

        seller_sku = d.pop("SellerSKU", UNSET)

        fn_sku = d.pop("FnSKU", UNSET)

        product_description = d.pop("ProductDescription", UNSET)

        asin = d.pop("ASIN", UNSET)

        result = cls(
            quantity=quantity,
            per_unit_amount=per_unit_amount,
            total_amount=total_amount,
            seller_sku=seller_sku,
            fn_sku=fn_sku,
            product_description=product_description,
            asin=asin,
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
