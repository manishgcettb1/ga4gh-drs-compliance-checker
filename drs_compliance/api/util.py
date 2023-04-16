import re


def verify_time_format(timestamp, field_name):
    """
    Verify the given timestamp is in ISO format
    :param timestamp: timetamp value
    :param field_name: optional
    :return: boolean
    """
    # Expected ISO 8601 format: YYYY-MM-DDTHH:MM:SS.mmmmmmZ
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'
    return re.match(pattern, timestamp) is not None
