from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fulfillment_preview_item_shipping_weight_calculation_method import (
    FulfillmentPreviewItemShippingWeightCalculationMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weight import Weight


T = TypeVar("T", bound="FulfillmentPreviewItem")


@attr.s(auto_attribs=True)
class FulfillmentPreviewItem:
    r"""Item information for a shipment in a fulfillment order preview.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        quantity (int): The item quantity.
        seller_fulfillment_order_item_id (str): A fulfillment order item identifier that the seller created with a call
            to the createFulfillmentOrder operation.
        estimated_shipping_weight (Union[Unset, Weight]): The weight.
        shipping_weight_calculation_method (Union[Unset, FulfillmentPreviewItemShippingWeightCalculationMethod]): The
            method used to calculate the estimated shipping weight.
    """

    seller_sku: str
    quantity: int
    seller_fulfillment_order_item_id: str
    estimated_shipping_weight: Union[Unset, "Weight"] = UNSET
    shipping_weight_calculation_method: Union[Unset, FulfillmentPreviewItemShippingWeightCalculationMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        quantity = self.quantity
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        estimated_shipping_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_shipping_weight, Unset):
            estimated_shipping_weight = self.estimated_shipping_weight.to_dict()

        shipping_weight_calculation_method: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_weight_calculation_method, Unset):
            shipping_weight_calculation_method = self.shipping_weight_calculation_method.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerSku": seller_sku,
                "quantity": quantity,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
            }
        )
        if estimated_shipping_weight is not UNSET:
            field_dict["estimatedShippingWeight"] = estimated_shipping_weight
        if shipping_weight_calculation_method is not UNSET:
            field_dict["shippingWeightCalculationMethod"] = shipping_weight_calculation_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.weight import Weight

        d = src_dict.copy()
        seller_sku = d.pop("sellerSku")

        quantity = d.pop("quantity")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        _estimated_shipping_weight = d.pop("estimatedShippingWeight", UNSET)
        estimated_shipping_weight: Union[Unset, Weight]
        if isinstance(_estimated_shipping_weight, Unset):
            estimated_shipping_weight = UNSET
        else:
            estimated_shipping_weight = Weight.from_dict(_estimated_shipping_weight)

        _shipping_weight_calculation_method = d.pop("shippingWeightCalculationMethod", UNSET)
        shipping_weight_calculation_method: Union[Unset, FulfillmentPreviewItemShippingWeightCalculationMethod]
        if isinstance(_shipping_weight_calculation_method, Unset):
            shipping_weight_calculation_method = UNSET
        else:
            shipping_weight_calculation_method = FulfillmentPreviewItemShippingWeightCalculationMethod(
                _shipping_weight_calculation_method
            )

        result = cls(
            seller_sku=seller_sku,
            quantity=quantity,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            estimated_shipping_weight=estimated_shipping_weight,
            shipping_weight_calculation_method=shipping_weight_calculation_method,
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
