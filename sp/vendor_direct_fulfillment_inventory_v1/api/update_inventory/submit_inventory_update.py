from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.submit_inventory_update_request import SubmitInventoryUpdateRequest
from ...models.submit_inventory_update_response import SubmitInventoryUpdateResponse
from ...types import Response


def _get_kwargs(
    warehouse_id: str,
    *,
    client: Client,
    json_body: SubmitInventoryUpdateRequest,
) -> Dict[str, Any]:
    url = "{}/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items".format(
        client.base_url, warehouseId=warehouse_id
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SubmitInventoryUpdateResponse]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = SubmitInventoryUpdateResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SubmitInventoryUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    warehouse_id: str,
    *,
    client: Client,
    json_body: SubmitInventoryUpdateRequest,
) -> Response[SubmitInventoryUpdateResponse]:
    """Submits inventory updates for the specified warehouse for either a partial or full feed of inventory
    items.

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
        warehouse_id (str):
        json_body (SubmitInventoryUpdateRequest): The request body for the submitInventoryUpdate
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitInventoryUpdateResponse]
    """

    kwargs = _get_kwargs(
        warehouse_id=warehouse_id,
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
    warehouse_id: str,
    *,
    client: Client,
    json_body: SubmitInventoryUpdateRequest,
) -> Optional[SubmitInventoryUpdateResponse]:
    """Submits inventory updates for the specified warehouse for either a partial or full feed of inventory
    items.

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
        warehouse_id (str):
        json_body (SubmitInventoryUpdateRequest): The request body for the submitInventoryUpdate
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitInventoryUpdateResponse]
    """

    return sync_detailed(
        warehouse_id=warehouse_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    warehouse_id: str,
    *,
    client: Client,
    json_body: SubmitInventoryUpdateRequest,
) -> Response[SubmitInventoryUpdateResponse]:
    """Submits inventory updates for the specified warehouse for either a partial or full feed of inventory
    items.

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
        warehouse_id (str):
        json_body (SubmitInventoryUpdateRequest): The request body for the submitInventoryUpdate
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitInventoryUpdateResponse]
    """

    kwargs = _get_kwargs(
        warehouse_id=warehouse_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    warehouse_id: str,
    *,
    client: Client,
    json_body: SubmitInventoryUpdateRequest,
) -> Optional[SubmitInventoryUpdateResponse]:
    """Submits inventory updates for the specified warehouse for either a partial or full feed of inventory
    items.

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
        warehouse_id (str):
        json_body (SubmitInventoryUpdateRequest): The request body for the submitInventoryUpdate
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitInventoryUpdateResponse]
    """

    return (
        await asyncio_detailed(
            warehouse_id=warehouse_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
