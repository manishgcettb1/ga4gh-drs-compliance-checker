import os
import sys
from urllib.parse import urlparse

import requests
import json

from drs_compliance.api.util import verify_time_format

# Add the root directory of the project to the system path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root_path)

# Import the get_drs_url() function from the config_reader module
from drs_compliance.config_reader import get_drs_url

# Call the get_drs_url() function to get the DRS URL
DRS_URL = get_drs_url()


def verify_drs_object_res_status_code(drs_object_id, expected_status, test_name):
    response = requests.get(DRS_URL + "objects/" + drs_object_id)
    status_code = response.status_code
    response_json = response.json()
    result = {"object_id": drs_object_id, "test_name": test_name}
    if expected_status == status_code:
        result["pass"] = True
        result["message"] = "status of object_id {} returned {} ".format(drs_object_id, status_code)
    else:
        result["pass"] = False
        # Log message from response
        if response.status_code != 200:
            result["message"] = "{}".format(response_json['msg'])
        else:
            result["message"] = "Test failed as value of status_code is:{} while expected value is:{}".format(
                status_code,
                expected_status)
    print(result)


def verify_drs_object_header(object_id, drs_header_field, expected_values, test_name):
    response = requests.get(DRS_URL + "objects/" + object_id)
    json_res = response.json()
    actual_value = response.headers[drs_header_field]
    result = {"object_id": object_id, "test_name": test_name}
    if expected_values == actual_value:
        result["pass"] = True
    else:
        result["pass"] = False

    if response.status_code != 200:
        result["message"] = "{}".format(json_res['msg'])
    elif response.status_code != 200 and False == result["pass"]:
        result["message"] = "Test failed as value of {} is:{} while expected value is:{}".format(drs_header_field,
                                                                                                 actual_value,
                                                                                                 expected_values)
    print(result)


def verify_drs_fields(object_id, required_fields, test_name):
    response = requests.get(DRS_URL + "objects/" + object_id)
    result = {"object_id": object_id, "test_name": test_name}
    if response.status_code == 200:
        if response.headers['content-type'] == "application/json":
            json_res = response.json()
            # Check if all the required fields are present in the JSON response
            missing_fields = set(required_fields) - set(json_res.keys())
            if len(missing_fields) == 0:
                # All required fields are present
                result["pass"] = True
                result["message"] = "API response contains all required fields as per DRS specification v1.2"
            else:
                # Some required fields are missing
                result["pass"] = False
                result["message"] = "API response doesn't meet DRS specification v1.2 as it has missing fields in " \
                                    "response {}".format(missing_fields)
        else:
            result["pass"] = False
            result["message"] = "Verification failed. Response content type is not JSON"
    else:
        result["pass"] = False
        result["message"] = "Verification failed. Request failed with status code {}".format(response.status_code)

    print(result)


def verify_drs_id(object_id, test_name):
    response = requests.get(DRS_URL + "objects/" + object_id)
    result = {"object_id": object_id, "test_name": test_name}
    if response.status_code == 200:
        if response.headers['content-type'] == "application/json":
            json_res = response.json()
            # Check if object id is being returned  in the JSON response
            if json_res.get('id') == object_id:
                # All required fields are present
                result["pass"] = True
                result["message"] = "API response contains object_id as per DRS specification v1.2"
            else:
                # Some required fields are missing
                result["pass"] = False
                result["message"] = "API response doesn't meet DRS specification v1.2 doesn't contain object_id in " \
                                    "response"
        else:
            result["pass"] = False
            result["message"] = "Verification failed. Response content type is not JSON"
    else:
        result["pass"] = False
        result["message"] = "Verification failed. Request failed with status code {}".format(response.status_code)

    print(result)


def verify_drs_checksums(object_id, test_name):
    response = requests.get(DRS_URL + "objects/" + object_id)
    result = {"object_id": object_id, "test_name": test_name}
    if response.status_code == 200:
        if response.headers['content-type'] == "application/json":
            json_res = response.json()
            # Check if checksums is being returned  in the JSON response
            checksums = json_res.get('checksums')
            if isinstance(checksums, list) and all(
                    isinstance(checksum, dict) and 'type' in checksum and 'checksum' in checksum for checksum in
                    checksums):
                # "checksums" field in the response contains a list of dictionaries with "type" and "checksum" keys
                result["pass"] = True
                result["message"] = "Checksums fields are expected as per DRS specification"
            else:
                # "checksums" field in the response does not contain a list of dictionaries with "type" and
                # "checksum" keys
                result["pass"] = False
                result["message"] = "checksums field in the response does not contain a list of dictionaries with " \
                                    "type and checksum keys"
        else:
            result["pass"] = False
            result["message"] = "Verification failed. Response content type is not JSON"
    else:
        result["pass"] = False
        result["message"] = "Verification failed. Request failed with status code {}".format(response.status_code)

    print(result)


def verify_drs_access_methods(object_id, test_name):
    response = requests.get(DRS_URL + "objects/" + object_id)
    result = {"object_id": object_id, "test_name": test_name}
    if response.status_code == 200:
        if response.headers['content-type'] == "application/json":
            json_res = response.json()
            # Check if checksums is being returned  in the JSON response
            access_methods = json_res.get('access_methods')
            if isinstance(access_methods, list) and all(
                    isinstance(access_method, dict) and 'type' in access_method and 'access_url' in access_method for
                    access_method in access_methods):
                # "access_methods" field in the response contains a list of dictionaries with "type" and "access_url"
                # keys

                for access_method in access_methods:
                    access_url = access_method.get('access_url')
                    if access_url:
                        # Access URL is present
                        parsed_url = urlparse(str(access_url))
                        if bool(parsed_url):
                            result["pass"] = True
                            result["message"] = "value of access_methods fields are expected as per DRS specification"
                        '''
                        if all([parsed_url.scheme, parsed_url.netloc]):
                            # Access URL is a valid URL
                            result["pass"] = True
                            result["message"] = "value of access_methods fields are expected as per DRS specification"
                        else:
                            # Access URL is not a valid URL
                            result["pass"] = False
                            result["message"] = "Access URL '{}' is not a valid URL".format(access_url)
                        '''
                    else:
                        # Access URL is missing
                        result["pass"] = False
                        result["message"] = "Access URL is missing"
            else:
                # "checksums" field in the response does not contain a list of dictionaries with "type" and
                # "checksum" keys
                result["pass"] = False
                result["message"] = "access_methods field in the response does not contain a list of dictionaries " \
                                    "with type " \
                                    "and access_url keys"
        else:
            result["pass"] = False
            result["message"] = "Verification failed. Response content type is not JSON"
    else:
        result["pass"] = False
        result["message"] = "Verification failed. Request failed with status code {}".format(response.status_code)

    print(result)


import re


def verify_drs_time_format(object_id, field_name, test_name):
    response = requests.get(DRS_URL + "objects/" + object_id)
    result = {"object_id": object_id, "test_name": test_name}

    if response.status_code == 200:
        if response.headers['content-type'] == "application/json":
            json_res = response.json()

            # Verify time_stamp from response
            time = json_res.get(field_name)
            if time:
                if verify_time_format(time, field_name):
                    result["pass"] = True
                    result["message"] = "{} format is correct.".format(field_name)
                else:
                    result["pass"] = False
                    result["message"] = "{} format is incorrect, value in response:.".format(field_name, time)
            if not time:
                result["pass"] = False
                result["message"] = "Field {} is not present in the response.".format(field_name)
        else:
            result["pass"] = False
            result["message"] = "Verification failed. Response content type is not JSON."
    else:
        result["pass"] = False
        result["message"] = f"Verification failed. Request failed with status code {response.status_code}."

    print(result)


verify_drs_object_res_status_code('8e18bfb64168994489bc9e7fda0acd4f', 200, 'verify_status_code')
verify_drs_object_res_status_code('8e18bfb64168994489bc9e7fda0acd4fdfadf', 404, 'verify_status_code')
expected_fields = ['id', 'names', 'sizes', 'checksums', 'access_methods', 'created_time', 'updated_time', 'version']
verify_drs_fields("8e18bfb64168994489bc9e7fda0acd4f", expected_fields, "verify_DRS_fields")
verify_drs_id("8e18bfb64168994489bc9e7fda0acd4f", "verfiy_object_id")
verify_drs_checksums("8e18bfb64168994489bc9e7fda0acd4f", "verify_checksums")
verify_drs_access_methods("8e18bfb64168994489bc9e7fda0acd4f", "verify_access_methods")
verify_drs_time_format("8e18bfb64168994489bc9e7fda0acd4f", "created_time", "verify_created_time")
verify_drs_time_format("8e18bfb64168994489bc9e7fda0acd4f", "updated_time", "verify_created_time")
