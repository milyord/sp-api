from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_scheduled_package_request import CreateScheduledPackageRequest
from ...models.error_list import ErrorList
from ...models.package import Package
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateScheduledPackageRequest,
) -> Dict[str, Any]:
    url = "{}/easyShip/2022-03-23/package".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, Package]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Package.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, Package]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateScheduledPackageRequest,
) -> Response[Union[ErrorList, Package]]:
    """Schedules an Easy Ship order and returns the scheduled package information.

    This operation does the following:

    *  Specifies the time slot and handover method for the order to be scheduled for delivery.

    * Updates the Easy Ship order status.

    * Generates a shipping label and an invoice. Calling `createScheduledPackage` also generates a
    warranty document if you specify a `SerialNumber` value. To get these documents, see [How to get
    invoice, shipping label, and warranty documents](doc:easyship-api-v2022-03-23-use-case-guide).

    * Shows the status of Easy Ship orders when you call the `getOrders` operation of the Selling
    Partner API for Orders and examine the `EasyShipShipmentStatus` property in the response body.

    See the **Shipping Label**, **Invoice**, and **Warranty** columns in the [Marketplace Support
    Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which documents
    are supported in each marketplace.

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
        json_body (CreateScheduledPackageRequest): The request schema for the
            `createScheduledPackage` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Package]]
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
    json_body: CreateScheduledPackageRequest,
) -> Optional[Union[ErrorList, Package]]:
    """Schedules an Easy Ship order and returns the scheduled package information.

    This operation does the following:

    *  Specifies the time slot and handover method for the order to be scheduled for delivery.

    * Updates the Easy Ship order status.

    * Generates a shipping label and an invoice. Calling `createScheduledPackage` also generates a
    warranty document if you specify a `SerialNumber` value. To get these documents, see [How to get
    invoice, shipping label, and warranty documents](doc:easyship-api-v2022-03-23-use-case-guide).

    * Shows the status of Easy Ship orders when you call the `getOrders` operation of the Selling
    Partner API for Orders and examine the `EasyShipShipmentStatus` property in the response body.

    See the **Shipping Label**, **Invoice**, and **Warranty** columns in the [Marketplace Support
    Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which documents
    are supported in each marketplace.

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
        json_body (CreateScheduledPackageRequest): The request schema for the
            `createScheduledPackage` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Package]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateScheduledPackageRequest,
) -> Response[Union[ErrorList, Package]]:
    """Schedules an Easy Ship order and returns the scheduled package information.

    This operation does the following:

    *  Specifies the time slot and handover method for the order to be scheduled for delivery.

    * Updates the Easy Ship order status.

    * Generates a shipping label and an invoice. Calling `createScheduledPackage` also generates a
    warranty document if you specify a `SerialNumber` value. To get these documents, see [How to get
    invoice, shipping label, and warranty documents](doc:easyship-api-v2022-03-23-use-case-guide).

    * Shows the status of Easy Ship orders when you call the `getOrders` operation of the Selling
    Partner API for Orders and examine the `EasyShipShipmentStatus` property in the response body.

    See the **Shipping Label**, **Invoice**, and **Warranty** columns in the [Marketplace Support
    Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which documents
    are supported in each marketplace.

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
        json_body (CreateScheduledPackageRequest): The request schema for the
            `createScheduledPackage` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Package]]
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
    json_body: CreateScheduledPackageRequest,
) -> Optional[Union[ErrorList, Package]]:
    """Schedules an Easy Ship order and returns the scheduled package information.

    This operation does the following:

    *  Specifies the time slot and handover method for the order to be scheduled for delivery.

    * Updates the Easy Ship order status.

    * Generates a shipping label and an invoice. Calling `createScheduledPackage` also generates a
    warranty document if you specify a `SerialNumber` value. To get these documents, see [How to get
    invoice, shipping label, and warranty documents](doc:easyship-api-v2022-03-23-use-case-guide).

    * Shows the status of Easy Ship orders when you call the `getOrders` operation of the Selling
    Partner API for Orders and examine the `EasyShipShipmentStatus` property in the response body.

    See the **Shipping Label**, **Invoice**, and **Warranty** columns in the [Marketplace Support
    Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which documents
    are supported in each marketplace.

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
        json_body (CreateScheduledPackageRequest): The request schema for the
            `createScheduledPackage` operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, Package]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
