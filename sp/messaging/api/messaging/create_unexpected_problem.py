from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_unexpected_problem_request import CreateUnexpectedProblemRequest
from ...models.create_unexpected_problem_response import CreateUnexpectedProblemResponse
from ...types import UNSET, Response


def _get_kwargs(
    amazon_order_id: str,
    *,
    client: Client,
    json_body: CreateUnexpectedProblemRequest,
    marketplace_ids: List[str],
) -> Dict[str, Any]:
    url = "{}/messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem".format(
        client.base_url, amazonOrderId=amazon_order_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateUnexpectedProblemResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = CreateUnexpectedProblemResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateUnexpectedProblemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    amazon_order_id: str,
    *,
    client: Client,
    json_body: CreateUnexpectedProblemRequest,
    marketplace_ids: List[str],
) -> Response[CreateUnexpectedProblemResponse]:
    """Sends a critical message to a buyer that an unexpected problem was encountered affecting the
    completion of the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):
        json_body (CreateUnexpectedProblemRequest): The request schema for the
            createUnexpectedProblem operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUnexpectedProblemResponse]
    """

    kwargs = _get_kwargs(
        amazon_order_id=amazon_order_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    amazon_order_id: str,
    *,
    client: Client,
    json_body: CreateUnexpectedProblemRequest,
    marketplace_ids: List[str],
) -> Optional[CreateUnexpectedProblemResponse]:
    """Sends a critical message to a buyer that an unexpected problem was encountered affecting the
    completion of the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):
        json_body (CreateUnexpectedProblemRequest): The request schema for the
            createUnexpectedProblem operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUnexpectedProblemResponse]
    """

    return sync_detailed(
        amazon_order_id=amazon_order_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
    ).parsed


async def asyncio_detailed(
    amazon_order_id: str,
    *,
    client: Client,
    json_body: CreateUnexpectedProblemRequest,
    marketplace_ids: List[str],
) -> Response[CreateUnexpectedProblemResponse]:
    """Sends a critical message to a buyer that an unexpected problem was encountered affecting the
    completion of the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):
        json_body (CreateUnexpectedProblemRequest): The request schema for the
            createUnexpectedProblem operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUnexpectedProblemResponse]
    """

    kwargs = _get_kwargs(
        amazon_order_id=amazon_order_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    amazon_order_id: str,
    *,
    client: Client,
    json_body: CreateUnexpectedProblemRequest,
    marketplace_ids: List[str],
) -> Optional[CreateUnexpectedProblemResponse]:
    """Sends a critical message to a buyer that an unexpected problem was encountered affecting the
    completion of the order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):
        json_body (CreateUnexpectedProblemRequest): The request schema for the
            createUnexpectedProblem operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUnexpectedProblemResponse]
    """

    return (
        await asyncio_detailed(
            amazon_order_id=amazon_order_id,
            client=client,
            json_body=json_body,
            marketplace_ids=marketplace_ids,
        )
    ).parsed
