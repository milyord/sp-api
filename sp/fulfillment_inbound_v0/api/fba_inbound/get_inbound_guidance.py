from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_inbound_guidance_response import GetInboundGuidanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marketplace_id: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/itemsGuidance".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MarketplaceId"] = marketplace_id

    json_seller_sku_list: Union[Unset, None, List[str]] = UNSET
    if not isinstance(seller_sku_list, Unset):
        if seller_sku_list is None:
            json_seller_sku_list = None
        else:
            json_seller_sku_list = seller_sku_list

    params["SellerSKUList"] = json_seller_sku_list

    json_asin_list: Union[Unset, None, List[str]] = UNSET
    if not isinstance(asin_list, Unset):
        if asin_list is None:
            json_asin_list = None
        else:
            json_asin_list = asin_list

    params["ASINList"] = json_asin_list

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetInboundGuidanceResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetInboundGuidanceResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetInboundGuidanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    marketplace_id: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Response[GetInboundGuidanceResponse]:
    """Returns information that lets a seller know if Amazon recommends sending an item to a given
    marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not
    recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not
    recommended, at their discretion.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInboundGuidanceResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        seller_sku_list=seller_sku_list,
        asin_list=asin_list,
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
    marketplace_id: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Optional[GetInboundGuidanceResponse]:
    """Returns information that lets a seller know if Amazon recommends sending an item to a given
    marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not
    recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not
    recommended, at their discretion.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInboundGuidanceResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_id=marketplace_id,
        seller_sku_list=seller_sku_list,
        asin_list=asin_list,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_id: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Response[GetInboundGuidanceResponse]:
    """Returns information that lets a seller know if Amazon recommends sending an item to a given
    marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not
    recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not
    recommended, at their discretion.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInboundGuidanceResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        seller_sku_list=seller_sku_list,
        asin_list=asin_list,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_id: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Optional[GetInboundGuidanceResponse]:
    """Returns information that lets a seller know if Amazon recommends sending an item to a given
    marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not
    recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not
    recommended, at their discretion.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInboundGuidanceResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_id=marketplace_id,
            seller_sku_list=seller_sku_list,
            asin_list=asin_list,
        )
    ).parsed
