from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_restricted_data_token_request import CreateRestrictedDataTokenRequest
from ...models.create_restricted_data_token_response import CreateRestrictedDataTokenResponse
from ...models.error_list import ErrorList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateRestrictedDataTokenRequest,
) -> Dict[str, Any]:
    url = "{}/tokens/2021-03-01/restrictedDataToken".format(client.base_url)

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
) -> Optional[Union[CreateRestrictedDataTokenResponse, ErrorList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateRestrictedDataTokenResponse.from_dict(response.json())

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
) -> Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateRestrictedDataTokenRequest,
) -> Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]:
    """Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A
    restricted resource is the HTTP method and path from a restricted operation that returns Personally
    Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested.
    See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as
    the access token in subsequent calls to the corresponding restricted operations.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 1 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        json_body (CreateRestrictedDataTokenRequest): The request schema for the
            createRestrictedDataToken operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]
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
    json_body: CreateRestrictedDataTokenRequest,
) -> Optional[Union[CreateRestrictedDataTokenResponse, ErrorList]]:
    """Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A
    restricted resource is the HTTP method and path from a restricted operation that returns Personally
    Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested.
    See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as
    the access token in subsequent calls to the corresponding restricted operations.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 1 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        json_body (CreateRestrictedDataTokenRequest): The request schema for the
            createRestrictedDataToken operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateRestrictedDataTokenRequest,
) -> Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]:
    """Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A
    restricted resource is the HTTP method and path from a restricted operation that returns Personally
    Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested.
    See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as
    the access token in subsequent calls to the corresponding restricted operations.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 1 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        json_body (CreateRestrictedDataTokenRequest): The request schema for the
            createRestrictedDataToken operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]
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
    json_body: CreateRestrictedDataTokenRequest,
) -> Optional[Union[CreateRestrictedDataTokenResponse, ErrorList]]:
    """Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A
    restricted resource is the HTTP method and path from a restricted operation that returns Personally
    Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested.
    See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as
    the access token in subsequent calls to the corresponding restricted operations.

    **Usage Plans:**

    | Plan type | Rate (requests per second) | Burst |
    | ---- | ---- | ---- |
    |Default| 1 | 10 |
    |Selling partner specific| Variable | Variable |

    The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to
    the requested operation. Rate limits for some selling partners will vary from the default rate and
    burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the
    Selling Partner API documentation.

    Args:
        json_body (CreateRestrictedDataTokenRequest): The request schema for the
            createRestrictedDataToken operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateRestrictedDataTokenResponse, ErrorList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
