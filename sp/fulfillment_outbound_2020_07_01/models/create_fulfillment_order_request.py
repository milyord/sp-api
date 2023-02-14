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
    from ..models.cod_settings import CODSettings
    from ..models.create_fulfillment_order_item import CreateFulfillmentOrderItem
    from ..models.delivery_window import DeliveryWindow
    from ..models.feature_settings import FeatureSettings


T = TypeVar("T", bound="CreateFulfillmentOrderRequest")


@attr.s(auto_attribs=True)
class CreateFulfillmentOrderRequest:
    r"""The request body schema for the createFulfillmentOrder operation.

    Attributes:
        seller_fulfillment_order_id (str): A fulfillment order identifier that the seller creates to track their
            fulfillment order. The SellerFulfillmentOrderId must be unique for each fulfillment order that a seller creates.
            If the seller's system already creates unique order identifiers, then these might be good values for them to
            use.
        displayable_order_id (str): A fulfillment order identifier that the seller creates. This value displays as the
            order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of
            DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can
            use the SellerFulfillmentOrderId for this value or they can specify an alternate value if they want the
            recipient to reference an alternate order identifier.

            The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot
            contain two spaces in a row. Leading and trailing white space is removed.
        displayable_order_date (datetime.datetime):
        displayable_order_comment (str): Order-specific text that appears in recipient-facing materials such as the
            outbound shipment packing slip.
        shipping_speed_category (ShippingSpeedCategory): The shipping method used for the fulfillment order.
        destination_address (Address): A physical address.
        items (List['CreateFulfillmentOrderItem']): An array of item information for creating a fulfillment order.
        marketplace_id (Union[Unset, str]): The marketplace the fulfillment order is placed against.
        delivery_window (Union[Unset, DeliveryWindow]): The time range within which a Scheduled Delivery fulfillment
            order should be delivered.
        fulfillment_action (Union[Unset, FulfillmentAction]): Specifies whether the fulfillment order should ship now or
            have an order hold put on it.
        fulfillment_policy (Union[Unset, FulfillmentPolicy]): The FulfillmentPolicy value specified when you submitted
            the createFulfillmentOrder operation.
        cod_settings (Union[Unset, CODSettings]): The COD (Cash On Delivery) charges that you associate with a COD
            fulfillment order.
        ship_from_country_code (Union[Unset, str]): The two-character country code for the country from which the
            fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.
        notification_emails (Union[Unset, List[str]]): A list of email addresses that the seller provides that are used
            by Amazon to send ship-complete notifications to recipients on behalf of the seller.
        feature_constraints (Union[Unset, List['FeatureSettings']]): A list of features and their fulfillment policies
            to apply to the order.
    """

    seller_fulfillment_order_id: str
    displayable_order_id: str
    displayable_order_date: datetime.datetime
    displayable_order_comment: str
    shipping_speed_category: ShippingSpeedCategory
    destination_address: "Address"
    items: List["CreateFulfillmentOrderItem"]
    marketplace_id: Union[Unset, str] = UNSET
    delivery_window: Union[Unset, "DeliveryWindow"] = UNSET
    fulfillment_action: Union[Unset, FulfillmentAction] = UNSET
    fulfillment_policy: Union[Unset, FulfillmentPolicy] = UNSET
    cod_settings: Union[Unset, "CODSettings"] = UNSET
    ship_from_country_code: Union[Unset, str] = UNSET
    notification_emails: Union[Unset, List[str]] = UNSET
    feature_constraints: Union[Unset, List["FeatureSettings"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_fulfillment_order_id = self.seller_fulfillment_order_id
        displayable_order_id = self.displayable_order_id
        displayable_order_date = self.displayable_order_date.isoformat()

        displayable_order_comment = self.displayable_order_comment
        shipping_speed_category = self.shipping_speed_category.value

        destination_address = self.destination_address.to_dict()

        items = []
        for componentsschemas_create_fulfillment_order_item_list_item_data in self.items:
            componentsschemas_create_fulfillment_order_item_list_item = (
                componentsschemas_create_fulfillment_order_item_list_item_data.to_dict()
            )

            items.append(componentsschemas_create_fulfillment_order_item_list_item)

        marketplace_id = self.marketplace_id
        delivery_window: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delivery_window, Unset):
            delivery_window = self.delivery_window.to_dict()

        fulfillment_action: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_action, Unset):
            fulfillment_action = self.fulfillment_action.value

        fulfillment_policy: Union[Unset, str] = UNSET
        if not isinstance(self.fulfillment_policy, Unset):
            fulfillment_policy = self.fulfillment_policy.value

        cod_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cod_settings, Unset):
            cod_settings = self.cod_settings.to_dict()

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerFulfillmentOrderId": seller_fulfillment_order_id,
                "displayableOrderId": displayable_order_id,
                "displayableOrderDate": displayable_order_date,
                "displayableOrderComment": displayable_order_comment,
                "shippingSpeedCategory": shipping_speed_category,
                "destinationAddress": destination_address,
                "items": items,
            }
        )
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if delivery_window is not UNSET:
            field_dict["deliveryWindow"] = delivery_window
        if fulfillment_action is not UNSET:
            field_dict["fulfillmentAction"] = fulfillment_action
        if fulfillment_policy is not UNSET:
            field_dict["fulfillmentPolicy"] = fulfillment_policy
        if cod_settings is not UNSET:
            field_dict["codSettings"] = cod_settings
        if ship_from_country_code is not UNSET:
            field_dict["shipFromCountryCode"] = ship_from_country_code
        if notification_emails is not UNSET:
            field_dict["notificationEmails"] = notification_emails
        if feature_constraints is not UNSET:
            field_dict["featureConstraints"] = feature_constraints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.cod_settings import CODSettings
        from ..models.create_fulfillment_order_item import CreateFulfillmentOrderItem
        from ..models.delivery_window import DeliveryWindow
        from ..models.feature_settings import FeatureSettings

        d = src_dict.copy()
        seller_fulfillment_order_id = d.pop("sellerFulfillmentOrderId")

        displayable_order_id = d.pop("displayableOrderId")

        displayable_order_date = isoparse(d.pop("displayableOrderDate"))

        displayable_order_comment = d.pop("displayableOrderComment")

        shipping_speed_category = ShippingSpeedCategory(d.pop("shippingSpeedCategory"))

        destination_address = Address.from_dict(d.pop("destinationAddress"))

        items = []
        _items = d.pop("items")
        for componentsschemas_create_fulfillment_order_item_list_item_data in _items:
            componentsschemas_create_fulfillment_order_item_list_item = CreateFulfillmentOrderItem.from_dict(
                componentsschemas_create_fulfillment_order_item_list_item_data
            )

            items.append(componentsschemas_create_fulfillment_order_item_list_item)

        marketplace_id = d.pop("marketplaceId", UNSET)

        _delivery_window = d.pop("deliveryWindow", UNSET)
        delivery_window: Union[Unset, DeliveryWindow]
        if isinstance(_delivery_window, Unset):
            delivery_window = UNSET
        else:
            delivery_window = DeliveryWindow.from_dict(_delivery_window)

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

        _cod_settings = d.pop("codSettings", UNSET)
        cod_settings: Union[Unset, CODSettings]
        if isinstance(_cod_settings, Unset):
            cod_settings = UNSET
        else:
            cod_settings = CODSettings.from_dict(_cod_settings)

        ship_from_country_code = d.pop("shipFromCountryCode", UNSET)

        notification_emails = cast(List[str], d.pop("notificationEmails", UNSET))

        feature_constraints = []
        _feature_constraints = d.pop("featureConstraints", UNSET)
        for feature_constraints_item_data in _feature_constraints or []:
            feature_constraints_item = FeatureSettings.from_dict(feature_constraints_item_data)

            feature_constraints.append(feature_constraints_item)

        result = cls(
            seller_fulfillment_order_id=seller_fulfillment_order_id,
            displayable_order_id=displayable_order_id,
            displayable_order_date=displayable_order_date,
            displayable_order_comment=displayable_order_comment,
            shipping_speed_category=shipping_speed_category,
            destination_address=destination_address,
            items=items,
            marketplace_id=marketplace_id,
            delivery_window=delivery_window,
            fulfillment_action=fulfillment_action,
            fulfillment_policy=fulfillment_policy,
            cod_settings=cod_settings,
            ship_from_country_code=ship_from_country_code,
            notification_emails=notification_emails,
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
