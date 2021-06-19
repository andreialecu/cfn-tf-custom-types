# TF::TencentCloud::CcnBandwidthLimit

Provides a resource to limit CCN bandwidth.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CcnBandwidthLimit",
    "Properties" : {
        "<a href="#bandwidthlimit" title="BandwidthLimit">BandwidthLimit</a>" : <i>Double</i>,
        "<a href="#ccnid" title="CcnId">CcnId</a>" : <i>String</i>,
        "<a href="#dstregion" title="DstRegion">DstRegion</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CcnBandwidthLimit
Properties:
    <a href="#bandwidthlimit" title="BandwidthLimit">BandwidthLimit</a>: <i>Double</i>
    <a href="#ccnid" title="CcnId">CcnId</a>: <i>String</i>
    <a href="#dstregion" title="DstRegion">DstRegion</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### BandwidthLimit

Limitation of bandwidth.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CcnId

ID of the CCN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstRegion

Destination area restriction. If the `CCN` rate limit type is `OUTER_REGION_LIMIT`, this value does not need to be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Limitation of region.

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

