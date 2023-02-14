from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package import Package
    from ..models.rejected_order import RejectedOrder


T = TypeVar("T", bound="CreateScheduledPackagesResponse")


@attr.s(auto_attribs=True)
class CreateScheduledPackagesResponse:
    r"""The response schema for the bulk scheduling API. It returns by the bulk scheduling API containing an array of the
    scheduled packtages, an optional list of orders we couldn't schedule with the reason, and a pre-signed URL for a ZIP
    file containing the associated shipping labels plus the documents enabled for your marketplace.

        Attributes:
            scheduled_packages (Union[Unset, List['Package']]): A list of packages. Refer to the `Package` object.
            rejected_orders (Union[Unset, List['RejectedOrder']]): A list of orders we couldn't scheduled on your behalf.
                Each element contains the reason and details on the error.
            printable_documents_url (Union[Unset, str]): A pre-signed URL for the zip document containing the shipping
                labels and the documents enabled for your marketplace.
    """

    scheduled_packages: Union[Unset, List["Package"]] = UNSET
    rejected_orders: Union[Unset, List["RejectedOrder"]] = UNSET
    printable_documents_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_packages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scheduled_packages, Unset):
            scheduled_packages = []
            for scheduled_packages_item_data in self.scheduled_packages:
                scheduled_packages_item = scheduled_packages_item_data.to_dict()

                scheduled_packages.append(scheduled_packages_item)

        rejected_orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rejected_orders, Unset):
            rejected_orders = []
            for rejected_orders_item_data in self.rejected_orders:
                rejected_orders_item = rejected_orders_item_data.to_dict()

                rejected_orders.append(rejected_orders_item)

        printable_documents_url = self.printable_documents_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheduled_packages is not UNSET:
            field_dict["scheduledPackages"] = scheduled_packages
        if rejected_orders is not UNSET:
            field_dict["rejectedOrders"] = rejected_orders
        if printable_documents_url is not UNSET:
            field_dict["printableDocumentsUrl"] = printable_documents_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package import Package
        from ..models.rejected_order import RejectedOrder

        d = src_dict.copy()
        scheduled_packages = []
        _scheduled_packages = d.pop("scheduledPackages", UNSET)
        for scheduled_packages_item_data in _scheduled_packages or []:
            scheduled_packages_item = Package.from_dict(scheduled_packages_item_data)

            scheduled_packages.append(scheduled_packages_item)

        rejected_orders = []
        _rejected_orders = d.pop("rejectedOrders", UNSET)
        for rejected_orders_item_data in _rejected_orders or []:
            rejected_orders_item = RejectedOrder.from_dict(rejected_orders_item_data)

            rejected_orders.append(rejected_orders_item)

        printable_documents_url = d.pop("printableDocumentsUrl", UNSET)

        result = cls(
            scheduled_packages=scheduled_packages,
            rejected_orders=rejected_orders,
            printable_documents_url=printable_documents_url,
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
