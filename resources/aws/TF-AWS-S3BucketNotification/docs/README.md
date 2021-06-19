# TF::AWS::S3BucketNotification

Manages a S3 Bucket Notification Configuration. For additional information, see the [Configuring S3 Event Notifications section in the Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html).

~> **NOTE:** S3 Buckets only support a single notification configuration. Declaring multiple `aws_s3_bucket_notification` resources to the same S3 Bucket will cause a perpetual difference in configuration. See the example "Trigger multiple Lambda functions" for an option.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::S3BucketNotification",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#lambdafunction" title="LambdaFunction">LambdaFunction</a>" : <i>[ <a href="lambdafunctiondefinition.md">LambdaFunctionDefinition</a>, ... ]</i>,
        "<a href="#queue" title="Queue">Queue</a>" : <i>[ <a href="queuedefinition.md">QueueDefinition</a>, ... ]</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>[ <a href="topicdefinition.md">TopicDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::S3BucketNotification
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#lambdafunction" title="LambdaFunction">LambdaFunction</a>: <i>
      - <a href="lambdafunctiondefinition.md">LambdaFunctionDefinition</a></i>
    <a href="#queue" title="Queue">Queue</a>: <i>
      - <a href="queuedefinition.md">QueueDefinition</a></i>
    <a href="#topic" title="Topic">Topic</a>: <i>
      - <a href="topicdefinition.md">TopicDefinition</a></i>
</pre>

## Properties

#### Bucket

The name of the bucket to put notification configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunction

_Required_: No

_Type_: List of <a href="lambdafunctiondefinition.md">LambdaFunctionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Queue

_Required_: No

_Type_: List of <a href="queuedefinition.md">QueueDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: No

_Type_: List of <a href="topicdefinition.md">TopicDefinition</a>

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

