from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_details import PackageDetails


T = TypeVar("T", bound="OrderScheduleDetails")


@attr.s(auto_attribs=True)
class OrderScheduleDetails:
    r"""This object allows users to specify an order to be scheduled. Only the amazonOrderId is required.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier. Identifies the order that the seller wants to deliver
            using Amazon Easy Ship.
        package_details (Union[Unset, PackageDetails]): Package details. Includes `packageItems`, `packageTimeSlot`, and
            `packageIdentifier`.
    """

    amazon_order_id: str
    package_details: Union[Unset, "PackageDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        package_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_details, Unset):
            package_details = self.package_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonOrderId": amazon_order_id,
            }
        )
        if package_details is not UNSET:
            field_dict["packageDetails"] = package_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_details import PackageDetails

        d = src_dict.copy()
        amazon_order_id = d.pop("amazonOrderId")

        _package_details = d.pop("packageDetails", UNSET)
        package_details: Union[Unset, PackageDetails]
        if isinstance(_package_details, Unset):
            package_details = UNSET
        else:
            package_details = PackageDetails.from_dict(_package_details)

        result = cls(
            amazon_order_id=amazon_order_id,
            package_details=package_details,
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
