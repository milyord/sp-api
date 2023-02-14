from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.granularity import Granularity
    from ..models.inventory_summary import InventorySummary


T = TypeVar("T", bound="GetInventorySummariesResult")


@attr.s(auto_attribs=True)
class GetInventorySummariesResult:
    r"""The payload schema for the getInventorySummaries operation.

    Attributes:
        granularity (Granularity): Describes a granularity at which inventory data can be aggregated. For example, if
            you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the
            given marketplace.
        inventory_summaries (List['InventorySummary']): A list of inventory summaries.
    """

    granularity: "Granularity"
    inventory_summaries: List["InventorySummary"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        granularity = self.granularity.to_dict()

        inventory_summaries = []
        for componentsschemas_inventory_summaries_item_data in self.inventory_summaries:
            componentsschemas_inventory_summaries_item = componentsschemas_inventory_summaries_item_data.to_dict()

            inventory_summaries.append(componentsschemas_inventory_summaries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "granularity": granularity,
                "inventorySummaries": inventory_summaries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.granularity import Granularity
        from ..models.inventory_summary import InventorySummary

        d = src_dict.copy()
        granularity = Granularity.from_dict(d.pop("granularity"))

        inventory_summaries = []
        _inventory_summaries = d.pop("inventorySummaries")
        for componentsschemas_inventory_summaries_item_data in _inventory_summaries:
            componentsschemas_inventory_summaries_item = InventorySummary.from_dict(
                componentsschemas_inventory_summaries_item_data
            )

            inventory_summaries.append(componentsschemas_inventory_summaries_item)

        result = cls(
            granularity=granularity,
            inventory_summaries=inventory_summaries,
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
