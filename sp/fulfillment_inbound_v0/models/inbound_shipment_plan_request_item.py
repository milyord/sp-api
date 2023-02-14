from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.condition import Condition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prep_details import PrepDetails


T = TypeVar("T", bound="InboundShipmentPlanRequestItem")


@attr.s(auto_attribs=True)
class InboundShipmentPlanRequestItem:
    r"""Item information for creating an inbound shipment plan. Submitted with a call to the createInboundShipmentPlan
    operation.

        Attributes:
            seller_sku (str): The seller SKU of the item.
            asin (str): The Amazon Standard Identification Number (ASIN) of the item.
            condition (Condition): The condition of the item.
            quantity (int): The item quantity.
            quantity_in_case (Union[Unset, int]): The item quantity.
            prep_details_list (Union[Unset, List['PrepDetails']]): A list of preparation instructions and who is responsible
                for that preparation.
    """

    seller_sku: str
    asin: str
    condition: Condition
    quantity: int
    quantity_in_case: Union[Unset, int] = UNSET
    prep_details_list: Union[Unset, List["PrepDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        asin = self.asin
        condition = self.condition.value

        quantity = self.quantity
        quantity_in_case = self.quantity_in_case
        prep_details_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prep_details_list, Unset):
            prep_details_list = []
            for componentsschemas_prep_details_list_item_data in self.prep_details_list:
                componentsschemas_prep_details_list_item = componentsschemas_prep_details_list_item_data.to_dict()

                prep_details_list.append(componentsschemas_prep_details_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SellerSKU": seller_sku,
                "ASIN": asin,
                "Condition": condition,
                "Quantity": quantity,
            }
        )
        if quantity_in_case is not UNSET:
            field_dict["QuantityInCase"] = quantity_in_case
        if prep_details_list is not UNSET:
            field_dict["PrepDetailsList"] = prep_details_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prep_details import PrepDetails

        d = src_dict.copy()
        seller_sku = d.pop("SellerSKU")

        asin = d.pop("ASIN")

        condition = Condition(d.pop("Condition"))

        quantity = d.pop("Quantity")

        quantity_in_case = d.pop("QuantityInCase", UNSET)

        prep_details_list = []
        _prep_details_list = d.pop("PrepDetailsList", UNSET)
        for componentsschemas_prep_details_list_item_data in _prep_details_list or []:
            componentsschemas_prep_details_list_item = PrepDetails.from_dict(
                componentsschemas_prep_details_list_item_data
            )

            prep_details_list.append(componentsschemas_prep_details_list_item)

        result = cls(
            seller_sku=seller_sku,
            asin=asin,
            condition=condition,
            quantity=quantity,
            quantity_in_case=quantity_in_case,
            prep_details_list=prep_details_list,
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
