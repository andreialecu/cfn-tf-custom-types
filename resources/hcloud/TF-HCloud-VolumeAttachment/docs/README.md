# TF::HCloud::VolumeAttachment

Provides a Hetzner Cloud Volume attachment to attach a Volume to a Hetzner Cloud Server. Deleting a Volume Attachment will detach the Volume from the Server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCloud::VolumeAttachment",
    "Properties" : {
        "<a href="#automount" title="Automount">Automount</a>" : <i>Boolean</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCloud::VolumeAttachment
Properties:
    <a href="#automount" title="Automount">Automount</a>: <i>Boolean</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>Double</i>
</pre>

## Properties

#### Automount

Automount the volume upon attaching it.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

Server to attach the Volume to.
- `automount` - (Optional, bool) Automount the volume upon attaching it.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

ID of the Volume.
- `server_id` - (Required, int) Server to attach the Volume to.
- `automount` - (Optional, bool) Automount the volume upon attaching it.

_Required_: Yes

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

