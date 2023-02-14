from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transport_content import TransportContent


T = TypeVar("T", bound="GetTransportDetailsResult")


@attr.s(auto_attribs=True)
class GetTransportDetailsResult:
    r"""
    Attributes:
        transport_content (Union[Unset, TransportContent]): Inbound shipment information, including carrier details,
            shipment status, and the workflow status for a request for shipment with an Amazon-partnered carrier.
    """

    transport_content: Union[Unset, "TransportContent"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transport_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transport_content, Unset):
            transport_content = self.transport_content.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transport_content is not UNSET:
            field_dict["TransportContent"] = transport_content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_content import TransportContent

        d = src_dict.copy()
        _transport_content = d.pop("TransportContent", UNSET)
        transport_content: Union[Unset, TransportContent]
        if isinstance(_transport_content, Unset):
            transport_content = UNSET
        else:
            transport_content = TransportContent.from_dict(_transport_content)

        result = cls(
            transport_content=transport_content,
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
