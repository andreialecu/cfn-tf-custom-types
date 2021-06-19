# TF::Thunder::SlbTemplateImapPop3

`thunder_slb_template_imap_pop3` provides details about slb template imap-pop3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateImapPop3",
    "Properties" : {
        "<a href="#logindisabled" title="Logindisabled">Logindisabled</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#starttls" title="Starttls">Starttls</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateImapPop3
Properties:
    <a href="#logindisabled" title="Logindisabled">Logindisabled</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#starttls" title="Starttls">Starttls</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### Logindisabled

Disable Login before STARTTLS.Works only for imap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

IMAP-POP3 Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Starttls

'disabled’: Disable STARTTLS; 'optional’: STARTTLS is optional requirement; 'enforced’: Must issue STARTTLS command before imap transaction;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

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

