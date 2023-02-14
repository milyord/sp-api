from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.update_verification_status_request_body import UpdateVerificationStatusRequestBody


T = TypeVar("T", bound="UpdateVerificationStatusRequest")


@attr.s(auto_attribs=True)
class UpdateVerificationStatusRequest:
    r"""The request body for the updateVerificationStatus operation.

    Attributes:
        regulated_order_verification_status (UpdateVerificationStatusRequestBody): The updated values of the
            VerificationStatus field.
    """

    regulated_order_verification_status: "UpdateVerificationStatusRequestBody"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regulated_order_verification_status = self.regulated_order_verification_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regulatedOrderVerificationStatus": regulated_order_verification_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_verification_status_request_body import UpdateVerificationStatusRequestBody

        d = src_dict.copy()
        regulated_order_verification_status = UpdateVerificationStatusRequestBody.from_dict(
            d.pop("regulatedOrderVerificationStatus")
        )

        result = cls(
            regulated_order_verification_status=regulated_order_verification_status,
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
