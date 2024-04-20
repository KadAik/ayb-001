from dem1.utilities.dbconnexion import db_connection
from dem1.utilities.data_querying import data_query
from pathlib import Path


# Config file path
CONFIG_FILE = Path(Path(__file__).resolve().parent.parent, "configurations", "config.ini")

# Initialize db connection
conn = db_connection(CONFIG_FILE)

# Queries

query_all = ("SELECT *\n"
             "FROM drug\n"
             "LIMIT 30;\n"
             " ")


def retrieve_data(connection=conn, query=query_all):
    """ Call data_query to retrieve data and return the result."""
    if connection == 0:
        print("Connection failed")
        return 0
    else:
        if connection.is_connected():
            query_set = data_query(connection, query)
            connection.close()
            # print("Debugging entry for retrieve_data...")
            # print(f"query_set_dict number of keys : {len(query_set.keys())}")
            # print(query_set)
            return query_set
