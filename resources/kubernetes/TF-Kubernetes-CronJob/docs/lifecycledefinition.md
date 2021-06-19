# TF::Kubernetes::CronJob LifecycleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#poststart" title="PostStart">PostStart</a>" : <i>[ <a href="poststartdefinition.md">PostStartDefinition</a>, ... ]</i>,
    "<a href="#prestop" title="PreStop">PreStop</a>" : <i>[ <a href="prestopdefinition.md">PreStopDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#poststart" title="PostStart">PostStart</a>: <i>
      - <a href="poststartdefinition.md">PostStartDefinition</a></i>
<a href="#prestop" title="PreStop">PreStop</a>: <i>
      - <a href="prestopdefinition.md">PreStopDefinition</a></i>
</pre>

## Properties

#### PostStart

_Required_: No

_Type_: List of <a href="poststartdefinition.md">PostStartDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStop

_Required_: No

_Type_: List of <a href="prestopdefinition.md">PreStopDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

