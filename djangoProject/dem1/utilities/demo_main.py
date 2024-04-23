
from dem1.utilities.data_querying import data_query


def retrieve_data(connection, table_name, query, sort_on, limit):
    """ Call data_query to retrieve data and return the result."""
    print("Function retrieve_data entry point ...")
    query_set = -1
    if connection.is_connected():
        print("Connection to db successful, calling data_query ...")
        query_set = data_query(connection, table_name, query, sort_on, limit)
        # connection.close()
        # print("Debugging entry for retrieve_data...")
        # print(f"query_set_dict number of keys : {len(query_set.keys())}")
        # print(query_set)
    else:
        print(" Connection error; threw from function : retrieve_data")
    return query_set
