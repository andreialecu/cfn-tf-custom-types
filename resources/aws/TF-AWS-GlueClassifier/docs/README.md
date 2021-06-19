# TF::AWS::GlueClassifier

Provides a Glue Classifier resource.

~> **NOTE:** It is only valid to create one type of classifier (csv, grok, JSON, or XML). Changing classifier types will recreate the classifier.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GlueClassifier",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#csvclassifier" title="CsvClassifier">CsvClassifier</a>" : <i>[ <a href="csvclassifierdefinition.md">CsvClassifierDefinition</a>, ... ]</i>,
        "<a href="#grokclassifier" title="GrokClassifier">GrokClassifier</a>" : <i>[ <a href="grokclassifierdefinition.md">GrokClassifierDefinition</a>, ... ]</i>,
        "<a href="#jsonclassifier" title="JsonClassifier">JsonClassifier</a>" : <i>[ <a href="jsonclassifierdefinition.md">JsonClassifierDefinition</a>, ... ]</i>,
        "<a href="#xmlclassifier" title="XmlClassifier">XmlClassifier</a>" : <i>[ <a href="xmlclassifierdefinition.md">XmlClassifierDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GlueClassifier
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#csvclassifier" title="CsvClassifier">CsvClassifier</a>: <i>
      - <a href="csvclassifierdefinition.md">CsvClassifierDefinition</a></i>
    <a href="#grokclassifier" title="GrokClassifier">GrokClassifier</a>: <i>
      - <a href="grokclassifierdefinition.md">GrokClassifierDefinition</a></i>
    <a href="#jsonclassifier" title="JsonClassifier">JsonClassifier</a>: <i>
      - <a href="jsonclassifierdefinition.md">JsonClassifierDefinition</a></i>
    <a href="#xmlclassifier" title="XmlClassifier">XmlClassifier</a>: <i>
      - <a href="xmlclassifierdefinition.md">XmlClassifierDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsvClassifier

_Required_: No

_Type_: List of <a href="csvclassifierdefinition.md">CsvClassifierDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrokClassifier

_Required_: No

_Type_: List of <a href="grokclassifierdefinition.md">GrokClassifierDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonClassifier

_Required_: No

_Type_: List of <a href="jsonclassifierdefinition.md">JsonClassifierDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XmlClassifier

_Required_: No

_Type_: List of <a href="xmlclassifierdefinition.md">XmlClassifierDefinition</a>

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

