import yaml
import sys

def write_yml(file, data):
    with open(file, 'w+') as ff:
        yaml.dump_all([data], ff)
        
        
if __name__ == "__main__":
    CHART_NAME = sys.argv[1]
    CHART_REPOSITORY = sys.argv[2]
    VARIABLE_NAME = sys.argv[3]
    
    TEMPLATEDATA = { "sources": { "helm": { "kind": "helmchart", "pattern": "*", "spec": { "name": "", "url": "", "version": "latest" } } }, "targets": { "update_version": { "name": "Update version in input.tf", "kind": "terraform/file", "spec": { "file": "Template/EKS/input.tf", "path": "variable..default" } } } }
    
    TEMPLATEDATA['sources']['helm']['spec']['name'] = CHART_NAME
    TEMPLATEDATA['sources']['helm']['spec']['url'] = CHART_REPOSITORY
    # TEMPLATEDATA['targets']['update_version']['spec']['path'] = variable.VARIABLE_NAME.default
    
    TEMPLATEDATA['targets']['update_version']['spec']['path'] = f"variable.{VARIABLE_NAME}.default"

    
    filename = ".github/updatecli.yaml"
    write_yml(filename, TEMPLATEDATA)
    print (CHART_NAME)
    print (CHART_REPOSITORY)
    print (VARIABLE_NAME)