# TF::Google::ContainerNodePool NodeConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>" : <i>[ <a href="guestacceleratordefinition.md">GuestAcceleratorDefinition</a>, ... ]</i>,
    "<a href="#imagetype" title="ImageType">ImageType</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>" : <i>Double</i>,
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
    "<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#preemptible" title="Preemptible">Preemptible</a>" : <i>Boolean</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#taint" title="Taint">Taint</a>" : <i>[ <a href="taintdefinition.md">TaintDefinition</a>, ... ]</i>,
    "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>, ... ]</i>,
    "<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>" : <i>[ <a href="workloadmetadataconfigdefinition.md">WorkloadMetadataConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>: <i>
      - <a href="guestacceleratordefinition.md">GuestAcceleratorDefinition</a></i>
<a href="#imagetype" title="ImageType">ImageType</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>: <i>Double</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>: <i>
      - String</i>
<a href="#preemptible" title="Preemptible">Preemptible</a>: <i>Boolean</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#taint" title="Taint">Taint</a>: <i>
      - <a href="taintdefinition.md">TaintDefinition</a></i>
<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a></i>
<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>: <i>
      - <a href="workloadmetadataconfigdefinition.md">WorkloadMetadataConfigDefinition</a></i>
</pre>

## Properties

#### DiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerator

_Required_: No

_Type_: List of <a href="guestacceleratordefinition.md">GuestAcceleratorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsdCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taint

_Required_: No

_Type_: List of <a href="taintdefinition.md">TaintDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadMetadataConfig

_Required_: No

_Type_: List of <a href="workloadmetadataconfigdefinition.md">WorkloadMetadataConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

