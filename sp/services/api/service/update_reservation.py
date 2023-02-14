from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.update_reservation_request import UpdateReservationRequest
from ...models.update_reservation_response import UpdateReservationResponse
from ...types import UNSET, Response


def _get_kwargs(
    reservation_id: str,
    *,
    client: Client,
    json_body: UpdateReservationRequest,
    marketplace_ids: List[str],
) -> Dict[str, Any]:
    url = "{}/service/v1/reservation/{reservationId}".format(client.base_url, reservationId=reservation_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UpdateReservationResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateReservationResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateReservationResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = UpdateReservationResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = UpdateReservationResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = UpdateReservationResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = UpdateReservationResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = UpdateReservationResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = UpdateReservationResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = UpdateReservationResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UpdateReservationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reservation_id: str,
    *,
    client: Client,
    json_body: UpdateReservationRequest,
    marketplace_ids: List[str],
) -> Response[UpdateReservationResponse]:
    """Update a reservation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        reservation_id (str):
        marketplace_ids (List[str]):
        json_body (UpdateReservationRequest): Request schema for the `updateReservation`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateReservationResponse]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
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
    reservation_id: str,
    *,
    client: Client,
    json_body: UpdateReservationRequest,
    marketplace_ids: List[str],
) -> Optional[UpdateReservationResponse]:
    """Update a reservation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        reservation_id (str):
        marketplace_ids (List[str]):
        json_body (UpdateReservationRequest): Request schema for the `updateReservation`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateReservationResponse]
    """

    return sync_detailed(
        reservation_id=reservation_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
    ).parsed


async def asyncio_detailed(
    reservation_id: str,
    *,
    client: Client,
    json_body: UpdateReservationRequest,
    marketplace_ids: List[str],
) -> Response[UpdateReservationResponse]:
    """Update a reservation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        reservation_id (str):
        marketplace_ids (List[str]):
        json_body (UpdateReservationRequest): Request schema for the `updateReservation`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateReservationResponse]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reservation_id: str,
    *,
    client: Client,
    json_body: UpdateReservationRequest,
    marketplace_ids: List[str],
) -> Optional[UpdateReservationResponse]:
    """Update a reservation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        reservation_id (str):
        marketplace_ids (List[str]):
        json_body (UpdateReservationRequest): Request schema for the `updateReservation`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateReservationResponse]
    """

    return (
        await asyncio_detailed(
            reservation_id=reservation_id,
            client=client,
            json_body=json_body,
            marketplace_ids=marketplace_ids,
        )
    ).parsed
