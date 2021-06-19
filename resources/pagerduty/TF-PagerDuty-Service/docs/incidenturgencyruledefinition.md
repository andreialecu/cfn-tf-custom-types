# TF::PagerDuty::Service IncidentUrgencyRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#urgency" title="Urgency">Urgency</a>" : <i>String</i>,
    "<a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>" : <i>[ <a href="duringsupporthoursdefinition.md">DuringSupportHoursDefinition</a>, ... ]</i>,
    "<a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>" : <i>[ <a href="outsidesupporthoursdefinition.md">OutsideSupportHoursDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#urgency" title="Urgency">Urgency</a>: <i>String</i>
<a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>: <i>
      - <a href="duringsupporthoursdefinition.md">DuringSupportHoursDefinition</a></i>
<a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>: <i>
      - <a href="outsidesupporthoursdefinition.md">OutsideSupportHoursDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Urgency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuringSupportHours

_Required_: No

_Type_: List of <a href="duringsupporthoursdefinition.md">DuringSupportHoursDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideSupportHours

_Required_: No

_Type_: List of <a href="outsidesupporthoursdefinition.md">OutsideSupportHoursDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

