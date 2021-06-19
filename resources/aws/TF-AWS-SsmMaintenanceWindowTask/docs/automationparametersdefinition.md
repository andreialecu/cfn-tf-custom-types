# TF::AWS::SsmMaintenanceWindowTask AutomationParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#documentversion" title="DocumentVersion">DocumentVersion</a>" : <i>String</i>,
    "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ <a href="parameterdefinition.md">ParameterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#documentversion" title="DocumentVersion">DocumentVersion</a>: <i>String</i>
<a href="#parameter" title="Parameter">Parameter</a>: <i>
      - <a href="parameterdefinition.md">ParameterDefinition</a></i>
</pre>

## Properties

#### DocumentVersion

The version of an Automation document to use during task execution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No

_Type_: List of <a href="parameterdefinition.md">ParameterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

