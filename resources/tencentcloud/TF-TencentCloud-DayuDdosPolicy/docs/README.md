# TF::TencentCloud::DayuDdosPolicy

Use this resource to create dayu DDoS policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::DayuDdosPolicy",
    "Properties" : {
        "<a href="#blackips" title="BlackIps">BlackIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#whiteips" title="WhiteIps">WhiteIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#dropoptions" title="DropOptions">DropOptions</a>" : <i>[ <a href="dropoptionsdefinition.md">DropOptionsDefinition</a>, ... ]</i>,
        "<a href="#packetfilters" title="PacketFilters">PacketFilters</a>" : <i>[ <a href="packetfiltersdefinition.md">PacketFiltersDefinition</a>, ... ]</i>,
        "<a href="#portfilters" title="PortFilters">PortFilters</a>" : <i>[ <a href="portfiltersdefinition.md">PortFiltersDefinition</a>, ... ]</i>,
        "<a href="#watermarkfilters" title="WatermarkFilters">WatermarkFilters</a>" : <i>[ <a href="watermarkfiltersdefinition.md">WatermarkFiltersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::DayuDdosPolicy
Properties:
    <a href="#blackips" title="BlackIps">BlackIps</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#whiteips" title="WhiteIps">WhiteIps</a>: <i>
      - String</i>
    <a href="#dropoptions" title="DropOptions">DropOptions</a>: <i>
      - <a href="dropoptionsdefinition.md">DropOptionsDefinition</a></i>
    <a href="#packetfilters" title="PacketFilters">PacketFilters</a>: <i>
      - <a href="packetfiltersdefinition.md">PacketFiltersDefinition</a></i>
    <a href="#portfilters" title="PortFilters">PortFilters</a>: <i>
      - <a href="portfiltersdefinition.md">PortFiltersDefinition</a></i>
    <a href="#watermarkfilters" title="WatermarkFilters">WatermarkFilters</a>: <i>
      - <a href="watermarkfiltersdefinition.md">WatermarkFiltersDefinition</a></i>
</pre>

## Properties

#### BlackIps

Black IP list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the DDoS policy. Length should between 1 and 32.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Type of the resource that the DDoS policy works for. Valid values: `bgpip`, `bgp`, `bgp-multip` and `net`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhiteIps

White IP list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropOptions

_Required_: No

_Type_: List of <a href="dropoptionsdefinition.md">DropOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketFilters

_Required_: No

_Type_: List of <a href="packetfiltersdefinition.md">PacketFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortFilters

_Required_: No

_Type_: List of <a href="portfiltersdefinition.md">PortFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkFilters

_Required_: No

_Type_: List of <a href="watermarkfiltersdefinition.md">WatermarkFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### PolicyId

Returns the <code>PolicyId</code> value.

#### SceneId

Returns the <code>SceneId</code> value.

#### WatermarkKey

Returns the <code>WatermarkKey</code> value.

