# TF::AzureRM::VpnServerConfiguration RadiusServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>String</i>,
    "<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>" : <i>[ <a href="clientrootcertificatedefinition.md">ClientRootCertificateDefinition</a>, ... ]</i>,
    "<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>" : <i>[ <a href="serverrootcertificatedefinition.md">ServerRootCertificateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#secret" title="Secret">Secret</a>: <i>String</i>
<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>: <i>
      - <a href="clientrootcertificatedefinition.md">ClientRootCertificateDefinition</a></i>
<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>: <i>
      - <a href="serverrootcertificatedefinition.md">ServerRootCertificateDefinition</a></i>
</pre>

## Properties

#### Address

The Address of the Radius Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

The Secret used to communicate with the Radius Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRootCertificate

_Required_: No

_Type_: List of <a href="clientrootcertificatedefinition.md">ClientRootCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRootCertificate

_Required_: No

_Type_: List of <a href="serverrootcertificatedefinition.md">ServerRootCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

