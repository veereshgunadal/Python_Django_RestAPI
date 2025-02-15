from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from app1.models import Student
from app1.admin import StudentAdmin
from app1.forms import StudentForm

import json

# Create your views here.

class CreateSimple(View):
    def post(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        print(type(json_data))
        try:
            data = json.loads(json_data)
        except:
            json_data = json.dumps({'error_code': 400, 'error_message': 'bad request'})
            return HttpResponse(json_data, content_type = 'application/json', status = 400)
        return HttpResponse(json_data, content_type='application/json', status=201)

class Create(View):
    def post(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        #data = json.loads(json_data)
        try:
            data = json.loads(json_data)
        except:
            json_data = json.dumps({'error_code': 400, 'error_message': 'bad request'})
            return HttpResponse(json_data, content_type = 'application/json', status = 400)

        form = StudentForm(data)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'message':'resource create'})
            return HttpResponse(json_data, content_type = 'application/json', status = 201)
        if form.errors:
            print(form.errors)
            json_data = json.dumps({'error_code': 400, 'error_message': 'bad request'})
            return HttpResponse(json.dumps(form.errors),content_type='application/json', status = 400)


class ValidateAndCreate(View):
    def post(self, request, *args, **kwargs):
        req_data = request.body
        try:
            json.loads(req_data)
        except:
            res_data = json.dumps({'error_code':400, 'error_message':'request body is not proper json'})
            return HttpResponse(res_data, content_type ='application/json', status = 400)
        data = json.loads(req_data)
        
        all_data = Student.objects.all()  
        roll_nos = []
        for i in all_data:
            roll_nos.append(i.roll_no)
        if data['roll_no'] in roll_nos:
            res_data = json.dumps({'error_code':400, 'error_message':'roll no is already with other student'})
            return HttpResponse(res_data, content_type ='application/json', status = 400)
        
        form = StudentForm(data)
        if form.is_valid():
            form.save(commit=True)
            stu = Student.objects.get(roll_no = data['roll_no'])
            data_created = {'name':stu.name, 'roll_no':stu.roll_no, 'age':stu.age,
                            'addr':stu.addr, 'ph_no':stu.ph_no, 'department':stu.department}

            res_body = {'code':201, 'message':'resource created'}
            res_body.update(data_created)
            res_data = json.dumps(res_body)
            return HttpResponse(res_data, content_type ='application/json', status = 201)
        if form.errors:
            print(form.errors)
            print(json.dumps(form.errors))
            res = json.loads(json.dumps(form.errors))
            field_name = list(res.keys())[0]
            res_body = {'error_code': 400, 'error': 'bad request','field_name':field_name,'error_message':res[field_name]}
            json_data = json.dumps(res_body)
            return HttpResponse(json_data,content_type='application/json', status = 400)