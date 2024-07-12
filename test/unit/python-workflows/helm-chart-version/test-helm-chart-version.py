import pytest
import yaml
import sys

from main import write_yaml, generate_updatecli_yaml

# Define mock data for testing
mock_data = {
    "sources": {
        "helm": {
            "kind": "helmchart",
            "pattern": "*",
            "spec": {
                "name": "mock_chart_name",
                "url": "mock_chart_repo",
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
                "path": "variable.mock_variable_name.default"
            }
        }
    }
}

@pytest.fixture
def mock_file(tmp_path):
    """Fixture to create a temporary file for testing."""
    file_path = tmp_path / "test.yaml"
    return str(file_path)

def test_write_yaml(mock_file):
    """Test write_yaml function."""
    write_yaml(mock_file, mock_data)
    
    # Read written YAML file to check content
    with open(mock_file, 'r') as f:
        written_data = yaml.safe_load(f)
    
    assert written_data == mock_data, "YAML data was not written correctly"

def test_generate_updatecli_yaml():
    """Test generate_updatecli_yaml function."""
    chart_name = "mock_chart_name"
    chart_repo = "mock_chart_repo"
    variable_name = "mock_variable_name"
    
    generated_data = generate_updatecli_yaml(chart_name, chart_repo, variable_name)
    
    assert generated_data == mock_data, "Generated updatecli.yaml data does not match expected mock data"

# If you have other test cases or fixtures, add them here
