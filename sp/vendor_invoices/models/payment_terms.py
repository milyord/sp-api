from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.payment_terms_type import PaymentTermsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentTerms")


@attr.s(auto_attribs=True)
class PaymentTerms:
    r"""Terms of the payment for the invoice. The basis of the payment terms is the invoice date.

    Attributes:
        type (Union[Unset, PaymentTermsType]): The payment term type for the invoice.
        discount_percent (Union[Unset, str]): A decimal number with no loss of precision. Useful when precision loss is
            unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** :
            `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
        discount_due_days (Union[Unset, float]): The number of calendar days from the Base date (Invoice date) until the
            discount is no longer valid.
        net_due_days (Union[Unset, float]): The number of calendar days from the base date (invoice date) until the
            total amount on the invoice is due.
    """

    type: Union[Unset, PaymentTermsType] = UNSET
    discount_percent: Union[Unset, str] = UNSET
    discount_due_days: Union[Unset, float] = UNSET
    net_due_days: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        discount_percent = self.discount_percent
        discount_due_days = self.discount_due_days
        net_due_days = self.net_due_days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if discount_due_days is not UNSET:
            field_dict["discountDueDays"] = discount_due_days
        if net_due_days is not UNSET:
            field_dict["netDueDays"] = net_due_days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, PaymentTermsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PaymentTermsType(_type)

        discount_percent = d.pop("discountPercent", UNSET)

        discount_due_days = d.pop("discountDueDays", UNSET)

        net_due_days = d.pop("netDueDays", UNSET)

        result = cls(
            type=type,
            discount_percent=discount_percent,
            discount_due_days=discount_due_days,
            net_due_days=net_due_days,
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
