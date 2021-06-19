# TF::Kubernetes::Daemonset FlexVolumeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ <a href="secretrefdefinition.md">SecretRefDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - <a href="secretrefdefinition.md">SecretRefDefinition</a></i>
</pre>

## Properties

#### Driver

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of <a href="secretrefdefinition.md">SecretRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

