from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transport_result import TransportResult


T = TypeVar("T", bound="CommonTransportResult")


@attr.s(auto_attribs=True)
class CommonTransportResult:
    r"""
    Attributes:
        transport_result (Union[Unset, TransportResult]): The workflow status for a shipment with an Amazon-partnered
            carrier.
    """

    transport_result: Union[Unset, "TransportResult"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transport_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transport_result, Unset):
            transport_result = self.transport_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transport_result is not UNSET:
            field_dict["TransportResult"] = transport_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transport_result import TransportResult

        d = src_dict.copy()
        _transport_result = d.pop("TransportResult", UNSET)
        transport_result: Union[Unset, TransportResult]
        if isinstance(_transport_result, Unset):
            transport_result = UNSET
        else:
            transport_result = TransportResult.from_dict(_transport_result)

        result = cls(
            transport_result=transport_result,
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
