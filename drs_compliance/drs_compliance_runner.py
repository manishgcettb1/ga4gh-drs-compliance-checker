from drs_compliance.api.drs_object_ep_value_specification import *
from drs_compliance.api.drs_specification import *


def main():
    """
    Execute the specification case wrote in methods of drs_specification.py and print the result
    Execute the specification case for verifying the values for given object_id by calling drs_object_ep_value_specification.py
    :return:
    """
    # Verify status of DRS object"
    verify_drs_object_res_status_code('8e18bfb64168994489bc9e7fda0acd4f', 200, 'verify_status_code')
    verify_drs_object_res_status_code('8e18bfb64168994489bc9e7fda0acd4fdfadf', 404, 'verify_status_code')

    # Verify fields are available in response
    expected_fields = ['id', 'names', 'sizes', 'checksums', 'access_methods', 'created_time', 'updated_time', 'version']
    verify_drs_fields("8e18bfb64168994489bc9e7fda0acd4f", expected_fields, "verify_DRS_fields")

    # Verify ID is returned  in response
    verify_drs_id("8e18bfb64168994489bc9e7fda0acd4f", "verify_object_id")

    # Verify checksums are returned  in response and have valid type
    verify_drs_checksums("8e18bfb64168994489bc9e7fda0acd4f", "verify_checksums")

    # Verify access_methods are returned  in response and have valid type
    verify_drs_access_methods("8e18bfb64168994489bc9e7fda0acd4f", "verify_access_methods")

    # Verify time created_time field are returned  in response and have valid ISO date time
    verify_drs_time_format("8e18bfb64168994489bc9e7fda0acd4f", "created_time", "verify_created_time")

    # Verify time created_time field are returned  in response and have valid ISO date time
    verify_drs_time_format("8e18bfb64168994489bc9e7fda0acd4f", "updated_time", "verify_created_time")

    # Verify value for description for object_id 8e18bfb64168994489bc9e7fda0acd4f
    verify_drs_object("8e18bfb64168994489bc9e7fda0acd4f", "description",
                      "High coverage, downsampled CRAM file for sample HG00449",
                      "test_description_for_object_8e18bfb64168994489bc9e7fda0acd4f")
    # Verify value for alias for object_id 8e18bfb64168994489bc9e7fda0acd4f
    test_drs_object_aliases("8e18bfb64168994489bc9e7fda0acd4f", "HG00449 high coverage downsampled CRAM",
                            "alias_test_for_8e18bfb64168994489bc9e7fda0acd4f")


if __name__ == '__main__':
    main()
