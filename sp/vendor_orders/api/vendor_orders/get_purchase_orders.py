import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_purchase_orders_po_item_state import GetPurchaseOrdersPoItemState
from ...models.get_purchase_orders_purchase_order_state import GetPurchaseOrdersPurchaseOrderState
from ...models.get_purchase_orders_response import GetPurchaseOrdersResponse
from ...models.get_purchase_orders_sort_order import GetPurchaseOrdersSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    po_item_state: Union[Unset, None, GetPurchaseOrdersPoItemState] = UNSET,
    is_po_changed: Union[Unset, None, str] = UNSET,
    purchase_order_state: Union[Unset, None, GetPurchaseOrdersPurchaseOrderState] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vendor/orders/v1/purchaseOrders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    json_created_after: Union[Unset, None, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat() if created_after else None

    params["createdAfter"] = json_created_after

    json_created_before: Union[Unset, None, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat() if created_before else None

    params["createdBefore"] = json_created_before

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params["nextToken"] = next_token

    params["includeDetails"] = include_details

    json_changed_after: Union[Unset, None, str] = UNSET
    if not isinstance(changed_after, Unset):
        json_changed_after = changed_after.isoformat() if changed_after else None

    params["changedAfter"] = json_changed_after

    json_changed_before: Union[Unset, None, str] = UNSET
    if not isinstance(changed_before, Unset):
        json_changed_before = changed_before.isoformat() if changed_before else None

    params["changedBefore"] = json_changed_before

    json_po_item_state: Union[Unset, None, str] = UNSET
    if not isinstance(po_item_state, Unset):
        json_po_item_state = po_item_state.value if po_item_state else None

    params["poItemState"] = json_po_item_state

    params["isPOChanged"] = is_po_changed

    json_purchase_order_state: Union[Unset, None, str] = UNSET
    if not isinstance(purchase_order_state, Unset):
        json_purchase_order_state = purchase_order_state.value if purchase_order_state else None

    params["purchaseOrderState"] = json_purchase_order_state

    params["orderingVendorCode"] = ordering_vendor_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetPurchaseOrdersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetPurchaseOrdersResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetPurchaseOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    po_item_state: Union[Unset, None, GetPurchaseOrdersPoItemState] = UNSET,
    is_po_changed: Union[Unset, None, str] = UNSET,
    purchase_order_state: Union[Unset, None, GetPurchaseOrdersPurchaseOrderState] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
) -> Response[GetPurchaseOrdersResponse]:
    """Returns a list of purchase orders created or changed during the time frame that you specify. You
    define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore
    parameters. The date range to search must not be more than 7 days. You can choose to get only the
    purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder
    operation to receive details for a specific purchase order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        limit (Union[Unset, None, int]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        sort_order (Union[Unset, None, GetPurchaseOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):
        changed_after (Union[Unset, None, datetime.datetime]):
        changed_before (Union[Unset, None, datetime.datetime]):
        po_item_state (Union[Unset, None, GetPurchaseOrdersPoItemState]):
        is_po_changed (Union[Unset, None, str]):
        purchase_order_state (Union[Unset, None, GetPurchaseOrdersPurchaseOrderState]):
        ordering_vendor_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
        include_details=include_details,
        changed_after=changed_after,
        changed_before=changed_before,
        po_item_state=po_item_state,
        is_po_changed=is_po_changed,
        purchase_order_state=purchase_order_state,
        ordering_vendor_code=ordering_vendor_code,
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
    limit: Union[Unset, None, int] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    po_item_state: Union[Unset, None, GetPurchaseOrdersPoItemState] = UNSET,
    is_po_changed: Union[Unset, None, str] = UNSET,
    purchase_order_state: Union[Unset, None, GetPurchaseOrdersPurchaseOrderState] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
) -> Optional[GetPurchaseOrdersResponse]:
    """Returns a list of purchase orders created or changed during the time frame that you specify. You
    define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore
    parameters. The date range to search must not be more than 7 days. You can choose to get only the
    purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder
    operation to receive details for a specific purchase order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        limit (Union[Unset, None, int]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        sort_order (Union[Unset, None, GetPurchaseOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):
        changed_after (Union[Unset, None, datetime.datetime]):
        changed_before (Union[Unset, None, datetime.datetime]):
        po_item_state (Union[Unset, None, GetPurchaseOrdersPoItemState]):
        is_po_changed (Union[Unset, None, str]):
        purchase_order_state (Union[Unset, None, GetPurchaseOrdersPurchaseOrderState]):
        ordering_vendor_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
        include_details=include_details,
        changed_after=changed_after,
        changed_before=changed_before,
        po_item_state=po_item_state,
        is_po_changed=is_po_changed,
        purchase_order_state=purchase_order_state,
        ordering_vendor_code=ordering_vendor_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    po_item_state: Union[Unset, None, GetPurchaseOrdersPoItemState] = UNSET,
    is_po_changed: Union[Unset, None, str] = UNSET,
    purchase_order_state: Union[Unset, None, GetPurchaseOrdersPurchaseOrderState] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
) -> Response[GetPurchaseOrdersResponse]:
    """Returns a list of purchase orders created or changed during the time frame that you specify. You
    define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore
    parameters. The date range to search must not be more than 7 days. You can choose to get only the
    purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder
    operation to receive details for a specific purchase order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        limit (Union[Unset, None, int]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        sort_order (Union[Unset, None, GetPurchaseOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):
        changed_after (Union[Unset, None, datetime.datetime]):
        changed_before (Union[Unset, None, datetime.datetime]):
        po_item_state (Union[Unset, None, GetPurchaseOrdersPoItemState]):
        is_po_changed (Union[Unset, None, str]):
        purchase_order_state (Union[Unset, None, GetPurchaseOrdersPurchaseOrderState]):
        ordering_vendor_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        next_token=next_token,
        include_details=include_details,
        changed_after=changed_after,
        changed_before=changed_before,
        po_item_state=po_item_state,
        is_po_changed=is_po_changed,
        purchase_order_state=purchase_order_state,
        ordering_vendor_code=ordering_vendor_code,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    include_details: Union[Unset, None, str] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    po_item_state: Union[Unset, None, GetPurchaseOrdersPoItemState] = UNSET,
    is_po_changed: Union[Unset, None, str] = UNSET,
    purchase_order_state: Union[Unset, None, GetPurchaseOrdersPurchaseOrderState] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
) -> Optional[GetPurchaseOrdersResponse]:
    """Returns a list of purchase orders created or changed during the time frame that you specify. You
    define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore
    parameters. The date range to search must not be more than 7 days. You can choose to get only the
    purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder
    operation to receive details for a specific purchase order.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        limit (Union[Unset, None, int]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        sort_order (Union[Unset, None, GetPurchaseOrdersSortOrder]):
        next_token (Union[Unset, None, str]):
        include_details (Union[Unset, None, str]):
        changed_after (Union[Unset, None, datetime.datetime]):
        changed_before (Union[Unset, None, datetime.datetime]):
        po_item_state (Union[Unset, None, GetPurchaseOrdersPoItemState]):
        is_po_changed (Union[Unset, None, str]):
        purchase_order_state (Union[Unset, None, GetPurchaseOrdersPurchaseOrderState]):
        ordering_vendor_code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            created_after=created_after,
            created_before=created_before,
            sort_order=sort_order,
            next_token=next_token,
            include_details=include_details,
            changed_after=changed_after,
            changed_before=changed_before,
            po_item_state=po_item_state,
            is_po_changed=is_po_changed,
            purchase_order_state=purchase_order_state,
            ordering_vendor_code=ordering_vendor_code,
        )
    ).parsed
