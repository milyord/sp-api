from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity
    from ..models.money import Money


T = TypeVar("T", bound="OrderItem")


@attr.s(auto_attribs=True)
class OrderItem:
    r"""
    Attributes:
        item_sequence_number (str): Numbering of the item on the purchase order. The first item will be 1, the second 2,
            and so on.
        ordered_quantity (ItemQuantity): Details of quantity ordered.
        is_back_order_allowed (bool): When true, we will accept backorder confirmations for this item.
        amazon_product_identifier (Union[Unset, str]): Amazon Standard Identification Number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item.
        net_cost (Union[Unset, Money]): An amount of money, including units in the form of currency.
        list_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
    """

    item_sequence_number: str
    ordered_quantity: "ItemQuantity"
    is_back_order_allowed: bool
    amazon_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    net_cost: Union[Unset, "Money"] = UNSET
    list_price: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_sequence_number = self.item_sequence_number
        ordered_quantity = self.ordered_quantity.to_dict()

        is_back_order_allowed = self.is_back_order_allowed
        amazon_product_identifier = self.amazon_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        net_cost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.net_cost, Unset):
            net_cost = self.net_cost.to_dict()

        list_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.list_price, Unset):
            list_price = self.list_price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemSequenceNumber": item_sequence_number,
                "orderedQuantity": ordered_quantity,
                "isBackOrderAllowed": is_back_order_allowed,
            }
        )
        if amazon_product_identifier is not UNSET:
            field_dict["amazonProductIdentifier"] = amazon_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if net_cost is not UNSET:
            field_dict["netCost"] = net_cost
        if list_price is not UNSET:
            field_dict["listPrice"] = list_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity
        from ..models.money import Money

        d = src_dict.copy()
        item_sequence_number = d.pop("itemSequenceNumber")

        ordered_quantity = ItemQuantity.from_dict(d.pop("orderedQuantity"))

        is_back_order_allowed = d.pop("isBackOrderAllowed")

        amazon_product_identifier = d.pop("amazonProductIdentifier", UNSET)

        vendor_product_identifier = d.pop("vendorProductIdentifier", UNSET)

        _net_cost = d.pop("netCost", UNSET)
        net_cost: Union[Unset, Money]
        if isinstance(_net_cost, Unset):
            net_cost = UNSET
        else:
            net_cost = Money.from_dict(_net_cost)

        _list_price = d.pop("listPrice", UNSET)
        list_price: Union[Unset, Money]
        if isinstance(_list_price, Unset):
            list_price = UNSET
        else:
            list_price = Money.from_dict(_list_price)

        result = cls(
            item_sequence_number=item_sequence_number,
            ordered_quantity=ordered_quantity,
            is_back_order_allowed=is_back_order_allowed,
            amazon_product_identifier=amazon_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            net_cost=net_cost,
            list_price=list_price,
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
