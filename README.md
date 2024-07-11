# Automation-1
Scenario Based Update-


Paths :
1) chart.json   = 
2) chart.yaml   = .github/configs/chart,son
3) input.tf     = Template/EKS/input.tf     
4) main.py      = Pthon-Script/main.py
5) scrpt        = .github/workflows/my_script.yaml

-->  write a github action that will install pip, jq, yq, updatecli and dependencies.
-->  write a python script that will create updatecli.yaml of manifest file of updatecli, that will
and this updatecli will perform the following action -->
  -->  this will read my chart.json file's "tf_version_var_name" variable and chart.
  --> in chart.yaml file there is also chart variable that is same as chart.json variable, based on chart
  here is a repository variable, so it should read repository variable.
  -->  updatecli has helmchart built in functionality that automatically fetch latest version value based on chart and repository url. 
  -->  I have terraform's input.tf file, in this file has block of variable and defined its default value, variable name same as "tf_version_var_name" that is in chart.json file so this default value should update with latest version value.
  -->  for every perticular value update in one by  one in a loop when  and git for perticular variable it should create a PR for that .


# github action  -> 
write a github action that will install pip, python3, jq, yq, updatecli and dependencies and run in a loop of python script executing  and for every loop it create a PR.

# python script  ->
write a python script that will create updatecli.yaml of manifest file of updatecli.
this updatecli script will 

# chart.yaml ->
I have define multiple blocks of chart and repository in chart.yaml

# chart.json ->
I have defined multiple blocks of chart, repository, version and tf_version_var_name.
it should take only chart and tf_version_var_name from this file chart is checking the same as chart.json value of chart if this is matching take its repository according to chart of chart.yaml file.
and  tf_version_var_name is used for searching the variable name same as input.tf file's variable name.

# input.tf  -> 
 in input.tf file it 