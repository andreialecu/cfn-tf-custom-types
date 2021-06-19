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
    BalancerProtocol: Optional[str]
    Certificates: Optional[Sequence[str]]
    Enabled: Optional[bool]
    Id: Optional[str]
    LoadBalancer: Optional[str]
    Name: Optional[str]
    OperationDetails: Optional[str]
    ParentListener: Optional[str]
    PathPrefixes: Optional[Sequence[str]]
    Policies: Optional[Sequence[str]]
    Port: Optional[float]
    ServerPool: Optional[str]
    ServerProtocol: Optional[str]
    State: Optional[bool]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]
    VirtualHosts: Optional[Sequence[str]]

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
            BalancerProtocol=json_data.get("BalancerProtocol"),
            Certificates=json_data.get("Certificates"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            LoadBalancer=json_data.get("LoadBalancer"),
            Name=json_data.get("Name"),
            OperationDetails=json_data.get("OperationDetails"),
            ParentListener=json_data.get("ParentListener"),
            PathPrefixes=json_data.get("PathPrefixes"),
            Policies=json_data.get("Policies"),
            Port=json_data.get("Port"),
            ServerPool=json_data.get("ServerPool"),
            ServerProtocol=json_data.get("ServerProtocol"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            VirtualHosts=json_data.get("VirtualHosts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


