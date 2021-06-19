# TF::AzureRM::HdinsightHadoopCluster EdgeNodeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>" : <i>Double</i>,
    "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
    "<a href="#installscriptaction" title="InstallScriptAction">InstallScriptAction</a>" : <i>[ <a href="installscriptactiondefinition.md">InstallScriptActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>: <i>Double</i>
<a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
<a href="#installscriptaction" title="InstallScriptAction">InstallScriptAction</a>: <i>
      - <a href="installscriptactiondefinition.md">InstallScriptActionDefinition</a></i>
</pre>

## Properties

#### TargetInstanceCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

The Size of the Virtual Machine which should be used as the Edge Nodes. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallScriptAction

_Required_: No

_Type_: List of <a href="installscriptactiondefinition.md">InstallScriptActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

