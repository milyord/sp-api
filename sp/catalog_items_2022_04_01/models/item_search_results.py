from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.item import Item
    from ..models.pagination import Pagination
    from ..models.refinements import Refinements


T = TypeVar("T", bound="ItemSearchResults")


@attr.s(auto_attribs=True)
class ItemSearchResults:
    r"""Items in the Amazon catalog and search related metadata.

    Attributes:
        number_of_results (int): For `identifiers`-based searches, the total number of Amazon catalog items found. For
            `keywords`-based searches, the estimated total number of Amazon catalog items matched by the search query (only
            results up to the page count limit will be returned per request regardless of the number found).

            Note: The maximum number of items (ASINs) that can be returned and paged through is 1000.
        pagination (Pagination): When a request produces a response that exceeds the `pageSize`, pagination occurs. This
            means the response is divided into individual pages. To retrieve the next page or the previous page, you must
            pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. When
            you receive the last page, there will be no `nextToken` key in the pagination object.
        refinements (Refinements): Search refinements.
        items (List['Item']): A list of items from the Amazon catalog.
    """

    number_of_results: int
    pagination: "Pagination"
    refinements: "Refinements"
    items: List["Item"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_results = self.number_of_results
        pagination = self.pagination.to_dict()

        refinements = self.refinements.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfResults": number_of_results,
                "pagination": pagination,
                "refinements": refinements,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item import Item
        from ..models.pagination import Pagination
        from ..models.refinements import Refinements

        d = src_dict.copy()
        number_of_results = d.pop("numberOfResults")

        pagination = Pagination.from_dict(d.pop("pagination"))

        refinements = Refinements.from_dict(d.pop("refinements"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        result = cls(
            number_of_results=number_of_results,
            pagination=pagination,
            refinements=refinements,
            items=items,
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
