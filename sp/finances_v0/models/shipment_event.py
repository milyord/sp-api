import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent
    from ..models.direct_payment import DirectPayment
    from ..models.fee_component import FeeComponent
    from ..models.shipment_item import ShipmentItem


T = TypeVar("T", bound="ShipmentEvent")


@attr.s(auto_attribs=True)
class ShipmentEvent:
    r"""A shipment, refund, guarantee claim, or chargeback.

    Attributes:
        amazon_order_id (Union[Unset, str]): An Amazon-defined identifier for an order.
        seller_order_id (Union[Unset, str]): A seller-defined identifier for an order.
        marketplace_name (Union[Unset, str]): The name of the marketplace where the event occurred.
        order_charge_list (Union[Unset, List['ChargeComponent']]): A list of charge information on the seller's account.
        order_charge_adjustment_list (Union[Unset, List['ChargeComponent']]): A list of charge information on the
            seller's account.
        shipment_fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        shipment_fee_adjustment_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        order_fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        order_fee_adjustment_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        direct_payment_list (Union[Unset, List['DirectPayment']]): A list of direct payment information.
        posted_date (Union[Unset, datetime.datetime]):
        shipment_item_list (Union[Unset, List['ShipmentItem']]): A list of shipment items.
        shipment_item_adjustment_list (Union[Unset, List['ShipmentItem']]): A list of shipment items.
    """

    amazon_order_id: Union[Unset, str] = UNSET
    seller_order_id: Union[Unset, str] = UNSET
    marketplace_name: Union[Unset, str] = UNSET
    order_charge_list: Union[Unset, List["ChargeComponent"]] = UNSET
    order_charge_adjustment_list: Union[Unset, List["ChargeComponent"]] = UNSET
    shipment_fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    shipment_fee_adjustment_list: Union[Unset, List["FeeComponent"]] = UNSET
    order_fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    order_fee_adjustment_list: Union[Unset, List["FeeComponent"]] = UNSET
    direct_payment_list: Union[Unset, List["DirectPayment"]] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    shipment_item_list: Union[Unset, List["ShipmentItem"]] = UNSET
    shipment_item_adjustment_list: Union[Unset, List["ShipmentItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        seller_order_id = self.seller_order_id
        marketplace_name = self.marketplace_name
        order_charge_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_charge_list, Unset):
            order_charge_list = []
            for componentsschemas_charge_component_list_item_data in self.order_charge_list:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                order_charge_list.append(componentsschemas_charge_component_list_item)

        order_charge_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_charge_adjustment_list, Unset):
            order_charge_adjustment_list = []
            for componentsschemas_charge_component_list_item_data in self.order_charge_adjustment_list:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                order_charge_adjustment_list.append(componentsschemas_charge_component_list_item)

        shipment_fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_fee_list, Unset):
            shipment_fee_list = []
            for componentsschemas_fee_component_list_item_data in self.shipment_fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                shipment_fee_list.append(componentsschemas_fee_component_list_item)

        shipment_fee_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_fee_adjustment_list, Unset):
            shipment_fee_adjustment_list = []
            for componentsschemas_fee_component_list_item_data in self.shipment_fee_adjustment_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                shipment_fee_adjustment_list.append(componentsschemas_fee_component_list_item)

        order_fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_fee_list, Unset):
            order_fee_list = []
            for componentsschemas_fee_component_list_item_data in self.order_fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                order_fee_list.append(componentsschemas_fee_component_list_item)

        order_fee_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_fee_adjustment_list, Unset):
            order_fee_adjustment_list = []
            for componentsschemas_fee_component_list_item_data in self.order_fee_adjustment_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                order_fee_adjustment_list.append(componentsschemas_fee_component_list_item)

        direct_payment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.direct_payment_list, Unset):
            direct_payment_list = []
            for componentsschemas_direct_payment_list_item_data in self.direct_payment_list:
                componentsschemas_direct_payment_list_item = componentsschemas_direct_payment_list_item_data.to_dict()

                direct_payment_list.append(componentsschemas_direct_payment_list_item)

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        shipment_item_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_item_list, Unset):
            shipment_item_list = []
            for componentsschemas_shipment_item_list_item_data in self.shipment_item_list:
                componentsschemas_shipment_item_list_item = componentsschemas_shipment_item_list_item_data.to_dict()

                shipment_item_list.append(componentsschemas_shipment_item_list_item)

        shipment_item_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_item_adjustment_list, Unset):
            shipment_item_adjustment_list = []
            for componentsschemas_shipment_item_list_item_data in self.shipment_item_adjustment_list:
                componentsschemas_shipment_item_list_item = componentsschemas_shipment_item_list_item_data.to_dict()

                shipment_item_adjustment_list.append(componentsschemas_shipment_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_order_id is not UNSET:
            field_dict["AmazonOrderId"] = amazon_order_id
        if seller_order_id is not UNSET:
            field_dict["SellerOrderId"] = seller_order_id
        if marketplace_name is not UNSET:
            field_dict["MarketplaceName"] = marketplace_name
        if order_charge_list is not UNSET:
            field_dict["OrderChargeList"] = order_charge_list
        if order_charge_adjustment_list is not UNSET:
            field_dict["OrderChargeAdjustmentList"] = order_charge_adjustment_list
        if shipment_fee_list is not UNSET:
            field_dict["ShipmentFeeList"] = shipment_fee_list
        if shipment_fee_adjustment_list is not UNSET:
            field_dict["ShipmentFeeAdjustmentList"] = shipment_fee_adjustment_list
        if order_fee_list is not UNSET:
            field_dict["OrderFeeList"] = order_fee_list
        if order_fee_adjustment_list is not UNSET:
            field_dict["OrderFeeAdjustmentList"] = order_fee_adjustment_list
        if direct_payment_list is not UNSET:
            field_dict["DirectPaymentList"] = direct_payment_list
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if shipment_item_list is not UNSET:
            field_dict["ShipmentItemList"] = shipment_item_list
        if shipment_item_adjustment_list is not UNSET:
            field_dict["ShipmentItemAdjustmentList"] = shipment_item_adjustment_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent
        from ..models.direct_payment import DirectPayment
        from ..models.fee_component import FeeComponent
        from ..models.shipment_item import ShipmentItem

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId", UNSET)

        seller_order_id = d.pop("SellerOrderId", UNSET)

        marketplace_name = d.pop("MarketplaceName", UNSET)

        order_charge_list = []
        _order_charge_list = d.pop("OrderChargeList", UNSET)
        for componentsschemas_charge_component_list_item_data in _order_charge_list or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            order_charge_list.append(componentsschemas_charge_component_list_item)

        order_charge_adjustment_list = []
        _order_charge_adjustment_list = d.pop("OrderChargeAdjustmentList", UNSET)
        for componentsschemas_charge_component_list_item_data in _order_charge_adjustment_list or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            order_charge_adjustment_list.append(componentsschemas_charge_component_list_item)

        shipment_fee_list = []
        _shipment_fee_list = d.pop("ShipmentFeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _shipment_fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            shipment_fee_list.append(componentsschemas_fee_component_list_item)

        shipment_fee_adjustment_list = []
        _shipment_fee_adjustment_list = d.pop("ShipmentFeeAdjustmentList", UNSET)
        for componentsschemas_fee_component_list_item_data in _shipment_fee_adjustment_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            shipment_fee_adjustment_list.append(componentsschemas_fee_component_list_item)

        order_fee_list = []
        _order_fee_list = d.pop("OrderFeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _order_fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            order_fee_list.append(componentsschemas_fee_component_list_item)

        order_fee_adjustment_list = []
        _order_fee_adjustment_list = d.pop("OrderFeeAdjustmentList", UNSET)
        for componentsschemas_fee_component_list_item_data in _order_fee_adjustment_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            order_fee_adjustment_list.append(componentsschemas_fee_component_list_item)

        direct_payment_list = []
        _direct_payment_list = d.pop("DirectPaymentList", UNSET)
        for componentsschemas_direct_payment_list_item_data in _direct_payment_list or []:
            componentsschemas_direct_payment_list_item = DirectPayment.from_dict(
                componentsschemas_direct_payment_list_item_data
            )

            direct_payment_list.append(componentsschemas_direct_payment_list_item)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        shipment_item_list = []
        _shipment_item_list = d.pop("ShipmentItemList", UNSET)
        for componentsschemas_shipment_item_list_item_data in _shipment_item_list or []:
            componentsschemas_shipment_item_list_item = ShipmentItem.from_dict(
                componentsschemas_shipment_item_list_item_data
            )

            shipment_item_list.append(componentsschemas_shipment_item_list_item)

        shipment_item_adjustment_list = []
        _shipment_item_adjustment_list = d.pop("ShipmentItemAdjustmentList", UNSET)
        for componentsschemas_shipment_item_list_item_data in _shipment_item_adjustment_list or []:
            componentsschemas_shipment_item_list_item = ShipmentItem.from_dict(
                componentsschemas_shipment_item_list_item_data
            )

            shipment_item_adjustment_list.append(componentsschemas_shipment_item_list_item)

        result = cls(
            amazon_order_id=amazon_order_id,
            seller_order_id=seller_order_id,
            marketplace_name=marketplace_name,
            order_charge_list=order_charge_list,
            order_charge_adjustment_list=order_charge_adjustment_list,
            shipment_fee_list=shipment_fee_list,
            shipment_fee_adjustment_list=shipment_fee_adjustment_list,
            order_fee_list=order_fee_list,
            order_fee_adjustment_list=order_fee_adjustment_list,
            direct_payment_list=direct_payment_list,
            posted_date=posted_date,
            shipment_item_list=shipment_item_list,
            shipment_item_adjustment_list=shipment_item_adjustment_list,
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
