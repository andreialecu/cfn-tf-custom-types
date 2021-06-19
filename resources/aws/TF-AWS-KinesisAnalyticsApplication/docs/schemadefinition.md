# TF::AWS::KinesisAnalyticsApplication SchemaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#recordencoding" title="RecordEncoding">RecordEncoding</a>" : <i>String</i>,
    "<a href="#recordcolumns" title="RecordColumns">RecordColumns</a>" : <i>[ <a href="recordcolumnsdefinition.md">RecordColumnsDefinition</a>, ... ]</i>,
    "<a href="#recordformat" title="RecordFormat">RecordFormat</a>" : <i>[ <a href="recordformatdefinition.md">RecordFormatDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#recordencoding" title="RecordEncoding">RecordEncoding</a>: <i>String</i>
<a href="#recordcolumns" title="RecordColumns">RecordColumns</a>: <i>
      - <a href="recordcolumnsdefinition.md">RecordColumnsDefinition</a></i>
<a href="#recordformat" title="RecordFormat">RecordFormat</a>: <i>
      - <a href="recordformatdefinition.md">RecordFormatDefinition</a></i>
</pre>

## Properties

#### RecordEncoding

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordColumns

_Required_: No

_Type_: List of <a href="recordcolumnsdefinition.md">RecordColumnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFormat

_Required_: No

_Type_: List of <a href="recordformatdefinition.md">RecordFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

