from django.http import HttpResponse

from django.shortcuts import render

from dem1.utilities.demo_main import retrieve_data
from pathlib import Path

# Create your views here.

# Template directory to use
TEMPLATE_DIR = Path(Path(__file__).resolve().parent, "templates", "dem1", "html")
print(TEMPLATE_DIR)

def index(request):
    template = Path(TEMPLATE_DIR,"index.html")
    context = {"query_result": retrieve_data()}
    # print("index view debugging : context content")
    # print(context)
    if context["query_result"] == 0:
        return HttpResponse("Error while connecting to the database...")
    else:
        return render(request, template, context=context)
