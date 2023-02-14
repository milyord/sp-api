import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="CapacityReservationBillingEvent")


@attr.s(auto_attribs=True)
class CapacityReservationBillingEvent:
    r"""An event related to a capacity reservation billing charge.

    Attributes:
        transaction_type (Union[Unset, str]): Indicates the type of transaction. For example, FBA Inventory Fee
        posted_date (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]): A short description of the capacity reservation billing event.
        transaction_amount (Union[Unset, Currency]): A currency type and amount.
    """

    transaction_type: Union[Unset, str] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    transaction_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_type = self.transaction_type
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        description = self.description
        transaction_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_amount, Unset):
            transaction_amount = self.transaction_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_type is not UNSET:
            field_dict["TransactionType"] = transaction_type
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if description is not UNSET:
            field_dict["Description"] = description
        if transaction_amount is not UNSET:
            field_dict["TransactionAmount"] = transaction_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        transaction_type = d.pop("TransactionType", UNSET)

        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        description = d.pop("Description", UNSET)

        _transaction_amount = d.pop("TransactionAmount", UNSET)
        transaction_amount: Union[Unset, Currency]
        if isinstance(_transaction_amount, Unset):
            transaction_amount = UNSET
        else:
            transaction_amount = Currency.from_dict(_transaction_amount)

        result = cls(
            transaction_type=transaction_type,
            posted_date=posted_date,
            description=description,
            transaction_amount=transaction_amount,
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
