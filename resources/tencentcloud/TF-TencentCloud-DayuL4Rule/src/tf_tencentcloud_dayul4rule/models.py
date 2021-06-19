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
    DPort: Optional[float]
    HealthCheckHealthNum: Optional[float]
    HealthCheckInterval: Optional[float]
    HealthCheckSwitch: Optional[bool]
    HealthCheckTimeout: Optional[float]
    HealthCheckUnhealthNum: Optional[float]
    Id: Optional[str]
    LbType: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    RuleId: Optional[str]
    SPort: Optional[float]
    SessionSwitch: Optional[bool]
    SessionTime: Optional[float]
    SourceType: Optional[float]
    SourceList: Optional[Sequence["_SourceListDefinition"]]

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
            DPort=json_data.get("DPort"),
            HealthCheckHealthNum=json_data.get("HealthCheckHealthNum"),
            HealthCheckInterval=json_data.get("HealthCheckInterval"),
            HealthCheckSwitch=json_data.get("HealthCheckSwitch"),
            HealthCheckTimeout=json_data.get("HealthCheckTimeout"),
            HealthCheckUnhealthNum=json_data.get("HealthCheckUnhealthNum"),
            Id=json_data.get("Id"),
            LbType=json_data.get("LbType"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            RuleId=json_data.get("RuleId"),
            SPort=json_data.get("SPort"),
            SessionSwitch=json_data.get("SessionSwitch"),
            SessionTime=json_data.get("SessionTime"),
            SourceType=json_data.get("SourceType"),
            SourceList=deserialize_list(json_data.get("SourceList"), SourceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SourceListDefinition(BaseModel):
    Source: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceListDefinition = SourceListDefinition


