from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.schema_link_link import SchemaLinkLink


T = TypeVar("T", bound="SchemaLink")


@attr.s(auto_attribs=True)
class SchemaLink:
    r"""
    Attributes:
        link (SchemaLinkLink): Link to retrieve the schema.
        checksum (str): Checksum hash of the schema (Base64 MD5). Can be used to verify schema contents, identify
            changes between schema versions, and for caching.
    """

    link: "SchemaLinkLink"
    checksum: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link.to_dict()

        checksum = self.checksum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "checksum": checksum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_link_link import SchemaLinkLink

        d = src_dict.copy()
        link = SchemaLinkLink.from_dict(d.pop("link"))

        checksum = d.pop("checksum")

        result = cls(
            link=link,
            checksum=checksum,
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
