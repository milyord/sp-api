from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentShipmentItem")


@attr.s(auto_attribs=True)
class FulfillmentShipmentItem:
    r"""Item information for a shipment in a fulfillment order.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        seller_fulfillment_order_item_id (str): The fulfillment order item identifier that the seller created and
            submitted with a call to the createFulfillmentOrder operation.
        quantity (int): The item quantity.
        package_number (Union[Unset, int]): An identifier for the package that contains the item quantity.
        serial_number (Union[Unset, str]): The serial number of the shipped item.
    """

    seller_sku: str
    seller_fulfillment_order_item_id: str
    quantity: int
    package_number: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        quantity = self.quantity
        package_number = self.package_number
        serial_number = self.serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerSku": seller_sku,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
                "quantity": quantity,
            }
        )
        if package_number is not UNSET:
            field_dict["packageNumber"] = package_number
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_sku = d.pop("sellerSku")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        quantity = d.pop("quantity")

        package_number = d.pop("packageNumber", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        result = cls(
            seller_sku=seller_sku,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            quantity=quantity,
            package_number=package_number,
            serial_number=serial_number,
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
