from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_product_review_and_seller_feedback_solicitation_response import (
    CreateProductReviewAndSellerFeedbackSolicitationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    amazon_order_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
) -> Dict[str, Any]:
    url = "{}/solicitations/v1/orders/{amazonOrderId}/solicitations/productReviewAndSellerFeedback".format(
        client.base_url, amazonOrderId=amazon_order_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CreateProductReviewAndSellerFeedbackSolicitationResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = CreateProductReviewAndSellerFeedbackSolicitationResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]:
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
    marketplace_ids: List[str],
) -> Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]:
    """Sends a solicitation to a buyer asking for seller feedback and a product review for the specified
    order. Send only one productReviewAndSellerFeedback or free form proactive message per order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]
    """

    kwargs = _get_kwargs(
        amazon_order_id=amazon_order_id,
        client=client,
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
    marketplace_ids: List[str],
) -> Optional[CreateProductReviewAndSellerFeedbackSolicitationResponse]:
    """Sends a solicitation to a buyer asking for seller feedback and a product review for the specified
    order. Send only one productReviewAndSellerFeedback or free form proactive message per order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]
    """

    return sync_detailed(
        amazon_order_id=amazon_order_id,
        client=client,
        marketplace_ids=marketplace_ids,
    ).parsed


async def asyncio_detailed(
    amazon_order_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
) -> Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]:
    """Sends a solicitation to a buyer asking for seller feedback and a product review for the specified
    order. Send only one productReviewAndSellerFeedback or free form proactive message per order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]
    """

    kwargs = _get_kwargs(
        amazon_order_id=amazon_order_id,
        client=client,
        marketplace_ids=marketplace_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    amazon_order_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
) -> Optional[CreateProductReviewAndSellerFeedbackSolicitationResponse]:
    """Sends a solicitation to a buyer asking for seller feedback and a product review for the specified
    order. Send only one productReviewAndSellerFeedback or free form proactive message per order.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        amazon_order_id (str):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductReviewAndSellerFeedbackSolicitationResponse]
    """

    return (
        await asyncio_detailed(
            amazon_order_id=amazon_order_id,
            client=client,
            marketplace_ids=marketplace_ids,
        )
    ).parsed
