from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelData")


@attr.s(auto_attribs=True)
class LabelData:
    r"""Details of the shipment label.

    Attributes:
        content (str): This field will contain the Base64encoded string of the shipment label content.
        package_identifier (Union[Unset, str]): Identifier for the package. The first package will be 001, the second
            002, and so on. This number is used as a reference to refer to this package from the pallet level.
        tracking_number (Union[Unset, str]): Package tracking identifier from the shipping carrier.
        ship_method (Union[Unset, str]): Ship method to be used for shipping the order. Amazon defines Ship Method Codes
            indicating shipping carrier and shipment service level. Ship Method Codes are case and format sensitive. The
            same ship method code should returned on the shipment confirmation. Note that the Ship Method Codes are vendor
            specific and will be provided to each vendor during the implementation.
        ship_method_name (Union[Unset, str]): Shipping method name for internal reference.
    """

    content: str
    package_identifier: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    ship_method: Union[Unset, str] = UNSET
    ship_method_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        package_identifier = self.package_identifier
        tracking_number = self.tracking_number
        ship_method = self.ship_method
        ship_method_name = self.ship_method_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if package_identifier is not UNSET:
            field_dict["packageIdentifier"] = package_identifier
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if ship_method is not UNSET:
            field_dict["shipMethod"] = ship_method
        if ship_method_name is not UNSET:
            field_dict["shipMethodName"] = ship_method_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        package_identifier = d.pop("packageIdentifier", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        ship_method = d.pop("shipMethod", UNSET)

        ship_method_name = d.pop("shipMethodName", UNSET)

        result = cls(
            content=content,
            package_identifier=package_identifier,
            tracking_number=tracking_number,
            ship_method=ship_method,
            ship_method_name=ship_method_name,
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
