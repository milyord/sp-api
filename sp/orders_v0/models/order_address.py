from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="OrderAddress")


@attr.s(auto_attribs=True)
class OrderAddress:
    r"""The shipping address for the order.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        shipping_address (Union[Unset, Address]): The shipping address for the order.
    """

    amazon_order_id: str
    shipping_address: Union[Unset, "Address"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AmazonOrderId": amazon_order_id,
            }
        )
        if shipping_address is not UNSET:
            field_dict["ShippingAddress"] = shipping_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId")

        _shipping_address = d.pop("ShippingAddress", UNSET)
        shipping_address: Union[Unset, Address]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = Address.from_dict(_shipping_address)

        result = cls(
            amazon_order_id=amazon_order_id,
            shipping_address=shipping_address,
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
