# TF::AzureRM::KubernetesCluster OmsAgentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#loganalyticsworkspaceid" title="LogAnalyticsWorkspaceId">LogAnalyticsWorkspaceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#loganalyticsworkspaceid" title="LogAnalyticsWorkspaceId">LogAnalyticsWorkspaceId</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Is the OMS Agent Enabled?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAnalyticsWorkspaceId

The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if `enabled` is `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

