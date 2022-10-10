from django.shortcuts import render
from django.http import HttpResponse #import class HttpResponse from module http
from django.views.generic import View  #View is the parentclass of all views
# Create your views here.
#function based views
#class based views
#class based views are better ,we get oops features

#function based view
# def index(request):
#     return render(request,"home.html")
#
# def login(request):
#     print("*******************",request.method)
#     return render(request,'login.html')
#
# def registration(request):
#     return render(request,'reg.html')

#class based views
class IndexView(View):
    def get(self,request):                       # View is the parent class of all views
        return render(request,'index.html')

class LoginView(View):                           # if request is get method,return login.html page
    def get(self,request):                       # View is the parent class of all views
        return render(request,'login.html')
    def post(self,request):
        print(request.POST.get('u_name'))
        print(request.POST.get('pwd'))
        return render(request,'login.html')



class RegistrationView(View):
    def get(self,request):
        return render(request,'reg.html')
    def post(self,request):
        print(request.POST)                #it will give a dictionary
        print(request.POST.get('f_name'))
        print(request.POST.get('l_name'))
        print(request.POST.get('e_mail'))
        print(request.POST.get('pwd'))
        print(request.POST.get('u_name'))
        return render(request,'reg.html')



