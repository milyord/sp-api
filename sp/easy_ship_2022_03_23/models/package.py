from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.package_status import PackageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimensions import Dimensions
    from ..models.invoice_data import InvoiceData
    from ..models.item import Item
    from ..models.scheduled_package_id import ScheduledPackageId
    from ..models.time_slot import TimeSlot
    from ..models.tracking_details import TrackingDetails
    from ..models.weight import Weight


T = TypeVar("T", bound="Package")


@attr.s(auto_attribs=True)
class Package:
    r"""A package. This object contains all the details of the scheduled Easy Ship package including the package identifier,
    physical attributes such as dimensions and weight, selected time slot to handover the package to carrier, status of
    the package, and tracking/invoice details.

        Attributes:
            scheduled_package_id (ScheduledPackageId): Identifies the scheduled package to be updated.
            package_dimensions (Dimensions): The dimensions of the scheduled package.
            package_weight (Weight): The weight of the scheduled package
            package_time_slot (TimeSlot): A time window to hand over an Easy Ship package to Amazon Logistics.
            package_items (Union[Unset, List['Item']]): A list of items contained in the package.
            package_identifier (Union[Unset, str]): Optional seller-created identifier that is printed on the shipping label
                to help the seller identify the package.
            invoice (Union[Unset, InvoiceData]): Invoice number and date.
            package_status (Union[Unset, PackageStatus]): The status of the package.
            tracking_details (Union[Unset, TrackingDetails]): Representation of tracking metadata.
    """

    scheduled_package_id: "ScheduledPackageId"
    package_dimensions: "Dimensions"
    package_weight: "Weight"
    package_time_slot: "TimeSlot"
    package_items: Union[Unset, List["Item"]] = UNSET
    package_identifier: Union[Unset, str] = UNSET
    invoice: Union[Unset, "InvoiceData"] = UNSET
    package_status: Union[Unset, PackageStatus] = UNSET
    tracking_details: Union[Unset, "TrackingDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_package_id = self.scheduled_package_id.to_dict()

        package_dimensions = self.package_dimensions.to_dict()

        package_weight = self.package_weight.to_dict()

        package_time_slot = self.package_time_slot.to_dict()

        package_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.package_items, Unset):
            package_items = []
            for componentsschemas_items_item_data in self.package_items:
                componentsschemas_items_item = componentsschemas_items_item_data.to_dict()

                package_items.append(componentsschemas_items_item)

        package_identifier = self.package_identifier
        invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice, Unset):
            invoice = self.invoice.to_dict()

        package_status: Union[Unset, str] = UNSET
        if not isinstance(self.package_status, Unset):
            package_status = self.package_status.value

        tracking_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking_details, Unset):
            tracking_details = self.tracking_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledPackageId": scheduled_package_id,
                "packageDimensions": package_dimensions,
                "packageWeight": package_weight,
                "packageTimeSlot": package_time_slot,
            }
        )
        if package_items is not UNSET:
            field_dict["packageItems"] = package_items
        if package_identifier is not UNSET:
            field_dict["packageIdentifier"] = package_identifier
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if package_status is not UNSET:
            field_dict["packageStatus"] = package_status
        if tracking_details is not UNSET:
            field_dict["trackingDetails"] = tracking_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensions import Dimensions
        from ..models.invoice_data import InvoiceData
        from ..models.item import Item
        from ..models.scheduled_package_id import ScheduledPackageId
        from ..models.time_slot import TimeSlot
        from ..models.tracking_details import TrackingDetails
        from ..models.weight import Weight

        d = src_dict.copy()
        scheduled_package_id = ScheduledPackageId.from_dict(d.pop("scheduledPackageId"))

        package_dimensions = Dimensions.from_dict(d.pop("packageDimensions"))

        package_weight = Weight.from_dict(d.pop("packageWeight"))

        package_time_slot = TimeSlot.from_dict(d.pop("packageTimeSlot"))

        package_items = []
        _package_items = d.pop("packageItems", UNSET)
        for componentsschemas_items_item_data in _package_items or []:
            componentsschemas_items_item = Item.from_dict(componentsschemas_items_item_data)

            package_items.append(componentsschemas_items_item)

        package_identifier = d.pop("packageIdentifier", UNSET)

        _invoice = d.pop("invoice", UNSET)
        invoice: Union[Unset, InvoiceData]
        if isinstance(_invoice, Unset):
            invoice = UNSET
        else:
            invoice = InvoiceData.from_dict(_invoice)

        _package_status = d.pop("packageStatus", UNSET)
        package_status: Union[Unset, PackageStatus]
        if isinstance(_package_status, Unset):
            package_status = UNSET
        else:
            package_status = PackageStatus(_package_status)

        _tracking_details = d.pop("trackingDetails", UNSET)
        tracking_details: Union[Unset, TrackingDetails]
        if isinstance(_tracking_details, Unset):
            tracking_details = UNSET
        else:
            tracking_details = TrackingDetails.from_dict(_tracking_details)

        result = cls(
            scheduled_package_id=scheduled_package_id,
            package_dimensions=package_dimensions,
            package_weight=package_weight,
            package_time_slot=package_time_slot,
            package_items=package_items,
            package_identifier=package_identifier,
            invoice=invoice,
            package_status=package_status,
            tracking_details=tracking_details,
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
