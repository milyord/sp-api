from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="ChargeComponent")


@attr.s(auto_attribs=True)
class ChargeComponent:
    r"""A charge on the seller's account.

    Possible values:

    * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity
    ordered.

    * Tax - The tax collected by the seller on the Principal.

    * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal.

    * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge.

    * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge.

    * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges.

    * Discount - The promotional discount for an order item.

    * TaxDiscount - The tax amount deducted for promotional rebates.

    * CODItemCharge - The COD charge for an order item.

    * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge.

    * CODOrderCharge - The COD charge for an order.

    * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge.

    * CODShippingCharge - Shipping charges for a COD order.

    * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge.

    * ShippingCharge - The shipping charge.

    * ShippingTax - The tax collected by the seller on a ShippingCharge.

    * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the
    buying experience.

    * Giftwrap - The gift wrap charge.

    * GiftwrapTax - The tax collected by the seller on a Giftwrap charge.

    * RestockingFee - The charge applied to the buyer when returning a product in certain categories.

    * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at
    fault.

    * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to
    cover the deduction.

    * GenericDeduction - A generic bad debt deduction.

    * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item,
    requests a free replacement, and returns the incorrect item.

    * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.

    * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of
    the Amazon Global program.

    * SAFE-TReimbursement - The SAFE-T claim amount for the item.

    * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).

    * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).

    * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).

    * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).

        Attributes:
            charge_type (Union[Unset, str]): The type of charge.
            charge_amount (Union[Unset, Currency]): A currency type and amount.
    """

    charge_type: Union[Unset, str] = UNSET
    charge_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charge_type = self.charge_type
        charge_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.charge_amount, Unset):
            charge_amount = self.charge_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_type is not UNSET:
            field_dict["ChargeType"] = charge_type
        if charge_amount is not UNSET:
            field_dict["ChargeAmount"] = charge_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        charge_type = d.pop("ChargeType", UNSET)

        _charge_amount = d.pop("ChargeAmount", UNSET)
        charge_amount: Union[Unset, Currency]
        if isinstance(_charge_amount, Unset):
            charge_amount = UNSET
        else:
            charge_amount = Currency.from_dict(_charge_amount)

        result = cls(
            charge_type=charge_type,
            charge_amount=charge_amount,
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
