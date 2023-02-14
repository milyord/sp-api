from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_bill_of_lading_response import GetBillOfLadingResponse
from ...types import Response


def _get_kwargs(
    shipment_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/shipments/{shipmentId}/billOfLading".format(client.base_url, shipmentId=shipment_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetBillOfLadingResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetBillOfLadingResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetBillOfLadingResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetBillOfLadingResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetBillOfLadingResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetBillOfLadingResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetBillOfLadingResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetBillOfLadingResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetBillOfLadingResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetBillOfLadingResponse]:
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
) -> Response[GetBillOfLadingResponse]:
    """Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The
    getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-
    partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.

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
        Response[GetBillOfLadingResponse]
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
) -> Optional[GetBillOfLadingResponse]:
    """Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The
    getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-
    partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.

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
        Response[GetBillOfLadingResponse]
    """

    return sync_detailed(
        shipment_id=shipment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    shipment_id: str,
    *,
    client: Client,
) -> Response[GetBillOfLadingResponse]:
    """Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The
    getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-
    partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.

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
        Response[GetBillOfLadingResponse]
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
) -> Optional[GetBillOfLadingResponse]:
    """Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The
    getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-
    partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.

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
        Response[GetBillOfLadingResponse]
    """

    return (
        await asyncio_detailed(
            shipment_id=shipment_id,
            client=client,
        )
    ).parsed
