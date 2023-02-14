from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_error_level import ErrorErrorLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    r"""Error response returned when the request is unsuccessful.

    Attributes:
        code (str): An error code that identifies the type of error that occurred.
        message (str): A message that describes the error condition in a human-readable form.
        details (Union[Unset, str]): Additional details that can help the caller understand or fix the issue.
        error_level (Union[Unset, ErrorErrorLevel]): The type of error.
    """

    code: str
    message: str
    details: Union[Unset, str] = UNSET
    error_level: Union[Unset, ErrorErrorLevel] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message
        details = self.details
        error_level: Union[Unset, str] = UNSET
        if not isinstance(self.error_level, Unset):
            error_level = self.error_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if error_level is not UNSET:
            field_dict["errorLevel"] = error_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        message = d.pop("message")

        details = d.pop("details", UNSET)

        _error_level = d.pop("errorLevel", UNSET)
        error_level: Union[Unset, ErrorErrorLevel]
        if isinstance(_error_level, Unset):
            error_level = UNSET
        else:
            error_level = ErrorErrorLevel(_error_level)

        result = cls(
            code=code,
            message=message,
            details=details,
            error_level=error_level,
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
