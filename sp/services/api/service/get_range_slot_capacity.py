from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.range_slot_capacity import RangeSlotCapacity
from ...models.range_slot_capacity_errors import RangeSlotCapacityErrors
from ...models.range_slot_capacity_query import RangeSlotCapacityQuery
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource_id: str,
    *,
    client: Client,
    json_body: RangeSlotCapacityQuery,
    marketplace_ids: List[str],
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/service/v1/serviceResources/{resourceId}/capacity/range".format(client.base_url, resourceId=resource_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["nextPageToken"] = next_page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RangeSlotCapacity.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = RangeSlotCapacityErrors.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    *,
    client: Client,
    json_body: RangeSlotCapacityQuery,
    marketplace_ids: List[str],
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]:
    """Provides capacity slots in a format similar to availability records.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        resource_id (str):
        marketplace_ids (List[str]):
        next_page_token (Union[Unset, None, str]):
        json_body (RangeSlotCapacityQuery): Request schema for the `getRangeSlotCapacity`
            operation. This schema is used to define the time range and capacity types that are being
            queried.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
        next_page_token=next_page_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    *,
    client: Client,
    json_body: RangeSlotCapacityQuery,
    marketplace_ids: List[str],
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]:
    """Provides capacity slots in a format similar to availability records.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        resource_id (str):
        marketplace_ids (List[str]):
        next_page_token (Union[Unset, None, str]):
        json_body (RangeSlotCapacityQuery): Request schema for the `getRangeSlotCapacity`
            operation. This schema is used to define the time range and capacity types that are being
            queried.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
        next_page_token=next_page_token,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    *,
    client: Client,
    json_body: RangeSlotCapacityQuery,
    marketplace_ids: List[str],
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]:
    """Provides capacity slots in a format similar to availability records.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        resource_id (str):
        marketplace_ids (List[str]):
        next_page_token (Union[Unset, None, str]):
        json_body (RangeSlotCapacityQuery): Request schema for the `getRangeSlotCapacity`
            operation. This schema is used to define the time range and capacity types that are being
            queried.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
        next_page_token=next_page_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    *,
    client: Client,
    json_body: RangeSlotCapacityQuery,
    marketplace_ids: List[str],
    next_page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]:
    """Provides capacity slots in a format similar to availability records.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        resource_id (str):
        marketplace_ids (List[str]):
        next_page_token (Union[Unset, None, str]):
        json_body (RangeSlotCapacityQuery): Request schema for the `getRangeSlotCapacity`
            operation. This schema is used to define the time range and capacity types that are being
            queried.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RangeSlotCapacity, RangeSlotCapacityErrors]]
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
            json_body=json_body,
            marketplace_ids=marketplace_ids,
            next_page_token=next_page_token,
        )
    ).parsed
