from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_service_jobs_response import GetServiceJobsResponse
from ...models.get_service_jobs_service_job_status_item import GetServiceJobsServiceJobStatusItem
from ...models.get_service_jobs_sort_field import GetServiceJobsSortField
from ...models.get_service_jobs_sort_order import GetServiceJobsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    service_order_ids: Union[Unset, None, List[str]] = UNSET,
    service_job_status: Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 20,
    sort_field: Union[Unset, None, GetServiceJobsSortField] = UNSET,
    sort_order: Union[Unset, None, GetServiceJobsSortOrder] = UNSET,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    schedule_start_date: Union[Unset, None, str] = UNSET,
    schedule_end_date: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    asins: Union[Unset, None, List[str]] = UNSET,
    required_skills: Union[Unset, None, List[str]] = UNSET,
    store_ids: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/service/v1/serviceJobs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_service_order_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(service_order_ids, Unset):
        if service_order_ids is None:
            json_service_order_ids = None
        else:
            json_service_order_ids = service_order_ids

    params["serviceOrderIds"] = json_service_order_ids

    json_service_job_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(service_job_status, Unset):
        if service_job_status is None:
            json_service_job_status = None
        else:
            json_service_job_status = []
            for service_job_status_item_data in service_job_status:
                service_job_status_item = service_job_status_item_data.value

                json_service_job_status.append(service_job_status_item)

    params["serviceJobStatus"] = json_service_job_status

    params["pageToken"] = page_token

    params["pageSize"] = page_size

    json_sort_field: Union[Unset, None, str] = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value if sort_field else None

    params["sortField"] = json_sort_field

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params["createdAfter"] = created_after

    params["createdBefore"] = created_before

    params["lastUpdatedAfter"] = last_updated_after

    params["lastUpdatedBefore"] = last_updated_before

    params["scheduleStartDate"] = schedule_start_date

    params["scheduleEndDate"] = schedule_end_date

    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    json_asins: Union[Unset, None, List[str]] = UNSET
    if not isinstance(asins, Unset):
        if asins is None:
            json_asins = None
        else:
            json_asins = asins

    params["asins"] = json_asins

    json_required_skills: Union[Unset, None, List[str]] = UNSET
    if not isinstance(required_skills, Unset):
        if required_skills is None:
            json_required_skills = None
        else:
            json_required_skills = required_skills

    params["requiredSkills"] = json_required_skills

    json_store_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(store_ids, Unset):
        if store_ids is None:
            json_store_ids = None
        else:
            json_store_ids = store_ids

    params["storeIds"] = json_store_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetServiceJobsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetServiceJobsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetServiceJobsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetServiceJobsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetServiceJobsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = GetServiceJobsResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetServiceJobsResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetServiceJobsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetServiceJobsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetServiceJobsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetServiceJobsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    service_order_ids: Union[Unset, None, List[str]] = UNSET,
    service_job_status: Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 20,
    sort_field: Union[Unset, None, GetServiceJobsSortField] = UNSET,
    sort_order: Union[Unset, None, GetServiceJobsSortOrder] = UNSET,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    schedule_start_date: Union[Unset, None, str] = UNSET,
    schedule_end_date: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    asins: Union[Unset, None, List[str]] = UNSET,
    required_skills: Union[Unset, None, List[str]] = UNSET,
    store_ids: Union[Unset, None, List[str]] = UNSET,
) -> Response[GetServiceJobsResponse]:
    """Gets service job details for the specified filter query.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 40 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_order_ids (Union[Unset, None, List[str]]):
        service_job_status (Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]]):
        page_token (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 20.
        sort_field (Union[Unset, None, GetServiceJobsSortField]):
        sort_order (Union[Unset, None, GetServiceJobsSortOrder]):
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        schedule_start_date (Union[Unset, None, str]):
        schedule_end_date (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        asins (Union[Unset, None, List[str]]):
        required_skills (Union[Unset, None, List[str]]):
        store_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceJobsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        service_order_ids=service_order_ids,
        service_job_status=service_job_status,
        page_token=page_token,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
        created_after=created_after,
        created_before=created_before,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        schedule_start_date=schedule_start_date,
        schedule_end_date=schedule_end_date,
        marketplace_ids=marketplace_ids,
        asins=asins,
        required_skills=required_skills,
        store_ids=store_ids,
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
    service_order_ids: Union[Unset, None, List[str]] = UNSET,
    service_job_status: Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 20,
    sort_field: Union[Unset, None, GetServiceJobsSortField] = UNSET,
    sort_order: Union[Unset, None, GetServiceJobsSortOrder] = UNSET,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    schedule_start_date: Union[Unset, None, str] = UNSET,
    schedule_end_date: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    asins: Union[Unset, None, List[str]] = UNSET,
    required_skills: Union[Unset, None, List[str]] = UNSET,
    store_ids: Union[Unset, None, List[str]] = UNSET,
) -> Optional[GetServiceJobsResponse]:
    """Gets service job details for the specified filter query.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 40 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_order_ids (Union[Unset, None, List[str]]):
        service_job_status (Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]]):
        page_token (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 20.
        sort_field (Union[Unset, None, GetServiceJobsSortField]):
        sort_order (Union[Unset, None, GetServiceJobsSortOrder]):
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        schedule_start_date (Union[Unset, None, str]):
        schedule_end_date (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        asins (Union[Unset, None, List[str]]):
        required_skills (Union[Unset, None, List[str]]):
        store_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceJobsResponse]
    """

    return sync_detailed(
        client=client,
        service_order_ids=service_order_ids,
        service_job_status=service_job_status,
        page_token=page_token,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
        created_after=created_after,
        created_before=created_before,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        schedule_start_date=schedule_start_date,
        schedule_end_date=schedule_end_date,
        marketplace_ids=marketplace_ids,
        asins=asins,
        required_skills=required_skills,
        store_ids=store_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    service_order_ids: Union[Unset, None, List[str]] = UNSET,
    service_job_status: Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 20,
    sort_field: Union[Unset, None, GetServiceJobsSortField] = UNSET,
    sort_order: Union[Unset, None, GetServiceJobsSortOrder] = UNSET,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    schedule_start_date: Union[Unset, None, str] = UNSET,
    schedule_end_date: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    asins: Union[Unset, None, List[str]] = UNSET,
    required_skills: Union[Unset, None, List[str]] = UNSET,
    store_ids: Union[Unset, None, List[str]] = UNSET,
) -> Response[GetServiceJobsResponse]:
    """Gets service job details for the specified filter query.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 40 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_order_ids (Union[Unset, None, List[str]]):
        service_job_status (Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]]):
        page_token (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 20.
        sort_field (Union[Unset, None, GetServiceJobsSortField]):
        sort_order (Union[Unset, None, GetServiceJobsSortOrder]):
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        schedule_start_date (Union[Unset, None, str]):
        schedule_end_date (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        asins (Union[Unset, None, List[str]]):
        required_skills (Union[Unset, None, List[str]]):
        store_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceJobsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        service_order_ids=service_order_ids,
        service_job_status=service_job_status,
        page_token=page_token,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
        created_after=created_after,
        created_before=created_before,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        schedule_start_date=schedule_start_date,
        schedule_end_date=schedule_end_date,
        marketplace_ids=marketplace_ids,
        asins=asins,
        required_skills=required_skills,
        store_ids=store_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    service_order_ids: Union[Unset, None, List[str]] = UNSET,
    service_job_status: Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 20,
    sort_field: Union[Unset, None, GetServiceJobsSortField] = UNSET,
    sort_order: Union[Unset, None, GetServiceJobsSortOrder] = UNSET,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    schedule_start_date: Union[Unset, None, str] = UNSET,
    schedule_end_date: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    asins: Union[Unset, None, List[str]] = UNSET,
    required_skills: Union[Unset, None, List[str]] = UNSET,
    store_ids: Union[Unset, None, List[str]] = UNSET,
) -> Optional[GetServiceJobsResponse]:
    """Gets service job details for the specified filter query.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 40 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        service_order_ids (Union[Unset, None, List[str]]):
        service_job_status (Union[Unset, None, List[GetServiceJobsServiceJobStatusItem]]):
        page_token (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 20.
        sort_field (Union[Unset, None, GetServiceJobsSortField]):
        sort_order (Union[Unset, None, GetServiceJobsSortOrder]):
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        schedule_start_date (Union[Unset, None, str]):
        schedule_end_date (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        asins (Union[Unset, None, List[str]]):
        required_skills (Union[Unset, None, List[str]]):
        store_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceJobsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            service_order_ids=service_order_ids,
            service_job_status=service_job_status,
            page_token=page_token,
            page_size=page_size,
            sort_field=sort_field,
            sort_order=sort_order,
            created_after=created_after,
            created_before=created_before,
            last_updated_after=last_updated_after,
            last_updated_before=last_updated_before,
            schedule_start_date=schedule_start_date,
            schedule_end_date=schedule_end_date,
            marketplace_ids=marketplace_ids,
            asins=asins,
            required_skills=required_skills,
            store_ids=store_ids,
        )
    ).parsed
