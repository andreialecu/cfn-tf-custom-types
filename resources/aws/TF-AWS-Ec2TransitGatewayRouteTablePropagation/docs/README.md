# TF::AWS::Ec2TransitGatewayRouteTablePropagation

Manages an EC2 Transit Gateway Route Table propagation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Ec2TransitGatewayRouteTablePropagation",
    "Properties" : {
        "<a href="#transitgatewayattachmentid" title="TransitGatewayAttachmentId">TransitGatewayAttachmentId</a>" : <i>String</i>,
        "<a href="#transitgatewayroutetableid" title="TransitGatewayRouteTableId">TransitGatewayRouteTableId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Ec2TransitGatewayRouteTablePropagation
Properties:
    <a href="#transitgatewayattachmentid" title="TransitGatewayAttachmentId">TransitGatewayAttachmentId</a>: <i>String</i>
    <a href="#transitgatewayroutetableid" title="TransitGatewayRouteTableId">TransitGatewayRouteTableId</a>: <i>String</i>
</pre>

## Properties

#### TransitGatewayAttachmentId

Identifier of EC2 Transit Gateway Attachment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayRouteTableId

Identifier of EC2 Transit Gateway Route Table.

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

#### ResourceId

Returns the <code>ResourceId</code> value.

#### ResourceType

Returns the <code>ResourceType</code> value.

