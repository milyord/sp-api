from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_offers_http_status_line import GetOffersHttpStatusLine
    from ..models.get_offers_response import GetOffersResponse
    from ..models.http_response_headers import HttpResponseHeaders
    from ..models.item_offers_request_params import ItemOffersRequestParams


T = TypeVar("T", bound="ItemOffersResponse")


@attr.s(auto_attribs=True)
class ItemOffersResponse:
    r"""
    Attributes:
        body (GetOffersResponse): The response schema for the `getListingOffers` and `getItemOffers` operations.
        request (ItemOffersRequestParams):
        headers (Union[Unset, HttpResponseHeaders]): A mapping of additional HTTP headers to send/receive for the
            individual batch request.
        status (Union[Unset, GetOffersHttpStatusLine]): The HTTP status line associated with the response.  For more
            information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
    """

    body: "GetOffersResponse"
    request: "ItemOffersRequestParams"
    headers: Union[Unset, "HttpResponseHeaders"] = UNSET
    status: Union[Unset, "GetOffersHttpStatusLine"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body.to_dict()

        request = self.request.to_dict()

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "request": request,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_offers_http_status_line import GetOffersHttpStatusLine
        from ..models.get_offers_response import GetOffersResponse
        from ..models.http_response_headers import HttpResponseHeaders
        from ..models.item_offers_request_params import ItemOffersRequestParams

        d = src_dict.copy()
        body = GetOffersResponse.from_dict(d.pop("body"))

        request = ItemOffersRequestParams.from_dict(d.pop("request"))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HttpResponseHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpResponseHeaders.from_dict(_headers)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GetOffersHttpStatusLine]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetOffersHttpStatusLine.from_dict(_status)

        result = cls(
            body=body,
            request=request,
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
