from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_reason import ErrorReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidASIN")


@attr.s(auto_attribs=True)
class InvalidASIN:
    r"""
    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        error_reason (Union[Unset, ErrorReason]): The reason that the ASIN is invalid.
    """

    asin: Union[Unset, str] = UNSET
    error_reason: Union[Unset, ErrorReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        error_reason: Union[Unset, str] = UNSET
        if not isinstance(self.error_reason, Unset):
            error_reason = self.error_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if error_reason is not UNSET:
            field_dict["ErrorReason"] = error_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asin = d.pop("ASIN", UNSET)

        _error_reason = d.pop("ErrorReason", UNSET)
        error_reason: Union[Unset, ErrorReason]
        if isinstance(_error_reason, Unset):
            error_reason = UNSET
        else:
            error_reason = ErrorReason(_error_reason)

        result = cls(
            asin=asin,
            error_reason=error_reason,
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
