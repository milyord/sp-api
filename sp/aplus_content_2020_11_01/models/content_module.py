from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.content_module_type import ContentModuleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_company_logo_module import StandardCompanyLogoModule
    from ..models.standard_comparison_table_module import StandardComparisonTableModule
    from ..models.standard_four_image_text_module import StandardFourImageTextModule
    from ..models.standard_four_image_text_quadrant_module import StandardFourImageTextQuadrantModule
    from ..models.standard_header_image_text_module import StandardHeaderImageTextModule
    from ..models.standard_image_sidebar_module import StandardImageSidebarModule
    from ..models.standard_image_text_overlay_module import StandardImageTextOverlayModule
    from ..models.standard_multiple_image_text_module import StandardMultipleImageTextModule
    from ..models.standard_product_description_module import StandardProductDescriptionModule
    from ..models.standard_single_image_highlights_module import StandardSingleImageHighlightsModule
    from ..models.standard_single_image_specs_detail_module import StandardSingleImageSpecsDetailModule
    from ..models.standard_single_side_image_module import StandardSingleSideImageModule
    from ..models.standard_tech_specs_module import StandardTechSpecsModule
    from ..models.standard_text_module import StandardTextModule
    from ..models.standard_three_image_text_module import StandardThreeImageTextModule


T = TypeVar("T", bound="ContentModule")


@attr.s(auto_attribs=True)
class ContentModule:
    r"""An A+ Content module. An A+ Content document is composed of content modules. The contentModuleType property selects
    which content module types to use.

        Attributes:
            content_module_type (ContentModuleType): The type of A+ Content module.
            standard_company_logo (Union[Unset, StandardCompanyLogoModule]): The standard company logo image.
            standard_comparison_table (Union[Unset, StandardComparisonTableModule]): The standard product comparison table.
            standard_four_image_text (Union[Unset, StandardFourImageTextModule]): Four standard images with text, presented
                across a single row.
            standard_four_image_text_quadrant (Union[Unset, StandardFourImageTextQuadrantModule]): Four standard images with
                text, presented on a grid of four quadrants.
            standard_header_image_text (Union[Unset, StandardHeaderImageTextModule]): Standard headline text, an image, and
                body text.
            standard_image_sidebar (Union[Unset, StandardImageSidebarModule]): Two images, two paragraphs, and two bulleted
                lists. One image is smaller and displayed in the sidebar.
            standard_image_text_overlay (Union[Unset, StandardImageTextOverlayModule]): A standard background image with a
                floating text box.
            standard_multiple_image_text (Union[Unset, StandardMultipleImageTextModule]): Standard images with text,
                presented one at a time. The user clicks on thumbnails to view each block.
            standard_product_description (Union[Unset, StandardProductDescriptionModule]): Standard product description
                text.
            standard_single_image_highlights (Union[Unset, StandardSingleImageHighlightsModule]): A standard image with
                several paragraphs and a bulleted list.
            standard_single_image_specs_detail (Union[Unset, StandardSingleImageSpecsDetailModule]): A standard image with
                paragraphs and a bulleted list, and extra space for technical details.
            standard_single_side_image (Union[Unset, StandardSingleSideImageModule]): A standard headline and body text with
                an image on the side.
            standard_tech_specs (Union[Unset, StandardTechSpecsModule]): The standard table of technical feature names and
                definitions.
            standard_text (Union[Unset, StandardTextModule]): A standard headline and body text.
            standard_three_image_text (Union[Unset, StandardThreeImageTextModule]): Three standard images with text,
                presented across a single row.
    """

    content_module_type: ContentModuleType
    standard_company_logo: Union[Unset, "StandardCompanyLogoModule"] = UNSET
    standard_comparison_table: Union[Unset, "StandardComparisonTableModule"] = UNSET
    standard_four_image_text: Union[Unset, "StandardFourImageTextModule"] = UNSET
    standard_four_image_text_quadrant: Union[Unset, "StandardFourImageTextQuadrantModule"] = UNSET
    standard_header_image_text: Union[Unset, "StandardHeaderImageTextModule"] = UNSET
    standard_image_sidebar: Union[Unset, "StandardImageSidebarModule"] = UNSET
    standard_image_text_overlay: Union[Unset, "StandardImageTextOverlayModule"] = UNSET
    standard_multiple_image_text: Union[Unset, "StandardMultipleImageTextModule"] = UNSET
    standard_product_description: Union[Unset, "StandardProductDescriptionModule"] = UNSET
    standard_single_image_highlights: Union[Unset, "StandardSingleImageHighlightsModule"] = UNSET
    standard_single_image_specs_detail: Union[Unset, "StandardSingleImageSpecsDetailModule"] = UNSET
    standard_single_side_image: Union[Unset, "StandardSingleSideImageModule"] = UNSET
    standard_tech_specs: Union[Unset, "StandardTechSpecsModule"] = UNSET
    standard_text: Union[Unset, "StandardTextModule"] = UNSET
    standard_three_image_text: Union[Unset, "StandardThreeImageTextModule"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_module_type = self.content_module_type.value

        standard_company_logo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_company_logo, Unset):
            standard_company_logo = self.standard_company_logo.to_dict()

        standard_comparison_table: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_comparison_table, Unset):
            standard_comparison_table = self.standard_comparison_table.to_dict()

        standard_four_image_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_four_image_text, Unset):
            standard_four_image_text = self.standard_four_image_text.to_dict()

        standard_four_image_text_quadrant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_four_image_text_quadrant, Unset):
            standard_four_image_text_quadrant = self.standard_four_image_text_quadrant.to_dict()

        standard_header_image_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_header_image_text, Unset):
            standard_header_image_text = self.standard_header_image_text.to_dict()

        standard_image_sidebar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_image_sidebar, Unset):
            standard_image_sidebar = self.standard_image_sidebar.to_dict()

        standard_image_text_overlay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_image_text_overlay, Unset):
            standard_image_text_overlay = self.standard_image_text_overlay.to_dict()

        standard_multiple_image_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_multiple_image_text, Unset):
            standard_multiple_image_text = self.standard_multiple_image_text.to_dict()

        standard_product_description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_product_description, Unset):
            standard_product_description = self.standard_product_description.to_dict()

        standard_single_image_highlights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_single_image_highlights, Unset):
            standard_single_image_highlights = self.standard_single_image_highlights.to_dict()

        standard_single_image_specs_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_single_image_specs_detail, Unset):
            standard_single_image_specs_detail = self.standard_single_image_specs_detail.to_dict()

        standard_single_side_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_single_side_image, Unset):
            standard_single_side_image = self.standard_single_side_image.to_dict()

        standard_tech_specs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_tech_specs, Unset):
            standard_tech_specs = self.standard_tech_specs.to_dict()

        standard_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_text, Unset):
            standard_text = self.standard_text.to_dict()

        standard_three_image_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.standard_three_image_text, Unset):
            standard_three_image_text = self.standard_three_image_text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentModuleType": content_module_type,
            }
        )
        if standard_company_logo is not UNSET:
            field_dict["standardCompanyLogo"] = standard_company_logo
        if standard_comparison_table is not UNSET:
            field_dict["standardComparisonTable"] = standard_comparison_table
        if standard_four_image_text is not UNSET:
            field_dict["standardFourImageText"] = standard_four_image_text
        if standard_four_image_text_quadrant is not UNSET:
            field_dict["standardFourImageTextQuadrant"] = standard_four_image_text_quadrant
        if standard_header_image_text is not UNSET:
            field_dict["standardHeaderImageText"] = standard_header_image_text
        if standard_image_sidebar is not UNSET:
            field_dict["standardImageSidebar"] = standard_image_sidebar
        if standard_image_text_overlay is not UNSET:
            field_dict["standardImageTextOverlay"] = standard_image_text_overlay
        if standard_multiple_image_text is not UNSET:
            field_dict["standardMultipleImageText"] = standard_multiple_image_text
        if standard_product_description is not UNSET:
            field_dict["standardProductDescription"] = standard_product_description
        if standard_single_image_highlights is not UNSET:
            field_dict["standardSingleImageHighlights"] = standard_single_image_highlights
        if standard_single_image_specs_detail is not UNSET:
            field_dict["standardSingleImageSpecsDetail"] = standard_single_image_specs_detail
        if standard_single_side_image is not UNSET:
            field_dict["standardSingleSideImage"] = standard_single_side_image
        if standard_tech_specs is not UNSET:
            field_dict["standardTechSpecs"] = standard_tech_specs
        if standard_text is not UNSET:
            field_dict["standardText"] = standard_text
        if standard_three_image_text is not UNSET:
            field_dict["standardThreeImageText"] = standard_three_image_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standard_company_logo_module import StandardCompanyLogoModule
        from ..models.standard_comparison_table_module import StandardComparisonTableModule
        from ..models.standard_four_image_text_module import StandardFourImageTextModule
        from ..models.standard_four_image_text_quadrant_module import StandardFourImageTextQuadrantModule
        from ..models.standard_header_image_text_module import StandardHeaderImageTextModule
        from ..models.standard_image_sidebar_module import StandardImageSidebarModule
        from ..models.standard_image_text_overlay_module import StandardImageTextOverlayModule
        from ..models.standard_multiple_image_text_module import StandardMultipleImageTextModule
        from ..models.standard_product_description_module import StandardProductDescriptionModule
        from ..models.standard_single_image_highlights_module import StandardSingleImageHighlightsModule
        from ..models.standard_single_image_specs_detail_module import StandardSingleImageSpecsDetailModule
        from ..models.standard_single_side_image_module import StandardSingleSideImageModule
        from ..models.standard_tech_specs_module import StandardTechSpecsModule
        from ..models.standard_text_module import StandardTextModule
        from ..models.standard_three_image_text_module import StandardThreeImageTextModule

        d = src_dict.copy()
        content_module_type = ContentModuleType(d.pop("contentModuleType"))

        _standard_company_logo = d.pop("standardCompanyLogo", UNSET)
        standard_company_logo: Union[Unset, StandardCompanyLogoModule]
        if isinstance(_standard_company_logo, Unset):
            standard_company_logo = UNSET
        else:
            standard_company_logo = StandardCompanyLogoModule.from_dict(_standard_company_logo)

        _standard_comparison_table = d.pop("standardComparisonTable", UNSET)
        standard_comparison_table: Union[Unset, StandardComparisonTableModule]
        if isinstance(_standard_comparison_table, Unset):
            standard_comparison_table = UNSET
        else:
            standard_comparison_table = StandardComparisonTableModule.from_dict(_standard_comparison_table)

        _standard_four_image_text = d.pop("standardFourImageText", UNSET)
        standard_four_image_text: Union[Unset, StandardFourImageTextModule]
        if isinstance(_standard_four_image_text, Unset):
            standard_four_image_text = UNSET
        else:
            standard_four_image_text = StandardFourImageTextModule.from_dict(_standard_four_image_text)

        _standard_four_image_text_quadrant = d.pop("standardFourImageTextQuadrant", UNSET)
        standard_four_image_text_quadrant: Union[Unset, StandardFourImageTextQuadrantModule]
        if isinstance(_standard_four_image_text_quadrant, Unset):
            standard_four_image_text_quadrant = UNSET
        else:
            standard_four_image_text_quadrant = StandardFourImageTextQuadrantModule.from_dict(
                _standard_four_image_text_quadrant
            )

        _standard_header_image_text = d.pop("standardHeaderImageText", UNSET)
        standard_header_image_text: Union[Unset, StandardHeaderImageTextModule]
        if isinstance(_standard_header_image_text, Unset):
            standard_header_image_text = UNSET
        else:
            standard_header_image_text = StandardHeaderImageTextModule.from_dict(_standard_header_image_text)

        _standard_image_sidebar = d.pop("standardImageSidebar", UNSET)
        standard_image_sidebar: Union[Unset, StandardImageSidebarModule]
        if isinstance(_standard_image_sidebar, Unset):
            standard_image_sidebar = UNSET
        else:
            standard_image_sidebar = StandardImageSidebarModule.from_dict(_standard_image_sidebar)

        _standard_image_text_overlay = d.pop("standardImageTextOverlay", UNSET)
        standard_image_text_overlay: Union[Unset, StandardImageTextOverlayModule]
        if isinstance(_standard_image_text_overlay, Unset):
            standard_image_text_overlay = UNSET
        else:
            standard_image_text_overlay = StandardImageTextOverlayModule.from_dict(_standard_image_text_overlay)

        _standard_multiple_image_text = d.pop("standardMultipleImageText", UNSET)
        standard_multiple_image_text: Union[Unset, StandardMultipleImageTextModule]
        if isinstance(_standard_multiple_image_text, Unset):
            standard_multiple_image_text = UNSET
        else:
            standard_multiple_image_text = StandardMultipleImageTextModule.from_dict(_standard_multiple_image_text)

        _standard_product_description = d.pop("standardProductDescription", UNSET)
        standard_product_description: Union[Unset, StandardProductDescriptionModule]
        if isinstance(_standard_product_description, Unset):
            standard_product_description = UNSET
        else:
            standard_product_description = StandardProductDescriptionModule.from_dict(_standard_product_description)

        _standard_single_image_highlights = d.pop("standardSingleImageHighlights", UNSET)
        standard_single_image_highlights: Union[Unset, StandardSingleImageHighlightsModule]
        if isinstance(_standard_single_image_highlights, Unset):
            standard_single_image_highlights = UNSET
        else:
            standard_single_image_highlights = StandardSingleImageHighlightsModule.from_dict(
                _standard_single_image_highlights
            )

        _standard_single_image_specs_detail = d.pop("standardSingleImageSpecsDetail", UNSET)
        standard_single_image_specs_detail: Union[Unset, StandardSingleImageSpecsDetailModule]
        if isinstance(_standard_single_image_specs_detail, Unset):
            standard_single_image_specs_detail = UNSET
        else:
            standard_single_image_specs_detail = StandardSingleImageSpecsDetailModule.from_dict(
                _standard_single_image_specs_detail
            )

        _standard_single_side_image = d.pop("standardSingleSideImage", UNSET)
        standard_single_side_image: Union[Unset, StandardSingleSideImageModule]
        if isinstance(_standard_single_side_image, Unset):
            standard_single_side_image = UNSET
        else:
            standard_single_side_image = StandardSingleSideImageModule.from_dict(_standard_single_side_image)

        _standard_tech_specs = d.pop("standardTechSpecs", UNSET)
        standard_tech_specs: Union[Unset, StandardTechSpecsModule]
        if isinstance(_standard_tech_specs, Unset):
            standard_tech_specs = UNSET
        else:
            standard_tech_specs = StandardTechSpecsModule.from_dict(_standard_tech_specs)

        _standard_text = d.pop("standardText", UNSET)
        standard_text: Union[Unset, StandardTextModule]
        if isinstance(_standard_text, Unset):
            standard_text = UNSET
        else:
            standard_text = StandardTextModule.from_dict(_standard_text)

        _standard_three_image_text = d.pop("standardThreeImageText", UNSET)
        standard_three_image_text: Union[Unset, StandardThreeImageTextModule]
        if isinstance(_standard_three_image_text, Unset):
            standard_three_image_text = UNSET
        else:
            standard_three_image_text = StandardThreeImageTextModule.from_dict(_standard_three_image_text)

        result = cls(
            content_module_type=content_module_type,
            standard_company_logo=standard_company_logo,
            standard_comparison_table=standard_comparison_table,
            standard_four_image_text=standard_four_image_text,
            standard_four_image_text_quadrant=standard_four_image_text_quadrant,
            standard_header_image_text=standard_header_image_text,
            standard_image_sidebar=standard_image_sidebar,
            standard_image_text_overlay=standard_image_text_overlay,
            standard_multiple_image_text=standard_multiple_image_text,
            standard_product_description=standard_product_description,
            standard_single_image_highlights=standard_single_image_highlights,
            standard_single_image_specs_detail=standard_single_image_specs_detail,
            standard_single_side_image=standard_single_side_image,
            standard_tech_specs=standard_tech_specs,
            standard_text=standard_text,
            standard_three_image_text=standard_three_image_text,
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
