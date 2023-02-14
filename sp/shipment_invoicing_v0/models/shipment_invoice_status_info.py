from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.shipment_invoice_status import ShipmentInvoiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipmentInvoiceStatusInfo")


@attr.s(auto_attribs=True)
class ShipmentInvoiceStatusInfo:
    r"""The shipment invoice status information.

    Attributes:
        amazon_shipment_id (Union[Unset, str]): The Amazon-defined shipment identifier.
        invoice_status (Union[Unset, ShipmentInvoiceStatus]): The shipment invoice status.
    """

    amazon_shipment_id: Union[Unset, str] = UNSET
    invoice_status: Union[Unset, ShipmentInvoiceStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_shipment_id = self.amazon_shipment_id
        invoice_status: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_status, Unset):
            invoice_status = self.invoice_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_shipment_id is not UNSET:
            field_dict["AmazonShipmentId"] = amazon_shipment_id
        if invoice_status is not UNSET:
            field_dict["InvoiceStatus"] = invoice_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amazon_shipment_id = d.pop("AmazonShipmentId", UNSET)

        _invoice_status = d.pop("InvoiceStatus", UNSET)
        invoice_status: Union[Unset, ShipmentInvoiceStatus]
        if isinstance(_invoice_status, Unset):
            invoice_status = UNSET
        else:
            invoice_status = ShipmentInvoiceStatus(_invoice_status)

        result = cls(
            amazon_shipment_id=amazon_shipment_id,
            invoice_status=invoice_status,
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
