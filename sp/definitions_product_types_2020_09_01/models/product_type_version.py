from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductTypeVersion")


@attr.s(auto_attribs=True)
class ProductTypeVersion:
    r"""The version details for an Amazon product type.

    Attributes:
        version (str): Version identifier.
        latest (bool): When true, the version indicated by the version identifier is the latest available for the Amazon
            product type.
        release_candidate (Union[Unset, bool]): When true, the version indicated by the version identifier is the
            prerelease (release candidate) for the Amazon product type.
    """

    version: str
    latest: bool
    release_candidate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        latest = self.latest
        release_candidate = self.release_candidate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "latest": latest,
            }
        )
        if release_candidate is not UNSET:
            field_dict["releaseCandidate"] = release_candidate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version")

        latest = d.pop("latest")

        release_candidate = d.pop("releaseCandidate", UNSET)

        result = cls(
            version=version,
            latest=latest,
            release_candidate=release_candidate,
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
