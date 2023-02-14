from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.shipping_label import ShippingLabel


T = TypeVar("T", bound="ShippingLabelList")


@attr.s(auto_attribs=True)
class ShippingLabelList:
    r"""
    Attributes:
        pagination (Union[Unset, Pagination]):
        shipping_labels (Union[Unset, List['ShippingLabel']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    shipping_labels: Union[Unset, List["ShippingLabel"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        shipping_labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_labels, Unset):
            shipping_labels = []
            for shipping_labels_item_data in self.shipping_labels:
                shipping_labels_item = shipping_labels_item_data.to_dict()

                shipping_labels.append(shipping_labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if shipping_labels is not UNSET:
            field_dict["shippingLabels"] = shipping_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.shipping_label import ShippingLabel

        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        shipping_labels = []
        _shipping_labels = d.pop("shippingLabels", UNSET)
        for shipping_labels_item_data in _shipping_labels or []:
            shipping_labels_item = ShippingLabel.from_dict(shipping_labels_item_data)

            shipping_labels.append(shipping_labels_item)

        result = cls(
            pagination=pagination,
            shipping_labels=shipping_labels,
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
