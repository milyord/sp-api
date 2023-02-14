from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plain_text_item import PlainTextItem
    from ..models.standard_comparison_product_block import StandardComparisonProductBlock


T = TypeVar("T", bound="StandardComparisonTableModule")


@attr.s(auto_attribs=True)
class StandardComparisonTableModule:
    r"""The standard product comparison table.

    Attributes:
        product_columns (Union[Unset, List['StandardComparisonProductBlock']]):
        metric_row_labels (Union[Unset, List['PlainTextItem']]):
    """

    product_columns: Union[Unset, List["StandardComparisonProductBlock"]] = UNSET
    metric_row_labels: Union[Unset, List["PlainTextItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_columns, Unset):
            product_columns = []
            for product_columns_item_data in self.product_columns:
                product_columns_item = product_columns_item_data.to_dict()

                product_columns.append(product_columns_item)

        metric_row_labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metric_row_labels, Unset):
            metric_row_labels = []
            for metric_row_labels_item_data in self.metric_row_labels:
                metric_row_labels_item = metric_row_labels_item_data.to_dict()

                metric_row_labels.append(metric_row_labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_columns is not UNSET:
            field_dict["productColumns"] = product_columns
        if metric_row_labels is not UNSET:
            field_dict["metricRowLabels"] = metric_row_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plain_text_item import PlainTextItem
        from ..models.standard_comparison_product_block import StandardComparisonProductBlock

        d = src_dict.copy()
        product_columns = []
        _product_columns = d.pop("productColumns", UNSET)
        for product_columns_item_data in _product_columns or []:
            product_columns_item = StandardComparisonProductBlock.from_dict(product_columns_item_data)

            product_columns.append(product_columns_item)

        metric_row_labels = []
        _metric_row_labels = d.pop("metricRowLabels", UNSET)
        for metric_row_labels_item_data in _metric_row_labels or []:
            metric_row_labels_item = PlainTextItem.from_dict(metric_row_labels_item_data)

            metric_row_labels.append(metric_row_labels_item)

        result = cls(
            product_columns=product_columns,
            metric_row_labels=metric_row_labels,
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
