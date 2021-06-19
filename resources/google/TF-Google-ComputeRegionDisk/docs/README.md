# TF::Google::ComputeRegionDisk

Persistent disks are durable storage devices that function similarly to
the physical disks in a desktop or a server. Compute Engine manages the
hardware behind these devices to ensure data redundancy and optimize
performance for you. Persistent disks are available as either standard
hard disk drives (HDD) or solid-state drives (SSD).

Persistent disks are located independently from your virtual machine
instances, so you can detach or move persistent disks to keep your data
even after you delete your instances. Persistent disk performance scales
automatically with size, so you can resize your existing persistent disks
or add more persistent disks to an instance to meet your performance and
storage space requirements.

Add a persistent disk to your instance when you need reliable and
affordable storage with consistent performance characteristics.


To get more information about RegionDisk, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionDisks)
* How-to Guides
    * ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ComputeRegionDisk",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#physicalblocksizebytes" title="PhysicalBlockSizeBytes">PhysicalBlockSizeBytes</a>" : <i>Double</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#replicazones" title="ReplicaZones">ReplicaZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a>, ... ]</i>,
        "<a href="#sourcesnapshotencryptionkey" title="SourceSnapshotEncryptionKey">SourceSnapshotEncryptionKey</a>" : <i>[ <a href="sourcesnapshotencryptionkeydefinition.md">SourceSnapshotEncryptionKeyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ComputeRegionDisk
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#physicalblocksizebytes" title="PhysicalBlockSizeBytes">PhysicalBlockSizeBytes</a>: <i>Double</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#replicazones" title="ReplicaZones">ReplicaZones</a>: <i>
      - String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshot" title="Snapshot">Snapshot</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a></i>
    <a href="#sourcesnapshotencryptionkey" title="SourceSnapshotEncryptionKey">SourceSnapshotEncryptionKey</a>: <i>
      - <a href="sourcesnapshotencryptionkeydefinition.md">SourceSnapshotEncryptionKeyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhysicalBlockSizeBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaZones

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSnapshotEncryptionKey

_Required_: No

_Type_: List of <a href="sourcesnapshotencryptionkeydefinition.md">SourceSnapshotEncryptionKeyDefinition</a>

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

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### Id

Returns the <code>Id</code> value.

#### LabelFingerprint

Returns the <code>LabelFingerprint</code> value.

#### LastAttachTimestamp

Returns the <code>LastAttachTimestamp</code> value.

#### LastDetachTimestamp

Returns the <code>LastDetachTimestamp</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### SourceSnapshotId

Returns the <code>SourceSnapshotId</code> value.

#### Users

Returns the <code>Users</code> value.

