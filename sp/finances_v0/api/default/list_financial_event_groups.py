import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_financial_event_groups_response import ListFinancialEventGroupsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    financial_event_group_started_before: Union[Unset, None, datetime.datetime] = UNSET,
    financial_event_group_started_after: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/finances/v0/financialEventGroups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MaxResultsPerPage"] = max_results_per_page

    json_financial_event_group_started_before: Union[Unset, None, str] = UNSET
    if not isinstance(financial_event_group_started_before, Unset):
        json_financial_event_group_started_before = (
            financial_event_group_started_before.isoformat() if financial_event_group_started_before else None
        )

    params["FinancialEventGroupStartedBefore"] = json_financial_event_group_started_before

    json_financial_event_group_started_after: Union[Unset, None, str] = UNSET
    if not isinstance(financial_event_group_started_after, Unset):
        json_financial_event_group_started_after = (
            financial_event_group_started_after.isoformat() if financial_event_group_started_after else None
        )

    params["FinancialEventGroupStartedAfter"] = json_financial_event_group_started_after

    params["NextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListFinancialEventGroupsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ListFinancialEventGroupsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListFinancialEventGroupsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    financial_event_group_started_before: Union[Unset, None, datetime.datetime] = UNSET,
    financial_event_group_started_after: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[ListFinancialEventGroupsResponse]:
    """Returns financial event groups for a given date range.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        financial_event_group_started_before (Union[Unset, None, datetime.datetime]):
        financial_event_group_started_after (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventGroupsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        max_results_per_page=max_results_per_page,
        financial_event_group_started_before=financial_event_group_started_before,
        financial_event_group_started_after=financial_event_group_started_after,
        next_token=next_token,
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
    max_results_per_page: Union[Unset, None, int] = 100,
    financial_event_group_started_before: Union[Unset, None, datetime.datetime] = UNSET,
    financial_event_group_started_after: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[ListFinancialEventGroupsResponse]:
    """Returns financial event groups for a given date range.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        financial_event_group_started_before (Union[Unset, None, datetime.datetime]):
        financial_event_group_started_after (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventGroupsResponse]
    """

    return sync_detailed(
        client=client,
        max_results_per_page=max_results_per_page,
        financial_event_group_started_before=financial_event_group_started_before,
        financial_event_group_started_after=financial_event_group_started_after,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    financial_event_group_started_before: Union[Unset, None, datetime.datetime] = UNSET,
    financial_event_group_started_after: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[ListFinancialEventGroupsResponse]:
    """Returns financial event groups for a given date range.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        financial_event_group_started_before (Union[Unset, None, datetime.datetime]):
        financial_event_group_started_after (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventGroupsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        max_results_per_page=max_results_per_page,
        financial_event_group_started_before=financial_event_group_started_before,
        financial_event_group_started_after=financial_event_group_started_after,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    max_results_per_page: Union[Unset, None, int] = 100,
    financial_event_group_started_before: Union[Unset, None, datetime.datetime] = UNSET,
    financial_event_group_started_after: Union[Unset, None, datetime.datetime] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[ListFinancialEventGroupsResponse]:
    """Returns financial event groups for a given date range.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        max_results_per_page (Union[Unset, None, int]):  Default: 100.
        financial_event_group_started_before (Union[Unset, None, datetime.datetime]):
        financial_event_group_started_after (Union[Unset, None, datetime.datetime]):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFinancialEventGroupsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            max_results_per_page=max_results_per_page,
            financial_event_group_started_before=financial_event_group_started_before,
            financial_event_group_started_after=financial_event_group_started_after,
            next_token=next_token,
        )
    ).parsed
