import os
import sys
import requests

# Add the root directory of the project to the system path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root_path)

# Import the get_drs_url() function from the config_reader module
from drs_compliance.config_reader import get_drs_url

# Call the get_drs_url() function to get the DRS URL
DRS_URL = get_drs_url()

DRS_OBJECT_IDS = ["8e18bfb64168994489bc9e7fda0acd4f", "ecbb0b5131051c41f1c302287c13495c",
                  "xx18bfb64168994489bc9e7fda0acd4f"]
EXPECTED_RESPONSES = [
    {"status_code": 200, "content_type": "application/json"},
    {"status_code": 200, "content_type": "application/json"},
    {"status_code": 404, "content_type": "application/json"},
]


def test_drs_object():
    for i, object_id in enumerate(DRS_OBJECT_IDS):
        response = requests.get(DRS_URL + "objects/" + object_id)
        expected_status_code = EXPECTED_RESPONSES[i]["status_code"]
        expected_content_type = EXPECTED_RESPONSES[i]["content_type"]
        test_name = "DRS Object Test #" + str(i + 1)
        result = {"object_id": object_id, "test_name": test_name}

        if response.status_code == expected_status_code and response.headers["Content-Type"] == expected_content_type:
            result["pass"] = True
            result["message"] = "Test passed."
        else:
            result["pass"] = False
            result[
                "message"] = "Test failed. Expected status code: {}. Expected content type: {}. Actual status code: {" \
                             "}. Actual content type: {}".format(
                expected_status_code, expected_content_type, response.status_code, response.headers["Content-Type"])

        print(result)


test_drs_object()
