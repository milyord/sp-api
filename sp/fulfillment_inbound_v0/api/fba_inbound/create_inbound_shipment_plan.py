from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_inbound_shipment_plan_request import CreateInboundShipmentPlanRequest
from ...models.create_inbound_shipment_plan_response import CreateInboundShipmentPlanResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateInboundShipmentPlanRequest,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/plans".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateInboundShipmentPlanResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = CreateInboundShipmentPlanResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateInboundShipmentPlanResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateInboundShipmentPlanRequest,
) -> Response[CreateInboundShipmentPlanResponse]:
    """Returns one or more inbound shipment plans, which provide the information you need to create one or
    more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be
    required so that items can be optimally placed in Amazon's fulfillment network—for example,
    positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be
    created with the same Amazon fulfillment center destination if the two shipment plans require
    different processing—for example, items that require labels must be shipped separately from
    stickerless, commingled inventory.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateInboundShipmentPlanRequest): The request schema for the
            createInboundShipmentPlan operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInboundShipmentPlanResponse]
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
    json_body: CreateInboundShipmentPlanRequest,
) -> Optional[CreateInboundShipmentPlanResponse]:
    """Returns one or more inbound shipment plans, which provide the information you need to create one or
    more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be
    required so that items can be optimally placed in Amazon's fulfillment network—for example,
    positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be
    created with the same Amazon fulfillment center destination if the two shipment plans require
    different processing—for example, items that require labels must be shipped separately from
    stickerless, commingled inventory.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateInboundShipmentPlanRequest): The request schema for the
            createInboundShipmentPlan operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInboundShipmentPlanResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateInboundShipmentPlanRequest,
) -> Response[CreateInboundShipmentPlanResponse]:
    """Returns one or more inbound shipment plans, which provide the information you need to create one or
    more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be
    required so that items can be optimally placed in Amazon's fulfillment network—for example,
    positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be
    created with the same Amazon fulfillment center destination if the two shipment plans require
    different processing—for example, items that require labels must be shipped separately from
    stickerless, commingled inventory.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateInboundShipmentPlanRequest): The request schema for the
            createInboundShipmentPlan operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInboundShipmentPlanResponse]
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
    json_body: CreateInboundShipmentPlanRequest,
) -> Optional[CreateInboundShipmentPlanResponse]:
    """Returns one or more inbound shipment plans, which provide the information you need to create one or
    more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be
    required so that items can be optimally placed in Amazon's fulfillment network—for example,
    positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be
    created with the same Amazon fulfillment center destination if the two shipment plans require
    different processing—for example, items that require labels must be shipped separately from
    stickerless, commingled inventory.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateInboundShipmentPlanRequest): The request schema for the
            createInboundShipmentPlan operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInboundShipmentPlanResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
