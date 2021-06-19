# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    DatAddress: Optional[str]
    DatDynamicDistribution: Optional[str]
    DatPort: Optional[float]
    DatType: Optional[str]
    Description: Optional[str]
    DestinationAddresses: Optional[Sequence[str]]
    DestinationZone: Optional[str]
    Disabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Rulebase: Optional[str]
    SatAddressType: Optional[str]
    SatFallbackInterface: Optional[str]
    SatFallbackIpAddress: Optional[str]
    SatFallbackIpType: Optional[str]
    SatFallbackTranslatedAddresses: Optional[Sequence[str]]
    SatFallbackType: Optional[str]
    SatInterface: Optional[str]
    SatIpAddress: Optional[str]
    SatStaticBiDirectional: Optional[bool]
    SatStaticTranslatedAddress: Optional[str]
    SatTranslatedAddresses: Optional[Sequence[str]]
    SatType: Optional[str]
    Service: Optional[str]
    SourceAddresses: Optional[Sequence[str]]
    SourceZones: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    ToInterface: Optional[str]
    Type: Optional[str]
    Vsys: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DatAddress=json_data.get("DatAddress"),
            DatDynamicDistribution=json_data.get("DatDynamicDistribution"),
            DatPort=json_data.get("DatPort"),
            DatType=json_data.get("DatType"),
            Description=json_data.get("Description"),
            DestinationAddresses=json_data.get("DestinationAddresses"),
            DestinationZone=json_data.get("DestinationZone"),
            Disabled=json_data.get("Disabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Rulebase=json_data.get("Rulebase"),
            SatAddressType=json_data.get("SatAddressType"),
            SatFallbackInterface=json_data.get("SatFallbackInterface"),
            SatFallbackIpAddress=json_data.get("SatFallbackIpAddress"),
            SatFallbackIpType=json_data.get("SatFallbackIpType"),
            SatFallbackTranslatedAddresses=json_data.get("SatFallbackTranslatedAddresses"),
            SatFallbackType=json_data.get("SatFallbackType"),
            SatInterface=json_data.get("SatInterface"),
            SatIpAddress=json_data.get("SatIpAddress"),
            SatStaticBiDirectional=json_data.get("SatStaticBiDirectional"),
            SatStaticTranslatedAddress=json_data.get("SatStaticTranslatedAddress"),
            SatTranslatedAddresses=json_data.get("SatTranslatedAddresses"),
            SatType=json_data.get("SatType"),
            Service=json_data.get("Service"),
            SourceAddresses=json_data.get("SourceAddresses"),
            SourceZones=json_data.get("SourceZones"),
            Tags=json_data.get("Tags"),
            ToInterface=json_data.get("ToInterface"),
            Type=json_data.get("Type"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


