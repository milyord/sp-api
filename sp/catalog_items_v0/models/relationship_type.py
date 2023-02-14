from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decimal_with_units import DecimalWithUnits
    from ..models.dimension_type import DimensionType
    from ..models.identifier_type import IdentifierType


T = TypeVar("T", bound="RelationshipType")


@attr.s(auto_attribs=True)
class RelationshipType:
    r"""Specific variations of the item.

    Attributes:
        identifiers (Union[Unset, IdentifierType]):
        color (Union[Unset, str]): The color variation of the item.
        edition (Union[Unset, str]): The edition variation of the item.
        flavor (Union[Unset, str]): The flavor variation of the item.
        gem_type (Union[Unset, List[str]]): The gem type variations of the item.
        golf_club_flex (Union[Unset, str]): The golf club flex variation of an item.
        hand_orientation (Union[Unset, str]): The hand orientation variation of an item.
        hardware_platform (Union[Unset, str]): The hardware platform variation of an item.
        material_type (Union[Unset, List[str]]): The material type variations of an item.
        metal_type (Union[Unset, str]): The metal type variation of an item.
        model (Union[Unset, str]): The model variation of an item.
        operating_system (Union[Unset, List[str]]): The operating system variations of an item.
        product_type_subcategory (Union[Unset, str]): The product type subcategory variation of an item.
        ring_size (Union[Unset, str]): The ring size variation of an item.
        shaft_material (Union[Unset, str]): The shaft material variation of an item.
        scent (Union[Unset, str]): The scent variation of an item.
        size (Union[Unset, str]): The size variation of an item.
        size_per_pearl (Union[Unset, str]): The size per pearl variation of an item.
        golf_club_loft (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        total_diamond_weight (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        total_gem_weight (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        package_quantity (Union[Unset, int]): The package quantity variation of an item.
        item_dimensions (Union[Unset, DimensionType]): The dimension type attribute of an item.
    """

    identifiers: Union[Unset, "IdentifierType"] = UNSET
    color: Union[Unset, str] = UNSET
    edition: Union[Unset, str] = UNSET
    flavor: Union[Unset, str] = UNSET
    gem_type: Union[Unset, List[str]] = UNSET
    golf_club_flex: Union[Unset, str] = UNSET
    hand_orientation: Union[Unset, str] = UNSET
    hardware_platform: Union[Unset, str] = UNSET
    material_type: Union[Unset, List[str]] = UNSET
    metal_type: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    operating_system: Union[Unset, List[str]] = UNSET
    product_type_subcategory: Union[Unset, str] = UNSET
    ring_size: Union[Unset, str] = UNSET
    shaft_material: Union[Unset, str] = UNSET
    scent: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    size_per_pearl: Union[Unset, str] = UNSET
    golf_club_loft: Union[Unset, "DecimalWithUnits"] = UNSET
    total_diamond_weight: Union[Unset, "DecimalWithUnits"] = UNSET
    total_gem_weight: Union[Unset, "DecimalWithUnits"] = UNSET
    package_quantity: Union[Unset, int] = UNSET
    item_dimensions: Union[Unset, "DimensionType"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers.to_dict()

        color = self.color
        edition = self.edition
        flavor = self.flavor
        gem_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.gem_type, Unset):
            gem_type = self.gem_type

        golf_club_flex = self.golf_club_flex
        hand_orientation = self.hand_orientation
        hardware_platform = self.hardware_platform
        material_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.material_type, Unset):
            material_type = self.material_type

        metal_type = self.metal_type
        model = self.model
        operating_system: Union[Unset, List[str]] = UNSET
        if not isinstance(self.operating_system, Unset):
            operating_system = self.operating_system

        product_type_subcategory = self.product_type_subcategory
        ring_size = self.ring_size
        shaft_material = self.shaft_material
        scent = self.scent
        size = self.size
        size_per_pearl = self.size_per_pearl
        golf_club_loft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.golf_club_loft, Unset):
            golf_club_loft = self.golf_club_loft.to_dict()

        total_diamond_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_diamond_weight, Unset):
            total_diamond_weight = self.total_diamond_weight.to_dict()

        total_gem_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_gem_weight, Unset):
            total_gem_weight = self.total_gem_weight.to_dict()

        package_quantity = self.package_quantity
        item_dimensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_dimensions, Unset):
            item_dimensions = self.item_dimensions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifiers is not UNSET:
            field_dict["Identifiers"] = identifiers
        if color is not UNSET:
            field_dict["Color"] = color
        if edition is not UNSET:
            field_dict["Edition"] = edition
        if flavor is not UNSET:
            field_dict["Flavor"] = flavor
        if gem_type is not UNSET:
            field_dict["GemType"] = gem_type
        if golf_club_flex is not UNSET:
            field_dict["GolfClubFlex"] = golf_club_flex
        if hand_orientation is not UNSET:
            field_dict["HandOrientation"] = hand_orientation
        if hardware_platform is not UNSET:
            field_dict["HardwarePlatform"] = hardware_platform
        if material_type is not UNSET:
            field_dict["MaterialType"] = material_type
        if metal_type is not UNSET:
            field_dict["MetalType"] = metal_type
        if model is not UNSET:
            field_dict["Model"] = model
        if operating_system is not UNSET:
            field_dict["OperatingSystem"] = operating_system
        if product_type_subcategory is not UNSET:
            field_dict["ProductTypeSubcategory"] = product_type_subcategory
        if ring_size is not UNSET:
            field_dict["RingSize"] = ring_size
        if shaft_material is not UNSET:
            field_dict["ShaftMaterial"] = shaft_material
        if scent is not UNSET:
            field_dict["Scent"] = scent
        if size is not UNSET:
            field_dict["Size"] = size
        if size_per_pearl is not UNSET:
            field_dict["SizePerPearl"] = size_per_pearl
        if golf_club_loft is not UNSET:
            field_dict["GolfClubLoft"] = golf_club_loft
        if total_diamond_weight is not UNSET:
            field_dict["TotalDiamondWeight"] = total_diamond_weight
        if total_gem_weight is not UNSET:
            field_dict["TotalGemWeight"] = total_gem_weight
        if package_quantity is not UNSET:
            field_dict["PackageQuantity"] = package_quantity
        if item_dimensions is not UNSET:
            field_dict["ItemDimensions"] = item_dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.decimal_with_units import DecimalWithUnits
        from ..models.dimension_type import DimensionType
        from ..models.identifier_type import IdentifierType

        d = src_dict.copy()
        _identifiers = d.pop("Identifiers", UNSET)
        identifiers: Union[Unset, IdentifierType]
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = IdentifierType.from_dict(_identifiers)

        color = d.pop("Color", UNSET)

        edition = d.pop("Edition", UNSET)

        flavor = d.pop("Flavor", UNSET)

        gem_type = cast(List[str], d.pop("GemType", UNSET))

        golf_club_flex = d.pop("GolfClubFlex", UNSET)

        hand_orientation = d.pop("HandOrientation", UNSET)

        hardware_platform = d.pop("HardwarePlatform", UNSET)

        material_type = cast(List[str], d.pop("MaterialType", UNSET))

        metal_type = d.pop("MetalType", UNSET)

        model = d.pop("Model", UNSET)

        operating_system = cast(List[str], d.pop("OperatingSystem", UNSET))

        product_type_subcategory = d.pop("ProductTypeSubcategory", UNSET)

        ring_size = d.pop("RingSize", UNSET)

        shaft_material = d.pop("ShaftMaterial", UNSET)

        scent = d.pop("Scent", UNSET)

        size = d.pop("Size", UNSET)

        size_per_pearl = d.pop("SizePerPearl", UNSET)

        _golf_club_loft = d.pop("GolfClubLoft", UNSET)
        golf_club_loft: Union[Unset, DecimalWithUnits]
        if isinstance(_golf_club_loft, Unset):
            golf_club_loft = UNSET
        else:
            golf_club_loft = DecimalWithUnits.from_dict(_golf_club_loft)

        _total_diamond_weight = d.pop("TotalDiamondWeight", UNSET)
        total_diamond_weight: Union[Unset, DecimalWithUnits]
        if isinstance(_total_diamond_weight, Unset):
            total_diamond_weight = UNSET
        else:
            total_diamond_weight = DecimalWithUnits.from_dict(_total_diamond_weight)

        _total_gem_weight = d.pop("TotalGemWeight", UNSET)
        total_gem_weight: Union[Unset, DecimalWithUnits]
        if isinstance(_total_gem_weight, Unset):
            total_gem_weight = UNSET
        else:
            total_gem_weight = DecimalWithUnits.from_dict(_total_gem_weight)

        package_quantity = d.pop("PackageQuantity", UNSET)

        _item_dimensions = d.pop("ItemDimensions", UNSET)
        item_dimensions: Union[Unset, DimensionType]
        if isinstance(_item_dimensions, Unset):
            item_dimensions = UNSET
        else:
            item_dimensions = DimensionType.from_dict(_item_dimensions)

        result = cls(
            identifiers=identifiers,
            color=color,
            edition=edition,
            flavor=flavor,
            gem_type=gem_type,
            golf_club_flex=golf_club_flex,
            hand_orientation=hand_orientation,
            hardware_platform=hardware_platform,
            material_type=material_type,
            metal_type=metal_type,
            model=model,
            operating_system=operating_system,
            product_type_subcategory=product_type_subcategory,
            ring_size=ring_size,
            shaft_material=shaft_material,
            scent=scent,
            size=size,
            size_per_pearl=size_per_pearl,
            golf_club_loft=golf_club_loft,
            total_diamond_weight=total_diamond_weight,
            total_gem_weight=total_gem_weight,
            package_quantity=package_quantity,
            item_dimensions=item_dimensions,
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
