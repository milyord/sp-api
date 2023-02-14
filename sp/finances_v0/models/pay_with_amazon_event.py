import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent
    from ..models.fee_component import FeeComponent


T = TypeVar("T", bound="PayWithAmazonEvent")


@attr.s(auto_attribs=True)
class PayWithAmazonEvent:
    r"""An event related to the seller's Pay with Amazon account.

    Attributes:
        seller_order_id (Union[Unset, str]): An order identifier that is specified by the seller.
        transaction_posted_date (Union[Unset, datetime.datetime]):
        business_object_type (Union[Unset, str]): The type of business object.
        sales_channel (Union[Unset, str]): The sales channel for the transaction.
        charge (Union[Unset, ChargeComponent]): A charge on the seller's account.

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
        fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        payment_amount_type (Union[Unset, str]): The type of payment.

            Possible values:

            * Sales
        amount_description (Union[Unset, str]): A short description of this payment event.
        fulfillment_channel (Union[Unset, str]): The fulfillment channel.

            Possible values:

            * AFN - Amazon Fulfillment Network (Fulfillment by Amazon)

            * MFN - Merchant Fulfillment Network (self-fulfilled)
        store_name (Union[Unset, str]): The store name where the event occurred.
    """

    seller_order_id: Union[Unset, str] = UNSET
    transaction_posted_date: Union[Unset, datetime.datetime] = UNSET
    business_object_type: Union[Unset, str] = UNSET
    sales_channel: Union[Unset, str] = UNSET
    charge: Union[Unset, "ChargeComponent"] = UNSET
    fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    payment_amount_type: Union[Unset, str] = UNSET
    amount_description: Union[Unset, str] = UNSET
    fulfillment_channel: Union[Unset, str] = UNSET
    store_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_order_id = self.seller_order_id
        transaction_posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_posted_date, Unset):
            transaction_posted_date = self.transaction_posted_date.isoformat()

        business_object_type = self.business_object_type
        sales_channel = self.sales_channel
        charge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.charge, Unset):
            charge = self.charge.to_dict()

        fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fee_list, Unset):
            fee_list = []
            for componentsschemas_fee_component_list_item_data in self.fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                fee_list.append(componentsschemas_fee_component_list_item)

        payment_amount_type = self.payment_amount_type
        amount_description = self.amount_description
        fulfillment_channel = self.fulfillment_channel
        store_name = self.store_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seller_order_id is not UNSET:
            field_dict["SellerOrderId"] = seller_order_id
        if transaction_posted_date is not UNSET:
            field_dict["TransactionPostedDate"] = transaction_posted_date
        if business_object_type is not UNSET:
            field_dict["BusinessObjectType"] = business_object_type
        if sales_channel is not UNSET:
            field_dict["SalesChannel"] = sales_channel
        if charge is not UNSET:
            field_dict["Charge"] = charge
        if fee_list is not UNSET:
            field_dict["FeeList"] = fee_list
        if payment_amount_type is not UNSET:
            field_dict["PaymentAmountType"] = payment_amount_type
        if amount_description is not UNSET:
            field_dict["AmountDescription"] = amount_description
        if fulfillment_channel is not UNSET:
            field_dict["FulfillmentChannel"] = fulfillment_channel
        if store_name is not UNSET:
            field_dict["StoreName"] = store_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent
        from ..models.fee_component import FeeComponent

        d = src_dict.copy()
        seller_order_id = d.pop("SellerOrderId", UNSET)

        _transaction_posted_date = d.pop("TransactionPostedDate", UNSET)
        transaction_posted_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_posted_date, Unset):
            transaction_posted_date = UNSET
        else:
            transaction_posted_date = isoparse(_transaction_posted_date)

        business_object_type = d.pop("BusinessObjectType", UNSET)

        sales_channel = d.pop("SalesChannel", UNSET)

        _charge = d.pop("Charge", UNSET)
        charge: Union[Unset, ChargeComponent]
        if isinstance(_charge, Unset):
            charge = UNSET
        else:
            charge = ChargeComponent.from_dict(_charge)

        fee_list = []
        _fee_list = d.pop("FeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            fee_list.append(componentsschemas_fee_component_list_item)

        payment_amount_type = d.pop("PaymentAmountType", UNSET)

        amount_description = d.pop("AmountDescription", UNSET)

        fulfillment_channel = d.pop("FulfillmentChannel", UNSET)

        store_name = d.pop("StoreName", UNSET)

        result = cls(
            seller_order_id=seller_order_id,
            transaction_posted_date=transaction_posted_date,
            business_object_type=business_object_type,
            sales_channel=sales_channel,
            charge=charge,
            fee_list=fee_list,
            payment_amount_type=payment_amount_type,
            amount_description=amount_description,
            fulfillment_channel=fulfillment_channel,
            store_name=store_name,
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
