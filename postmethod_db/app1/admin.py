from django.contrib import admin
from app1.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list = ['name','roll_no','age','addr','ph_no','deparment']

admin.site.register(Student,StudentAdmin)