import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.item import Item
    from ..models.label_customization import LabelCustomization
    from ..models.package_dimensions import PackageDimensions
    from ..models.shipping_service_options import ShippingServiceOptions
    from ..models.weight import Weight


T = TypeVar("T", bound="ShipmentRequestDetails")


@attr.s(auto_attribs=True)
class ShipmentRequestDetails:
    r"""Shipment information required for requesting shipping service offers or for creating a shipment.

    Attributes:
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        item_list (List['Item']): The list of items to be included in a shipment.
        ship_from_address (Address): The postal address information.
        package_dimensions (PackageDimensions): The dimensions of a package contained in a shipment.
        weight (Weight): The weight.
        shipping_service_options (ShippingServiceOptions): Extra services provided by a carrier.
        seller_order_id (Union[Unset, str]): A seller-defined order identifier.
        must_arrive_by_date (Union[Unset, datetime.datetime]):
        ship_date (Union[Unset, datetime.datetime]):
        label_customization (Union[Unset, LabelCustomization]): Custom text for shipping labels.
    """

    amazon_order_id: str
    item_list: List["Item"]
    ship_from_address: "Address"
    package_dimensions: "PackageDimensions"
    weight: "Weight"
    shipping_service_options: "ShippingServiceOptions"
    seller_order_id: Union[Unset, str] = UNSET
    must_arrive_by_date: Union[Unset, datetime.datetime] = UNSET
    ship_date: Union[Unset, datetime.datetime] = UNSET
    label_customization: Union[Unset, "LabelCustomization"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_order_id = self.amazon_order_id
        item_list = []
        for componentsschemas_item_list_item_data in self.item_list:
            componentsschemas_item_list_item = componentsschemas_item_list_item_data.to_dict()

            item_list.append(componentsschemas_item_list_item)

        ship_from_address = self.ship_from_address.to_dict()

        package_dimensions = self.package_dimensions.to_dict()

        weight = self.weight.to_dict()

        shipping_service_options = self.shipping_service_options.to_dict()

        seller_order_id = self.seller_order_id
        must_arrive_by_date: Union[Unset, str] = UNSET
        if not isinstance(self.must_arrive_by_date, Unset):
            must_arrive_by_date = self.must_arrive_by_date.isoformat()

        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        label_customization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label_customization, Unset):
            label_customization = self.label_customization.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "AmazonOrderId": amazon_order_id,
                "ItemList": item_list,
                "ShipFromAddress": ship_from_address,
                "PackageDimensions": package_dimensions,
                "Weight": weight,
                "ShippingServiceOptions": shipping_service_options,
            }
        )
        if seller_order_id is not UNSET:
            field_dict["SellerOrderId"] = seller_order_id
        if must_arrive_by_date is not UNSET:
            field_dict["MustArriveByDate"] = must_arrive_by_date
        if ship_date is not UNSET:
            field_dict["ShipDate"] = ship_date
        if label_customization is not UNSET:
            field_dict["LabelCustomization"] = label_customization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.item import Item
        from ..models.label_customization import LabelCustomization
        from ..models.package_dimensions import PackageDimensions
        from ..models.shipping_service_options import ShippingServiceOptions
        from ..models.weight import Weight

        d = src_dict.copy()
        amazon_order_id = d.pop("AmazonOrderId")

        item_list = []
        _item_list = d.pop("ItemList")
        for componentsschemas_item_list_item_data in _item_list:
            componentsschemas_item_list_item = Item.from_dict(componentsschemas_item_list_item_data)

            item_list.append(componentsschemas_item_list_item)

        ship_from_address = Address.from_dict(d.pop("ShipFromAddress"))

        package_dimensions = PackageDimensions.from_dict(d.pop("PackageDimensions"))

        weight = Weight.from_dict(d.pop("Weight"))

        shipping_service_options = ShippingServiceOptions.from_dict(d.pop("ShippingServiceOptions"))

        seller_order_id = d.pop("SellerOrderId", UNSET)

        _must_arrive_by_date = d.pop("MustArriveByDate", UNSET)
        must_arrive_by_date: Union[Unset, datetime.datetime]
        if isinstance(_must_arrive_by_date, Unset):
            must_arrive_by_date = UNSET
        else:
            must_arrive_by_date = isoparse(_must_arrive_by_date)

        _ship_date = d.pop("ShipDate", UNSET)
        ship_date: Union[Unset, datetime.datetime]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date)

        _label_customization = d.pop("LabelCustomization", UNSET)
        label_customization: Union[Unset, LabelCustomization]
        if isinstance(_label_customization, Unset):
            label_customization = UNSET
        else:
            label_customization = LabelCustomization.from_dict(_label_customization)

        result = cls(
            amazon_order_id=amazon_order_id,
            item_list=item_list,
            ship_from_address=ship_from_address,
            package_dimensions=package_dimensions,
            weight=weight,
            shipping_service_options=shipping_service_options,
            seller_order_id=seller_order_id,
            must_arrive_by_date=must_arrive_by_date,
            ship_date=ship_date,
            label_customization=label_customization,
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
