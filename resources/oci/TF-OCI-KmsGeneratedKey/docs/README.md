# TF::OCI::KmsGeneratedKey

This resource provides the Generated Key resource in Oracle Cloud Infrastructure Kms service.

Generates a key that you can use to encrypt or decrypt data.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::KmsGeneratedKey",
    "Properties" : {
        "<a href="#associateddata" title="AssociatedData">AssociatedData</a>" : <i>[ <a href="associateddatadefinition.md">AssociatedDataDefinition</a>, ... ]</i>,
        "<a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>" : <i>String</i>,
        "<a href="#includeplaintextkey" title="IncludePlaintextKey">IncludePlaintextKey</a>" : <i>Boolean</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#loggingcontext" title="LoggingContext">LoggingContext</a>" : <i>[ <a href="loggingcontextdefinition.md">LoggingContextDefinition</a>, ... ]</i>,
        "<a href="#keyshape" title="KeyShape">KeyShape</a>" : <i>[ <a href="keyshapedefinition.md">KeyShapeDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::KmsGeneratedKey
Properties:
    <a href="#associateddata" title="AssociatedData">AssociatedData</a>: <i>
      - <a href="associateddatadefinition.md">AssociatedDataDefinition</a></i>
    <a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>: <i>String</i>
    <a href="#includeplaintextkey" title="IncludePlaintextKey">IncludePlaintextKey</a>: <i>Boolean</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#loggingcontext" title="LoggingContext">LoggingContext</a>: <i>
      - <a href="loggingcontextdefinition.md">LoggingContextDefinition</a></i>
    <a href="#keyshape" title="KeyShape">KeyShape</a>: <i>
      - <a href="keyshapedefinition.md">KeyShapeDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AssociatedData

Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associated data must be fewer than 4096 characters.

_Required_: No

_Type_: List of <a href="associateddatadefinition.md">AssociatedDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CryptoEndpoint

The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations. see Vault Crypto endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludePlaintextKey

If true, the generated key is also returned unencrypted.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The OCID of the master encryption key to encrypt the generated data encryption key with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingContext

Information that provides context for audit logging. You can provide this additional data by formatting it as key-value pairs to include in audit logs when audit logging is enabled.

_Required_: No

_Type_: List of <a href="loggingcontextdefinition.md">LoggingContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyShape

_Required_: No

_Type_: List of <a href="keyshapedefinition.md">KeyShapeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Ciphertext

Returns the <code>Ciphertext</code> value.

#### Id

Returns the <code>Id</code> value.

#### Plaintext

Returns the <code>Plaintext</code> value.

#### PlaintextChecksum

Returns the <code>PlaintextChecksum</code> value.

