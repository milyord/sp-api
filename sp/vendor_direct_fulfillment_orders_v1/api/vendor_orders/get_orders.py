import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_orders_response import GetOrdersResponse
from ...models.get_orders_sort_order import GetOrdersSortOrder
from ...models.get_orders_status import GetOrdersStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, GetOrdersStatus] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = "true",
) -> Dict[str, Any]:
    url = "{}/vendor/directFulfillment/orders/v1/purchaseOrders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["shipFromPartyId"] = ship_from_party_id

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

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

    params["includeDetails"] = include_details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetOrdersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOrdersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOrdersResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOrdersResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetOrdersResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetOrdersResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetOrdersResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetOrdersResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetOrdersResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetOrdersResponse]:
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
    status: Union[Unset, None, GetOrdersStatus] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = "true",
) -> Response[GetOrdersResponse]:
    """Returns a list of purchase orders created during the time frame that you specify. You define the
    time frame using the createdAfter and createdBefore parameters. You must use both parameters. You
    can choose to get only the purchase order numbers by setting the includeDetails parameter to false.
    In that case, the operation returns a list of purchase order numbers. You can then call the getOrder
    operation to return the details of a specific order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        status (Union[Unset, None, GetOrdersStatus]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        ship_from_party_id=ship_from_party_id,
        status=status,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
        include_details=include_details,
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
    status: Union[Unset, None, GetOrdersStatus] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = "true",
) -> Optional[GetOrdersResponse]:
    """Returns a list of purchase orders created during the time frame that you specify. You define the
    time frame using the createdAfter and createdBefore parameters. You must use both parameters. You
    can choose to get only the purchase order numbers by setting the includeDetails parameter to false.
    In that case, the operation returns a list of purchase order numbers. You can then call the getOrder
    operation to return the details of a specific order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        status (Union[Unset, None, GetOrdersStatus]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    return sync_detailed(
        client=client,
        ship_from_party_id=ship_from_party_id,
        status=status,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
        include_details=include_details,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, GetOrdersStatus] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = "true",
) -> Response[GetOrdersResponse]:
    """Returns a list of purchase orders created during the time frame that you specify. You define the
    time frame using the createdAfter and createdBefore parameters. You must use both parameters. You
    can choose to get only the purchase order numbers by setting the includeDetails parameter to false.
    In that case, the operation returns a list of purchase order numbers. You can then call the getOrder
    operation to return the details of a specific order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        status (Union[Unset, None, GetOrdersStatus]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        ship_from_party_id=ship_from_party_id,
        status=status,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
        include_details=include_details,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    ship_from_party_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, GetOrdersStatus] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    created_after: datetime.datetime,
    created_before: datetime.datetime,
    sort_order: Union[Unset, None, GetOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = "true",
) -> Optional[GetOrdersResponse]:
    """Returns a list of purchase orders created during the time frame that you specify. You define the
    time frame using the createdAfter and createdBefore parameters. You must use both parameters. You
    can choose to get only the purchase order numbers by setting the includeDetails parameter to false.
    In that case, the operation returns a list of purchase order numbers. You can then call the getOrder
    operation to return the details of a specific order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        ship_from_party_id (Union[Unset, None, str]):
        status (Union[Unset, None, GetOrdersStatus]):
        limit (Union[Unset, None, int]):
        created_after (datetime.datetime):
        created_before (datetime.datetime):
        sort_order (Union[Unset, None, GetOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            ship_from_party_id=ship_from_party_id,
            status=status,
            limit=limit,
            created_after=created_after,
            created_before=created_before,
            sort_order=sort_order,
            next_token=next_token,
            include_details=include_details,
        )
    ).parsed
