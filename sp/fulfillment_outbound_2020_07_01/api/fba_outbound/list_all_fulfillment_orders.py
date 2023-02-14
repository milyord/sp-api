import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_all_fulfillment_orders_response import ListAllFulfillmentOrdersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    query_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/fba/outbound/2020-07-01/fulfillmentOrders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_query_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(query_start_date, Unset):
        json_query_start_date = query_start_date.isoformat() if query_start_date else None

    params["queryStartDate"] = json_query_start_date

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListAllFulfillmentOrdersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ListAllFulfillmentOrdersResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListAllFulfillmentOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    query_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[ListAllFulfillmentOrdersResponse]:
    """Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by
    the next token parameter.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        query_start_date (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllFulfillmentOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        query_start_date=query_start_date,
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
    query_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[ListAllFulfillmentOrdersResponse]:
    """Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by
    the next token parameter.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        query_start_date (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllFulfillmentOrdersResponse]
    """

    return sync_detailed(
        client=client,
        query_start_date=query_start_date,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    query_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[ListAllFulfillmentOrdersResponse]:
    """Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by
    the next token parameter.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        query_start_date (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllFulfillmentOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        query_start_date=query_start_date,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    query_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[ListAllFulfillmentOrdersResponse]:
    """Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by
    the next token parameter.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        query_start_date (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllFulfillmentOrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            query_start_date=query_start_date,
            next_token=next_token,
        )
    ).parsed
