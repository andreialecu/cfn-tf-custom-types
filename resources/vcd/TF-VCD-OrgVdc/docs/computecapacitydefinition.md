# TF::VCD::OrgVdc ComputeCapacityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>[ <a href="cpudefinition.md">CpuDefinition</a>, ... ]</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>[ <a href="memorydefinition.md">MemoryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cpu" title="Cpu">Cpu</a>: <i>
      - <a href="cpudefinition.md">CpuDefinition</a></i>
<a href="#memory" title="Memory">Memory</a>: <i>
      - <a href="memorydefinition.md">MemoryDefinition</a></i>
</pre>

## Properties

#### Cpu

_Required_: No

_Type_: List of <a href="cpudefinition.md">CpuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: List of <a href="memorydefinition.md">MemoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

