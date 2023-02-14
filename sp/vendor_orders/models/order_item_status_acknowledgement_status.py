from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_item_status_acknowledgement_status_confirmation_status import (
    OrderItemStatusAcknowledgementStatusConfirmationStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledgement_status_details import AcknowledgementStatusDetails
    from ..models.item_quantity import ItemQuantity


T = TypeVar("T", bound="OrderItemStatusAcknowledgementStatus")


@attr.s(auto_attribs=True)
class OrderItemStatusAcknowledgementStatus:
    r"""Acknowledgement status information.

    Attributes:
        confirmation_status (Union[Unset, OrderItemStatusAcknowledgementStatusConfirmationStatus]): Confirmation status
            of line item.
        accepted_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
        rejected_quantity (Union[Unset, ItemQuantity]): Details of quantity ordered.
        acknowledgement_status_details (Union[Unset, List['AcknowledgementStatusDetails']]): Details of item quantity
            confirmed.
    """

    confirmation_status: Union[Unset, OrderItemStatusAcknowledgementStatusConfirmationStatus] = UNSET
    accepted_quantity: Union[Unset, "ItemQuantity"] = UNSET
    rejected_quantity: Union[Unset, "ItemQuantity"] = UNSET
    acknowledgement_status_details: Union[Unset, List["AcknowledgementStatusDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confirmation_status: Union[Unset, str] = UNSET
        if not isinstance(self.confirmation_status, Unset):
            confirmation_status = self.confirmation_status.value

        accepted_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accepted_quantity, Unset):
            accepted_quantity = self.accepted_quantity.to_dict()

        rejected_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejected_quantity, Unset):
            rejected_quantity = self.rejected_quantity.to_dict()

        acknowledgement_status_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acknowledgement_status_details, Unset):
            acknowledgement_status_details = []
            for acknowledgement_status_details_item_data in self.acknowledgement_status_details:
                acknowledgement_status_details_item = acknowledgement_status_details_item_data.to_dict()

                acknowledgement_status_details.append(acknowledgement_status_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmation_status is not UNSET:
            field_dict["confirmationStatus"] = confirmation_status
        if accepted_quantity is not UNSET:
            field_dict["acceptedQuantity"] = accepted_quantity
        if rejected_quantity is not UNSET:
            field_dict["rejectedQuantity"] = rejected_quantity
        if acknowledgement_status_details is not UNSET:
            field_dict["acknowledgementStatusDetails"] = acknowledgement_status_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acknowledgement_status_details import AcknowledgementStatusDetails
        from ..models.item_quantity import ItemQuantity

        d = src_dict.copy()
        _confirmation_status = d.pop("confirmationStatus", UNSET)
        confirmation_status: Union[Unset, OrderItemStatusAcknowledgementStatusConfirmationStatus]
        if isinstance(_confirmation_status, Unset):
            confirmation_status = UNSET
        else:
            confirmation_status = OrderItemStatusAcknowledgementStatusConfirmationStatus(_confirmation_status)

        _accepted_quantity = d.pop("acceptedQuantity", UNSET)
        accepted_quantity: Union[Unset, ItemQuantity]
        if isinstance(_accepted_quantity, Unset):
            accepted_quantity = UNSET
        else:
            accepted_quantity = ItemQuantity.from_dict(_accepted_quantity)

        _rejected_quantity = d.pop("rejectedQuantity", UNSET)
        rejected_quantity: Union[Unset, ItemQuantity]
        if isinstance(_rejected_quantity, Unset):
            rejected_quantity = UNSET
        else:
            rejected_quantity = ItemQuantity.from_dict(_rejected_quantity)

        acknowledgement_status_details = []
        _acknowledgement_status_details = d.pop("acknowledgementStatusDetails", UNSET)
        for acknowledgement_status_details_item_data in _acknowledgement_status_details or []:
            acknowledgement_status_details_item = AcknowledgementStatusDetails.from_dict(
                acknowledgement_status_details_item_data
            )

            acknowledgement_status_details.append(acknowledgement_status_details_item)

        result = cls(
            confirmation_status=confirmation_status,
            accepted_quantity=accepted_quantity,
            rejected_quantity=rejected_quantity,
            acknowledgement_status_details=acknowledgement_status_details,
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
