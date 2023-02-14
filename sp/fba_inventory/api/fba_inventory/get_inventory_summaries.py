import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_inventory_summaries_granularity_type import GetInventorySummariesGranularityType
from ...models.get_inventory_summaries_response import GetInventorySummariesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    details: Union[Unset, None, bool] = False,
    granularity_type: GetInventorySummariesGranularityType,
    granularity_id: str,
    start_date_time: Union[Unset, None, datetime.datetime] = UNSET,
    seller_skus: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
) -> Dict[str, Any]:
    url = "{}/fba/inventory/v1/summaries".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["details"] = details

    json_granularity_type = granularity_type.value

    params["granularityType"] = json_granularity_type

    params["granularityId"] = granularity_id

    json_start_date_time: Union[Unset, None, str] = UNSET
    if not isinstance(start_date_time, Unset):
        json_start_date_time = start_date_time.isoformat() if start_date_time else None

    params["startDateTime"] = json_start_date_time

    json_seller_skus: Union[Unset, None, List[str]] = UNSET
    if not isinstance(seller_skus, Unset):
        if seller_skus is None:
            json_seller_skus = None
        else:
            json_seller_skus = seller_skus

    params["sellerSkus"] = json_seller_skus

    params["nextToken"] = next_token

    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetInventorySummariesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetInventorySummariesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetInventorySummariesResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetInventorySummariesResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetInventorySummariesResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetInventorySummariesResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetInventorySummariesResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetInventorySummariesResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetInventorySummariesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    details: Union[Unset, None, bool] = False,
    granularity_type: GetInventorySummariesGranularityType,
    granularity_id: str,
    start_date_time: Union[Unset, None, datetime.datetime] = UNSET,
    seller_skus: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
) -> Response[GetInventorySummariesResponse]:
    """Returns a list of inventory summaries. The summaries returned depend on the presence or absence of
    the `startDateTime` and `sellerSkus` parameters:

    - All inventory summaries with available details are returned when the `startDateTime` and
    `sellerSkus` parameters are omitted.
    - When `startDateTime` is provided, the operation returns inventory summaries that have had changes
    after the date and time specified. The `sellerSkus` parameter is ignored. **Important:** To avoid
    errors, use both `startDateTime` and `nextToken` to get the next page of inventory summaries that
    have changed after the date and time specified.
    - When the `sellerSkus` parameter is provided, the operation returns inventory summaries for only
    the specified `sellerSkus`.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        details (Union[Unset, None, bool]):
        granularity_type (GetInventorySummariesGranularityType):
        granularity_id (str):
        start_date_time (Union[Unset, None, datetime.datetime]):
        seller_skus (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInventorySummariesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        details=details,
        granularity_type=granularity_type,
        granularity_id=granularity_id,
        start_date_time=start_date_time,
        seller_skus=seller_skus,
        next_token=next_token,
        marketplace_ids=marketplace_ids,
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
    details: Union[Unset, None, bool] = False,
    granularity_type: GetInventorySummariesGranularityType,
    granularity_id: str,
    start_date_time: Union[Unset, None, datetime.datetime] = UNSET,
    seller_skus: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
) -> Optional[GetInventorySummariesResponse]:
    """Returns a list of inventory summaries. The summaries returned depend on the presence or absence of
    the `startDateTime` and `sellerSkus` parameters:

    - All inventory summaries with available details are returned when the `startDateTime` and
    `sellerSkus` parameters are omitted.
    - When `startDateTime` is provided, the operation returns inventory summaries that have had changes
    after the date and time specified. The `sellerSkus` parameter is ignored. **Important:** To avoid
    errors, use both `startDateTime` and `nextToken` to get the next page of inventory summaries that
    have changed after the date and time specified.
    - When the `sellerSkus` parameter is provided, the operation returns inventory summaries for only
    the specified `sellerSkus`.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        details (Union[Unset, None, bool]):
        granularity_type (GetInventorySummariesGranularityType):
        granularity_id (str):
        start_date_time (Union[Unset, None, datetime.datetime]):
        seller_skus (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInventorySummariesResponse]
    """

    return sync_detailed(
        client=client,
        details=details,
        granularity_type=granularity_type,
        granularity_id=granularity_id,
        start_date_time=start_date_time,
        seller_skus=seller_skus,
        next_token=next_token,
        marketplace_ids=marketplace_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    details: Union[Unset, None, bool] = False,
    granularity_type: GetInventorySummariesGranularityType,
    granularity_id: str,
    start_date_time: Union[Unset, None, datetime.datetime] = UNSET,
    seller_skus: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
) -> Response[GetInventorySummariesResponse]:
    """Returns a list of inventory summaries. The summaries returned depend on the presence or absence of
    the `startDateTime` and `sellerSkus` parameters:

    - All inventory summaries with available details are returned when the `startDateTime` and
    `sellerSkus` parameters are omitted.
    - When `startDateTime` is provided, the operation returns inventory summaries that have had changes
    after the date and time specified. The `sellerSkus` parameter is ignored. **Important:** To avoid
    errors, use both `startDateTime` and `nextToken` to get the next page of inventory summaries that
    have changed after the date and time specified.
    - When the `sellerSkus` parameter is provided, the operation returns inventory summaries for only
    the specified `sellerSkus`.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        details (Union[Unset, None, bool]):
        granularity_type (GetInventorySummariesGranularityType):
        granularity_id (str):
        start_date_time (Union[Unset, None, datetime.datetime]):
        seller_skus (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInventorySummariesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        details=details,
        granularity_type=granularity_type,
        granularity_id=granularity_id,
        start_date_time=start_date_time,
        seller_skus=seller_skus,
        next_token=next_token,
        marketplace_ids=marketplace_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    details: Union[Unset, None, bool] = False,
    granularity_type: GetInventorySummariesGranularityType,
    granularity_id: str,
    start_date_time: Union[Unset, None, datetime.datetime] = UNSET,
    seller_skus: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
) -> Optional[GetInventorySummariesResponse]:
    """Returns a list of inventory summaries. The summaries returned depend on the presence or absence of
    the `startDateTime` and `sellerSkus` parameters:

    - All inventory summaries with available details are returned when the `startDateTime` and
    `sellerSkus` parameters are omitted.
    - When `startDateTime` is provided, the operation returns inventory summaries that have had changes
    after the date and time specified. The `sellerSkus` parameter is ignored. **Important:** To avoid
    errors, use both `startDateTime` and `nextToken` to get the next page of inventory summaries that
    have changed after the date and time specified.
    - When the `sellerSkus` parameter is provided, the operation returns inventory summaries for only
    the specified `sellerSkus`.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        details (Union[Unset, None, bool]):
        granularity_type (GetInventorySummariesGranularityType):
        granularity_id (str):
        start_date_time (Union[Unset, None, datetime.datetime]):
        seller_skus (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInventorySummariesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            details=details,
            granularity_type=granularity_type,
            granularity_id=granularity_id,
            start_date_time=start_date_time,
            seller_skus=seller_skus,
            next_token=next_token,
            marketplace_ids=marketplace_ids,
        )
    ).parsed
