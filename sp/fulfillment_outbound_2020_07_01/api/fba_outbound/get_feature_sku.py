from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_feature_sku_response import GetFeatureSkuResponse
from ...types import UNSET, Response


def _get_kwargs(
    feature_name: str,
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Dict[str, Any]:
    url = "{}/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}".format(
        client.base_url, featureName=feature_name, sellerSku=seller_sku
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["marketplaceId"] = marketplace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetFeatureSkuResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFeatureSkuResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetFeatureSkuResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetFeatureSkuResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetFeatureSkuResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetFeatureSkuResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetFeatureSkuResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetFeatureSkuResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetFeatureSkuResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetFeatureSkuResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feature_name: str,
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Response[GetFeatureSkuResponse]:
    """Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the
    specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty
    skuInfo object.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        seller_sku (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureSkuResponse]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
        seller_sku=seller_sku,
        client=client,
        marketplace_id=marketplace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feature_name: str,
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Optional[GetFeatureSkuResponse]:
    """Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the
    specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty
    skuInfo object.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        seller_sku (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureSkuResponse]
    """

    return sync_detailed(
        feature_name=feature_name,
        seller_sku=seller_sku,
        client=client,
        marketplace_id=marketplace_id,
    ).parsed


async def asyncio_detailed(
    feature_name: str,
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Response[GetFeatureSkuResponse]:
    """Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the
    specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty
    skuInfo object.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        seller_sku (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureSkuResponse]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
        seller_sku=seller_sku,
        client=client,
        marketplace_id=marketplace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feature_name: str,
    seller_sku: str,
    *,
    client: Client,
    marketplace_id: str,
) -> Optional[GetFeatureSkuResponse]:
    """Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the
    specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty
    skuInfo object.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        seller_sku (str):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureSkuResponse]
    """

    return (
        await asyncio_detailed(
            feature_name=feature_name,
            seller_sku=seller_sku,
            client=client,
            marketplace_id=marketplace_id,
        )
    ).parsed
