from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.item_approval_status import ItemApprovalStatus
from ..models.item_approval_type import ItemApprovalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_support_data_element import ApprovalSupportDataElement


T = TypeVar("T", bound="ItemApprovalContext")


@attr.s(auto_attribs=True)
class ItemApprovalContext:
    r"""Generic item approval context. Check the applicable restrictions at the specific approval type schemas.

    Attributes:
        approval_type (ItemApprovalType): Defines the approval process types available for order items.
        approval_status (ItemApprovalStatus): Defines the possible status of an order item approval.
        approval_support_data (Union[Unset, List['ApprovalSupportDataElement']]): List of additional data elements
            supporting the approval process. Check the applicable restrictions at the specific approval type schemas.
    """

    approval_type: ItemApprovalType
    approval_status: ItemApprovalStatus
    approval_support_data: Union[Unset, List["ApprovalSupportDataElement"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        approval_type = self.approval_type.value

        approval_status = self.approval_status.value

        approval_support_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approval_support_data, Unset):
            approval_support_data = []
            for componentsschemas_approval_support_data_element_list_item_data in self.approval_support_data:
                componentsschemas_approval_support_data_element_list_item = (
                    componentsschemas_approval_support_data_element_list_item_data.to_dict()
                )

                approval_support_data.append(componentsschemas_approval_support_data_element_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ApprovalType": approval_type,
                "ApprovalStatus": approval_status,
            }
        )
        if approval_support_data is not UNSET:
            field_dict["ApprovalSupportData"] = approval_support_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_support_data_element import ApprovalSupportDataElement

        d = src_dict.copy()
        approval_type = ItemApprovalType(d.pop("ApprovalType"))

        approval_status = ItemApprovalStatus(d.pop("ApprovalStatus"))

        approval_support_data = []
        _approval_support_data = d.pop("ApprovalSupportData", UNSET)
        for componentsschemas_approval_support_data_element_list_item_data in _approval_support_data or []:
            componentsschemas_approval_support_data_element_list_item = ApprovalSupportDataElement.from_dict(
                componentsschemas_approval_support_data_element_list_item_data
            )

            approval_support_data.append(componentsschemas_approval_support_data_element_list_item)

        result = cls(
            approval_type=approval_type,
            approval_status=approval_status,
            approval_support_data=approval_support_data,
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
