import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceData")


@attr.s(auto_attribs=True)
class InvoiceData:
    r"""Invoice number and date.

    Attributes:
        invoice_number (str): A string of up to 255 characters.
        invoice_date (Union[Unset, datetime.datetime]): A datetime value in ISO 8601 format.
    """

    invoice_number: str
    invoice_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_number = self.invoice_number
        invoice_date: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_date, Unset):
            invoice_date = self.invoice_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceNumber": invoice_number,
            }
        )
        if invoice_date is not UNSET:
            field_dict["invoiceDate"] = invoice_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_number = d.pop("invoiceNumber")

        _invoice_date = d.pop("invoiceDate", UNSET)
        invoice_date: Union[Unset, datetime.datetime]
        if isinstance(_invoice_date, Unset):
            invoice_date = UNSET
        else:
            invoice_date = isoparse(_invoice_date)

        result = cls(
            invoice_number=invoice_number,
            invoice_date=invoice_date,
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
