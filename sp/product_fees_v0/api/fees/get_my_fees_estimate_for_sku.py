from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_my_fees_estimate_response import GetMyFeesEstimateResponse
from ...types import Response


def _get_kwargs(
    seller_sku: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/products/fees/v0/listings/{SellerSKU}/feesEstimate".format(client.base_url, SellerSKU=seller_sku)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetMyFeesEstimateResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetMyFeesEstimateResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetMyFeesEstimateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    seller_sku: str,
    *,
    client: Client,
) -> Response[GetMyFeesEstimateResponse]:
    """Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace
    specified in the request body.

    You can call `getMyFeesEstimateForSKU` for an item on behalf of a selling partner before the selling
    partner sets the item's price. The selling partner can then take any estimated fees into account.
    Each fees estimate request must include an original identifier. This identifier is included in the
    fees estimate so that you can correlate a fees estimate with the original request.

    **Note:** The identifier value is only an estimate, actual costs may vary. Search \"fees\" in
    [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for
    the most up-to-date information.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyFeesEstimateResponse]
    """

    kwargs = _get_kwargs(
        seller_sku=seller_sku,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    seller_sku: str,
    *,
    client: Client,
) -> Optional[GetMyFeesEstimateResponse]:
    """Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace
    specified in the request body.

    You can call `getMyFeesEstimateForSKU` for an item on behalf of a selling partner before the selling
    partner sets the item's price. The selling partner can then take any estimated fees into account.
    Each fees estimate request must include an original identifier. This identifier is included in the
    fees estimate so that you can correlate a fees estimate with the original request.

    **Note:** The identifier value is only an estimate, actual costs may vary. Search \"fees\" in
    [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for
    the most up-to-date information.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyFeesEstimateResponse]
    """

    return sync_detailed(
        seller_sku=seller_sku,
        client=client,
    ).parsed


async def asyncio_detailed(
    seller_sku: str,
    *,
    client: Client,
) -> Response[GetMyFeesEstimateResponse]:
    """Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace
    specified in the request body.

    You can call `getMyFeesEstimateForSKU` for an item on behalf of a selling partner before the selling
    partner sets the item's price. The selling partner can then take any estimated fees into account.
    Each fees estimate request must include an original identifier. This identifier is included in the
    fees estimate so that you can correlate a fees estimate with the original request.

    **Note:** The identifier value is only an estimate, actual costs may vary. Search \"fees\" in
    [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for
    the most up-to-date information.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyFeesEstimateResponse]
    """

    kwargs = _get_kwargs(
        seller_sku=seller_sku,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    seller_sku: str,
    *,
    client: Client,
) -> Optional[GetMyFeesEstimateResponse]:
    """Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace
    specified in the request body.

    You can call `getMyFeesEstimateForSKU` for an item on behalf of a selling partner before the selling
    partner sets the item's price. The selling partner can then take any estimated fees into account.
    Each fees estimate request must include an original identifier. This identifier is included in the
    fees estimate so that you can correlate a fees estimate with the original request.

    **Note:** The identifier value is only an estimate, actual costs may vary. Search \"fees\" in
    [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for
    the most up-to-date information.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_sku (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyFeesEstimateResponse]
    """

    return (
        await asyncio_detailed(
            seller_sku=seller_sku,
            client=client,
        )
    ).parsed
