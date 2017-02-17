from django import forms


class CreateLectureForm(forms.Form):
    name = forms.CharField(max_length=128, label='Name:')
    course = forms.CharField(max_length=128, label='Course:')
    week = forms.CharField(max_length=128, label='Week:')
    url = forms.CharField(max_length=128, label='URL:')


class EditLectureForm(forms.Form):
    name = forms.CharField(max_length=128, label='Name:', required=False)
    course = forms.CharField(max_length=128, label='Course:', required=False)
    week = forms.CharField(max_length=128, label='Week:', required=False)
    url = forms.CharField(max_length=128, label='URL:', required=False)
