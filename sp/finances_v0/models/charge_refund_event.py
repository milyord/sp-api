import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_refund_transaction import ChargeRefundTransaction


T = TypeVar("T", bound="ChargeRefundEvent")


@attr.s(auto_attribs=True)
class ChargeRefundEvent:
    r"""An event related to charge refund.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        reason_code (Union[Unset, str]): The reason given for a charge refund.

            Example: `SubscriptionFeeCorrection`
        reason_code_description (Union[Unset, str]): A description of the Reason Code.

            Example: `SubscriptionFeeCorrection`
        charge_refund_transactions (Union[Unset, ChargeRefundTransaction]): The charge refund transaction.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    reason_code: Union[Unset, str] = UNSET
    reason_code_description: Union[Unset, str] = UNSET
    charge_refund_transactions: Union[Unset, "ChargeRefundTransaction"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        reason_code = self.reason_code
        reason_code_description = self.reason_code_description
        charge_refund_transactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.charge_refund_transactions, Unset):
            charge_refund_transactions = self.charge_refund_transactions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if reason_code is not UNSET:
            field_dict["ReasonCode"] = reason_code
        if reason_code_description is not UNSET:
            field_dict["ReasonCodeDescription"] = reason_code_description
        if charge_refund_transactions is not UNSET:
            field_dict["ChargeRefundTransactions"] = charge_refund_transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_refund_transaction import ChargeRefundTransaction

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        reason_code = d.pop("ReasonCode", UNSET)

        reason_code_description = d.pop("ReasonCodeDescription", UNSET)

        _charge_refund_transactions = d.pop("ChargeRefundTransactions", UNSET)
        charge_refund_transactions: Union[Unset, ChargeRefundTransaction]
        if isinstance(_charge_refund_transactions, Unset):
            charge_refund_transactions = UNSET
        else:
            charge_refund_transactions = ChargeRefundTransaction.from_dict(_charge_refund_transactions)

        result = cls(
            posted_date=posted_date,
            reason_code=reason_code,
            reason_code_description=reason_code_description,
            charge_refund_transactions=charge_refund_transactions,
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
