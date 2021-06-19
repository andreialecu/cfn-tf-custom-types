# TF::AzureRM::SiteRecoveryReplicatedVm

Manages a VM replicated using Azure Site Recovery (Azure to Azure only). A replicated VM keeps a copiously updated image of the VM in another region in order to be able to start the VM in that region in case of a disaster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SiteRecoveryReplicatedVm",
    "Properties" : {
        "<a href="#manageddisk" title="ManagedDisk">ManagedDisk</a>" : <i>[ <a href="manageddiskdefinition.md">ManagedDiskDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#recoveryreplicationpolicyid" title="RecoveryReplicationPolicyId">RecoveryReplicationPolicyId</a>" : <i>String</i>,
        "<a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sourcerecoveryfabricname" title="SourceRecoveryFabricName">SourceRecoveryFabricName</a>" : <i>String</i>,
        "<a href="#sourcerecoveryprotectioncontainername" title="SourceRecoveryProtectionContainerName">SourceRecoveryProtectionContainerName</a>" : <i>String</i>,
        "<a href="#sourcevmid" title="SourceVmId">SourceVmId</a>" : <i>String</i>,
        "<a href="#targetavailabilitysetid" title="TargetAvailabilitySetId">TargetAvailabilitySetId</a>" : <i>String</i>,
        "<a href="#targetnetworkid" title="TargetNetworkId">TargetNetworkId</a>" : <i>String</i>,
        "<a href="#targetrecoveryfabricid" title="TargetRecoveryFabricId">TargetRecoveryFabricId</a>" : <i>String</i>,
        "<a href="#targetrecoveryprotectioncontainerid" title="TargetRecoveryProtectionContainerId">TargetRecoveryProtectionContainerId</a>" : <i>String</i>,
        "<a href="#targetresourcegroupid" title="TargetResourceGroupId">TargetResourceGroupId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SiteRecoveryReplicatedVm
Properties:
    <a href="#manageddisk" title="ManagedDisk">ManagedDisk</a>: <i>
      - <a href="manageddiskdefinition.md">ManagedDiskDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#recoveryreplicationpolicyid" title="RecoveryReplicationPolicyId">RecoveryReplicationPolicyId</a>: <i>String</i>
    <a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sourcerecoveryfabricname" title="SourceRecoveryFabricName">SourceRecoveryFabricName</a>: <i>String</i>
    <a href="#sourcerecoveryprotectioncontainername" title="SourceRecoveryProtectionContainerName">SourceRecoveryProtectionContainerName</a>: <i>String</i>
    <a href="#sourcevmid" title="SourceVmId">SourceVmId</a>: <i>String</i>
    <a href="#targetavailabilitysetid" title="TargetAvailabilitySetId">TargetAvailabilitySetId</a>: <i>String</i>
    <a href="#targetnetworkid" title="TargetNetworkId">TargetNetworkId</a>: <i>String</i>
    <a href="#targetrecoveryfabricid" title="TargetRecoveryFabricId">TargetRecoveryFabricId</a>: <i>String</i>
    <a href="#targetrecoveryprotectioncontainerid" title="TargetRecoveryProtectionContainerId">TargetRecoveryProtectionContainerId</a>: <i>String</i>
    <a href="#targetresourcegroupid" title="TargetResourceGroupId">TargetResourceGroupId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ManagedDisk

One or more `managed_disk` block.

_Required_: No

_Type_: List of <a href="manageddiskdefinition.md">ManagedDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the network mapping.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

One or more `network_interface` block.

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryReplicationPolicyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryVaultName

The name of the vault that should be updated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Name of the resource group where the vault that should be updated is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRecoveryFabricName

Name of fabric that should contains this replication.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRecoveryProtectionContainerName

Name of the protection container to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVmId

Id of the VM to replicate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAvailabilitySetId

Id of availability set that the new VM should belong to when a failover is done.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetNetworkId

Network to use when a failover is done (recommended to set if any network_interface is configured for failover).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRecoveryFabricId

Id of fabric where the VM replication should be handled when a failover is done.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRecoveryProtectionContainerId

Id of protection container where the VM replication should be created when a failover is done.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceGroupId

Id of resource group where the VM should be created when a failover is done.

_Required_: Yes

_Type_: String

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

#### Id

Returns the <code>Id</code> value.

