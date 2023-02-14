import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_purchase_orders_status_item_confirmation_status import GetPurchaseOrdersStatusItemConfirmationStatus
from ...models.get_purchase_orders_status_item_receive_status import GetPurchaseOrdersStatusItemReceiveStatus
from ...models.get_purchase_orders_status_purchase_order_status import GetPurchaseOrdersStatusPurchaseOrderStatus
from ...models.get_purchase_orders_status_response import GetPurchaseOrdersStatusResponse
from ...models.get_purchase_orders_status_sort_order import GetPurchaseOrdersStatusSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersStatusSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    purchase_order_status: Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus] = UNSET,
    item_confirmation_status: Union[Unset, None, GetPurchaseOrdersStatusItemConfirmationStatus] = UNSET,
    item_receive_status: Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
    ship_to_party_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vendor/orders/v1/purchaseOrdersStatus".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params["nextToken"] = next_token

    json_created_after: Union[Unset, None, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat() if created_after else None

    params["createdAfter"] = json_created_after

    json_created_before: Union[Unset, None, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat() if created_before else None

    params["createdBefore"] = json_created_before

    json_updated_after: Union[Unset, None, str] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.isoformat() if updated_after else None

    params["updatedAfter"] = json_updated_after

    json_updated_before: Union[Unset, None, str] = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.isoformat() if updated_before else None

    params["updatedBefore"] = json_updated_before

    params["purchaseOrderNumber"] = purchase_order_number

    json_purchase_order_status: Union[Unset, None, str] = UNSET
    if not isinstance(purchase_order_status, Unset):
        json_purchase_order_status = purchase_order_status.value if purchase_order_status else None

    params["purchaseOrderStatus"] = json_purchase_order_status

    json_item_confirmation_status: Union[Unset, None, str] = UNSET
    if not isinstance(item_confirmation_status, Unset):
        json_item_confirmation_status = item_confirmation_status.value if item_confirmation_status else None

    params["itemConfirmationStatus"] = json_item_confirmation_status

    json_item_receive_status: Union[Unset, None, str] = UNSET
    if not isinstance(item_receive_status, Unset):
        json_item_receive_status = item_receive_status.value if item_receive_status else None

    params["itemReceiveStatus"] = json_item_receive_status

    params["orderingVendorCode"] = ordering_vendor_code

    params["shipToPartyId"] = ship_to_party_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetPurchaseOrdersStatusResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetPurchaseOrdersStatusResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetPurchaseOrdersStatusResponse]:
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
    sort_order: Union[Unset, None, GetPurchaseOrdersStatusSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    purchase_order_status: Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus] = UNSET,
    item_confirmation_status: Union[Unset, None, GetPurchaseOrdersStatusItemConfirmationStatus] = UNSET,
    item_receive_status: Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
    ship_to_party_id: Union[Unset, None, str] = UNSET,
) -> Response[GetPurchaseOrdersStatusResponse]:
    """Returns purchase order statuses based on the filters that you specify. Date range to search must not
    be more than 7 days. You can return a list of purchase order statuses using the available filters,
    or a single purchase order status by providing the purchase order number.

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
        sort_order (Union[Unset, None, GetPurchaseOrdersStatusSortOrder]):
        next_token (Union[Unset, None, str]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        purchase_order_number (Union[Unset, None, str]):
        purchase_order_status (Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus]):
        item_confirmation_status (Union[Unset, None,
            GetPurchaseOrdersStatusItemConfirmationStatus]):
        item_receive_status (Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus]):
        ordering_vendor_code (Union[Unset, None, str]):
        ship_to_party_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersStatusResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        sort_order=sort_order,
        next_token=next_token,
        created_after=created_after,
        created_before=created_before,
        updated_after=updated_after,
        updated_before=updated_before,
        purchase_order_number=purchase_order_number,
        purchase_order_status=purchase_order_status,
        item_confirmation_status=item_confirmation_status,
        item_receive_status=item_receive_status,
        ordering_vendor_code=ordering_vendor_code,
        ship_to_party_id=ship_to_party_id,
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
    sort_order: Union[Unset, None, GetPurchaseOrdersStatusSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    purchase_order_status: Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus] = UNSET,
    item_confirmation_status: Union[Unset, None, GetPurchaseOrdersStatusItemConfirmationStatus] = UNSET,
    item_receive_status: Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
    ship_to_party_id: Union[Unset, None, str] = UNSET,
) -> Optional[GetPurchaseOrdersStatusResponse]:
    """Returns purchase order statuses based on the filters that you specify. Date range to search must not
    be more than 7 days. You can return a list of purchase order statuses using the available filters,
    or a single purchase order status by providing the purchase order number.

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
        sort_order (Union[Unset, None, GetPurchaseOrdersStatusSortOrder]):
        next_token (Union[Unset, None, str]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        purchase_order_number (Union[Unset, None, str]):
        purchase_order_status (Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus]):
        item_confirmation_status (Union[Unset, None,
            GetPurchaseOrdersStatusItemConfirmationStatus]):
        item_receive_status (Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus]):
        ordering_vendor_code (Union[Unset, None, str]):
        ship_to_party_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersStatusResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        sort_order=sort_order,
        next_token=next_token,
        created_after=created_after,
        created_before=created_before,
        updated_after=updated_after,
        updated_before=updated_before,
        purchase_order_number=purchase_order_number,
        purchase_order_status=purchase_order_status,
        item_confirmation_status=item_confirmation_status,
        item_receive_status=item_receive_status,
        ordering_vendor_code=ordering_vendor_code,
        ship_to_party_id=ship_to_party_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersStatusSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    purchase_order_status: Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus] = UNSET,
    item_confirmation_status: Union[Unset, None, GetPurchaseOrdersStatusItemConfirmationStatus] = UNSET,
    item_receive_status: Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
    ship_to_party_id: Union[Unset, None, str] = UNSET,
) -> Response[GetPurchaseOrdersStatusResponse]:
    """Returns purchase order statuses based on the filters that you specify. Date range to search must not
    be more than 7 days. You can return a list of purchase order statuses using the available filters,
    or a single purchase order status by providing the purchase order number.

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
        sort_order (Union[Unset, None, GetPurchaseOrdersStatusSortOrder]):
        next_token (Union[Unset, None, str]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        purchase_order_number (Union[Unset, None, str]):
        purchase_order_status (Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus]):
        item_confirmation_status (Union[Unset, None,
            GetPurchaseOrdersStatusItemConfirmationStatus]):
        item_receive_status (Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus]):
        ordering_vendor_code (Union[Unset, None, str]):
        ship_to_party_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersStatusResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        sort_order=sort_order,
        next_token=next_token,
        created_after=created_after,
        created_before=created_before,
        updated_after=updated_after,
        updated_before=updated_before,
        purchase_order_number=purchase_order_number,
        purchase_order_status=purchase_order_status,
        item_confirmation_status=item_confirmation_status,
        item_receive_status=item_receive_status,
        ordering_vendor_code=ordering_vendor_code,
        ship_to_party_id=ship_to_party_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetPurchaseOrdersStatusSortOrder] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    purchase_order_number: Union[Unset, None, str] = UNSET,
    purchase_order_status: Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus] = UNSET,
    item_confirmation_status: Union[Unset, None, GetPurchaseOrdersStatusItemConfirmationStatus] = UNSET,
    item_receive_status: Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus] = UNSET,
    ordering_vendor_code: Union[Unset, None, str] = UNSET,
    ship_to_party_id: Union[Unset, None, str] = UNSET,
) -> Optional[GetPurchaseOrdersStatusResponse]:
    """Returns purchase order statuses based on the filters that you specify. Date range to search must not
    be more than 7 days. You can return a list of purchase order statuses using the available filters,
    or a single purchase order status by providing the purchase order number.

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
        sort_order (Union[Unset, None, GetPurchaseOrdersStatusSortOrder]):
        next_token (Union[Unset, None, str]):
        created_after (Union[Unset, None, datetime.datetime]):
        created_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        purchase_order_number (Union[Unset, None, str]):
        purchase_order_status (Union[Unset, None, GetPurchaseOrdersStatusPurchaseOrderStatus]):
        item_confirmation_status (Union[Unset, None,
            GetPurchaseOrdersStatusItemConfirmationStatus]):
        item_receive_status (Union[Unset, None, GetPurchaseOrdersStatusItemReceiveStatus]):
        ordering_vendor_code (Union[Unset, None, str]):
        ship_to_party_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPurchaseOrdersStatusResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            sort_order=sort_order,
            next_token=next_token,
            created_after=created_after,
            created_before=created_before,
            updated_after=updated_after,
            updated_before=updated_before,
            purchase_order_number=purchase_order_number,
            purchase_order_status=purchase_order_status,
            item_confirmation_status=item_confirmation_status,
            item_receive_status=item_receive_status,
            ordering_vendor_code=ordering_vendor_code,
            ship_to_party_id=ship_to_party_id,
        )
    ).parsed
