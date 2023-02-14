from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.submit_shipment_status_updates_request import SubmitShipmentStatusUpdatesRequest
from ...models.submit_shipment_status_updates_response import SubmitShipmentStatusUpdatesResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SubmitShipmentStatusUpdatesRequest,
) -> Dict[str, Any]:
    url = "{}/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SubmitShipmentStatusUpdatesResponse]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = SubmitShipmentStatusUpdatesResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SubmitShipmentStatusUpdatesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SubmitShipmentStatusUpdatesRequest,
) -> Response[SubmitShipmentStatusUpdatesResponse]:
    """This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a
    shipment status update for the package that a vendor has shipped. It will provide the Amazon
    customer visibility on their order, when the package is outside of Amazon Network visibility.

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
        json_body (SubmitShipmentStatusUpdatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitShipmentStatusUpdatesResponse]
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
    json_body: SubmitShipmentStatusUpdatesRequest,
) -> Optional[SubmitShipmentStatusUpdatesResponse]:
    """This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a
    shipment status update for the package that a vendor has shipped. It will provide the Amazon
    customer visibility on their order, when the package is outside of Amazon Network visibility.

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
        json_body (SubmitShipmentStatusUpdatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitShipmentStatusUpdatesResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SubmitShipmentStatusUpdatesRequest,
) -> Response[SubmitShipmentStatusUpdatesResponse]:
    """This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a
    shipment status update for the package that a vendor has shipped. It will provide the Amazon
    customer visibility on their order, when the package is outside of Amazon Network visibility.

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
        json_body (SubmitShipmentStatusUpdatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitShipmentStatusUpdatesResponse]
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
    json_body: SubmitShipmentStatusUpdatesRequest,
) -> Optional[SubmitShipmentStatusUpdatesResponse]:
    """This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a
    shipment status update for the package that a vendor has shipped. It will provide the Amazon
    customer visibility on their order, when the package is outside of Amazon Network visibility.

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
        json_body (SubmitShipmentStatusUpdatesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitShipmentStatusUpdatesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
