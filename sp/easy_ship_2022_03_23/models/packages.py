from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.package import Package


T = TypeVar("T", bound="Packages")


@attr.s(auto_attribs=True)
class Packages:
    r"""A list of packages.

    Attributes:
        packages (List['Package']):
    """

    packages: List["Package"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()

            packages.append(packages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packages": packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package import Package

        d = src_dict.copy()
        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = Package.from_dict(packages_item_data)

            packages.append(packages_item)

        result = cls(
            packages=packages,
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
