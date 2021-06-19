# TF::GoogleBeta::GoogleBigqueryTable ExternalDataConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autodetect" title="Autodetect">Autodetect</a>" : <i>Boolean</i>,
    "<a href="#compression" title="Compression">Compression</a>" : <i>String</i>,
    "<a href="#ignoreunknownvalues" title="IgnoreUnknownValues">IgnoreUnknownValues</a>" : <i>Boolean</i>,
    "<a href="#maxbadrecords" title="MaxBadRecords">MaxBadRecords</a>" : <i>Double</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>String</i>,
    "<a href="#sourceformat" title="SourceFormat">SourceFormat</a>" : <i>String</i>,
    "<a href="#sourceuris" title="SourceUris">SourceUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#csvoptions" title="CsvOptions">CsvOptions</a>" : <i>[ <a href="csvoptionsdefinition.md">CsvOptionsDefinition</a>, ... ]</i>,
    "<a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>" : <i>[ <a href="googlesheetsoptionsdefinition.md">GoogleSheetsOptionsDefinition</a>, ... ]</i>,
    "<a href="#hivepartitioningoptions" title="HivePartitioningOptions">HivePartitioningOptions</a>" : <i>[ <a href="hivepartitioningoptionsdefinition.md">HivePartitioningOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autodetect" title="Autodetect">Autodetect</a>: <i>Boolean</i>
<a href="#compression" title="Compression">Compression</a>: <i>String</i>
<a href="#ignoreunknownvalues" title="IgnoreUnknownValues">IgnoreUnknownValues</a>: <i>Boolean</i>
<a href="#maxbadrecords" title="MaxBadRecords">MaxBadRecords</a>: <i>Double</i>
<a href="#schema" title="Schema">Schema</a>: <i>String</i>
<a href="#sourceformat" title="SourceFormat">SourceFormat</a>: <i>String</i>
<a href="#sourceuris" title="SourceUris">SourceUris</a>: <i>
      - String</i>
<a href="#csvoptions" title="CsvOptions">CsvOptions</a>: <i>
      - <a href="csvoptionsdefinition.md">CsvOptionsDefinition</a></i>
<a href="#googlesheetsoptions" title="GoogleSheetsOptions">GoogleSheetsOptions</a>: <i>
      - <a href="googlesheetsoptionsdefinition.md">GoogleSheetsOptionsDefinition</a></i>
<a href="#hivepartitioningoptions" title="HivePartitioningOptions">HivePartitioningOptions</a>: <i>
      - <a href="hivepartitioningoptionsdefinition.md">HivePartitioningOptionsDefinition</a></i>
</pre>

## Properties

#### Autodetect

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreUnknownValues

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBadRecords

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFormat

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUris

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvOptions

_Required_: No

_Type_: List of <a href="csvoptionsdefinition.md">CsvOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleSheetsOptions

_Required_: No

_Type_: List of <a href="googlesheetsoptionsdefinition.md">GoogleSheetsOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HivePartitioningOptions

_Required_: No

_Type_: List of <a href="hivepartitioningoptionsdefinition.md">HivePartitioningOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

