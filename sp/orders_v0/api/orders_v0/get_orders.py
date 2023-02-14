from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_orders_response import GetOrdersResponse
from ...models.item_approval_status import ItemApprovalStatus
from ...models.item_approval_type import ItemApprovalType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    order_statuses: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
    fulfillment_channels: Union[Unset, None, List[str]] = UNSET,
    payment_methods: Union[Unset, None, List[str]] = UNSET,
    buyer_email: Union[Unset, None, str] = UNSET,
    seller_order_id: Union[Unset, None, str] = UNSET,
    max_results_per_page: Union[Unset, None, int] = UNSET,
    easy_ship_shipment_statuses: Union[Unset, None, List[str]] = UNSET,
    electronic_invoice_statuses: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    amazon_order_ids: Union[Unset, None, List[str]] = UNSET,
    actual_fulfillment_supply_source_id: Union[Unset, None, str] = UNSET,
    is_ispu: Union[Unset, None, bool] = UNSET,
    store_chain_store_id: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orders/v0/orders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["CreatedAfter"] = created_after

    params["CreatedBefore"] = created_before

    params["LastUpdatedAfter"] = last_updated_after

    params["LastUpdatedBefore"] = last_updated_before

    json_order_statuses: Union[Unset, None, List[str]] = UNSET
    if not isinstance(order_statuses, Unset):
        if order_statuses is None:
            json_order_statuses = None
        else:
            json_order_statuses = order_statuses

    params["OrderStatuses"] = json_order_statuses

    json_marketplace_ids = marketplace_ids

    params["MarketplaceIds"] = json_marketplace_ids

    json_fulfillment_channels: Union[Unset, None, List[str]] = UNSET
    if not isinstance(fulfillment_channels, Unset):
        if fulfillment_channels is None:
            json_fulfillment_channels = None
        else:
            json_fulfillment_channels = fulfillment_channels

    params["FulfillmentChannels"] = json_fulfillment_channels

    json_payment_methods: Union[Unset, None, List[str]] = UNSET
    if not isinstance(payment_methods, Unset):
        if payment_methods is None:
            json_payment_methods = None
        else:
            json_payment_methods = payment_methods

    params["PaymentMethods"] = json_payment_methods

    params["BuyerEmail"] = buyer_email

    params["SellerOrderId"] = seller_order_id

    params["MaxResultsPerPage"] = max_results_per_page

    json_easy_ship_shipment_statuses: Union[Unset, None, List[str]] = UNSET
    if not isinstance(easy_ship_shipment_statuses, Unset):
        if easy_ship_shipment_statuses is None:
            json_easy_ship_shipment_statuses = None
        else:
            json_easy_ship_shipment_statuses = easy_ship_shipment_statuses

    params["EasyShipShipmentStatuses"] = json_easy_ship_shipment_statuses

    json_electronic_invoice_statuses: Union[Unset, None, List[str]] = UNSET
    if not isinstance(electronic_invoice_statuses, Unset):
        if electronic_invoice_statuses is None:
            json_electronic_invoice_statuses = None
        else:
            json_electronic_invoice_statuses = electronic_invoice_statuses

    params["ElectronicInvoiceStatuses"] = json_electronic_invoice_statuses

    params["NextToken"] = next_token

    json_amazon_order_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(amazon_order_ids, Unset):
        if amazon_order_ids is None:
            json_amazon_order_ids = None
        else:
            json_amazon_order_ids = amazon_order_ids

    params["AmazonOrderIds"] = json_amazon_order_ids

    params["ActualFulfillmentSupplySourceId"] = actual_fulfillment_supply_source_id

    params["IsISPU"] = is_ispu

    params["StoreChainStoreId"] = store_chain_store_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetOrdersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOrdersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOrdersResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOrdersResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetOrdersResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetOrdersResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetOrdersResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetOrdersResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    order_statuses: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
    fulfillment_channels: Union[Unset, None, List[str]] = UNSET,
    payment_methods: Union[Unset, None, List[str]] = UNSET,
    buyer_email: Union[Unset, None, str] = UNSET,
    seller_order_id: Union[Unset, None, str] = UNSET,
    max_results_per_page: Union[Unset, None, int] = UNSET,
    easy_ship_shipment_statuses: Union[Unset, None, List[str]] = UNSET,
    electronic_invoice_statuses: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    amazon_order_ids: Union[Unset, None, List[str]] = UNSET,
    actual_fulfillment_supply_source_id: Union[Unset, None, str] = UNSET,
    is_ispu: Union[Unset, None, bool] = UNSET,
    store_chain_store_id: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Response[GetOrdersResponse]:
    """Returns orders created or updated during the time frame indicated by the specified parameters. You
    can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is
    present, that will be used to retrieve the orders instead of other criteria.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0167 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        order_statuses (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):
        fulfillment_channels (Union[Unset, None, List[str]]):
        payment_methods (Union[Unset, None, List[str]]):
        buyer_email (Union[Unset, None, str]):
        seller_order_id (Union[Unset, None, str]):
        max_results_per_page (Union[Unset, None, int]):
        easy_ship_shipment_statuses (Union[Unset, None, List[str]]):
        electronic_invoice_statuses (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        amazon_order_ids (Union[Unset, None, List[str]]):
        actual_fulfillment_supply_source_id (Union[Unset, None, str]):
        is_ispu (Union[Unset, None, bool]):
        store_chain_store_id (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        created_after=created_after,
        created_before=created_before,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        order_statuses=order_statuses,
        marketplace_ids=marketplace_ids,
        fulfillment_channels=fulfillment_channels,
        payment_methods=payment_methods,
        buyer_email=buyer_email,
        seller_order_id=seller_order_id,
        max_results_per_page=max_results_per_page,
        easy_ship_shipment_statuses=easy_ship_shipment_statuses,
        electronic_invoice_statuses=electronic_invoice_statuses,
        next_token=next_token,
        amazon_order_ids=amazon_order_ids,
        actual_fulfillment_supply_source_id=actual_fulfillment_supply_source_id,
        is_ispu=is_ispu,
        store_chain_store_id=store_chain_store_id,
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
    *,
    client: Client,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    order_statuses: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
    fulfillment_channels: Union[Unset, None, List[str]] = UNSET,
    payment_methods: Union[Unset, None, List[str]] = UNSET,
    buyer_email: Union[Unset, None, str] = UNSET,
    seller_order_id: Union[Unset, None, str] = UNSET,
    max_results_per_page: Union[Unset, None, int] = UNSET,
    easy_ship_shipment_statuses: Union[Unset, None, List[str]] = UNSET,
    electronic_invoice_statuses: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    amazon_order_ids: Union[Unset, None, List[str]] = UNSET,
    actual_fulfillment_supply_source_id: Union[Unset, None, str] = UNSET,
    is_ispu: Union[Unset, None, bool] = UNSET,
    store_chain_store_id: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Optional[GetOrdersResponse]:
    """Returns orders created or updated during the time frame indicated by the specified parameters. You
    can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is
    present, that will be used to retrieve the orders instead of other criteria.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0167 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        order_statuses (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):
        fulfillment_channels (Union[Unset, None, List[str]]):
        payment_methods (Union[Unset, None, List[str]]):
        buyer_email (Union[Unset, None, str]):
        seller_order_id (Union[Unset, None, str]):
        max_results_per_page (Union[Unset, None, int]):
        easy_ship_shipment_statuses (Union[Unset, None, List[str]]):
        electronic_invoice_statuses (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        amazon_order_ids (Union[Unset, None, List[str]]):
        actual_fulfillment_supply_source_id (Union[Unset, None, str]):
        is_ispu (Union[Unset, None, bool]):
        store_chain_store_id (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    return sync_detailed(
        client=client,
        created_after=created_after,
        created_before=created_before,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        order_statuses=order_statuses,
        marketplace_ids=marketplace_ids,
        fulfillment_channels=fulfillment_channels,
        payment_methods=payment_methods,
        buyer_email=buyer_email,
        seller_order_id=seller_order_id,
        max_results_per_page=max_results_per_page,
        easy_ship_shipment_statuses=easy_ship_shipment_statuses,
        electronic_invoice_statuses=electronic_invoice_statuses,
        next_token=next_token,
        amazon_order_ids=amazon_order_ids,
        actual_fulfillment_supply_source_id=actual_fulfillment_supply_source_id,
        is_ispu=is_ispu,
        store_chain_store_id=store_chain_store_id,
        item_approval_types=item_approval_types,
        item_approval_status=item_approval_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    order_statuses: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
    fulfillment_channels: Union[Unset, None, List[str]] = UNSET,
    payment_methods: Union[Unset, None, List[str]] = UNSET,
    buyer_email: Union[Unset, None, str] = UNSET,
    seller_order_id: Union[Unset, None, str] = UNSET,
    max_results_per_page: Union[Unset, None, int] = UNSET,
    easy_ship_shipment_statuses: Union[Unset, None, List[str]] = UNSET,
    electronic_invoice_statuses: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    amazon_order_ids: Union[Unset, None, List[str]] = UNSET,
    actual_fulfillment_supply_source_id: Union[Unset, None, str] = UNSET,
    is_ispu: Union[Unset, None, bool] = UNSET,
    store_chain_store_id: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Response[GetOrdersResponse]:
    """Returns orders created or updated during the time frame indicated by the specified parameters. You
    can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is
    present, that will be used to retrieve the orders instead of other criteria.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0167 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        order_statuses (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):
        fulfillment_channels (Union[Unset, None, List[str]]):
        payment_methods (Union[Unset, None, List[str]]):
        buyer_email (Union[Unset, None, str]):
        seller_order_id (Union[Unset, None, str]):
        max_results_per_page (Union[Unset, None, int]):
        easy_ship_shipment_statuses (Union[Unset, None, List[str]]):
        electronic_invoice_statuses (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        amazon_order_ids (Union[Unset, None, List[str]]):
        actual_fulfillment_supply_source_id (Union[Unset, None, str]):
        is_ispu (Union[Unset, None, bool]):
        store_chain_store_id (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        created_after=created_after,
        created_before=created_before,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        order_statuses=order_statuses,
        marketplace_ids=marketplace_ids,
        fulfillment_channels=fulfillment_channels,
        payment_methods=payment_methods,
        buyer_email=buyer_email,
        seller_order_id=seller_order_id,
        max_results_per_page=max_results_per_page,
        easy_ship_shipment_statuses=easy_ship_shipment_statuses,
        electronic_invoice_statuses=electronic_invoice_statuses,
        next_token=next_token,
        amazon_order_ids=amazon_order_ids,
        actual_fulfillment_supply_source_id=actual_fulfillment_supply_source_id,
        is_ispu=is_ispu,
        store_chain_store_id=store_chain_store_id,
        item_approval_types=item_approval_types,
        item_approval_status=item_approval_status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    created_after: Union[Unset, None, str] = UNSET,
    created_before: Union[Unset, None, str] = UNSET,
    last_updated_after: Union[Unset, None, str] = UNSET,
    last_updated_before: Union[Unset, None, str] = UNSET,
    order_statuses: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
    fulfillment_channels: Union[Unset, None, List[str]] = UNSET,
    payment_methods: Union[Unset, None, List[str]] = UNSET,
    buyer_email: Union[Unset, None, str] = UNSET,
    seller_order_id: Union[Unset, None, str] = UNSET,
    max_results_per_page: Union[Unset, None, int] = UNSET,
    easy_ship_shipment_statuses: Union[Unset, None, List[str]] = UNSET,
    electronic_invoice_statuses: Union[Unset, None, List[str]] = UNSET,
    next_token: Union[Unset, None, str] = UNSET,
    amazon_order_ids: Union[Unset, None, List[str]] = UNSET,
    actual_fulfillment_supply_source_id: Union[Unset, None, str] = UNSET,
    is_ispu: Union[Unset, None, bool] = UNSET,
    store_chain_store_id: Union[Unset, None, str] = UNSET,
    item_approval_types: Union[Unset, None, List[ItemApprovalType]] = UNSET,
    item_approval_status: Union[Unset, None, List[ItemApprovalStatus]] = UNSET,
) -> Optional[GetOrdersResponse]:
    """Returns orders created or updated during the time frame indicated by the specified parameters. You
    can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is
    present, that will be used to retrieve the orders instead of other criteria.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0167 | 20 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        created_after (Union[Unset, None, str]):
        created_before (Union[Unset, None, str]):
        last_updated_after (Union[Unset, None, str]):
        last_updated_before (Union[Unset, None, str]):
        order_statuses (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):
        fulfillment_channels (Union[Unset, None, List[str]]):
        payment_methods (Union[Unset, None, List[str]]):
        buyer_email (Union[Unset, None, str]):
        seller_order_id (Union[Unset, None, str]):
        max_results_per_page (Union[Unset, None, int]):
        easy_ship_shipment_statuses (Union[Unset, None, List[str]]):
        electronic_invoice_statuses (Union[Unset, None, List[str]]):
        next_token (Union[Unset, None, str]):
        amazon_order_ids (Union[Unset, None, List[str]]):
        actual_fulfillment_supply_source_id (Union[Unset, None, str]):
        is_ispu (Union[Unset, None, bool]):
        store_chain_store_id (Union[Unset, None, str]):
        item_approval_types (Union[Unset, None, List[ItemApprovalType]]):
        item_approval_status (Union[Unset, None, List[ItemApprovalStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrdersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_after=created_after,
            created_before=created_before,
            last_updated_after=last_updated_after,
            last_updated_before=last_updated_before,
            order_statuses=order_statuses,
            marketplace_ids=marketplace_ids,
            fulfillment_channels=fulfillment_channels,
            payment_methods=payment_methods,
            buyer_email=buyer_email,
            seller_order_id=seller_order_id,
            max_results_per_page=max_results_per_page,
            easy_ship_shipment_statuses=easy_ship_shipment_statuses,
            electronic_invoice_statuses=electronic_invoice_statuses,
            next_token=next_token,
            amazon_order_ids=amazon_order_ids,
            actual_fulfillment_supply_source_id=actual_fulfillment_supply_source_id,
            is_ispu=is_ispu,
            store_chain_store_id=store_chain_store_id,
            item_approval_types=item_approval_types,
            item_approval_status=item_approval_status,
        )
    ).parsed
