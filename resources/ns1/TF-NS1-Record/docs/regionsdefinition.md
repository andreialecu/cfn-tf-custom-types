# TF::NS1::Record RegionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="metadefinition.md">MetaDefinition</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="metadefinition.md">MetaDefinition</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Meta

_Required_: No

_Type_: List of <a href="metadefinition.md">MetaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

