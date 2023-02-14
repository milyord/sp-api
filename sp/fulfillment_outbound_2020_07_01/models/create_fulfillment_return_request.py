from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.create_return_item import CreateReturnItem


T = TypeVar("T", bound="CreateFulfillmentReturnRequest")


@attr.s(auto_attribs=True)
class CreateFulfillmentReturnRequest:
    r"""The createFulfillmentReturn operation creates a fulfillment return for items that were fulfilled using the
    createFulfillmentOrder operation. For calls to createFulfillmentReturn, you must include ReturnReasonCode values
    returned by a previous call to the listReturnReasonCodes operation.

        Attributes:
            items (List['CreateReturnItem']): An array of items to be returned.
    """

    items: List["CreateReturnItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for componentsschemas_create_return_item_list_item_data in self.items:
            componentsschemas_create_return_item_list_item = (
                componentsschemas_create_return_item_list_item_data.to_dict()
            )

            items.append(componentsschemas_create_return_item_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_return_item import CreateReturnItem

        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for componentsschemas_create_return_item_list_item_data in _items:
            componentsschemas_create_return_item_list_item = CreateReturnItem.from_dict(
                componentsschemas_create_return_item_list_item_data
            )

            items.append(componentsschemas_create_return_item_list_item)

        result = cls(
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
