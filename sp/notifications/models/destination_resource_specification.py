from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_bridge_resource_specification import EventBridgeResourceSpecification
    from ..models.sqs_resource import SqsResource


T = TypeVar("T", bound="DestinationResourceSpecification")


@attr.s(auto_attribs=True)
class DestinationResourceSpecification:
    r"""The information required to create a destination resource. Applications should use one resource type (sqs or
    eventBridge) per destination.

        Attributes:
            sqs (Union[Unset, SqsResource]): The information required to create an Amazon Simple Queue Service (Amazon SQS)
                queue destination.
            event_bridge (Union[Unset, EventBridgeResourceSpecification]): The information required to create an Amazon
                EventBridge destination.
    """

    sqs: Union[Unset, "SqsResource"] = UNSET
    event_bridge: Union[Unset, "EventBridgeResourceSpecification"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sqs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sqs, Unset):
            sqs = self.sqs.to_dict()

        event_bridge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_bridge, Unset):
            event_bridge = self.event_bridge.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sqs is not UNSET:
            field_dict["sqs"] = sqs
        if event_bridge is not UNSET:
            field_dict["eventBridge"] = event_bridge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_bridge_resource_specification import EventBridgeResourceSpecification
        from ..models.sqs_resource import SqsResource

        d = src_dict.copy()
        _sqs = d.pop("sqs", UNSET)
        sqs: Union[Unset, SqsResource]
        if isinstance(_sqs, Unset):
            sqs = UNSET
        else:
            sqs = SqsResource.from_dict(_sqs)

        _event_bridge = d.pop("eventBridge", UNSET)
        event_bridge: Union[Unset, EventBridgeResourceSpecification]
        if isinstance(_event_bridge, Unset):
            event_bridge = UNSET
        else:
            event_bridge = EventBridgeResourceSpecification.from_dict(_event_bridge)

        result = cls(
            sqs=sqs,
            event_bridge=event_bridge,
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
