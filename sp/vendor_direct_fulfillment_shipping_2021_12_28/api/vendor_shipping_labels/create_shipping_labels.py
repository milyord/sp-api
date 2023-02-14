from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_shipping_labels_request import CreateShippingLabelsRequest
from ...models.error_list import ErrorList
from ...models.shipping_label import ShippingLabel
from ...types import Response


def _get_kwargs(
    purchase_order_number: str,
    *,
    client: Client,
    json_body: CreateShippingLabelsRequest,
) -> Dict[str, Any]:
    url = "{}/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber}".format(
        client.base_url, purchaseOrderNumber=purchase_order_number
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, ShippingLabel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ShippingLabel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorList.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorList.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = ErrorList.from_dict(response.json())

        return response_413
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, ShippingLabel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    purchase_order_number: str,
    *,
    client: Client,
    json_body: CreateShippingLabelsRequest,
) -> Response[Union[ErrorList, ShippingLabel]]:
    """Creates shipping labels for a purchase order and returns the labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        purchase_order_number (str):
        json_body (CreateShippingLabelsRequest): The request body for the createShippingLabels
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabel]]
    """

    kwargs = _get_kwargs(
        purchase_order_number=purchase_order_number,
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
    purchase_order_number: str,
    *,
    client: Client,
    json_body: CreateShippingLabelsRequest,
) -> Optional[Union[ErrorList, ShippingLabel]]:
    """Creates shipping labels for a purchase order and returns the labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        purchase_order_number (str):
        json_body (CreateShippingLabelsRequest): The request body for the createShippingLabels
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabel]]
    """

    return sync_detailed(
        purchase_order_number=purchase_order_number,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    purchase_order_number: str,
    *,
    client: Client,
    json_body: CreateShippingLabelsRequest,
) -> Response[Union[ErrorList, ShippingLabel]]:
    """Creates shipping labels for a purchase order and returns the labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        purchase_order_number (str):
        json_body (CreateShippingLabelsRequest): The request body for the createShippingLabels
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabel]]
    """

    kwargs = _get_kwargs(
        purchase_order_number=purchase_order_number,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purchase_order_number: str,
    *,
    client: Client,
    json_body: CreateShippingLabelsRequest,
) -> Optional[Union[ErrorList, ShippingLabel]]:
    """Creates shipping labels for a purchase order and returns the labels.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 10 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        purchase_order_number (str):
        json_body (CreateShippingLabelsRequest): The request body for the createShippingLabels
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ShippingLabel]]
    """

    return (
        await asyncio_detailed(
            purchase_order_number=purchase_order_number,
            client=client,
            json_body=json_body,
        )
    ).parsed
