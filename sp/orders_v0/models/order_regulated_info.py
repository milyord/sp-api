from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.regulated_information import RegulatedInformation
    from ..models.regulated_order_verification_status import RegulatedOrderVerificationStatus


T = TypeVar("T", bound="OrderRegulatedInfo")


@attr.s(auto_attribs=True)
class OrderRegulatedInfo:
    r"""The order's regulated information along with its verification status.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        regulated_information (RegulatedInformation): The regulated information collected during purchase and used to
            verify the order.
        requires_dosage_label (bool): When true, the order requires attaching a dosage information label when shipped.
        regulated_order_verification_status (RegulatedOrderVerificationStatus): The verification status of the order
            along with associated approval or rejection metadata.
    """

    amazon_order_id: str
    regulated_information: "RegulatedInformation"
    requires_dosage_label: bool
    regulated_order_verification_status: "RegulatedOrderVerificationStatus"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        regulated_information = self.regulated_information.to_dict()

        requires_dosage_label = self.requires_dosage_label
        regulated_order_verification_status = self.regulated_order_verification_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AmazonOrderId": amazon_order_id,
                "RegulatedInformation": regulated_information,
                "RequiresDosageLabel": requires_dosage_label,
                "RegulatedOrderVerificationStatus": regulated_order_verification_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.regulated_information import RegulatedInformation
        from ..models.regulated_order_verification_status import RegulatedOrderVerificationStatus

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId")

        regulated_information = RegulatedInformation.from_dict(d.pop("RegulatedInformation"))

        requires_dosage_label = d.pop("RequiresDosageLabel")

        regulated_order_verification_status = RegulatedOrderVerificationStatus.from_dict(
            d.pop("RegulatedOrderVerificationStatus")
        )

        result = cls(
            amazon_order_id=amazon_order_id,
            regulated_information=regulated_information,
            requires_dosage_label=requires_dosage_label,
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
