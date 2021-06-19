# TF::AzureRM::ServiceFabricCluster CommonNamesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatecommonname" title="CertificateCommonName">CertificateCommonName</a>" : <i>String</i>,
    "<a href="#certificateissuerthumbprint" title="CertificateIssuerThumbprint">CertificateIssuerThumbprint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificatecommonname" title="CertificateCommonName">CertificateCommonName</a>: <i>String</i>
<a href="#certificateissuerthumbprint" title="CertificateIssuerThumbprint">CertificateIssuerThumbprint</a>: <i>String</i>
</pre>

## Properties

#### CertificateCommonName

The common or subject name of the certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateIssuerThumbprint

The Issuer Thumbprint of the Certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

