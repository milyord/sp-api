from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_catalog_categories_response import ListCatalogCategoriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marketplace_id: str,
    asin: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/catalog/v0/categories".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MarketplaceId"] = marketplace_id

    params["ASIN"] = asin

    params["SellerSKU"] = seller_sku

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListCatalogCategoriesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ListCatalogCategoriesResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListCatalogCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    marketplace_id: str,
    asin: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
) -> Response[ListCatalogCategoriesResponse]:
    """Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.

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
        marketplace_id (str):
        asin (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogCategoriesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        asin=asin,
        seller_sku=seller_sku,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    marketplace_id: str,
    asin: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
) -> Optional[ListCatalogCategoriesResponse]:
    """Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.

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
        marketplace_id (str):
        asin (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogCategoriesResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_id=marketplace_id,
        asin=asin,
        seller_sku=seller_sku,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_id: str,
    asin: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
) -> Response[ListCatalogCategoriesResponse]:
    """Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.

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
        marketplace_id (str):
        asin (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogCategoriesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        asin=asin,
        seller_sku=seller_sku,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_id: str,
    asin: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
) -> Optional[ListCatalogCategoriesResponse]:
    """Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.

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
        marketplace_id (str):
        asin (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogCategoriesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_id=marketplace_id,
            asin=asin,
            seller_sku=seller_sku,
        )
    ).parsed
