import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="ProductAdsPaymentEvent")


@attr.s(auto_attribs=True)
class ProductAdsPaymentEvent:
    r"""A Sponsored Products payment event.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        transaction_type (Union[Unset, str]): Indicates if the transaction is for a charge or a refund.

            Possible values:

            * charge - Charge

            * refund - Refund
        invoice_id (Union[Unset, str]): Identifier for the invoice that the transaction appears in.
        base_value (Union[Unset, Currency]): A currency type and amount.
        tax_value (Union[Unset, Currency]): A currency type and amount.
        transaction_value (Union[Unset, Currency]): A currency type and amount.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    transaction_type: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    base_value: Union[Unset, "Currency"] = UNSET
    tax_value: Union[Unset, "Currency"] = UNSET
    transaction_value: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        transaction_type = self.transaction_type
        invoice_id = self.invoice_id
        base_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_value, Unset):
            base_value = self.base_value.to_dict()

        tax_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_value, Unset):
            tax_value = self.tax_value.to_dict()

        transaction_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_value, Unset):
            transaction_value = self.transaction_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if base_value is not UNSET:
            field_dict["baseValue"] = base_value
        if tax_value is not UNSET:
            field_dict["taxValue"] = tax_value
        if transaction_value is not UNSET:
            field_dict["transactionValue"] = transaction_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        transaction_type = d.pop("transactionType", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        _base_value = d.pop("baseValue", UNSET)
        base_value: Union[Unset, Currency]
        if isinstance(_base_value, Unset):
            base_value = UNSET
        else:
            base_value = Currency.from_dict(_base_value)

        _tax_value = d.pop("taxValue", UNSET)
        tax_value: Union[Unset, Currency]
        if isinstance(_tax_value, Unset):
            tax_value = UNSET
        else:
            tax_value = Currency.from_dict(_tax_value)

        _transaction_value = d.pop("transactionValue", UNSET)
        transaction_value: Union[Unset, Currency]
        if isinstance(_transaction_value, Unset):
            transaction_value = UNSET
        else:
            transaction_value = Currency.from_dict(_transaction_value)

        result = cls(
            posted_date=posted_date,
            transaction_type=transaction_type,
            invoice_id=invoice_id,
            base_value=base_value,
            tax_value=tax_value,
            transaction_value=transaction_value,
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
