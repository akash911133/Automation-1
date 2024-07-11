import yaml
import json
import subprocess
import time



YAML_FILE = '.github/config/chart.yaml'
JSON_FILE = '.github/chart.json'

TEMPLATEDATA = { "sources": { "helm": { "kind": "helmchart", "pattern": "*", "spec": { "name": "cluster-autoscaler", "url": "https://kubernetes.github.io/autoscaler", "version": "latest" } } }, "targets": { "update_version": { "name": "Update version in input.tf", "kind": "terraform/file", "spec": { "file": "Template/EKS/input.tf", "path": "variable.cluster-autoscaler.default" } } } }


def load_json(file):
    with open(file, "r") as f:
        data = json.load(f)    
    return data


def load_yml(file):
    with open(file, "r") as f:
        data = yaml.safe_load(f)
    return data

def write_yml(file, data):
    with open(file, 'w+') as ff:
        yaml.dump_all([data], ff)


yml_data = load_yml(YAML_FILE)


json_data = load_json(JSON_FILE)
loaded_data = {}
for json_chart in json_data['charts']:
    for yaml_chart in yml_data['charts']:
        if yaml_chart['chart'] == json_chart['chart']:
            loaded_data[json_chart['chart']] = {'repo': yaml_chart['repository'], 'tf_var_name': json_chart['tf_version_var_name']}

for chart_name, item in loaded_data.items():
    TEMPLATEDATA['sources']['helm']['spec']['name'] = chart_name
    TEMPLATEDATA['sources']['helm']['spec']['url'] = item['repo']
    TEMPLATEDATA['targets']['update_version']['spec']['path'] = f"variable.{item['tf_var_name']}.default"
    filename = "updatecli-generated.yml"
    write_yml(filename, TEMPLATEDATA)
    command = ["updatecli", "apply", "--config", f"{filename}"]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    print(proc)
    time.sleep(3)
