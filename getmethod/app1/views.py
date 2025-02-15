from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

import json

# Create your views here.

def html_string(request):
    data = "Hi i am string content in html page"
    return HttpResponse(data)

def html_tag(request):
    data = "<h1> Hi i am h1 tag content in html page</h1>"
    return HttpResponse(data)

def http_json(request):
    data = {'name' : 'Virat', 'method':'HttpResponse'}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type = 'application/json')

def json_json(request):
    data = {'name' : 'Rohit', 'method':'JsonResponse'}
    return JsonResponse(data)