from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_container_type import ContainerContainerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.container_item import ContainerItem
    from ..models.currency import Currency
    from ..models.dimensions import Dimensions
    from ..models.weight import Weight


T = TypeVar("T", bound="Container")


@attr.s(auto_attribs=True)
class Container:
    r"""Container in the shipment.

    Attributes:
        container_reference_id (str): An identifier for the container. This must be unique within all the containers in
            the same shipment.
        value (Currency): The total value of all items in the container.
        dimensions (Dimensions): A set of measurements for a three-dimensional object.
        items (List['ContainerItem']): A list of the items in the container.
        weight (Weight): The weight.
        container_type (Union[Unset, ContainerContainerType]): The type of physical container being used. (always
            'PACKAGE')
    """

    container_reference_id: str
    value: "Currency"
    dimensions: "Dimensions"
    items: List["ContainerItem"]
    weight: "Weight"
    container_type: Union[Unset, ContainerContainerType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_reference_id = self.container_reference_id
        value = self.value.to_dict()

        dimensions = self.dimensions.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        weight = self.weight.to_dict()

        container_type: Union[Unset, str] = UNSET
        if not isinstance(self.container_type, Unset):
            container_type = self.container_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerReferenceId": container_reference_id,
                "value": value,
                "dimensions": dimensions,
                "items": items,
                "weight": weight,
            }
        )
        if container_type is not UNSET:
            field_dict["containerType"] = container_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.container_item import ContainerItem
        from ..models.currency import Currency
        from ..models.dimensions import Dimensions
        from ..models.weight import Weight

        d = src_dict.copy()
        container_reference_id = d.pop("containerReferenceId")

        value = Currency.from_dict(d.pop("value"))

        dimensions = Dimensions.from_dict(d.pop("dimensions"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ContainerItem.from_dict(items_item_data)

            items.append(items_item)

        weight = Weight.from_dict(d.pop("weight"))

        _container_type = d.pop("containerType", UNSET)
        container_type: Union[Unset, ContainerContainerType]
        if isinstance(_container_type, Unset):
            container_type = UNSET
        else:
            container_type = ContainerContainerType(_container_type)

        result = cls(
            container_reference_id=container_reference_id,
            value=value,
            dimensions=dimensions,
            items=items,
            weight=weight,
            container_type=container_type,
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
