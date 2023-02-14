import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.fulfillment_action import FulfillmentAction
from ..models.fulfillment_policy import FulfillmentPolicy
from ..models.shipping_speed_category import ShippingSpeedCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.feature_settings import FeatureSettings
    from ..models.update_fulfillment_order_item import UpdateFulfillmentOrderItem


T = TypeVar("T", bound="UpdateFulfillmentOrderRequest")


@attr.s(auto_attribs=True)
class UpdateFulfillmentOrderRequest:
    r"""
    Attributes:
        marketplace_id (Union[Unset, str]): The marketplace the fulfillment order is placed against.
        displayable_order_id (Union[Unset, str]): A fulfillment order identifier that the seller creates. This value
            displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The
            value of DisplayableOrderId should match the order identifier that the seller provides to the recipient. The
            seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want
            the recipient to reference an alternate order identifier.
        displayable_order_date (Union[Unset, datetime.datetime]):
        displayable_order_comment (Union[Unset, str]): Order-specific text that appears in recipient-facing materials
            such as the outbound shipment packing slip.
        shipping_speed_category (Union[Unset, ShippingSpeedCategory]): The shipping method used for the fulfillment
            order.
        destination_address (Union[Unset, Address]): A physical address.
        fulfillment_action (Union[Unset, FulfillmentAction]): Specifies whether the fulfillment order should ship now or
            have an order hold put on it.
        fulfillment_policy (Union[Unset, FulfillmentPolicy]): The FulfillmentPolicy value specified when you submitted
            the createFulfillmentOrder operation.
        ship_from_country_code (Union[Unset, str]): The two-character country code for the country from which the
            fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
        notification_emails (Union[Unset, List[str]]): A list of email addresses that the seller provides that are used
            by Amazon to send ship-complete notifications to recipients on behalf of the seller.
        feature_constraints (Union[Unset, List['FeatureSettings']]): A list of features and their fulfillment policies
            to apply to the order.
        items (Union[Unset, List['UpdateFulfillmentOrderItem']]): An array of fulfillment order item information for
            updating a fulfillment order.
    """

    marketplace_id: Union[Unset, str] = UNSET
    displayable_order_id: Union[Unset, str] = UNSET
    displayable_order_date: Union[Unset, datetime.datetime] = UNSET
    displayable_order_comment: Union[Unset, str] = UNSET
    shipping_speed_category: Union[Unset, ShippingSpeedCategory] = UNSET
    destination_address: Union[Unset, "Address"] = UNSET
    fulfillment_action: Union[Unset, FulfillmentAction] = UNSET
    fulfillment_policy: Union[Unset, FulfillmentPolicy] = UNSET
    ship_from_country_code: Union[Unset, str] = UNSET
    notification_emails: Union[Unset, List[str]] = UNSET
    feature_constraints: Union[Unset, List["FeatureSettings"]] = UNSET
    items: Union[Unset, List["UpdateFulfillmentOrderItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        displayable_order_id = self.displayable_order_id
        displayable_order_date: Union[Unset, str] = UNSET
        if not isinstance(self.displayable_order_date, Unset):
            displayable_order_date = self.displayable_order_date.isoformat()

        displayable_order_comment = self.displayable_order_comment
        shipping_speed_category: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_speed_category, Unset):
            shipping_speed_category = self.shipping_speed_category.value

        destination_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination_address, Unset):
            destination_address = self.destination_address.to_dict()

        fulfillment_action: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_action, Unset):
            fulfillment_action = self.fulfillment_action.value

        fulfillment_policy: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_policy, Unset):
            fulfillment_policy = self.fulfillment_policy.value

        ship_from_country_code = self.ship_from_country_code
        notification_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notification_emails, Unset):
            notification_emails = self.notification_emails

        feature_constraints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.feature_constraints, Unset):
            feature_constraints = []
            for feature_constraints_item_data in self.feature_constraints:
                feature_constraints_item = feature_constraints_item_data.to_dict()

                feature_constraints.append(feature_constraints_item)

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for componentsschemas_update_fulfillment_order_item_list_item_data in self.items:
                componentsschemas_update_fulfillment_order_item_list_item = (
                    componentsschemas_update_fulfillment_order_item_list_item_data.to_dict()
                )

                items.append(componentsschemas_update_fulfillment_order_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if displayable_order_id is not UNSET:
            field_dict["displayableOrderId"] = displayable_order_id
        if displayable_order_date is not UNSET:
            field_dict["displayableOrderDate"] = displayable_order_date
        if displayable_order_comment is not UNSET:
            field_dict["displayableOrderComment"] = displayable_order_comment
        if shipping_speed_category is not UNSET:
            field_dict["shippingSpeedCategory"] = shipping_speed_category
        if destination_address is not UNSET:
            field_dict["destinationAddress"] = destination_address
        if fulfillment_action is not UNSET:
            field_dict["fulfillmentAction"] = fulfillment_action
        if fulfillment_policy is not UNSET:
            field_dict["fulfillmentPolicy"] = fulfillment_policy
        if ship_from_country_code is not UNSET:
            field_dict["shipFromCountryCode"] = ship_from_country_code
        if notification_emails is not UNSET:
            field_dict["notificationEmails"] = notification_emails
        if feature_constraints is not UNSET:
            field_dict["featureConstraints"] = feature_constraints
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.feature_settings import FeatureSettings
        from ..models.update_fulfillment_order_item import UpdateFulfillmentOrderItem

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId", UNSET)

        displayable_order_id = d.pop("displayableOrderId", UNSET)

        _displayable_order_date = d.pop("displayableOrderDate", UNSET)
        displayable_order_date: Union[Unset, datetime.datetime]
        if isinstance(_displayable_order_date, Unset):
            displayable_order_date = UNSET
        else:
            displayable_order_date = isoparse(_displayable_order_date)

        displayable_order_comment = d.pop("displayableOrderComment", UNSET)

        _shipping_speed_category = d.pop("shippingSpeedCategory", UNSET)
        shipping_speed_category: Union[Unset, ShippingSpeedCategory]
        if isinstance(_shipping_speed_category, Unset):
            shipping_speed_category = UNSET
        else:
            shipping_speed_category = ShippingSpeedCategory(_shipping_speed_category)

        _destination_address = d.pop("destinationAddress", UNSET)
        destination_address: Union[Unset, Address]
        if isinstance(_destination_address, Unset):
            destination_address = UNSET
        else:
            destination_address = Address.from_dict(_destination_address)

        _fulfillment_action = d.pop("fulfillmentAction", UNSET)
        fulfillment_action: Union[Unset, FulfillmentAction]
        if isinstance(_fulfillment_action, Unset):
            fulfillment_action = UNSET
        else:
            fulfillment_action = FulfillmentAction(_fulfillment_action)

        _fulfillment_policy = d.pop("fulfillmentPolicy", UNSET)
        fulfillment_policy: Union[Unset, FulfillmentPolicy]
        if isinstance(_fulfillment_policy, Unset):
            fulfillment_policy = UNSET
        else:
            fulfillment_policy = FulfillmentPolicy(_fulfillment_policy)

        ship_from_country_code = d.pop("shipFromCountryCode", UNSET)

        notification_emails = cast(List[str], d.pop("notificationEmails", UNSET))

        feature_constraints = []
        _feature_constraints = d.pop("featureConstraints", UNSET)
        for feature_constraints_item_data in _feature_constraints or []:
            feature_constraints_item = FeatureSettings.from_dict(feature_constraints_item_data)

            feature_constraints.append(feature_constraints_item)

        items = []
        _items = d.pop("items", UNSET)
        for componentsschemas_update_fulfillment_order_item_list_item_data in _items or []:
            componentsschemas_update_fulfillment_order_item_list_item = UpdateFulfillmentOrderItem.from_dict(
                componentsschemas_update_fulfillment_order_item_list_item_data
            )

            items.append(componentsschemas_update_fulfillment_order_item_list_item)

        result = cls(
            marketplace_id=marketplace_id,
            displayable_order_id=displayable_order_id,
            displayable_order_date=displayable_order_date,
            displayable_order_comment=displayable_order_comment,
            shipping_speed_category=shipping_speed_category,
            destination_address=destination_address,
            fulfillment_action=fulfillment_action,
            fulfillment_policy=fulfillment_policy,
            ship_from_country_code=ship_from_country_code,
            notification_emails=notification_emails,
            feature_constraints=feature_constraints,
            items=items,
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
