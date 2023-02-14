import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="PartneredEstimate")


@attr.s(auto_attribs=True)
class PartneredEstimate:
    r"""The estimated shipping cost for a shipment using an Amazon-partnered carrier.

    Attributes:
        amount (Amount): The monetary value.
        confirm_deadline (Union[Unset, datetime.datetime]):
        void_deadline (Union[Unset, datetime.datetime]):
    """

    amount: "Amount"
    confirm_deadline: Union[Unset, datetime.datetime] = UNSET
    void_deadline: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount.to_dict()

        confirm_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.confirm_deadline, Unset):
            confirm_deadline = self.confirm_deadline.isoformat()

        void_deadline: Union[Unset, str] = UNSET
        if not isinstance(self.void_deadline, Unset):
            void_deadline = self.void_deadline.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Amount": amount,
            }
        )
        if confirm_deadline is not UNSET:
            field_dict["ConfirmDeadline"] = confirm_deadline
        if void_deadline is not UNSET:
            field_dict["VoidDeadline"] = void_deadline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount import Amount

        d = src_dict.copy()
        amount = Amount.from_dict(d.pop("Amount"))

        _confirm_deadline = d.pop("ConfirmDeadline", UNSET)
        confirm_deadline: Union[Unset, datetime.datetime]
        if isinstance(_confirm_deadline, Unset):
            confirm_deadline = UNSET
        else:
            confirm_deadline = isoparse(_confirm_deadline)

        _void_deadline = d.pop("VoidDeadline", UNSET)
        void_deadline: Union[Unset, datetime.datetime]
        if isinstance(_void_deadline, Unset):
            void_deadline = UNSET
        else:
            void_deadline = isoparse(_void_deadline)

        result = cls(
            amount=amount,
            confirm_deadline=confirm_deadline,
            void_deadline=void_deadline,
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
