from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.shipment_status import ShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_items_item import OrderItemsItem


T = TypeVar("T", bound="UpdateShipmentStatusRequest")


@attr.s(auto_attribs=True)
class UpdateShipmentStatusRequest:
    r"""The request body for the updateShipmentStatus operation.

    Attributes:
        marketplace_id (str): The unobfuscated marketplace identifier.
        shipment_status (ShipmentStatus): The shipment status to apply.
        order_items (Union[Unset, List['OrderItemsItem']]): For partial shipment status updates, the list of order items
            and quantities to be updated.
    """

    marketplace_id: str
    shipment_status: ShipmentStatus
    order_items: Union[Unset, List["OrderItemsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        shipment_status = self.shipment_status.value

        order_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_items, Unset):
            order_items = []
            for componentsschemas_order_items_item_data in self.order_items:
                componentsschemas_order_items_item = componentsschemas_order_items_item_data.to_dict()

                order_items.append(componentsschemas_order_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "shipmentStatus": shipment_status,
            }
        )
        if order_items is not UNSET:
            field_dict["orderItems"] = order_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_items_item import OrderItemsItem

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        shipment_status = ShipmentStatus(d.pop("shipmentStatus"))

        order_items = []
        _order_items = d.pop("orderItems", UNSET)
        for componentsschemas_order_items_item_data in _order_items or []:
            componentsschemas_order_items_item = OrderItemsItem.from_dict(componentsschemas_order_items_item_data)

            order_items.append(componentsschemas_order_items_item)

        result = cls(
            marketplace_id=marketplace_id,
            shipment_status=shipment_status,
            order_items=order_items,
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
