# TF::AzureRM::AutomationModule ModuleLinkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#hash" title="Hash">Hash</a>" : <i>[ <a href="hashdefinition.md">HashDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#hash" title="Hash">Hash</a>: <i>
      - <a href="hashdefinition.md">HashDefinition</a></i>
</pre>

## Properties

#### Uri

The uri of the module content (zip or nupkg).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hash

_Required_: No

_Type_: List of <a href="hashdefinition.md">HashDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

