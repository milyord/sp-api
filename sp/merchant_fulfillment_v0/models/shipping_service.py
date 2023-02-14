import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.label_format import LabelFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_shipping_service_options import AvailableShippingServiceOptions
    from ..models.currency_amount import CurrencyAmount
    from ..models.label_format_option import LabelFormatOption
    from ..models.shipping_service_options import ShippingServiceOptions


T = TypeVar("T", bound="ShippingService")


@attr.s(auto_attribs=True)
class ShippingService:
    r"""A shipping service offer made by a carrier.

    Attributes:
        shipping_service_name (str): A plain text representation of a carrier's shipping service. For example, "UPS
            Ground" or "FedEx Standard Overnight".
        carrier_name (str): The name of the carrier.
        shipping_service_id (str): An Amazon-defined shipping service identifier.
        shipping_service_offer_id (str): An Amazon-defined shipping service offer identifier.
        ship_date (datetime.datetime):
        rate (CurrencyAmount): Currency type and amount.
        shipping_service_options (ShippingServiceOptions): Extra services provided by a carrier.
        requires_additional_seller_inputs (bool): When true, additional seller inputs are required.
        earliest_estimated_delivery_date (Union[Unset, datetime.datetime]):
        latest_estimated_delivery_date (Union[Unset, datetime.datetime]):
        available_shipping_service_options (Union[Unset, AvailableShippingServiceOptions]): The available shipping
            service options.
        available_label_formats (Union[Unset, List[LabelFormat]]): List of label formats.
        available_format_options_for_label (Union[Unset, List['LabelFormatOption']]): The available label formats.
    """

    shipping_service_name: str
    carrier_name: str
    shipping_service_id: str
    shipping_service_offer_id: str
    ship_date: datetime.datetime
    rate: "CurrencyAmount"
    shipping_service_options: "ShippingServiceOptions"
    requires_additional_seller_inputs: bool
    earliest_estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    latest_estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    available_shipping_service_options: Union[Unset, "AvailableShippingServiceOptions"] = UNSET
    available_label_formats: Union[Unset, List[LabelFormat]] = UNSET
    available_format_options_for_label: Union[Unset, List["LabelFormatOption"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipping_service_name = self.shipping_service_name
        carrier_name = self.carrier_name
        shipping_service_id = self.shipping_service_id
        shipping_service_offer_id = self.shipping_service_offer_id
        ship_date = self.ship_date.isoformat()

        rate = self.rate.to_dict()

        shipping_service_options = self.shipping_service_options.to_dict()

        requires_additional_seller_inputs = self.requires_additional_seller_inputs
        earliest_estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.earliest_estimated_delivery_date, Unset):
            earliest_estimated_delivery_date = self.earliest_estimated_delivery_date.isoformat()

        latest_estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_estimated_delivery_date, Unset):
            latest_estimated_delivery_date = self.latest_estimated_delivery_date.isoformat()

        available_shipping_service_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_shipping_service_options, Unset):
            available_shipping_service_options = self.available_shipping_service_options.to_dict()

        available_label_formats: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_label_formats, Unset):
            available_label_formats = []
            for componentsschemas_label_format_list_item_data in self.available_label_formats:
                componentsschemas_label_format_list_item = componentsschemas_label_format_list_item_data.value

                available_label_formats.append(componentsschemas_label_format_list_item)

        available_format_options_for_label: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_format_options_for_label, Unset):
            available_format_options_for_label = []
            for (
                componentsschemas_available_format_options_for_label_list_item_data
            ) in self.available_format_options_for_label:
                componentsschemas_available_format_options_for_label_list_item = (
                    componentsschemas_available_format_options_for_label_list_item_data.to_dict()
                )

                available_format_options_for_label.append(
                    componentsschemas_available_format_options_for_label_list_item
                )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShippingServiceName": shipping_service_name,
                "CarrierName": carrier_name,
                "ShippingServiceId": shipping_service_id,
                "ShippingServiceOfferId": shipping_service_offer_id,
                "ShipDate": ship_date,
                "Rate": rate,
                "ShippingServiceOptions": shipping_service_options,
                "RequiresAdditionalSellerInputs": requires_additional_seller_inputs,
            }
        )
        if earliest_estimated_delivery_date is not UNSET:
            field_dict["EarliestEstimatedDeliveryDate"] = earliest_estimated_delivery_date
        if latest_estimated_delivery_date is not UNSET:
            field_dict["LatestEstimatedDeliveryDate"] = latest_estimated_delivery_date
        if available_shipping_service_options is not UNSET:
            field_dict["AvailableShippingServiceOptions"] = available_shipping_service_options
        if available_label_formats is not UNSET:
            field_dict["AvailableLabelFormats"] = available_label_formats
        if available_format_options_for_label is not UNSET:
            field_dict["AvailableFormatOptionsForLabel"] = available_format_options_for_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.available_shipping_service_options import AvailableShippingServiceOptions
        from ..models.currency_amount import CurrencyAmount
        from ..models.label_format_option import LabelFormatOption
        from ..models.shipping_service_options import ShippingServiceOptions

        d = src_dict.copy()
        shipping_service_name = d.pop("ShippingServiceName")

        carrier_name = d.pop("CarrierName")

        shipping_service_id = d.pop("ShippingServiceId")

        shipping_service_offer_id = d.pop("ShippingServiceOfferId")

        ship_date = isoparse(d.pop("ShipDate"))

        rate = CurrencyAmount.from_dict(d.pop("Rate"))

        shipping_service_options = ShippingServiceOptions.from_dict(d.pop("ShippingServiceOptions"))

        requires_additional_seller_inputs = d.pop("RequiresAdditionalSellerInputs")

        _earliest_estimated_delivery_date = d.pop("EarliestEstimatedDeliveryDate", UNSET)
        earliest_estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_earliest_estimated_delivery_date, Unset):
            earliest_estimated_delivery_date = UNSET
        else:
            earliest_estimated_delivery_date = isoparse(_earliest_estimated_delivery_date)

        _latest_estimated_delivery_date = d.pop("LatestEstimatedDeliveryDate", UNSET)
        latest_estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_estimated_delivery_date, Unset):
            latest_estimated_delivery_date = UNSET
        else:
            latest_estimated_delivery_date = isoparse(_latest_estimated_delivery_date)

        _available_shipping_service_options = d.pop("AvailableShippingServiceOptions", UNSET)
        available_shipping_service_options: Union[Unset, AvailableShippingServiceOptions]
        if isinstance(_available_shipping_service_options, Unset):
            available_shipping_service_options = UNSET
        else:
            available_shipping_service_options = AvailableShippingServiceOptions.from_dict(
                _available_shipping_service_options
            )

        available_label_formats = []
        _available_label_formats = d.pop("AvailableLabelFormats", UNSET)
        for componentsschemas_label_format_list_item_data in _available_label_formats or []:
            componentsschemas_label_format_list_item = LabelFormat(componentsschemas_label_format_list_item_data)

            available_label_formats.append(componentsschemas_label_format_list_item)

        available_format_options_for_label = []
        _available_format_options_for_label = d.pop("AvailableFormatOptionsForLabel", UNSET)
        for componentsschemas_available_format_options_for_label_list_item_data in (
            _available_format_options_for_label or []
        ):
            componentsschemas_available_format_options_for_label_list_item = LabelFormatOption.from_dict(
                componentsschemas_available_format_options_for_label_list_item_data
            )

            available_format_options_for_label.append(componentsschemas_available_format_options_for_label_list_item)

        result = cls(
            shipping_service_name=shipping_service_name,
            carrier_name=carrier_name,
            shipping_service_id=shipping_service_id,
            shipping_service_offer_id=shipping_service_offer_id,
            ship_date=ship_date,
            rate=rate,
            shipping_service_options=shipping_service_options,
            requires_additional_seller_inputs=requires_additional_seller_inputs,
            earliest_estimated_delivery_date=earliest_estimated_delivery_date,
            latest_estimated_delivery_date=latest_estimated_delivery_date,
            available_shipping_service_options=available_shipping_service_options,
            available_label_formats=available_label_formats,
            available_format_options_for_label=available_format_options_for_label,
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
