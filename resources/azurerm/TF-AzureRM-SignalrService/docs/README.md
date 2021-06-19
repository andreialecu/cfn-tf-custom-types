# TF::AzureRM::SignalrService

Manages an Azure SignalR service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SignalrService",
    "Properties" : {
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="corsdefinition.md">CorsDefinition</a>, ... ]</i>,
        "<a href="#features" title="Features">Features</a>" : <i>[ <a href="featuresdefinition.md">FeaturesDefinition</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="skudefinition.md">SkuDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#upstreamendpoint" title="UpstreamEndpoint">UpstreamEndpoint</a>" : <i>[ <a href="upstreamendpointdefinition.md">UpstreamEndpointDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SignalrService
Properties:
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="corsdefinition.md">CorsDefinition</a></i>
    <a href="#features" title="Features">Features</a>: <i>
      - <a href="featuresdefinition.md">FeaturesDefinition</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="skudefinition.md">SkuDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#upstreamendpoint" title="UpstreamEndpoint">UpstreamEndpoint</a>: <i>
      - <a href="upstreamendpointdefinition.md">UpstreamEndpointDefinition</a></i>
</pre>

## Properties

#### Location

Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the SignalR service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="corsdefinition.md">CorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Features

_Required_: No

_Type_: List of <a href="featuresdefinition.md">FeaturesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="skudefinition.md">SkuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamEndpoint

_Required_: No

_Type_: List of <a href="upstreamendpointdefinition.md">UpstreamEndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Hostname

Returns the <code>Hostname</code> value.

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### PrimaryAccessKey

Returns the <code>PrimaryAccessKey</code> value.

#### PrimaryConnectionString

Returns the <code>PrimaryConnectionString</code> value.

#### PublicPort

Returns the <code>PublicPort</code> value.

#### SecondaryAccessKey

Returns the <code>SecondaryAccessKey</code> value.

#### SecondaryConnectionString

Returns the <code>SecondaryConnectionString</code> value.

#### ServerPort

Returns the <code>ServerPort</code> value.

