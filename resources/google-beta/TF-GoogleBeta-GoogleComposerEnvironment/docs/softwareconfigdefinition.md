# TF::GoogleBeta::GoogleComposerEnvironment SoftwareConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#airflowconfigoverrides" title="AirflowConfigOverrides">AirflowConfigOverrides</a>" : <i>[ <a href="airflowconfigoverridesdefinition.md">AirflowConfigOverridesDefinition</a>, ... ]</i>,
    "<a href="#envvariables" title="EnvVariables">EnvVariables</a>" : <i>[ <a href="envvariablesdefinition.md">EnvVariablesDefinition</a>, ... ]</i>,
    "<a href="#imageversion" title="ImageVersion">ImageVersion</a>" : <i>String</i>,
    "<a href="#pypipackages" title="PypiPackages">PypiPackages</a>" : <i>[ <a href="pypipackagesdefinition.md">PypiPackagesDefinition</a>, ... ]</i>,
    "<a href="#pythonversion" title="PythonVersion">PythonVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#airflowconfigoverrides" title="AirflowConfigOverrides">AirflowConfigOverrides</a>: <i>
      - <a href="airflowconfigoverridesdefinition.md">AirflowConfigOverridesDefinition</a></i>
<a href="#envvariables" title="EnvVariables">EnvVariables</a>: <i>
      - <a href="envvariablesdefinition.md">EnvVariablesDefinition</a></i>
<a href="#imageversion" title="ImageVersion">ImageVersion</a>: <i>String</i>
<a href="#pypipackages" title="PypiPackages">PypiPackages</a>: <i>
      - <a href="pypipackagesdefinition.md">PypiPackagesDefinition</a></i>
<a href="#pythonversion" title="PythonVersion">PythonVersion</a>: <i>String</i>
</pre>

## Properties

#### AirflowConfigOverrides

_Required_: No

_Type_: List of <a href="airflowconfigoverridesdefinition.md">AirflowConfigOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVariables

_Required_: No

_Type_: List of <a href="envvariablesdefinition.md">EnvVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PypiPackages

_Required_: No

_Type_: List of <a href="pypipackagesdefinition.md">PypiPackagesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PythonVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

