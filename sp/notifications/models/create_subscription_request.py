from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processing_directive import ProcessingDirective


T = TypeVar("T", bound="CreateSubscriptionRequest")


@attr.s(auto_attribs=True)
class CreateSubscriptionRequest:
    r"""The request schema for the createSubscription operation.

    Attributes:
        payload_version (Union[Unset, str]): The version of the payload object to be used in the notification.
        destination_id (Union[Unset, str]): The identifier for the destination where notifications will be delivered.
        processing_directive (Union[Unset, ProcessingDirective]): Additional information passed to the subscription to
            control the processing of notifications. For example, you can use an eventFilter to customize your subscription
            to send notifications for only the specified marketplaceId's, or select the aggregation time period at which to
            send notifications (e.g. limit to one notification every five minutes for high frequency notifications). The
            specific features available vary depending on the notificationType.

            This feature is limited to specific notificationTypes and is currently only supported by the ANY_OFFER_CHANGED
            notificationType.
    """

    payload_version: Union[Unset, str] = UNSET
    destination_id: Union[Unset, str] = UNSET
    processing_directive: Union[Unset, "ProcessingDirective"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload_version = self.payload_version
        destination_id = self.destination_id
        processing_directive: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.processing_directive, Unset):
            processing_directive = self.processing_directive.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload_version is not UNSET:
            field_dict["payloadVersion"] = payload_version
        if destination_id is not UNSET:
            field_dict["destinationId"] = destination_id
        if processing_directive is not UNSET:
            field_dict["processingDirective"] = processing_directive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.processing_directive import ProcessingDirective

        d = src_dict.copy()
        payload_version = d.pop("payloadVersion", UNSET)

        destination_id = d.pop("destinationId", UNSET)

        _processing_directive = d.pop("processingDirective", UNSET)
        processing_directive: Union[Unset, ProcessingDirective]
        if isinstance(_processing_directive, Unset):
            processing_directive = UNSET
        else:
            processing_directive = ProcessingDirective.from_dict(_processing_directive)

        result = cls(
            payload_version=payload_version,
            destination_id=destination_id,
            processing_directive=processing_directive,
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
