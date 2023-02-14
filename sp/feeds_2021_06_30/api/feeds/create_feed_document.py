from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_feed_document_response import CreateFeedDocumentResponse
from ...models.create_feed_document_specification import CreateFeedDocumentSpecification
from ...models.error_list import ErrorList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateFeedDocumentSpecification,
) -> Dict[str, Any]:
    url = "{}/feeds/2021-06-30/documents".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[CreateFeedDocumentResponse, ErrorList]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateFeedDocumentResponse.from_dict(response.json())

        return response_201
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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[CreateFeedDocumentResponse, ErrorList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateFeedDocumentSpecification,
) -> Response[Union[CreateFeedDocumentResponse, ErrorList]]:
    """Creates a feed document for the feed type that you specify. This operation returns a presigned URL
    for uploading the feed document contents. It also returns a feedDocumentId value that you can pass
    in with a subsequent call to the createFeed operation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0083 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateFeedDocumentSpecification): Specifies the content type for the
            createFeedDocument operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateFeedDocumentResponse, ErrorList]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: CreateFeedDocumentSpecification,
) -> Optional[Union[CreateFeedDocumentResponse, ErrorList]]:
    """Creates a feed document for the feed type that you specify. This operation returns a presigned URL
    for uploading the feed document contents. It also returns a feedDocumentId value that you can pass
    in with a subsequent call to the createFeed operation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0083 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateFeedDocumentSpecification): Specifies the content type for the
            createFeedDocument operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateFeedDocumentResponse, ErrorList]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateFeedDocumentSpecification,
) -> Response[Union[CreateFeedDocumentResponse, ErrorList]]:
    """Creates a feed document for the feed type that you specify. This operation returns a presigned URL
    for uploading the feed document contents. It also returns a feedDocumentId value that you can pass
    in with a subsequent call to the createFeed operation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0083 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateFeedDocumentSpecification): Specifies the content type for the
            createFeedDocument operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateFeedDocumentResponse, ErrorList]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateFeedDocumentSpecification,
) -> Optional[Union[CreateFeedDocumentResponse, ErrorList]]:
    """Creates a feed document for the feed type that you specify. This operation returns a presigned URL
    for uploading the feed document contents. It also returns a feedDocumentId value that you can pass
    in with a subsequent call to the createFeed operation.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.0083 | 15 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (CreateFeedDocumentSpecification): Specifies the content type for the
            createFeedDocument operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateFeedDocumentResponse, ErrorList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
