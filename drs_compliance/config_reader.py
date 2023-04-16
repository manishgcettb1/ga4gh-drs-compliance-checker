import os
import configparser


def get_drs_url():
    """
    Returns the value of the 'drs_url' property from the 'conf.ini' file.
    Returns:
        str: The DRS URL.
    """
    # Get the path to the 'conf.ini' file
    root_path = os.path.dirname(os.path.abspath(__file__))
    conf_path = os.path.join(root_path, '..', 'conf.ini')

    # Read the 'conf.ini' file
    config = configparser.ConfigParser()
    config.read(conf_path)

    # Get the DRS URL from the 'conf.ini' file
    drs_url = config['DRS']['drs_url']

    return drs_url
