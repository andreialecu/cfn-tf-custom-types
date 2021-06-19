# TF::Packet::DeviceNetworkType

This resource controls network type of Equinix Metal devices.

To learn more about Layer 2 networking in Equinix Metal, refer to

* <https://metal.equinix.com/developers/docs/networking/layer2/>
* <https://metal.equinix.com/developers/docs/networking/layer2-configs/>

If you are attaching VLAN to a device (i.e. using packet_port_vlan_attachment), link the device ID from this resource, in order to make the port attachment implicitly dependent on the state of the network type. If you link the device ID from the packet_device resource, Terraform will not wait for the network type change. See examples in [packet_port_vlan_attachment](port_vlan_attachment).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Packet::DeviceNetworkType",
    "Properties" : {
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Packet::DeviceNetworkType
Properties:
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### DeviceId

The ID of the device on which the network type should be set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Network type to set. Must be one of `layer3`, `hybrid`, `layer2-individual` and `layer2-bonded`.

_Required_: Yes

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

