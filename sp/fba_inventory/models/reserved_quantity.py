from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReservedQuantity")


@attr.s(auto_attribs=True)
class ReservedQuantity:
    r"""The quantity of reserved inventory.

    Attributes:
        total_reserved_quantity (Union[Unset, int]): The total number of units in Amazon's fulfillment network that are
            currently being picked, packed, and shipped; or are sidelined for measurement, sampling, or other internal
            processes.
        pending_customer_order_quantity (Union[Unset, int]): The number of units reserved for customer orders.
        pending_transshipment_quantity (Union[Unset, int]): The number of units being transferred from one fulfillment
            center to another.
        fc_processing_quantity (Union[Unset, int]): The number of units that have been sidelined at the fulfillment
            center for additional processing.
    """

    total_reserved_quantity: Union[Unset, int] = UNSET
    pending_customer_order_quantity: Union[Unset, int] = UNSET
    pending_transshipment_quantity: Union[Unset, int] = UNSET
    fc_processing_quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_reserved_quantity = self.total_reserved_quantity
        pending_customer_order_quantity = self.pending_customer_order_quantity
        pending_transshipment_quantity = self.pending_transshipment_quantity
        fc_processing_quantity = self.fc_processing_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_reserved_quantity is not UNSET:
            field_dict["totalReservedQuantity"] = total_reserved_quantity
        if pending_customer_order_quantity is not UNSET:
            field_dict["pendingCustomerOrderQuantity"] = pending_customer_order_quantity
        if pending_transshipment_quantity is not UNSET:
            field_dict["pendingTransshipmentQuantity"] = pending_transshipment_quantity
        if fc_processing_quantity is not UNSET:
            field_dict["fcProcessingQuantity"] = fc_processing_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_reserved_quantity = d.pop("totalReservedQuantity", UNSET)

        pending_customer_order_quantity = d.pop("pendingCustomerOrderQuantity", UNSET)

        pending_transshipment_quantity = d.pop("pendingTransshipmentQuantity", UNSET)

        fc_processing_quantity = d.pop("fcProcessingQuantity", UNSET)

        result = cls(
            total_reserved_quantity=total_reserved_quantity,
            pending_customer_order_quantity=pending_customer_order_quantity,
            pending_transshipment_quantity=pending_transshipment_quantity,
            fc_processing_quantity=fc_processing_quantity,
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
