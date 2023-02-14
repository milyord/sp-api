from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimensions import Dimensions


T = TypeVar("T", bound="ItemDimensionsByMarketplace")


@attr.s(auto_attribs=True)
class ItemDimensionsByMarketplace:
    r"""Dimensions associated with the item in the Amazon catalog for the indicated Amazon marketplace.

    Attributes:
        marketplace_id (str): Amazon marketplace identifier.
        item (Union[Unset, Dimensions]): Dimensions of an Amazon catalog item or item in its packaging.
        package (Union[Unset, Dimensions]): Dimensions of an Amazon catalog item or item in its packaging.
    """

    marketplace_id: str
    item: Union[Unset, "Dimensions"] = UNSET
    package: Union[Unset, "Dimensions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
            }
        )
        if item is not UNSET:
            field_dict["item"] = item
        if package is not UNSET:
            field_dict["package"] = package

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensions import Dimensions

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        _item = d.pop("item", UNSET)
        item: Union[Unset, Dimensions]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = Dimensions.from_dict(_item)

        _package = d.pop("package", UNSET)
        package: Union[Unset, Dimensions]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = Dimensions.from_dict(_package)

        result = cls(
            marketplace_id=marketplace_id,
            item=item,
            package=package,
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
