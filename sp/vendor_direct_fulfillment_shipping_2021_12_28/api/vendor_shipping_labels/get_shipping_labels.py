import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.get_shipping_labels_sort_order import GetShippingLabelsSortOrder
from ...models.shipping_label_list import ShippingLabelList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetShippingLabelsSortOrder] = GetShippingLabelsSortOrder.ASC,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vendor/directFulfillment/shipping/2021-12-28/shippingLabels".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["shipFromPartyId"] = ship_from_party_id

    params["limit"] = limit

    json_created_after = created_after.isoformat()

    params["createdAfter"] = json_created_after

    json_created_before = created_before.isoformat()

    params["createdBefore"] = json_created_before

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, ShippingLabelList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ShippingLabelList.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, ShippingLabelList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetShippingLabelsSortOrder] = GetShippingLabelsSortOrder.ASC,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, ShippingLabelList]]:
    """Returns a list of shipping labels created during the time frame that you specify. You define that
    time frame using the createdAfter and createdBefore parameters. You must use both of these
    parameters. The date range to search must not be more than 7 days.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetShippingLabelsSortOrder]):  Default:
            GetShippingLabelsSortOrder.ASC.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabelList]]
    """

    kwargs = _get_kwargs(
        client=client,
        ship_from_party_id=ship_from_party_id,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
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
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetShippingLabelsSortOrder] = GetShippingLabelsSortOrder.ASC,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, ShippingLabelList]]:
    """Returns a list of shipping labels created during the time frame that you specify. You define that
    time frame using the createdAfter and createdBefore parameters. You must use both of these
    parameters. The date range to search must not be more than 7 days.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetShippingLabelsSortOrder]):  Default:
            GetShippingLabelsSortOrder.ASC.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabelList]]
    """

    return sync_detailed(
        client=client,
        ship_from_party_id=ship_from_party_id,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetShippingLabelsSortOrder] = GetShippingLabelsSortOrder.ASC,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, ShippingLabelList]]:
    """Returns a list of shipping labels created during the time frame that you specify. You define that
    time frame using the createdAfter and createdBefore parameters. You must use both of these
    parameters. The date range to search must not be more than 7 days.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetShippingLabelsSortOrder]):  Default:
            GetShippingLabelsSortOrder.ASC.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabelList]]
    """

    kwargs = _get_kwargs(
        client=client,
        ship_from_party_id=ship_from_party_id,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetShippingLabelsSortOrder] = GetShippingLabelsSortOrder.ASC,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, ShippingLabelList]]:
    """Returns a list of shipping labels created during the time frame that you specify. You define that
    time frame using the createdAfter and createdBefore parameters. You must use both of these
    parameters. The date range to search must not be more than 7 days.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetShippingLabelsSortOrder]):  Default:
            GetShippingLabelsSortOrder.ASC.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabelList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            ship_from_party_id=ship_from_party_id,
            limit=limit,
            created_after=created_after,
            created_before=created_before,
            sort_order=sort_order,
            next_token=next_token,
        )
    ).parsed
