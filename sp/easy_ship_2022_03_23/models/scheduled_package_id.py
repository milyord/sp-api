from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduledPackageId")


@attr.s(auto_attribs=True)
class ScheduledPackageId:
    r"""Identifies the scheduled package to be updated.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier. Identifies the order that the seller wants to deliver
            using Amazon Easy Ship.
        package_id (Union[Unset, str]): An Amazon-defined identifier for the scheduled package.
    """

    amazon_order_id: str
    package_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        package_id = self.package_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amazonOrderId": amazon_order_id,
            }
        )
        if package_id is not UNSET:
            field_dict["packageId"] = package_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amazon_order_id = d.pop("amazonOrderId")

        package_id = d.pop("packageId", UNSET)

        result = cls(
            amazon_order_id=amazon_order_id,
            package_id=package_id,
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
