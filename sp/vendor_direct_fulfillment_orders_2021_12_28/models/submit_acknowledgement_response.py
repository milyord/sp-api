from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_list import ErrorList
    from ..models.transaction_id import TransactionId


T = TypeVar("T", bound="SubmitAcknowledgementResponse")


@attr.s(auto_attribs=True)
class SubmitAcknowledgementResponse:
    r"""The response schema for the submitAcknowledgement operation.

    Attributes:
        payload (Union[Unset, TransactionId]):
        errors (Union[Unset, ErrorList]): A list of error responses returned when a request is unsuccessful.
    """

    payload: Union[Unset, "TransactionId"] = UNSET
    errors: Union[Unset, "ErrorList"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        errors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_list import ErrorList
        from ..models.transaction_id import TransactionId

        d = src_dict.copy()
        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, TransactionId]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TransactionId.from_dict(_payload)

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, ErrorList]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ErrorList.from_dict(_errors)

        result = cls(
            payload=payload,
            errors=errors,
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
