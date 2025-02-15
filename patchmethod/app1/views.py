from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View


from app1.models import Student
from app1.forms import StudentForm
from app1.utils import is_json

import json

# Create your views here.

class Update(View):
    def put(self, request, rollno, *args, **kwargs):
        req = request.body
        if not is_json(req):
            return HttpResponse(json.dumps({'errorcode':400, 'errormessage':'request payload is not valid json'}), content_type='application/json', status = 400)
        
        try:
            data_obj = Student.objects.get(roll_no = rollno)
            original_data = {'name':data_obj.name, 'roll_no':data_obj.roll_no, 'age':data_obj.age,
                             'addr':data_obj.addr, 'ph_no':data_obj.ph_no, 'department':data_obj.department}
            #print(original_data)
            req_data = json.loads(req)
            original_data.update(req_data)
        
            form = StudentForm(original_data, instance=data_obj)
            print(original_data)
            if form.is_valid():
                print('li')
                form.save(commit=True)
                return HttpResponse(json.dumps({'code':200,'message':'resource updated'}), content_type='application/json', status = 200)
            if form.errors:
                return HttpResponse(json.dumps(form.errors))
        except:
            return HttpResponse(json.dumps({'errorcode':404, 'errormessage':'resource not found'}), content_type='application/json', status = 404)

class Update1(View):
    def put(self, request, rollno, *args, **kwargs):
        req = request.body
        
        try:
            req_data = json.loads(req)
            data_obj = Student.objects.get(roll_no = rollno)
            original_data = {'name':data_obj.name, 'roll_no':data_obj.roll_no, 'age':data_obj.age,
                             'addr':data_obj.addr, 'ph_no':data_obj.ph_no, 'department':data_obj.department}
            original_data.update(req_data)
            form = StudentForm(original_data, instance=data_obj)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponse(json.dumps({'code':200, 'message':'resource updated'}), status =200)
            if form.errors:
                return HttpResponse(json.dumps(form.errors), status=400)
        except ValueError:
            return HttpResponse(json.dumps({'code':400, 'message':'payload is not valid json'}), content_type='application/json', status=400)
        except:
            return HttpResponse(json.dumps({'code':404, 'message':'resources not found'}), content_type='application/json', status=404)