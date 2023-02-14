from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.featured_offer_expected_price_request_params import FeaturedOfferExpectedPriceRequestParams
    from ..models.featured_offer_expected_price_response_body import FeaturedOfferExpectedPriceResponseBody
    from ..models.http_headers import HttpHeaders
    from ..models.http_status_line import HttpStatusLine


T = TypeVar("T", bound="FeaturedOfferExpectedPriceResponse")


@attr.s(auto_attribs=True)
class FeaturedOfferExpectedPriceResponse:
    r"""
    Attributes:
        headers (HttpHeaders): A mapping of additional HTTP headers to send/receive for an individual request within a
            batch.
        status (HttpStatusLine): The HTTP status line associated with the response to an individual request within a
            batch. For more information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
        request (FeaturedOfferExpectedPriceRequestParams): The parameters for an individual request.
        body (Union[Unset, FeaturedOfferExpectedPriceResponseBody]): The featured offer expected price response data for
            a requested SKU.
    """

    headers: "HttpHeaders"
    status: "HttpStatusLine"
    request: "FeaturedOfferExpectedPriceRequestParams"
    body: Union[Unset, "FeaturedOfferExpectedPriceResponseBody"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers = self.headers.to_dict()

        status = self.status.to_dict()

        request = self.request.to_dict()

        body: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headers": headers,
                "status": status,
                "request": request,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.featured_offer_expected_price_request_params import FeaturedOfferExpectedPriceRequestParams
        from ..models.featured_offer_expected_price_response_body import FeaturedOfferExpectedPriceResponseBody
        from ..models.http_headers import HttpHeaders
        from ..models.http_status_line import HttpStatusLine

        d = src_dict.copy()
        headers = HttpHeaders.from_dict(d.pop("headers"))

        status = HttpStatusLine.from_dict(d.pop("status"))

        request = FeaturedOfferExpectedPriceRequestParams.from_dict(d.pop("request"))

        _body = d.pop("body", UNSET)
        body: Union[Unset, FeaturedOfferExpectedPriceResponseBody]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = FeaturedOfferExpectedPriceResponseBody.from_dict(_body)

        result = cls(
            headers=headers,
            status=status,
            request=request,
            body=body,
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
