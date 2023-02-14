import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.shipment_status import ShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.currency_amount import CurrencyAmount
    from ..models.item import Item
    from ..models.label import Label
    from ..models.package_dimensions import PackageDimensions
    from ..models.shipping_service import ShippingService
    from ..models.weight import Weight


T = TypeVar("T", bound="Shipment")


@attr.s(auto_attribs=True)
class Shipment:
    r"""The details of a shipment, including the shipment status.

    Attributes:
        shipment_id (str): An Amazon-defined shipment identifier.
        amazon_order_id (str): An Amazon-defined order identifier, in 3-7-7 format.
        item_list (List['Item']): The list of items to be included in a shipment.
        ship_from_address (Address): The postal address information.
        ship_to_address (Address): The postal address information.
        package_dimensions (PackageDimensions): The dimensions of a package contained in a shipment.
        weight (Weight): The weight.
        insurance (CurrencyAmount): Currency type and amount.
        shipping_service (ShippingService): A shipping service offer made by a carrier.
        label (Label): Data for creating a shipping label and dimensions for printing the label.
        status (ShipmentStatus): The shipment status.
        created_date (datetime.datetime):
        seller_order_id (Union[Unset, str]): A seller-defined order identifier.
        tracking_id (Union[Unset, str]): The shipment tracking identifier provided by the carrier.
        last_updated_date (Union[Unset, datetime.datetime]):
    """

    shipment_id: str
    amazon_order_id: str
    item_list: List["Item"]
    ship_from_address: "Address"
    ship_to_address: "Address"
    package_dimensions: "PackageDimensions"
    weight: "Weight"
    insurance: "CurrencyAmount"
    shipping_service: "ShippingService"
    label: "Label"
    status: ShipmentStatus
    created_date: datetime.datetime
    seller_order_id: Union[Unset, str] = UNSET
    tracking_id: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id
        amazon_order_id = self.amazon_order_id
        item_list = []
        for componentsschemas_item_list_item_data in self.item_list:
            componentsschemas_item_list_item = componentsschemas_item_list_item_data.to_dict()

            item_list.append(componentsschemas_item_list_item)

        ship_from_address = self.ship_from_address.to_dict()

        ship_to_address = self.ship_to_address.to_dict()

        package_dimensions = self.package_dimensions.to_dict()

        weight = self.weight.to_dict()

        insurance = self.insurance.to_dict()

        shipping_service = self.shipping_service.to_dict()

        label = self.label.to_dict()

        status = self.status.value

        created_date = self.created_date.isoformat()

        seller_order_id = self.seller_order_id
        tracking_id = self.tracking_id
        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ShipmentId": shipment_id,
                "AmazonOrderId": amazon_order_id,
                "ItemList": item_list,
                "ShipFromAddress": ship_from_address,
                "ShipToAddress": ship_to_address,
                "PackageDimensions": package_dimensions,
                "Weight": weight,
                "Insurance": insurance,
                "ShippingService": shipping_service,
                "Label": label,
                "Status": status,
                "CreatedDate": created_date,
            }
        )
        if seller_order_id is not UNSET:
            field_dict["SellerOrderId"] = seller_order_id
        if tracking_id is not UNSET:
            field_dict["TrackingId"] = tracking_id
        if last_updated_date is not UNSET:
            field_dict["LastUpdatedDate"] = last_updated_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.currency_amount import CurrencyAmount
        from ..models.item import Item
        from ..models.label import Label
        from ..models.package_dimensions import PackageDimensions
        from ..models.shipping_service import ShippingService
        from ..models.weight import Weight

        d = src_dict.copy()
        shipment_id = d.pop("ShipmentId")

        amazon_order_id = d.pop("AmazonOrderId")

        item_list = []
        _item_list = d.pop("ItemList")
        for componentsschemas_item_list_item_data in _item_list:
            componentsschemas_item_list_item = Item.from_dict(componentsschemas_item_list_item_data)

            item_list.append(componentsschemas_item_list_item)

        ship_from_address = Address.from_dict(d.pop("ShipFromAddress"))

        ship_to_address = Address.from_dict(d.pop("ShipToAddress"))

        package_dimensions = PackageDimensions.from_dict(d.pop("PackageDimensions"))

        weight = Weight.from_dict(d.pop("Weight"))

        insurance = CurrencyAmount.from_dict(d.pop("Insurance"))

        shipping_service = ShippingService.from_dict(d.pop("ShippingService"))

        label = Label.from_dict(d.pop("Label"))

        status = ShipmentStatus(d.pop("Status"))

        created_date = isoparse(d.pop("CreatedDate"))

        seller_order_id = d.pop("SellerOrderId", UNSET)

        tracking_id = d.pop("TrackingId", UNSET)

        _last_updated_date = d.pop("LastUpdatedDate", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        result = cls(
            shipment_id=shipment_id,
            amazon_order_id=amazon_order_id,
            item_list=item_list,
            ship_from_address=ship_from_address,
            ship_to_address=ship_to_address,
            package_dimensions=package_dimensions,
            weight=weight,
            insurance=insurance,
            shipping_service=shipping_service,
            label=label,
            status=status,
            created_date=created_date,
            seller_order_id=seller_order_id,
            tracking_id=tracking_id,
            last_updated_date=last_updated_date,
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
