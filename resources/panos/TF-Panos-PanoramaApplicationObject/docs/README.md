# TF::Panos::PanoramaApplicationObject

This resource allows you to add/update/delete Panorama application objects.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaApplicationObject",
    "Properties" : {
        "<a href="#abletofiletransfer" title="AbleToFileTransfer">AbleToFileTransfer</a>" : <i>Boolean</i>,
        "<a href="#algdisablecapability" title="AlgDisableCapability">AlgDisableCapability</a>" : <i>String</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#continuescanningforotherapplications" title="ContinueScanningForOtherApplications">ContinueScanningForOtherApplications</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#evasivebehavior" title="EvasiveBehavior">EvasiveBehavior</a>" : <i>Boolean</i>,
        "<a href="#excessivebandwidth" title="ExcessiveBandwidth">ExcessiveBandwidth</a>" : <i>Boolean</i>,
        "<a href="#hasknownvulnerability" title="HasKnownVulnerability">HasKnownVulnerability</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noappidcaching" title="NoAppIdCaching">NoAppIdCaching</a>" : <i>Boolean</i>,
        "<a href="#parentapp" title="ParentApp">ParentApp</a>" : <i>String</i>,
        "<a href="#pervasiveuse" title="PervasiveUse">PervasiveUse</a>" : <i>Boolean</i>,
        "<a href="#pronetomisuse" title="ProneToMisuse">ProneToMisuse</a>" : <i>Boolean</i>,
        "<a href="#risk" title="Risk">Risk</a>" : <i>Double</i>,
        "<a href="#subcategory" title="Subcategory">Subcategory</a>" : <i>String</i>,
        "<a href="#technology" title="Technology">Technology</a>" : <i>String</i>,
        "<a href="#tunnelsotherapplications" title="TunnelsOtherApplications">TunnelsOtherApplications</a>" : <i>Boolean</i>,
        "<a href="#usedbymalware" title="UsedByMalware">UsedByMalware</a>" : <i>Boolean</i>,
        "<a href="#defaults" title="Defaults">Defaults</a>" : <i>[ <a href="defaultsdefinition.md">DefaultsDefinition</a>, ... ]</i>,
        "<a href="#scanning" title="Scanning">Scanning</a>" : <i>[ <a href="scanningdefinition.md">ScanningDefinition</a>, ... ]</i>,
        "<a href="#timeoutsettings" title="TimeoutSettings">TimeoutSettings</a>" : <i>[ <a href="timeoutsettingsdefinition.md">TimeoutSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaApplicationObject
Properties:
    <a href="#abletofiletransfer" title="AbleToFileTransfer">AbleToFileTransfer</a>: <i>Boolean</i>
    <a href="#algdisablecapability" title="AlgDisableCapability">AlgDisableCapability</a>: <i>String</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#continuescanningforotherapplications" title="ContinueScanningForOtherApplications">ContinueScanningForOtherApplications</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#evasivebehavior" title="EvasiveBehavior">EvasiveBehavior</a>: <i>Boolean</i>
    <a href="#excessivebandwidth" title="ExcessiveBandwidth">ExcessiveBandwidth</a>: <i>Boolean</i>
    <a href="#hasknownvulnerability" title="HasKnownVulnerability">HasKnownVulnerability</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noappidcaching" title="NoAppIdCaching">NoAppIdCaching</a>: <i>Boolean</i>
    <a href="#parentapp" title="ParentApp">ParentApp</a>: <i>String</i>
    <a href="#pervasiveuse" title="PervasiveUse">PervasiveUse</a>: <i>Boolean</i>
    <a href="#pronetomisuse" title="ProneToMisuse">ProneToMisuse</a>: <i>Boolean</i>
    <a href="#risk" title="Risk">Risk</a>: <i>Double</i>
    <a href="#subcategory" title="Subcategory">Subcategory</a>: <i>String</i>
    <a href="#technology" title="Technology">Technology</a>: <i>String</i>
    <a href="#tunnelsotherapplications" title="TunnelsOtherApplications">TunnelsOtherApplications</a>: <i>Boolean</i>
    <a href="#usedbymalware" title="UsedByMalware">UsedByMalware</a>: <i>Boolean</i>
    <a href="#defaults" title="Defaults">Defaults</a>: <i>
      - <a href="defaultsdefinition.md">DefaultsDefinition</a></i>
    <a href="#scanning" title="Scanning">Scanning</a>: <i>
      - <a href="scanningdefinition.md">ScanningDefinition</a></i>
    <a href="#timeoutsettings" title="TimeoutSettings">TimeoutSettings</a>: <i>
      - <a href="timeoutsettingsdefinition.md">TimeoutSettingsDefinition</a></i>
</pre>

## Properties

#### AbleToFileTransfer

Able to file transfer.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlgDisableCapability

The alg disable capability.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

The category.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinueScanningForOtherApplications

Continue scanning for
other applications.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The object's description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvasiveBehavior

App is evasive.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcessiveBandwidth

Excessive bandwidth use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasKnownVulnerability

Has known vulnerabilities.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The object's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAppIdCaching

No appid caching.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentApp

The parent application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PervasiveUse

App is pervasive.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProneToMisuse

Prone to misuse.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Risk

The risk (default: 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subcategory

The subcategory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Technology

The technology.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelsOtherApplications

This application tunnels other apps.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsedByMalware

App is used by malware.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Defaults

_Required_: No

_Type_: List of <a href="defaultsdefinition.md">DefaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scanning

_Required_: No

_Type_: List of <a href="scanningdefinition.md">ScanningDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSettings

_Required_: No

_Type_: List of <a href="timeoutsettingsdefinition.md">TimeoutSettingsDefinition</a>

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

