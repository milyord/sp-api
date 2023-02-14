from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_order_items_response import GetOrderItemsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orders/v0/orders/{orderId}/orderItems".format(client.base_url, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetOrderItemsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOrderItemsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOrderItemsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOrderItemsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetOrderItemsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetOrderItemsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetOrderItemsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetOrderItemsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetOrderItemsResponse]:
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
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[GetOrderItemsResponse]:
    """Returns detailed order item information for the order that you specify. If NextToken is provided,
    it's used to retrieve the next page of order items.

    __Note__: When an order is in the Pending state (the order has been placed but payment has not been
    authorized), the getOrderItems operation does not return information about pricing, taxes, shipping
    charges, gift status or promotions for the order items in the order. After an order leaves the
    Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially
    Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes,
    shipping charges, gift status and promotions for the order items in the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderItemsResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
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
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[GetOrderItemsResponse]:
    """Returns detailed order item information for the order that you specify. If NextToken is provided,
    it's used to retrieve the next page of order items.

    __Note__: When an order is in the Pending state (the order has been placed but payment has not been
    authorized), the getOrderItems operation does not return information about pricing, taxes, shipping
    charges, gift status or promotions for the order items in the order. After an order leaves the
    Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially
    Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes,
    shipping charges, gift status and promotions for the order items in the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderItemsResponse]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[GetOrderItemsResponse]:
    """Returns detailed order item information for the order that you specify. If NextToken is provided,
    it's used to retrieve the next page of order items.

    __Note__: When an order is in the Pending state (the order has been placed but payment has not been
    authorized), the getOrderItems operation does not return information about pricing, taxes, shipping
    charges, gift status or promotions for the order items in the order. After an order leaves the
    Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially
    Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes,
    shipping charges, gift status and promotions for the order items in the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderItemsResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[GetOrderItemsResponse]:
    """Returns detailed order item information for the order that you specify. If NextToken is provided,
    it's used to retrieve the next page of order items.

    __Note__: When an order is in the Pending state (the order has been placed but payment has not been
    authorized), the getOrderItems operation does not return information about pricing, taxes, shipping
    charges, gift status or promotions for the order items in the order. After an order leaves the
    Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially
    Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes,
    shipping charges, gift status and promotions for the order items in the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderItemsResponse]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            next_token=next_token,
        )
    ).parsed
