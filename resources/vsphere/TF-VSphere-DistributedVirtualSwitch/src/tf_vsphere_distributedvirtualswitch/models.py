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
    ActiveUplinks: Optional[Sequence[str]]
    AllowForgedTransmits: Optional[bool]
    AllowMacChanges: Optional[bool]
    AllowPromiscuous: Optional[bool]
    BackupnfcMaximumMbit: Optional[float]
    BackupnfcReservationMbit: Optional[float]
    BackupnfcShareCount: Optional[float]
    BackupnfcShareLevel: Optional[str]
    BlockAllPorts: Optional[bool]
    CheckBeacon: Optional[bool]
    ConfigVersion: Optional[str]
    ContactDetail: Optional[str]
    ContactName: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributesDefinition"]]
    DatacenterId: Optional[str]
    Description: Optional[str]
    DirectpathGen2Allowed: Optional[bool]
    EgressShapingAverageBandwidth: Optional[float]
    EgressShapingBurstSize: Optional[float]
    EgressShapingEnabled: Optional[bool]
    EgressShapingPeakBandwidth: Optional[float]
    Failback: Optional[bool]
    FaulttoleranceMaximumMbit: Optional[float]
    FaulttoleranceReservationMbit: Optional[float]
    FaulttoleranceShareCount: Optional[float]
    FaulttoleranceShareLevel: Optional[str]
    Folder: Optional[str]
    HbrMaximumMbit: Optional[float]
    HbrReservationMbit: Optional[float]
    HbrShareCount: Optional[float]
    HbrShareLevel: Optional[str]
    Id: Optional[str]
    IgnoreOtherPvlanMappings: Optional[bool]
    IngressShapingAverageBandwidth: Optional[float]
    IngressShapingBurstSize: Optional[float]
    IngressShapingEnabled: Optional[bool]
    IngressShapingPeakBandwidth: Optional[float]
    Ipv4Address: Optional[str]
    IscsiMaximumMbit: Optional[float]
    IscsiReservationMbit: Optional[float]
    IscsiShareCount: Optional[float]
    IscsiShareLevel: Optional[str]
    LacpApiVersion: Optional[str]
    LacpEnabled: Optional[bool]
    LacpMode: Optional[str]
    LinkDiscoveryOperation: Optional[str]
    LinkDiscoveryProtocol: Optional[str]
    ManagementMaximumMbit: Optional[float]
    ManagementReservationMbit: Optional[float]
    ManagementShareCount: Optional[float]
    ManagementShareLevel: Optional[str]
    MaxMtu: Optional[float]
    MulticastFilteringMode: Optional[str]
    Name: Optional[str]
    NetflowActiveFlowTimeout: Optional[float]
    NetflowCollectorIpAddress: Optional[str]
    NetflowCollectorPort: Optional[float]
    NetflowEnabled: Optional[bool]
    NetflowIdleFlowTimeout: Optional[float]
    NetflowInternalFlowsOnly: Optional[bool]
    NetflowObservationDomainId: Optional[float]
    NetflowSamplingRate: Optional[float]
    NetworkResourceControlEnabled: Optional[bool]
    NetworkResourceControlVersion: Optional[str]
    NfsMaximumMbit: Optional[float]
    NfsReservationMbit: Optional[float]
    NfsShareCount: Optional[float]
    NfsShareLevel: Optional[str]
    NotifySwitches: Optional[bool]
    PortPrivateSecondaryVlanId: Optional[float]
    StandbyUplinks: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    TeamingPolicy: Optional[str]
    TxUplink: Optional[bool]
    Uplinks: Optional[Sequence[str]]
    VdpMaximumMbit: Optional[float]
    VdpReservationMbit: Optional[float]
    VdpShareCount: Optional[float]
    VdpShareLevel: Optional[str]
    Version: Optional[str]
    VirtualmachineMaximumMbit: Optional[float]
    VirtualmachineReservationMbit: Optional[float]
    VirtualmachineShareCount: Optional[float]
    VirtualmachineShareLevel: Optional[str]
    VlanId: Optional[float]
    VmotionMaximumMbit: Optional[float]
    VmotionReservationMbit: Optional[float]
    VmotionShareCount: Optional[float]
    VmotionShareLevel: Optional[str]
    VsanMaximumMbit: Optional[float]
    VsanReservationMbit: Optional[float]
    VsanShareCount: Optional[float]
    VsanShareLevel: Optional[str]
    Host: Optional[Sequence["_HostDefinition"]]
    PvlanMapping: Optional[Sequence["_PvlanMappingDefinition"]]
    VlanRange: Optional[Sequence["_VlanRangeDefinition"]]

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
            ActiveUplinks=json_data.get("ActiveUplinks"),
            AllowForgedTransmits=json_data.get("AllowForgedTransmits"),
            AllowMacChanges=json_data.get("AllowMacChanges"),
            AllowPromiscuous=json_data.get("AllowPromiscuous"),
            BackupnfcMaximumMbit=json_data.get("BackupnfcMaximumMbit"),
            BackupnfcReservationMbit=json_data.get("BackupnfcReservationMbit"),
            BackupnfcShareCount=json_data.get("BackupnfcShareCount"),
            BackupnfcShareLevel=json_data.get("BackupnfcShareLevel"),
            BlockAllPorts=json_data.get("BlockAllPorts"),
            CheckBeacon=json_data.get("CheckBeacon"),
            ConfigVersion=json_data.get("ConfigVersion"),
            ContactDetail=json_data.get("ContactDetail"),
            ContactName=json_data.get("ContactName"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttributesDefinition),
            DatacenterId=json_data.get("DatacenterId"),
            Description=json_data.get("Description"),
            DirectpathGen2Allowed=json_data.get("DirectpathGen2Allowed"),
            EgressShapingAverageBandwidth=json_data.get("EgressShapingAverageBandwidth"),
            EgressShapingBurstSize=json_data.get("EgressShapingBurstSize"),
            EgressShapingEnabled=json_data.get("EgressShapingEnabled"),
            EgressShapingPeakBandwidth=json_data.get("EgressShapingPeakBandwidth"),
            Failback=json_data.get("Failback"),
            FaulttoleranceMaximumMbit=json_data.get("FaulttoleranceMaximumMbit"),
            FaulttoleranceReservationMbit=json_data.get("FaulttoleranceReservationMbit"),
            FaulttoleranceShareCount=json_data.get("FaulttoleranceShareCount"),
            FaulttoleranceShareLevel=json_data.get("FaulttoleranceShareLevel"),
            Folder=json_data.get("Folder"),
            HbrMaximumMbit=json_data.get("HbrMaximumMbit"),
            HbrReservationMbit=json_data.get("HbrReservationMbit"),
            HbrShareCount=json_data.get("HbrShareCount"),
            HbrShareLevel=json_data.get("HbrShareLevel"),
            Id=json_data.get("Id"),
            IgnoreOtherPvlanMappings=json_data.get("IgnoreOtherPvlanMappings"),
            IngressShapingAverageBandwidth=json_data.get("IngressShapingAverageBandwidth"),
            IngressShapingBurstSize=json_data.get("IngressShapingBurstSize"),
            IngressShapingEnabled=json_data.get("IngressShapingEnabled"),
            IngressShapingPeakBandwidth=json_data.get("IngressShapingPeakBandwidth"),
            Ipv4Address=json_data.get("Ipv4Address"),
            IscsiMaximumMbit=json_data.get("IscsiMaximumMbit"),
            IscsiReservationMbit=json_data.get("IscsiReservationMbit"),
            IscsiShareCount=json_data.get("IscsiShareCount"),
            IscsiShareLevel=json_data.get("IscsiShareLevel"),
            LacpApiVersion=json_data.get("LacpApiVersion"),
            LacpEnabled=json_data.get("LacpEnabled"),
            LacpMode=json_data.get("LacpMode"),
            LinkDiscoveryOperation=json_data.get("LinkDiscoveryOperation"),
            LinkDiscoveryProtocol=json_data.get("LinkDiscoveryProtocol"),
            ManagementMaximumMbit=json_data.get("ManagementMaximumMbit"),
            ManagementReservationMbit=json_data.get("ManagementReservationMbit"),
            ManagementShareCount=json_data.get("ManagementShareCount"),
            ManagementShareLevel=json_data.get("ManagementShareLevel"),
            MaxMtu=json_data.get("MaxMtu"),
            MulticastFilteringMode=json_data.get("MulticastFilteringMode"),
            Name=json_data.get("Name"),
            NetflowActiveFlowTimeout=json_data.get("NetflowActiveFlowTimeout"),
            NetflowCollectorIpAddress=json_data.get("NetflowCollectorIpAddress"),
            NetflowCollectorPort=json_data.get("NetflowCollectorPort"),
            NetflowEnabled=json_data.get("NetflowEnabled"),
            NetflowIdleFlowTimeout=json_data.get("NetflowIdleFlowTimeout"),
            NetflowInternalFlowsOnly=json_data.get("NetflowInternalFlowsOnly"),
            NetflowObservationDomainId=json_data.get("NetflowObservationDomainId"),
            NetflowSamplingRate=json_data.get("NetflowSamplingRate"),
            NetworkResourceControlEnabled=json_data.get("NetworkResourceControlEnabled"),
            NetworkResourceControlVersion=json_data.get("NetworkResourceControlVersion"),
            NfsMaximumMbit=json_data.get("NfsMaximumMbit"),
            NfsReservationMbit=json_data.get("NfsReservationMbit"),
            NfsShareCount=json_data.get("NfsShareCount"),
            NfsShareLevel=json_data.get("NfsShareLevel"),
            NotifySwitches=json_data.get("NotifySwitches"),
            PortPrivateSecondaryVlanId=json_data.get("PortPrivateSecondaryVlanId"),
            StandbyUplinks=json_data.get("StandbyUplinks"),
            Tags=json_data.get("Tags"),
            TeamingPolicy=json_data.get("TeamingPolicy"),
            TxUplink=json_data.get("TxUplink"),
            Uplinks=json_data.get("Uplinks"),
            VdpMaximumMbit=json_data.get("VdpMaximumMbit"),
            VdpReservationMbit=json_data.get("VdpReservationMbit"),
            VdpShareCount=json_data.get("VdpShareCount"),
            VdpShareLevel=json_data.get("VdpShareLevel"),
            Version=json_data.get("Version"),
            VirtualmachineMaximumMbit=json_data.get("VirtualmachineMaximumMbit"),
            VirtualmachineReservationMbit=json_data.get("VirtualmachineReservationMbit"),
            VirtualmachineShareCount=json_data.get("VirtualmachineShareCount"),
            VirtualmachineShareLevel=json_data.get("VirtualmachineShareLevel"),
            VlanId=json_data.get("VlanId"),
            VmotionMaximumMbit=json_data.get("VmotionMaximumMbit"),
            VmotionReservationMbit=json_data.get("VmotionReservationMbit"),
            VmotionShareCount=json_data.get("VmotionShareCount"),
            VmotionShareLevel=json_data.get("VmotionShareLevel"),
            VsanMaximumMbit=json_data.get("VsanMaximumMbit"),
            VsanReservationMbit=json_data.get("VsanReservationMbit"),
            VsanShareCount=json_data.get("VsanShareCount"),
            VsanShareLevel=json_data.get("VsanShareLevel"),
            Host=deserialize_list(json_data.get("Host"), HostDefinition),
            PvlanMapping=deserialize_list(json_data.get("PvlanMapping"), PvlanMappingDefinition),
            VlanRange=deserialize_list(json_data.get("VlanRange"), VlanRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributesDefinition = CustomAttributesDefinition


@dataclass
class HostDefinition(BaseModel):
    Devices: Optional[Sequence[str]]
    HostSystemId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDefinition"]:
        if not json_data:
            return None
        return cls(
            Devices=json_data.get("Devices"),
            HostSystemId=json_data.get("HostSystemId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostDefinition = HostDefinition


@dataclass
class PvlanMappingDefinition(BaseModel):
    PrimaryVlanId: Optional[float]
    PvlanType: Optional[str]
    SecondaryVlanId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PvlanMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PvlanMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            PrimaryVlanId=json_data.get("PrimaryVlanId"),
            PvlanType=json_data.get("PvlanType"),
            SecondaryVlanId=json_data.get("SecondaryVlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PvlanMappingDefinition = PvlanMappingDefinition


@dataclass
class VlanRangeDefinition(BaseModel):
    MaxVlan: Optional[float]
    MinVlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VlanRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VlanRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxVlan=json_data.get("MaxVlan"),
            MinVlan=json_data.get("MinVlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VlanRangeDefinition = VlanRangeDefinition


