charts=$(jq -c '.charts[]' .github/chart.json)

for chart in $charts; do
  chart_name_json=$(echo "$chart" | jq -r '.chart')
  echo "chart_name_json: $chart_name_json"

  # Read chart details from config/chart.yaml
  repository=$(yq eval ".charts[] | select(.chart == \"$chart\") | .repository" .github/config/chart.yaml)
  chart_name_yaml=$(yq eval ".charts[] | select(.chart == \"$chart\") | .chart" .github/config/chart.yaml)
  echo "repository: $repository"
  echo "chart_name_yaml: $chart_name_yaml"

  # Update updatecli.yaml only if names match
  if [[ "$chart_name_json" == "$chart_name_yaml" ]]; then
    echo "Names match. Updating updatecli.yaml..."
    sed -i "s/\"$${variable}\"/\"url: '$repository'\"\;/; s/\"SOURCE\"/\"\'$chart_name_yaml'\"\;/" .github/updatecli.yaml
  else
    echo "Names don't match. Skipping update."
  fi
done

updatecli apply --config .github/updatecli.yaml


# charts=$(jq -c '.charts[]' .github/chart.json)

# for chart in $charts; do

#     chart_name_json=$(echo "$chart" | jq -r '.chart')
#     echo "$chart_name_json"
#     variable=$(echo "$chart" | jq -r '.tf_version_var_name')
#     echo "$variable"

#     # Read chart names from helmchart.yaml
#     charts=$(yq eval '.charts[].chart' .github/config/chart.yaml)


#     for chart in "$charts"; do

#         repository=$(yq eval ".charts[] | select(.chart == \"$chart\") | .repository" .github/config/chart.yaml)
#         echo "$repository"
#         chart_name_yaml=$(yq eval ".charts[] | select(.chart == \"$chart\") | .chart" .github/config/chart.yaml)
#         echo "$chart_name_yaml"
#         if [ "$chart_name_json" == "$chart_name_yaml" ]; then
#             sed -i "s/\"$$variable\"/\"url: '$repository'\"\;/; s/\"SOURCE\"/\"\'$chart_name_yaml'\"\;/" .github/updatecli.yaml
#         fi
#     done
#     # for chart in $charts; do

#     # repository=$(yq eval ".charts[] | select(.chart == \"$chart\") | .repository" .github/config/chart.yaml)
#     # chart_name_yaml=$(yq eval ".charts[] | select(.chart == \"$chart\") | .chart" .github/config/chart.yaml)
    
#     # if [ "$chart_name_json" == "$chart_name_yaml"]; then 
#     #     sed -i '/"'$chart_name_json'"/{n;s/"name: NAME"/"name: '$chart_name_json'"/}' .github/updatecli.yaml
#     #     sed -i '/"'$variable'"/{n;s/"url: URL"/"url: '$repository'"/}' github/updatecli.yaml
#     #     sed -i '/"'$'"/{n;s/".VAR_NAME."/"url: '$variable'"/}' github/updatecli.yaml
#     #     sed -i '/"'$'"/{n;s/"SOURCE"/"'$chart_name_yaml'"/}' github/updatecli.yaml
#     # fi
#     # done
sed -i '/"'akash'"/{n;s/"'NAME'"/"'akash'"/}' updatecli.yaml

sed -i '/"'akash'"/{n;s/"NAME"/"'akash'"/}' updatecli.yaml
sed -i {n;s/"URL"/"https://kubernetes.github.io/autoscaler"/} updatecli.yaml
#     updatecli apply --config .github/updatecli.yaml
# done