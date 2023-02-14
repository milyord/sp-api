from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_authorization_code_response import GetAuthorizationCodeResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    selling_partner_id: str,
    developer_id: str,
    mws_auth_token: str,
) -> Dict[str, Any]:
    url = "{}/authorization/v1/authorizationCode".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sellingPartnerId"] = selling_partner_id

    params["developerId"] = developer_id

    params["mwsAuthToken"] = mws_auth_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetAuthorizationCodeResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetAuthorizationCodeResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetAuthorizationCodeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    selling_partner_id: str,
    developer_id: str,
    mws_auth_token: str,
) -> Response[GetAuthorizationCodeResponse]:
    """Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.

     With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization
    code that will allow you to call a Selling Partner API on behalf of a seller who has already
    authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an
    MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that
    the seller previously granted you. The operation returns an LWA authorization code that can be
    exchanged for a refresh token and access token representing authorization to call the Selling
    Partner API on the seller's behalf. By using this API, sellers who have already authorized you for
    Amazon MWS do not need to re-authorize you for the Selling Partner API.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        selling_partner_id (str):
        developer_id (str):
        mws_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizationCodeResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        selling_partner_id=selling_partner_id,
        developer_id=developer_id,
        mws_auth_token=mws_auth_token,
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
    selling_partner_id: str,
    developer_id: str,
    mws_auth_token: str,
) -> Optional[GetAuthorizationCodeResponse]:
    """Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.

     With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization
    code that will allow you to call a Selling Partner API on behalf of a seller who has already
    authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an
    MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that
    the seller previously granted you. The operation returns an LWA authorization code that can be
    exchanged for a refresh token and access token representing authorization to call the Selling
    Partner API on the seller's behalf. By using this API, sellers who have already authorized you for
    Amazon MWS do not need to re-authorize you for the Selling Partner API.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        selling_partner_id (str):
        developer_id (str):
        mws_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizationCodeResponse]
    """

    return sync_detailed(
        client=client,
        selling_partner_id=selling_partner_id,
        developer_id=developer_id,
        mws_auth_token=mws_auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    selling_partner_id: str,
    developer_id: str,
    mws_auth_token: str,
) -> Response[GetAuthorizationCodeResponse]:
    """Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.

     With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization
    code that will allow you to call a Selling Partner API on behalf of a seller who has already
    authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an
    MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that
    the seller previously granted you. The operation returns an LWA authorization code that can be
    exchanged for a refresh token and access token representing authorization to call the Selling
    Partner API on the seller's behalf. By using this API, sellers who have already authorized you for
    Amazon MWS do not need to re-authorize you for the Selling Partner API.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        selling_partner_id (str):
        developer_id (str):
        mws_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizationCodeResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        selling_partner_id=selling_partner_id,
        developer_id=developer_id,
        mws_auth_token=mws_auth_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    selling_partner_id: str,
    developer_id: str,
    mws_auth_token: str,
) -> Optional[GetAuthorizationCodeResponse]:
    """Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.

     With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization
    code that will allow you to call a Selling Partner API on behalf of a seller who has already
    authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an
    MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that
    the seller previously granted you. The operation returns an LWA authorization code that can be
    exchanged for a refresh token and access token representing authorization to call the Selling
    Partner API on the seller's behalf. By using this API, sellers who have already authorized you for
    Amazon MWS do not need to re-authorize you for the Selling Partner API.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 5 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        selling_partner_id (str):
        developer_id (str):
        mws_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizationCodeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            selling_partner_id=selling_partner_id,
            developer_id=developer_id,
            mws_auth_token=mws_auth_token,
        )
    ).parsed
