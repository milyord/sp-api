from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.researching_quantity_entry_name import ResearchingQuantityEntryName

T = TypeVar("T", bound="ResearchingQuantityEntry")


@attr.s(auto_attribs=True)
class ResearchingQuantityEntry:
    r"""The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers.

    Attributes:
        name (ResearchingQuantityEntryName): The duration of the research.
        quantity (int): The number of units.
    """

    name: ResearchingQuantityEntryName
    quantity: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.value

        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = ResearchingQuantityEntryName(d.pop("name"))

        quantity = d.pop("quantity")

        result = cls(
            name=name,
            quantity=quantity,
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
