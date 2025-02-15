from django.shortcuts import render

from django.http import HttpResponse
from app1.models import Student
import json

from django.core.serializers import serialize

# Create your views here.

def student_by_rollno(request, rollno):
    try:
        stu = Student.objects.get(roll_no =rollno)
        data = {'name' : stu.name, 
            'age' : stu.age,
            'roll_no' : stu.roll_no,
            'address' : stu.addr,
            'ph_no' : stu.phno,
            'department' : stu.department}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

    except Student.DoesNotExist:
        data = {'errorcode':'404', 'errormessage':'resource not found'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json', status=404)

def students(request):
        stus = Student.objects.all()
        print(type(stus))
        list_data = []
        for stu in stus:
            data = {'name' : stu.name, 
            'age' : stu.age,
            'roll_no' : stu.roll_no,
            'address' : stu.addr,
            'ph_no' : stu.phno,
            'department' : stu.department}
            list_data.append(data)
        json_data = json.dumps(list_data)
        return HttpResponse(json_data, content_type='application/json')
 
def students_using_serilize(request, *args):
    stus = Student.objects.all()
    json_data = serialize('json', stus)
    return HttpResponse(json_data, content_type='application/json')

def students_using_serilize_required(request, *args):
    stus = Student.objects.all()
    json_data = serialize('json', stus)
    data = json.loads(json_data)
    print(data)
    list_data = []
    for i in data:
        list_data.append(i['fields'])
    print(list_data)
    json_data = json.dumps(list_data)
    return HttpResponse(json_data, content_type='application/json')
