from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transport_status import TransportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransportResult")


@attr.s(auto_attribs=True)
class TransportResult:
    r"""The workflow status for a shipment with an Amazon-partnered carrier.

    Attributes:
        transport_status (TransportStatus): Indicates the status of the Amazon-partnered carrier shipment.
        error_code (Union[Unset, str]): An error code that identifies the type of error that occured.
        error_description (Union[Unset, str]): A message that describes the error condition.
    """

    transport_status: TransportStatus
    error_code: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transport_status = self.transport_status.value

        error_code = self.error_code
        error_description = self.error_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TransportStatus": transport_status,
            }
        )
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code
        if error_description is not UNSET:
            field_dict["ErrorDescription"] = error_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transport_status = TransportStatus(d.pop("TransportStatus"))

        error_code = d.pop("ErrorCode", UNSET)

        error_description = d.pop("ErrorDescription", UNSET)

        result = cls(
            transport_status=transport_status,
            error_code=error_code,
            error_description=error_description,
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
