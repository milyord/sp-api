from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_instrument import ChargeInstrument
    from ..models.currency import Currency
    from ..models.debt_recovery_item import DebtRecoveryItem


T = TypeVar("T", bound="DebtRecoveryEvent")


@attr.s(auto_attribs=True)
class DebtRecoveryEvent:
    r"""A debt payment or debt adjustment.

    Attributes:
        debt_recovery_type (Union[Unset, str]): The debt recovery type.

            Possible values:

            * DebtPayment

            * DebtPaymentFailure

            *DebtAdjustment
        recovery_amount (Union[Unset, Currency]): A currency type and amount.
        over_payment_credit (Union[Unset, Currency]): A currency type and amount.
        debt_recovery_item_list (Union[Unset, List['DebtRecoveryItem']]): A list of debt recovery item information.
        charge_instrument_list (Union[Unset, List['ChargeInstrument']]): A list of payment instruments.
    """

    debt_recovery_type: Union[Unset, str] = UNSET
    recovery_amount: Union[Unset, "Currency"] = UNSET
    over_payment_credit: Union[Unset, "Currency"] = UNSET
    debt_recovery_item_list: Union[Unset, List["DebtRecoveryItem"]] = UNSET
    charge_instrument_list: Union[Unset, List["ChargeInstrument"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        debt_recovery_type = self.debt_recovery_type
        recovery_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recovery_amount, Unset):
            recovery_amount = self.recovery_amount.to_dict()

        over_payment_credit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.over_payment_credit, Unset):
            over_payment_credit = self.over_payment_credit.to_dict()

        debt_recovery_item_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.debt_recovery_item_list, Unset):
            debt_recovery_item_list = []
            for componentsschemas_debt_recovery_item_list_item_data in self.debt_recovery_item_list:
                componentsschemas_debt_recovery_item_list_item = (
                    componentsschemas_debt_recovery_item_list_item_data.to_dict()
                )

                debt_recovery_item_list.append(componentsschemas_debt_recovery_item_list_item)

        charge_instrument_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.charge_instrument_list, Unset):
            charge_instrument_list = []
            for componentsschemas_charge_instrument_list_item_data in self.charge_instrument_list:
                componentsschemas_charge_instrument_list_item = (
                    componentsschemas_charge_instrument_list_item_data.to_dict()
                )

                charge_instrument_list.append(componentsschemas_charge_instrument_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debt_recovery_type is not UNSET:
            field_dict["DebtRecoveryType"] = debt_recovery_type
        if recovery_amount is not UNSET:
            field_dict["RecoveryAmount"] = recovery_amount
        if over_payment_credit is not UNSET:
            field_dict["OverPaymentCredit"] = over_payment_credit
        if debt_recovery_item_list is not UNSET:
            field_dict["DebtRecoveryItemList"] = debt_recovery_item_list
        if charge_instrument_list is not UNSET:
            field_dict["ChargeInstrumentList"] = charge_instrument_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_instrument import ChargeInstrument
        from ..models.currency import Currency
        from ..models.debt_recovery_item import DebtRecoveryItem

        d = src_dict.copy()
        debt_recovery_type = d.pop("DebtRecoveryType", UNSET)

        _recovery_amount = d.pop("RecoveryAmount", UNSET)
        recovery_amount: Union[Unset, Currency]
        if isinstance(_recovery_amount, Unset):
            recovery_amount = UNSET
        else:
            recovery_amount = Currency.from_dict(_recovery_amount)

        _over_payment_credit = d.pop("OverPaymentCredit", UNSET)
        over_payment_credit: Union[Unset, Currency]
        if isinstance(_over_payment_credit, Unset):
            over_payment_credit = UNSET
        else:
            over_payment_credit = Currency.from_dict(_over_payment_credit)

        debt_recovery_item_list = []
        _debt_recovery_item_list = d.pop("DebtRecoveryItemList", UNSET)
        for componentsschemas_debt_recovery_item_list_item_data in _debt_recovery_item_list or []:
            componentsschemas_debt_recovery_item_list_item = DebtRecoveryItem.from_dict(
                componentsschemas_debt_recovery_item_list_item_data
            )

            debt_recovery_item_list.append(componentsschemas_debt_recovery_item_list_item)

        charge_instrument_list = []
        _charge_instrument_list = d.pop("ChargeInstrumentList", UNSET)
        for componentsschemas_charge_instrument_list_item_data in _charge_instrument_list or []:
            componentsschemas_charge_instrument_list_item = ChargeInstrument.from_dict(
                componentsschemas_charge_instrument_list_item_data
            )

            charge_instrument_list.append(componentsschemas_charge_instrument_list_item)

        result = cls(
            debt_recovery_type=debt_recovery_type,
            recovery_amount=recovery_amount,
            over_payment_credit=over_payment_credit,
            debt_recovery_item_list=debt_recovery_item_list,
            charge_instrument_list=charge_instrument_list,
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
