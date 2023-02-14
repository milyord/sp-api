import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="SellerDealPaymentEvent")


@attr.s(auto_attribs=True)
class SellerDealPaymentEvent:
    r"""An event linked to the payment of a fee related to the specified deal.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        deal_id (Union[Unset, str]): The unique identifier of the deal.
        deal_description (Union[Unset, str]): The internal description of the deal.
        event_type (Union[Unset, str]): The type of event: SellerDealComplete.
        fee_type (Union[Unset, str]): The type of fee: RunLightningDealFee.
        fee_amount (Union[Unset, Currency]): A currency type and amount.
        tax_amount (Union[Unset, Currency]): A currency type and amount.
        total_amount (Union[Unset, Currency]): A currency type and amount.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    deal_id: Union[Unset, str] = UNSET
    deal_description: Union[Unset, str] = UNSET
    event_type: Union[Unset, str] = UNSET
    fee_type: Union[Unset, str] = UNSET
    fee_amount: Union[Unset, "Currency"] = UNSET
    tax_amount: Union[Unset, "Currency"] = UNSET
    total_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        deal_id = self.deal_id
        deal_description = self.deal_description
        event_type = self.event_type
        fee_type = self.fee_type
        fee_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_amount, Unset):
            fee_amount = self.fee_amount.to_dict()

        tax_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_amount, Unset):
            tax_amount = self.tax_amount.to_dict()

        total_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_amount, Unset):
            total_amount = self.total_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if deal_id is not UNSET:
            field_dict["dealId"] = deal_id
        if deal_description is not UNSET:
            field_dict["dealDescription"] = deal_description
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if fee_type is not UNSET:
            field_dict["feeType"] = fee_type
        if fee_amount is not UNSET:
            field_dict["feeAmount"] = fee_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        deal_id = d.pop("dealId", UNSET)

        deal_description = d.pop("dealDescription", UNSET)

        event_type = d.pop("eventType", UNSET)

        fee_type = d.pop("feeType", UNSET)

        _fee_amount = d.pop("feeAmount", UNSET)
        fee_amount: Union[Unset, Currency]
        if isinstance(_fee_amount, Unset):
            fee_amount = UNSET
        else:
            fee_amount = Currency.from_dict(_fee_amount)

        _tax_amount = d.pop("taxAmount", UNSET)
        tax_amount: Union[Unset, Currency]
        if isinstance(_tax_amount, Unset):
            tax_amount = UNSET
        else:
            tax_amount = Currency.from_dict(_tax_amount)

        _total_amount = d.pop("totalAmount", UNSET)
        total_amount: Union[Unset, Currency]
        if isinstance(_total_amount, Unset):
            total_amount = UNSET
        else:
            total_amount = Currency.from_dict(_total_amount)

        result = cls(
            posted_date=posted_date,
            deal_id=deal_id,
            deal_description=deal_description,
            event_type=event_type,
            fee_type=fee_type,
            fee_amount=fee_amount,
            tax_amount=tax_amount,
            total_amount=total_amount,
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
