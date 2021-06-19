# TF::AWS::LexBotAlias LogSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
    "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>,
    "<a href="#resourcearn" title="ResourceArn">ResourceArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destination" title="Destination">Destination</a>: <i>String</i>
<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
<a href="#resourcearn" title="ResourceArn">ResourceArn</a>: <i>String</i>
</pre>

## Properties

#### Destination

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

