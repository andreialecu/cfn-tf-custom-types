# TF::Vault::AwsAuthBackendIdentityWhitelist

Configures the periodic tidying operation of the whitelisted identity entries.

For more information, see the
[Vault docs](https://www.vaultproject.io/api-docs/auth/aws#configure-identity-whitelist-tidy-operation).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vault::AwsAuthBackendIdentityWhitelist",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#disableperiodictidy" title="DisablePeriodicTidy">DisablePeriodicTidy</a>" : <i>Boolean</i>,
        "<a href="#safetybuffer" title="SafetyBuffer">SafetyBuffer</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vault::AwsAuthBackendIdentityWhitelist
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#disableperiodictidy" title="DisablePeriodicTidy">DisablePeriodicTidy</a>: <i>Boolean</i>
    <a href="#safetybuffer" title="SafetyBuffer">SafetyBuffer</a>: <i>Double</i>
</pre>

## Properties

#### Backend

The path of the AWS backend being configured.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePeriodicTidy

If set to true, disables the periodic
tidying of the identity-whitelist entries.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafetyBuffer

The amount of extra time, in minutes, that must
have passed beyond the roletag expiration, before it is removed from the
backend storage.

_Required_: No

_Type_: Double

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

