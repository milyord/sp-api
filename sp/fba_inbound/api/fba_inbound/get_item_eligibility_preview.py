from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_item_eligibility_preview_program import GetItemEligibilityPreviewProgram
from ...models.get_item_eligibility_preview_response import GetItemEligibilityPreviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    asin: str,
    program: GetItemEligibilityPreviewProgram,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v1/eligibility/itemPreview".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_marketplace_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(marketplace_ids, Unset):
        if marketplace_ids is None:
            json_marketplace_ids = None
        else:
            json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["asin"] = asin

    json_program = program.value

    params["program"] = json_program

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetItemEligibilityPreviewResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetItemEligibilityPreviewResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetItemEligibilityPreviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    asin: str,
    program: GetItemEligibilityPreviewProgram,
) -> Response[GetItemEligibilityPreviewResponse]:
    """This operation gets an eligibility preview for an item that you specify. You can specify the type of
    eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify
    the marketplace in which you want to determine the item's eligibility.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 1 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_ids (Union[Unset, None, List[str]]):
        asin (str):
        program (GetItemEligibilityPreviewProgram):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetItemEligibilityPreviewResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_ids=marketplace_ids,
        asin=asin,
        program=program,
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
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    asin: str,
    program: GetItemEligibilityPreviewProgram,
) -> Optional[GetItemEligibilityPreviewResponse]:
    """This operation gets an eligibility preview for an item that you specify. You can specify the type of
    eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify
    the marketplace in which you want to determine the item's eligibility.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 1 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_ids (Union[Unset, None, List[str]]):
        asin (str):
        program (GetItemEligibilityPreviewProgram):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetItemEligibilityPreviewResponse]
    """

    return sync_detailed(
        client=client,
        marketplace_ids=marketplace_ids,
        asin=asin,
        program=program,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    asin: str,
    program: GetItemEligibilityPreviewProgram,
) -> Response[GetItemEligibilityPreviewResponse]:
    """This operation gets an eligibility preview for an item that you specify. You can specify the type of
    eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify
    the marketplace in which you want to determine the item's eligibility.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 1 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_ids (Union[Unset, None, List[str]]):
        asin (str):
        program (GetItemEligibilityPreviewProgram):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetItemEligibilityPreviewResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        marketplace_ids=marketplace_ids,
        asin=asin,
        program=program,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    marketplace_ids: Union[Unset, None, List[str]] = UNSET,
    asin: str,
    program: GetItemEligibilityPreviewProgram,
) -> Optional[GetItemEligibilityPreviewResponse]:
    """This operation gets an eligibility preview for an item that you specify. You can specify the type of
    eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify
    the marketplace in which you want to determine the item's eligibility.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 1 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        marketplace_ids (Union[Unset, None, List[str]]):
        asin (str):
        program (GetItemEligibilityPreviewProgram):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetItemEligibilityPreviewResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marketplace_ids=marketplace_ids,
            asin=asin,
            program=program,
        )
    ).parsed
