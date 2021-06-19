# TF::AzureRM::PointToSiteVpnGateway VpnClientAddressPoolDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>: <i>
      - String</i>
</pre>

## Properties

#### AddressPrefixes

A list of CIDR Ranges which should be used as Address Prefixes.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

