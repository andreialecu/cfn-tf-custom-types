# TF::AzureRM::KubernetesCluster DefaultNodePoolDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
    "<a href="#enableautoscaling" title="EnableAutoScaling">EnableAutoScaling</a>" : <i>Boolean</i>,
    "<a href="#enablehostencryption" title="EnableHostEncryption">EnableHostEncryption</a>" : <i>Boolean</i>,
    "<a href="#enablenodepublicip" title="EnableNodePublicIp">EnableNodePublicIp</a>" : <i>Boolean</i>,
    "<a href="#maxcount" title="MaxCount">MaxCount</a>" : <i>Double</i>,
    "<a href="#maxpods" title="MaxPods">MaxPods</a>" : <i>Double</i>,
    "<a href="#mincount" title="MinCount">MinCount</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#nodelabels" title="NodeLabels">NodeLabels</a>" : <i>[ <a href="nodelabelsdefinition.md">NodeLabelsDefinition</a>, ... ]</i>,
    "<a href="#nodepublicipprefixid" title="NodePublicIpPrefixId">NodePublicIpPrefixId</a>" : <i>String</i>,
    "<a href="#nodetaints" title="NodeTaints">NodeTaints</a>" : <i>[ String, ... ]</i>,
    "<a href="#onlycriticaladdonsenabled" title="OnlyCriticalAddonsEnabled">OnlyCriticalAddonsEnabled</a>" : <i>Boolean</i>,
    "<a href="#orchestratorversion" title="OrchestratorVersion">OrchestratorVersion</a>" : <i>String</i>,
    "<a href="#osdisksizegb" title="OsDiskSizeGb">OsDiskSizeGb</a>" : <i>Double</i>,
    "<a href="#osdisktype" title="OsDiskType">OsDiskType</a>" : <i>String</i>,
    "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
    "<a href="#vnetsubnetid" title="VnetSubnetId">VnetSubnetId</a>" : <i>String</i>,
    "<a href="#kubeletconfig" title="KubeletConfig">KubeletConfig</a>" : <i>[ <a href="kubeletconfigdefinition.md">KubeletConfigDefinition</a>, ... ]</i>,
    "<a href="#linuxosconfig" title="LinuxOsConfig">LinuxOsConfig</a>" : <i>[ <a href="linuxosconfigdefinition.md">LinuxOsConfigDefinition</a>, ... ]</i>,
    "<a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>" : <i>[ <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
<a href="#enableautoscaling" title="EnableAutoScaling">EnableAutoScaling</a>: <i>Boolean</i>
<a href="#enablehostencryption" title="EnableHostEncryption">EnableHostEncryption</a>: <i>Boolean</i>
<a href="#enablenodepublicip" title="EnableNodePublicIp">EnableNodePublicIp</a>: <i>Boolean</i>
<a href="#maxcount" title="MaxCount">MaxCount</a>: <i>Double</i>
<a href="#maxpods" title="MaxPods">MaxPods</a>: <i>Double</i>
<a href="#mincount" title="MinCount">MinCount</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#nodelabels" title="NodeLabels">NodeLabels</a>: <i>
      - <a href="nodelabelsdefinition.md">NodeLabelsDefinition</a></i>
<a href="#nodepublicipprefixid" title="NodePublicIpPrefixId">NodePublicIpPrefixId</a>: <i>String</i>
<a href="#nodetaints" title="NodeTaints">NodeTaints</a>: <i>
      - String</i>
<a href="#onlycriticaladdonsenabled" title="OnlyCriticalAddonsEnabled">OnlyCriticalAddonsEnabled</a>: <i>Boolean</i>
<a href="#orchestratorversion" title="OrchestratorVersion">OrchestratorVersion</a>: <i>String</i>
<a href="#osdisksizegb" title="OsDiskSizeGb">OsDiskSizeGb</a>: <i>Double</i>
<a href="#osdisktype" title="OsDiskType">OsDiskType</a>: <i>String</i>
<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
<a href="#vnetsubnetid" title="VnetSubnetId">VnetSubnetId</a>: <i>String</i>
<a href="#kubeletconfig" title="KubeletConfig">KubeletConfig</a>: <i>
      - <a href="kubeletconfigdefinition.md">KubeletConfigDefinition</a></i>
<a href="#linuxosconfig" title="LinuxOsConfig">LinuxOsConfig</a>: <i>
      - <a href="linuxosconfigdefinition.md">LinuxOsConfigDefinition</a></i>
<a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>: <i>
      - <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a></i>
</pre>

## Properties

#### AvailabilityZones

A list of Availability Zones across which the Node Pool should be spread. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoScaling

Should [the Kubernetes Auto Scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler) be enabled for this Node Pool? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHostEncryption

Should the nodes in the Default Node Pool have host encryption enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNodePublicIp

Should nodes in this Node Pool have a Public IP Address? Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPods

The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLabels

A map of Kubernetes labels which should be applied to nodes in the Default Node Pool. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="nodelabelsdefinition.md">NodeLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePublicIpPrefixId

Resource ID for the Public IP Addresses Prefix for the nodes in this Node Pool. `enable_node_public_ip` should be `true`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTaints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyCriticalAddonsEnabled

Enabling this option will taint default node pool with `CriticalAddonsOnly=true:NoSchedule` taint. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrchestratorVersion

Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDiskSizeGb

The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDiskType

The type of disk which should be used for the Operating System. Possible values are `Ephemeral` and `Managed`. Defaults to `Managed`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of Node Pool which should be created. Possible values are `AvailabilitySet` and `VirtualMachineScaleSets`. Defaults to `VirtualMachineScaleSets`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

The size of the Virtual Machine, such as `Standard_DS2_v2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetSubnetId

The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeletConfig

_Required_: No

_Type_: List of <a href="kubeletconfigdefinition.md">KubeletConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxOsConfig

_Required_: No

_Type_: List of <a href="linuxosconfigdefinition.md">LinuxOsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSettings

_Required_: No

_Type_: List of <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

