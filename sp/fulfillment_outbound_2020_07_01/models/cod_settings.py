from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="CODSettings")


@attr.s(auto_attribs=True)
class CODSettings:
    r"""The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.

    Attributes:
        is_cod_required (bool): When true, this fulfillment order requires a COD (Cash On Delivery) payment.
        cod_charge (Union[Unset, Money]): An amount of money, including units in the form of currency.
        cod_charge_tax (Union[Unset, Money]): An amount of money, including units in the form of currency.
        shipping_charge (Union[Unset, Money]): An amount of money, including units in the form of currency.
        shipping_charge_tax (Union[Unset, Money]): An amount of money, including units in the form of currency.
    """

    is_cod_required: bool
    cod_charge: Union[Unset, "Money"] = UNSET
    cod_charge_tax: Union[Unset, "Money"] = UNSET
    shipping_charge: Union[Unset, "Money"] = UNSET
    shipping_charge_tax: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_cod_required = self.is_cod_required
        cod_charge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cod_charge, Unset):
            cod_charge = self.cod_charge.to_dict()

        cod_charge_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cod_charge_tax, Unset):
            cod_charge_tax = self.cod_charge_tax.to_dict()

        shipping_charge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_charge, Unset):
            shipping_charge = self.shipping_charge.to_dict()

        shipping_charge_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_charge_tax, Unset):
            shipping_charge_tax = self.shipping_charge_tax.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCodRequired": is_cod_required,
            }
        )
        if cod_charge is not UNSET:
            field_dict["codCharge"] = cod_charge
        if cod_charge_tax is not UNSET:
            field_dict["codChargeTax"] = cod_charge_tax
        if shipping_charge is not UNSET:
            field_dict["shippingCharge"] = shipping_charge
        if shipping_charge_tax is not UNSET:
            field_dict["shippingChargeTax"] = shipping_charge_tax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        is_cod_required = d.pop("isCodRequired")

        _cod_charge = d.pop("codCharge", UNSET)
        cod_charge: Union[Unset, Money]
        if isinstance(_cod_charge, Unset):
            cod_charge = UNSET
        else:
            cod_charge = Money.from_dict(_cod_charge)

        _cod_charge_tax = d.pop("codChargeTax", UNSET)
        cod_charge_tax: Union[Unset, Money]
        if isinstance(_cod_charge_tax, Unset):
            cod_charge_tax = UNSET
        else:
            cod_charge_tax = Money.from_dict(_cod_charge_tax)

        _shipping_charge = d.pop("shippingCharge", UNSET)
        shipping_charge: Union[Unset, Money]
        if isinstance(_shipping_charge, Unset):
            shipping_charge = UNSET
        else:
            shipping_charge = Money.from_dict(_shipping_charge)

        _shipping_charge_tax = d.pop("shippingChargeTax", UNSET)
        shipping_charge_tax: Union[Unset, Money]
        if isinstance(_shipping_charge_tax, Unset):
            shipping_charge_tax = UNSET
        else:
            shipping_charge_tax = Money.from_dict(_shipping_charge_tax)

        result = cls(
            is_cod_required=is_cod_required,
            cod_charge=cod_charge,
            cod_charge_tax=cod_charge_tax,
            shipping_charge=shipping_charge,
            shipping_charge_tax=shipping_charge_tax,
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
