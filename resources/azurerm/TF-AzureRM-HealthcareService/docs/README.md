# TF::AzureRM::HealthcareService

Manages a Healthcare Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::HealthcareService",
    "Properties" : {
        "<a href="#accesspolicyobjectids" title="AccessPolicyObjectIds">AccessPolicyObjectIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#cosmosdbkeyvaultkeyversionlessid" title="CosmosdbKeyVaultKeyVersionlessId">CosmosdbKeyVaultKeyVersionlessId</a>" : <i>String</i>,
        "<a href="#cosmosdbthroughput" title="CosmosdbThroughput">CosmosdbThroughput</a>" : <i>Double</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#authenticationconfiguration" title="AuthenticationConfiguration">AuthenticationConfiguration</a>" : <i>[ <a href="authenticationconfigurationdefinition.md">AuthenticationConfigurationDefinition</a>, ... ]</i>,
        "<a href="#corsconfiguration" title="CorsConfiguration">CorsConfiguration</a>" : <i>[ <a href="corsconfigurationdefinition.md">CorsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::HealthcareService
Properties:
    <a href="#accesspolicyobjectids" title="AccessPolicyObjectIds">AccessPolicyObjectIds</a>: <i>
      - String</i>
    <a href="#cosmosdbkeyvaultkeyversionlessid" title="CosmosdbKeyVaultKeyVersionlessId">CosmosdbKeyVaultKeyVersionlessId</a>: <i>String</i>
    <a href="#cosmosdbthroughput" title="CosmosdbThroughput">CosmosdbThroughput</a>: <i>Double</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#authenticationconfiguration" title="AuthenticationConfiguration">AuthenticationConfiguration</a>: <i>
      - <a href="authenticationconfigurationdefinition.md">AuthenticationConfigurationDefinition</a></i>
    <a href="#corsconfiguration" title="CorsConfiguration">CorsConfiguration</a>: <i>
      - <a href="corsconfigurationdefinition.md">CorsConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessPolicyObjectIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbKeyVaultKeyVersionlessId

A versionless Key Vault Key ID for CMK encryption of the backing database. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosmosdbThroughput

The provisioned throughput for the backing database. Range of `400`-`1000`. Defaults to `400`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

The type of the service. Values at time of publication are: `fhir`, `fhir-Stu3` and `fhir-R4`. Default value is `fhir`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure Region where the Service should be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the service instance. Used for service endpoint, must be unique within the audience.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicNetworkAccessEnabled

Whether public network access is enabled or disabled for this service instance.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which to create the Service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationConfiguration

_Required_: No

_Type_: List of <a href="authenticationconfigurationdefinition.md">AuthenticationConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsConfiguration

_Required_: No

_Type_: List of <a href="corsconfigurationdefinition.md">CorsConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

