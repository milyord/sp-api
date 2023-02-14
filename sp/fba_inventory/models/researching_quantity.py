from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.researching_quantity_entry import ResearchingQuantityEntry


T = TypeVar("T", bound="ResearchingQuantity")


@attr.s(auto_attribs=True)
class ResearchingQuantity:
    r"""The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers.

    Attributes:
        total_researching_quantity (Union[Unset, int]): The total number of units currently being researched in Amazon's
            fulfillment network.
        researching_quantity_breakdown (Union[Unset, List['ResearchingQuantityEntry']]): A list of quantity details for
            items currently being researched.
    """

    total_researching_quantity: Union[Unset, int] = UNSET
    researching_quantity_breakdown: Union[Unset, List["ResearchingQuantityEntry"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_researching_quantity = self.total_researching_quantity
        researching_quantity_breakdown: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.researching_quantity_breakdown, Unset):
            researching_quantity_breakdown = []
            for researching_quantity_breakdown_item_data in self.researching_quantity_breakdown:
                researching_quantity_breakdown_item = researching_quantity_breakdown_item_data.to_dict()

                researching_quantity_breakdown.append(researching_quantity_breakdown_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_researching_quantity is not UNSET:
            field_dict["totalResearchingQuantity"] = total_researching_quantity
        if researching_quantity_breakdown is not UNSET:
            field_dict["researchingQuantityBreakdown"] = researching_quantity_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.researching_quantity_entry import ResearchingQuantityEntry

        d = src_dict.copy()
        total_researching_quantity = d.pop("totalResearchingQuantity", UNSET)

        researching_quantity_breakdown = []
        _researching_quantity_breakdown = d.pop("researchingQuantityBreakdown", UNSET)
        for researching_quantity_breakdown_item_data in _researching_quantity_breakdown or []:
            researching_quantity_breakdown_item = ResearchingQuantityEntry.from_dict(
                researching_quantity_breakdown_item_data
            )

            researching_quantity_breakdown.append(researching_quantity_breakdown_item)

        result = cls(
            total_researching_quantity=total_researching_quantity,
            researching_quantity_breakdown=researching_quantity_breakdown,
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
