from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.http_method import HttpMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_headers import HttpHeaders


T = TypeVar("T", bound="BatchRequest")


@attr.s(auto_attribs=True)
class BatchRequest:
    r"""The common properties for individual requests within a batch.

    Attributes:
        uri (str): The URI associated with an individual request within a batch. For FeaturedOfferExpectedPrice, this
            should be '/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice'.
        method (HttpMethod): The HTTP method associated with an individual request within a batch.
        body (Union[Unset, Any]): Additional HTTP body information associated with an individual request within a batch.
        headers (Union[Unset, HttpHeaders]): A mapping of additional HTTP headers to send/receive for an individual
            request within a batch.
    """

    uri: str
    method: HttpMethod
    body: Union[Unset, Any] = UNSET
    headers: Union[Unset, "HttpHeaders"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uri = self.uri
        method = self.method.value

        body = self.body
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "method": method,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_headers import HttpHeaders

        d = src_dict.copy()
        uri = d.pop("uri")

        method = HttpMethod(d.pop("method"))

        body = d.pop("body", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HttpHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpHeaders.from_dict(_headers)

        result = cls(
            uri=uri,
            method=method,
            body=body,
            headers=headers,
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
