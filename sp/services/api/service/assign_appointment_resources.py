from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.assign_appointment_resources_request import AssignAppointmentResourcesRequest
from ...models.assign_appointment_resources_response import AssignAppointmentResourcesResponse
from ...types import Response


def _get_kwargs(
    service_job_id: str,
    appointment_id: str,
    *,
    client: Client,
    json_body: AssignAppointmentResourcesRequest,
) -> Dict[str, Any]:
    url = "{}/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/resources".format(
        client.base_url, serviceJobId=service_job_id, appointmentId=appointment_id
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[AssignAppointmentResourcesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = AssignAppointmentResourcesResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[AssignAppointmentResourcesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_job_id: str,
    appointment_id: str,
    *,
    client: Client,
    json_body: AssignAppointmentResourcesRequest,
) -> Response[AssignAppointmentResourcesResponse]:
    """Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_job_id (str):
        appointment_id (str):
        json_body (AssignAppointmentResourcesRequest): Request schema for the
            `assignAppointmentResources` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignAppointmentResourcesResponse]
    """

    kwargs = _get_kwargs(
        service_job_id=service_job_id,
        appointment_id=appointment_id,
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
    service_job_id: str,
    appointment_id: str,
    *,
    client: Client,
    json_body: AssignAppointmentResourcesRequest,
) -> Optional[AssignAppointmentResourcesResponse]:
    """Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_job_id (str):
        appointment_id (str):
        json_body (AssignAppointmentResourcesRequest): Request schema for the
            `assignAppointmentResources` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignAppointmentResourcesResponse]
    """

    return sync_detailed(
        service_job_id=service_job_id,
        appointment_id=appointment_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    service_job_id: str,
    appointment_id: str,
    *,
    client: Client,
    json_body: AssignAppointmentResourcesRequest,
) -> Response[AssignAppointmentResourcesResponse]:
    """Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_job_id (str):
        appointment_id (str):
        json_body (AssignAppointmentResourcesRequest): Request schema for the
            `assignAppointmentResources` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignAppointmentResourcesResponse]
    """

    kwargs = _get_kwargs(
        service_job_id=service_job_id,
        appointment_id=appointment_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_job_id: str,
    appointment_id: str,
    *,
    client: Client,
    json_body: AssignAppointmentResourcesRequest,
) -> Optional[AssignAppointmentResourcesResponse]:
    """Assigns new resource(s) or overwrite/update the existing one(s) to a service job appointment.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_job_id (str):
        appointment_id (str):
        json_body (AssignAppointmentResourcesRequest): Request schema for the
            `assignAppointmentResources` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignAppointmentResourcesResponse]
    """

    return (
        await asyncio_detailed(
            service_job_id=service_job_id,
            appointment_id=appointment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
