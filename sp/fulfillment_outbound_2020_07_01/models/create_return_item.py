from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateReturnItem")


@attr.s(auto_attribs=True)
class CreateReturnItem:
    r"""An item that Amazon accepted for return.

    Attributes:
        seller_return_item_id (str): An identifier assigned by the seller to the return item.
        seller_fulfillment_order_item_id (str): The identifier assigned to the item by the seller when the fulfillment
            order was created.
        amazon_shipment_id (str): The identifier for the shipment that is associated with the return item.
        return_reason_code (str): The return reason code assigned to the return item by the seller.
        return_comment (Union[Unset, str]): An optional comment about the return item.
    """

    seller_return_item_id: str
    seller_fulfillment_order_item_id: str
    amazon_shipment_id: str
    return_reason_code: str
    return_comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_return_item_id = self.seller_return_item_id
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        amazon_shipment_id = self.amazon_shipment_id
        return_reason_code = self.return_reason_code
        return_comment = self.return_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerReturnItemId": seller_return_item_id,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
                "amazonShipmentId": amazon_shipment_id,
                "returnReasonCode": return_reason_code,
            }
        )
        if return_comment is not UNSET:
            field_dict["returnComment"] = return_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_return_item_id = d.pop("sellerReturnItemId")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        amazon_shipment_id = d.pop("amazonShipmentId")

        return_reason_code = d.pop("returnReasonCode")

        return_comment = d.pop("returnComment", UNSET)

        result = cls(
            seller_return_item_id=seller_return_item_id,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            amazon_shipment_id=amazon_shipment_id,
            return_reason_code=return_reason_code,
            return_comment=return_comment,
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
