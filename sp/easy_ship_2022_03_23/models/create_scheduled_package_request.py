from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.package_details import PackageDetails


T = TypeVar("T", bound="CreateScheduledPackageRequest")


@attr.s(auto_attribs=True)
class CreateScheduledPackageRequest:
    r"""The request schema for the `createScheduledPackage` operation.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier. Identifies the order that the seller wants to deliver
            using Amazon Easy Ship.
        marketplace_id (str): A string of up to 255 characters.
        package_details (PackageDetails): Package details. Includes `packageItems`, `packageTimeSlot`, and
            `packageIdentifier`.
    """

    amazon_order_id: str
    marketplace_id: str
    package_details: "PackageDetails"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        marketplace_id = self.marketplace_id
        package_details = self.package_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonOrderId": amazon_order_id,
                "marketplaceId": marketplace_id,
                "packageDetails": package_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_details import PackageDetails

        d = src_dict.copy()
        amazon_order_id = d.pop("amazonOrderId")

        marketplace_id = d.pop("marketplaceId")

        package_details = PackageDetails.from_dict(d.pop("packageDetails"))

        result = cls(
            amazon_order_id=amazon_order_id,
            marketplace_id=marketplace_id,
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
