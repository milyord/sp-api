from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_event_group import FinancialEventGroup


T = TypeVar("T", bound="ListFinancialEventGroupsPayload")


@attr.s(auto_attribs=True)
class ListFinancialEventGroupsPayload:
    r"""The payload for the listFinancialEventGroups operation.

    Attributes:
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
        financial_event_group_list (Union[Unset, List['FinancialEventGroup']]): A list of financial event group
            information.
    """

    next_token: Union[Unset, str] = UNSET
    financial_event_group_list: Union[Unset, List["FinancialEventGroup"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_token = self.next_token
        financial_event_group_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.financial_event_group_list, Unset):
            financial_event_group_list = []
            for componentsschemas_financial_event_group_list_item_data in self.financial_event_group_list:
                componentsschemas_financial_event_group_list_item = (
                    componentsschemas_financial_event_group_list_item_data.to_dict()
                )

                financial_event_group_list.append(componentsschemas_financial_event_group_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token
        if financial_event_group_list is not UNSET:
            field_dict["FinancialEventGroupList"] = financial_event_group_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_event_group import FinancialEventGroup

        d = src_dict.copy()
        next_token = d.pop("NextToken", UNSET)

        financial_event_group_list = []
        _financial_event_group_list = d.pop("FinancialEventGroupList", UNSET)
        for componentsschemas_financial_event_group_list_item_data in _financial_event_group_list or []:
            componentsschemas_financial_event_group_list_item = FinancialEventGroup.from_dict(
                componentsschemas_financial_event_group_list_item_data
            )

            financial_event_group_list.append(componentsschemas_financial_event_group_list_item)

        result = cls(
            next_token=next_token,
            financial_event_group_list=financial_event_group_list,
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
