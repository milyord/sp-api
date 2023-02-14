from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.cancel_feed_response import CancelFeedResponse
from ...types import Response


def _get_kwargs(
    feed_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/feeds/2020-09-04/feeds/{feedId}".format(client.base_url, feedId=feed_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CancelFeedResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CancelFeedResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CancelFeedResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CancelFeedResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CancelFeedResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CancelFeedResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = CancelFeedResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = CancelFeedResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CancelFeedResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = CancelFeedResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CancelFeedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feed_id: str,
    *,
    client: Client,
) -> Response[CancelFeedResponse]:
    """Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled.
    Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFeedResponse]
    """

    kwargs = _get_kwargs(
        feed_id=feed_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feed_id: str,
    *,
    client: Client,
) -> Optional[CancelFeedResponse]:
    """Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled.
    Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFeedResponse]
    """

    return sync_detailed(
        feed_id=feed_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    feed_id: str,
    *,
    client: Client,
) -> Response[CancelFeedResponse]:
    """Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled.
    Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFeedResponse]
    """

    kwargs = _get_kwargs(
        feed_id=feed_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feed_id: str,
    *,
    client: Client,
) -> Optional[CancelFeedResponse]:
    """Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled.
    Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feed_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFeedResponse]
    """

    return (
        await asyncio_detailed(
            feed_id=feed_id,
            client=client,
        )
    ).parsed
