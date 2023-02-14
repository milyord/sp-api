import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmPreorderResult")


@attr.s(auto_attribs=True)
class ConfirmPreorderResult:
    r"""
    Attributes:
        confirmed_need_by_date (Union[Unset, datetime.date]):
        confirmed_fulfillable_date (Union[Unset, datetime.date]):
    """

    confirmed_need_by_date: Union[Unset, datetime.date] = UNSET
    confirmed_fulfillable_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confirmed_need_by_date: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_need_by_date, Unset):
            confirmed_need_by_date = self.confirmed_need_by_date.isoformat()

        confirmed_fulfillable_date: Union[Unset, str] = UNSET
        if not isinstance(self.confirmed_fulfillable_date, Unset):
            confirmed_fulfillable_date = self.confirmed_fulfillable_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmed_need_by_date is not UNSET:
            field_dict["ConfirmedNeedByDate"] = confirmed_need_by_date
        if confirmed_fulfillable_date is not UNSET:
            field_dict["ConfirmedFulfillableDate"] = confirmed_fulfillable_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _confirmed_need_by_date = d.pop("ConfirmedNeedByDate", UNSET)
        confirmed_need_by_date: Union[Unset, datetime.date]
        if isinstance(_confirmed_need_by_date, Unset):
            confirmed_need_by_date = UNSET
        else:
            confirmed_need_by_date = isoparse(_confirmed_need_by_date).date()

        _confirmed_fulfillable_date = d.pop("ConfirmedFulfillableDate", UNSET)
        confirmed_fulfillable_date: Union[Unset, datetime.date]
        if isinstance(_confirmed_fulfillable_date, Unset):
            confirmed_fulfillable_date = UNSET
        else:
            confirmed_fulfillable_date = isoparse(_confirmed_fulfillable_date).date()

        result = cls(
            confirmed_need_by_date=confirmed_need_by_date,
            confirmed_fulfillable_date=confirmed_fulfillable_date,
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
