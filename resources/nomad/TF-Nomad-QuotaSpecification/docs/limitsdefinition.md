# TF::Nomad::QuotaSpecification LimitsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#regionlimit" title="RegionLimit">RegionLimit</a>" : <i>[ <a href="regionlimitdefinition.md">RegionLimitDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#regionlimit" title="RegionLimit">RegionLimit</a>: <i>
      - <a href="regionlimitdefinition.md">RegionLimitDefinition</a></i>
</pre>

## Properties

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionLimit

_Required_: No

_Type_: List of <a href="regionlimitdefinition.md">RegionLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

