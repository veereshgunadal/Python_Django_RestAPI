from django.contrib import admin
from app1.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list = ['name', 'age', 'roll_no', 'addr', 'phno', 'department']

admin.site.register(Student,StudentAdmin)