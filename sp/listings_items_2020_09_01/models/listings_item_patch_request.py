from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.patch_operation import PatchOperation


T = TypeVar("T", bound="ListingsItemPatchRequest")


@attr.s(auto_attribs=True)
class ListingsItemPatchRequest:
    r"""The request body schema for the patchListingsItem operation.

    Attributes:
        product_type (str): The Amazon product type of the listings item.
        patches (List['PatchOperation']): One or more JSON Patch operations to perform on the listings item.
    """

    product_type: str
    patches: List["PatchOperation"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_type = self.product_type
        patches = []
        for patches_item_data in self.patches:
            patches_item = patches_item_data.to_dict()

            patches.append(patches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productType": product_type,
                "patches": patches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_operation import PatchOperation

        d = src_dict.copy()
        product_type = d.pop("productType")

        patches = []
        _patches = d.pop("patches")
        for patches_item_data in _patches:
            patches_item = PatchOperation.from_dict(patches_item_data)

            patches.append(patches_item)

        result = cls(
            product_type=product_type,
            patches=patches,
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
