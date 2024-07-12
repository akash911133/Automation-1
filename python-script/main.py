import yaml
import sys
import os

def write_yaml(file, data):
    """Write YAML data to a file."""
    try:
        with open(file, 'w+') as ff:
            yaml.dump_all([data], ff)
    except IOError as e:
        print(f"Error writing to {file}: {e}")
        sys.exit(1)

def generate_updatecli_yaml(chart_name, chart_repository, variable_name):
    """Generate updatecli.yaml content based on input parameters."""
    template_data = {
        "sources": {
            "helm": {
                "kind": "helmchart",
                "pattern": "*",
                "spec": {
                    "name": chart_name,
                    "url": chart_repository,
                    "version": "latest"
                }
            }
        },
        "targets": {
            "update_version": {
                "name": "Update version in input.tf",
                "kind": "terraform/file",
                "spec": {
                    "file": "templates/eks/input.tf",
                    "path": f"variable.{variable_name}.default"
                }
            }
        }
    }
    return template_data

def main() -> None:
    CHART_NAME = sys.argv[1]
    CHART_REPOSITORY = sys.argv[2]
    VARIABLE_NAME = sys.argv[3]
    
    # Write YAML data to file
    # Generate updatecli.yaml content
    TEMPLATEDATA = generate_updatecli_yaml(CHART_NAME, CHART_REPOSITORY, VARIABLE_NAME)

    
    # # Set the path for updatecli.yaml in the base repository directory
    DEFAULT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    filename = os.path.join(DEFAULT_PATH, ".github/updatecli.yaml")

    write_yaml(filename, TEMPLATEDATA)
    
    # print(f"Successfully generated {filename}")
    print(f"Chart Name: {CHART_NAME}")
    print(f"Chart Repository: {CHART_REPOSITORY}")
    print(f"Variable Name: {VARIABLE_NAME}")


if __name__ == "__main__":
    main()