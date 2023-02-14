from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.feature import Feature


T = TypeVar("T", bound="GetFeaturesResult")


@attr.s(auto_attribs=True)
class GetFeaturesResult:
    r"""The payload for the getFeatures operation.

    Attributes:
        features (List['Feature']): An array of features.
    """

    features: List["Feature"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        features = []
        for componentsschemas_features_item_data in self.features:
            componentsschemas_features_item = componentsschemas_features_item_data.to_dict()

            features.append(componentsschemas_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature import Feature

        d = src_dict.copy()
        features = []
        _features = d.pop("features")
        for componentsschemas_features_item_data in _features:
            componentsschemas_features_item = Feature.from_dict(componentsschemas_features_item_data)

            features.append(componentsschemas_features_item)

        result = cls(
            features=features,
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
