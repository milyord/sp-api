from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_seller_inputs import AdditionalSellerInputs
    from ..models.weight import Weight


T = TypeVar("T", bound="Item")


@attr.s(auto_attribs=True)
class Item:
    r"""An Amazon order item identifier and a quantity.

    Attributes:
        order_item_id (str): An Amazon-defined identifier for an individual item in an order.
        quantity (int): The number of items.
        item_weight (Union[Unset, Weight]): The weight.
        item_description (Union[Unset, str]): The description of the item.
        transparency_code_list (Union[Unset, List[str]]): A list of transparency codes.
        item_level_seller_inputs_list (Union[Unset, List['AdditionalSellerInputs']]): A list of additional seller input
            pairs required to purchase shipping.
    """

    order_item_id: str
    quantity: int
    item_weight: Union[Unset, "Weight"] = UNSET
    item_description: Union[Unset, str] = UNSET
    transparency_code_list: Union[Unset, List[str]] = UNSET
    item_level_seller_inputs_list: Union[Unset, List["AdditionalSellerInputs"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_item_id = self.order_item_id
        quantity = self.quantity
        item_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_weight, Unset):
            item_weight = self.item_weight.to_dict()

        item_description = self.item_description
        transparency_code_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transparency_code_list, Unset):
            transparency_code_list = self.transparency_code_list

        item_level_seller_inputs_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_level_seller_inputs_list, Unset):
            item_level_seller_inputs_list = []
            for componentsschemas_additional_seller_inputs_list_item_data in self.item_level_seller_inputs_list:
                componentsschemas_additional_seller_inputs_list_item = (
                    componentsschemas_additional_seller_inputs_list_item_data.to_dict()
                )

                item_level_seller_inputs_list.append(componentsschemas_additional_seller_inputs_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "OrderItemId": order_item_id,
                "Quantity": quantity,
            }
        )
        if item_weight is not UNSET:
            field_dict["ItemWeight"] = item_weight
        if item_description is not UNSET:
            field_dict["ItemDescription"] = item_description
        if transparency_code_list is not UNSET:
            field_dict["TransparencyCodeList"] = transparency_code_list
        if item_level_seller_inputs_list is not UNSET:
            field_dict["ItemLevelSellerInputsList"] = item_level_seller_inputs_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_seller_inputs import AdditionalSellerInputs
        from ..models.weight import Weight

        d = src_dict.copy()
        order_item_id = d.pop("OrderItemId")

        quantity = d.pop("Quantity")

        _item_weight = d.pop("ItemWeight", UNSET)
        item_weight: Union[Unset, Weight]
        if isinstance(_item_weight, Unset):
            item_weight = UNSET
        else:
            item_weight = Weight.from_dict(_item_weight)

        item_description = d.pop("ItemDescription", UNSET)

        transparency_code_list = cast(List[str], d.pop("TransparencyCodeList", UNSET))

        item_level_seller_inputs_list = []
        _item_level_seller_inputs_list = d.pop("ItemLevelSellerInputsList", UNSET)
        for componentsschemas_additional_seller_inputs_list_item_data in _item_level_seller_inputs_list or []:
            componentsschemas_additional_seller_inputs_list_item = AdditionalSellerInputs.from_dict(
                componentsschemas_additional_seller_inputs_list_item_data
            )

            item_level_seller_inputs_list.append(componentsschemas_additional_seller_inputs_list_item)

        result = cls(
            order_item_id=order_item_id,
            quantity=quantity,
            item_weight=item_weight,
            item_description=item_description,
            transparency_code_list=transparency_code_list,
            item_level_seller_inputs_list=item_level_seller_inputs_list,
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
