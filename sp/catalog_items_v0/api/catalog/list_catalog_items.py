from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_catalog_items_response import ListCatalogItemsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marketplace_id: str,
    query: Union[Unset, None, str] = UNSET,
    query_context_id: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
    upc: Union[Unset, None, str] = UNSET,
    ean: Union[Unset, None, str] = UNSET,
    isbn: Union[Unset, None, str] = UNSET,
    jan: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/catalog/v0/items".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MarketplaceId"] = marketplace_id

    params["Query"] = query

    params["QueryContextId"] = query_context_id

    params["SellerSKU"] = seller_sku

    params["UPC"] = upc

    params["EAN"] = ean

    params["ISBN"] = isbn

    params["JAN"] = jan

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListCatalogItemsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListCatalogItemsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ListCatalogItemsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ListCatalogItemsResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ListCatalogItemsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListCatalogItemsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ListCatalogItemsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListCatalogItemsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ListCatalogItemsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListCatalogItemsResponse]:
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
    query: Union[Unset, None, str] = UNSET,
    query_context_id: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
    upc: Union[Unset, None, str] = UNSET,
    ean: Union[Unset, None, str] = UNSET,
    isbn: Union[Unset, None, str] = UNSET,
    jan: Union[Unset, None, str] = UNSET,
) -> Response[ListCatalogItemsResponse]:
    """Effective September 30, 2022, the `listCatalogItems` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. As an alternative, `searchCatalogItems` is available in
    the latest version of the [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-
    api-v2022-04-01-reference). Integrations that rely on the `listCatalogItems` operation should
    migrate to the `searchCatalogItems`operation to avoid service disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        marketplace_id (str):
        query (Union[Unset, None, str]):
        query_context_id (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):
        upc (Union[Unset, None, str]):
        ean (Union[Unset, None, str]):
        isbn (Union[Unset, None, str]):
        jan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogItemsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        query=query,
        query_context_id=query_context_id,
        seller_sku=seller_sku,
        upc=upc,
        ean=ean,
        isbn=isbn,
        jan=jan,
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
    query: Union[Unset, None, str] = UNSET,
    query_context_id: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
    upc: Union[Unset, None, str] = UNSET,
    ean: Union[Unset, None, str] = UNSET,
    isbn: Union[Unset, None, str] = UNSET,
    jan: Union[Unset, None, str] = UNSET,
) -> Optional[ListCatalogItemsResponse]:
    """Effective September 30, 2022, the `listCatalogItems` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. As an alternative, `searchCatalogItems` is available in
    the latest version of the [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-
    api-v2022-04-01-reference). Integrations that rely on the `listCatalogItems` operation should
    migrate to the `searchCatalogItems`operation to avoid service disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        marketplace_id (str):
        query (Union[Unset, None, str]):
        query_context_id (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):
        upc (Union[Unset, None, str]):
        ean (Union[Unset, None, str]):
        isbn (Union[Unset, None, str]):
        jan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogItemsResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_id=marketplace_id,
        query=query,
        query_context_id=query_context_id,
        seller_sku=seller_sku,
        upc=upc,
        ean=ean,
        isbn=isbn,
        jan=jan,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_id: str,
    query: Union[Unset, None, str] = UNSET,
    query_context_id: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
    upc: Union[Unset, None, str] = UNSET,
    ean: Union[Unset, None, str] = UNSET,
    isbn: Union[Unset, None, str] = UNSET,
    jan: Union[Unset, None, str] = UNSET,
) -> Response[ListCatalogItemsResponse]:
    """Effective September 30, 2022, the `listCatalogItems` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. As an alternative, `searchCatalogItems` is available in
    the latest version of the [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-
    api-v2022-04-01-reference). Integrations that rely on the `listCatalogItems` operation should
    migrate to the `searchCatalogItems`operation to avoid service disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        marketplace_id (str):
        query (Union[Unset, None, str]):
        query_context_id (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):
        upc (Union[Unset, None, str]):
        ean (Union[Unset, None, str]):
        isbn (Union[Unset, None, str]):
        jan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogItemsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        query=query,
        query_context_id=query_context_id,
        seller_sku=seller_sku,
        upc=upc,
        ean=ean,
        isbn=isbn,
        jan=jan,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_id: str,
    query: Union[Unset, None, str] = UNSET,
    query_context_id: Union[Unset, None, str] = UNSET,
    seller_sku: Union[Unset, None, str] = UNSET,
    upc: Union[Unset, None, str] = UNSET,
    ean: Union[Unset, None, str] = UNSET,
    isbn: Union[Unset, None, str] = UNSET,
    jan: Union[Unset, None, str] = UNSET,
) -> Optional[ListCatalogItemsResponse]:
    """Effective September 30, 2022, the `listCatalogItems` operation will no longer be available in the
    Selling Partner API for Catalog Items v0. As an alternative, `searchCatalogItems` is available in
    the latest version of the [Selling Partner API for Catalog Items v2022-04-01](doc:catalog-items-
    api-v2022-04-01-reference). Integrations that rely on the `listCatalogItems` operation should
    migrate to the `searchCatalogItems`operation to avoid service disruption.
    _Note:_ The [`listCatalogCategories`](#get-catalogv0categories) operation is not being deprecated
    and you can continue to make calls to it.

    Args:
        marketplace_id (str):
        query (Union[Unset, None, str]):
        query_context_id (Union[Unset, None, str]):
        seller_sku (Union[Unset, None, str]):
        upc (Union[Unset, None, str]):
        ean (Union[Unset, None, str]):
        isbn (Union[Unset, None, str]):
        jan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCatalogItemsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_id=marketplace_id,
            query=query,
            query_context_id=query_context_id,
            seller_sku=seller_sku,
            upc=upc,
            ean=ean,
            isbn=isbn,
            jan=jan,
        )
    ).parsed
