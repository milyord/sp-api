from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.get_listings_restrictions_condition_type import GetListingsRestrictionsConditionType
from ...models.restriction_list import RestrictionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    asin: str,
    condition_type: Union[Unset, None, GetListingsRestrictionsConditionType] = UNSET,
    seller_id: str,
    marketplace_ids: List[str],
    reason_locale: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/listings/2021-08-01/restrictions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["asin"] = asin

    json_condition_type: Union[Unset, None, str] = UNSET
    if not isinstance(condition_type, Unset):
        json_condition_type = condition_type.value if condition_type else None

    params["conditionType"] = json_condition_type

    params["sellerId"] = seller_id

    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["reasonLocale"] = reason_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[List["Error"], RestrictionList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RestrictionList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = []
        _response_400 = response.json()
        for componentsschemas_error_list_item_data in _response_400:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_400.append(componentsschemas_error_list_item)

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = []
        _response_403 = response.json()
        for componentsschemas_error_list_item_data in _response_403:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_403.append(componentsschemas_error_list_item)

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = []
        _response_404 = response.json()
        for componentsschemas_error_list_item_data in _response_404:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_404.append(componentsschemas_error_list_item)

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = []
        _response_413 = response.json()
        for componentsschemas_error_list_item_data in _response_413:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_413.append(componentsschemas_error_list_item)

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = []
        _response_415 = response.json()
        for componentsschemas_error_list_item_data in _response_415:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_415.append(componentsschemas_error_list_item)

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = []
        _response_429 = response.json()
        for componentsschemas_error_list_item_data in _response_429:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_429.append(componentsschemas_error_list_item)

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = []
        _response_500 = response.json()
        for componentsschemas_error_list_item_data in _response_500:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_500.append(componentsschemas_error_list_item)

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = []
        _response_503 = response.json()
        for componentsschemas_error_list_item_data in _response_503:
            componentsschemas_error_list_item = Error.from_dict(componentsschemas_error_list_item_data)

            response_503.append(componentsschemas_error_list_item)

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[List["Error"], RestrictionList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    asin: str,
    condition_type: Union[Unset, None, GetListingsRestrictionsConditionType] = UNSET,
    seller_id: str,
    marketplace_ids: List[str],
    reason_locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[List["Error"], RestrictionList]]:
    """Returns listing restrictions for an item in the Amazon Catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        condition_type (Union[Unset, None, GetListingsRestrictionsConditionType]):
        seller_id (str):
        marketplace_ids (List[str]):
        reason_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], RestrictionList]]
    """

    kwargs = _get_kwargs(
        client=client,
        asin=asin,
        condition_type=condition_type,
        seller_id=seller_id,
        marketplace_ids=marketplace_ids,
        reason_locale=reason_locale,
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
    asin: str,
    condition_type: Union[Unset, None, GetListingsRestrictionsConditionType] = UNSET,
    seller_id: str,
    marketplace_ids: List[str],
    reason_locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[List["Error"], RestrictionList]]:
    """Returns listing restrictions for an item in the Amazon Catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        condition_type (Union[Unset, None, GetListingsRestrictionsConditionType]):
        seller_id (str):
        marketplace_ids (List[str]):
        reason_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], RestrictionList]]
    """

    return sync_detailed(
        client=client,
        asin=asin,
        condition_type=condition_type,
        seller_id=seller_id,
        marketplace_ids=marketplace_ids,
        reason_locale=reason_locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    asin: str,
    condition_type: Union[Unset, None, GetListingsRestrictionsConditionType] = UNSET,
    seller_id: str,
    marketplace_ids: List[str],
    reason_locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[List["Error"], RestrictionList]]:
    """Returns listing restrictions for an item in the Amazon Catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        condition_type (Union[Unset, None, GetListingsRestrictionsConditionType]):
        seller_id (str):
        marketplace_ids (List[str]):
        reason_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], RestrictionList]]
    """

    kwargs = _get_kwargs(
        client=client,
        asin=asin,
        condition_type=condition_type,
        seller_id=seller_id,
        marketplace_ids=marketplace_ids,
        reason_locale=reason_locale,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    asin: str,
    condition_type: Union[Unset, None, GetListingsRestrictionsConditionType] = UNSET,
    seller_id: str,
    marketplace_ids: List[str],
    reason_locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[List["Error"], RestrictionList]]:
    """Returns listing restrictions for an item in the Amazon Catalog.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 5 | 10 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        asin (str):
        condition_type (Union[Unset, None, GetListingsRestrictionsConditionType]):
        seller_id (str):
        marketplace_ids (List[str]):
        reason_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['Error'], RestrictionList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            asin=asin,
            condition_type=condition_type,
            seller_id=seller_id,
            marketplace_ids=marketplace_ids,
            reason_locale=reason_locale,
        )
    ).parsed
