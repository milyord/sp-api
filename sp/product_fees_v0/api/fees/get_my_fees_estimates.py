from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.fees_estimate_by_id_request import FeesEstimateByIdRequest
from ...models.fees_estimate_result import FeesEstimateResult
from ...models.get_my_fees_estimates_error_list import GetMyFeesEstimatesErrorList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: List["FeesEstimateByIdRequest"],
) -> Dict[str, Any]:
    url = "{}/products/fees/v0/feesEstimate".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for componentsschemas_get_my_fees_estimates_request_item_data in json_body:
        componentsschemas_get_my_fees_estimates_request_item = (
            componentsschemas_get_my_fees_estimates_request_item_data.to_dict()
        )

        json_json_body.append(componentsschemas_get_my_fees_estimates_request_item)

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
) -> Optional[Union[GetMyFeesEstimatesErrorList, List["FeesEstimateResult"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_get_my_fees_estimates_response_item_data in _response_200:
            componentsschemas_get_my_fees_estimates_response_item = FeesEstimateResult.from_dict(
                componentsschemas_get_my_fees_estimates_response_item_data
            )

            response_200.append(componentsschemas_get_my_fees_estimates_response_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetMyFeesEstimatesErrorList.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[GetMyFeesEstimatesErrorList, List["FeesEstimateResult"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List["FeesEstimateByIdRequest"],
) -> Response[Union[GetMyFeesEstimatesErrorList, List["FeesEstimateResult"]]]:
    """Returns the estimated fees for a list of products.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (List['FeesEstimateByIdRequest']): Request for estimated fees for a list of
            products.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMyFeesEstimatesErrorList, List['FeesEstimateResult']]]
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
    json_body: List["FeesEstimateByIdRequest"],
) -> Optional[Union[GetMyFeesEstimatesErrorList, List["FeesEstimateResult"]]]:
    """Returns the estimated fees for a list of products.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (List['FeesEstimateByIdRequest']): Request for estimated fees for a list of
            products.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMyFeesEstimatesErrorList, List['FeesEstimateResult']]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List["FeesEstimateByIdRequest"],
) -> Response[Union[GetMyFeesEstimatesErrorList, List["FeesEstimateResult"]]]:
    """Returns the estimated fees for a list of products.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (List['FeesEstimateByIdRequest']): Request for estimated fees for a list of
            products.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMyFeesEstimatesErrorList, List['FeesEstimateResult']]]
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
    json_body: List["FeesEstimateByIdRequest"],
) -> Optional[Union[GetMyFeesEstimatesErrorList, List["FeesEstimateResult"]]]:
    """Returns the estimated fees for a list of products.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (List['FeesEstimateByIdRequest']): Request for estimated fees for a list of
            products.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMyFeesEstimatesErrorList, List['FeesEstimateResult']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
