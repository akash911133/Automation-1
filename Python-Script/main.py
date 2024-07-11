import yaml

# Define the data for the YAML file
data = {
  "sources": {
    "cluster_autoscaler_source": {
      "kind": "helmchart",
      "pattern": "*",
      "spec": {
        "name": "ingress-nginx",
        "url": "https://kubernetes.github.io/ingress-nginx",
        "version": "latest"
      }
    }
  },
  "targets": {
    "update_cluster_autoscaler_version": {
      "name": "Update cluster-autoscaler version in input.tf",
      "kind": "terraform/file",
      "spec": {
        "file": "Terraform/EKS/input.tf",
        "path": "variable.NGINX_CHART_VERSION.default"
      }
    }
  }
}

# Open the file for writing in YAML format
with open(".github/updatecli.yaml", "w") as f:
  yaml.dump(data, f, default_flow_style=False)

print("YAML file generated: .github/updatecli.yaml")
