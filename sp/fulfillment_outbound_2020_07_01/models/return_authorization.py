from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="ReturnAuthorization")


@attr.s(auto_attribs=True)
class ReturnAuthorization:
    r"""Return authorization information for items accepted for return.

    Attributes:
        return_authorization_id (str): An identifier for the return authorization. This identifier associates return
            items with the return authorization used to return them.
        fulfillment_center_id (str): An identifier for the Amazon fulfillment center that the return items should be
            sent to.
        return_to_address (Address): A physical address.
        amazon_rma_id (str): The return merchandise authorization (RMA) that Amazon needs to process the return.
        rma_page_url (str): A URL for a web page that contains the return authorization barcode and the mailing label.
            This does not include pre-paid shipping.
    """

    return_authorization_id: str
    fulfillment_center_id: str
    return_to_address: "Address"
    amazon_rma_id: str
    rma_page_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return_authorization_id = self.return_authorization_id
        fulfillment_center_id = self.fulfillment_center_id
        return_to_address = self.return_to_address.to_dict()

        amazon_rma_id = self.amazon_rma_id
        rma_page_url = self.rma_page_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returnAuthorizationId": return_authorization_id,
                "fulfillmentCenterId": fulfillment_center_id,
                "returnToAddress": return_to_address,
                "amazonRmaId": amazon_rma_id,
                "rmaPageURL": rma_page_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        return_authorization_id = d.pop("returnAuthorizationId")

        fulfillment_center_id = d.pop("fulfillmentCenterId")

        return_to_address = Address.from_dict(d.pop("returnToAddress"))

        amazon_rma_id = d.pop("amazonRmaId")

        rma_page_url = d.pop("rmaPageURL")

        result = cls(
            return_authorization_id=return_authorization_id,
            fulfillment_center_id=fulfillment_center_id,
            return_to_address=return_to_address,
            amazon_rma_id=amazon_rma_id,
            rma_page_url=rma_page_url,
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
