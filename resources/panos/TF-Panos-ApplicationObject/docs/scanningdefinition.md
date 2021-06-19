# TF::Panos::ApplicationObject ScanningDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datapatterns" title="DataPatterns">DataPatterns</a>" : <i>Boolean</i>,
    "<a href="#filetypes" title="FileTypes">FileTypes</a>" : <i>Boolean</i>,
    "<a href="#viruses" title="Viruses">Viruses</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#datapatterns" title="DataPatterns">DataPatterns</a>: <i>Boolean</i>
<a href="#filetypes" title="FileTypes">FileTypes</a>: <i>Boolean</i>
<a href="#viruses" title="Viruses">Viruses</a>: <i>Boolean</i>
</pre>

## Properties

#### DataPatterns

Data pattern scanning.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTypes

File type scanning.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Viruses

Virus scanning.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

