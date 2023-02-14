from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TermsAndConditionsNotAcceptedCarrier")


@attr.s(auto_attribs=True)
class TermsAndConditionsNotAcceptedCarrier:
    r"""A carrier whose terms and conditions have not been accepted by the seller.

    Attributes:
        carrier_name (str): The name of the carrier.
    """

    carrier_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carrier_name = self.carrier_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CarrierName": carrier_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        carrier_name = d.pop("CarrierName")

        result = cls(
            carrier_name=carrier_name,
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
