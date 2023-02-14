from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_component import ImageComponent
    from ..models.plain_text_item import PlainTextItem


T = TypeVar("T", bound="StandardComparisonProductBlock")


@attr.s(auto_attribs=True)
class StandardComparisonProductBlock:
    r"""The A+ Content standard comparison product block.

    Attributes:
        position (int): The rank or index of this comparison product block within the module. Different blocks cannot
            occupy the same position within a single module.
        image (Union[Unset, ImageComponent]): A reference to an image, hosted in the A+ Content media library.
        title (Union[Unset, str]): The comparison product title.
        asin (Union[Unset, str]): The Amazon Standard Identification Number (ASIN).
        highlight (Union[Unset, bool]): Determines whether this block of content is visually highlighted.
        metrics (Union[Unset, List['PlainTextItem']]): Comparison metrics for the product.
    """

    position: int
    image: Union[Unset, "ImageComponent"] = UNSET
    title: Union[Unset, str] = UNSET
    asin: Union[Unset, str] = UNSET
    highlight: Union[Unset, bool] = UNSET
    metrics: Union[Unset, List["PlainTextItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        title = self.title
        asin = self.asin
        highlight = self.highlight
        metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()

                metrics.append(metrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if title is not UNSET:
            field_dict["title"] = title
        if asin is not UNSET:
            field_dict["asin"] = asin
        if highlight is not UNSET:
            field_dict["highlight"] = highlight
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_component import ImageComponent
        from ..models.plain_text_item import PlainTextItem

        d = src_dict.copy()
        position = d.pop("position")

        _image = d.pop("image", UNSET)
        image: Union[Unset, ImageComponent]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ImageComponent.from_dict(_image)

        title = d.pop("title", UNSET)

        asin = d.pop("asin", UNSET)

        highlight = d.pop("highlight", UNSET)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = PlainTextItem.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        result = cls(
            position=position,
            image=image,
            title=title,
            asin=asin,
            highlight=highlight,
            metrics=metrics,
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
