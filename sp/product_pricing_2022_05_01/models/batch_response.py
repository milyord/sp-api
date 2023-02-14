from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.http_headers import HttpHeaders
    from ..models.http_status_line import HttpStatusLine


T = TypeVar("T", bound="BatchResponse")


@attr.s(auto_attribs=True)
class BatchResponse:
    r"""The common properties for responses to individual requests within a batch.

    Attributes:
        headers (HttpHeaders): A mapping of additional HTTP headers to send/receive for an individual request within a
            batch.
        status (HttpStatusLine): The HTTP status line associated with the response to an individual request within a
            batch. For more information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
    """

    headers: "HttpHeaders"
    status: "HttpStatusLine"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers = self.headers.to_dict()

        status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headers": headers,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_headers import HttpHeaders
        from ..models.http_status_line import HttpStatusLine

        d = src_dict.copy()
        headers = HttpHeaders.from_dict(d.pop("headers"))

        status = HttpStatusLine.from_dict(d.pop("status"))

        result = cls(
            headers=headers,
            status=status,
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
