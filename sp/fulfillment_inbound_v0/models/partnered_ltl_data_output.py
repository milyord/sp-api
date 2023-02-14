import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.seller_freight_class import SellerFreightClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.contact import Contact
    from ..models.pallet import Pallet
    from ..models.partnered_estimate import PartneredEstimate
    from ..models.weight import Weight


T = TypeVar("T", bound="PartneredLtlDataOutput")


@attr.s(auto_attribs=True)
class PartneredLtlDataOutput:
    r"""Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by an Amazon-partnered
    carrier.

        Attributes:
            contact (Contact): Contact information for the person in the seller's organization who is responsible for a Less
                Than Truckload/Full Truckload (LTL/FTL) shipment.
            box_count (int):
            freight_ready_date (datetime.date):
            pallet_list (List['Pallet']): A list of pallet information.
            total_weight (Weight): The weight of the package.
            preview_pickup_date (datetime.date):
            preview_delivery_date (datetime.date):
            preview_freight_class (SellerFreightClass): The freight class of the shipment. For information about determining
                the freight class, contact the carrier.
            amazon_reference_id (str): A unique identifier created by Amazon that identifies this Amazon-partnered, Less
                Than Truckload/Full Truckload (LTL/FTL) shipment.
            is_bill_of_lading_available (bool): Indicates whether the bill of lading for the shipment is available.
            carrier_name (str): The carrier for the inbound shipment.
            seller_freight_class (Union[Unset, SellerFreightClass]): The freight class of the shipment. For information
                about determining the freight class, contact the carrier.
            seller_declared_value (Union[Unset, Amount]): The monetary value.
            amazon_calculated_value (Union[Unset, Amount]): The monetary value.
            partnered_estimate (Union[Unset, PartneredEstimate]): The estimated shipping cost for a shipment using an
                Amazon-partnered carrier.
    """

    contact: "Contact"
    box_count: int
    freight_ready_date: datetime.date
    pallet_list: List["Pallet"]
    total_weight: "Weight"
    preview_pickup_date: datetime.date
    preview_delivery_date: datetime.date
    preview_freight_class: SellerFreightClass
    amazon_reference_id: str
    is_bill_of_lading_available: bool
    carrier_name: str
    seller_freight_class: Union[Unset, SellerFreightClass] = UNSET
    seller_declared_value: Union[Unset, "Amount"] = UNSET
    amazon_calculated_value: Union[Unset, "Amount"] = UNSET
    partnered_estimate: Union[Unset, "PartneredEstimate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact = self.contact.to_dict()

        box_count = self.box_count
        freight_ready_date = self.freight_ready_date.isoformat()
        pallet_list = []
        for componentsschemas_pallet_list_item_data in self.pallet_list:
            componentsschemas_pallet_list_item = componentsschemas_pallet_list_item_data.to_dict()

            pallet_list.append(componentsschemas_pallet_list_item)

        total_weight = self.total_weight.to_dict()

        preview_pickup_date = self.preview_pickup_date.isoformat()
        preview_delivery_date = self.preview_delivery_date.isoformat()
        preview_freight_class = self.preview_freight_class.value

        amazon_reference_id = self.amazon_reference_id
        is_bill_of_lading_available = self.is_bill_of_lading_available
        carrier_name = self.carrier_name
        seller_freight_class: Union[Unset, str] = UNSET
        if not isinstance(self.seller_freight_class, Unset):
            seller_freight_class = self.seller_freight_class.value

        seller_declared_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_declared_value, Unset):
            seller_declared_value = self.seller_declared_value.to_dict()

        amazon_calculated_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amazon_calculated_value, Unset):
            amazon_calculated_value = self.amazon_calculated_value.to_dict()

        partnered_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.partnered_estimate, Unset):
            partnered_estimate = self.partnered_estimate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Contact": contact,
                "BoxCount": box_count,
                "FreightReadyDate": freight_ready_date,
                "PalletList": pallet_list,
                "TotalWeight": total_weight,
                "PreviewPickupDate": preview_pickup_date,
                "PreviewDeliveryDate": preview_delivery_date,
                "PreviewFreightClass": preview_freight_class,
                "AmazonReferenceId": amazon_reference_id,
                "IsBillOfLadingAvailable": is_bill_of_lading_available,
                "CarrierName": carrier_name,
            }
        )
        if seller_freight_class is not UNSET:
            field_dict["SellerFreightClass"] = seller_freight_class
        if seller_declared_value is not UNSET:
            field_dict["SellerDeclaredValue"] = seller_declared_value
        if amazon_calculated_value is not UNSET:
            field_dict["AmazonCalculatedValue"] = amazon_calculated_value
        if partnered_estimate is not UNSET:
            field_dict["PartneredEstimate"] = partnered_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount import Amount
        from ..models.contact import Contact
        from ..models.pallet import Pallet
        from ..models.partnered_estimate import PartneredEstimate
        from ..models.weight import Weight

        d = src_dict.copy()
        contact = Contact.from_dict(d.pop("Contact"))

        box_count = d.pop("BoxCount")

        freight_ready_date = isoparse(d.pop("FreightReadyDate")).date()

        pallet_list = []
        _pallet_list = d.pop("PalletList")
        for componentsschemas_pallet_list_item_data in _pallet_list:
            componentsschemas_pallet_list_item = Pallet.from_dict(componentsschemas_pallet_list_item_data)

            pallet_list.append(componentsschemas_pallet_list_item)

        total_weight = Weight.from_dict(d.pop("TotalWeight"))

        preview_pickup_date = isoparse(d.pop("PreviewPickupDate")).date()

        preview_delivery_date = isoparse(d.pop("PreviewDeliveryDate")).date()

        preview_freight_class = SellerFreightClass(d.pop("PreviewFreightClass"))

        amazon_reference_id = d.pop("AmazonReferenceId")

        is_bill_of_lading_available = d.pop("IsBillOfLadingAvailable")

        carrier_name = d.pop("CarrierName")

        _seller_freight_class = d.pop("SellerFreightClass", UNSET)
        seller_freight_class: Union[Unset, SellerFreightClass]
        if isinstance(_seller_freight_class, Unset):
            seller_freight_class = UNSET
        else:
            seller_freight_class = SellerFreightClass(_seller_freight_class)

        _seller_declared_value = d.pop("SellerDeclaredValue", UNSET)
        seller_declared_value: Union[Unset, Amount]
        if isinstance(_seller_declared_value, Unset):
            seller_declared_value = UNSET
        else:
            seller_declared_value = Amount.from_dict(_seller_declared_value)

        _amazon_calculated_value = d.pop("AmazonCalculatedValue", UNSET)
        amazon_calculated_value: Union[Unset, Amount]
        if isinstance(_amazon_calculated_value, Unset):
            amazon_calculated_value = UNSET
        else:
            amazon_calculated_value = Amount.from_dict(_amazon_calculated_value)

        _partnered_estimate = d.pop("PartneredEstimate", UNSET)
        partnered_estimate: Union[Unset, PartneredEstimate]
        if isinstance(_partnered_estimate, Unset):
            partnered_estimate = UNSET
        else:
            partnered_estimate = PartneredEstimate.from_dict(_partnered_estimate)

        result = cls(
            contact=contact,
            box_count=box_count,
            freight_ready_date=freight_ready_date,
            pallet_list=pallet_list,
            total_weight=total_weight,
            preview_pickup_date=preview_pickup_date,
            preview_delivery_date=preview_delivery_date,
            preview_freight_class=preview_freight_class,
            amazon_reference_id=amazon_reference_id,
            is_bill_of_lading_available=is_bill_of_lading_available,
            carrier_name=carrier_name,
            seller_freight_class=seller_freight_class,
            seller_declared_value=seller_declared_value,
            amazon_calculated_value=amazon_calculated_value,
            partnered_estimate=partnered_estimate,
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
