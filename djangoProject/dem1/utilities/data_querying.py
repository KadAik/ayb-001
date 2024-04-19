

def data_query(conn, output_limit=20):
    query = ("SELECT *\n"
             "FROM drug\n"
             "LIMIT 30;\n"
             " ")
    cursor = conn.cursor()
    cursor.execute(query)
    # print("Debugging point for : data_query...")
    result_set = cursor.fetchmany(output_limit)
    # print(f"Query result_set length : {len(result_set)}")
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

    return {"query_result": list_obj}
