from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Participation")


@attr.s(auto_attribs=True)
class Participation:
    r"""Detailed information that is specific to a seller in a Marketplace.

    Attributes:
        is_participating (bool):
        has_suspended_listings (bool): Specifies if the seller has suspended listings. True if the seller Listing Status
            is set to Inactive, otherwise False.
    """

    is_participating: bool
    has_suspended_listings: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_participating = self.is_participating
        has_suspended_listings = self.has_suspended_listings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isParticipating": is_participating,
                "hasSuspendedListings": has_suspended_listings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_participating = d.pop("isParticipating")

        has_suspended_listings = d.pop("hasSuspendedListings")

        result = cls(
            is_participating=is_participating,
            has_suspended_listings=has_suspended_listings,
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
