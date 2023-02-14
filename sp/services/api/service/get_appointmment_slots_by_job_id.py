from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_appointment_slots_response import GetAppointmentSlotsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_job_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    start_time: Union[Unset, None, str] = UNSET,
    end_time: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/service/v1/serviceJobs/{serviceJobId}/appointmentSlots".format(
        client.base_url, serviceJobId=service_job_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["startTime"] = start_time

    params["endTime"] = end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetAppointmentSlotsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetAppointmentSlotsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetAppointmentSlotsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_job_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    start_time: Union[Unset, None, str] = UNSET,
    end_time: Union[Unset, None, str] = UNSET,
) -> Response[GetAppointmentSlotsResponse]:
    """Gets appointment slots for the service associated with the service job id specified.

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
        service_job_id (str):
        marketplace_ids (List[str]):
        start_time (Union[Unset, None, str]):
        end_time (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppointmentSlotsResponse]
    """

    kwargs = _get_kwargs(
        service_job_id=service_job_id,
        client=client,
        marketplace_ids=marketplace_ids,
        start_time=start_time,
        end_time=end_time,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_job_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    start_time: Union[Unset, None, str] = UNSET,
    end_time: Union[Unset, None, str] = UNSET,
) -> Optional[GetAppointmentSlotsResponse]:
    """Gets appointment slots for the service associated with the service job id specified.

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
        service_job_id (str):
        marketplace_ids (List[str]):
        start_time (Union[Unset, None, str]):
        end_time (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppointmentSlotsResponse]
    """

    return sync_detailed(
        service_job_id=service_job_id,
        client=client,
        marketplace_ids=marketplace_ids,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    service_job_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    start_time: Union[Unset, None, str] = UNSET,
    end_time: Union[Unset, None, str] = UNSET,
) -> Response[GetAppointmentSlotsResponse]:
    """Gets appointment slots for the service associated with the service job id specified.

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
        service_job_id (str):
        marketplace_ids (List[str]):
        start_time (Union[Unset, None, str]):
        end_time (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppointmentSlotsResponse]
    """

    kwargs = _get_kwargs(
        service_job_id=service_job_id,
        client=client,
        marketplace_ids=marketplace_ids,
        start_time=start_time,
        end_time=end_time,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_job_id: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    start_time: Union[Unset, None, str] = UNSET,
    end_time: Union[Unset, None, str] = UNSET,
) -> Optional[GetAppointmentSlotsResponse]:
    """Gets appointment slots for the service associated with the service job id specified.

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
        service_job_id (str):
        marketplace_ids (List[str]):
        start_time (Union[Unset, None, str]):
        end_time (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppointmentSlotsResponse]
    """

    return (
        await asyncio_detailed(
            service_job_id=service_job_id,
            client=client,
            marketplace_ids=marketplace_ids,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
