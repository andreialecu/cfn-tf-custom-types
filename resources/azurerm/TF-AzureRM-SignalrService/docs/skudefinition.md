# TF::AzureRM::SignalrService SkuDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Capacity

Specifies the number of units associated with this SignalR service. Valid values are `1`, `2`, `5`, `10`, `20`, `50` and `100`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies which tier to use. Valid values are `Free_F1` and `Standard_S1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

