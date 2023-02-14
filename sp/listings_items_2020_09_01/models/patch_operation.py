from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.patch_operation_op import PatchOperationOp
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_operation_value_item import PatchOperationValueItem


T = TypeVar("T", bound="PatchOperation")


@attr.s(auto_attribs=True)
class PatchOperation:
    r"""Individual JSON Patch operation for an HTTP PATCH request.

    Attributes:
        op (PatchOperationOp): Type of JSON Patch operation. Supported JSON Patch operations include add, replace, and
            delete. See <https://tools.ietf.org/html/rfc6902>.
        path (str): JSON Pointer path of the element to patch. See <https://tools.ietf.org/html/rfc6902>.
        value (Union[Unset, List['PatchOperationValueItem']]): JSON value to add, replace, or delete.
    """

    op: PatchOperationOp
    path: str
    value: Union[Unset, List["PatchOperationValueItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        op = self.op.value

        path = self.path
        value: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()

                value.append(value_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_operation_value_item import PatchOperationValueItem

        d = src_dict.copy()
        op = PatchOperationOp(d.pop("op"))

        path = d.pop("path")

        value = []
        _value = d.pop("value", UNSET)
        for value_item_data in _value or []:
            value_item = PatchOperationValueItem.from_dict(value_item_data)

            value.append(value_item)

        result = cls(
            op=op,
            path=path,
            value=value,
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
