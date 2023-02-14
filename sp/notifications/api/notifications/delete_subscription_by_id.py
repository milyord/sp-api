from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.delete_subscription_by_id_response import DeleteSubscriptionByIdResponse
from ...types import Response


def _get_kwargs(
    notification_type: str,
    subscription_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/notifications/v1/subscriptions/{notificationType}/{subscriptionId}".format(
        client.base_url, notificationType=notification_type, subscriptionId=subscription_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[DeleteSubscriptionByIdResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = DeleteSubscriptionByIdResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[DeleteSubscriptionByIdResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notification_type: str,
    subscription_id: str,
    *,
    client: Client,
) -> Response[DeleteSubscriptionByIdResponse]:
    """Deletes the subscription indicated by the subscription identifier and notification type that you
    specify. The subscription identifier can be for any subscription associated with your application.
    After you successfully call this operation, notifications will stop being sent for the associated
    subscription. The deleteSubscriptionById API is grantless. For more information, see [Grantless
    operations](doc:grantless-operations) in the Selling Partner API Developer Guide.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        notification_type (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriptionByIdResponse]
    """

    kwargs = _get_kwargs(
        notification_type=notification_type,
        subscription_id=subscription_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notification_type: str,
    subscription_id: str,
    *,
    client: Client,
) -> Optional[DeleteSubscriptionByIdResponse]:
    """Deletes the subscription indicated by the subscription identifier and notification type that you
    specify. The subscription identifier can be for any subscription associated with your application.
    After you successfully call this operation, notifications will stop being sent for the associated
    subscription. The deleteSubscriptionById API is grantless. For more information, see [Grantless
    operations](doc:grantless-operations) in the Selling Partner API Developer Guide.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        notification_type (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriptionByIdResponse]
    """

    return sync_detailed(
        notification_type=notification_type,
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    notification_type: str,
    subscription_id: str,
    *,
    client: Client,
) -> Response[DeleteSubscriptionByIdResponse]:
    """Deletes the subscription indicated by the subscription identifier and notification type that you
    specify. The subscription identifier can be for any subscription associated with your application.
    After you successfully call this operation, notifications will stop being sent for the associated
    subscription. The deleteSubscriptionById API is grantless. For more information, see [Grantless
    operations](doc:grantless-operations) in the Selling Partner API Developer Guide.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        notification_type (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriptionByIdResponse]
    """

    kwargs = _get_kwargs(
        notification_type=notification_type,
        subscription_id=subscription_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notification_type: str,
    subscription_id: str,
    *,
    client: Client,
) -> Optional[DeleteSubscriptionByIdResponse]:
    """Deletes the subscription indicated by the subscription identifier and notification type that you
    specify. The subscription identifier can be for any subscription associated with your application.
    After you successfully call this operation, notifications will stop being sent for the associated
    subscription. The deleteSubscriptionById API is grantless. For more information, see [Grantless
    operations](doc:grantless-operations) in the Selling Partner API Developer Guide.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        notification_type (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriptionByIdResponse]
    """

    return (
        await asyncio_detailed(
            notification_type=notification_type,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
