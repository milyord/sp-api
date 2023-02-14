from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_return_reason_codes_response import ListReturnReasonCodesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    seller_sku: str,
    marketplace_id: Union[Unset, None, str] = UNSET,
    seller_fulfillment_order_id: Union[Unset, None, str] = UNSET,
    language: str,
) -> Dict[str, Any]:
    url = "{}/fba/outbound/2020-07-01/returnReasonCodes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sellerSku"] = seller_sku

    params["marketplaceId"] = marketplace_id

    params["sellerFulfillmentOrderId"] = seller_fulfillment_order_id

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListReturnReasonCodesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ListReturnReasonCodesResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListReturnReasonCodesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    seller_sku: str,
    marketplace_id: Union[Unset, None, str] = UNSET,
    seller_fulfillment_order_id: Union[Unset, None, str] = UNSET,
    language: str,
) -> Response[ListReturnReasonCodesResponse]:
    """Returns a list of return reason codes for a seller SKU in a given marketplace.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_sku (str):
        marketplace_id (Union[Unset, None, str]):
        seller_fulfillment_order_id (Union[Unset, None, str]):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReturnReasonCodesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        seller_sku=seller_sku,
        marketplace_id=marketplace_id,
        seller_fulfillment_order_id=seller_fulfillment_order_id,
        language=language,
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
    seller_sku: str,
    marketplace_id: Union[Unset, None, str] = UNSET,
    seller_fulfillment_order_id: Union[Unset, None, str] = UNSET,
    language: str,
) -> Optional[ListReturnReasonCodesResponse]:
    """Returns a list of return reason codes for a seller SKU in a given marketplace.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_sku (str):
        marketplace_id (Union[Unset, None, str]):
        seller_fulfillment_order_id (Union[Unset, None, str]):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReturnReasonCodesResponse]
    """

    return sync_detailed(
        client=client,
        seller_sku=seller_sku,
        marketplace_id=marketplace_id,
        seller_fulfillment_order_id=seller_fulfillment_order_id,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    seller_sku: str,
    marketplace_id: Union[Unset, None, str] = UNSET,
    seller_fulfillment_order_id: Union[Unset, None, str] = UNSET,
    language: str,
) -> Response[ListReturnReasonCodesResponse]:
    """Returns a list of return reason codes for a seller SKU in a given marketplace.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_sku (str):
        marketplace_id (Union[Unset, None, str]):
        seller_fulfillment_order_id (Union[Unset, None, str]):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReturnReasonCodesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        seller_sku=seller_sku,
        marketplace_id=marketplace_id,
        seller_fulfillment_order_id=seller_fulfillment_order_id,
        language=language,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    seller_sku: str,
    marketplace_id: Union[Unset, None, str] = UNSET,
    seller_fulfillment_order_id: Union[Unset, None, str] = UNSET,
    language: str,
) -> Optional[ListReturnReasonCodesResponse]:
    """Returns a list of return reason codes for a seller SKU in a given marketplace.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        seller_sku (str):
        marketplace_id (Union[Unset, None, str]):
        seller_fulfillment_order_id (Union[Unset, None, str]):
        language (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReturnReasonCodesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            seller_sku=seller_sku,
            marketplace_id=marketplace_id,
            seller_fulfillment_order_id=seller_fulfillment_order_id,
            language=language,
        )
    ).parsed
