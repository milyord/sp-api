from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Feature")


@attr.s(auto_attribs=True)
class Feature:
    r"""A Multi-Channel Fulfillment feature.

    Attributes:
        feature_name (str): The feature name.
        feature_description (str): The feature description.
        seller_eligible (Union[Unset, bool]): When true, indicates that the seller is eligible to use the feature.
    """

    feature_name: str
    feature_description: str
    seller_eligible: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feature_name = self.feature_name
        feature_description = self.feature_description
        seller_eligible = self.seller_eligible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "featureName": feature_name,
                "featureDescription": feature_description,
            }
        )
        if seller_eligible is not UNSET:
            field_dict["sellerEligible"] = seller_eligible

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feature_name = d.pop("featureName")

        feature_description = d.pop("featureDescription")

        seller_eligible = d.pop("sellerEligible", UNSET)

        result = cls(
            feature_name=feature_name,
            feature_description=feature_description,
            seller_eligible=seller_eligible,
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
