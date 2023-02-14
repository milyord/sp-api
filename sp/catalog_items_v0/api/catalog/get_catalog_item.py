from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_catalog_item_response import GetCatalogItemResponse
from ...types import UNSET, Response


def _get_kwargs(
    asin: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Dict[str, Any]:
    url = "{}/catalog/v0/items/{asin}".format(client.base_url, asin=asin)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MarketplaceId"] = marketplace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetCatalogItemResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCatalogItemResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetCatalogItemResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetCatalogItemResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetCatalogItemResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetCatalogItemResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetCatalogItemResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetCatalogItemResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetCatalogItemResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetCatalogItemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asin: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Response[GetCatalogItemResponse]:
    """Effective September 30, 2022, the `getCatalogItem` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. This operation is available in the latest version of the
    [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-api-v2022-04-01-reference).
    Integrations that rely on this operation should migrate to the latest version to avoid service
    disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        asin (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCatalogItemResponse]
    """

    kwargs = _get_kwargs(
        asin=asin,
        client=client,
        marketplace_id=marketplace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asin: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Optional[GetCatalogItemResponse]:
    """Effective September 30, 2022, the `getCatalogItem` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. This operation is available in the latest version of the
    [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-api-v2022-04-01-reference).
    Integrations that rely on this operation should migrate to the latest version to avoid service
    disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        asin (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCatalogItemResponse]
    """

    return sync_detailed(
        asin=asin,
        client=client,
        marketplace_id=marketplace_id,
    ).parsed


async def asyncio_detailed(
    asin: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Response[GetCatalogItemResponse]:
    """Effective September 30, 2022, the `getCatalogItem` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. This operation is available in the latest version of the
    [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-api-v2022-04-01-reference).
    Integrations that rely on this operation should migrate to the latest version to avoid service
    disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        asin (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCatalogItemResponse]
    """

    kwargs = _get_kwargs(
        asin=asin,
        client=client,
        marketplace_id=marketplace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asin: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Optional[GetCatalogItemResponse]:
    """Effective September 30, 2022, the `getCatalogItem` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. This operation is available in the latest version of the
    [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-api-v2022-04-01-reference).
    Integrations that rely on this operation should migrate to the latest version to avoid service
    disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        asin (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCatalogItemResponse]
    """

    return (
        await asyncio_detailed(
            asin=asin,
            client=client,
            marketplace_id=marketplace_id,
        )
    ).parsed
