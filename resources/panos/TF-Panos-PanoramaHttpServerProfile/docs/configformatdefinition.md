# TF::Panos::PanoramaHttpServerProfile ConfigFormatDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#params" title="Params">Params</a>" : <i>[ <a href="paramsdefinition.md">ParamsDefinition</a>, ... ]</i>,
    "<a href="#payload" title="Payload">Payload</a>" : <i>String</i>,
    "<a href="#uriformat" title="UriFormat">UriFormat</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#params" title="Params">Params</a>: <i>
      - <a href="paramsdefinition.md">ParamsDefinition</a></i>
<a href="#payload" title="Payload">Payload</a>: <i>String</i>
<a href="#uriformat" title="UriFormat">UriFormat</a>: <i>String</i>
</pre>

## Properties

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Params

_Required_: No

_Type_: List of <a href="paramsdefinition.md">ParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Payload

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

