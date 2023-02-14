from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.cancel_fulfillment_order_response import CancelFulfillmentOrderResponse
from ...types import Response


def _get_kwargs(
    seller_fulfillment_order_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel".format(
        client.base_url, sellerFulfillmentOrderId=seller_fulfillment_order_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CancelFulfillmentOrderResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = CancelFulfillmentOrderResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CancelFulfillmentOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    seller_fulfillment_order_id: str,
    *,
    client: Client,
) -> Response[CancelFulfillmentOrderResponse]:
    """Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified
    order identifier.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_fulfillment_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFulfillmentOrderResponse]
    """

    kwargs = _get_kwargs(
        seller_fulfillment_order_id=seller_fulfillment_order_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    seller_fulfillment_order_id: str,
    *,
    client: Client,
) -> Optional[CancelFulfillmentOrderResponse]:
    """Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified
    order identifier.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_fulfillment_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFulfillmentOrderResponse]
    """

    return sync_detailed(
        seller_fulfillment_order_id=seller_fulfillment_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    seller_fulfillment_order_id: str,
    *,
    client: Client,
) -> Response[CancelFulfillmentOrderResponse]:
    """Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified
    order identifier.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_fulfillment_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFulfillmentOrderResponse]
    """

    kwargs = _get_kwargs(
        seller_fulfillment_order_id=seller_fulfillment_order_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    seller_fulfillment_order_id: str,
    *,
    client: Client,
) -> Optional[CancelFulfillmentOrderResponse]:
    """Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified
    order identifier.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_fulfillment_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFulfillmentOrderResponse]
    """

    return (
        await asyncio_detailed(
            seller_fulfillment_order_id=seller_fulfillment_order_id,
            client=client,
        )
    ).parsed
