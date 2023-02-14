from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.small_and_light_enrollment_status import SmallAndLightEnrollmentStatus

T = TypeVar("T", bound="SmallAndLightEnrollment")


@attr.s(auto_attribs=True)
class SmallAndLightEnrollment:
    r"""The Small and Light enrollment status of the item indicated by the specified seller SKU.

    Attributes:
        marketplace_id (str): A marketplace identifier.
        seller_sku (str): Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId,
            which is included with every operation that you submit.
        status (SmallAndLightEnrollmentStatus): The Small and Light enrollment status of the item.
    """

    marketplace_id: str
    seller_sku: str
    status: SmallAndLightEnrollmentStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        seller_sku = self.seller_sku
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "sellerSKU": seller_sku,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        seller_sku = d.pop("sellerSKU")

        status = SmallAndLightEnrollmentStatus(d.pop("status"))

        result = cls(
            marketplace_id=marketplace_id,
            seller_sku=seller_sku,
            status=status,
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
