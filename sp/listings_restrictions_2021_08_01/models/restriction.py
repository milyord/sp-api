from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.restriction_condition_type import RestrictionConditionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason import Reason


T = TypeVar("T", bound="Restriction")


@attr.s(auto_attribs=True)
class Restriction:
    r"""A listing restriction, optionally qualified by a condition, with a list of reasons for the restriction.

    Attributes:
        marketplace_id (str): A marketplace identifier. Identifies the Amazon marketplace where the restriction is
            enforced.
        condition_type (Union[Unset, RestrictionConditionType]): The condition that applies to the restriction.
        reasons (Union[Unset, List['Reason']]): A list of reasons for the restriction.
    """

    marketplace_id: str
    condition_type: Union[Unset, RestrictionConditionType] = UNSET
    reasons: Union[Unset, List["Reason"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        condition_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type.value

        reasons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item = reasons_item_data.to_dict()

                reasons.append(reasons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if condition_type is not UNSET:
            field_dict["conditionType"] = condition_type
        if reasons is not UNSET:
            field_dict["reasons"] = reasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reason import Reason

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        _condition_type = d.pop("conditionType", UNSET)
        condition_type: Union[Unset, RestrictionConditionType]
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = RestrictionConditionType(_condition_type)

        reasons = []
        _reasons = d.pop("reasons", UNSET)
        for reasons_item_data in _reasons or []:
            reasons_item = Reason.from_dict(reasons_item_data)

            reasons.append(reasons_item)

        result = cls(
            marketplace_id=marketplace_id,
            condition_type=condition_type,
            reasons=reasons,
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
