from django import forms
from employee.models import Employee

# class EmployeeForm(forms.Form):
#     eid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter id"}))
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         exp=cleaned_data.get("experience")
#         if exp<0:
#             msg="invalid exp"
#             self.add_error("experience",msg)

# class EmployeeCreateForm(forms.Form):
#     eid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

        widgets={
            "eid":forms.TextInput(attrs={"class":"form-control"}),
            "employee_name":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "experience":forms.NumberInput(attrs={"class":"form-control"})
        }

#image upload and display

#ModelForm is a class used to create a form equivalent to the model
#here we are styling the form