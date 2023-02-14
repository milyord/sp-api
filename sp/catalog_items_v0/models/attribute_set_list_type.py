from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_type import CreatorType
    from ..models.decimal_with_units import DecimalWithUnits
    from ..models.dimension_type import DimensionType
    from ..models.image import Image
    from ..models.language_type import LanguageType
    from ..models.price import Price


T = TypeVar("T", bound="AttributeSetListType")


@attr.s(auto_attribs=True)
class AttributeSetListType:
    r"""The attributes of the item.

    Attributes:
        actor (Union[Unset, List[str]]): The actor attributes of the item.
        artist (Union[Unset, List[str]]): The artist attributes of the item.
        aspect_ratio (Union[Unset, str]): The aspect ratio attribute of the item.
        audience_rating (Union[Unset, str]): The audience rating attribute of the item.
        author (Union[Unset, List[str]]): The author attributes of the item.
        back_finding (Union[Unset, str]): The back finding attribute of the item.
        band_material_type (Union[Unset, str]): The band material type attribute of the item.
        binding (Union[Unset, str]): The binding attribute of the item.
        bluray_region (Union[Unset, str]): The Bluray region attribute of the item.
        brand (Union[Unset, str]): The brand attribute of the item.
        cero_age_rating (Union[Unset, str]): The CERO age rating attribute of the item.
        chain_type (Union[Unset, str]): The chain type attribute of the item.
        clasp_type (Union[Unset, str]): The clasp type attribute of the item.
        color (Union[Unset, str]): The color attribute of the item.
        cpu_manufacturer (Union[Unset, str]): The CPU manufacturer attribute of the item.
        cpu_speed (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        cpu_type (Union[Unset, str]): The CPU type attribute of the item.
        creator (Union[Unset, List['CreatorType']]): The creator attributes of the item.
        department (Union[Unset, str]): The department attribute of the item.
        director (Union[Unset, List[str]]): The director attributes of the item.
        display_size (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        edition (Union[Unset, str]): The edition attribute of the item.
        episode_sequence (Union[Unset, str]): The episode sequence attribute of the item.
        esrb_age_rating (Union[Unset, str]): The ESRB age rating attribute of the item.
        feature (Union[Unset, List[str]]): The feature attributes of the item
        flavor (Union[Unset, str]): The flavor attribute of the item.
        format_ (Union[Unset, List[str]]): The format attributes of the item.
        gem_type (Union[Unset, List[str]]): The gem type attributes of the item.
        genre (Union[Unset, str]): The genre attribute of the item.
        golf_club_flex (Union[Unset, str]): The golf club flex attribute of the item.
        golf_club_loft (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        hand_orientation (Union[Unset, str]): The hand orientation attribute of the item.
        hard_disk_interface (Union[Unset, str]): The hard disk interface attribute of the item.
        hard_disk_size (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        hardware_platform (Union[Unset, str]): The hardware platform attribute of the item.
        hazardous_material_type (Union[Unset, str]): The hazardous material type attribute of the item.
        item_dimensions (Union[Unset, DimensionType]): The dimension type attribute of an item.
        is_adult_product (Union[Unset, bool]): The adult product attribute of the item.
        is_autographed (Union[Unset, bool]): The autographed attribute of the item.
        is_eligible_for_trade_in (Union[Unset, bool]): The is eligible for trade in attribute of the item.
        is_memorabilia (Union[Unset, bool]): The is memorabilia attribute of the item.
        issues_per_year (Union[Unset, str]): The issues per year attribute of the item.
        item_part_number (Union[Unset, str]): The item part number attribute of the item.
        label (Union[Unset, str]): The label attribute of the item.
        languages (Union[Unset, List['LanguageType']]): The languages attribute of the item.
        legal_disclaimer (Union[Unset, str]): The legal disclaimer attribute of the item.
        list_price (Union[Unset, Price]): The price attribute of the item.
        manufacturer (Union[Unset, str]): The manufacturer attribute of the item.
        manufacturer_maximum_age (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        manufacturer_minimum_age (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        manufacturer_parts_warranty_description (Union[Unset, str]): The manufacturer parts warranty description
            attribute of the item.
        material_type (Union[Unset, List[str]]): The material type attributes of the item.
        maximum_resolution (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        media_type (Union[Unset, List[str]]): The media type attributes of the item.
        metal_stamp (Union[Unset, str]): The metal stamp attribute of the item.
        metal_type (Union[Unset, str]): The metal type attribute of the item.
        model (Union[Unset, str]): The model attribute of the item.
        number_of_discs (Union[Unset, int]): The number of discs attribute of the item.
        number_of_issues (Union[Unset, int]): The number of issues attribute of the item.
        number_of_items (Union[Unset, int]): The number of items attribute of the item.
        number_of_pages (Union[Unset, int]): The number of pages attribute of the item.
        number_of_tracks (Union[Unset, int]): The number of tracks attribute of the item.
        operating_system (Union[Unset, List[str]]): The operating system attributes of the item.
        optical_zoom (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        package_dimensions (Union[Unset, DimensionType]): The dimension type attribute of an item.
        package_quantity (Union[Unset, int]): The package quantity attribute of the item.
        part_number (Union[Unset, str]): The part number attribute of the item.
        pegi_rating (Union[Unset, str]): The PEGI rating attribute of the item.
        platform (Union[Unset, List[str]]): The platform attributes of the item.
        processor_count (Union[Unset, int]): The processor count attribute of the item.
        product_group (Union[Unset, str]): The product group attribute of the item.
        product_type_name (Union[Unset, str]): The product type name attribute of the item.
        product_type_subcategory (Union[Unset, str]): The product type subcategory attribute of the item.
        publication_date (Union[Unset, str]): The publication date attribute of the item.
        publisher (Union[Unset, str]): The publisher attribute of the item.
        region_code (Union[Unset, str]): The region code attribute of the item.
        release_date (Union[Unset, str]): The release date attribute of the item.
        ring_size (Union[Unset, str]): The ring size attribute of the item.
        running_time (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        shaft_material (Union[Unset, str]): The shaft material attribute of the item.
        scent (Union[Unset, str]): The scent attribute of the item.
        season_sequence (Union[Unset, str]): The season sequence attribute of the item.
        seikodo_product_code (Union[Unset, str]): The Seikodo product code attribute of the item.
        size (Union[Unset, str]): The size attribute of the item.
        size_per_pearl (Union[Unset, str]): The size per pearl attribute of the item.
        small_image (Union[Unset, Image]): The image attribute of the item.
        studio (Union[Unset, str]): The studio attribute of the item.
        subscription_length (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        system_memory_size (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        system_memory_type (Union[Unset, str]): The system memory type attribute of the item.
        theatrical_release_date (Union[Unset, str]): The theatrical release date attribute of the item.
        title (Union[Unset, str]): The title attribute of the item.
        total_diamond_weight (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        total_gem_weight (Union[Unset, DecimalWithUnits]): The decimal value and unit.
        warranty (Union[Unset, str]): The warranty attribute of the item.
        weee_tax_value (Union[Unset, Price]): The price attribute of the item.
    """

    actor: Union[Unset, List[str]] = UNSET
    artist: Union[Unset, List[str]] = UNSET
    aspect_ratio: Union[Unset, str] = UNSET
    audience_rating: Union[Unset, str] = UNSET
    author: Union[Unset, List[str]] = UNSET
    back_finding: Union[Unset, str] = UNSET
    band_material_type: Union[Unset, str] = UNSET
    binding: Union[Unset, str] = UNSET
    bluray_region: Union[Unset, str] = UNSET
    brand: Union[Unset, str] = UNSET
    cero_age_rating: Union[Unset, str] = UNSET
    chain_type: Union[Unset, str] = UNSET
    clasp_type: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    cpu_manufacturer: Union[Unset, str] = UNSET
    cpu_speed: Union[Unset, "DecimalWithUnits"] = UNSET
    cpu_type: Union[Unset, str] = UNSET
    creator: Union[Unset, List["CreatorType"]] = UNSET
    department: Union[Unset, str] = UNSET
    director: Union[Unset, List[str]] = UNSET
    display_size: Union[Unset, "DecimalWithUnits"] = UNSET
    edition: Union[Unset, str] = UNSET
    episode_sequence: Union[Unset, str] = UNSET
    esrb_age_rating: Union[Unset, str] = UNSET
    feature: Union[Unset, List[str]] = UNSET
    flavor: Union[Unset, str] = UNSET
    format_: Union[Unset, List[str]] = UNSET
    gem_type: Union[Unset, List[str]] = UNSET
    genre: Union[Unset, str] = UNSET
    golf_club_flex: Union[Unset, str] = UNSET
    golf_club_loft: Union[Unset, "DecimalWithUnits"] = UNSET
    hand_orientation: Union[Unset, str] = UNSET
    hard_disk_interface: Union[Unset, str] = UNSET
    hard_disk_size: Union[Unset, "DecimalWithUnits"] = UNSET
    hardware_platform: Union[Unset, str] = UNSET
    hazardous_material_type: Union[Unset, str] = UNSET
    item_dimensions: Union[Unset, "DimensionType"] = UNSET
    is_adult_product: Union[Unset, bool] = UNSET
    is_autographed: Union[Unset, bool] = UNSET
    is_eligible_for_trade_in: Union[Unset, bool] = UNSET
    is_memorabilia: Union[Unset, bool] = UNSET
    issues_per_year: Union[Unset, str] = UNSET
    item_part_number: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    languages: Union[Unset, List["LanguageType"]] = UNSET
    legal_disclaimer: Union[Unset, str] = UNSET
    list_price: Union[Unset, "Price"] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    manufacturer_maximum_age: Union[Unset, "DecimalWithUnits"] = UNSET
    manufacturer_minimum_age: Union[Unset, "DecimalWithUnits"] = UNSET
    manufacturer_parts_warranty_description: Union[Unset, str] = UNSET
    material_type: Union[Unset, List[str]] = UNSET
    maximum_resolution: Union[Unset, "DecimalWithUnits"] = UNSET
    media_type: Union[Unset, List[str]] = UNSET
    metal_stamp: Union[Unset, str] = UNSET
    metal_type: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    number_of_discs: Union[Unset, int] = UNSET
    number_of_issues: Union[Unset, int] = UNSET
    number_of_items: Union[Unset, int] = UNSET
    number_of_pages: Union[Unset, int] = UNSET
    number_of_tracks: Union[Unset, int] = UNSET
    operating_system: Union[Unset, List[str]] = UNSET
    optical_zoom: Union[Unset, "DecimalWithUnits"] = UNSET
    package_dimensions: Union[Unset, "DimensionType"] = UNSET
    package_quantity: Union[Unset, int] = UNSET
    part_number: Union[Unset, str] = UNSET
    pegi_rating: Union[Unset, str] = UNSET
    platform: Union[Unset, List[str]] = UNSET
    processor_count: Union[Unset, int] = UNSET
    product_group: Union[Unset, str] = UNSET
    product_type_name: Union[Unset, str] = UNSET
    product_type_subcategory: Union[Unset, str] = UNSET
    publication_date: Union[Unset, str] = UNSET
    publisher: Union[Unset, str] = UNSET
    region_code: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    ring_size: Union[Unset, str] = UNSET
    running_time: Union[Unset, "DecimalWithUnits"] = UNSET
    shaft_material: Union[Unset, str] = UNSET
    scent: Union[Unset, str] = UNSET
    season_sequence: Union[Unset, str] = UNSET
    seikodo_product_code: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    size_per_pearl: Union[Unset, str] = UNSET
    small_image: Union[Unset, "Image"] = UNSET
    studio: Union[Unset, str] = UNSET
    subscription_length: Union[Unset, "DecimalWithUnits"] = UNSET
    system_memory_size: Union[Unset, "DecimalWithUnits"] = UNSET
    system_memory_type: Union[Unset, str] = UNSET
    theatrical_release_date: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    total_diamond_weight: Union[Unset, "DecimalWithUnits"] = UNSET
    total_gem_weight: Union[Unset, "DecimalWithUnits"] = UNSET
    warranty: Union[Unset, str] = UNSET
    weee_tax_value: Union[Unset, "Price"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actor: Union[Unset, List[str]] = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor

        artist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist

        aspect_ratio = self.aspect_ratio
        audience_rating = self.audience_rating
        author: Union[Unset, List[str]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author

        back_finding = self.back_finding
        band_material_type = self.band_material_type
        binding = self.binding
        bluray_region = self.bluray_region
        brand = self.brand
        cero_age_rating = self.cero_age_rating
        chain_type = self.chain_type
        clasp_type = self.clasp_type
        color = self.color
        cpu_manufacturer = self.cpu_manufacturer
        cpu_speed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cpu_speed, Unset):
            cpu_speed = self.cpu_speed.to_dict()

        cpu_type = self.cpu_type
        creator: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = []
            for creator_item_data in self.creator:
                creator_item = creator_item_data.to_dict()

                creator.append(creator_item)

        department = self.department
        director: Union[Unset, List[str]] = UNSET
        if not isinstance(self.director, Unset):
            director = self.director

        display_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.display_size, Unset):
            display_size = self.display_size.to_dict()

        edition = self.edition
        episode_sequence = self.episode_sequence
        esrb_age_rating = self.esrb_age_rating
        feature: Union[Unset, List[str]] = UNSET
        if not isinstance(self.feature, Unset):
            feature = self.feature

        flavor = self.flavor
        format_: Union[Unset, List[str]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        gem_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.gem_type, Unset):
            gem_type = self.gem_type

        genre = self.genre
        golf_club_flex = self.golf_club_flex
        golf_club_loft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.golf_club_loft, Unset):
            golf_club_loft = self.golf_club_loft.to_dict()

        hand_orientation = self.hand_orientation
        hard_disk_interface = self.hard_disk_interface
        hard_disk_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hard_disk_size, Unset):
            hard_disk_size = self.hard_disk_size.to_dict()

        hardware_platform = self.hardware_platform
        hazardous_material_type = self.hazardous_material_type
        item_dimensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_dimensions, Unset):
            item_dimensions = self.item_dimensions.to_dict()

        is_adult_product = self.is_adult_product
        is_autographed = self.is_autographed
        is_eligible_for_trade_in = self.is_eligible_for_trade_in
        is_memorabilia = self.is_memorabilia
        issues_per_year = self.issues_per_year
        item_part_number = self.item_part_number
        label = self.label
        languages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()

                languages.append(languages_item)

        legal_disclaimer = self.legal_disclaimer
        list_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.list_price, Unset):
            list_price = self.list_price.to_dict()

        manufacturer = self.manufacturer
        manufacturer_maximum_age: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manufacturer_maximum_age, Unset):
            manufacturer_maximum_age = self.manufacturer_maximum_age.to_dict()

        manufacturer_minimum_age: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manufacturer_minimum_age, Unset):
            manufacturer_minimum_age = self.manufacturer_minimum_age.to_dict()

        manufacturer_parts_warranty_description = self.manufacturer_parts_warranty_description
        material_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.material_type, Unset):
            material_type = self.material_type

        maximum_resolution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maximum_resolution, Unset):
            maximum_resolution = self.maximum_resolution.to_dict()

        media_type: Union[Unset, List[str]] = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type

        metal_stamp = self.metal_stamp
        metal_type = self.metal_type
        model = self.model
        number_of_discs = self.number_of_discs
        number_of_issues = self.number_of_issues
        number_of_items = self.number_of_items
        number_of_pages = self.number_of_pages
        number_of_tracks = self.number_of_tracks
        operating_system: Union[Unset, List[str]] = UNSET
        if not isinstance(self.operating_system, Unset):
            operating_system = self.operating_system

        optical_zoom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.optical_zoom, Unset):
            optical_zoom = self.optical_zoom.to_dict()

        package_dimensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict()

        package_quantity = self.package_quantity
        part_number = self.part_number
        pegi_rating = self.pegi_rating
        platform: Union[Unset, List[str]] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform

        processor_count = self.processor_count
        product_group = self.product_group
        product_type_name = self.product_type_name
        product_type_subcategory = self.product_type_subcategory
        publication_date = self.publication_date
        publisher = self.publisher
        region_code = self.region_code
        release_date = self.release_date
        ring_size = self.ring_size
        running_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.running_time, Unset):
            running_time = self.running_time.to_dict()

        shaft_material = self.shaft_material
        scent = self.scent
        season_sequence = self.season_sequence
        seikodo_product_code = self.seikodo_product_code
        size = self.size
        size_per_pearl = self.size_per_pearl
        small_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.small_image, Unset):
            small_image = self.small_image.to_dict()

        studio = self.studio
        subscription_length: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscription_length, Unset):
            subscription_length = self.subscription_length.to_dict()

        system_memory_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system_memory_size, Unset):
            system_memory_size = self.system_memory_size.to_dict()

        system_memory_type = self.system_memory_type
        theatrical_release_date = self.theatrical_release_date
        title = self.title
        total_diamond_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_diamond_weight, Unset):
            total_diamond_weight = self.total_diamond_weight.to_dict()

        total_gem_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_gem_weight, Unset):
            total_gem_weight = self.total_gem_weight.to_dict()

        warranty = self.warranty
        weee_tax_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weee_tax_value, Unset):
            weee_tax_value = self.weee_tax_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actor is not UNSET:
            field_dict["Actor"] = actor
        if artist is not UNSET:
            field_dict["Artist"] = artist
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if audience_rating is not UNSET:
            field_dict["AudienceRating"] = audience_rating
        if author is not UNSET:
            field_dict["Author"] = author
        if back_finding is not UNSET:
            field_dict["BackFinding"] = back_finding
        if band_material_type is not UNSET:
            field_dict["BandMaterialType"] = band_material_type
        if binding is not UNSET:
            field_dict["Binding"] = binding
        if bluray_region is not UNSET:
            field_dict["BlurayRegion"] = bluray_region
        if brand is not UNSET:
            field_dict["Brand"] = brand
        if cero_age_rating is not UNSET:
            field_dict["CeroAgeRating"] = cero_age_rating
        if chain_type is not UNSET:
            field_dict["ChainType"] = chain_type
        if clasp_type is not UNSET:
            field_dict["ClaspType"] = clasp_type
        if color is not UNSET:
            field_dict["Color"] = color
        if cpu_manufacturer is not UNSET:
            field_dict["CpuManufacturer"] = cpu_manufacturer
        if cpu_speed is not UNSET:
            field_dict["CpuSpeed"] = cpu_speed
        if cpu_type is not UNSET:
            field_dict["CpuType"] = cpu_type
        if creator is not UNSET:
            field_dict["Creator"] = creator
        if department is not UNSET:
            field_dict["Department"] = department
        if director is not UNSET:
            field_dict["Director"] = director
        if display_size is not UNSET:
            field_dict["DisplaySize"] = display_size
        if edition is not UNSET:
            field_dict["Edition"] = edition
        if episode_sequence is not UNSET:
            field_dict["EpisodeSequence"] = episode_sequence
        if esrb_age_rating is not UNSET:
            field_dict["EsrbAgeRating"] = esrb_age_rating
        if feature is not UNSET:
            field_dict["Feature"] = feature
        if flavor is not UNSET:
            field_dict["Flavor"] = flavor
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if gem_type is not UNSET:
            field_dict["GemType"] = gem_type
        if genre is not UNSET:
            field_dict["Genre"] = genre
        if golf_club_flex is not UNSET:
            field_dict["GolfClubFlex"] = golf_club_flex
        if golf_club_loft is not UNSET:
            field_dict["GolfClubLoft"] = golf_club_loft
        if hand_orientation is not UNSET:
            field_dict["HandOrientation"] = hand_orientation
        if hard_disk_interface is not UNSET:
            field_dict["HardDiskInterface"] = hard_disk_interface
        if hard_disk_size is not UNSET:
            field_dict["HardDiskSize"] = hard_disk_size
        if hardware_platform is not UNSET:
            field_dict["HardwarePlatform"] = hardware_platform
        if hazardous_material_type is not UNSET:
            field_dict["HazardousMaterialType"] = hazardous_material_type
        if item_dimensions is not UNSET:
            field_dict["ItemDimensions"] = item_dimensions
        if is_adult_product is not UNSET:
            field_dict["IsAdultProduct"] = is_adult_product
        if is_autographed is not UNSET:
            field_dict["IsAutographed"] = is_autographed
        if is_eligible_for_trade_in is not UNSET:
            field_dict["IsEligibleForTradeIn"] = is_eligible_for_trade_in
        if is_memorabilia is not UNSET:
            field_dict["IsMemorabilia"] = is_memorabilia
        if issues_per_year is not UNSET:
            field_dict["IssuesPerYear"] = issues_per_year
        if item_part_number is not UNSET:
            field_dict["ItemPartNumber"] = item_part_number
        if label is not UNSET:
            field_dict["Label"] = label
        if languages is not UNSET:
            field_dict["Languages"] = languages
        if legal_disclaimer is not UNSET:
            field_dict["LegalDisclaimer"] = legal_disclaimer
        if list_price is not UNSET:
            field_dict["ListPrice"] = list_price
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_maximum_age is not UNSET:
            field_dict["ManufacturerMaximumAge"] = manufacturer_maximum_age
        if manufacturer_minimum_age is not UNSET:
            field_dict["ManufacturerMinimumAge"] = manufacturer_minimum_age
        if manufacturer_parts_warranty_description is not UNSET:
            field_dict["ManufacturerPartsWarrantyDescription"] = manufacturer_parts_warranty_description
        if material_type is not UNSET:
            field_dict["MaterialType"] = material_type
        if maximum_resolution is not UNSET:
            field_dict["MaximumResolution"] = maximum_resolution
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if metal_stamp is not UNSET:
            field_dict["MetalStamp"] = metal_stamp
        if metal_type is not UNSET:
            field_dict["MetalType"] = metal_type
        if model is not UNSET:
            field_dict["Model"] = model
        if number_of_discs is not UNSET:
            field_dict["NumberOfDiscs"] = number_of_discs
        if number_of_issues is not UNSET:
            field_dict["NumberOfIssues"] = number_of_issues
        if number_of_items is not UNSET:
            field_dict["NumberOfItems"] = number_of_items
        if number_of_pages is not UNSET:
            field_dict["NumberOfPages"] = number_of_pages
        if number_of_tracks is not UNSET:
            field_dict["NumberOfTracks"] = number_of_tracks
        if operating_system is not UNSET:
            field_dict["OperatingSystem"] = operating_system
        if optical_zoom is not UNSET:
            field_dict["OpticalZoom"] = optical_zoom
        if package_dimensions is not UNSET:
            field_dict["PackageDimensions"] = package_dimensions
        if package_quantity is not UNSET:
            field_dict["PackageQuantity"] = package_quantity
        if part_number is not UNSET:
            field_dict["PartNumber"] = part_number
        if pegi_rating is not UNSET:
            field_dict["PegiRating"] = pegi_rating
        if platform is not UNSET:
            field_dict["Platform"] = platform
        if processor_count is not UNSET:
            field_dict["ProcessorCount"] = processor_count
        if product_group is not UNSET:
            field_dict["ProductGroup"] = product_group
        if product_type_name is not UNSET:
            field_dict["ProductTypeName"] = product_type_name
        if product_type_subcategory is not UNSET:
            field_dict["ProductTypeSubcategory"] = product_type_subcategory
        if publication_date is not UNSET:
            field_dict["PublicationDate"] = publication_date
        if publisher is not UNSET:
            field_dict["Publisher"] = publisher
        if region_code is not UNSET:
            field_dict["RegionCode"] = region_code
        if release_date is not UNSET:
            field_dict["ReleaseDate"] = release_date
        if ring_size is not UNSET:
            field_dict["RingSize"] = ring_size
        if running_time is not UNSET:
            field_dict["RunningTime"] = running_time
        if shaft_material is not UNSET:
            field_dict["ShaftMaterial"] = shaft_material
        if scent is not UNSET:
            field_dict["Scent"] = scent
        if season_sequence is not UNSET:
            field_dict["SeasonSequence"] = season_sequence
        if seikodo_product_code is not UNSET:
            field_dict["SeikodoProductCode"] = seikodo_product_code
        if size is not UNSET:
            field_dict["Size"] = size
        if size_per_pearl is not UNSET:
            field_dict["SizePerPearl"] = size_per_pearl
        if small_image is not UNSET:
            field_dict["SmallImage"] = small_image
        if studio is not UNSET:
            field_dict["Studio"] = studio
        if subscription_length is not UNSET:
            field_dict["SubscriptionLength"] = subscription_length
        if system_memory_size is not UNSET:
            field_dict["SystemMemorySize"] = system_memory_size
        if system_memory_type is not UNSET:
            field_dict["SystemMemoryType"] = system_memory_type
        if theatrical_release_date is not UNSET:
            field_dict["TheatricalReleaseDate"] = theatrical_release_date
        if title is not UNSET:
            field_dict["Title"] = title
        if total_diamond_weight is not UNSET:
            field_dict["TotalDiamondWeight"] = total_diamond_weight
        if total_gem_weight is not UNSET:
            field_dict["TotalGemWeight"] = total_gem_weight
        if warranty is not UNSET:
            field_dict["Warranty"] = warranty
        if weee_tax_value is not UNSET:
            field_dict["WeeeTaxValue"] = weee_tax_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.creator_type import CreatorType
        from ..models.decimal_with_units import DecimalWithUnits
        from ..models.dimension_type import DimensionType
        from ..models.image import Image
        from ..models.language_type import LanguageType
        from ..models.price import Price

        d = src_dict.copy()
        actor = cast(List[str], d.pop("Actor", UNSET))

        artist = cast(List[str], d.pop("Artist", UNSET))

        aspect_ratio = d.pop("AspectRatio", UNSET)

        audience_rating = d.pop("AudienceRating", UNSET)

        author = cast(List[str], d.pop("Author", UNSET))

        back_finding = d.pop("BackFinding", UNSET)

        band_material_type = d.pop("BandMaterialType", UNSET)

        binding = d.pop("Binding", UNSET)

        bluray_region = d.pop("BlurayRegion", UNSET)

        brand = d.pop("Brand", UNSET)

        cero_age_rating = d.pop("CeroAgeRating", UNSET)

        chain_type = d.pop("ChainType", UNSET)

        clasp_type = d.pop("ClaspType", UNSET)

        color = d.pop("Color", UNSET)

        cpu_manufacturer = d.pop("CpuManufacturer", UNSET)

        _cpu_speed = d.pop("CpuSpeed", UNSET)
        cpu_speed: Union[Unset, DecimalWithUnits]
        if isinstance(_cpu_speed, Unset):
            cpu_speed = UNSET
        else:
            cpu_speed = DecimalWithUnits.from_dict(_cpu_speed)

        cpu_type = d.pop("CpuType", UNSET)

        creator = []
        _creator = d.pop("Creator", UNSET)
        for creator_item_data in _creator or []:
            creator_item = CreatorType.from_dict(creator_item_data)

            creator.append(creator_item)

        department = d.pop("Department", UNSET)

        director = cast(List[str], d.pop("Director", UNSET))

        _display_size = d.pop("DisplaySize", UNSET)
        display_size: Union[Unset, DecimalWithUnits]
        if isinstance(_display_size, Unset):
            display_size = UNSET
        else:
            display_size = DecimalWithUnits.from_dict(_display_size)

        edition = d.pop("Edition", UNSET)

        episode_sequence = d.pop("EpisodeSequence", UNSET)

        esrb_age_rating = d.pop("EsrbAgeRating", UNSET)

        feature = cast(List[str], d.pop("Feature", UNSET))

        flavor = d.pop("Flavor", UNSET)

        format_ = cast(List[str], d.pop("Format", UNSET))

        gem_type = cast(List[str], d.pop("GemType", UNSET))

        genre = d.pop("Genre", UNSET)

        golf_club_flex = d.pop("GolfClubFlex", UNSET)

        _golf_club_loft = d.pop("GolfClubLoft", UNSET)
        golf_club_loft: Union[Unset, DecimalWithUnits]
        if isinstance(_golf_club_loft, Unset):
            golf_club_loft = UNSET
        else:
            golf_club_loft = DecimalWithUnits.from_dict(_golf_club_loft)

        hand_orientation = d.pop("HandOrientation", UNSET)

        hard_disk_interface = d.pop("HardDiskInterface", UNSET)

        _hard_disk_size = d.pop("HardDiskSize", UNSET)
        hard_disk_size: Union[Unset, DecimalWithUnits]
        if isinstance(_hard_disk_size, Unset):
            hard_disk_size = UNSET
        else:
            hard_disk_size = DecimalWithUnits.from_dict(_hard_disk_size)

        hardware_platform = d.pop("HardwarePlatform", UNSET)

        hazardous_material_type = d.pop("HazardousMaterialType", UNSET)

        _item_dimensions = d.pop("ItemDimensions", UNSET)
        item_dimensions: Union[Unset, DimensionType]
        if isinstance(_item_dimensions, Unset):
            item_dimensions = UNSET
        else:
            item_dimensions = DimensionType.from_dict(_item_dimensions)

        is_adult_product = d.pop("IsAdultProduct", UNSET)

        is_autographed = d.pop("IsAutographed", UNSET)

        is_eligible_for_trade_in = d.pop("IsEligibleForTradeIn", UNSET)

        is_memorabilia = d.pop("IsMemorabilia", UNSET)

        issues_per_year = d.pop("IssuesPerYear", UNSET)

        item_part_number = d.pop("ItemPartNumber", UNSET)

        label = d.pop("Label", UNSET)

        languages = []
        _languages = d.pop("Languages", UNSET)
        for languages_item_data in _languages or []:
            languages_item = LanguageType.from_dict(languages_item_data)

            languages.append(languages_item)

        legal_disclaimer = d.pop("LegalDisclaimer", UNSET)

        _list_price = d.pop("ListPrice", UNSET)
        list_price: Union[Unset, Price]
        if isinstance(_list_price, Unset):
            list_price = UNSET
        else:
            list_price = Price.from_dict(_list_price)

        manufacturer = d.pop("Manufacturer", UNSET)

        _manufacturer_maximum_age = d.pop("ManufacturerMaximumAge", UNSET)
        manufacturer_maximum_age: Union[Unset, DecimalWithUnits]
        if isinstance(_manufacturer_maximum_age, Unset):
            manufacturer_maximum_age = UNSET
        else:
            manufacturer_maximum_age = DecimalWithUnits.from_dict(_manufacturer_maximum_age)

        _manufacturer_minimum_age = d.pop("ManufacturerMinimumAge", UNSET)
        manufacturer_minimum_age: Union[Unset, DecimalWithUnits]
        if isinstance(_manufacturer_minimum_age, Unset):
            manufacturer_minimum_age = UNSET
        else:
            manufacturer_minimum_age = DecimalWithUnits.from_dict(_manufacturer_minimum_age)

        manufacturer_parts_warranty_description = d.pop("ManufacturerPartsWarrantyDescription", UNSET)

        material_type = cast(List[str], d.pop("MaterialType", UNSET))

        _maximum_resolution = d.pop("MaximumResolution", UNSET)
        maximum_resolution: Union[Unset, DecimalWithUnits]
        if isinstance(_maximum_resolution, Unset):
            maximum_resolution = UNSET
        else:
            maximum_resolution = DecimalWithUnits.from_dict(_maximum_resolution)

        media_type = cast(List[str], d.pop("MediaType", UNSET))

        metal_stamp = d.pop("MetalStamp", UNSET)

        metal_type = d.pop("MetalType", UNSET)

        model = d.pop("Model", UNSET)

        number_of_discs = d.pop("NumberOfDiscs", UNSET)

        number_of_issues = d.pop("NumberOfIssues", UNSET)

        number_of_items = d.pop("NumberOfItems", UNSET)

        number_of_pages = d.pop("NumberOfPages", UNSET)

        number_of_tracks = d.pop("NumberOfTracks", UNSET)

        operating_system = cast(List[str], d.pop("OperatingSystem", UNSET))

        _optical_zoom = d.pop("OpticalZoom", UNSET)
        optical_zoom: Union[Unset, DecimalWithUnits]
        if isinstance(_optical_zoom, Unset):
            optical_zoom = UNSET
        else:
            optical_zoom = DecimalWithUnits.from_dict(_optical_zoom)

        _package_dimensions = d.pop("PackageDimensions", UNSET)
        package_dimensions: Union[Unset, DimensionType]
        if isinstance(_package_dimensions, Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = DimensionType.from_dict(_package_dimensions)

        package_quantity = d.pop("PackageQuantity", UNSET)

        part_number = d.pop("PartNumber", UNSET)

        pegi_rating = d.pop("PegiRating", UNSET)

        platform = cast(List[str], d.pop("Platform", UNSET))

        processor_count = d.pop("ProcessorCount", UNSET)

        product_group = d.pop("ProductGroup", UNSET)

        product_type_name = d.pop("ProductTypeName", UNSET)

        product_type_subcategory = d.pop("ProductTypeSubcategory", UNSET)

        publication_date = d.pop("PublicationDate", UNSET)

        publisher = d.pop("Publisher", UNSET)

        region_code = d.pop("RegionCode", UNSET)

        release_date = d.pop("ReleaseDate", UNSET)

        ring_size = d.pop("RingSize", UNSET)

        _running_time = d.pop("RunningTime", UNSET)
        running_time: Union[Unset, DecimalWithUnits]
        if isinstance(_running_time, Unset):
            running_time = UNSET
        else:
            running_time = DecimalWithUnits.from_dict(_running_time)

        shaft_material = d.pop("ShaftMaterial", UNSET)

        scent = d.pop("Scent", UNSET)

        season_sequence = d.pop("SeasonSequence", UNSET)

        seikodo_product_code = d.pop("SeikodoProductCode", UNSET)

        size = d.pop("Size", UNSET)

        size_per_pearl = d.pop("SizePerPearl", UNSET)

        _small_image = d.pop("SmallImage", UNSET)
        small_image: Union[Unset, Image]
        if isinstance(_small_image, Unset):
            small_image = UNSET
        else:
            small_image = Image.from_dict(_small_image)

        studio = d.pop("Studio", UNSET)

        _subscription_length = d.pop("SubscriptionLength", UNSET)
        subscription_length: Union[Unset, DecimalWithUnits]
        if isinstance(_subscription_length, Unset):
            subscription_length = UNSET
        else:
            subscription_length = DecimalWithUnits.from_dict(_subscription_length)

        _system_memory_size = d.pop("SystemMemorySize", UNSET)
        system_memory_size: Union[Unset, DecimalWithUnits]
        if isinstance(_system_memory_size, Unset):
            system_memory_size = UNSET
        else:
            system_memory_size = DecimalWithUnits.from_dict(_system_memory_size)

        system_memory_type = d.pop("SystemMemoryType", UNSET)

        theatrical_release_date = d.pop("TheatricalReleaseDate", UNSET)

        title = d.pop("Title", UNSET)

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

        warranty = d.pop("Warranty", UNSET)

        _weee_tax_value = d.pop("WeeeTaxValue", UNSET)
        weee_tax_value: Union[Unset, Price]
        if isinstance(_weee_tax_value, Unset):
            weee_tax_value = UNSET
        else:
            weee_tax_value = Price.from_dict(_weee_tax_value)

        result = cls(
            actor=actor,
            artist=artist,
            aspect_ratio=aspect_ratio,
            audience_rating=audience_rating,
            author=author,
            back_finding=back_finding,
            band_material_type=band_material_type,
            binding=binding,
            bluray_region=bluray_region,
            brand=brand,
            cero_age_rating=cero_age_rating,
            chain_type=chain_type,
            clasp_type=clasp_type,
            color=color,
            cpu_manufacturer=cpu_manufacturer,
            cpu_speed=cpu_speed,
            cpu_type=cpu_type,
            creator=creator,
            department=department,
            director=director,
            display_size=display_size,
            edition=edition,
            episode_sequence=episode_sequence,
            esrb_age_rating=esrb_age_rating,
            feature=feature,
            flavor=flavor,
            format_=format_,
            gem_type=gem_type,
            genre=genre,
            golf_club_flex=golf_club_flex,
            golf_club_loft=golf_club_loft,
            hand_orientation=hand_orientation,
            hard_disk_interface=hard_disk_interface,
            hard_disk_size=hard_disk_size,
            hardware_platform=hardware_platform,
            hazardous_material_type=hazardous_material_type,
            item_dimensions=item_dimensions,
            is_adult_product=is_adult_product,
            is_autographed=is_autographed,
            is_eligible_for_trade_in=is_eligible_for_trade_in,
            is_memorabilia=is_memorabilia,
            issues_per_year=issues_per_year,
            item_part_number=item_part_number,
            label=label,
            languages=languages,
            legal_disclaimer=legal_disclaimer,
            list_price=list_price,
            manufacturer=manufacturer,
            manufacturer_maximum_age=manufacturer_maximum_age,
            manufacturer_minimum_age=manufacturer_minimum_age,
            manufacturer_parts_warranty_description=manufacturer_parts_warranty_description,
            material_type=material_type,
            maximum_resolution=maximum_resolution,
            media_type=media_type,
            metal_stamp=metal_stamp,
            metal_type=metal_type,
            model=model,
            number_of_discs=number_of_discs,
            number_of_issues=number_of_issues,
            number_of_items=number_of_items,
            number_of_pages=number_of_pages,
            number_of_tracks=number_of_tracks,
            operating_system=operating_system,
            optical_zoom=optical_zoom,
            package_dimensions=package_dimensions,
            package_quantity=package_quantity,
            part_number=part_number,
            pegi_rating=pegi_rating,
            platform=platform,
            processor_count=processor_count,
            product_group=product_group,
            product_type_name=product_type_name,
            product_type_subcategory=product_type_subcategory,
            publication_date=publication_date,
            publisher=publisher,
            region_code=region_code,
            release_date=release_date,
            ring_size=ring_size,
            running_time=running_time,
            shaft_material=shaft_material,
            scent=scent,
            season_sequence=season_sequence,
            seikodo_product_code=seikodo_product_code,
            size=size,
            size_per_pearl=size_per_pearl,
            small_image=small_image,
            studio=studio,
            subscription_length=subscription_length,
            system_memory_size=system_memory_size,
            system_memory_type=system_memory_type,
            theatrical_release_date=theatrical_release_date,
            title=title,
            total_diamond_weight=total_diamond_weight,
            total_gem_weight=total_gem_weight,
            warranty=warranty,
            weee_tax_value=weee_tax_value,
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
