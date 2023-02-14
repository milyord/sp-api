from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_quantity import ItemQuantity
    from ..models.money import Money
    from ..models.order_item_acknowledgement import OrderItemAcknowledgement


T = TypeVar("T", bound="OrderAcknowledgementItem")


@attr.s(auto_attribs=True)
class OrderAcknowledgementItem:
    r"""Details of the item being acknowledged.

    Attributes:
        ordered_quantity (ItemQuantity): Details of quantity ordered.
        item_acknowledgements (List['OrderItemAcknowledgement']): This is used to indicate acknowledged quantity.
        item_sequence_number (Union[Unset, str]): Line item sequence number for the item.
        amazon_product_identifier (Union[Unset, str]): Amazon Standard Identification Number (ASIN) of an item.
        vendor_product_identifier (Union[Unset, str]): The vendor selected product identification of the item. Should be
            the same as was sent in the purchase order.
        net_cost (Union[Unset, Money]): An amount of money, including units in the form of currency.
        list_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
        discount_multiplier (Union[Unset, str]): The discount multiplier that should be applied to the price if a vendor
            sells books with a list price. This is a multiplier factor to arrive at a final discounted price. A multiplier
            of .90 would be the factor if a 10% discount is given.
    """

    ordered_quantity: "ItemQuantity"
    item_acknowledgements: List["OrderItemAcknowledgement"]
    item_sequence_number: Union[Unset, str] = UNSET
    amazon_product_identifier: Union[Unset, str] = UNSET
    vendor_product_identifier: Union[Unset, str] = UNSET
    net_cost: Union[Unset, "Money"] = UNSET
    list_price: Union[Unset, "Money"] = UNSET
    discount_multiplier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ordered_quantity = self.ordered_quantity.to_dict()

        item_acknowledgements = []
        for item_acknowledgements_item_data in self.item_acknowledgements:
            item_acknowledgements_item = item_acknowledgements_item_data.to_dict()

            item_acknowledgements.append(item_acknowledgements_item)

        item_sequence_number = self.item_sequence_number
        amazon_product_identifier = self.amazon_product_identifier
        vendor_product_identifier = self.vendor_product_identifier
        net_cost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.net_cost, Unset):
            net_cost = self.net_cost.to_dict()

        list_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.list_price, Unset):
            list_price = self.list_price.to_dict()

        discount_multiplier = self.discount_multiplier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderedQuantity": ordered_quantity,
                "itemAcknowledgements": item_acknowledgements,
            }
        )
        if item_sequence_number is not UNSET:
            field_dict["itemSequenceNumber"] = item_sequence_number
        if amazon_product_identifier is not UNSET:
            field_dict["amazonProductIdentifier"] = amazon_product_identifier
        if vendor_product_identifier is not UNSET:
            field_dict["vendorProductIdentifier"] = vendor_product_identifier
        if net_cost is not UNSET:
            field_dict["netCost"] = net_cost
        if list_price is not UNSET:
            field_dict["listPrice"] = list_price
        if discount_multiplier is not UNSET:
            field_dict["discountMultiplier"] = discount_multiplier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_quantity import ItemQuantity
        from ..models.money import Money
        from ..models.order_item_acknowledgement import OrderItemAcknowledgement

        d = src_dict.copy()
        ordered_quantity = ItemQuantity.from_dict(d.pop("orderedQuantity"))

        item_acknowledgements = []
        _item_acknowledgements = d.pop("itemAcknowledgements")
        for item_acknowledgements_item_data in _item_acknowledgements:
            item_acknowledgements_item = OrderItemAcknowledgement.from_dict(item_acknowledgements_item_data)

            item_acknowledgements.append(item_acknowledgements_item)

        item_sequence_number = d.pop("itemSequenceNumber", UNSET)

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

        discount_multiplier = d.pop("discountMultiplier", UNSET)

        result = cls(
            ordered_quantity=ordered_quantity,
            item_acknowledgements=item_acknowledgements,
            item_sequence_number=item_sequence_number,
            amazon_product_identifier=amazon_product_identifier,
            vendor_product_identifier=vendor_product_identifier,
            net_cost=net_cost,
            list_price=list_price,
            discount_multiplier=discount_multiplier,
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
