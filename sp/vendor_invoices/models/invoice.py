import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.invoice_invoice_type import InvoiceInvoiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_details import AdditionalDetails
    from ..models.allowance_details import AllowanceDetails
    from ..models.charge_details import ChargeDetails
    from ..models.invoice_item import InvoiceItem
    from ..models.money import Money
    from ..models.party_identification import PartyIdentification
    from ..models.payment_terms import PaymentTerms
    from ..models.tax_details import TaxDetails


T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    r"""
    Attributes:
        invoice_type (InvoiceInvoiceType): Identifies the type of invoice.
        id (str): Unique number relating to the charges defined in this document. This will be invoice number if the
            document type is Invoice or CreditNote number if the document type is Credit Note. Failure to provide this
            reference will result in a rejection.
        date (datetime.datetime): Defines a date and time according to ISO8601.
        remit_to_party (PartyIdentification):
        invoice_total (Money): An amount of money, including units in the form of currency.
        reference_number (Union[Unset, str]): An additional unique reference number used for regulatory or other
            purposes.
        ship_to_party (Union[Unset, PartyIdentification]):
        ship_from_party (Union[Unset, PartyIdentification]):
        bill_to_party (Union[Unset, PartyIdentification]):
        payment_terms (Union[Unset, PaymentTerms]): Terms of the payment for the invoice. The basis of the payment terms
            is the invoice date.
        tax_details (Union[Unset, List['TaxDetails']]): Total tax amount details for all line items.
        additional_details (Union[Unset, List['AdditionalDetails']]): Additional details provided by the selling party,
            for tax related or other purposes.
        charge_details (Union[Unset, List['ChargeDetails']]): Total charge amount details for all line items.
        allowance_details (Union[Unset, List['AllowanceDetails']]): Total allowance amount details for all line items.
        items (Union[Unset, List['InvoiceItem']]): The list of invoice items.
    """

    invoice_type: InvoiceInvoiceType
    id: str
    date: datetime.datetime
    remit_to_party: "PartyIdentification"
    invoice_total: "Money"
    reference_number: Union[Unset, str] = UNSET
    ship_to_party: Union[Unset, "PartyIdentification"] = UNSET
    ship_from_party: Union[Unset, "PartyIdentification"] = UNSET
    bill_to_party: Union[Unset, "PartyIdentification"] = UNSET
    payment_terms: Union[Unset, "PaymentTerms"] = UNSET
    tax_details: Union[Unset, List["TaxDetails"]] = UNSET
    additional_details: Union[Unset, List["AdditionalDetails"]] = UNSET
    charge_details: Union[Unset, List["ChargeDetails"]] = UNSET
    allowance_details: Union[Unset, List["AllowanceDetails"]] = UNSET
    items: Union[Unset, List["InvoiceItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_type = self.invoice_type.value

        id = self.id
        date = self.date.isoformat()

        remit_to_party = self.remit_to_party.to_dict()

        invoice_total = self.invoice_total.to_dict()

        reference_number = self.reference_number
        ship_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_party, Unset):
            ship_to_party = self.ship_to_party.to_dict()

        ship_from_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_from_party, Unset):
            ship_from_party = self.ship_from_party.to_dict()

        bill_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_to_party, Unset):
            bill_to_party = self.bill_to_party.to_dict()

        payment_terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_terms, Unset):
            payment_terms = self.payment_terms.to_dict()

        tax_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_details, Unset):
            tax_details = []
            for tax_details_item_data in self.tax_details:
                tax_details_item = tax_details_item_data.to_dict()

                tax_details.append(tax_details_item)

        additional_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_details, Unset):
            additional_details = []
            for additional_details_item_data in self.additional_details:
                additional_details_item = additional_details_item_data.to_dict()

                additional_details.append(additional_details_item)

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

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceType": invoice_type,
                "id": id,
                "date": date,
                "remitToParty": remit_to_party,
                "invoiceTotal": invoice_total,
            }
        )
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if ship_to_party is not UNSET:
            field_dict["shipToParty"] = ship_to_party
        if ship_from_party is not UNSET:
            field_dict["shipFromParty"] = ship_from_party
        if bill_to_party is not UNSET:
            field_dict["billToParty"] = bill_to_party
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details
        if additional_details is not UNSET:
            field_dict["additionalDetails"] = additional_details
        if charge_details is not UNSET:
            field_dict["chargeDetails"] = charge_details
        if allowance_details is not UNSET:
            field_dict["allowanceDetails"] = allowance_details
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_details import AdditionalDetails
        from ..models.allowance_details import AllowanceDetails
        from ..models.charge_details import ChargeDetails
        from ..models.invoice_item import InvoiceItem
        from ..models.money import Money
        from ..models.party_identification import PartyIdentification
        from ..models.payment_terms import PaymentTerms
        from ..models.tax_details import TaxDetails

        d = src_dict.copy()
        invoice_type = InvoiceInvoiceType(d.pop("invoiceType"))

        id = d.pop("id")

        date = isoparse(d.pop("date"))

        remit_to_party = PartyIdentification.from_dict(d.pop("remitToParty"))

        invoice_total = Money.from_dict(d.pop("invoiceTotal"))

        reference_number = d.pop("referenceNumber", UNSET)

        _ship_to_party = d.pop("shipToParty", UNSET)
        ship_to_party: Union[Unset, PartyIdentification]
        if isinstance(_ship_to_party, Unset):
            ship_to_party = UNSET
        else:
            ship_to_party = PartyIdentification.from_dict(_ship_to_party)

        _ship_from_party = d.pop("shipFromParty", UNSET)
        ship_from_party: Union[Unset, PartyIdentification]
        if isinstance(_ship_from_party, Unset):
            ship_from_party = UNSET
        else:
            ship_from_party = PartyIdentification.from_dict(_ship_from_party)

        _bill_to_party = d.pop("billToParty", UNSET)
        bill_to_party: Union[Unset, PartyIdentification]
        if isinstance(_bill_to_party, Unset):
            bill_to_party = UNSET
        else:
            bill_to_party = PartyIdentification.from_dict(_bill_to_party)

        _payment_terms = d.pop("paymentTerms", UNSET)
        payment_terms: Union[Unset, PaymentTerms]
        if isinstance(_payment_terms, Unset):
            payment_terms = UNSET
        else:
            payment_terms = PaymentTerms.from_dict(_payment_terms)

        tax_details = []
        _tax_details = d.pop("taxDetails", UNSET)
        for tax_details_item_data in _tax_details or []:
            tax_details_item = TaxDetails.from_dict(tax_details_item_data)

            tax_details.append(tax_details_item)

        additional_details = []
        _additional_details = d.pop("additionalDetails", UNSET)
        for additional_details_item_data in _additional_details or []:
            additional_details_item = AdditionalDetails.from_dict(additional_details_item_data)

            additional_details.append(additional_details_item)

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

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        result = cls(
            invoice_type=invoice_type,
            id=id,
            date=date,
            remit_to_party=remit_to_party,
            invoice_total=invoice_total,
            reference_number=reference_number,
            ship_to_party=ship_to_party,
            ship_from_party=ship_from_party,
            bill_to_party=bill_to_party,
            payment_terms=payment_terms,
            tax_details=tax_details,
            additional_details=additional_details,
            charge_details=charge_details,
            allowance_details=allowance_details,
            items=items,
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
