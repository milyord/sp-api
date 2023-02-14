from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.set_appointment_fulfillment_data_request import SetAppointmentFulfillmentDataRequest
from ...types import Response


def _get_kwargs(
    service_job_id: str,
    appointment_id: str,
    *,
    client: Client,
    json_body: SetAppointmentFulfillmentDataRequest,
) -> Dict[str, Any]:
    url = "{}/service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId}/fulfillment".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[List["Error"], str]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(str, response.json())
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = []
        _response_400 = response.json()
        for componentsschemas_error_list_item_data in _response_400:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_400.append(componentsschemas_error_list_item)

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = []
        _response_403 = response.json()
        for componentsschemas_error_list_item_data in _response_403:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_403.append(componentsschemas_error_list_item)

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = []
        _response_404 = response.json()
        for componentsschemas_error_list_item_data in _response_404:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_404.append(componentsschemas_error_list_item)

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = []
        _response_413 = response.json()
        for componentsschemas_error_list_item_data in _response_413:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_413.append(componentsschemas_error_list_item)

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = []
        _response_415 = response.json()
        for componentsschemas_error_list_item_data in _response_415:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_415.append(componentsschemas_error_list_item)

        return response_415
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = []
        _response_422 = response.json()
        for componentsschemas_error_list_item_data in _response_422:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_422.append(componentsschemas_error_list_item)

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = []
        _response_429 = response.json()
        for componentsschemas_error_list_item_data in _response_429:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_429.append(componentsschemas_error_list_item)

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = []
        _response_500 = response.json()
        for componentsschemas_error_list_item_data in _response_500:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_500.append(componentsschemas_error_list_item)

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = []
        _response_503 = response.json()
        for componentsschemas_error_list_item_data in _response_503:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_503.append(componentsschemas_error_list_item)

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[List["Error"], str]]:
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
    json_body: SetAppointmentFulfillmentDataRequest,
) -> Response[Union[List["Error"], str]]:
    """Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.

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
        appointment_id (str):
        json_body (SetAppointmentFulfillmentDataRequest): Input for set appointment fulfillment
            data operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], str]]
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
    json_body: SetAppointmentFulfillmentDataRequest,
) -> Optional[Union[List["Error"], str]]:
    """Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.

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
        appointment_id (str):
        json_body (SetAppointmentFulfillmentDataRequest): Input for set appointment fulfillment
            data operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], str]]
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
    json_body: SetAppointmentFulfillmentDataRequest,
) -> Response[Union[List["Error"], str]]:
    """Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.

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
        appointment_id (str):
        json_body (SetAppointmentFulfillmentDataRequest): Input for set appointment fulfillment
            data operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], str]]
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
    json_body: SetAppointmentFulfillmentDataRequest,
) -> Optional[Union[List["Error"], str]]:
    """Updates the appointment fulfillment data related to a given `jobID` and `appointmentID`.

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
        appointment_id (str):
        json_body (SetAppointmentFulfillmentDataRequest): Input for set appointment fulfillment
            data operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], str]]
    """

    return (
        await asyncio_detailed(
            service_job_id=service_job_id,
            appointment_id=appointment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
