from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.small_and_light_fee_preview_request import SmallAndLightFeePreviewRequest
from ...models.small_and_light_fee_previews import SmallAndLightFeePreviews
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SmallAndLightFeePreviewRequest,
) -> Dict[str, Any]:
    url = "{}/fba/smallAndLight/v1/feePreviews".format(client.base_url)

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
) -> Optional[Union[ErrorList, SmallAndLightFeePreviews]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SmallAndLightFeePreviews.from_dict(response.json())

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
) -> Response[Union[ErrorList, SmallAndLightFeePreviews]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SmallAndLightFeePreviewRequest,
) -> Response[Union[ErrorList, SmallAndLightFeePreviews]]:
    """Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId
    parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The
    ordering of items in the response will mirror the order of the items in the request. Duplicate
    ASIN/price combinations are removed.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 3 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (SmallAndLightFeePreviewRequest): Request schema for submitting items for which
            to retrieve fee estimates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, SmallAndLightFeePreviews]]
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
    json_body: SmallAndLightFeePreviewRequest,
) -> Optional[Union[ErrorList, SmallAndLightFeePreviews]]:
    """Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId
    parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The
    ordering of items in the response will mirror the order of the items in the request. Duplicate
    ASIN/price combinations are removed.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 3 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (SmallAndLightFeePreviewRequest): Request schema for submitting items for which
            to retrieve fee estimates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, SmallAndLightFeePreviews]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SmallAndLightFeePreviewRequest,
) -> Response[Union[ErrorList, SmallAndLightFeePreviews]]:
    """Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId
    parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The
    ordering of items in the response will mirror the order of the items in the request. Duplicate
    ASIN/price combinations are removed.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 3 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (SmallAndLightFeePreviewRequest): Request schema for submitting items for which
            to retrieve fee estimates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, SmallAndLightFeePreviews]]
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
    json_body: SmallAndLightFeePreviewRequest,
) -> Optional[Union[ErrorList, SmallAndLightFeePreviews]]:
    """Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId
    parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The
    ordering of items in the response will mirror the order of the items in the request. Duplicate
    ASIN/price combinations are removed.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 3 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        json_body (SmallAndLightFeePreviewRequest): Request schema for submitting items for which
            to retrieve fee estimates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, SmallAndLightFeePreviews]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
