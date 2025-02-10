import pytest
import json
import requests
from unittest.mock import patch
from deepcode_api import analyze_code  # Replace with the actual function you're testing

# Sample code to be analyzed
sample_code = """
def greet(name):
    return f"Hello, {name}!"
"""

# Expected API Response Mock
mock_response = {
    "status": "success",
    "data": {
        "analysis_results": [
            {
                "issue": "Potential bug in the code.",
                "line": 3,
                "description": "This is a potential issue that should be reviewed."
            }
        ]
    }
}

# Test the API call functionality
def test_deepcode_api_analysis():
    # Mock the requests.post method to simulate API call
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        # Call the function you're testing (this could be a function like 'analyze_code')
        result = analyze_code(sample_code, "python")

        # Check that the requests.post was called correctly
        mock_post.assert_called_once_with(
            "https://api.deepcode.com/analyze",  # Replace with your actual API URL
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'language': 'python',
                'code': sample_code
            })
        )

        # Assert that the analysis result matches the mock response
        assert result['status'] == 'success'
        assert len(result['data']['analysis_results']) > 0
        assert result['data']['analysis_results'][0]['issue'] == "Potential bug in the code."
        assert result['data']['analysis_results'][0]['description'] == "This is a potential issue that should be reviewed."

# Test the API failure scenario
def test_deepcode_api_failure():
    # Mock the requests.post method to simulate API failure
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 500
        mock_post.return_value.json.return_value = {"status": "error", "message": "Internal Server Error"}

        # Call the function you're testing
        result = analyze_code(sample_code, "python")

        # Check that the API failed gracefully
        assert result['status'] == 'error'
        assert result['message'] == 'Internal Server Error'

# Test for invalid code (empty code string)
def test_deepcode_api_invalid_code():
    # Mock the requests.post method for an invalid code case
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"status": "error", "message": "Code is empty"}

        # Call the function with invalid input (empty code)
        result = analyze_code("", "python")

        # Ensure the API handles empty code gracefully
        assert result['status'] == 'error'
        assert result['message'] == 'Code is empty'

