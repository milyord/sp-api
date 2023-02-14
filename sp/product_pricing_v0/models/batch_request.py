from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.http_method import HttpMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_request_headers import HttpRequestHeaders


T = TypeVar("T", bound="BatchRequest")


@attr.s(auto_attribs=True)
class BatchRequest:
    r"""Common properties of batch requests against individual APIs.

    Attributes:
        uri (str): The resource path of the operation you are calling in batch without any query parameters.

            If you are calling `getItemOffersBatch`, supply the path of `getItemOffers`.

            **Example:** `/products/pricing/v0/items/B000P6Q7MY/offers`

            If you are calling `getListingOffersBatch`, supply the path of `getListingOffers`.

            **Example:** `/products/pricing/v0/listings/B000P6Q7MY/offers`
        method (HttpMethod): The HTTP method associated with the individual APIs being called as part of the batch
            request.
        headers (Union[Unset, HttpRequestHeaders]): A mapping of additional HTTP headers to send/receive for the
            individual batch request.
    """

    uri: str
    method: HttpMethod
    headers: Union[Unset, "HttpRequestHeaders"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uri = self.uri
        method = self.method.value

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
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_request_headers import HttpRequestHeaders

        d = src_dict.copy()
        uri = d.pop("uri")

        method = HttpMethod(d.pop("method"))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HttpRequestHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpRequestHeaders.from_dict(_headers)

        result = cls(
            uri=uri,
            method=method,
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
