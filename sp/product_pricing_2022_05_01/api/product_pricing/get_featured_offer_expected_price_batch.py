from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.errors import Errors
from ...models.get_featured_offer_expected_price_batch_request import GetFeaturedOfferExpectedPriceBatchRequest
from ...models.get_featured_offer_expected_price_batch_response import GetFeaturedOfferExpectedPriceBatchResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: GetFeaturedOfferExpectedPriceBatchRequest,
) -> Dict[str, Any]:
    url = "{}/batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice".format(client.base_url)

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
) -> Optional[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFeaturedOfferExpectedPriceBatchResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Errors.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = Errors.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Errors.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: GetFeaturedOfferExpectedPriceBatchRequest,
) -> Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]:
    """Returns the set of responses that correspond to the batched list of up to 40 requests defined in the
    request body. The response for each successful (HTTP status code 200) request in the set includes
    the computed listing price at or below which a seller can expect to become the featured offer
    (before applicable promotions). This is called the featured offer expected price (FOEP). Featured
    offer is not guaranteed, because competing offers may change, and different offers may be featured
    based on other factors, including fulfillment capabilities to a specific customer. The response to
    an unsuccessful request includes the available error text.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.033 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (GetFeaturedOfferExpectedPriceBatchRequest): The request body for the
            getFeaturedOfferExpectedPriceBatch operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]
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
    json_body: GetFeaturedOfferExpectedPriceBatchRequest,
) -> Optional[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]:
    """Returns the set of responses that correspond to the batched list of up to 40 requests defined in the
    request body. The response for each successful (HTTP status code 200) request in the set includes
    the computed listing price at or below which a seller can expect to become the featured offer
    (before applicable promotions). This is called the featured offer expected price (FOEP). Featured
    offer is not guaranteed, because competing offers may change, and different offers may be featured
    based on other factors, including fulfillment capabilities to a specific customer. The response to
    an unsuccessful request includes the available error text.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.033 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (GetFeaturedOfferExpectedPriceBatchRequest): The request body for the
            getFeaturedOfferExpectedPriceBatch operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: GetFeaturedOfferExpectedPriceBatchRequest,
) -> Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]:
    """Returns the set of responses that correspond to the batched list of up to 40 requests defined in the
    request body. The response for each successful (HTTP status code 200) request in the set includes
    the computed listing price at or below which a seller can expect to become the featured offer
    (before applicable promotions). This is called the featured offer expected price (FOEP). Featured
    offer is not guaranteed, because competing offers may change, and different offers may be featured
    based on other factors, including fulfillment capabilities to a specific customer. The response to
    an unsuccessful request includes the available error text.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.033 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (GetFeaturedOfferExpectedPriceBatchRequest): The request body for the
            getFeaturedOfferExpectedPriceBatch operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]
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
    json_body: GetFeaturedOfferExpectedPriceBatchRequest,
) -> Optional[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]:
    """Returns the set of responses that correspond to the batched list of up to 40 requests defined in the
    request body. The response for each successful (HTTP status code 200) request in the set includes
    the computed listing price at or below which a seller can expect to become the featured offer
    (before applicable promotions). This is called the featured offer expected price (FOEP). Featured
    offer is not guaranteed, because competing offers may change, and different offers may be featured
    based on other factors, including fulfillment capabilities to a specific customer. The response to
    an unsuccessful request includes the available error text.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 0.033 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to
    the requested operation, when available. The table above indicates the default rate and burst values
    for this operation. Selling partners whose business demands require higher throughput may see higher
    rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits
    in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

    Args:
        json_body (GetFeaturedOfferExpectedPriceBatchRequest): The request body for the
            getFeaturedOfferExpectedPriceBatch operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, GetFeaturedOfferExpectedPriceBatchResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
