from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.shipping_speed_category import ShippingSpeedCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.feature_settings import FeatureSettings
    from ..models.get_fulfillment_preview_item import GetFulfillmentPreviewItem


T = TypeVar("T", bound="GetFulfillmentPreviewRequest")


@attr.s(auto_attribs=True)
class GetFulfillmentPreviewRequest:
    r"""The request body schema for the getFulfillmentPreview operation.

    Attributes:
        address (Address): A physical address.
        items (List['GetFulfillmentPreviewItem']): An array of fulfillment preview item information.
        marketplace_id (Union[Unset, str]): The marketplace the fulfillment order is placed against.
        shipping_speed_categories (Union[Unset, List[ShippingSpeedCategory]]):
        include_cod_fulfillment_preview (Union[Unset, bool]): Specifies whether to return fulfillment order previews
            that are for COD (Cash On Delivery).

            Possible values:

            * true - Returns all fulfillment order previews (both for COD and not for COD).
            * false - Returns only fulfillment order previews that are not for COD.
        include_delivery_windows (Union[Unset, bool]): Specifies whether to return the ScheduledDeliveryInfo response
            object, which contains the available delivery windows for a Scheduled Delivery. The ScheduledDeliveryInfo
            response object can only be returned for fulfillment order previews with ShippingSpeedCategories =
            ScheduledDelivery.
        feature_constraints (Union[Unset, List['FeatureSettings']]): A list of features and their fulfillment policies
            to apply to the order.
    """

    address: "Address"
    items: List["GetFulfillmentPreviewItem"]
    marketplace_id: Union[Unset, str] = UNSET
    shipping_speed_categories: Union[Unset, List[ShippingSpeedCategory]] = UNSET
    include_cod_fulfillment_preview: Union[Unset, bool] = UNSET
    include_delivery_windows: Union[Unset, bool] = UNSET
    feature_constraints: Union[Unset, List["FeatureSettings"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address.to_dict()

        items = []
        for componentsschemas_get_fulfillment_preview_item_list_item_data in self.items:
            componentsschemas_get_fulfillment_preview_item_list_item = (
                componentsschemas_get_fulfillment_preview_item_list_item_data.to_dict()
            )

            items.append(componentsschemas_get_fulfillment_preview_item_list_item)

        marketplace_id = self.marketplace_id
        shipping_speed_categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.shipping_speed_categories, Unset):
            shipping_speed_categories = []
            for componentsschemas_shipping_speed_category_list_item_data in self.shipping_speed_categories:
                componentsschemas_shipping_speed_category_list_item = (
                    componentsschemas_shipping_speed_category_list_item_data.value
                )

                shipping_speed_categories.append(componentsschemas_shipping_speed_category_list_item)

        include_cod_fulfillment_preview = self.include_cod_fulfillment_preview
        include_delivery_windows = self.include_delivery_windows
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
                "address": address,
                "items": items,
            }
        )
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if shipping_speed_categories is not UNSET:
            field_dict["shippingSpeedCategories"] = shipping_speed_categories
        if include_cod_fulfillment_preview is not UNSET:
            field_dict["includeCODFulfillmentPreview"] = include_cod_fulfillment_preview
        if include_delivery_windows is not UNSET:
            field_dict["includeDeliveryWindows"] = include_delivery_windows
        if feature_constraints is not UNSET:
            field_dict["featureConstraints"] = feature_constraints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.feature_settings import FeatureSettings
        from ..models.get_fulfillment_preview_item import GetFulfillmentPreviewItem

        d = src_dict.copy()
        address = Address.from_dict(d.pop("address"))

        items = []
        _items = d.pop("items")
        for componentsschemas_get_fulfillment_preview_item_list_item_data in _items:
            componentsschemas_get_fulfillment_preview_item_list_item = GetFulfillmentPreviewItem.from_dict(
                componentsschemas_get_fulfillment_preview_item_list_item_data
            )

            items.append(componentsschemas_get_fulfillment_preview_item_list_item)

        marketplace_id = d.pop("marketplaceId", UNSET)

        shipping_speed_categories = []
        _shipping_speed_categories = d.pop("shippingSpeedCategories", UNSET)
        for componentsschemas_shipping_speed_category_list_item_data in _shipping_speed_categories or []:
            componentsschemas_shipping_speed_category_list_item = ShippingSpeedCategory(
                componentsschemas_shipping_speed_category_list_item_data
            )

            shipping_speed_categories.append(componentsschemas_shipping_speed_category_list_item)

        include_cod_fulfillment_preview = d.pop("includeCODFulfillmentPreview", UNSET)

        include_delivery_windows = d.pop("includeDeliveryWindows", UNSET)

        feature_constraints = []
        _feature_constraints = d.pop("featureConstraints", UNSET)
        for feature_constraints_item_data in _feature_constraints or []:
            feature_constraints_item = FeatureSettings.from_dict(feature_constraints_item_data)

            feature_constraints.append(feature_constraints_item)

        result = cls(
            address=address,
            items=items,
            marketplace_id=marketplace_id,
            shipping_speed_categories=shipping_speed_categories,
            include_cod_fulfillment_preview=include_cod_fulfillment_preview,
            include_delivery_windows=include_delivery_windows,
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
