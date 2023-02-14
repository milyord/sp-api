from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowance_details import AllowanceDetails
    from ..models.charge_details import ChargeDetails
    from ..models.credit_note_details import CreditNoteDetails
    from ..models.item_quantity import ItemQuantity
    from ..models.money import Money
    from ..models.tax_details import TaxDetails


T = TypeVar("T", bound="InvoiceItem")


@attr.s(auto_attribs=True)
class InvoiceItem:
    r"""Details of the item being invoiced.

    Attributes:
        item_sequence_number (int): Unique number related to this line item.
        invoiced_quantity (ItemQuantity): Details of quantity.
        net_cost (Money): An amount of money, including units in the form of currency.
        amazon_product_identifier (Union[Unset, str]): Amazon Standard Identification Number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identifier of the item. Should be the
            same as was provided in the purchase order.
        purchase_order_number (Union[Unset, str]): The Amazon purchase order number for this invoiced line item.
            Formatting Notes: 8-character alpha-numeric code. This value is mandatory only when invoiceType is Invoice, and
            is not required when invoiceType is CreditNote.
        hsn_code (Union[Unset, str]): HSN Tax code. The HSN number cannot contain alphabets.
        credit_note_details (Union[Unset, CreditNoteDetails]): References required in order to process a credit note.
            This information is required only if InvoiceType is CreditNote.
        tax_details (Union[Unset, List['TaxDetails']]): Individual tax details per line item.
        charge_details (Union[Unset, List['ChargeDetails']]): Individual charge details per line item.
        allowance_details (Union[Unset, List['AllowanceDetails']]): Individual allowance details per line item.
    """

    item_sequence_number: int
    invoiced_quantity: "ItemQuantity"
    net_cost: "Money"
    amazon_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    purchase_order_number: Union[Unset, str] = UNSET
    hsn_code: Union[Unset, str] = UNSET
    credit_note_details: Union[Unset, "CreditNoteDetails"] = UNSET
    tax_details: Union[Unset, List["TaxDetails"]] = UNSET
    charge_details: Union[Unset, List["ChargeDetails"]] = UNSET
    allowance_details: Union[Unset, List["AllowanceDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        invoiced_quantity = self.invoiced_quantity.to_dict()

        net_cost = self.net_cost.to_dict()

        amazon_product_identifier = self.amazon_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        purchase_order_number = self.purchase_order_number
        hsn_code = self.hsn_code
        credit_note_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_note_details, Unset):
            credit_note_details = self.credit_note_details.to_dict()

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

        allowance_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowance_details, Unset):
            allowance_details = []
            for allowance_details_item_data in self.allowance_details:
                allowance_details_item = allowance_details_item_data.to_dict()

                allowance_details.append(allowance_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
                "invoicedQuantity": invoiced_quantity,
                "netCost": net_cost,
            }
        )
        if amazon_product_identifier is not UNSET:
            field_dict["amazonProductIdentifier"] = amazon_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number
        if hsn_code is not UNSET:
            field_dict["hsnCode"] = hsn_code
        if credit_note_details is not UNSET:
            field_dict["creditNoteDetails"] = credit_note_details
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details
        if charge_details is not UNSET:
            field_dict["chargeDetails"] = charge_details
        if allowance_details is not UNSET:
            field_dict["allowanceDetails"] = allowance_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.allowance_details import AllowanceDetails
        from ..models.charge_details import ChargeDetails
        from ..models.credit_note_details import CreditNoteDetails
        from ..models.item_quantity import ItemQuantity
        from ..models.money import Money
        from ..models.tax_details import TaxDetails

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        invoiced_quantity = ItemQuantity.from_dict(d.pop("invoicedQuantity"))

        net_cost = Money.from_dict(d.pop("netCost"))

        amazon_product_identifier = d.pop("amazonProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        hsn_code = d.pop("hsnCode", UNSET)

        _credit_note_details = d.pop("creditNoteDetails", UNSET)
        credit_note_details: Union[Unset, CreditNoteDetails]
        if isinstance(_credit_note_details, Unset):
            credit_note_details = UNSET
        else:
            credit_note_details = CreditNoteDetails.from_dict(_credit_note_details)

        tax_details = []
        _tax_details = d.pop("taxDetails", UNSET)
        for tax_details_item_data in _tax_details or []:
            tax_details_item = TaxDetails.from_dict(tax_details_item_data)

            tax_details.append(tax_details_item)

        charge_details = []
        _charge_details = d.pop("chargeDetails", UNSET)
        for charge_details_item_data in _charge_details or []:
            charge_details_item = ChargeDetails.from_dict(charge_details_item_data)

            charge_details.append(charge_details_item)

        allowance_details = []
        _allowance_details = d.pop("allowanceDetails", UNSET)
        for allowance_details_item_data in _allowance_details or []:
            allowance_details_item = AllowanceDetails.from_dict(allowance_details_item_data)

            allowance_details.append(allowance_details_item)

        result = cls(
            item_sequence_number=item_sequence_number,
            invoiced_quantity=invoiced_quantity,
            net_cost=net_cost,
            amazon_product_identifier=amazon_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            purchase_order_number=purchase_order_number,
            hsn_code=hsn_code,
            credit_note_details=credit_note_details,
            tax_details=tax_details,
            charge_details=charge_details,
            allowance_details=allowance_details,
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
