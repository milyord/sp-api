from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.prep_instruction import PrepInstruction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="AmazonPrepFeesDetails")


@attr.s(auto_attribs=True)
class AmazonPrepFeesDetails:
    r"""The fees for Amazon to prep goods for shipment.

    Attributes:
        prep_instruction (Union[Unset, PrepInstruction]): Preparation instructions for shipping an item to Amazon's
            fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network,
            see the Seller Central Help for your marketplace.
        fee_per_unit (Union[Unset, Amount]): The monetary value.
    """

    prep_instruction: Union[Unset, PrepInstruction] = UNSET
    fee_per_unit: Union[Unset, "Amount"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prep_instruction: Union[Unset, str] = UNSET
        if not isinstance(self.prep_instruction, Unset):
            prep_instruction = self.prep_instruction.value

        fee_per_unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_per_unit, Unset):
            fee_per_unit = self.fee_per_unit.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prep_instruction is not UNSET:
            field_dict["PrepInstruction"] = prep_instruction
        if fee_per_unit is not UNSET:
            field_dict["FeePerUnit"] = fee_per_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount import Amount

        d = src_dict.copy()
        _prep_instruction = d.pop("PrepInstruction", UNSET)
        prep_instruction: Union[Unset, PrepInstruction]
        if isinstance(_prep_instruction, Unset):
            prep_instruction = UNSET
        else:
            prep_instruction = PrepInstruction(_prep_instruction)

        _fee_per_unit = d.pop("FeePerUnit", UNSET)
        fee_per_unit: Union[Unset, Amount]
        if isinstance(_fee_per_unit, Unset):
            fee_per_unit = UNSET
        else:
            fee_per_unit = Amount.from_dict(_fee_per_unit)

        result = cls(
            prep_instruction=prep_instruction,
            fee_per_unit=fee_per_unit,
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
