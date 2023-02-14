from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_order_metrics_buyer_type import GetOrderMetricsBuyerType
from ...models.get_order_metrics_first_day_of_week import GetOrderMetricsFirstDayOfWeek
from ...models.get_order_metrics_granularity import GetOrderMetricsGranularity
from ...models.get_order_metrics_response import GetOrderMetricsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marketplace_ids: List[str],
    interval: str,
    granularity_time_zone: Union[Unset, None, str] = UNSET,
    granularity: GetOrderMetricsGranularity,
    buyer_type: Union[Unset, None, GetOrderMetricsBuyerType] = GetOrderMetricsBuyerType.ALL,
    fulfillment_network: Union[Unset, None, str] = UNSET,
    first_day_of_week: Union[Unset, None, GetOrderMetricsFirstDayOfWeek] = GetOrderMetricsFirstDayOfWeek.MONDAY,
    asin: Union[Unset, None, str] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sales/v1/orderMetrics".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["interval"] = interval

    params["granularityTimeZone"] = granularity_time_zone

    json_granularity = granularity.value

    params["granularity"] = json_granularity

    json_buyer_type: Union[Unset, None, str] = UNSET
    if not isinstance(buyer_type, Unset):
        json_buyer_type = buyer_type.value if buyer_type else None

    params["buyerType"] = json_buyer_type

    params["fulfillmentNetwork"] = fulfillment_network

    json_first_day_of_week: Union[Unset, None, str] = UNSET
    if not isinstance(first_day_of_week, Unset):
        json_first_day_of_week = first_day_of_week.value if first_day_of_week else None

    params["firstDayOfWeek"] = json_first_day_of_week

    params["asin"] = asin

    params["sku"] = sku

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetOrderMetricsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOrderMetricsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOrderMetricsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOrderMetricsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetOrderMetricsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = GetOrderMetricsResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetOrderMetricsResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetOrderMetricsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetOrderMetricsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetOrderMetricsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetOrderMetricsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    marketplace_ids: List[str],
    interval: str,
    granularity_time_zone: Union[Unset, None, str] = UNSET,
    granularity: GetOrderMetricsGranularity,
    buyer_type: Union[Unset, None, GetOrderMetricsBuyerType] = GetOrderMetricsBuyerType.ALL,
    fulfillment_network: Union[Unset, None, str] = UNSET,
    first_day_of_week: Union[Unset, None, GetOrderMetricsFirstDayOfWeek] = GetOrderMetricsFirstDayOfWeek.MONDAY,
    asin: Union[Unset, None, str] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Response[GetOrderMetricsResponse]:
    """Returns aggregated order metrics for given interval, broken down by granularity, for given buyer
    type.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_ids (List[str]):
        interval (str):
        granularity_time_zone (Union[Unset, None, str]):
        granularity (GetOrderMetricsGranularity):
        buyer_type (Union[Unset, None, GetOrderMetricsBuyerType]):  Default:
            GetOrderMetricsBuyerType.ALL.
        fulfillment_network (Union[Unset, None, str]):
        first_day_of_week (Union[Unset, None, GetOrderMetricsFirstDayOfWeek]):  Default:
            GetOrderMetricsFirstDayOfWeek.MONDAY.
        asin (Union[Unset, None, str]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderMetricsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_ids=marketplace_ids,
        interval=interval,
        granularity_time_zone=granularity_time_zone,
        granularity=granularity,
        buyer_type=buyer_type,
        fulfillment_network=fulfillment_network,
        first_day_of_week=first_day_of_week,
        asin=asin,
        sku=sku,
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
    marketplace_ids: List[str],
    interval: str,
    granularity_time_zone: Union[Unset, None, str] = UNSET,
    granularity: GetOrderMetricsGranularity,
    buyer_type: Union[Unset, None, GetOrderMetricsBuyerType] = GetOrderMetricsBuyerType.ALL,
    fulfillment_network: Union[Unset, None, str] = UNSET,
    first_day_of_week: Union[Unset, None, GetOrderMetricsFirstDayOfWeek] = GetOrderMetricsFirstDayOfWeek.MONDAY,
    asin: Union[Unset, None, str] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Optional[GetOrderMetricsResponse]:
    """Returns aggregated order metrics for given interval, broken down by granularity, for given buyer
    type.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_ids (List[str]):
        interval (str):
        granularity_time_zone (Union[Unset, None, str]):
        granularity (GetOrderMetricsGranularity):
        buyer_type (Union[Unset, None, GetOrderMetricsBuyerType]):  Default:
            GetOrderMetricsBuyerType.ALL.
        fulfillment_network (Union[Unset, None, str]):
        first_day_of_week (Union[Unset, None, GetOrderMetricsFirstDayOfWeek]):  Default:
            GetOrderMetricsFirstDayOfWeek.MONDAY.
        asin (Union[Unset, None, str]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderMetricsResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_ids=marketplace_ids,
        interval=interval,
        granularity_time_zone=granularity_time_zone,
        granularity=granularity,
        buyer_type=buyer_type,
        fulfillment_network=fulfillment_network,
        first_day_of_week=first_day_of_week,
        asin=asin,
        sku=sku,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_ids: List[str],
    interval: str,
    granularity_time_zone: Union[Unset, None, str] = UNSET,
    granularity: GetOrderMetricsGranularity,
    buyer_type: Union[Unset, None, GetOrderMetricsBuyerType] = GetOrderMetricsBuyerType.ALL,
    fulfillment_network: Union[Unset, None, str] = UNSET,
    first_day_of_week: Union[Unset, None, GetOrderMetricsFirstDayOfWeek] = GetOrderMetricsFirstDayOfWeek.MONDAY,
    asin: Union[Unset, None, str] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Response[GetOrderMetricsResponse]:
    """Returns aggregated order metrics for given interval, broken down by granularity, for given buyer
    type.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_ids (List[str]):
        interval (str):
        granularity_time_zone (Union[Unset, None, str]):
        granularity (GetOrderMetricsGranularity):
        buyer_type (Union[Unset, None, GetOrderMetricsBuyerType]):  Default:
            GetOrderMetricsBuyerType.ALL.
        fulfillment_network (Union[Unset, None, str]):
        first_day_of_week (Union[Unset, None, GetOrderMetricsFirstDayOfWeek]):  Default:
            GetOrderMetricsFirstDayOfWeek.MONDAY.
        asin (Union[Unset, None, str]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderMetricsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_ids=marketplace_ids,
        interval=interval,
        granularity_time_zone=granularity_time_zone,
        granularity=granularity,
        buyer_type=buyer_type,
        fulfillment_network=fulfillment_network,
        first_day_of_week=first_day_of_week,
        asin=asin,
        sku=sku,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_ids: List[str],
    interval: str,
    granularity_time_zone: Union[Unset, None, str] = UNSET,
    granularity: GetOrderMetricsGranularity,
    buyer_type: Union[Unset, None, GetOrderMetricsBuyerType] = GetOrderMetricsBuyerType.ALL,
    fulfillment_network: Union[Unset, None, str] = UNSET,
    first_day_of_week: Union[Unset, None, GetOrderMetricsFirstDayOfWeek] = GetOrderMetricsFirstDayOfWeek.MONDAY,
    asin: Union[Unset, None, str] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Optional[GetOrderMetricsResponse]:
    """Returns aggregated order metrics for given interval, broken down by granularity, for given buyer
    type.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_ids (List[str]):
        interval (str):
        granularity_time_zone (Union[Unset, None, str]):
        granularity (GetOrderMetricsGranularity):
        buyer_type (Union[Unset, None, GetOrderMetricsBuyerType]):  Default:
            GetOrderMetricsBuyerType.ALL.
        fulfillment_network (Union[Unset, None, str]):
        first_day_of_week (Union[Unset, None, GetOrderMetricsFirstDayOfWeek]):  Default:
            GetOrderMetricsFirstDayOfWeek.MONDAY.
        asin (Union[Unset, None, str]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderMetricsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_ids=marketplace_ids,
            interval=interval,
            granularity_time_zone=granularity_time_zone,
            granularity=granularity,
            buyer_type=buyer_type,
            fulfillment_network=fulfillment_network,
            first_day_of_week=first_day_of_week,
            asin=asin,
            sku=sku,
        )
    ).parsed
