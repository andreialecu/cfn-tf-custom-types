# TF::AzureRM::KeyVaultCertificate SubjectAlternativeNamesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsnames" title="DnsNames">DnsNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#emails" title="Emails">Emails</a>" : <i>[ String, ... ]</i>,
    "<a href="#upns" title="Upns">Upns</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsnames" title="DnsNames">DnsNames</a>: <i>
      - String</i>
<a href="#emails" title="Emails">Emails</a>: <i>
      - String</i>
<a href="#upns" title="Upns">Upns</a>: <i>
      - String</i>
</pre>

## Properties

#### DnsNames

A list of alternative DNS names (FQDNs) identified by the Certificate. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Emails

A list of email addresses identified by this Certificate. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upns

A list of User Principal Names identified by the Certificate. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

