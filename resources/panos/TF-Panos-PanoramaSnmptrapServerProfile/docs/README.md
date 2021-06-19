# TF::Panos::PanoramaSnmptrapServerProfile

This resource allows you to add/update/delete Panorama snmptrap server profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaSnmptrapServerProfile",
    "Properties" : {
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#v2cserver" title="V2cServer">V2cServer</a>" : <i>[ <a href="v2cserverdefinition.md">V2cServerDefinition</a>, ... ]</i>,
        "<a href="#v3server" title="V3Server">V3Server</a>" : <i>[ <a href="v3serverdefinition.md">V3ServerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaSnmptrapServerProfile
Properties:
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#v2cserver" title="V2cServer">V2cServer</a>: <i>
      - <a href="v2cserverdefinition.md">V2cServerDefinition</a></i>
    <a href="#v3server" title="V3Server">V3Server</a>: <i>
      - <a href="v3serverdefinition.md">V3ServerDefinition</a></i>
</pre>

## Properties

#### DeviceGroup

The device group location.  Mutually exclusive with
`template` and `template_stack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The group's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template location.  Mutually exclusive with
`template_stack` and `device_group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack location.  Mutually exclusive
with `template` and `device_group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys.  This will likely be `shared`, and it should be
defined if you specified either `template` or `template_stack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V2cServer

_Required_: No

_Type_: List of <a href="v2cserverdefinition.md">V2cServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V3Server

_Required_: No

_Type_: List of <a href="v3serverdefinition.md">V3ServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AuthPasswordEnc

Returns the <code>AuthPasswordEnc</code> value.

#### AuthPasswordRaw

Returns the <code>AuthPasswordRaw</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivPasswordEnc

Returns the <code>PrivPasswordEnc</code> value.

#### PrivPasswordRaw

Returns the <code>PrivPasswordRaw</code> value.

