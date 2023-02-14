from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_list import ErrorList
from ...models.get_definitions_product_type_locale import GetDefinitionsProductTypeLocale
from ...models.get_definitions_product_type_requirements import GetDefinitionsProductTypeRequirements
from ...models.get_definitions_product_type_requirements_enforced import GetDefinitionsProductTypeRequirementsEnforced
from ...models.product_type_definition import ProductTypeDefinition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_type: str,
    *,
    client: Client,
    seller_id: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    product_type_version: Union[Unset, None, str] = "LATEST",
    requirements: Union[
        Unset, None, GetDefinitionsProductTypeRequirements
    ] = GetDefinitionsProductTypeRequirements.LISTING,
    requirements_enforced: Union[
        Unset, None, GetDefinitionsProductTypeRequirementsEnforced
    ] = GetDefinitionsProductTypeRequirementsEnforced.ENFORCED,
    locale: Union[Unset, None, GetDefinitionsProductTypeLocale] = GetDefinitionsProductTypeLocale.DEFAULT,
) -> Dict[str, Any]:
    url = "{}/definitions/2020-09-01/productTypes/{productType}".format(client.base_url, productType=product_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sellerId"] = seller_id

    json_marketplace_ids = marketplace_ids

    params["marketplaceIds"] = json_marketplace_ids

    params["productTypeVersion"] = product_type_version

    json_requirements: Union[Unset, None, str] = UNSET
    if not isinstance(requirements, Unset):
        json_requirements = requirements.value if requirements else None

    params["requirements"] = json_requirements

    json_requirements_enforced: Union[Unset, None, str] = UNSET
    if not isinstance(requirements_enforced, Unset):
        json_requirements_enforced = requirements_enforced.value if requirements_enforced else None

    params["requirementsEnforced"] = json_requirements_enforced

    json_locale: Union[Unset, None, str] = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value if locale else None

    params["locale"] = json_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorList, ProductTypeDefinition]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProductTypeDefinition.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorList, ProductTypeDefinition]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_type: str,
    *,
    client: Client,
    seller_id: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    product_type_version: Union[Unset, None, str] = "LATEST",
    requirements: Union[
        Unset, None, GetDefinitionsProductTypeRequirements
    ] = GetDefinitionsProductTypeRequirements.LISTING,
    requirements_enforced: Union[
        Unset, None, GetDefinitionsProductTypeRequirementsEnforced
    ] = GetDefinitionsProductTypeRequirementsEnforced.ENFORCED,
    locale: Union[Unset, None, GetDefinitionsProductTypeLocale] = GetDefinitionsProductTypeLocale.DEFAULT,
) -> Response[Union[ErrorList, ProductTypeDefinition]]:
    """Retrieve an Amazon product type definition.

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
        product_type (str):
        seller_id (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        product_type_version (Union[Unset, None, str]):  Default: 'LATEST'.
        requirements (Union[Unset, None, GetDefinitionsProductTypeRequirements]):  Default:
            GetDefinitionsProductTypeRequirements.LISTING.
        requirements_enforced (Union[Unset, None, GetDefinitionsProductTypeRequirementsEnforced]):
            Default: GetDefinitionsProductTypeRequirementsEnforced.ENFORCED.
        locale (Union[Unset, None, GetDefinitionsProductTypeLocale]):  Default:
            GetDefinitionsProductTypeLocale.DEFAULT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeDefinition]]
    """

    kwargs = _get_kwargs(
        product_type=product_type,
        client=client,
        seller_id=seller_id,
        marketplace_ids=marketplace_ids,
        product_type_version=product_type_version,
        requirements=requirements,
        requirements_enforced=requirements_enforced,
        locale=locale,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_type: str,
    *,
    client: Client,
    seller_id: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    product_type_version: Union[Unset, None, str] = "LATEST",
    requirements: Union[
        Unset, None, GetDefinitionsProductTypeRequirements
    ] = GetDefinitionsProductTypeRequirements.LISTING,
    requirements_enforced: Union[
        Unset, None, GetDefinitionsProductTypeRequirementsEnforced
    ] = GetDefinitionsProductTypeRequirementsEnforced.ENFORCED,
    locale: Union[Unset, None, GetDefinitionsProductTypeLocale] = GetDefinitionsProductTypeLocale.DEFAULT,
) -> Optional[Union[ErrorList, ProductTypeDefinition]]:
    """Retrieve an Amazon product type definition.

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
        product_type (str):
        seller_id (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        product_type_version (Union[Unset, None, str]):  Default: 'LATEST'.
        requirements (Union[Unset, None, GetDefinitionsProductTypeRequirements]):  Default:
            GetDefinitionsProductTypeRequirements.LISTING.
        requirements_enforced (Union[Unset, None, GetDefinitionsProductTypeRequirementsEnforced]):
            Default: GetDefinitionsProductTypeRequirementsEnforced.ENFORCED.
        locale (Union[Unset, None, GetDefinitionsProductTypeLocale]):  Default:
            GetDefinitionsProductTypeLocale.DEFAULT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeDefinition]]
    """

    return sync_detailed(
        product_type=product_type,
        client=client,
        seller_id=seller_id,
        marketplace_ids=marketplace_ids,
        product_type_version=product_type_version,
        requirements=requirements,
        requirements_enforced=requirements_enforced,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    product_type: str,
    *,
    client: Client,
    seller_id: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    product_type_version: Union[Unset, None, str] = "LATEST",
    requirements: Union[
        Unset, None, GetDefinitionsProductTypeRequirements
    ] = GetDefinitionsProductTypeRequirements.LISTING,
    requirements_enforced: Union[
        Unset, None, GetDefinitionsProductTypeRequirementsEnforced
    ] = GetDefinitionsProductTypeRequirementsEnforced.ENFORCED,
    locale: Union[Unset, None, GetDefinitionsProductTypeLocale] = GetDefinitionsProductTypeLocale.DEFAULT,
) -> Response[Union[ErrorList, ProductTypeDefinition]]:
    """Retrieve an Amazon product type definition.

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
        product_type (str):
        seller_id (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        product_type_version (Union[Unset, None, str]):  Default: 'LATEST'.
        requirements (Union[Unset, None, GetDefinitionsProductTypeRequirements]):  Default:
            GetDefinitionsProductTypeRequirements.LISTING.
        requirements_enforced (Union[Unset, None, GetDefinitionsProductTypeRequirementsEnforced]):
            Default: GetDefinitionsProductTypeRequirementsEnforced.ENFORCED.
        locale (Union[Unset, None, GetDefinitionsProductTypeLocale]):  Default:
            GetDefinitionsProductTypeLocale.DEFAULT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeDefinition]]
    """

    kwargs = _get_kwargs(
        product_type=product_type,
        client=client,
        seller_id=seller_id,
        marketplace_ids=marketplace_ids,
        product_type_version=product_type_version,
        requirements=requirements,
        requirements_enforced=requirements_enforced,
        locale=locale,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_type: str,
    *,
    client: Client,
    seller_id: Union[Unset, None, str] = UNSET,
    marketplace_ids: List[str],
    product_type_version: Union[Unset, None, str] = "LATEST",
    requirements: Union[
        Unset, None, GetDefinitionsProductTypeRequirements
    ] = GetDefinitionsProductTypeRequirements.LISTING,
    requirements_enforced: Union[
        Unset, None, GetDefinitionsProductTypeRequirementsEnforced
    ] = GetDefinitionsProductTypeRequirementsEnforced.ENFORCED,
    locale: Union[Unset, None, GetDefinitionsProductTypeLocale] = GetDefinitionsProductTypeLocale.DEFAULT,
) -> Optional[Union[ErrorList, ProductTypeDefinition]]:
    """Retrieve an Amazon product type definition.

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
        product_type (str):
        seller_id (Union[Unset, None, str]):
        marketplace_ids (List[str]):
        product_type_version (Union[Unset, None, str]):  Default: 'LATEST'.
        requirements (Union[Unset, None, GetDefinitionsProductTypeRequirements]):  Default:
            GetDefinitionsProductTypeRequirements.LISTING.
        requirements_enforced (Union[Unset, None, GetDefinitionsProductTypeRequirementsEnforced]):
            Default: GetDefinitionsProductTypeRequirementsEnforced.ENFORCED.
        locale (Union[Unset, None, GetDefinitionsProductTypeLocale]):  Default:
            GetDefinitionsProductTypeLocale.DEFAULT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorList, ProductTypeDefinition]]
    """

    return (
        await asyncio_detailed(
            product_type=product_type,
            client=client,
            seller_id=seller_id,
            marketplace_ids=marketplace_ids,
            product_type_version=product_type_version,
            requirements=requirements,
            requirements_enforced=requirements_enforced,
            locale=locale,
        )
    ).parsed
