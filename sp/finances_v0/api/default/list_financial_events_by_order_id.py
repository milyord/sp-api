from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_financial_events_response import ListFinancialEventsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/finances/v0/orders/{orderId}/financialEvents".format(client.base_url, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MaxResultsPerPage"] = max_results_per_page

    params["NextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListFinancialEventsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListFinancialEventsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ListFinancialEventsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ListFinancialEventsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListFinancialEventsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ListFinancialEventsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListFinancialEventsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ListFinancialEventsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListFinancialEventsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[ListFinancialEventsResponse]:
    """Returns all financial events for the specified order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        order_id (str):
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventsResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        max_results_per_page=max_results_per_page,
        next_token=next_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[ListFinancialEventsResponse]:
    """Returns all financial events for the specified order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        order_id (str):
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventsResponse]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        max_results_per_page=max_results_per_page,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[ListFinancialEventsResponse]:
    """Returns all financial events for the specified order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        order_id (str):
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventsResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        max_results_per_page=max_results_per_page,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[ListFinancialEventsResponse]:
    """Returns all financial events for the specified order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        order_id (str):
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventsResponse]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            max_results_per_page=max_results_per_page,
            next_token=next_token,
        )
    ).parsed
