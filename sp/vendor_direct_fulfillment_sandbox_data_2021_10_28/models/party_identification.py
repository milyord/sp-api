from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PartyIdentification")


@attr.s(auto_attribs=True)
class PartyIdentification:
    r"""The identification object for the party information. For example, warehouse code or vendor code. Please refer to
    specific party for more details.

        Attributes:
            party_id (str): Assigned identification for the party. For example, warehouse code or vendor code. Please refer
                to specific party for more details.
    """

    party_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        party_id = self.party_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyId": party_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        party_id = d.pop("partyId")

        result = cls(
            party_id=party_id,
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
