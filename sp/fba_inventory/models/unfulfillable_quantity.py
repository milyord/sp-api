from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnfulfillableQuantity")


@attr.s(auto_attribs=True)
class UnfulfillableQuantity:
    r"""The quantity of unfulfillable inventory.

    Attributes:
        total_unfulfillable_quantity (Union[Unset, int]): The total number of units in Amazon's fulfillment network in
            unsellable condition.
        customer_damaged_quantity (Union[Unset, int]): The number of units in customer damaged disposition.
        warehouse_damaged_quantity (Union[Unset, int]): The number of units in warehouse damaged disposition.
        distributor_damaged_quantity (Union[Unset, int]): The number of units in distributor damaged disposition.
        carrier_damaged_quantity (Union[Unset, int]): The number of units in carrier damaged disposition.
        defective_quantity (Union[Unset, int]): The number of units in defective disposition.
        expired_quantity (Union[Unset, int]): The number of units in expired disposition.
    """

    total_unfulfillable_quantity: Union[Unset, int] = UNSET
    customer_damaged_quantity: Union[Unset, int] = UNSET
    warehouse_damaged_quantity: Union[Unset, int] = UNSET
    distributor_damaged_quantity: Union[Unset, int] = UNSET
    carrier_damaged_quantity: Union[Unset, int] = UNSET
    defective_quantity: Union[Unset, int] = UNSET
    expired_quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_unfulfillable_quantity = self.total_unfulfillable_quantity
        customer_damaged_quantity = self.customer_damaged_quantity
        warehouse_damaged_quantity = self.warehouse_damaged_quantity
        distributor_damaged_quantity = self.distributor_damaged_quantity
        carrier_damaged_quantity = self.carrier_damaged_quantity
        defective_quantity = self.defective_quantity
        expired_quantity = self.expired_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_unfulfillable_quantity is not UNSET:
            field_dict["totalUnfulfillableQuantity"] = total_unfulfillable_quantity
        if customer_damaged_quantity is not UNSET:
            field_dict["customerDamagedQuantity"] = customer_damaged_quantity
        if warehouse_damaged_quantity is not UNSET:
            field_dict["warehouseDamagedQuantity"] = warehouse_damaged_quantity
        if distributor_damaged_quantity is not UNSET:
            field_dict["distributorDamagedQuantity"] = distributor_damaged_quantity
        if carrier_damaged_quantity is not UNSET:
            field_dict["carrierDamagedQuantity"] = carrier_damaged_quantity
        if defective_quantity is not UNSET:
            field_dict["defectiveQuantity"] = defective_quantity
        if expired_quantity is not UNSET:
            field_dict["expiredQuantity"] = expired_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_unfulfillable_quantity = d.pop("totalUnfulfillableQuantity", UNSET)

        customer_damaged_quantity = d.pop("customerDamagedQuantity", UNSET)

        warehouse_damaged_quantity = d.pop("warehouseDamagedQuantity", UNSET)

        distributor_damaged_quantity = d.pop("distributorDamagedQuantity", UNSET)

        carrier_damaged_quantity = d.pop("carrierDamagedQuantity", UNSET)

        defective_quantity = d.pop("defectiveQuantity", UNSET)

        expired_quantity = d.pop("expiredQuantity", UNSET)

        result = cls(
            total_unfulfillable_quantity=total_unfulfillable_quantity,
            customer_damaged_quantity=customer_damaged_quantity,
            warehouse_damaged_quantity=warehouse_damaged_quantity,
            distributor_damaged_quantity=distributor_damaged_quantity,
            carrier_damaged_quantity=carrier_damaged_quantity,
            defective_quantity=defective_quantity,
            expired_quantity=expired_quantity,
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
