from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.optional_fulfillment_program import OptionalFulfillmentProgram
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_to_estimate_fees import PriceToEstimateFees


T = TypeVar("T", bound="FeesEstimateRequest")


@attr.s(auto_attribs=True)
class FeesEstimateRequest:
    r"""
    Attributes:
        marketplace_id (str): A marketplace identifier.
        price_to_estimate_fees (PriceToEstimateFees): Price information for an item, used to estimate fees.
        identifier (str): A unique identifier provided by the caller to track this request.
        is_amazon_fulfilled (Union[Unset, bool]): When true, the offer is fulfilled by Amazon.
        optional_fulfillment_program (Union[Unset, OptionalFulfillmentProgram]): An optional enrollment program to
            return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """

    marketplace_id: str
    price_to_estimate_fees: "PriceToEstimateFees"
    identifier: str
    is_amazon_fulfilled: Union[Unset, bool] = UNSET
    optional_fulfillment_program: Union[Unset, OptionalFulfillmentProgram] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        price_to_estimate_fees = self.price_to_estimate_fees.to_dict()

        identifier = self.identifier
        is_amazon_fulfilled = self.is_amazon_fulfilled
        optional_fulfillment_program: Union[Unset, str] = UNSET
        if not isinstance(self.optional_fulfillment_program, Unset):
            optional_fulfillment_program = self.optional_fulfillment_program.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "MarketplaceId": marketplace_id,
                "PriceToEstimateFees": price_to_estimate_fees,
                "Identifier": identifier,
            }
        )
        if is_amazon_fulfilled is not UNSET:
            field_dict["IsAmazonFulfilled"] = is_amazon_fulfilled
        if optional_fulfillment_program is not UNSET:
            field_dict["OptionalFulfillmentProgram"] = optional_fulfillment_program

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_to_estimate_fees import PriceToEstimateFees

        d = src_dict.copy()
        marketplace_id = d.pop("MarketplaceId")

        price_to_estimate_fees = PriceToEstimateFees.from_dict(d.pop("PriceToEstimateFees"))

        identifier = d.pop("Identifier")

        is_amazon_fulfilled = d.pop("IsAmazonFulfilled", UNSET)

        _optional_fulfillment_program = d.pop("OptionalFulfillmentProgram", UNSET)
        optional_fulfillment_program: Union[Unset, OptionalFulfillmentProgram]
        if isinstance(_optional_fulfillment_program, Unset):
            optional_fulfillment_program = UNSET
        else:
            optional_fulfillment_program = OptionalFulfillmentProgram(_optional_fulfillment_program)

        result = cls(
            marketplace_id=marketplace_id,
            price_to_estimate_fees=price_to_estimate_fees,
            identifier=identifier,
            is_amazon_fulfilled=is_amazon_fulfilled,
            optional_fulfillment_program=optional_fulfillment_program,
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
