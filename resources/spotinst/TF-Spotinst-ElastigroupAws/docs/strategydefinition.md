# TF::Spotinst::ElastigroupAws StrategyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#batchminhealthypercentage" title="BatchMinHealthyPercentage">BatchMinHealthyPercentage</a>" : <i>Double</i>,
    "<a href="#shoulddraininstances" title="ShouldDrainInstances">ShouldDrainInstances</a>" : <i>Boolean</i>,
    "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>[ <a href="onfailuredefinition.md">OnFailureDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#batchminhealthypercentage" title="BatchMinHealthyPercentage">BatchMinHealthyPercentage</a>: <i>Double</i>
<a href="#shoulddraininstances" title="ShouldDrainInstances">ShouldDrainInstances</a>: <i>Boolean</i>
<a href="#onfailure" title="OnFailure">OnFailure</a>: <i>
      - <a href="onfailuredefinition.md">OnFailureDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchMinHealthyPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldDrainInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnFailure

_Required_: No

_Type_: List of <a href="onfailuredefinition.md">OnFailureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

