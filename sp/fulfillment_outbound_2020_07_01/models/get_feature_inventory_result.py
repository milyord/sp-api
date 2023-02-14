from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_sku import FeatureSku


T = TypeVar("T", bound="GetFeatureInventoryResult")


@attr.s(auto_attribs=True)
class GetFeatureInventoryResult:
    r"""The payload for the getEligibileInventory operation.

    Attributes:
        marketplace_id (str): The requested marketplace.
        feature_name (str): The name of the feature.
        next_token (Union[Unset, str]): When present and not empty, pass this string token in the next request to return
            the next response page.
        feature_skus (Union[Unset, List['FeatureSku']]): An array of SKUs eligible for this feature and the quantity
            available.
    """

    marketplace_id: str
    feature_name: str
    next_token: Union[Unset, str] = UNSET
    feature_skus: Union[Unset, List["FeatureSku"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        feature_name = self.feature_name
        next_token = self.next_token
        feature_skus: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.feature_skus, Unset):
            feature_skus = []
            for feature_skus_item_data in self.feature_skus:
                feature_skus_item = feature_skus_item_data.to_dict()

                feature_skus.append(feature_skus_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "featureName": feature_name,
            }
        )
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if feature_skus is not UNSET:
            field_dict["featureSkus"] = feature_skus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature_sku import FeatureSku

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        feature_name = d.pop("featureName")

        next_token = d.pop("nextToken", UNSET)

        feature_skus = []
        _feature_skus = d.pop("featureSkus", UNSET)
        for feature_skus_item_data in _feature_skus or []:
            feature_skus_item = FeatureSku.from_dict(feature_skus_item_data)

            feature_skus.append(feature_skus_item)

        result = cls(
            marketplace_id=marketplace_id,
            feature_name=feature_name,
            next_token=next_token,
            feature_skus=feature_skus,
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
