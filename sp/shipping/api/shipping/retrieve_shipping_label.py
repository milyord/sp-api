from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.retrieve_shipping_label_request import RetrieveShippingLabelRequest
from ...models.retrieve_shipping_label_response import RetrieveShippingLabelResponse
from ...types import Response


def _get_kwargs(
    shipment_id: str,
    tracking_id: str,
    *,
    client: Client,
    json_body: RetrieveShippingLabelRequest,
) -> Dict[str, Any]:
    url = "{}/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label".format(
        client.base_url, shipmentId=shipment_id, trackingId=tracking_id
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RetrieveShippingLabelResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = RetrieveShippingLabelResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RetrieveShippingLabelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shipment_id: str,
    tracking_id: str,
    *,
    client: Client,
    json_body: RetrieveShippingLabelRequest,
) -> Response[RetrieveShippingLabelResponse]:
    """Retrieve shipping label based on the shipment id and tracking id.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        tracking_id (str):
        json_body (RetrieveShippingLabelRequest): The request schema for the retrieveShippingLabel
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveShippingLabelResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        tracking_id=tracking_id,
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
    shipment_id: str,
    tracking_id: str,
    *,
    client: Client,
    json_body: RetrieveShippingLabelRequest,
) -> Optional[RetrieveShippingLabelResponse]:
    """Retrieve shipping label based on the shipment id and tracking id.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        tracking_id (str):
        json_body (RetrieveShippingLabelRequest): The request schema for the retrieveShippingLabel
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveShippingLabelResponse]
    """

    return sync_detailed(
        shipment_id=shipment_id,
        tracking_id=tracking_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    shipment_id: str,
    tracking_id: str,
    *,
    client: Client,
    json_body: RetrieveShippingLabelRequest,
) -> Response[RetrieveShippingLabelResponse]:
    """Retrieve shipping label based on the shipment id and tracking id.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        tracking_id (str):
        json_body (RetrieveShippingLabelRequest): The request schema for the retrieveShippingLabel
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveShippingLabelResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        tracking_id=tracking_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shipment_id: str,
    tracking_id: str,
    *,
    client: Client,
    json_body: RetrieveShippingLabelRequest,
) -> Optional[RetrieveShippingLabelResponse]:
    """Retrieve shipping label based on the shipment id and tracking id.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        tracking_id (str):
        json_body (RetrieveShippingLabelRequest): The request schema for the retrieveShippingLabel
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveShippingLabelResponse]
    """

    return (
        await asyncio_detailed(
            shipment_id=shipment_id,
            tracking_id=tracking_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
