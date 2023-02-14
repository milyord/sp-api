from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_order_approvals_response import GetOrderApprovalsResponse
from ...models.item_approval_status import ItemApprovalStatus
from ...models.item_approval_type import ItemApprovalType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orders/v0/orders/{orderId}/approvals".format(client.base_url, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["NextToken"] = next_token

    json_item_approval_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(item_approval_types, Unset):
        if item_approval_types is None:
            json_item_approval_types = None
        else:
            json_item_approval_types = []
            for item_approval_types_item_data in item_approval_types:
                item_approval_types_item = item_approval_types_item_data.value

                json_item_approval_types.append(item_approval_types_item)

    params["ItemApprovalTypes"] = json_item_approval_types

    json_item_approval_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(item_approval_status, Unset):
        if item_approval_status is None:
            json_item_approval_status = None
        else:
            json_item_approval_status = []
            for item_approval_status_item_data in item_approval_status:
                item_approval_status_item = item_approval_status_item_data.value

                json_item_approval_status.append(item_approval_status_item)

    params["ItemApprovalStatus"] = json_item_approval_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetOrderApprovalsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetOrderApprovalsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetOrderApprovalsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Response[GetOrderApprovalsResponse]:
    """Returns detailed order items approvals information for the order specified. If NextToken is
    provided, it's used to retrieve the next page of order items approvals.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 0.5 | 30 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderApprovalsResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        next_token=next_token,
        item_approval_types=item_approval_types,
        item_approval_status=item_approval_status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Optional[GetOrderApprovalsResponse]:
    """Returns detailed order items approvals information for the order specified. If NextToken is
    provided, it's used to retrieve the next page of order items approvals.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 0.5 | 30 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderApprovalsResponse]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        next_token=next_token,
        item_approval_types=item_approval_types,
        item_approval_status=item_approval_status,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Response[GetOrderApprovalsResponse]:
    """Returns detailed order items approvals information for the order specified. If NextToken is
    provided, it's used to retrieve the next page of order items approvals.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 0.5 | 30 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderApprovalsResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        client=client,
        next_token=next_token,
        item_approval_types=item_approval_types,
        item_approval_status=item_approval_status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: Client,
    next_token: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Optional[GetOrderApprovalsResponse]:
    """Returns detailed order items approvals information for the order specified. If NextToken is
    provided, it's used to retrieve the next page of order items approvals.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 0.5 | 30 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        order_id (str):
        next_token (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderApprovalsResponse]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            next_token=next_token,
            item_approval_types=item_approval_types,
            item_approval_status=item_approval_status,
        )
    ).parsed
