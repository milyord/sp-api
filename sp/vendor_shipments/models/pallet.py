from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carton_reference_details import CartonReferenceDetails
    from ..models.container_identification import ContainerIdentification
    from ..models.container_item import ContainerItem
    from ..models.dimensions import Dimensions
    from ..models.weight import Weight


T = TypeVar("T", bound="Pallet")


@attr.s(auto_attribs=True)
class Pallet:
    r"""Details of the Pallet/Tare being shipped.

    Attributes:
        pallet_identifiers (List['ContainerIdentification']): A list of pallet identifiers.
        tier (Union[Unset, int]): Number of layers per pallet.
        block (Union[Unset, int]): Number of cartons per layer on the pallet.
        dimensions (Union[Unset, Dimensions]): Physical dimensional measurements of a container.
        weight (Union[Unset, Weight]): The weight.
        carton_reference_details (Union[Unset, CartonReferenceDetails]):
        items (Union[Unset, List['ContainerItem']]): A list of container item details.
    """

    pallet_identifiers: List["ContainerIdentification"]
    tier: Union[Unset, int] = UNSET
    block: Union[Unset, int] = UNSET
    dimensions: Union[Unset, "Dimensions"] = UNSET
    weight: Union[Unset, "Weight"] = UNSET
    carton_reference_details: Union[Unset, "CartonReferenceDetails"] = UNSET
    items: Union[Unset, List["ContainerItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pallet_identifiers = []
        for pallet_identifiers_item_data in self.pallet_identifiers:
            pallet_identifiers_item = pallet_identifiers_item_data.to_dict()

            pallet_identifiers.append(pallet_identifiers_item)

        tier = self.tier
        block = self.block
        dimensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        carton_reference_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.carton_reference_details, Unset):
            carton_reference_details = self.carton_reference_details.to_dict()

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "palletIdentifiers": pallet_identifiers,
            }
        )
        if tier is not UNSET:
            field_dict["tier"] = tier
        if block is not UNSET:
            field_dict["block"] = block
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if weight is not UNSET:
            field_dict["weight"] = weight
        if carton_reference_details is not UNSET:
            field_dict["cartonReferenceDetails"] = carton_reference_details
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.carton_reference_details import CartonReferenceDetails
        from ..models.container_identification import ContainerIdentification
        from ..models.container_item import ContainerItem
        from ..models.dimensions import Dimensions
        from ..models.weight import Weight

        d = src_dict.copy()
        pallet_identifiers = []
        _pallet_identifiers = d.pop("palletIdentifiers")
        for pallet_identifiers_item_data in _pallet_identifiers:
            pallet_identifiers_item = ContainerIdentification.from_dict(pallet_identifiers_item_data)

            pallet_identifiers.append(pallet_identifiers_item)

        tier = d.pop("tier", UNSET)

        block = d.pop("block", UNSET)

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

        _carton_reference_details = d.pop("cartonReferenceDetails", UNSET)
        carton_reference_details: Union[Unset, CartonReferenceDetails]
        if isinstance(_carton_reference_details, Unset):
            carton_reference_details = UNSET
        else:
            carton_reference_details = CartonReferenceDetails.from_dict(_carton_reference_details)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ContainerItem.from_dict(items_item_data)

            items.append(items_item)

        result = cls(
            pallet_identifiers=pallet_identifiers,
            tier=tier,
            block=block,
            dimensions=dimensions,
            weight=weight,
            carton_reference_details=carton_reference_details,
            items=items,
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
