import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.seller_freight_class import SellerFreightClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.contact import Contact
    from ..models.pallet import Pallet
    from ..models.weight import Weight


T = TypeVar("T", bound="PartneredLtlDataInput")


@attr.s(auto_attribs=True)
class PartneredLtlDataInput:
    r"""Information that is required by an Amazon-partnered carrier to ship a Less Than Truckload/Full Truckload (LTL/FTL)
    inbound shipment.

        Attributes:
            contact (Union[Unset, Contact]): Contact information for the person in the seller's organization who is
                responsible for a Less Than Truckload/Full Truckload (LTL/FTL) shipment.
            box_count (Union[Unset, int]):
            seller_freight_class (Union[Unset, SellerFreightClass]): The freight class of the shipment. For information
                about determining the freight class, contact the carrier.
            freight_ready_date (Union[Unset, datetime.date]):
            pallet_list (Union[Unset, List['Pallet']]): A list of pallet information.
            total_weight (Union[Unset, Weight]): The weight of the package.
            seller_declared_value (Union[Unset, Amount]): The monetary value.
    """

    contact: Union[Unset, "Contact"] = UNSET
    box_count: Union[Unset, int] = UNSET
    seller_freight_class: Union[Unset, SellerFreightClass] = UNSET
    freight_ready_date: Union[Unset, datetime.date] = UNSET
    pallet_list: Union[Unset, List["Pallet"]] = UNSET
    total_weight: Union[Unset, "Weight"] = UNSET
    seller_declared_value: Union[Unset, "Amount"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        box_count = self.box_count
        seller_freight_class: Union[Unset, str] = UNSET
        if not isinstance(self.seller_freight_class, Unset):
            seller_freight_class = self.seller_freight_class.value

        freight_ready_date: Union[Unset, str] = UNSET
        if not isinstance(self.freight_ready_date, Unset):
            freight_ready_date = self.freight_ready_date.isoformat()

        pallet_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pallet_list, Unset):
            pallet_list = []
            for componentsschemas_pallet_list_item_data in self.pallet_list:
                componentsschemas_pallet_list_item = componentsschemas_pallet_list_item_data.to_dict()

                pallet_list.append(componentsschemas_pallet_list_item)

        total_weight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_weight, Unset):
            total_weight = self.total_weight.to_dict()

        seller_declared_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_declared_value, Unset):
            seller_declared_value = self.seller_declared_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["Contact"] = contact
        if box_count is not UNSET:
            field_dict["BoxCount"] = box_count
        if seller_freight_class is not UNSET:
            field_dict["SellerFreightClass"] = seller_freight_class
        if freight_ready_date is not UNSET:
            field_dict["FreightReadyDate"] = freight_ready_date
        if pallet_list is not UNSET:
            field_dict["PalletList"] = pallet_list
        if total_weight is not UNSET:
            field_dict["TotalWeight"] = total_weight
        if seller_declared_value is not UNSET:
            field_dict["SellerDeclaredValue"] = seller_declared_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount import Amount
        from ..models.contact import Contact
        from ..models.pallet import Pallet
        from ..models.weight import Weight

        d = src_dict.copy()
        _contact = d.pop("Contact", UNSET)
        contact: Union[Unset, Contact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = Contact.from_dict(_contact)

        box_count = d.pop("BoxCount", UNSET)

        _seller_freight_class = d.pop("SellerFreightClass", UNSET)
        seller_freight_class: Union[Unset, SellerFreightClass]
        if isinstance(_seller_freight_class, Unset):
            seller_freight_class = UNSET
        else:
            seller_freight_class = SellerFreightClass(_seller_freight_class)

        _freight_ready_date = d.pop("FreightReadyDate", UNSET)
        freight_ready_date: Union[Unset, datetime.date]
        if isinstance(_freight_ready_date, Unset):
            freight_ready_date = UNSET
        else:
            freight_ready_date = isoparse(_freight_ready_date).date()

        pallet_list = []
        _pallet_list = d.pop("PalletList", UNSET)
        for componentsschemas_pallet_list_item_data in _pallet_list or []:
            componentsschemas_pallet_list_item = Pallet.from_dict(componentsschemas_pallet_list_item_data)

            pallet_list.append(componentsschemas_pallet_list_item)

        _total_weight = d.pop("TotalWeight", UNSET)
        total_weight: Union[Unset, Weight]
        if isinstance(_total_weight, Unset):
            total_weight = UNSET
        else:
            total_weight = Weight.from_dict(_total_weight)

        _seller_declared_value = d.pop("SellerDeclaredValue", UNSET)
        seller_declared_value: Union[Unset, Amount]
        if isinstance(_seller_declared_value, Unset):
            seller_declared_value = UNSET
        else:
            seller_declared_value = Amount.from_dict(_seller_declared_value)

        result = cls(
            contact=contact,
            box_count=box_count,
            seller_freight_class=seller_freight_class,
            freight_ready_date=freight_ready_date,
            pallet_list=pallet_list,
            total_weight=total_weight,
            seller_declared_value=seller_declared_value,
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
