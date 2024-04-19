from dem1.utilities.dbconnexion import db_connection
from dem1.utilities.data_querying import data_query
# Initialize connection
conf_path = "C:/Users/rodol/Documents/demo/demo/djangoProject/dem1/utilities/config.ini"
def retrieve_data():
    conn = db_connection(conf_path)
    if conn == 0:
        return 0
    else:
        if conn.is_connected():
            query_set = data_query(conn)
            conn.close()
            print("Debugging entry for retrieve_data...")
            print(f"query_set_dict number of keys : {len(query_set.keys())}")
            print(query_set)
            return query_set