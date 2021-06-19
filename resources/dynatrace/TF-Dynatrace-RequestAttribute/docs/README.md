# TF::Dynatrace::RequestAttribute

CloudFormation equivalent of dynatrace_request_attribute

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::RequestAttribute",
    "Properties" : {
        "<a href="#aggregation" title="Aggregation">Aggregation</a>" : <i>String</i>,
        "<a href="#confidential" title="Confidential">Confidential</a>" : <i>Boolean</i>,
        "<a href="#datatype" title="DataType">DataType</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#normalization" title="Normalization">Normalization</a>" : <i>String</i>,
        "<a href="#skippersonaldatamasking" title="SkipPersonalDataMasking">SkipPersonalDataMasking</a>" : <i>Boolean</i>,
        "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
        "<a href="#datasources" title="DataSources">DataSources</a>" : <i>[ <a href="datasourcesdefinition.md">DataSourcesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::RequestAttribute
Properties:
    <a href="#aggregation" title="Aggregation">Aggregation</a>: <i>String</i>
    <a href="#confidential" title="Confidential">Confidential</a>: <i>Boolean</i>
    <a href="#datatype" title="DataType">DataType</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#normalization" title="Normalization">Normalization</a>: <i>String</i>
    <a href="#skippersonaldatamasking" title="SkipPersonalDataMasking">SkipPersonalDataMasking</a>: <i>Boolean</i>
    <a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
    <a href="#datasources" title="DataSources">DataSources</a>: <i>
      - <a href="datasourcesdefinition.md">DataSourcesDefinition</a></i>
</pre>

## Properties

#### Aggregation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Confidential

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Normalization

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipPersonalDataMasking

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSources

_Required_: No

_Type_: List of <a href="datasourcesdefinition.md">DataSourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

