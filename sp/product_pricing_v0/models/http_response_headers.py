from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpResponseHeaders")


@attr.s(auto_attribs=True)
class HttpResponseHeaders:
    r"""A mapping of additional HTTP headers to send/receive for the individual batch request.

    Attributes:
        date (Union[Unset, str]): The timestamp that the API request was received.  For more information, consult [RFC
            2616 Section 14](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
        x_amzn_request_id (Union[Unset, str]): Unique request reference ID.
    """

    date: Union[Unset, str] = UNSET
    x_amzn_request_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        x_amzn_request_id = self.x_amzn_request_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["Date"] = date
        if x_amzn_request_id is not UNSET:
            field_dict["x-amzn-RequestId"] = x_amzn_request_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("Date", UNSET)

        x_amzn_request_id = d.pop("x-amzn-RequestId", UNSET)

        result = cls(
            date=date,
            x_amzn_request_id=x_amzn_request_id,
        )

        result.additional_properties = d
        return result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
