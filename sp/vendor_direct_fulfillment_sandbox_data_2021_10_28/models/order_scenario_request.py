from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.party_identification import PartyIdentification


T = TypeVar("T", bound="OrderScenarioRequest")


@attr.s(auto_attribs=True)
class OrderScenarioRequest:
    r"""The party identifiers required to generate the test data.

    Attributes:
        selling_party (PartyIdentification): The identification object for the party information. For example, warehouse
            code or vendor code. Please refer to specific party for more details.
        ship_from_party (PartyIdentification): The identification object for the party information. For example,
            warehouse code or vendor code. Please refer to specific party for more details.
    """

    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        selling_party = self.selling_party.to_dict()

        ship_from_party = self.ship_from_party.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellingParty": selling_party,
                "shipFromParty": ship_from_party,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.party_identification import PartyIdentification

        d = src_dict.copy()
        selling_party = PartyIdentification.from_dict(d.pop("sellingParty"))

        ship_from_party = PartyIdentification.from_dict(d.pop("shipFromParty"))

        result = cls(
            selling_party=selling_party,
            ship_from_party=ship_from_party,
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
