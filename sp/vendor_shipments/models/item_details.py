from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_details_handling_code import ItemDetailsHandlingCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expiry import Expiry
    from ..models.money import Money


T = TypeVar("T", bound="ItemDetails")


@attr.s(auto_attribs=True)
class ItemDetails:
    r"""Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is
    appropriate.

        Attributes:
            purchase_order_number (Union[Unset, str]): The Amazon purchase order number for the shipment being confirmed. If
                the items in this shipment belong to multiple purchase order numbers that are in particular carton or pallet
                within the shipment, then provide the purchaseOrderNumber at the appropriate carton or pallet level. Formatting
                Notes: 8-character alpha-numeric code.
            lot_number (Union[Unset, str]): The batch or lot number associates an item with information the manufacturer
                considers relevant for traceability of the trade item to which the Element String is applied. The data may refer
                to the trade item itself or to items contained. This field is mandatory for all perishable items.
            expiry (Union[Unset, Expiry]):
            maximum_retail_price (Union[Unset, Money]): An amount of money, including units in the form of currency.
            handling_code (Union[Unset, ItemDetailsHandlingCode]): Identification of the instructions on how specified
                item/carton/pallet should be handled.
    """

    purchase_order_number: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    expiry: Union[Unset, "Expiry"] = UNSET
    maximum_retail_price: Union[Unset, "Money"] = UNSET
    handling_code: Union[Unset, ItemDetailsHandlingCode] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order_number = self.purchase_order_number
        lot_number = self.lot_number
        expiry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expiry, Unset):
            expiry = self.expiry.to_dict()

        maximum_retail_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maximum_retail_price, Unset):
            maximum_retail_price = self.maximum_retail_price.to_dict()

        handling_code: Union[Unset, str] = UNSET
        if not isinstance(self.handling_code, Unset):
            handling_code = self.handling_code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if maximum_retail_price is not UNSET:
            field_dict["maximumRetailPrice"] = maximum_retail_price
        if handling_code is not UNSET:
            field_dict["handlingCode"] = handling_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.expiry import Expiry
        from ..models.money import Money

        d = src_dict.copy()
        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        _expiry = d.pop("expiry", UNSET)
        expiry: Union[Unset, Expiry]
        if isinstance(_expiry, Unset):
            expiry = UNSET
        else:
            expiry = Expiry.from_dict(_expiry)

        _maximum_retail_price = d.pop("maximumRetailPrice", UNSET)
        maximum_retail_price: Union[Unset, Money]
        if isinstance(_maximum_retail_price, Unset):
            maximum_retail_price = UNSET
        else:
            maximum_retail_price = Money.from_dict(_maximum_retail_price)

        _handling_code = d.pop("handlingCode", UNSET)
        handling_code: Union[Unset, ItemDetailsHandlingCode]
        if isinstance(_handling_code, Unset):
            handling_code = UNSET
        else:
            handling_code = ItemDetailsHandlingCode(_handling_code)

        result = cls(
            purchase_order_number=purchase_order_number,
            lot_number=lot_number,
            expiry=expiry,
            maximum_retail_price=maximum_retail_price,
            handling_code=handling_code,
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
