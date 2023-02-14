from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Granularity")


@attr.s(auto_attribs=True)
class Granularity:
    r"""Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity,
    the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace.

        Attributes:
            granularity_type (Union[Unset, str]): The granularity type for the inventory aggregation level.
            granularity_id (Union[Unset, str]): The granularity ID for the specified granularity type. When granularityType
                is Marketplace, specify the marketplaceId.
    """

    granularity_type: Union[Unset, str] = UNSET
    granularity_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        granularity_type = self.granularity_type
        granularity_id = self.granularity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if granularity_type is not UNSET:
            field_dict["granularityType"] = granularity_type
        if granularity_id is not UNSET:
            field_dict["granularityId"] = granularity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        granularity_type = d.pop("granularityType", UNSET)

        granularity_id = d.pop("granularityId", UNSET)

        result = cls(
            granularity_type=granularity_type,
            granularity_id=granularity_id,
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
