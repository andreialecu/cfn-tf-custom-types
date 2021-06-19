# TF::AWS::WorklinkFleet

CloudFormation equivalent of aws_worklink_fleet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::WorklinkFleet",
    "Properties" : {
        "<a href="#auditstreamarn" title="AuditStreamArn">AuditStreamArn</a>" : <i>String</i>,
        "<a href="#devicecacertificate" title="DeviceCaCertificate">DeviceCaCertificate</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#optimizeforenduserlocation" title="OptimizeForEndUserLocation">OptimizeForEndUserLocation</a>" : <i>Boolean</i>,
        "<a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>" : <i>[ <a href="identityproviderdefinition.md">IdentityProviderDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::WorklinkFleet
Properties:
    <a href="#auditstreamarn" title="AuditStreamArn">AuditStreamArn</a>: <i>String</i>
    <a href="#devicecacertificate" title="DeviceCaCertificate">DeviceCaCertificate</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#optimizeforenduserlocation" title="OptimizeForEndUserLocation">OptimizeForEndUserLocation</a>: <i>Boolean</i>
    <a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>: <i>
      - <a href="identityproviderdefinition.md">IdentityProviderDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
</pre>

## Properties

#### AuditStreamArn

The ARN of the Amazon Kinesis data stream that receives the audit events. Kinesis data stream name must begin with `"AmazonWorkLink-"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceCaCertificate

The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The name of the fleet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A region-unique name for the AMI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizeForEndUserLocation

The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityProvider

_Required_: No

_Type_: List of <a href="identityproviderdefinition.md">IdentityProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CompanyCode

Returns the <code>CompanyCode</code> value.

#### CreatedTime

Returns the <code>CreatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdatedTime

Returns the <code>LastUpdatedTime</code> value.

