from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.researching_quantity import ResearchingQuantity
    from ..models.reserved_quantity import ReservedQuantity
    from ..models.unfulfillable_quantity import UnfulfillableQuantity


T = TypeVar("T", bound="InventoryDetails")


@attr.s(auto_attribs=True)
class InventoryDetails:
    r"""Summarized inventory details. This object will not appear if the details parameter in the request is false.

    Attributes:
        fulfillable_quantity (Union[Unset, int]): The item quantity that can be picked, packed, and shipped.
        inbound_working_quantity (Union[Unset, int]): The number of units in an inbound shipment for which you have
            notified Amazon.
        inbound_shipped_quantity (Union[Unset, int]): The number of units in an inbound shipment that you have notified
            Amazon about and have provided a tracking number.
        inbound_receiving_quantity (Union[Unset, int]): The number of units that have not yet been received at an Amazon
            fulfillment center for processing, but are part of an inbound shipment with some units that have already been
            received and processed.
        reserved_quantity (Union[Unset, ReservedQuantity]): The quantity of reserved inventory.
        researching_quantity (Union[Unset, ResearchingQuantity]): The number of misplaced or warehouse damaged units
            that are actively being confirmed at our fulfillment centers.
        unfulfillable_quantity (Union[Unset, UnfulfillableQuantity]): The quantity of unfulfillable inventory.
    """

    fulfillable_quantity: Union[Unset, int] = UNSET
    inbound_working_quantity: Union[Unset, int] = UNSET
    inbound_shipped_quantity: Union[Unset, int] = UNSET
    inbound_receiving_quantity: Union[Unset, int] = UNSET
    reserved_quantity: Union[Unset, "ReservedQuantity"] = UNSET
    researching_quantity: Union[Unset, "ResearchingQuantity"] = UNSET
    unfulfillable_quantity: Union[Unset, "UnfulfillableQuantity"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillable_quantity = self.fulfillable_quantity
        inbound_working_quantity = self.inbound_working_quantity
        inbound_shipped_quantity = self.inbound_shipped_quantity
        inbound_receiving_quantity = self.inbound_receiving_quantity
        reserved_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reserved_quantity, Unset):
            reserved_quantity = self.reserved_quantity.to_dict()

        researching_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.researching_quantity, Unset):
            researching_quantity = self.researching_quantity.to_dict()

        unfulfillable_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unfulfillable_quantity, Unset):
            unfulfillable_quantity = self.unfulfillable_quantity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillable_quantity is not UNSET:
            field_dict["fulfillableQuantity"] = fulfillable_quantity
        if inbound_working_quantity is not UNSET:
            field_dict["inboundWorkingQuantity"] = inbound_working_quantity
        if inbound_shipped_quantity is not UNSET:
            field_dict["inboundShippedQuantity"] = inbound_shipped_quantity
        if inbound_receiving_quantity is not UNSET:
            field_dict["inboundReceivingQuantity"] = inbound_receiving_quantity
        if reserved_quantity is not UNSET:
            field_dict["reservedQuantity"] = reserved_quantity
        if researching_quantity is not UNSET:
            field_dict["researchingQuantity"] = researching_quantity
        if unfulfillable_quantity is not UNSET:
            field_dict["unfulfillableQuantity"] = unfulfillable_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.researching_quantity import ResearchingQuantity
        from ..models.reserved_quantity import ReservedQuantity
        from ..models.unfulfillable_quantity import UnfulfillableQuantity

        d = src_dict.copy()
        fulfillable_quantity = d.pop("fulfillableQuantity", UNSET)

        inbound_working_quantity = d.pop("inboundWorkingQuantity", UNSET)

        inbound_shipped_quantity = d.pop("inboundShippedQuantity", UNSET)

        inbound_receiving_quantity = d.pop("inboundReceivingQuantity", UNSET)

        _reserved_quantity = d.pop("reservedQuantity", UNSET)
        reserved_quantity: Union[Unset, ReservedQuantity]
        if isinstance(_reserved_quantity, Unset):
            reserved_quantity = UNSET
        else:
            reserved_quantity = ReservedQuantity.from_dict(_reserved_quantity)

        _researching_quantity = d.pop("researchingQuantity", UNSET)
        researching_quantity: Union[Unset, ResearchingQuantity]
        if isinstance(_researching_quantity, Unset):
            researching_quantity = UNSET
        else:
            researching_quantity = ResearchingQuantity.from_dict(_researching_quantity)

        _unfulfillable_quantity = d.pop("unfulfillableQuantity", UNSET)
        unfulfillable_quantity: Union[Unset, UnfulfillableQuantity]
        if isinstance(_unfulfillable_quantity, Unset):
            unfulfillable_quantity = UNSET
        else:
            unfulfillable_quantity = UnfulfillableQuantity.from_dict(_unfulfillable_quantity)

        result = cls(
            fulfillable_quantity=fulfillable_quantity,
            inbound_working_quantity=inbound_working_quantity,
            inbound_shipped_quantity=inbound_shipped_quantity,
            inbound_receiving_quantity=inbound_receiving_quantity,
            reserved_quantity=reserved_quantity,
            researching_quantity=researching_quantity,
            unfulfillable_quantity=unfulfillable_quantity,
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
