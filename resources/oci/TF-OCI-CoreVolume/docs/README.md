# TF::OCI::CoreVolume

This resource provides the Volume resource in Oracle Cloud Infrastructure Core service.

Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from
50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB).
For general information about block volumes, see
[Overview of Block Volume Service](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/overview.htm).

A volume and instance can be in separate compartments but must be in the same availability domain.
For information about access control and compartments, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about
availability domains, see [Regions and Availability Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
To get a list of availability domains, use the `ListAvailabilityDomains` operation
in the Identity and Access Management Service API.

You may...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreVolume",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#backuppolicyid" title="BackupPolicyId">BackupPolicyId</a>" : <i>String</i>,
        "<a href="#blockvolumereplicasdeletion" title="BlockVolumeReplicasDeletion">BlockVolumeReplicasDeletion</a>" : <i>Boolean</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#isautotuneenabled" title="IsAutoTuneEnabled">IsAutoTuneEnabled</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#sizeingbs" title="SizeInGbs">SizeInGbs</a>" : <i>String</i>,
        "<a href="#sizeinmbs" title="SizeInMbs">SizeInMbs</a>" : <i>String</i>,
        "<a href="#volumebackupid" title="VolumeBackupId">VolumeBackupId</a>" : <i>String</i>,
        "<a href="#vpuspergb" title="VpusPerGb">VpusPerGb</a>" : <i>String</i>,
        "<a href="#blockvolumereplicas" title="BlockVolumeReplicas">BlockVolumeReplicas</a>" : <i>[ <a href="blockvolumereplicasdefinition.md">BlockVolumeReplicasDefinition</a>, ... ]</i>,
        "<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>" : <i>[ <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreVolume
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#backuppolicyid" title="BackupPolicyId">BackupPolicyId</a>: <i>String</i>
    <a href="#blockvolumereplicasdeletion" title="BlockVolumeReplicasDeletion">BlockVolumeReplicasDeletion</a>: <i>Boolean</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#isautotuneenabled" title="IsAutoTuneEnabled">IsAutoTuneEnabled</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#sizeingbs" title="SizeInGbs">SizeInGbs</a>: <i>String</i>
    <a href="#sizeinmbs" title="SizeInMbs">SizeInMbs</a>: <i>String</i>
    <a href="#volumebackupid" title="VolumeBackupId">VolumeBackupId</a>: <i>String</i>
    <a href="#vpuspergb" title="VpusPerGb">VpusPerGb</a>: <i>String</i>
    <a href="#blockvolumereplicas" title="BlockVolumeReplicas">BlockVolumeReplicas</a>: <i>
      - <a href="blockvolumereplicasdefinition.md">BlockVolumeReplicasDefinition</a></i>
    <a href="#sourcedetails" title="SourceDetails">SourceDetails</a>: <i>
      - <a href="sourcedetailsdefinition.md">SourceDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityDomain

(Updatable) The availability domain of the block volume replica.  Example: `Uocm:PHX-AD-1`
* `display_name` - (Optional) (Updatable) The display name of the block volume replica. You may optionally specify a *display name* for the block volume replica, otherwise a default is provided.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPolicyId

If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockVolumeReplicasDeletion

(updatable) The boolean value, if you have replicas and want to disable replicas set this argument to true and remove `block_volume_replicas` in representation at the same time. If you want to enable a new replicas, remove this argument and use `block_volume_replicas` again.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The OCID of the compartment that contains the volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoTuneEnabled

(Updatable) Specifies whether the auto-tune performance is enabled for this volume.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

(Updatable) The OCID of the Key Management key to assign as the master encryption key for the volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeInGbs

(Updatable) The size of the volume in GBs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeInMbs

The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use `size_in_gbs` instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeBackupId

The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the `source_details` field instead to specify the backup for the volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpusPerGb

(Updatable) The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Elastic Performance](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm) for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockVolumeReplicas

_Required_: No

_Type_: List of <a href="blockvolumereplicasdefinition.md">BlockVolumeReplicasDefinition</a>

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

#### AutoTunedVpusPerGb

Returns the <code>AutoTunedVpusPerGb</code> value.

#### Id

The OCID of the block volume replica.
* `type` - (Required) The type can be one of these values: `blockVolumeReplica`, `volume`, `volumeBackup`.

#### IsHydrated

Returns the <code>IsHydrated</code> value.

#### State

Returns the <code>State</code> value.

#### SystemTags

Returns the <code>SystemTags</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VolumeGroupId

Returns the <code>VolumeGroupId</code> value.

