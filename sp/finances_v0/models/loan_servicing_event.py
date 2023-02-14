from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="LoanServicingEvent")


@attr.s(auto_attribs=True)
class LoanServicingEvent:
    r"""A loan advance, loan payment, or loan refund.

    Attributes:
        loan_amount (Union[Unset, Currency]): A currency type and amount.
        source_business_event_type (Union[Unset, str]): The type of event.

            Possible values:

            * LoanAdvance

            * LoanPayment

            * LoanRefund
    """

    loan_amount: Union[Unset, "Currency"] = UNSET
    source_business_event_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loan_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.loan_amount, Unset):
            loan_amount = self.loan_amount.to_dict()

        source_business_event_type = self.source_business_event_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loan_amount is not UNSET:
            field_dict["LoanAmount"] = loan_amount
        if source_business_event_type is not UNSET:
            field_dict["SourceBusinessEventType"] = source_business_event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _loan_amount = d.pop("LoanAmount", UNSET)
        loan_amount: Union[Unset, Currency]
        if isinstance(_loan_amount, Unset):
            loan_amount = UNSET
        else:
            loan_amount = Currency.from_dict(_loan_amount)

        source_business_event_type = d.pop("SourceBusinessEventType", UNSET)

        result = cls(
            loan_amount=loan_amount,
            source_business_event_type=source_business_event_type,
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
