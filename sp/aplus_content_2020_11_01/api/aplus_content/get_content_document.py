from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.get_content_document_included_data_set_item import GetContentDocumentIncludedDataSetItem
from ...models.get_content_document_response import GetContentDocumentResponse
from ...types import UNSET, Response


def _get_kwargs(
    content_reference_key: str,
    *,
    client: Client,
    marketplace_id: str,
    included_data_set: List[GetContentDocumentIncludedDataSetItem],
) -> Dict[str, Any]:
    url = "{}/aplus/2020-11-01/contentDocuments/{contentReferenceKey}".format(
        client.base_url, contentReferenceKey=content_reference_key
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["marketplaceId"] = marketplace_id

    json_included_data_set = []
    for included_data_set_item_data in included_data_set:
        included_data_set_item = included_data_set_item_data.value

        json_included_data_set.append(included_data_set_item)

    params["includedDataSet"] = json_included_data_set

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorList, GetContentDocumentResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetContentDocumentResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorList.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorList.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorList.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorList.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.GONE:
        response_410 = ErrorList.from_dict(response.json())

        return response_410
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
) -> Response[Union[ErrorList, GetContentDocumentResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    content_reference_key: str,
    *,
    client: Client,
    marketplace_id: str,
    included_data_set: List[GetContentDocumentIncludedDataSetItem],
) -> Response[Union[ErrorList, GetContentDocumentResponse]]:
    """Returns an A+ Content document, if available.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        content_reference_key (str):
        marketplace_id (str):
        included_data_set (List[GetContentDocumentIncludedDataSetItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetContentDocumentResponse]]
    """

    kwargs = _get_kwargs(
        content_reference_key=content_reference_key,
        client=client,
        marketplace_id=marketplace_id,
        included_data_set=included_data_set,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    content_reference_key: str,
    *,
    client: Client,
    marketplace_id: str,
    included_data_set: List[GetContentDocumentIncludedDataSetItem],
) -> Optional[Union[ErrorList, GetContentDocumentResponse]]:
    """Returns an A+ Content document, if available.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        content_reference_key (str):
        marketplace_id (str):
        included_data_set (List[GetContentDocumentIncludedDataSetItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetContentDocumentResponse]]
    """

    return sync_detailed(
        content_reference_key=content_reference_key,
        client=client,
        marketplace_id=marketplace_id,
        included_data_set=included_data_set,
    ).parsed


async def asyncio_detailed(
    content_reference_key: str,
    *,
    client: Client,
    marketplace_id: str,
    included_data_set: List[GetContentDocumentIncludedDataSetItem],
) -> Response[Union[ErrorList, GetContentDocumentResponse]]:
    """Returns an A+ Content document, if available.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        content_reference_key (str):
        marketplace_id (str):
        included_data_set (List[GetContentDocumentIncludedDataSetItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetContentDocumentResponse]]
    """

    kwargs = _get_kwargs(
        content_reference_key=content_reference_key,
        client=client,
        marketplace_id=marketplace_id,
        included_data_set=included_data_set,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    content_reference_key: str,
    *,
    client: Client,
    marketplace_id: str,
    included_data_set: List[GetContentDocumentIncludedDataSetItem],
) -> Optional[Union[ErrorList, GetContentDocumentResponse]]:
    """Returns an A+ Content document, if available.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 10 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        content_reference_key (str):
        marketplace_id (str):
        included_data_set (List[GetContentDocumentIncludedDataSetItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, GetContentDocumentResponse]]
    """

    return (
        await asyncio_detailed(
            content_reference_key=content_reference_key,
            client=client,
            marketplace_id=marketplace_id,
            included_data_set=included_data_set,
        )
    ).parsed
