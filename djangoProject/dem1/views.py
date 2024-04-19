from django.http import HttpResponse

from django.shortcuts import render

from dem1.utilities.demo_main import retrieve_data
# Create your views here.

def index(request):
    template = "dem1/html/index.html"
    context = retrieve_data()
    print("index view debugging : context content")
    print(context)
    if context == 0:
        return HttpResponse("Error while connecting to the database...")
    else:
        return render(request, template, context=context)
