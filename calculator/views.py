from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm


# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'calc-home.html')

class AddView(View):
    def get(self,request):
        form = OperationForm()                               #creating the object of form class
        return render(request,'add.html',{'form':form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)+int(n2)
        # print(result)
        form=OperationForm(request.POST)                  #request.POST will have num1,num2 etc
        if form.is_valid():                               #is valid() will call clean ()
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1+n2
            print(form.cleaned_data)
            return render(request,'add.html',{"res":result,"form":form})  #passing the result to html page
        else:
            return render(request,'add.html',{'form':form})


class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'sub.html',{'form':form})
    def post(self,request):
        # n1 = request.POST.get("num1")
        # n2 = request.POST.get("num2")
        # result = int(n1)-int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if not form.is_valid():
            return render(request,'sub.html',{"form":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1-n2
        return render(request,'sub.html',{"subres":result,"form":form})

class MulView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, 'mul.html', {'form': form})
    def post(self,request):
        # n1 = request.POST.get("num1")
        # n2 = request.POST.get("num2")
        # result = int(n1)*int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1*n2
            return render(request, 'mul.html', {"mulres":result,"form": form})
        else:
            return render(request,'mul.html',{'form': form})

class DivView(View):
    def get(self,request):
        form=OperationForm()
        return render(request, 'div.html',{'form': form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)/int(n2)
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = n1 / n2
            return render(request, 'div.html', {"divres": result, 'form': form})
        else:
            return render(request, 'div.html', {"form": form})

class WordCountView(View):
    def get(self,request):
        return render(request, 'wordcount.html')
    def post(self,request):
        word=request.POST.get("word")                               #word="hello hai hello hai"
        words=word.split(" ")                                       #['hello', 'hai', 'hello', 'hai']
        wc={}                                                       #'hello':2,'hai':2
        for w in words:                                             #w="hello","hai","hello","hai"
            if w not in wc:
                wc[w]=1
            else:
                wc[w]+=1
        for k,v in wc.items():
            print(k,v)
        return render(request,'wordcount.html',{'wordres':wc})

class PrimeView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, 'prime.html', {'form': form})
    def post(self,request):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        prime=[]
        for i in range(n1,n2+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                prime.append(i)
        print(prime)
        return render(request,'prime.html',{'result':prime})





