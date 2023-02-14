from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_listing_offers_customer_type import GetListingOffersCustomerType
from ...models.get_listing_offers_item_condition import GetListingOffersItemCondition
from ...models.get_offers_response import GetOffersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
    item_condition: GetListingOffersItemCondition,
    customer_type: Union[Unset, None, GetListingOffersCustomerType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/products/pricing/v0/listings/{SellerSKU}/offers".format(client.base_url, SellerSKU=seller_sku)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MarketplaceId"] = marketplace_id

    json_item_condition = item_condition.value

    params["ItemCondition"] = json_item_condition

    json_customer_type: Union[Unset, None, str] = UNSET
    if not isinstance(customer_type, Unset):
        json_customer_type = customer_type.value if customer_type else None

    params["CustomerType"] = json_customer_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetOffersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOffersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOffersResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetOffersResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOffersResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetOffersResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetOffersResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetOffersResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetOffersResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetOffersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
    item_condition: GetListingOffersItemCondition,
    customer_type: Union[Unset, None, GetListingOffersCustomerType] = UNSET,
) -> Response[GetOffersResponse]:
    """Returns the lowest priced offers for a single SKU listing.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):
        marketplace_id (str):
        item_condition (GetListingOffersItemCondition):
        customer_type (Union[Unset, None, GetListingOffersCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffersResponse]
    """

    kwargs = _get_kwargs(
        seller_sku=seller_sku,
        client=client,
        marketplace_id=marketplace_id,
        item_condition=item_condition,
        customer_type=customer_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
    item_condition: GetListingOffersItemCondition,
    customer_type: Union[Unset, None, GetListingOffersCustomerType] = UNSET,
) -> Optional[GetOffersResponse]:
    """Returns the lowest priced offers for a single SKU listing.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):
        marketplace_id (str):
        item_condition (GetListingOffersItemCondition):
        customer_type (Union[Unset, None, GetListingOffersCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffersResponse]
    """

    return sync_detailed(
        seller_sku=seller_sku,
        client=client,
        marketplace_id=marketplace_id,
        item_condition=item_condition,
        customer_type=customer_type,
    ).parsed


async def asyncio_detailed(
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
    item_condition: GetListingOffersItemCondition,
    customer_type: Union[Unset, None, GetListingOffersCustomerType] = UNSET,
) -> Response[GetOffersResponse]:
    """Returns the lowest priced offers for a single SKU listing.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):
        marketplace_id (str):
        item_condition (GetListingOffersItemCondition):
        customer_type (Union[Unset, None, GetListingOffersCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffersResponse]
    """

    kwargs = _get_kwargs(
        seller_sku=seller_sku,
        client=client,
        marketplace_id=marketplace_id,
        item_condition=item_condition,
        customer_type=customer_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
    item_condition: GetListingOffersItemCondition,
    customer_type: Union[Unset, None, GetListingOffersCustomerType] = UNSET,
) -> Optional[GetOffersResponse]:
    """Returns the lowest priced offers for a single SKU listing.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):
        marketplace_id (str):
        item_condition (GetListingOffersItemCondition):
        customer_type (Union[Unset, None, GetListingOffersCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffersResponse]
    """

    return (
        await asyncio_detailed(
            seller_sku=seller_sku,
            client=client,
            marketplace_id=marketplace_id,
            item_condition=item_condition,
            customer_type=customer_type,
        )
    ).parsed
