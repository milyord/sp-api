import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.removal_shipment_item import RemovalShipmentItem


T = TypeVar("T", bound="RemovalShipmentEvent")


@attr.s(auto_attribs=True)
class RemovalShipmentEvent:
    r"""A removal shipment event for a removal order.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        merchant_order_id (Union[Unset, str]): The merchant removal orderId.
        order_id (Union[Unset, str]): The identifier for the removal shipment order.
        transaction_type (Union[Unset, str]): The type of removal order.

            Possible values:

            * WHOLESALE_LIQUIDATION
        removal_shipment_item_list (Union[Unset, List['RemovalShipmentItem']]): A list of information about removal
            shipment items.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    merchant_order_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, str] = UNSET
    removal_shipment_item_list: Union[Unset, List["RemovalShipmentItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        merchant_order_id = self.merchant_order_id
        order_id = self.order_id
        transaction_type = self.transaction_type
        removal_shipment_item_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.removal_shipment_item_list, Unset):
            removal_shipment_item_list = []
            for componentsschemas_removal_shipment_item_list_item_data in self.removal_shipment_item_list:
                componentsschemas_removal_shipment_item_list_item = (
                    componentsschemas_removal_shipment_item_list_item_data.to_dict()
                )

                removal_shipment_item_list.append(componentsschemas_removal_shipment_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if merchant_order_id is not UNSET:
            field_dict["MerchantOrderId"] = merchant_order_id
        if order_id is not UNSET:
            field_dict["OrderId"] = order_id
        if transaction_type is not UNSET:
            field_dict["TransactionType"] = transaction_type
        if removal_shipment_item_list is not UNSET:
            field_dict["RemovalShipmentItemList"] = removal_shipment_item_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.removal_shipment_item import RemovalShipmentItem

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        merchant_order_id = d.pop("MerchantOrderId", UNSET)

        order_id = d.pop("OrderId", UNSET)

        transaction_type = d.pop("TransactionType", UNSET)

        removal_shipment_item_list = []
        _removal_shipment_item_list = d.pop("RemovalShipmentItemList", UNSET)
        for componentsschemas_removal_shipment_item_list_item_data in _removal_shipment_item_list or []:
            componentsschemas_removal_shipment_item_list_item = RemovalShipmentItem.from_dict(
                componentsschemas_removal_shipment_item_list_item_data
            )

            removal_shipment_item_list.append(componentsschemas_removal_shipment_item_list_item)

        result = cls(
            posted_date=posted_date,
            merchant_order_id=merchant_order_id,
            order_id=order_id,
            transaction_type=transaction_type,
            removal_shipment_item_list=removal_shipment_item_list,
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
