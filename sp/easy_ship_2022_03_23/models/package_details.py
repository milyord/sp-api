from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item import Item
    from ..models.time_slot import TimeSlot


T = TypeVar("T", bound="PackageDetails")


@attr.s(auto_attribs=True)
class PackageDetails:
    r"""Package details. Includes `packageItems`, `packageTimeSlot`, and `packageIdentifier`.

    Attributes:
        package_time_slot (TimeSlot): A time window to hand over an Easy Ship package to Amazon Logistics.
        package_items (Union[Unset, List['Item']]): A list of items contained in the package.
        package_identifier (Union[Unset, str]): Optional seller-created identifier that is printed on the shipping label
            to help the seller identify the package.
    """

    package_time_slot: "TimeSlot"
    package_items: Union[Unset, List["Item"]] = UNSET
    package_identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_time_slot = self.package_time_slot.to_dict()

        package_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.package_items, Unset):
            package_items = []
            for componentsschemas_items_item_data in self.package_items:
                componentsschemas_items_item = componentsschemas_items_item_data.to_dict()

                package_items.append(componentsschemas_items_item)

        package_identifier = self.package_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageTimeSlot": package_time_slot,
            }
        )
        if package_items is not UNSET:
            field_dict["packageItems"] = package_items
        if package_identifier is not UNSET:
            field_dict["packageIdentifier"] = package_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item import Item
        from ..models.time_slot import TimeSlot

        d = src_dict.copy()
        package_time_slot = TimeSlot.from_dict(d.pop("packageTimeSlot"))

        package_items = []
        _package_items = d.pop("packageItems", UNSET)
        for componentsschemas_items_item_data in _package_items or []:
            componentsschemas_items_item = Item.from_dict(componentsschemas_items_item_data)

            package_items.append(componentsschemas_items_item)

        package_identifier = d.pop("packageIdentifier", UNSET)

        result = cls(
            package_time_slot=package_time_slot,
            package_items=package_items,
            package_identifier=package_identifier,
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
