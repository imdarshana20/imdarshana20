from django.shortcuts import render
from WebApp import forms

# Create your views here.
def EmpViews(request):
    form=forms.EmpForms()
    return render(request,'welcome.html',{'form':form})