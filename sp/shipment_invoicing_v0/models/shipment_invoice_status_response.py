from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_invoice_status_info import ShipmentInvoiceStatusInfo


T = TypeVar("T", bound="ShipmentInvoiceStatusResponse")


@attr.s(auto_attribs=True)
class ShipmentInvoiceStatusResponse:
    r"""The shipment invoice status response.

    Attributes:
        shipments (Union[Unset, ShipmentInvoiceStatusInfo]): The shipment invoice status information.
    """

    shipments: Union[Unset, "ShipmentInvoiceStatusInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipments, Unset):
            shipments = self.shipments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipments is not UNSET:
            field_dict["Shipments"] = shipments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shipment_invoice_status_info import ShipmentInvoiceStatusInfo

        d = src_dict.copy()
        _shipments = d.pop("Shipments", UNSET)
        shipments: Union[Unset, ShipmentInvoiceStatusInfo]
        if isinstance(_shipments, Unset):
            shipments = UNSET
        else:
            shipments = ShipmentInvoiceStatusInfo.from_dict(_shipments)

        result = cls(
            shipments=shipments,
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
