from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_invoice import CustomerInvoice
    from ..models.pagination import Pagination


T = TypeVar("T", bound="CustomerInvoiceList")


@attr.s(auto_attribs=True)
class CustomerInvoiceList:
    r"""
    Attributes:
        pagination (Union[Unset, Pagination]):
        customer_invoices (Union[Unset, List['CustomerInvoice']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    customer_invoices: Union[Unset, List["CustomerInvoice"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        customer_invoices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.customer_invoices, Unset):
            customer_invoices = []
            for customer_invoices_item_data in self.customer_invoices:
                customer_invoices_item = customer_invoices_item_data.to_dict()

                customer_invoices.append(customer_invoices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if customer_invoices is not UNSET:
            field_dict["customerInvoices"] = customer_invoices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_invoice import CustomerInvoice
        from ..models.pagination import Pagination

        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        customer_invoices = []
        _customer_invoices = d.pop("customerInvoices", UNSET)
        for customer_invoices_item_data in _customer_invoices or []:
            customer_invoices_item = CustomerInvoice.from_dict(customer_invoices_item_data)

            customer_invoices.append(customer_invoices_item)

        result = cls(
            pagination=pagination,
            customer_invoices=customer_invoices,
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
