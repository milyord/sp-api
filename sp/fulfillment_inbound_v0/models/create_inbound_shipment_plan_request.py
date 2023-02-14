from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.label_prep_preference import LabelPrepPreference
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.inbound_shipment_plan_request_item import InboundShipmentPlanRequestItem


T = TypeVar("T", bound="CreateInboundShipmentPlanRequest")


@attr.s(auto_attribs=True)
class CreateInboundShipmentPlanRequest:
    r"""The request schema for the createInboundShipmentPlan operation.

    Attributes:
        ship_from_address (Address):
        label_prep_preference (LabelPrepPreference): The preference for label preparation for an inbound shipment.
        inbound_shipment_plan_request_items (List['InboundShipmentPlanRequestItem']):
        ship_to_country_code (Union[Unset, str]): The two-character country code for the country where the inbound
            shipment is to be sent.

            Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.

             Values:

             ShipToCountryCode values for North America:
             * CA – Canada
             * MX - Mexico
             * US - United States

            ShipToCountryCode values for MCI sellers in Europe:
             * DE – Germany
             * ES – Spain
             * FR – France
             * GB – United Kingdom
             * IT – Italy

            Default: The country code for the seller's home marketplace.
        ship_to_country_subdivision_code (Union[Unset, str]): The two-character country code, followed by a dash and
            then up to three characters that represent the subdivision of the country where the inbound shipment is to be
            sent. For example, "IN-MH". In full ISO 3166-2 format.

            Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
    """

    ship_from_address: "Address"
    label_prep_preference: LabelPrepPreference
    inbound_shipment_plan_request_items: List["InboundShipmentPlanRequestItem"]
    ship_to_country_code: Union[Unset, str] = UNSET
    ship_to_country_subdivision_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ship_from_address = self.ship_from_address.to_dict()

        label_prep_preference = self.label_prep_preference.value

        inbound_shipment_plan_request_items = []
        for (
            componentsschemas_inbound_shipment_plan_request_item_list_item_data
        ) in self.inbound_shipment_plan_request_items:
            componentsschemas_inbound_shipment_plan_request_item_list_item = (
                componentsschemas_inbound_shipment_plan_request_item_list_item_data.to_dict()
            )

            inbound_shipment_plan_request_items.append(componentsschemas_inbound_shipment_plan_request_item_list_item)

        ship_to_country_code = self.ship_to_country_code
        ship_to_country_subdivision_code = self.ship_to_country_subdivision_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipFromAddress": ship_from_address,
                "LabelPrepPreference": label_prep_preference,
                "InboundShipmentPlanRequestItems": inbound_shipment_plan_request_items,
            }
        )
        if ship_to_country_code is not UNSET:
            field_dict["ShipToCountryCode"] = ship_to_country_code
        if ship_to_country_subdivision_code is not UNSET:
            field_dict["ShipToCountrySubdivisionCode"] = ship_to_country_subdivision_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.inbound_shipment_plan_request_item import InboundShipmentPlanRequestItem

        d = src_dict.copy()
        ship_from_address = Address.from_dict(d.pop("ShipFromAddress"))

        label_prep_preference = LabelPrepPreference(d.pop("LabelPrepPreference"))

        inbound_shipment_plan_request_items = []
        _inbound_shipment_plan_request_items = d.pop("InboundShipmentPlanRequestItems")
        for componentsschemas_inbound_shipment_plan_request_item_list_item_data in _inbound_shipment_plan_request_items:
            componentsschemas_inbound_shipment_plan_request_item_list_item = InboundShipmentPlanRequestItem.from_dict(
                componentsschemas_inbound_shipment_plan_request_item_list_item_data
            )

            inbound_shipment_plan_request_items.append(componentsschemas_inbound_shipment_plan_request_item_list_item)

        ship_to_country_code = d.pop("ShipToCountryCode", UNSET)

        ship_to_country_subdivision_code = d.pop("ShipToCountrySubdivisionCode", UNSET)

        result = cls(
            ship_from_address=ship_from_address,
            label_prep_preference=label_prep_preference,
            inbound_shipment_plan_request_items=inbound_shipment_plan_request_items,
            ship_to_country_code=ship_to_country_code,
            ship_to_country_subdivision_code=ship_to_country_subdivision_code,
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
