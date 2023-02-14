from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="GetFulfillmentPreviewItem")


@attr.s(auto_attribs=True)
class GetFulfillmentPreviewItem:
    r"""Item information for a fulfillment order preview.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        quantity (int): The item quantity.
        seller_fulfillment_order_item_id (str): A fulfillment order item identifier that the seller creates to track
            items in the fulfillment preview.
        per_unit_declared_value (Union[Unset, Money]): An amount of money, including units in the form of currency.
    """

    seller_sku: str
    quantity: int
    seller_fulfillment_order_item_id: str
    per_unit_declared_value: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        quantity = self.quantity
        seller_fulfillment_order_item_id = self.seller_fulfillment_order_item_id
        per_unit_declared_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.per_unit_declared_value, Unset):
            per_unit_declared_value = self.per_unit_declared_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sellerSku": seller_sku,
                "quantity": quantity,
                "sellerFulfillmentOrderItemId": seller_fulfillment_order_item_id,
            }
        )
        if per_unit_declared_value is not UNSET:
            field_dict["perUnitDeclaredValue"] = per_unit_declared_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        seller_sku = d.pop("sellerSku")

        quantity = d.pop("quantity")

        seller_fulfillment_order_item_id = d.pop("sellerFulfillmentOrderItemId")

        _per_unit_declared_value = d.pop("perUnitDeclaredValue", UNSET)
        per_unit_declared_value: Union[Unset, Money]
        if isinstance(_per_unit_declared_value, Unset):
            per_unit_declared_value = UNSET
        else:
            per_unit_declared_value = Money.from_dict(_per_unit_declared_value)

        result = cls(
            seller_sku=seller_sku,
            quantity=quantity,
            seller_fulfillment_order_item_id=seller_fulfillment_order_item_id,
            per_unit_declared_value=per_unit_declared_value,
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
