from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.fee_line_item_fee_type import FeeLineItemFeeType

if TYPE_CHECKING:
    from ..models.money_type import MoneyType


T = TypeVar("T", bound="FeeLineItem")


@attr.s(auto_attribs=True)
class FeeLineItem:
    r"""Fee details for a specific fee.

    Attributes:
        fee_type (FeeLineItemFeeType): The type of fee charged to the seller.
        fee_charge (MoneyType):
    """

    fee_type: FeeLineItemFeeType
    fee_charge: "MoneyType"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fee_type = self.fee_type.value

        fee_charge = self.fee_charge.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feeType": fee_type,
                "feeCharge": fee_charge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_type import MoneyType

        d = src_dict.copy()
        fee_type = FeeLineItemFeeType(d.pop("feeType"))

        fee_charge = MoneyType.from_dict(d.pop("feeCharge"))

        result = cls(
            fee_type=fee_type,
            fee_charge=fee_charge,
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
