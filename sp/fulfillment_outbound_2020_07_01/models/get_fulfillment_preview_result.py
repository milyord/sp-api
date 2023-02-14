from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fulfillment_preview import FulfillmentPreview


T = TypeVar("T", bound="GetFulfillmentPreviewResult")


@attr.s(auto_attribs=True)
class GetFulfillmentPreviewResult:
    r"""A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated
    ship dates and arrival dates.

        Attributes:
            fulfillment_previews (Union[Unset, List['FulfillmentPreview']]): An array of fulfillment preview information.
    """

    fulfillment_previews: Union[Unset, List["FulfillmentPreview"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fulfillment_previews: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fulfillment_previews, Unset):
            fulfillment_previews = []
            for componentsschemas_fulfillment_preview_list_item_data in self.fulfillment_previews:
                componentsschemas_fulfillment_preview_list_item = (
                    componentsschemas_fulfillment_preview_list_item_data.to_dict()
                )

                fulfillment_previews.append(componentsschemas_fulfillment_preview_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fulfillment_previews is not UNSET:
            field_dict["fulfillmentPreviews"] = fulfillment_previews

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfillment_preview import FulfillmentPreview

        d = src_dict.copy()
        fulfillment_previews = []
        _fulfillment_previews = d.pop("fulfillmentPreviews", UNSET)
        for componentsschemas_fulfillment_preview_list_item_data in _fulfillment_previews or []:
            componentsschemas_fulfillment_preview_list_item = FulfillmentPreview.from_dict(
                componentsschemas_fulfillment_preview_list_item_data
            )

            fulfillment_previews.append(componentsschemas_fulfillment_preview_list_item)

        result = cls(
            fulfillment_previews=fulfillment_previews,
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
