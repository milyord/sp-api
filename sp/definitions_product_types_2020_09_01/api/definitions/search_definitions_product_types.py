from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.product_type_list import ProductTypeList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    keywords: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
) -> Dict[str, Any]:
    url = "{}/definitions/2020-09-01/productTypes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_keywords: Union[Unset, None, List[str]] = UNSET
    if not isinstance(keywords, Unset):
        if keywords is None:
            json_keywords = None
        else:
            json_keywords = keywords

    params["keywords"] = json_keywords

    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, ProductTypeList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProductTypeList.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, ProductTypeList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    keywords: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
) -> Response[Union[ErrorList, ProductTypeList]]:
    """Search for and return a list of Amazon product types that have definitions available.

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
        keywords (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeList]]
    """

    kwargs = _get_kwargs(
        client=client,
        keywords=keywords,
        marketplace_ids=marketplace_ids,
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
    keywords: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
) -> Optional[Union[ErrorList, ProductTypeList]]:
    """Search for and return a list of Amazon product types that have definitions available.

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
        keywords (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeList]]
    """

    return sync_detailed(
        client=client,
        keywords=keywords,
        marketplace_ids=marketplace_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    keywords: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
) -> Response[Union[ErrorList, ProductTypeList]]:
    """Search for and return a list of Amazon product types that have definitions available.

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
        keywords (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeList]]
    """

    kwargs = _get_kwargs(
        client=client,
        keywords=keywords,
        marketplace_ids=marketplace_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    keywords: Union[Unset, None, List[str]] = UNSET,
    marketplace_ids: List[str],
) -> Optional[Union[ErrorList, ProductTypeList]]:
    """Search for and return a list of Amazon product types that have definitions available.

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
        keywords (Union[Unset, None, List[str]]):
        marketplace_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            keywords=keywords,
            marketplace_ids=marketplace_ids,
        )
    ).parsed
