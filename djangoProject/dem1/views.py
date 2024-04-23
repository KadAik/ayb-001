from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dem1.utilities.demo_main import retrieve_data
from pathlib import Path
from dem1.utilities.dbconnexion import db_connection
import json

# Queries

query = """
            SELECT *
            FROM {}
            ORDER BY {}
            LIMIT {}
        """
# Config file path
CONFIG_FILE = Path(Path(__file__).resolve().parent, "configurations", "config.ini")

# Initialize db connection
print("Db connection initialization from view module...")
conn = db_connection(CONFIG_FILE)
if conn.is_connected():
    print("Connection successful, threw from module view")
else:
    print("Error while connecting to db, threw from module view")

# Create your views here.

# Template directory to use
TEMPLATE_DIR = Path(Path(__file__).resolve().parent, "templates", "dem1", "html")
print(TEMPLATE_DIR)


@csrf_exempt
def index(request):
    print("View index entry point ...")
    template = Path(TEMPLATE_DIR, "index.html")
    if request.method == "POST":
        print("The request is POST, action ...")
        # request.body is a bytestring, it is decoded to str
        rq = request.body.decode("utf-8")
        # In order to obtain a hash, let's parse the string into JSON
        rq = dict(json.loads(rq))
        print("POST request payload : ")
        print(rq, type(rq))
        # --------------------------------
        # Now the context can be got
        col = rq['headerCol']
        print("Function retrieve_data calling from view index in POST context...")
        res = retrieve_data(conn, 'drug', query, col, 5)
        print("Result from retrieve_data to view index in context POST")
        print(res)
        context = {"query_result": res}
        return JsonResponse(context)
    else:
        print("The request is GET, action ...")
        print("Function retrieve_data calling from view index in GET context...")
        res = retrieve_data(conn, 'drug', query, 'id', 5)
        print("Result from retrieve_data to view index in context GET")
        print(res)
        context = {"query_result": res}
        return render(request, template, context=context)


# Closing the connection
if __name__ == "__main__":
    conn.close()

