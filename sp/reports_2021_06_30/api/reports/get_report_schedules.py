from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.report_schedule_list import ReportScheduleList
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    report_types: List[str],
) -> Dict[str, Any]:
    url = "{}/reports/2021-06-30/schedules".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_report_types = report_types

    params["reportTypes"] = json_report_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, ReportScheduleList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReportScheduleList.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, ReportScheduleList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    report_types: List[str],
) -> Response[Union[ErrorList, ReportScheduleList]]:
    """Returns report schedule details that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-
    and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

    Args:
        report_types (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ReportScheduleList]]
    """

    kwargs = _get_kwargs(
        client=client,
        report_types=report_types,
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
    report_types: List[str],
) -> Optional[Union[ErrorList, ReportScheduleList]]:
    """Returns report schedule details that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-
    and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

    Args:
        report_types (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ReportScheduleList]]
    """

    return sync_detailed(
        client=client,
        report_types=report_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    report_types: List[str],
) -> Response[Union[ErrorList, ReportScheduleList]]:
    """Returns report schedule details that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-
    and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

    Args:
        report_types (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ReportScheduleList]]
    """

    kwargs = _get_kwargs(
        client=client,
        report_types=report_types,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    report_types: List[str],
) -> Optional[Union[ErrorList, ReportScheduleList]]:
    """Returns report schedule details that match the filters that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0222 | 10 |

    For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-
    and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.

    Args:
        report_types (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ReportScheduleList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            report_types=report_types,
        )
    ).parsed
