from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.image_component import ImageComponent


T = TypeVar("T", bound="StandardCompanyLogoModule")


@attr.s(auto_attribs=True)
class StandardCompanyLogoModule:
    r"""The standard company logo image.

    Attributes:
        company_logo (ImageComponent): A reference to an image, hosted in the A+ Content media library.
    """

    company_logo: "ImageComponent"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company_logo = self.company_logo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyLogo": company_logo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_component import ImageComponent

        d = src_dict.copy()
        company_logo = ImageComponent.from_dict(d.pop("companyLogo"))

        result = cls(
            company_logo=company_logo,
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
