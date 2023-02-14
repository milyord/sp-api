from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_scheduled_packages_request import CreateScheduledPackagesRequest
from ...models.create_scheduled_packages_response import CreateScheduledPackagesResponse
from ...models.error_list import ErrorList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateScheduledPackagesRequest,
) -> Dict[str, Any]:
    url = "{}/easyShip/2022-03-23/packages/bulk".format(client.base_url)

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
) -> Optional[Union[CreateScheduledPackagesResponse, ErrorList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateScheduledPackagesResponse.from_dict(response.json())

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
) -> Response[Union[CreateScheduledPackagesResponse, ErrorList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateScheduledPackagesRequest,
) -> Response[Union[CreateScheduledPackagesResponse, ErrorList]]:
    """This operation automatically schedules a time slot for all the `amazonOrderId`s given as input,
    generating the associated shipping labels, along with other compliance documents according to the
    marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table)).

    Developers calling this operation may optionally assign a `packageDetails` object, allowing them to
    input a preferred time slot for each order in ther request. In this case, Amazon will try to
    schedule the respective packages using their optional settings. On the other hand, *i.e.*, if the
    time slot is not provided, Amazon will then pick the earliest time slot possible.

    Regarding the shipping label's file format, external developers are able to choose between PDF or
    ZPL, and Amazon will create the label accordingly.

    This operation returns an array composed of the scheduled packages, and a short-lived URL pointing
    to a zip file containing the generated shipping labels and the other documents enabled for your
    marketplace. If at least an order couldn't be scheduled, then Amazon adds the `rejectedOrders` list
    into the response, which contains an entry for each order we couldn't process. Each entry is
    composed of an error message describing the reason of the failure, so that sellers can take action.

    The table below displays the supported request and burst maximum rates:

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
        json_body (CreateScheduledPackagesRequest): The request body for the POST
            /easyShip/2022-03-23/packages/bulk API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateScheduledPackagesResponse, ErrorList]]
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
    json_body: CreateScheduledPackagesRequest,
) -> Optional[Union[CreateScheduledPackagesResponse, ErrorList]]:
    """This operation automatically schedules a time slot for all the `amazonOrderId`s given as input,
    generating the associated shipping labels, along with other compliance documents according to the
    marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table)).

    Developers calling this operation may optionally assign a `packageDetails` object, allowing them to
    input a preferred time slot for each order in ther request. In this case, Amazon will try to
    schedule the respective packages using their optional settings. On the other hand, *i.e.*, if the
    time slot is not provided, Amazon will then pick the earliest time slot possible.

    Regarding the shipping label's file format, external developers are able to choose between PDF or
    ZPL, and Amazon will create the label accordingly.

    This operation returns an array composed of the scheduled packages, and a short-lived URL pointing
    to a zip file containing the generated shipping labels and the other documents enabled for your
    marketplace. If at least an order couldn't be scheduled, then Amazon adds the `rejectedOrders` list
    into the response, which contains an entry for each order we couldn't process. Each entry is
    composed of an error message describing the reason of the failure, so that sellers can take action.

    The table below displays the supported request and burst maximum rates:

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
        json_body (CreateScheduledPackagesRequest): The request body for the POST
            /easyShip/2022-03-23/packages/bulk API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateScheduledPackagesResponse, ErrorList]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateScheduledPackagesRequest,
) -> Response[Union[CreateScheduledPackagesResponse, ErrorList]]:
    """This operation automatically schedules a time slot for all the `amazonOrderId`s given as input,
    generating the associated shipping labels, along with other compliance documents according to the
    marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table)).

    Developers calling this operation may optionally assign a `packageDetails` object, allowing them to
    input a preferred time slot for each order in ther request. In this case, Amazon will try to
    schedule the respective packages using their optional settings. On the other hand, *i.e.*, if the
    time slot is not provided, Amazon will then pick the earliest time slot possible.

    Regarding the shipping label's file format, external developers are able to choose between PDF or
    ZPL, and Amazon will create the label accordingly.

    This operation returns an array composed of the scheduled packages, and a short-lived URL pointing
    to a zip file containing the generated shipping labels and the other documents enabled for your
    marketplace. If at least an order couldn't be scheduled, then Amazon adds the `rejectedOrders` list
    into the response, which contains an entry for each order we couldn't process. Each entry is
    composed of an error message describing the reason of the failure, so that sellers can take action.

    The table below displays the supported request and burst maximum rates:

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
        json_body (CreateScheduledPackagesRequest): The request body for the POST
            /easyShip/2022-03-23/packages/bulk API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateScheduledPackagesResponse, ErrorList]]
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
    json_body: CreateScheduledPackagesRequest,
) -> Optional[Union[CreateScheduledPackagesResponse, ErrorList]]:
    """This operation automatically schedules a time slot for all the `amazonOrderId`s given as input,
    generating the associated shipping labels, along with other compliance documents according to the
    marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-
    case-guide#marketplace-support-table)).

    Developers calling this operation may optionally assign a `packageDetails` object, allowing them to
    input a preferred time slot for each order in ther request. In this case, Amazon will try to
    schedule the respective packages using their optional settings. On the other hand, *i.e.*, if the
    time slot is not provided, Amazon will then pick the earliest time slot possible.

    Regarding the shipping label's file format, external developers are able to choose between PDF or
    ZPL, and Amazon will create the label accordingly.

    This operation returns an array composed of the scheduled packages, and a short-lived URL pointing
    to a zip file containing the generated shipping labels and the other documents enabled for your
    marketplace. If at least an order couldn't be scheduled, then Amazon adds the `rejectedOrders` list
    into the response, which contains an entry for each order we couldn't process. Each entry is
    composed of an error message describing the reason of the failure, so that sellers can take action.

    The table below displays the supported request and burst maximum rates:

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
        json_body (CreateScheduledPackagesRequest): The request body for the POST
            /easyShip/2022-03-23/packages/bulk API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateScheduledPackagesResponse, ErrorList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
