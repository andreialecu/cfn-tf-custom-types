# TF::AWS::SsmAssociation OutputLocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>" : <i>String</i>,
    "<a href="#s3keyprefix" title="S3KeyPrefix">S3KeyPrefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>: <i>String</i>
<a href="#s3keyprefix" title="S3KeyPrefix">S3KeyPrefix</a>: <i>String</i>
</pre>

## Properties

#### S3BucketName

The S3 bucket name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3KeyPrefix

The S3 bucket prefix. Results stored in the root if not configured.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

