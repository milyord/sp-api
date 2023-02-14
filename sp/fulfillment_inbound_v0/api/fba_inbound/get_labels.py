from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_labels_label_type import GetLabelsLabelType
from ...models.get_labels_page_type import GetLabelsPageType
from ...models.get_labels_response import GetLabelsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    shipment_id: str,
    *,
    client: Client,
    page_type: GetLabelsPageType,
    label_type: GetLabelsLabelType,
    number_of_packages: Union[Unset, None, int] = UNSET,
    package_labels_to_print: Union[Unset, None, List[str]] = UNSET,
    number_of_pallets: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_start_index: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/shipments/{shipmentId}/labels".format(client.base_url, shipmentId=shipment_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_page_type = page_type.value

    params["PageType"] = json_page_type

    json_label_type = label_type.value

    params["LabelType"] = json_label_type

    params["NumberOfPackages"] = number_of_packages

    json_package_labels_to_print: Union[Unset, None, List[str]] = UNSET
    if not isinstance(package_labels_to_print, Unset):
        if package_labels_to_print is None:
            json_package_labels_to_print = None
        else:
            json_package_labels_to_print = package_labels_to_print

    params["PackageLabelsToPrint"] = json_package_labels_to_print

    params["NumberOfPallets"] = number_of_pallets

    params["PageSize"] = page_size

    params["PageStartIndex"] = page_start_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetLabelsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetLabelsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetLabelsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetLabelsResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetLabelsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetLabelsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetLabelsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetLabelsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetLabelsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetLabelsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shipment_id: str,
    *,
    client: Client,
    page_type: GetLabelsPageType,
    label_type: GetLabelsLabelType,
    number_of_packages: Union[Unset, None, int] = UNSET,
    package_labels_to_print: Union[Unset, None, List[str]] = UNSET,
    number_of_pallets: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_start_index: Union[Unset, None, int] = UNSET,
) -> Response[GetLabelsResponse]:
    """Returns package/pallet labels for faster and more accurate shipment processing at the Amazon
    fulfillment center.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        page_type (GetLabelsPageType):
        label_type (GetLabelsLabelType):
        number_of_packages (Union[Unset, None, int]):
        package_labels_to_print (Union[Unset, None, List[str]]):
        number_of_pallets (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        page_start_index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelsResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        client=client,
        page_type=page_type,
        label_type=label_type,
        number_of_packages=number_of_packages,
        package_labels_to_print=package_labels_to_print,
        number_of_pallets=number_of_pallets,
        page_size=page_size,
        page_start_index=page_start_index,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    shipment_id: str,
    *,
    client: Client,
    page_type: GetLabelsPageType,
    label_type: GetLabelsLabelType,
    number_of_packages: Union[Unset, None, int] = UNSET,
    package_labels_to_print: Union[Unset, None, List[str]] = UNSET,
    number_of_pallets: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_start_index: Union[Unset, None, int] = UNSET,
) -> Optional[GetLabelsResponse]:
    """Returns package/pallet labels for faster and more accurate shipment processing at the Amazon
    fulfillment center.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        page_type (GetLabelsPageType):
        label_type (GetLabelsLabelType):
        number_of_packages (Union[Unset, None, int]):
        package_labels_to_print (Union[Unset, None, List[str]]):
        number_of_pallets (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        page_start_index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelsResponse]
    """

    return sync_detailed(
        shipment_id=shipment_id,
        client=client,
        page_type=page_type,
        label_type=label_type,
        number_of_packages=number_of_packages,
        package_labels_to_print=package_labels_to_print,
        number_of_pallets=number_of_pallets,
        page_size=page_size,
        page_start_index=page_start_index,
    ).parsed


async def asyncio_detailed(
    shipment_id: str,
    *,
    client: Client,
    page_type: GetLabelsPageType,
    label_type: GetLabelsLabelType,
    number_of_packages: Union[Unset, None, int] = UNSET,
    package_labels_to_print: Union[Unset, None, List[str]] = UNSET,
    number_of_pallets: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_start_index: Union[Unset, None, int] = UNSET,
) -> Response[GetLabelsResponse]:
    """Returns package/pallet labels for faster and more accurate shipment processing at the Amazon
    fulfillment center.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        page_type (GetLabelsPageType):
        label_type (GetLabelsLabelType):
        number_of_packages (Union[Unset, None, int]):
        package_labels_to_print (Union[Unset, None, List[str]]):
        number_of_pallets (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        page_start_index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelsResponse]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        client=client,
        page_type=page_type,
        label_type=label_type,
        number_of_packages=number_of_packages,
        package_labels_to_print=package_labels_to_print,
        number_of_pallets=number_of_pallets,
        page_size=page_size,
        page_start_index=page_start_index,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shipment_id: str,
    *,
    client: Client,
    page_type: GetLabelsPageType,
    label_type: GetLabelsLabelType,
    number_of_packages: Union[Unset, None, int] = UNSET,
    package_labels_to_print: Union[Unset, None, List[str]] = UNSET,
    number_of_pallets: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_start_index: Union[Unset, None, int] = UNSET,
) -> Optional[GetLabelsResponse]:
    """Returns package/pallet labels for faster and more accurate shipment processing at the Amazon
    fulfillment center.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_id (str):
        page_type (GetLabelsPageType):
        label_type (GetLabelsLabelType):
        number_of_packages (Union[Unset, None, int]):
        package_labels_to_print (Union[Unset, None, List[str]]):
        number_of_pallets (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        page_start_index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelsResponse]
    """

    return (
        await asyncio_detailed(
            shipment_id=shipment_id,
            client=client,
            page_type=page_type,
            label_type=label_type,
            number_of_packages=number_of_packages,
            package_labels_to_print=package_labels_to_print,
            number_of_pallets=number_of_pallets,
            page_size=page_size,
            page_start_index=page_start_index,
        )
    ).parsed
