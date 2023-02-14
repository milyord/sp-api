from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.barcode_instruction import BarcodeInstruction
from ..models.prep_guidance import PrepGuidance
from ..models.prep_instruction import PrepInstruction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ASINPrepInstructions")


@attr.s(auto_attribs=True)
class ASINPrepInstructions:
    r"""Item preparation instructions to help with item sourcing decisions.

    Attributes:
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN) of the item.
        barcode_instruction (Union[Unset, BarcodeInstruction]): Labeling requirements for the item. For more information
            about FBA labeling requirements, see the Seller Central Help for your marketplace.
        prep_guidance (Union[Unset, PrepGuidance]): Item preparation instructions.
        prep_instruction_list (Union[Unset, List[PrepInstruction]]): A list of preparation instructions to help with
            item sourcing decisions.
    """

    asin: Union[Unset, str] = UNSET
    barcode_instruction: Union[Unset, BarcodeInstruction] = UNSET
    prep_guidance: Union[Unset, PrepGuidance] = UNSET
    prep_instruction_list: Union[Unset, List[PrepInstruction]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        barcode_instruction: Union[Unset, str] = UNSET
        if not isinstance(self.barcode_instruction, Unset):
            barcode_instruction = self.barcode_instruction.value

        prep_guidance: Union[Unset, str] = UNSET
        if not isinstance(self.prep_guidance, Unset):
            prep_guidance = self.prep_guidance.value

        prep_instruction_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.prep_instruction_list, Unset):
            prep_instruction_list = []
            for componentsschemas_prep_instruction_list_item_data in self.prep_instruction_list:
                componentsschemas_prep_instruction_list_item = componentsschemas_prep_instruction_list_item_data.value

                prep_instruction_list.append(componentsschemas_prep_instruction_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asin is not UNSET:
            field_dict["ASIN"] = asin
        if barcode_instruction is not UNSET:
            field_dict["BarcodeInstruction"] = barcode_instruction
        if prep_guidance is not UNSET:
            field_dict["PrepGuidance"] = prep_guidance
        if prep_instruction_list is not UNSET:
            field_dict["PrepInstructionList"] = prep_instruction_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asin = d.pop("ASIN", UNSET)

        _barcode_instruction = d.pop("BarcodeInstruction", UNSET)
        barcode_instruction: Union[Unset, BarcodeInstruction]
        if isinstance(_barcode_instruction, Unset):
            barcode_instruction = UNSET
        else:
            barcode_instruction = BarcodeInstruction(_barcode_instruction)

        _prep_guidance = d.pop("PrepGuidance", UNSET)
        prep_guidance: Union[Unset, PrepGuidance]
        if isinstance(_prep_guidance, Unset):
            prep_guidance = UNSET
        else:
            prep_guidance = PrepGuidance(_prep_guidance)

        prep_instruction_list = []
        _prep_instruction_list = d.pop("PrepInstructionList", UNSET)
        for componentsschemas_prep_instruction_list_item_data in _prep_instruction_list or []:
            componentsschemas_prep_instruction_list_item = PrepInstruction(
                componentsschemas_prep_instruction_list_item_data
            )

            prep_instruction_list.append(componentsschemas_prep_instruction_list_item)

        result = cls(
            asin=asin,
            barcode_instruction=barcode_instruction,
            prep_guidance=prep_guidance,
            prep_instruction_list=prep_instruction_list,
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
