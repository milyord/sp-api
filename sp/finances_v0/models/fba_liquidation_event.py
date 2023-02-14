import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="FBALiquidationEvent")


@attr.s(auto_attribs=True)
class FBALiquidationEvent:
    r"""A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US
    marketplace.

        Attributes:
            posted_date (Union[Unset, datetime.datetime]):
            original_removal_order_id (Union[Unset, str]): The identifier for the original removal order.
            liquidation_proceeds_amount (Union[Unset, Currency]): A currency type and amount.
            liquidation_fee_amount (Union[Unset, Currency]): A currency type and amount.
    """

    posted_date: Union[Unset, datetime.datetime] = UNSET
    original_removal_order_id: Union[Unset, str] = UNSET
    liquidation_proceeds_amount: Union[Unset, "Currency"] = UNSET
    liquidation_fee_amount: Union[Unset, "Currency"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        original_removal_order_id = self.original_removal_order_id
        liquidation_proceeds_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.liquidation_proceeds_amount, Unset):
            liquidation_proceeds_amount = self.liquidation_proceeds_amount.to_dict()

        liquidation_fee_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.liquidation_fee_amount, Unset):
            liquidation_fee_amount = self.liquidation_fee_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted_date is not UNSET:
            field_dict["PostedDate"] = posted_date
        if original_removal_order_id is not UNSET:
            field_dict["OriginalRemovalOrderId"] = original_removal_order_id
        if liquidation_proceeds_amount is not UNSET:
            field_dict["LiquidationProceedsAmount"] = liquidation_proceeds_amount
        if liquidation_fee_amount is not UNSET:
            field_dict["LiquidationFeeAmount"] = liquidation_fee_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        _posted_date = d.pop("PostedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        original_removal_order_id = d.pop("OriginalRemovalOrderId", UNSET)

        _liquidation_proceeds_amount = d.pop("LiquidationProceedsAmount", UNSET)
        liquidation_proceeds_amount: Union[Unset, Currency]
        if isinstance(_liquidation_proceeds_amount, Unset):
            liquidation_proceeds_amount = UNSET
        else:
            liquidation_proceeds_amount = Currency.from_dict(_liquidation_proceeds_amount)

        _liquidation_fee_amount = d.pop("LiquidationFeeAmount", UNSET)
        liquidation_fee_amount: Union[Unset, Currency]
        if isinstance(_liquidation_fee_amount, Unset):
            liquidation_fee_amount = UNSET
        else:
            liquidation_fee_amount = Currency.from_dict(_liquidation_fee_amount)

        result = cls(
            posted_date=posted_date,
            original_removal_order_id=original_removal_order_id,
            liquidation_proceeds_amount=liquidation_proceeds_amount,
            liquidation_fee_amount=liquidation_fee_amount,
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
