from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_events import FinancialEvents


T = TypeVar("T", bound="ListFinancialEventsPayload")


@attr.s(auto_attribs=True)
class ListFinancialEventsPayload:
    r"""The payload for the listFinancialEvents operation.

    Attributes:
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
        financial_events (Union[Unset, FinancialEvents]): Contains all information related to a financial event.
    """

    next_token: Union[Unset, str] = UNSET
    financial_events: Union[Unset, "FinancialEvents"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_token = self.next_token
        financial_events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.financial_events, Unset):
            financial_events = self.financial_events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token
        if financial_events is not UNSET:
            field_dict["FinancialEvents"] = financial_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_events import FinancialEvents

        d = src_dict.copy()
        next_token = d.pop("NextToken", UNSET)

        _financial_events = d.pop("FinancialEvents", UNSET)
        financial_events: Union[Unset, FinancialEvents]
        if isinstance(_financial_events, Unset):
            financial_events = UNSET
        else:
            financial_events = FinancialEvents.from_dict(_financial_events)

        result = cls(
            next_token=next_token,
            financial_events=financial_events,
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
