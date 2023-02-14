from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="NonPartneredLtlDataInput")


@attr.s(auto_attribs=True)
class NonPartneredLtlDataInput:
    r"""Information that you provide to Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by a carrier
    that has not partnered with Amazon.

        Attributes:
            carrier_name (str): The carrier that you are using for the inbound shipment.
            pro_number (str): The PRO number ("progressive number" or "progressive ID") assigned to the shipment by the
                carrier.
    """

    carrier_name: str
    pro_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_name = self.carrier_name
        pro_number = self.pro_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CarrierName": carrier_name,
                "ProNumber": pro_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier_name = d.pop("CarrierName")

        pro_number = d.pop("ProNumber")

        result = cls(
            carrier_name=carrier_name,
            pro_number=pro_number,
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
