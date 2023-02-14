from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_eligibility_preview_ineligibility_reason_list_item import (
    ItemEligibilityPreviewIneligibilityReasonListItem,
)
from ..models.item_eligibility_preview_program import ItemEligibilityPreviewProgram
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemEligibilityPreview")


@attr.s(auto_attribs=True)
class ItemEligibilityPreview:
    r"""The response object which contains the ASIN, marketplaceId if required, eligibility program, the eligibility status
    (boolean), and a list of ineligibility reason codes.

        Attributes:
            asin (str): The ASIN for which eligibility was determined.
            program (ItemEligibilityPreviewProgram): The program for which eligibility was determined.
            is_eligible_for_program (bool): Indicates if the item is eligible for the program.
            marketplace_id (Union[Unset, str]): The marketplace for which eligibility was determined.
            ineligibility_reason_list (Union[Unset, List[ItemEligibilityPreviewIneligibilityReasonListItem]]): Potential
                Ineligibility Reason Codes.
    """

    asin: str
    program: ItemEligibilityPreviewProgram
    is_eligible_for_program: bool
    marketplace_id: Union[Unset, str] = UNSET
    ineligibility_reason_list: Union[Unset, List[ItemEligibilityPreviewIneligibilityReasonListItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asin = self.asin
        program = self.program.value

        is_eligible_for_program = self.is_eligible_for_program
        marketplace_id = self.marketplace_id
        ineligibility_reason_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ineligibility_reason_list, Unset):
            ineligibility_reason_list = []
            for ineligibility_reason_list_item_data in self.ineligibility_reason_list:
                ineligibility_reason_list_item = ineligibility_reason_list_item_data.value

                ineligibility_reason_list.append(ineligibility_reason_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asin": asin,
                "program": program,
                "isEligibleForProgram": is_eligible_for_program,
            }
        )
        if marketplace_id is not UNSET:
            field_dict["marketplaceId"] = marketplace_id
        if ineligibility_reason_list is not UNSET:
            field_dict["ineligibilityReasonList"] = ineligibility_reason_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asin = d.pop("asin")

        program = ItemEligibilityPreviewProgram(d.pop("program"))

        is_eligible_for_program = d.pop("isEligibleForProgram")

        marketplace_id = d.pop("marketplaceId", UNSET)

        ineligibility_reason_list = []
        _ineligibility_reason_list = d.pop("ineligibilityReasonList", UNSET)
        for ineligibility_reason_list_item_data in _ineligibility_reason_list or []:
            ineligibility_reason_list_item = ItemEligibilityPreviewIneligibilityReasonListItem(
                ineligibility_reason_list_item_data
            )

            ineligibility_reason_list.append(ineligibility_reason_list_item)

        result = cls(
            asin=asin,
            program=program,
            is_eligible_for_program=is_eligible_for_program,
            marketplace_id=marketplace_id,
            ineligibility_reason_list=ineligibility_reason_list,
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
