from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.listings_item_patch_request import ListingsItemPatchRequest
from ...models.listings_item_submission_response import ListingsItemSubmissionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    seller_id: str,
    sku: str,
    *,
    client: Client,
    json_body: ListingsItemPatchRequest,
    marketplace_ids: List[str],
    issue_locale: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/listings/2020-09-01/items/{sellerId}/{sku}".format(client.base_url, sellerId=seller_id, sku=sku)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["issueLocale"] = issue_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorList, ListingsItemSubmissionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingsItemSubmissionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorList, ListingsItemSubmissionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    seller_id: str,
    sku: str,
    *,
    client: Client,
    json_body: ListingsItemPatchRequest,
    marketplace_ids: List[str],
    issue_locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, ListingsItemSubmissionResponse]]:
    """Partially update (patch) a listings item for a selling partner. Only top-level listings item
    attributes can be patched. Patching nested attributes is not supported.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 5 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the
    Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_id (str):
        sku (str):
        marketplace_ids (List[str]):
        issue_locale (Union[Unset, None, str]):
        json_body (ListingsItemPatchRequest): The request body schema for the patchListingsItem
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListingsItemSubmissionResponse]]
    """

    kwargs = _get_kwargs(
        seller_id=seller_id,
        sku=sku,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
        issue_locale=issue_locale,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    seller_id: str,
    sku: str,
    *,
    client: Client,
    json_body: ListingsItemPatchRequest,
    marketplace_ids: List[str],
    issue_locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, ListingsItemSubmissionResponse]]:
    """Partially update (patch) a listings item for a selling partner. Only top-level listings item
    attributes can be patched. Patching nested attributes is not supported.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 5 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the
    Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_id (str):
        sku (str):
        marketplace_ids (List[str]):
        issue_locale (Union[Unset, None, str]):
        json_body (ListingsItemPatchRequest): The request body schema for the patchListingsItem
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListingsItemSubmissionResponse]]
    """

    return sync_detailed(
        seller_id=seller_id,
        sku=sku,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
        issue_locale=issue_locale,
    ).parsed


async def asyncio_detailed(
    seller_id: str,
    sku: str,
    *,
    client: Client,
    json_body: ListingsItemPatchRequest,
    marketplace_ids: List[str],
    issue_locale: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorList, ListingsItemSubmissionResponse]]:
    """Partially update (patch) a listings item for a selling partner. Only top-level listings item
    attributes can be patched. Patching nested attributes is not supported.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 5 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the
    Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_id (str):
        sku (str):
        marketplace_ids (List[str]):
        issue_locale (Union[Unset, None, str]):
        json_body (ListingsItemPatchRequest): The request body schema for the patchListingsItem
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListingsItemSubmissionResponse]]
    """

    kwargs = _get_kwargs(
        seller_id=seller_id,
        sku=sku,
        client=client,
        json_body=json_body,
        marketplace_ids=marketplace_ids,
        issue_locale=issue_locale,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    seller_id: str,
    sku: str,
    *,
    client: Client,
    json_body: ListingsItemPatchRequest,
    marketplace_ids: List[str],
    issue_locale: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorList, ListingsItemSubmissionResponse]]:
    """Partially update (patch) a listings item for a selling partner. Only top-level listings item
    attributes can be patched. Patching nested attributes is not supported.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 5 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the
    Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        seller_id (str):
        sku (str):
        marketplace_ids (List[str]):
        issue_locale (Union[Unset, None, str]):
        json_body (ListingsItemPatchRequest): The request body schema for the patchListingsItem
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ListingsItemSubmissionResponse]]
    """

    return (
        await asyncio_detailed(
            seller_id=seller_id,
            sku=sku,
            client=client,
            json_body=json_body,
            marketplace_ids=marketplace_ids,
            issue_locale=issue_locale,
        )
    ).parsed
