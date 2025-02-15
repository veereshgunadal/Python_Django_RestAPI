from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View

from app1.models import Student
from app1.forms import StudentForm
import json

# Create your views here.

class Delete(View):
    def delete(self, request, rollno, *args, **kwargs):
         try:
             data_obj = Student.objects.get(roll_no = rollno)
             print(data_obj)
             status, data = data_obj.delete()
             if status == 1:
                 print(data)
                 return HttpResponse(json.dumps({'code':204,'message':'resoruce delete'}), content_type='application/json', status = 204)
             else:
                 return HttpResponse(json.dumps({'code':400,'message':'unable to delete'}), content_type='application/json', status = 400)
         except ValueError:
             return HttpResponse(json.dumps({'code':400, 'message':'payload is not valid json'}), content_type='application/json', status = 400)
         except Exception as e:
             print(e)
             return HttpResponse(json.dumps({'code':404, 'message':'resource not found'}), content_type='application/json', status = 404)