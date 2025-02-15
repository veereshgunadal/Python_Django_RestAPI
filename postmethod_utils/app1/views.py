from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View

from app1.models import Student
from app1.forms import StudentForm

import json
from app1.utils import is_json

# Create your views here.

class Create(View):
    def post(self, request, *args, **kwargs):
        req = request.body
        if not is_json(req):
            return HttpResponse(json.dumps({'code':'400','message':'request body is not valid json'}), content_type='application/json', status=400)
        
        req_data = json.loads(req)
        
        form = StudentForm(req_data)
        if form.is_valid():
            form.save(commit = True)
            res = {'code':201, 'message':'created'}
            res_body = json.dumps(res)
            return HttpResponse(res_body, content_type = 'application/json', status = 201)

class Create1(View):
    def post(self, request, *args, **kwargs):
        req = request.body
        if not is_json(req):
            return HttpResponse(json.dumps({'code':'400','message':'request body is not valid json'}), content_type='application/json', status=400)
        
        req_data = json.loads(req)
        
        form = StudentForm(req_data)
        if form.is_valid():
            form.save(commit = True)
            res = {'code':201, 'message':'created'}
            res_body = json.dumps(res)
            return HttpResponse(res_body, content_type = 'application/json', status = 201)

        if form.errors:
           error = json.loads(json.dumps(form.errors))
           res = {'code':'400','message':'request field validation failed', 'fieldname':error}
           res_body = json.dumps(res)
           return HttpResponse(res_body, content_type = 'application/json', status = 400)
    
