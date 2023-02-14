from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_component import ChargeComponent


T = TypeVar("T", bound="SAFETReimbursementItem")


@attr.s(auto_attribs=True)
class SAFETReimbursementItem:
    r"""An item from a SAFE-T claim reimbursement.

    Attributes:
        item_charge_list (Union[Unset, List['ChargeComponent']]): A list of charge information on the seller's account.
        product_description (Union[Unset, str]): The description of the item as shown on the product detail page on the
            retail website.
        quantity (Union[Unset, str]): The number of units of the item being reimbursed.
    """

    item_charge_list: Union[Unset, List["ChargeComponent"]] = UNSET
    product_description: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_charge_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_charge_list, Unset):
            item_charge_list = []
            for componentsschemas_charge_component_list_item_data in self.item_charge_list:
                componentsschemas_charge_component_list_item = (
                    componentsschemas_charge_component_list_item_data.to_dict()
                )

                item_charge_list.append(componentsschemas_charge_component_list_item)

        product_description = self.product_description
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_charge_list is not UNSET:
            field_dict["itemChargeList"] = item_charge_list
        if product_description is not UNSET:
            field_dict["productDescription"] = product_description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_component import ChargeComponent

        d = src_dict.copy()
        item_charge_list = []
        _item_charge_list = d.pop("itemChargeList", UNSET)
        for componentsschemas_charge_component_list_item_data in _item_charge_list or []:
            componentsschemas_charge_component_list_item = ChargeComponent.from_dict(
                componentsschemas_charge_component_list_item_data
            )

            item_charge_list.append(componentsschemas_charge_component_list_item)

        product_description = d.pop("productDescription", UNSET)

        quantity = d.pop("quantity", UNSET)

        result = cls(
            item_charge_list=item_charge_list,
            product_description=product_description,
            quantity=quantity,
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
