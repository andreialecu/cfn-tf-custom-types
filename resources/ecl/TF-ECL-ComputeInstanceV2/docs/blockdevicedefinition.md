# TF::ECL::ComputeInstanceV2 BlockDeviceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bootindex" title="BootIndex">BootIndex</a>" : <i>Double</i>,
    "<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>" : <i>Boolean</i>,
    "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#bootindex" title="BootIndex">BootIndex</a>: <i>Double</i>
<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>: <i>Boolean</i>
<a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>Double</i>
</pre>

## Properties

#### BootIndex

The boot index of the volume. It defaults to 0.
Changing this creates a new server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteOnTermination

Delete the volume / block device upon
termination of the instance. Defaults to false. Changing this creates a
new server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

The type that gets created. Possible values
are "volume" and "local". Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

The source type of the device. Must be one of
"blank", "image", "volume", or "snapshot". Changing this creates a new
server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

The UUID of
the image, volume, or snapshot. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

The size of the volume to create (in gigabytes). Required
in the following combinations: source=image and destination=volume,
source=blank and destination=local, and source=blank and destination=volume.
Changing this creates a new server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

