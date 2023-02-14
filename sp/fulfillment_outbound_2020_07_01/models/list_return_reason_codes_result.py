from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason_code_details import ReasonCodeDetails


T = TypeVar("T", bound="ListReturnReasonCodesResult")


@attr.s(auto_attribs=True)
class ListReturnReasonCodesResult:
    r"""
    Attributes:
        reason_code_details (Union[Unset, List['ReasonCodeDetails']]): An array of return reason code details.
    """

    reason_code_details: Union[Unset, List["ReasonCodeDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason_code_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reason_code_details, Unset):
            reason_code_details = []
            for componentsschemas_reason_code_details_list_item_data in self.reason_code_details:
                componentsschemas_reason_code_details_list_item = (
                    componentsschemas_reason_code_details_list_item_data.to_dict()
                )

                reason_code_details.append(componentsschemas_reason_code_details_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason_code_details is not UNSET:
            field_dict["reasonCodeDetails"] = reason_code_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reason_code_details import ReasonCodeDetails

        d = src_dict.copy()
        reason_code_details = []
        _reason_code_details = d.pop("reasonCodeDetails", UNSET)
        for componentsschemas_reason_code_details_list_item_data in _reason_code_details or []:
            componentsschemas_reason_code_details_list_item = ReasonCodeDetails.from_dict(
                componentsschemas_reason_code_details_list_item_data
            )

            reason_code_details.append(componentsschemas_reason_code_details_list_item)

        result = cls(
            reason_code_details=reason_code_details,
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
