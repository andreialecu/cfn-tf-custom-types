# TF::AzureRM::VirtualMachine VaultCertificatesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatestore" title="CertificateStore">CertificateStore</a>" : <i>String</i>,
    "<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificatestore" title="CertificateStore">CertificateStore</a>: <i>String</i>
<a href="#certificateurl" title="CertificateUrl">CertificateUrl</a>: <i>String</i>
</pre>

## Properties

#### CertificateStore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateUrl

The ID of the Key Vault Secret. Stored secret is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be:.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

