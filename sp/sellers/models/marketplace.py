from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Marketplace")


@attr.s(auto_attribs=True)
class Marketplace:
    r"""Detailed information about an Amazon market where a seller can list items for sale and customers can view and
    purchase items.

        Attributes:
            id (str): The encrypted marketplace value.
            name (str): Marketplace name.
            country_code (str): The ISO 3166-1 alpha-2 format country code of the marketplace.
            default_currency_code (str): The ISO 4217 format currency code of the marketplace.
            default_language_code (str): The ISO 639-1 format language code of the marketplace.
            domain_name (str): The domain name of the marketplace.
    """

    id: str
    name: str
    country_code: str
    default_currency_code: str
    default_language_code: str
    domain_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        country_code = self.country_code
        default_currency_code = self.default_currency_code
        default_language_code = self.default_language_code
        domain_name = self.domain_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "countryCode": country_code,
                "defaultCurrencyCode": default_currency_code,
                "defaultLanguageCode": default_language_code,
                "domainName": domain_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        country_code = d.pop("countryCode")

        default_currency_code = d.pop("defaultCurrencyCode")

        default_language_code = d.pop("defaultLanguageCode")

        domain_name = d.pop("domainName")

        result = cls(
            id=id,
            name=name,
            country_code=country_code,
            default_currency_code=default_currency_code,
            default_language_code=default_language_code,
            domain_name=domain_name,
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
