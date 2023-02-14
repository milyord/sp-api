from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.shipping_speed_category import ShippingSpeedCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_settings import FeatureSettings
    from ..models.fee import Fee
    from ..models.fulfillment_preview_shipment import FulfillmentPreviewShipment
    from ..models.scheduled_delivery_info import ScheduledDeliveryInfo
    from ..models.unfulfillable_preview_item import UnfulfillablePreviewItem
    from ..models.weight import Weight


T = TypeVar("T", bound="FulfillmentPreview")


@attr.s(auto_attribs=True)
class FulfillmentPreview:
    r"""Information about a fulfillment order preview, including delivery and fee information based on shipping method.

    Attributes:
        shipping_speed_category (ShippingSpeedCategory): The shipping method used for the fulfillment order.
        is_fulfillable (bool): When true, this fulfillment order preview is fulfillable.
        is_cod_capable (bool): When true, this fulfillment order preview is for COD (Cash On Delivery).
        marketplace_id (str): The marketplace the fulfillment order is placed against.
        scheduled_delivery_info (Union[Unset, ScheduledDeliveryInfo]): Delivery information for a scheduled delivery.
        estimated_shipping_weight (Union[Unset, Weight]): The weight.
        estimated_fees (Union[Unset, List['Fee']]): An array of fee type and cost pairs.
        fulfillment_preview_shipments (Union[Unset, List['FulfillmentPreviewShipment']]): An array of fulfillment
            preview shipment information.
        unfulfillable_preview_items (Union[Unset, List['UnfulfillablePreviewItem']]): An array of unfulfillable preview
            item information.
        order_unfulfillable_reasons (Union[Unset, List[str]]):
        feature_constraints (Union[Unset, List['FeatureSettings']]): A list of features and their fulfillment policies
            to apply to the order.
    """

    shipping_speed_category: ShippingSpeedCategory
    is_fulfillable: bool
    is_cod_capable: bool
    marketplace_id: str
    scheduled_delivery_info: Union[Unset, "ScheduledDeliveryInfo"] = UNSET
    estimated_shipping_weight: Union[Unset, "Weight"] = UNSET
    estimated_fees: Union[Unset, List["Fee"]] = UNSET
    fulfillment_preview_shipments: Union[Unset, List["FulfillmentPreviewShipment"]] = UNSET
    unfulfillable_preview_items: Union[Unset, List["UnfulfillablePreviewItem"]] = UNSET
    order_unfulfillable_reasons: Union[Unset, List[str]] = UNSET
    feature_constraints: Union[Unset, List["FeatureSettings"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_speed_category = self.shipping_speed_category.value

        is_fulfillable = self.is_fulfillable
        is_cod_capable = self.is_cod_capable
        marketplace_id = self.marketplace_id
        scheduled_delivery_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scheduled_delivery_info, Unset):
            scheduled_delivery_info = self.scheduled_delivery_info.to_dict()

        estimated_shipping_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_shipping_weight, Unset):
            estimated_shipping_weight = self.estimated_shipping_weight.to_dict()

        estimated_fees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.estimated_fees, Unset):
            estimated_fees = []
            for componentsschemas_fee_list_item_data in self.estimated_fees:
                componentsschemas_fee_list_item = componentsschemas_fee_list_item_data.to_dict()

                estimated_fees.append(componentsschemas_fee_list_item)

        fulfillment_preview_shipments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_preview_shipments, Unset):
            fulfillment_preview_shipments = []
            for componentsschemas_fulfillment_preview_shipment_list_item_data in self.fulfillment_preview_shipments:
                componentsschemas_fulfillment_preview_shipment_list_item = (
                    componentsschemas_fulfillment_preview_shipment_list_item_data.to_dict()
                )

                fulfillment_preview_shipments.append(componentsschemas_fulfillment_preview_shipment_list_item)

        unfulfillable_preview_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unfulfillable_preview_items, Unset):
            unfulfillable_preview_items = []
            for componentsschemas_unfulfillable_preview_item_list_item_data in self.unfulfillable_preview_items:
                componentsschemas_unfulfillable_preview_item_list_item = (
                    componentsschemas_unfulfillable_preview_item_list_item_data.to_dict()
                )

                unfulfillable_preview_items.append(componentsschemas_unfulfillable_preview_item_list_item)

        order_unfulfillable_reasons: Union[Unset, List[str]] = UNSET
        if not isinstance(self.order_unfulfillable_reasons, Unset):
            order_unfulfillable_reasons = self.order_unfulfillable_reasons

        feature_constraints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.feature_constraints, Unset):
            feature_constraints = []
            for feature_constraints_item_data in self.feature_constraints:
                feature_constraints_item = feature_constraints_item_data.to_dict()

                feature_constraints.append(feature_constraints_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shippingSpeedCategory": shipping_speed_category,
                "isFulfillable": is_fulfillable,
                "isCODCapable": is_cod_capable,
                "marketplaceId": marketplace_id,
            }
        )
        if scheduled_delivery_info is not UNSET:
            field_dict["scheduledDeliveryInfo"] = scheduled_delivery_info
        if estimated_shipping_weight is not UNSET:
            field_dict["estimatedShippingWeight"] = estimated_shipping_weight
        if estimated_fees is not UNSET:
            field_dict["estimatedFees"] = estimated_fees
        if fulfillment_preview_shipments is not UNSET:
            field_dict["fulfillmentPreviewShipments"] = fulfillment_preview_shipments
        if unfulfillable_preview_items is not UNSET:
            field_dict["unfulfillablePreviewItems"] = unfulfillable_preview_items
        if order_unfulfillable_reasons is not UNSET:
            field_dict["orderUnfulfillableReasons"] = order_unfulfillable_reasons
        if feature_constraints is not UNSET:
            field_dict["featureConstraints"] = feature_constraints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature_settings import FeatureSettings
        from ..models.fee import Fee
        from ..models.fulfillment_preview_shipment import FulfillmentPreviewShipment
        from ..models.scheduled_delivery_info import ScheduledDeliveryInfo
        from ..models.unfulfillable_preview_item import UnfulfillablePreviewItem
        from ..models.weight import Weight

        d = src_dict.copy()
        shipping_speed_category = ShippingSpeedCategory(d.pop("shippingSpeedCategory"))

        is_fulfillable = d.pop("isFulfillable")

        is_cod_capable = d.pop("isCODCapable")

        marketplace_id = d.pop("marketplaceId")

        _scheduled_delivery_info = d.pop("scheduledDeliveryInfo", UNSET)
        scheduled_delivery_info: Union[Unset, ScheduledDeliveryInfo]
        if isinstance(_scheduled_delivery_info, Unset):
            scheduled_delivery_info = UNSET
        else:
            scheduled_delivery_info = ScheduledDeliveryInfo.from_dict(_scheduled_delivery_info)

        _estimated_shipping_weight = d.pop("estimatedShippingWeight", UNSET)
        estimated_shipping_weight: Union[Unset, Weight]
        if isinstance(_estimated_shipping_weight, Unset):
            estimated_shipping_weight = UNSET
        else:
            estimated_shipping_weight = Weight.from_dict(_estimated_shipping_weight)

        estimated_fees = []
        _estimated_fees = d.pop("estimatedFees", UNSET)
        for componentsschemas_fee_list_item_data in _estimated_fees or []:
            componentsschemas_fee_list_item = Fee.from_dict(componentsschemas_fee_list_item_data)

            estimated_fees.append(componentsschemas_fee_list_item)

        fulfillment_preview_shipments = []
        _fulfillment_preview_shipments = d.pop("fulfillmentPreviewShipments", UNSET)
        for componentsschemas_fulfillment_preview_shipment_list_item_data in _fulfillment_preview_shipments or []:
            componentsschemas_fulfillment_preview_shipment_list_item = FulfillmentPreviewShipment.from_dict(
                componentsschemas_fulfillment_preview_shipment_list_item_data
            )

            fulfillment_preview_shipments.append(componentsschemas_fulfillment_preview_shipment_list_item)

        unfulfillable_preview_items = []
        _unfulfillable_preview_items = d.pop("unfulfillablePreviewItems", UNSET)
        for componentsschemas_unfulfillable_preview_item_list_item_data in _unfulfillable_preview_items or []:
            componentsschemas_unfulfillable_preview_item_list_item = UnfulfillablePreviewItem.from_dict(
                componentsschemas_unfulfillable_preview_item_list_item_data
            )

            unfulfillable_preview_items.append(componentsschemas_unfulfillable_preview_item_list_item)

        order_unfulfillable_reasons = cast(List[str], d.pop("orderUnfulfillableReasons", UNSET))

        feature_constraints = []
        _feature_constraints = d.pop("featureConstraints", UNSET)
        for feature_constraints_item_data in _feature_constraints or []:
            feature_constraints_item = FeatureSettings.from_dict(feature_constraints_item_data)

            feature_constraints.append(feature_constraints_item)

        result = cls(
            shipping_speed_category=shipping_speed_category,
            is_fulfillable=is_fulfillable,
            is_cod_capable=is_cod_capable,
            marketplace_id=marketplace_id,
            scheduled_delivery_info=scheduled_delivery_info,
            estimated_shipping_weight=estimated_shipping_weight,
            estimated_fees=estimated_fees,
            fulfillment_preview_shipments=fulfillment_preview_shipments,
            unfulfillable_preview_items=unfulfillable_preview_items,
            order_unfulfillable_reasons=order_unfulfillable_reasons,
            feature_constraints=feature_constraints,
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
