from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.container_container_type import ContainerContainerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimensions import Dimensions
    from ..models.packed_item import PackedItem
    from ..models.weight import Weight


T = TypeVar("T", bound="Container")


@attr.s(auto_attribs=True)
class Container:
    r"""
    Attributes:
        container_type (ContainerContainerType): The type of container.
        container_identifier (str): The container identifier.
        packed_items (List['PackedItem']): A list of packed items.
        tracking_number (Union[Unset, str]): The tracking number.
        manifest_id (Union[Unset, str]): The manifest identifier.
        manifest_date (Union[Unset, str]): The date of the manifest.
        ship_method (Union[Unset, str]): The shipment method. This property is required when calling the
            submitShipmentConfirmations operation, and optional otherwise.
        scac_code (Union[Unset, str]): SCAC code required for NA VOC vendors only.
        carrier (Union[Unset, str]): Carrier required for EU VOC vendors only.
        container_sequence_number (Union[Unset, int]): An integer that must be submitted for multi-box shipments only,
            where one item may come in separate packages.
        dimensions (Union[Unset, Dimensions]): Physical dimensional measurements of a container.
        weight (Union[Unset, Weight]): The weight.
    """

    container_type: ContainerContainerType
    container_identifier: str
    packed_items: List["PackedItem"]
    tracking_number: Union[Unset, str] = UNSET
    manifest_id: Union[Unset, str] = UNSET
    manifest_date: Union[Unset, str] = UNSET
    ship_method: Union[Unset, str] = UNSET
    scac_code: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    container_sequence_number: Union[Unset, int] = UNSET
    dimensions: Union[Unset, "Dimensions"] = UNSET
    weight: Union[Unset, "Weight"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_type = self.container_type.value

        container_identifier = self.container_identifier
        packed_items = []
        for packed_items_item_data in self.packed_items:
            packed_items_item = packed_items_item_data.to_dict()

            packed_items.append(packed_items_item)

        tracking_number = self.tracking_number
        manifest_id = self.manifest_id
        manifest_date = self.manifest_date
        ship_method = self.ship_method
        scac_code = self.scac_code
        carrier = self.carrier
        container_sequence_number = self.container_sequence_number
        dimensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerType": container_type,
                "containerIdentifier": container_identifier,
                "packedItems": packed_items,
            }
        )
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if manifest_id is not UNSET:
            field_dict["manifestId"] = manifest_id
        if manifest_date is not UNSET:
            field_dict["manifestDate"] = manifest_date
        if ship_method is not UNSET:
            field_dict["shipMethod"] = ship_method
        if scac_code is not UNSET:
            field_dict["scacCode"] = scac_code
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if container_sequence_number is not UNSET:
            field_dict["containerSequenceNumber"] = container_sequence_number
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimensions import Dimensions
        from ..models.packed_item import PackedItem
        from ..models.weight import Weight

        d = src_dict.copy()
        container_type = ContainerContainerType(d.pop("containerType"))

        container_identifier = d.pop("containerIdentifier")

        packed_items = []
        _packed_items = d.pop("packedItems")
        for packed_items_item_data in _packed_items:
            packed_items_item = PackedItem.from_dict(packed_items_item_data)

            packed_items.append(packed_items_item)

        tracking_number = d.pop("trackingNumber", UNSET)

        manifest_id = d.pop("manifestId", UNSET)

        manifest_date = d.pop("manifestDate", UNSET)

        ship_method = d.pop("shipMethod", UNSET)

        scac_code = d.pop("scacCode", UNSET)

        carrier = d.pop("carrier", UNSET)

        container_sequence_number = d.pop("containerSequenceNumber", UNSET)

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

        result = cls(
            container_type=container_type,
            container_identifier=container_identifier,
            packed_items=packed_items,
            tracking_number=tracking_number,
            manifest_id=manifest_id,
            manifest_date=manifest_date,
            ship_method=ship_method,
            scac_code=scac_code,
            carrier=carrier,
            container_sequence_number=container_sequence_number,
            dimensions=dimensions,
            weight=weight,
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
