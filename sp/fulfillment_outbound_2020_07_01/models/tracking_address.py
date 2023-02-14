from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TrackingAddress")


@attr.s(auto_attribs=True)
class TrackingAddress:
    r"""Address information for tracking the package.

    Attributes:
        city (str): The city.
        state (str): The state.
        country (str): The country.
    """

    city: str
    state: str
    country: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city
        state = self.state
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "state": state,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city")

        state = d.pop("state")

        country = d.pop("country")

        result = cls(
            city=city,
            state=state,
            country=country,
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
