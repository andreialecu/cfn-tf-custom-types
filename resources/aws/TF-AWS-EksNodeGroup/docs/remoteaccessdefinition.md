# TF::AWS::EksNodeGroup RemoteAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ec2sshkey" title="Ec2SshKey">Ec2SshKey</a>" : <i>String</i>,
    "<a href="#sourcesecuritygroupids" title="SourceSecurityGroupIds">SourceSecurityGroupIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ec2sshkey" title="Ec2SshKey">Ec2SshKey</a>: <i>String</i>
<a href="#sourcesecuritygroupids" title="SourceSecurityGroupIds">SourceSecurityGroupIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Ec2SshKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

