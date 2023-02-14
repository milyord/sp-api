from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerRequestedCancel")


@attr.s(auto_attribs=True)
class BuyerRequestedCancel:
    r"""Information about whether or not a buyer requested cancellation.

    Attributes:
        is_buyer_requested_cancel (Union[Unset, bool]): When true, the buyer has requested cancellation.
        buyer_cancel_reason (Union[Unset, str]): The reason that the buyer requested cancellation.
    """

    is_buyer_requested_cancel: Union[Unset, bool] = UNSET
    buyer_cancel_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_buyer_requested_cancel = self.is_buyer_requested_cancel
        buyer_cancel_reason = self.buyer_cancel_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_buyer_requested_cancel is not UNSET:
            field_dict["IsBuyerRequestedCancel"] = is_buyer_requested_cancel
        if buyer_cancel_reason is not UNSET:
            field_dict["BuyerCancelReason"] = buyer_cancel_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_buyer_requested_cancel = d.pop("IsBuyerRequestedCancel", UNSET)

        buyer_cancel_reason = d.pop("BuyerCancelReason", UNSET)

        result = cls(
            is_buyer_requested_cancel=is_buyer_requested_cancel,
            buyer_cancel_reason=buyer_cancel_reason,
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
