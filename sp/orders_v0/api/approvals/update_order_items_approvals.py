from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.update_items_approvals_error_response import UpdateItemsApprovalsErrorResponse
from ...models.update_order_approvals_request import UpdateOrderApprovalsRequest
from ...types import Response


def _get_kwargs(
    order_id: str,
    *,
    client: Client,
    json_body: UpdateOrderApprovalsRequest,
) -> Dict[str, Any]:
    url = "{}/orders/v0/orders/{orderId}/approvals".format(client.base_url, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, UpdateItemsApprovalsErrorResponse]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = UpdateItemsApprovalsErrorResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, UpdateItemsApprovalsErrorResponse]]:
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
    json_body: UpdateOrderApprovalsRequest,
) -> Response[Union[Any, UpdateItemsApprovalsErrorResponse]]:
    """Update the order items approvals for an order that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        json_body (UpdateOrderApprovalsRequest): The request body for the
            updateOrderItemsApprovals operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateItemsApprovalsErrorResponse]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        json_body=json_body,
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
    json_body: UpdateOrderApprovalsRequest,
) -> Optional[Union[Any, UpdateItemsApprovalsErrorResponse]]:
    """Update the order items approvals for an order that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        json_body (UpdateOrderApprovalsRequest): The request body for the
            updateOrderItemsApprovals operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateItemsApprovalsErrorResponse]]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Client,
    json_body: UpdateOrderApprovalsRequest,
) -> Response[Union[Any, UpdateItemsApprovalsErrorResponse]]:
    """Update the order items approvals for an order that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        json_body (UpdateOrderApprovalsRequest): The request body for the
            updateOrderItemsApprovals operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateItemsApprovalsErrorResponse]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Client,
    json_body: UpdateOrderApprovalsRequest,
) -> Optional[Union[Any, UpdateItemsApprovalsErrorResponse]]:
    """Update the order items approvals for an order that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        order_id (str):
        json_body (UpdateOrderApprovalsRequest): The request body for the
            updateOrderItemsApprovals operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateItemsApprovalsErrorResponse]]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
