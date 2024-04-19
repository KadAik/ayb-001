"""
Functions to connect to a database
"""

import configparser
import mysql.connector
from mysql.connector import Error as MyqlError


def db_connection(config_file, section="MySQL"):
    """ Connect to a database and return the connection."""
    config = configparser.ConfigParser()
    conn = None
    config_dict = dict()

    # Reading the configuration file
    try:
        config.read(config_file)
        if not config.has_section(section):
            print("Cannot find MySQL section in the config file")
            return 0
        else:
            for key, value in config[section].items():
                config_dict[key] = value
    except FileNotFoundError:
        print(f"Cannot find file {config_file}")
        return 0

    # Establishing the connexion
    try:
        conn = mysql.connector.connect(**config_dict)
        return conn
    except MyqlError as e:
        print(f"An error occurred when establishing the connection: {e}")
        return 0
