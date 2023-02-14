import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.tax_withholding_period import TaxWithholdingPeriod


T = TypeVar("T", bound="TaxWithholdingEvent")


@attr.s(auto_attribs=True)
class TaxWithholdingEvent:
    r"""A TaxWithholding event on seller's account.

    Attributes:
        posted_date (Union[Unset, datetime.datetime]):
        base_amount (Union[Unset, Currency]): A currency type and amount.
        withheld_amount (Union[Unset, Currency]): A currency type and amount.
        tax_withholding_period (Union[Unset, TaxWithholdingPeriod]): Period which taxwithholding on seller's account is
            calculated.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    base_amount: Union[Unset, "Currency"] = UNSET
    withheld_amount: Union[Unset, "Currency"] = UNSET
    tax_withholding_period: Union[Unset, "TaxWithholdingPeriod"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        base_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_amount, Unset):
            base_amount = self.base_amount.to_dict()

        withheld_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.withheld_amount, Unset):
            withheld_amount = self.withheld_amount.to_dict()

        tax_withholding_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_withholding_period, Unset):
            tax_withholding_period = self.tax_withholding_period.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if base_amount is not UNSET:
            field_dict["BaseAmount"] = base_amount
        if withheld_amount is not UNSET:
            field_dict["WithheldAmount"] = withheld_amount
        if tax_withholding_period is not UNSET:
            field_dict["TaxWithholdingPeriod"] = tax_withholding_period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.tax_withholding_period import TaxWithholdingPeriod

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        _base_amount = d.pop("BaseAmount", UNSET)
        base_amount: Union[Unset, Currency]
        if isinstance(_base_amount, Unset):
            base_amount = UNSET
        else:
            base_amount = Currency.from_dict(_base_amount)

        _withheld_amount = d.pop("WithheldAmount", UNSET)
        withheld_amount: Union[Unset, Currency]
        if isinstance(_withheld_amount, Unset):
            withheld_amount = UNSET
        else:
            withheld_amount = Currency.from_dict(_withheld_amount)

        _tax_withholding_period = d.pop("TaxWithholdingPeriod", UNSET)
        tax_withholding_period: Union[Unset, TaxWithholdingPeriod]
        if isinstance(_tax_withholding_period, Unset):
            tax_withholding_period = UNSET
        else:
            tax_withholding_period = TaxWithholdingPeriod.from_dict(_tax_withholding_period)

        result = cls(
            posted_date=posted_date,
            base_amount=base_amount,
            withheld_amount=withheld_amount,
            tax_withholding_period=tax_withholding_period,
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
