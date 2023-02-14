import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.get_feeds_processing_statuses_item import GetFeedsProcessingStatusesItem
from ...models.get_feeds_response import GetFeedsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    feed_types: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    processing_statuses: Union[Unset, None, List[GetFeedsProcessingStatusesItem]] = UNSET,
    created_since: Union[Unset, None, datetime.datetime] = UNSET,
    created_until: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/feeds/2021-06-30/feeds".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_feed_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(feed_types, Unset):
        if feed_types is None:
            json_feed_types = None
        else:
            json_feed_types = feed_types

    params["feedTypes"] = json_feed_types

    json_marketplace_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(marketplace_ids, Unset):
        if marketplace_ids is None:
            json_marketplace_ids = None
        else:
            json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["pageSize"] = page_size

    json_processing_statuses: Union[Unset, None, List[str]] = UNSET
    if not isinstance(processing_statuses, Unset):
        if processing_statuses is None:
            json_processing_statuses = None
        else:
            json_processing_statuses = []
            for processing_statuses_item_data in processing_statuses:
                processing_statuses_item = processing_statuses_item_data.value

                json_processing_statuses.append(processing_statuses_item)

    params["processingStatuses"] = json_processing_statuses

    json_created_since: Union[Unset, None, str] = UNSET
    if not isinstance(created_since, Unset):
        json_created_since = created_since.isoformat() if created_since else None

    params["createdSince"] = json_created_since

    json_created_until: Union[Unset, None, str] = UNSET
    if not isinstance(created_until, Unset):
        json_created_until = created_until.isoformat() if created_until else None

    params["createdUntil"] = json_created_until

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, GetFeedsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFeedsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorList.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorList.from_dict(response.json())

        return response_404
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, GetFeedsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    feed_types: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    processing_statuses: Union[Unset, None, List[GetFeedsProcessingStatusesItem]] = UNSET,
    created_since: Union[Unset, None, datetime.datetime] = UNSET,
    created_until: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, GetFeedsResponse]]:
    """Returns feed details for the feeds that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_types (Union[Unset, None, List[str]]):
        marketplace_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        processing_statuses (Union[Unset, None, List[GetFeedsProcessingStatusesItem]]):
        created_since (Union[Unset, None, datetime.datetime]):
        created_until (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetFeedsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        feed_types=feed_types,
        marketplace_ids=marketplace_ids,
        page_size=page_size,
        processing_statuses=processing_statuses,
        created_since=created_since,
        created_until=created_until,
        next_token=next_token,
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
    feed_types: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    processing_statuses: Union[Unset, None, List[GetFeedsProcessingStatusesItem]] = UNSET,
    created_since: Union[Unset, None, datetime.datetime] = UNSET,
    created_until: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, GetFeedsResponse]]:
    """Returns feed details for the feeds that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_types (Union[Unset, None, List[str]]):
        marketplace_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        processing_statuses (Union[Unset, None, List[GetFeedsProcessingStatusesItem]]):
        created_since (Union[Unset, None, datetime.datetime]):
        created_until (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetFeedsResponse]]
    """

    return sync_detailed(
        client=client,
        feed_types=feed_types,
        marketplace_ids=marketplace_ids,
        page_size=page_size,
        processing_statuses=processing_statuses,
        created_since=created_since,
        created_until=created_until,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    feed_types: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    processing_statuses: Union[Unset, None, List[GetFeedsProcessingStatusesItem]] = UNSET,
    created_since: Union[Unset, None, datetime.datetime] = UNSET,
    created_until: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, GetFeedsResponse]]:
    """Returns feed details for the feeds that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_types (Union[Unset, None, List[str]]):
        marketplace_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        processing_statuses (Union[Unset, None, List[GetFeedsProcessingStatusesItem]]):
        created_since (Union[Unset, None, datetime.datetime]):
        created_until (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetFeedsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        feed_types=feed_types,
        marketplace_ids=marketplace_ids,
        page_size=page_size,
        processing_statuses=processing_statuses,
        created_since=created_since,
        created_until=created_until,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    feed_types: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    processing_statuses: Union[Unset, None, List[GetFeedsProcessingStatusesItem]] = UNSET,
    created_since: Union[Unset, None, datetime.datetime] = UNSET,
    created_until: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, GetFeedsResponse]]:
    """Returns feed details for the feeds that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_types (Union[Unset, None, List[str]]):
        marketplace_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        processing_statuses (Union[Unset, None, List[GetFeedsProcessingStatusesItem]]):
        created_since (Union[Unset, None, datetime.datetime]):
        created_until (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetFeedsResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            feed_types=feed_types,
            marketplace_ids=marketplace_ids,
            page_size=page_size,
            processing_statuses=processing_statuses,
            created_since=created_since,
            created_until=created_until,
            next_token=next_token,
        )
    ).parsed
