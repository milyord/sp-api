from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.marketplace import Marketplace
    from ..models.participation import Participation


T = TypeVar("T", bound="MarketplaceParticipation")


@attr.s(auto_attribs=True)
class MarketplaceParticipation:
    r"""
    Attributes:
        marketplace (Marketplace): Detailed information about an Amazon market where a seller can list items for sale
            and customers can view and purchase items.
        participation (Participation): Detailed information that is specific to a seller in a Marketplace.
    """

    marketplace: "Marketplace"
    participation: "Participation"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace = self.marketplace.to_dict()

        participation = self.participation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplace": marketplace,
                "participation": participation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.marketplace import Marketplace
        from ..models.participation import Participation

        d = src_dict.copy()
        marketplace = Marketplace.from_dict(d.pop("marketplace"))

        participation = Participation.from_dict(d.pop("participation"))

        result = cls(
            marketplace=marketplace,
            participation=participation,
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
