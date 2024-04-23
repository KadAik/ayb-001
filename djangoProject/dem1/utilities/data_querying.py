

def data_query(conn, table_name, query, sort_on, limit=50):
    """
    Query a database and return the query set as a list of rows (objects) consisting in a map :
    JSON style.
    Parameters
    ----------
    table_name: str
    Table to execute query against
    sort_on: str
    Sort the result set on the given column name
    conn: mysql.connector.Connexion
    The database connexion
    query: str
    The query as a string
    limit: int DEFAULT 50
    Limit the result set to a maximum of rows

    Returns
    -------
    list_obj: list
    List of objects in JSON style; each object is a row in the result set
    """
    print("Function data_query entry point ...")
    cursor = conn.cursor()
    query = query.format(*(table_name, sort_on, limit))
    print("Query string outputing from data_query...")
    print(query)
    cursor.execute(query)
    result_set = cursor.fetchall()
    print(f"Debugging point : Query result_set length : {len(result_set)}")
    # The following transform an object in the result set (consisting in a row) into a hash
    # The object is then added to a list
    headers = ["id", "Age", "Sex", "BP", "Cholesterol", "Na_to_K", "Drug"]
    obj_dict = dict()
    list_obj = list()
    for obj in result_set:
        for i in range(len(headers)):
            obj_dict[headers[i]] = obj[i]
        list_obj.append(obj_dict)
        obj_dict = dict()   # flush (reset) the hash
    """
    # Each object is now mapped to its id (primary key) to return a map as a result
    result = dict()
    for j in range(len(result_dict_list)):
        result[result_dict_list[j]["id"]] = result_dict_list[j]
    """
    print("Function data_query exit point ...")
    return list_obj
