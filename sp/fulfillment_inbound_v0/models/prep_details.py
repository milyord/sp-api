from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.prep_instruction import PrepInstruction
from ..models.prep_owner import PrepOwner

T = TypeVar("T", bound="PrepDetails")


@attr.s(auto_attribs=True)
class PrepDetails:
    r"""Preparation instructions and who is responsible for the preparation.

    Attributes:
        prep_instruction (PrepInstruction): Preparation instructions for shipping an item to Amazon's fulfillment
            network. For more information about preparing items for shipment to Amazon's fulfillment network, see the Seller
            Central Help for your marketplace.
        prep_owner (PrepOwner): Indicates who will prepare the item.
    """

    prep_instruction: PrepInstruction
    prep_owner: PrepOwner
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prep_instruction = self.prep_instruction.value

        prep_owner = self.prep_owner.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PrepInstruction": prep_instruction,
                "PrepOwner": prep_owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prep_instruction = PrepInstruction(d.pop("PrepInstruction"))

        prep_owner = PrepOwner(d.pop("PrepOwner"))

        result = cls(
            prep_instruction=prep_instruction,
            prep_owner=prep_owner,
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
