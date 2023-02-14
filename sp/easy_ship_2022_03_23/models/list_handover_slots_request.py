from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.dimensions import Dimensions
    from ..models.weight import Weight


T = TypeVar("T", bound="ListHandoverSlotsRequest")


@attr.s(auto_attribs=True)
class ListHandoverSlotsRequest:
    r"""The request schema for the `listHandoverSlots` operation.

    Attributes:
        marketplace_id (str): A string of up to 255 characters.
        amazon_order_id (str): An Amazon-defined order identifier. Identifies the order that the seller wants to deliver
            using Amazon Easy Ship.
        package_dimensions (Dimensions): The dimensions of the scheduled package.
        package_weight (Weight): The weight of the scheduled package
    """

    marketplace_id: str
    amazon_order_id: str
    package_dimensions: "Dimensions"
    package_weight: "Weight"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        amazon_order_id = self.amazon_order_id
        package_dimensions = self.package_dimensions.to_dict()

        package_weight = self.package_weight.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "amazonOrderId": amazon_order_id,
                "packageDimensions": package_dimensions,
                "packageWeight": package_weight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensions import Dimensions
        from ..models.weight import Weight

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        amazon_order_id = d.pop("amazonOrderId")

        package_dimensions = Dimensions.from_dict(d.pop("packageDimensions"))

        package_weight = Weight.from_dict(d.pop("packageWeight"))

        result = cls(
            marketplace_id=marketplace_id,
            amazon_order_id=amazon_order_id,
            package_dimensions=package_dimensions,
            package_weight=package_weight,
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
