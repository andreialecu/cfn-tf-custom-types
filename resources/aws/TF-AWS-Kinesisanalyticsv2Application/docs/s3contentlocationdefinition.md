# TF::AWS::Kinesisanalyticsv2Application S3ContentLocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketarn" title="BucketArn">BucketArn</a>" : <i>String</i>,
    "<a href="#filekey" title="FileKey">FileKey</a>" : <i>String</i>,
    "<a href="#objectversion" title="ObjectVersion">ObjectVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bucketarn" title="BucketArn">BucketArn</a>: <i>String</i>
<a href="#filekey" title="FileKey">FileKey</a>: <i>String</i>
<a href="#objectversion" title="ObjectVersion">ObjectVersion</a>: <i>String</i>
</pre>

## Properties

#### BucketArn

The ARN for the S3 bucket containing the application code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileKey

The file key for the object containing the application code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectVersion

The version of the object containing the application code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

