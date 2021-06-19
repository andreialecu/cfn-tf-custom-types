# TF::GoogleBeta::GoogleKmsCryptoKey

CloudFormation equivalent of google_kms_crypto_key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleKmsCryptoKey",
    "Properties" : {
        "<a href="#keyring" title="KeyRing">KeyRing</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#purpose" title="Purpose">Purpose</a>" : <i>String</i>,
        "<a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>" : <i>String</i>,
        "<a href="#skipinitialversioncreation" title="SkipInitialVersionCreation">SkipInitialVersionCreation</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#versiontemplate" title="VersionTemplate">VersionTemplate</a>" : <i>[ <a href="versiontemplatedefinition.md">VersionTemplateDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleKmsCryptoKey
Properties:
    <a href="#keyring" title="KeyRing">KeyRing</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#purpose" title="Purpose">Purpose</a>: <i>String</i>
    <a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>: <i>String</i>
    <a href="#skipinitialversioncreation" title="SkipInitialVersionCreation">SkipInitialVersionCreation</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#versiontemplate" title="VersionTemplate">VersionTemplate</a>: <i>
      - <a href="versiontemplatedefinition.md">VersionTemplateDefinition</a></i>
</pre>

## Properties

#### KeyRing

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Purpose

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipInitialVersionCreation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionTemplate

_Required_: No

_Type_: List of <a href="versiontemplatedefinition.md">VersionTemplateDefinition</a>

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

#### SelfLink

Returns the <code>SelfLink</code> value.

