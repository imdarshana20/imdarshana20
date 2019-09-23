from django import forms
class EmpForms(forms.Form):
    Name=forms.CharField()
    Salary=forms.IntegerField()