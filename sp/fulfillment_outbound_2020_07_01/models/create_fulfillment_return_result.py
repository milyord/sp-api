from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invalid_return_item import InvalidReturnItem
    from ..models.return_authorization import ReturnAuthorization
    from ..models.return_item import ReturnItem


T = TypeVar("T", bound="CreateFulfillmentReturnResult")


@attr.s(auto_attribs=True)
class CreateFulfillmentReturnResult:
    r"""
    Attributes:
        return_items (Union[Unset, List['ReturnItem']]): An array of items that Amazon accepted for return. Returns
            empty if no items were accepted for return.
        invalid_return_items (Union[Unset, List['InvalidReturnItem']]): An array of invalid return item information.
        return_authorizations (Union[Unset, List['ReturnAuthorization']]): An array of return authorization information.
    """

    return_items: Union[Unset, List["ReturnItem"]] = UNSET
    invalid_return_items: Union[Unset, List["InvalidReturnItem"]] = UNSET
    return_authorizations: Union[Unset, List["ReturnAuthorization"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_items, Unset):
            return_items = []
            for componentsschemas_return_item_list_item_data in self.return_items:
                componentsschemas_return_item_list_item = componentsschemas_return_item_list_item_data.to_dict()

                return_items.append(componentsschemas_return_item_list_item)

        invalid_return_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_return_items, Unset):
            invalid_return_items = []
            for componentsschemas_invalid_return_item_list_item_data in self.invalid_return_items:
                componentsschemas_invalid_return_item_list_item = (
                    componentsschemas_invalid_return_item_list_item_data.to_dict()
                )

                invalid_return_items.append(componentsschemas_invalid_return_item_list_item)

        return_authorizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.return_authorizations, Unset):
            return_authorizations = []
            for componentsschemas_return_authorization_list_item_data in self.return_authorizations:
                componentsschemas_return_authorization_list_item = (
                    componentsschemas_return_authorization_list_item_data.to_dict()
                )

                return_authorizations.append(componentsschemas_return_authorization_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_items is not UNSET:
            field_dict["returnItems"] = return_items
        if invalid_return_items is not UNSET:
            field_dict["invalidReturnItems"] = invalid_return_items
        if return_authorizations is not UNSET:
            field_dict["returnAuthorizations"] = return_authorizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invalid_return_item import InvalidReturnItem
        from ..models.return_authorization import ReturnAuthorization
        from ..models.return_item import ReturnItem

        d = src_dict.copy()
        return_items = []
        _return_items = d.pop("returnItems", UNSET)
        for componentsschemas_return_item_list_item_data in _return_items or []:
            componentsschemas_return_item_list_item = ReturnItem.from_dict(componentsschemas_return_item_list_item_data)

            return_items.append(componentsschemas_return_item_list_item)

        invalid_return_items = []
        _invalid_return_items = d.pop("invalidReturnItems", UNSET)
        for componentsschemas_invalid_return_item_list_item_data in _invalid_return_items or []:
            componentsschemas_invalid_return_item_list_item = InvalidReturnItem.from_dict(
                componentsschemas_invalid_return_item_list_item_data
            )

            invalid_return_items.append(componentsschemas_invalid_return_item_list_item)

        return_authorizations = []
        _return_authorizations = d.pop("returnAuthorizations", UNSET)
        for componentsschemas_return_authorization_list_item_data in _return_authorizations or []:
            componentsschemas_return_authorization_list_item = ReturnAuthorization.from_dict(
                componentsschemas_return_authorization_list_item_data
            )

            return_authorizations.append(componentsschemas_return_authorization_list_item)

        result = cls(
            return_items=return_items,
            invalid_return_items=invalid_return_items,
            return_authorizations=return_authorizations,
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
