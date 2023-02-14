from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_sku import FeatureSku


T = TypeVar("T", bound="GetFeatureSkuResult")


@attr.s(auto_attribs=True)
class GetFeatureSkuResult:
    r"""The payload for the getFeatureSKU operation.

    Attributes:
        marketplace_id (str): The requested marketplace.
        feature_name (str): The name of the feature.
        is_eligible (bool): When true, the seller SKU is eligible for the requested feature.
        ineligible_reasons (Union[Unset, List[str]]): A list of one or more reasons that the seller SKU is ineligibile
            for the feature.

            Possible values:
            * MERCHANT_NOT_ENROLLED - The merchant isn't enrolled for the feature.
            * SKU_NOT_ELIGIBLE - The SKU doesn't reside in a warehouse that supports the feature.
            * INVALID_SKU - There is an issue with the SKU provided.
        sku_info (Union[Unset, FeatureSku]): Information about an SKU, including the count available, identifiers, and a
            list of overlapping SKUs that share the same inventory pool.
    """

    marketplace_id: str
    feature_name: str
    is_eligible: bool
    ineligible_reasons: Union[Unset, List[str]] = UNSET
    sku_info: Union[Unset, "FeatureSku"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        feature_name = self.feature_name
        is_eligible = self.is_eligible
        ineligible_reasons: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ineligible_reasons, Unset):
            ineligible_reasons = self.ineligible_reasons

        sku_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sku_info, Unset):
            sku_info = self.sku_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "featureName": feature_name,
                "isEligible": is_eligible,
            }
        )
        if ineligible_reasons is not UNSET:
            field_dict["ineligibleReasons"] = ineligible_reasons
        if sku_info is not UNSET:
            field_dict["skuInfo"] = sku_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature_sku import FeatureSku

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        feature_name = d.pop("featureName")

        is_eligible = d.pop("isEligible")

        ineligible_reasons = cast(List[str], d.pop("ineligibleReasons", UNSET))

        _sku_info = d.pop("skuInfo", UNSET)
        sku_info: Union[Unset, FeatureSku]
        if isinstance(_sku_info, Unset):
            sku_info = UNSET
        else:
            sku_info = FeatureSku.from_dict(_sku_info)

        result = cls(
            marketplace_id=marketplace_id,
            feature_name=feature_name,
            is_eligible=is_eligible,
            ineligible_reasons=ineligible_reasons,
            sku_info=sku_info,
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
