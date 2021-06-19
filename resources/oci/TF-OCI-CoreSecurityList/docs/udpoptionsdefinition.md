# TF::OCI::CoreSecurityList UdpOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#max" title="Max">Max</a>" : <i>Double</i>,
    "<a href="#min" title="Min">Min</a>" : <i>Double</i>,
    "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>[ <a href="sourceportrangedefinition.md">SourcePortRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#max" title="Max">Max</a>: <i>Double</i>
<a href="#min" title="Min">Min</a>: <i>Double</i>
<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>
      - <a href="sourceportrangedefinition.md">SourcePortRangeDefinition</a></i>
</pre>

## Properties

#### Max

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Min

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

_Required_: No

_Type_: List of <a href="sourceportrangedefinition.md">SourcePortRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

