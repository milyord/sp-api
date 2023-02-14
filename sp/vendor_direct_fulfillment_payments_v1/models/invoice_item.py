from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_details import ChargeDetails
    from ..models.item_quantity import ItemQuantity
    from ..models.money import Money
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="InvoiceItem")


@attr.s(auto_attribs=True)
class InvoiceItem:
    r"""
    Attributes:
        item_sequence_number (str): Numbering of the item on the purchase order. The first item will be 1, the second 2,
            and so on.
        invoiced_quantity (ItemQuantity): Details of item quantity.
        net_cost (Money): An amount of money, including units in the form of currency.
        purchase_order_number (str): The purchase order number for this order. Formatting Notes: 8-character alpha-
            numeric code.
        buyer_product_identifier (Union[Unset, str]): Buyer's standard identification number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item.
        vendor_order_number (Union[Unset, str]): The vendor's order number for this order.
        hsn_code (Union[Unset, str]): HSN tax code. The HSN number cannot contain alphabets.
        tax_details (Union[Unset, List['TaxDetail']]): Individual tax details per line item.
        charge_details (Union[Unset, List['ChargeDetails']]): Individual charge details per line item.
    """

    item_sequence_number: str
    invoiced_quantity: "ItemQuantity"
    net_cost: "Money"
    purchase_order_number: str
    buyer_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    vendor_order_number: Union[Unset, str] = UNSET
    hsn_code: Union[Unset, str] = UNSET
    tax_details: Union[Unset, List["TaxDetail"]] = UNSET
    charge_details: Union[Unset, List["ChargeDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        invoiced_quantity = self.invoiced_quantity.to_dict()

        net_cost = self.net_cost.to_dict()

        purchase_order_number = self.purchase_order_number
        buyer_product_identifier = self.buyer_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        vendor_order_number = self.vendor_order_number
        hsn_code = self.hsn_code
        tax_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_details, Unset):
            tax_details = []
            for tax_details_item_data in self.tax_details:
                tax_details_item = tax_details_item_data.to_dict()

                tax_details.append(tax_details_item)

        charge_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.charge_details, Unset):
            charge_details = []
            for charge_details_item_data in self.charge_details:
                charge_details_item = charge_details_item_data.to_dict()

                charge_details.append(charge_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
                "invoicedQuantity": invoiced_quantity,
                "netCost": net_cost,
                "purchaseOrderNumber": purchase_order_number,
            }
        )
        if buyer_product_identifier is not UNSET:
            field_dict["buyerProductIdentifier"] = buyer_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if vendor_order_number is not UNSET:
            field_dict["vendorOrderNumber"] = vendor_order_number
        if hsn_code is not UNSET:
            field_dict["hsnCode"] = hsn_code
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details
        if charge_details is not UNSET:
            field_dict["chargeDetails"] = charge_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_details import ChargeDetails
        from ..models.item_quantity import ItemQuantity
        from ..models.money import Money
        from ..models.tax_detail import TaxDetail

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        invoiced_quantity = ItemQuantity.from_dict(d.pop("invoicedQuantity"))

        net_cost = Money.from_dict(d.pop("netCost"))

        purchase_order_number = d.pop("purchaseOrderNumber")

        buyer_product_identifier = d.pop("buyerProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        vendor_order_number = d.pop("vendorOrderNumber", UNSET)

        hsn_code = d.pop("hsnCode", UNSET)

        tax_details = []
        _tax_details = d.pop("taxDetails", UNSET)
        for tax_details_item_data in _tax_details or []:
            tax_details_item = TaxDetail.from_dict(tax_details_item_data)

            tax_details.append(tax_details_item)

        charge_details = []
        _charge_details = d.pop("chargeDetails", UNSET)
        for charge_details_item_data in _charge_details or []:
            charge_details_item = ChargeDetails.from_dict(charge_details_item_data)

            charge_details.append(charge_details_item)

        result = cls(
            item_sequence_number=item_sequence_number,
            invoiced_quantity=invoiced_quantity,
            net_cost=net_cost,
            purchase_order_number=purchase_order_number,
            buyer_product_identifier=buyer_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            vendor_order_number=vendor_order_number,
            hsn_code=hsn_code,
            tax_details=tax_details,
            charge_details=charge_details,
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
