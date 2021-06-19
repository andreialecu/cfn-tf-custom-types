# TF::AWS::SsmPatchBaseline ApprovalRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#approveafterdays" title="ApproveAfterDays">ApproveAfterDays</a>" : <i>Double</i>,
    "<a href="#approveuntildate" title="ApproveUntilDate">ApproveUntilDate</a>" : <i>String</i>,
    "<a href="#compliancelevel" title="ComplianceLevel">ComplianceLevel</a>" : <i>String</i>,
    "<a href="#enablenonsecurity" title="EnableNonSecurity">EnableNonSecurity</a>" : <i>Boolean</i>,
    "<a href="#patchfilter" title="PatchFilter">PatchFilter</a>" : <i>[ <a href="patchfilterdefinition.md">PatchFilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#approveafterdays" title="ApproveAfterDays">ApproveAfterDays</a>: <i>Double</i>
<a href="#approveuntildate" title="ApproveUntilDate">ApproveUntilDate</a>: <i>String</i>
<a href="#compliancelevel" title="ComplianceLevel">ComplianceLevel</a>: <i>String</i>
<a href="#enablenonsecurity" title="EnableNonSecurity">EnableNonSecurity</a>: <i>Boolean</i>
<a href="#patchfilter" title="PatchFilter">PatchFilter</a>: <i>
      - <a href="patchfilterdefinition.md">PatchFilterDefinition</a></i>
</pre>

## Properties

#### ApproveAfterDays

The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100. Conflicts with `approve_until_date`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApproveUntilDate

The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Date is formatted as `YYYY-MM-DD`. Conflicts with `approve_after_days`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceLevel

Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNonSecurity

Boolean enabling the application of non-security updates. The default value is 'false'. Valid for Linux instances only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchFilter

_Required_: No

_Type_: List of <a href="patchfilterdefinition.md">PatchFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

