from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_features_response import GetFeaturesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    marketplace_id: str,
) -> Dict[str, Any]:
    url = "{}/fba/outbound/2020-07-01/features".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetFeaturesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFeaturesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetFeaturesResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetFeaturesResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetFeaturesResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetFeaturesResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetFeaturesResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetFeaturesResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetFeaturesResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetFeaturesResponse]:
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
) -> Response[GetFeaturesResponse]:
    """Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you
    specify, and whether the seller for which you made the call is enrolled for each feature.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeaturesResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Client,
    marketplace_id: str,
) -> Optional[GetFeaturesResponse]:
    """Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you
    specify, and whether the seller for which you made the call is enrolled for each feature.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeaturesResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_id=marketplace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_id: str,
) -> Response[GetFeaturesResponse]:
    """Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you
    specify, and whether the seller for which you made the call is enrolled for each feature.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeaturesResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_id=marketplace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_id: str,
) -> Optional[GetFeaturesResponse]:
    """Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you
    specify, and whether the seller for which you made the call is enrolled for each feature.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeaturesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_id=marketplace_id,
        )
    ).parsed
