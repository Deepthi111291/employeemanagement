# from django.shortcuts import render,redirect
# from django.http import HttpResponse #import class HttpResponse from module http
# from django.views.generic import View  #View is the parentclass of all views
# from employee.forms import EmployeeForm
# from django.contrib import messages
# Create your views here.
#function based views
#class based views
#class based views are better ,we get oops features

#function based view
# def index(request):
#
# def login(request):
#     print("*******************",request.method)
#     return render(request,'login.html')
#
# def registration(request):
#     return render(request,'reg.html')

#class based views
# class IndexView(View):
#     def get(self,request):                       # View is the parent class of all views
#         return render(request,'index.html')
#
# class LoginView(View):                           # if request is get method,return login.html page
#     def get(self,request):                       # View is the parent class of all views
#         return render(request,'login.html')
#     def post(self,request):
#         print(request.POST.get('u_name'))
#         print(request.POST.get('pwd'))
#         return render(request,'login.html')
#
#
#
# class RegistrationView(View):
#     def get(self,request):
#         return render(request,'reg.html')
#
#     def post(self,request):
#         print(request.POST)                #it will give a dictionary
#         print(request.POST.get('f_name'))
#         print(request.POST.get('l_name'))
#         print(request.POST.get('e_mail'))
#         print(request.POST.get('pwd'))
#         print(request.POST.get('u_name'))
#         return render(request,'reg.html')

# class EmployeeCreateView(View):
#     form_class=EmployeeForm            #try to use same variable names like form_class and template_name always
#     template_name="emp-add.html"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("eid"))
#             print(form.cleaned_data.get("employee_name"))
#             print(form.cleaned_data.get("designation"))
#             messages.success(request,"profile has been added")
#             return redirect("emp-add")                 #name=emp-add in the urlsand get method of that view will work
#         else:
#             messages.error(request,"profile adding failed")
#             return render(request,self.template_name,{"form":form})

from django.shortcuts import render,redirect
from employee.models import Employee
from django.contrib import messages
from django.views.generic import View
from employee.forms import EmployeeCreateForm

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):                               #*args(list),**kwargs(dict)
        form=EmployeeCreateForm()
        return render(request,'add-nemp.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST,files=request.FILES)     #files=request.FILES  ->for images
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # Employee.objects.create(
            #     eid=form.cleaned_data.get("eid"),
            #     employee_name=form.cleaned_data.get("employee_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     salary=form.cleaned_data.get("salary"),
            #     email=form.cleaned_data.get("email"),
            #     experience=form.cleaned_data.get("experience")
            # )
            messages.success(request,"employee has been added")
            return redirect('emp-add')                           #emp-add is the name we given in urls
        else:
            messages.error(request,"employee added failed")
            return render(request,'add-nemp.html',{'form':form})
        
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,'emp-list.html',{'employees':qs})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.get(eid=kwargs.get('emp_id'))
        return render(request,'emp-detail.html',{'employee':qs})          #print(kwargs)->{'emp_id':'emp_100'}

class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,'emp-edit.html',{'form':form})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        form = EmployeeCreateForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "employee has been updated")
            return redirect('emp-add')                        # emp-add is the name we given in urls
        else:
            messages.error(request, "employee updating failed")
            return render(request, 'emp-add.html', {'form': form})

def remove_employee(request,*args,**kwargs):
    eid = kwargs.get("e_id")
    employee = Employee.objects.get(eid=eid)
    employee.delete()
    messages.error(request,"employee has been removed")
    return redirect('emp-list')



