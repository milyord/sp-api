from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.confirm_transport_response import ConfirmTransportResponse
from ...types import Response


def _get_kwargs(
    shipment_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/shipments/{shipmentId}/transport/confirm".format(client.base_url, shipmentId=shipment_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ConfirmTransportResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ConfirmTransportResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ConfirmTransportResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ConfirmTransportResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ConfirmTransportResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ConfirmTransportResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ConfirmTransportResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ConfirmTransportResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ConfirmTransportResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ConfirmTransportResponse]:
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
) -> Response[ConfirmTransportResponse]:
    """Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to
    charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the
    inbound shipment.

    Prior to calling the confirmTransport operation, you should call the getTransportDetails operation
    to get the Amazon-partnered shipping estimate.

    Important: After confirming the transportation request, if the seller decides that they do not want
    the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation
    to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours
    after confirming a transportation request to void the transportation request. For a Less Than
    Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a
    transportation request to void it. After the grace period has expired the seller's account will be
    charged for the shipping cost.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmTransportResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        client=client,
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
) -> Optional[ConfirmTransportResponse]:
    """Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to
    charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the
    inbound shipment.

    Prior to calling the confirmTransport operation, you should call the getTransportDetails operation
    to get the Amazon-partnered shipping estimate.

    Important: After confirming the transportation request, if the seller decides that they do not want
    the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation
    to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours
    after confirming a transportation request to void the transportation request. For a Less Than
    Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a
    transportation request to void it. After the grace period has expired the seller's account will be
    charged for the shipping cost.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmTransportResponse]
    """

    return sync_detailed(
        shipment_id=shipment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    shipment_id: str,
    *,
    client: Client,
) -> Response[ConfirmTransportResponse]:
    """Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to
    charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the
    inbound shipment.

    Prior to calling the confirmTransport operation, you should call the getTransportDetails operation
    to get the Amazon-partnered shipping estimate.

    Important: After confirming the transportation request, if the seller decides that they do not want
    the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation
    to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours
    after confirming a transportation request to void the transportation request. For a Less Than
    Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a
    transportation request to void it. After the grace period has expired the seller's account will be
    charged for the shipping cost.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmTransportResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shipment_id: str,
    *,
    client: Client,
) -> Optional[ConfirmTransportResponse]:
    """Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to
    charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the
    inbound shipment.

    Prior to calling the confirmTransport operation, you should call the getTransportDetails operation
    to get the Amazon-partnered shipping estimate.

    Important: After confirming the transportation request, if the seller decides that they do not want
    the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation
    to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours
    after confirming a transportation request to void the transportation request. For a Less Than
    Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a
    transportation request to void it. After the grace period has expired the seller's account will be
    charged for the shipping cost.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmTransportResponse]
    """

    return (
        await asyncio_detailed(
            shipment_id=shipment_id,
            client=client,
        )
    ).parsed
