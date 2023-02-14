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
        party_id (str): Assigned identification for the party. For example, warehouse code or vendor code. Please refer
            to specific party for more details.
        address (Union[Unset, Address]): Address of the party.
        tax_info (Union[Unset, TaxRegistrationDetails]): Tax registration details of the entity.
    """

    party_id: str
    address: Union[Unset, "Address"] = UNSET
    tax_info: Union[Unset, "TaxRegistrationDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        party_id = self.party_id
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        tax_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_info, Unset):
            tax_info = self.tax_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyId": party_id,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if tax_info is not UNSET:
            field_dict["taxInfo"] = tax_info

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

        _tax_info = d.pop("taxInfo", UNSET)
        tax_info: Union[Unset, TaxRegistrationDetails]
        if isinstance(_tax_info, Unset):
            tax_info = UNSET
        else:
            tax_info = TaxRegistrationDetails.from_dict(_tax_info)

        result = cls(
            party_id=party_id,
            address=address,
            tax_info=tax_info,
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
