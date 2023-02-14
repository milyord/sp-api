import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent
    from ..models.currency import Currency
    from ..models.fee_component import FeeComponent


T = TypeVar("T", bound="SellerReviewEnrollmentPaymentEvent")


@attr.s(auto_attribs=True)
class SellerReviewEnrollmentPaymentEvent:
    r"""A fee payment event for the Early Reviewer Program.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        enrollment_id (Union[Unset, str]): An enrollment identifier.
        parent_asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item that was enrolled
            in the Early Reviewer Program.
        fee_component (Union[Unset, FeeComponent]): A fee associated with the event.
        charge_component (Union[Unset, ChargeComponent]): A charge on the seller's account.

            Possible values:

            * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the
            quantity ordered.

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

            * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon
            Points to cover the deduction.

            * GenericDeduction - A generic bad debt deduction.

            * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item,
            requests a free replacement, and returns the incorrect item.

            * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces.

            * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part
            of the Amazon Global program.

            * SAFE-TReimbursement - The SAFE-T claim amount for the item.

            * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST).

            * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST).

            * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST).

            * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
        total_amount (Union[Unset, Currency]): A currency type and amount.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    enrollment_id: Union[Unset, str] = UNSET
    parent_asin: Union[Unset, str] = UNSET
    fee_component: Union[Unset, "FeeComponent"] = UNSET
    charge_component: Union[Unset, "ChargeComponent"] = UNSET
    total_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        enrollment_id = self.enrollment_id
        parent_asin = self.parent_asin
        fee_component: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_component, Unset):
            fee_component = self.fee_component.to_dict()

        charge_component: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.charge_component, Unset):
            charge_component = self.charge_component.to_dict()

        total_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_amount, Unset):
            total_amount = self.total_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if enrollment_id is not UNSET:
            field_dict["EnrollmentId"] = enrollment_id
        if parent_asin is not UNSET:
            field_dict["ParentASIN"] = parent_asin
        if fee_component is not UNSET:
            field_dict["FeeComponent"] = fee_component
        if charge_component is not UNSET:
            field_dict["ChargeComponent"] = charge_component
        if total_amount is not UNSET:
            field_dict["TotalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent
        from ..models.currency import Currency
        from ..models.fee_component import FeeComponent

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        enrollment_id = d.pop("EnrollmentId", UNSET)

        parent_asin = d.pop("ParentASIN", UNSET)

        _fee_component = d.pop("FeeComponent", UNSET)
        fee_component: Union[Unset, FeeComponent]
        if isinstance(_fee_component, Unset):
            fee_component = UNSET
        else:
            fee_component = FeeComponent.from_dict(_fee_component)

        _charge_component = d.pop("ChargeComponent", UNSET)
        charge_component: Union[Unset, ChargeComponent]
        if isinstance(_charge_component, Unset):
            charge_component = UNSET
        else:
            charge_component = ChargeComponent.from_dict(_charge_component)

        _total_amount = d.pop("TotalAmount", UNSET)
        total_amount: Union[Unset, Currency]
        if isinstance(_total_amount, Unset):
            total_amount = UNSET
        else:
            total_amount = Currency.from_dict(_total_amount)

        result = cls(
            posted_date=posted_date,
            enrollment_id=enrollment_id,
            parent_asin=parent_asin,
            fee_component=fee_component,
            charge_component=charge_component,
            total_amount=total_amount,
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
