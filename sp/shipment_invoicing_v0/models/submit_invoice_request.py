from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitInvoiceRequest")


@attr.s(auto_attribs=True)
class SubmitInvoiceRequest:
    r"""The request schema for the submitInvoice operation.

    Attributes:
        invoice_content (str): Shipment invoice document content.
        content_md5_value (str): MD5 sum for validating the invoice data. For more information about calculating this
            value, see [Working with Content-MD5
            Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
        marketplace_id (Union[Unset, str]): An Amazon marketplace identifier.
    """

    invoice_content: str
    content_md5_value: str
    marketplace_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_content = self.invoice_content
        content_md5_value = self.content_md5_value
        marketplace_id = self.marketplace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "InvoiceContent": invoice_content,
                "ContentMD5Value": content_md5_value,
            }
        )
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_content = d.pop("InvoiceContent")

        content_md5_value = d.pop("ContentMD5Value")

        marketplace_id = d.pop("MarketplaceId", UNSET)

        result = cls(
            invoice_content=invoice_content,
            content_md5_value=content_md5_value,
            marketplace_id=marketplace_id,
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
