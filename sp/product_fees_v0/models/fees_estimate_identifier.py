from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.id_type import IdType
from ..models.optional_fulfillment_program import OptionalFulfillmentProgram
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_to_estimate_fees import PriceToEstimateFees


T = TypeVar("T", bound="FeesEstimateIdentifier")


@attr.s(auto_attribs=True)
class FeesEstimateIdentifier:
    r"""An item identifier, marketplace, time of request, and other details that identify an estimate.

    Attributes:
        marketplace_id (Union[Unset, str]): A marketplace identifier.
        seller_id (Union[Unset, str]): The seller identifier.
        id_type (Union[Unset, IdType]): The type of product identifier used in a `FeesEstimateByIdRequest`.
        id_value (Union[Unset, str]): The item identifier.
        is_amazon_fulfilled (Union[Unset, bool]): When true, the offer is fulfilled by Amazon.
        price_to_estimate_fees (Union[Unset, PriceToEstimateFees]): Price information for an item, used to estimate
            fees.
        seller_input_identifier (Union[Unset, str]): A unique identifier provided by the caller to track this request.
        optional_fulfillment_program (Union[Unset, OptionalFulfillmentProgram]): An optional enrollment program to
            return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """

    marketplace_id: Union[Unset, str] = UNSET
    seller_id: Union[Unset, str] = UNSET
    id_type: Union[Unset, IdType] = UNSET
    id_value: Union[Unset, str] = UNSET
    is_amazon_fulfilled: Union[Unset, bool] = UNSET
    price_to_estimate_fees: Union[Unset, "PriceToEstimateFees"] = UNSET
    seller_input_identifier: Union[Unset, str] = UNSET
    optional_fulfillment_program: Union[Unset, OptionalFulfillmentProgram] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        marketplace_id = self.marketplace_id
        seller_id = self.seller_id
        id_type: Union[Unset, str] = UNSET
        if not isinstance(self.id_type, Unset):
            id_type = self.id_type.value

        id_value = self.id_value
        is_amazon_fulfilled = self.is_amazon_fulfilled
        price_to_estimate_fees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_to_estimate_fees, Unset):
            price_to_estimate_fees = self.price_to_estimate_fees.to_dict()

        seller_input_identifier = self.seller_input_identifier
        optional_fulfillment_program: Union[Unset, str] = UNSET
        if not isinstance(self.optional_fulfillment_program, Unset):
            optional_fulfillment_program = self.optional_fulfillment_program.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if marketplace_id is not UNSET:
            field_dict["MarketplaceId"] = marketplace_id
        if seller_id is not UNSET:
            field_dict["SellerId"] = seller_id
        if id_type is not UNSET:
            field_dict["IdType"] = id_type
        if id_value is not UNSET:
            field_dict["IdValue"] = id_value
        if is_amazon_fulfilled is not UNSET:
            field_dict["IsAmazonFulfilled"] = is_amazon_fulfilled
        if price_to_estimate_fees is not UNSET:
            field_dict["PriceToEstimateFees"] = price_to_estimate_fees
        if seller_input_identifier is not UNSET:
            field_dict["SellerInputIdentifier"] = seller_input_identifier
        if optional_fulfillment_program is not UNSET:
            field_dict["OptionalFulfillmentProgram"] = optional_fulfillment_program

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.price_to_estimate_fees import PriceToEstimateFees

        d = src_dict.copy()
        marketplace_id = d.pop("MarketplaceId", UNSET)

        seller_id = d.pop("SellerId", UNSET)

        _id_type = d.pop("IdType", UNSET)
        id_type: Union[Unset, IdType]
        if isinstance(_id_type, Unset):
            id_type = UNSET
        else:
            id_type = IdType(_id_type)

        id_value = d.pop("IdValue", UNSET)

        is_amazon_fulfilled = d.pop("IsAmazonFulfilled", UNSET)

        _price_to_estimate_fees = d.pop("PriceToEstimateFees", UNSET)
        price_to_estimate_fees: Union[Unset, PriceToEstimateFees]
        if isinstance(_price_to_estimate_fees, Unset):
            price_to_estimate_fees = UNSET
        else:
            price_to_estimate_fees = PriceToEstimateFees.from_dict(_price_to_estimate_fees)

        seller_input_identifier = d.pop("SellerInputIdentifier", UNSET)

        _optional_fulfillment_program = d.pop("OptionalFulfillmentProgram", UNSET)
        optional_fulfillment_program: Union[Unset, OptionalFulfillmentProgram]
        if isinstance(_optional_fulfillment_program, Unset):
            optional_fulfillment_program = UNSET
        else:
            optional_fulfillment_program = OptionalFulfillmentProgram(_optional_fulfillment_program)

        result = cls(
            marketplace_id=marketplace_id,
            seller_id=seller_id,
            id_type=id_type,
            id_value=id_value,
            is_amazon_fulfilled=is_amazon_fulfilled,
            price_to_estimate_fees=price_to_estimate_fees,
            seller_input_identifier=seller_input_identifier,
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
