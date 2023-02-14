from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.list_handover_slots_request import ListHandoverSlotsRequest
from ...models.list_handover_slots_response import ListHandoverSlotsResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ListHandoverSlotsRequest,
) -> Dict[str, Any]:
    url = "{}/easyShip/2022-03-23/timeSlot".format(client.base_url)

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorList, ListHandoverSlotsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListHandoverSlotsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorList.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorList.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = ErrorList.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ErrorList.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorList.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ErrorList.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorList, ListHandoverSlotsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ListHandoverSlotsRequest,
) -> Response[Union[ErrorList, ListHandoverSlotsResponse]]:
    """Returns time slots available for Easy Ship orders to be scheduled based on the package weight and
    dimensions that the seller specifies.

    This operation is available for scheduled and unscheduled orders based on marketplace support. See
    **Get Time Slots** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-
    guide#marketplace-support-table).

    This operation can return time slots that have either pickup or drop-off handover methods - see
    **Supported Handover Methods** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table).

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
        json_body (ListHandoverSlotsRequest): The request schema for the `listHandoverSlots`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListHandoverSlotsResponse]]
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
    json_body: ListHandoverSlotsRequest,
) -> Optional[Union[ErrorList, ListHandoverSlotsResponse]]:
    """Returns time slots available for Easy Ship orders to be scheduled based on the package weight and
    dimensions that the seller specifies.

    This operation is available for scheduled and unscheduled orders based on marketplace support. See
    **Get Time Slots** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-
    guide#marketplace-support-table).

    This operation can return time slots that have either pickup or drop-off handover methods - see
    **Supported Handover Methods** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table).

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
        json_body (ListHandoverSlotsRequest): The request schema for the `listHandoverSlots`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListHandoverSlotsResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ListHandoverSlotsRequest,
) -> Response[Union[ErrorList, ListHandoverSlotsResponse]]:
    """Returns time slots available for Easy Ship orders to be scheduled based on the package weight and
    dimensions that the seller specifies.

    This operation is available for scheduled and unscheduled orders based on marketplace support. See
    **Get Time Slots** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-
    guide#marketplace-support-table).

    This operation can return time slots that have either pickup or drop-off handover methods - see
    **Supported Handover Methods** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table).

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
        json_body (ListHandoverSlotsRequest): The request schema for the `listHandoverSlots`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListHandoverSlotsResponse]]
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
    json_body: ListHandoverSlotsRequest,
) -> Optional[Union[ErrorList, ListHandoverSlotsResponse]]:
    """Returns time slots available for Easy Ship orders to be scheduled based on the package weight and
    dimensions that the seller specifies.

    This operation is available for scheduled and unscheduled orders based on marketplace support. See
    **Get Time Slots** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-
    guide#marketplace-support-table).

    This operation can return time slots that have either pickup or drop-off handover methods - see
    **Supported Handover Methods** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table).

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
        json_body (ListHandoverSlotsRequest): The request schema for the `listHandoverSlots`
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListHandoverSlotsResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
