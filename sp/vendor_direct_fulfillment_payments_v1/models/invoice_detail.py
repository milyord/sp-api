import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_details import AdditionalDetails
    from ..models.charge_details import ChargeDetails
    from ..models.invoice_item import InvoiceItem
    from ..models.money import Money
    from ..models.party_identification import PartyIdentification
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="InvoiceDetail")


@attr.s(auto_attribs=True)
class InvoiceDetail:
    r"""
    Attributes:
        invoice_number (str): The unique invoice number.
        invoice_date (datetime.datetime): Invoice date.
        remit_to_party (PartyIdentification):
        ship_from_party (PartyIdentification):
        invoice_total (Money): An amount of money, including units in the form of currency.
        items (List['InvoiceItem']): Provides the details of the items in this invoice.
        reference_number (Union[Unset, str]): An additional unique reference number used for regulatory or other
            purposes.
        bill_to_party (Union[Unset, PartyIdentification]):
        ship_to_country_code (Union[Unset, str]): Ship-to country code.
        payment_terms_code (Union[Unset, str]): The payment terms for the invoice.
        tax_totals (Union[Unset, List['TaxDetail']]): Individual tax details per line item.
        additional_details (Union[Unset, List['AdditionalDetails']]): Additional details provided by the selling party,
            for tax related or other purposes.
        charge_details (Union[Unset, List['ChargeDetails']]): Total charge amount details for all line items.
    """

    invoice_number: str
    invoice_date: datetime.datetime
    remit_to_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    invoice_total: "Money"
    items: List["InvoiceItem"]
    reference_number: Union[Unset, str] = UNSET
    bill_to_party: Union[Unset, "PartyIdentification"] = UNSET
    ship_to_country_code: Union[Unset, str] = UNSET
    payment_terms_code: Union[Unset, str] = UNSET
    tax_totals: Union[Unset, List["TaxDetail"]] = UNSET
    additional_details: Union[Unset, List["AdditionalDetails"]] = UNSET
    charge_details: Union[Unset, List["ChargeDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_number = self.invoice_number
        invoice_date = self.invoice_date.isoformat()

        remit_to_party = self.remit_to_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        invoice_total = self.invoice_total.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        reference_number = self.reference_number
        bill_to_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_to_party, Unset):
            bill_to_party = self.bill_to_party.to_dict()

        ship_to_country_code = self.ship_to_country_code
        payment_terms_code = self.payment_terms_code
        tax_totals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_totals, Unset):
            tax_totals = []
            for tax_totals_item_data in self.tax_totals:
                tax_totals_item = tax_totals_item_data.to_dict()

                tax_totals.append(tax_totals_item)

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceNumber": invoice_number,
                "invoiceDate": invoice_date,
                "remitToParty": remit_to_party,
                "shipFromParty": ship_from_party,
                "invoiceTotal": invoice_total,
                "items": items,
            }
        )
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if bill_to_party is not UNSET:
            field_dict["billToParty"] = bill_to_party
        if ship_to_country_code is not UNSET:
            field_dict["shipToCountryCode"] = ship_to_country_code
        if payment_terms_code is not UNSET:
            field_dict["paymentTermsCode"] = payment_terms_code
        if tax_totals is not UNSET:
            field_dict["taxTotals"] = tax_totals
        if additional_details is not UNSET:
            field_dict["additionalDetails"] = additional_details
        if charge_details is not UNSET:
            field_dict["chargeDetails"] = charge_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_details import AdditionalDetails
        from ..models.charge_details import ChargeDetails
        from ..models.invoice_item import InvoiceItem
        from ..models.money import Money
        from ..models.party_identification import PartyIdentification
        from ..models.tax_detail import TaxDetail

        d = src_dict.copy()
        invoice_number = d.pop("invoiceNumber")

        invoice_date = isoparse(d.pop("invoiceDate"))

        remit_to_party = PartyIdentification.from_dict(d.pop("remitToParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        invoice_total = Money.from_dict(d.pop("invoiceTotal"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        reference_number = d.pop("referenceNumber", UNSET)

        _bill_to_party = d.pop("billToParty", UNSET)
        bill_to_party: Union[Unset, PartyIdentification]
        if isinstance(_bill_to_party, Unset):
            bill_to_party = UNSET
        else:
            bill_to_party = PartyIdentification.from_dict(_bill_to_party)

        ship_to_country_code = d.pop("shipToCountryCode", UNSET)

        payment_terms_code = d.pop("paymentTermsCode", UNSET)

        tax_totals = []
        _tax_totals = d.pop("taxTotals", UNSET)
        for tax_totals_item_data in _tax_totals or []:
            tax_totals_item = TaxDetail.from_dict(tax_totals_item_data)

            tax_totals.append(tax_totals_item)

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

        result = cls(
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            remit_to_party=remit_to_party,
            ship_from_party=ship_from_party,
            invoice_total=invoice_total,
            items=items,
            reference_number=reference_number,
            bill_to_party=bill_to_party,
            ship_to_country_code=ship_to_country_code,
            payment_terms_code=payment_terms_code,
            tax_totals=tax_totals,
            additional_details=additional_details,
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
