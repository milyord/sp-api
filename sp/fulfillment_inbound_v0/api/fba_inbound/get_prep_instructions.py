from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_prep_instructions_response import GetPrepInstructionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    ship_to_country_code: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/prepInstructions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ShipToCountryCode"] = ship_to_country_code

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetPrepInstructionsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetPrepInstructionsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetPrepInstructionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    ship_to_country_code: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Response[GetPrepInstructionsResponse]:
    """Returns labeling requirements and item preparation instructions to help prepare items for shipment
    to Amazon's fulfillment network.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        ship_to_country_code (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrepInstructionsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        ship_to_country_code=ship_to_country_code,
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
    ship_to_country_code: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Optional[GetPrepInstructionsResponse]:
    """Returns labeling requirements and item preparation instructions to help prepare items for shipment
    to Amazon's fulfillment network.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        ship_to_country_code (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrepInstructionsResponse]
    """

    return sync_detailed(
        client=client,
        ship_to_country_code=ship_to_country_code,
        seller_sku_list=seller_sku_list,
        asin_list=asin_list,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    ship_to_country_code: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Response[GetPrepInstructionsResponse]:
    """Returns labeling requirements and item preparation instructions to help prepare items for shipment
    to Amazon's fulfillment network.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        ship_to_country_code (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrepInstructionsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        ship_to_country_code=ship_to_country_code,
        seller_sku_list=seller_sku_list,
        asin_list=asin_list,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    ship_to_country_code: str,
    seller_sku_list: Union[Unset, None, List[str]] = UNSET,
    asin_list: Union[Unset, None, List[str]] = UNSET,
) -> Optional[GetPrepInstructionsResponse]:
    """Returns labeling requirements and item preparation instructions to help prepare items for shipment
    to Amazon's fulfillment network.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        ship_to_country_code (str):
        seller_sku_list (Union[Unset, None, List[str]]):
        asin_list (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrepInstructionsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            ship_to_country_code=ship_to_country_code,
            seller_sku_list=seller_sku_list,
            asin_list=asin_list,
        )
    ).parsed
