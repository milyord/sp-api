from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.purchase_shipment_request import PurchaseShipmentRequest
from ...models.purchase_shipment_response import PurchaseShipmentResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PurchaseShipmentRequest,
) -> Dict[str, Any]:
    url = "{}/shipping/v1/purchaseShipment".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PurchaseShipmentResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PurchaseShipmentResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PurchaseShipmentResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PurchaseShipmentResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = PurchaseShipmentResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PurchaseShipmentResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = PurchaseShipmentResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PurchaseShipmentResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = PurchaseShipmentResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PurchaseShipmentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PurchaseShipmentRequest,
) -> Response[PurchaseShipmentResponse]:
    """Purchase shipping labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (PurchaseShipmentRequest): The payload schema for the purchaseShipment
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseShipmentResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Client,
    json_body: PurchaseShipmentRequest,
) -> Optional[PurchaseShipmentResponse]:
    """Purchase shipping labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (PurchaseShipmentRequest): The payload schema for the purchaseShipment
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseShipmentResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PurchaseShipmentRequest,
) -> Response[PurchaseShipmentResponse]:
    """Purchase shipping labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (PurchaseShipmentRequest): The payload schema for the purchaseShipment
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseShipmentResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PurchaseShipmentRequest,
) -> Optional[PurchaseShipmentResponse]:
    """Purchase shipping labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (PurchaseShipmentRequest): The payload schema for the purchaseShipment
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseShipmentResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
