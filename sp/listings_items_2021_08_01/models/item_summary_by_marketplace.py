import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.item_summary_by_marketplace_condition_type import ItemSummaryByMarketplaceConditionType
from ..models.item_summary_by_marketplace_status_item import ItemSummaryByMarketplaceStatusItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_image import ItemImage


T = TypeVar("T", bound="ItemSummaryByMarketplace")


@attr.s(auto_attribs=True)
class ItemSummaryByMarketplace:
    r"""Summary details of a listings item for an Amazon marketplace.

    Attributes:
        marketplace_id (str): A marketplace identifier. Identifies the Amazon marketplace for the listings item.
        asin (str): Amazon Standard Identification Number (ASIN) of the listings item.
        product_type (str): The Amazon product type of the listings item.
        status (List[ItemSummaryByMarketplaceStatusItem]): Statuses that apply to the listings item.
        item_name (str): Name, or title, associated with an Amazon catalog item.
        created_date (datetime.datetime): Date the listings item was created, in ISO 8601 format.
        last_updated_date (datetime.datetime): Date the listings item was last updated, in ISO 8601 format.
        condition_type (Union[Unset, ItemSummaryByMarketplaceConditionType]): Identifies the condition of the listings
            item.
        fn_sku (Union[Unset, str]): Fulfillment network stock keeping unit is an identifier used by Amazon fulfillment
            centers to identify each unique item.
        main_image (Union[Unset, ItemImage]): Image for the listings item.
    """

    marketplace_id: str
    asin: str
    product_type: str
    status: List[ItemSummaryByMarketplaceStatusItem]
    item_name: str
    created_date: datetime.datetime
    last_updated_date: datetime.datetime
    condition_type: Union[Unset, ItemSummaryByMarketplaceConditionType] = UNSET
    fn_sku: Union[Unset, str] = UNSET
    main_image: Union[Unset, "ItemImage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        asin = self.asin
        product_type = self.product_type
        status = []
        for status_item_data in self.status:
            status_item = status_item_data.value

            status.append(status_item)

        item_name = self.item_name
        created_date = self.created_date.isoformat()

        last_updated_date = self.last_updated_date.isoformat()

        condition_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type.value

        fn_sku = self.fn_sku
        main_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.main_image, Unset):
            main_image = self.main_image.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketplaceId": marketplace_id,
                "asin": asin,
                "productType": product_type,
                "status": status,
                "itemName": item_name,
                "createdDate": created_date,
                "lastUpdatedDate": last_updated_date,
            }
        )
        if condition_type is not UNSET:
            field_dict["conditionType"] = condition_type
        if fn_sku is not UNSET:
            field_dict["fnSku"] = fn_sku
        if main_image is not UNSET:
            field_dict["mainImage"] = main_image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.item_image import ItemImage

        d = src_dict.copy()
        marketplace_id = d.pop("marketplaceId")

        asin = d.pop("asin")

        product_type = d.pop("productType")

        status = []
        _status = d.pop("status")
        for status_item_data in _status:
            status_item = ItemSummaryByMarketplaceStatusItem(status_item_data)

            status.append(status_item)

        item_name = d.pop("itemName")

        created_date = isoparse(d.pop("createdDate"))

        last_updated_date = isoparse(d.pop("lastUpdatedDate"))

        _condition_type = d.pop("conditionType", UNSET)
        condition_type: Union[Unset, ItemSummaryByMarketplaceConditionType]
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = ItemSummaryByMarketplaceConditionType(_condition_type)

        fn_sku = d.pop("fnSku", UNSET)

        _main_image = d.pop("mainImage", UNSET)
        main_image: Union[Unset, ItemImage]
        if isinstance(_main_image, Unset):
            main_image = UNSET
        else:
            main_image = ItemImage.from_dict(_main_image)

        result = cls(
            marketplace_id=marketplace_id,
            asin=asin,
            product_type=product_type,
            status=status,
            item_name=item_name,
            created_date=created_date,
            last_updated_date=last_updated_date,
            condition_type=condition_type,
            fn_sku=fn_sku,
            main_image=main_image,
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
