from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.item_search_results import ItemSearchResults
from ...models.search_catalog_items_identifiers_type import SearchCatalogItemsIdentifiersType
from ...models.search_catalog_items_included_data_item import SearchCatalogItemsIncludedDataItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    identifiers: Union[Unset, None, List[str]] = UNSET,
    identifiers_type: Union[Unset, None, SearchCatalogItemsIdentifiersType] = UNSET,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
    seller_id: Union[Unset, None, str] = UNSET,
    keywords: Union[Unset, None, List[str]] = UNSET,
    brand_names: Union[Unset, None, List[str]] = UNSET,
    classification_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    page_token: Union[Unset, None, str] = UNSET,
    keywords_locale: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/catalog/2022-04-01/items".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_identifiers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(identifiers, Unset):
        if identifiers is None:
            json_identifiers = None
        else:
            json_identifiers = identifiers

    params["identifiers"] = json_identifiers

    json_identifiers_type: Union[Unset, None, str] = UNSET
    if not isinstance(identifiers_type, Unset):
        json_identifiers_type = identifiers_type.value if identifiers_type else None

    params["identifiersType"] = json_identifiers_type

    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    json_included_data: Union[Unset, None, List[str]] = UNSET
    if not isinstance(included_data, Unset):
        if included_data is None:
            json_included_data = None
        else:
            json_included_data = []
            for included_data_item_data in included_data:
                included_data_item = included_data_item_data.value

                json_included_data.append(included_data_item)

    params["includedData"] = json_included_data

    params["locale"] = locale

    params["sellerId"] = seller_id

    json_keywords: Union[Unset, None, List[str]] = UNSET
    if not isinstance(keywords, Unset):
        if keywords is None:
            json_keywords = None
        else:
            json_keywords = keywords

    params["keywords"] = json_keywords

    json_brand_names: Union[Unset, None, List[str]] = UNSET
    if not isinstance(brand_names, Unset):
        if brand_names is None:
            json_brand_names = None
        else:
            json_brand_names = brand_names

    params["brandNames"] = json_brand_names

    json_classification_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(classification_ids, Unset):
        if classification_ids is None:
            json_classification_ids = None
        else:
            json_classification_ids = classification_ids

    params["classificationIds"] = json_classification_ids

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["keywordsLocale"] = keywords_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, ItemSearchResults]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ItemSearchResults.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorList.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = ErrorList.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = ErrorList.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = ErrorList.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorList.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ErrorList.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, ItemSearchResults]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    identifiers: Union[Unset, None, List[str]] = UNSET,
    identifiers_type: Union[Unset, None, SearchCatalogItemsIdentifiersType] = UNSET,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
    seller_id: Union[Unset, None, str] = UNSET,
    keywords: Union[Unset, None, List[str]] = UNSET,
    brand_names: Union[Unset, None, List[str]] = UNSET,
    classification_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    page_token: Union[Unset, None, str] = UNSET,
    keywords_locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, ItemSearchResults]]:
    """Search for and return a list of Amazon catalog items and associated information either by identifier
    or by keywords.

    **Usage Plans:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        identifiers (Union[Unset, None, List[str]]):
        identifiers_type (Union[Unset, None, SearchCatalogItemsIdentifiersType]):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]]):
        locale (Union[Unset, None, str]):
        seller_id (Union[Unset, None, str]):
        keywords (Union[Unset, None, List[str]]):
        brand_names (Union[Unset, None, List[str]]):
        classification_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_token (Union[Unset, None, str]):
        keywords_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ItemSearchResults]]
    """

    kwargs = _get_kwargs(
        client=client,
        identifiers=identifiers,
        identifiers_type=identifiers_type,
        marketplace_ids=marketplace_ids,
        included_data=included_data,
        locale=locale,
        seller_id=seller_id,
        keywords=keywords,
        brand_names=brand_names,
        classification_ids=classification_ids,
        page_size=page_size,
        page_token=page_token,
        keywords_locale=keywords_locale,
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
    identifiers: Union[Unset, None, List[str]] = UNSET,
    identifiers_type: Union[Unset, None, SearchCatalogItemsIdentifiersType] = UNSET,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
    seller_id: Union[Unset, None, str] = UNSET,
    keywords: Union[Unset, None, List[str]] = UNSET,
    brand_names: Union[Unset, None, List[str]] = UNSET,
    classification_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    page_token: Union[Unset, None, str] = UNSET,
    keywords_locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, ItemSearchResults]]:
    """Search for and return a list of Amazon catalog items and associated information either by identifier
    or by keywords.

    **Usage Plans:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        identifiers (Union[Unset, None, List[str]]):
        identifiers_type (Union[Unset, None, SearchCatalogItemsIdentifiersType]):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]]):
        locale (Union[Unset, None, str]):
        seller_id (Union[Unset, None, str]):
        keywords (Union[Unset, None, List[str]]):
        brand_names (Union[Unset, None, List[str]]):
        classification_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_token (Union[Unset, None, str]):
        keywords_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ItemSearchResults]]
    """

    return sync_detailed(
        client=client,
        identifiers=identifiers,
        identifiers_type=identifiers_type,
        marketplace_ids=marketplace_ids,
        included_data=included_data,
        locale=locale,
        seller_id=seller_id,
        keywords=keywords,
        brand_names=brand_names,
        classification_ids=classification_ids,
        page_size=page_size,
        page_token=page_token,
        keywords_locale=keywords_locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    identifiers: Union[Unset, None, List[str]] = UNSET,
    identifiers_type: Union[Unset, None, SearchCatalogItemsIdentifiersType] = UNSET,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
    seller_id: Union[Unset, None, str] = UNSET,
    keywords: Union[Unset, None, List[str]] = UNSET,
    brand_names: Union[Unset, None, List[str]] = UNSET,
    classification_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    page_token: Union[Unset, None, str] = UNSET,
    keywords_locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, ItemSearchResults]]:
    """Search for and return a list of Amazon catalog items and associated information either by identifier
    or by keywords.

    **Usage Plans:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        identifiers (Union[Unset, None, List[str]]):
        identifiers_type (Union[Unset, None, SearchCatalogItemsIdentifiersType]):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]]):
        locale (Union[Unset, None, str]):
        seller_id (Union[Unset, None, str]):
        keywords (Union[Unset, None, List[str]]):
        brand_names (Union[Unset, None, List[str]]):
        classification_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_token (Union[Unset, None, str]):
        keywords_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ItemSearchResults]]
    """

    kwargs = _get_kwargs(
        client=client,
        identifiers=identifiers,
        identifiers_type=identifiers_type,
        marketplace_ids=marketplace_ids,
        included_data=included_data,
        locale=locale,
        seller_id=seller_id,
        keywords=keywords,
        brand_names=brand_names,
        classification_ids=classification_ids,
        page_size=page_size,
        page_token=page_token,
        keywords_locale=keywords_locale,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    identifiers: Union[Unset, None, List[str]] = UNSET,
    identifiers_type: Union[Unset, None, SearchCatalogItemsIdentifiersType] = UNSET,
    marketplace_ids: List[str],
    included_data: Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]] = UNSET,
    locale: Union[Unset, None, str] = UNSET,
    seller_id: Union[Unset, None, str] = UNSET,
    keywords: Union[Unset, None, List[str]] = UNSET,
    brand_names: Union[Unset, None, List[str]] = UNSET,
    classification_ids: Union[Unset, None, List[str]] = UNSET,
    page_size: Union[Unset, None, int] = 10,
    page_token: Union[Unset, None, str] = UNSET,
    keywords_locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, ItemSearchResults]]:
    """Search for and return a list of Amazon catalog items and associated information either by identifier
    or by keywords.

    **Usage Plans:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 2 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may observe
    higher rate and burst values than those shown here. For more information, refer to the [Usage Plans
    and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        identifiers (Union[Unset, None, List[str]]):
        identifiers_type (Union[Unset, None, SearchCatalogItemsIdentifiersType]):
        marketplace_ids (List[str]):
        included_data (Union[Unset, None, List[SearchCatalogItemsIncludedDataItem]]):
        locale (Union[Unset, None, str]):
        seller_id (Union[Unset, None, str]):
        keywords (Union[Unset, None, List[str]]):
        brand_names (Union[Unset, None, List[str]]):
        classification_ids (Union[Unset, None, List[str]]):
        page_size (Union[Unset, None, int]):  Default: 10.
        page_token (Union[Unset, None, str]):
        keywords_locale (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ItemSearchResults]]
    """

    return (
        await asyncio_detailed(
            client=client,
            identifiers=identifiers,
            identifiers_type=identifiers_type,
            marketplace_ids=marketplace_ids,
            included_data=included_data,
            locale=locale,
            seller_id=seller_id,
            keywords=keywords,
            brand_names=brand_names,
            classification_ids=classification_ids,
            page_size=page_size,
            page_token=page_token,
            keywords_locale=keywords_locale,
        )
    ).parsed
