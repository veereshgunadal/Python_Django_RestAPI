from django import forms
from app1.models import Student

class StudentForm(forms.ModelForm):
    def clean_name(self):
        input_name = self.cleaned_data['name']
        if not input_name.isalpha():
            raise forms.ValidationError(' The Name should accept only alphabet')
        return input_name

    class Meta:
        model = Student
        fields = '__all__'