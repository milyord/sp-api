from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_upload_destination_response import CreateUploadDestinationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    content_md5: str,
    content_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/uploads/2020-11-01/uploadDestinations/{resource}".format(client.base_url, resource=resource)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["contentMD5"] = content_md5

    params["contentType"] = content_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateUploadDestinationResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = CreateUploadDestinationResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateUploadDestinationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    content_md5: str,
    content_type: Union[Unset, None, str] = UNSET,
) -> Response[CreateUploadDestinationResponse]:
    """Creates an upload destination, returning the information required to upload a file to the
    destination and to programmatically access the file.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        resource (str):
        marketplace_ids (List[str]):
        content_md5 (str):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUploadDestinationResponse]
    """

    kwargs = _get_kwargs(
        resource=resource,
        client=client,
        marketplace_ids=marketplace_ids,
        content_md5=content_md5,
        content_type=content_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    content_md5: str,
    content_type: Union[Unset, None, str] = UNSET,
) -> Optional[CreateUploadDestinationResponse]:
    """Creates an upload destination, returning the information required to upload a file to the
    destination and to programmatically access the file.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        resource (str):
        marketplace_ids (List[str]):
        content_md5 (str):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUploadDestinationResponse]
    """

    return sync_detailed(
        resource=resource,
        client=client,
        marketplace_ids=marketplace_ids,
        content_md5=content_md5,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    resource: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    content_md5: str,
    content_type: Union[Unset, None, str] = UNSET,
) -> Response[CreateUploadDestinationResponse]:
    """Creates an upload destination, returning the information required to upload a file to the
    destination and to programmatically access the file.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        resource (str):
        marketplace_ids (List[str]):
        content_md5 (str):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUploadDestinationResponse]
    """

    kwargs = _get_kwargs(
        resource=resource,
        client=client,
        marketplace_ids=marketplace_ids,
        content_md5=content_md5,
        content_type=content_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource: str,
    *,
    client: Client,
    marketplace_ids: List[str],
    content_md5: str,
    content_type: Union[Unset, None, str] = UNSET,
) -> Optional[CreateUploadDestinationResponse]:
    """Creates an upload destination, returning the information required to upload a file to the
    destination and to programmatically access the file.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | .1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        resource (str):
        marketplace_ids (List[str]):
        content_md5 (str):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUploadDestinationResponse]
    """

    return (
        await asyncio_detailed(
            resource=resource,
            client=client,
            marketplace_ids=marketplace_ids,
            content_md5=content_md5,
            content_type=content_type,
        )
    ).parsed
