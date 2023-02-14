from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.hazmat_type import HazmatType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_seller_inputs import AdditionalSellerInputs
    from ..models.label_format_option_request import LabelFormatOptionRequest
    from ..models.shipment_request_details import ShipmentRequestDetails


T = TypeVar("T", bound="CreateShipmentRequest")


@attr.s(auto_attribs=True)
class CreateShipmentRequest:
    r"""Request schema.

    Attributes:
        shipment_request_details (ShipmentRequestDetails): Shipment information required for requesting shipping service
            offers or for creating a shipment.
        shipping_service_id (str): An Amazon-defined shipping service identifier.
        shipping_service_offer_id (Union[Unset, str]): Identifies a shipping service order made by a carrier.
        hazmat_type (Union[Unset, HazmatType]): Hazardous materials options for a package. Consult the terms and
            conditions for each carrier for more information on hazardous materials.
        label_format_option (Union[Unset, LabelFormatOptionRequest]): Whether to include a packing slip.
        shipment_level_seller_inputs_list (Union[Unset, List['AdditionalSellerInputs']]): A list of additional seller
            input pairs required to purchase shipping.
    """

    shipment_request_details: "ShipmentRequestDetails"
    shipping_service_id: str
    shipping_service_offer_id: Union[Unset, str] = UNSET
    hazmat_type: Union[Unset, HazmatType] = UNSET
    label_format_option: Union[Unset, "LabelFormatOptionRequest"] = UNSET
    shipment_level_seller_inputs_list: Union[Unset, List["AdditionalSellerInputs"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_request_details = self.shipment_request_details.to_dict()

        shipping_service_id = self.shipping_service_id
        shipping_service_offer_id = self.shipping_service_offer_id
        hazmat_type: Union[Unset, str] = UNSET
        if not isinstance(self.hazmat_type, Unset):
            hazmat_type = self.hazmat_type.value

        label_format_option: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label_format_option, Unset):
            label_format_option = self.label_format_option.to_dict()

        shipment_level_seller_inputs_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_level_seller_inputs_list, Unset):
            shipment_level_seller_inputs_list = []
            for componentsschemas_additional_seller_inputs_list_item_data in self.shipment_level_seller_inputs_list:
                componentsschemas_additional_seller_inputs_list_item = (
                    componentsschemas_additional_seller_inputs_list_item_data.to_dict()
                )

                shipment_level_seller_inputs_list.append(componentsschemas_additional_seller_inputs_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipmentRequestDetails": shipment_request_details,
                "ShippingServiceId": shipping_service_id,
            }
        )
        if shipping_service_offer_id is not UNSET:
            field_dict["ShippingServiceOfferId"] = shipping_service_offer_id
        if hazmat_type is not UNSET:
            field_dict["HazmatType"] = hazmat_type
        if label_format_option is not UNSET:
            field_dict["LabelFormatOption"] = label_format_option
        if shipment_level_seller_inputs_list is not UNSET:
            field_dict["ShipmentLevelSellerInputsList"] = shipment_level_seller_inputs_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_seller_inputs import AdditionalSellerInputs
        from ..models.label_format_option_request import LabelFormatOptionRequest
        from ..models.shipment_request_details import ShipmentRequestDetails

        d = src_dict.copy()
        shipment_request_details = ShipmentRequestDetails.from_dict(d.pop("ShipmentRequestDetails"))

        shipping_service_id = d.pop("ShippingServiceId")

        shipping_service_offer_id = d.pop("ShippingServiceOfferId", UNSET)

        _hazmat_type = d.pop("HazmatType", UNSET)
        hazmat_type: Union[Unset, HazmatType]
        if isinstance(_hazmat_type, Unset):
            hazmat_type = UNSET
        else:
            hazmat_type = HazmatType(_hazmat_type)

        _label_format_option = d.pop("LabelFormatOption", UNSET)
        label_format_option: Union[Unset, LabelFormatOptionRequest]
        if isinstance(_label_format_option, Unset):
            label_format_option = UNSET
        else:
            label_format_option = LabelFormatOptionRequest.from_dict(_label_format_option)

        shipment_level_seller_inputs_list = []
        _shipment_level_seller_inputs_list = d.pop("ShipmentLevelSellerInputsList", UNSET)
        for componentsschemas_additional_seller_inputs_list_item_data in _shipment_level_seller_inputs_list or []:
            componentsschemas_additional_seller_inputs_list_item = AdditionalSellerInputs.from_dict(
                componentsschemas_additional_seller_inputs_list_item_data
            )

            shipment_level_seller_inputs_list.append(componentsschemas_additional_seller_inputs_list_item)

        result = cls(
            shipment_request_details=shipment_request_details,
            shipping_service_id=shipping_service_id,
            shipping_service_offer_id=shipping_service_offer_id,
            hazmat_type=hazmat_type,
            label_format_option=label_format_option,
            shipment_level_seller_inputs_list=shipment_level_seller_inputs_list,
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
