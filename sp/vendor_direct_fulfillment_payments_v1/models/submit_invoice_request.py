from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_detail import InvoiceDetail


T = TypeVar("T", bound="SubmitInvoiceRequest")


@attr.s(auto_attribs=True)
class SubmitInvoiceRequest:
    r"""The request schema for the submitInvoice operation.

    Attributes:
        invoices (Union[Unset, List['InvoiceDetail']]):
    """

    invoices: Union[Unset, List["InvoiceDetail"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()

                invoices.append(invoices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoices is not UNSET:
            field_dict["invoices"] = invoices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_detail import InvoiceDetail

        d = src_dict.copy()
        invoices = []
        _invoices = d.pop("invoices", UNSET)
        for invoices_item_data in _invoices or []:
            invoices_item = InvoiceDetail.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        result = cls(
            invoices=invoices,
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
