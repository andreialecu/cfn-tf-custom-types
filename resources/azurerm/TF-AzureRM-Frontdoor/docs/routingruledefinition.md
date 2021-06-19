# TF::AzureRM::Frontdoor RoutingRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptedprotocols" title="AcceptedProtocols">AcceptedProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#frontendendpoints" title="FrontendEndpoints">FrontendEndpoints</a>" : <i>[ <a href="frontendendpointsdefinition.md">FrontendEndpointsDefinition</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#patternstomatch" title="PatternsToMatch">PatternsToMatch</a>" : <i>[ String, ... ]</i>,
    "<a href="#forwardingconfiguration" title="ForwardingConfiguration">ForwardingConfiguration</a>" : <i>[ <a href="forwardingconfigurationdefinition.md">ForwardingConfigurationDefinition</a>, ... ]</i>,
    "<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>" : <i>[ <a href="redirectconfigurationdefinition.md">RedirectConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acceptedprotocols" title="AcceptedProtocols">AcceptedProtocols</a>: <i>
      - String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#frontendendpoints" title="FrontendEndpoints">FrontendEndpoints</a>: <i>
      - <a href="frontendendpointsdefinition.md">FrontendEndpointsDefinition</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#patternstomatch" title="PatternsToMatch">PatternsToMatch</a>: <i>
      - String</i>
<a href="#forwardingconfiguration" title="ForwardingConfiguration">ForwardingConfiguration</a>: <i>
      - <a href="forwardingconfigurationdefinition.md">ForwardingConfigurationDefinition</a></i>
<a href="#redirectconfiguration" title="RedirectConfiguration">RedirectConfiguration</a>: <i>
      - <a href="redirectconfigurationdefinition.md">RedirectConfigurationDefinition</a></i>
</pre>

## Properties

#### AcceptedProtocols

Protocol schemes to match for the Backend Routing Rule. Defaults to `Http`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

`Enable` or `Disable` use of this Backend Routing Rule. Permitted values are `true` or `false`. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendEndpoints

_Required_: Yes

_Type_: List of <a href="frontendendpointsdefinition.md">FrontendEndpointsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Routing Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatternsToMatch

The route patterns for the Backend Routing Rule. Defaults to `/*`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingConfiguration

_Required_: No

_Type_: List of <a href="forwardingconfigurationdefinition.md">ForwardingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfiguration

_Required_: No

_Type_: List of <a href="redirectconfigurationdefinition.md">RedirectConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

