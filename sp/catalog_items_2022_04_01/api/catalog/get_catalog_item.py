from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.get_catalog_item_included_data_item import GetCatalogItemIncludedDataItem
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asin: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[GetCatalogItemIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/catalog/2022-04-01/items/{asin}".format(client.base_url, asin=asin)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    json_included_data: Union[Unset, None, List[str]] = UNSET
    if not isinstance(included_data, Unset):
        if included_data is None:
            json_included_data = None
        else:
            json_included_data = []
            for included_data_item_data in included_data:
                included_data_item = included_data_item_data.value

                json_included_data.append(included_data_item)

    params["includedData"] = json_included_data

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, Item]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Item.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorList.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = ErrorList.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = ErrorList.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ErrorList.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorList.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ErrorList.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, Item]]:
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
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[GetCatalogItemIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, Item]]:
    """Retrieves details for an item in the Amazon catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[GetCatalogItemIncludedDataItem]]):
        locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Item]]
    """

    kwargs = _get_kwargs(
        asin=asin,
        client=client,
        marketplace_ids=marketplace_ids,
        included_data=included_data,
        locale=locale,
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
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[GetCatalogItemIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, Item]]:
    """Retrieves details for an item in the Amazon catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[GetCatalogItemIncludedDataItem]]):
        locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Item]]
    """

    return sync_detailed(
        asin=asin,
        client=client,
        marketplace_ids=marketplace_ids,
        included_data=included_data,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    asin: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[GetCatalogItemIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, Item]]:
    """Retrieves details for an item in the Amazon catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[GetCatalogItemIncludedDataItem]]):
        locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Item]]
    """

    kwargs = _get_kwargs(
        asin=asin,
        client=client,
        marketplace_ids=marketplace_ids,
        included_data=included_data,
        locale=locale,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asin: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[GetCatalogItemIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, Item]]:
    """Retrieves details for an item in the Amazon catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[GetCatalogItemIncludedDataItem]]):
        locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Item]]
    """

    return (
        await asyncio_detailed(
            asin=asin,
            client=client,
            marketplace_ids=marketplace_ids,
            included_data=included_data,
            locale=locale,
        )
    ).parsed
