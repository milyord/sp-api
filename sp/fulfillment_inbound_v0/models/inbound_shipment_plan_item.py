from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prep_details import PrepDetails


T = TypeVar("T", bound="InboundShipmentPlanItem")


@attr.s(auto_attribs=True)
class InboundShipmentPlanItem:
    r"""Item information used to create an inbound shipment. Returned by the createInboundShipmentPlan operation.

    Attributes:
        seller_sku (str): The seller SKU of the item.
        fulfillment_network_sku (str): Amazon's fulfillment network SKU of the item.
        quantity (int): The item quantity.
        prep_details_list (Union[Unset, List['PrepDetails']]): A list of preparation instructions and who is responsible
            for that preparation.
    """

    seller_sku: str
    fulfillment_network_sku: str
    quantity: int
    prep_details_list: Union[Unset, List["PrepDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_sku = self.seller_sku
        fulfillment_network_sku = self.fulfillment_network_sku
        quantity = self.quantity
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
                "FulfillmentNetworkSKU": fulfillment_network_sku,
                "Quantity": quantity,
            }
        )
        if prep_details_list is not UNSET:
            field_dict["PrepDetailsList"] = prep_details_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prep_details import PrepDetails

        d = src_dict.copy()
        seller_sku = d.pop("SellerSKU")

        fulfillment_network_sku = d.pop("FulfillmentNetworkSKU")

        quantity = d.pop("Quantity")

        prep_details_list = []
        _prep_details_list = d.pop("PrepDetailsList", UNSET)
        for componentsschemas_prep_details_list_item_data in _prep_details_list or []:
            componentsschemas_prep_details_list_item = PrepDetails.from_dict(
                componentsschemas_prep_details_list_item_data
            )

            prep_details_list.append(componentsschemas_prep_details_list_item)

        result = cls(
            seller_sku=seller_sku,
            fulfillment_network_sku=fulfillment_network_sku,
            quantity=quantity,
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
