import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_shipments_query_type import GetShipmentsQueryType
from ...models.get_shipments_response import GetShipmentsResponse
from ...models.get_shipments_shipment_status_list_item import GetShipmentsShipmentStatusListItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    shipment_status_list: Union[Unset, None, List[GetShipmentsShipmentStatusListItem]] = UNSET,
    shipment_id_list: Union[Unset, None, List[str]] = UNSET,
    last_updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    query_type: GetShipmentsQueryType,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_id: str,
) -> Dict[str, Any]:
    url = "{}/fba/inbound/v0/shipments".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_shipment_status_list: Union[Unset, None, List[str]] = UNSET
    if not isinstance(shipment_status_list, Unset):
        if shipment_status_list is None:
            json_shipment_status_list = None
        else:
            json_shipment_status_list = []
            for shipment_status_list_item_data in shipment_status_list:
                shipment_status_list_item = shipment_status_list_item_data.value

                json_shipment_status_list.append(shipment_status_list_item)

    params["ShipmentStatusList"] = json_shipment_status_list

    json_shipment_id_list: Union[Unset, None, List[str]] = UNSET
    if not isinstance(shipment_id_list, Unset):
        if shipment_id_list is None:
            json_shipment_id_list = None
        else:
            json_shipment_id_list = shipment_id_list

    params["ShipmentIdList"] = json_shipment_id_list

    json_last_updated_after: Union[Unset, None, str] = UNSET
    if not isinstance(last_updated_after, Unset):
        json_last_updated_after = last_updated_after.isoformat() if last_updated_after else None

    params["LastUpdatedAfter"] = json_last_updated_after

    json_last_updated_before: Union[Unset, None, str] = UNSET
    if not isinstance(last_updated_before, Unset):
        json_last_updated_before = last_updated_before.isoformat() if last_updated_before else None

    params["LastUpdatedBefore"] = json_last_updated_before

    json_query_type = query_type.value

    params["QueryType"] = json_query_type

    params["NextToken"] = next_token

    params["MarketplaceId"] = marketplace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetShipmentsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetShipmentsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetShipmentsResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetShipmentsResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetShipmentsResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetShipmentsResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = GetShipmentsResponse.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetShipmentsResponse.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = GetShipmentsResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetShipmentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    shipment_status_list: Union[Unset, None, List[GetShipmentsShipmentStatusListItem]] = UNSET,
    shipment_id_list: Union[Unset, None, List[str]] = UNSET,
    last_updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    query_type: GetShipmentsQueryType,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_id: str,
) -> Response[GetShipmentsResponse]:
    """Returns a list of inbound shipments based on criteria that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_status_list (Union[Unset, None, List[GetShipmentsShipmentStatusListItem]]):
        shipment_id_list (Union[Unset, None, List[str]]):
        last_updated_after (Union[Unset, None, datetime.datetime]):
        last_updated_before (Union[Unset, None, datetime.datetime]):
        query_type (GetShipmentsQueryType):
        next_token (Union[Unset, None, str]):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipmentsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        shipment_status_list=shipment_status_list,
        shipment_id_list=shipment_id_list,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        query_type=query_type,
        next_token=next_token,
        marketplace_id=marketplace_id,
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
    shipment_status_list: Union[Unset, None, List[GetShipmentsShipmentStatusListItem]] = UNSET,
    shipment_id_list: Union[Unset, None, List[str]] = UNSET,
    last_updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    query_type: GetShipmentsQueryType,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_id: str,
) -> Optional[GetShipmentsResponse]:
    """Returns a list of inbound shipments based on criteria that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_status_list (Union[Unset, None, List[GetShipmentsShipmentStatusListItem]]):
        shipment_id_list (Union[Unset, None, List[str]]):
        last_updated_after (Union[Unset, None, datetime.datetime]):
        last_updated_before (Union[Unset, None, datetime.datetime]):
        query_type (GetShipmentsQueryType):
        next_token (Union[Unset, None, str]):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipmentsResponse]
    """

    return sync_detailed(
        client=client,
        shipment_status_list=shipment_status_list,
        shipment_id_list=shipment_id_list,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        query_type=query_type,
        next_token=next_token,
        marketplace_id=marketplace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    shipment_status_list: Union[Unset, None, List[GetShipmentsShipmentStatusListItem]] = UNSET,
    shipment_id_list: Union[Unset, None, List[str]] = UNSET,
    last_updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    query_type: GetShipmentsQueryType,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_id: str,
) -> Response[GetShipmentsResponse]:
    """Returns a list of inbound shipments based on criteria that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_status_list (Union[Unset, None, List[GetShipmentsShipmentStatusListItem]]):
        shipment_id_list (Union[Unset, None, List[str]]):
        last_updated_after (Union[Unset, None, datetime.datetime]):
        last_updated_before (Union[Unset, None, datetime.datetime]):
        query_type (GetShipmentsQueryType):
        next_token (Union[Unset, None, str]):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipmentsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        shipment_status_list=shipment_status_list,
        shipment_id_list=shipment_id_list,
        last_updated_after=last_updated_after,
        last_updated_before=last_updated_before,
        query_type=query_type,
        next_token=next_token,
        marketplace_id=marketplace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl, auth=client.get_auth()) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    shipment_status_list: Union[Unset, None, List[GetShipmentsShipmentStatusListItem]] = UNSET,
    shipment_id_list: Union[Unset, None, List[str]] = UNSET,
    last_updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    query_type: GetShipmentsQueryType,
    next_token: Union[Unset, None, str] = UNSET,
    marketplace_id: str,
) -> Optional[GetShipmentsResponse]:
    """Returns a list of inbound shipments based on criteria that you specify.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 2 | 30 |

    For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

    Args:
        shipment_status_list (Union[Unset, None, List[GetShipmentsShipmentStatusListItem]]):
        shipment_id_list (Union[Unset, None, List[str]]):
        last_updated_after (Union[Unset, None, datetime.datetime]):
        last_updated_before (Union[Unset, None, datetime.datetime]):
        query_type (GetShipmentsQueryType):
        next_token (Union[Unset, None, str]):
        marketplace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipmentsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            shipment_status_list=shipment_status_list,
            shipment_id_list=shipment_id_list,
            last_updated_after=last_updated_after,
            last_updated_before=last_updated_before,
            query_type=query_type,
            next_token=next_token,
            marketplace_id=marketplace_id,
        )
    ).parsed
