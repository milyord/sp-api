from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="GetAdditionalSellerInputsRequest")


@attr.s(auto_attribs=True)
class GetAdditionalSellerInputsRequest:
    r"""Request schema.

    Attributes:
        shipping_service_id (str): An Amazon-defined shipping service identifier.
        ship_from_address (Address): The postal address information.
        order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
    """

    shipping_service_id: str
    ship_from_address: "Address"
    order_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_service_id = self.shipping_service_id
        ship_from_address = self.ship_from_address.to_dict()

        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShippingServiceId": shipping_service_id,
                "ShipFromAddress": ship_from_address,
                "OrderId": order_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        shipping_service_id = d.pop("ShippingServiceId")

        ship_from_address = Address.from_dict(d.pop("ShipFromAddress"))

        order_id = d.pop("OrderId")

        result = cls(
            shipping_service_id=shipping_service_id,
            ship_from_address=ship_from_address,
            order_id=order_id,
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
