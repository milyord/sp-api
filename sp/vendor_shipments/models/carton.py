from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.container_identification import ContainerIdentification
    from ..models.container_item import ContainerItem
    from ..models.dimensions import Dimensions
    from ..models.weight import Weight


T = TypeVar("T", bound="Carton")


@attr.s(auto_attribs=True)
class Carton:
    r"""Details of the carton/package being shipped.

    Attributes:
        carton_sequence_number (str): Carton sequence number for the carton. The first carton will be 001, the second
            002, and so on. This number is used as a reference to refer to this carton from the pallet level.
        items (List['ContainerItem']): A list of container item details.
        carton_identifiers (Union[Unset, List['ContainerIdentification']]): A list of carton identifiers.
        dimensions (Union[Unset, Dimensions]): Physical dimensional measurements of a container.
        weight (Union[Unset, Weight]): The weight.
        tracking_number (Union[Unset, str]): This is required to be provided for every carton in the small parcel
            shipments.
    """

    carton_sequence_number: str
    items: List["ContainerItem"]
    carton_identifiers: Union[Unset, List["ContainerIdentification"]] = UNSET
    dimensions: Union[Unset, "Dimensions"] = UNSET
    weight: Union[Unset, "Weight"] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        carton_sequence_number = self.carton_sequence_number
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        carton_identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.carton_identifiers, Unset):
            carton_identifiers = []
            for carton_identifiers_item_data in self.carton_identifiers:
                carton_identifiers_item = carton_identifiers_item_data.to_dict()

                carton_identifiers.append(carton_identifiers_item)

        dimensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        tracking_number = self.tracking_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cartonSequenceNumber": carton_sequence_number,
                "items": items,
            }
        )
        if carton_identifiers is not UNSET:
            field_dict["cartonIdentifiers"] = carton_identifiers
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if weight is not UNSET:
            field_dict["weight"] = weight
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.container_identification import ContainerIdentification
        from ..models.container_item import ContainerItem
        from ..models.dimensions import Dimensions
        from ..models.weight import Weight

        d = src_dict.copy()
        carton_sequence_number = d.pop("cartonSequenceNumber")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ContainerItem.from_dict(items_item_data)

            items.append(items_item)

        carton_identifiers = []
        _carton_identifiers = d.pop("cartonIdentifiers", UNSET)
        for carton_identifiers_item_data in _carton_identifiers or []:
            carton_identifiers_item = ContainerIdentification.from_dict(carton_identifiers_item_data)

            carton_identifiers.append(carton_identifiers_item)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, Dimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = Dimensions.from_dict(_dimensions)

        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, Weight]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Weight.from_dict(_weight)

        tracking_number = d.pop("trackingNumber", UNSET)

        result = cls(
            carton_sequence_number=carton_sequence_number,
            items=items,
            carton_identifiers=carton_identifiers,
            dimensions=dimensions,
            weight=weight,
            tracking_number=tracking_number,
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
