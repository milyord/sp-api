from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money
    from ..models.order_item_status_acknowledgement_status import OrderItemStatusAcknowledgementStatus
    from ..models.order_item_status_ordered_quantity import OrderItemStatusOrderedQuantity
    from ..models.order_item_status_receiving_status import OrderItemStatusReceivingStatus


T = TypeVar("T", bound="OrderItemStatus")


@attr.s(auto_attribs=True)
class OrderItemStatus:
    r"""
    Attributes:
        item_sequence_number (str): Numbering of the item on the purchase order. The first item will be 1, the second 2,
            and so on.
        buyer_product_identifier (Union[Unset, str]): Buyer's Standard Identification Number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item.
        net_cost (Union[Unset, Money]): An amount of money, including units in the form of currency.
        list_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
        ordered_quantity (Union[Unset, OrderItemStatusOrderedQuantity]): Ordered quantity information.
        acknowledgement_status (Union[Unset, OrderItemStatusAcknowledgementStatus]): Acknowledgement status information.
        receiving_status (Union[Unset, OrderItemStatusReceivingStatus]): Item receive status at the buyer's warehouse.
    """

    item_sequence_number: str
    buyer_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    net_cost: Union[Unset, "Money"] = UNSET
    list_price: Union[Unset, "Money"] = UNSET
    ordered_quantity: Union[Unset, "OrderItemStatusOrderedQuantity"] = UNSET
    acknowledgement_status: Union[Unset, "OrderItemStatusAcknowledgementStatus"] = UNSET
    receiving_status: Union[Unset, "OrderItemStatusReceivingStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        buyer_product_identifier = self.buyer_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        net_cost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.net_cost, Unset):
            net_cost = self.net_cost.to_dict()

        list_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.list_price, Unset):
            list_price = self.list_price.to_dict()

        ordered_quantity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ordered_quantity, Unset):
            ordered_quantity = self.ordered_quantity.to_dict()

        acknowledgement_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.acknowledgement_status, Unset):
            acknowledgement_status = self.acknowledgement_status.to_dict()

        receiving_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.receiving_status, Unset):
            receiving_status = self.receiving_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
            }
        )
        if buyer_product_identifier is not UNSET:
            field_dict["buyerProductIdentifier"] = buyer_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if net_cost is not UNSET:
            field_dict["netCost"] = net_cost
        if list_price is not UNSET:
            field_dict["listPrice"] = list_price
        if ordered_quantity is not UNSET:
            field_dict["orderedQuantity"] = ordered_quantity
        if acknowledgement_status is not UNSET:
            field_dict["acknowledgementStatus"] = acknowledgement_status
        if receiving_status is not UNSET:
            field_dict["receivingStatus"] = receiving_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money
        from ..models.order_item_status_acknowledgement_status import OrderItemStatusAcknowledgementStatus
        from ..models.order_item_status_ordered_quantity import OrderItemStatusOrderedQuantity
        from ..models.order_item_status_receiving_status import OrderItemStatusReceivingStatus

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        buyer_product_identifier = d.pop("buyerProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        _net_cost = d.pop("netCost", UNSET)
        net_cost: Union[Unset, Money]
        if isinstance(_net_cost, Unset):
            net_cost = UNSET
        else:
            net_cost = Money.from_dict(_net_cost)

        _list_price = d.pop("listPrice", UNSET)
        list_price: Union[Unset, Money]
        if isinstance(_list_price, Unset):
            list_price = UNSET
        else:
            list_price = Money.from_dict(_list_price)

        _ordered_quantity = d.pop("orderedQuantity", UNSET)
        ordered_quantity: Union[Unset, OrderItemStatusOrderedQuantity]
        if isinstance(_ordered_quantity, Unset):
            ordered_quantity = UNSET
        else:
            ordered_quantity = OrderItemStatusOrderedQuantity.from_dict(_ordered_quantity)

        _acknowledgement_status = d.pop("acknowledgementStatus", UNSET)
        acknowledgement_status: Union[Unset, OrderItemStatusAcknowledgementStatus]
        if isinstance(_acknowledgement_status, Unset):
            acknowledgement_status = UNSET
        else:
            acknowledgement_status = OrderItemStatusAcknowledgementStatus.from_dict(_acknowledgement_status)

        _receiving_status = d.pop("receivingStatus", UNSET)
        receiving_status: Union[Unset, OrderItemStatusReceivingStatus]
        if isinstance(_receiving_status, Unset):
            receiving_status = UNSET
        else:
            receiving_status = OrderItemStatusReceivingStatus.from_dict(_receiving_status)

        result = cls(
            item_sequence_number=item_sequence_number,
            buyer_product_identifier=buyer_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            net_cost=net_cost,
            list_price=list_price,
            ordered_quantity=ordered_quantity,
            acknowledgement_status=acknowledgement_status,
            receiving_status=receiving_status,
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
