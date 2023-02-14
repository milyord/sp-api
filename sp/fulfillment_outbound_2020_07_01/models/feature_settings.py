from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.feature_settings_feature_fulfillment_policy import FeatureSettingsFeatureFulfillmentPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureSettings")


@attr.s(auto_attribs=True)
class FeatureSettings:
    r"""FeatureSettings allows users to apply fulfillment features to an order. To block an order from being shipped using
    Amazon Logistics (AMZL) and an AMZL tracking number, use featureName as BLOCK_AMZL and featureFulfillmentPolicy as
    Required. Blocking AMZL will incur an additional fee surcharge on your MCF orders and increase the risk of some of
    your orders being unfulfilled or delivered late if there are no alternative carriers available. Using BLOCK_AMZL in
    an order request will take precedence over your Seller Central account setting.

        Attributes:
            feature_name (Union[Unset, str]): The name of the feature.
            feature_fulfillment_policy (Union[Unset, FeatureSettingsFeatureFulfillmentPolicy]): Specifies the policy to use
                when fulfilling an order.
    """

    feature_name: Union[Unset, str] = UNSET
    feature_fulfillment_policy: Union[Unset, FeatureSettingsFeatureFulfillmentPolicy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feature_name = self.feature_name
        feature_fulfillment_policy: Union[Unset, str] = UNSET
        if not isinstance(self.feature_fulfillment_policy, Unset):
            feature_fulfillment_policy = self.feature_fulfillment_policy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_name is not UNSET:
            field_dict["featureName"] = feature_name
        if feature_fulfillment_policy is not UNSET:
            field_dict["featureFulfillmentPolicy"] = feature_fulfillment_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feature_name = d.pop("featureName", UNSET)

        _feature_fulfillment_policy = d.pop("featureFulfillmentPolicy", UNSET)
        feature_fulfillment_policy: Union[Unset, FeatureSettingsFeatureFulfillmentPolicy]
        if isinstance(_feature_fulfillment_policy, Unset):
            feature_fulfillment_policy = UNSET
        else:
            feature_fulfillment_policy = FeatureSettingsFeatureFulfillmentPolicy(_feature_fulfillment_policy)

        result = cls(
            feature_name=feature_name,
            feature_fulfillment_policy=feature_fulfillment_policy,
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
