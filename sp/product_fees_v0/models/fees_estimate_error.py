from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.fees_estimate_error_detail_item import FeesEstimateErrorDetailItem


T = TypeVar("T", bound="FeesEstimateError")


@attr.s(auto_attribs=True)
class FeesEstimateError:
    r"""An unexpected error occurred during this operation.

    Attributes:
        type (str): An error type, identifying either the receiver or the sender as the originator of the error.
        code (str): An error code that identifies the type of error that occurred.
        message (str): A message that describes the error condition.
        detail (List['FeesEstimateErrorDetailItem']): Additional information that can help the caller understand or fix
            the issue.
    """

    type: str
    code: str
    message: str
    detail: List["FeesEstimateErrorDetailItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        code = self.code
        message = self.message
        detail = []
        for componentsschemas_fees_estimate_error_detail_item_data in self.detail:
            componentsschemas_fees_estimate_error_detail_item = (
                componentsschemas_fees_estimate_error_detail_item_data.to_dict()
            )

            detail.append(componentsschemas_fees_estimate_error_detail_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Type": type,
                "Code": code,
                "Message": message,
                "Detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fees_estimate_error_detail_item import FeesEstimateErrorDetailItem

        d = src_dict.copy()
        type = d.pop("Type")

        code = d.pop("Code")

        message = d.pop("Message")

        detail = []
        _detail = d.pop("Detail")
        for componentsschemas_fees_estimate_error_detail_item_data in _detail:
            componentsschemas_fees_estimate_error_detail_item = FeesEstimateErrorDetailItem.from_dict(
                componentsschemas_fees_estimate_error_detail_item_data
            )

            detail.append(componentsschemas_fees_estimate_error_detail_item)

        result = cls(
            type=type,
            code=code,
            message=message,
            detail=detail,
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
