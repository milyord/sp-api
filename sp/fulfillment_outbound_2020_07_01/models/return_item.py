import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.fulfillment_return_item_status import FulfillmentReturnItemStatus
from ..models.return_item_disposition import ReturnItemDisposition
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReturnItem")


@attr.s(auto_attribs=True)
class ReturnItem:
    r"""An item that Amazon accepted for return.

    Attributes:
        seller_return_item_id (str): An identifier assigned by the seller to the return item.
        seller_fulfillment_order_item_id (str): The identifier assigned to the item by the seller when the fulfillment
            order was created.
        amazon_shipment_id (str): The identifier for the shipment that is associated with the return item.
        seller_return_reason_code (str): The return reason code assigned to the return item by the seller.
        status (FulfillmentReturnItemStatus): Indicates if the return item has been processed by a fulfillment center.
        status_changed_date (datetime.datetime):
        return_comment (Union[Unset, str]): An optional comment about the return item.
        amazon_return_reason_code (Union[Unset, str]): The return reason code that the Amazon fulfillment center
            assigned to the return item.
        return_authorization_id (Union[Unset, str]): Identifies the return authorization used to return this item. See
            ReturnAuthorization.
        return_received_condition (Union[Unset, ReturnItemDisposition]): The condition of the return item when received
            by an Amazon fulfillment center.
        fulfillment_center_id (Union[Unset, str]): The identifier for the Amazon fulfillment center that processed the
            return item.
    """

    seller_return_item_id: str
    seller_fulfillment_order_item_id: str
    amazon_shipment_id: str
    seller_return_reason_code: str
    status: FulfillmentReturnItemStatus
    status_changed_date: datetime.datetime
    return_comment: Union[Unset, str] = UNSET
    amazon_return_reason_code: Union[Unset, str] = UNSET
    return_authorization_id: Union[Unset, str] = UNSET
    return_received_condition: Union[Unset, ReturnItemDisposition] = UNSET
    fulfillment_center_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_return_item_id = self.seller_return_item_id
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        amazon_shipment_id = self.amazon_shipment_id
        seller_return_reason_code = self.seller_return_reason_code
        status = self.status.value

        status_changed_date = self.status_changed_date.isoformat()

        return_comment = self.return_comment
        amazon_return_reason_code = self.amazon_return_reason_code
        return_authorization_id = self.return_authorization_id
        return_received_condition: Union[Unset, str] = UNSET
        if not isinstance(self.return_received_condition, Unset):
            return_received_condition = self.return_received_condition.value

        fulfillment_center_id = self.fulfillment_center_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerReturnItemId": seller_return_item_id,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
                "amazonShipmentId": amazon_shipment_id,
                "sellerReturnReasonCode": seller_return_reason_code,
                "status": status,
                "statusChangedDate": status_changed_date,
            }
        )
        if return_comment is not UNSET:
            field_dict["returnComment"] = return_comment
        if amazon_return_reason_code is not UNSET:
            field_dict["amazonReturnReasonCode"] = amazon_return_reason_code
        if return_authorization_id is not UNSET:
            field_dict["returnAuthorizationId"] = return_authorization_id
        if return_received_condition is not UNSET:
            field_dict["returnReceivedCondition"] = return_received_condition
        if fulfillment_center_id is not UNSET:
            field_dict["fulfillmentCenterId"] = fulfillment_center_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_return_item_id = d.pop("sellerReturnItemId")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        amazon_shipment_id = d.pop("amazonShipmentId")

        seller_return_reason_code = d.pop("sellerReturnReasonCode")

        status = FulfillmentReturnItemStatus(d.pop("status"))

        status_changed_date = isoparse(d.pop("statusChangedDate"))

        return_comment = d.pop("returnComment", UNSET)

        amazon_return_reason_code = d.pop("amazonReturnReasonCode", UNSET)

        return_authorization_id = d.pop("returnAuthorizationId", UNSET)

        _return_received_condition = d.pop("returnReceivedCondition", UNSET)
        return_received_condition: Union[Unset, ReturnItemDisposition]
        if isinstance(_return_received_condition, Unset):
            return_received_condition = UNSET
        else:
            return_received_condition = ReturnItemDisposition(_return_received_condition)

        fulfillment_center_id = d.pop("fulfillmentCenterId", UNSET)

        result = cls(
            seller_return_item_id=seller_return_item_id,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            amazon_shipment_id=amazon_shipment_id,
            seller_return_reason_code=seller_return_reason_code,
            status=status,
            status_changed_date=status_changed_date,
            return_comment=return_comment,
            amazon_return_reason_code=amazon_return_reason_code,
            return_authorization_id=return_authorization_id,
            return_received_condition=return_received_condition,
            fulfillment_center_id=fulfillment_center_id,
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
