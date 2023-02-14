from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_competitive_pricing_customer_type import GetCompetitivePricingCustomerType
from ...models.get_competitive_pricing_item_type import GetCompetitivePricingItemType
from ...models.get_pricing_response import GetPricingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marketplace_id: str,
    asins: Union[Unset, None, List[str]] = UNSET,
    skus: Union[Unset, None, List[str]] = UNSET,
    item_type: GetCompetitivePricingItemType,
    customer_type: Union[Unset, None, GetCompetitivePricingCustomerType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/products/pricing/v0/competitivePrice".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["MarketplaceId"] = marketplace_id

    json_asins: Union[Unset, None, List[str]] = UNSET
    if not isinstance(asins, Unset):
        if asins is None:
            json_asins = None
        else:
            json_asins = asins

    params["Asins"] = json_asins

    json_skus: Union[Unset, None, List[str]] = UNSET
    if not isinstance(skus, Unset):
        if skus is None:
            json_skus = None
        else:
            json_skus = skus

    params["Skus"] = json_skus

    json_item_type = item_type.value

    params["ItemType"] = json_item_type

    json_customer_type: Union[Unset, None, str] = UNSET
    if not isinstance(customer_type, Unset):
        json_customer_type = customer_type.value if customer_type else None

    params["CustomerType"] = json_customer_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetPricingResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPricingResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetPricingResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetPricingResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetPricingResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetPricingResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetPricingResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetPricingResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetPricingResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetPricingResponse]:
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
    asins: Union[Unset, None, List[str]] = UNSET,
    skus: Union[Unset, None, List[str]] = UNSET,
    item_type: GetCompetitivePricingItemType,
    customer_type: Union[Unset, None, GetCompetitivePricingCustomerType] = UNSET,
) -> Response[GetPricingResponse]:
    """Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_id (str):
        asins (Union[Unset, None, List[str]]):
        skus (Union[Unset, None, List[str]]):
        item_type (GetCompetitivePricingItemType):
        customer_type (Union[Unset, None, GetCompetitivePricingCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPricingResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        asins=asins,
        skus=skus,
        item_type=item_type,
        customer_type=customer_type,
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
    asins: Union[Unset, None, List[str]] = UNSET,
    skus: Union[Unset, None, List[str]] = UNSET,
    item_type: GetCompetitivePricingItemType,
    customer_type: Union[Unset, None, GetCompetitivePricingCustomerType] = UNSET,
) -> Optional[GetPricingResponse]:
    """Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_id (str):
        asins (Union[Unset, None, List[str]]):
        skus (Union[Unset, None, List[str]]):
        item_type (GetCompetitivePricingItemType):
        customer_type (Union[Unset, None, GetCompetitivePricingCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPricingResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_id=marketplace_id,
        asins=asins,
        skus=skus,
        item_type=item_type,
        customer_type=customer_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_id: str,
    asins: Union[Unset, None, List[str]] = UNSET,
    skus: Union[Unset, None, List[str]] = UNSET,
    item_type: GetCompetitivePricingItemType,
    customer_type: Union[Unset, None, GetCompetitivePricingCustomerType] = UNSET,
) -> Response[GetPricingResponse]:
    """Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_id (str):
        asins (Union[Unset, None, List[str]]):
        skus (Union[Unset, None, List[str]]):
        item_type (GetCompetitivePricingItemType):
        customer_type (Union[Unset, None, GetCompetitivePricingCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPricingResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
        asins=asins,
        skus=skus,
        item_type=item_type,
        customer_type=customer_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_id: str,
    asins: Union[Unset, None, List[str]] = UNSET,
    skus: Union[Unset, None, List[str]] = UNSET,
    item_type: GetCompetitivePricingItemType,
    customer_type: Union[Unset, None, GetCompetitivePricingCustomerType] = UNSET,
) -> Optional[GetPricingResponse]:
    """Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.5 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        marketplace_id (str):
        asins (Union[Unset, None, List[str]]):
        skus (Union[Unset, None, List[str]]):
        item_type (GetCompetitivePricingItemType):
        customer_type (Union[Unset, None, GetCompetitivePricingCustomerType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPricingResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_id=marketplace_id,
            asins=asins,
            skus=skus,
            item_type=item_type,
            customer_type=customer_type,
        )
    ).parsed
