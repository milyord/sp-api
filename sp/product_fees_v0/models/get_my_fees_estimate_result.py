from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fees_estimate_result import FeesEstimateResult


T = TypeVar("T", bound="GetMyFeesEstimateResult")


@attr.s(auto_attribs=True)
class GetMyFeesEstimateResult:
    r"""Response schema.

    Attributes:
        fees_estimate_result (Union[Unset, FeesEstimateResult]): An item identifier and the estimated fees for the item.
    """

    fees_estimate_result: Union[Unset, "FeesEstimateResult"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fees_estimate_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees_estimate_result, Unset):
            fees_estimate_result = self.fees_estimate_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fees_estimate_result is not UNSET:
            field_dict["FeesEstimateResult"] = fees_estimate_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fees_estimate_result import FeesEstimateResult

        d = src_dict.copy()
        _fees_estimate_result = d.pop("FeesEstimateResult", UNSET)
        fees_estimate_result: Union[Unset, FeesEstimateResult]
        if isinstance(_fees_estimate_result, Unset):
            fees_estimate_result = UNSET
        else:
            fees_estimate_result = FeesEstimateResult.from_dict(_fees_estimate_result)

        result = cls(
            fees_estimate_result=fees_estimate_result,
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
