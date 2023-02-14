from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOffersHttpStatusLine")


@attr.s(auto_attribs=True)
class GetOffersHttpStatusLine:
    r"""The HTTP status line associated with the response.  For more information, consult [RFC
    2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).

        Attributes:
            status_code (Union[Unset, int]): The HTTP response Status Code.
            reason_phrase (Union[Unset, str]): The HTTP response Reason-Phase.
    """

    status_code: Union[Unset, int] = UNSET
    reason_phrase: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_code = self.status_code
        reason_phrase = self.reason_phrase

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if reason_phrase is not UNSET:
            field_dict["reasonPhrase"] = reason_phrase

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode", UNSET)

        reason_phrase = d.pop("reasonPhrase", UNSET)

        result = cls(
            status_code=status_code,
            reason_phrase=reason_phrase,
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
