# TF::Google::DataLossPreventionJobTrigger RegexFileSetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#excluderegex" title="ExcludeRegex">ExcludeRegex</a>" : <i>[ String, ... ]</i>,
    "<a href="#includeregex" title="IncludeRegex">IncludeRegex</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#excluderegex" title="ExcludeRegex">ExcludeRegex</a>: <i>
      - String</i>
<a href="#includeregex" title="IncludeRegex">IncludeRegex</a>: <i>
      - String</i>
</pre>

## Properties

#### BucketName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeRegex

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeRegex

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

