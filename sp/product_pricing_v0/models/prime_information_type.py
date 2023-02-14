from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PrimeInformationType")


@attr.s(auto_attribs=True)
class PrimeInformationType:
    r"""Amazon Prime information.

    Attributes:
        is_prime (bool): Indicates whether the offer is an Amazon Prime offer.
        is_national_prime (bool): Indicates whether the offer is an Amazon Prime offer throughout the entire marketplace
            where it is listed.
    """

    is_prime: bool
    is_national_prime: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_prime = self.is_prime
        is_national_prime = self.is_national_prime

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IsPrime": is_prime,
                "IsNationalPrime": is_national_prime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_prime = d.pop("IsPrime")

        is_national_prime = d.pop("IsNationalPrime")

        result = cls(
            is_prime=is_prime,
            is_national_prime=is_national_prime,
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
