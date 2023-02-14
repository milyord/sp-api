from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.put_transport_details_request import PutTransportDetailsRequest
from ...models.put_transport_details_response import PutTransportDetailsResponse
from ...types import Response


def _get_kwargs(
    shipment_id: str,
    *,
    client: Client,
    json_body: PutTransportDetailsRequest,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/shipments/{shipmentId}/transport".format(client.base_url, shipmentId=shipment_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PutTransportDetailsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutTransportDetailsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PutTransportDetailsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PutTransportDetailsResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = PutTransportDetailsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PutTransportDetailsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = PutTransportDetailsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PutTransportDetailsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = PutTransportDetailsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PutTransportDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shipment_id: str,
    *,
    client: Client,
    json_body: PutTransportDetailsRequest,
) -> Response[PutTransportDetailsResponse]:
    """Sends transportation information to Amazon about an inbound shipment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        json_body (PutTransportDetailsRequest): The request schema for a putTransportDetails
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTransportDetailsResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
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
    *,
    client: Client,
    json_body: PutTransportDetailsRequest,
) -> Optional[PutTransportDetailsResponse]:
    """Sends transportation information to Amazon about an inbound shipment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        json_body (PutTransportDetailsRequest): The request schema for a putTransportDetails
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTransportDetailsResponse]
    """

    return sync_detailed(
        shipment_id=shipment_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    shipment_id: str,
    *,
    client: Client,
    json_body: PutTransportDetailsRequest,
) -> Response[PutTransportDetailsResponse]:
    """Sends transportation information to Amazon about an inbound shipment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        json_body (PutTransportDetailsRequest): The request schema for a putTransportDetails
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTransportDetailsResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shipment_id: str,
    *,
    client: Client,
    json_body: PutTransportDetailsRequest,
) -> Optional[PutTransportDetailsResponse]:
    """Sends transportation information to Amazon about an inbound shipment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        json_body (PutTransportDetailsRequest): The request schema for a putTransportDetails
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutTransportDetailsResponse]
    """

    return (
        await asyncio_detailed(
            shipment_id=shipment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
