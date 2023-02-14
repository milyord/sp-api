import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.fulfillment_action import FulfillmentAction
from ..models.fulfillment_order_status import FulfillmentOrderStatus
from ..models.fulfillment_policy import FulfillmentPolicy
from ..models.shipping_speed_category import ShippingSpeedCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.cod_settings import CODSettings
    from ..models.delivery_window import DeliveryWindow
    from ..models.feature_settings import FeatureSettings


T = TypeVar("T", bound="FulfillmentOrder")


@attr.s(auto_attribs=True)
class FulfillmentOrder:
    r"""General information about a fulfillment order, including its status.

    Attributes:
        seller_fulfillment_order_id (str): The fulfillment order identifier submitted with the createFulfillmentOrder
            operation.
        marketplace_id (str): The identifier for the marketplace the fulfillment order is placed against.
        displayable_order_id (str): A fulfillment order identifier submitted with the createFulfillmentOrder operation.
            Displays as the order identifier in recipient-facing materials such as the packing slip.
        displayable_order_date (datetime.datetime):
        displayable_order_comment (str): A text block submitted with the createFulfillmentOrder operation. Displays in
            recipient-facing materials such as the packing slip.
        shipping_speed_category (ShippingSpeedCategory): The shipping method used for the fulfillment order.
        destination_address (Address): A physical address.
        received_date (datetime.datetime):
        fulfillment_order_status (FulfillmentOrderStatus): The current status of the fulfillment order.
        status_updated_date (datetime.datetime):
        delivery_window (Union[Unset, DeliveryWindow]): The time range within which a Scheduled Delivery fulfillment
            order should be delivered.
        fulfillment_action (Union[Unset, FulfillmentAction]): Specifies whether the fulfillment order should ship now or
            have an order hold put on it.
        fulfillment_policy (Union[Unset, FulfillmentPolicy]): The FulfillmentPolicy value specified when you submitted
            the createFulfillmentOrder operation.
        cod_settings (Union[Unset, CODSettings]): The COD (Cash On Delivery) charges that you associate with a COD
            fulfillment order.
        notification_emails (Union[Unset, List[str]]): A list of email addresses that the seller provides that are used
            by Amazon to send ship-complete notifications to recipients on behalf of the seller.
        feature_constraints (Union[Unset, List['FeatureSettings']]): A list of features and their fulfillment policies
            to apply to the order.
    """

    seller_fulfillment_order_id: str
    marketplace_id: str
    displayable_order_id: str
    displayable_order_date: datetime.datetime
    displayable_order_comment: str
    shipping_speed_category: ShippingSpeedCategory
    destination_address: "Address"
    received_date: datetime.datetime
    fulfillment_order_status: FulfillmentOrderStatus
    status_updated_date: datetime.datetime
    delivery_window: Union[Unset, "DeliveryWindow"] = UNSET
    fulfillment_action: Union[Unset, FulfillmentAction] = UNSET
    fulfillment_policy: Union[Unset, FulfillmentPolicy] = UNSET
    cod_settings: Union[Unset, "CODSettings"] = UNSET
    notification_emails: Union[Unset, List[str]] = UNSET
    feature_constraints: Union[Unset, List["FeatureSettings"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_fulfillment_order_id = self.seller_fulfillment_order_id
        marketplace_id = self.marketplace_id
        displayable_order_id = self.displayable_order_id
        displayable_order_date = self.displayable_order_date.isoformat()

        displayable_order_comment = self.displayable_order_comment
        shipping_speed_category = self.shipping_speed_category.value

        destination_address = self.destination_address.to_dict()

        received_date = self.received_date.isoformat()

        fulfillment_order_status = self.fulfillment_order_status.value

        status_updated_date = self.status_updated_date.isoformat()

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
                "marketplaceId": marketplace_id,
                "displayableOrderId": displayable_order_id,
                "displayableOrderDate": displayable_order_date,
                "displayableOrderComment": displayable_order_comment,
                "shippingSpeedCategory": shipping_speed_category,
                "destinationAddress": destination_address,
                "receivedDate": received_date,
                "fulfillmentOrderStatus": fulfillment_order_status,
                "statusUpdatedDate": status_updated_date,
            }
        )
        if delivery_window is not UNSET:
            field_dict["deliveryWindow"] = delivery_window
        if fulfillment_action is not UNSET:
            field_dict["fulfillmentAction"] = fulfillment_action
        if fulfillment_policy is not UNSET:
            field_dict["fulfillmentPolicy"] = fulfillment_policy
        if cod_settings is not UNSET:
            field_dict["codSettings"] = cod_settings
        if notification_emails is not UNSET:
            field_dict["notificationEmails"] = notification_emails
        if feature_constraints is not UNSET:
            field_dict["featureConstraints"] = feature_constraints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.cod_settings import CODSettings
        from ..models.delivery_window import DeliveryWindow
        from ..models.feature_settings import FeatureSettings

        d = src_dict.copy()
        seller_fulfillment_order_id = d.pop("sellerFulfillmentOrderId")

        marketplace_id = d.pop("marketplaceId")

        displayable_order_id = d.pop("displayableOrderId")

        displayable_order_date = isoparse(d.pop("displayableOrderDate"))

        displayable_order_comment = d.pop("displayableOrderComment")

        shipping_speed_category = ShippingSpeedCategory(d.pop("shippingSpeedCategory"))

        destination_address = Address.from_dict(d.pop("destinationAddress"))

        received_date = isoparse(d.pop("receivedDate"))

        fulfillment_order_status = FulfillmentOrderStatus(d.pop("fulfillmentOrderStatus"))

        status_updated_date = isoparse(d.pop("statusUpdatedDate"))

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

        notification_emails = cast(List[str], d.pop("notificationEmails", UNSET))

        feature_constraints = []
        _feature_constraints = d.pop("featureConstraints", UNSET)
        for feature_constraints_item_data in _feature_constraints or []:
            feature_constraints_item = FeatureSettings.from_dict(feature_constraints_item_data)

            feature_constraints.append(feature_constraints_item)

        result = cls(
            seller_fulfillment_order_id=seller_fulfillment_order_id,
            marketplace_id=marketplace_id,
            displayable_order_id=displayable_order_id,
            displayable_order_date=displayable_order_date,
            displayable_order_comment=displayable_order_comment,
            shipping_speed_category=shipping_speed_category,
            destination_address=destination_address,
            received_date=received_date,
            fulfillment_order_status=fulfillment_order_status,
            status_updated_date=status_updated_date,
            delivery_window=delivery_window,
            fulfillment_action=fulfillment_action,
            fulfillment_policy=fulfillment_policy,
            cod_settings=cod_settings,
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
