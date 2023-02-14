from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customer_type import CustomerType
from ..models.http_method import HttpMethod
from ..models.item_condition import ItemCondition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_request_headers import HttpRequestHeaders


T = TypeVar("T", bound="ItemOffersRequest")


@attr.s(auto_attribs=True)
class ItemOffersRequest:
    r"""
    Attributes:
        uri (str): The resource path of the operation you are calling in batch without any query parameters.

            If you are calling `getItemOffersBatch`, supply the path of `getItemOffers`.

            **Example:** `/products/pricing/v0/items/B000P6Q7MY/offers`

            If you are calling `getListingOffersBatch`, supply the path of `getListingOffers`.

            **Example:** `/products/pricing/v0/listings/B000P6Q7MY/offers`
        method (HttpMethod): The HTTP method associated with the individual APIs being called as part of the batch
            request.
        marketplace_id (str): A marketplace identifier. Specifies the marketplace for which prices are returned.
        item_condition (ItemCondition): Filters the offer listings to be considered based on item condition. Possible
            values: New, Used, Collectible, Refurbished, Club.
        headers (Union[Unset, HttpRequestHeaders]): A mapping of additional HTTP headers to send/receive for the
            individual batch request.
        customer_type (Union[Unset, CustomerType]): Indicates whether to request Consumer or Business offers. Default is
            Consumer.
    """

    uri: str
    method: HttpMethod
    marketplace_id: str
    item_condition: ItemCondition
    headers: Union[Unset, "HttpRequestHeaders"] = UNSET
    customer_type: Union[Unset, CustomerType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uri = self.uri
        method = self.method.value

        marketplace_id = self.marketplace_id
        item_condition = self.item_condition.value

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        customer_type: Union[Unset, str] = UNSET
        if not isinstance(self.customer_type, Unset):
            customer_type = self.customer_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "method": method,
                "MarketplaceId": marketplace_id,
                "ItemCondition": item_condition,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if customer_type is not UNSET:
            field_dict["CustomerType"] = customer_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_request_headers import HttpRequestHeaders

        d = src_dict.copy()
        uri = d.pop("uri")

        method = HttpMethod(d.pop("method"))

        marketplace_id = d.pop("MarketplaceId")

        item_condition = ItemCondition(d.pop("ItemCondition"))

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HttpRequestHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpRequestHeaders.from_dict(_headers)

        _customer_type = d.pop("CustomerType", UNSET)
        customer_type: Union[Unset, CustomerType]
        if isinstance(_customer_type, Unset):
            customer_type = UNSET
        else:
            customer_type = CustomerType(_customer_type)

        result = cls(
            uri=uri,
            method=method,
            marketplace_id=marketplace_id,
            item_condition=item_condition,
            headers=headers,
            customer_type=customer_type,
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
