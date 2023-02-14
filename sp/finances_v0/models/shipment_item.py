from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent
    from ..models.currency import Currency
    from ..models.fee_component import FeeComponent
    from ..models.promotion import Promotion
    from ..models.tax_withheld_component import TaxWithheldComponent


T = TypeVar("T", bound="ShipmentItem")


@attr.s(auto_attribs=True)
class ShipmentItem:
    r"""An item of a shipment, refund, guarantee claim, or chargeback.

    Attributes:
        seller_sku (Union[Unset, str]): The seller SKU of the item. The seller SKU is qualified by the seller's seller
            ID, which is included with every call to the Selling Partner API.
        order_item_id (Union[Unset, str]): An Amazon-defined order item identifier.
        order_adjustment_item_id (Union[Unset, str]): An Amazon-defined order adjustment identifier defined for refunds,
            guarantee claims, and chargeback events.
        quantity_shipped (Union[Unset, int]): The number of items shipped.
        item_charge_list (Union[Unset, List['ChargeComponent']]): A list of charge information on the seller's account.
        item_charge_adjustment_list (Union[Unset, List['ChargeComponent']]): A list of charge information on the
            seller's account.
        item_fee_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        item_fee_adjustment_list (Union[Unset, List['FeeComponent']]): A list of fee component information.
        item_tax_withheld_list (Union[Unset, List['TaxWithheldComponent']]): A list of information about taxes withheld.
        promotion_list (Union[Unset, List['Promotion']]): A list of promotions.
        promotion_adjustment_list (Union[Unset, List['Promotion']]): A list of promotions.
        cost_of_points_granted (Union[Unset, Currency]): A currency type and amount.
        cost_of_points_returned (Union[Unset, Currency]): A currency type and amount.
    """

    seller_sku: Union[Unset, str] = UNSET
    order_item_id: Union[Unset, str] = UNSET
    order_adjustment_item_id: Union[Unset, str] = UNSET
    quantity_shipped: Union[Unset, int] = UNSET
    item_charge_list: Union[Unset, List["ChargeComponent"]] = UNSET
    item_charge_adjustment_list: Union[Unset, List["ChargeComponent"]] = UNSET
    item_fee_list: Union[Unset, List["FeeComponent"]] = UNSET
    item_fee_adjustment_list: Union[Unset, List["FeeComponent"]] = UNSET
    item_tax_withheld_list: Union[Unset, List["TaxWithheldComponent"]] = UNSET
    promotion_list: Union[Unset, List["Promotion"]] = UNSET
    promotion_adjustment_list: Union[Unset, List["Promotion"]] = UNSET
    cost_of_points_granted: Union[Unset, "Currency"] = UNSET
    cost_of_points_returned: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        order_item_id = self.order_item_id
        order_adjustment_item_id = self.order_adjustment_item_id
        quantity_shipped = self.quantity_shipped
        item_charge_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_charge_list, Unset):
            item_charge_list = []
            for componentsschemas_charge_component_list_item_data in self.item_charge_list:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                item_charge_list.append(componentsschemas_charge_component_list_item)

        item_charge_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_charge_adjustment_list, Unset):
            item_charge_adjustment_list = []
            for componentsschemas_charge_component_list_item_data in self.item_charge_adjustment_list:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                item_charge_adjustment_list.append(componentsschemas_charge_component_list_item)

        item_fee_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_fee_list, Unset):
            item_fee_list = []
            for componentsschemas_fee_component_list_item_data in self.item_fee_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                item_fee_list.append(componentsschemas_fee_component_list_item)

        item_fee_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_fee_adjustment_list, Unset):
            item_fee_adjustment_list = []
            for componentsschemas_fee_component_list_item_data in self.item_fee_adjustment_list:
                componentsschemas_fee_component_list_item = componentsschemas_fee_component_list_item_data.to_dict()

                item_fee_adjustment_list.append(componentsschemas_fee_component_list_item)

        item_tax_withheld_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_tax_withheld_list, Unset):
            item_tax_withheld_list = []
            for componentsschemas_tax_withheld_component_list_item_data in self.item_tax_withheld_list:
                componentsschemas_tax_withheld_component_list_item = (
                    componentsschemas_tax_withheld_component_list_item_data.to_dict()
                )

                item_tax_withheld_list.append(componentsschemas_tax_withheld_component_list_item)

        promotion_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.promotion_list, Unset):
            promotion_list = []
            for componentsschemas_promotion_list_item_data in self.promotion_list:
                componentsschemas_promotion_list_item = componentsschemas_promotion_list_item_data.to_dict()

                promotion_list.append(componentsschemas_promotion_list_item)

        promotion_adjustment_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.promotion_adjustment_list, Unset):
            promotion_adjustment_list = []
            for componentsschemas_promotion_list_item_data in self.promotion_adjustment_list:
                componentsschemas_promotion_list_item = componentsschemas_promotion_list_item_data.to_dict()

                promotion_adjustment_list.append(componentsschemas_promotion_list_item)

        cost_of_points_granted: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_of_points_granted, Unset):
            cost_of_points_granted = self.cost_of_points_granted.to_dict()

        cost_of_points_returned: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_of_points_returned, Unset):
            cost_of_points_returned = self.cost_of_points_returned.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seller_sku is not UNSET:
            field_dict["SellerSKU"] = seller_sku
        if order_item_id is not UNSET:
            field_dict["OrderItemId"] = order_item_id
        if order_adjustment_item_id is not UNSET:
            field_dict["OrderAdjustmentItemId"] = order_adjustment_item_id
        if quantity_shipped is not UNSET:
            field_dict["QuantityShipped"] = quantity_shipped
        if item_charge_list is not UNSET:
            field_dict["ItemChargeList"] = item_charge_list
        if item_charge_adjustment_list is not UNSET:
            field_dict["ItemChargeAdjustmentList"] = item_charge_adjustment_list
        if item_fee_list is not UNSET:
            field_dict["ItemFeeList"] = item_fee_list
        if item_fee_adjustment_list is not UNSET:
            field_dict["ItemFeeAdjustmentList"] = item_fee_adjustment_list
        if item_tax_withheld_list is not UNSET:
            field_dict["ItemTaxWithheldList"] = item_tax_withheld_list
        if promotion_list is not UNSET:
            field_dict["PromotionList"] = promotion_list
        if promotion_adjustment_list is not UNSET:
            field_dict["PromotionAdjustmentList"] = promotion_adjustment_list
        if cost_of_points_granted is not UNSET:
            field_dict["CostOfPointsGranted"] = cost_of_points_granted
        if cost_of_points_returned is not UNSET:
            field_dict["CostOfPointsReturned"] = cost_of_points_returned

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent
        from ..models.currency import Currency
        from ..models.fee_component import FeeComponent
        from ..models.promotion import Promotion
        from ..models.tax_withheld_component import TaxWithheldComponent

        d = src_dict.copy()
        seller_sku = d.pop("SellerSKU", UNSET)

        order_item_id = d.pop("OrderItemId", UNSET)

        order_adjustment_item_id = d.pop("OrderAdjustmentItemId", UNSET)

        quantity_shipped = d.pop("QuantityShipped", UNSET)

        item_charge_list = []
        _item_charge_list = d.pop("ItemChargeList", UNSET)
        for componentsschemas_charge_component_list_item_data in _item_charge_list or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            item_charge_list.append(componentsschemas_charge_component_list_item)

        item_charge_adjustment_list = []
        _item_charge_adjustment_list = d.pop("ItemChargeAdjustmentList", UNSET)
        for componentsschemas_charge_component_list_item_data in _item_charge_adjustment_list or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            item_charge_adjustment_list.append(componentsschemas_charge_component_list_item)

        item_fee_list = []
        _item_fee_list = d.pop("ItemFeeList", UNSET)
        for componentsschemas_fee_component_list_item_data in _item_fee_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            item_fee_list.append(componentsschemas_fee_component_list_item)

        item_fee_adjustment_list = []
        _item_fee_adjustment_list = d.pop("ItemFeeAdjustmentList", UNSET)
        for componentsschemas_fee_component_list_item_data in _item_fee_adjustment_list or []:
            componentsschemas_fee_component_list_item = FeeComponent.from_dict(
                componentsschemas_fee_component_list_item_data
            )

            item_fee_adjustment_list.append(componentsschemas_fee_component_list_item)

        item_tax_withheld_list = []
        _item_tax_withheld_list = d.pop("ItemTaxWithheldList", UNSET)
        for componentsschemas_tax_withheld_component_list_item_data in _item_tax_withheld_list or []:
            componentsschemas_tax_withheld_component_list_item = TaxWithheldComponent.from_dict(
                componentsschemas_tax_withheld_component_list_item_data
            )

            item_tax_withheld_list.append(componentsschemas_tax_withheld_component_list_item)

        promotion_list = []
        _promotion_list = d.pop("PromotionList", UNSET)
        for componentsschemas_promotion_list_item_data in _promotion_list or []:
            componentsschemas_promotion_list_item = Promotion.from_dict(componentsschemas_promotion_list_item_data)

            promotion_list.append(componentsschemas_promotion_list_item)

        promotion_adjustment_list = []
        _promotion_adjustment_list = d.pop("PromotionAdjustmentList", UNSET)
        for componentsschemas_promotion_list_item_data in _promotion_adjustment_list or []:
            componentsschemas_promotion_list_item = Promotion.from_dict(componentsschemas_promotion_list_item_data)

            promotion_adjustment_list.append(componentsschemas_promotion_list_item)

        _cost_of_points_granted = d.pop("CostOfPointsGranted", UNSET)
        cost_of_points_granted: Union[Unset, Currency]
        if isinstance(_cost_of_points_granted, Unset):
            cost_of_points_granted = UNSET
        else:
            cost_of_points_granted = Currency.from_dict(_cost_of_points_granted)

        _cost_of_points_returned = d.pop("CostOfPointsReturned", UNSET)
        cost_of_points_returned: Union[Unset, Currency]
        if isinstance(_cost_of_points_returned, Unset):
            cost_of_points_returned = UNSET
        else:
            cost_of_points_returned = Currency.from_dict(_cost_of_points_returned)

        result = cls(
            seller_sku=seller_sku,
            order_item_id=order_item_id,
            order_adjustment_item_id=order_adjustment_item_id,
            quantity_shipped=quantity_shipped,
            item_charge_list=item_charge_list,
            item_charge_adjustment_list=item_charge_adjustment_list,
            item_fee_list=item_fee_list,
            item_fee_adjustment_list=item_fee_adjustment_list,
            item_tax_withheld_list=item_tax_withheld_list,
            promotion_list=promotion_list,
            promotion_adjustment_list=promotion_adjustment_list,
            cost_of_points_granted=cost_of_points_granted,
            cost_of_points_returned=cost_of_points_returned,
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
