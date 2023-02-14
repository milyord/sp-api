from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_feature_inventory_response import GetFeatureInventoryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    feature_name: str,
    *,
    client: Client,
    marketplace_id: str,
    next_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/fba/outbound/2020-07-01/features/inventory/{featureName}".format(
        client.base_url, featureName=feature_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["marketplaceId"] = marketplace_id

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetFeatureInventoryResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetFeatureInventoryResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetFeatureInventoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feature_name: str,
    *,
    client: Client,
    marketplace_id: str,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[GetFeatureInventoryResponse]:
    """Returns a list of inventory items that are eligible for the fulfillment feature you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        marketplace_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureInventoryResponse]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
        client=client,
        marketplace_id=marketplace_id,
        next_token=next_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feature_name: str,
    *,
    client: Client,
    marketplace_id: str,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[GetFeatureInventoryResponse]:
    """Returns a list of inventory items that are eligible for the fulfillment feature you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        marketplace_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureInventoryResponse]
    """

    return sync_detailed(
        feature_name=feature_name,
        client=client,
        marketplace_id=marketplace_id,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    feature_name: str,
    *,
    client: Client,
    marketplace_id: str,
    next_token: Union[Unset, None, str] = UNSET,
) -> Response[GetFeatureInventoryResponse]:
    """Returns a list of inventory items that are eligible for the fulfillment feature you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        marketplace_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureInventoryResponse]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
        client=client,
        marketplace_id=marketplace_id,
        next_token=next_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feature_name: str,
    *,
    client: Client,
    marketplace_id: str,
    next_token: Union[Unset, None, str] = UNSET,
) -> Optional[GetFeatureInventoryResponse]:
    """Returns a list of inventory items that are eligible for the fulfillment feature you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        feature_name (str):
        marketplace_id (str):
        next_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureInventoryResponse]
    """

    return (
        await asyncio_detailed(
            feature_name=feature_name,
            client=client,
            marketplace_id=marketplace_id,
            next_token=next_token,
        )
    ).parsed
