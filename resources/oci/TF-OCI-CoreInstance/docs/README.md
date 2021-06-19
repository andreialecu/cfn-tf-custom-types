# TF::OCI::CoreInstance

This resource provides the Instance resource in Oracle Cloud Infrastructure Core service.

Creates a new instance in the specified compartment and the specified availability domain.
For general information about instances, see
[Overview of the Compute Service](https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm).

For information about access control and compartments, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

For information about availability domains, see
[Regions and Availability Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
To get a list of availability domains, use the `ListAvailabilityDomains` operation
in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned,
unique ID called an Oracle Cloud Identifier (OCID).
When you create a resource, you can find its OCID in the response. You can
als...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreInstance",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#capacityreservationid" title="CapacityReservationId">CapacityReservationId</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#dedicatedvmhostid" title="DedicatedVmHostId">DedicatedVmHostId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#extendedmetadata" title="ExtendedMetadata">ExtendedMetadata</a>" : <i>[ <a href="extendedmetadatadefinition.md">ExtendedMetadataDefinition</a>, ... ]</i>,
        "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#ipxescript" title="IpxeScript">IpxeScript</a>" : <i>String</i>,
        "<a href="#ispvencryptionintransitenabled" title="IsPvEncryptionInTransitEnabled">IsPvEncryptionInTransitEnabled</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#preservebootvolume" title="PreserveBootVolume">PreserveBootVolume</a>" : <i>Boolean</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#agentconfig" title="AgentConfig">AgentConfig</a>" : <i>[ <a href="agentconfigdefinition.md">AgentConfigDefinition</a>, ... ]</i>,
        "<a href="#availabilityconfig" title="AvailabilityConfig">AvailabilityConfig</a>" : <i>[ <a href="availabilityconfigdefinition.md">AvailabilityConfigDefinition</a>, ... ]</i>,
        "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a>, ... ]</i>,
        "<a href="#instanceoptions" title="InstanceOptions">InstanceOptions</a>" : <i>[ <a href="instanceoptionsdefinition.md">InstanceOptionsDefinition</a>, ... ]</i>,
        "<a href="#launchoptions" title="LaunchOptions">LaunchOptions</a>" : <i>[ <a href="launchoptionsdefinition.md">LaunchOptionsDefinition</a>, ... ]</i>,
        "<a href="#platformconfig" title="PlatformConfig">PlatformConfig</a>" : <i>[ <a href="platformconfigdefinition.md">PlatformConfigDefinition</a>, ... ]</i>,
        "<a href="#preemptibleinstanceconfig" title="PreemptibleInstanceConfig">PreemptibleInstanceConfig</a>" : <i>[ <a href="preemptibleinstanceconfigdefinition.md">PreemptibleInstanceConfigDefinition</a>, ... ]</i>,
        "<a href="#shapeconfig" title="ShapeConfig">ShapeConfig</a>" : <i>[ <a href="shapeconfigdefinition.md">ShapeConfigDefinition</a>, ... ]</i>,
        "<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>" : <i>[ <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreInstance
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#capacityreservationid" title="CapacityReservationId">CapacityReservationId</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#dedicatedvmhostid" title="DedicatedVmHostId">DedicatedVmHostId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#extendedmetadata" title="ExtendedMetadata">ExtendedMetadata</a>: <i>
      - <a href="extendedmetadatadefinition.md">ExtendedMetadataDefinition</a></i>
    <a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#ipxescript" title="IpxeScript">IpxeScript</a>: <i>String</i>
    <a href="#ispvencryptionintransitenabled" title="IsPvEncryptionInTransitEnabled">IsPvEncryptionInTransitEnabled</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#preservebootvolume" title="PreserveBootVolume">PreserveBootVolume</a>: <i>Boolean</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#agentconfig" title="AgentConfig">AgentConfig</a>: <i>
      - <a href="agentconfigdefinition.md">AgentConfigDefinition</a></i>
    <a href="#availabilityconfig" title="AvailabilityConfig">AvailabilityConfig</a>: <i>
      - <a href="availabilityconfigdefinition.md">AvailabilityConfigDefinition</a></i>
    <a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a></i>
    <a href="#instanceoptions" title="InstanceOptions">InstanceOptions</a>: <i>
      - <a href="instanceoptionsdefinition.md">InstanceOptionsDefinition</a></i>
    <a href="#launchoptions" title="LaunchOptions">LaunchOptions</a>: <i>
      - <a href="launchoptionsdefinition.md">LaunchOptionsDefinition</a></i>
    <a href="#platformconfig" title="PlatformConfig">PlatformConfig</a>: <i>
      - <a href="platformconfigdefinition.md">PlatformConfigDefinition</a></i>
    <a href="#preemptibleinstanceconfig" title="PreemptibleInstanceConfig">PreemptibleInstanceConfig</a>: <i>
      - <a href="preemptibleinstanceconfigdefinition.md">PreemptibleInstanceConfigDefinition</a></i>
    <a href="#shapeconfig" title="ShapeConfig">ShapeConfig</a>: <i>
      - <a href="shapeconfigdefinition.md">ShapeConfigDefinition</a></i>
    <a href="#sourcedetails" title="SourceDetails">SourceDetails</a>: <i>
      - <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityDomain

The availability domain of the instance.  Example: `Uocm:PHX-AD-1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationId

(Updatable) The OCID of the compute capacity reservation this instance is launched under. You can opt out of all default reservations by specifying an empty string as input for this field. For more information, see [Capacity Reservations](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The OCID of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedVmHostId

The OCID of dedicated VM host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedMetadata

(Updatable) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.

_Required_: No

_Type_: List of <a href="extendedmetadatadefinition.md">ExtendedMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

(Updatable) A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameLabel

Deprecated. Instead use `hostnameLabel` in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/CreateVnicDetails/). If you provide both, the values must match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/InstanceSourceViaImageDetails) source type instead. If you specify values for both, the values must match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpxeScript

This is an advanced option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPvEncryptionInTransitEnabled

(Updatable) Use this for update operation only. This field is  Deprecated during create. For create use `isPvEncryptionInTransitEnabled` in [LaunchInstanceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/datatypes/LaunchInstanceDetails).
* `network_type` - (Optional) (Updatable) Emulation type for the physical network interface card (NIC).
* `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver.
* `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking.
* `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
* `remote_data_volume_type` - (Optional) Emulation type for volume.
* `ISCSI` - ISCSI attached block storage device.
* `SCSI` - Emulated SCSI disk.
* `IDE` - Emulated IDE disk.
* `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images.
* `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

(Updatable) Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveBootVolume

Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.
* `type` - (Required) The type of action to run when the instance is interrupted for eviction.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

(Updatable) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

(Updatable) The target state for the instance. Could be set to RUNNING or STOPPED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Deprecated. Instead use `subnetId` in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/CreateVnicDetails/). At least one of them is required; if you provide both, the values must match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentConfig

_Required_: No

_Type_: List of <a href="agentconfigdefinition.md">AgentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityConfig

_Required_: No

_Type_: List of <a href="availabilityconfigdefinition.md">AvailabilityConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of <a href="createvnicdetailsdefinition.md">CreateVnicDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceOptions

_Required_: No

_Type_: List of <a href="instanceoptionsdefinition.md">InstanceOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchOptions

_Required_: No

_Type_: List of <a href="launchoptionsdefinition.md">LaunchOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformConfig

_Required_: No

_Type_: List of <a href="platformconfigdefinition.md">PlatformConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptibleInstanceConfig

_Required_: No

_Type_: List of <a href="preemptibleinstanceconfigdefinition.md">PreemptibleInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapeConfig

_Required_: No

_Type_: List of <a href="shapeconfigdefinition.md">ShapeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetails

_Required_: No

_Type_: List of <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BootVolumeId

Returns the <code>BootVolumeId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LaunchMode

Returns the <code>LaunchMode</code> value.

#### PrivateIp

A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC's *primary* private IP address. The value appears in the [Vnic](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/Vnic/) object and also the [PrivateIp](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/) object returned by [ListPrivateIps](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) and [GetPrivateIp](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp).

#### PublicIp

Returns the <code>PublicIp</code> value.

#### Region

Returns the <code>Region</code> value.

#### SystemTags

Returns the <code>SystemTags</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeMaintenanceRebootDue

Returns the <code>TimeMaintenanceRebootDue</code> value.

