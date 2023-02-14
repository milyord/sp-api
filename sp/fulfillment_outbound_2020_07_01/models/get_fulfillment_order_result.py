from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_order import FulfillmentOrder
    from ..models.fulfillment_order_item import FulfillmentOrderItem
    from ..models.fulfillment_shipment import FulfillmentShipment
    from ..models.return_authorization import ReturnAuthorization
    from ..models.return_item import ReturnItem


T = TypeVar("T", bound="GetFulfillmentOrderResult")


@attr.s(auto_attribs=True)
class GetFulfillmentOrderResult:
    r"""
    Attributes:
        fulfillment_order (FulfillmentOrder): General information about a fulfillment order, including its status.
        fulfillment_order_items (List['FulfillmentOrderItem']): An array of fulfillment order item information.
        return_items (List['ReturnItem']): An array of items that Amazon accepted for return. Returns empty if no items
            were accepted for return.
        return_authorizations (List['ReturnAuthorization']): An array of return authorization information.
        fulfillment_shipments (Union[Unset, List['FulfillmentShipment']]): An array of fulfillment shipment information.
    """

    fulfillment_order: "FulfillmentOrder"
    fulfillment_order_items: List["FulfillmentOrderItem"]
    return_items: List["ReturnItem"]
    return_authorizations: List["ReturnAuthorization"]
    fulfillment_shipments: Union[Unset, List["FulfillmentShipment"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillment_order = self.fulfillment_order.to_dict()

        fulfillment_order_items = []
        for componentsschemas_fulfillment_order_item_list_item_data in self.fulfillment_order_items:
            componentsschemas_fulfillment_order_item_list_item = (
                componentsschemas_fulfillment_order_item_list_item_data.to_dict()
            )

            fulfillment_order_items.append(componentsschemas_fulfillment_order_item_list_item)

        return_items = []
        for componentsschemas_return_item_list_item_data in self.return_items:
            componentsschemas_return_item_list_item = componentsschemas_return_item_list_item_data.to_dict()

            return_items.append(componentsschemas_return_item_list_item)

        return_authorizations = []
        for componentsschemas_return_authorization_list_item_data in self.return_authorizations:
            componentsschemas_return_authorization_list_item = (
                componentsschemas_return_authorization_list_item_data.to_dict()
            )

            return_authorizations.append(componentsschemas_return_authorization_list_item)

        fulfillment_shipments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_shipments, Unset):
            fulfillment_shipments = []
            for componentsschemas_fulfillment_shipment_list_item_data in self.fulfillment_shipments:
                componentsschemas_fulfillment_shipment_list_item = (
                    componentsschemas_fulfillment_shipment_list_item_data.to_dict()
                )

                fulfillment_shipments.append(componentsschemas_fulfillment_shipment_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fulfillmentOrder": fulfillment_order,
                "fulfillmentOrderItems": fulfillment_order_items,
                "returnItems": return_items,
                "returnAuthorizations": return_authorizations,
            }
        )
        if fulfillment_shipments is not UNSET:
            field_dict["fulfillmentShipments"] = fulfillment_shipments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfillment_order import FulfillmentOrder
        from ..models.fulfillment_order_item import FulfillmentOrderItem
        from ..models.fulfillment_shipment import FulfillmentShipment
        from ..models.return_authorization import ReturnAuthorization
        from ..models.return_item import ReturnItem

        d = src_dict.copy()
        fulfillment_order = FulfillmentOrder.from_dict(d.pop("fulfillmentOrder"))

        fulfillment_order_items = []
        _fulfillment_order_items = d.pop("fulfillmentOrderItems")
        for componentsschemas_fulfillment_order_item_list_item_data in _fulfillment_order_items:
            componentsschemas_fulfillment_order_item_list_item = FulfillmentOrderItem.from_dict(
                componentsschemas_fulfillment_order_item_list_item_data
            )

            fulfillment_order_items.append(componentsschemas_fulfillment_order_item_list_item)

        return_items = []
        _return_items = d.pop("returnItems")
        for componentsschemas_return_item_list_item_data in _return_items:
            componentsschemas_return_item_list_item = ReturnItem.from_dict(componentsschemas_return_item_list_item_data)

            return_items.append(componentsschemas_return_item_list_item)

        return_authorizations = []
        _return_authorizations = d.pop("returnAuthorizations")
        for componentsschemas_return_authorization_list_item_data in _return_authorizations:
            componentsschemas_return_authorization_list_item = ReturnAuthorization.from_dict(
                componentsschemas_return_authorization_list_item_data
            )

            return_authorizations.append(componentsschemas_return_authorization_list_item)

        fulfillment_shipments = []
        _fulfillment_shipments = d.pop("fulfillmentShipments", UNSET)
        for componentsschemas_fulfillment_shipment_list_item_data in _fulfillment_shipments or []:
            componentsschemas_fulfillment_shipment_list_item = FulfillmentShipment.from_dict(
                componentsschemas_fulfillment_shipment_list_item_data
            )

            fulfillment_shipments.append(componentsschemas_fulfillment_shipment_list_item)

        result = cls(
            fulfillment_order=fulfillment_order,
            fulfillment_order_items=fulfillment_order_items,
            return_items=return_items,
            return_authorizations=return_authorizations,
            fulfillment_shipments=fulfillment_shipments,
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
