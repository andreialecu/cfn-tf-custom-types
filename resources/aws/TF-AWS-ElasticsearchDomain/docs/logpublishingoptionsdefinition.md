# TF::AWS::ElasticsearchDomain LogPublishingOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchloggrouparn" title="CloudwatchLogGroupArn">CloudwatchLogGroupArn</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchloggrouparn" title="CloudwatchLogGroupArn">CloudwatchLogGroupArn</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
</pre>

## Properties

#### CloudwatchLogGroupArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

