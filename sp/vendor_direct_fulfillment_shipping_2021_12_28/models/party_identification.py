from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.tax_registration_details import TaxRegistrationDetails


T = TypeVar("T", bound="PartyIdentification")


@attr.s(auto_attribs=True)
class PartyIdentification:
    r"""
    Attributes:
        party_id (str): Assigned Identification for the party.
        address (Union[Unset, Address]): Address of the party.
        tax_registration_details (Union[Unset, List['TaxRegistrationDetails']]): Tax registration details of the entity.
    """

    party_id: str
    address: Union[Unset, "Address"] = UNSET
    tax_registration_details: Union[Unset, List["TaxRegistrationDetails"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        party_id = self.party_id
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        tax_registration_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_registration_details, Unset):
            tax_registration_details = []
            for tax_registration_details_item_data in self.tax_registration_details:
                tax_registration_details_item = tax_registration_details_item_data.to_dict()

                tax_registration_details.append(tax_registration_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyId": party_id,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if tax_registration_details is not UNSET:
            field_dict["taxRegistrationDetails"] = tax_registration_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.tax_registration_details import TaxRegistrationDetails

        d = src_dict.copy()
        party_id = d.pop("partyId")

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        tax_registration_details = []
        _tax_registration_details = d.pop("taxRegistrationDetails", UNSET)
        for tax_registration_details_item_data in _tax_registration_details or []:
            tax_registration_details_item = TaxRegistrationDetails.from_dict(tax_registration_details_item_data)

            tax_registration_details.append(tax_registration_details_item)

        result = cls(
            party_id=party_id,
            address=address,
            tax_registration_details=tax_registration_details,
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
