from django import forms

from app1.models import Student

class StudentForm(forms.ModelForm):
    def clean_age(self):
        input_age = self.cleaned_data['age']
        if input_age > 40:
            raise forms.ValidationError('The minimum Age should be less than 40')
        return input_age

    def clean_name(self):
        input_name = self.cleaned_data['name']
        if not input_name.isalpha():
            raise forms.ValidationError('The Name field should accept only alphabets')
        return input_name

    def clean_addr(self):
        input_addr = self.cleaned_data['addr']
        if not input_addr.isalpha():
            raise forms.ValidationError('The Address field should accept only alphabets')
        return input_addr

    def clean_ph_no(self):
        input_ph_no = self.cleaned_data['ph_no']
        if not str(input_ph_no).isdigit():
            raise forms.ValidationError('The Phone no field should accept only alphabets')
        return input_ph_no


    class Meta:
        model = Student
        fields = '__all__'