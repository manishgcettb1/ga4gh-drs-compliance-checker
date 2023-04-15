import os
import sys
import requests
import json

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


# test drs_response from body
def test_drs_object(drs_object_id, drs_field, expected_values, test_name):
    response = requests.get(DRS_URL + "objects/" + drs_object_id)
    response_json = response.json()
    actual_value = response_json[drs_field]
    result = {"object_id": drs_object_id, "test_name": test_name}
    if expected_values == actual_value:
        result["pass"] = True
    else:
        result["pass"] = False
        # Log message from response
        if response.status_code != 200:
            result["message"] = "{}".format(response_json['msg'])
        else:
            result["message"] = "Test failed as value of {} is:{} while expected value is:{}".format(drs_field,
                                                                                                     actual_value,
                                                                                                     expected_values)
    print(result)


def test_drs_object_header(drs_object_id, drs_header_field, expected_values, test_name):
    response = requests.get(DRS_URL + "objects/" + drs_object_id)
    response_json = response.json()
    actual_value = response.headers[drs_header_field]
    result = {"object_id": drs_object_id, "test_name": test_name}
    if expected_values == actual_value:
        result["pass"] = True
    else:
        result["pass"] = False

    if response.status_code != 200:
        result["message"] = "{}".format(response_json['msg'])
    elif response.status_code != 200 and False == result["pass"]:
        result["message"] = "Test failed as value of {} is:{} while expected value is:{}".format(drs_header_field,
                                                                                                 actual_value,
                                                                                                 expected_values)
    print(result)


def test_drs_object_aliases(drs_object_id, expected_values, test_name):
    response = requests.get(DRS_URL + "objects/" + drs_object_id)
    response_json = response.json()
    actual_value = response_json["aliases"]
    result = {"object_id": drs_object_id, "test_name": test_name}
    if expected_values == actual_value[0]:
        result["pass"] = True
    else:
        result["pass"] = False

    if response.status_code != 200:
        result["message"] = "{}".format(response_json['msg'])
    elif response.status_code == 200 and False == result["pass"]:
        result["message"] = "Test failed as value of  alias is:{} while expected value is:{}".format(
            actual_value[0],
            expected_values)
    print(result)


# call below in some method and pass objects in loop
test_drs_object("8e18bfb64168994489bc9e7fda0acd4f", "description",
                "High coverage, downsampled CRAM file for sample HG00449",
                "test_description_for_object_8e18bfb64168994489bc9e7fda0acd4f")

test_drs_object_header("8e18bfb64168994489bc9e7fda0acd4f", "Content-Type",
                       "application/json",
                       "test__header_content_type_for_object_8e18bfb64168994489bc9e7fda0acd4f")

test_drs_object_aliases("8e18bfb64168994489bc9e7fda0acd4f", "HG00449 high coverage downsampled CRAM",
                        "alias_test_for_8e18bfb64168994489bc9e7fda0acd4f")
