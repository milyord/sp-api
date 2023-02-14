from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.restricted_resource_method import RestrictedResourceMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrictedResource")


@attr.s(auto_attribs=True)
class RestrictedResource:
    r"""Model of a restricted resource.

    Attributes:
        method (RestrictedResourceMethod): The HTTP method in the restricted resource.
        path (str): The path in the restricted resource. Here are some path examples:
            - ```/orders/v0/orders```. For getting an RDT for the getOrders operation of the Orders API. For bulk orders.
            - ```/orders/v0/orders/123-1234567-1234567```. For getting an RDT for the getOrder operation of the Orders API.
            For a specific order.
            - ```/orders/v0/orders/123-1234567-1234567/orderItems```. For getting an RDT for the getOrderItems operation of
            the Orders API. For the order items in a specific order.
            - ```/mfn/v0/shipments/FBA1234ABC5D```. For getting an RDT for the getShipment operation of the Shipping API.
            For a specific shipment.
            - ```/mfn/v0/shipments/{shipmentId}```. For getting an RDT for the getShipment operation of the Shipping API.
            For any of a selling partner's shipments that you specify when you call the getShipment operation.
        data_elements (Union[Unset, List[str]]): Indicates the type of Personally Identifiable Information requested.
            This parameter is required only when getting an RDT for use with the getOrder, getOrders, or getOrderItems
            operation of the Orders API. For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-
            guide). Possible values include:
            - **buyerInfo**. On the order level this includes general identifying information about the buyer and tax-
            related information. On the order item level this includes gift wrap information and custom order information,
            if available.
            - **shippingAddress**. This includes information for fulfilling orders.
            - **buyerTaxInformation**. This includes information for issuing tax invoices.
    """

    method: RestrictedResourceMethod
    path: str
    data_elements: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method.value

        path = self.path
        data_elements: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_elements, Unset):
            data_elements = self.data_elements

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "path": path,
            }
        )
        if data_elements is not UNSET:
            field_dict["dataElements"] = data_elements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = RestrictedResourceMethod(d.pop("method"))

        path = d.pop("path")

        data_elements = cast(List[str], d.pop("dataElements", UNSET))

        result = cls(
            method=method,
            path=path,
            data_elements=data_elements,
        )

        result.additional_properties = d
        return result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
